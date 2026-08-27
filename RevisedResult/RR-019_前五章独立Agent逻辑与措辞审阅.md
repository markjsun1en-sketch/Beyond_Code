# RR-019：前五章独立 Agent 逻辑与措辞审阅

- 记录日期：2026-08-19
- 主要对象：`OringinalDocs/第1章.md` 至 `OringinalDocs/第5章.md`
- 对照对象：全书大纲、第三章 Harness 补充、第二／四／五章现有工作稿、当前第六章工作稿
- 仓库基线：`main@cd842c6fd82f`
- 审阅方式：三个只读 Agent 分别审阅第1–3章、第4–5章和第1–6章跨章逻辑，再由主笔归并
- 当前状态：审阅完成；修改建议等待作者裁决

## 总体结论

前五章的最小叙事链可以成立：

```text
Agent 进入开放式、多步、可行动的执行环
        ↓
部分既有操作条件在特定规模、风险与并发下变得不可靠
        ↓
软件工程需要针对这种执行委托扩展工程环境
        ↓
分别处理 Desired Outcome、Supplied Information 与 Typed State Records
```

当前最大问题不是缺少新理论，而是前后存在两代对象模型：

- 第1–3章仍多次使用层级化的 AI-native 分类、固定 `Truth` 类型和统一 Evidence 强度阶梯；
- 第4、5章原稿仍把 Intent Object 和 Context Pack 写成吸收多种职责的超级对象；
- 第4、5章回接稿已经拆开这些职责；
- 第6章进一步把 Intent、Decision、State Claim、Assumption 与 Evidence 分型，并否定单一 Truth Hierarchy。

如果直接把这些版本组合成书，读者会先在前文接受一个强模型，再在第6章看到它被收窄，却没有得到显式的概念修正。因此，本轮首先要求统一定义和章节所有权；不建议在统一前继续增加新 Pattern、Registry、Gate 或成熟度等级。

## 独立审阅边界

三路审阅是任务独立，不是三名 Agent 对全部一万余行逐句重复检查：

1. 第1–3章审阅者检查历史叙事、理论定义、事实／推导混合和措辞强度；
2. 第4–5章审阅者检查 Intent、Prompt、Agent Input、Context、Manifest、Snapshot、Memory 与 Skill 的对象边界；
3. 跨章审阅者检查第1–6章的论证顺序、术语漂移、重复职责和案例循环支持。

三名 Agent 均报告只读完成，且未读取其他 Agent 的输出。以下结论经过主笔去重；纯风格偏好未进入本记录。

## 每章裁决

| 章节 | 裁决 | 核心原因 |
|---|---|---|
| 第1章 | `narrow` | 角色变化叙事可保留；工具／Agent 二分、历史“首次性”和三层分类写得比证据更确定。 |
| 第2章 | `split` | 七项变化可作为条件式风险诊断；不宜称为已证明的传统软件工程共同历史假设，2.8 的 Truth 模型已被第6章否定。 |
| 第3章 | `split` | 工作定义和“Agentic 不等于 AI-native”成立；定义门槛、两系统／三层模型、Truth 与 Evidence 模型仍互相冲突。 |
| 第4章 | `narrow` | Intent 的长期身份与单次 Agent Input 应分开；原稿和回接稿现在包含两套不兼容 Schema。 |
| 第5章 | `split` | Context 选择与传输属于第五章；来源的 State、Authority 与 Validation 语义属于第六章。原稿和回接稿尚未完全同步。 |

## 第1章：历史叙事需要从“本体差异”收窄为“委托边界变化”

### 1. 工具与 Agent 被写成过强二分

- 位置：`OringinalDocs/第1章.md` 约 295–305、472–500 行。
- 问题：规划器、搜索、优化器和自动调度也会选择路径；一个受严格 Workflow 控制的 Agent 可能比复杂优化器拥有更少开放式裁量。
- 最小处理：差异绑定“被委托的开放式任务解释范围、行动面和运行时反馈闭环”，不绑定某种工具的本体身份。

### 2. “Agent 首次大规模承担”是未经限定的历史断言

- 位置：约 884–914 行。
- 问题：`首次`、`大规模` 需要历史范围和采用数据；专家系统、RPA、自动运维和规划系统构成潜在反例。
- 最小处理：改为“当前一代软件工程 Agent 正把开放式目标解释和多工具行动带入更广泛的日常开发任务”。

### 3. AI-assisted、Agentic、AI-native 名义上不是等级，实际仍被写成阶梯

- 位置：约 583–652 行；并与第2章 1235 行、第3章 387 行附近对照。
- 问题：`第一／第二／第三层`、`最高层级` 与“不是产品代际”相互冲突；多 Agent、长期 Memory 也被误写成 AI-native 的隐含必要条件。
- 最小处理：分成两个轴：`execution delegation` 与 `engineering governance`。多 Agent、长期任务和 Memory 是复杂度触发器，不是定义条件。

### 4. Agent 不天然拥有实现路径

- 位置：约 550 行；第2章约 207 行。
- 问题：“人类拥有目标，Agent 拥有实现路径”把局部裁量写成天然所有权；第四章工作稿实际采用 Delegation、Scope 和 Policy。
- 最小处理：改为“Intent Owner 与部分执行路径的被委托决策者可能分离”。

## 第2章：把“历史隐含假设”改为条件式诊断框架

### 5. 回顾性模型被写成历史事实

- 位置：`OringinalDocs/第2章.md` 约 21–41、57–91 行。
- 问题：Code Review、形式化方法、SRE、安全审批和供应链治理早已处理不完全理解、状态分叉和高变化率。现有材料不足以证明传统制度共同建立在七项统一假设上。
- 最小处理：称为“本书用于诊断现有机制适用边界的七个操作条件”，明确这是 retrospective lens，而不是对设计者动机的历史复原。

### 6. “隐性知识必须显式工程化”超出证据

- 位置：约 217–243、1028–1083、1496–1506 行。
- 既有状态：RR-007 已将 `CLM-C02-001` 评为 `partial / unreviewed`。
- 问题：显式化也会产生维护、过期和错误 Authority；一个 SP122 案例不支持所有 Agent 任务都采用同等治理重量。
- 最小处理：采用现有第二章证据化样例的边界：当复杂度、并发、风险或恢复成本超过人类可持续直接理解的范围时，关键边界、Authority 和完成 Evidence 按风险显式化。

### 7. “行为分布”没有可观察定义

- 位置：约 447–529 行。
- 问题：正文只说明 Agent 可能选择不同路径，却没有给出重复运行、样本集合、模型版本和 Eval 协议；一次任务无法直接观察概率分布。
- 最小处理：没有重复采样时使用“允许行为集合与已观察变异”；只有存在采样协议时才讨论 distribution。

### 8. 2.8 的 Truth Hierarchy 与第6章直接冲突

- 位置：约 927–1024、1069–1077 行。
- 当前模型：`Doc = Intent`、`Code = Implementation Truth`、`Runtime = Behavioral Truth`、`Memory State`。
- 问题：文档可能是 Proposal、Policy、Decision 或 Observation；Code 可能尚未构建／部署；Runtime capture 只覆盖特定场景；Memory 是信息来源，不是项目状态域。
- 最小处理：改为 Typed Records、State Claims、question-scoped Authority 和 preserved conflict；删除固定 Truth Hierarchy 与 `Memory State`。

### 9. 模型能力与治理强度不是单调关系

- 位置：约 1544–1548 行。
- 当前表述：“更强执行能力通常意味着更高治理要求。”
- 反例：能力更强但只读、隔离且必须人工采用的 Agent，治理强度未必高于能力较弱却有生产写权限的 Agent。
- 最小处理：能力可能扩大潜在行动面；实际治理强度由授予的行动面、影响、可逆性、可验证性和历史失效率决定。

## 第3章：它是全书定义枢纽，应优先修正

### 10. 工作定义无法排除普通 AI-assisted Development

- 位置：`OringinalDocs/第3章.md` 约 42–146 行。
- 问题：仅说“人类和智能代理共同参与”也包含 Copilot 提供候选代码，与 3.1 想排除的第一种模式矛盾。
- 最小处理：增加两个判别条件：Agent 被委托真实项目中的部分执行路径；工程环境针对这种委托建立了可裁剪的 State、Authority、Evidence 和 Recovery 机制。

### 11. “两个系统”与“第三层／第三个主要系统”未统一

- 位置：约 273–340、1939–2025 行；Harness 补充约 435–553 行。
- 问题：Product System 与 Production Intelligence System 先被定义为两个系统，Control and Evidence Plane 随后又被提升为第三个同级系统；Intent、Context、Memory、Policy 和 Evidence 在图中改变归属。
- 最小处理：保留两个被工程化的系统；把 Control and Evidence Plane 定义为横切治理与观察能力，不称第三个同级生产系统。

### 12. Evidence 被排成通用强度阶梯

- 位置：约 1080–1136 行。
- 当前模型：`Explanation < Diff < Static Analysis < Test < Runtime < Real-world Validation`，随后自然进入 Acceptance。
- 问题：Evidence 适用性依赖目标 Claim。Diff 对 Repository Change 可能是直接证据，Runtime capture 对源代码内容并不更强；Acceptance 是对具名 Decision Target 的授权处置，不是 Validation 的自然下一等级。
- 最小处理：改为 Claim-dependent Evidence Portfolio；Validation Coverage 与 Acceptance Disposition 分成两条路径。

### 13. 第3章反复恢复已经被第6章撤销的 Truth 模型

- 位置：约 1259–1295、1535–1540、1974–2004、2082–2100、2152–2170 行。
- 问题：Decision 和 Assumption 被 Truth Architecture 吸收；`Doc → Intent / Code → Implementation Truth / Runtime Evidence → Behavioral Truth` 被当成正式映射；流程要求一次性回答“当前真实状态是什么”。
- 最小处理：正式表述统一为“识别 Typed Records，形成有 Scope 的 State Claims，检查 Evidence、Authority、Freshness 与 unresolved conflict”。`Doc as Intent, Code as implementation baseline` 只能作为明确注明局限的启发式。

### 14. 第3章生命周期把第五、六章错误写成单向流水线

- 位置：约 1466 行；大纲约 40 行。
- 当前顺序：`Context Assembly → Truth / State Resolution → Planning`。
- 问题：Context 选择本身依赖 Authority、Freshness 和 Conflict；状态冲突又会触发 Progressive Retrieval。
- 最小处理：改为迭代关系：

```text
Minimum Initial Context
        ↕
Claim / State Resolution
        ↕
Progressive Retrieval
        ↓ sufficient for current boundary
Planning
```

## 第4章：原稿与回接稿必须选择同一对象模型

### 15. Intent Object 存在两套不兼容定义

- 位置：`OringinalDocs/第4章.md` 约 890–925 行；`OptimizedDocs/第4章_Intent与Agent_Input对象边界回接稿.md` 约 51–98 行。
- 原稿：直接内嵌 Truth Baseline、Allowed Authority、Assumption、Risk、Rollback 和 Required Evidence。
- 回接稿：Intent 只保存自身字段及其他对象引用。
- 裁决：采用回接稿边界。Intent 自有 Motivation、Desired Outcome、Scope、Constraint 与 Acceptance Target；State、Assumption、Decision、Authority 和 Evidence 保存引用，不复制运行态内容。

### 16. Task 不一定来自 Intent Graph

- 位置：回接稿约 24–30 行。
- 问题：调查、Incident Response、例行维护或 Evidence Collection 可能由 Policy、告警或事件直接触发。
- 最小处理：仅在 Task 由 Intent 派生时要求 Parent Intent；其他 Task 记录触发来源，在需要改变价值目标时再建立或升级 Intent。

### 17. Prompt 与 Agent Input 的边界仍需统一

- 位置：原稿约 962–1018 行；回接稿约 32–46、199–246 行。
- 问题：Prompt 有时被定义为一次调用的全部输入，有时又只是完整 Agent Input 的文本序列化。实际运行还可能包含多消息、Tool Schema、附件和运行时状态。
- 最小处理：Prompt 是 Agent Input 的指令／消息表达层；Agent Input 是完整运行输入包。Prompt 不应成为长期 Intent 的唯一载体，但实际序列化输入可能具有审计价值。

### 18. Intent Lifecycle 示例裸用 `verified / accepted / rejected`

- 位置：回接稿约 116–139 行。
- 问题：没有说明被验证或拒绝的是 Evidence、实现范围、Adoption 还是 Release，与第6／9章的裁决边界冲突。
- 最小处理：改成具名状态，例如 `evidence_verified`、`implementation_scope_rejected`、`adoption_not_decided`。

### 19. 风险建议被写成固定治理规则

- 位置：回接稿约 276、320–352 行。
- 问题：短期合规任务也可能需要稳定 ID；不可逆未知可以进入自动 Block、Isolation、Evidence Collection 或已授权 Gate，不一定都升级给 Human。
- 最小处理：把“才需要／必须升级”改为“更可能需要／必须进入已授权处置路径”。

### 20. 既有多方 Intent 冲突缺口仍未解决

- 依据：RR-005。
- 问题：当前回接稿主要处理 Parent/Child 与 Agent Delegation，尚未处理产品、技术、安全、体验、成本等多个合法 Intent 之间的优先级、冲突 Authority 和受影响方。
- 最小处理：正式重写时保留一个冲突与裁决接口，不把所有冲突都简化为 Child Intent 偏离 Parent Intent。

## 第5章：Context 的工程记录不能声称模型认知状态

### 21. Selected Context、Pack、Manifest、Access 与 Interpretation 混用

- 位置：`OptimizedDocs/第5章_Context对象边界回接稿.md` 约 24–36、71–103、309–318 行。
- 问题：工程记录可以证明被选择、装配、发送、开放访问或被工具读取；通常不能证明模型注意、理解或使用了什么。
- 最小处理：
  - Contract：应／可／禁止提供；
  - Pack：装配或传输的 Payload；
  - Manifest：Payload 的来源、版本与装配记录；
  - Access Log：可观察到的读取行为；
  - Interpretation：除非有外显输出，否则不作事实声明。

### 22. Context Quality 不是已经证明正交的维度

- 位置：回接稿约 199–226 行。
- 问题：Authority 依赖 Scope，Freshness 影响 Validation 的当前适用性，Security Policy 又可能禁止使用高相关来源。
- 最小处理：改称“不可压缩成单一分数的分别检查项”，不作数学独立性或统一 Schema 声明。

### 23. Hot/Warm/Cold 与 expired/invalidated 不是同一 Lifecycle

- 位置：回接稿约 257–269 行。
- 问题：前者是 Storage/Access Tier，后者是语义有效性；一个 invalidated Record 可能因正在调查而保持 hot，一个 cold archive 也可能仍有效。
- 最小处理：拆成 `storage/access tier` 与 `validity status`。

### 24. Role Projection 不能使内容“可信”

- 位置：回接稿约 283–293 行。
- 问题：Policy 能决定谁可访问、谁可按某来源行动，不能使来源在认识论上变真。
- 最小处理：将“能看到、信任或执行”改为“可访问、获准依赖或获准执行”；Validation 继续引用第6章。

### 25. Snapshot 的范围和归属仍不稳定

- 位置：原稿约 1497–1568 行；回接稿约 309–337 行。
- 问题：State Snapshot 不能完整回答“项目处于什么状态”；Context Snapshot 也不能可靠保存“对决策具有实质影响”的全部内容。
- 最小处理：
  - State Snapshot：声明范围与时点内已识别的 State Claim／状态引用；
  - Context Manifest：被装配的信息；
  - Execution Snapshot：进度、产物和未决项；
  - Execution Baseline：本次获准依赖的组合。

### 26. Memory 与 Skill 不能只按普通 Context 处理

- 位置：原稿约 1855–1961 行；回接稿尚未完整回接。
- 问题：“Memory 是长期、Context 是当前”只适用于特定 Project Memory 定义；Skill 还同时包含 Procedure、Instruction 和 Tool Authority。过期也不等于内容错误。
- 最小处理：Project Memory 作为候选持久来源，被检索并获准提供后才进入 Context；Skill 分开内容、Procedure 与 Instruction/Tool Authority，分别处理 Freshness、Compatibility 与权限。

## 跨章结构问题

### 27. 第5章与第6章是反馈环，不是严格章节流水线

```text
Intent / current task boundary
        ↓
Minimum Initial Context
        ↕
Typed Record / Claim resolution
        ↕
Progressive Retrieval
        ↓
Context Manifest + Execution Baseline
```

第五章在书中位于第六章之前可以成立，但必须显式前向引用。第五章决定信息如何进入工作表面，第六章解释这些来源的类型、Authority、Freshness 与 Conflict；两者在实际执行中迭代。

### 28. SP122/Player Status 存在循环支持风险

- 位置：第2章约 945 行、第4章约 2174 行、第5章约 2472 行、第6章工作稿约 976 行。
- 问题：如果早期章节中的 ID、Schema 和状态是作者基于理论事后重构，再在第6章把同一重构表示当成理论证据，就形成循环支持。
- 最小处理：每次标记 `observable project fact / contemporaneous judgment / reconstructed illustration / current recommendation`。只有绑定 Receipt 的事实支持 Claim；说明性 YAML 只负责教学。

### 29. 原稿与工作稿不能继续充当两个并列规范版本

- 问题：仓库规则正确地保留了原稿，但正式组书时必须明确：原稿是历史材料，工作稿是待裁决候选。不能从两份文件各取方便的定义后声称它们共同组成一个模型。
- 最小处理：每章正式修订先确定对象模型，再从原稿恢复叙事、案例和解释；不要在原稿上逐句修补旧 Schema。

## 术语单一所有权

| 术语 | 唯一定义章节 | 其他章节的边界 |
|---|---|---|
| AI-assisted / Agentic / AI-native | 第3章 | 第1、2章只预告现象，不建立成熟度等级。 |
| Product System / Production Intelligence System | 第3章 | 后章引用，不重新分层。 |
| Control and Evidence Plane | 第3章 | 作为横切平面，不与两个系统竞争同级身份。 |
| Intent Artifact / Intent Owner / Execution View | 第4章 | 后章只引用 ID、Version 和投影视图。 |
| Acceptance Criterion | 第4章 | 第9章定义 Evidence 组合及裁决使用。 |
| Context Contract / Pack / Manifest / Projection | 第5章 | 第4、6章只定义接口。 |
| State Claim / State Snapshot / Authority Applicability | 第6章 | 第5章携带引用，不判断真实性。 |
| Decision / Policy / Assumption | 第6章定义类型与生命周期 | 第4章只引用；执行和治理章节使用其授权结果。 |
| Truth | 第6章的问题域名称 | 不作为可写入、可升级的持久对象。 |
| Execution Baseline Manifest | 第6章 | 第7章引用它打开执行，不复制其内容。 |
| Execution Contract | 第7章 | 第4–6章只前向引用。 |
| Evidence Coverage / Intended Use / Acceptance Disposition | 第9章 | 第4章声明验收目标；第6章只定义 Evidence 与 Claim 的基本关系。 |
| Governance Profile / Gate / Escalation Policy | 第13章 | 前章只描述触发信号和跨章接口。 |
| Evaluation Comparator Baseline | 第9章 | 与第6章的 Execution State Baseline 分开。 |

`Authority Matrix` 暂不列为必备正式对象。第6章先统一 `Authority Grant` 与 `Authority Applicability`；只有实际案例证明矩阵值得维护时，再决定是否保留该名称。

## 与既有审阅结论的关系

| 既有记录 | 本轮结果 |
|---|---|
| RR-004 第3章 Harness | 保持：Harness 与 AI-native 大量重叠，不写成固定集合从属。 |
| RR-005 第4章 Intent | 保持：本章是 Agent-facing requirements operationalization，不宣称替代 Requirements Engineering；多方冲突仍待补。 |
| RR-007 第二章 Claim | 保持：显式化只在风险、复杂度等条件触发，不升级为普遍因果。 |
| RR-009 第5章 Context | 保持：拒绝线性 Pattern 和 Level 0–5；新增 Manifest 观测边界与 Lifecycle 拆轴问题。 |
| RR-018 第6章 | 前五章必须服从其类型分离方向；但 RR-018 中尚未裁决的第6章 Schema 不能反过来被当前前章当作已验证定律。 |

本轮没有新事实要求推翻上述既有结论。变化来自第6章对象模型形成后，可以更精确地定位前五章中的术语冲突。

## 建议修订顺序

这是依赖顺序，不是阅读顺序：

1. 先裁决 RR-018 中第6章的对象轴与 Authority 定义；
2. 重写第3章的工作定义、两个系统／横切平面和 Evidence 模型；
3. 用第3章定义回收第1章的分类和第2章的条件式诊断；
4. 以第4、5章回接稿为对象模型基线，从原稿恢复叙事与案例，而不是逐句修补原 Schema；
5. 最后做第1–6章术语、案例标签和章节转场检查。

不建议先逐句润色第1章，然后按章节顺序一路向后。核心定义位于第3、6章，若它们后改，前章会二次返工。

## Human Disposition

- 本轮审阅结论：`unreviewed`
- 各章原稿：本轮未修改
- 各章工作稿：本轮未修改
- Claim Ledger：本轮未修改
- 建议下一步：作者先裁决“每章裁决”“术语单一所有权”和“建议修订顺序”

## 验证记录

- 三个独立 Agent 均报告只读完成；
- `OringinalDocs/` 未修改；
- `OptimizedDocs/` 未因本次前五章审阅新增改动；
- `Evidence/` 未修改；
- 外部工程未访问或修改；
- 本记录是审阅依据，不是新的 Evidence Receipt。
