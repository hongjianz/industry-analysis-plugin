---
name: industry-analysis
description: >
  Implements Wang Yuquan's (王煜全) Industrial Insights Methodology as a
  systematic 18-step SOP for industry analysis. Supports five industry types:
  manufacturing, software, biotech/pharma, energy/cleantech, and frontier technology.
  Three modes: --quick (4-step rapid scan), --full (18-step deep analysis),
  and --compare (cross-industry comparison).
version: 2.0.0
argument-hint: "'[--quick|--full|--compare] <industry-name>'"
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
---

# Industry Analysis SOP (产业洞察SOP)

Systematic industry analysis framework based on Wang Yuquan's methodology. Delivers structured analysis from industry boundary definition through scenario matrix and signal tracking.

## Session Initialization

On session start, verify integrity and check past analysis outputs.

## Mode Selection

| Mode | Flag | Description |
|------|------|-------------|
| Quick scan | `--quick` | 4 steps: boundary → leading indicators → competition → pyramid output |
| Full analysis | `--full` | 18 steps across 4 phases: define → research → predict → reflect |
| Compare | `--compare` | Side-by-side comparison of two industries |

## Industry Types

| Type | Key Characteristics |
|------|-------------------|
| **Manufacturing** | Physical supply chain, production scale |
| **Software** | Platform effects, network moats |
| **Biotech/Pharma** | R&D pipeline, regulatory path, clinical trials |
| **Energy/Cleantech** | Policy-driven, learning curves, project finance |
| **Frontier Technology** | Pre-commercialization, capital-intensive |

## Output Format

All deliverables use the **pyramid structure**:

```
┌──────────────────────────────────────┐
│   ONE CONCLUSION / THESIS STATEMENT  │
├──────────────────────────────────────┤
│  Argument 1  │  Argument 2 │  Arg 3  │
├──────────────────────────────────────┤
│ Evidence │ Data │ Source │ Analysis  │
└──────────────────────────────────────┘
```

## Notes

- Cite all sources with links
- State assumptions explicitly when uncertain
- MCP tools (PubMed, ChEMBL, Consensus, ClinicalTrials.gov) are optional enhancements
- For complete methodology, see `references/SOP-v2.0.md` (Chinese, primary) or `references/english/SOP_en.md`
