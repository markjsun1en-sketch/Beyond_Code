# RR-033：第20章 AgentOps、成本与模型漂移首轮调整计划

- 记录日期：2026-08-26
- 工作稿：[第20章 AgentOps、成本与模型漂移](../OptimizedDocs/第20章_AgentOps_成本与模型漂移_首轮修订稿.md)
- 原始结构：[全书大纲第20章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 跨章来源：[RR-011](RR-011_Execution_Epoch与治理逻辑.md)、[RR-024](RR-024_第13章Governed_Autonomy首轮回接说明.md)、[RR-025](RR-025_第14章Observability与Intervention首轮回接说明.md)、[RR-027](RR-027_第16章Self_Evolution_Engineering首轮回接说明.md)、[RR-030](RR-030_第19章Security_Privacy与IP_Boundary首轮回接说明.md)
- 记录性质：章节对象与所有权规划，不是效果验证或经济模型证明
- 实施状态：`implemented / accepted`
- Evidence Routing：本轮只审查候选概念模型，不新建 Claim 或 Receipt；效果、精确历史、跨项目推广和准备反馈 AI Game Dev OS 的结论另行路由

## 1. 入口结论

原大纲保留了六个必要主题：

1. AgentOps 与 DevOps / LLMOps 的关系；
2. 成本模型；
3. Model Routing；
4. Model / Tool Drift；
5. Re-evaluation；
6. Agent Economics。

问题不在主题缺失，而在对象层级混合：

- Agent 状态、Tool Call、Latency 与 Permission Use 是 Observation；
- Model Routing 是运行处置；
- Drift 是相对具名 Baseline 的变化判断；
- Re-evaluation 是由变化或到期触发的重新取证与裁决；
- Economics 是为具名 Decision Target 定义成本边界与比较方式。

如果把它们写成一个 Dashboard 指标列表，第20章会重复第14章，并把“可观察”
误写成“已解释”或“可优化”。

第20章建议围绕一个更窄的问题展开：

> 在具名运行配置、Workload、时间窗和 Authority 下，Agent 生产系统是否仍处于已经接受的 Outcome、Risk、Cost、Human Attention 与 Control 边界内；如果不是，什么证据能够支持继续、收窄、重路由、回滚、暂停或退役？

这是一项候选工程分解，不声称 `AgentOps` 已经构成边界稳定的新学科，也不声称
一套统一指标可以比较所有 Agent 系统。

## 2. 第20章拥有和不拥有的对象

| 对象 | 所属章节 | 第20章的使用边界 |
|---|---|---|
| Observation、Detector、Signal、Intervention | 第14章 | 消费有来源的运行观察，不重新定义 Telemetry Truth |
| Capability、Permission、Authority、Autonomy Profile | 第13章 | 观察实际使用和变化，但不自行授予或扩大 Authority |
| Evaluation、Adoption、Post-adoption Disposition | 第16章 | 提供长期运行窗口和再评估触发，不取代 Candidate Lifecycle |
| Data、Model、Tool、Supply Chain、IP Boundary | 第19章 | 观察这些边界是否漂移，不重新定义安全或法律结论 |
| Evidence Use、Acceptance、Adoption、Release | 第9章 | 指明指标和运行记录能支持什么处置 |
| Trace、Provenance、Accountability | 第18章 | 提供可追踪来源；第20章不从指标自动推导责任 |
| Operational Baseline、Evaluation Window、Drift Finding、Re-evaluation Case、Operational Disposition | 第20章 | 本章候选核心对象 |

AgentOps 不应成为一个复制所有上游对象的新 Truth Store。它更适合作为运行评价和
处置层：引用上游身份、合同、观察和 Evidence，在时间维度上判断它们是否仍适用。

## 3. 四个核心对象与两个投影

首轮工作稿优先限制为四个核心对象。

### 3.1 Operational Baseline

**Operational Baseline（运行基线：在具名用途和时间窗内，用于解释运行结果的
版本化配置与边界引用集合）** 可以引用：

- Workload / Use-case 与 Population；
- Model、Endpoint、Version / Change Policy；
- Tool、Skill、Prompt / Policy、Context Contract；
- Permission、Credential Scope 与 Authority；
- Evaluation Suite 与已知 Coverage；
- Outcome / Guardrail Boundary；
- Budget、Owner 与有效期。

它不是“已知最佳配置”，也不复制所有原始 Artifact。

### 3.2 Evaluation Window

**Evaluation Window（评价窗口：为一组可比 Work、配置和时间范围绑定分母、
Observation Coverage 与处置用途的观察区间）** 需要说明：

- 时间和 Work 边界；
- 纳入与排除条件；
- Baseline Identity；
- Outcome Unit 与分母；
- 数据缺口、采样和未观察面；
- Incident、Override 与异常流量是否单列；
- 这组观察准备支持哪个 Decision Target。

没有分母和纳入规则的 `success rate`、`intervention rate` 或 `cost` 不可稳定比较。

### 3.3 Drift Finding

**Drift Finding（漂移发现：记录当前观察与具名 Baseline 之间的相关变化、
覆盖范围、不确定性和潜在影响的版本化判断）** 必须分开：

~~~text
observed change
≠ impact inference
≠ cause candidate
≠ operational disposition
~~~

变化可能真实存在，但尚未证明影响结果；结果退化也可能来自 Workload、Evaluator、
Tool、Policy 或观测覆盖变化，而不是 Model 本身。

### 3.4 Re-evaluation Case 与 Operational Disposition

**Re-evaluation Case（再评估案件：由 Change、Expiry、Incident、Boundary Breach
或新用途触发的有范围重新取证与裁决工作）** 连接：

- Trigger；
- Baseline 与 Candidate Current State；
- 需要重跑或补充的 Evaluation；
- Security / Authority / Rights Guardrail；
- Cost 与 Human Review Boundary；
- Decision Authority；
- Disposition、有效期与后续观察。

**Operational Disposition（运行处置：有权角色针对具名运行配置作出的继续、
观察、收窄、重路由、Canary、回滚、暂停、重新授权或退役决定）** 是案件的结果，
不是 Drift Detector 自动生成的事实。

### 3.5 两个投影，不新增 Truth Store

- **Cost Attribution View**：把已有运行、Review、等待、返工、恢复和维护记录
  投影到具名 Decision Target；
- **Routing Comparison View**：在相同 Purpose、Data / Tool Boundary 与
  Evaluation Window 下比较候选 Model / Tool 路径。

它们是查询与决策视图，不要求再建立两套独立 Registry。

## 4. AgentOps 与 Observability 的边界

第14章回答“发生了哪些可观察事件、哪些 Detector 触发、怎样 Intervention”。

第20章回答：

- 这些事件属于哪个 Baseline 和 Evaluation Window；
- Outcome、Guardrail、Cost 或 Human Capacity 是否越界；
- 变化能否被归因，还是只能形成 Cause Candidate；
- 是否触发 Re-evaluation；
- 谁有权改变 Routing、Budget、Permission、Evaluation 或运行状态。

因此 AgentOps 不等于：

- 收集所有 Log；
- 建立一个统一 Dashboard；
- 用单一成功率替代 Acceptance；
- 用平均延迟掩盖尾部失败；
- 从 Tool Call 数量推断生产力；
- 从 Human Intervention 数量推断系统成熟度。

## 5. 指标先绑定 Claim、分母和处置用途

每个运行指标至少需要：

~~~text
metric definition
+ source and coverage
+ baseline identity
+ population / denominator
+ time window
+ segmentation
+ uncertainty / missingness
+ decision use
+ owner
~~~

首轮可按八个不可自动合并的观察面组织：

1. Outcome 与 Acceptance；
2. Reliability、Failure 与 `non-result`；
3. Latency、Waiting 与 Queue；
4. Model、Tool、Compute 与 Environment Cost；
5. Review、Decision 与 Human Attention；
6. Coordination、Handoff 与 Integration；
7. Rework、Incident、Recovery 与 Maintenance；
8. Permission、Security、Evaluation Coverage 与 Control Health。

`cost_per_accepted_outcome` 可能比 `token_per_task` 更接近生产问题，但它仍不能
吞并安全、隐私、不可逆损失、Human Decision Right 或创意质量等 Guardrail。

## 6. Cost Boundary 与 Governance Economics

成本需要绑定 Decision Target、Scope 和时间窗，避免把不同层级重复计入。

候选成本面包括：

- Direct Execution：Model、Token、Compute、Tool、Build、Test Environment；
- Context：Retrieval、Assembly、Storage、Transfer 与 Freshness Maintenance；
- Verification：Test、Evaluation、Review、Approval 与 Evidence；
- Human Attention：理解、等待、Context Reconstruction、Decision 与 Interruption；
- Coordination：Decomposition、Handoff、Conflict、Integration 与 Output Triage；
- Failure：Retry、Rework、Rollback、Incident、Recovery 与 External Repair；
- Governance：Policy、Gate、Trace、Detector、Exception Handling 与 Audit；
- Maintenance：Prompt、Skill、Model / Tool Integration、Baseline 与 Evaluation Refresh；
- Opportunity / Delay：错过窗口和排队造成的影响；只在边界可解释时估计。

Governance Economics 不应被压成“治理越少越好”或一个伪精确公式。

推荐使用多目标比较：

~~~text
compare incremental execution, review, waiting, cognitive,
governance, rework, recovery and maintenance cost

subject to:
  protected control floor
  legal / security / privacy constraints
  unacceptable-loss limits
  human decision rights
  minimum outcome and evidence boundaries
~~~

`Governance Overhead Ratio`、`Rework Avoided`、`Failure Cost Avoided`、
`False Escalation Rate` 和 `Under-governance Incident Rate` 可以作为局部指标，
但必须说明反事实、漏报、损失不对称和 Observation Coverage。它们不是通用成熟度分数。

## 7. Drift 不只属于 Model

首轮 Drift Taxonomy 建议包括：

- Identity / Version Drift：Model、Tool、Skill、Prompt、Policy 或依赖身份变化；
- Workload Drift：任务、语言、数据、用户或难度分布变化；
- Behavior / Output Drift：格式、稳定性、错误模式或结果分布变化；
- Tool / Interface Drift：Schema、Side Effect、Latency、Error 与外部 API 变化；
- Permission / Authority Drift：开放能力、Credential Scope 或授权边界变化；
- Control Drift：Detector、Gate、Sandbox、Fallback 或 Recovery 能力变化；
- Evaluation Drift：Dataset、Judge、Rubric、Coverage 或测量机制变化；
- Economic Drift：价格、Token、Runtime、Review、Waiting 或 Maintenance Cost 变化；
- Contract / Rights Drift：Provider Terms、Region、Retention、License 或用途边界变化。

`Drift` 不是任何数字变化的同义词。它需要相对于具名 Baseline，并且对某个
Claim、Boundary 或 Decision Target 具有潜在意义。

## 8. Re-evaluation 按 Trigger 和 Impact Scope 裁剪

候选 Trigger 包括：

- Model / Endpoint / Tool / Skill 身份或 Change Policy 变化；
- Tool Function、Schema、Permission、Credential 或 Action Sink 变化；
- Provider Terms、Data Region、Retention、License 或安全事件变化；
- Outcome、Guardrail、Cost 或 Human Load 超出当前 Boundary；
- Incident、Rollback、Unknown External Result 或重复人工 Override；
- Evaluation、Detector 或 Observation Coverage 变化；
- Baseline 到期；
- 新 Workload、新法域、新 Data Class 或更高影响用途。

Re-evaluation 不等于每次全部重测。它应先确定：

1. 哪个引用或边界发生变化；
2. 哪些 Claim 和下游处置受到影响；
3. 原 Evidence 哪部分仍可复用；
4. 需要补充什么 Evaluation；
5. 在完成前应继续、限制、Canary、Fallback 还是暂停。

## 9. Model Routing 不是便宜模型与强模型的静态分层

第19章已经拥有 Data Permission、Provider Contract、Local / Private / Cloud 与
Tool / Network Boundary。第20章只处理这些路径在运行中的评价和调整。

Routing 比较需要尽量保持以下条件可比：

- Purpose 与 Workload；
- Data / Rights Boundary；
- Tool / Permission / Authority；
- Evaluation Window 与 Outcome Unit；
- Retry、Fallback、Review 与 Recovery Policy；
- Cost Boundary；
- Model / Endpoint / Tool Identity。

Routing Disposition 可能是继续、局部任务重路由、Fallback、Canary、限制能力或
暂停，而不是把所有工作统一迁往最低价格或公开 Benchmark 最高的模型。

## 10. 与 AI Game Dev OS Evidence 的路由

当前材料可以支持提出观察问题，但还不能直接证明：

- AI Game Dev OS 已降低 Total Production Cost；
- 某个 Governance Profile 具有更低单位风险成本；
- 多 Agent、更多 Gate 或更小实现具有稳定净收益；
- 某次 v4.94 修正已经改善长期 Reliability、Cost 或 Human Load。

如果第20章准备引用 v4.94 的 D-048、D-073—D-075、D-079 或其他运行案例来
支持上述效果或准备反馈到 OS，应单独选择不超过三条 Claim，并按正式 Evidence
流程绑定 Commit、Branch、Dirty State、Artifact、Counterevidence 与 Human
Disposition。

首轮正文可以先把这些案例写成待检验的 Operational Questions，不把缺少对照的
过程变化写成效果结论。

## 11. 计划中的章节结构

1. 为什么 AgentOps 不是 Dashboard；
2. 必要、有用与可选的运行治理；
3. AgentOps 与 DevOps / LLMOps 的关系边界；
4. Operational Baseline 与 Evaluation Window；
5. Outcome、Guardrail、Coverage 与分母；
6. Total Production Cost 的边界；
7. Governance Economics 与 Protected Control Floor；
8. Model Routing 的运行处置；
9. Model、Tool、Permission、Evaluation、Economic 与 Contract Drift；
10. Observation、Impact、Cause 与 Disposition 分离；
11. Re-evaluation Trigger 与 Scope；
12. Continue、Restrict、Reroute、Canary、Rollback、Suspend 与 Retire；
13. Human Attention 与 Decision Capacity；
14. AI Game Dev OS v4.94 的待验证运行问题；
15. 跨章接口、原则、反模式、检查清单与结论。

## 12. 实施顺序

1. 在 `OptimizedDocs/` 创建第20章首轮工作稿，采用三项 Header；
2. 先完成概念对象、跨章所有权和反例，不先添加正式 Claim；
3. 检查所有指标是否具备 Baseline、分母、窗口、Coverage 与 Decision Use；
4. 检查所有 Drift 句子是否分开 Observation、Impact、Cause 与 Disposition；
5. 检查 Economics 是否保留 Protected Floor、不可量化损失和 Human Right；
6. 再判断是否需要引用 v4.94 并触发正式 Evidence；
7. 完成后回看第19章五个候选对象，删除第20章没有消费的字段；
8. 将章节对象和措辞交给 Human Review，不从计划状态推导接受。

## 13. 2026-08-26 实施结果

[第20章首轮修订稿](../OptimizedDocs/第20章_AgentOps_成本与模型漂移_首轮修订稿.md)
已经形成，共 `20.1–20.36` 三十六节。

原大纲六个主题均保留，但对象关系已经重排：

| 原主题 | 首轮修订位置 | 结构变化 |
|---|---|---|
| AgentOps 与 DevOps / LLMOps | 20.2–20.3 | 从工具类别改为运行评价与处置范围 |
| 成本模型 | 20.11–20.15 | 从 Token 清单扩展为有 Cost Boundary 的多目标比较 |
| Model Routing | 20.16–20.17 | 从模型等级选择改为绑定 Purpose、Boundary、Evaluation 与 Fallback 的处置 |
| Model / Tool Drift | 20.18–20.23 | 扩展到 Workload、Permission、Control、Evaluation、Economic 与 Contract Drift |
| Re-evaluation | 20.24–20.29 | 从全量重测清单改为 Trigger、Impact Mapping、Case、Authority 与 Disposition |
| Agent Economics | 20.11–20.15 | 明确为总生产经济性；Governance Economics 是其中一部分 |

### 13.1 对象结果

正文采用四个候选核心对象：

1. Operational Baseline；
2. Evaluation Window；
3. Drift Finding；
4. Re-evaluation Case，以及它产生的 Operational Disposition。

Cost Attribution View 与 Routing Comparison View 被限定为投影，不建立新的
Truth Store。Metric Contract、Outcome Unit 与 Routing Disposition 是接口对象，
不要求实现为全局 Registry。

### 13.2 Evidence Routing 结果

- 没有为概念模型新建 Claim ID 或 Evidence Receipt；
- 没有声称统一指标适用于所有 Agent 系统；
- 没有声称 AI Game Dev OS v4.94 已降低 Total Production Cost、Human Load 或事故率；
- D-073—D-075、D-048 与 D-079 只用于说明 Governance Activity、Verifier Result、
  Target `non-result`、Test PASS 与 Human Acceptance 的测量语义；
- 如果后续准备从这些案例推导效果或反馈到 AI Game Dev OS，仍需单独进入正式 Evidence Workflow。

### 13.3 第19章五对象下游消费检查

第20章完成后，对第19章五个候选对象进行了接口回看：

| 第19章对象 | 第20章消费位置 | 当前处理 |
|---|---|---|
| Data Handling Profile | Workload、Data Class、Purpose、Routing 与 Contract / Rights Drift | 保留引用，不复制全部字段 |
| Model Processing Contract | Operational Baseline、Provider Change、Region、Retention、Terms 与 Re-evaluation | 保留 |
| Tool Security Contract | Tool / Permission / Control Drift、Action Sink、Recovery 与自动处置 | 保留 |
| Supply Chain Component Record | Identity、Version、Change Policy、Monitoring、Fallback 与 Retirement | 保留 |
| IP Disposition Record | Intended Use、Provider Terms、License、Jurisdiction 与 Rights Trigger | 按相关用途引用，不进入每个低风险 Baseline |

本次没有仅因“正文存在下游引用”就宣称这些对象已经最小或完备，也没有删除字段。
是否过重仍需要在真实 Work 的 Baseline 和 Re-evaluation Case 中试跑；特别是 IP 与
Supply Chain 字段应按 Purpose 和风险选择，而不是进入每个 AgentOps Record。

### 13.4 验证结果

- 三项 Reader-facing Header 已应用；
- 数字章节 Heading 连续为 `20.1–20.36`；
- Markdown Fence 成对闭合；
- 原大纲六个主题均有正文落点；
- Reader-facing 正文没有 Claim ID、Receipt ID、Human Status 或 Claim Ledger 状态；
- v4.94 三组案例均保留明确不支持范围；
- 相对链接目标可解析；
- `git diff --check` 通过；
- `OringinalDocs/` 没有 tracked diff。

### 13.5 待 Human Review

1. 第20章是否应以“版本化运行基线是否仍处于可接受边界”为中心问题；
2. 四个核心对象与两个投影是否过多或不足；
3. Agent Economics 与 Governance Economics 的上下位关系是否符合作者观点；
4. Drift 是否应同时覆盖 Model、Tool、Workload、Permission、Control、Evaluation、Economic 与 Contract；
5. v4.94 是否只作为测量语义案例，而暂不承担效果证明；
6. 第20章接受后是否进入第21章 Lifecycle。

## Human Disposition

- Status: `accepted`
- Decision by: Human Author
- Decision at: 2026-08-26
- Accepted scope: 第20章以版本化 Operational Baseline、Evaluation Window、Drift Finding、Re-evaluation Case 与有 Authority 的 Operational Disposition 组织 AgentOps；Agent Economics 覆盖总生产经济性，Governance Economics 是其受 Protected Control Floor 约束的子问题；Drift 同时覆盖 Model、Tool、Workload、Permission、Control、Evaluation、Economic 与 Contract；v4.94 只作为测量语义案例。
- Excluded scope: 四个核心对象与两个投影已经完备或最优；统一指标可以比较所有 Agent 系统；本章已经证明 AI、多 Agent、特定 Routing 或 Governance 配置降低成本、提高可靠性或减少风险；v4.94 已形成长期效果对照。
- Evidence boundary: 本章没有新增正式 Claim 或 Receipt；后续效果主张、跨项目推广或准备反馈 AI Game Dev OS 的结论仍需单独路由。
- Verbatim decision: “20 章确认 ok，接受并进入 21 章”。
- Rationale: 作者在收到章节结构、限制与验证结果后明确接受，并授权工作流进入第21章；该决定不扩大本章明示的非主张范围。
