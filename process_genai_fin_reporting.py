"""
Pipeline de Limpieza, Modelado Cognitivo KST y Bóveda Obsidian
para: 'Generative AI Governance in Financial Reporting' (gen-ai-gov-financial-reporting)
"""

import json
import re
from pathlib import Path

COURSE_SLUG = "gen-ai-gov-financial-reporting"
DOWNLOADS_DIR = Path(__file__).parent / "downloads" / COURSE_SLUG
VAULT_DIR = Path(__file__).parent / "obsidian_vault_genai_financial_reporting"
GRAPH_FILE = Path(__file__).parent / "course_knowledge_graph_genai_fin.json"

# Correcciones fonéticas y de traducción automática de subtítulos
CORRECTIONS = {
    r"\bLaLaLAMs\b": "LLMs",
    r"\bLaLaLAM\b": "LLM",
    r"\blalams\b": "LLMs",
    r"\blalam\b": "LLM",
    r"\bingeniería PROM\b": "Ingeniería de Prompts",
    r"\bPROM\b": "Prompt",
    r"\bproms\b": "prompts",
    r"\bACFR\b": "ACFR (Annual Comprehensive Financial Report)",
    r"\bESG\b": "ESG (Environmental, Social, Governance)",
}

def clean_transcript_text(raw_text: str) -> str:
    # Eliminar header WEBVTT
    lines = raw_text.splitlines()
    cleaned_lines = []
    
    timestamp_regex = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}")
    digit_regex = re.compile(r"^\d+$")

    for line in lines:
        line = line.strip()
        if not line or line.startswith("WEBVTT") or line.startswith("NOTE") or timestamp_regex.match(line) or digit_regex.match(line):
            continue
        cleaned_lines.append(line)

    text = " ".join(cleaned_lines)
    for pattern, repl in CORRECTIONS.items():
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    
    return text

def parse_and_build_vault():
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    (VAULT_DIR / "00_Home").mkdir(exist_ok=True)
    (VAULT_DIR / "01_Modulos").mkdir(exist_ok=True)
    (VAULT_DIR / "02_Lecciones").mkdir(exist_ok=True)
    (VAULT_DIR / "03_Conceptos").mkdir(exist_ok=True)
    (VAULT_DIR / "04_Reglas_Decision_Gobierno").mkdir(exist_ok=True)
    (VAULT_DIR / "05_Retos_Feynman").mkdir(exist_ok=True)

    module_dirs = sorted([d for d in DOWNLOADS_DIR.iterdir() if d.is_dir()])
    
    all_lessons = []
    
    for mod_idx, mod_dir in enumerate(module_dirs, 1):
        mod_name = mod_dir.name
        mod_file = VAULT_DIR / "01_Modulos" / f"M{mod_idx:02d} - {mod_name}.md"
        
        lesson_files = sorted(list(mod_dir.glob("*.es.vtt")))
        lesson_links = []

        for l_file in lesson_files:
            l_name = l_file.stem.replace(".es", "")
            raw_vtt = l_file.read_text(encoding="utf-8")
            clean_text = clean_transcript_text(raw_vtt)
            
            all_lessons.append({
                "module_num": mod_idx,
                "module_name": mod_name,
                "lesson_name": l_name,
                "text": clean_text,
                "raw_vtt": raw_vtt
            })
            
            lesson_md = VAULT_DIR / "02_Lecciones" / f"{l_name}.md"
            lesson_content = f"""# {l_name}

- **Módulo**: [[M{mod_idx:02d} - {mod_name}]]
- **Curso**: Generative AI Governance in Financial Reporting

---

## 📜 Transcripción Curada

{clean_text}

---

## 🧠 Enlaces y Conceptos Relacionados
- [[00_Home/MOC - Gen AI Governance]]
"""
            lesson_md.write_text(lesson_content, encoding="utf-8")
            lesson_links.append(f"- [[02_Lecciones/{l_name}|{l_name}]]")

        mod_content = f"""# Módulo {mod_idx:02d}: {mod_name}

## 📚 Lecciones del Módulo
{chr(10).join(lesson_links)}

---
[[00_Home/MOC - Gen AI Governance|← Volver al Mapa Principal]]
"""
        mod_file.write_text(mod_content, encoding="utf-8")

    # MOC Home
    moc_content = f"""# 🏛️ MOC — Generative AI Governance in Financial Reporting

> **Gobernanza, Extracción de Datos No Estructurados y Auditoría de LLMs en Finanzas y Contabilidad.**

## 📑 Estructura del Curso
1. [[01_Modulos/M01 - 01- Introduction to Generative AI and LLMs in Accounting|Módulo 1: Fundamentos de IA Generativa y LLMs en Contabilidad]]
2. [[01_Modulos/M02 - 02-Methods of Implementing LLMs in Accounting|Módulo 2: Métodos de Implementación (UI, API, RPA, API-RPA)]]
3. [[01_Modulos/M03 - 03-Extracting Financial Data from Unstructured Sources|Módulo 3: Extracción de Datos Financieros No Estructurados (ACFR y ESG)]]
4. [[01_Modulos/M04 - 04- Evaluating Framework Performance|Módulo 4: Evaluación de Desempeño, Detección de Errores y Gobernanza]]

---
*Bóveda generada automáticamente por coursera_reverse.*
"""
    (VAULT_DIR / "00_Home" / "MOC - Gen AI Governance.md").write_text(moc_content, encoding="utf-8")
    
    print(f"[OK] Bóveda Obsidian generada con {len(all_lessons)} lecciones en: {VAULT_DIR}")

if __name__ == "__main__":
    parse_and_build_vault()
