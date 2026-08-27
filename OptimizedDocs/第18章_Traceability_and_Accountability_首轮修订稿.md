# 第18章 Traceability and Accountability
## 追踪外部决策环境，保留责任关系，不伪造隐藏推理

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 或 [Cognitive Control、Trust 与 Human Control Plane v0.1](../OringinalDocs/ai_native_cognitive_control_trust_human_control_plane_v0.1.md)。
> 回接说明：[RR-029](../RevisedResult/RR-029_第18章Traceability_and_Accountability首轮回接说明.md)。
> 适用边界：本章保存可观察的外部决策环境，不声称恢复隐藏推理或保证确定性重放；在本书的组织模型中，Trace 只提供问责依据，Accountability 仍由具名 Human／组织 Authority 分配。

Git 可以记录：

- Commit；
- Diff；
- Parent；
- Branch；
- Tag；
- Author / Committer Metadata；
- Message；
- Signature；
- 文件历史。

这些能力很重要。

但它们不会自动回答：

- 这个 Change 对应哪个 Intent；
- 当时的 Baseline、Context 与 Assumption 是什么；
- 哪个 Human、Agent、Tool 或 Gate 实际参与；
- 谁被授权执行，谁被授权裁决；
- Review 检查了哪个 Claim；
- Evidence 支持多大 Scope；
- 为什么一个 PASS 没有形成 Adoption；
- 哪些条件后来失效；
- 事故后谁负责解释、恢复与改变控制。

这不是 Git 的缺陷。

Git History 管理版本关系；Decision Trace 管理工程关系。二者需要互相引用，而不是由后者替代前者。

本章采用两个工作定义。

> **Traceability（可追溯性：沿着具名、版本绑定且有来源的关系，定位 Intent、Work、Context、Subject、Authority、Action、Change、Evidence、Review、Decision 与 Outcome 的能力）**。

> **Accountability（问责归属：组织要求具名 Human 或角色对目标、控制设计、授权、复核、处置、运行或恢复承担解释、审查、纠正或后果责任的规范性关系）**。

Responsibility（职责）是角色被分配去执行、维护、响应或恢复某项工作的义务；Accountability 则规定谁必须解释、审查、纠正或承担组织后果。一个主体可以同时承担两者，但它们不会因同一次 Assignment 自动合并。

Traceability 提供可检查材料。

Accountability 决定哪些主体必须对哪些决定和控制作出解释。

前者不能自动生成后者。

---

# 18.1 先区分必要、有用与可选

## 必要

只要某个受托动作可能产生重要、外部、难恢复或多方影响，项目至少需要能够回答：

- 当前在追踪哪个 Work / Decision Target；
- 哪个 Subject 以什么配置行动；
- 使用了哪个 Authority；
- 从哪个 Baseline 开始；
- 实际改变了什么；
- 观察到了什么；
- 谁作出后续处置；
- 哪些信息缺失。

低风险、局部且易恢复的修改，可以通过 Task Reference、Commit、简单验证和具名接受记录满足这些问题。

## 有用

当任务跨 Thread、跨 Agent、跨系统、跨 Release，或者存在高风险、长期维护、复杂 Authority 与事故复盘需要时，Decision Graph、Audit Trail、签名、Correlation ID 和长期 Retention 可能有用。

## 可选

完整 Event Sourcing、全量 Prompt Archive、逐 Tool Token Trace、Cryptographic Ledger、Deterministic Replay Platform 和统一企业 Graph 都是可选机制。

机制数量不是 Traceability 成熟度。

---

# 18.2 Git History 是版本事实的重要来源，不是完整决策模型

Git 擅长回答：

~~~text
which tree changed
from which parent
through which commit
with which recorded author / committer metadata
~~~

结合规范使用，它还可以保存：

- Decision Link；
- Task / Issue Link；
- Signed Commit；
- Review Reference；
- Release Tag；
- Revert / Forward Correction 历史。

但需要保留四条边界：

1. Commit Author 不自动等于代码的唯一产生者；
2. Committer 不自动等于 Decision Authority；
3. Merge 不自动等于 Adoption 或 Release；
4. Commit Message 是外部说明，不是隐藏推理记录。

一个 Agent 可以生成 Diff，由 Human Commit，由 Gate Review，再由另一个 Role Release。

把它们全部归入 Git Author，会丢失实际责任链。

Decision Graph 应引用 Commit Identity、Diff 与 Ancestry，不复制 Git 成为第二套 Repository State。

---

# 18.3 八个概念不能压成“有日志”

| 概念 | 本章工作定义 | 不自动保证 |
|---|---|---|
| Provenance | 一个 Record、Claim 或 Artifact 从何而来、怎样派生 | 当前仍适用或内容为真 |
| Traceability | 能否沿具名关系定位相关记录 | 记录完整或决定正确 |
| Auditability | 有权审计者能否在规定边界内查询、验证和评价记录 | 审计一定发现问题 |
| Reconstructability | 能否有限重建当时可观察的外部决策环境 | 重现相同模型行为 |
| Replayability | 能否重新执行一组记录的动作或事件 | 获得相同结果 |
| Explainability | 能否为具名受众提供有来源的外部行为或决定说明 | 说明完整、因果正确或揭示隐藏推理 |
| Attribution | 能否把可观察动作、产物或决定关联到具名 Subject / Tool / Configuration | 法律、道德或组织问责已经成立 |
| Accountability | 谁必须对具名目标、授权、控制、决定或结果作出解释并承担组织后果 | 由日志自动决定责任 |

**Provenance（来源及派生关系：记录 Entity、Activity、Subject、Source、Revision、Transformation 与 Time 之间怎样关联）** 是 Trace 的基础之一。

**Auditability（可审计性：有权主体能够查询记录、检查完整性边界并评价控制与决定的能力）** 依赖 Trace，但还需要 Access、Retention、Integrity 和 Review Contract。

**Reconstructability（有限重建能力：在已保存材料范围内重新组成当时可外部观察的状态、输入、授权、行动、Evidence 与决定环境）** 不承诺确定性再现。

**Replayability（行动重放能力：在新的 Attempt 中重新执行已记录动作、输入或事件序列的能力）** 不承诺结果相同，也不等于恢复旧状态。

**Explainability（可解释性：面向具名受众和问题，使用有来源记录说明行为、决定、限制与未知的能力）** 不要求也不应伪装成恢复隐藏推理。

**Attribution（可观察归因：将动作、Artifact、Finding 或 Decision 与具名 Human、Agent Instance、Tool、Gate 和配置关联）** 不应被翻译成自动归责。

---

# 18.4 十一种 Record Role 展开一条责任链

本章使用下列候选 Record Role：

| Record Role | 回答的问题 |
|---|---|
| Trace Contract | 当前为什么追踪、必须覆盖什么、保留多久 |
| Intent / Work Reference | 该活动服务于哪个目标与 Work |
| Execution Baseline Reference | 当时允许依赖哪些 State、Decision、Assumption 与 Context |
| Subject Configuration Reference | 哪个 Human、Agent、Gate 或 Tool 以什么配置参与 |
| Assignment / Authority Reference | 谁被要求做什么，谁被允许做什么 |
| Action / Activity Record | 实际发起、尝试或完成了什么动作 |
| Change / Artifact Reference | 哪个 Repository、Runtime、Data 或外部状态发生变化 |
| Evidence / Observation Reference | 实际观察了什么，Coverage 与生成边界是什么 |
| Review / Handoff Reference | 谁检查或接管了什么，范围和结果是什么 |
| Decision Record | 哪个 Authority 对哪个 Target 作出什么处置 |
| Outcome / Exception / Recovery Reference | 后来发生了什么，是否触发介入、恢复或重开 |

这些是语义角色，不要求一项活动生成十一个文件。

同一个签名后的 Release Record 可以同时引用 Decision、Artifact、Evidence 与 Deployment Outcome。

真正需要避免的是：

- 不能识别记录的 Subject；
- 不能区分 Action 与 Decision；
- 不能定位当时 Baseline；
- 不能判断 Evidence 覆盖；
- 不知道某个关系是观察、授权、时间相邻还是事后推导。

---

# 18.5 Decision Graph 是有类型投影，不是新的 Truth Store

**Decision Graph（决策关系图：把版本化工程记录按有语义的关系连接起来，用于查询决定的输入、Authority、处置和后续影响的派生投影）** 不应只有一条线：

~~~text
Intent
→ Context
→ Plan
→ Agent
→ Tool Action
→ Change
→ Evidence
→ Review
→ Decision
~~~

实际关系更接近：

~~~text
Intent ──scopes──────────────┐
Baseline ──bounds────────────┤
Assignment ─binds──> Subject ├──performs──> Action
Context Manifest ─supplies───┘                  │
                                                ├──changes──> Artifact / State
                                                └──produces─> Evidence

Authority Source / Grantor ─issues───> Authority Grant
Authority Grant ─authorizes─────────> Subject + Action / Decision Type
Decision / Policy ─constrains────────> Action / Future Decision

Evidence ─supports-for-scope─> Claim
Review ─evaluates────────────> Candidate / Claim
Authorized Subject ─creates───────> Decision Record
Decision Record ─targets─────────> Decision Target
Decision Record ─records─────────> Target-specific Disposition
Adoption Disposition ─adopts / rejects─> Candidate
Release Authorization ─permits──────> Release Target
Release Execution ─acts on────────> Authorized Release Target
Release Outcome ─is observed at─────> Environment / User / Downstream
Later Evidence ─supports / challenges───> Prior Claim
New Decision Record ─supersedes─────> Prior Decision Record
~~~

至少需要区分关系类型：

- `derived_from`；
- `used`；
- `supplied_to`；
- `performed_by`；
- `authorized_by`；
- `generated`；
- `observed`；
- `supports_for_scope`；
- `reviewed_by`；
- `disposed_by`；
- `supersedes`；
- `invalidates`；
- `handed_to`；
- `released_as`；
- `recovered_by`。

时间先后关系不应自动命名为 `caused_by`。

Graph 可以从 Primary Record 生成；Graph 节点仍需要 Source Link、Version、Freshness 与缺失状态。

---

# 18.6 Trace Contract 先定义审计问题和覆盖边界

**Trace Contract（追踪契约：为具名 Work、Decision Target 或风险声明必需记录、关系、完整性检查、访问与保留条件的版本化约束）** 可以包括：

~~~yaml
trace_contract_id: TRC-018
version: 2

target:
  work_ref: WU-042
  decision_targets:
    - source_adoption
    - production_release

required_references:
  - intent_version
  - execution_baseline
  - assignment
  - authority_grant
  - subject_configuration
  - change_identity
  - evidence_coverage
  - review_disposition
  - final_decision

required_relationships:
  - performed_by
  - authorized_by
  - supports_for_scope
  - disposed_by

integrity:
  ordering: correlation_sequence
  correction_mode: append_and_supersede

access_profile: named-audit-role
retention_profile: project-risk-profile
known_exclusions:
  - hidden_reasoning
~~~

这是设计示例，不是通用 Schema。

Trace Coverage 只能相对于 Contract 声明：

~~~text
complete-for-release-decision-v2
partial-for-incident-causality
missing-external-service-response
unknown-tool-side-effect
~~~

“完整执行轨迹”如果没有 Target、Scope 和 Exclusion，是不可验证的口号。

---

# 18.7 Identity、Authentication、Attribution 与 Accountability 分开

一条活动可能涉及：

- Intent Owner；
- Requester；
- Planner；
- Assigned Worker；
- Agent Instance；
- Model / Agent Contract；
- Tool；
- Runtime Credential；
- Commit Author；
- Committer；
- Reviewer；
- Decision Authority；
- Deployer；
- Incident Responder。

这些身份不能由一个 `actor` 字段吞掉。

**Subject Configuration Reference（主体配置引用：把具名参与主体绑定到当时的 Human / Agent / Gate Identity、模型或规则版本、Tool、Credential Scope 与运行边界）** 用于可观察归因。

Authentication 证明某个 Credential 或身份完成了认证。

Attribution 把可见动作关联到 Subject Configuration。

Accountability 则来自组织制度、授权与责任分配，不由 Authentication Log 自动产生。

一个 Human 使用自己的账号提交 Agent 生成的 Change，不表示：

- Human 亲自生成每一行；
- Agent 获得 Commit Authority；
- Human 已完成独立 Review；
- Commit 本身构成 Adoption；
- 平台账号决定全部组织责任。

---

# 18.8 Action Record 不自动证明 Intent、因果或决定

**Action Record（行动记录：对 Subject 发起、尝试、完成、中断或撤销的具名 Tool / Runtime 动作及其输入输出引用的记录）** 可以说明：

- 什么动作被请求；
- 哪个配置发起；
- 何时开始和结束；
- 使用哪个 Tool / Endpoint；
- 返回了什么 Tool Return / Error；
- 是否产生可识别 Side Effect；
- 是否有后续 Observation。

它不能单独说明：

- 为什么 Subject 选择该动作；
- 动作是否符合上层 Intent；
- 动作是否获得正确 Authority；
- 紧随其后的状态变化一定由它导致；
- 成功返回表示目标完成；
- 没有日志表示没有动作。

如果需要提出因果关系，应建立 Causal Claim，记录支持 Evidence、替代解释和不确定性。

Action Sequence 是时间线输入，不是 Root Cause。

---

# 18.9 Context Trace 只记录外部供应和访问，不推断模型内部使用

第5章已经区分 Context Contract、Pack、Manifest 与 Access。

第18章只追踪这些对象怎样参与一次执行：

~~~text
eligible source
→ selected
→ supplied or made accessible
→ optionally accessed through a visible tool
→ cited or referenced in output
~~~

Context Manifest 可以证明某些内容被装配或传输。

Tool Log 可以证明某个资源被请求或返回。

Citation 可以证明输出显式引用了某个来源。

这些记录都不能保证：

- 模型注意了全部 Context；
- 某条信息实际决定了输出；
- 没有 Citation 就完全没有影响；
- Full Transcript 等于 Decision Environment；
- Summary 无遗漏。

因此本章追踪 External Context Relation，不建立“模型内部使用记录”。

---

# 18.10 Plan、Assignment 与 Replanning 都需要版本身份

Plan 是 Candidate，Assignment 是 Subject、Role、Work 与 Authority 的具名绑定。

Trace 应分别记录：

- Plan Candidate Version；
- Plan Review；
- Plan Disposition；
- Assignment Created；
- Assignment Accepted / Rejected；
- Authority Reference；
- Execution Start；
- Replanning Trigger；
- Revised Plan；
- Cancellation / Reassignment；
- Handoff Receipt。

执行中发现新状态并调整顺序并不必然是错误。

问题在于：

- 原 Plan 被静默覆盖；
- Replanning 扩大 Scope；
- 新动作需要的 Authority 没有更新；
- 被取消的 Assignment 仍继续产生 Side Effect；
- 后来者无法判断实际执行的是哪个 Plan Version。

对高影响变化，可以要求 Replanning 记录：

~~~text
trigger
new observation
affected dependency
scope change
authority impact
evidence impact
accepted by
~~~

低风险探索只需保存关键转折点，不必记录每一次局部路径选择。

---

# 18.11 Decision Record 保存外部理由、Authority 与生命周期

**Decision Record（决策记录：有权主体对具名 Decision Target 作出的处置及其当时输入、外部理由、适用范围与生命周期记录）** 可以包含：

~~~yaml
decision_id: DEC-184
decision_target: candidate_source_adoption

subject:
  authority_holder_ref: product-owner-01
authority_ref: AUTH-031

disposition: rejected_for_current_scope
candidate_ref: commit-ref
baseline_ref: baseline-ref

intent_ref: INT-008
work_ref: WU-042
context_manifest_ref: CTX-M-077
plan_ref: PLAN-021-v4

evidence_refs:
  - EV-101
counterevidence_refs:
  - EV-104

stated_rationale:
  - candidate_exceeds_current_contract
alternatives_considered:
  - accept_as_is
  - narrow_and_forward_correct

assumptions:
  - smaller_candidate_can_preserve_behavior
unknowns:
  - lifetime_maintenance_cost

effective_scope: e1-source-baseline
effective_at: named-time
expires_or_reopens_on:
  - contract_change
  - new_counterevidence

supersedes: none
recorded_at: named-time
~~~

这是设计 Profile。

关键不是字段数量，而是后来者能够区分：

- 哪个问题被决定；
- 谁在什么 Grant 下决定；
- 当时有哪些可用输入；
- 哪些 Evidence 被用于什么范围；
- 哪些 Unknown 被保留；
- 决定何时生效、何时失效或被替代。

---

# 18.12 Stated Rationale 不是 Hidden Reasoning

**Stated Rationale（外部陈述理由：由具名主体为某个 Decision 提供、可被审查的目标、约束、Evidence、Trade-off 与选择说明）** 是工程记录。

它可能是：

- contemporaneous；
- reconstructed-after-the-fact；
- Human-authored；
- Agent-drafted and Human-accepted；
- derived from a Policy / Rule；
- generated by an authorized deterministic Gate。

这些来源和时间必须保留。

Rationale 不应被宣称为：

- 模型的完整内部推理；
- 行动发生的唯一心理原因；
- 没有遗漏的因果解释；
- Decision 正确性的独立证据。

工程上更有用的问题是：

~~~text
What objective was stated?
Which constraints and authority applied?
Which evidence was available?
Which alternatives were externally recorded?
Which unknowns remained?
What decision was made?
~~~

而不是要求保存或复现隐藏 Chain-of-Thought。

Conversation Transcript 可以作为过程记录，但它需要 Retention、Access、Privacy、Source Identity 和适用边界，不能取代 Decision Record。

---

# 18.13 Evidence Link 必须说明支持关系和用途

Evidence 与 Decision 之间不是：

~~~text
Evidence exists
→ Decision is correct
~~~

而是：

~~~text
Evidence
→ supports named Claim for declared Scope
→ accepted or rejected for named use
→ informs an Authority-bound Decision
~~~

一条关系至少需要说明：

- Evidence Identity；
- Produced By / Activity；
- Observed Target；
- Coverage；
- Claim；
- Intended Use；
- Accepted / Rejected By；
- Decision Target；
- Non-claims；
- Invalidation / Supersession。

同一份 Test Result 可以：

- 支持一个行为 Claim；
- 不支持 Scope Necessity；
- 被接受为 Development Evidence；
- 仍不足以支持 Qualification；
- 不产生 Release Authority。

第9章拥有 Evidence Use 与 Decision Disposition 的详细模型；本章只保留它们之间的可追踪关系。

---

# 18.14 Review、Acknowledgment、Approval 与 Decision 分开

第10章拥有 Review、Review Target、Finding、Review Independence 与 Review Disposition 的定义；本节只追踪这些对象的提交、授权与下游关系，不重新定义审阅语义。

常见记录需要区分：

| Record | 回答的问题 |
|---|---|
| Review Submitted | Reviewer 针对哪个 Review Target 提交了什么 Finding、Coverage 与 Recommendation |
| Finding | Review Target 相对具名 Criteria、Evidence、Coverage 与 Unknown 呈现什么有范围关系；它本身不授予动作 |
| Review Disposition | 具名 Authority 是否在 Review Contract 范围内，通过 Decision Record 对“如何关闭、限制或继续使用该 Review Target”这一具名 Decision Target 作出处置 |
| Acknowledgment | 某主体确认已看到某项信息 |
| Approval | 某 Authority 对具名 Target 表示允许 |
| Acceptance | 结果是否满足具名 Criterion |
| Adoption | 项目是否开始依赖或维护 |
| Release Authorization | 是否允许进入目标发布面 |
| Release Execution / Deployment Record | 实际分发、部署或推进了什么 |
| Release Outcome | 目标环境、用户或下游实际观察到什么后果 |

`approved` 如果没有 Decision Target 与 Authority，只是一个含义不明的字符串。

无相应 Authority Grant 时，Reviewer 只能提交 Finding 与 Disposition Recommendation。项目可以在 Review Contract 中把窄范围 PASS / FAIL 委托为有权 Review Disposition，但必须同时记录 Target、Scope 与 Grant。

同样：

- Reviewer 报告的 PASS 不等于有权 Review Disposition，更不等于 Adoption；
- Human Acknowledgment 不等于 Approval；
- Merge Approval 不等于 Product Acceptance；
- Release Authorization 不证明 Deployment 已发生；
- Deployment Success 不证明 Outcome 健康。

Release Authorization 是规范性 Decision；Release Execution 是受托动作；Release Outcome 是可观察后果。三者通过 Trace 关联，但不能压成一个 `released` 状态。

Trace 要保留这些差异，不负责把流程强制变长。

一个低风险 Gate 可以被明确委托同时完成 Validation 与 Acceptance；它仍不能把 Authority 扩张到未授权的 Adoption 或 Release。

---

# 18.15 Accountability Surface 按决定与控制分配

**Accountability Surface（问责表面：项目中需要具名主体承担解释、维护、复核或后果责任的目标、控制与决定集合）** 可以包括：

| 责任关系 | 可被行动归因的执行主体 | 承担组织问责的具名角色 |
|---|---|---|
| Intent / Product | Human / Agent Proposal Author | Product / Creative / Business Authority |
| System Design | Human / Agent Builder | Architecture / Engineering Authority |
| Policy | Human / Agent Policy Author、Validator | Policy / Security / Governance Owner |
| Delegation | Grant Issuer、Automation | Delegating Authority 与其 Control Owner |
| Assignment / Execution | Assigned Human / Agent Role | Work Owner；Human Assignee 也可能直接承担 |
| Evidence | Tool、Validator、Evidence Producer | Verification / Evidence Owner |
| Review | Human / Agent Reviewer | Review Authority / Quality Owner |
| Adoption | Candidate / Integration Subject | Product / Project Authority |
| Release / Operations | Deployer、Release Tool / Gate | Release / Operations Authority |
| Recovery | Human / Agent Responder、Recovery Tool | Incident / Recovery Owner |
| Record Governance | Collector、Indexer、Audit Tool | Audit / Records Owner |

一个主体可以承担多个关系，多个主体也可以共同承担一项决定。

但共同承担不等于无人承担。

“最终责任”如果没有 Decision Target、Scope 和制度来源，通常太模糊。

本章不决定法律责任。法律、合同与监管归属依赖司法管辖、组织制度和具体事实，不能由本书对象模型自动推出。

---

# 18.16 Agent 可以被 Operationally Attributed，但不能被一句话变成最终责任主体

Agent 可以：

- 接受 Assignment；
- 在 Role Contract 下承担 Operational Responsibility；
- 使用被授予的 Tool 与 Permission；
- 生成 Change、Evidence、Finding 或 Handoff；
- 触发自动 Gate；
- 在可见条件下升级或返回 `non-result`。

因此 Trace 应记录 Agent Instance、Model / Contract Version、Tool、Context Boundary、Authority Reference 与可见 Action。

但这不表示 Agent 自动拥有：

- 独立的组织职位；
- 风险承受能力；
- 法律责任能力；
- 价值判断的最终 Authority；
- 为自身配置、授权和监督负责的能力。

项目仍需回答：

- 谁选择使用这个 Agent；
- 谁配置它；
- 谁确定它可达到的 Permission；
- 谁授予当前 Authority；
- 谁定义 Review 与 Recovery；
- 谁在 Evidence 不足时决定是否继续依赖。

这不是把所有错误都归给某一个 Human。

它是阻止组织通过“AI 做的”消除设计、授权、监督和处置责任。

---

# 18.17 Traceability 支持责任判断，但不等于 Blame Assignment

事故后，Trace 可以帮助识别：

- 哪个控制存在或缺失；
- 谁拥有哪个 Grant；
- 哪个 Subject 执行了什么；
- 哪些 Evidence 当时可见；
- 哪个 Decision 使结果进入后续阶段；
- 哪些 Observation 或 Escalation 没有发生；
- 哪些恢复动作有效或无效。

这些材料可以支持 Responsibility Review。

但一个时间线不能自动决定“谁有错”。

失败可能来自：

- 目标矛盾；
- 资源不足；
- 组织激励；
- 错误 Policy；
- 不充分 Tool；
- 共同 Context 缺口；
- Review 共因失败；
- Authority 重叠；
- Observer Failure；
- 外部依赖；
- 多个因素联合作用。

如果 Audit 只寻找最后点击按钮的人，会把系统设计问题改写成末端操作者问题。

Accountability 需要同时检查：

~~~text
control design
authority allocation
operational execution
review and decision
organizational conditions
recovery response
~~~

---

# 18.18 Audit Trail 需要可查询、可校正和可暴露缺口

**Audit Trail（审计轨迹：为具名审计目的保存的、具有身份、顺序、来源、完整性边界、访问与保留规则的活动和决定记录集合）** 可能需要：

- Queryability；
- Stable Identity；
- Source / Revision Binding；
- Time / Ordering；
- Cross-system Correlation；
- Tamper Evidence；
- Append-preserving Correction；
- Coverage / Gap；
- Access Control；
- Data Minimization；
- Retention / Deletion；
- Exportability；
- Detector / Collector Health；
- Drill-down to Primary Record。

“不可修改日志”不是充分条件。

一个 Append-only Log 仍可能：

- 从未收到关键事件；
- 使用错误 Clock；
- 将多个 Subject 合并；
- 记录过量敏感数据；
- 丢失 External Side Effect；
- 被错误 Parser 解读；
- 没有任何人查询；
- 因 Retention 过短在事故前消失。

因此 Audit Trail 需要记录自身的 Observation Coverage 与 Integrity Limitation。

---

# 18.19 Tamper-evident 不等于 Tamper-proof

**Tamper-evident（篡改可察觉：记录被删除、替换、重排或无授权改写时，系统有机会通过完整性机制暴露异常）** 可以使用：

- Content Hash；
- Signed Record；
- Append-only Storage；
- Hash Chain；
- Immutable Artifact Reference；
- Independent Copy；
- Access Log；
- Sequence Number；
- Witness / External Timestamp；
- Periodic Integrity Check。

这些机制各自保护不同风险。

例如：

- Hash 可以检测内容变化，但不证明原内容真实；
- Signature 可以绑定 Credential，但不证明签名者理解内容；
- Append-only 可以保留历史，但不能记录从未进入系统的事件；
- External Timestamp 可以约束时间范围，但不能消除 Clock Skew；
- Independent Copy 可以增加删除难度，也会扩大敏感数据表面。

因此本章不使用“Tamper-proof Audit Log”作为默认承诺。

Correction 应通过：

~~~text
original record
→ correction record
→ reason and authority
→ supersession relation
→ affected downstream decisions
~~~

完成，而不是静默重写历史。

---

# 18.20 Time、Ordering 与 Cross-system Correlation 都可能失真

多个 Agent、Tool、CI、Cloud API、Repository 和 Human Interface 可能使用不同 Clock 和 Identity。

需要区分：

- Event Time；
- Ingestion Time；
- Commit Time；
- Decision Effective Time；
- Observation Time；
- Recorded Time。

时间戳相近不表示严格顺序，更不表示因果。

跨系统 Trace 可以使用：

- Correlation ID；
- Parent / Predecessor Reference；
- Attempt ID；
- Work ID；
- Execution Epoch / Profile Reference；
- Request / Response ID；
- Artifact Hash；
- Monotonic Sequence within a source。

Execution Epoch 可以作为一类 Correlation Profile，用于声明一段执行期间适用的 Intent、Baseline、Authority、Tool 与 Governance 配置。

它是可选组织方式，不是所有任务的必备对象，也不是全书新的超级生命周期。

当 Ordering 无法确定时，应记录：

~~~text
before / after
concurrent-or-unknown
observed-by-source-x
conflicting-time-record
~~~

不能为了形成漂亮时间线而虚构精确顺序。

---

# 18.21 Retention、Access 与 Privacy 互相约束

Trace 可能包含：

- Source Code；
- Prompt / Response；
- Personal Data；
- Secret 或 Credential Metadata；
- Business Decision；
- Security Finding；
- Customer / Player Data；
- Human Review；
- Incident Detail；
- Model / Tool Identifier。

“全部永久保留”会扩大：

- Privacy Risk；
- Secret Exposure；
- Insider Access；
- Legal / Contract Risk；
- Storage Cost；
- Search Noise；
- 模型再次摄入污染记录的概率。

Trace Contract 因此需要声明：

- Purpose；
- Required Fields；
- Redaction；
- Access Role；
- Retention Window；
- Deletion / Tombstone；
- Export；
- Cross-border / External Service Boundary；
- Incident Hold 或其他组织规则。

本章只说明 Trace 需要受治理。

具体 Data Classification、Model Boundary、Secret、IP、License 和合规要求由第19章展开。

能够下钻 Primary Record 不表示所有 Reviewer 都应获得全部原始 Prompt、Credential 或个人数据。

---

# 18.22 Reconstruction、Replay 与 Reproduction 不是同一目标

| 目标 | 当前问题 | 典型结果 |
|---|---|---|
| Decision Environment Reconstruction | 能否重组当时可见的 Intent、Baseline、Context、Authority、Action、Evidence 与 Decision | 有边界的外部环境包 |
| Action Replay | 能否重新执行记录的 Action Sequence | 新 Attempt 与新 Observation |
| Result Reproduction | 在声明条件下能否得到可比较结果 | Reproduced / Diverged / `non-result` |
| State Restoration | 能否恢复到允许继续的状态 | Rollback 或 Forward Recovery |

同一 Prompt、Model Name 和 Commit 不足以保证相同输出。

还可能受到：

- Model Revision；
- Sampling；
- Tool Version；
- External API；
- Runtime / OS；
- Data；
- Time；
- Credential；
- Network；
- Hidden Service State；
- Human Judgment；
- Concurrent Change。

因此高风险系统需要的是与风险相称的 Reconstructability 和必要时的 Replay Harness，不是虚假的“完全可重放”标签。

第8章拥有 Attempt Outcome、Target Result、Evaluation Result 与 `non-result` 的分类。一次 Replay 会打开新的 Attempt，并产生新的 Outcome / Result；这些记录可以被用于形成新 Evidence，但不会自动成为 Evidence，也不能覆盖原 Attempt。

---

# 18.23 Decision Reconstruction 按“当时可知”与“后来发现”分层

发生问题后，可以按下列顺序有限重建：

1. 命名 Incident / Decision Target 与时间范围；
2. 保全当前 Artifact、Log、External State 和访问边界；
3. 识别当时的 Intent、Plan、Assignment 与 Authority；
4. 绑定当时的 Baseline、Context Manifest、Tool 和 Subject Configuration；
5. 建立有来源 Timeline，显式保留 Ordering Unknown；
6. 分开 Action、Observation、Evidence、Review 与 Decision；
7. 重建当时可见的 Evidence、Counterevidence、Assumption 与 Unknown；
8. 记录后来新增或被证伪的信息；
9. 提出可重叠 Causal Hypothesis 与替代解释；
10. 检查 Trace Gap、Observer Failure 与 Policy / Authority 问题；
11. 由具名主体决定 Correction、Recovery、Accountability Review 与 Reopen；
12. 保留原记录，通过新关系 Supersede 或 Narrow。

**Contemporaneous View（同期视图：只使用决定发生时可合理获得的信息形成的重建）** 与 **Retrospective View（事后视图：加入后来 Evidence、结果和推导形成的分析）** 必须分开。

否则容易产生 Hindsight Bias：

> 因为现在知道失败，所以当时的失败一定显而易见。

Decision Reconstruction 的目标不是证明过去的人或 Agent“应该知道一切”，而是判断：

- 当时可以知道什么；
- 哪些控制本应暴露风险；
- 哪些假设没有被验证；
- 哪个 Authority 作了什么决定；
- 哪些组织条件需要改变。

---

# 18.24 Later Evidence 应建立 Invalidation Link，不应重写过去

一份 Evidence 后来可能被发现：

- Generator 有缺陷；
- Scope 被夸大；
- Source 已过期；
- Artifact 被污染；
- Sample 不具代表性；
- Reviewer 使用了错误 Baseline；
- External Service 返回不可信结果；
- Human Decision 被新 Policy supersede。

这不表示所有引用它的历史记录都应被删除。

更可检查的处理是：

~~~text
Evidence EV-101
status at decision time: accepted-for-scope

Later finding EV-188
finding: generator omitted target observation

Invalidation relation
EV-188 narrows EV-101

Affected decisions
DEC-184 requires review
REL-031 remains historical but no longer active
~~~

需要分别问：

- 该 Decision 在当时信息下是否合理；
- 新 Evidence 是否改变当前适用性；
- 哪些下游 Claim / Adoption / Release 需要重开；
- 是否存在安全或数据处置；
- 原 Trace 为什么没有更早发现问题。

历史状态与当前状态不能塞进同一个 `valid` 字段。

---

# 18.25 Trace Gap 与 `non-result` 必须分开

**Trace Gap（追踪缺口：Trace Contract 要求的事件、关系、身份、时间或 Source 无法被确认的具名缺失）** 可以包括：

- Collector 未运行；
- External API 不返回 Request ID；
- Agent Instance Identity 丢失；
- Context Manifest 未保存；
- Action 有 Side Effect 但没有 Outcome Observation；
- Decision 只有聊天确认，没有具名 Target；
- Clock / Ordering 冲突；
- Log 被 Retention 删除；
- Record Integrity 失败；
- 访问受限，当前审计者无法检查。

缺口不自动证明：

- 动作没有发生；
- Subject 有恶意；
- Target FAIL；
- 系统健康；
- Decision 无效。

它改变的是可重建关系与可支持结论的 Trace Coverage。

`non-result` 由第8章在 Target 未形成可评价结果时分类；Trace Gap 只表示必要追踪关系无法被确认。二者不能互相推导：完整 Trace 仍可能记录一次 `non-result`，而 Trace 不完整时也可能已经存在 Target Result，只是其来源链无法充分重建。

对于必须追踪的高风险动作，项目可以选择：

- Block；
- Reduce Scope；
- Switch to supervised path；
- Require secondary observation；
- Use break-glass authority；
- Proceed with explicit Unknown and mandatory follow-up。

Emergency / Break-glass 不应伪装成普通合规路径。它需要记录触发条件、Authority、被跳过的控制、Side Effect、补录要求和后续 Review。

---

# 18.26 Random Audit 需要 Sampling Contract，不采用固定比例神话

HCP 提案建议低风险任务由 Human 随机抽查 2–5%。

本章不保留固定比例。

抽查率需要考虑：

- Population；
- Risk / Severity；
- Change Type；
- Model / Workflow Version；
- Novelty；
- Reversibility；
- Detection Power；
- Historical Failure；
- Common-mode Risk；
- Human Capacity；
- Cost of False Confidence。

**Sampling Contract（抽样契约：声明审计总体、抽样框、分层、方法、目标风险、样本身份和结论边界的记录）** 可以组合：

- Random Sample；
- Risk-weighted Sample；
- New Capability Oversample；
- Adversarial / Counterexample Sample；
- Incident-triggered Sample；
- Reviewer Rotation；
- Blind Spot Probe。

抽样结果只支持声明 Population、Window 与 Method 下的结论。

它不自动产生：

- 全局 Trust Score；
- 永久 Autonomy；
- 未抽中任务无缺陷；
- Review Agent 已独立；
- 人类抽查必然发现共因失败。

Audit History 可以成为后续 Autonomy 或 Reliance Decision 的 Evidence，但 Authority 与处置仍由第13章规则约束。

---

# 18.27 Human Control Plane 投影 Trace，不成为 Audit Truth

Human 不应通过浏览全部 Log 才知道发生了什么。

HCP 可以投影：

- 当前高风险 Work；
- Pending Decision；
- Authority / Assignment；
- Trace Coverage；
- Missing / Stale Reference；
- Integrity Warning；
- Evidence 与 Non-claim；
- Review Conflict；
- Exception；
- Intervention / Recovery Path。

但 HCP 需要显示：

- Projection Generated At；
- Source Link；
- Freshness；
- Coverage；
- Collector / Detector Health；
- Unknown；
- Redaction；
- Drill-down Availability。

HCP 上的绿色状态不创造新的 Truth、Authority 或 Accountability。

如果 Summary 丢失 Trace Gap、Counterevidence 或 Decision Target，它会成为认知压缩故障。

第12章负责 Human Decision Interface；第18章只规定投影必须能回到责任链与 Primary Record。

---

# 18.28 Traceability Cost 需要按风险裁剪

记录更多内容会增加：

- Storage；
- Indexing；
- Schema Migration；
- Cross-system Integration；
- Collector Reliability Surface；
- Privacy / Security Surface；
- Review Cost；
- Cognitive Load；
- Retention / Deletion Complexity；
- False Sense of Completeness。

可以按当前风险选择不同 Trace Profile，但不要把它们写成成熟度等级。

## 低风险、局部、易恢复

可能只需要：

~~~text
task / intent reference
current baseline
change identity
simple evidence
named disposition
~~~

## 跨 Thread、跨 Agent 或存在集成风险

可能增加：

~~~text
assignment and role
subject configuration
context / plan versions
handoff receipt
review target
integration disposition
trace gap
~~~

## 高影响、难恢复、多方 Authority 或强审计要求

可能再增加：

~~~text
trace contract
typed decision graph
independent integrity record
detailed authority history
cross-system correlation
retention and access policy
sampling / audit contract
incident reconstruction drill
~~~

好的 Traceability 不是“记录一切”。

它是在合理成本内保存会改变重要判断、恢复和责任解释的关系。

---

# 18.29 现有案例支持哪些有限边界

本节只使用已有项目记录绑定的可观察事实，不把设计提案或当前工作稿反向作为事实来源。

## 18.29.1 SP122 保存了可检查的外部决策环境

[SP122 外部决策环境案例记录](../Evidence/receipts/ER-20260810-003__CLM-C06-003.md) 显示：

- Frozen Agent Run Plan 在执行前已有不可变 Commit；
- Plan 声明 Lane Owner、Tool / Skill、输入输出引用、允许写面、Handoff Authority 与 Conflict Rule；
- Result Manifest 绑定 Plan Commit、Repair Revision、Runtime Identities、Machine Checks、Human Review、Non-claims 与 Evidence Hashes；
- Human Lead 接受 Evidence Chain，同时保留 Adoption 与 Production Block。

这些 Observable Fact 支持：

- 后来者可以在不依赖隐藏推理的情况下检查当时执行边界；
- Plan、Revision、Runtime、Evidence 与 Human Decision 可以通过有来源关系绑定；
- Evidence Acceptance 与后续 Adoption / Release 可以分开。

它们不证明：

- 后来的 Agent 可以从这些材料完整恢复任务；
- 所有字段都必需；
- 记录这些字段提高了速度或质量；
- Runtime Identity 等于完整行动解释；
- 该 Trace 已经完成组织 Accountability。

## 18.29.2 Snapshot Schema 存在，不表示 Live Trace 已经成立

同一案例记录还显示，AI Game Dev OS v4.93 包含 Snapshot Generator，可导出活动对象、Decision、Risk 与 Next Action 引用。

但当时检查到的 `project_status_snapshot.json` 是空 Registry Skeleton，没有已摄入任务。

这个反例说明：

> Schema Capability、Artifact Existence、Operational Population 与 Audit Use 是不同状态。

不能因为存在 Registry 文件就声称项目已有完整 Traceability。

## 18.29.3 D-079 可以从外部记录重建处置边界

[D-079 测试与范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md) 显示：

- Over-scoped Candidate 的 42 项 Focused Tests PASS；
- Human Authority 没有接受该 Candidate 作为 E1 Source Baseline；
- Forward Correction 移除更大范围并进入后续 F1 Ancestry；
- F4a 后续 Test PASS 仍保留 Qualification、Gate 与 Production Non-claims。

这些记录允许后来者区分：

~~~text
test result
scope decision
source adoption
forward correction
later ancestry
release non-claim
~~~

这不需要重建 Agent 当时的隐藏推理。

但该序列也不能证明 Human Scope Decision 在所有项目中最优，不能证明较小实现的长期成本更低。

## 18.29.4 Evidence 与 Accountability 的边界

[SP122 结果包案例记录](../Evidence/receipts/ER-20260810-002__CLM-C06-002.md) 和 [D-079 测试与范围裁决记录](../Evidence/receipts/ER-20260818-003__CLM-C09-001.md) 支持 Agent Assertion、Machine Validation、Human Evidence Disposition、Adoption 与 Release 应保持可区分。

现有 Evidence 未直接验证：

- 本章十一个 Record Role 的完备性；
- Decision Graph 比简单 Commit / Decision Log 更有效；
- Trace Contract 降低事故成本；
- Random Audit 的最佳方法；
- Traceability 能自动形成 Accountability；
- 本章 Accountability Surface 能适用于不同组织、合同或法律环境。

因此，本章把 Accountability Surface 作为候选模型；现有案例只支持 Trace、Authority 与 Decision 的部分分离关系，并未验证该模型的完备性或跨组织适用性。

---

# 18.30 最小实现从一个需要解释的 Decision Target 开始

不要先建立全项目 Graph。

选择一个：

- 经常发生“谁批准了什么”争议；
- Test PASS 与 Adoption 经常混淆；
- 跨 Agent Handoff 容易丢失；
- 事故后无法确认当时 Baseline；
- 高风险 Action 的 Authority 难以追踪；
- Later Evidence 经常需要重开旧 Decision。

建立最小闭环：

1. 分配 Correlation / Work ID；
2. 引用 Intent 与 Decision Target；
3. 保存 Baseline、Context / Plan Version；
4. 绑定 Assignment、Subject Configuration 与 Authority；
5. 记录 Attempt Reference、Action Record、Change Identity 与可见 Side Effect；
6. 绑定 Evidence、Coverage、Counterevidence 与 Non-claim；
7. 记录 Review 与 Decision Disposition；
8. 保存 Attempt Outcome / Result、Exception、Intervention、Recovery 或 Release Outcome 的具名引用；
9. 明确 Trace Gap；
10. 声明 Retention、Access 与 Correction；
11. 从 Human Decision Surface 下钻 Primary Record；
12. 用一次真实 Incident / Scope Dispute 演练 Reconstruction。

验收问题不是：

> Graph 中有多少节点？

而是：

- 能否确认当时用了哪个 Baseline；
- 能否区分谁执行、谁 Review、谁决定；
- 能否看到 Evidence 只支持什么；
- 能否找到缺失关系；
- 能否识别后来被推翻的信息；
- 能否知道谁负责下一步恢复或重开。

如果 Commit、Test 与一条清楚的 Decision Note 已经足够，就不需要额外 Graph。

---

# 18.31 与相邻章节的所有权边界

| 对象 | 所属章节 | 第18章如何使用 |
|---|---|---|
| Intent Artifact、Hierarchy、Conflict、Acceptance Target | 第4章 | 引用决定服务的目标，不重新定义 Intent |
| Context Contract、Pack、Manifest、Access | 第5章 | 追踪供应和访问关系，不推断内部注意 |
| State Claim、Decision、Assumption、Provenance、Execution Baseline | 第6章 | 提供外部决策环境与 Source Identity |
| Work、Execution Contract、Attempt、Checkpoint、Bounded Execution | 第7章 | 提供具名执行边界与 Attempt Reference |
| Attempt Outcome、Target Result、Evaluation Result、Failure、`non-result`、Recovery | 第8章 | 提供执行结果分类与恢复关系 |
| Evidence Coverage、Acceptance、Adoption、Release Authorization | 第9章 | 为 Evidence-to-Decision Edge 提供规范性语义 |
| Review、Review Target、Finding、Review Budget、Review Independence、Review Disposition | 第10章 | 追踪 Review Submitted、Finding、Recommendation 与有权处置 |
| Release Execution、Deployment Record、Release Outcome | 第18章 | 追踪实际动作、目标环境观察和后续状态 |
| HCP Projection、Brief、Compression Validation | 第12章 | 向 Human 投影 Trace Coverage 与 Pending Decision |
| Authority、Delegation、Revocation、Autonomy | 第13章 | 提供 `authorized_by` 与责任边界 |
| Observation、Detector、Exception、Intervention | 第14章 | 提供 Outcome、Gap 与 Collector Health |
| Memory Provenance、Supersession、Retention | 第15章 | 保存长期记录，但不成为 Trace Truth |
| Role、Assignment、Handoff、Conflict、Integration | 第17章 | 提供组织行动和责任关系 |
| Trace Contract、Decision Graph、Attribution、Audit、Reconstruction、Accountability Evidence | 第18章 | 本章核心对象 |
| Data、Model、Secret、Privacy、IP、Supply Chain Boundary | 第19章 | 约束 Trace 采集、访问、存储和外部传输 |
| Metrics、AgentOps 与 Governance Economics | 第20章 | 评价 Trace / Audit 的成本与运行效果 |

第18章不重新定义所有上游对象。

它只回答：

> 这些对象怎样通过有来源关系形成可查询、可有限重建并可用于责任审查的外部记录？

---

# 18.32 本章原则

1. **Git History 与 Decision Trace 互补。** Git 管版本，Trace 连接 Intent、Authority、Evidence 与 Decision。
2. **Traceability 不等于 Accountability。** 记录支持责任判断，不自动分配组织责任。
3. **Decision Graph 是派生投影。** 它引用 Primary Record，不成为第二个 Truth Store。
4. **线性时间线不等于因果。** Action Sequence 需要与 Causal Claim 分开。
5. **External Decision Environment 是可治理对象。** 不依赖隐藏推理完成审计。
6. **Stated Rationale 需要来源和时间。** 它是可审查说明，不是完整内部原因。
7. **Context Supplied 不等于 Context Used。** Access、Citation 与内部影响保持边界。
8. **Evidence Link 声明 Claim、Scope 与 Use。** Evidence 存在不证明 Decision 正确。
9. **Approval 必须有 Target 和 Authority。** `approved` 不能吞掉 Review、Adoption 与 Release。
10. **Agent 可被行动归因。** 但组织不能把设计、授权和最终处置责任推给模型。
11. **Audit Trail 暴露 Coverage 与 Gap。** Append-only 不等于完整。
12. **Tamper-evident 不等于 Tamper-proof。** Integrity Mechanism 不证明原始内容真实。
13. **Reconstruction、Replay、Reproduction 与 Restoration 分开。** 新 Attempt 不覆盖旧 Evidence。
14. **同期视图与事后视图分开。** Later Evidence 通过 Invalidation / Supersession 更新关系。
15. **Random Audit 需要 Sampling Contract。** 固定比例和全局 Trust Score 不进入正文。
16. **Trace 深度与风险相称。** 简单任务不需要为 Graph 而 Graph。

---

# 18.33 常见反模式

- 把 Git 贬低成只能保存 Diff；
- 把 Commit Author 当作唯一代码生产者、批准者和责任主体；
- Decision Graph 复制 Repository State；
- 把所有工程关系压成一条线性 Pipeline；
- 时间相邻自动写成因果；
- 用一个 `actor` 字段吞掉 Agent、Tool、Committer、Reviewer 与 Authority；
- Authentication Log 自动变成 Accountability；
- 保存 Full Transcript 后声称已保存隐藏推理；
- 要求模型输出完整 Chain-of-Thought 才能审计；
- Stated Rationale 被当作唯一真实原因；
- Context Manifest 被写成模型已理解的内容；
- Tool Access Log 被写成信息实际影响了决定；
- Plan 被静默替换，不保留 Replanning Trigger；
- `approved` 没有 Decision Target；
- Review PASS 自动成为 Adoption / Release；
- Evidence Link 不声明 Claim、Scope 与 Non-claim；
- 把 Agent 写成最终法律或组织责任主体；
- 事故复盘只寻找最后点击按钮的人；
- Append-only Log 被写成完整且真实；
- Hash 正确被解释为内容正确；
- 缺少日志被解释为动作没有发生；
- Trace Gap 被改写成 Target FAIL；
- 所有高风险工作都承诺 Deterministic Replay；
- Replay 新结果覆盖原 Attempt；
- Later Evidence 静默改写历史 Decision；
- 同期视图混入后来才知道的信息；
- 固定 2–5% 抽查被推广为通用比例；
- Audit PASS 自动产生永久 Trust 或 Autonomy；
- 全量永久保存 Prompt、Secret 和个人数据；
- Registry 文件存在就声称 Live Trace 已运行；
- 用 Graph 节点数量证明可审计性；
- 低风险小改动被强制生成完整责任图。

---

# 18.34 本章检查清单

## Target 与 Contract

- 当前 Trace 服务哪个 Work、Decision Target、Risk 或 Incident？
- Trace Contract 要求哪些 Record、Relation、Integrity、Access 与 Retention？
- Coverage 是 Complete-for-scope、Partial、Missing 还是 Unknown？
- Hidden Reasoning 是否被明确排除？

## Identity 与 Authority

- Requester、Worker、Agent Instance、Tool、Reviewer、Authority、Committer 与 Deployer 是否可区分？
- Subject Configuration 是否绑定模型／规则、Tool、Credential Scope 与运行边界？
- Authentication、Attribution、Responsibility 与 Accountability 是否被混用？
- Action 的 Authority Reference 是否在当时有效？

## Baseline、Context 与 Plan

- Intent、Execution Baseline、Context Manifest、Plan 和 Assignment 使用哪个 Version？
- Context 是 Eligible、Selected、Supplied、Accessed 还是 Cited？
- 是否错误推断模型内部使用？
- Replanning 是否保留 Trigger、Scope 与 Authority Impact？

## Action、Change 与 Outcome

- Action 是 Requested、Attempted、Completed、Interrupted 还是 Revoked？
- Tool Success 是否有独立 Outcome Observation？
- Change Identity 是否绑定 Repository、Runtime、Data 或 External State？
- Action Sequence 是否被误写成 Causal Claim？
- Side Effect 与 In-flight Work 是否进入 Trace？

## Evidence、Review 与 Decision

- Evidence 实际观察了什么，Coverage 与 Non-claim 是什么？
- Evidence-to-Claim / Decision Edge 是否声明 Scope 与 Use？
- Review Contract、Finding、Disposition 与 Independence 是否清楚？
- Acknowledgment、Approval、Acceptance、Adoption、Release Authorization 与 Deployment 是否分开？
- Decision Record 是否包含 Target、Authority、外部理由、Assumption、Unknown、Expiry 与 Supersession？

## Audit 与 Integrity

- Audit Trail 是否可查询并能下钻 Primary Record？
- Collector / Detector Health 是否可见？
- Hash、Signature、Append-only 与 External Copy 分别保护什么风险？
- Event Time、Ingestion Time、Effective Time 与 Recorded Time 是否混淆？
- Cross-system Correlation 和 Ordering Unknown 是否保留？
- Correction 是否通过追加与 Supersession 完成？

## Reconstruction 与 Accountability

- 同期视图与事后视图是否分开？
- Later Evidence 怎样 Narrow、Invalidate 或 Reopen 旧 Decision？
- Trace Gap 是否被显式记录？
- 谁对 Intent、System Design、Policy、Delegation、Review、Adoption、Release、Recovery 与 Record Governance 负责？
- 是否把最后操作者错误当成全部责任？
- 法律责任是否被对象模型未经依据地自动推出？

## Cost、Privacy 与 Scope

- 是否记录了超过审计目的所需的 Prompt、Secret 或个人数据？
- Access、Redaction、Retention、Deletion 与 Export 是否有 Owner？
- Sampling Contract 是否声明 Population、Method 与结论边界？
- 当前项目需要 Decision Graph，还是 Commit + Test + Decision Note 已足够？
- Trace 成本是否超过被保护风险与后续解释价值？

---

# 18.35 本章结论

Traceability and Accountability 不要求保存 Agent 的隐藏思维，也不把所有活动压成一条线性日志。

它建立的是：

~~~text
named Trace Contract
→ source-linked external decision environment
→ typed Action / Change / Evidence / Review relations
→ Authority-bound Decision Record
→ visible Outcome, Gap and Correction
→ bounded Reconstruction and Accountability Review
~~~

其中：

- Git 保存版本事实，Decision Trace 保存工程关系；
- Context Trace 记录供应与访问，不声称模型内部注意；
- Action Record 保存可见执行，不自动证明 Intent 或因果；
- Evidence Link 说明 Claim、Scope 与 Use，不产生 Authority；
- Decision Record 保存外部理由和生命周期，不伪装成 Hidden Reasoning；
- Audit Trail 暴露完整性边界，不承诺记录一切；
- Attribution 连接 Subject 与 Action，不自动完成 Accountability；
- Accountability 绑定具名目标、控制、Authority、Human / Organization Role 与后果关系。

> **Preserve what was externally knowable, authorized, done, observed and decided. Do not pretend to recover hidden reasoning. Traceability supplies accountability evidence; it does not create accountability.**

中文语义是：

> **保存当时外部可知、被授权、实际执行、被观察和被裁决的内容，不伪装成能够恢复隐藏推理；Traceability 可以提供问责依据，但不能自动创造 Accountability。**

下一章将讨论：当 Trace 本身包含 Source Code、Prompt、Secret、个人数据、外部 Model / Tool 与第三方 Artifact 时，怎样建立 Security、Privacy 与 IP Boundary，避免“为了可追溯”制造新的泄露、越权与供应链风险。
