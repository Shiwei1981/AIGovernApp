# AI Govern Dashboard - 栏目结构 V1

本文档记录当前确认的 dashboard 一级栏目、首页关键指标、二级目录、主要指标与关键数据来源。

说明：关键数据来源优先采用微软平台数据，包括 Azure、Microsoft 365、Microsoft Entra、Microsoft Purview、Microsoft Defender、Microsoft Sentinel、Azure DevOps、Dataverse / SharePoint Online。

补充说明：
- 一级栏目、二级目录与关键数据来源以本文档为主
- 当前信息架构采用两层页面：
  - **一级页面** = 首页总览，展示 8 个领域，每个领域只展示 2 个关键指标
  - **二级页面** = 点击某一领域后进入的领域页面，只对应一个领域，并承接该领域全部相关指标
- 一级页面显示的 2 个指标，必须是对应二级页面全部指标的**子集**
- 首页卡片指标中，**1-6 域已按当前评审结论更新**
- **7-8 域首页指标仍可继续迭代**

## 一级目录最终顺序

1. AI 资产台账
2. 第三方与供应链
3. 数据与隐私
4. AI 安全防护
5. 输出可信与内容溯源
6. 验证、审计与合规保证
7. 运行事件、响应与整改
8. 治理监督与控制执行

## 一级目录设计总览

本节用于记录一级目录层面的设计定位，作为首页卡片设计、二级页面设计、以及后续二级目录展开的统一上层约束。

### 一级目录设计原则

1. **一级目录按治理对象与治理闭环位置拆分**
   - 避免同一问题在多个栏目重复解释
   - 先确保边界清晰，再考虑展示完整性

2. **首页只展示每个一级目录最重要的 1-2 个指标**
   - 用于快速判断哪个领域需要关注
   - 不在首页堆叠大量解释性内容

3. **一级目录页再承接二级目录**
   - 点击一级页面中的某一领域卡片，将进入只对应这个领域的二级页面
   - 二级目录是后续页面展开、图表设计、数据接入的主要指导层
   - 一级页面的 2 个关键指标必须能够在该领域的二级页面中找到对应承接
   - 因此二级目录的边界稳定性优先于首页展示完整性

4. **优先使用可自动化、可持续获取的数据**
   - 优先使用 Microsoft 平台原生数据
   - 对自动化成熟度不足的内容，可先作为后置或样例数据处理

### 当前一级目录设计结果

| 一级目录 | 英文名称 | 设计定位 | 首页关键指标状态 |
|---|---|---|---|
| 1. AI 资产台账 | AI Asset Inventory | 定义治理对象总体范围，回答“我们到底在管什么” | 已确认 |
| 2. 第三方与供应链 | Third-Party and Supply Chain | 管理外部模型、API、开源组件、skill/agent 等依赖面 | 已确认 |
| 3. 数据与隐私 | Data and Privacy | 管理 AI 使用数据的识别、分类、暴露与隐私风险 | 已确认 |
| 4. AI 安全防护 | AI Security Protection | 管理 AI 运行面、接口面、身份面与防护姿态 | 已确认 |
| 5. 输出可信与内容溯源 | Output Trustworthiness and Content Provenance | 管理输出可信性、合成内容标识与 provenance / disclosure | 已确认 |
| 6. 验证、审计与合规保证 | Validation, Audit, and Compliance Assurance | 管理 assurance baseline、formal validation、audit evidence 与 findings | 已确认 |
| 7. 运行事件、响应与整改 | Operational Incidents, Response, and Remediation | 管理 AI 相关事件、处置时效与整改闭环 | 待确认 |
| 8. 治理监督与控制执行 | Governance Oversight and Control Execution | 管理治理动作执行、例外、风险接受与监督机制 | 待确认 |

## 一级页面的内容与设计

本节中的“一级页面”指首页总览页。

### 一级页面的内容

1. 展示 **8 个领域**
2. 每个领域只展示 **2 个关键指标**
3. 每个领域以 **一个卡片** 作为统一容器
4. 卡片内容包括：
   - 领域名称
   - 2 个关键指标
   - 必要的短说明
   - 风险/关注状态
5. 一级页面不承载该领域的全部指标，只承载最需要管理者快速判断的指标

### 一级页面的设计原则

1. **总览优先**
   - 目标是快速判断“哪个领域最值得点进去看”
   - 不在首页展开过多解释与图表

2. **8 个领域并列**
   - 首页同时展示全部 8 个领域
   - 用统一卡片结构降低认知切换成本

3. **每个领域只保留 2 个关键指标**
   - 这 2 个指标必须最有代表性
   - 这 2 个指标必须是对应二级页面全部指标的子集

4. **交互简单**
   - 用户点击某个领域卡片后，直接进入该领域的二级页面

### 一级页面与本文件的关系

- 本文档中每个领域下的 **“首页关键指标”**，就是一级页面该领域卡片中显示的 2 个指标
- 这些指标服务于首页展示，不等于该领域的全部指标集合

### 一级页面当前指标设计结果

| 领域 | 指标 | 设计思路 | 指标解释 | 图形 | 指标数据汇集来源 | 状态 |
|---|---|---|---|---|---|---|
| 1. AI 资产台账 | Discovered Assets | 直接表达治理对象总体规模 | 当前企业范围内已发现并纳入统计范围的 AI 资产总数 | plain number | Azure Resource Graph、Azure AI Foundry / Azure Machine Learning Registry、Microsoft Entra ID、Dataverse / SharePoint Online 资产台账 | 已确认 |
| 1. AI 资产台账 | Asset Type Mix | 表达资产结构，而不是再放一个 coverage 类伪指标 | 当前已发现 AI 资产按主要类型拆分后的结构分布 | stacked composition bar + legend | Azure Resource Graph、Azure AI Foundry / Azure Machine Learning Registry、Dataverse / SharePoint Online 资产台账、应用程序资产分类字段 | 已确认 |
| 2. 第三方与供应链 | 3rd-Party Dependencies | 表达整体依赖面与主要依赖类型 | 当前 AI 环境中使用的第三方模型、API、软件包、服务等依赖总量与分类 | plain number + category mix | Azure API Management、Azure AI Foundry 模型/连接清单、Azure Resource Graph、应用程序连接配置与依赖清单 | 已确认 |
| 2. 第三方与供应链 | Critical Open-Source Findings | 表达当前供应链高风险问题积压 | 当前尚未关闭的开源组件高危发现数量 | plain number + sparkline | Microsoft Defender for DevOps、Defender Vulnerability Management、Azure Artifacts、Azure Container Registry | 已确认 |
| 3. 数据与隐私 | Purview Classification Coverage | 表达 Purview 对结构化 AI 数据资源的分类覆盖程度 | Purview 已发现且可做列级解析的数据库 / 文件资源中，已完成 classify 的列占总列数的比例 | donut | Microsoft Purview Data Map、Purview scan results、Purview classification 结果 | 已确认 |
| 3. 数据与隐私 | Sensitive Data Exposure Alerts | 表达默认 Purview 控制面已观测到的实际暴露风险信号，并优先保证自动化可落地 | 最近周期内来自 M365 / Purview 控制面的 unique sensitive-data exposure alert cases | plain number + 4-week bars | Microsoft Purview DLP / Alert Center、Purview Audit | 已确认 |
| 4. AI 安全防护 | AI Resources in Unhealthy State | 直接使用 Defender posture 原生 unhealthy 状态表达问题面 | 当前 AI scope 内被 Defender posture 标记为 unhealthy 的资源占比 | donut | Microsoft Defender for Cloud / AI security posture、Azure Resource Graph（用于 AI scope 过滤） | 已确认 |
| 4. AI 安全防护 | Open High/Critical Defender Recommendations | 表达高优先级安全整改积压 | 当前 AI scope 内未关闭的 High / Critical Defender 建议数量 | plain number + sparkline | Microsoft Defender for Cloud recommendations / assessments、Azure Resource Graph（用于 AI scope 过滤） | 已确认 |
| 5. 输出可信与内容溯源 | Grounded Response Rate | 表达输出是否有依据、是否可信 | 已评估输出中，可追溯到批准来源或验证证据的输出占比 | donut | Azure AI Foundry Evaluations、Azure AI Search 检索日志、Application Insights / Log Analytics 输出日志 | 已确认 |
| 5. 输出可信与内容溯源 | Synthetic Content Labeling Gaps | 表达 disclosure / provenance 缺口 | 当前生成内容中，缺少 AI-generated label / disclosure 的项目数 | plain number + sparkline | 应用程序生成事件日志、Azure Blob metadata / index tags、Azure AI Vision / Video Indexer、内容管理记录 | 已确认 |
| 6. 验证、审计与合规保证 | Required Validation Coverage | 表达 assurance baseline 是否真正完成 | 纳入范围的 AI 系统中，已完成必需 validation baseline 的占比 | donut | Azure AI Foundry Evaluations、Azure DevOps Test Plans / Work Items、Microsoft Purview Compliance Manager、Defender for Cloud Regulatory Compliance | 已确认 |
| 6. 验证、审计与合规保证 | Open High-Risk Findings | 表达 formal assurance findings 的未关闭积压 | 来自 validation、audit、compliance activities 的高风险未关闭发现数 | plain number + sparkline | Azure DevOps Work Items、Microsoft Purview Compliance Manager、Defender for Cloud Regulatory Compliance、审计发现台账 | 已确认 |
| 7. 运行事件、响应与整改 | AI Incidents This Week | 表达当前周度事件压力 | 当前周度 AI 相关安全、隐私、内容事件数量 | plain number + sparkline | Microsoft Sentinel、Microsoft Defender XDR、Azure Monitor Alerts、Microsoft Purview Alert Center | 当前工作版本 / Sample data |
| 7. 运行事件、响应与整改 | Average Closure Time | 表达高严重事件关闭效率与目标差距 | 高严重 AI 事件从发现到关闭的平均耗时 | plain number + bullet bar | Microsoft Sentinel 事件时间线、Defender XDR 处置记录、Azure DevOps Boards、Power Automate 审批/通知日志 | 当前工作版本 / Sample data |
| 8. 治理监督与控制执行 | On-Time Governance Actions | 表达治理动作执行率 | 计划中的治理动作在要求周期内按时完成的占比 | donut | Microsoft Purview Compliance Manager、Azure Policy、Azure DevOps Approvals、Dataverse / SharePoint Online 治理任务台账 | 当前工作版本 / Sample data |
| 8. 治理监督与控制执行 | Open Exceptions / Risk Acceptances | 表达例外与风险接受存量 | 当前仍在跟踪中的治理例外与风险接受项目数 | plain number + sparkline | Azure Policy exemptions、Microsoft Defender for Cloud exemptions、Dataverse / SharePoint Online 风险接受台账、Power Automate 审批记录 | 当前工作版本 / Sample data |

### 一级页面已确认 KPI 实施口径（开发参考）

说明：
- 以下口径只覆盖当前 **一级页面 / 首页总览** 已确认的 1-6 域 KPI
- 默认统计周期为**最近 4 周**
- 趋势型指标按**周**聚合
- `7-8` 域当前仍是 sample data / 工作版本，不在本节展开

#### 1.1 Discovered Assets

- **设计逻辑**：先让管理者看到企业当前到底有多少 AI 治理对象在管。
- **来源系统**：
  - Azure Resource Graph
  - Azure AI Foundry / Azure Machine Learning Registry
  - Microsoft Entra ID
  - Dataverse / SharePoint Online 资产台账
- **需要抽取的关键字段**：
  - asset id / resource id / app id
  - asset type
  - asset name
  - lifecycle state（可选）
- **计算逻辑**：
  1. 合并应用、模型、Agent、API 等在管 AI 资产来源
  2. 统一归一为资产主键（优先 `resourceId` / `appId` / registry id）
  3. 去重后统计总量
  4. 首页显示该 deduplicated total population

#### 1.2 Asset Type Mix

- **设计逻辑**：在总量之外，再给管理者一个结构视图，快速知道当前 AI 资产以什么类型为主。
- **来源系统**：
  - Azure Resource Graph
  - Azure AI Foundry / Azure Machine Learning Registry
  - Dataverse / SharePoint Online 资产台账
  - 应用程序资产分类字段
- **需要抽取的关键字段**：
  - asset id
  - normalized asset type
- **计算逻辑**：
  1. 以 `Discovered Assets` 的去重后资产全集为输入
  2. 将资产映射到统一类型集合（如 Applications、Models、Agents、APIs）
  3. 按类型聚合数量
  4. 输出 stacked composition bar 与 legend

#### 2.1 3rd-Party Dependencies

- **设计逻辑**：表达 AI 环境当前暴露在多少外部依赖之上，以及依赖结构是否健康。
- **来源系统**：
  - Azure API Management
  - Azure AI Foundry 模型 / connection 清单
  - Azure Resource Graph
  - 应用程序连接配置与依赖清单
- **需要抽取的关键字段**：
  - dependency id / endpoint / package name
  - dependency type
  - vendor / provider
  - linked system / application
- **计算逻辑**：
  1. 汇总外部模型、API、软件包、服务等依赖记录
  2. 以 dependency 主键（如 endpoint、package identifier、model deployment reference）做归一去重
  3. 统计依赖总数
  4. 按主要依赖类型聚合，生成分类结构

#### 2.2 Critical Open-Source Findings

- **设计逻辑**：管理者需要看到当前供应链里最紧急、最难拖延的问题积压。
- **来源系统**：
  - Microsoft Defender for DevOps
  - Defender Vulnerability Management
  - Azure Artifacts
  - Azure Container Registry
- **需要抽取的关键字段**：
  - finding id
  - severity
  - status
  - component / package / image
  - detected time
- **计算逻辑**：
  1. 只保留开源组件相关 finding
  2. 过滤 `severity = Critical`
  3. 过滤 `status != Closed / Resolved`
  4. 统计 open findings 数量
  5. 按周聚合新增或期末未关闭数量，生成 sparkline

#### 3.1 Purview Classification Coverage

- **设计逻辑**：首页不做抽象的数据资产总量推断，直接看 Purview 对结构化 AI 数据资源的识别覆盖。
- **来源系统**：
  - Microsoft Purview Data Map
  - Purview scan results
  - Purview classification 结果
- **需要抽取的关键字段**：
  - 资源标识
  - 资源类型
  - column 清单
  - 每列 classification 状态
- **计算逻辑**：
  1. 取 Purview 已发现且可做列级解析的数据库 / 文件资源
  2. 统计总列数
  3. 统计已完成 classification 的列数
  4. 计算覆盖率：
     - `classified columns / total columns`
  5. 首页以 donut 呈现百分比

#### 3.2 Sensitive Data Exposure Alerts

- **设计逻辑**：首页优先表达真实暴露风险，而不是静态敏感系统数量；同时优先保证自动化可落地。
- **来源系统**：
  - Microsoft Purview DLP / Alert Center
  - Purview Audit
- **需要抽取的关键字段**：
  - alert / case id
  - created time
  - location / workload
  - policy / rule
- **计算逻辑**：
  1. 取所选周期内全部 M365 / Purview sensitive-data exposure alerts
  2. 以 `alert / case id` 去重
  3. 统计 unique alert cases 总数
  4. 按周聚合 unique alert cases，生成 4-week bars
  5. 首页保留通用名称 `Sensitive Data Exposure Alerts`

#### 4.1 AI Resources in Unhealthy State

- **设计逻辑**：直接复用 Defender posture 原生 unhealthy 语义，避免再造一个自定义安全评分。
- **来源系统**：
  - Microsoft Defender for Cloud / AI security posture
  - Azure Resource Graph（用于 AI scope 过滤）
- **需要抽取的关键字段**：
  - resource id
  - AI scope 标记 / resource classification
  - posture state
- **计算逻辑**：
  1. 定义 AI-scoped resource population
  2. 取该范围内全部 posture records
  3. 过滤 `state = Unhealthy`
  4. 计算：
     - `unhealthy AI resources / total AI-scoped resources`
  5. 首页以 donut 呈现占比

#### 4.2 Open High/Critical Defender Recommendations

- **设计逻辑**：与 posture 占比配套，直接看尚未关闭的高优先级整改积压。
- **来源系统**：
  - Microsoft Defender for Cloud recommendations / assessments
  - Azure Resource Graph（用于 AI scope 过滤）
- **需要抽取的关键字段**：
  - recommendation id
  - severity
  - status
  - related resource id
  - detected time
- **计算逻辑**：
  1. 只保留 AI-scoped resources 对应的 recommendations
  2. 过滤 `severity in (High, Critical)`
  3. 过滤未关闭 recommendations
  4. 统计总数
  5. 按周聚合 open backlog 或新增高危 recommendation，生成 sparkline

#### 5.1 Grounded Response Rate

- **设计逻辑**：比“幻觉率”更稳定，也更符合 trustworthiness 的治理表达。
- **来源系统**：
  - Azure AI Foundry Evaluations
  - Azure AI Search 检索日志
  - Application Insights / Log Analytics 输出日志
- **需要抽取的关键字段**：
  - response / evaluation id
  - grounded / citation / evaluator result
  - output time
  - linked source references
- **计算逻辑**：
  1. 取所选时间段内已评估输出样本
  2. 识别其中被判定为 grounded 的输出
  3. 计算：
     - `grounded outputs / evaluated outputs`
  4. 首页以 donut 呈现 grounded response rate

#### 5.2 Synthetic Content Labeling Gaps

- **设计逻辑**：直接表达 disclosure / provenance 缺口，比做完整 provenance coverage 更适合当前阶段自动化。
- **来源系统**：
  - 应用程序生成事件日志
  - Azure Blob metadata / index tags
  - Azure AI Vision / Video Indexer
  - 内容管理记录
- **需要抽取的关键字段**：
  - content id
  - generated time
  - content type
  - AI-generated label / disclosure / watermark flag
- **计算逻辑**：
  1. 取所选时间段内全部生成内容记录
  2. 过滤缺少 label / disclosure / watermark 标识的记录
  3. 以 `content id` 去重后统计数量
  4. 按周聚合缺口数量，生成 sparkline

#### 6.1 Required Validation Coverage

- **设计逻辑**：回答 assurance baseline 是否真正做完，而不是只看有没有创建测试或有没有总分。
- **来源系统**：
  - Azure AI Foundry Evaluations
  - Azure DevOps Test Plans / Work Items
  - Microsoft Purview Compliance Manager
  - Defender for Cloud Regulatory Compliance
- **需要抽取的关键字段**：
  - system / application id
  - required validation baseline
  - evaluation / test / compliance evidence status
- **计算逻辑**：
  1. 识别所有纳入 assurance 范围且要求做 validation baseline 的 AI 系统
  2. 检查每个系统要求的 validation / audit / compliance evidence 是否全部完成
  3. 计算：
     - `systems with completed required baseline / systems requiring baseline`
  4. 首页以 donut 呈现覆盖率

#### 6.2 Open High-Risk Findings

- **设计逻辑**：coverage 说明“做没做”，这个指标说明“做出来的问题有没有真关闭”。
- **来源系统**：
  - Azure DevOps Work Items
  - Microsoft Purview Compliance Manager
  - Defender for Cloud Regulatory Compliance
  - 审计发现台账
- **需要抽取的关键字段**：
  - finding id
  - severity / risk rating
  - status
  - finding source
  - opened time
- **计算逻辑**：
  1. 只保留 formal assurance 活动产生的 findings
  2. 过滤高风险 finding（如 High / Severe / Major，按统一 risk mapping）
  3. 过滤未关闭 findings
  4. 统计总数
  5. 按周聚合 open backlog 或新增高风险 finding，生成 sparkline

## 二级页面的内容与设计

本节中的“二级页面”指点击某个领域卡片后进入的单领域页面。

### 二级页面的内容

1. 每个二级页面只对应 **1 个领域**
2. 二级页面应承接该领域 **全部相关指标**
3. 二级页面以内部分区承接该领域的 **二级目录**
4. 二级页面中的内容来源包括：
   - 本领域的首页 2 个关键指标
   - 本领域各二级目录中的主要指标
   - 后续该领域页面展开时需要的图表、明细、趋势与说明

### 二级页面的设计原则

1. **单领域展开**
   - 一个页面只解释一个领域
   - 不把其他领域的问题混入当前页面

2. **二级目录作为展开骨架**
   - 本文档中的“二级目录”是二级页面信息组织的基础
   - 后续页面区块、图表设计、数据接入，都优先围绕二级目录展开

3. **承接首页，不强制在页头重复首页**
   - 二级页面整体应承接首页中的 2 个关键指标
   - 页头不要求重复显示首页 KPI；页面主体覆盖即可
   - 页面主体再进一步展开该领域的全部相关指标

4. **边界稳定优先**
   - 二级页面中的二级目录边界，应比首页卡片文案更稳定
   - 因为二级目录是后续设计与开发的重要指导层

### 二级页面与本文件的关系

- 本文档中每个领域下的 **“二级目录 / 是否本期实现 / 主要指标 / 关键数据来源”**，主要用于指导二级页面设计
- 因此本文件中最重要、最需要保持稳定的部分，是各领域下的 **二级目录结构与主要指标方向**

### 二级页面与一级页面的承接关系

1. 一级页面中的 **2 个关键指标**，必须在对应二级页面的完整指标集合中被覆盖
2. 二级页面不要求把这 2 个指标原样重复显示为单独的顶部卡片
3. 二级页面可以使用**不同的图形**或**不同的组织形式**来表达相同的基础数据
4. 必要时，一级页面中的 1 个指标可以在二级页面中拆分为多个更细的指标
5. 二级页面主体再进一步展开该领域的全部相关指标

### 一级页面指标在二级页面中的覆盖方式（按领域）

| 领域 | 一级页面的 2 个关键指标 | 二级页面中的覆盖方式 |
|---|---|---|
| 1. AI 资产台账 | Discovered Assets；Asset Type Mix | 应在资产总览 / 资产结构相关指标中被覆盖，不要求重复显示与首页完全相同的两块卡片 |
| 2. 第三方与供应链 | 3rd-Party Dependencies；Critical Open-Source Findings | 应在依赖面、开源与基础组件等指标中被覆盖，不要求重复显示与首页完全相同的两块卡片 |
| 3. 数据与隐私 | Purview Classification Coverage；Sensitive Data Exposure Alerts | `Purview Classification Coverage` 在二级页中不再作为 `3.2.1` 独立卡片重复展示，而是作为 `3.2.1 Potential Sensitive Data Consumer Applications` 与 `3.2.2 Sensitive Data Category Mix` 的输入基础；`Sensitive Data Exposure Alerts` 当前由 `3.3 M365 / Purview Exposure Alerts` 承接，首页保留通用名称，但当前确认范围不再包含独立的 Azure AI App Exposure Alerts 卡片 |
| 4. AI 安全防护 | AI Resources in Unhealthy State；Open High/Critical Defender Recommendations | 应在 Defender posture / recommendation 相关指标中被覆盖，可按更细粒度展开 |
| 5. 输出可信与内容溯源 | Grounded Response Rate；Synthetic Content Labeling Gaps | 应在输出可信性、合成内容标识相关指标中被覆盖，可按场景或内容类型展开 |
| 6. 验证、审计与合规保证 | Required Validation Coverage；Open High-Risk Findings | 应在 validation / audit / compliance 相关指标中被覆盖，不要求在页头重复同名卡片 |
| 7. 运行事件、响应与整改 | AI Incidents This Week；Average Closure Time | 当前为工作版本；二级页面应覆盖事件数量与关闭时效，但具体组织形式待确认 |
| 8. 治理监督与控制执行 | On-Time Governance Actions；Open Exceptions / Risk Acceptances | 当前为工作版本；二级页面应覆盖治理动作执行与例外 / 风险接受存量，但具体组织形式待确认 |

### 二级页面当前内容组织结果（按领域）

说明：以下二级页面设计已改为 **一指标一行**；“设计确认状态”用于记录你对每个指标/图形的逐项确认结果；“指标数据来源”也按指标单独定义，不再由整个二级目录共用。

## 1. AI 资产台账

二级页面应覆盖一级页面指标：**Discovered Assets**；**Asset Type Mix**

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 1.1 资产总览 | AI 应用数 | plain number | 是 | 待确认 | 当前发现并纳入统计范围的 AI 应用数量 | Azure Resource Graph、Dataverse / SharePoint Online 资产台账 |
| 1.1 资产总览 | 模型数 | plain number | 是 | 待确认 | 当前发现并纳入统计范围的模型数量 | Azure AI Foundry / Azure Machine Learning Registry、Azure Resource Graph |
| 1.1 资产总览 | Agent 数 | plain number | 是 | 待确认 | 当前发现并纳入统计范围的 Agent 数量 | Azure AI Foundry Agent Service、Copilot Studio、Dataverse / SharePoint Online 资产台账 |
| 1.1 资产总览 | 纳管覆盖率 | donut | 是 | 待确认 | 已入台账资产占已发现资产的比例 | Azure Resource Graph、Azure AI Foundry / Azure Machine Learning Registry、Dataverse / SharePoint Online 资产台账 |
| 1.1 资产总览 | 按 BU/地区分布 | stacked bar | 是 | 待确认 | 已发现 AI 资产在业务单元与地区上的分布结构 | Dataverse / SharePoint Online 资产台账、Microsoft Entra ID 组织属性、Azure Resource Graph 标签 |
| 1.2 责任归属 | owner 缺失率 | donut | 是 | 待确认 | 缺少明确 owner 的 AI 资产占比 | Microsoft Entra ID、Dataverse / SharePoint Online RACI 台账 |
| 1.2 责任归属 | 技术负责人覆盖率 | donut | 是 | 待确认 | 已指定技术负责人的 AI 资产占比 | Azure RBAC、Microsoft Entra ID、Dataverse / SharePoint Online RACI 台账 |
| 1.2 责任归属 | 业务负责人覆盖率 | donut | 是 | 待确认 | 已指定业务负责人的 AI 资产占比 | Microsoft Entra ID、Dataverse / SharePoint Online RACI 台账 |
| 1.3 重要性与分级 | 高/中/低风险资产数 | stacked bar | 否 | 待确认 | 按风险等级拆分的 AI 资产数量 | Dataverse / SharePoint Online 风险分级台账、Azure Resource Graph 标签 |
| 1.3 重要性与分级 | 涉及敏感数据资产数 | plain number | 否 | 待确认 | 使用或处理敏感数据的 AI 资产数量 | Microsoft Purview Data Map、Dataverse / SharePoint Online 风险分级台账 |
| 1.3 重要性与分级 | 面向外部用户资产数 | plain number | 否 | 待确认 | 面向外部用户或客户暴露的 AI 资产数量 | Azure Resource Graph 标签、Microsoft Entra ID 应用属性、Dataverse / SharePoint Online 资产台账 |
| 1.4 生命周期状态 | 开发/测试/生产/下线数量 | stacked bar | 否 | 待确认 | 按生命周期状态拆分的 AI 资产数量 | Azure DevOps、Azure Activity Log、Dataverse / SharePoint Online 资产台账 |
| 1.4 生命周期状态 | 长期无人维护资产数 | plain number + sparkline | 否 | 待确认 | 长期缺少变更、访问或维护活动的 AI 资产数量 | Azure Activity Log、Application Insights、Azure Resource Graph |

## 2. 第三方与供应链

二级页面应覆盖一级页面指标：**3rd-Party Dependencies**；**Critical Open-Source Findings**

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 2.1 第三方模型/API 依赖 | 使用外部 LLM/API 的系统数 | plain number | 是 | 待确认 | 使用外部模型或 API 的 AI 系统数量 | Azure API Management、Azure AI Foundry 模型/连接清单、Azure Resource Graph |
| 2.1 第三方模型/API 依赖 | 按供应商分布 | stacked bar | 是 | 待确认 | 按主要第三方供应商拆分的依赖结构 | Azure API Management、Azure AI Foundry 模型/连接清单、Azure Cost Management |
| 2.1 第三方模型/API 依赖 | 单一供应商集中度 | donut | 是 | 待确认 | 对单一外部供应商高度集中的依赖比例 | Azure API Management、Azure Cost Management、Azure AI Foundry 模型/连接清单 |
| 2.2 Skill 与 Agent 使用发现 | 检测到 skill/agent 配置或调用的代码库数 | plain number | 是 | 待确认 | 检测到 skill 或 agent 配置/调用痕迹的代码库数量 | Azure DevOps Repos / GitHub Enterprise code search、Dataverse / SharePoint Online 台账 |
| 2.2 Skill 与 Agent 使用发现 | 疑似 vibe coding 线索数 | plain number + sparkline | 是 | 待确认 | 检测到可疑自动编码或未经治理引入模式的线索数 | GitHub Advanced Security / Microsoft Defender for DevOps、Azure DevOps Repos / GitHub Enterprise code search |
| 2.2 Skill 与 Agent 使用发现 | 已识别 owner 的 skill/agent 项数 | donut | 是 | 待确认 | 已明确 owner 的 skill/agent 配置项占比 | Dataverse / SharePoint Online 台账、Microsoft Entra ID |
| 2.3 开源与基础组件 | 开源模型/库数量 | plain number | 是 | 待确认 | AI 环境中使用的开源模型和库数量 | Azure Artifacts、Azure Container Registry、Azure AI Foundry 模型清单 |
| 2.3 开源与基础组件 | 关键组件漏洞数 | plain number + sparkline | 是 | 待确认 | 当前关键开源/基础组件中的漏洞数量 | Microsoft Defender for DevOps、Defender Vulnerability Management、Azure Container Registry |
| 2.3 开源与基础组件 | 未维护组件数 | plain number | 是 | 待确认 | 长期无更新或已弃用的关键组件数量 | Microsoft Defender for DevOps、Azure Artifacts、Azure Container Registry |
| 2.4 插件与扩展组件 | 插件数量 | plain number | 否 | 待确认 | 当前已启用的插件与扩展组件总量 | Azure AI Foundry Agent Service、Copilot Studio、Power Platform connectors |
| 2.4 插件与扩展组件 | 高权限插件数量 | plain number | 否 | 待确认 | 具备高权限访问能力的插件数量 | Microsoft Entra 企业应用日志、Copilot Studio、Power Platform connectors |
| 2.4 插件与扩展组件 | 未评估插件数 | plain number + sparkline | 否 | 待确认 | 尚未完成安全/治理评估的插件数量 | Azure AI Foundry Agent Service、Copilot Studio、Dataverse / SharePoint Online 评估台账 |
| 2.5 供应商风险与替代性 | 高风险供应商数 | plain number | 否 | 待确认 | 被评为高风险的第三方供应商数量 | Dataverse / SharePoint Online 第三方台账、Microsoft Entra 企业应用 |
| 2.5 供应商风险与替代性 | 无替代方案依赖数 | plain number | 否 | 待确认 | 缺少可替代供应商或方案的关键依赖数量 | Dataverse / SharePoint Online 第三方台账、Azure API Management 调用日志 |
| 2.5 供应商风险与替代性 | 合同/SLA 覆盖率 | donut | 否 | 待确认 | 已具备合同或 SLA 保障的第三方依赖占比 | Dataverse / SharePoint Online 第三方台账、Azure Cost Management |

## 3. 数据与隐私

二级页面应覆盖一级页面指标：**Purview Classification Coverage**；**Sensitive Data Exposure Alerts**。其中 `Purview Classification Coverage` 的 Purview classification 数据在二级页中作为 `3.2.1` 与 `3.2.2` 的输入基础，不再作为单独 coverage 卡片重复展示。

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 3.1 Azure 数据资源纳管与 AI 标签 | Purview-Controlled vs AI-Tagged Azure Resources | paired count cards + collapsible comparison table | 是 | 已确认 | 仅统计 Azure 数据库与 Azure 云存储两类资源；分别对比已纳入 Purview 控管的资源数量与已打 `AI` tag 的资源数量，并提供默认折叠的资源对照表（资源名、resource group、是否有 `AI` tag、是否受 Purview 控管、Owner） | Microsoft Purview governed asset list / Data Map、Azure Resource Graph、Azure tags（`AI`、`Owner`） |
| 3.1 Azure 数据资源纳管与 AI 标签 | Potential AI-Use Azure Resources Without AI Tag | paired count cards + collapsible resource list | 是 | 已确认 | 仅统计 Azure 数据库与 Azure 云存储两类资源；如果某个 resource group 中含 AI 相关 Azure 资源，或任一资源带 `AI` tag，则该 resource group 中未打 `AI` tag 的数据库/云存储应被统计，并提供默认折叠的资源列表（资源名、resource group、资源类型、Owner） | Azure Resource Graph、Azure resource group membership、Azure tags（`AI`、`Owner`） |
| 3.2 敏感数据使用 | Potential Sensitive Data Consumer Applications | plain number + DB/File split stats + collapsible application list | 是 | 已确认 | 基于 Purview classification 找到敏感 Azure DB / Azure file 资源，再结合 DB / file 访问日志识别直接消费应用，并通过 Application Insights / OpenTelemetry 应用调用图递归追踪所有依赖这些应用的上游 / 传递应用；主卡片展示 total、DB-linked apps、File-linked apps，其中 DB/File 两个数字是 non-additive；默认折叠列表只保留 application Name、Owner、Type、data resource name、Classification | Microsoft Purview classification、Azure SQL Audit / Monitor logs、Azure Storage / Azure Files diagnostic logs、Application Insights / OpenTelemetry dependencies、Azure Resource Graph、Azure resource tags（`Owner`） |
| 3.2 敏感数据使用 | Sensitive Data Category Mix | stacked composition bar | 是 | 已确认 | 已被 classify 的敏感数据列按 classification 类别聚合后的结构分布 | Purview classification 结果、Microsoft Purview Information Protection |
| 3.2 敏感数据使用 | Top Requested Classifications | top 3 ranking cards + collapsible table | 是 | 已确认 | 在所选时间段内，被特定应用程序请求可见性的 classified 数据列中，访问量最高的 top 3 classification；并提供默认折叠的 classification 访问量明细表（classification、访问量） | 自定义 classified column visibility request 数据库 |
| 3.2 敏感数据使用 | Data Mask Activity | plain number + sparkline + collapsible table | 是 | 已确认 | 在所选时间段内记录到的 mask 执行次数；并提供默认折叠的资源级明细表（资源名、mask 次数、mask 方法） | 自定义 mask request 数据库 |
| 3.3 M365 敏感数据保护与告警 | Protected Sensitive M365 Items | plain number + collapsible table | 是 | 已确认 | 基于默认 Purview 数据，统计在 SharePoint Online、OneDrive、Exchange Online 等位置中，已检测到敏感信息类型且已带敏感度标签的项目数量；并提供默认折叠的位置级列表 | Microsoft Purview Content Explorer、Microsoft Purview Information Protection、SharePoint Online / OneDrive / Exchange Online metadata |
| 3.3 M365 敏感数据保护与告警 | M365 / Purview Exposure Alerts | plain number + sparkline + collapsible table | 是 | 已确认 | 来自 M365 / Purview 控制面的敏感数据暴露告警案例数；并提供默认折叠的 location / policy 明细列表 | Microsoft Purview DLP / Alert Center、Purview Audit |
| 3.4 数据保留与删除 | Over-Retention Data Resources | plain number + sparkline + collapsible table | 否 | 已确认 | 已超出批准保留周期、但仍处于保留状态的数据资源数量；并提供默认折叠的资源明细列表 | Microsoft Purview Data Lifecycle Management、Azure Storage lifecycle policies、Purview retention state |
| 3.4 数据保留与删除 | Data Resources Without Effective Retention Policy | plain number + collapsible table | 否 | 已确认 | 当前未匹配到有效 retention policy / lifecycle policy 的数据资源数量；并提供默认折叠的资源明细列表 | Azure Policy、Azure Storage lifecycle policies、Microsoft Purview Data Lifecycle Management |
| 3.5 数据跨境与共享（当前隐藏） | Cross-Border Transfers | plain number + sparkline | 否（当前隐藏） | 当前隐藏 | AI 相关数据跨地理或监管边界传输的事件数 | Microsoft Purview Audit、Microsoft Entra 跨租户 / 登录日志、Azure Data Factory access logs |
| 3.5 数据跨境与共享（当前隐藏） | Cross-Department Shared Datasets | plain number + stacked composition bar | 否（当前隐藏） | 当前隐藏 | 用于 AI 用例的跨部门共享数据集数量与结构 | Microsoft Purview Audit、Defender for Cloud Apps、Microsoft Entra cross-tenant logs |
| 3.5 数据跨境与共享（当前隐藏） | Unapproved Sharing | plain number + sparkline | 否（当前隐藏） | 当前隐藏 | 未经过要求审批流程的共享行为数量 | Microsoft Purview Audit、Defender for Cloud Apps、Power Automate approval records |
| 3.6 PII 使用（当前隐藏） | PII-Handling AI Systems | plain number | 否（当前隐藏） | 当前隐藏 | 处理个人可识别信息的 AI 系统数量 | Microsoft Purview Information Protection、Purview Data Map classification |
| 3.6 PII 使用（当前隐藏） | PII Use Cases | plain number + sparkline | 否（当前隐藏） | 当前隐藏 | 已记录的 PII 使用或转换场景数量 | privacy use-case registry、Dataverse / SharePoint Online 台账 |
| 3.6 PII 使用（当前隐藏） | PII Minimization Coverage | donut | 否（当前隐藏） | 当前隐藏 | 已部署 PII 最小化控制的系统占比 | Purview DLP、application data-handling metadata、Microsoft Purview Information Protection |

### 3.1-3.4 已确认 KPI 实施口径（开发参考）

说明：
- 以下口径对应当前已经确认的 `3.1`–`3.4`
- 默认统计周期为**最近 4 周**；涉及趋势的图形按**周**聚合
- `3.2.3` 与 `3.2.4` 按已确认要求来自**自定义数据库**
- 其余指标优先使用 **Microsoft 原生系统数据**，不依赖手工录入
- Azure 与 Purview 的资源对照，优先使用 `resourceId`；若 Purview 侧无法直接取到 Azure `resourceId`，则退化为 `resource name + resource group + normalized resource type` 做匹配

#### 3.1.1 Purview-Controlled vs AI-Tagged Azure Resources

- **设计逻辑**：同一张卡同时看“是否已受 Purview 控管”与“是否已显式标注 AI 用途”，帮助管理员快速发现纳管缺口和标签缺口。
- **来源系统**：
  - Microsoft Purview governed asset list / Data Map
  - Azure Resource Graph
  - Azure resource tags
- **需要抽取的关键字段**：
  - Azure：`resourceId`、资源名、`resourceGroup`、资源类型、tag `AI`、tag `Owner`
  - Purview：governed asset reference、资产名、资产类型、可回溯到 Azure 资源的标识
- **计算逻辑**：
  1. 只保留两类资源：**Azure 数据库**、**Azure 云存储**
  2. 从 Purview 取当前已纳管资源清单
  3. 从 Azure 取当前带 `AI` tag 的资源清单
  4. 以 `resourceId` 优先做 Purview / Azure 对照；缺失时用名称 + resource group + 类型做补充匹配
  5. 分别按“Azure 数据库 / Azure 云存储”输出：
     - Purview-controlled count
     - AI-tagged count
  6. 明细表输出 5 列：资源名、resource group、是否有 `AI` tag、是否受 Purview 控管、Owner

#### 3.1.2 Potential AI-Use Azure Resources Without AI Tag

- **设计逻辑**：找出很可能已经用于 AI，但尚未显式打 `AI` tag 的 Azure 数据资源，便于管理员直接追责和补标签。
- **来源系统**：
  - Azure Resource Graph
  - Azure resource group membership
  - Azure resource tags
- **需要抽取的关键字段**：
  - `resourceId`、资源名、`resourceGroup`、资源类型、tag `AI`、tag `Owner`
  - resource group 内资源清单
- **计算逻辑**：
  1. 先识别“AI 相关 resource group”：
     - resource group 中存在 AI 相关 Azure 资源，或
     - resource group 中任一资源带 `AI` tag
  2. 在这些 resource group 中，只保留 **Azure 数据库** 与 **Azure 云存储**
  3. 过滤出未带 `AI` tag 的资源
  4. 分别按“Azure 数据库 / Azure 云存储”统计数量
  5. 明细表输出 4 列：资源名、resource group、资源类型、Owner

#### 3.2.1 Potential Sensitive Data Consumer Applications

- **设计逻辑**：`Sensitive Data Use` 更应该回答“哪些应用正在直接或间接受敏感数据使用影响”，而不是只回答“数据是否已经被 classify”。本指标用 Purview classification 识别敏感数据资源，再用访问日志和应用调用图推断潜在敏感数据消费应用范围。
- **来源系统**：
  - Microsoft Purview classification / Data Map
  - Azure SQL Audit / Monitor logs
  - Azure Storage / Azure Files diagnostic logs
  - Application Insights / OpenTelemetry dependencies
  - Azure Resource Graph
  - Azure resource tags（`Owner`）
- **需要抽取的关键字段**：
  - Purview：data resource id / name、classification、resource type
  - DB / file access logs：data resource id / name、caller identity、access time
  - Application Insights / OpenTelemetry：caller application、callee application、dependency target、operation id、timestamp
  - Azure Resource Graph / tags：application resource mapping、tag `Owner`
- **计算逻辑**：
  1. 从 Purview classification 结果中识别包含敏感 classification 的 Azure DB / Azure file 资源
  2. 对 Azure DB 使用 Azure SQL Audit / Monitor logs，识别访问这些敏感数据资源的应用身份
  3. 对 Azure file / storage 使用 Azure Storage / Azure Files diagnostic logs，识别访问这些敏感文件资源的应用身份
  4. 将这些直接访问敏感数据资源的应用标记为 **Direct**
  5. 基于 Application Insights / OpenTelemetry dependencies 构建应用调用图
  6. 从 Direct 应用出发，沿调用图递归追踪所有依赖 Direct 应用的上游 / 传递应用，不限制 hop 数
  7. 将这些通过调用链关联到 Direct 应用的应用标记为 **Transitive**
  8. 对 `Direct ∪ Transitive` 应用按 application identity 去重，得到主 KPI 数值
  9. 主卡片同时展示两个资源类型拆分数字：
     - **DB-linked apps**：关联到敏感 Azure DB 的 potential sensitive data consumer applications 数量
     - **File-linked apps**：关联到敏感 Azure file / storage 的 potential sensitive data consumer applications 数量
  10. `DB-linked apps` 与 `File-linked apps` 是 **non-additive counts**；同一个应用如果同时关联 DB 与 file，可能同时计入两个拆分数字，因此两个数字不应相加得到 total
  11. Owner 从应用 Azure resource 的 `Owner` tag 获取；如果应用资源没有 `Owner` tag，可回退到 resource group 的 `Owner` tag；仍无法获取则显示 `Unknown`
  12. 默认折叠列表只输出 5 列：application Name、Owner、Type、data resource name、Classification

#### 3.2.2 Sensitive Data Category Mix

- **设计逻辑**：仅看 coverage 还不够，管理员还需要知道当前被识别出来的敏感数据主要是哪几类。
- **来源系统**：
  - Purview classification 结果
  - Microsoft Purview Information Protection
- **需要抽取的关键字段**：
  - 列标识
  - classification 名称 / 类型
  - classification 优先级或主分类标记（若一列命中多个 classification）
- **计算逻辑**：
  1. 以已完成 classification 的列为输入集合
  2. 每列只取一个用于聚合的**主 classification**
     - 优先使用系统提供的 primary classification
     - 若无 primary 字段，则按预设优先级取一个主类，避免重复累计导致占比超过 100%
  3. 按 classification 类别聚合列数
  4. 计算各类别占比，输出 stacked composition bar

#### 3.2.3 Top Requested Classifications

- **设计逻辑**：帮助管理员看到“哪些敏感数据类别最常被应用请求可见性”，这是实际使用压力而不是静态存量。
- **来源系统**：
  - 自定义 classified column visibility request 数据库
- **需要抽取的关键字段**：
  - request time
  - application / requester 标识
  - classification
  - request id
- **计算逻辑**：
  1. 取所选时间段内全部 visibility request 记录
  2. 按 classification 聚合 request 数量
  3. 排序后输出访问量最高的 top 3 classification
  4. 默认折叠表输出所有 classification 的访问量明细（classification、访问量）

#### 3.2.4 Data Mask Activity

- **设计逻辑**：帮助管理员看到过去一段时间中敏感数据保护动作是否真实发生，而不是只看是否存在静态 mask 配置。
- **来源系统**：
  - 自定义 mask request 数据库
- **需要抽取的关键字段**：
  - execution time
  - resource name
  - mask method
  - execution / request id
- **计算逻辑**：
  1. 取所选时间段内全部 mask execution 记录
  2. 统计总执行次数，作为主 KPI 数值
  3. 按周聚合 execution count，生成 sparkline
  4. 默认折叠表按资源聚合，输出：资源名、mask 次数、mask 方法

#### 3.3.1 Protected Sensitive M365 Items

- **设计逻辑**：只看“有多少敏感项目已被保护”比做一个难稳定的 coverage 分母更可操作，也更适合直接用 Purview 默认数据自动化提取。
- **来源系统**：
  - Microsoft Purview Content Explorer
  - Microsoft Purview Information Protection
  - SharePoint Online / OneDrive / Exchange Online metadata
- **需要抽取的关键字段**：
  - item id
  - location / workload（SharePoint / OneDrive / Exchange）
  - detected sensitive information types
  - sensitivity label / label name
- **计算逻辑**：
  1. 取 SharePoint Online、OneDrive、Exchange Online 中已被 Purview 检测到 sensitive information types 的项目
  2. 过滤出同时已存在 sensitivity label 的项目
  3. 以 `item id` 去重后统计数量
  4. 默认折叠表按 location 聚合，输出：Location、Protected Items、Primary Label

#### 3.3.2 M365 / Purview Exposure Alerts

- **设计逻辑**：这是当前首页 `Sensitive Data Exposure Alerts` 的已确认落地口径，优先用默认 Purview / M365 告警能力表达真实暴露风险。
- **来源系统**：
  - Microsoft Purview DLP / Alert Center
  - Purview Audit
- **需要抽取的关键字段**：
  - alert / case id
  - created time
  - location
  - policy / rule name
  - alert state（可选）
- **计算逻辑**：
  1. 取所选时间段内全部 M365 / Purview 暴露告警
  2. 以 alert / case id 去重，得到 unique alert cases
  3. 主 KPI 显示该时间段内 unique alert cases 总数
  4. 按周聚合 unique alert cases，生成趋势图
  5. 默认折叠表按 `location + policy / rule` 聚合，输出对应 alert cases

#### 3.4.1 Over-Retention Data Resources

- **设计逻辑**：帮助管理员直接看到“哪些数据资源已经超过批准保留周期但还没被处理”，这是明确的 retention 风险积压。
- **来源系统**：
  - Microsoft Purview Data Lifecycle Management
  - Azure Storage lifecycle policies
  - Purview retention state
- **需要抽取的关键字段**：
  - resource id / name / type
  - effective retention policy
  - approved retention period 或 retention end date
  - current retention state
- **计算逻辑**：
  1. 取当前在管的数据资源及其 effective retention policy
  2. 计算每个资源的批准保留截止时间
  3. 过滤出“当前时间已超过批准保留截止时间，且资源仍处于保留状态”的资源
  4. 统计资源数量，作为主 KPI
  5. 折叠表输出：资源名、资源类型、Days Over Retention

#### 3.4.2 Data Resources Without Effective Retention Policy

- **设计逻辑**：帮助管理员直接找到仍未真正挂上 retention / lifecycle policy 的资源，这是治理覆盖缺口而不是事件型风险。
- **来源系统**：
  - Azure Policy
  - Azure Storage lifecycle policies
  - Microsoft Purview Data Lifecycle Management
- **需要抽取的关键字段**：
  - resource id / name / type
  - retention policy assignment / lifecycle policy assignment
  - Azure Policy compliance state
  - current policy state
- **计算逻辑**：
  1. 取当前在管的数据资源
  2. 检查每个资源是否已匹配到有效 retention policy 或 lifecycle policy
  3. 将以下情况计入：
     - 没有任何 policy assignment
     - assignment 存在但无效
     - Azure Policy 显示 non-compliant，导致实际无有效保留控制
  4. 统计资源数量，作为主 KPI
  5. 折叠表输出：资源名、资源类型、Current Policy State

## 4. AI 安全防护

二级页面应覆盖一级页面指标：**AI Resources in Unhealthy State**；**Open High/Critical Defender Recommendations**

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 4.1 Prompt / 输入攻击防护 | Prompt Injection 检测率 | donut | 是 | 待确认 | 已检测到输入攻击尝试的识别覆盖率 | Azure AI Content Safety、Application Insights / Log Analytics、Microsoft Defender for Cloud（AI security posture） |
| 4.1 Prompt / 输入攻击防护 | 拦截率 | bullet bar | 是 | 待确认 | 已检测攻击中被成功阻断的比例 | Azure AI Content Safety、Azure API Management、Application Insights / Log Analytics |
| 4.1 Prompt / 输入攻击防护 | 未加输入防护系统数 | plain number | 是 | 待确认 | 尚未启用输入攻击防护控制的系统数量 | Microsoft Defender for Cloud（AI security posture）、Azure Resource Graph |
| 4.2 访问控制与凭据保护 | 未启用鉴权系统数 | plain number | 是 | 待确认 | 未启用合规身份验证控制的系统数量 | Microsoft Entra ID、Azure RBAC、Microsoft Defender for Cloud |
| 4.2 访问控制与凭据保护 | 过度权限集成数 | plain number | 是 | 待确认 | 拥有超出需要权限的集成连接数量 | Azure RBAC、Microsoft Entra 企业应用/API 权限、Microsoft Defender for Cloud |
| 4.2 访问控制与凭据保护 | 密钥泄露事件数 | plain number + sparkline | 是 | 待确认 | 检测到的密钥或凭据泄露事件数量 | Azure Key Vault 诊断日志、Microsoft Defender for Cloud、Microsoft Sentinel |
| 4.3 模型接口与运行面安全 | 暴露公网模型端点数 | plain number | 是 | 待确认 | 直接暴露在公网的模型或推理端点数量 | Azure API Management、Azure Front Door WAF、Azure Resource Graph |
| 4.3 模型接口与运行面安全 | 未限流接口数 | plain number | 是 | 待确认 | 未配置速率限制的关键接口数量 | Azure API Management、Microsoft Defender for Cloud |
| 4.3 模型接口与运行面安全 | 异常调用率 | plain number + sparkline | 是 | 待确认 | 超出正常模式的模型调用占比或趋势 | Azure Monitor / Log Analytics、Azure API Management |
| 4.4 滥用防护（后置） | 恶意提示尝试数 | plain number + sparkline | 是 | 待确认 | 检测到的恶意或规避型提示尝试数量 | Azure AI Content Safety、Microsoft Sentinel |
| 4.4 滥用防护（后置） | 违规内容请求数 | plain number + sparkline | 是 | 待确认 | 触发违规内容策略的请求数量 | Azure AI Content Safety、Defender for Cloud Apps |
| 4.4 滥用防护（后置） | 账号滥用率 | donut | 是 | 待确认 | 被判定存在滥用风险的账号占比 | Microsoft Entra ID 风险日志、Defender for Cloud Apps |
| 4.5 工具调用与插件风险 | 高风险 tool use 数 | plain number | 否 | 待确认 | 触发高风险判定的工具调用次数 | Azure AI Foundry Agent Service、Azure Monitor |
| 4.5 工具调用与插件风险 | 外联调用数 | plain number | 否 | 待确认 | 调用外部系统或互联网资源的工具调用次数 | Copilot Studio、Azure Monitor、Microsoft Entra 企业应用/API 权限 |
| 4.5 工具调用与插件风险 | 未限制工具权限数 | plain number | 否 | 待确认 | 未设置明确工具权限边界的配置项数量 | Azure AI Foundry Agent Service、Copilot Studio、Microsoft Entra 企业应用/API 权限 |

## 5. 输出可信与内容溯源

二级页面应覆盖一级页面指标：**Grounded Response Rate**；**Synthetic Content Labeling Gaps**

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 5.1 输出准确性与事实性 | 幻觉率 | donut | 是 | 待确认 | 输出中被判定为无依据或事实错误的比例 | Azure AI Foundry Evaluations、Application Insights、Dataverse / Power Apps 反馈记录 |
| 5.1 输出准确性与事实性 | 事实核验失败率 | donut | 是 | 待确认 | 经事实核验后判定失败的输出占比 | Azure AI Foundry Evaluations、Dataverse / Power Apps 反馈记录 |
| 5.1 输出准确性与事实性 | RAG grounding 命中率 | donut | 是 | 待确认 | 输出成功命中检索证据或批准来源的比例 | Azure AI Search 检索日志、Azure AI Foundry Evaluations、Application Insights |
| 5.2 合成内容标识 | 水印覆盖率 | donut | 是 | 待确认 | 生成内容中已应用水印或同等标识的比例 | Azure AI Vision / Video Indexer、Azure Blob Storage metadata、Application Insights |
| 5.2 合成内容标识 | 检测成功率 | donut | 是 | 待确认 | 已标识内容被检测流水线正确识别的比例 | Azure AI Content Safety、Azure AI Vision / Video Indexer |
| 5.2 合成内容标识 | 未标识合成内容数 | plain number + sparkline | 是 | 待确认 | 缺少 AI-generated label / disclosure 的生成内容数量 | Application Insights、Azure Blob Storage metadata、Azure AI Vision / Video Indexer |
| 5.3 信息完整性与 deepfake 风险 | 可疑深伪内容数 | plain number | 是 | 待确认 | 被判定为可疑深伪的内容数量 | Azure AI Vision / Video Indexer、Microsoft Sentinel |
| 5.3 信息完整性与 deepfake 风险 | 来源不明内容占比 | donut | 是 | 待确认 | 无法追溯来源或 provenance 的内容占比 | Purview Audit、多媒体检测流水线日志、Dataverse provenance 台账 |
| 5.3 信息完整性与 deepfake 风险 | 篡改检测命中数 | plain number + sparkline | 是 | 待确认 | 检测到疑似篡改或完整性破坏的命中数量 | Azure AI Vision / Video Indexer、多媒体检测流水线日志（Azure Functions / Logic Apps）、Microsoft Sentinel |
| 5.4 内容溯源与 provenance | 带 provenance/metadata 输出占比 | donut | 否 | 待确认 | 输出中附带 provenance 或 metadata 的比例 | Azure Blob Storage metadata / index tags、Azure Event Grid、Dataverse provenance 台账 |
| 5.4 内容溯源与 provenance | 可追溯内容占比 | donut | 否 | 待确认 | 能够追溯到明确来源链路的内容占比 | Microsoft Purview Audit、Dataverse provenance 台账、Azure Event Grid |
| 5.5 偏差/稳定性/人机协同（后置） | 输出波动率 | plain number + sparkline | 否 | 待确认 | 相同输入下输出结果不稳定的程度 | Azure AI Foundry Evaluations、Application Insights |
| 5.5 偏差/稳定性/人机协同（后置） | 人工复核推翻率 | donut | 否 | 待确认 | 人工复核后被推翻的输出占比 | Dataverse 人工复核队列、Power BI 评测结果集 |
| 5.5 偏差/稳定性/人机协同（后置） | 偏差样本率 | donut | 否 | 待确认 | 评测样本中触发偏差判定的比例 | Azure AI Foundry Evaluations、Power BI 评测结果集 |

## 6. 验证、审计与合规保证

二级页面应覆盖一级页面指标：**Required Validation Coverage**；**Open High-Risk Findings**

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 6.1 基线评测与控制验证 | 已完成基线评测系统占比 | donut | 是 | 待确认 | 已完成要求中的 baseline evaluation 的系统占比 | Azure AI Foundry Evaluations、Azure DevOps Test Plans |
| 6.1 基线评测与控制验证 | 控制有效率 | donut | 是 | 待确认 | 已验证控制中被判定有效的比例 | Azure Policy、Microsoft Defender for Cloud、Azure AI Foundry Evaluations |
| 6.1 基线评测与控制验证 | 失败控制数 | plain number | 是 | 待确认 | 当前验证失败的控制项数量 | Azure Policy、Azure DevOps Test Plans、Microsoft Defender for Cloud |
| 6.2 红队与对抗测试 | 红队覆盖率 | donut | 是 | 待确认 | 已完成红队/对抗测试的系统占比 | Azure DevOps Test Plans、Azure AI Foundry 评测运行记录 |
| 6.2 红队与对抗测试 | 高危发现数 | plain number | 是 | 待确认 | 红队或对抗测试中产出的高危发现数量 | Azure DevOps Work Items、Microsoft Sentinel 演练记录 |
| 6.2 红队与对抗测试 | 复测通过率 | donut | 是 | 待确认 | 整改后通过复测的高风险问题占比 | Azure DevOps Work Items、Azure AI Foundry 评测运行记录 |
| 6.3 合规检查与审计发现 | 合规缺口数 | plain number | 是 | 待确认 | 当前识别到的合规缺口数量 | Microsoft Purview Compliance Manager、Azure Policy 合规结果 |
| 6.3 合规检查与审计发现 | 审计发现数 | plain number | 是 | 待确认 | 来自内部/外部审计活动的发现数量 | Purview Audit、审计发现台账 |
| 6.3 合规检查与审计发现 | 高优先级未关闭项 | plain number + sparkline | 是 | 待确认 | 尚未关闭的高优先级合规/审计问题数量 | Defender for Cloud Regulatory Compliance、Purview Audit、Azure DevOps Work Items |
| 6.4 证据与可审计性 | 证据链完整率 | donut | 是 | 待确认 | 拥有完整评测、审批、日志证据链的系统占比 | Microsoft Purview Audit、Azure Monitor / Log Analytics、Azure DevOps 审批记录 |
| 6.4 证据与可审计性 | 缺少评测/审批/日志证据的系统数 | plain number | 是 | 待确认 | 缺失关键可审计证据的系统数量 | Microsoft Entra 审计日志、Azure DevOps 审批记录、Microsoft Purview Audit |
| 6.5 发布准入（后置） | 未满足 gate 发布次数 | plain number | 否 | 待确认 | 未满足发布 gate 仍尝试发布的次数 | Azure DevOps Pipelines / Environments、Azure Policy |
| 6.5 发布准入（后置） | 例外发布次数 | plain number | 否 | 待确认 | 通过例外流程放行的发布次数 | Azure DevOps Pipelines / Environments、Power Automate 审批记录 |
| 6.5 发布准入（后置） | go/no-go 拒绝率 | donut | 否 | 待确认 | 发布评审中被判定为 no-go 的比例 | Azure DevOps Pipelines / Environments、Azure Deployment History、Microsoft Defender for DevOps |

## 7. 运行事件、响应与整改

二级页面应覆盖一级页面指标：**AI Incidents This Week**；**Average Closure Time**

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 7.1 事件管理 | 事件数量 | plain number + sparkline | 是（仅做假数据） | 待确认 | 当前周期内 AI 相关事件总数 | Microsoft Sentinel、Microsoft Defender XDR、Azure Monitor Alerts、Microsoft Purview Alert Center |
| 7.1 事件管理 | 严重度分布 | stacked bar | 是（仅做假数据） | 待确认 | 按严重度拆分的事件结构 | Microsoft Sentinel、Microsoft Defender XDR |
| 7.1 事件管理 | 按类型分布（隐私/安全/内容） | stacked bar | 是（仅做假数据） | 待确认 | 按事件类型拆分的结构分布 | Microsoft Purview Alert Center、Microsoft Sentinel、Azure Monitor Alerts |
| 7.2 响应与处置时效 | MTTD | plain number + bullet bar | 是（仅做假数据） | 待确认 | 从发生到发现的平均耗时 | Microsoft Sentinel 事件时间线、Defender XDR 处置记录 |
| 7.2 响应与处置时效 | MTTR | plain number + bullet bar | 是（仅做假数据） | 待确认 | 从发现到完成处置的平均耗时 | Microsoft Sentinel 事件时间线、Azure DevOps Boards |
| 7.2 响应与处置时效 | SLA 达标率 | donut | 是（仅做假数据） | 待确认 | 在 SLA 内完成响应/处置的比例 | Azure DevOps Boards、Power Automate 审批/通知日志 |
| 7.2 响应与处置时效 | 超时工单数 | plain number | 是（仅做假数据） | 待确认 | 超过 SLA 未完成的工单数量 | Azure DevOps Boards、Power Automate 审批/通知日志 |
| 7.3 整改闭环 | 未关闭整改数 | plain number | 是（仅做假数据） | 待确认 | 当前仍未关闭的整改项数量 | Azure DevOps Boards / Work Items、Dataverse 整改台账 |
| 7.3 整改闭环 | 超期整改数 | plain number | 是（仅做假数据） | 待确认 | 超出要求期限仍未完成的整改项数量 | Azure Policy remediation tasks、Azure DevOps Boards / Work Items |
| 7.3 整改闭环 | 重复发生率 | donut | 是（仅做假数据） | 待确认 | 同类事件再次发生的比例 | Dataverse 整改台账、Defender for Cloud 建议、Azure DevOps Boards / Work Items |
| 7.4 事件披露与通报 | 已披露事件数 | plain number | 是（仅做假数据） | 待确认 | 已完成对内或对外披露的事件数量 | Dataverse / SharePoint Online 披露台账、Microsoft Sentinel 事件记录 |
| 7.4 事件披露与通报 | 待披露事件数 | plain number | 是（仅做假数据） | 待确认 | 尚未完成披露决策或动作的事件数量 | Dataverse / SharePoint Online 披露台账、Purview Audit |
| 7.4 事件披露与通报 | 对内/对外通报时效 | bullet bar | 是（仅做假数据） | 待确认 | 对内或对外通报相对于目标时限的达标情况 | Teams / Power Automate 通知记录、Dataverse / SharePoint Online 披露台账 |

## 8. 治理监督与控制执行

二级页面应覆盖一级页面指标：**On-Time Governance Actions**；**Open Exceptions / Risk Acceptances**

| 二级目录 | 指标 | 图形 | 是否本期实现 | 设计确认状态 | 指标解释 | 指标数据来源 |
|---|---|---|---|---|---|---|
| 8.1 治理动作执行 | 风险评审完成率 | donut | 是（仅做假数据） | 待确认 | 在规定周期内完成风险评审的比例 | Microsoft Purview Compliance Manager、Dataverse / SharePoint Online 治理任务台账 |
| 8.1 治理动作执行 | 政策确认率 | donut | 是（仅做假数据） | 待确认 | 已完成政策确认或再确认的比例 | Azure DevOps Approvals、Dataverse / SharePoint Online 治理任务台账 |
| 8.1 治理动作执行 | 必做控制完成率 | donut | 是（仅做假数据） | 待确认 | 要求执行的治理控制中已完成的比例 | Azure Policy、Microsoft Purview Compliance Manager、Dataverse / SharePoint Online 治理任务台账 |
| 8.2 例外与风险接受 | 例外申请数 | plain number | 是（仅做假数据） | 待确认 | 当前周期提交的治理例外申请数量 | Azure Policy exemptions、Power Automate 审批记录 |
| 8.2 例外与风险接受 | 风险接受数 | plain number | 是（仅做假数据） | 待确认 | 当前仍处于有效状态的风险接受数量 | Dataverse / SharePoint Online 风险接受台账、Microsoft Defender for Cloud exemptions |
| 8.2 例外与风险接受 | 长期未复核例外数 | plain number + sparkline | 是（仅做假数据） | 待确认 | 超过复核周期但尚未复核的例外数量 | Dataverse / SharePoint Online 风险接受台账、Power Automate 审批记录 |
| 8.3 责任与组织覆盖（后置） | owner 覆盖率 | donut | 否（仅做假数据） | 待确认 | 关键治理对象中已明确 owner 的比例 | Microsoft Entra ID、Dataverse / SharePoint Online RACI 台账 |
| 8.3 责任与组织覆盖（后置） | 责任矩阵完整率 | donut | 否（仅做假数据） | 待确认 | RACI 矩阵中关键角色完整配置的比例 | Azure RBAC、Dataverse / SharePoint Online RACI 台账 |
| 8.3 责任与组织覆盖（后置） | 治理委员会覆盖范围 | donut | 否（仅做假数据） | 待确认 | 已纳入治理委员会视野的业务单元或资产范围占比 | M365 Groups / Teams、Dataverse / SharePoint Online RACI 台账 |
| 8.4 风险分级与优先级（后置） | 高风险系统占比 | donut | 否（仅做假数据） | 待确认 | 被判定为高风险的系统占全部纳管系统的比例 | Dataverse / SharePoint Online 风险台账、Microsoft Purview Compliance Manager |
| 8.4 风险分级与优先级（后置） | 未复评高风险系统数 | plain number | 否（仅做假数据） | 待确认 | 超过复评周期仍未重新评估的高风险系统数量 | Dataverse / SharePoint Online 风险台账、Azure Policy 合规趋势 |
| 8.4 风险分级与优先级（后置） | 分级变更频次 | plain number + sparkline | 否（仅做假数据） | 待确认 | 一定时期内风险分级发生变化的次数 | Dataverse / SharePoint Online 风险台账、Defender for Cloud |
| 8.5 培训与宣导（后置） | 强制培训完成率 | donut | 否（仅做假数据） | 待确认 | 被要求参加强制治理/安全培训的人员中已完成的比例 | Microsoft Viva Learning、SharePoint Online 学习记录 |
| 8.5 培训与宣导（后置） | 关键角色培训覆盖率 | donut | 否（仅做假数据） | 待确认 | 关键治理角色已完成相关培训的覆盖比例 | Microsoft Entra ID 组分配、Power BI 培训报表、Microsoft Viva Learning |

## 已按要求后置的话题

- 责任与风险分级 -> 8.3 / 8.4
- 滥用防护 -> 4.4
- CI/CD、上线前 gate、go/no-go、发布准入 -> 6.5
- 人机协同、偏差、稳定性 -> 5.5
