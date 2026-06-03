---
name: industry-analysis
description: >
  This skill should be used when the user asks to "分析行业", "行业洞察", "产业分析",
  "industry analysis", "行业研究", "分析一下 XXX 行业", or uses the /industry-analysis
  command. It implements Wang Yuquan's (王煜全) Industrial Insights Methodology as a
  systematic 18-step SOP validated across manufacturing, software, and frontier technology
  industries. Supports two modes: --quick (4-step rapid scan) and --full (18-step deep analysis).
version: 1.1.0
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
  ]
session-start:
  - "Run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py --verify` to verify all reference files exist"
---

# Industry Analysis SOP / 产业洞察SOP

Systematic industry analysis framework based on Wang Yuquan's Industrial Insights Methodology (产业洞察方法学). Delivers structured analysis from industry boundary definition through scenario matrix and signal tracking.

## Session Initialization

On session start, verify integrity:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py --verify
```

If any files are missing, report them before proceeding. Restore context from `CLAUDE.md` at the project root if available.

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

**Step 4: Pyramid Output**

Synthesize findings into a pyramid-structured report:
- **Top**: One-sentence conclusion (investment/thesis judgment)
- **Middle**: 3-5 key supporting arguments
- **Bottom**: Evidence summary for each argument

---

### Full Mode (18 Steps)

Complete in 3-5 conversation turns. Load `references/SOP-v1.0.md` for the complete methodology.

**Phase A: Define & Frame (Steps 1-4)**
1. Define industry boundary (scope what's in/out)
2. Apply four-dimension evaluation
3. Build logic tree with hypotheses
4. Design data collection plan

**Phase B: Research & Analyze (Steps 5-10)**
5. Multi-source data collection — use `scripts/search.py` to generate a search strategy
6. Identify leading indicators (超前指标)
7. Analyze supply/ecosystem chain — peel to upstream scarcity control points
8. Select analytical model (Porter's Five Forces / Value Chain / Platform Ecosystem / etc.)
9. Build pyramid structure
10. Validate each hypothesis against collected data

**Phase C: Predict & Conclude (Steps 11-15)**
11. Identify 2-4 key variables shaping the industry's future
12. Build 2x2 scenario matrix — use `assets/scenario-matrix.md` as template
13. Assign probabilities and identify signals for each scenario
14. Formulate actionable thesis
15. Document key risks and assumptions

**Phase D: Reflect (Steps 16-18)**
16. Review what worked and what didn't in this analysis
17. Update leading indicator tracker
18. Identify next review trigger (time-based or event-based)

---

## Multi-Source Search Strategy

Run the search script to generate tailored search queries:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py "<industry>" <manufacturing|software|frontier>
```

Example:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/scripts/search.py "solid state battery" manufacturing
```

Use WebSearch for each query and WebFetch for the most promising results.

---

## MCP-Enhanced Data Collection (Optional)

> **Note:** This is a placeholder for Phase 2 MCP integration. When bio-research MCP servers are available:
> - **Medical/Pharma/Biotech**: Use ClinicalTrials.gov for trial pipeline, ChEMBL for drug mechanisms, PubMed for literature
> - **Frontier Tech**: Use Consensus for technology readiness, PubMed for research papers
> - **Manufacturing/Software**: WebSearch remains primary; MCP is supplementary
>
> MCP tools are optional — the SOP works with WebSearch alone when servers are unavailable.

---

## Reference Files

### Core Methodology
- **`references/SOP-v1.0.md`** — Complete 18-step SOP with detailed instructions for each step

### Industry Templates
- **`references/templates/manufacturing.md`** — Manufacturing-specific analysis template (supply chain, raw materials, production scale)
- **`references/templates/software.md`** — Software-specific template (platform effects, network moats, ecosystem)
- **`references/templates/frontier.md`** — Frontier tech template (tech roadmap uncertainty, capital intensity, policy drivers)

### Examples (Validated Case Studies)
- **`references/examples/cgm-example.md`** — CGM case: supply chain scarcity determines pricing power
- **`references/examples/ai-coding-example.md`** — AI Coding Tools: from supply chain to ecosystem analysis
- **`references/examples/solid-state-example.md`** — Solid-State Battery: multi-route parallel technology assessment
- **`references/examples/fusion-example.md`** — Nuclear Fusion: pre-commercialization analysis framework

### Assets
- **`assets/scenario-matrix.md`** — 2x2 scenario matrix template for Step 13

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
- Always cite sources with links when using WebSearch/WebFetch results
- When uncertain, state assumptions explicitly rather than fabricating data
- For quantitative data (market size, share, revenue), prefer official sources or reputable third-party research
- Run integrity check (`search.py --verify`) before starting analysis to ensure all files are available
