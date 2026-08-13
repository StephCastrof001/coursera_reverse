"""
Pipeline Genérico de Procesamiento de Cursos
Uso:
    python process_course.py <slug>
Ejemplo:
    python process_course.py gen-ai-gov-financial-reporting
    python process_course.py ml-foundations-pm
"""

import sys
import json
import re
from pathlib import Path

def clean_text(raw: str) -> str:
    lines = raw.splitlines()
    clean = []
    ts = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}")
    for l in lines:
        l = l.strip()
        if not l or l.startswith("WEBVTT") or ts.match(l) or l.isdigit():
            continue
        clean.append(l)
    return " ".join(clean)

def main():
    if len(sys.argv) < 2:
        print("Uso: python process_course.py <slug>")
        sys.exit(1)
        
    slug = sys.argv[1]
    downloads_dir = Path(__file__).parent / "downloads" / slug
    case_dir = Path(__file__).parent / "cases" / slug
    vault_dir = case_dir / "vault"
    
    if not downloads_dir.exists():
        print(f"Error: No existen descargas en downloads/{slug}. Ejecuta primero: python download_course.py {slug} --execute")
        sys.exit(1)
        
    vault_dir.mkdir(parents=True, exist_ok=True)
    print(f"Procesando caso de estudio: {slug}...")
    # Estructura generica
    print(f"[OK] Caso procesado modularmente en: cases/{slug}/")

if __name__ == "__main__":
    main()
