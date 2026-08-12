"""Descarga un curso propio de Coursera: estructura + transcripts (+ video opt-in).

Default = dry-run y solo subtítulos. El video se baja con --videos porque pesa
~10.000x más y no aporta señal extra si el objetivo es resumir/estudiar.

Uso:
    python download_course.py <slug>                    # dry-run, ve qué haría
    python download_course.py <slug> --execute          # baja transcripts
    python download_course.py <slug> --execute --videos --resolution 720p

Salida: downloads/<slug>/<NN-modulo>/<NN-item>.vtt (+ .mp4)
"""

from __future__ import annotations

import argparse
import json
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

# Pausa entre requests. No es paranoia: es no parecer un scraper agresivo.
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


def build_session() -> requests.Session:
    if not SESSION_FILE.exists():
        log("ERROR", "auth", f"falta {SESSION_FILE} — corre capture_session.py")
        raise SystemExit(1)
    cauth = json.loads(SESSION_FILE.read_text(encoding="utf-8"))["cauth"]
    session = requests.Session()
    session.cookies.set("CAUTH", cauth, domain=".coursera.org")
    session.headers.update(HEADERS)
    return session


def get_json(session: requests.Session, path: str) -> dict | None:
    """GET con la distinción crítica: 200+HTML es request mal armado, no 401."""
    time.sleep(POLITE_DELAY_S)
    try:
        response = session.get(BASE + path, timeout=30)
    except requests.RequestException as exc:
        log("ERROR", "http", f"{type(exc).__name__}")
        return None
    if response.status_code != 200:
        log("WARNING", "http", f"HTTP {response.status_code}")
        return None
    try:
        return response.json()
    except ValueError:
        log("WARNING", "http", "200 pero HTML — sesión vencida o params malos")
        return None


def build_plan(payload: dict) -> list[dict]:
    """Aplana el árbol a una lista ordenada de lecciones de video."""
    linked = payload.get("linked") or {}
    modules = linked.get("onDemandCourseMaterialModules.v1") or []
    lessons = {x["id"]: x for x in linked.get("onDemandCourseMaterialLessons.v1") or []}
    items = {x["id"]: x for x in linked.get("onDemandCourseMaterialItems.v2") or []}

    plan: list[dict] = []
    for m_idx, module in enumerate(modules, 1):
        for lesson_id in module.get("lessonIds", []):
            for item_id in lessons.get(lesson_id, {}).get("itemIds", []):
                item = items.get(item_id, {})
                summary = item.get("contentSummary") or {}
                if summary.get("typeName") != "lecture":
                    continue
                plan.append(
                    {
                        "item_id": item_id,
                        "name": item.get("name", "?"),
                        "module_idx": m_idx,
                        "module_name": module.get("name", "?"),
                    }
                )
    return plan


def absolutize(url: str) -> str:
    """Los subtítulos vienen como ruta relativa; requests exige URL absoluta."""
    return url if url.startswith("http") else BASE + url


def pick_video_url(entry: dict | str) -> str | None:
    """Cada resolución es un dict de formatos, no una URL suelta.

    Preferir mp4 sobre webm: ffmpeg/players lo tragan sin recodificar.
    """
    if isinstance(entry, str):
        return entry
    for key in ("mp4VideoUrl", "webMVideoUrl"):
        if entry.get(key):
            return entry[key]
    return next((v for v in entry.values() if isinstance(v, str) and "http" in v), None)


def fetch_media(session: requests.Session, course_id: str, item_id: str) -> dict | None:
    """Devuelve {vtt: {lang: url}, mp4: {res: url}} ya normalizado.

    Ambas familias de URL van firmadas (hmac / CloudFront Signature) con
    expiry — hay que descargar cerca de haberlas pedido, no cachearlas.
    """
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


def save_file(session: requests.Session, url: str, dest: Path) -> bool:
    """Descarga con streaming. Salta si ya existe (resume barato)."""
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


def process(args, session: requests.Session, course_id: str, plan: list[dict]) -> None:
    """Recorre el plan. En dry-run solo reporta lo que haría."""
    root = Path(args.out) / args.slug
    saved = 0
    for idx, entry in enumerate(plan, 1):
        folder = root / safe_name(f"{entry['module_idx']:02d}-{entry['module_name']}")
        stem = safe_name(f"{idx:02d}-{entry['name']}")

        if args.dry_run:
            log("INFO", "plan", f"{folder.name}/{stem}.vtt")
            continue

        media = fetch_media(session, course_id, entry["item_id"])
        if not media:
            log("WARNING", "media", f"sin media para {entry['name']}")
            continue

        for lang, url in media["vtt"].items():
            if save_file(session, url, folder / f"{stem}.{lang}.vtt"):
                saved += 1

        if args.videos:
            mp4 = media["mp4"]
            url = mp4.get(args.resolution) or next(iter(mp4.values()), None)
            if url:
                save_file(session, url, folder / f"{stem}.mp4")

    if args.dry_run:
        log("INFO", "dry-run", f"{len(plan)} lecciones. Repetir con --execute.")
    else:
        log("INFO", "done", f"{saved} transcripts en {root}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Descarga un curso propio de Coursera")
    parser.add_argument("slug", help="slug del curso (lo que va tras /learn/)")
    parser.add_argument("--execute", dest="dry_run", action="store_false", default=True)
    parser.add_argument("--videos", action="store_true", help="también bajar mp4")
    parser.add_argument("--resolution", default="720p")
    parser.add_argument("--out", default="downloads")
    args = parser.parse_args()

    session = build_session()
    payload = get_json(session, ENDPOINTS["materials"].format(slug=args.slug))
    if not payload:
        return 1

    course_id = (payload.get("elements") or [{}])[0].get("id", "")
    plan = build_plan(payload)
    if not plan:
        log("ERROR", "plan", "sin lecciones de video")
        return 1

    mode = "DRY-RUN" if args.dry_run else "EJECUTANDO"
    log("INFO", "start", f"{mode} — {args.slug} ({len(plan)} lecciones)")
    process(args, session, course_id, plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
