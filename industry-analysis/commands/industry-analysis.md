---
name: industry-analysis
description: 产业洞察SOP——基于王煜全方法学的系统性行业分析。支持 --quick（4步快速扫描）和 --full（18步完整分析）两种模式。
argument-hint: "'[--quick|--full] <行业名称>'"
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

Use this command when the user explicitly invokes it. For the full skill instructions that also auto-trigger on keywords, see the skill at `${CLAUDE_PLUGIN_ROOT}/skills/industry-analysis/SKILL.md`.

## Usage

```
/industry-analysis --quick <industry-name>     # Quick scan (4 steps)
/industry-analysis --full <industry-name>      # Full analysis (18 steps)
```

## Examples

```
/industry-analysis --quick 固态电池
/industry-analysis --full AI编程工具
```

The full SOP methodology is in the referenced skill file — load it to begin execution.
