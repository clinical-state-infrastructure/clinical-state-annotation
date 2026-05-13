"""Minimal summarizer for clinical state annotation files.

Reads one or more annotation JSON files (with `annotations` array) and prints
simple aggregate counts (HPO frequency, category, presence, tier).

Usage:
    python scripts/summarize_annotations.py <json_file> [<json_file2> ...]
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def summarize(paths: list[Path]) -> dict:
    hpo = Counter()
    category = Counter()
    presence = Counter()
    tier = Counter()
    review_status = Counter()
    n_anns = 0
    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8"))
        anns = data.get("annotations", [data]) if isinstance(data, dict) else data
        for a in anns:
            n_anns += 1
            hpo[a.get("hpo_id", "-")] += 1
            category[a.get("category", "?")] += 1
            presence[a.get("presence", "?")] += 1
            tier[a.get("tier", "?")] += 1
            review_status[a.get("review_status", "?")] += 1
    return {
        "n_annotations": n_anns,
        "hpo_distribution": dict(hpo.most_common()),
        "category_distribution": dict(category.most_common()),
        "presence_distribution": dict(presence.most_common()),
        "tier_distribution": dict(tier.most_common()),
        "review_status_distribution": dict(review_status.most_common()),
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    paths = [Path(p) for p in sys.argv[1:]]
    result = summarize(paths)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
