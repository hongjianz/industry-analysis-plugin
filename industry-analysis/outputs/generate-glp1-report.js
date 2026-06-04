const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat,
  HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak
} = require("docx");

// ── Color palette ──────────────────────────────────────
const C = {
  primary: "1F4E79",    // Dark blue (headings, accents)
  accent: "2E75B6",     // Medium blue (subheadings, borders)
  light: "D5E8F0",      // Light blue (table header bg)
  highlight: "E8F0FE",  // Very light blue (alternate rows)
  body: "333333",       // Body text
  muted: "666666",      // Secondary text
  white: "FFFFFF",
};

// ── Shared helpers ─────────────────────────────────────
const border = { style: BorderStyle.SINGLE, size: 1, color: "BFBFBF" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0 };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

const cellMargins = { top: 60, bottom: 60, left: 100, right: 100 };

function headerCell(text, width) {
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    shading: { fill: C.primary, type: ShadingType.CLEAR },
    margins: cellMargins,
    verticalAlign: "center",
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 40, after: 40 },
      children: [new TextRun({ text, bold: true, font: "Arial", size: 20, color: C.white })]
    })]
  });
}

function dataCell(text, width, opts = {}) {
  const { bold, color, align, shading } = opts;
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    shading: shading ? { fill: shading, type: ShadingType.CLEAR } : undefined,
    margins: cellMargins,
    children: [new Paragraph({
      alignment: align || AlignmentType.LEFT,
      spacing: { before: 30, after: 30 },
      children: [new TextRun({
        text: String(text), font: "Arial", size: 20, color: color || C.body,
        bold: bold || false,
      })]
    })]
  });
}

function sectionHeading(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 200 },
    children: [new TextRun({
      text, font: "Arial", size: 32, bold: true, color: C.primary
    })]
  });
}

function subHeading(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 160 },
    children: [new TextRun({
      text, font: "Arial", size: 26, bold: true, color: C.accent
    })]
  });
}

function bodyText(text, opts = {}) {
  const { bold, color, spacing } = opts;
  return new Paragraph({
    spacing: { before: spacing?.before || 60, after: spacing?.after || 120 },
    children: [new TextRun({
      text, font: "Arial", size: 22, color: color || C.body, bold: bold || false,
    })]
  });
}

function bulletItem(text, level = 0) {
  return new Paragraph({
    numbering: { reference: "bullets", level },
    spacing: { before: 40, after: 40 },
    children: [new TextRun({ text, font: "Arial", size: 22, color: C.body })]
  });
}

function highlightBox(text) {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    shading: { fill: C.highlight, type: ShadingType.CLEAR },
    children: [new TextRun({
      text, font: "Arial", size: 22, bold: true, color: C.primary, italics: true,
    })]
  });
}

// ── Table widths (A4 content = 9026 DXA) ──────────────
const T = 9026;

// ── BUILD DOCUMENT ────────────────────────────────────
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: C.primary },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: C.accent },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
    ]
  },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
    }]
  },
  sections: [
    // ═══════════ COVER PAGE ═══════════
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 }, // A4
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      children: [
        new Paragraph({ spacing: { before: 3000 }, children: [] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 200 },
          children: [new TextRun({
            text: "GLP-1 受体激动剂",
            font: "Arial", size: 52, bold: true, color: C.primary,
          })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 100 },
          children: [new TextRun({
            text: "行业深度分析报告",
            font: "Arial", size: 44, bold: true, color: C.accent,
          })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          border: {
            bottom: { style: BorderStyle.SINGLE, size: 6, color: C.accent, space: 12 }
          },
          spacing: { after: 600 },
          children: [],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 200 },
          children: [new TextRun({
            text: "Industry Analysis Report",
            font: "Arial", size: 28, color: C.muted, italics: true,
          })]
        }),
        new Paragraph({ spacing: { before: 600 }, children: [] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 80 },
          children: [new TextRun({ text: "分析模式", font: "Arial", size: 22, color: C.muted })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 120 },
          children: [new TextRun({
            text: "完整 18 步 SOP + 紫苏叶卡点分析 (Shiso) + MCP 数据增强",
            font: "Arial", size: 22, color: C.body, bold: true,
          })]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 80 },
          children: [new TextRun({ text: "基于王煜全《学会洞察行业》方法学体系", font: "Arial", size: 22, color: C.muted })],
        }),
        new Paragraph({ spacing: { before: 600 }, children: [] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 80 },
          children: [
            new TextRun({ text: "分析日期：", font: "Arial", size: 22, color: C.muted }),
            new TextRun({ text: "2026 年 6 月 3 日", font: "Arial", size: 22, color: C.body, bold: true }),
          ]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 80 },
          children: [
            new TextRun({ text: "行业类型：", font: "Arial", size: 22, color: C.muted }),
            new TextRun({ text: "生物医药 / 制药 (Biotech / Pharmaceuticals)", font: "Arial", size: 22, color: C.body, bold: true }),
          ]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "关键词：", font: "Arial", size: 22, color: C.muted }),
            new TextRun({ text: "GLP-1 | 司美格鲁肽 | 替尔泊肽 | orforglipron | CagriSema | 肥胖 | 糖尿病 | 双寡头 | 专利悬崖", font: "Arial", size: 22, color: C.body, bold: true }),
          ]
        }),
      ]
    },

    // ═══════════ MAIN CONTENT ═══════════
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.accent, space: 4 } },
            children: [new TextRun({
              text: "GLP-1 行业深度分析 | 机密",
              font: "Arial", size: 16, color: C.muted, italics: true,
            })]
          })]
        })
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            border: { top: { style: BorderStyle.SINGLE, size: 4, color: C.accent, space: 4 } },
            children: [
              new TextRun({ text: "第 ", font: "Arial", size: 16, color: C.muted }),
              new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: C.muted }),
              new TextRun({ text: " 页", font: "Arial", size: 16, color: C.muted }),
            ]
          })]
        })
      },
      children: [

        // ── 1. 核心结论 ──
        sectionHeading("1. 核心结论"),
        highlightBox(
          "GLP-1 是全球制药史上最大的药物市场（2025年约$750亿→2030年$1,300-2,000亿），" +
          "双寡头格局短期稳固，口服小分子（orforglipron）正在改写中远期规则，中国仿制药黎明因数据保护延迟至2027年。"
        ),

        // ── 2. 关键论据 ──
        sectionHeading("2. 关键论据"),
        new Table({
          width: { size: T, type: WidthType.DXA },
          columnWidths: [400, 3200, 3626, 1800],
          rows: [
            new TableRow({
              children: [
                headerCell("#", 400),
                headerCell("论据", 3200),
                headerCell("支撑证据摘要", 3626),
                headerCell("证据来源", 1800),
              ]
            }),
            ...[
              ["1", "市场规模史无前例", "2025 ~$750亿, 2030 $1,300-2,000亿；替尔泊肽$365亿 + 司美格鲁肽$330亿 = 2025已接近峰值药2-3倍", "Evaluate, Grand View, TrimRX"],
              ["2", "Lilly 首次超越 Novo，口服小分子开启新战场", "Tirzepatide $365亿 > Semaglutide $330亿 (2025); Orforglipron 2026.4 FDA获批", "JPM26, PatSnap, Pharmacy Times"],
              ["3", "中国专利悬崖已至但仿制药推迟", "司美格鲁肽CN专利2026.3到期；10+家申请0家获批；数据保护2027.4到期；Novo主动降价47%", "phirda, 网易, 新浪财经"],
              ["4", "fill/finish 制剂产能是最硬卡点", "Novo收购Catalent $165亿已验证；2024短缺→2026平衡", "Outsourced Pharma, Drug Delivery Leader"],
            ].map((row, i) => new TableRow({
              children: [
                dataCell(row[0], 400, { align: AlignmentType.CENTER, bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[1], 3200, { bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[2], 3626, { shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[3], 1800, { color: C.muted, shading: i % 2 === 0 ? C.highlight : undefined }),
              ]
            }))
          ]
        }),

        // ── 3. 市场与技术状态 ──
        sectionHeading("3. 市场与技术状态"),
        subHeading("技术成熟度"),
        bulletItem("注射肽：成熟期（第2代），已广泛商业化"),
        bulletItem("口服小分子：引入期（orforglipron 2026.4获批）"),
        bulletItem("多靶点组合：探索期（retatrutide Phase 3, amycretin Phase 1/2）"),

        subHeading("市场阶段"),
        bulletItem("爆发增长期。糖尿病适应症成熟，肥胖爆发（2025-2030 CAGR ~17%）"),
        bulletItem("MASH/CVD/睡眠呼吸暂停等新适应症正在打开"),

        subHeading("竞争格局"),
        bulletItem("Novo Nordisk vs Eli Lilly 双寡头（>95% 市场份额）"),
        bulletItem("信达（玛仕度肽）等中国创新药边缘竞争"),
        bulletItem("10+中国仿制药候审"),

        subHeading("产业链完整性"),
        bulletItem("上游API：多源（Bachem + 中国企业）"),
        bulletItem("中游fill/finish：结构性瓶颈（Catalent收购）"),
        bulletItem("下游渠道/医保：逐步打开"),

        // ── 4. 紫苏叶卡点排序 ──
        sectionHeading("4. 紫苏叶卡点排序"),
        bodyText("基于 Shiso Chokepoint Analysis 模块对各卡点的稀缺性与控制力进行量化排序："),
        new Paragraph({ spacing: { before: 120 }, children: [] }),
        new Table({
          width: { size: T, type: WidthType.DXA },
          columnWidths: [700, 3400, 1000, 2226, 1700],
          rows: [
            new TableRow({
              children: [
                headerCell("排名", 700),
                headerCell("卡点", 3400),
                headerCell("类型", 1000),
                headerCell("持有方", 2226),
                headerCell("诚实分", 1700),
              ]
            }),
            ...[
              ["🥇 第1", "fill/finish 无菌制剂产能", "制造", "Novo（Catalent收购）/ Lilly自建", "🟢 8/10"],
              ["🥈 第2", "SELECT CVOT 临床数据壁垒", "制度", "Novo Nordisk（17,000人, MACE↓20%）", "🟡 7/10"],
              ["🥉 第3", "专利+数据保护双重墙（中国）", "制度", "Novo（CN专利+中瑞自贸协定）", "🟡 7/10"],
              ["4", "SPPS 合成产率天花板", "化学", "行业结构性（45-65%粗品纯度）", "🟡 6/10"],
            ].map((row, i) => new TableRow({
              children: [
                dataCell(row[0], 700, { align: AlignmentType.CENTER, bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[1], 3400, { bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[2], 1000, { align: AlignmentType.CENTER, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[3], 2226, { shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[4], 1700, { align: AlignmentType.CENTER, bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
              ]
            }))
          ]
        }),

        // ── 5. 第一性原理 Ground Truth ──
        sectionHeading("5. 第一性原理 Ground Truth"),
        new Table({
          width: { size: T, type: WidthType.DXA },
          columnWidths: [700, 1200, 2626, 4500],
          rows: [
            new TableRow({
              children: [
                headerCell("编号", 700),
                headerCell("学科", 1200),
                headerCell("核心约束", 2626),
                headerCell("对行业的影响", 4500),
              ]
            }),
            ...[
              ["GT-1", "🌍 物理", "肽类药物分子量>4kDa，无法口服吸收", "注射剂主导→口服小分子（orforglipron）才是真突破"],
              ["GT-2", "⚗️ 化学", "SPPS 每步~99%，30步后粗品纯度仅45-65%", "产能扩张受限于化学反应动力学而非投资"],
              ["GT-3", "🧬 生物", "GLP-1 半衰期1-2分钟，需脂肪酸侧链延长", "决定了每周一次而非每天一次的给药频率"],
              ["GT-4", "🏛️ 制度", "SELECT 数据不可复制+中瑞数据保护", "即使专利到期，仿制药也无法立即引用临床数据"],
              ["GT-5", "💰 经济", "生产成本每降10倍，可及市场扩大10倍", "口服小分子的经济革命 > 技术革命"],
            ].map((row, i) => new TableRow({
              children: [
                dataCell(row[0], 700, { align: AlignmentType.CENTER, bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[1], 1200, { align: AlignmentType.CENTER, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[2], 2626, { shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[3], 4500, { shading: i % 2 === 0 ? C.highlight : undefined }),
              ]
            }))
          ]
        }),

        // ── 6. 超前指标识别 ──
        sectionHeading("6. 超前指标识别"),
        bodyText("以下指标需要持续追踪，以验证或修正分析结论："),
        new Paragraph({ spacing: { before: 120 }, children: [] }),
        new Table({
          width: { size: T, type: WidthType.DXA },
          columnWidths: [2400, 1500, 1100, 2626, 1400],
          rows: [
            new TableRow({
              children: [
                headerCell("指标", 2400),
                headerCell("数据来源", 1500),
                headerCell("更新节奏", 1100),
                headerCell("当前信号", 2626),
                headerCell("信号方向", 1400),
              ]
            }),
            ...[
              ["orforglipron 处方增速", "Lilly IR, IQVIA", "季度", "2026.4获批，华尔街估$15-28亿首年", "📈 口服革命启动"],
              ["CagriSema FDA决定", "FDA审评日历", "月度", "2026年底预期；22.7%减重", "🟡 待定"],
              ["Lilly vs Novo份额", "两司财报", "季度", "Tirzepatide $365亿 > Semaglutide $330亿", "📈 Lilly超越"],
              ["中国司美格鲁肽类似药获批", "NMPA", "月度", "0家获批（2026.6）；10+家排队", "🔴 数据保护墙"],
              ["fill/finish产能利用率", "行业报告", "半年", "2024短缺→2026平衡", "🟡 缓解中"],
            ].map((row, i) => new TableRow({
              children: [
                dataCell(row[0], 2400, { bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[1], 1500, { color: C.muted, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[2], 1100, { color: C.muted, align: AlignmentType.CENTER, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[3], 2626, { shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[4], 1400, { bold: true, align: AlignmentType.CENTER, shading: i % 2 === 0 ? C.highlight : undefined }),
              ]
            }))
          ]
        }),

        // ── 7. 关键变量 ──
        sectionHeading("7. 关键变量（场景推演基础）"),
        new Table({
          width: { size: T, type: WidthType.DXA },
          columnWidths: [2600, 900, 3626, 1900],
          rows: [
            new TableRow({
              children: [
                headerCell("变量", 2600),
                headerCell("不确定性", 900),
                headerCell("路径分叉", 3626),
                headerCell("时间窗口", 1900),
              ]
            }),
            ...[
              ["orforglipron 口服安全性与处方增速", "中", "快速渗透→GLP-1市场2×；安全事件→回调", "2026-2028"],
              ["中国仿制药2027集中上市价格战烈度", "高", "市场3×扩容但利润↓；或质量事件→监管收紧", "2027-2029"],
              ["retatrutide 三靶 vs CagriSema 组合", "中", "三靶全面领先→Lilly碾压；或并存竞争", "2027-2029"],
              ["阿尔茨海默适应症成败", "高", "Phase 3成功→+$100-200亿；失败→预期回调", "2028-2032"],
            ].map((row, i) => new TableRow({
              children: [
                dataCell(row[0], 2600, { bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[1], 900, { align: AlignmentType.CENTER, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[2], 3626, { shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[3], 1900, { align: AlignmentType.CENTER, color: C.muted, shading: i % 2 === 0 ? C.highlight : undefined }),
              ]
            }))
          ]
        }),

        // ── 8. 情景矩阵 ──
        sectionHeading("8. 情景矩阵分析"),
        bodyText("基于口服小分子渗透速度与适应症扩展两个关键维度构建 2×2 情景矩阵："),
        new Paragraph({ spacing: { before: 120 }, children: [] }),

        // Scenario A
        subHeading("情景 A：GLP-1 黄金时代（概率 35%）"),
        bodyText("口服小分子快速渗透（orforglipron 放量）+ 适应症扩展（CVD/MASH/Cachexia）+ 医保覆盖扩大 → 2030 年市场规模达 $2,000 亿以上。"),

        // Scenario B
        subHeading("情景 B：双寡头困兽斗（概率 30%）"),
        bodyText("CagriSema vs Retatrutide 激烈竞争、加速降本，口服渗透慢于预期，双方展开价格竞争，市场份额均分~$2,000 亿。"),

        // Scenario C
        subHeading("情景 C：中国仿制药海啸（概率 25%）"),
        bodyText("2027 年仿制药集中上市，价格降50%+、量增3倍；但中国人均仍低，全球格局影响有限。"),

        // Scenario D
        subHeading("情景 D：安全事件黑天鹅（概率 10%）"),
        bodyText("GLP-1 长期安全性事件（甲状腺C细胞/胰腺），全球监管收紧、处方受限，市场回调至 $1,000 亿。"),
        new Paragraph({ spacing: { before: 120 }, children: [] }),

        // ── 9. 风险评估 ──
        sectionHeading("9. 风险评估"),
        new Table({
          width: { size: T, type: WidthType.DXA },
          columnWidths: [2800, 1000, 1200, 4026],
          rows: [
            new TableRow({
              children: [
                headerCell("风险", 2800),
                headerCell("可能性", 1000),
                headerCell("影响", 1200),
                headerCell("缓释措施", 4026),
              ]
            }),
            ...[
              ["GLP-1 长期安全性未知（甲状腺C细胞/胰腺）", "中低", "极高—全品类受阻", "关注FDA持续安全性监测数据"],
              ["美国药价谈判（IRA）扩展至GLP-1", "中", "高—利润压缩", "口服药在Medicare Part D已有定价优势"],
              ["中国仿制药2027质量事件", "低", "中—影响整体品类信任", "关注龙头企业工艺验证披露"],
              ["中美供应链脱钩→原料药断供", "中低", "中—部分企业停产", "Bachem非中国供应策略有对冲"],
            ].map((row, i) => new TableRow({
              children: [
                dataCell(row[0], 2800, { bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[1], 1000, { align: AlignmentType.CENTER, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[2], 1200, { align: AlignmentType.CENTER, color: "C00000", bold: true, shading: i % 2 === 0 ? C.highlight : undefined }),
                dataCell(row[3], 4026, { shading: i % 2 === 0 ? C.highlight : undefined }),
              ]
            }))
          ]
        }),

        // ── 10. 复查计划 ──
        sectionHeading("10. 复查计划"),
        bodyText("复查触发条件：", { bold: true }),
        bulletItem("Novo Nordisk / Eli Lilly 2026 Q2-Q4 财报发布"),
        bulletItem("CagriSema FDA 审批决定"),
        bulletItem("中国首款司美格鲁肽仿制药获批"),
        new Paragraph({ spacing: { before: 80 }, children: [] }),
        bodyText("建议复查日期：2026 年 9 月 3 日", { bold: true, color: C.primary }),
        new Paragraph({ spacing: { before: 80 }, children: [] }),
        bodyText("需重点关注的信号：", { bold: true }),
        bulletItem("orforglipron 处方量的早期数据"),
        bulletItem("CagriSema 审评进度"),
        bulletItem("中国仿制药审批动态"),

        // ── 11. 反思与改进 ──
        sectionHeading("11. 反思与改进"),

        subHeading("最有价值的发现"),
        bodyText(
          "fill/finish 制剂产能是本次分析揭示的最硬卡点——Novo以$165亿收购Catalent本身就证明了其稀缺性。 " +
          "口服小分子（orforglipron）物理上绕过了注射剂路线，因此不只影响给药便利性，还影响整个产业链的控制点分布。"
        ),

        subHeading("本次分析的不足"),
        bulletItem("对 retatrutide（三靶）的 Phase 3 进度和疗效数据覆盖不够"),
        bulletItem("对信达/先为达等中国创新药的竞争力分析偏浅"),
        bulletItem("对 GLP-1 在阿尔茨海默方向的 Phase 2/3 时间线估算基于推测"),

        subHeading("下次可以改进的地方"),
        bulletItem("使用 ChEMBL 的 get_admet 对比 orforglipron 与注射肽的 ADMET 差异（口服药的DMPK优势）"),
        bulletItem("使用 ClinicalTrials.gov 搜索中国GLP-1仿制药的 BE 试验状态，判断2027批准概率"),

        // ── Footer note ──
        new Paragraph({ spacing: { before: 600 }, children: [] }),
        new Paragraph({
          border: { top: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 8 } },
          spacing: { before: 120 },
          children: [new TextRun({
            text: "此报告由 产业洞察SOP v2.1.0 自动生成 | 分析框架基于王煜全《学会洞察行业》方法学 | MCP数据源：ChEMBL, PubMed, ClinicalTrials.gov",
            font: "Arial", size: 16, color: C.muted, italics: true,
          })]
        }),
      ]
    }
  ]
});

// ── OUTPUT ─────────────────────────────────────────────
const outPath = "/home/hongjianz/industry-analysis-plugin/industry-analysis/outputs/GLP-1-行业深度分析报告.docx";
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outPath, buffer);
  console.log("✅ Report generated:", outPath);
  console.log("   Size:", (buffer.length / 1024).toFixed(1), "KB");
});
