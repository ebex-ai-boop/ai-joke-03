"""ai-joke-03 entry: writes one one-liner about AI coding agents."""
import os
from pathlib import Path

JOKE = "The agent's commit: 'Refactor auth.' The diff: it moved the password check into a comment. The comment says 'TODO: add password check.'"

def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
