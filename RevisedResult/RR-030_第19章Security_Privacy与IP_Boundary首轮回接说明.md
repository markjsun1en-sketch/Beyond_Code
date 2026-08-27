# RR-030：第19章 Security、Privacy 与 IP Boundary 首轮回接说明

- 记录日期：2026-08-24
- 工作稿：[第19章 Security、Privacy 与 IP Boundary](../OptimizedDocs/第19章_Security_Privacy与IP_Boundary_首轮修订稿.md)
- 原始结构：[全书大纲第19章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- Security Claim：[CLM-C19-001](../Evidence/receipts/ER-20260824-004__CLM-C19-001.md)，`partial / unreviewed / narrow`
- Supply Chain Claim：[CLM-C19-002](../Evidence/receipts/ER-20260824-005__CLM-C19-002.md)，`partial / unreviewed / narrow`
- IP Claim：[CLM-C19-003](../Evidence/receipts/ER-20260824-006__CLM-C19-003.md)，`partial / unreviewed / narrow`
- 案例边界：[CLM-C06-004](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md)，`partial / accepted / narrow`
- 章节接口：[第5章 Context](../OptimizedDocs/第5章_Context对象边界回接稿.md)、[第13章 Governed Autonomy](../OptimizedDocs/第13章_Governed_Autonomy_首轮修订稿.md)、[第15章 Memory Engineering](../OptimizedDocs/第15章_Memory_Engineering_首轮修订稿.md)、[第18章 Traceability](../OptimizedDocs/第18章_Traceability_and_Accountability_首轮修订稿.md)
- 记录性质：章节回接说明与 Evidence 适配审计，不是法律意见或新的外部标准
- 章节对象模型与措辞状态：`accepted`（仅限候选工程分解与现有限制）

## 回接结果

第19章已经形成独立工作稿。

原大纲的六个问题都被保留：

1. 数据边界；
2. Model Boundary；
3. Tool and Agent Permissions；
4. 知识产权；
5. Supply Chain Security；
6. Local、Private 与 Cloud Boundary。

本轮没有沿用“先按敏感度分类，再决定本地或云”的单轴结构。

原因是其中混合了不同问题：

- 公开／内部／机密描述 Access 与 Confidentiality；
- 个人数据描述 Data 与个人的关系；
- 受监管描述法域、用途和主体触发的义务；
- IP / License 描述权利与合同；
- Tool Permission 与 Authority 描述行动边界；
- Local / Private / Cloud 描述部署与处理拓扑。

它们会相互影响，但不能互相替代。

章节中心句是：

> Treat every external input as data without authority, every model output as an untrusted proposal, and every tool action as an independently authorized side effect.

本轮将其中文语义固定为：

> 把每个外部输入先视为不带指令权威的数据，把每个模型输出视为未经验证的提案，把每个 Tool Action 视为需要独立授权的副作用。

## 三条核心 Claim

### CLM-C19-001：Security Boundary

收窄后的主张是：

> 当 Agent 会读取不可信内容并调用可产生副作用的 Tool 时，仅依赖 Prompt、模型自律或内容过滤不足以形成安全边界；系统应在模型外分离 Data 与 Instruction，限制 Context、Function、Permission、Credential 与 Action Sink，并按风险设置独立授权、验证、记录和停止机制。部署位置只改变信任边界，不自动证明安全。

Coverage 为 `partial`：

- OWASP LLM01 支持 Direct、Indirect、Multimodal Injection 及 RAG / Fine-tuning 并非完整缓解；
- OWASP LLM06 支持分离 Functionality、Permission 与 Autonomy；
- OWASP LLM07 支持 System Prompt 不应被当成 Secret 或 Security Control；
- D-048 支持 Trusted Tool 也可能在目标前产生未声明 Side Effect，且独立 Check 可以 Fail Closed。

不支持：

- 通用充分控制集；
- Prompt Injection 的完全消除；
- Local、Private 或 Cloud 的绝对安全排序；
- 所有动作都必须人工批准。

### CLM-C19-002：Supply Chain Boundary

收窄后的主张是：

> 供应链对象不应只包括 Package；凡是能够改变 Context、Decision、Tool、Build、Runtime 或 Output 的行为组件，都应按风险记录身份、来源、版本、权限、权利、更新、监控与恢复。Provenance 只支持来源和产生过程 Claim。

Coverage 为 `partial`：

- SLSA v1.2 提供 Provenance 的限定定义；
- NIST AI 600-1 明确纳入 Provider、Model、Library、Tool、API、Monitoring、Incident Response 与 Fallback；
- D-048 说明 Script / Launcher 也可能改变 Authority-bearing Surface。

不支持：

- 工作稿组件列表已完备或最小；
- 所有远程 Model / Service 都能固定 Digest；
- Registry、SBOM 或 Provenance 能证明行为安全；
- 新增治理必然降低事故率。

### CLM-C19-003：IP Boundary

收窄后的主张是：

> `AI-generated` 不能单独决定 IP 处置；Input Permission、Provider Terms、Third-party License、Human Contribution、Output Provenance、下游用途与法域需要分开。

Coverage 为 `partial`：

- U.S. Copyright Office Part 2 支持在美国著作权资格分析中区分辅助使用、Human Contribution、纯 AI 生成材料与个案判断；
- NIST AI 600-1 支持将 Ownership、Usage Rights、Provenance、Third-party IP、Training Data 与 Infringement Response 分开。

不支持：

- 具体 Output 的所有权、著作权资格或不侵权；
- 全球统一规则；
- Prompt 数量或长度可以机械证明 Human Authorship；
- Similarity / License Scanner PASS 可以完成法律裁决。

## 原大纲的六项结构修正

### 1. 数据边界从分类表改为 Data Handling Profile

工作稿保留公开、内部、商业机密、个人和受监管数据，但将它们拆到不同轴：

- Access；
- Person Relation；
- Rights；
- Integrity / Availability Criticality；
- Regulatory / Contract Duty；
- Instruction Trust；
- Lifecycle。

并将 `may_read`、`may_send_to_model`、`may_store`、`may_learn`、`may_publish` 与 `may_treat_as_instruction` 分开。

### 2. Model Boundary 从位置选择改为 Processing Contract

工作稿不再以 Model 名称或 `local / cloud` 标签代替处理条件。

新增 Model Processing Contract，覆盖：

- Provider / Operator；
- Endpoint / Model / Version Policy；
- Region / Subprocessor；
- Retention / Training；
- Logging / Support Access；
- Deletion / Incident；
- Output Terms；
- Tool / Network / Retrieval；
- Change Control / Fallback。

### 3. Tool Permission 从风险清单改为可执行 Contract

新增 Tool Security Contract，并从第13章回接 Capability、Permission 与 Authority。

Tool Contract 约束：

- Function；
- Resource / Path / Destination；
- Parameter；
- Credential；
- Environment；
- Side Effect；
- Approval；
- Postcondition；
- Recovery。

同时明确 System Prompt、Sandbox 与 Human Approval 的有限作用。

### 4. IP 从问题列表改为 Disposition Interface

原大纲已经提出输入权利、License、训练数据、生成资产、Skill 与 Memory 所有权问题。

工作稿进一步区分：

- Access / Processing Permission；
- Confidentiality / Trade Secret；
- Provider Terms；
- Third-party License；
- Human Contribution；
- Output Provenance；
- Similarity / Infringement Risk；
- Intended Use / Jurisdiction。

IP Disposition Record 允许 `unknown`、`pending` 与 `not_assessed`，避免让 Agent 生成伪法律确定性。

### 5. Supply Chain 从 Package 列表改为行为组件清单

组件集合扩展到：

- Script / Launcher；
- Plugin / Skill；
- MCP / Tool Server；
- Model / Adapter；
- Dataset / Evaluation Set；
- Embedding / Vector / Retrieval；
- Prompt Template / Policy Pack；
- CI Image / Build Tool；
- External API / Hosted Service；
- Generated Artifact。

工作稿同时强调，SLSA Provenance、SBOM、Signature、Vulnerability Scan 与 Use-case Evaluation 支持不同 Claim。

### 6. Local / Private / Cloud 从安全等级改为 Trust Boundary

工作稿给出项目内工作定义，并明确：

> Locality changes the trust boundary; it does not eliminate it.

Routing 需要同时考虑 Data Permission、Provider Contract、Capability、Tool / Network、Cost、Latency、Availability、Change Policy、Incident Response、Law / Policy 与维护能力。

新增 `model_context_denied`，用于表达即使本地部署也不应进入 Model Context 的材料。

## D-048 案例处置

D-048 被放在 Tool Integrity 与 Supply Chain 两个窄位置：

- Trusted Launcher 产生了未声明 Bytecode Side Effect；
- Side Effect 改变了 Authority-bearing Manifest Surface；
- Exact-inventory Check 在目标执行前 Fail Closed；
- Target 保持 `non-result`；
- 后续方向是前向修正 Observer / Launcher，而不是重写历史 Evidence。

明确不做以下扩张：

- 不称其为 Prompt Injection；
- 不称其为恶意供应链攻击；
- 不推导所有 Tool 必须无副作用；
- 不以一个 Python 事件证明完整安全架构。

## 新增五个工作对象

1. Data Handling Profile；
2. Model Processing Contract；
3. Tool Security Contract；
4. Supply Chain Component Record；
5. IP Disposition Record。

它们是候选语义对象，不要求实现为五套独立平台或文件。

对象的完备性、最小性和字段命名尚未通过跨项目验证。

## 与前后章的边界

- 第5章拥有 Context Selection、Packaging、Access 与 Data / Instruction 边界；第19章拥有处理、传输、保留与 Security / Privacy 约束。
- 第6、9章拥有 Claim、Evidence、Coverage 与 Decision Disposition；第19章提供具体 Security / Privacy / IP Claim 类型。
- 第13章拥有 Capability、Permission、Authority、Autonomy 与 Protected Control Floor；第19章落实到 Tool、Credential 与 Action Sink。
- 第14章拥有 Observer、Detector、Signal 与 Intervention；第19章提供 Secret、Access、Provider 与 Component Security Signal。
- 第15章拥有 Memory 生命周期；第19章拥有 Memory 的 Source Rights、Privacy、Confidentiality 与跨项目边界。
- 第18章拥有 Trace 与 Accountability；第19章约束安全记录的 Access、Retention 与 Incident / IP Authority。
- 第20章拥有 Drift、运行成本、Permission 使用和 Re-evaluation；第19章定义需要持续观察的边界。

## 当前保留的不确定性

- 三条新 Claim 都尚未获得作者 Human Disposition；
- Data / Model / Tool / Component / IP 五个对象是否过重，需在真实 Work 上试跑；
- 没有跨行业数据证明该结构减少事故、成本或法律风险；
- NIST / OWASP / SLSA 是框架和指南，不是全部法定义务；
- U.S. Copyright Office 结论必须保持美国法域和 2025 时间边界；
- Privacy、IP、Provider Terms 与安全标准会变化，成稿前需要再次核对。

## 建议的下一步

先不要扩写第19章理论。

优先进入第20章，建立 Model / Tool Drift、AgentOps、Cost 与 Re-evaluation 的运行接口。完成第20章后，再回看第19章五个对象中哪些字段真的会被运行监控消费，删除没有下游用途的字段。

## 2026-08-25 Narrative Cleanup Addendum

本次调整没有新增运行 Evidence，也没有改变 `CLM-C19-001`、
`CLM-C19-002`、`CLM-C19-003` 的 Receipt、Coverage、Human Status 或
Claim Ledger 历史。

改变的是 Evidence Routing 与读者层表达的分工：三条 Claim 的详细状态、
来源绑定、反向证据和人工裁决继续由 Receipt 与 Claim Ledger 承担；正文保留
与论证直接相关的来源、法域、案例和适用边界，不再重复内部审计状态。

Reader-facing Chapter 已据此：

1. 将 Header 收束为工作稿、回接说明与适用边界三项；
2. 删除“三条核心 Claim 的当前证据状态”整节；
3. 保留各主题段落中的具体来源、反例、法域限制与 D-048 窄边界；
4. 明确外部框架不能证明本章五对象模型普遍最优，本章也不构成法律意见；
5. 将原 `19.35`—`19.38` 顺延为 `19.34`—`19.37`。

因此，`partial / unreviewed / narrow` 继续限制效果、充分性、完备性与跨法域
推广等 Claim，但不阻止候选工程分解进入正文。结论变化来自 Workflow 的
适用范围和呈现层调整，不来自对既有证据的重新解释。

## 2026-08-25 Human Review Gate 来源复核

本轮为第19章 Human Review Gate 重新核对既有三份 Receipt 与正文边界，
没有把框架指南、标准或单一法域报告升级为普遍事实。

复核范围：

- [OWASP LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)、
  [LLM06:2025](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) 与
  [LLM07:2025](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/)；
- [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1)；
- [SLSA v1.2 Provenance](https://slsa.dev/spec/v1.2/provenance)；
- [U.S. Copyright Office Part 2](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)。

复核结论：

1. `CLM-C19-001` 仍只支持把不可信内容、模型输出与有副作用 Tool 之间的
   授权边界放在模型外；它不支持通用充分控制集、Prompt Injection 完全消除
   或部署拓扑的绝对安全排序。
2. `CLM-C19-002` 仍支持把 Provenance、第三方清单、Supplier Assessment、
   Monitoring、Incident Response 与 Fallback 分开；它不支持组件分类已经
   完备、统一 Schema 必然适用或治理必然降低事故率。
3. `CLM-C19-003` 仍支持把美国著作权资格、Human Contribution、合同权利、
   第三方 IP、Provenance 与侵权处置分开；它不支持具体作品结论、全球统一
   规则或 Scanner PASS 等于不侵权。

正文没有发现超出上述边界的结构性扩张。发现的一处局部措辞是英文原则
`Provenance establishes origin claims` 比同段中文和 Receipt 更强，现已收窄为
`Provenance supports origin claims; it does not establish fitness claims.`

本次复核没有改变三条 Claim 的 `partial / unreviewed / narrow`，也没有形成
作者裁决。建议 Human Gate 只接受第19章作为候选工程分解及其现有限制，
不同时接受对象完备性、效果主张或跨法域法律结论；三条正式 Claim 是否接受，
仍需另行明确。

## Human Disposition

- Status: `accepted`
- Decision by: Human Author
- Decision at: 2026-08-26
- Accepted scope: 第19章作为按风险裁剪的候选工程分解，以及正文中保留的安全、供应链、Privacy、IP、法域与案例限制。
- Excluded scope: 五个对象已经完备或最优；该模型已经证明安全、成本或法律效果；美国著作权报告可以推广为跨法域结论。
- Claim boundary: `CLM-C19-001`、`CLM-C19-002`、`CLM-C19-003` 仍为 `partial / unreviewed / narrow`，本次章节级接受不构成三条正式 Claim 的 Human Disposition。
- Verbatim decision: “第19章边界呈现：`accepted`。仅接受其作为按风险裁剪的候选工程分解及现有限制；不接受五个对象已经完备或最优，不接受其已证明安全、成本或法律效果，也不将美国法域结论推广到其他法域。`CLM-C19-001/002/003` 暂时维持 `partial / unreviewed / narrow`。”
- Rationale: 作者先在收到上述精确范围后回复“接受”，随后用完整裁决文本再次确认；后一条记录消除了接受对象与排除范围的歧义。
