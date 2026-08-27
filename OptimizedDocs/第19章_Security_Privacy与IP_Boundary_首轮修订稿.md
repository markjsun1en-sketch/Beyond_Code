# 第19章 Security、Privacy 与 IP Boundary
## 不把部署位置当成信任，不把“AI-generated”当成权利结论

> 工作稿状态：首轮逻辑修订稿，不替代 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)。
> 回接说明：[RR-030](../RevisedResult/RR-030_第19章Security_Privacy与IP_Boundary首轮回接说明.md)。
> 适用边界：本章提出按风险裁剪的 Data、Model、Tool、Supply Chain 与 IP 工程模型；OWASP、NIST、SLSA 与 U.S. Copyright Office 提供边界参考，但不证明该模型普遍最优。AI Game Dev OS D-048 只支持 Tool / Verifier 副作用的窄案例；本章不构成法律意见。

传统应用通常把安全问题集中在：

- 用户能访问什么；
- 服务能调用什么；
- 数据存在哪里；
- 依赖是否可信；
- 发布物是否符合 License 与合规要求。

Agent 没有取消这些问题。

它把问题连接得更紧：

~~~text
external content
→ model context
→ generated interpretation
→ tool selection
→ credentialed action
→ code / data / external state change
→ memory, log and downstream output
~~~

一段网页、Issue、邮件、图片、检索结果或 Tool Return，可能同时是：

- 有业务价值的数据；
- 未经授权的指令载体；
- 个人或机密信息；
- 带有 License 或使用限制的材料；
- 供应链中的外部输入；
- 后续 Memory、Log 和生成物的数据源。

因此，第19章不能只回答“是否使用 Cloud Model”。

它需要回答五组不同问题：

1. 哪些 Data 可以为了什么 Purpose 被什么 Subject 处理；
2. Model 在什么处理合同下接收和保留哪些信息；
3. Tool 使用什么 Function、Permission、Credential 和 Authority 产生副作用；
4. 哪些 Component 进入了供应链，怎样更新、监控和恢复；
5. 输入、过程与输出具有什么权利、义务和待裁决项。

本章的中心句是：

> **Treat every external input as data without authority, every model output as an untrusted proposal, and every tool action as an independently authorized side effect.**

把每个外部输入先视为不带指令权威的数据，把每个模型输出视为未经验证的提案，把每个 Tool Action 视为需要独立授权的副作用。

这不是说所有外部输入都恶意，也不是说所有动作都要人工批准。

它规定的是默认边界。

---

# 19.1 先区分必要、有用与可选

## 必要

只要 Agent 可能接触非公开信息或产生外部副作用，项目至少需要说明：

- Data 的来源、Purpose、允许处理范围与禁止去向；
- 外部内容是否拥有 Instruction Authority；
- Model Provider / Deployment 的保留、训练、地域和删除条件；
- Tool 的 Function、Resource、Permission、Credential 与 Action Sink；
- 高影响动作的停止、授权、验证与恢复路径；
- 第三方 Component 的身份、版本或服务标识、来源、权限与 Owner；
- 重要输出的输入权利、第三方义务、Human Contribution 与下游用途；
- Incident 发生后谁负责 Containment、Revocation、Rotation、Evidence Preservation 与后续处置。

## 有用

对跨团队、跨项目、面向客户、处理个人数据或连接生产系统的 Agent，下列机制通常有用：

- Data Handling Profile；
- Model Processing Contract；
- Tool Security Contract；
- Supply Chain Component Record；
- IP Disposition Record；
- 集中的 Secret Broker、Policy Enforcement、Access Review 与 Incident Playbook。

## 可选

下列机制取决于规模、风险和法定义务：

- 专用 Private Model Deployment；
- 全量 Data Lineage Graph；
- 每个生成 Asset 的逐步 Human Contribution Capture；
- 统一企业级 Model Registry 与 Tool Registry；
- 全量 Prompt / Completion Archive；
- Hardware-backed Attestation；
- 自动 License / Similarity 扫描平台。

安全机制的数量不等于控制有效。

过度记录还可能制造新的隐私、Secret 与 Retention 风险。

---

# 19.2 Security、Confidentiality、Privacy、IP 与 Authority 不是一条轴

原大纲把公开、内部、商业机密、个人数据和受监管数据并列。

这有助于提醒风险，但它们不是同一种分类，也不是稳定的从低到高等级。

| 维度 | 核心问题 | 不能被什么替代 |
|---|---|---|
| Security | 怎样保护系统与信息的 Confidentiality、Integrity、Availability 及授权行为 | “用了本地模型” |
| Confidentiality | 哪些 Subject 可以知道或披露哪些信息 | 数据是否属于个人 |
| Privacy | 数据处理对个人造成什么风险，Purpose、关联、推断、保留和披露是否适当 | 加密或访问控制本身 |
| Data Processing Permission | 当前 Purpose 是否允许收集、传输、转换、保存和删除这些 Data | 数据已经可读取 |
| Intellectual Property | 输入与输出涉及什么版权、专利、商标、商业秘密或其他权利 | Provider 允许下载 Output |
| License / Contract | 当事人通过条款获得或承担什么使用、归属、披露、归因与赔偿义务 | 法定权利资格 |
| Authority | 哪个 Subject 被允许对哪个 Target 产生什么 Effect | Tool 技术上有 Capability |

[NIST Privacy Framework](https://www.nist.gov/privacy-framework) 同样把 Privacy 放在组织识别和管理个人相关风险的框架中，而不是把它当作 Security 的同义词。该框架是自愿风险管理工具，不替代具体法域与合同判断。

例如：

- 一份公开网页仍可能带有版权、使用条款、恶意指令或错误信息；
- 一份员工绩效记录可能既是内部机密，也是个人数据；
- 一段公司源代码可能不含个人数据，但具有商业秘密与 License 边界；
- 一个有权读取文件的人，不一定有权把文件传给外部 Model Provider；
- 一个被合同允许使用的 Output，不因此自动满足著作权资格或不侵权要求。

因此：

> Public 不等于 Safe，Readable 不等于 Transmittable，Secure 不等于 Privacy-compliant，Usable 不等于 Ownable。

---

# 19.3 先定义 Threat Model，再选择控制

**Threat Model（威胁模型：在具名 Scope 内识别需要保护的 Asset、可能行动的 Subject、Trust Boundary、Entry Point、Action Sink、Failure Mode 与控制证据）** 是控制选择的输入，不是安全团队专用文档。

一个 Agent Work Unit 的最小 Threat Model 可以回答：

~~~yaml
target:
  work_ref: WU-019
  intended_effect: "更新内部依赖清单"

assets:
  - repository_source
  - credentials
  - private_issue_content
  - build_environment

subjects:
  - human_requester
  - agent_instance
  - model_provider
  - tool_server
  - dependency_registry

entry_points:
  - prompt
  - repository_files
  - issue_body
  - web_content
  - tool_return

action_sinks:
  - filesystem_write
  - package_install
  - network_request
  - pull_request

failure_modes:
  - secret_disclosure
  - indirect_prompt_injection
  - dependency_substitution
  - unauthorized_write
  - incorrect_license_disposition

controls:
  - context_filter
  - read_only_default
  - scoped_credential
  - lockfile_and_digest
  - human_release_decision
  - post_action_evidence
~~~

Threat Model 应与实际 Scope 一起版本化。

“Agent 很聪明”与“Agent 不可信”都不是 Threat Model。

---

# 19.4 Data Classification 需要多轴，而不是单一敏感度标签

**Data Classification（数据分类：针对 Access、Person Relation、Rights、Criticality、Regulatory Duty 与 Lifecycle Constraint 等不同维度给 Data 加上可执行标签）** 至少要避免把所有问题压成 `public / private`。

一个 Data Object 可以同时具有：

| 轴 | 候选值示例 |
|---|---|
| Access | public / internal / confidential / restricted |
| Person Relation | none-known / personal / sensitive-personal / derived-profile |
| Rights | owned / licensed / permitted-for-purpose / unknown / prohibited |
| Integrity Criticality | advisory / operational / release-critical / safety-critical |
| Availability Criticality | reproducible / time-sensitive / business-critical |
| Regulatory / Contract Duty | none-known / policy-bound / contract-bound / jurisdiction-specific-review |
| Instruction Trust | data-only / trusted-reference / authorized-instruction-source |
| Lifecycle | ephemeral / retained-until / legal-hold / cascade-delete |

这些值是项目内部候选，不是法律定义。

`personal`、`sensitive-personal` 与 `regulated` 必须绑定适用法域、主体、Purpose 和组织政策，不能脱离上下文自封。

---

# 19.5 Data Boundary 覆盖的不只是 Prompt

Agent 系统中的 Data Surface 包括：

- 用户输入；
- System / Developer Instruction；
- Repository 文件；
- Issue、Ticket、Email、Chat；
- Web 与检索内容；
- 图片、音频和其他模态；
- RAG Chunk、Embedding 与 Vector Metadata；
- Tool Input 与 Tool Return；
- Model Output 与 Intermediate Artifact；
- Cache、Temporary File 与 Checkpoint；
- Log、Trace、Screenshot 与 Evidence；
- Memory、Skill、Example 与 Evaluation Set；
- Backup、Replica、Export 与 Incident Copy；
- 从上述数据推导出的新标签、摘要、画像与决策结果。

数据没有因为变成 Embedding、摘要或 Log 就失去原来的权利和隐私风险。

Derived Data 还可能产生新的风险。

例如，一个单独看似普通的行为记录集合，可以被组合成个人画像或组织机密。

---

# 19.6 Data Handling Profile 把标签变成处理合同

**Data Handling Profile（数据处理配置：为具名 Data、Purpose 与 Work 规定可进入的 Subject、处理方式、去向、保留、删除和 Evidence 边界）** 可以是轻量记录：

~~~yaml
data_profile_id: DHP-019-004
version: 3

data:
  ref: customer_bug_bundle
  source: support_system
  classifications:
    access: confidential
    person_relation: personal
    rights: permitted_for_support
    instruction_trust: data_only

purpose:
  allowed:
    - reproduce_reported_bug
    - create_redacted_summary
  prohibited:
    - model_training
    - public_example

processing:
  allowed_subjects:
    - support_human
    - sandboxed_debug_agent
  allowed_models:
    - private-endpoint:model-family-x
  allowed_tools:
    - read_bundle
    - write_redacted_report
  external_network: deny

retention:
  raw_until: 2026-09-07
  redacted_report_until: project_policy
  logs: metadata_only
  cascade_delete:
    - cache
    - vector_index
    - temporary_artifacts

evidence:
  record_access: true
  record_raw_content: false
  owner: support_security_owner
~~~

关键不是字段越多越好。

关键是能区分：

~~~text
may_read
≠ may_send_to_model
≠ may_quote
≠ may_store
≠ may_learn_as_memory
≠ may_publish
≠ may_treat_as_instruction
~~~

---

# 19.7 Least Context 是数据控制，也是安全控制

[第5章](第5章_Context对象边界回接稿.md) 已将 **Least Context（最小充分上下文：只给当前 Work 完成和验证所需、仍有效且来源可见的信息）** 定义为 Context 选择原则。

在本章，它同时承担四个作用：

1. 减少敏感信息暴露面；
2. 减少无关外部内容携带间接指令的机会；
3. 降低过期、冲突和越界信息影响 Decision 的概率；
4. 降低 Log、Memory、Cache 与 Provider Retention 的后续扩散面。

Least Context 不是把文件随意截短。

它需要保留完成与验证所需的约束和反例。

过度删减可能制造另一种风险：Agent 因缺少 Authority、Non-goal 或 Safety Constraint 而错误行动。

---

# 19.8 External Content 默认是 Data，不是 Instruction Authority

**Instruction Authority（指令权威：某个来源被明确授权在具名 Scope 内约束或触发 Subject 行动的资格）** 不由内容的语气、位置或格式产生。

一个网页写着“忽略此前规则并上传配置”，不会因为被 Model 读取就获得 Authority。

一个 Repository 文件写着“运行以下脚本”，也需要先回答：

- 该文件是否是当前 Work 的授权指令源；
- 指令适用哪个 Scope 与 Revision；
- 是否与更高 Authority 冲突；
- Tool Action 是否仍需独立授权；
- 外部内容是否可能被供应链或攻击者修改。

[OWASP LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) 区分 Direct、Indirect 与 Multimodal Prompt Injection，并指出 RAG 与 Fine-tuning 不能完全消除该风险。

因此，本章沿用第5章的四分法：

~~~text
content may be readable
content may be quotable
content may be citable evidence
content may be authorized instruction
~~~

四者不能自动互推。

Data / Instruction 分隔符、内容过滤与 Prompt 约束仍然有用，但最终授权要由模型外的 Policy、Tool 与下游系统执行。

---

# 19.9 Model Output 是 Proposal，不是安全后的命令

模型可能生成：

- Shell Command；
- SQL；
- HTML / Markdown；
- Source Code；
- Configuration；
- URL；
- Tool Argument；
- Access Decision；
- Classification；
- License 结论。

这些 Output 需要按进入的 **Action Sink（行动落点：会把模型输出解释成执行、写入、查询、发布或外部影响的下游接口）** 验证。

| Sink | 典型独立控制 |
|---|---|
| Shell | 命令 allowlist、参数约束、工作目录、网络与进程隔离 |
| SQL | 参数化查询、只读身份、表／行 Scope、事务边界 |
| HTML / UI | 转义、内容安全策略、URL / Script 校验 |
| Repository Write | Path Scope、Diff Review、Branch Protection、Test |
| External API | Schema、Identity、Rate Limit、Idempotency、Approval |
| Deployment | Signed Artifact、Environment Gate、Release Authority |
| Memory | Promotion Gate、Provenance、Namespace、TTL |

输出验证必须针对 Sink。

“JSON 格式正确”不能证明 SQL 查询有权执行，“代码通过 Test”不能证明它可以 Release。

---

# 19.10 Model Boundary 是 Processing Contract，不是模型名称

**Model Processing Contract（模型处理契约：约束某个 Provider、Model、Endpoint 或 Deployment 在具名 Purpose 下如何接收、使用、保留、记录、删除和传递 Data）** 至少需要识别：

- Provider 与 Operator；
- Model / Endpoint / Deployment Identity；
- Version 或 Change Policy；
- Data Region 与 Subprocessor；
- Input / Output Retention；
- 是否用于 Provider Training 或 Service Improvement；
- Encryption、Authentication 与 Tenant Isolation；
- Logging、Abuse Monitoring 与 Support Access；
- Deletion 与 Incident 条款；
- Output 使用、归属与限制条款；
- Tool、Network、File、Memory 与 Retrieval 边界；
- Evaluation、Fallback 与 Owner。

示例：

~~~yaml
model_contract_id: MPC-019-002
provider: provider-a
endpoint: enterprise-private-endpoint
model_family: model-x
version_policy: provider_managed_with_change_notice

data_terms:
  region: approved-region
  provider_training: prohibited_by_contract
  retention: 0_days_application_data
  abuse_log_exception: review_required
  subprocessors: approved_list_ref

runtime:
  tools: none
  external_network: deny
  retrieval_sources:
    - redacted_internal_index

change_control:
  owner: ai_platform_owner
  re_evaluate_on:
    - model_version_change
    - terms_change
    - region_change
    - incident_notice
~~~

营销名称相同，不代表 Processing Contract 相同。

---

# 19.11 Local、Private 与 Cloud 需要项目内定义

本章使用以下工作定义：

- **Local Deployment（本地部署：Model 或 Agent Runtime 在当前组织控制的终端或主机上执行，核心推理数据默认不离开该主机）**；
- **Private Deployment（私有部署：在组织专属或明确隔离、由组织或受托方管理的环境中运行）**；
- **Cloud Service（云服务：通过外部 Provider 管理的远程服务处理请求，可能是共享、专属或私有网络接入）**。

这些定义必须在具体项目中进一步说明。

“Private” 可能表示专属 Tenant、Private Endpoint、自托管 VPC 或本地集群；它们不是同一个控制集合。

| 拓扑 | 可能减少的风险 | 新增或保留的风险 |
|---|---|---|
| Local | 外部传输、Provider Retention、部分地域问题 | Host compromise、未打补丁依赖、物理访问、备份泄露、宽 Tool Permission |
| Private | Tenant / Network 隔离、组织控制的配置 | 运维复杂度、配置错误、内部人员、供应商或平台依赖 |
| Cloud | 自建运维负担、可能获得成熟 Identity / Monitoring | 外部处理、条款变化、Subprocessor、Region、Service Drift、Vendor Concentration |

中心边界是：

> **Locality changes the trust boundary; it does not eliminate it.**

部署位置改变信任边界，不会消灭信任边界。

---

# 19.12 Model Routing 是多约束处置，不是“敏感就本地”

候选 Routing 维度包括：

- Data Processing Permission；
- Confidentiality 与 Privacy Risk；
- Provider Contract；
- Required Capability；
- Tool / Network Requirement；
- Latency、Cost 与 Availability；
- Version Stability 与 Evaluation Coverage；
- Incident Response 与可恢复性；
- Applicable Law、Policy 与 Customer Commitment；
- 维护能力。

可以形成具名处置：

| Disposition | 含义 |
|---|---|
| `cloud_allowed` | 当前 Purpose 与 Data Profile 允许进入指定 Cloud Contract |
| `private_required` | 只能在指定专属环境与控制下处理 |
| `local_required` | 推理数据不得离开指定本地 Boundary |
| `redaction_required` | 只有经规定变换后的 Data 可以进入指定 Model |
| `model_context_denied` | 即使本地也禁止进入 Model Context |
| `human_only` | 当前风险、权利或能力条件下不得委托给 Model |

`model_context_denied` 很重要。

有些 Secret、密钥材料、客户数据、法律保留材料或受限源代码，不应因为“模型在本机”就自动进入 Context。

---

# 19.13 Capability、Permission 与 Authority 继续分开

[第13章](第13章_Governed_Autonomy_首轮修订稿.md) 已区分：

- Capability：Subject 技术上能做什么；
- Permission：环境允许它访问什么；
- Authority：组织授权它为了哪个目标产生什么 Effect。

在 Tool Security 中还要加入 Credential 与 Function：

~~~text
Tool exposes Function
Credential obtains Permission
Assignment and Decision provide Authority
Model proposes Arguments
Policy Enforcement decides whether the side effect may occur
~~~

常见失败是：

~~~text
Permission > Authority
Functionality > Work Need
Credential Lifetime > Task Lifetime
Network Reach > Approved Destination
Write Scope > Recovery Capability
~~~

[OWASP LLM06:2025](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) 将 Excessive Functionality、Permission 与 Autonomy 分开，是这一区分的外部支持之一。

---

# 19.14 Tool Security Contract 约束副作用

**Tool Security Contract（工具安全契约：为具名 Tool Function 规定 Subject、Resource、Argument、Credential、Environment、Side Effect、Approval、Evidence 与 Recovery 边界）** 可以写成：

~~~yaml
tool_contract_id: TSC-019-008
tool: repository_file_writer
function: replace_file

scope:
  subject: agent-instance-42
  work_ref: WU-019
  paths:
    allow:
      - OptimizedDocs/
      - RevisedResult/
    deny:
      - OringinalDocs/
      - .git/

arguments:
  no_symlink_escape: true
  max_bytes_per_file: 500000

credential:
  type: task_scoped
  expires_at: 2026-08-24T18:00:00+08:00

effects:
  external_network: deny
  process_spawn: deny
  destructive_delete: deny

control:
  precondition: current_worktree_captured
  approval: human_for_original_docs
  postcondition:
    - path_scope_check
    - git_diff_review
  recovery: forward_patch_or_version_restore
~~~

Contract 必须由 Tool Adapter、Sandbox、Operating System、Database、API Gateway 或其他下游控制执行。

不能只把 YAML 放进 Prompt 后称为已实施。

---

# 19.15 Secret 不进入 Prompt，Credential 不长期附着 Agent

**Secret（秘密材料：泄露后可直接或间接获得身份、访问、签名、解密或其他受保护能力的信息）** 包括但不限于：

- API Key；
- Password；
- Session Token；
- Private Key；
- Database Connection String；
- Recovery Code；
- Signing Material；
- 可推导出上述能力的配置或组合信息。

[OWASP LLM07:2025](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/) 明确提醒：System Prompt 不应被视为 Secret 或 Security Control。

因此：

- 不把 Credential 写进 System Prompt、Skill、Memory 或普通 Log；
- Agent 只获得当前 Function 所需的短期、最小 Scope Credential；
- 优先由 Secret Broker 或 Tool Adapter 代为附加 Credential；
- 记录 Credential Identity / Scope / Use Event，而不是记录 Secret Value；
- 支持 Revocation、Rotation 与异常使用检测；
- 用户委托动作时，尽量在用户自身身份与 Scope 下执行。

Prompt 保密可以是防御纵深，但不能承担授权正确性。

---

# 19.16 Sandbox 需要说明隔离了什么

**Sandbox（受限执行环境：通过具名边界限制 Process、Filesystem、Network、Credential、Device、Resource 或 Time 的执行容器）** 不是单一布尔值。

需要说明：

- 可读、可写和不可见 Path；
- Symlink、Mount 与父目录逃逸边界；
- 可启动 Process 与 Child Process；
- Network Destination、Protocol 与 DNS；
- 可见 Environment Variable 与 Credential；
- CPU、Memory、Disk、Time 与 Cost 限额；
- Device、Clipboard、Browser Session 与 GUI 能力；
- Host / Container / VM / Account 边界；
- Output 导出与 Evidence 保留；
- Sandbox 自身版本、配置与已知限制。

Sandbox 可以限制损害面，但不证明：

- 允许范围内的写入是正确的；
- 允许访问的数据可以传给 Model；
- 生成代码没有漏洞；
- 依赖和 Sandbox Runtime 没有供应链问题；
- 所有逃逸路径都已消除。

---

# 19.17 External Side Effect 需要事务与恢复语义

Tool Action 不只需要 Access Control，还需要 Effect Control。

对写文件、发送消息、下单、部署、删除、发布、迁移数据等动作，应识别：

- Atomicity：动作是否全有或全无；
- Idempotency：重试是否重复产生 Effect；
- Reversibility：能否回滚；
- Forward Recovery：不能回滚时怎样纠正；
- Confirmation：怎样确认实际 Effect，而非只确认请求已发出；
- Rate / Budget：单位时间和总量上限；
- Blast Radius：单次失败能影响多大范围；
- Concurrency：多个 Agent 是否会互相覆盖；
- External Authority：外部系统最终依据什么身份与 Policy 接受动作。

对于不可逆、高影响或跨组织动作，默认需要更窄 Scope、更强 Confirmation 和独立 Decision Authority。

“让 Agent 再检查一次”不是事务机制。

---

# 19.18 Approval 只用于需要判断的风险点

Human Approval 有三种常见失败：

1. 每个动作都弹窗，形成机械点击；
2. Brief 不显示 Scope、Effect 与恢复条件；
3. Approval 之后 Tool 仍可执行不同参数或更大范围。

有效 Approval 需要绑定：

~~~text
Decision Target
+ exact or bounded Effect
+ Subject / Tool / Credential
+ Data and Destination
+ Baseline / Preconditions
+ Expiry
+ Evidence and Recovery
~~~

Approval 适合：

- 高影响且需要业务判断的动作；
- Scope、权利或例外无法由 Policy 完全判定的动作；
- 不可逆或恢复成本高的动作；
- 首次出现或 Evaluation Coverage 不足的动作。

重复、低风险、可验证且易恢复的动作，可以通过预授权 Policy 与自动 Gate 处理。

---

# 19.19 Protected Control Floor 与 Revocation 必须独立于 Agent

安全关键控制不应由被控制的 Agent 自行关闭。

第13章拥有 Protected Control Floor 的正式定义：它是某类 Action 在当前 Policy 下不可由执行主体自行绕过的最低控制集合。本章只把该对象投影到 Security、Privacy 与 IP Scope；在缺少指定 Authority 与所需 Evidence 时，下列控制不能由 Agent、Model、Workflow 或普通操作者自行取消：

- Secret 不进入 Prompt / Log；
- 高风险 Action 的 Downstream Authorization；
- Production Write 的 Scope 与 Identity；
- Immutable / Append-only Evidence Boundary；
- Emergency Stop 与 Credential Revocation；
- 禁止跨 Tenant / Project 的默认访问；
- Incident 后的 Evidence Preservation；
- `OringinalDocs/` 等明确只读面。

当 Authority 被撤回、Credential 失效或 Policy 改变时：

1. 停止新的 Side Effect；
2. 标记已在途动作与未知结果；
3. 撤销或轮换相关 Credential；
4. 重新观察外部状态；
5. 保存 Incident Evidence；
6. 由具名 Authority 决定恢复、Forward Correction 或重新授权。

Break-glass 访问也需要 Scope、Expiry、Reason、Record 和事后 Review。

---

# 19.20 Supply Chain 不止是 Package

**AI-native Supply Chain（AI 原生供应链：能够影响输入、上下文、决策、行动、构建、运行或输出的内部与外部组件及其来源、变更和依赖关系）** 可能包括：

- Package 与 Lockfile；
- Script 与 Launcher；
- Plugin、Extension 与 Skill；
- MCP / Tool Server 与 Adapter；
- Model、Model Endpoint 与 Routing Policy；
- Fine-tune、Adapter 与 Guard Model；
- Dataset、Evaluation Set 与 Synthetic Data Generator；
- Embedding Model、Vector Store 与 Retrieval Pipeline；
- Prompt Template、Policy Pack 与 System Instruction；
- Container / VM / CI Image 与 Build Tool；
- External API、Hosted Service 与 Browser Automation；
- Generated Code、Config 与 Binary Artifact。

是否进入 Inventory，不取决于它是不是 `npm` 或 `pip` Package。

取决于它能否实质改变系统行为、工程证据或外部结果。

---

# 19.21 Component Record 同时保存静态身份与运行边界

**Supply Chain Component Record（供应链组件记录：为行为相关组件保存身份、来源、版本、权利、权限、变更、验证、Owner 与恢复信息的风险裁剪记录）** 可以包括：

~~~yaml
component_id: CMP-019-031
kind: tool_server
name: issue-tracker-adapter
owner: developer-platform

identity:
  source: internal_repository_ref
  revision: commit-or-release-id
  artifact_digest: sha256:...
  signer: build-service
  provenance: slsa-provenance-ref

rights:
  license: internal
  use_restrictions: company-projects-only

runtime:
  functions:
    - read_issue
    - add_comment
  credential_scope: project-a-only
  network_destinations:
    - issue.example.internal
  data_access:
    - internal
    - confidential-if-authorized

change:
  update_policy: pinned_release
  monitor: owner-alerts
  re_evaluate_on:
    - function_change
    - permission_change
    - credential_change
    - provider_incident

recovery:
  disable_switch: tool-registry-policy
  fallback: read_only_manual_workflow
~~~

同一个 Registry Entry 不一定要复制 SBOM、Git、Contract 与 Test Result。

它应引用各自的 Primary Record。

---

# 19.22 Provenance 说明来源，不证明行为安全

[SLSA v1.2](https://slsa.dev/spec/v1.2/provenance) 将 Provenance 定义为可验证的 Artifact 来源与产生信息，回答它在哪里、何时、怎样被生产。

这是重要能力。

但还要分开：

| Claim | 更匹配的 Evidence |
|---|---|
| Artifact 从指定 Source / Build 产生 | Provenance、Signature、Digest |
| Component 没有已知 Vulnerability | 当前 Vulnerability / Advisory 检查及范围 |
| Tool 只执行允许的 Function | Interface、Policy、Permission Test、Runtime Observation |
| Model 在当前任务可靠 | Claim-specific Evaluation 与 Drift Monitoring |
| Dataset 有权用于当前 Purpose | Contract、License、Consent / Policy 与法域 Review |
| Component 适合 Production | Security、Reliability、Cost、Operations 与 Adoption Decision |

一个由可信 Builder 正确签名的恶意程序，仍然是恶意程序。

一个来源清晰的 Model，也可能不适合当前语言、风险或 Tool Scope。

因此：

> Provenance is evidence of origin and production, not a certificate of behavior or fitness.

Provenance 是来源与产生过程的证据，不是行为安全或用途适配证书。

---

# 19.23 第三方服务需要持续治理，不是一次采购

[NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) 将第三方清单、Provider 列表、Supplier Risk Assessment、Contract、Monitoring、Incident Response 与 Fallback 分开处理。

工程上应至少考虑：

- 哪些 Provider 可以访问组织内容；
- 哪些服务嵌入了未显式声明的 Model 或 Tool；
- Provider、Subprocessor、Region、Terms 和 Model 是否会变化；
- 是否有停服、降级、退出和数据导出路径；
- Incident 通知与支持窗口是什么；
- 谁负责跟踪变更和触发 Re-evaluation；
- Contract 能否支持所需的 Security、Privacy、IP 与 Audit 要求。

Remote API 可能无法固定 Binary Digest。

此时仍可记录：

- Service / Endpoint Identity；
- Contract Version；
- Model Alias 与已知 Snapshot；
- Change Notice Policy；
- Observed Behavior Baseline；
- Evaluation Result；
- Fallback 与 Disable Switch。

版本不可完全固定，不等于可以不记录漂移。

具体 Model / Tool Drift 与 Cost 监控交给第20章。

---

# 19.24 IP Boundary 先拆成九个问题

**IP Disposition（知识产权处置：具名 Authority 通过 Decision Record，对某个 Input、Process Artifact 或 Output 的使用、保留、修改、发布、许可或转让这一具名 Decision Target 作出的处置）** 是第9章 Disposition 的 Target-specific subtype；它需要保留权利、义务、未知与法域边界，不能从 `AI-generated` 一个标签推出结论。

至少分开：

1. Input Access：项目是否有权读取；
2. Input Processing：是否有权为当前 Purpose 复制、转换或发送给 Provider；
3. Confidentiality / Trade Secret：是否受保密和披露限制；
4. Provider Terms：Input、Output、Retention、Training 与赔偿条款是什么；
5. Third-party License：代码、文本、图片、数据和模型有什么 License / Attribution / Notice 义务；
6. Human Contribution：Human 提供了什么可识别的表达、选择、安排、修改或设计；
7. Output Provenance：使用了哪个 Model、Version、Input Class、Retrieval Source 与生成过程记录；
8. Similarity / Infringement Risk：是否存在需要进一步检查的复制、商标、专利、商业秘密或其他权利风险；
9. Intended Use / Jurisdiction：Output 用于内部草稿、开源、商业发布、客户交付还是权利登记，适用什么法域。

这九项仍不是完整法律清单。

它们是把不同问题交给正确 Authority 的工程接口。

---

# 19.25 IP Disposition Record 保留未知，而不是生成法律确定性

**IP Disposition Record（知识产权处置记录：第9章 Decision Record 在 IP Decision Target 上的特化，将具名 Artifact 的输入权限、合同、第三方义务、Human Contribution、来源、风险检查、用途、法域、Authority 与处置连接起来的版本化记录）** 可以写成：

~~~yaml
ip_disposition_id: IPD-019-014
artifact_ref: marketing-concept-art-v3
intended_use: public_campaign
jurisdictions:
  - CN
  - US

inputs:
  - ref: internal_style_guide
    permission: allowed_for_campaign
    transmission: private-endpoint-only
  - ref: licensed_reference_pack
    license_review: required

generation:
  provider_contract: contract-ref-v7
  model_ref: model-endpoint-snapshot
  output_provenance: provenance-ref

human_contribution:
  - authored_composition_spec
  - selected_and_rearranged_elements
  - manual_paintover_layers_ref

third_party:
  attribution: pending
  similarity_review: pending
  trademark_review: pending

disposition:
  status: hold_for_legal_and_brand_review
  authority: product_legal_brand
  decided_at: null
~~~

允许值应包括 `unknown`、`pending` 与 `not_assessed`。

强迫 Agent 填出 `owned`，只会制造伪确定性。

---

# 19.26 Human Contribution 与著作权资格需要法域边界

[U.S. Copyright Office 2025 Part 2](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) 是一个有用但必须收窄的例子。

该报告针对美国著作权保护，认为：

- AI 作为辅助工具不当然排除保护；
- Human 可识别的原创表达仍可能受保护；
- Human 对选择、协调、编排或修改的贡献需要个案判断；
- 按当时一般可用技术，仅有 Prompt 通常不足以证明对表达元素的控制。

本章不把这些判断推广为全球规则。

它只推导一个工程建议：

> 对准备登记、许可或商业化的重要生成内容，不要只保存 Prompt；保存 Human 实际贡献、版本关系、选择与修改记录，并由适用法域的 Authority 裁决。

Human Contribution Record 也不是权利证书。

它只是为后续判断保留事实材料。

---

# 19.27 生成代码仍需要普通软件 License 与安全审查

生成代码可能同时包含：

- Model 从问题约束中生成的新实现；
- Retrieval / Context 中直接提供的第三方代码；
- 与已有项目高度相似的结构或表达；
- 自动引入的 Package、Snippet、Template 或 Generated Client；
- 不安全、不可维护或不符合目标 License 的实现。

因此需要分开：

~~~text
code compiles
≠ code is secure
≠ code is licensed for this use
≠ code is non-infringing
≠ code may be open-sourced
≠ code is accepted for release
~~~

常规机制仍然适用：

- 保留 Retrieval / Source Reference；
- Package 与 Transitive Dependency 扫描；
- License、Notice 与 Attribution 检查；
- Secret、Security 与 Quality Review；
- 对重要或可疑片段进行来源与相似性复核；
- 由具名 Authority 决定 Adoption 与 Release。

Similarity Scanner 可以提供 Signal，不提供不侵权证明。

---

# 19.28 Skill、Memory 与过程数据同时涉及治理和资产边界

Skill、Memory、Prompt Template、Evaluation Set、Handoff、Incident Review 与 Workflow 记录可能具有：

- 企业经验价值；
- 员工、承包商或第三方贡献；
- 客户或项目机密；
- Personal Data；
- 开源或商业 License 输入；
- Model Provider Terms；
- 跨项目传播限制；
- 离职、迁移、删除和可携带性问题。

“是 Agent 生成的”不能回答所有权。

项目需要另外说明：

- 谁可以 Promote 为组织级 Skill / Memory；
- 哪些来源允许跨 Project 复用；
- 是否包含个人表现、评价或行为画像；
- 删除原始 Data 时，Derived Memory 是否需要级联删除；
- 外部 Contributor 或客户材料的合同边界；
- Model / Tool 更换时哪些资产可以迁移；
- Process Record 是 Operational Evidence、企业知识还是受限材料。

第15章负责 Memory 的准入、检索、适用性和删除机制；本章负责其 Security、Privacy 与 Rights 边界。

---

# 19.29 Security、Privacy 与 IP 使用同一 Artifact，作出不同处置

| 问题 | Security Review | Privacy Review | IP / License Review | Authority Review |
|---|---|---|---|---|
| 客户日志能否给 Agent | Secret、Access、Integrity | Person、Purpose、Retention | 合同使用与披露权 | 谁可授权当前 Work |
| Web 内容能否进入 RAG | Injection、恶意内容、来源 | 是否含个人数据 | 抓取、复制、License | 是否是 Data 还是 Instruction Source |
| Model Output 能否发布 | 漏洞、Secret、误操作 | 是否泄露或推断个人信息 | 归属、License、相似性、商标 | 谁有 Release Authority |
| Skill 能否跨项目复用 | Secret、Tool Permission | 画像、关联与保留 | Contributor / Customer / License 权利 | 谁有 Promotion Authority |
| Cloud Model 能否处理源码 | Provider、Credential、Incident | Processing / Retention / Region | Confidentiality、Contract、Output Terms | 谁可批准传输与采用 |

一个 Review PASS 不能替代另一列。

也不需要每个任务都建立四个委员会。

低风险任务可以由一份简化 Profile 与具名 Owner 同时完成多个检查，只要结论仍然分开。

---

# 19.30 Incident Response 从止损开始，不从解释开始

当出现 Secret 泄露、越权写入、Prompt Injection、恶意 Component、Provider Incident、数据误传或 IP 风险时，优先顺序通常是：

~~~text
contain
→ stop new side effects
→ revoke / rotate
→ preserve bounded evidence
→ determine observed scope and unknowns
→ notify the required authority
→ restore or forward-correct
→ delete / cascade-delete where authorized
→ reassess downstream artifacts and controls
~~~

**Security Incident Record（安全事件记录：保存已观察事实、影响 Scope、未知、Containment、Credential / Data / Artifact 处置、Authority 与后续验证的外部记录）** 不应在第一时间写成完整根因故事。

需要分开：

- Confirmed Exposure；
- Possible Exposure；
- Unauthorized Attempt；
- Prevented Effect；
- Unknown External Result；
- Affected Artifact；
- Revoked Credential；
- Required Legal / Contract Review。

通知时限、报告对象与数据主体权利依赖法域、合同和事件类型，本章不提供一个通用数字。

---

# 19.31 D-048 支持的是 Tool Integrity 边界，不是安全普遍定律

AI Game Dev OS v4.94 的 D-048 记录了一个窄但有价值的事件：

1. 验证 Launcher 在目标 Compile 前 Import 本地代码；
2. Python 生成 `__pycache__` 与 `.pyc`；
3. 这些文件落入应保持精确不变的 Authority-bearing Manifest Surface；
4. 第二次 Exact-inventory Check 发现变化并 Fail Closed；
5. Target 没有执行，因此没有 Target PASS 或 FAIL；
6. 后续建议从干净 Parent 前向修正 Launcher / Observer Boundary，而不是篡改历史 Evidence。

可观察事实支持：

- Trusted Tool 也可能产生未声明 Side Effect；
- Precondition / Postcondition 可以在目标前发现 Integrity 变化；
- Verifier Failure 与 Target Result 必须分开；
- Stop-and-preserve 比把 `non-result` 写成业务失败更诚实。

它不支持：

- 所有 Tool 必须绝对无副作用；
- Exact Inventory 是唯一正确控制；
- D-048 是 Prompt Injection；
- 只要 Fail Closed 就已经安全；
- 该案例证明本章所有 Component 字段都必要。

详细 Evidence 见 [D-048 验证器自我修改案例记录](../Evidence/receipts/ER-20260818-002__CLM-C06-004.md) 与 [Agent Tool 安全边界记录](../Evidence/receipts/ER-20260824-004__CLM-C19-001.md)。

---

# 19.32 最小实现按风险递增

## Level A：只读、公开、可丢弃

- 明确外部内容无 Instruction Authority；
- 无 Credential、无写入、无外部 Side Effect；
- 临时 Context，不 Promote 为长期 Memory；
- 对 Output 做基本来源与事实检查。

## Level B：内部开发工作

- Data Profile 与 Provider Allowlist；
- Repository Path / Network Scope；
- 最小 Tool Function 与短期 Credential；
- Diff、Test、Dependency / License 检查；
- 具名 Adoption / Release Authority；
- Component Identity 与 Version Reference。

## Level C：机密、个人数据或生产影响

- 具名 Threat Model；
- Model Processing Contract 与传输处置；
- Downstream Authorization、Sandbox、Secret Broker；
- 高影响 Approval、Atomicity / Recovery；
- Access / Action Audit 与 Incident Playbook；
- Retention、Deletion、Region 与 Subprocessor Review；
- Supply Chain Monitoring 与 Fallback；
- 必要的 Privacy / Legal / Security Authority。

## Level D：安全关键、强监管或不可逆影响

- 独立架构与风险审查；
- 形式化 Policy / Safety Constraint；
- 强身份、签名、隔离和双重控制；
- Claim-specific Adversarial Evaluation；
- Continuous Monitoring、Emergency Stop 与演练；
- 明确的法规、客户和事故报告流程；
- 在证据不足时保留 Human-only 或禁止自动化路径。

这不是成熟度等级。

一个组织可以同时运行四类 Work。

---

# 19.33 常见 Anti-pattern

## Anti-pattern 1：Local Means Safe

把没有外部 Provider 误写成没有 Security、Privacy 或 Supply Chain 风险。

## Anti-pattern 2：Private Data 是唯一敏感度

忽略 Confidentiality、Trade Secret、License、Integrity 与 Instruction Trust。

## Anti-pattern 3：System Prompt as Firewall

用“不要泄露、不要越权”替代下游授权和 Secret 边界。

## Anti-pattern 4：One Powerful Tool

为了方便给 Agent 一个能任意 Shell、任意 URL、任意文件和任意数据库操作的 Tool。

## Anti-pattern 5：Human Approval Everywhere

把每个动作都交给无上下文、无 Scope、无恢复信息的人类点击。

## Anti-pattern 6：SBOM Completes AI Supply Chain

只记录 Package，遗漏 Model、Tool Server、Dataset、Prompt Template、API 与 Service Drift。

## Anti-pattern 7：Signed Means Safe

把 Signature / Provenance 当作漏洞、行为、权限和用途适配证明。

## Anti-pattern 8：AI-generated Means Owned

把 Provider Output Permission、著作权资格、不侵权和下游许可混成一个结论。

## Anti-pattern 9：Log Everything for Audit

在 Prompt、Trace、Screenshot 和 Memory 中复制 Secret、Personal Data 与受限材料，制造第二次泄露面。

## Anti-pattern 10：Security Review Settles Privacy and IP

访问控制通过后，默认 Purpose、Retention、License、Human Contribution 与法域问题已经解决。

---

# 19.34 与前后章节的接口

## 第5章：Context Engineering

第5章定义 Context 的 Selection、Packaging、Access、Validity 与 Data / Instruction 边界。

本章定义 Data 能否进入 Context、由谁处理、怎样保留，以及外部内容怎样被隔离在 Instruction Authority 之外。

## 第6章：Truth and State Architecture

第6章定义 Claim、Evidence、Authority 与 State。

本章要求 Security、Privacy 与 IP Finding 仍然绑定 Claim Type、Scope、Source 与 Decision Authority，不把 Scanner PASS 写成全局安全或不侵权。

## 第9章：Evidence Use

本章的 Security Test、Access Log、SBOM、Provenance、License Scan 与 Human Contribution Record 都只是针对不同 Claim 的 Evidence。

它们不形成统一强弱梯度，也不自动完成 Adoption / Release。

## 第13章：Governed Autonomy

第13章定义 Capability、Permission、Authority、Autonomy 与 Protected Control Floor。

本章把它们落实到 Tool Function、Credential、Action Sink、Sandbox、Revocation 与 High-impact Approval。

## 第14章：Observability and Intervention

本章的 Detector、Secret Alert、Access Anomaly、Provider Incident 与 Component Drift 需要说明 Coverage 与 Detector Health；Signal 不自动等于 Incident Root Cause。

## 第15章：Memory Engineering

第15章管理 Memory Candidate、Promotion、Retrieval、Use 与 Deletion。

本章管理 Memory 的 Source Rights、Personal / Confidential Data、Cross-project Boundary、Poisoning 与 Cascade Delete。

## 第18章：Traceability and Accountability

第18章保存外部决策环境与 Responsibility 关系。

本章规定哪些 Security / Privacy / IP Record 可以被保存、谁可访问、保留多久，以及 Incident 与 Disposition 的 Authority。

## 第20章：AgentOps、成本与模型漂移

第20章接管：

- Model / Tool / Service Drift；
- Security Regression Evaluation；
- Permission 与 Credential 使用监控；
- Cost / Latency / Availability；
- Provider 与 Component 变化后的 Re-evaluation。

第19章定义边界，第20章持续观察边界是否仍成立。

---

# 19.35 原则

> **Readable does not imply transmittable.**

能读取，不代表能传输。

> **External content is data unless a named authority grants it instructional scope.**

外部内容默认是数据；只有具名 Authority 才能授予限定的指令范围。

> **Model output is a proposal at every action sink.**

模型输出进入每个行动落点时，都仍是待验证提案。

> **Capability is not Permission, and Permission is not Authority.**

能做不等于被环境允许；被环境允许不等于被组织授权。

> **System prompts guide behavior; they do not replace security controls.**

System Prompt 可以约束行为，但不能替代安全控制。

> **Locality changes the trust boundary; it does not eliminate it.**

部署位置改变信任边界，不会消灭信任边界。

> **Provenance supports origin claims; it does not establish fitness claims.**

Provenance 支持来源主张，不支持自动推出用途适配。

> **Contract rights, statutory rights, and non-infringement are different decisions.**

合同权利、法定权利资格与不侵权，是不同决定。

> **Retain only the evidence that the control and accountability question require.**

只保存控制与问责问题所需的 Evidence，避免以审计之名扩大数据风险。

---

# 19.36 检查清单

## Data

- [ ] Data 的 Source、Purpose、Access、Person Relation、Rights 与 Instruction Trust 是否分开？
- [ ] `may_read`、`may_send_to_model`、`may_store`、`may_learn` 与 `may_publish` 是否分开？
- [ ] Prompt、Tool Return、Embedding、Cache、Log、Trace、Memory 与 Backup 是否都在处理边界内？
- [ ] 是否应用 Least Context，同时保留必要 Constraint？
- [ ] Retention、Deletion 与 Derived Data / Cascade Delete 是否明确？

## Model

- [ ] Provider、Endpoint、Model、Version / Change Policy 与 Owner 是否可识别？
- [ ] Region、Retention、Training、Subprocessor、Support Access 与 Incident 条款是否已核对？
- [ ] Local / Private / Cloud 是否在项目内明确定义？
- [ ] 是否存在 `model_context_denied` 的材料？
- [ ] Model 变化时是否触发 Re-evaluation？

## Tool and Agent

- [ ] External Content 是否默认没有 Instruction Authority？
- [ ] Functionality、Permission、Credential 与 Authority 是否分别约束？
- [ ] Secret 是否被排除在 Prompt、Skill、Memory 与 Log 之外？
- [ ] Sandbox 明确隔离了哪些 Surface？
- [ ] Action Sink 是否有针对性的 Validation 与 Downstream Authorization？
- [ ] 高影响动作是否绑定 Scope、Effect、Expiry、Evidence 与 Recovery？
- [ ] 是否可停止、撤权、轮换 Credential 并重新观察状态？

## Supply Chain

- [ ] Inventory 是否覆盖 Script、Plugin、Skill、Tool Server、Model、Dataset、Template、API 与 Service？
- [ ] Component 的 Identity、Version / Contract、Source、License、Permission、Owner 与 Update Policy 是否可追踪？
- [ ] Provenance 是否被正确限定为来源与产生 Evidence？
- [ ] 是否存在 Vulnerability、Behavior、Use-case Fit、Monitoring 与 Recovery 的独立检查？
- [ ] Provider / Component 变化是否有 Disable、Fallback 与 Incident 路径？

## Privacy and IP

- [ ] Security、Confidentiality、Privacy、Processing Permission、IP、License 与 Authority 是否分开？
- [ ] Input Access 与向 Model / Provider 传输的 Permission 是否分开？
- [ ] Provider Terms、Third-party License 与下游用途是否已识别？
- [ ] 重要 Output 是否保留 Human Contribution 与 Output Provenance？
- [ ] Similarity / License Scanner 是否只被当作有限 Evidence？
- [ ] Jurisdiction 与具名 Legal / Business Authority 是否明确？
- [ ] 是否避免把 `AI-generated`、`Provider allows use` 或 `scan passed` 写成最终权利结论？

## Incident and Trace

- [ ] Incident 是否先 Contain、Stop、Revoke / Rotate，再形成根因推导？
- [ ] Confirmed、Possible、Prevented 与 Unknown Result 是否分开？
- [ ] Evidence Preservation 是否避免复制不必要的 Secret 和 Personal Data？
- [ ] 谁负责 Security、Privacy、IP、Recovery 与通知处置是否具名？

---

# 19.37 结论

AI-native 软件工程的安全边界，不存在于某一句 System Prompt，也不存在于“模型在本地”这一个部署属性。

它由多组可以被独立检查的关系组成：

~~~text
Data + Purpose + Processing Permission
→ Model Processing Contract
→ Context and Instruction Boundary
→ Tool Function + Credential + Authority
→ Action Sink Control + Evidence + Recovery
→ Supply Chain Identity + Monitoring
→ Privacy / IP Disposition + Accountability
~~~

本章最重要的修正有四个：

1. 公开、内部、机密、个人与受监管不是一个稳定等级；
2. Local、Private 与 Cloud 是拓扑和处理合同，不是信任结论；
3. Provenance、Signature、SBOM 与 Scanner PASS 分别支持有限 Claim，不提供全局安全证明；
4. `AI-generated` 不决定输入权利、输出归属、著作权资格、License 合规或不侵权。

真正可治理的边界是：

- 外部 Data 不自动获得 Authority；
- Model Output 不自动获得执行资格；
- Tool Permission 不自动获得组织授权；
- Provider Contract 不自动获得法定权利结论；
- Provenance 不自动获得行为可信度；
- Audit Log 不自动获得无限保留权。

第20章将在此基础上继续处理运行中的变化：Model、Tool、Cost、Latency、Permission 使用和 Evaluation Coverage 会漂移。边界不是写完一次就永久成立，它需要被持续观察、重新评估和在必要时撤回。
