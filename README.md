# Industry Analysis SOP Plugin

> 产业洞察SOP v1.0 — A Claude Code plugin for systematic industry analysis based on Wang Yuquan's (王煜全) methodology.

## Features

- **Two analysis modes**: `--quick` (4-step rapid scan) and `--full` (18-step deep analysis)
- **Three industry templates**: Manufacturing (制造业), Software (软件业), Frontier Technology (前沿技术)
- **Validated across 4 industries**: CGM, AI Coding Tools, Solid-State Battery, Nuclear Fusion
- **Multi-source research automation**: Search strategy generator included

## Installation

Copy to your Claude Code project's plugin directory:

```bash
cp -r industry-analysis-plugin /path/to/your-project/.claude-plugin/plugins/
```

Or install via project-level `.claude-plugin/`:

```bash
ln -s /path/to/industry-analysis-plugin /path/to/your-project/.claude-plugin/plugins/industry-analysis
```

Then run `/reload-plugins` in Claude Code.

## Usage

### Auto-trigger

Simply ask Claude:
> 帮我分析一下固态电池行业
> 用产业洞察框架分析CGM行业
> 做个新能源汽车产业的快速扫描

### Slash command

```
/industry-analysis --quick <行业名称>
/industry-analysis --full <行业名称>
```

### Examples

```
/industry-analysis --quick 固态电池
/industry-analysis --full AI编程工具
```

## Structure

```
industry-analysis-plugin/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── commands/
│   └── industry-analysis.md     # Slash command entry
└── skills/
    └── industry-analysis/
        ├── SKILL.md             # Core instructions
        ├── references/
        │   ├── SOP-v1.0.md     # Full 18-step SOP
        │   ├── templates/      # 3 industry templates
        │   └── examples/       # 4 case studies
        ├── scripts/
        │   └── search.py       # Search strategy generator
        └── assets/
            └── scenario-matrix.md  # Scenario matrix template
```

## Methodology

Based on Wang Yuquan's **Industrial Insights Methodology** (产业洞察方法学):
- Leading indicators vs lagging indicators
- Supply chain scarcity analysis (剥洋葱到产业链上游)
- Four-step prediction method (scenario building + signal tracking)
- Pyramid structure output

## License

MIT
