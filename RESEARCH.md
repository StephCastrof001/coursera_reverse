# RESEARCH — Coursera (Tipo B: cookie de sesión vía browser)

Recon en vivo: 2026-08-12. Curso de prueba: `conquistaaudienciasconiag`.
Verificado contra cuenta propia con enrollment activo.

---

## Portal Map

| Portal | URL Base | Auth | Anti-bot | Contenido |
|---|---|---|---|---|
| Web | www.coursera.org | Cookie `CAUTH` (dominio `.coursera.org`) | CAPTCHA solo en login automatizado | Catálogo, materiales, videos, subtítulos |

Plataforma: **API interna "Naptime"** — todas las respuestas comparten el
envelope `{elements, paging, linked}`.

---

## Auth Flow

Cookie de auth: **`CAUTH`** (~601 chars).

⚠ **No confundir con cookies de visitante anónimo**: `__204u`, `csrf3-token`,
`usertype`, `__400v`. Aparecen sin login y guardan una sesión inútil.

### Método (browser handoff)
1. Playwright abre `coursera.org/?authMode=login` con `headless=False`
2. Usuario se loguea **a mano** — automatizar el tipeo dispara CAPTCHA
   (así murió `coursera-download-with-selenium`)
3. Polear `context.cookies()` hasta encontrar `CAUTH`
4. Verificar contra un endpoint real antes de declararla válida
5. Guardar en `~/.config/coursera_recon/session.json`

Perfil persistente en `~/.config/coursera_recon/browser_profile` → la segunda
captura es instantánea.

### TTL
**Sin medir.** Pendiente: observar cuándo empieza a dar HTML en vez de JSON.

---

## Gotchas numerados

1. **`Accept: application/json` es obligatorio.** Sin él, Coursera negocia
   contenido y devuelve el HTML de la SPA con **status 200**. Un 200 con HTML
   NO significa sesión inválida — significa request mal armado. Un 401/403 sí
   sería sesión inválida. Confundirlos cuesta horas.
2. **`typeName` vive anidado** en `contentSummary.typeName`, no en la raíz del
   item. Pedirlo plano devuelve `None` en silencio.
3. **`pscp` no expande `~`** al copiar a una VM — usar ruta absoluta.
4. Headers que acompañan: `X-Requested-With: XMLHttpRequest`, `Referer`.
5. **`subtitlesVtt` devuelve rutas RELATIVAS** (`/api/subtitleAssetProxy.v1/...`).
   `requests` las rechaza con `MissingSchema`. Hay que anteponer el host.
6. **`sources.byResolution["1080p"]` es un dict, no una URL.** Contiene
   `mp4VideoUrl` / `webMVideoUrl`. Tratarlo como string revienta con
   `TypeError: unhashable type: 'slice'`.
7. **Las URLs de media van FIRMADAS y expiran.** Subtítulos con
   `?expiry=<ms>&hmac=<...>`; video con CloudFront `?Expires=<s>&Signature=<...>`.
   Corolario: no se pueden cachear las URLs y descargar después — hay que pedir
   y bajar en la misma pasada. Un JSON de curso guardado ayer tiene links muertos.
8. Los archivos `.vtt` llegan en **UTF-8**. `Get-Content` de PowerShell 5.1 los
   muestra como mojibake (`mÃ³dulo`) por codepage ANSI — es display, no
   corrupción. Verificar con `read_bytes()` antes de "arreglar" nada.

---

## Endpoints — estado verificado 2026-08-12

| Endpoint | Estado | Devuelve |
|---|---|---|
| `onDemandCourseMaterials.v2` | ✅ VIVO | árbol módulos→lecciones→items |
| `onDemandCourses.v1` | ✅ VIVO | metadata, descripción, courseId desde slug |
| `onDemandLectureVideos.v1` | ✅ VIVO | mp4 por resolución + subtítulos srt/vtt |
| `memberships.v1` | ✅ VIVO | los cursos en los que estás inscrita |
| `adminUserPermissions.v1` | ✅ VIVO | permisos |
| `onDemandCourseMaterials.v1` | ❌ MUERTO | 200 + HTML — **esto mató a `coursera-dl`** |
| `externalBasicProfiles.v1` | ❌ MUERTO | 200 + HTML |
| `/api/users/v1/me/enrollments` | ❌ 404 | el flujo OAuth2 del Developer Console ya no existe |
| `onDemandReferences.v1` | ⚠ 405 | existe, verbo equivocado |
| `onDemandCourseMaterialItems.v2` | ⚠ | params equivocados, no confirmado muerto |

### Rutas confirmadas

```
GET /api/onDemandCourses.v1/?q=slug&slug={slug}
GET /api/onDemandCourseMaterials.v2/?q=slug&slug={slug}
      &includes=modules,lessons,items
      &fields=moduleIds,
              onDemandCourseMaterialModules.v1(name,slug,lessonIds),
              onDemandCourseMaterialLessons.v1(name,slug,itemIds),
              onDemandCourseMaterialItems.v2(name,slug,contentSummary)
GET /api/onDemandLectureVideos.v1/{courseId}~{itemId}
      ?includes=video
      &fields=onDemandVideos.v1(sources,subtitles,subtitlesVtt)
GET /api/memberships.v1?q=me&includes=courseId,course
      &fields=courseId,course.v1(name,slug,courseType)&limit=100
```

`itemId` es el segmento de la URL: `/learn/{slug}/lecture/{itemId}/...`

---

## Contenido disponible (medido)

Curso `conquistaaudienciasconiag` — courseId `MQQf3JsJEfCPiQr_2dbk-Q`:

- 48 items, 18 de tipo `lecture`
- Otros tipos: `supplement` (lecturas CML), quizzes
- Video `DSzDu`: mp4 en `1080p / 720p / 540p / 360p / 240p`
- Subtítulos: `es` y `es-LA` en **srt** y **vtt**
- **Sin DRM, sin Widevine, sin CAPTCHA en la capa de API**
- ⚠ Corrección a una nota anterior: las URLs de media **sí** van firmadas
  (hmac / CloudFront Signature) con expiry. No hay DRM, pero tampoco son
  links permanentes. Ver gotcha 7.

### Corrida real (2026-08-12)
26 archivos `.vtt` (`es` + `es-LA`), 128.7 KB, 0 vacíos, 4 carpetas de módulo.
Todo el curso en texto pesa menos que un solo frame en 1080p.

---

## Decisión de diseño: transcripts-first

Un curso de 18 videos ≈ varios GB en mp4, contra ~200 KB en `.vtt`. Para
resumir, generar flashcards o montar RAG, el mp4 no aporta señal extra sobre
el transcript. Default del descargador = subtítulos + estructura; video
opt-in con `--videos`.

---

## Anti-patrón a evitar

No hardcodear rutas en el código. Van en `endpoints.json` versionado: cuando
Coursera vuelva a deprecar una `.v2`, el fix es una línea de datos. Esa fue
exactamente la deuda que mató a `coursera-dl`.
