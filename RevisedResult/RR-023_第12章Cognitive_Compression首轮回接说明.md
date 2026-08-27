# RR-023：第12章 Cognitive Compression 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第12章 Cognitive Compression 与 Human Decision Interface](../OptimizedDocs/第12章_Cognitive_Compression与Human_Decision_Interface_首轮修订稿.md)
- 原始结构：[全书大纲第12章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 新增材料：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 审阅依据：[RR-021](RR-021_Human_Control_Plane与认知控制架构审阅.md)
- Evidence：[ER-20260824-002](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)
- 核心 Claim：`CLM-C12-001`，`accepted + narrowed`，Evidence Coverage 为 `partial`
- 记录性质：章节回接说明，不是新的 Evidence Receipt
- 章节措辞状态：`unreviewed`

## 回接结果

第12章已经形成独立工作稿。

中心定义被固定为：

> Human Control Plane 是 Control and Evidence Plane 在具名决策上的 non-authoritative human-facing projection。

它可以选择、转换、路由和呈现已有 State Claim、Evidence、Authority、Risk、Exception 与 Recovery 信息，也可以调用已有的 Authority-bearing Action Path。

它不能：

- 产生新的 Truth；
- 将 Evidence 自动转换为 Decision；
- 生成 Reliance Disposition；
- 授予 Authority；
- 成为新的 Memory、Telemetry 或 State Store；
- 把 `no alert` 转换成全局健康声明。

## 原大纲内容保留情况

| 原大纲主题 | 新工作稿落点 | 处理 |
|---|---|---|
| 压缩目标 | 12.1–12.4 | 增加 Decision Target、Source、Scope、Unknown 与 Projection Contract |
| Progressive Disclosure | 12.5 | 保留；强调不同层级不能改变 Claim 和 Disposition 语义 |
| Change Narrative | 12.6 | 保留；拆分 Fact、Judgment、Inference 与 Recommendation |
| Architecture Impact View | 12.7 | 保留；新增 Observed、Inferred 与 Unobserved |
| Risk Map | 12.8 | 保留；定义为 Risk Claim 的投影，不使用统一自动裁决分数 |
| Decision Surface | 12.9 | 保留；绑定 Authority、选项、Non-effect、Deadline 与 Recovery |
| Compression 的可信问题 | 12.13–12.14 | 改为八类 Compression Validation 与共同模式故障检查 |
| Human Cognitive Authority | 12.15 | 拆成 Interface Capability 与 Authority-bearing Action |

原大纲主题均有承接，但没有保留会导致对象所有权混淆的表达。

## 新增的章节骨架

### 1. 适用条件

工作稿明确：HCP 是可选接口，不是 AI-native 项目的定义门槛。

小型项目、低频任务和高风险专家审阅可能更适合直接 Review；底层 Source、Evidence 与 Authority 尚未工程化时，也不应先建设 HCP。

### 2. Projection Contract

新增最小 Contract，要求声明：

- Projection Identity、Generated At 与 Expiry；
- Decision Target 与 Intended Use；
- Subject、Candidate 与 Baseline；
- State Claim 与 Evidence 引用；
- Counterevidence、Coverage 与 Unknown；
- Observation Freshness 与 Detector Health Reference；
- Available Action 与 Authority Reference；
- Drill-down Source Index。

示例明确标为设计 Profile，不是通用 Schema。

### 3. Brief 与 Attention Routing

Project / Production Brief、Control Brief 和 Learning / Evolution Brief 被保留为可选 View，而不是三个新数据库。

工作稿将 `Exception-driven` 收窄为：

> 在已声明、仍新鲜且 Detector Health 正常的观测覆盖内，没有检测到需要当前角色介入的具名异常。

`Silence should mean healthy` 没有进入正文。

### 4. HJL 与 TTE

HJL 被写成分项候选观测，需要同时考虑 Decision Class、Age、Judgment Time、Rework 与 Escaped Incident。

TTE 被绑定到具名角色、Decision Class、准确性和完整性标准。固定五分钟目标和 North-star Metric 表述被撤回。

### 5. Compression Validation

工作稿新增：

1. Source Binding；
2. Scope Preservation；
3. Epistemic Separation；
4. Counterevidence and Unknowns；
5. Coverage and Freshness；
6. Drill-down Fidelity；
7. Action Correctness；
8. Omission Testing。

这使 Cognitive Compression 自身成为可审阅对象，而不是默认可信的 AI Summary。

### 6. 最小实现

建议从一个高成本 Decision Path 建立闭环，不一次建设 Trust Engine、Telemetry Platform、Workflow Optimizer 和 Learning Center。

扩张条件是 Projection 在真实任务中反复有用，并且维护成本、漏报、误报和返工得到观察。

## Evidence 回接边界

正文只使用 ER-20260824-002 已记录的窄证据：

- v4.94 task-level non-authoritative read model；
- blocker、handoff、cancel、claim withdrawal 和 review rejection 路径；
- D-048 target non-result 对“无正常结果不等于健康”的支持；
- SP122 对 Evidence Acceptance、Adoption 与 Production Disposition 分离的支持。

正文明确保留：

- 没有完整 HCP 实现；
- 没有全局 takeover、delegation revocation 或 Detector Health interface；
- 没有 HJL、TTE、事故率、返工或 Review 时间对照；
- 没有证据证明 HCP 优于直接 Review；
- Evidence Coverage 仍为 `partial`。

## 有意不进入本章的内容

- HCP 拥有 Constitution、Authority、Decision Ledger、Trust、Memory、Telemetry 与 Workflow；
- 固定 Truth Mapping；
- Trust Engine 或 Trust Score；
- 固定五层 Progressive Disclosure；
- `SYSTEM STABLE` 作为全局健康声明；
- `Silence should mean healthy`；
- 固定五分钟 TTE；
- HJL 作为已验证 North-star Metric；
- “所有 Human 都能覆盖所有 Policy”；
- UI Button 自行产生 Authority；
- 一次建设完整 HCP 平台；
- v4.94 已验证完整 Human Control Plane。

## 与后续章节的接口

- 第13章拥有 Authority Grant、Delegation、Autonomy Profile、Revocation 与 Takeover；
- 第14章拥有 Telemetry Source、Observation Coverage、Detector Health、Exception Lifecycle 与 Intervention；
- 第15章拥有 Memory Promotion、Retrieval、Conflict 与 Expiry；
- 第16章拥有 Workflow Candidate、Baseline、Calibration 与 Recovery Decision。

第12章只负责把这些对象投影到 Human Decision Interface，不改变它们的 Owner。

## 当前审阅点

核心 Claim 已接受，但章节措辞和篇幅尚未单独裁决。下一轮审阅应重点检查：

1. Projection Contract 是否过重；
2. Progressive Disclosure 示例是否需要进一步压缩；
3. Change Narrative、Architecture Impact 和 Risk Map 是否与第9、10章重复；
4. Brief 是否适合保留为正文主体，还是移入附录模板；
5. HJL 与 TTE 是否应保留在本章或移动到第20章；
6. v4.94 案例篇幅是否与 `partial` Coverage 相称；
7. 第12章是否为第13、14章保留了足够清楚的对象所有权。

## Human Disposition

- 章节逻辑与措辞：`unreviewed`
- Decision by：pending
- Decision at：pending
- Rationale：核心 Claim 已接受；本记录等待作者对第12章工作稿本身作出接受、收窄或继续修改的裁决。
