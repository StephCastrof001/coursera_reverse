import re
import os
import json
from pathlib import Path

def clean_vtt_file(vtt_path: Path) -> str:
    text = vtt_path.read_text(encoding="utf-8")
    pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}\r?\n([\s\S]*?)(?=\r?\n\r?\n|\Z)')
    cues = pattern.findall(text)
    
    paragraphs, current_p, current_ts = [], [], None
    for ts, raw_cue in cues:
        cue_text = " ".join(raw_cue.strip().split())
        if not cue_text:
            continue
        if current_ts is None:
            current_ts = ts.split(".")[0][3:] # '01:23'
        current_p.append(cue_text)
        
        full_line = " ".join(current_p)
        if len(full_line) > 280 and cue_text[-1] in '.?!':
            paragraphs.append(f"[{current_ts}] {full_line}")
            current_p, current_ts = [], None
            
    if current_p:
        paragraphs.append(f"[{current_ts}] {' '.join(current_p)}")
    return "\n\n".join(paragraphs)

def process_course(course_dir: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    stats = []
    
    # Process each module folder
    for mod_dir in sorted(course_dir.glob("0*")):
        if not mod_dir.is_dir():
            continue
        mod_name = mod_dir.name
        mod_out_dir = out_dir / mod_name
        mod_out_dir.mkdir(exist_ok=True)
        
        # Look for Spanish or English files
        vtt_files = sorted(mod_dir.glob("*.es.vtt"))
        lang = "es"
        if not vtt_files:
            vtt_files = sorted(mod_dir.glob("*.en.vtt"))
            lang = "en"
            
        mod_text_blocks = []
        for vtt in vtt_files:
            lec_title = vtt.name.replace(f".{lang}.vtt", "")
            cleaned = clean_vtt_file(vtt)
            words = len(cleaned.split())
            stats.append({"module": mod_name, "lecture": lec_title, "words": words, "lang": lang})
            
            # Save single lesson markdown
            lesson_md = f"# {lec_title}\n<!-- Módulo: {mod_name} | Archivo: {vtt.name} -->\n\n{cleaned}\n"
            (mod_out_dir / f"{lec_title}.md").write_text(lesson_md, encoding="utf-8")
            
            mod_text_blocks.append(lesson_md)
            
        # Save complete module markdown
        (out_dir / f"{mod_name}.md").write_text("\n\n---\n\n".join(mod_text_blocks), encoding="utf-8")
        
    summary_file = out_dir / "course_stats.json"
    summary_file.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    
    total_words = sum(s["words"] for s in stats)
    total_lessons = len(stats)
    print(f"PROCESAMIENTO COMPLETO:")
    print(f"- Lecciones procesadas: {total_lessons}")
    print(f"- Total de palabras en el curso: {total_words:,}")
    print(f"- Tokens estimados: ~{int(total_words * 1.35):,}")

if __name__ == "__main__":
    course_root = Path("/home/focusacademia05/coursera_reverse/downloads/machine-learning-foundations-for-product-managers")
    output_root = Path("/home/focusacademia05/coursera_reverse/cleaned_ml_course")
    process_course(course_root, output_root)
