# coursera_reverse

Extracción de tus propios cursos de Coursera vía su API interna: temario,
transcripts y video. Recon documentado, no adivinado.

**Tipo B** (login por formulario + cookie de sesión) según el framework de
`klipso_reverse`.

---

## Por qué existe

Los downloaders públicos de Coursera están muertos. `coursera-dl` lo dice en
su propio README. La causa no es anti-bot: Coursera deprecó
`onDemandCourseMaterials.v1` y nadie actualizó la constante.

Este repo sondea qué rutas siguen vivas **antes** de construir encima, y
guarda las rutas en datos (`endpoints.json`) para que la próxima deprecación
sea un fix de una línea.

Estado verificado el **2026-08-12** contra un curso real:
26 transcripts `.vtt`, 4 módulos, 0 archivos vacíos.

---

## Quickstart

```bash
pip install requests playwright
python -m playwright install chromium

python capture_session.py          # abre Chromium, logueate a mano
python list_courses.py             # ver tus cursos y sus slugs
python download_course.py <slug>            # dry-run: qué haría
python download_course.py <slug> --execute  # baja transcripts
```

Video (opt-in, pesado):

```bash
python download_course.py <slug> --execute --videos --resolution 720p
```

Diagnóstico cuando algo se rompe:

```bash
python probe_endpoints.py <slug>   # tabla vivo/muerto de endpoints
```

---

## Estructura

| Archivo | Rol |
|---|---|
| `capture_session.py` | Browser handoff: login manual → cookie `CAUTH` verificada |
| `list_courses.py` | Tus cursos vía `memberships.v1` |
| `fetch_course.py` | Árbol del curso + sondeo de media de una lección |
| `download_course.py` | Descarga. Dry-run por defecto |
| `probe_endpoints.py` | Diagnóstico: qué rutas siguen vivas |
| `endpoints.json` | Rutas verificadas — el fix va acá, no en el código |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Cómo funciona y por qué así |
| [`RESEARCH.md`](RESEARCH.md) | Recon crudo: endpoints, 8 gotchas numerados |

---

## Diseño en una línea

**Transcripts-first.** Un curso pesa GB en mp4 y ~130 KB en `.vtt`. Para
resumir o montar un RAG, el video no aporta señal extra. El default baja
texto; el video es opt-in.

---

## Alcance

Para **cursos propios con enrollment activo**, uso personal.

No evade DRM —no hay: Coursera ya ofrece descarga oficial por lección, esto
automatiza hacerlo 18 veces. No evade paywall: sin enrollment la API no
devuelve material. Incluye pausa entre requests. El material descargado no se
redistribuye y el `.gitignore` bloquea `downloads/`, `*.vtt` y `*.mp4` para
que no se filtre en un commit distraído.
