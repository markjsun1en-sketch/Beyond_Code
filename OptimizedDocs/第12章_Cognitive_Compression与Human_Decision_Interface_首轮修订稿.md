# 第12章 Cognitive Compression 与 Human Decision Interface
## 把系统复杂度转换为可判断、可下钻的投影

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-023](../RevisedResult/RR-023_第12章Cognitive_Compression首轮回接说明.md)。
> 适用边界：本章提出 Cognitive Compression 与 Human Decision Interface 的候选接口契约；现有案例只支持非权威投影、Evidence 与 Authority 分离及“没有正常结果或告警不等于健康”等局部边界，尚不证明 HCP 已降低判断负担、返工或事故，也不证明统一 HCP 架构普遍适用。

第11章讨论了一个条件式问题：

> 当需要人类判断的被保留变化持续超过合格审阅容量时，项目怎样恢复平衡？

限流、缩小 Scope、扩充 Reviewer、自动验证和风险分层都可能降低负担。

但在长期、跨工具、跨 Agent 的受托执行系统中，即使已经采取这些措施，人仍然需要面对大量 State、Evidence、Authority、Risk、Exception 和 Recovery 信息。

把所有原始日志、Diff、运行记录和治理对象直接展示给人，不等于透明，也不等于控制。

把它们压缩成一句 `SYSTEM STABLE`，同样不等于控制。

本章讨论两项相互约束的设计：

- **Cognitive Compression（认知压缩：把机器级工程状态转换为与当前决定相匹配、可追溯且可下钻的信息投影）**；
- **Human Decision Interface（人类决策接口：让有权角色定位待决问题、检查依据、理解限制并发起允许动作的交互表面）**。

这两项设计与后文 HCP 的关系是：Cognitive Compression 是转换机制，Human Decision Interface 是承载投影与动作入口的交互表面；第12.2节定义的 HCP 是组织这些 Interface 与 Projection 的一种可选方式。

两者共同解决的不是“怎样让人看到更少”，而是：

> **怎样让人只在第一层看到当前判断所需的信息，同时保留发现遗漏、质疑摘要和回到来源的能力？**

---

## 12.1 压缩的目标不是隐藏，而是形成决策层级

面向人的 Cognitive Compression 通常不会在第一层展示全部细节，因此始终存在信息损失、遗漏或误读风险。

如果压缩后的表面没有说明选择标准、来源和遗漏范围，信息减少可能只是把风险移出视野。

因此，本章所说的 Cognitive Compression 必须同时满足三项要求：

1. 面向具名 Decision Target 选择信息；
2. 保留 Source、Scope、Evidence、Unknown 和 Counterevidence；
3. 允许从摘要逐层下钻到产生它的原始对象。

基本关系是：

~~~text
Source records and observations
            ↓ select / transform
Non-authoritative projection
            ↓ present / route
Human or authorized decision
            ↓ invoke
Existing authority-bearing action path
~~~

压缩后的 Projection 不会因更容易阅读而获得更高权威。

它可以帮助人理解已有 Claim，也可以暴露已有 Authority，但不能：

- 把推断变成事实；
- 把 Evidence 变成 Decision；
- 把“没有告警”变成健康证明；
- 把摘要生成者变成 Source Owner；
- 把界面按钮变成新的 Authority Grant；
- 把旧数据伪装成当前 State。

一个适合本章的原则是：

> **Encapsulate Execution, Expose Evidence.**

它的中文语义不是“隐藏执行过程”，而是：

> 默认不暴露与当前判断无关的全部搜索和中间步骤，但显式暴露结果、Scope、Evidence、Unknown、Risk、必要 Trace 与下钻路径。

所以：

~~~text
Transparency
≠ Show everything

Transparency
= Expose what is required
  to verify, decide and intervene
~~~

---

## 12.2 不是所有项目都需要 Human Control Plane

**Human Control Plane（HCP，面向人的控制接口：Control and Evidence Plane 在具名决策上的非权威人机投影）** 是组织一个或多个 Human Decision Interface 及其 Projection 的可选方式，不是 AI-native 项目的定义门槛。

它更可能有用的条件包括：

- 存在多个长期受托执行路径；
- State、Evidence 与 Authority 分布在多个系统；
- 人不再逐项审阅所有低风险输出；
- 高影响决定需要跨对象汇总；
- 项目需要持续的暂停、否决、接管或撤销委托路径；
- 原始日志和 Dashboard 已经形成新的认知负担。

它可能不值得建设的条件包括：

- 项目规模小、状态简单；
- 直接 Review 更便宜、更可靠；
- 任务低频且每次差异很大；
- 关键变化必须由专家逐项检查；
- 底层 Source、Evidence 和 Authority 尚未工程化；
- 没有人负责维护 Projection 的正确性和时效。

如果底层记录本身不可靠，HCP 只会把不可靠信息压缩得更有说服力。

因此，Human Control Plane 不是治理基础设施的替代品，也不是用 UI 修复架构问题的方法。

---

## 12.3 Human Control Plane 只拥有投影，不拥有源对象

本书已经把 Product System、Production Intelligence System 与横切的 Control and Evidence Plane 分开。

HCP 不是第四个系统，也不是 Control and Evidence Plane 之上的超级层。

它消费已有对象：

| 被投影对象 | 权威来源或 Owner | HCP 可以做什么 | HCP 不能做什么 |
|---|---|---|---|
| Intent / Decision | Intent、Decision 或 Policy Record | 展示目标、约束与待决项 | 改写原始 Intent |
| State Claim | 具名 Source 与 Version | 展示 Claim、Scope、Freshness 与 Conflict | 声明新的全局 Truth |
| Evidence | Evidence Record 与 Artifact | 展示 Coverage、Use、Limitations 与 Counterevidence | 自动完成 Acceptance |
| Authority | Authority Grant、Role 与 Policy | 展示谁可执行哪项动作 | 仅凭按钮创造权限 |
| Risk | Risk Claim、Assessment 与 Owner | 汇总影响、暴露和可逆性 | 把评分当成事实 |
| Telemetry / Exception | Runtime、Observer 与 Detector | 展示观测结果、覆盖与未知 | 把未告警解释为健康 |
| Recovery | Versioned Baseline 与 Recovery Contract | 展示可用路径和前提 | 保证回滚一定成功 |
| Memory | Memory Source 与 Promotion Record | 展示相关历史与 Provenance | 把 Memory 当作当前 Truth |

对象关系可以写成：

~~~text
State / Evidence / Authority / Risk / Telemetry / Recovery
                         │
                         │ source-linked read
                         ▼
              Human-facing Projection
               ├─ attention routing
               ├─ progressive disclosure
               ├─ evidence drill-down
               └─ authorized action invocation
~~~

Projection 可以有自己的 Identity、Generation Time 和 Expiry，但这些字段描述的是 Projection 本身，不是被投影系统的 Truth。

---

## 12.4 Projection Contract 必须说明“它展示了什么”

**Projection（投影：从权威来源选择并转换出的、面向特定决定的非权威视图）** 需要一个最小 Contract。

下面只是设计示例，不是所有项目必须采用的 Schema：

~~~yaml
projection_id: HCP-PRJ-042
projection_type: decision_brief
generated_at: 2026-08-24T14:30:00+08:00
expires_at: 2026-08-24T18:30:00+08:00
generated_by: control-brief-builder-v3

decision_target:
  id: DEC-TARGET-091
  question: 是否接受 save migration candidate 的 qualifying evidence
  intended_use: qualifying_evidence_disposition
  deadline: 2026-08-25T12:00:00+08:00

subject:
  project: example-game
  candidate_ref: commit:abc123
  baseline_ref: commit:def456

state_claim_refs:
  - current_save_format_state

evidence:
  supporting_refs:
    - EV-TEST-041
    - EV-RUNTIME-019
  counterevidence_refs:
    - EV-REVIEW-007
  coverage_summary:
    covered:
      - bounded migration behavior
    not_covered:
      - production adoption

observation:
  as_of: 2026-08-24T14:20:00+08:00
  coverage_ref: OBS-COVERAGE-012
  detector_health_ref: DET-HEALTH-006
  unknowns:
    - legacy save population size

risk_and_impact:
  assessment_refs:
    - RISK-033

available_actions:
  - action: accept_qualifying_evidence
    authority_ref: AUTH-QUAL-002
  - action: request_more_evidence
    authority_ref: AUTH-QUAL-002
  - action: reject_scope
    authority_ref: AUTH-QUAL-002

drill_down:
  source_index_ref: SRC-IDX-091
  raw_artifact_refs:
    - ARTIFACT-201
~~~

这个 Contract 强制回答：

- 这份 Projection 为哪个决定生成；
- 它基于哪个 Candidate 与 Baseline；
- 数据截至何时；
- 哪些 Claim 有什么 Evidence；
- 哪些范围没有覆盖；
- 存在哪些反证与未知；
- 当前有哪些动作；
- 每项动作从哪里获得 Authority；
- 如何回到 Source。

如果一个 Brief 不能回答这些问题，它更接近叙事性总结，而不是可用于控制的决策接口。

---

## 12.5 Progressive Disclosure 必须保持语义不变

**Progressive Disclosure（渐进披露：先展示当前判断所需的最小信息，再按需要逐层开放依据和原始细节）** 可以降低默认认知负担。

一个项目 Profile 可以采用如下层级：

~~~text
Level 0  Attention status + coverage status
Level 1  Decision cards + deadline + available actions
Level 2  Risk, impact, Evidence coverage, unknowns
Level 3  Change narrative, architecture view, history
Level 4  Source records, Diff, logs, trace, raw artifacts
~~~

这不是成熟度阶梯，也不是通用固定五层。

安全 Incident 可能默认打开 Level 3；低风险重复任务可能只展示 Level 1；创意评审可能直接进入可视 Artifact，而不是先看工程摘要。

更重要的约束是：

> 同一个 Claim 在不同层级中的语义不能静默改变。

例如，Level 1 显示：

~~~text
Qualifying evidence accepted
Adoption blocked
Production not approved
~~~

下钻以后不能把它折叠成：

~~~text
Candidate approved
~~~

Progressive Disclosure 可以隐藏细节，不能隐藏处置边界。

### 每一层都应保留的最小信息

- Subject Identity；
- Decision Target；
- Scope；
- 当前状态的时间边界；
- Coverage 与 Unknown；
- 当前是否需要 Human Action；
- Drill-down 入口。

如果低层摘要会删除这些字段，项目宁可展示更少的自然语言，也不应展示一个更确定但不准确的状态。

---

## 12.6 Change Narrative 必须区分事实、推导与建议

**Change Narrative（变更叙事：把变化及其理由、影响、证据和待决问题组织成可追踪的论证与关系结构）**，不是让 AI 把 Diff 写成更流畅的故事。

推荐结构是：

~~~text
Observed problem
→ Intent and constraints
→ Candidate and alternatives
→ Actual changes
→ Impact claims
→ Supporting and opposing Evidence
→ Unknowns
→ Current recommendation
→ Authorized disposition target
~~~

其中至少要区分：

### 可观察事实

- 哪些文件、配置、运行状态实际变化；
- 哪些测试或观察实际执行；
- 哪些对象没有被观察；
- 当前 Candidate 与 Baseline 身份。

### 同期判断

- 当时为什么选择某个方向；
- 哪些替代方案被排除；
- 哪个风险被认为最重要；
- 谁作出了什么范围裁决。

### 事后推导

- 为什么问题可能发生；
- 变化可能通过哪些依赖产生影响；
- 哪些成功或失败可能与本次修改有关。

### 当前建议

- 接受、拒绝、收窄、补 Evidence、延后或恢复；
- 建议针对哪个 Decision Target；
- 推荐依据与不确定性。

自然语言连贯性容易把这四类内容融合成一个确定叙事。

所以，Change Narrative 的质量不由“读起来像完整故事”决定，而由来源绑定、类别边界和反证可见性决定。其中任何因果关系仍需独立 Evidence；Narrative 的顺序和连贯性本身不能证明因果。

---

## 12.7 Architecture Impact View 不能把“没看到”写成“没影响”

**Architecture Impact View（架构影响视图：展示 Candidate 对模块、Contract、依赖、数据流与运行边界的已知影响及未知区域）** 可以帮助 Reviewer 定位下钻范围。

它可以展示：

- 受影响模块；
- 新增或移除的依赖；
- 接口和 Schema 变化；
- 数据流与状态生命周期变化；
- Runtime、Deployment 或 Configuration 变化；
- Tool、Permission、Agent Contract 或 Workflow 变化；
- 明确检查过且未发现变化的区域；
- 尚未观察或无法确认的区域。

建议至少区分三种标记：

| 标记 | 含义 |
|---|---|
| Observed Impact | 有直接 Diff、Runtime Observation 或其他具名 Evidence |
| Inferred Impact | 根据 Dependency、Contract 或分析推导，尚未直接观察 |
| Unobserved / Unknown | 没有足够覆盖，不能判断是否受影响 |

“未受影响区域”是一个 Claim，也需要依据。

没有文件 Diff 不证明 Runtime 行为不变；单元测试通过不证明外部系统无影响；没有告警也不证明依赖路径未被触发。

Architecture Impact View 必须允许显示 `unknown`，否则它会把 Coverage Gap 伪装成干净架构图。

---

## 12.8 Risk Map 是 Risk Claim 的投影

**Risk Map（风险图：按当前决定组织影响、暴露、可逆性和检测条件的风险主张视图）** 不是对未来的客观测量。

一项 Risk Claim 可以包含：

~~~yaml
risk_id: RISK-033
subject_ref: commit:abc123
decision_target: production_adoption

hazard: legacy save data may become unreadable
affected_scope: users with v2 save format
impact: high
exposure: unknown
reversibility: forward-recovery only
detection:
  available: partial
  blind_spots:
    - corrupted saves not represented in fixtures

evidence_refs:
  - EV-MIGRATION-021
assumption_refs:
  - ASM-LEGACY-004
owner: release-safety-lead
expires_at: 2026-09-01
~~~

Risk Map 可以帮助比较：

- 影响范围；
- 可逆性；
- 数据、安全与用户体验风险；
- 当前 Exposure；
- 检测与恢复能力；
- 哪些 Assumption 仍未验证。

它不应把 `high / medium / low` 当作脱离 Scope 的永久属性。

统一风险分数还可能掩盖：

- 一个低概率但不可逆的高影响事件；
- 一个高频但容易恢复的小问题；
- Exposure 完全未知；
- Detector 与 Builder 共享同一错误假设；
- 风险 Owner 没有作出处置的 Authority。

因此，Risk Map 是帮助决定下钻和升级的索引，不是自动裁决器。

---

## 12.9 Decision Surface 只展示真正待决的问题

**Decision Surface（决策面：当前需要具名角色作出处置的问题、选项、依据、期限与后果的集合）** 应与一般通知分开。

一个 Decision Card 可以包含：

~~~yaml
decision_id: DEC-091
question: 是否接受本次 qualifying evidence
decision_authority_ref: AUTH-QUAL-002
deadline: 2026-08-25T12:00:00+08:00

options:
  - accept_for_qualifying_evidence_only
  - reject_and_request_more_evidence
  - narrow_claim_scope
  - defer

supporting_evidence_refs:
  - EV-TEST-041
counterevidence_refs:
  - EV-REVIEW-007
unknowns:
  - production population exposure

non_effects:
  - does_not_approve_adoption
  - does_not_approve_production

recovery_or_follow_up:
  - collect production-like migration samples
~~~

Decision Surface 应优先路由：

- 不可逆或难恢复的变化；
- Authority、Permission 或 Delegation 变化；
- 架构与公共 Contract 变化；
- 数据迁移；
- Scope 扩张；
- 新外部依赖；
- 核心体验与创意方向；
- 安全边界；
- Memory、Skill、Workflow 与治理规则的长期变化；
- Evidence 不足但时间窗口即将关闭的决定。

它不应把所有异常、通知和任务都升级成 Human Decision。

“需要 Human 看到”与“需要 Human 决定”是不同状态。前者可能只是通知或审计，后者必须绑定 Decision Authority。

---

## 12.10 Brief 是一种 View，不是新的 State Store

**Brief（简报：面向特定时间窗和决策角色生成的短期 Projection）** 可以成为 Human Decision Interface 的主要呈现形式。

一个项目可能使用三类 Brief。

### Project / Production Brief

回答：

> Product 或 Project 当前发生了什么，哪些结果与风险需要关注？

### Control Brief

回答：

> 生产 Product 的 Agent、Workflow、Gate、Memory 和验证系统出现了什么具名异常或 Authority 变化？

### Learning / Evolution Brief

回答：

> 哪些 Lesson、Workflow Candidate 或 Memory Promotion 正在等待独立 Evidence 与处置？

这三类只是可选 View，不要求三个新数据库。

Brief 应通过引用连接到原对象；当 Source 改变或过期时，Brief 应重新生成、标记 stale 或失效，而不是继续作为当前状态被手工维护。

### 一个最小 Control Brief

~~~text
CONTROL BRIEF

SUBJECT
Agent workflow candidate WF-042

AS OF
2026-08-24 14:20 +08:00

ATTENTION
1 named exception requires disposition

OBSERVATION COVERAGE
runtime: partial
authority changes: covered
detector health: healthy as of 14:18
unknown: external tool retry side effects

DECISION
Continue supervised pilot or freeze candidate

EVIDENCE
3 supporting records
1 counterevidence record

AVAILABLE ACTIONS
continue_supervised
freeze_candidate
request_more_evidence

DRILL-DOWN
source index: SRC-IDX-WF-042
~~~

这个 Brief 没有写 `SYSTEM STABLE`，因为它没有资格对未覆盖表面作全局健康声明。

---

## 12.11 Exception-driven 不等于 Silence-driven

**Attention Routing（注意力路由：依据风险、Authority、时效和异常条件，把有限的 Human Attention 分配给具名对象）** 可以让日常接口以 Exception 为中心。

但 **Exception-driven（异常驱动：日常只路由命中具名异常条件的对象）** 需要先定义：

- 哪个正常条件；
- 哪个观测范围；
- 哪个 Detector；
- 数据多久仍算新鲜；
- 哪类异常需要哪种角色；
- Detector 失效时怎样报告；
- 未观测区域怎样显示。

因此：

~~~text
No alert
≠ Healthy
~~~

更准确的表达是：

> 在已声明、仍新鲜且 Detector Health 正常的观测覆盖内，没有检测到需要当前角色介入的具名异常。

如果 Coverage 不足，界面应显示：

~~~text
NO NAMED EXCEPTION DETECTED
OBSERVATION COVERAGE: PARTIAL
DETECTOR HEALTH: UNKNOWN
GLOBAL HEALTH: NOT ASSERTED
~~~

如果 Detector 失效，它本身应成为 Exception，而不是让界面变得安静。

第14章将进一步讨论 Observation Coverage、Detector Health 和 Exception 生命周期。本章只规定：任何面向人的压缩层都不能删除这些边界。

---

## 12.12 HJL 与 TTE 只能先作为试验性探针

### HJL — Human Judgment Load

**Human Judgment Load（HJL，人类判断负载：在特定时间窗内需要人类作出处置的判断集合及其成本）** 可以观察需要人类处置的决定数量，但单纯计数会漏掉：

- 每项判断的难度；
- 所需专业能力；
- 风险和不可逆性；
- 等待时间；
- Context 重建成本；
- 漏报与事故逃逸；
- 因压缩错误造成的返工。

所以 HJL 不能只写成：

~~~text
100 tasks → 7 human decisions
is better than
100 tasks → 42 human decisions
~~~

七个决定可能都是高风险 Incident，四十二个决定也可能只是快速创意选择。

HJL 当前更适合作为分项观测：

~~~text
decision count by class
decision age
judgment time
escalation source
reversal and rework
escaped incident
unowned high-risk decision
~~~

任何“降低 HJL”的试验都要同时观察质量、安全和漏报。

### TTE — Time To Explain

**Time To Explain（解释时间：某个具名角色在给定准确性与完整性标准下理解一类决定所需的时间）** 可以测试界面可用性。

它必须绑定：

~~~text
named user or role
named decision class
required explanation content
accuracy / completeness threshold
maximum acceptable delay
~~~

“任何重要行为都应在五分钟内解释清楚”没有证据基础。

快速但错误的说明不会产生控制；复杂 Incident 也可能需要更长时间。TTE 只能比较相近任务和相近标准下的接口表现，不能作为全项目单一 North-star Metric。

---

## 12.13 怎样验证压缩没有破坏判断

Cognitive Compression 本身也需要 Verification。

可以从以下八个方面检查。

### 1. Source Binding

- 每个关键状态和数字能否定位 Source；
- Source Identity、Version 和时间是否明确；
- Projection 是否可能引用已被 supersede 的对象。

### 2. Scope Preservation

- 摘要是否保留 Claim Scope；
- 局部 PASS 是否被写成端到端成功；
- Evidence Acceptance 是否被写成 Adoption 或 Release。

### 3. Epistemic Separation

- Fact、Contemporaneous Judgment、Inference 和 Recommendation 是否分开；
- Risk 与 Impact 是否被标为 Claim；
- Assumption 是否仍可见。

### 4. Counterevidence and Unknowns

- 反证是否被压掉；
- `unknown` 是否被默认值替代；
- 未覆盖区域是否被误写为 unaffected。

### 5. Coverage and Freshness

- 数据截至何时；
- Observation Coverage 是否声明；
- Detector Health 是否可见；
- Projection 是否设置 Expiry。

### 6. Drill-down Fidelity

- 从摘要能否到 Evidence；
- 从 Evidence 能否到 Artifact、Diff、Log 或 Runtime Record；
- 下钻后是否仍指向同一 Subject 与 Version。

### 7. Action Correctness

- 按钮是否绑定真实 Authority；
- Preconditions 是否满足；
- 动作后果、范围和 Recovery 是否可见；
- UI 是否错误地允许一个角色作出无权决定。

### 8. Omission Testing

- 抽样比较 Projection 与 Source；
- 主动寻找摘要遗漏的限制；
- 用失效 Detector、stale data、冲突 Evidence 和空结果测试界面；
- 检查 Builder 与 Projector 是否共享同一错误假设。

验证结果同样需要有边界。一次抽样通过不证明所有未来 Projection 都可靠。

---

## 12.14 AI Summary 不能自动为 AI Execution 背书

AI 可以生成 Change Narrative、Risk Map 和 Brief。

但下面这条链路存在 Common-mode Failure（共同模式故障：多个环节因共享同一错误假设而同时失败）：

~~~text
AI builds
→ AI selects evidence
→ AI summarizes
→ AI recommends
→ summary is treated as approval
~~~

风险较高时，可以采用：

- 独立 Evidence Source；
- 与 Builder 分离的 Reviewer；
- 不同 Context 或不同验证路径；
- 规则化 Source completeness check；
- Human random audit；
- 对高影响 Claim 的直接 Artifact inspection；
- 强制显示 Counterevidence 与 Unknown；
- 对 Recommendation 保留独立 Disposition。

独立不只表示换一个 Agent 名称。

如果两个 Agent 使用同一摘要、同一遗漏 Source 和同一 Prompt assumption，它们仍然可能相关失败。

同样，不是每个低风险任务都需要完全独立 Review。独立强度应与 Claim、风险、可逆性和现有 Evidence Coverage 相称。

---

## 12.15 Human Decision Interface 不创造 Human Authority

原大纲将以下能力放入 Human Cognitive Authority：

- 知情；
- 解释；
- 决定；
- 否决；
- 接管；
- 要求下钻。

这些能力需要分成两类。

### Interface Capability

界面应让合适角色能够：

- 发现待决问题；
- 查看 Scope、Evidence、Unknown 与 Counterevidence；
- 要求解释或更多 Evidence；
- 下钻到 Source；
- 看见可用动作和后果。

### Authority-bearing Action

接受、拒绝、暂停、撤销 Delegation、发布或接管，是 Authority-bearing Action。

它们必须绑定：

- 具名角色或 Gate；
- Authority Grant；
- Scope；
- Preconditions；
- 允许的动作；
- Audit 与 Recovery。

并非“Human”这个抽象身份中的每个人都能覆盖所有 Policy。安全、合规和职责分离可能要求一个人不能单独解除某些控制。

因此，HCP 保留的是：

> 对 Authority 的可见性和对已授权动作的可用调用路径。

Authority 怎样授予、限制、撤销和降级，由第13章定义。

---

## 12.16 AI Game Dev OS 与 lessismore 支持什么

本节依据 [控制接口案例记录](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md) 汇集的 AI Game Dev OS v4.94 与 lessismore SP122 材料，说明现有实现能够支持什么，以及尚未支持什么。

### 可观察事实

- AI Game Dev OS v4.94 已实现 task-level non-authoritative read model，能够汇总 task、attempt、blocker、handoff 和部分 context。
- v4.94 暴露了 checkpoint、cancel、authorized claim withdrawal 与 review rejection back to rework 等局部控制路径。
- D-048 没有产生正常 target result，目标也没有被观察；外部失败证据仍表明系统不能被视为健康。
- lessismore SP122 的 Human disposition 将 `qualifying evidence accepted`、`adoption blocked` 与 `production not approved` 保持为不同状态。
- 没有被检查的 Artifact 实现完整 HCP、全局 takeover、delegation revocation、Observation Coverage health 或 Detector Health interface。

### 可支持的推导

- 面向人的状态摘要可以作为 non-authoritative projection；
- Evidence 与 Authority disposition 必须在摘要中保持分离；
- `no normal result` 或 `no alert` 不能被解释为健康；
- 控制动作需要显式回到已有 Authority 和状态对象。

### 不能支持的结论

- HCP 已经降低 Human Judgment Load；
- HCP 已经减少事故、返工或 Review 时间；
- 当前字段集合已经完整；
- Brief 比直接 Review 在所有任务中更可靠；
- pause、takeover、revocation 与 Detector Health 已完整实现；
- v4.94 或 SP122 验证了统一 Human Control Plane 架构。

这些材料只形成局部案例支持；本章的 Interface Contract 仍是一个有待通过后续原型和任务测试检验的候选设计。
完整 Episode、失败路径与 shared provenance 边界见[第23章](第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md)；这里的多项观察不是彼此独立的架构验证。

---

## 12.17 最小实现应从一个 Decision Path 开始

项目不需要一次建设 Constitution Dashboard、Trust Engine、Telemetry Platform、Workflow Optimizer 和 Learning Center。

更安全的起点是选择一个已经反复产生认知成本的 Decision Path，例如：

~~~text
qualification evidence disposition
workflow candidate acceptance
high-risk data migration
authority expansion request
production incident takeover
~~~

为这个路径实现最小闭环：

1. 绑定 Candidate、Baseline 与 Decision Target；
2. 引用 State Claim、Evidence、Counterevidence 与 Unknown；
3. 声明 Coverage、Freshness 与 Detector Health Reference；
4. 只展示当前角色有权或需要处理的 Decision；
5. 保留 Source Drill-down；
6. 提供真实可用的 authorized action；
7. 设置 Projection Expiry；
8. 抽样比较 Projection 与 Source；
9. 记录错误压缩、漏报、误报、判断时间和返工。

只有在这个闭环反复有用以后，再考虑：

- 更多 Decision Type；
- 跨项目 Brief；
- 自动 Attention Routing；
- HJL / TTE 观测；
- Random Audit；
- Learning / Evolution View。

可选界面不应提前升级成新的持久化对象体系。

---

## 12.18 与第13、14章的所有权边界

第12章拥有：

- Projection Contract；
- Progressive Disclosure；
- Change Narrative；
- Architecture Impact View；
- Risk Map 的呈现边界；
- Decision Surface；
- Brief 与 Attention Routing；
- Compression Validation。

第12章不拥有：

| 对象 | 所属章节 |
|---|---|
| Authority Grant、Delegation、Autonomy Profile、Revocation | 第13章 Governed Autonomy |
| Telemetry Source、Observation Coverage、Detector Health、Exception Lifecycle | 第14章 Observability and Intervention |
| Memory Promotion、Retrieval、Conflict 与 Expiry | 第15章 Memory Engineering |
| Self-Evolution Candidate、Evaluation Contract、Activation / Rollout Record | 第16章 Self-Evolution Engineering；基础 Recovery 与 Decision 分别引用第8、9章 |

HCP 可以把这些对象投影到一个或多个 Human Decision Interface，但不会因为同屏显示而改变它们的类型或 Owner。

---

## 12.19 本章原则

1. **压缩面向 Decision Target。** 不为“看起来完整”汇总所有信息。
2. **Projection 非权威。** 它不产生 Truth、Evidence、Reliance Disposition 或 Authority。
3. **Encapsulate Execution, Expose Evidence。** 默认隐藏无关细节，保留结果、依据、未知和下钻。
4. **Progressive Disclosure 保持语义。** 层级变化不能改变 Scope 和 Disposition。
5. **没有观察不等于没有影响。** Architecture View 必须显示 Unknown。
6. **Risk 是 Claim。** Risk Map 帮助判断，不自动裁决。
7. **通知与决定分开。** 只有具名 Decision 才进入 Decision Surface。
8. **Brief 是 View，不是 State Store。** Source 变化后 Projection 应更新、过期或失效。
9. **Silence 只表示有边界的 non-detection。** 必须同时显示 Coverage、Freshness 和 Detector Health。
10. **HJL 与 TTE 是试验性探针。** 不建立未经验证的 North-star Metric。
11. **界面不创造 Authority。** 所有动作都回到具名 Grant 与 Preconditions。
12. **压缩本身需要验证。** 特别检查遗漏、陈旧、共同模式故障和错误动作。

---

## 12.20 常见反模式

- 把 Dashboard 数量等同于可观测性；
- 把摘要写得更短等同于 Cognitive Compression；
- 用 `SYSTEM STABLE` 覆盖未知区域；
- 将 `no alert` 写成 `healthy`；
- 把 Projection 维护成第二套 State Store；
- 将局部 PASS 压缩成 Candidate Approved；
- 隐藏 Counterevidence、Assumption 或 `unknown`；
- 把 Inferred Impact 写成 Observed Impact；
- 声称“未受影响”却没有 Coverage；
- 用统一 Risk Score 自动排序所有决定；
- 把所有通知都升级为 Human Decision；
- 为了减少 HJL 而关闭告警或错误委托 Authority；
- 用固定五分钟 TTE 衡量所有任务；
- 让 Builder、Evidence Selector、Summarizer 和 Approver 共用同一错误来源；
- 在 UI 中提供没有真实 Authority 或 Recovery 的停止按钮；
- 一次构建完整 HCP 平台，再寻找它要解决的问题；
- 从 v4.94 的局部 read model 宣称完整 HCP 已验证。

---

## 12.21 本章检查清单

### Projection Identity

- Projection 为哪个 Decision Target 生成？
- Subject、Candidate 与 Baseline 是否明确？
- Source、Version、Generated At 与 Expiry 是否存在？
- Projection 是否被误当成新的 Truth Source？

### Information Boundary

- Fact、Judgment、Inference 与 Recommendation 是否分开？
- Scope、Counterevidence、Unknown 与 Non-effect 是否可见？
- Observation Coverage、Freshness 与 Detector Health 是否显示？
- 每一层 Progressive Disclosure 是否保持同一语义？

### Decision Surface

- 当前真的需要 Human Decision，还是只需通知？
- Decision Authority 与 Deadline 是否明确？
- Acceptance、Adoption、Release 是否分开？
- 每个 Action 是否有 Authority Ref、Preconditions、后果与 Recovery？

### Drill-down

- 能否从 Brief 到 Evidence？
- 能否从 Evidence 到 Source、Diff、Log 或 Artifact？
- 下钻后是否仍指向同一 Subject 和 Version？
- 高风险对象是否保留直接 Review 路径？

### Compression Validation

- 是否抽样比较 Projection 与 Source？
- 是否测试 stale data、Detector failure、冲突 Evidence 和 Target `non-result`？
- 是否记录漏报、误报、返工和错误处置？
- Builder 与 Reviewer 是否真正独立到足以降低相关失败？
- HCP 的维护成本是否低于它减少的判断与恢复成本？

---

## 12.22 本章结论

Cognitive Compression 不是把一个复杂系统改写成一句确定的状态。

它是一个有损、可检查的转换：

~~~text
many source objects
→ decision-bound selection
→ non-authoritative projection
→ progressive disclosure
→ human or authorized disposition
→ source-linked action and recovery
~~~

一个有效的 Human Decision Interface 不要求人默认阅读所有实现和日志，但必须让人能够回答：

~~~text
WHAT is being claimed?
FOR WHICH decision?
BASED ON WHAT evidence?
WITH WHAT coverage and unknowns?
AUTHORIZED BY WHOM?
WHAT can be done now?
HOW do I drill down, stop or recover?
~~~

本章最重要的边界是：

> **作为可选的接口组织方式，Human Control Plane 可以压缩和路由已有控制信息，但不能成为新的 Truth、Trust、Authority、Memory 或 Telemetry Owner。**

下一章将进入被本章刻意保留在界面之外的问题：Authority 怎样授予，Autonomy 怎样配置，Human 怎样暂停、撤销委托与接管。
