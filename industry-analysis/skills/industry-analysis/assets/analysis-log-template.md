# Analysis Log 模板

> 每次完成行业分析后，将分析摘要写入 `outputs/` 目录。
> 文件命名：`<YYYY-MM-DD>-<industry-slug>.md`

---

## 元数据

- **日期：** `{{ date }}`
- **行业：** `{{ industry }}`
- **行业类型：** `{{ industry_type }}`（manufacturing / software / biotech / frontier）
- **分析模式：** `{{ mode }}`（quick / full）
- **关键词：** `{{ keywords }}`

---

## 核心结论（一句话）

```
{{ one-sentence conclusion }}
```

## 关键论据（3-5 条）

| # | 论据 | 支撑证据摘要 | 证据来源 |
|---|------|------------|---------|
| 1 | {{ argument_1 }} | {{ evidence_1 }} | {{ source_1 }} |
| 2 | {{ argument_2 }} | {{ evidence_2 }} | {{ source_2 }} |
| 3 | {{ argument_3 }} | {{ evidence_3 }} | {{ source_3 }} |

## 市场/技术状态

- **技术成熟度：** {{ technology_maturity }}
- **市场阶段：** {{ market_stage }}
- **竞争格局：** {{ competitive_pattern }}
- **产业链完整性：** {{ chain_completeness }}

## 超前指标识别

| 指标 | 数据来源 | 更新节奏 | 当前信号 | 信号方向 |
|------|---------|---------|---------|---------|
| {{ indicator_1 }} | {{ source_1 }} | {{ cadence_1 }} | {{ signal_1 }} | 🟢🔴🟡 |
| {{ indicator_2 }} | {{ source_2 }} | {{ cadence_2 }} | {{ signal_2 }} | 🟢🔴🟡 |
| {{ indicator_3 }} | {{ source_3 }} | {{ cadence_3 }} | {{ signal_3 }} | 🟢🔴🟡 |

## 关键变量（用于场景推演）

| 变量 | 不确定性 | 路径分叉 | 时间窗口 |
|------|---------|---------|---------|
| {{ variable_1 }} | 高/中/低 | {{ fork_1 }} | {{ window_1 }} |
| {{ variable_2 }} | 高/中/低 | {{ fork_2 }} | {{ window_2 }} |

## 2×2 情景矩阵摘要

```
                        变量B高
                           │
        情景2：             │       情景1：
    {{ scenario_2 }}        │   {{ scenario_1 }}
       概率：X%             │      概率：X%
                           │
  ─────────────────────────┼─────────────────── 变量A
                           │
        情景3：             │       情景4：
    {{ scenario_3 }}        │   {{ scenario_4 }}
       概率：X%             │      概率：X%
                           │
                        变量B低
```

## 风险评估

| 风险 | 可能性 | 影响 | 缓释措施 |
|------|-------|------|---------|
| {{ risk_1 }} | 高/中/低 | 高/中/低 | {{ mitigation_1 }} |
| {{ risk_2 }} | 高/中/低 | 高/中/低 | {{ mitigation_2 }} |

## 下次复查

- **复查触发条件：** {{ review_trigger }}
- **建议复查日期：** {{ review_date }}
- **需重点关注的信号：** {{ focus_signals }}

---

## 反思（SOP Step 16）

- **本次分析最有价值的发现：**
  {{ most_valuable_finding }}

- **本次分析的不足：**
  {{ limitations }}

- **下次可以改进的地方：**
  {{ improvements }}

---

> 此模板由产业洞察 SOP 自动生成。update 记录见 `signal-tracker.md`。
