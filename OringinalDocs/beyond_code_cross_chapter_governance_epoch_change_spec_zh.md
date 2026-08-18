# Beyond Code: AI-Native Software Engineering
## 跨章节治理逻辑修订说明
### Execution Epoch / Policy-bounded Adaptive Governance / Governance Economics

> 本文档用于修订《Beyond Code: AI-Native Software Engineering》现有章节结构与理论逻辑。
>
> 本次修订来源于四个核心问题：
> 1. AI-native 治理机制如果全部启用，治理成本可能过高；
> 2. 当前方法越来越接近“在一个 Sprint / Task 内锁定 Working Truth，外部变化不能静默干预”的执行方式；
> 3. 不存在单一“完美 AI-native 架构”，更合理的是稳定原则 + 阶段适配；
> 4. Governance Level 不能简单交给 Agent 自由判断，否则会产生自我授权问题。

---

# 0. 核心理论修正

本次修订正式引入五个跨章节概念：

- **Execution Epoch**
- **Working Truth Baseline**
- **Policy-bounded Adaptive Governance**
- **Monotonic Governance Escalation**
- **Governance Economics**

核心主线：

```text
Stable Engineering Invariants
        ↓
Project Governance Policy
        ↓
Default Governance Profile
        ↓
Execution Epoch
        ↓
Agent Execution
        ↓
Risk Detection
        ↓
Monotonic Governance Escalation
        ↓
Evidence / Review
        ↓
Epoch Close
        ↓
New Verified State
```

---

# 1. Execution Epoch

> **Execution Epoch 是一个具有固定 Intent Version、Working Truth Baseline、State Snapshot、Context Baseline 和 Governance Profile 的受控执行窗口。**

它不是冻结真实世界，而是阻止外部变化在没有显式治理的情况下静默改变 Agent 的工作世界。

建议结构：

```text
Execution Epoch

Intent Version
Working Truth Baseline
State Snapshot
Context Baseline
Governance Profile
Authority / Permission
Evidence Requirement
```

外部变化：

```text
External Change
        ↓
Relevant?
   ┌────┴────┐
   ↓         ↓
  No        Yes
   ↓         ↓
Continue   Impact Analysis
               ↓
      Ignore / Rebase / Escalate / Restart
```

Sprint 只是较大粒度的 Execution Epoch 实现，不是理论前提。

---

# 2. Working Truth Baseline

> **Working Truth Baseline 是当前 Execution Epoch 被授权依赖的事实集合。**

包括：

```text
Baseline Commit
Active Decisions
Current Runtime State
Relevant Data Version
Known Dirty Changes
Approved Constraints
Open Assumptions
```

重要原则：

```text
New Truth Claim
≠
Automatic Baseline Mutation
```

而是：

```text
New Claim
→ Validate
→ Assess Impact
→ Rebase / Escalate
```

---

# 3. Governance Economics

> **Governance itself is a production cost.**

治理成本包括：

- Intent maintenance
- Context assembly
- Snapshot
- Registry
- Review
- Evidence
- Approval
- Human attention
- Coordination / waiting

建议工程思考模型：

```text
Expected Total Production Cost
=
Execution Cost
+ Context Cost
+ Governance Cost
+ Review Cost
+ Cognitive Cost
+ Expected Failure Cost
+ Rework Cost
```

因此目标不是 Maximum Governance，而是：

> **Minimum Expected Total Production Cost**

核心原则：

> **Governance should be proportional to expected loss, not maximized by default.**

---

# 4. Governance Profiles

建议通用等级：

## G0 — Trivial
适合 typo、formatting、generated temp artifact。

```text
Execute
→ Simple verify
```

## G1 — Local / Reversible
适合小 UI 修改、局部 Bug、独立 Refactor。

```text
Intent
Scope
Local Verification
Diff
```

## G2 — Standard Engineering
适合普通 Feature、多文件修改。

```text
Intent
Baseline
Context
Acceptance
Evidence
Review
```

## G3 — High Risk
适合跨模块、公共 API、架构、Save、大重构。

```text
State Snapshot
Expanded Context
Decision Record
Review Agent
Human Checkpoint
Rollback
```

## G4 — Critical
适合 Production Deployment、Security、不可逆 Data Migration、Payments、User Data。

```text
Full Governance
Human Approval
Strong Evidence
Rollback
Audit
```

---

# 5. Governance Floor

> **Governance Floor 是某类任务根据项目 Policy 必须满足的最低治理等级。**

例如：

```text
Irreversible data migration
→ minimum G4

Public API change
→ minimum G3

Cross-module refactor
→ minimum G2/G3

Local UI tweak
→ minimum G1
```

Agent 不能因为“觉得简单”自行绕过最低等级。

---

# 6. Monotonic Governance Escalation

> **在同一个 Execution Epoch 内，Agent 可以自动提高治理等级，但不能自行降低治理等级。**

允许：

```text
G1 → G2
G2 → G3
G3 → G4
```

不允许执行 Agent 自行：

```text
G3 → G1
```

治理降级只能发生在：

- 下一 Execution Epoch；或
- 显式 Human / Authorized Policy Decision。

原则：

> **Escalation can be local and automatic; de-escalation must cross an authority boundary.**

---

# 7. Continuous Governance Calibration

治理级别不能只在任务开始时选一次。

```text
Initial Profile
        ↓
Execute
        ↓
Observe
        ↓
Risk Trigger?
        ↓
Escalate / Continue
```

同一 Epoch 内遵守 Monotonic Escalation。

---

# 8. Risk Trigger Matrix

建议至少关注：

| Risk Dimension | 核心问题 |
|---|---|
| Blast Radius | 出错影响多大？ |
| Reversibility | 是否容易回滚？ |
| Uncertainty | 有多少未知？ |
| State Volatility | 当前状态是否持续变化？ |
| Dependency Scope | 是否跨模块 / 跨 Agent？ |
| Evidence Coverage | 是否容易可靠验证？ |
| Security / Data Impact | 是否涉及安全或不可逆数据？ |
| Novelty | 系统是否做过类似任务？ |
| Historical Reliability | Agent / Skill 在该类任务上是否可靠？ |

Trigger 示例：

```text
Irreversible data change → minimum G4
Security-sensitive access → minimum G4
Public API change → minimum G3
Cross-module + weak tests → minimum G3
Dirty shared state → escalate one level
Unresolved Truth Conflict → escalate one level
Missing rollback → escalate
Missing required evidence → task cannot close
Unknown external tool → minimum G2
Scope expansion → escalate / rebase
```

---

# 9. Stable Invariants vs Adaptive Mechanisms

## Stable Invariants

```text
Intent must be identifiable
Critical state needs a baseline
Assumptions must remain explicit
Authority must be bounded
High-impact changes require evidence
Critical state transitions must be traceable
Human decision rights must remain where required
```

## Adaptive Mechanisms

```text
Markdown or DB
Sprint or Task Epoch
Human Review or Review Agent
Lean or Full Context
One Gate or Five Gates
RAG or Index
Snapshot file or structured store
```

核心结论：

> **不存在全局最优的 AI-native architecture，但存在稳定的工程 Invariants，以及针对当前阶段更合适的 Architecture Fitness。**

---

# 10. Architecture Fitness

> **Architecture Fitness：一个 AI-native 架构与当前项目阶段、风险、规模和执行模式之间的适配程度。**

主要受：

```text
Project Stage
Risk
Team Size
Agent Autonomy
Task Type
State Volatility
Cost Sensitivity
Required Reliability
```

影响。

---

# 11. 受影响章节总览

| 章节 | 优先级 | 修改程度 |
|---|---:|---|
| 第1章 软件工程角色演进 | 无 | 不改 |
| 第2章 传统隐含假设失效 | P2 | 小补充 |
| 第3章 什么是 AI-Native SE | P0 | 理论修正 |
| 第4章 Intent Engineering | P2 | 衔接 Epoch |
| 第5章 Context Engineering | P1 | 增加 Epoch Context Baseline |
| 第6章 Truth & State | P0 | 新增 Execution Epoch / Working Truth |
| 第7章 Agent Execution | P0 | 以 Epoch 组织执行 |
| 第8章 Reliability | P1 | Risk Trigger |
| 第9章 Evidence | P1 | Evidence Coverage → Governance |
| 第10章 Review | P1 | Review 强度与 Profile 绑定 |
| 第11章 Cognitive Overload | P2 | 治理成本也是 Cognitive Load |
| 第12章 Cognitive Compression | P2 | 高治理必须压缩人类接口 |
| 第13章 Governed Autonomy | P0 | 重大重写 |
| 第14章 Observability | P1 / P0 | 运行中发现 Risk Trigger |
| 第15章 Memory | P2 | Epoch close → memory candidate |
| 第16章 Self-Evolution | P1 | 不可自行降级 Guardrail |
| 第17章 Multi-Agent Organization | P1 | Epoch / Shared Truth / State Isolation |
| 第18章 Traceability | P1 | 记录 Epoch / Profile / Escalation |
| 第19章 Security | P1 | Governance Floor |
| 第20章 AgentOps / Economics | P0 | Governance Economics |
| 第21章 AI-Native SDLC | P0 | Epoch-driven lifecycle |
| 第22章 Maturity Model | P0 | 成熟 ≠ 治理更多 |
| 第23章 AI Game Dev OS | P0 | Sprint 作为 Epoch 实例 |

---

# 12. 第2章修改

## P2

在 Human Smoothing / Smoothing Gap 后补充：

> 显性工程机制并不是越多越好。过去被 Human Smoothing 吸收的问题需要被选择性外部化；只有高影响、重复出现、难以可靠推断的问题，才值得持续承担治理成本。

再增加：

> AI-native 的挑战不是把所有隐性协调全部编码进流程，而是在失控风险与治理成本之间寻找合理边界。

---

# 13. 第3章修改

## P0

新增：

# Stable Invariants 与 Adaptive Mechanisms

并重写 Adaptive Governance 为：

> **Policy-bounded Adaptive Governance：项目 Policy 定义 Governance Floor 和允许的治理 Envelope；Agent 可以在该范围内工作，并在发现风险时自动升级，但不能自行解除既有 Guardrail。**

新增原则：

- Governance strength should match expected loss.
- No globally optimal AI-native architecture; only better-fit architecture for current constraints.
- Stable Invariants, Adaptive Mechanisms.

---

# 14. 第4章修改

## P2

在 Intent Lifecycle / Versioning 后增加：

# Intent Pinning within an Execution Epoch

```text
Epoch starts
→ Intent version pinned
```

重大 Intent 变化：

```text
Intent v2 → v3
→ Impact Analysis
→ Rebase / Restart / New Epoch
```

强调 Intent Evolution 允许，但必须显式跨越 Execution Boundary。

---

# 15. 第5章修改

## P1

在 Context Lifecycle / Snapshot / Projection 附近新增：

# Epoch Context Baseline

定义：

> Execution Epoch 开始时，用 Context Pack Version 和 Working Truth Baseline 建立本次执行的 Context Baseline。

新 Context：

```text
New Context
≠
Automatic Context Mutation
```

而是：

```text
Retrieve
→ Validate
→ Relevant?
→ Rebase / Escalate if necessary
```

---

# 16. 第6章修改

## P0

建议在 Working Truth / State Snapshot 之后新增：

# Execution Epoch 与 Working Truth Baseline

包含：

- Execution Epoch 定义
- Epoch Metadata
- Consistency Window
- 外部变化处理
- Sprint 只是 Pattern

并把：

> Code as Truth

升级解释为：

```text
Code → Implementation Truth
Runtime → Behavioral Truth
Data → Operational Truth
Decision → Normative Authority
Assumption → Unverified Claim
```

但保留“Doc as Intent, Code as Truth”作为简单默认 heuristic。

---

# 17. 第7章修改

## P0

Agent Execution 核心链路改为：

```text
Intent
        ↓
Execution Contract
        ↓
Governance Profile
        ↓
Open Execution Epoch
        ↓
Agent Loop
        ↓
State / Risk Monitoring
        ↓
Evidence
        ↓
Close Epoch
        ↓
Verified New State
```

新增：

- Epoch Open
- Epoch Rebase
- Epoch Close

完成标准从 “Done” 改为：

```text
Input State
→ Change
→ Evidence
→ Verified Output State
```

---

# 18. 第8章修改

## P1

新增：

# Reliability Signals as Governance Triggers

例如：

```text
Unexpected failure
Repeated retry
Scope expansion
State mismatch
Tool uncertainty
Unknown dependency
```

触发：

```text
Governance Escalation
```

---

# 19. 第9章修改

## P1

新增：

# Evidence Coverage as Governance Input

原则：

> **Low evidence coverage increases required governance.**

强自动证据可以降低 Review 负担；弱证据、高主观性、高影响任务应提高治理等级。

---

# 20. 第10章修改

## P1

Review 强度与 Governance Profile 绑定：

```text
G0 → no dedicated review
G1 → self-check / lightweight diff
G2 → structured review
G3 → independent review + human checkpoint
G4 → multi-layer review / approval
```

新增：

> **Review intensity should be profile-driven, not universally maximal.**

---

# 21. 第11–12章修改

## P2

新增：

> Governance Overload 也是 Cognitive Load 的来源。

强调：

```text
More governance
≠
more human understanding
```

高治理任务要通过 Cognitive Compression 给人提供决策界面，而不是暴露全部过程数据。

---

# 22. 第13章修改

## P0 — 重大重写

推荐结构：

```text
13.1 Why autonomy needs governance
13.2 Governance is a cost
13.3 Governance Profiles G0–G4
13.4 Governance Floor
13.5 Policy-bounded Adaptive Governance
13.6 Risk Trigger Matrix
13.7 Monotonic Governance Escalation
13.8 Continuous Governance Calibration
13.9 De-escalation Authority
13.10 Governance and Execution Epoch
13.11 Risk-based Autonomy
13.12 Human Decision Rights
13.13 Anti-pattern: maximum governance
13.14 Anti-pattern: self-authorized autonomy
```

核心句：

> **Agent may increase scrutiny when risk rises, but it may not grant itself permission to reduce scrutiny.**

---

# 23. 第14章修改

## P1 / 接近 P0

Observability 新职责：

> 发现 Governance Escalation Trigger。

监控：

```text
Scope growth
State mismatch
Repeated failure
Unexpected tool use
Dependency expansion
Dirty state
Truth conflict
Evidence gap
```

形成：

```text
Observability
→ Risk Signal
→ Governance Escalation
```

---

# 24. 第15章修改

## P2

Memory 写入尽量在：

> Epoch Close / Verified State

之后发生。

```text
Epoch result
→ verified?
→ Memory Candidate
```

避免执行中推测直接成为长期 Memory。

---

# 25. 第16章修改

## P1

Self-Evolution 可以建议：

- 提高治理；
- 修改 Governance Floor；
- 指出长期过度治理。

但 Policy 修改必须：

```text
AI proposes
→ Evidence
→ Authorized Review
→ Policy update
```

Agent 不能自行降低 Guardrail。

---

# 26. 第17章修改

## P1

新增：

# Shared Epoch vs Local Epoch

```text
Parent Epoch
    ↓
Worker Epoch A
Worker Epoch B
Reviewer Epoch
```

保持：

```text
Shared Truth
+
Explicit Handoff
```

禁止 Worker 静默自行 Rebase。

---

# 27. 第18章修改

## P1

Traceability 增加：

```text
Execution Epoch ID
Governance Profile
Governance Floor
Escalation Trigger
Escalation Time
Authority Decision
Intent Version
Truth Baseline
Output State
```

---

# 28. 第19章修改

## P1

安全类任务定义 Governance Floor，例如：

```text
Secret access → min G3/G4
Permission modification → min G4
Production data write → min G4
```

Security Policy 不能由执行 Agent 自行降低。

---

# 29. 第20章修改

## P0

新增大节：

# Governance Economics

讨论：

```text
Token Cost
Execution Cost
Context Cost
Review Cost
Governance Cost
Human Attention Cost
Failure Cost
Rework Cost
```

可加入指标：

```text
Governance Overhead Ratio
Rework Avoided
Failure Cost Avoided
Review Time
Human Decision Time
Escalation Frequency
False Escalation Rate
Under-governance Incident Rate
```

核心原则：

> 最成熟的系统不是治理最多，而是单位风险下降所需治理成本最低。

---

# 30. 第21章修改

## P0

AI-Native SDLC 改为：

```text
Human Need
    ↓
Intent Formation
    ↓
Governance Profile Selection
    ↓
Truth / State Baseline
    ↓
Context Assembly
    ↓
Open Execution Epoch
    ↓
Agent Execution
    ↓
Continuous Risk Detection
    ↓
Escalate / Rebase if needed
    ↓
Evidence
    ↓
Review
    ↓
Close Epoch
    ↓
Verified New State
    ↓
Snapshot / Memory Candidate
```

---

# 31. 第22章修改

## P0

必须避免：

```text
more registry
more agents
more gates
more automation
more governance
=
more mature
```

新定义：

> **AI-native engineering maturity 是系统在保持关键工程 Invariants 的同时，以尽可能低的治理成本，对不同风险任务选择合适治理方式的能力。**

成熟系统：

```text
typo → G0
local UI → G1
standard feature → G2
save migration → G4
```

不成熟但“严格”的系统可能：

```text
everything → G4
```

---

# 32. 第23章修改

## P0

新增：

# AI Game Dev OS as a Sprint-based Epoch Model

映射：

```text
Sprint Start
→ Working Truth Baseline
→ Execution
→ Explicit intervention only
→ Sprint Close
→ Snapshot / Archive
```

并明确：

> Sprint 是游戏长期开发中的一种合适 Epoch Pattern，不是 AI-native SE 唯一工作方式。

再增加：

# Evolution toward Policy-bounded Adaptive Governance

说明从手动 / Sprint-level governance 向 risk-aware adaptive governance 演进。

---

# 33. 主大纲修改

不改章节数量，只更新摘要：

- 第3章：增加 Stable Invariants / Architecture Fitness / Policy-bounded Adaptive Governance
- 第6章：增加 Execution Epoch / Working Truth Baseline
- 第7章：增加 Epoch-based Agent Execution
- 第13章：加入 Governance Profile / Floor / Monotonic Escalation / Continuous Calibration
- 第20章：加入 Governance Economics
- 第21章：改为 Epoch-driven AI-Native SDLC
- 第22章：明确 Maturity ≠ More Governance
- 第23章：明确 Sprint is one Execution Epoch pattern

---

# 34. 术语表新增

## Execution Epoch
一段具有固定 Intent Version、Working Truth Baseline、State Snapshot、Context Baseline 和 Governance Profile 的受控执行窗口。

## Working Truth Baseline
当前 Execution Epoch 被授权依赖的事实集合。

## Consistency Window
在执行期间维持关键状态一致性的受控工作边界。

## Governance Profile
针对某类风险水平定义的治理强度配置。

## Governance Floor
某类任务根据项目 Policy 必须满足的最低治理等级。

## Policy-bounded Adaptive Governance
在项目 Policy 定义的治理 Envelope 内动态调整，并允许风险触发自动升级的治理方式。

## Monotonic Governance Escalation
同一 Execution Epoch 内，执行 Agent 可以自动提高治理等级，但不能自行降低治理等级。

## Continuous Governance Calibration
执行过程中持续根据风险信号重新评估是否需要提高治理强度。

## Governance Economics
研究治理成本、失败风险、Review 成本和总体生产成本之间关系的工程视角。

## Architecture Fitness
AI-native 架构与当前项目阶段、风险、规模和约束之间的适配程度。

---

# 35. 核心设计原则更新

原有：

```text
Intent over Instruction
Doc as Intent, Code as Truth
Tight Boundaries, Flexible Execution
Contract over Reasoning Process
High Agent Cohesion, Low Agent Coupling
Encapsulate Execution, Expose Evidence
Evidence over Confidence
Automation Default Off
Risk-based Autonomy
Human Cognitive Authority
```

新增：

```text
Policy-bounded Adaptive Governance
Monotonic Governance Escalation
Governance Proportional to Expected Loss
Stable Invariants, Adaptive Mechanisms
Shared Truth, Local Context
```

---

# 36. 新的跨章节理论主线

```text
Human Intent
        ↓
Intent Artifact
        ↓
Project Policy
        ↓
Governance Floor
        ↓
Truth / State Baseline
        ↓
Context Assembly
        ↓
Execution Contract
        ↓
Open Execution Epoch
        ↓
Flexible Agent Execution
        ↓
Observability / Risk Signals
        ↓
Monotonic Governance Escalation
        ↓
Evidence / Review
        ↓
Verified State Transition
        ↓
Epoch Close
        ↓
Snapshot / Memory / Evolution
```

---

# 37. 四个原始问题对应答案

## 治理成本过高
→ Governance Economics + Governance Profiles。

## 很像 Sprint-driven
→ 抽象成 Execution Epoch / Consistency Window。

## 没有完美架构
→ Stable Invariants + Adaptive Mechanisms + Architecture Fitness。

## AI 如何选择治理等级
→ Policy-defined Governance Floor + Default Profile + Risk Trigger + Monotonic Escalation。

---

# 38. 修改优先级

## P0 — 必须修改
- 第3章
- 第6章
- 第7章
- 第13章
- 第20章
- 第21章
- 第22章
- 第23章
- 主大纲相关摘要
- 术语表
- 核心设计原则

## P1 — 建议同步
- 第5章
- 第8章
- 第9章
- 第10章
- 第14章
- 第16章
- 第17章
- 第18章
- 第19章

## P2 — 小幅衔接
- 第2章
- 第4章
- 第11章
- 第12章
- 第15章

## 无需修改
- 第1章

---

# 39. 最终结论

本次修订修正了全书一个潜在危险方向：

> **AI-native 软件工程不应该被写成“因为 Agent 不可靠，所以必须建立越来越多治理机制”。**

更成熟的理论应该是：

> **因为 Agent 是具有不确定性的执行者，所以需要稳定工程 Invariants；但具体治理强度必须受风险和经济性约束，并允许在执行过程中随风险单调升级。**

最终形成：

```text
Stable Invariants
+
Adaptive Architecture
+
Policy-bounded Governance
+
Execution Epoch
+
Risk-triggered Escalation
+
Governance Economics
```

因此，本书对 AI-native 架构的最终态度不应是：

> “建立最完整的治理系统。”

而应该是：

> **建立一个能够用最小必要治理成本维持可靠、可验证、可恢复生产的系统。**

这也给：

> Tight Boundaries, Flexible Execution

补上此前缺失的一半答案：

> **边界不是越紧越好；边界应该足够紧，以覆盖当前风险，但不能紧到压垮生产效率。**
