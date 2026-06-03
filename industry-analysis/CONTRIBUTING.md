# 贡献指南

感谢你有兴趣为产业洞察 SOP 插件贡献力量！本文档说明如何贡献新的行业模板、案例研究、翻译和改进建议。

---

## 目录

- [贡献方式](#贡献方式)
- [开发环境](#开发环境)
- [贡献模板](#贡献模板)
- [贡献案例](#贡献案例)
- [贡献翻译](#贡献翻译)
- [提交 PR 流程](#提交-pr-流程)
- [代码规范](#代码规范)

---

## 贡献方式

| 贡献类型 | 难度 | 说明 |
|---------|------|------|
| 🆕 **新行业模板** | 高 | 新增一个行业类型及完整模板 |
| 📋 **验证案例** | 中 | 使用 SOP 分析一个真实行业并记录 |
| 🌐 **翻译** | 中 | 将核心文件翻译为英文 |
| 🐛 **Bug 修复** | 低 | 修复搜索脚本或文档错误 |
| 💡 **改进建议** | 低 | 在 Issues 中提出方法学改进 |

---

## 开发环境

1. 将该插件安装到 Claude Code 中（见 [README](README.md) 安装说明）
2. 运行完整性检查：`python3 skills/industry-analysis/scripts/search.py --verify`
3. 熟悉现有模板结构（见 `references/templates/` 目录）

---

## 贡献模板

创建新行业模板前，请先阅读 `references/templates/TEMPLATE-GUIDE.md`。

### 步骤

1. 在 `references/templates/` 下创建 `<行业名>.md`
2. 确保包含模板指南中列出的所有必需章节
3. 在 `SKILL.md` 的 Step 0 行业分类表中添加新类型
4. 在 `scripts/search.py` 中添加该行业类型的搜索查询
5. 更新 `SOP-v1.0.md` 的完整性清单
6. 运行 `python3 scripts/search.py --verify` 确认完整性
7. 使用 `--quick` 模式实际分析一个该行业，验证模板有效性

---

## 贡献案例

案例用于验证 SOP 在不同行业的有效性：

1. 使用 SOP 快速或完整模式分析一个真实行业
2. 按案例模板记录过程和发现（参考现有案例）
3. 提交到 `references/examples/` 目录

案例文件结构：

```markdown
# [行业名] — 产业洞察分析案例

**行业：** [名称]
**类型：** [制造/软件/生物医药/前沿/能源]
**分析日期：** [YYYY-MM-DD]
**使用模式：** [quick/full]

## 核心结论
一句话判断。

## 关键发现
1. ...
2. ...

## 最有价值的SOP步骤
- [步骤号]：[说明]

## 改进建议
- SOP 在此行业中的不足之处
```

---

## 贡献翻译

1. 核心英文文件放在 `references/english/` 目录
2. 命名规则：原文件 `SKILL.md` → 英文版 `SKILL_en.md`
3. SOP 方法学术语尽量保留中文拼音或直译 + 英文注释

核心翻译优先级：
1. `SKILL.md` — 技能说明（最高优先级）
2. `SOP-v1.0.md` — 方法论参考
3. 行业模板

---

## 提交 PR 流程

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feat/your-feature`
3. 提交变更：`git commit -m "description of changes"`
4. 推送到你的 Fork：`git push origin feat/your-feature`
5. 创建 Pull Request

### PR 检查清单

- [ ] 完整性检查通过：`search.py --verify`
- [ ] 如果有新模板，已在 SKILL.md 中添加行业类型
- [ ] 如果有新模板，已在 search.py 中添加搜索查询
- [ ] 更新了 SOP 完整性清单
- [ ] 所有文件使用中文（英文翻译除外）
- [ ] 没有破坏现有功能

---

## 代码规范

- **语言**：模板和案例使用中文（行业名称可保留英文）
- **链接**：所有外部引用标注来源链接
- **格式**：Markdown 文件，保持 80 字符宽度
- **数据**：不确定时明确标注假设条件，不编造数据
- **MCP**：所有 MCP 工具声明为可选，确保 SOP 在没有 MCP 时完整可用

---

## 问题与讨论

- 在 [GitHub Issues](https://github.com/hongjianz/industry-analysis-plugin/issues) 提交问题
- 方法学讨论建议提供具体行业案例作为上下文
