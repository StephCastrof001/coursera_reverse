# coursera_reverse

Extracción, desbloqueo y modelado de conocimiento de tus propios cursos de Coursera vía su API interna: temario, transcripciones, lecturas y grafos de conocimiento estructurados.

---

## 🎯 Objetivo y Alcance

Este repositorio contiene las **herramientas de extracción, desbloqueo universal de módulos y curación de transcripciones** (Tipo B con sesión `CAUTH`).

> [!NOTE]
> **Aislamiento de Casos de Estudio (`cases/`)**:
> Los cursos extraídos se generan modularmente dentro de `cases/<slug>/` como cartuchos de conocimiento independientes.
> 
> * **Caso de Referencia Incluido**: `cases/duke_ml_foundations/` (Machine Learning Foundations for Product Managers - Duke University).
> * **Otros Cursos y Contenido Privado**: Los cursos de producción o casos de negocio adicionales deben almacenarse en repositorios privados independientes.

---

## 🔓 Metodología de Desbloqueo Universal de Cursos

Coursera suele censurar los módulos 2, 3 y 4 en cursos en modo *preview/auditoría* o con semanas bloqueadas:
1. **El Problema:** La API agregadora `onDemandCourseMaterials.v2` oculta el campo `typeName` de los items no inscritos, provocando que los scrapers tradicionales se salten el 75% del temario.
2. **La Solución:** `download_course.py` utiliza una arquitectura de **sondeo polimórfico a microservicios atómicos** (`onDemandLectureVideos.v1` y `onDemandSupplements.v1`), extrayendo directamente los enlaces firmados de AWS CloudFront para cada ID de lección, desbloqueando el 100% de los módulos.

Para conocer todos los detalles técnicos, consulta [`ARCHITECTURE.md`](ARCHITECTURE.md).

---

## 🚀 Quickstart

1. **Instalación de dependencias**:
```bash
pip install requests playwright
python -m playwright install chromium
```

2. **Captura de sesión y extracción**:
```bash
python capture_session.py                     # Login manual para capturar cookie CAUTH
python list_courses.py                        # Ver cursos con enrollment activo
python download_course.py <slug>              # Dry-run: muestra el plan de descarga
python download_course.py <slug> --execute    # Descarga desbloqueada de transcripts .vtt y lecturas .reading.md
python download_course.py <slug> --execute --videos --resolution 720p  # Descarga opcional de videos MP4
```

3. **Generación del Grafo y Bóveda Modular**:
```bash
python process_course.py <slug>               # Estructura el caso dentro de cases/<slug>/
```

---

## 📁 Estructura del Repositorio

| Archivo / Directorio | Rol |
| :--- | :--- |
| `capture_session.py` | Captura interactiva de la cookie `CAUTH`. |
| `list_courses.py` | Consulta tus cursos activos vía `memberships.v1`. |
| `fetch_course.py` | Obtiene el árbol y metadatos de lecciones del curso. |
| `download_course.py` | Descargador y extractor desbloqueado de transcripts `.vtt`, lecturas y videos. |
| `process_course.py` | Pipeline genérico para procesar y modelar cualquier curso. |
| `probe_endpoints.py` | Diagnóstico de endpoints de Coursera. |
| `endpoints.json` | Mapeo de URLs de la API de Coursera. |
| `ARCHITECTURE.md` | Explicación detallada de la arquitectura y método de desbloqueo. |
| `cases/duke_ml_foundations/` | **Caso de Referencia Único**: Grafo KST y Bóveda Markdown de Duke. |

---

## 🔒 Privacidad y Buenas Prácticas

- Los tokens de sesión y descargas temporales masivas (`downloads/`) están protegidos en `.gitignore`.
- El material privado o corporativo debe mantenerse en repositorios privados desacoplados.
