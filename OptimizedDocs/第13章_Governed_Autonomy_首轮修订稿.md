# 第13章 Governed Autonomy
## 自治是可撤回的委托配置，不是 Agent 的固有属性

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-024](../RevisedResult/RR-024_第13章Governed_Autonomy首轮回接说明.md)。
> 适用边界：本章提出一个候选 Governed Autonomy 对象模型，用于区分 Capability、Permission、Authority Grant、Reliance Disposition、Autonomy Profile 与 Responsibility；AI Game Dev OS v4.94 的案例只支持项目内边界，不证明该对象组合跨项目最优，也没有验证自治效率或治理成本效果。

第12章建立了 Human Decision Interface：

> 人可以看到待决问题、Evidence、Unknown、Authority 与可用动作，但界面本身不创造 Authority。

这留下了更基础的问题：

- Agent 能做什么？
- 平台允许它做什么？
- 组织授权它做什么？
- 哪些动作可以无需逐次批准？
- 哪些条件触发暂停、降级或接管？
- 运行历史怎样影响依赖判断？
- 谁可以扩大或撤销委托？

把这些问题都压成“自治等级”，容易造成两种误解。

第一，仿佛自治是 Agent 的固有能力，模型越强就自然拥有越多权限。

第二，仿佛项目沿着 L0 到 L5 单向成熟，越少人工介入就越先进。

本章采用不同定义：

> **Governed Autonomy（受治理的自治：在具名 Authority、Scope、Policy、Evidence、监督和恢复条件内，系统无需逐次人工批准即可执行的动作配置）**。

自治不是人格属性，也不是奖励分数。

它是一个可版本化、可过期、可暂停、可收窄和可撤销的 Delegation Configuration。

---

# 13.1 自动化不是二元选择，也不是单轴阶梯

一个系统可以：

- 自动读取 Repository，但写入需要批准；
- 自动修改隔离 Worktree，但不能 Commit；
- 自动 Commit，但不能 Merge；
- 自动 Merge 到开发分支，但不能 Release；
- 自动运行测试，但无权接受 Scope；
- 自动接受一个窄 Criterion，却无权作出 Adoption；
- 在低风险环境自动执行，在生产环境只提供建议。

所以“Human”与“Auto”之间并不是一个开关。

原大纲使用：

~~~text
L0 Advisory
L1 Generate, Human executes
L2 Execute, Human approves each time
L3 Low risk auto, high risk approval
L4 Goal-level autonomy with monitoring
L5 Highly autonomous, exception only
~~~

这些标签可以描述某个项目的运行模式，但不能作为通用成熟度阶梯。

同一项目可以同时拥有：

~~~text
code suggestion          advisory
isolated test execution  bounded_auto
repository write         approval_required
development commit       auto_with_audit
production deployment    human_or_release_gate
policy modification      prohibited
~~~

更高的自动比例不自动意味着更成熟。

如果 Observation、Recovery 或 Authority 不清，减少 Human checkpoint 可能只是扩大无监督失败面。

---

# 13.2 本章区分六个对象

本章的候选 Governed Autonomy 模型区分六个经常被混用的对象。

## Capability（能力：系统在技术上可能完成的动作）

回答：

> 它能不能做到？

例如，模型和工具组合可能能够修改文件、运行命令、调用外部 API 或生成部署 Artifact。

Capability 不产生 Permission 或 Authority。

## Permission（权限：技术执行环境实际开放的操作面）

回答：

> 当前 Sandbox、Tool、Credential 与 Platform 允许它做什么？

Permission 是执行层约束。一个动作被平台允许，不表示组织授权它用于当前目标。

## Authority Grant（授权授予：有权来源允许具名主体对指定目标采取或裁决某类动作的记录）

回答：

> 谁允许哪个 Subject，在什么 Scope、条件与用途下采取什么动作？

Authority 是规范性边界，不等于技术可达性。

Authority Grant 是授权来源。Decision / Policy Record 是在有效 Grant 下形成的规范性内容；Disposition 是其中针对具名 Decision Target 的结果关系。三者不能互换：成功历史、技术 Permission、Autonomy Profile 或一条 Decision Record 都不能自行创造或扩大 Authority Grant。

## Reliance Disposition（依赖处置：Decision Record 针对具名依赖用途形成的处置结果）

回答：

> 对这个具体用途，当前 Evidence 是否足以让项目依赖它？

Reliance 的 Decision Target 必须绑定 Capability、Configuration、环境、时间与 Intended Use。Disposition 可以是 provisional、restricted 或 accepted-for-scope，但不会自行授予行动权限。

## Autonomy Profile（自治配置：把已有 Authority 转换成运行时监督、审批、升级、审计与恢复条件的版本化配置）

回答：

> 已被授权的动作，在什么条件下可以无需逐次批准地执行？

Autonomy Profile 实现 Delegation，不创造 Delegation。

## Responsibility（职责：被分配去执行、维护、响应或恢复某项工作的义务）

回答：

> 谁被要求执行、维护、复核、升级或恢复这套自动化边界？

Agent 可以被分配 Operational Responsibility，但 Responsibility 不自动授予 Authority，也不等于 Accountability。第18章拥有 Accountability 的上位定义：组织要求具名 Human 或角色承担解释、审查、纠正或后果责任的规范性关系。法律责任仍取决于司法管辖、制度与具体事实，不能由本章模型推出。

这些对象共同约束可执行动作，而不是按成熟度依次生成：

~~~text
Capability            technical possibility
Permission            executable surface
Authority Grant       normative authorization for named use
Autonomy Profile      runtime delegation conditions
        │
        └── together delimit the eligible action surface
                         │
                         ▼
                      Execution
                         │ produces observations and evidence
                         ▼
                 scoped Reliance Claim
                         │ informs an Authority-bound Decision Record
                         ▼
              scoped Reliance Disposition

Responsibility
cross-cuts the work chain

Accountability
is assigned by the organizational control model
~~~

Execution 产生的 Evidence 只能支持或挑战具名 Reliance Claim，并可促使持有相应 Authority Grant 的 Subject 形成新的 Decision Record。Evidence 本身不能直接改写 Reliance Disposition，也不能反向扩大 Permission、Authority Grant 或 Autonomy Profile。

---

# 13.3 Autonomy Profile 是多维配置

一个 Autonomy Profile 不应只保存 `level: 4`。

下面是设计示例，不是通用 Schema：

~~~yaml
profile_id: AUT-PROFILE-042
version: 3
status: active

subject:
  agent_role: implementation-agent
  agent_contract_version: 7
  model_adapter: model-profile-a
  workflow_version: wf-implementation-12

authority_ref: AUTH-GRANT-108
capability: modify_gameplay_source
action_classes:
  - read
  - write
  - run_bounded_tests
  - create_development_commit

scope:
  repository: example-game
  paths:
    - src/gameplay/**
    - tests/gameplay/**
  environment: isolated-worktree
  excluded:
    - release/**
    - production-data
    - policy/**

supervision:
  write: bounded_auto
  test_execution: bounded_auto
  commit: auto_with_audit
  merge: approval_required
  deploy: prohibited

preconditions:
  - clean_bound_worktree
  - intent_scope_resolved
  - required_test_harness_available

evidence_requirements:
  - diff_scope
  - focused_tests
  - unresolved_assumptions

escalation_triggers:
  - scope_growth
  - external_dependency_change
  - authority_boundary_contact
  - target_non_result

protected_stop_conditions:
  - write_outside_scope
  - credential_request
  - production_state_contact

recovery:
  checkpoint_required: true
  rollback_ref: RECOVERY-021
  forward_recovery_allowed: true

expires_at: 2026-09-30
revocation_authority_ref: AUTH-REVOKE-004
~~~

Profile 至少要绑定：

- Subject Configuration；
- Capability 与 Action Class；
- Repository、Path、Environment 与 Data Scope；
- Authority Reference；
- Supervision Mode；
- Preconditions；
- Evidence Requirement；
- Escalation Trigger；
- Protected Stop Condition；
- Recovery；
- Expiry 与 Revocation。

同一个 Agent 换了 Model、Contract、Workflow、Tool Permission 或 Environment，可能已经不再是同一个 Delegated Subject。

---

# 13.4 新 Capability 不应静默继承旧边界

一个 Agent 在 gameplay implementation 上表现稳定，不表示它可以修改：

- Governance；
- Authority Policy；
- Deployment；
- Memory Promotion；
- Skill Registry；
- Security Boundary；
- Production Data。

旧运行历史只覆盖旧配置、旧 Capability 和旧 Intended Use。

因此，新 Capability 至少需要重新检查：

~~~text
subject identity
action surface
scope
impact
irreversibility
observation
verification
recovery
authority source
~~~

这不意味着每个新函数都创建一个新角色或完整治理包。

边界粒度应与风险相称。一个低风险、同 Contract 内的新操作可以由现有 Grant 覆盖；跨越新的 Resource、Environment、Decision Target 或不可逆动作时，则需要明确扩展或新 Grant。

关键原则是：

> **Authority 不通过语义相似性或 Agent 人格静默继承。**

---

# 13.5 Automation Default Off 需要绑定风险表面

原大纲提出：

> 能力存在，不代表权限默认开放。

这个方向成立，但 `Automation Default Off` 不能成为所有动作的绝对规则。

只读搜索、隔离环境中的纯计算和无副作用检查，可能由项目 Policy 默认开放。

对以下动作，更适合 Default Deny 或显式 Grant：

- 写入受保护 Source；
- 改变 Authority、Permission 或 Policy；
- 接触 Credential；
- 外部网络写操作；
- Commit、Merge、Release 或 Deploy；
- 修改 Production Data；
- 执行不可逆迁移；
- 推广 Memory、Skill 或 Workflow；
- 扩大自身工具或运行边界。

默认策略应绑定：

~~~text
action class
resource class
environment
impact
reversibility
existing organizational policy
~~~

“默认关闭”保护的是具名风险，不是把所有自动化都变成人工点击。

---

# 13.6 Permission Model 必须与 Authority Model 对齐

常见 Permission 可以拆成：

~~~text
Read
Write
Execute
Commit
Merge
Deploy
External Read
External Write
Credential Use
Memory Update
Skill Update
Workflow Update
Policy Update
Permission Change
~~~

仅列出 Permission 仍然不够。

例如：

- Git Credential 技术上允许 Push；
- 当前 Task 只授权创建本地 Commit；
- Release Policy 要求独立 Gate；
- Agent 因工具配置错误仍能执行 Push。

这里存在：

~~~text
Technical Permission > Granted Authority
~~~

系统应尽量让 Permission 不大于当前可用 Authority，但两者仍是不同对象。

Authority 还需要表达：

- Decision Target；
- Subject；
- Resource 与 Environment；
- 时间；
- Preconditions；
- Delegation Depth；
- 是否允许再委托；
- Audit 与 Recovery；
- Revocation。

Permission Enforcement 保护技术边界；Authority Record 解释为什么某项动作被允许。

---

# 13.7 Risk-based Autonomy 不等于 Risk Score

自治范围应与风险条件相关，但不需要把所有因素相乘成单一分数。

可以检查：

~~~text
Granted Action Surface
Impact
Irreversibility
State Uncertainty
Verification Difficulty
Observation Coverage
Recovery Cost
External Exposure
Decision Authority
~~~

同一个高能力模型：

- 在只读、隔离、可重放环境中，可能适合 bounded_auto；
- 在生产数据迁移中，可能只能提出方案；
- 在已授权的窄 Gate 中，可能自动作出 Acceptance；
- 对 Adoption 或 Release 仍然没有 Authority。

风险变化后的响应也不只有“询问 Human”：

~~~text
continue within scope
narrow scope
collect evidence
isolate
switch supervision mode
invoke delegated gate
pause
block
escalate
~~~

项目应根据当前风险、角色和可恢复性选择动作。

---

# 13.8 Structural Assurance 与 Operational Evidence 不产生 Authority

原材料将 Trust 拆成 `Assured Trust` 与 `Earned Trust`。

这个区分包含有用直觉，但更清楚的对象是：

## Structural Assurance（结构保障：由边界、隔离、验证和恢复设计提供的先验控制条件）

例如：

- Bounded Authority；
- Sandbox；
- 确定性检查；
- Versioned Baseline；
- Stop 与 Recovery；
- Independent Review Path；
- Observation Coverage。

新 Capability 即使没有运行历史，也可以拥有部分 Structural Assurance。

## Operational Evidence（运行证据：具名配置在具体环境和任务中产生的可检查观察）

例如：

- Runs；
- Failure 与 Rework；
- Rollback Exercise；
- Human Intervention；
- QA Reopen；
- Defect Escape；
- Audit 与 Incident。

运行历史可以支持或反对一个 Reliance Claim。

二者的关系是：

~~~text
Structural Assurance
+ Operational Evidence
→ supports or challenges a scoped Reliance Claim
→ informs an Authority-bound Decision Record
→ produces a scoped Reliance Disposition
~~~

不是：

~~~text
success history
→ earned Authority
~~~

Authority 来自有权 Grantor 与 Policy，不是由成功次数自动生成。

即使系统长期表现稳定，组织仍可能因为法规、产品责任或职责分离而保留 Human 或独立 Gate。

反过来，一个新 Capability 也可能在强隔离、可逆和窄 Scope 中获得有限 Delegation，而不需要先伪造历史成功率。

---

# 13.9 不建立全局 Trust Score

`Trust Score = 87.3` 把多个问题压成一个数字：

- 对哪个 Capability；
- 哪个 Configuration；
- 哪个环境；
- 哪种任务；
- 哪个时间窗口；
- 哪个 Intended Use；
- 哪些 Evidence；
- 哪个 Authority。

更适合工程记录的是有范围的 Reliance Disposition，例如：

~~~yaml
reliance_id: REL-042
subject_ref: AUT-PROFILE-042
capability: modify_gameplay_source
environment: isolated-worktree
intended_use: development_candidate_generation

disposition: accepted_for_scope
supporting_evidence_refs:
  - EV-RUNS-012
  - EV-ROLLBACK-004
limitations:
  - not qualified for release
  - external dependencies require review
expires_at: 2026-09-30
decision_authority_ref: AUTH-REL-003
~~~

一个 Profile 可以在某个用途上被依赖，在另一个用途上仍是 `unsupported` 或 `restricted`。

趋势指标可以帮助发现变化，但不能替代 Scope 和 Decision。

---

# 13.10 Authority Grant 与 Delegation Contract

**Delegation（委托：有权角色把具名动作或决定在限定条件下交给另一 Subject 执行的关系）** 需要可检查记录。

一个 Authority Grant 可以包含：

~~~yaml
grant_id: AUTH-GRANT-108
grantor: engineering-lead
grantor_authority_ref: AUTH-ORG-001

subject_ref: AUT-PROFILE-042
action_classes:
  - write_gameplay_source
  - create_development_commit
decision_targets:
  - development_candidate

scope:
  repository: example-game
  paths:
    - src/gameplay/**
  environment: isolated-worktree

preconditions:
  - intent_scope_resolved
  - no_production_credentials

prohibited:
  - merge
  - deploy
  - policy_change
  - downstream_delegation

evidence_obligations:
  - scoped_diff
  - focused_tests
  - unresolved_assumptions

valid_from: 2026-08-24
expires_at: 2026-09-30
revocation_ref: AUTH-REVOKE-004
~~~

Grantor 也必须拥有授予这些动作的 Authority。

如果允许 Downstream Delegation（下游委托：被委托主体继续把部分动作交给其他主体），还需要声明：

- 最大 Delegation Depth；
- 可再委托的 Action Class；
- Subject Eligibility；
- 是否继承或重新收窄 Scope；
- Evidence 与 Audit 责任；
- 如何级联撤销。

默认不能因为 Agent 能创建 Subagent，就假设它有权把原 Grant 全量转交。

---

# 13.11 Supervision Mode 是动作配置，不是身份等级

常见 Supervision Mode 可以包括：

| Mode | 含义 | 适用示例 |
|---|---|---|
| advisory | 只提出建议，不执行真实变化 | 架构候选、产品方向 |
| human_executes | 系统生成步骤，由 Human 执行 | 高风险一次性操作 |
| approval_required | 系统准备动作，每次由有权角色批准 | 数据迁移、权限变更 |
| bounded_auto | 在固定 Scope 与 Preconditions 内自动执行 | 隔离测试、局部修改 |
| auto_with_audit | 自动执行，保留抽样或周期审计 | 成熟的重复性低风险工作 |
| exception_routed | 正常路径自动，命中具名 Exception 时升级 | 有健康 Detector 的长期 Workflow |
| prohibited | 当前不允许执行 | 自行扩权、未授权发布 |

这些 Mode 不表示从低到高的成熟顺序。

同一 Profile 可以为不同 Action 配置不同 Mode；同一 Action 在不同 Environment 也可以不同。

Exception-routed 只有在 Observation Coverage、Detector Health 和 Recovery 条件成立时才有意义。否则“只在异常时通知”会退化成“没有观察到就继续”。

---

# 13.12 Governance 有成本，不能默认单调增加

治理机制本身会消耗：

- Runtime；
- Review Time；
- Human Attention；
- State Management；
- Proof Surface；
- Coordination；
- Recovery Complexity；
- False Positive Cost。

更多 Gate、Role、Manifest 和 Review 不自动带来更安全的执行。

治理设计需要回答：

~~~text
Which risk is protected?
At which action boundary?
By which control?
With what detection?
At what cost?
What happens on failure?
~~~

如果一个 Governance Finding 不能指出：

- 当前可达的危险动作；
- 可能发生的 false promotion；
- 被保护的 Authority Boundary；
- 当前阶段需要的 Evidence；

它可能只是 Process Warning，而不是 Hard Stop。

这不表示 Governance 越少越好。

它表示治理强度应与当前 Claim、风险、阶段和恢复条件匹配。

---

# 13.13 Protected Control Floor 不是 G0–G4 阶梯

**Protected Control Floor（受保护控制下限：某类 Action 在当前 Policy 下不可由执行主体自行绕过的最低控制集合）** 可以包括：

- 禁止 Scope 外写入；
- 禁止 Credential 或生产状态接触；
- 禁止把 development Evidence 宣称为 qualification；
- 禁止未授权 Merge、Release 或 Policy Change；
- 要求不可逆动作具有明确 Authority 与 Recovery；
- 要求重要 Identity 与 Provenance 可检查。

它绑定 Action Class 与 Environment，不是全项目统一等级。

项目可以允许 Subject 在风险上升时自动增加审查，例如：

~~~text
bounded_auto
→ approval_required
→ paused
~~~

但 Subject 不能静默修改自己的 Authority Grant、Protected Floor 或 Revocation 条件。

自动 De-escalation（降级治理强度）也不是绝对禁止。项目可以预先授权：

- 在哪些 Evidence 条件下恢复某个 Mode；
- 谁或哪个 Gate 有权决定；
- 哪些 Control 永远不在该授权范围内；
- 何时重新评估。

关键边界不是“只能升级不能降级”，而是：

> **治理强度的改变必须来自既有 Policy 或有权处置，不能由执行成功或 Agent 自我评价静默产生。**

---

# 13.14 Stop-the-line 必须区分 Hard Stop 与 Process Warning

**Hard Stop（硬停止：为阻止当前可达的高影响危险、越权动作或错误语义升级而立即终止或隔离执行）** 可以由以下条件触发：

- 当前 Intent 或 Authority 冲突使动作无合法解释；
- 写入、执行或外部访问越过 Scope；
- 不可逆动作缺少要求的批准或 Recovery；
- Validator Integrity 失效，目标结果不能安全解释；
- development Evidence 正在被提升为 qualification 或 Release；
- Subject 试图扩大自身 Permission、Authority 或 Delegation；
- 当前 Baseline 身份无法确定且继续会改变受保护状态；
- 工具行为触及 Credential、Production Data 或受保护外部系统。

Process Warning（过程警告）可以包括：

- 连续 meta-only successor；
- Proof Surface 增长而 source/test 不增长；
- Object、Digest、Role 或 Gate 数量持续增加；
- Review Finding 无法指出当前 unsafe action；
- Test 数量增长但当前 Contract 没有扩大；
- Scope、Dependency 或 Review Backlog 出现上升趋势。

Process Warning 可以触发：

~~~text
narrow claim
reduce scope
re-stage work
collect evidence
request human checkpoint
freeze new successors
~~~

它不应自动创建下一份 Governance Transaction，从而继续扩大原问题。

---

# 13.15 Human-in-the-loop 的目的不是每一步点击

Human-in-the-loop 可以承担不同职责：

- 价值与产品方向判断；
- 高影响风险接受；
- Authority Grant 与 Revocation；
- Scope、Adoption 与 Release；
- 复杂例外和冲突；
- 创意与体验裁决；
- 自动化制度本身的审查。

低风险、可逆且被明确委托的动作，可以不经过逐次 Human Approval。

Human Cognitive Authority（人类对需要 Human Judgment 之事项保留的最终认知裁决权）更准确地表示组织能够：

- 定位原始 Evidence；
- 理解 Claim、Scope 与 Unknown；
- 识别越权与 Evidence Gap；
- 改变 Delegation 和 Policy；
- 暂停、否决、接管和恢复；
- 把最终责任绑定到真实角色。

它不表示任意 Human 都能覆盖所有 Policy。

本书不另设一个与它并列的 `Human Decision Right` 对象。需要保留给 Human 的 Decision Type，应映射到具名 Human Authority Grant、制度边界或自然语言所说的 Human 保留裁决权。

安全、合规和职责分离可能要求多个角色或独立 Gate。自动 Gate 也可以在被明确委托的 Decision Target 内拥有处置权。

第12章的 Human Decision Interface 负责显示这些路径；本章负责说明路径从哪里获得 Authority。

---

# 13.16 Pause、Restrict、Revoke 与 Takeover 是不同动作

自治边界发生问题时，系统不只有 `on / off`。

## Pause（暂停）

暂时阻止新动作，保留当前 Profile 与 Grant，等待 Evidence 或处置。

## Restrict（收窄）

缩小 Action、Scope、Environment 或 Supervision Mode。

## Revoke（撤销）

由有权角色终止某项 Grant，使后续动作失去 Authority。

## Expire（过期）

Grant 或 Profile 达到预定时间、版本或条件后自动失效。

## Takeover（接管：由新的有权主体取得当前任务和控制状态，并决定继续、恢复或终止）

接管前需要知道：

- 当前 Candidate 与 Baseline；
- 已完成、在途和未开始的动作；
- Worktree、Lock、Tool Session 与外部副作用；
- 当前 Authority 与 Credential；
- 已产生的 Evidence 和 Unknown；
- Stop 是否已经真正生效；
- 可用 Recovery；
- 新 Subject 的 Grant。

仅把 UI 中的 Owner 改成人类，不构成 Takeover。

如果外部副作用不可回滚，接管可能只能选择 Forward Recovery，而不是恢复旧状态。

---

# 13.17 Revocation 必须处理在途与下游委托

撤销一个 Grant 不会自动撤回已经发生的物理动作。

Revocation Contract 应说明：

~~~text
new action denial
in-flight action handling
credential invalidation
subagent / downstream grant cascade
queued task cancellation
external side-effect reconciliation
evidence preservation
recovery ownership
resume criteria
~~~

需要区分：

- Authority 已撤销；
- Permission 已关闭；
- 执行已停止；
- 外部状态已恢复；
- Evidence 已保存；
- 任务已重新分配。

这些状态不会在同一时刻自动完成。

对高影响 Capability，项目应演练 Pause、Credential Revocation、Takeover 与 Recovery，而不是只在 Contract 中声明按钮存在。

---

# 13.18 Automated Gate 可以有 Authority，但不能扩大自己的用途

第9章已经区分：

~~~text
Evidence / Validation
Acceptance
Adoption
Release
~~~

项目可以授权自动 Gate：

> 当具名 Test Suite 在绑定 Build 和环境中通过时，自动接受 AC-07。

这项 Authority 不自动扩张为：

- 实现 Scope 必要；
- Candidate 应被采用；
- 生产环境可以发布；
- Gate 可以改变自己的 Test、Threshold 或 Scope；
- Gate PASS 可以升级自己的 Delegation。

一个 Delegated Gate 需要：

- Decision Target；
- Claim Scope；
- Subject / Build Identity；
- Required Evidence；
- Authority Source；
- Failure 与 non-result 语义；
- Expiry；
- Override / Appeal；
- Audit。

Gate 是 Authority-bearing mechanism，不是 Truth Machine。

---

# 13.19 案例只保留 Authority 投影

完整事件与失败路径见[第23章](第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md)；本章不重复时间线，只保留每个 Episode 对 Governed Autonomy 的约束。

| Episode | 可观察关系 | 本章能说明 | 不能说明 |
|---|---|---|---|
| D-048 | Validator 改变自身 exact inventory，检查停止，Target 未被观察 | Protected Stop 可以阻断执行；Target 仍是 `non-result`，后续 Retry 与 Round Accounting 需要有权处置 | 停止等于 Target Failure，或所有 Validator 必须零副作用 |
| D-073 至 D-075 | Governance / Review Artifact 增长，Delivery Evidence 未同步前进，Gate 仍阻塞 | Process Warning 应指向当前危险与 Evidence Use，Governance Cost 必须进入设计 | 严格治理普遍无效，或新增 Artifact 自动提高安全性 |
| D-079 | 42 个 Selected Tests 通过，Human 未接受 Over-scoped E1 Candidate，较小 Forward Correction 成为后续 Baseline | Test Evidence 不产生 Scope Acceptance Authority；Reliance、Scope 与 Adoption 分开 | 较小实现长期更好，或本章 Profile Schema 已被验证 |

来源与限制分别见[控制接口案例记录](../Evidence/receipts/ER-20260824-002__CLM-C12-001.md)、[治理活锁历史记录](../Evidence/receipts/ER-20260818-001__CLM-OUTLINE-002.md)、[认知负担案例记录](../Evidence/receipts/ER-20260824-001__CLM-C11-001.md)和[测试与范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md)。这些共享来源没有提供自治效率或治理成本的量化对照。

---

# 13.20 最小落地从一个 Capability 开始

项目可以选择一个重复、高成本但边界清楚的 Capability，例如：

~~~text
modify gameplay source in isolated worktree
run bounded regression suite
create development commit
triage non-production incident
generate release candidate evidence
~~~

建立最小闭环：

1. 识别 Subject Configuration；
2. 定义 Capability 与 Action Class；
3. 对齐 Permission 与 Authority；
4. 写明 Scope、Environment 与 Exclusion；
5. 选择每项 Action 的 Supervision Mode；
6. 声明 Preconditions、Evidence 和 Unknown；
7. 配置 Escalation 与 Protected Stop；
8. 验证 Pause、Revoke、Takeover 与 Recovery；
9. 设置 Expiry；
10. 收集 Operational Evidence；
11. 由有权角色更新 Reliance 或 Profile。

不要先建设全项目自治等级、Trust Score 和 Governance Dashboard。

只有当一个 Capability 的边界在真实运行中可观察、可停止和可恢复，再扩展到相邻 Action。

---

# 13.21 与第14–16章的所有权边界

第13章拥有：

- Capability / Permission / Authority 分离；
- Authority Grant 与 Delegation；
- Autonomy Profile；
- Supervision Mode；
- Protected Control Floor；
- Pause、Restrict、Revoke 与 Takeover Contract；
- Risk-based Delegation；
- scoped Reliance 与 Autonomy 的关系。

第13章不拥有：

| 对象 | 所属章节 |
|---|---|
| Telemetry Source、Observation Coverage、Detector Health、Exception Record | 第14章 |
| Memory Promotion、Retrieval、Conflict、Expiry | 第15章 |
| Self-Evolution Candidate、Evaluation Contract、Activation / Rollout Record | 第16章；基础 Adoption 引用第9章 |

第13章引用 Observation 与 Evidence 来触发 Profile 动作，但不重新定义这些记录。

---

# 13.22 本章原则

1. **自治是配置，不是人格。** 它绑定 Subject、Capability、Scope、Environment 和 Version。
2. **Capability、Permission 与 Authority 分开。** 技术可达不等于组织授权。
3. **Reliance 不产生 Authority。** Structural Assurance 与 Operational Evidence 只支持或挑战具名 Reliance Claim；持有相应 Authority Grant 的 Subject 通过 Decision Record 形成目标特定的 Reliance Disposition。
4. **Autonomy Profile 实现 Delegation。** 它不能自行创建或扩大 Grant。
5. **不使用单轴成熟度。** 同一系统可以对不同 Action 使用不同 Supervision Mode。
6. **Default Policy 绑定风险。** 不是所有自动化都必须关闭，也不是能力存在就默认开放。
7. **治理成本进入设计。** Gate、Review 和 Proof Surface 不是免费安全。
8. **Protected Floor 绑定 Action。** 不建立全项目 G0–G4 通用阶梯。
9. **Hard Stop 指向当前危险。** Process Warning 不自动制造下一轮 Governance。
10. **Human-in-the-loop 不等于逐次点击。** 重要的是委托来源、认知控制和接管能力。
11. **撤销不是瞬时恢复。** Authority、Permission、Execution、External State 和 Recovery 分开记录。
12. **Gate Authority 绑定 Decision Target。** PASS 不自动升级为 Adoption 或 Release。

---

# 13.23 常见反模式

- 把 L0–L5 写成所有项目的成熟路径；
- 认为模型越强就应获得越多 Authority；
- 用历史成功次数自动升级 Autonomy；
- 将 Capability、Permission、Authority 和 Responsibility 合并；
- 全局 Trust Score；
- 新 Capability 静默继承旧 Profile；
- Agent 创建 Subagent 时自动转交全部 Grant；
- Platform Permission 大于 Authority，却没有监测或限制；
- 所有动作 Default Off，导致无意义人工点击；
- 所有低风险动作默认 Auto，忽略 Environment 和 Recovery；
- 用更多 Gate 解决 Governance Livelock；
- Process Warning 自动产生新的 Governance Transaction；
- Agent 自行降低 Protected Floor；
- 把 Pause Button 当作实际 Stop；
- 撤销 Grant 后不处理 Credential、Queue、Subagent 和外部副作用；
- Test PASS 自动形成 Scope Acceptance、Adoption 或 Release；
- 任何 Human 都能覆盖所有 Policy；
- 用 v4.94 单案例证明一套通用 Autonomy Schema。

---

# 13.24 本章检查清单

## Subject 与动作

- 当前 Subject 包含哪些 Agent、Model、Contract、Workflow 和 Tool Version？
- Capability 与 Action Class 是什么？
- Environment、Resource、Data 和 Path Scope 是否明确？
- 新 Capability 是否静默继承旧 Authority？

## Permission 与 Authority

- 技术 Permission 是否大于当前 Grant？
- Grantor 是否有权授予这些动作？
- Decision Target、Preconditions、Expiry 和 Prohibited Action 是否存在？
- 是否允许 Downstream Delegation，怎样级联撤销？

## Autonomy Profile

- 每项 Action 的 Supervision Mode 是否独立配置？
- Profile 是否绑定 Evidence Requirement、Escalation 和 Protected Stop？
- Observation Coverage 与 Detector Health 是否足以支持 exception_routed？
- Profile 是否可暂停、收窄、撤销和过期？

## Reliance

- Structural Assurance 与 Operational Evidence 是否分开？
- Reliance 是否绑定 Capability、Configuration、Environment 和 Intended Use？
- 是否错误地让 Reliance 或 Test PASS 产生 Authority？
- 运行历史是否包含 Failure、Rework、Rollback 和 Human Intervention，而不只记录成功？

## Stop 与 Recovery

- Hard Stop 是否指向当前危险、越权或 false promotion？
- Process Warning 是否会反向制造 Governance Overload？
- Pause 后新动作是否真的停止？
- Revocation 是否处理 Credential、Queue、Subagent 和 in-flight action？
- Takeover 是否提供 Baseline、Evidence、Unknown 和 Recovery？
- 不可逆外部副作用是否有 Forward Recovery Owner？

## Human 与 Gate

- 哪些决定需要 Human，哪些可以由 Delegated Gate 完成？
- Human Decision Interface 是否显示真实 Authority，而不是只显示按钮？
- Acceptance、Adoption 与 Release 是否分开？
- Separation of Duties 是否允许一个角色单独覆盖所有控制？

---

# 13.25 本章结论

Governed Autonomy 不是让 Agent 沿着等级不断获得自由。

它是把委托拆成可检查对象：

~~~text
Capability
+ Permission
+ Authority Grant
+ scoped Reliance
+ Autonomy Profile
+ Observation and Evidence
+ Stop / Revocation / Recovery
~~~

运行历史可以支持或挑战 Reliance Claim，并触发持有相应 Authority Grant 的 Subject 形成新的 Decision Record 与 Reliance Disposition；历史不会直接改写规范性处置。

风险和 Evidence 可以触发 Supervision Mode 变化。

但 Authority 仍然来自具名 Grantor 签发的 Authority Grant，并受制度、Policy 与 Delegation 约束。被明确委托的 Gate 是持有窄 Grant 的裁决 Subject，不是 Authority 的来源。

本章最重要的边界是：

> **Autonomy does not earn Authority. Autonomy operationalizes Authority that has already been granted for a named scope.**

中文语义是：

> **自治不会靠成功历史自动获得授权；它只是在具名范围内，把已经存在的授权转换成可执行、可监督和可撤回的运行条件。**

下一章将讨论这套配置依赖的观察前提：系统怎样知道发生了什么、哪些表面没有被观察、Detector 是否健康，以及何时触发 Intervention。
