#!/usr/bin/env python3
"""Industry Analysis SOP - Multi-source search strategy generator.

Usage: python3 search.py <industry_name> <industry_type: manufacturing|software|frontier>
Example: python3 search.py "solid state battery" manufacturing
"""

import sys
from dataclasses import dataclass
from typing import List


@dataclass
class SearchQuery:
    query: str
    priority: int  # 1=high, 2=medium, 3=low
    category: str  # market|technology|competition|supply_chain|policy


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
