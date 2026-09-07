#!/usr/bin/env python3
"""Print health metrics for a second-brain vault.

Usage:
    python3 vault_stats.py /path/to/vault

Reports page counts by type, link density, orphan rate and the most connected
pages. Track these over time: a rising orphan rate means ingestion is running
without linking, which is the usual way a vault stops being useful.
"""
import os
import re
import sys
from collections import Counter, defaultdict

LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
TYPE = re.compile(r"^type:\s*(\S+)", re.M)
SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", "raw"}


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: vault_stats.py /path/to/vault")
    vault = sys.argv[1]

    pages, types = {}, Counter()
    for dirpath, dirnames, filenames in os.walk(vault):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                path = os.path.join(dirpath, name)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                pages[path] = text
                m = TYPE.search(text)
                types[m.group(1) if m else "untyped"] += 1

    if not pages:
        sys.exit("no markdown files found")

    stems = {os.path.splitext(os.path.basename(p))[0].lower(): p for p in pages}
    indeg = defaultdict(int)
    total = 0
    for path, text in pages.items():
        for target in LINK.findall(text):
            dest = stems.get(target.strip().lower())
            if dest and dest != path:
                indeg[dest] += 1
                total += 1

    orphans = [p for p in pages if indeg[p] == 0]
    words = sum(len(t.split()) for t in pages.values())

    print(f"pages          {len(pages)}")
    for t, c in types.most_common():
        print(f"  {t:<12} {c}")
    print(f"words          {words:,}")
    print(f"links          {total}")
    print(f"avg degree     {total / len(pages):.2f}")
    print(f"orphan rate    {100 * len(orphans) / len(pages):.1f}%")
    print("\nmost linked:")
    for path, n in sorted(indeg.items(), key=lambda kv: -kv[1])[:10]:
        print(f"  {n:>4}  {os.path.relpath(path, vault)}")


if __name__ == "__main__":
    main()
