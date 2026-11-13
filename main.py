"""ai-joke-03 entry: writes one one-liner about AI coding agents."""
import os
from pathlib import Path

JOKE = "I asked my agent to add error handling. It wrapped everything in try/except: pass. The app never crashes now. It also never works."

def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
