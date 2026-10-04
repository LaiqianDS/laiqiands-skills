#!/usr/bin/env python3
"""Build course.html, the course book, from the Markdown files of a course.

Usage: build_book.py [workspace] [lang]

The script only embeds the files. The page parses and renders them.
"""

import json
import sys
from pathlib import Path

SLOT = "{{data}}"
TEMPLATE = Path(__file__).resolve().parent.parent / "references" / "course-template.html"


def build(workspace: Path, lang: str) -> Path:
    data = {
        "lang": lang,
        "course": (workspace / "COURSE.md").read_text(encoding="utf-8"),
        "map": (workspace / "MAP.md").read_text(encoding="utf-8"),
        "lessons": [
            {"id": path.stem, "md": path.read_text(encoding="utf-8")}
            for path in sorted((workspace / "lessons").glob("*.md"))
        ],
    }
    template = TEMPLATE.read_text(encoding="utf-8")
    assert template.count(SLOT) == 1, "the template must hold exactly one data slot"
    # "<" is escaped so that no lesson text can close the script element.
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    out = workspace / "course.html"
    out.write_text(template.replace(SLOT, payload), encoding="utf-8")
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        print(build(Path(args[0] if args else "."), args[1] if len(args) > 1 else "en"))
    except FileNotFoundError as error:
        sys.exit(f"Not a course workspace: {error.filename} is missing.")
