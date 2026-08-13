# coursera_reverse

Extracción y modelado de conocimiento de tus propios cursos de Coursera vía su API interna: temario, transcripciones y grafos de conocimiento estructurados.

---

## 🎯 Objetivo y Alcance

Este repositorio contiene las **herramientas genéricas de extracción y curación de transcripciones** (Tipo B con sesión `CAUTH`).

> [!NOTE]
> **Aislamiento de Casos de Estudio (`cases/`)**:
> Los cursos extraídos se generan modularmente dentro de `cases/<slug>/` como cartuchos de conocimiento independientes.
> 
> * **Caso de Referencia Incluido**: `cases/duke_ml_foundations/` (Machine Learning Foundations for Product Managers - Duke University).
> * **Otros Cursos y Contenido Privado**: Los cursos de producción o casos de negocio adicionales deben almacenarse en repositorios privados independientes.

---

## 🚀 Quickstart

1. **Instalación de dependencias**:
```bash
pip install requests playwright
python -m playwright install chromium
```

2. **Captura de sesión y extracción**:
```bash
python capture_session.py             # Login manual para capturar cookie CAUTH
python list_courses.py                # Ver cursos con enrollment activo
python download_course.py <slug>      # Dry-run: muestra el plan de descarga
python download_course.py <slug> --execute  # Descarga las transcripciones .vtt
```

3. **Generación del Grafo y Bóveda Modular**:
```bash
python process_course.py <slug>       # Estructura el caso dentro de cases/<slug>/
```

---

## 📁 Estructura del Repositorio

| Archivo / Directorio | Rol |
| :--- | :--- |
| `capture_session.py` | Captura interactiva de la cookie `CAUTH`. |
| `list_courses.py` | Consulta tus cursos activos vía `memberships.v1`. |
| `fetch_course.py` | Obtiene el árbol y metadatos de lecciones del curso. |
| `download_course.py` | Descarga transcripts `.vtt` (y video opt-in). |
| `process_course.py` | Pipeline genérico para procesar y modelar cualquier curso. |
| `probe_endpoints.py` | Diagnóstico de endpoints de Coursera. |
| `endpoints.json` | Mapeo de URLs de la API de Coursera. |
| `cases/duke_ml_foundations/` | **Caso de Referencia Único**: Grafo KST y Bóveda Markdown de Duke. |

---

## 🔒 Privacidad y Buenas Prácticas

- Los tokens de sesión y descargas temporales masivas (`downloads/`) están protegidos en `.gitignore`.
- El material privado o corporativo debe mantenerse en repositorios privados desacoplados.
