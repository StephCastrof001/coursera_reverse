"""Recon de endpoints internos de Coursera (2026).

Mapea qué rutas de la API interna siguen vivas, usando la cookie CAUTH de una
sesión propia ya autenticada. NO descarga contenido: solo registra qué
endpoints responden y con qué forma, para saber sobre cuáles construir.

Contexto: coursera-dl murió porque Coursera deprecó `onDemandCourseMaterials.v1`
y nadie actualizó la ruta. Este script existe para no repetir ese error a ciegas.

Uso:
    set COURSERA_CAUTH=<valor de la cookie>
    python probe_endpoints.py <course-slug>

Salida: tabla en consola + RESEARCH.md con los endpoints vivos.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://www.coursera.org"
TIMEOUT = 20

# Endpoints que solo necesitan el slug del curso.
SLUG_ENDPOINTS: dict[str, str] = {
    "auth_smoke": "/api/externalBasicProfiles.v1?q=me",
    "enrollments": "/api/users/v1/me/enrollments",
    "courses_v1": "/api/onDemandCourses.v1/?q=slug&slug={slug}",
    "materials_v1_LEGACY": "/api/onDemandCourseMaterials.v1/?q=slug&slug={slug}",
    "materials_v2": (
        "/api/onDemandCourseMaterials.v2/?q=slug&slug={slug}"
        "&includes=modules,lessons,items"
    ),
}

# Endpoints que necesitan el courseId resuelto desde el slug.
COURSE_ID_ENDPOINTS: dict[str, str] = {
    "material_items_v2": (
        "/api/onDemandCourseMaterialItems.v2/?q=lesson&courseId={course_id}"
    ),
    "lecture_videos_v1": "/api/onDemandLectureVideos.v1/{course_id}~{item_id}",
    "lecture_assets_v1": "/api/onDemandLectureAssets.v1/{course_id}~{item_id}",
    "supplements_v1": "/api/onDemandSupplements.v1/{course_id}~{item_id}",
    "reference_items": "/api/onDemandReferences.v1/?q=courseId&courseId={course_id}",
}


@dataclass
class ProbeResult:
    """Resultado de golpear un endpoint candidato."""

    name: str
    url: str
    status: int | str
    alive: bool
    top_keys: list[str] = field(default_factory=list)
    note: str = ""


def build_session(cauth: str) -> requests.Session:
    """Sesión con la cookie CAUTH y los headers que Coursera espera.

    El Referer importa: varias rutas internas devuelven 403 sin él aunque la
    cookie sea válida (mismo patrón visto en otros WAF).
    """
    session = requests.Session()
    session.cookies.set("CAUTH", cauth, domain=".coursera.org")
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "Referer": f"{BASE}/",
            "X-Requested-With": "XMLHttpRequest",
        }
    )
    return session


def probe(session: requests.Session, name: str, path: str) -> ProbeResult:
    """Golpea un endpoint y resume la respuesta sin volcar el payload entero."""
    url = BASE + path
    try:
        response = session.get(url, timeout=TIMEOUT)
    except requests.RequestException as exc:
        return ProbeResult(name, url, "ERR", False, note=type(exc).__name__)

    alive = response.status_code == 200
    top_keys: list[str] = []
    note = ""

    if alive:
        try:
            payload = response.json()
            top_keys = list(payload)[:6] if isinstance(payload, dict) else ["<list>"]
        except ValueError:
            alive = False
            note = "200 pero no es JSON (probable redirect a login)"

    return ProbeResult(name, url, response.status_code, alive, top_keys, note)


def resolve_course_id(session: requests.Session, slug: str) -> str | None:
    """Traduce el slug del curso a su courseId interno.

    Sin esto, la mitad de los endpoints no se pueden ni probar.
    """
    path = f"/api/onDemandCourses.v1/?q=slug&slug={slug}"
    try:
        response = session.get(BASE + path, timeout=TIMEOUT)
        elements = response.json().get("elements", [])
    except (requests.RequestException, ValueError, AttributeError):
        return None
    return elements[0].get("id") if elements else None


def run_probes(session: requests.Session, slug: str) -> list[ProbeResult]:
    """Corre las dos fases: rutas por slug, después rutas que piden courseId."""
    results = [probe(session, n, p.format(slug=slug)) for n, p in SLUG_ENDPOINTS.items()]

    course_id = resolve_course_id(session, slug)
    if not course_id:
        results.append(
            ProbeResult("course_id", "-", "SKIP", False, note="no se pudo resolver")
        )
        return results

    print(f"courseId resuelto: {course_id}\n")
    for name, path in COURSE_ID_ENDPOINTS.items():
        if "{item_id}" in path:
            results.append(
                ProbeResult(name, path, "SKIP", False, note="necesita un itemId real")
            )
            continue
        results.append(probe(session, name, path.format(course_id=course_id)))
    return results


def write_research(slug: str, results: list[ProbeResult]) -> Path:
    """Deja el hallazgo en RESEARCH.md para no re-descubrirlo en 3 meses."""
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# RESEARCH — endpoints internos Coursera",
        "",
        f"- Fecha del sondeo: {stamp}",
        f"- Curso de prueba: `{slug}`",
        "- Auth: cookie `CAUTH` de sesión propia",
        "",
        "| Endpoint | Status | Vivo | Claves top-level | Nota |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        mark = "SI" if r.alive else "NO"
        keys = ", ".join(r.top_keys) or "-"
        lines.append(f"| `{r.name}` | {r.status} | {mark} | {keys} | {r.note or '-'} |")

    lines += ["", "## Siguiente paso", "", "Construir el descargador SOLO sobre los",
              "endpoints marcados vivos. Guardar sus rutas en `endpoints.json`",
              "para que un cambio de Coursera sea un fix de datos, no de código.", ""]

    path = Path(__file__).parent / "RESEARCH.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    cauth = os.environ.get("COURSERA_CAUTH", "").strip()
    if not cauth:
        print("ERROR: falta COURSERA_CAUTH. Ver .env.example.", file=sys.stderr)
        return 1
    if len(sys.argv) < 2:
        print("Uso: python probe_endpoints.py <course-slug>", file=sys.stderr)
        return 1

    slug = sys.argv[1]
    print(f"CAUTH cargada (len={len(cauth)}, ...{cauth[-4:]})")
    print(f"Sondeando curso: {slug}\n")

    results = run_probes(build_session(cauth), slug)

    for r in results:
        mark = "OK  " if r.alive else "FAIL"
        print(f"[{mark}] {r.name:24} {str(r.status):5} {r.note}")

    alive = sum(1 for r in results if r.alive)
    print(f"\n{alive}/{len(results)} endpoints vivos")
    print(f"Escrito: {write_research(slug, results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
