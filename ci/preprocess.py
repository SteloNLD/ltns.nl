#!/usr/bin/env python3
"""Preprocess Obsidian content for a target SSG.

Uses obsidian-export to convert wikilinks and embeds, then generates
the _index.md files Hugo and Zola need for section listings.

Usage: python ci/preprocess.py <hugo|zola>
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
CONTENT_SRC = ROOT / "content"
STATIC_SRC = ROOT / "static"
SECTIONS = ["notes", "references"]


def generate_index_files(dst: Path) -> None:
    for section in SECTIONS:
        index_file = dst / section / "_index.md"
        index_file.parent.mkdir(parents=True, exist_ok=True)
        if not index_file.exists():
            index_file.write_text(f"---\ntitle: {section.capitalize()}\n---\n")

    root_index = dst / "_index.md"
    if not root_index.exists():
        root_index.write_text("---\ntitle: ltns.nl\n---\n")


QUARTZ_IGNORE = shutil.ignore_patterns("templates", "inbox", "journal")


def preprocess(target: str) -> None:
    dst = ROOT / target / "content"
    if dst.exists():
        shutil.rmtree(dst)

    if target == "quartz":
        shutil.copytree(CONTENT_SRC, dst, ignore=QUARTZ_IGNORE)
    else:
        dst.mkdir(parents=True)
        subprocess.run(
            ["obsidian-export", str(CONTENT_SRC), str(dst)],
            check=True,
        )
        # Hugo and Zola use _index.md for the home page
        index = dst / "index.md"
        if index.exists():
            index.rename(dst / "_index.md")
        generate_index_files(dst)

    static_dst = ROOT / target / "static"
    if static_dst.exists():
        shutil.rmtree(static_dst)
    shutil.copytree(STATIC_SRC, static_dst)

    print(f"Done → {target}/content/ + {target}/static/")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("hugo", "zola", "quartz"):
        print("Usage: preprocess.py <hugo|zola|quartz>")
        sys.exit(1)
    preprocess(sys.argv[1])
