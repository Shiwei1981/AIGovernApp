# AI Govern Dashboard - 设计总结与关键决策 V1

本文档用于集中记录当前阶段已经确认的设计方向、设计思路、设计结果、关键设计决定，以及各设计文件之间的关系，作为后续 UI 设计、前端开发、数据接入和领域页展开的总说明。

## 1. 项目定位

本项目不是文档门户，也不是报表仓库，而是一个面向企业 AI governance / AI security 团队的 **AI Control Tower**。

它的核心目标是：

1. 用最少点击让管理者看到 **哪个治理领域最需要关注**
2. 首页只做 **跨领域总览与导航**
3. 详细分析放到二级页面中完成

## 2. 方法论与输入依据

当前设计基于以下方法论与输入：

| 输入 | 作用 |
|---|---|
| **NIST AI RMF** | 提供 Govern / Map / Measure / Manage 的治理框架视角 |
| **NIST AI 600-1** | 提供 GenAI 风险与治理重点，尤其是治理、测试、内容 provenance、事件披露等方向 |
| **OWASP Top 10 for LLM Applications** | 提供 AI 应用安全风险清单，帮助界定安全防护与验证重点 |
| **Microsoft 平台能力** | 作为本期主要可落地数据源与实现基础 |

### 关键方法论判断

1. **NIST AI 600-1 不能直接翻译成 7/8 个 dashboard 栏目**
   - 它更像风险与治理方法论
   - 不能简单把章节标题直接拿来做页面栏目

2. **一级栏目必须低重叠**
   - 不能让“安全”“验证”“内容可信”“数据与隐私”互相打架
   - 所以一级栏目最终按 **管理对象 + 治理闭环位置** 来拆分

3. **首页指标必须是 decision-useful metrics**
   - 不接受看起来成立、其实容易永远 100% 的伪指标
   - 不依赖很难自动生成的长句说明

## 3. 当前确认的一级栏目

当前确认的 8 个一级栏目如下：

1. **AI Asset Inventory**
2. **Third-Party and Supply Chain**
3. **Data and Privacy**
4. **AI Security Protection**
5. **Output Trustworthiness and Content Provenance**
6. **Validation, Audit, and Compliance Assurance**
7. **Operational Incidents, Response, and Remediation**
8. **Governance Oversight and Control Execution**

## 4. 已明确后置的话题

以下主题不从一级栏目中拿掉，但在优先级上后置：

| 话题 | 当前归属 |
|---|---|
| 责任与风险分级 | 8.3 / 8.4 |
| 知识产权 | 3.6 |
| 滥用防护 | 4.4 |
| CI/CD、上线 gate、go/no-go | 6.5 |
| 人机协同、偏差、稳定性 | 5.5 |

## 5. 全站设计原则

### 5.1 产品与页面原则

1. **决策优先**
   - 先回答“哪里有风险、哪里要行动”
   - 不把首页做成制度清单或说明书

2. **一级页面总览，二级页面下钻**
   - 一级页面只放 8 张领域卡片
   - 每张卡片只放 1-2 个最重要的指标
   - 点击后进入只对应 1 个领域的二级页面

3. **真实数据优先，假数据补位**
   - 能接微软真实数据的优先真数据
   - 事件、治理类允许先用 sample data 占位

4. **默认周视图**
   - 趋势相关图形默认按周表达

### 5.2 首页 UI 原则

1. **首页只保留顶部状态条 + 8 张领域卡片**
    - 已删除全局摘要区
    - 已删除重点行动区
   - 顶部状态条当前只保留 **Time** 与 **Last Updated**
   - 不再在顶部显示 `Region`、`BU`、`Data Coverage`

2. **卡片布局强调可扫读**
   - 大屏优先 4 张卡 / 行
   - 增大左右页边距与卡片间距
   - 每张卡片中的 2 个指标左右并排

3. **状态语义优先**
   - 右上 badge 使用统一的领域状态词：
     - **High Risk**
     - **Attention**
     - **Low Risk**
   - badge 配色与领域状态颜色保持一致
   - `Sample Data` 不与风险状态混用，改为单独的中性说明

4. **文案控制**
   - 不使用自动生成难度高的 narrative issue text
   - 删除 `Why it matters`
   - 指标说明采用短词组，不用长句

5. **图形按含义选型**
   - 覆盖率 / 占比 -> donut
   - 结构分布 -> stacked composition bar
   - 积压 / 趋势 -> 大数字 + sparkline
   - 周事件趋势 + 来源拆分 -> 大数字 + stacked weekly bars
   - 首页中的 donut 指标统一采用 **上文下图**
   - 即：数值 / 说明文字在上，donut 在下
   - 不再使用首页卡片中的左右并排 donut 布局，以避免窄卡片中出现文字挤压或 donut 偏移

### 5.3 一级页面与二级页面关系

1. **一级页面** = 首页总览
   - 8 个领域
   - 每个领域 2 个关键指标

2. **二级页面** = 单一领域页面
   - 每个二级页面只对应 1 个领域
   - 承接该领域的全部相关指标

3. **关键约束**
     - 一级页面中的 2 个指标，必须是对应二级页面全部指标的子集
     - 二级目录是二级页面的展开骨架，因此比首页指标更稳定、更基础
     - 二级页面不要求把一级页面的 2 个指标原样重复显示
     - 二级页面区块标题不再显示 `Current Phase` / `Phase 2` 之类的 phase 标签
     - 只要求二级页面的完整指标集合能够覆盖一级页面指标，必要时可拆分成更细的指标
     - 二级页面设计文档应按**一指标一行**记录，不再按整个二级目录共用一条数据来源
     - 二级页面原型中，每个指标 / 图形卡片也应带自己的数据来源说明

## 6. 当前已确认的首页卡片指标

以下 6 个领域已经完成一轮较深入确认：

| 领域 | 指标 1 | 指标 2 | 当前数据逻辑 |
|---|---|---|---|
| **AI Asset Inventory** | Discovered Assets | Asset Type Mix | 用总量表达治理对象规模；用结构表达资产构成 |
| **Third-Party and Supply Chain** | 3rd-Party Dependencies | Critical Open-Source Findings | 用依赖总数与分类表达依赖面；用高危开源发现表达风险积压 |
| **Data and Privacy** | Purview Classification Coverage | Sensitive Data Exposure Alerts | 用 Purview 分类覆盖表达识别能力；当前确认用 M365 / Purview unique alert cases 表达实际暴露风险 |
| **AI Security Protection** | AI Resources in Unhealthy State | Open High/Critical Defender Recommendations | 直接引用 Defender posture 原生状态与建议项 |
| **Output Trustworthiness and Content Provenance** | Grounded Response Rate | Synthetic Content Labeling Gaps | 用 grounded 输出占比表达可信性；用 labeling gaps 表达 disclosure / provenance 缺口 |
| **Validation, Audit, and Compliance Assurance** | Required Validation Coverage | Open High-Risk Findings | 用 assurance 覆盖率表达是否完成必需验证；用高风险发现积压表达 formal assurance backlog |

### 6.1 Domain 1 - AI Asset Inventory

关键决定：
- 放弃 `Inventory Coverage` 与 `Owner Coverage`
- 原因是这类指标容易成为自证型指标或接近永远 100%
- 改用 **Discovered Assets** + **Asset Type Mix**

UI 决定：
- `Discovered Assets` 用纯数字
- `Asset Type Mix` 用 stacked composition bar + legend
- 两个子框保持等宽

### 6.2 Domain 2 - Third-Party and Supply Chain

关键决定：
- 放弃 `External Dependency Ratio`
- 原因是其管理意义不够强
- 改用 **3rd-Party Dependencies** + **Critical Open-Source Findings**

UI 决定：
- 左侧用总数 + 分类结构
- 右侧用大数字 + 趋势线

### 6.3 Domain 3 - Data and Privacy

关键决定：
- 第一个指标从 `Data Source Registration Coverage` 调整为 **Purview Classification Coverage**
- 原因是它比 lineage / source registration 更能表达隐私与敏感数据识别能力
- 第二个指标确定为 **Sensitive Data Exposure Alerts**

统计口径决定：
- `Sensitive Data Exposure Alerts` 以 **unique alert cases** 为首页表达
- 当前确认的实现口径优先采用 **M365 / Purview** 默认告警能力，不依赖额外的 Azure 应用日志拼接
- 在二级页面中，该首页指标当前由 **3.3 M365 / Purview Exposure Alerts** 承接
- 首页保留通用名称 `Sensitive Data Exposure Alerts`，但当前确认范围不再包含独立的 **Azure AI App Exposure Alerts** 卡片

UI 决定：
- `Purview Classification Coverage` 使用 donut，并上对齐
- `Sensitive Data Exposure Alerts` 使用大数字 + 4 周 bars
- 二级页面中的 `3.1` 已收敛为 **2 个 Azure 资源治理指标**
  - **Purview-Controlled vs AI-Tagged Azure Resources**
  - **Potential AI-Use Azure Resources Without AI Tag**
- 两项都只统计 **Azure 数据库** 与 **Azure 云存储**
- 卡片默认显示数量；资源对照 / 资源列表默认折叠，按需展开
- `3.2` 当前原型已调整为 **4 个指标 / 每行 2 个**，并已**确认**
  - **Purview Classification Coverage**
  - **Sensitive Data Category Mix**
  - **Top Requested Classifications**
  - **Mask Execution Activity**
- `3.3` 已改为 **M365 敏感数据保护与告警**，并收敛为只依赖**默认 Purview / M365 数据**的 2 个指标，且已**确认**
  - **Protected Sensitive M365 Items**
  - **M365 / Purview Exposure Alerts**
- `3.4` 已收敛为 **1 行 2 指标**，且已**确认**
  - **Over-Retention Data Resources**
  - **Data Resources Without Effective Retention Policy**
- `3.4` 的两项都只依赖 **Azure / Policy / Purview** 可直接提供的数据
- 原 `3.3 PII` 内容已后移到 `3.6`
- 当前原型中，`3.5` 与 `3.6` 设为**隐藏**
- `3.1`–`3.4` 的设计逻辑、取数系统、关键字段与计算方法，现已在 `dashboard-columns-v1.md` 中按开发口径详细记录

### 6.4 Domain 4 - AI Security Protection

关键决定：
- 放弃自定义 AI security baseline 的思路
- 不自己发明一套标准作为首页主指标
- 直接采用 **Microsoft Defender for Cloud / AI security posture** 的原生语义

当前确定的两个指标：
- **AI Resources in Unhealthy State**
- **Open High/Critical Defender Recommendations**

原因：
- 更接近微软原生结果
- 比自定义评分更有说服力
- 比 Secure Score 更容易解释

### 6.5 Domain 5 - Output Trustworthiness and Content Provenance

关键决定：
- 保留 **Grounded Response Rate** 作为首页第一个指标
- 保留 **Synthetic Content Labeling Gaps** 作为首页第二个指标
- 暂不优先把 `Provenance Coverage` 作为首页主指标

原因：
- `Grounded Response Rate` 更能表达输出是否有依据、是否可信
- `Synthetic Content Labeling Gaps` 更容易自动化，也更贴近 disclosure / provenance 要求
- `Provenance Coverage` 虽然有意义，但在 metadata 尚未全面打通前不够稳

自动化实现判断：
- `Grounded Response Rate`：中高成熟度，依赖 citation、retrieval trace、evaluation results
- `Synthetic Content Labeling Gaps`：高成熟度，依赖统一的 label / disclosure / watermark 字段

### 6.6 Domain 6 - Validation, Audit, and Compliance Assurance

关键决定：
- 第一个指标定为 **Required Validation Coverage**
- 第二个指标保留 **Open High-Risk Findings**
- 不采用抽象总分作为首页主表达

原因：
- `Required Validation Coverage` 更能表达 assurance baseline 是否已经真正执行
- `Open High-Risk Findings` 更能表达 formal assurance 活动产生的问题积压
- 这组指标比 runtime posture、incident count、release gate pass rate 更符合该领域边界

边界说明：
- 只统计 formal validation / audit / compliance activities
- 不混入 Defender posture recommendation、runtime alert、operational incident

## 7. 当前文件分工

| 文件 | 用途 |
|---|---|
| `dashboard-columns-v1.md` | 一级栏目、二级目录、首页关键指标、数据源、分期 |
| `dashboard-ia-v1.md` | 站点信息架构、页面骨架、页面层级策略 |
| `homepage-design-decisions-v1.md` | 首页卡片级设计决策与指标选择逻辑 |
| `homepage-overview-mockup-v1.html` | 当前首页视觉原型 |
| `design-summary-v1.md` | 本文档，总结设计思路、结果与关键决策 |

补充：
- `dashboard-columns-v1.md` 现已补充 **一级页面已确认 KPI 实施口径（开发参考）**
- 开发如需实现首页 1-6 域 KPI，应优先阅读该节中的来源系统、关键字段与计算逻辑

## 8. 当前状态

### 已确认

1. 网站定位与方法论方向
2. 8 个一级栏目
3. 首页整体骨架
4. 首页卡片设计原则
5. Domain 1-6 的首页指标与主要图形方式

### 待继续确认

1. Domain 7-8 的首页指标
2. 各一级栏目页的区块与图表组合
3. 状态色规则与阈值
4. `AI scope`、`unique alert case` 等统计口径

## 9. 使用建议

如果后续要继续推进设计与开发，建议按以下顺序使用当前文档：

1. 先看 `design-summary-v1.md` 了解全局设计结论
2. 再看 `dashboard-columns-v1.md` 了解领域结构、数据源与分期
3. 再看 `dashboard-ia-v1.md` 了解页面骨架
4. 需要实现首页时，以 `homepage-design-decisions-v1.md` + `homepage-overview-mockup-v1.html` 为直接依据
