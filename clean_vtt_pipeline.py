import re
import os
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

if __name__ == "__main__":
    import sys
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    for vtt in sorted(base_dir.glob("*.es.vtt")):
        clean_text = clean_vtt_file(vtt)
        words = len(clean_text.split())
        print(f"=== {vtt.name} ({words} palabras) ===")
        print(clean_text[:350] + "...\n")
