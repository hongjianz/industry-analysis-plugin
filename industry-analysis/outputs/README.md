# Analysis Outputs / 分析输出目录

此目录存放每次行业分析的分析报告和信号追踪数据。

## 文件说明

| 文件 | 说明 |
|------|------|
| `<YYYY-MM-DD>-<industry-slug>.md` | 单次行业分析完整报告，按日期 + 行业名称命名 |
| `signal-tracker.md` | 跨 session 超前指标信号追踪器，持续追加更新 |

## 输出规范

- 每次分析完成后自动写入日志文件
- 分析报告使用 `analysis-log-template.md` 模板
- 信号追踪追加到 `signal-tracker.md`
- 通过 CLAUDE.md 恢复上次分析的上下文
