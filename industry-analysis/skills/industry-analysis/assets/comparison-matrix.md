# Cross-Industry Comparison Matrix / 跨行业对比矩阵

> 当用户使用 `--compare` 模式时加载此模板。
> 用法：`/industry-analysis --compare "Industry A" "Industry B"`

---

## 元数据

- **行业 A：** `{{ industry_a }}`（类型：{{ type_a }}）
- **行业 B：** `{{ industry_b }}`（类型：{{ type_b }}）
- **对比日期：** `{{ date }}`
- **对比目的：** `{{ purpose }}`（投资选择 / 职业方向 / 技术替代评估 / 其他）

---

## 核心结论

```
{{ Which industry has the stronger thesis and why }}
```

---

## 行业基础对比

| 维度 | 行业 A | 行业 B |
|------|--------|--------|
| **行业类型** | {{ type_a }} | {{ type_b }} |
| **一句话定义** | {{ definition_a }} | {{ definition_b }} |
| **技术成熟度** | {{ tech_maturity_a }} | {{ tech_maturity_b }} |
| **市场阶段** | {{ market_stage_a }} | {{ market_stage_b }} |
| **地缘因素** | {{ geopolitical_a }} | {{ geopolitical_b }} |

---

## 产业链 / 生态对比

| 维度 | 行业 A | 行业 B |
|------|--------|--------|
| **核心价值链** | {{ value_chain_a }} | {{ value_chain_b }} |
| **稀缺控制点** | {{ scarcity_a }} | {{ scarcity_b }} |
| **主要玩家** | {{ players_a }} | {{ players_b }} |
| **进入壁垒** | {{ barriers_a }} | {{ barriers_b }} |

---

## 超前指标对比

| 指标类别 | 行业 A | 行业 B |
|---------|--------|--------|
| **技术信号** | {{ tech_signal_a }} | {{ tech_signal_b }} |
| **市场信号** | {{ market_signal_a }} | {{ market_signal_b }} |
| **政策信号** | {{ policy_signal_a }} | {{ policy_signal_b }} |
| **资本信号** | {{ capital_signal_a }} | {{ capital_signal_b }} |

**综合信号强度：** 行业 A `🟢🔴🟡` vs 行业 B `🟢🔴🟡`

---

## 关键变量 + 不确定因素

| 变量 | 对 A 的影响 | 对 B 的影响 | 不确定性 |
|------|-----------|-----------|---------|
| {{ variable_1 }} | {{ impact_a_1 }} | {{ impact_b_1 }} | 高/中/低 |
| {{ variable_2 }} | {{ impact_a_2 }} | {{ impact_b_2 }} | 高/中/低 |
| {{ variable_3 }} | {{ impact_a_3 }} | {{ impact_b_3 }} | 高/中/低 |

---

## 跨行业关联分析

- **玩家重叠：** {{ overlap }}（同一批公司在两个行业都出现？）
- **价值链关联：** {{ value_chain_link }}（A 的产出是否成为 B 的投入？）
- **替代风险：** {{ substitution_risk }}（一个行业的技术会让另一个过时吗？）
- **协同效应：** {{ synergy }}（两个行业的发展是否互相促进？）

---

## 风险评估

| 风险类型 | 行业 A | 行业 B |
|---------|--------|--------|
| **技术风险** | {{ tech_risk_a }} | {{ tech_risk_b }} |
| **市场风险** | {{ market_risk_a }} | {{ market_risk_b }} |
| **政策风险** | {{ policy_risk_a }} | {{ policy_risk_b }} |
| **竞争风险** | {{ comp_risk_a }} | {{ comp_risk_b }} |

---

## 推荐判断

```
推荐方向：偏向行业 [A/B]

核心理由：
1. {{ reason_1 }}
2. {{ reason_2 }}
3. {{ reason_3 }}

条件性判断：
- 如果 [条件X] 发生 → 可能转向行业 [A/B]
- 如果 [条件Y] 发生 → 两个行业的相对吸引力变化

建议跟踪信号：
- {{ watch_signal_1 }}
- {{ watch_signal_2 }}
```

---

> 此矩阵由 `--compare` 模式自动生成。两个行业各自的分析日志见 `outputs/` 目录。
