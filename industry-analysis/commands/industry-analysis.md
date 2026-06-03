---
name: industry-analysis
description: 产业洞察SOP——基于王煜全方法学的系统性行业分析。支持 --quick（4步快速扫描）、--full（18步完整分析）--compare（双行业对比）和 --with-shiso（卡点分析增强）四种模式。覆盖制造业、软件、生物医药、能源、前沿技术五类行业。
argument-hint: "'[--quick|--full|--compare] <行业名称>'"
allowed-tools:
  [
    "WebSearch",
    "WebFetch",
    "Bash",
    "Read",
    "Write",
  ]
---

# Industry Analysis / 产业洞察 SOP

Use this command when the user explicitly invokes it. For the full skill instructions (including auto-trigger behavior), see the skill at `${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/SKILL.md`.

## Usage

```
/industry-analysis --quick <industry-name>                # Quick scan (4 steps)
/industry-analysis --full <industry-name>                 # Full analysis (18 steps)
/industry-analysis --compare "Industry A" "Industry B"          # Side-by-side comparison
/industry-analysis --quick --with-shiso <industry-name>         # Quick scan + chokepoint analysis
/industry-analysis --full --with-shiso <industry-name>          # Full analysis + chokepoint analysis
```

## Supported Industry Types

| Type | Description | Template |
|------|-------------|----------|
| **Manufacturing** | Physical products, supply chain, production scale | `templates/manufacturing.md` |
| **Software** | Code/data-driven, platform effects, SaaS | `templates/software.md` |
| **Biotech/Pharma** | R&D pipeline-driven, regulatory path, clinical trials | `templates/biotech.md` |
| **Frontier** | Pre-commercialization, capital-intensive | `templates/frontier.md` |

## MCP Enhanced Data Collection

When bio-research MCP servers are available, the SOP can use ClinicalTrials.gov (trial pipeline), ChEMBL (drug mechanisms), PubMed (literature), and Consensus (academic synthesis) for enhanced data quality in biotech and frontier analyses.

## Comparison Mode

The `--compare` flag runs Quick Mode on two industries sequentially, then compares them across all SOP dimensions using the comparison matrix template.

### Examples

```
/industry-analysis --quick 固态电池
/industry-analysis --full AI编程工具
/industry-analysis --compare "CGM" "智能手表健康监测"    ← 两个相近行业对比
/industry-analysis --compare "EV battery" "hydrogen fuel cell"  ← 替代技术对比
```

The full SOP methodology is in the referenced skill file — load it to begin execution.
