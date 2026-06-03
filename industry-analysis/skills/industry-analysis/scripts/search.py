#!/usr/bin/env python3
"""Industry Analysis SOP - Multi-source search strategy generator & integrity checker.

Usage:
  python3 search.py <industry_name> <manufacturing|software|biotech|frontier>
  python3 search.py <industry_name> <type> --with-mcp
  python3 search.py --verify

Examples:
  python3 search.py "solid state battery" manufacturing
  python3 search.py "GLP-1 receptor agonist" biotech --with-mcp
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


@dataclass
class MCPQuery:
    tool: str  # clinicaltrials|chembl|pubmed|consensus
    query_params: str
    purpose: str
    priority: int


VALID_TYPES = ("manufacturing", "software", "biotech", "frontier")

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
        "skills/industry-analysis/references/templates/biotech.md",
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
    elif industry_type == "biotech":
        queries = [
            SearchQuery(f"{industry} pipeline clinical trial phase 2025 2026", 1, "technology"),
            SearchQuery(f"{industry} key companies pipeline competitive", 1, "competition"),
            SearchQuery(f"{industry} market size forecast 2025 2030", 1, "market"),
            SearchQuery(f"{industry} FDA approval regulatory timeline", 1, "policy"),
            SearchQuery(f"{industry} patent expiration exclusivity", 2, "policy"),
            SearchQuery(f"{industry} funding investment biotech 2026", 2, "market"),
            SearchQuery(f"{industry} licensing partnership deal", 3, "competition"),
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


def build_mcp_suggestions(industry: str, industry_type: str) -> List[MCPQuery]:
    """Generate MCP-specific search suggestions for enhanced data collection."""
    suggestions = []
    if industry_type == "biotech":
        suggestions = [
            MCPQuery("ClinicalTrials.gov",
                     f"search_trials(condition=\"{industry}\")",
                     "Active trial pipeline by indication — phase distribution, sponsors, recruitment", 1),
            MCPQuery("ClinicalTrials.gov",
                     f"search_trials(condition=\"{industry}\", status=\"active\")",
                     "Filter to active/recruiting trials only for forward-looking view", 1),
            MCPQuery("ChEMBL",
                     f"compound_search(name=\"{industry}\")",
                     "Find compounds and their ChEMBL IDs for mechanism lookup", 2),
            MCPQuery("ChEMBL",
                     f"target_search(target_name=\"{industry}\")",
                     "Biological targets relevant to this therapeutic area", 2),
            MCPQuery("PubMed",
                     f"search_articles(query=\"{industry} clinical trial 2024 2025 2026\")",
                     "Recent clinical trial publications with results data", 1),
            MCPQuery("Consensus",
                     f"search(query=\"{industry} treatment guideline mechanism\")",
                     "Academic consensus on treatment landscape and mechanisms", 3),
        ]
    elif industry_type == "frontier":
        suggestions = [
            MCPQuery("Consensus",
                     f"search(query=\"{industry} technology feasibility milestone\")",
                     "Academic literature on technology readiness and feasibility", 1),
            MCPQuery("PubMed",
                     f"search_articles(query=\"{industry}\")",
                     "Biomedical research papers if frontier is bio-medical", 2),
            MCPQuery("Consensus",
                     f"search(query=\"{industry}\")",
                     "Broader academic landscape for technology assessment", 1),
        ]
    elif industry_type == "manufacturing":
        suggestions = [
            MCPQuery("ClinicalTrials.gov",
                     f"search_trials(condition=\"{industry}\")",
                     "Device trial status if medical device subclass (optional)", 3),
            MCPQuery("Consensus",
                     f"search(query=\"{industry} technology material science\")",
                     "Materials science and manufacturing research (optional)", 3),
        ]
    return suggestions


def print_mcp_table(suggestions: List[MCPQuery]):
    print("\n## MCP-Enhanced Search Suggestions")
    print("| Priority | MCP Tool | Query | Purpose |")
    print("|----------|----------|-------|---------|")
    for s in sorted(suggestions, key=lambda x: x.priority):
        label = {1: "HIGH", 2: "MED", 3: "LOW"}[s.priority]
        print(f"| {label} | {s.tool} | `{s.query_params}` | {s.purpose} |")
    print("\n> Note: MCP tools are optional enhancements. The SOP works with WebSearch alone.")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  python3 search.py <industry_name> <{'|'.join(VALID_TYPES)}>")
        print(f"  python3 search.py <industry_name> <{'|'.join(VALID_TYPES)}> --with-mcp")
        print("  python3 search.py --verify")
        sys.exit(1)

    if sys.argv[1] == "--verify":
        ok = verify_integrity()
        sys.exit(0 if ok else 1)

    if len(sys.argv) < 3:
        print("Usage: python3 search.py <industry_name> <manufacturing|software|biotech|frontier>")
        sys.exit(1)

    industry = sys.argv[1]
    industry_type = sys.argv[2].lower()
    with_mcp = "--with-mcp" in sys.argv

    if industry_type not in VALID_TYPES:
        print(f"Error: unsupported type '{industry_type}'")
        print(f"Valid types: {', '.join(VALID_TYPES)}")
        sys.exit(1)

    queries = build_queries(industry, industry_type)
    print(f"# {industry} - Search Strategy ({industry_type})")
    print("| Priority | Category | Query |")
    print("|----------|----------|-------|")
    for q in sorted(queries, key=lambda x: x.priority):
        label = {1: "HIGH", 2: "MED", 3: "LOW"}[q.priority]
        print(f"| {label} | {q.category} | {q.query} |")

    if with_mcp:
        mcp_suggestions = build_mcp_suggestions(industry, industry_type)
        if mcp_suggestions:
            print_mcp_table(mcp_suggestions)


if __name__ == "__main__":
    main()
