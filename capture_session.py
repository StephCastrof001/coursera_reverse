"""Captura la cookie de sesión de Coursera vía browser handoff (Tipo B).

Patrón tomado de klipso_reverse/_knowledge/targets/plazavea.md:
abrir browser headed, el usuario se loguea a mano, polear context.cookies()
hasta que aparezca la cookie de auth. NO automatiza el login: escribir
credenciales por script es lo que dispara CAPTCHA (ver el repo
coursera-download-with-selenium, muerto por exactamente eso).

Cierra el loop verificando el token contra un endpoint real antes de
declararlo válido — capturar != funcionar.

Uso:
    python capture_session.py

Salida: ~/.config/coursera_recon/session.json + comando export listo.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

LOGIN_URL = "https://www.coursera.org/?authMode=login"
AUTH_COOKIE = "CAUTH"

# Varios candidatos: gatear contra uno solo da falso negativo si justo ese
# está deprecado (le pasó a coursera-dl con onDemandCourseMaterials.v1).
SMOKE_URLS = {
    "externalBasicProfiles.v1": (
        "https://www.coursera.org/api/externalBasicProfiles.v1?q=me"
    ),
    "adminUserPermissions.v1": (
        "https://www.coursera.org/api/adminUserPermissions.v1?q=my"
    ),
    "enrollments": "https://www.coursera.org/api/users/v1/me/enrollments",
    "memberships.v1": (
        "https://www.coursera.org/api/memberships.v1?q=me&showHidden=true&limit=3"
    ),
}

# Sin esto Coursera negocia contenido y devuelve el HTML de la SPA con 200.
JSON_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.coursera.org/",
}

# Cookies que existen para visitantes anónimos. Confundirlas con auth guarda
# una sesión inútil que da 401 después (misma trampa que vtex_session).
ANON_COOKIES = {"__204u", "csrf3-token", "usertype", "__400v"}

CONFIG_DIR = Path.home() / ".config" / "coursera_recon"
PROFILE_DIR = CONFIG_DIR / "browser_profile"
SESSION_FILE = CONFIG_DIR / "session.json"

POLL_TIMEOUT_S = 300
POLL_INTERVAL_S = 2


def find_auth_cookie(cookies: list[dict]) -> str | None:
    """Devuelve el valor de CAUTH, ignorando cookies de visitante anónimo."""
    for cookie in cookies:
        name = cookie.get("name", "")
        if name in ANON_COOKIES:
            continue
        if name == AUTH_COOKIE and cookie.get("value"):
            return cookie["value"]
    return None


def probe_smoke(page, name: str, url: str) -> tuple[bool, str]:
    """Golpea un candidato con headers de JSON explícitos."""
    try:
        response = page.request.get(url, headers=JSON_HEADERS)
    except Exception as exc:  # noqa: BLE001 - reportar cualquier fallo de red
        return False, f"error de red: {type(exc).__name__}"

    if response.status != 200:
        return False, f"HTTP {response.status}"
    try:
        payload = response.json()
    except ValueError:
        return False, "200 pero HTML (content negotiation o sesión inválida)"

    keys = ", ".join(list(payload)[:4]) if isinstance(payload, dict) else "<list>"
    return True, f"JSON OK — claves: {keys}"


def verify_token(page) -> tuple[bool, dict[str, str]]:
    """Prueba todos los candidatos. Capturar la cookie no prueba que sirva.

    Devuelve (alguno_vivo, detalle_por_endpoint). El detalle es recon
    gratis: dice cuáles rutas siguen vivas en 2026.
    """
    detail: dict[str, str] = {}
    any_alive = False
    for name, url in SMOKE_URLS.items():
        ok, note = probe_smoke(page, name, url)
        detail[name] = ("OK   " if ok else "FAIL ") + note
        any_alive = any_alive or ok
    return any_alive, detail


def save_session(cauth: str, cookies: list[dict], verified: bool) -> Path:
    """Guarda fuera del repo. Es una credencial viva, no un artefacto.

    Guarda aunque no verifique, marcando el estado: descartar un token real
    por un endpoint deprecado obliga a re-loguearse al pedo.
    """
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(
        json.dumps(
            {
                "cauth": cauth,
                "verified": verified,
                "cookies": cookies,
                "captured_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return SESSION_FILE


def poll_for_login(context, page) -> str | None:
    """Espera a que el usuario termine de loguearse a mano."""
    print(f"Esperando login manual (timeout {POLL_TIMEOUT_S}s)...")
    deadline = time.time() + POLL_TIMEOUT_S
    while time.time() < deadline:
        cauth = find_auth_cookie(context.cookies())
        if cauth:
            print(f"\n{AUTH_COOKIE} detectada (len={len(cauth)})")
            return cauth
        time.sleep(POLL_INTERVAL_S)
        print(".", end="", flush=True)
    return None


def main() -> int:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    print("Abriendo Chromium. Logueate en la ventana; no toco tus credenciales.\n")

    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            viewport={"width": 1280, "height": 900},
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(LOGIN_URL, wait_until="domcontentloaded")

        cauth = poll_for_login(context, page)
        if not cauth:
            print("\nTIMEOUT: no apareció CAUTH. ¿Completaste el login?")
            context.close()
            return 1

        ok, detail = verify_token(page)
        cookies = context.cookies()
        context.close()

    print("\nVerificación por endpoint:")
    for name, note in detail.items():
        print(f"  {name:28} {note}")

    path = save_session(cauth, cookies, verified=ok)
    print(f"\nGuardado: {path}  (verified={ok})")
    if not ok:
        print("Ningún endpoint devolvió JSON. Token guardado igual, pero no")
        print("lo uses hasta saber si es la sesión o las rutas lo que falla.")
        return 1
    print("\nPara correr el recon:\n")
    print(f'  $env:COURSERA_CAUTH = "{cauth[:6]}...{cauth[-4:]}"   # <- valor real en el json')
    print("  python probe_endpoints.py <course-slug>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
