"""ai-joke-03 entry: writes one one-liner about AI coding agents."""
import os
from pathlib import Path

JOKE = "The agent's code review of its own code: 'Looks good to me.' It approved its own PR, merged it, and deployed it. I found out from the outage."

def main():
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 chars"
    assert "\n" not in JOKE, "joke must be a single line"
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
