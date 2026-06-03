#!/usr/bin/env python3
"""Industry Analysis SOP - Multi-source search strategy generator & integrity checker.

Usage:
  python3 search.py <industry_name> <type>
  python3 search.py <industry_name> <type> --with-shiso
  python3 search.py <industry_name> <type>
  python3 search.py <industry_name> <type> --with-shiso --with-mcp
  python3 search.py --compare "Industry A" <type_a> "Industry B" <type_b>
  python3 search.py --verify

Examples:
  python3 search.py "solid state battery" manufacturing
  python3 search.py "GLP-1 receptor agonist" biotech --with-mcp
  python3 search.py --compare "CGM" manufacturing "smartwatch" manufacturing
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


@dataclass
class ShisoQuery:
    branch: str
    queries: List[str]
    purpose: str
    priority: int  # 1=high, 2=medium, 3=low


INDUSTRY_TYPES_STR = "manufacturing|software|biotech|energy|frontier"
VALID_TYPES = tuple(INDUSTRY_TYPES_STR.split("|"))

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
        "skills/industry-analysis/references/templates/energy.md",
        "skills/industry-analysis/references/templates/frontier.md",
        "skills/industry-analysis/references/templates/TEMPLATE-GUIDE.md",
    ],
    "Examples": [
        "skills/industry-analysis/references/examples/cgm-example.md",
        "skills/industry-analysis/references/examples/ai-coding-example.md",
        "skills/industry-analysis/references/examples/solid-state-example.md",
        "skills/industry-analysis/references/examples/fusion-example.md",
    ],
    "Assets": [
        "skills/industry-analysis/assets/scenario-matrix.md",
        "skills/industry-analysis/assets/analysis-log-template.md",
        "skills/industry-analysis/assets/signal-tracker.md",
        "skills/industry-analysis/assets/comparison-matrix.md",
    ],
    "Outputs": [
        "outputs/README.md",
    ],
    "English": [
        "skills/industry-analysis/references/english/SKILL_en.md",
        "skills/industry-analysis/references/english/SOP_en.md",
    ],
    "Guides": [
        "CONTRIBUTING.md",
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
    elif industry_type == "energy":
        queries = [
            SearchQuery(f"{industry} market size installed capacity 2025 2030", 1, "market"),
            SearchQuery(f"{industry} LCOE cost learning curve", 1, "technology"),
            SearchQuery(f"{industry} policy subsidy regulation carbon price", 1, "policy"),
            SearchQuery(f"{industry} key companies market share competitive", 1, "competition"),
            SearchQuery(f"{industry} supply chain critical materials", 2, "supply_chain"),
            SearchQuery(f"{industry} project finance investment funding", 2, "market"),
            SearchQuery(f"{industry} technology breakthrough efficiency 2026", 2, "technology"),
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


def build_shiso_queries(industry: str, industry_type: str) -> List[ShisoQuery]:
    """Generate supply chain drill-down queries for chokepoint analysis."""
    queries = []
    if industry_type == "manufacturing":
        queries = [
            ShisoQuery("Raw Materials", [f"{industry} raw materials supply source", f"{industry} critical material dependency"], "Identify material-level scarcity", 1),
            ShisoQuery("Core Components", [f"{industry} key components suppliers", f"{industry} component bottleneck"], "Find component-level concentration", 1),
            ShisoQuery("Manufacturing Process", [f"{industry} production process critical step", f"{industry} manufacturing yield"], "Process-level chokepoints", 2),
            ShisoQuery("Equipment", [f"{industry} production equipment suppliers", f"{industry} manufacturing tooling"], "Equipment supply concentration", 2),
        ]
    elif industry_type == "software":
        queries = [
            ShisoQuery("Infrastructure", [f"{industry} cloud infrastructure dependency", f"{industry} compute cost"], "Infrastructure-level lock-in", 1),
            ShisoQuery("Data", [f"{industry} training data sources proprietary", f"{industry} data moat"], "Data scarcity and exclusivity", 1),
            ShisoQuery("Ecosystem", [f"{industry} platform dependency lock-in", f"{industry} API dependency"], "Platform/ecosystem control points", 2),
            ShisoQuery("Talent", [f"{industry} key talent scarcity hiring"], "Talent concentration risk", 3),
        ]
    elif industry_type == "biotech":
        queries = [
            ShisoQuery("Target/IP", [f"{industry} key patent exclusivity", f"{industry} target IP landscape"], "IP chokepoints", 1),
            ShisoQuery("Supply Chain", [f"{industry} raw material reagent supplier", f"{industry} manufacturing CMO CDMO"], "Manufacturing dependency", 1),
            ShisoQuery("Regulatory", [f"{industry} FDA approval bottleneck", f"{industry} regulatory pathway"], "Regulatory gatekeeper", 2),
            ShisoQuery("Clinical", [f"{industry} clinical trial enrollment site"], "Clinical execution risk", 2),
        ]
    elif industry_type == "energy":
        queries = [
            ShisoQuery("Critical Materials", [f"{industry} critical material supply chain", f"{industry} rare earth dependency"], "Material scarcity", 1),
            ShisoQuery("Manufacturing", [f"{industry} manufacturing equipment supplier concentration", f"{industry} production bottleneck"], "Equipment and production chokepoints", 1),
            ShisoQuery("Infrastructure", [f"{industry} grid connection permitting bottleneck", f"{industry} project approval timeline"], "Infrastructure access", 2),
            ShisoQuery("Capital", [f"{industry} project finance availability cost of capital"], "Capital concentration", 3),
        ]
    elif industry_type == "frontier":
        queries = [
            ShisoQuery("Capital", [f"{industry} venture capital concentration key investors"], "Capital gatekeeper", 1),
            ShisoQuery("Talent", [f"{industry} key scientist talent poaching"], "Talent bottleneck", 1),
            ShisoQuery("IP", [f"{industry} foundational patent university license"], "IP ownership", 2),
            ShisoQuery("Supply Chain", [f"{industry} specialized equipment supplier"], "Equipment dependency", 2),
        ]
    return queries


def print_shiso_table(queries: List[ShisoQuery]):
    print("\n## Shiso Chokepoint Analysis -- Supply Chain Drill-Down Queries")
    print("| Priority | Branch | Query | Purpose |")
    print("|----------|--------|-------|---------|")
    for q in sorted(queries, key=lambda x: x.priority):
        label = {1: "HIGH", 2: "MED", 3: "LOW"}[q.priority]
        for query in q.queries:
            print(f"| {label} | {q.branch} | `{query}` | {q.purpose} |")
    print("\nAfter gathering data, apply the 6-step Shiso method:")
    print("  1. Lock terminal demand  2. Branch drill-down + stop ruling")
    print("  3. First-principles GT    4. Cross-interaction + resort")
    print("  5. Forced falsification   6. Map companies to chokepoints")
    print("See `references/templates/shiso-chokepoint.md` for the full method.\n")


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


def print_compare_section(industry_a, type_a, industry_b, type_b):
    """Print parallel search queries for cross-industry comparison."""
    queries_a = build_queries(industry_a, type_a)
    queries_b = build_queries(industry_b, type_b)

    print(f"# Comparison: {industry_a} vs {industry_b}")
    print()
    print("## Side-by-Side Search Queries")
    print()
    print(f"| Dimension | {industry_a} | {industry_b} |")
    print(f"|-----------|{'─' * (len(industry_a) + 2)}|{'─' * (len(industry_b) + 2)}|")

    # Group by category for side-by-side comparison
    categories = ["market", "competition", "technology", "supply_chain", "policy"]
    for cat in categories:
        q_a = [q for q in queries_a if q.category == cat]
        q_b = [q for q in queries_b if q.category == cat]
        if not q_a and not q_b:
            continue
        label = {"market": "Market", "competition": "Competition",
                 "technology": "Technology", "supply_chain": "Supply Chain",
                 "policy": "Policy"}.get(cat, cat)
        a_text = "; ".join(q.query for q in q_a) if q_a else "(not applicable)"
        b_text = "; ".join(q.query for q in q_b) if q_b else "(not applicable)"
        print(f"| **{label}** | {a_text} | {b_text} |")

    # MCP suggestions for both
    mcp_a = build_mcp_suggestions(industry_a, type_a)
    mcp_b = build_mcp_suggestions(industry_b, type_b)
    if mcp_a or mcp_b:
        print()
        print("## MCP-Enhanced Suggestions")
        print("| Industry | Tool | Query | Purpose |")
        print("|----------|------|-------|---------|")
        for s in mcp_a:
            label = {1: "HIGH", 2: "MED", 3: "LOW"}[s.priority]
            print(f"| {industry_a} | {s.tool} | `{s.query_params}` | {s.purpose} [{label}] |")
        for s in mcp_b:
            label = {1: "HIGH", 2: "MED", 3: "LOW"}[s.priority]
            print(f"| {industry_b} | {s.tool} | `{s.query_params}` | {s.purpose} [{label}] |")

    print()
    print("## Recommended Workflow")
    print("1. Run Quick Mode on Industry A first, capture findings")
    print("2. Run Quick Mode on Industry B, capture findings")
    print("3. Load `assets/comparison-matrix.md` and fill side by side")
    print("4. Deliver comparison with explicit recommendation")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  python3 search.py <industry_name> <{INDUSTRY_TYPES_STR}>")
        print(f"  python3 search.py <industry_name> <{INDUSTRY_TYPES_STR}> --with-mcp")
        print(f"  python3 search.py --compare \"Industry A\" <type> \"Industry B\" <type>")
        print("  python3 search.py --verify")
        sys.exit(1)

    if sys.argv[1] == "--verify":
        ok = verify_integrity()
        sys.exit(0 if ok else 1)

    if sys.argv[1] == "--compare":
        if len(sys.argv) < 6:
            print("Usage: python3 search.py --compare \"Industry A\" <type_a> \"Industry B\" <type_b>")
            print(f"Valid types: {', '.join(VALID_TYPES)}")
            sys.exit(1)
        industry_a = sys.argv[2]
        type_a = sys.argv[3].lower()
        industry_b = sys.argv[4]
        type_b = sys.argv[5].lower()
        if type_a not in VALID_TYPES or type_b not in VALID_TYPES:
            print(f"Error: invalid type. Valid types: {', '.join(VALID_TYPES)}")
            sys.exit(1)
        print_compare_section(industry_a, type_a, industry_b, type_b)
        return

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

    if "--with-shiso" in sys.argv:
        shiso_queries = build_shiso_queries(industry, industry_type)
        if shiso_queries:
            print_shiso_table(shiso_queries)


if __name__ == "__main__":
    main()
