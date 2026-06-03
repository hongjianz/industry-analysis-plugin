---
name: industry-analysis
description: >
  This skill should be used when the user asks to "分析行业", "行业洞察", "产业分析",
  "industry analysis", "行业研究", "分析一下 XXX 行业", or uses the /industry-analysis
  command. It implements Wang Yuquan's (王煜全) Industrial Insights Methodology as a
  systematic 18-step SOP validated across manufacturing, software, biotech, and frontier technology
  industries. Supports two modes: --quick (4-step rapid scan) and --full (18-step deep analysis).
version: 1.3.0
argument-hint: "'[--quick|--full] <industry-name>'"
allowed-tools:
  [
    "WebSearch",
    "WebFetch",
    "Bash",
    "Read",
    "Write",
    "Edit",
    "Agent",
    "WebSearch",
    "WebFetch",
  ]
session-start:
  - "Run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py --verify` to verify all reference files exist"
  - "Check which MCP servers are available — especially bio-research tools (PubMed, ChEMBL, Consensus, ClinicalTrials)"
---

# Industry Analysis SOP / 产业洞察SOP

Systematic industry analysis framework based on Wang Yuquan's Industrial Insights Methodology (产业洞察方法学). Delivers structured analysis from industry boundary definition through scenario matrix and signal tracking.

## Session Initialization

On session start, verify integrity:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py --verify
```

If any files are missing, report them before proceeding. Restore context from `CLAUDE.md` at the project root if available.

Check `outputs/signal-tracker.md` for previously tracked leading indicators — this provides continuity with past analyses. If `outputs/` contains past analysis logs, briefly summarize the most recent one to orient the session.

Check available MCP servers. The following bio-research tools significantly enhance data quality when present:
- **PubMed**: Biomedical literature search
- **ChEMBL**: Drug target mechanisms and compound data
- **Consensus**: Academic paper synthesis with citation metadata
- **ClinicalTrials.gov**: Clinical trial pipeline data

---

## Quick Start

### Mode Selection

| Mode | Flag | Steps | When to Use |
|------|------|-------|-------------|
| Quick scan | `--quick` | 4 steps | Rapid assessment: is this industry worth deeper analysis? |
| Full analysis | `--full` | 18 steps | Deep dive: comprehensive understanding with prediction |

### Examples

```
/industry-analysis --quick 固态电池
/industry-analysis --full AI编程工具
```

Or invoke naturally: *"帮我用产业洞察框架分析一下CGM行业"*

## Execution Workflow

### Step 0: Determine Industry Type

Classify the industry before starting:

| Type | Characteristics | Template |
|------|----------------|----------|
| **Manufacturing** | Physical supply chain, raw materials, production scale, inventory | `references/templates/manufacturing.md` |
| **Software** | No physical supply chain, platform effects, network moats, R&D driven | `references/templates/software.md` |
| **Biotech/Pharma** | R&D pipeline-driven, FDA/EMA regulatory path, patent lifecycle, clinical trial data as leading indicator | `references/templates/biotech.md` |
| **Frontier Technology** | Pre-commercialization, tech roadmap uncertain, capital-intensive | `references/templates/frontier.md` |

Load the corresponding template — it will guide the analysis structure.

---

### Quick Mode (4 Steps)

Complete in 1-2 conversation turns.

**Step 1: Industry Boundary + Four-Dimension Check**

Load `references/SOP-v1.0.md` for the four-dimension evaluation framework (Technology Maturity, Market Stage, Industry Chain Completeness, Competitive Pattern). Apply it to the target industry and document the assessment.

**Step 2: Leading Indicator Identification**

Identify 3-5 leading indicators (超前指标) that signal where the industry is heading. Store in a structured table with columns: Indicator | Data Source | Update Cadence | Current Signal.

Peel the supply/ecosystem chain upstream to find scarcity control points (稀缺性控制点).

**Step 3: Competitive Landscape Scan**

Search for market share data, key players, revenue figures, and competitive dynamics. Focus on who controls the scarcity points identified above.

**Step 4: Pyramid Output + Persist**

Synthesize findings into a pyramid-structured report:
- **Top**: One-sentence conclusion (investment/thesis judgment)
- **Middle**: 3-5 key supporting arguments
- **Bottom**: Evidence summary for each argument

**After the report, persist the analysis:**
1. Load `assets/analysis-log-template.md` and fill it with the findings
2. Write the filled log to `outputs/<YYYY-MM-DD>-<industry-slug>.md`
3. Append new leading indicators to `outputs/signal-tracker.md` (or update existing ones)
4. Mention the output file path in the final response so the user knows where to find it

---

### Full Mode (18 Steps)

Complete in 3-5 conversation turns. Load `references/SOP-v1.0.md` for the complete methodology.

**Phase A: Define & Frame (Steps 1-4)**
1. Define industry boundary (scope what's in/out)
2. Apply four-dimension evaluation
3. Build logic tree with hypotheses
4. Design data collection plan — include MCP tools if applicable (see MCP Decision Tree below)

**Phase B: Research & Analyze (Steps 5-10)**
5. **Multi-source data collection**:
   - Run `scripts/search.py` to generate web search queries
   - Use MCP tools where applicable (see MCP Decision Tree below)
   - Cross-validate findings across WebSearch and MCP sources
6. Identify leading indicators (超前指标)
7. Analyze supply/ecosystem chain — peel to upstream scarcity control points
8. Select analytical model (Porter's Five Forces / Value Chain / Platform Ecosystem / Pipeline Analysis / etc.)
9. Build pyramid structure
10. Validate each hypothesis against collected data

**Phase C: Predict & Conclude (Steps 11-15)**
11. Identify 2-4 key variables shaping the industry's future
12. Build 2x2 scenario matrix — use `assets/scenario-matrix.md` as template
13. Assign probabilities and identify signals for each scenario
14. Formulate actionable thesis
15. Document key risks and assumptions

**Phase D: Reflect & Persist (Steps 16-18)**
16. Review what worked and what didn't in this analysis
17. Update leading indicator tracker in `outputs/signal-tracker.md`
18. Identify next review trigger (time-based or event-based)

**After Phase D, persist the full analysis:**
1. Load `assets/analysis-log-template.md` and fill it with all findings from Phases A-D
2. Write the completed log to `outputs/<YYYY-MM-DD>-<industry-slug>.md`
3. Append new leading indicators to `outputs/signal-tracker.md` (or update existing entries with latest values and trend direction)
4. Mention the output file path in the final response so the user knows where to find it

---

## Multi-Source Search Strategy

Run the search script to generate tailored search queries:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py "<industry>" <manufacturing|software|frontier>
```

For MCP-enhanced search, use the `--with-mcp` flag:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py "<industry>" <type> --with-mcp
```

This generates both web search queries and MCP-specific search suggestions.

---

## MCP Decision Tree

MCP tools are **optional enhancements** — the SOP works with WebSearch alone. When bio-research MCP servers are available, use the following decision tree to supplement data collection:

```
Industry classified as Biotech/Pharma?
├── YES → Use ALL available bio-research tools:
│   ├── ClinicalTrials.gov
│   │   ├── Trial pipeline by indication/drug class
│   │   ├── Phase distribution (Preclinical → I → II → III → Approved)
│   │   ├── Sponsor landscape (which companies are running trials)
│   │   └── Enrollment data (trial size, recruitment status)
│   ├── ChEMBL
│   │   ├── Drug mechanism of action (target, pathway)
│   │   ├── Compound landscape (which drugs target which proteins)
│   │   └── Bioactivity data (potency, selectivity)
│   ├── PubMed
│   │   ├── Therapeutic area literature review
│   │   ├── Clinical trial results publications
│   │   └── Mechanism / target validation papers
│   └── Consensus
│       ├── Academic literature synthesis
│       └── Citation analysis for key claims
│
├── Industry = Frontier Technology?
│   ├── YES → Use:
│   │   ├── Consensus
│   │   │   ├── Technology readiness literature
│   │   │   ├── Feasibility studies and milestone validation
│   │   │   └── Academic landscape overview
│   │   └── PubMed (if bio-medical frontier, e.g., gene therapy, cell therapy)
│   │       ├── Preclinical research papers
│   │       └── Early-phase clinical data
│   │
│   └── NO → WebSearch remains primary
│
└── Industry = Manufacturing or Software?
    └── WebSearch/WebFetch remain primary
        └── Consensus as supplementary for:
            ├── Technology trend reports
            └── Academic research on specific technologies
```

**Important rules:**
1. Always verify MCP servers are actually available before calling them — check session initialization output
2. Cross-validate MCP findings with WebSearch — MCP provides depth, WebSearch provides breadth
3. Cite MCP sources the same way you cite WebSearch: with specific references and links
4. When MCP servers are unavailable, fall back to WebSearch — the SOP never depends on MCP

---

## Persistence: Cross-Session Memory

The SOP supports cross-session persistence through structured output files. This enables the "Reflect" phase's core purpose: tracking leading indicators over time and revisiting past predictions.

### Output Directory Structure

```
outputs/
├── <YYYY-MM-DD>-<industry-slug>.md      # Analysis log (one per analysis)
├── signal-tracker.md                     # Growing tracker of leading indicators
└── README.md                             # Directory guide
```

### How Persistence Works

1. **After each analysis**, fill `assets/analysis-log-template.md` with findings and write to `outputs/`
2. **Update or append** leading indicators to `outputs/signal-tracker.md`:
   - New indicators get a new entry
   - Existing indicators get a new date row with latest value and trend direction
3. **On next session start**, check `outputs/signal-tracker.md` for continuity:
   - Which industries were analyzed?
   - What leading indicators are being tracked?
   - What signals to watch for next?
4. **Signal direction markers**: 🟢 Up 🔴 Down 🟡 Flat ⚪ Pending

### When to Persist

| Mode | Persistence Action |
|------|-------------------|
| **Quick scan** | Write analysis log + update signal tracker |
| **Full analysis** | Write full analysis log + update signal tracker |
| **Signal review** (ad-hoc) | Update signal tracker only |

> Persistence is opt-in by design — the user can skip it if the analysis is exploratory. Always ask before writing if uncertain.

---

## Reference Files

### Core Methodology
- **`references/SOP-v1.0.md`** — Complete 18-step SOP with detailed instructions for each step

### Industry Templates
- **`references/templates/manufacturing.md`** — Manufacturing-specific analysis template (supply chain, raw materials, production scale)
- **`references/templates/software.md`** — Software-specific template (platform effects, network moats, ecosystem)
- **`references/templates/biotech.md`** — Biotech/pharma template (pipeline analysis, regulatory path, patent lifecycle, MCP-optimized)
- **`references/templates/frontier.md`** — Frontier tech template (tech roadmap uncertainty, capital intensity, policy drivers)

### Examples (Validated Case Studies)
- **`references/examples/cgm-example.md`** — CGM case: supply chain scarcity determines pricing power
- **`references/examples/ai-coding-example.md`** — AI Coding Tools: from supply chain to ecosystem analysis
- **`references/examples/solid-state-example.md`** — Solid-State Battery: multi-route parallel technology assessment
- **`references/examples/fusion-example.md`** — Nuclear Fusion: pre-commercialization analysis framework

### Assets
- **`assets/scenario-matrix.md`** — 2x2 scenario matrix template for Step 13
- **`assets/analysis-log-template.md`** — Structured analysis log template for persistence
- **`assets/signal-tracker.md`** — Leading indicator signal tracker template

### Outputs (generated by analysis)
- **`outputs/<YYYY-MM-DD>-<industry-slug>.md`** — Analysis reports (one per analysis)
- **`outputs/signal-tracker.md`** — Cross-session leading indicator tracker

---

## Output Format

Structure all deliverables as a **pyramid** (金字塔结构):

```
┌──────────────────────────────────────┐
│   ONE CONCLUSION / THESIS STATEMENT  │  ← Top: actionable judgment
├──────────────────────────────────────┤
│  Argument 1  │  Argument 2 │  Arg 3  │  ← Middle: 3-5 pillars
├──────────────────────────────────────┤
│ Evidence │ Data │ Source │ Analysis  │  ← Bottom: proof
└──────────────────────────────────────┘
```

## Notes

- Prefer Chinese for all output (industry names can stay in English)
- Always cite sources with links when using WebSearch/WebFetch/MCP results
- When uncertain, state assumptions explicitly rather than fabricating data
- For quantitative data (market size, share, revenue), prefer official sources or reputable third-party research
- Run integrity check (`search.py --verify`) before starting analysis to ensure all files are available
- MCP tools enhance data quality for biotech and frontier industries — use them when available, never depend on them
