# RR-034：第21章 AI-Native Software Development Lifecycle 首轮调整计划

- 记录日期：2026-08-26
- 工作稿：[第21章 AI-Native Software Development Lifecycle](../OptimizedDocs/第21章_AI_Native_SDLC_首轮修订稿.md)
- 原始结构：[全书大纲第21章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 跨章来源：[第3章工作稿](../OptimizedDocs/第3章_AI原生软件工程定义_首轮修订稿.md)、[RR-011](RR-011_Execution_Epoch与治理逻辑.md)、[RR-012](RR-012_2026-08-10新增内容总裁决.md)、[RR-014](RR-014_AI_Game_Dev_OS_v4.94开发证据与全书优化.md)、[RR-033](RR-033_第20章AgentOps_成本与模型漂移首轮调整计划.md)
- 记录性质：跨章 Lifecycle 关系与状态迁移规划，不是流程效果证明
- 实施状态：`implemented / accepted`
- Evidence Routing：本轮整合既有概念边界，不新建 Claim 或 Receipt；若后续声称某 Lifecycle Profile 降低成本、错误、等待或风险，或准备据此修改 AI Game Dev OS Workflow，另行进入正式 Evidence Workflow

## 1. 入口结论

原大纲保留了三个有用主题：

1. 传统 SDLC 与 AI-native SDLC 的关系；
2. 各阶段输入与输出；
3. Gate 和不同任务的流程裁剪。

但现有表达存在四个结构问题。

### 1.1 把 Lifecycle 写成单向流水线

原流程从 Intent 依次走到 Memory 与 Evolution，容易暗示每项工作都完成所有阶段，
并且一次 Decision 后不再回到 Context、State、Plan 或 Execution。

实际工作中可能出现：

- Intent 冲突，返回目标形成；
- Context 缺口，返回 Retrieval；
- Baseline Drift，触发 Rebase；
- Verification 失败，进入 Rework；
- Test PASS 但 Scope 未接受，进入 Narrow 或 Reject；
- Integration 后出现运行 Drift，触发 Re-evaluation；
- Incident 先 Contain，再恢复或重新授权。

### 1.2 把阶段名称当成完成事实

`Truth Resolution` 不产生无范围的最终 Truth；`Evidence Collection` 不产生 Acceptance；
`Memory Update` 和 `Evolution Candidate` 也不应成为每次成功工作后的自动尾声。

### 1.3 把十个 Gate 当成通用流程重量

Intent、Context、Plan、Risk、Checkpoint、Evidence、Merge、Deployment、Memory 与
Evolution Gate 都可能有用途，但不能要求每个任务建立十个独立 Gate。

Gate 需要绑定具名 Decision Target、Evidence、Authority 和 Disposition；否则只是
增加等待和表单。

### 1.4 把 Execution Epoch 升级成统一必经阶段

既有裁决只允许把 Execution Epoch 作为某些长任务的受控执行区间或 Correlation
Profile。它不是所有任务的必备对象，也不是全书新的超级生命周期。

第21章建议围绕以下问题展开：

> 一个具名 Work 如何在 Intent、Grounding、Execution、Evaluation、Disposition、Integration、Operations 与 Learning 之间有边界地迁移，同时保留 Scope、Baseline、Authority、Evidence、`non-result` 与 Recovery，并允许不同风险任务裁剪路径？

这是一套候选 Lifecycle 关系，不声称它替代所有传统 SDLC，也不声称阶段数量或顺序普遍最优。

## 2. 传统 SDLC 不会被替换

Requirement、Design、Implementation、Test、Deployment 与 Maintenance 仍然描述
产品和软件交付活动。

AI-native Lifecycle 增加的是受托 Agent 工作所需的控制关系：

- Intent 与 Acceptance Target；
- Context、State、Assumption 与 Conflict；
- Execution Contract、Authority 与 Tool Boundary；
- Observation、Evidence、Coverage 与 Decision Disposition；
- Human Attention、Intervention 与 Takeover；
- Memory Candidate、Evolution Candidate 与 Adoption；
- Operational Baseline、Drift 与 Re-evaluation。

这些关系可以嵌入 Requirement、Implementation、Test、Operations 等不同阶段，
不是在传统 SDLC 外再串联一条固定流水线。

## 3. Lifecycle 是状态迁移网络，不是章节顺序

候选主干可以表示为：

~~~text
Need / Trigger
  ↕
Intent + Acceptance Target
  ↕
Grounding
  State / Decision / Assumption / Conflict
  Context Contract + Manifest
  Authority + Risk Boundary
  ↓
Plan / Execution Contract
  ↓
Bounded Execution Attempt
  ↕ observe / pause / retrieve / rebase / recover
Observation + Evidence + Coverage
  ↓
Authorized Disposition
  ├── retrieve / replan / rework / narrow
  ├── reject / cancel / non-result
  ├── accept-for-scope / integrate / release
  └── hold / rollback / suspend
  ↓ when applicable
Operations
  ↕ Drift / Re-evaluation
Memory Candidate / Evolution Candidate
  ↓ separate promotion or adoption decision
Future Baseline
~~~

箭头表示允许的关系，不表示每项工作都必须持久化每个节点。

Lifecycle 也不是只有一个闭环：

- 一个 Work 可以包含多个 Attempt；
- 一个 Change 可以有 Evaluation、Adoption 与 Release 三次不同处置；
- 一个 Release 可以进入长期 Operations；
- 一个运行事件可以重新打开 Re-evaluation；
- 一个经验可以成为 Memory Candidate，但最终被拒绝或过期。

## 4. 第21章拥有 Transition Semantics，不拥有全部对象

| 对象 | 主要所属章节 | 第21章如何使用 |
|---|---|---|
| Intent Artifact、Acceptance Target | 第4章 | 打开 Work 的目标和完成边界 |
| Context Contract / Manifest | 第5章 | 提供有来源、有限覆盖的信息面 |
| State Claim、Decision、Assumption、Conflict、Baseline | 第6章 | 形成当前执行依据和未知 |
| Plan、Execution Contract、Attempt | 第7–8章 | 组织受权执行和恢复 |
| Evidence、Coverage、Acceptance / Adoption / Release | 第9章 | 支持有范围处置 |
| Human Review、Decision Interface | 第10–12章 | 提供有权判断和认知边界 |
| Authority、Autonomy、Observation、Intervention | 第13–14章 | 约束运行和中途变化 |
| Memory / Evolution Candidate | 第15–16章 | 连接有选择的学习，不自动更新 |
| Agent Organization、Trace、Security Boundary | 第17–19章 | 约束协作、记录和外部影响 |
| Operational Baseline、Drift、Re-evaluation | 第20章 | 处理采用后的持续适用性 |

第21章不建立新的全局 Lifecycle Truth Store。

它只拥有：

- 这些对象之间允许的 Transition；
- 每个 Transition 需要的输入、Decision Target、Authority 与 Evidence Boundary；
- Path 裁剪、循环、停止、恢复和关闭语义；
- Lifecycle Profile 作为可选配置投影。

## 5. Lifecycle Profile 是路径配置，不是成熟度等级

**Lifecycle Profile（生命周期配置：针对具名 Work、风险面和恢复条件，选择必要
Transition、Gate、Observation、Review 与 Recovery 的有范围配置）** 可以引用：

- Work Type、Environment 与 Intended Use；
- Data、Tool、Permission 与 External Effect；
- Reversibility 与 Recovery；
- State Uncertainty 与 Conflict；
- Duration、Concurrency 与 Handoff；
- Evaluation Coverage；
- Human Decision Right；
- Protected Control Floor；
- Required Transition 与可选 Transition；
- Escalation、Fallback、Expiry 与 Owner。

它不等于：

- G0–G4 通用等级；
- 组织成熟度；
- Agent 能力排名；
- 固定低／中／高任务表；
- 对所有项目通用的 YAML Schema。

Profile 可以被压缩进一份短任务说明，也可以在高影响 Work 中成为版本化配置。

## 6. Lifecycle Transition 绑定 Decision Target

**Lifecycle Transition（生命周期转换：把具名 Work 或 Attempt 从一个有边界状态
迁移到另一个状态的授权关系）** 至少需要回答：

- Transition Target 是什么；
- 当前 Scope、Baseline 与输入是什么；
- 需要哪些 Evidence 或已知 Coverage；
- 谁拥有 Decision Authority；
- 允许哪些 Disposition；
- 失败、未知、超时或撤权时怎样处理；
- 是否产生新的 Attempt、Baseline 或下游 Candidate。

示例：

~~~yaml
transition_id: LT-021-018
work_ref: W-021-UI-fix
from: evidence_ready
decision_target: accept_change_for_integration

scope:
  paths:
    - ui/settings/
  non_goals:
    - save_migration

required_inputs:
  - intent_ref
  - baseline_ref
  - diff_ref
  - focused_test_result
  - coverage_statement

authority:
  decider: ui_maintainer
  automated_gate: focused_test_gate_for_named_scope

dispositions:
  - accept_for_integration
  - request_change
  - narrow_scope
  - reject
  - hold

on_unknown:
  action: hold_and_request_evidence
~~~

这不是要求每次 Transition 创建独立文件。

它是检查 Gate 是否真正具有语义的最小结构。

## 7. 阶段输入输出需要按现有对象模型修正

| Lifecycle 面 | 主要输入 | 候选输出 | 不自动产生 |
|---|---|---|---|
| Need / Trigger | Human Need、Incident、Observation、Opportunity | Work Candidate | 已接受 Intent |
| Intent Formation | Need、Stakeholder、Constraint | Intent Artifact、Acceptance Target、Non-goal | 实施授权 |
| Grounding | State Source、Decision、Assumption、Conflict | Execution Baseline、Context Contract / Manifest、Known Gap | 完整 Truth |
| Planning | Intent、Baseline、Context、Authority | Plan、Execution Contract、Evidence Plan、Recovery Boundary | Plan Acceptance |
| Execution | Contract、Tool、Permission、Attempt State | Action、Artifact、Observed Effect、Checkpoint | 正确结果 |
| Evaluation | Outcome、Claim、Test、Observation | Evidence、Coverage、Counterevidence、`non-result` | Acceptance |
| Disposition | Evidence、Scope、Authority | Accept、Reject、Narrow、Rework、Hold、Cancel | Integration / Release |
| Integration | Accepted Change、Target Baseline、Conflict Check | Integrated State Observation | Production Release |
| Release | Release Candidate、Environment、Release Authority | Released / Failed / Rolled-back / Unknown Result | 长期适用性 |
| Operations | Operational Baseline、Window、Telemetry | Drift Finding、Incident、Re-evaluation Case | Root Cause |
| Learning | Accepted Experience、Failure、Review | Memory / Evolution Candidate | Promotion / Adoption |

`可验证 Context Pack` 应收窄为可检查的 Context Contract / Manifest 与已知缺口；
它记录选择和来源，不证明内容为真或模型实际采用。

`Verified New State` 也不作为统一尾声。更准确的是保存 Post-action State Observation、
Verification Scope 与 Authorized Disposition。

## 8. 原来的十个 Gate 改成候选 Decision Target

| 原 Gate | 更准确的候选 Decision Target | 何时可能需要独立 Gate |
|---|---|---|
| Intent Gate | Intent 是否足以打开当前 Work | 多方冲突、高错误成本或开放式委托 |
| Context Gate | 当前信息是否足以支持下一动作，且允许进入该处理面 | 数据受限、来源冲突或高状态不确定性 |
| Plan Gate | 当前 Plan / Contract 是否在 Authority 与 Scope 内 | 长任务、跨系统或难恢复动作 |
| Risk Gate | 是否满足 Protected Floor 与当前风险处置 | 高影响、不可逆或受监管动作 |
| Checkpoint Gate | 是否可以继续、Rebase、Restrict 或 Stop | 长任务、并发写入或状态易漂移 |
| Evidence Gate | Evidence 是否足以支持具名 Decision Target | Acceptance、Adoption、Release 等重要处置 |
| Merge Gate | Change 是否适合进入目标 Baseline | 冲突、Scope、Review 与集成风险 |
| Deployment Gate | Release Candidate 是否可进入具名 Environment | 外部影响、回滚和运行准备要求高 |
| Memory Gate | Candidate 是否可 Promote 到具名 Memory Scope | 长期、跨会话或跨项目传播 |
| Evolution Gate | Candidate 是否可 Adopt / Activate | Workflow、Policy、Skill 或组织结构变化 |

不是每个 Decision Target 都需要独立服务、文档或 Human 点击。

Automated Gate 只有在获得当前 Scope 的明确 Authority 时，才能直接作出对应处置。

## 9. Gate 不等于 Review，也不等于 Human Approval

需要分开：

- Validation：检查某个可判定条件；
- Review：有资格主体检查材料并形成评价；
- Gate：控制是否允许发生某类 Transition；
- Decision：有 Authority 主体作出 Disposition；
- Approval：一种允许目标动作的 Decision；
- Acceptance：针对 Outcome 与 Scope 的处置。

一个 Gate 可以：

- 自动允许具名低风险 Transition；
- Fail Closed；
- 请求 Human Decision；
- 限制 Scope；
- 打开新 Attempt；
- 返回 `unknown` 或 `non-result`。

Human Approval 也不能替代缺失的 Scope、Evidence、Permission、Recovery 或下游授权。

## 10. Adaptive Governance 依据风险面，不依据固定等级

流程裁剪可以考虑：

- External Effect 与 Blast Radius；
- Data、Secret、Privacy、IP 与 Provider Boundary；
- Tool、Credential、Permission 与 Authority；
- Reversibility、Rollback 与 Forward Recovery；
- State Uncertainty、Conflict 与 Dirty Work；
- Duration、Concurrency、Agent 数量与 Handoff；
- Evaluation Coverage 与未知失败面；
- Human Decision Capacity；
- Production、Customer、Player 或法定影响；
- Governance 与 Total Production Cost。

回答“是”的数量不是风险分数。

不同风险面可能要求不同控制，例如：

- 数据受限但动作只读：重点在 Context、Provider 与 Retention；
- 数据公开但可修改 Production：重点在 Authority、Action Sink 与 Recovery；
- 低影响但长生命周期：重点在 Baseline、Handoff、Drift 与 Rebase；
- 局部且易恢复：可以压缩 Plan、Review 与持久化对象。

执行 Agent 可以增加检查、暂停或请求更高权限，但不能自行降低 Protected Control Floor、
扩大 Authority 或删除已记录风险。具名 Authority 可以依据新 Evidence 调整非关键控制。

## 11. Execution Epoch 只是一种可选受控区间

**Execution Epoch（执行区间：从某个 Execution Contract 被打开，到关闭、重启或
显式 Rebase 之间，由固定引用的 Intent、Baseline、Authority、Tool 与 Governance
配置约束的受控运行区间）** 适合：

- 跨会话或持续较长时间；
- 外部状态可能变化；
- 多 Agent / Tool 需要共享 Correlation Boundary；
- 中途变化不能静默替换 Baseline；
- 需要 Pause、Rebase、Escalate 或 Recover；
- Close 时需要明确 Attempt / Output State。

它不一定适合：

- 单文件低风险修正；
- 一次只读查询；
- 已由现有 Transaction、Job、Run 或 Request 明确覆盖的工作；
- 引入新名词的成本高于边界收益的项目。

Execution Epoch 是 Contract 的生命周期区间，不复制 Intent、Context、State、Policy
和 Evidence 成为大型容器。

## 12. Sprint、Task、Run、Attempt 与 Epoch 不是同义词

- Sprint 是团队规划和交付节奏；
- Task / Work Unit 是目标和责任边界；
- Run 是一次运行实例；
- Attempt 是针对同一 Work 的一次有身份尝试；
- Transaction 是具有提交 / 回滚语义的状态变化边界；
- Execution Epoch 是可选的受控引用区间。

一个 Sprint 可以包含多个 Work、Run 与 Epoch；一个长期 Work 也可以跨越多个 Sprint。

AI Game Dev OS 可以使用 Sprint 组织开发，但不能由此推出 Sprint 是 AI-native SDLC 的
唯一实现。

## 13. Completion、Closure、Integration 与 Release 分开

需要区分：

~~~text
Attempt Closed
Work Outcome Observed
Evidence Ready
Outcome Accepted for Scope
Change Integrated
Artifact Released
Operational Baseline Active
Memory Candidate Promoted
Evolution Candidate Adopted
~~~

它们不是同一条成熟度阶梯，也不会自动连续发生。

Work 可以以以下状态关闭：

- accepted-for-scope；
- rejected；
- cancelled；
- superseded；
- partial；
- unknown external result；
- target `non-result`；
- transferred with explicit open items。

关闭不是把未知清零。

## 14. Failure 与 Recovery 会改变路径

候选失败路径包括：

| 事件 | 可能返回或转移到 |
|---|---|
| Intent Conflict | Stakeholder / Intent Formation |
| Missing Context | Retrieval / Human Request |
| Baseline Drift | Pause / Rebase / New Attempt |
| Permission Denied | Replan / Authority Request / Cancel |
| Verifier Failure before Target | Preserve Evidence / `non-result` / Repair Verifier |
| Target Validation Failure | Rework / Narrow / Reject |
| Scope Not Accepted | Narrow / Replan / Reject |
| Integration Conflict | Rebase / Conflict Decision |
| Release Failure | Rollback / Forward Recovery / Incident |
| Operational Drift | Restrict / Reroute / Re-evaluate / Retire |

Lifecycle 图如果只画 Happy Path，会把最需要治理的状态迁移隐藏起来。

## 15. Memory 与 Evolution 是独立候选生命周期

成功、失败和 Incident 都可能产生 Learning Candidate。

但它们只有在经过：

- Source 与 Provenance 检查；
- Scope 与适用条件说明；
- Counterexample 与 Conflict 检查；
- Privacy、Security 与 Rights 处置；
- Promotion / Adoption Authority；
- Expiry、Rollback 或 Revocation 设计；

之后，才可能进入 Memory、Skill、Workflow、Policy 或 Organization Baseline。

因此第21章使用：

~~~text
Work Outcome
→ Learning Candidate
→ separate evaluation and disposition
→ optional promotion / adoption
~~~

不使用 `完成任务 → 自动更新 Memory → 系统进化`。

## 16. Deployment 不是 Lifecycle 终点

进入 Production 或外部使用后，仍需要第20章提供：

- Operational Baseline；
- Evaluation Window；
- Outcome、Cost 与 Control Observation；
- Model、Tool、Permission、Evaluation 与 Contract Drift；
- Incident 与 Re-evaluation Trigger；
- Continue、Restrict、Reroute、Rollback、Suspend 或 Retire。

运行 Evidence 可能重新打开：

- Intent；
- Design / Plan；
- Evaluation；
- Security / IP Disposition；
- Memory / Evolution Candidate；
- Release 或 Retirement Decision。

Lifecycle 是持续适用性管理，不是 Deployment 前的一次审批链。

## 17. 三类候选 Profile 只用于说明裁剪

首轮正文可以用三类对比案例，但不把它们命名为成熟度等级。

### 局部、可逆、易观察

- 简短 Intent / Scope / Acceptance Target；
- 当前文件或状态引用；
- 一个受限 Attempt；
- 自动 Validation；
- Diff / Result Review；
- 不建立独立 Epoch 或多重 Gate。

### 跨会话、跨角色或存在集成风险

- 版本化 Baseline 与 Context Manifest；
- Execution Contract；
- Attempt / Handoff Identity；
- Checkpoint 与 Evidence Plan；
- Integration Disposition；
- 必要时使用 Execution Epoch。

### 高影响、难恢复或多方 Authority

- 独立 Intent、Risk、Security / Rights 与 Release Decision Target；
- Protected Control Floor；
- 更强 State Observation 与 Recovery；
- Canary / Staged Rollout；
- 独立 Review 或多方 Authority；
- 运行 Re-evaluation 与 Incident Path。

这些 Profile 依据实际风险面组合，不表示所有项目沿同一路径升级。

## 18. AI Game Dev OS 案例边界

v4.94 的既有记录可以说明：

- Governance Activity 与 Delivery Evidence 需要分开；
- Verifier Result 与 Target Result 需要分开；
- Test PASS 与 Scope Acceptance 需要分开；
- Function、Qualification、Gate 与 Production Claim 可以处于不同阶段；
- `NON_QUALIFYING`、`non-result` 与 Not Accepted 不能从 Lifecycle 图中消失。

它不能证明：

- Execution Epoch 是最优 Lifecycle 单元；
- Function-first 是普遍最佳顺序；
- 新 Lifecycle 降低时间、返工、缺陷或 Human Waiting；
- Sprint-based Epoch 是 AI-native SDLC 的唯一实现。

第21章只使用这些边界关系；完整时间序列仍由第23章案例承担。

## 19. 计划中的章节结构

1. 传统 SDLC 仍然存在；
2. AI-native 增加的是受托执行控制循环；
3. Lifecycle 是状态迁移网络，不是固定 Pipeline；
4. Work、Attempt、Outcome 与 Transition；
5. Lifecycle Profile 与风险裁剪；
6. 各 Lifecycle 面的输入、输出与非主张；
7. Gate、Review、Decision、Approval 与 Acceptance 分离；
8. Intent、Grounding 与 Execution Contract；
9. Bounded Attempt、Observation 与 Evidence；
10. Authorized Disposition 与多种 Closure；
11. Integration、Release 与 Operations；
12. Memory / Evolution Candidate 的独立生命周期；
13. Execution Epoch 的可选边界；
14. Sprint、Task、Run、Attempt、Transaction 与 Epoch；
15. Failure、Rebase、Recovery 与 Re-evaluation 路径；
16. 三类按风险裁剪的示例 Profile；
17. AI Game Dev OS v4.94 的受限状态迁移案例；
18. 跨章接口、原则、反模式、检查清单与结论。

## 20. 实施顺序

1. 在 `OptimizedDocs/` 创建第21章首轮工作稿，采用三项 Header；
2. 以第3章 3.15 的迭代 Lifecycle 为入口，不复制所有章节定义；
3. 把原线性流程改成包含返回、停止、恢复和运行重开的状态迁移网络；
4. 把十个 Gate 改写为候选 Decision Target，不创建固定 Gate Stack；
5. 把 Execution Epoch 保持为可选受控区间；
6. 将 `Truth Resolution`、`Verified New State`、`Memory Update` 等过强表达收窄；
7. 保留传统 SDLC 与不同风险任务的流程裁剪；
8. 只把 v4.94 写成状态与处置语义案例，不推导效果；
9. 检查第4–20章的对象所有权，删除第21章中的重复定义；
10. 将 Lifecycle Profile、Transition 和 Closure 交给 Human Review。

## 21. 2026-08-26 实施结果

[第21章首轮修订稿](../OptimizedDocs/第21章_AI_Native_SDLC_首轮修订稿.md)已经形成，
共 `21.1–21.43` 四十三节。

原大纲主题均已保留，但关系已经重排：

| 原主题 | 首轮修订位置 | 结构变化 |
|---|---|---|
| 传统 SDLC | 21.2 | 保留 Requirement、Design、Implementation、Test、Deployment 与 Maintenance |
| AI-native SDLC | 21.3–21.4 | 从单向 Pipeline 改为允许循环、停止、恢复和重开的状态迁移网络 |
| 各阶段输入输出 | 21.12 及 21.13–21.25 | 增加“非主张”列，收窄 Truth、Context、Evidence、Acceptance、Release 与 Learning |
| Lifecycle Gate | 21.26–21.31 | 十个固定 Gate 改为候选 Decision Target，分离 Validation、Review、Decision 与 Acceptance |
| 不同任务流程裁剪 | 21.6–21.7、21.30–21.36 | Lifecycle Profile 依据实际风险面组合，不形成低／中／高成熟度等级 |
| Execution Epoch / Sprint | 21.32–21.33 | Epoch 保持可选受控区间，Sprint 保持团队节奏，两者不成为通用 Lifecycle 单元 |

### 21.1 对象所有权结果

第21章只新增两个候选整合概念：

1. Lifecycle Profile：选择 Transition、Gate、Observation、Review 与 Recovery 的路径配置；
2. Lifecycle Transition：绑定转换 Target、输入、Evidence、Authority、Disposition 与失败路径的关系。

以下对象均被明确限定为复用或关系，不形成新的平行 Registry：

- Work 沿用第17章；
- Outcome 沿用第20章；
- Attempt 作为第7–8章执行实例进入 Lifecycle；
- Grounding 是活动投影，不是新的 Truth Record；
- Decision Gate 是 Transition Control，不是 Truth Source；
- Closure 是保留未知和后续路径的关系；
- Execution Epoch 是可选的 Contract 运行区间。

### 21.2 过强表达修正

- `Truth Resolution` 改为有范围 Grounding；
- `可验证 Context Pack` 改为可检查的 Context Contract / Manifest 与 Known Gap；
- `Verified New State` 改为 Post-action State Observation、Verification Scope 与 Disposition；
- `Evidence Collection` 不再自动通向 Human Acceptance；
- `Memory Update` 改为 Memory Candidate 与独立 Promotion；
- `Evolution Candidate` 不自动 Adoption / Activation；
- Deployment 不再作为 Lifecycle 终点，Operations / Drift 可以重新打开 Lifecycle；
- Fixed Gate Stack 改为按 Decision Target 和风险面选择。

### 21.3 Execution Epoch 边界

正文保持既有结论不变：

- Epoch 可以用于长任务、跨会话、多 Agent / Tool Correlation、Baseline Pinning 与 Rebase；
- 它不是所有任务必备对象；
- 它不复制 Intent、Context、State、Policy 和 Evidence；
- Sprint、Task、Run、Attempt、Transaction 与 Epoch 保持区分；
- v4.94 不证明 Epoch 优于其他时间或运行边界。

没有因为第21章主题是 Lifecycle，就改变 RR-011、RR-012、RR-014 与第18章的既有裁决。

### 21.4 Evidence Routing 结果

- 没有新建正式 Claim 或 Evidence Receipt；
- 没有声称本章 Lifecycle 降低时间、返工、缺陷、等待、成本或风险；
- 没有声称更多 Gate、多 Agent、Epoch 或 Automation 代表更成熟；
- D-073—D-075、D-048、D-079 与 F1–F4a 只承担 Activity、Verifier、Target、
  Acceptance 与 `NON_QUALIFYING` 的状态迁移语义；
- 完整 v4.94 时间序列继续留给第23章；
- 如果后续准备把 Lifecycle Profile 反馈到 AI Game Dev OS Workflow，仍需正式取证与独立处置。

### 21.5 验证结果

- 三项 Reader-facing Header 已应用；
- 数字章节 Heading 连续为 `21.1–21.43`；
- Markdown Fence 成对闭合；
- 原大纲传统 SDLC、AI-native 流程、输入输出、Gate 与流程裁剪均有正文落点；
- 核心英文术语具有首次中文语义定义；
- Reader-facing 正文没有 Claim ID、Receipt ID、Coverage Status 或 Human Status；
- 相对链接目标可解析；
- `git diff --check` 通过；
- `OringinalDocs/` 没有 tracked diff。

### 21.6 待 Human Review

1. 第21章是否应以“有授权状态迁移网络”而不是阶段 Pipeline 为中心；
2. Lifecycle Profile 与 Lifecycle Transition 是否足以承担本章新增语义；
3. Grounding、Attempt、Closure 和 Decision Gate 是否已经避免成为重复对象；
4. 十个原 Gate 改为候选 Decision Target 是否符合作者观点；
5. Execution Epoch 是否应继续保持可选区间；
6. 三类 Profile 是否只作为裁剪示例，而不形成成熟度等级；
7. v4.94 是否继续只承担状态与处置语义；
8. 第21章接受后是否进入第22章能力适配／成熟度模型重构。

## Human Disposition

- Status: `accepted`
- Decision by: Human Author
- Decision at: 2026-08-27
- Rationale: 作者明确回复“确认，进入下一步”。本次接受限定于：以有授权状态迁移网络而非固定阶段 Pipeline 组织本章；将 Lifecycle Profile 与 Lifecycle Transition 作为候选整合概念；把原十个 Gate 收窄为具名 Decision Target；保持 Execution Epoch 可选；并继续分离 Work、Attempt、Outcome、Change、Integration、Release、Operations 与 Learning。接受不表示对象集已经完备、最优或普遍适用，不表示传统 SDLC 已被替代，也不表示固定 Gate 数量或 Epoch 是必要条件；本章没有形成效率、质量、成本或安全效果证明。AI Game Dev OS v4.94 继续只承担状态与处置语义案例。工作流进入第22章能力适配／成熟度模型重构。
