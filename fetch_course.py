"""Baja el árbol de un curso y sondea video + transcript de una lección real.

Cierra el hueco que dejó probe_endpoints.py: `onDemandLectureVideos.v1` no se
puede probar sin un itemId, y los itemId viven en `onDemandCourseMaterials.v2`.

Uso:
    python fetch_course.py <course-slug>

Salida: árbol en consola + <slug>_tree.json con la estructura cruda.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SESSION_FILE = Path.home() / ".config" / "coursera_recon" / "session.json"
BASE = "https://www.coursera.org"

MATERIALS = (
    "/api/onDemandCourseMaterials.v2/?q=slug&slug={slug}"
    "&includes=modules,lessons,items"
    "&fields=moduleIds,onDemandCourseMaterialModules.v1(name,slug,lessonIds),"
    "onDemandCourseMaterialLessons.v1(name,slug,itemIds),"
    "onDemandCourseMaterialItems.v2(name,slug,typeName,contentSummary)"
)

VIDEO = (
    "/api/onDemandLectureVideos.v1/{course_id}~{item_id}"
    "?includes=video&fields=onDemandVideos.v1(sources,subtitles,subtitlesVtt)"
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


def build_session() -> requests.Session:
    """Sesión con la cookie ya capturada. Nunca imprime el token."""
    if not SESSION_FILE.exists():
        print(f"ERROR: falta {SESSION_FILE}. Corre capture_session.py.", file=sys.stderr)
        raise SystemExit(1)
    cauth = json.loads(SESSION_FILE.read_text(encoding="utf-8"))["cauth"]
    session = requests.Session()
    session.cookies.set("CAUTH", cauth, domain=".coursera.org")
    session.headers.update(HEADERS)
    return session


def get_json(session: requests.Session, path: str) -> dict | None:
    """GET que distingue 'no autorizado' de 'ruta equivocada'."""
    response = session.get(BASE + path, timeout=30)
    if response.status_code != 200:
        print(f"  HTTP {response.status_code}")
        return None
    try:
        return response.json()
    except ValueError:
        print("  200 pero HTML (ruta o params equivocados)")
        return None


def index_linked(payload: dict) -> dict[str, dict]:
    """Aplana el bloque `linked` de Naptime a {prefijo: {id: objeto}}."""
    index: dict[str, dict] = {}
    for key, rows in (payload.get("linked") or {}).items():
        if not isinstance(rows, list):
            continue
        prefix = key.split(".")[0]
        index[prefix] = {row.get("id"): row for row in rows if isinstance(row, dict)}
    return index


def print_tree(index: dict[str, dict]) -> list[dict]:
    """Imprime módulos → lecciones → items. Devuelve los items de tipo lecture."""
    modules = index.get("onDemandCourseMaterialModules", {})
    lessons = index.get("onDemandCourseMaterialLessons", {})
    items = index.get("onDemandCourseMaterialItems", {})

    lectures: list[dict] = []
    for module in modules.values():
        print(f"\n[MODULO] {module.get('name', '?')}")
        for lesson_id in module.get("lessonIds", []):
            lesson = lessons.get(lesson_id, {})
            print(f"  [LECCION] {lesson.get('name', '?')}")
            for item_id in lesson.get("itemIds", []):
                item = items.get(item_id, {})
                # typeName vive anidado, no en la raiz del item.
                type_name = (item.get("contentSummary") or {}).get("typeName", "?")
                print(f"    - ({type_name}) {item.get('name', '?')}")
                if type_name == "lecture":
                    lectures.append({"id": item_id, "name": item.get("name", "?")})
    return lectures


def probe_video(session: requests.Session, course_id: str, item: dict) -> None:
    """Verifica si de verdad salen mp4 y subtítulos para una lección real."""
    print(f"\n=== Sondeo de video: {item['name']} ===")
    payload = get_json(session, VIDEO.format(course_id=course_id, item_id=item["id"]))
    if not payload:
        return

    videos = (payload.get("linked") or {}).get("onDemandVideos.v1", [])
    if not videos:
        print("  Sin bloque onDemandVideos.v1 — revisar `fields`")
        print(f"  claves devueltas: {list(payload)}")
        return

    video = videos[0]
    sources = video.get("sources") or {}
    resolutions = list((sources.get("byResolution") or {}))
    subtitles = list((video.get("subtitles") or {}))
    subtitles_vtt = list((video.get("subtitlesVtt") or {}))

    print(f"  Resoluciones mp4 : {resolutions or 'ninguna'}")
    print(f"  Subtitulos (srt) : {subtitles or 'ninguno'}")
    print(f"  Subtitulos (vtt) : {subtitles_vtt or 'ninguno'}")


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso: python fetch_course.py <course-slug>", file=sys.stderr)
        return 1
    slug = sys.argv[1]
    session = build_session()

    print(f"Bajando arbol de: {slug}")
    payload = get_json(session, MATERIALS.format(slug=slug))
    if not payload:
        return 1

    course_id = (payload.get("elements") or [{}])[0].get("id", "")
    index = index_linked(payload)
    print(f"courseId: {course_id}")
    print(f"bloques linked: {list(index)}")

    lectures = print_tree(index)
    print(f"\nTotal lecciones de video: {len(lectures)}")

    out = Path(f"{slug}_tree.json")
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Arbol crudo: {out}")

    # Segundo argumento opcional: sondear un itemId puntual (el de la URL
    # /lecture/<itemId>/...) en vez de la primera leccion del arbol.
    if len(sys.argv) > 2 and course_id:
        probe_video(session, course_id, {"id": sys.argv[2], "name": sys.argv[2]})
    elif lectures and course_id:
        probe_video(session, course_id, lectures[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
