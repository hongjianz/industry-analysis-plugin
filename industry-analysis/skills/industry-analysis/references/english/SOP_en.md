# SOP v2.0 Reference (English)

> English summary of the 18-step Industry Analysis SOP.
> For the complete Chinese version, see `references/SOP-v1.0.md`.

---

## 18-Step Flow

```
① Define industry boundary (scope + product definition)
② Classify industry type (→ route to corresponding template)
③ Technology roadmap analysis (single route → S-curve; multi-route → parallel matrix)
④ Four-dimension evaluation (technology / market / chain / competition)
⑤ Logic tree decomposition + initial hypotheses
⑥ Multi-source data collection + cross-validation
   ⑥a. WebSearch/WebFetch (all industries)
   ⑥b. MCP-enhanced collection (optional, see Step 5b)
⑦ Leading indicator identification
⑧ Model selection (PEST / Four Quadrants / Comparative / Co-opetition / etc.)
⑨ Supply/ecosystem chain deep dive (per industry template)
⑩ Geopolitical analysis (for policy-sensitive industries)
⑪ Market size estimation (commercialized: TAM/SAM/SOM; pre-commercial: scenario-based)
⑫ Pyramid structure output (conclusion first)
⑬ Hypothesis validation (actively seek counter-evidence)
⑭ Key variable identification (path divergence + uncertainty + time window)
⑮ Scenario planning (2×2 matrix + probability weighting)
⑯ Signal definition + reflection & iteration
⑯.5 Archive to analysis log + update signal tracker (persistence)
⑰ Shovel seller analysis (frontier tech only)
⑱ Open source / community analysis (software only)
```

## Four-Dimension Evaluation

| Dimension | Key Questions |
|-----------|--------------|
| **Technology Maturity** | S-curve position? Multiple competing routes? |
| **Market Stage** | Growth rate? Adoption curve? TAM? |
| **Industry Chain Completeness** | Bottlenecks? Scarcity control points? |
| **Competitive Pattern** | Concentration? Moats? Entry barriers? |

## Leading Indicators by Industry Type

| Type | Lagging Indicators | Leading Indicators |
|------|-------------------|-------------------|
| Manufacturing | Earnings, market share | Raw material shipments, partnerships, regulatory changes |
| Software | User count, quarterly revenue | Benchmark scores, developer community growth, BYOK adoption |
| Biotech | Drug sales | Trial phase progression (Phase II→III), data readouts, patent challenges |
| Energy | Installed capacity, generation | LCOE decline curve, learning rate slope, policy roadmap, PPA volume |
| Frontier Tech | None | Technology milestone validation, capital inflow, policy roadmap |

## Scarcity Control Points

- **Manufacturing**: Raw materials / core process / brand
- **Software**: Model capability / workflow lock-in / data flywheel
- **Biotech**: Target exclusivity / patent壁垒 / clinical data ownership
- **Energy**: Critical materials / grid access / project permitting
- **Frontier**: Capital-talent-policy triangle

## MCP-Enhanced Data Collection

| MCP Tool | Best Use | Industries |
|----------|---------|------------|
| ClinicalTrials.gov | Trial pipeline analysis | Biotech, MedTech |
| ChEMBL | Drug mechanism & target analysis | Biotech, Pharma |
| PubMed | Biomedical literature | Biotech, Frontier, MedTech |
| Consensus | Academic synthesis | Frontier, Biotech |

All MCP tools are optional. The SOP works with WebSearch alone.

## Persistence

After each analysis:
1. Fill `assets/analysis-log-template.md` → write to `outputs/<YYYY-MM-DD>-<industry>.md`
2. Update `outputs/signal-tracker.md` with leading indicator status

## Key Principles

- **Pyramid output**: Conclusion first, arguments second, evidence third
- **Multi-source cross-validation**: Never rely on a single data source
- **Leading over lagging**: Focus on forward signals, not historical data
- **Scarcity determines profit**: Find who controls the irreplaceable node
- **Scenario over prediction**: Multiple futures with probability weights
- **Reflect and iterate**: Every analysis improves the next
