"""Lista tus cursos de Coursera usando la sesión ya capturada.

`memberships.v1` reemplaza al viejo `/api/users/v1/me/enrollments` (404 en 2026).
Devuelve el slug de cada curso, que es el input de probe_endpoints.py.

Uso:
    python list_courses.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SESSION_FILE = Path.home() / ".config" / "coursera_recon" / "session.json"
BASE = "https://www.coursera.org"

MEMBERSHIPS = (
    "/api/memberships.v1?q=me"
    "&includes=courseId,course"
    "&fields=courseId,course.v1(name,slug,courseType)"
    "&limit=100"
)

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"{BASE}/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
}


def load_cauth() -> str:
    """Lee el token del store. Nunca lo imprime."""
    if not SESSION_FILE.exists():
        print(f"ERROR: no existe {SESSION_FILE}. Corre capture_session.py.", file=sys.stderr)
        raise SystemExit(1)
    return json.loads(SESSION_FILE.read_text(encoding="utf-8"))["cauth"]


def fetch_courses(cauth: str) -> list[dict]:
    """Trae los cursos desde el bloque `linked` de la respuesta Naptime."""
    session = requests.Session()
    session.cookies.set("CAUTH", cauth, domain=".coursera.org")
    session.headers.update(HEADERS)

    response = session.get(BASE + MEMBERSHIPS, timeout=30)
    if response.status_code != 200:
        print(f"ERROR: HTTP {response.status_code}", file=sys.stderr)
        raise SystemExit(1)

    payload = response.json()
    linked = payload.get("linked", {})
    # La clave de `linked` varía de versión; tomar la que traiga los cursos.
    for key, value in linked.items():
        if key.startswith("courses.v1") and isinstance(value, list):
            return value
    return []


def main() -> int:
    courses = fetch_courses(load_cauth())
    if not courses:
        print("Sin cursos en la respuesta. Revisar la forma de `linked`.")
        return 1

    print(f"{len(courses)} cursos encontrados:\n")
    print(f"{'SLUG':<50} {'TIPO':<14} NOMBRE")
    print("-" * 100)
    for course in courses:
        slug = course.get("slug", "?")
        name = (course.get("name") or "?")[:40]
        ctype = course.get("courseType", "?")
        print(f"{slug:<50} {ctype:<14} {name}")

    print("\nPara sondear uno:")
    print(f"  python probe_endpoints.py {courses[0].get('slug', '<slug>')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
