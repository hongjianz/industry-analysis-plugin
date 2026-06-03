#!/usr/bin/env python3
"""Industry Analysis SOP - Multi-source search strategy generator & integrity checker.

Usage:
  python3 search.py <industry_name> <industry_type: manufacturing|software|frontier>
  python3 search.py --verify

Examples:
  python3 search.py "solid state battery" manufacturing
  python3 search.py --verify
"""

import os
import sys
from dataclasses import dataclass
from typing import List


@dataclass
class SearchQuery:
    query: str
    priority: int  # 1=high, 2=medium, 3=low
    category: str  # market|technology|competition|supply_chain|policy


PLUGIN_ROOT = os.environ.get(
    "CLAUDE_PLUGIN_ROOT",
    os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "..")),
)

REQUIRED_FILES = {
    "Core": [
        "skills/industry-analysis/SKILL.md",
        "skills/industry-analysis/references/SOP-v1.0.md",
        "skills/industry-analysis/scripts/search.py",
    ],
    "Templates": [
        "skills/industry-analysis/references/templates/manufacturing.md",
        "skills/industry-analysis/references/templates/software.md",
        "skills/industry-analysis/references/templates/frontier.md",
    ],
    "Examples": [
        "skills/industry-analysis/references/examples/cgm-example.md",
        "skills/industry-analysis/references/examples/ai-coding-example.md",
        "skills/industry-analysis/references/examples/solid-state-example.md",
        "skills/industry-analysis/references/examples/fusion-example.md",
    ],
    "Assets": [
        "skills/industry-analysis/assets/scenario-matrix.md",
    ],
    "Plugin Config": [
        ".claude-plugin/plugin.json",
        ".claude/settings.json",
        "CLAUDE.md",
    ],
}


def verify_integrity() -> bool:
    """Check that all required plugin files exist."""
    all_ok = True
    print("# Industry Analysis Plugin - Integrity Check")
    print(f"Root: {PLUGIN_ROOT}")
    print()
    for group, files in REQUIRED_FILES.items():
        print(f"## {group}")
        for rel_path in files:
            full_path = os.path.join(PLUGIN_ROOT, rel_path)
            exists = os.path.isfile(full_path)
            status = "✓" if exists else "✗ MISSING"
            if not exists:
                all_ok = False
            print(f"  [{status}] {rel_path}")
        print()
    if all_ok:
        print("Result: ALL FILES PRESENT")
    else:
        print("Result: SOME FILES ARE MISSING — check the ✗ entries above")
    return all_ok


def build_queries(industry: str, industry_type: str) -> List[SearchQuery]:
    queries = []
    if industry_type == "manufacturing":
        queries = [
            SearchQuery(f"{industry} market size 2025 2026", 1, "market"),
            SearchQuery(f"{industry} market share competitive landscape", 1, "competition"),
            SearchQuery(f"{industry} leading companies revenue", 1, "competition"),
            SearchQuery(f"{industry} supply chain upstream raw materials", 2, "supply_chain"),
            SearchQuery(f"{industry} technology roadmap manufacturing", 2, "technology"),
            SearchQuery(f"{industry} breakthrough 2026", 2, "technology"),
            SearchQuery(f"{industry} policy regulation subsidy", 3, "policy"),
        ]
    elif industry_type == "software":
        queries = [
            SearchQuery(f"{industry} market size 2025 2026 ARR", 1, "market"),
            SearchQuery(f"{industry} competitive landscape market share", 1, "competition"),
            SearchQuery(f"{industry} benchmark evaluation comparison", 2, "technology"),
            SearchQuery(f"{industry} open source vs proprietary", 2, "technology"),
            SearchQuery(f"{industry} pricing model funding 2026", 1, "market"),
            SearchQuery(f"{industry} developer adoption survey", 3, "market"),
        ]
    elif industry_type == "frontier":
        queries = [
            SearchQuery(f"{industry} technology breakthrough 2026", 1, "technology"),
            SearchQuery(f"{industry} key players funding investment", 1, "competition"),
            SearchQuery(f"{industry} government policy roadmap", 1, "policy"),
            SearchQuery(f"{industry} timeline commercial 2025 2030", 2, "technology"),
            SearchQuery(f"{industry} supply chain materials equipment", 3, "supply_chain"),
        ]
    return queries


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 search.py <industry_name> <manufacturing|software|frontier>")
        print("  python3 search.py --verify")
        sys.exit(1)

    if sys.argv[1] == "--verify":
        ok = verify_integrity()
        sys.exit(0 if ok else 1)

    if len(sys.argv) < 3:
        print("Usage: python3 search.py <industry_name> <manufacturing|software|frontier>")
        sys.exit(1)

    industry = sys.argv[1]
    industry_type = sys.argv[2].lower()
    if industry_type not in ("manufacturing", "software", "frontier"):
        print(f"Error: unsupported type '{industry_type}'")
        sys.exit(1)

    queries = build_queries(industry, industry_type)
    print(f"# {industry} - Search Strategy ({industry_type})")
    print("| Priority | Category | Query |")
    print("|----------|----------|-------|")
    for q in sorted(queries, key=lambda x: x.priority):
        label = {1: "HIGH", 2: "MED", 3: "LOW"}[q.priority]
        print(f"| {label} | {q.category} | {q.query} |")


if __name__ == "__main__":
    main()
