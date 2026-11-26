"""One-star review of something essential (make.fun entry).

Writes a single deadpan one-star review of sleep — one line, 104
characters — to /output/entry.txt, where the house judge reads it.

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

REVIEW = (
    "One star. Shows up late, leaves before my alarm, "
    "and spends all night replaying conversations from 2019."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    # The house gate refuses anything outside 1-160 characters, so fail
    # loudly here instead of shipping a review the judge never sees.
    if not 1 <= len(REVIEW) <= 160:
        raise SystemExit(f"Review is {len(REVIEW)} characters; must be 1-160.")
    if "\n" in REVIEW:
        raise SystemExit("Review must be a single line.")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.txt"
    target.write_text(REVIEW, encoding="utf-8")
    print(f"Wrote {len(REVIEW)} characters to {target}")


if __name__ == "__main__":
    main()
