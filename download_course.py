"""Descarga un curso propio de Coursera: estructura + transcripts + lecturas/enlaces (+ video opt-in).

Uso:
    python download_course.py <slug>                    # dry-run, ve qué haría
    python download_course.py <slug> --execute          # baja transcripts y lecturas con links
    python download_course.py <slug> --execute --fetch-links  # además raspa el texto de links públicos
    python download_course.py <slug> --execute --videos --resolution 720p

Salida: downloads/<slug>/<NN-modulo>/<NN-item>.vtt (+ .reading.md, .mp4)
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
from pathlib import Path

import requests

SESSION_FILE = Path.home() / ".config" / "coursera_recon" / "session.json"
ENDPOINTS = json.loads((Path(__file__).parent / "endpoints.json").read_text("utf-8"))
BASE = ENDPOINTS["base"]

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"{BASE}/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
}

POLITE_DELAY_S = 0.6
INVALID_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def log(level: str, action: str, message: str) -> None:
    """Log estructurado: [TIMESTAMP] [LEVEL] [MODULE] [ACTION] mensaje."""
    stamp = time.strftime("%Y-%m-%dT%H:%M:%S")
    print(f"[{stamp}] [{level}] [download] [{action}] {message}")


def safe_name(name: str, limit: int = 70) -> str:
    """Nombre de archivo válido en Windows, truncado por el límite de 260 chars."""
    cleaned = INVALID_CHARS.sub("", name).strip().rstrip(".")
    return (cleaned[:limit] or "sin-nombre").strip()


def load_cauth() -> str:
    """Token desde env var o desde el store local."""
    token = os.environ.get("COURSERA_CAUTH")
    if token:
        log("INFO", "auth", "Usando COURSERA_CAUTH desde variable de entorno")
        return token.strip()
    if not SESSION_FILE.exists():
        log("ERROR", "auth", f"Falta {SESSION_FILE}. Corre capture_session.py.")
        sys.exit(1)
    try:
        data = json.loads(SESSION_FILE.read_text("utf-8"))
        token = data.get("cauth", "").strip()
        if not token:
            raise ValueError("archivo vacio")
        log("INFO", "auth", f"Usando sesion guardada en {SESSION_FILE}")
        return token
    except Exception as exc:
        log("ERROR", "auth", f"No se pudo leer {SESSION_FILE}: {exc}")
        sys.exit(1)


def build_session(cauth: str) -> requests.Session:
    session = requests.Session()
    session.cookies.set("CAUTH", cauth, domain=".coursera.org")
    session.headers.update(HEADERS)
    return session


def get_json(session: requests.Session, path: str) -> dict | None:
    url = path if path.startswith("http") else BASE + path
    try:
        response = session.get(url, timeout=30)
        if response.status_code == 401:
            log("ERROR", "http", "401 Unauthorized — la cookie CAUTH expiro")
            return None
        if response.status_code != 200:
            log("WARN", "http", f"{response.status_code} en {path[:60]}")
            return None
        return response.json()
    except Exception as exc:
        log("ERROR", "http", f"{type(exc).__name__} en {path[:60]}")
        return None


def fetch_materials(session: requests.Session, slug: str) -> tuple[str, dict] | tuple[None, None]:
    path = ENDPOINTS["materials"].format(slug=slug)
    payload = get_json(session, path)
    if not payload:
        return None, None
    elements = payload.get("elements") or []
    if not elements:
        log("ERROR", "materials", f"Curso '{slug}' no encontrado")
        return None, None
    return elements[0]["id"], payload


def build_plan(payload: dict) -> list[dict]:
    """Aplana el árbol a una lista ordenada de lecciones (videos y lecturas/suplementos)."""
    linked = payload.get("linked") or {}
    modules = linked.get("onDemandCourseMaterialModules.v1") or []
    lessons = {x["id"]: x for x in linked.get("onDemandCourseMaterialLessons.v1") or []}
    items = {x["id"]: x for x in linked.get("onDemandCourseMaterialItems.v2") or []}

    plan: list[dict] = []
    item_counter = 0
    for m_idx, module in enumerate(modules, 1):
        for lesson_id in module.get("lessonIds", []):
            for item_id in lessons.get(lesson_id, {}).get("itemIds", []):
                item = items.get(item_id, {})
                summary = item.get("contentSummary") or {}
                type_name = summary.get("typeName", "")
                if type_name not in ("lecture", "supplement"):
                    continue
                item_counter += 1
                plan.append(
                    {
                        "item_id": item_id,
                        "item_num": item_counter,
                        "name": item.get("name", "?"),
                        "type": type_name,
                        "module_idx": m_idx,
                        "module_name": module.get("name", "?"),
                    }
                )
    return plan


def absolutize(url: str) -> str:
    return url if url.startswith("http") else BASE + url


def pick_video_url(entry: dict | str) -> str | None:
    if isinstance(entry, str):
        return entry
    for key in ("mp4VideoUrl", "webMVideoUrl"):
        if entry.get(key):
            return entry[key]
    return next((v for v in entry.values() if isinstance(v, str) and "http" in v), None)


def fetch_media(session: requests.Session, course_id: str, item_id: str) -> dict | None:
    path = ENDPOINTS["lecture_video"].format(course_id=course_id, item_id=item_id)
    payload = get_json(session, path)
    if not payload:
        return None
    videos = (payload.get("linked") or {}).get("onDemandVideos.v1") or []
    if not videos:
        return None

    video = videos[0]
    vtt = {
        lang: absolutize(url)
        for lang, url in (video.get("subtitlesVtt") or {}).items()
        if isinstance(url, str)
    }
    by_resolution = (video.get("sources") or {}).get("byResolution") or {}
    mp4 = {}
    for resolution, entry in by_resolution.items():
        url = pick_video_url(entry)
        if url:
            mp4[resolution] = url
    return {"vtt": vtt, "mp4": mp4}


def fetch_supplement(session: requests.Session, course_id: str, item_id: str) -> dict | None:
    """Obtiene el contenido de una lectura / suplemento de Coursera y extrae sus links."""
    path = ENDPOINTS.get("supplement", "/api/onDemandSupplements.v1/{course_id}~{item_id}?includes=asset&fields=content").format(
        course_id=course_id, item_id=item_id
    )
    payload = get_json(session, path)
    if not payload:
        return None
    assets = (payload.get("linked") or {}).get("openCourseAssets.v1") or []
    if not assets:
        return None
    
    definition = assets[0].get("definition") or {}
    raw_cml = definition.get("value", "")
    html_content = (definition.get("renderableHtmlWithMetadata") or {}).get("renderableHtml", "")
    
    # Extraer URLs externas dentro del contenido
    links = re.findall(r'href=["\'](https?://[^"\']+)["\']', raw_cml or html_content)
    
    # Limpiar CML a texto plano
    clean_text = re.sub(r'<[^>]+>', ' ', raw_cml)
    clean_text = html.unescape(clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    return {
        "raw_cml": raw_cml,
        "clean_text": clean_text,
        "links": list(dict.fromkeys(links))
    }


def save_file(session: requests.Session, url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        log("INFO", "skip", dest.name)
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with session.get(url, stream=True, timeout=120) as response:
            response.raise_for_status()
            with dest.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=65536):
                    handle.write(chunk)
    except (requests.RequestException, OSError) as exc:
        log("ERROR", "save", f"{dest.name}: {type(exc).__name__}")
        return False
    log("INFO", "saved", f"{dest.name} ({dest.stat().st_size // 1024} KB)")
    return True


def fetch_external_article_text(url: str) -> str:
    """Descarga de forma segura el texto de un artículo público externo."""
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        if resp.status_code == 200:
            text = re.sub(r'<script[^>]*>.*?</script>', ' ', resp.text, flags=re.DOTALL | re.IGNORECASE)
            text = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL | re.IGNORECASE)
            text = re.sub(r'<[^>]+>', ' ', text)
            text = html.unescape(text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text[:4000] # Primeras 4k chars de extracto
    except Exception:
        pass
    return ""


def process(args, session: requests.Session, course_id: str, plan: list[dict]) -> None:
    root = Path(args.out) / args.slug
    saved = 0
    for entry in plan:
        folder = root / safe_name(f"{entry['module_idx']:02d}-{entry['module_name']}")
        stem = safe_name(f"{entry['item_num']:02d}-{entry['name']}")
        
        # Caso 1: LECTURA / SUPLEMENTO
        if entry["type"] == "supplement":
            if args.dry_run:
                log("INFO", "plan", f"[LECTURA] {folder.name}/{stem}.reading.md")
                continue
            
            supp = fetch_supplement(session, course_id, entry["item_id"])
            if supp:
                reading_file = folder / f"{stem}.reading.md"
                reading_file.parent.mkdir(parents=True, exist_ok=True)
                
                content_md = [
                    f"# 📖 {entry['name']}",
                    f"- **Módulo**: {entry['module_name']}",
                    f"- **Tipo**: Lectura Complementaria Oficial",
                    "",
                    "## 📜 Contenido de la Lectura",
                    supp["clean_text"],
                    "",
                    "## 🔗 Enlaces y Artículos Externos Citados"
                ]
                
                for link in supp["links"]:
                    content_md.append(f"- [{link}]({link})")
                    if getattr(args, "fetch_links", False):
                        article_snippet = fetch_external_article_text(link)
                        if article_snippet:
                            content_md.append(f"  > **Extracto**: {article_snippet[:300]}...")
                
                reading_file.write_text("\n".join(content_md), encoding="utf-8")
                log("INFO", "saved", f"{reading_file.name} ({len(supp['links'])} enlaces)")
                saved += 1
            time.sleep(POLITE_DELAY_S)
            continue

        # Caso 2: LECTURE / VIDEO
        if args.dry_run:
            log("INFO", "plan", f"[VIDEO] {folder.name}/{stem}.vtt")
            continue

        media = fetch_media(session, course_id, entry["item_id"])
        if not media:
            log("WARN", "media", f"Sin media para '{entry['name']}'")
            continue

        for lang, url in media["vtt"].items():
            dest = folder / f"{stem}.{lang}.vtt"
            if save_file(session, url, dest):
                saved += 1

        if args.videos:
            res = args.resolution
            url = media["mp4"].get(res) or next(iter(media["mp4"].values()), None)
            if url:
                dest = folder / f"{stem}.{res}.mp4"
                if save_file(session, url, dest):
                    saved += 1

        time.sleep(POLITE_DELAY_S)

    if not args.dry_run:
        log("INFO", "done", f"{saved} archivos procesados en {root}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug", help="Slug del curso")
    parser.add_argument("--execute", dest="dry_run", action="store_false", default=True, help="Descarga real")
    parser.add_argument("--fetch-links", action="store_true", default=False, help="Descarga también el contenido de enlaces externos citados")
    parser.add_argument("--videos", action="store_true", help="Descargar tambien video")
    parser.add_argument("--resolution", default="720p", choices=["1080p", "720p", "540p", "360p", "240p"])
    parser.add_argument("--out", default="downloads")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cauth = load_cauth()
    session = build_session(cauth)

    log("INFO", "init", f"Consultando curso '{args.slug}'...")
    course_id, materials = fetch_materials(session, args.slug)
    if not course_id or not materials:
        sys.exit(1)

    plan = build_plan(materials)
    mode = "DRY-RUN" if args.dry_run else "EXECUTE"
    log("INFO", "start", f"{mode} — {args.slug} ({len(plan)} lecciones: videos + lecturas)")

    process(args, session, course_id, plan)


if __name__ == "__main__":
    main()
