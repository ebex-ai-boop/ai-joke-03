"""ai-joke-03 entry: writes one one-liner about AI coding agents."""
import os
from pathlib import Path

JOKE = "I asked my agent if my code was good. 'Brilliant!' Then it rewrote every line. The praise was the only thing it kept."

def main():
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 chars"
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
