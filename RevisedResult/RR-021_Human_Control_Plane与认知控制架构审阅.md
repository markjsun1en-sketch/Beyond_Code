# RR-021：Human Control Plane 与认知控制架构审阅

- 记录日期：2026-08-24
- 审阅对象：[Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)
- 讨论来源：[共享讨论](https://chatgpt.com/share/6a8bb8da-140c-83ea-922a-61a024af423b)
- 对照正文：[第3章](../OptimizedDocs/第3章_AI原生软件工程定义_首轮修订稿.md)、[第6章](../OptimizedDocs/第6章_Truth与State_Architecture_重构稿.md)、[第9章](../OptimizedDocs/第9章_Evidence_Use与Decision_Disposition边界稿.md)
- 工程证据：AI Game Dev OS v4.94、lessismore SP122
- Evidence：[ER-20260824-001](../Evidence/receipts/ER-20260824-001__CLM-C11-001.md)、[ER-20260824-002](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)、[ER-20260824-003](../Evidence/receipts/ER-20260824-003__CLM-C16-001.md)
- 审阅方式：Evidence Curator 与 Critical Reviewer 独立只读分析，主任务核对并整合
- 记录性质：跨章概念审阅、Evidence 边界与后续修改依据
- Human Disposition：三条核心 Claim 已接受，并保留 `split / narrow` 边界

## 核心结论

这份新材料对《Beyond Code》有调整意义，但调整对象是第11–16章的概念边界和接口设计，不是全书结构。

综合结论为：

- **概念价值较高**：它把“作者为什么开始失去实现级掌控感”组织为 Output、State、Dependency、Judgment 和 Meta-level Overload，并把人的角色迁移、Attention Routing、Brief 与 Workflow Calibration 串成一条可讨论的推导链。
- **跨章影响中等**：现有第11–16章已经有承接位置；没有证据支持新增一章，也不应把 Human Control Plane 提升成覆盖现有架构的超级层。
- **独立证据价值较低**：共享讨论和本地整合稿属于同一语义来源链，不能互相证明。AI Game Dev OS 与 lessismore 能支持若干窄机制和反例，但尚未验证完整 HCP、HJL、TTE 或 Trust 模型的效果。

因此，当前处理是“吸收、拆分、收窄，并按已确认边界进入章节工作稿”，而不是直接把整篇文档并入正文。

## 与此前结论的关系

此前已经形成的结论是：

1. Control and Evidence Plane 是横切于两个工程系统的治理平面，不是第三套 Truth System；
2. Truth、State Claim、Evidence、Authority、Decision Disposition 必须保持类型边界；
3. Evidence 类型必须匹配 Claim、Scope、Risk 和 Intended Use，不能形成跨问题的通用强弱阶梯；
4. 线性成熟度阶梯容易把多维能力误写成单一路径。

本轮没有出现足以推翻这些结论的新事实。新材料的价值在于提出了一个面向人的接口问题；它必须被现有对象模型约束，而不能反向吞并现有模型。

## 三条正式 Claim

| Claim | 类型 | Evidence 覆盖 | 处置 | Human Disposition | 生效边界 |
|---|---|---|---|---|---|
| `CLM-C11-001`：当需人工判断的保留 AI 变更持续超过合格审阅容量时，逐项审阅不能单独维持控制 | inference | `partial` | `split` | `accepted` | 将“是否出现带宽失配”与“采用何种响应”拆开；不接受 AI 单因解释或 HCP 唯一解 |
| `CLM-C12-001`：HCP 是现有 Control and Evidence Plane 面向人的有边界投影 | recommendation | `partial` | `narrow` | `accepted` | 移除超级层、Truth Owner 和“沉默即健康”含义 |
| `CLM-C16-001`：重要且可恢复的 Workflow 变更是待验证候选，不因产生、合并或 Test PASS 自动成为 Improvement | recommendation | `partial` | `narrow` | `accepted` | 绑定适用范围、比较条件、Baseline 有效性和恢复可行性 |

## 证据身份与边界

### Beyond Code

- 采集时为 `main@cd842c6fd82fc8994f21d4ff761af7482bae106c`。
- Worktree 已有 13 项未提交变化；被审阅的 v0.1 文档自身为 untracked。
- 共享讨论未暴露可靠时间戳。
- 共享讨论与 v0.1 文档是一条讨论—整合来源链，只能作为作者体验、同期判断与理论形成过程的来源。

### AI_DEV_OS_Evolve

- 采集时为 `main@a99ace44a984e58e30c323d84d951d960fac6744`，worktree clean，未配置 upstream。
- v4.94 的 committed incident、transaction、implementation、test 与 closure 可以支撑具体历史和实现原语。
- v4.94 没有记录 HJL、TTE、人工审阅时间、告警漏报率或 HCP 前后对照。

### lessismore

- 采集时为 `codex/sp128-g0-g6-checkpoint@66b7d3aefdc0f3f2224a379d819e2540abffb3f9`，worktree clean，未配置 upstream。
- SP122 的 Human qualifying review 支持“用有边界证据链做人工裁决”，同时构成对“人已无法直接审阅”的反向证据。
- SP122 与 AI Game Dev OS 共享方法和工具背景，不应被当作完全独立的行业样本。

## 必须保持的认识论分层

### 可观察事实

- v4.94 包含跨代码、测试、Schema、规则、工作流、状态、Memory 与 Evidence 的广泛工程表面。
- D-073 至 D-075 增加了治理和审阅对象，却没有产生 source、runtime、test 或 qualification 进展。
- v4.94 已存在 non-authoritative read model、blocker/handoff aggregation、cancel、claim withdrawal 和 review rejection 等局部控制原语。
- D-048 在目标执行前发生 verifier self-mutation，没有产生正常目标结果；“没有正常结果”没有表示健康。
- D-079 的 42 个 selected tests 通过，但候选范围仍被 Human 拒绝；后续较小的 forward correction 成为继续使用的 Baseline。
- SP122 接受 qualifying evidence 的同时，仍将 adoption 和 production 保持为未批准。

### 同期判断

- 作者记录了实现级理解和逐项审阅带来的控制感下降。
- v4.94 将 D-073 至 D-075 序列判断为 Governance Livelock。
- Human 在 D-076、D-079 和 SP122 中保留了最终范围或 Evidence disposition。

### 事后推导

- 认知负担可能来自“需要人工判断的保留变更”与“合格审阅容量”的持续失配。
- v4.94 的负担也可能来自工作流膨胀、生命周期耦合、文档债、治理对象过多、多任务并发或改变规模，而不只是 AI 生成速度。
- 将当前状态、风险、Evidence 和 Authority 压缩为面向人的投影，可能比展示所有内部对象更适合部分长期委托系统。

### 当前建议

- 把 HCP 定义为接口契约，不定义为新的权威系统。
- 将 Trust、Authority 与 Autonomy 拆成不同对象。
- 将 Workflow 变化视为有边界的 Candidate，并保留合适的比较或恢复路径。
- 将 HJL、TTE 和异常路由先写成待验证设计，而不是已验证指标体系。

## 对象模型修正

### 1. Human Control Plane 不是“超级平面”

v0.1 把 Constitution、Authority、Decision Ledger、Trust、Known-Good、Rollback 和 Attention 都放入 HCP，容易让读者理解为 HCP 拥有这些对象。这个含义与第3章既有的 Control and Evidence Plane 冲突。

建议对象关系为：

~~~text
Truth / State Claim owner
Evidence records and Evidence Use
Authority grants and Decision Disposition
Telemetry / Detector / Recovery records
                    │
                    ▼
Human Control Plane
= non-authoritative human-facing projection
  + attention routing
  + source-linked drill-down
  + authorized control actions
~~~

HCP 可以汇总、路由和发起有权动作，但不能复制后变成第二套 Truth、Authority、Memory 或 Evidence Store。

### 2. Trust、Authority 与 Autonomy 必须拆开

`Assured Trust`、`Earned Trust` 和 `Earned Autonomy` 混合了结构保障、运行证据、依赖判断和权限授予。建议改成：

~~~text
Structural Assurance
+ Operational Evidence
→ supports a scoped Reliance Disposition

Authority Grant
→ permits named actions or decisions

Autonomy Profile
→ operationalizes delegated Authority
  under stated scope, risk and revocation conditions
~~~

- Structural Assurance 描述机制、隔离、验证与恢复能力。
- Operational Evidence 描述具名版本和环境中的实际观察。
- Reliance Disposition 表示在指定 Capability、Configuration、Scope、Environment、Time 与 Intended Use 下是否可以依赖。
- Authority 决定谁可以采取或裁决哪些动作。
- Autonomy 是 Authority 的可撤回运行配置，不是系统靠成功历史自动“挣得”的固有属性。

如果正文保留 `Trust`，它只能作为 scoped reliance 的短名，不能作为全局分数或权限来源。

### 3. Truth 映射不能固定成项目通用层级

v0.1 中的多级 Truth 映射可作为某个系统的示例 Profile，不能写成 AI-native 工程的固定层级。第6章已经要求 Source of Truth 绑定具体问题、Domain、版本、状态和冲突规则。

建议将固定层级改写为：

> HCP 展示与当前决策有关的 State Claim 及其 Source、Version、Scope、Freshness、Evidence 和 Conflict；它不重新定义全局 Truth 顺序。

### 4. Evidence 不能使用 Weak / Medium / Strong 通用阶梯

同一种 Evidence 对一个 Claim 直接，对另一个 Claim 可能完全无关。D-048 和 D-079 已经表明：

- exact inventory 可以回答 verifier integrity，却不能产生 target compile 结果；
- Test PASS 可以支持 selected behavior，却不能裁决实现范围、Acceptance、Adoption 或 Release。

因此第15节应改成 Claim-specific Evidence Portfolio 或 Coverage Map，不把 Production Metrics 自动放在 Diff、Static Analysis 或 Test 之上。

### 5. Known-Good 必须改成 scoped accepted baseline

`Known-Good` 容易暗示无条件和永久正确。建议正文使用：

> 在指定 Scope、Environment、Time 与 Intended Use 下被接受或资格化、且当前仍安全适用的 Baseline。

基线可能过期、不可比较或变得不安全。数据迁移、外部副作用和强制升级也可能只能前向恢复，因此“永远保留并可回滚”不能作为一般规律。

### 6. Silence 只能表示有边界的 non-detection

`Silence should mean healthy` 与文档自身关于“降低 interruption 可能来自漏报”的分析冲突。最小可辩护表达为：

> 在已声明、仍新鲜且 Detector Health 正常的观测覆盖内，没有检测到需要人工介入的具名异常。

HCP 必须显示：

- observation coverage；
- source freshness；
- detector health；
- unknown / unobserved surfaces；
- last successful observation；
- evidence drill-down。

没有这些字段，沉默只是“没有告警”，不是健康证明。

## HJL、TTE 与演化叙事

### HJL — Human Judgment Load

单纯统计“需要人决定几次”不能表示判断难度、风险、持续时间、漏报或事故代价。HJL 当前只能作为 Attention Routing 的候选观测量，并至少与以下信号联合：

- decision count by risk class；
- judgment time and waiting time；
- false negative / escaped incident；
- rework caused by compressed or missing context；
- interruption source；
- unresolved high-risk decision age。

在获得真实任务数据前，不应称其为 North-star Metric。

### TTE — Time To Explain

“五分钟内解释清楚”没有证据基础。快速但错误的解释不产生控制；复杂事故也可能需要更久。TTE 可保留为有约束的可用性探针：

~~~text
named user
+ named decision class
+ completeness / accuracy threshold
+ maximum acceptable explanation delay
~~~

不得把所有事件压成单一时间目标。

### Generation 1–4

线性代际叙事与第3章拒绝单轴成熟度阶梯的结论冲突。一个项目可以同时在不同 Capability 上使用 Copilot、Coder、Engineering System 和 Governed Delegation。

建议改为多维运行模式或 Capability Profile。是否需要 HCP 应由 Delegation、Risk、Scale、Observability 和 Recovery 条件触发，而不是由“进入 Generation 4”触发。

## Workflow Calibration 的保留边界

`Workflow Calibration` 有书内价值，但它并不是因为换了名称就成为新理论。它与版本化变更控制、实验设计、渐进采用和恢复机制高度重叠。

建议把其最小独立含义固定为：

> 判断一个可版本化 Workflow Candidate 是否适合当前阶段、风险、环境和 Intended Use，而不是寻找无条件最优流程。

适用前提：

- Workflow 重要且重复发生；
- Candidate 与 Baseline 在比较窗口内具有基本可比性；
- Objective 和 Guardrail 能形成具名 Claim；
- 变更可回滚或有可信前向恢复路径；
- 评估收益足以覆盖维护双路径和治理的成本。

不适用或需另行处理：

- 紧急安全修复；
- 强制 API / 数据格式迁移；
- 已经不安全的旧 Baseline；
- 低频且无法形成可比样本的流程；
- 不可逆外部副作用；
- 微小、局部且低风险的普通编辑。

v4.94 支持“Candidate 不等于 Improvement”和“Test PASS 不等于 Adoption”，但没有证明 Calibration 提高长期效率或质量。

## 章节落点

| 章节 | 建议吸收 | 不应吸收 |
|---|---|---|
| 第3章 | HCP 是 Control and Evidence Plane 的 human-facing projection | 新的第三工程系统或成熟度代际 |
| 第6章 | HCP 消费具名 State Claim、Source、Version、Scope、Freshness 与 Conflict | 固定 Truth 等级和全局 Trust State |
| 第8–10章 | Evidence drill-down、review independence、Human disposition | AI review 自动产生 Trust 或 Authority |
| 第11章 | 五类 overload；带宽失配必须写成有条件命题并列出替代解释 | “AI Output 必然超过 Human Review Capacity” |
| 第12章 | Progressive Disclosure、Brief、HJL/TTE 候选探针 | HCP 已经被证明能保持控制 |
| 第13章 | Authority、Autonomy、Stop、Downgrade、Takeover、Revocation | 成功历史自动授予 Autonomy |
| 第14章 | Telemetry Coverage、Freshness、Detector Health、Exception Routing | `Silence = healthy` |
| 第15章 | Memory 提供连续性但不产生 Truth；关注 memory-amplified error | LTM 作为 Trust 或 Authority 来源 |
| 第16章 | Workflow Candidate、scoped accepted baseline、Guardrail、Recovery | “永远 Known-Good”或一次成功即 Improvement |
| 第20章 | HJL/TTE 作为待验证的分项观测；同时记录安全与质量反指标 | 单一 North-star Score |
| 第23章 | D-048、D-073–075、D-076、D-079、SP122 的边界案例 | 用单项目宣称完整 HCP 已验证 |

## 必要、实用与可选

### 必要

- HCP 定义为非权威投影，不重新拥有 Truth、Evidence、Authority、Memory 或 Telemetry。
- Trust、Authority 和 Autonomy 拆成独立对象。
- 删除通用 Evidence 强弱阶梯和固定 Truth 层级。
- 将 `Silence should mean healthy` 改为带 Coverage、Freshness 和 Detector Health 的 non-detection。
- 将 Known-Good 改为有范围、有时效的 accepted / qualified Baseline。
- 第11章明确替代解释，不把认知负担单因归结为 AI。

### 实用

- 将五类 Cognitive Overload 放入第11章，作为诊断视角而不是已验证分类学。
- 第12章加入 Human Decision Interface contract。
- 第14章加入 Detector Health 与 unknown coverage。
- 第16章使用 D-076、D-079 解释 Candidate、Evidence 与 Disposition 分离。
- 第23章用失败—修正—非声明的时间序列承载案例。

### 可选

- Brief 的三种视图模板；
- HJL 与 TTE 的试验性埋点；
- Random Audit；
- Capability Profile；
- HCP UI 或 Dashboard 原型。

可选项不应在书中写成完成该架构的必要条件。

## 当前不进入正文的内容

- `Trust Score = 87.3` 或其他统一分数；
- `Assured Trust + Earned Trust = Total Trust`；
- `Earned Autonomy` 的自动升级叙事；
- Weak / Medium / Strong Evidence；
- `Silence should mean healthy`；
- 固定五级 Truth Mapping；
- 永久 Known-Good；
- 五分钟 TTE 目标；
- HJL 作为已验证 North-star Metric；
- Generation 1–4 线性成熟度路径；
- HCP 已降低事故、返工或认知负担的效果声明。

## 当前 revise 结论

这份材料最有价值的不是提出另一个架构中心，而是指出一个现有架构尚未回答清楚的接口问题：

> 当系统内部的 State、Evidence、Authority、Risk 和 Recovery 已经工程化后，人应通过什么有边界、可下钻、可干预的投影继续承担最终判断？

这个问题值得进入《Beyond Code》。当前证据只支持把 HCP 写成**待验证的 Human Decision Interface contract**，不支持把它写成已经验证的系统层。

本轮不修改 `OringinalDocs/` 或 `OptimizedDocs/`。作者裁决已经完成；当前 `OptimizedDocs/` 尚无第11–16章工作稿，下一步应先依据大纲和本记录建立第11章工作稿，再按“第12–14章收窄接口、第16章限定 Calibration”的顺序推进。

## Human Disposition

- `CLM-C11-001`：`accepted + split`
- `CLM-C12-001`：`accepted + narrowed`
- `CLM-C16-001`：`accepted + narrowed`
- Decision by：Human author
- Decision at：2026-08-24T14:20:08+08:00
- Rationale：作者确认采用本记录建议的收窄边界；接受不改变三条 Claim 的 `partial` Evidence 覆盖，也不把单项目案例提升为普遍证明。
