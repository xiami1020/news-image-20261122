"""Entry point: copy the bundled 22 November 2026 news front page.

Run:  python3 main.py

Copies the repository's entry.png to /output/entry.png, deterministically:
the same bytes on every run. Outside the grader, MAKEFUN_OUTPUT_DIR
stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main() -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)
    if out.stat().st_size != src.stat().st_size:
        raise RuntimeError("copied file size does not match source")
    print(f"copied {src} -> {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
