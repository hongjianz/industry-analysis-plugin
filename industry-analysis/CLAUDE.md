# Industry Analysis Plugin / 产业洞察SOP

基于王煜全《学会洞察行业》方法学的系统性行业分析框架。验证于4个行业（CGM、AI编程工具、固态电池、核聚变）。

## Key Files / 关键文件

| Purpose | Path |
|---------|------|
| 插件清单 | `.claude-plugin/plugin.json` |
| 项目设置 | `.claude/settings.json` |
| 命令入口 | `commands/industry-analysis.md` |
| 核心技能 | `skills/industry-analysis/SKILL.md` |
| 完整SOP | `skills/industry-analysis/references/SOP-v1.0.md` |
| 搜索策略 | `skills/industry-analysis/scripts/search.py` |

## 行业模板

- 制造业: `skills/industry-analysis/references/templates/manufacturing.md`
- 软件: `skills/industry-analysis/references/templates/software.md`
- 前沿技术: `skills/industry-analysis/references/templates/frontier.md`

## 核心SOP流程（快速参考）

```
Step 0: 行业类型分类 → 加载对应模板
--quick (4步): 边界判断 → 超前指标 → 竞争格局 → 金字塔输出
--full (18步): 定义框架(A) → 研究分析(B) → 预测结论(C) → 反思迭代(D)
```

## 输出规范

- 所有输出使用中文（行业名称可保留英文）
- 结论先行金字塔结构
- 所有数据必须标注来源链接
- 不确定时明确标注假设条件
