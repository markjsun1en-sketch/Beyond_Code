# RR-035：第22章 AI-Native 工程能力适配模型首轮调整计划

- 记录日期：2026-08-27
- 原始结构：[全书大纲第22章](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md)
- 主要接口：[第3章工作定义](../OptimizedDocs/第3章_AI原生软件工程定义_首轮修订稿.md)、[第5章 Capability Profile](../OptimizedDocs/第5章_Context对象边界回接稿.md)、[第13章 Governed Autonomy](../OptimizedDocs/第13章_Governed_Autonomy_首轮修订稿.md)、[第16章 Self-Evolution](../OptimizedDocs/第16章_Self_Evolution_Engineering_首轮修订稿.md)、[第20章 AgentOps](../OptimizedDocs/第20章_AgentOps_成本与模型漂移_首轮修订稿.md)、[第21章 Lifecycle](../OptimizedDocs/第21章_AI_Native_SDLC_首轮修订稿.md)
- 案例边界：[RR-014](RR-014_AI_Game_Dev_OS_v4.94开发证据与全书优化.md)
- 记录性质：概念模型与章节结构调整，不是成熟度测量结果或效果证明
- 实施状态：implemented / accepted
- Evidence Routing：本轮检验概念定义、内部一致性、反例和适用范围，不新建 Claim 或 Receipt。若后续对具体项目作等级排名，声称某配置提高效率、质量、安全或成本表现，或准备据此修改 AI Game Dev OS Workflow、Authority 或 Runtime，另行进入正式 Evidence Workflow。

## 1. 入口结论

原第22章试图回答一个成立的问题：

> 一个团队已经具备哪些 AI-native 工程能力，还缺少什么，下一项变化应当是什么？

但 Level 0–5 不是这个问题的可靠答案。

六个 Level 在相邻层之间不断更换评价对象：

| 原 Level | 主要描述对象 | 实际评价维度 |
|---|---|---|
| Level 0：Ad Hoc Assistant | Chat、复制粘贴、无项目记忆 | AI 使用方式与连续性 |
| Level 1：Supervised Copilot | AI 编码、逐项人工 Review | 协作方式与监督强度 |
| Level 2：Bounded Workflow Agent | 工具权限、Evidence、Sandbox、Rollback | 执行 Authority、验证与恢复 |
| Level 3：Governed Multi-Agent System | Controller / Worker、Registry、Review Agent、Handoff | 组织 Topology 与协作控制 |
| Level 4：Cognitive and Evidence-driven Organization | 认知压缩、Decision Interface、Observability、Review Budget | Human Control、Evidence 与运行能力 |
| Level 5：Controlled Self-Evolving Organization | Memory、Skill Evolution、跨项目迁移、组织优化 | 学习、采用与演化 |

这些维度既不互斥，也没有共同的自然单位。

同一个项目可能同时具有：

- 对局部代码补全采用 Supervised Copilot；
- 对生产发布采用 Bounded Workflow Agent；
- 对安全 Review 采用独立 Reviewer；
- 对项目 Memory 保持人工 Promotion；
- 完全不采用多 Agent 或 Self-Evolution。

因此，原六级结构更接近六种混合 Operating Configuration，而不是从低到高的测量刻度。

本轮建议把第22章从“研发成熟度排名”改为：

> 评估当前工程能力是否适合具名 Workload、Intended Use、风险、恢复要求和成本约束，并决定维持、限制、试验、增强、替换或退出哪些机制。

## 2. 与此前结论的一致性

本轮没有出现推翻前文结论的新事实。

已经形成的跨章边界包括：

1. 第3章：AI-assisted、Agentic 与 AI-native 不是单轴成熟度阶梯；
2. 第5章：Context Pattern 是可组合能力，Capability Profile 不产生统一 Level；
3. 第13章：Autonomy 是有范围配置，不是越高越成熟；
4. 第16章：Memory 与 Evolution 是有条件采用的能力，不是终点；
5. 第17章：Agent 数量与组织 Topology 不代表成熟度；
6. 第18章：Trace 机制数量不代表成熟度；
7. 第20章：治理、运行和维护成本不能被机制数量遮蔽；
8. 第21章：Lifecycle Profile 选择路径，不定义项目排名。

如果第22章继续把多 Agent、全链路 Evidence、认知界面、Memory 和 Self-Evolution
依次排成更高 Level，就会反向撤销这些边界。

因此本轮改变的是第22章的表达模型，不是前文结论。

## 3. 事实、推导、建议与未证明部分

### 3.1 可观察事实

- 原大纲明确列出 Level 0–5，并为不同 Level 分配了不同类型的能力；
- 原大纲给出 Truth → Context → Evidence → Governance → Cognition → Memory → Evolution 的推荐迁移顺序；
- 已完成工作稿反复拒绝把 Agent 数量、自治强度、Gate 数量、Trace 数量、Memory 或 Evolution 当成统一成熟度；
- AI Game Dev OS v4.94 的既有记录包含 Governance Activity 增长但 Delivery Evidence 停滞、Test PASS 但 Scope 未接受，以及开发闭环仍为 NON_QUALIFYING 的实例。

### 3.2 事后推导

- 原六级结构混合了使用方式、Authority、组织结构、Evidence、Human Control、Operations 和 Evolution；
- 机制存在、机制被调用、机制有边界、机制产生 Evidence、机制适合当前用途，是不同判断；
- 更多机制可能同时增加控制能力、运行成本、认知负担和错误表面；
- 迁移关系更适合表达为条件依赖，而不是所有组织共享的固定顺序。

### 3.3 当前建议

- 用 Engineering Capability Profile 描述当前能力配置；
- 用 Capability Fit Review 比较具名用途的需要与当前能力；
- 将 Finding 与有权 Disposition 分开；
- 将 Adoption State 与 Fitness 分开；
- 以 Need-driven Dependency 代替固定成熟度迁移顺序；
- 将原六个 Level 保留为“为什么单轴模型失效”的拆解材料，不再作为章节主骨架。

### 3.4 当前没有证明

- 新模型能提高生产率、质量、安全、可靠性或成本表现；
- 本章候选能力面已经完备或彼此正交；
- 任一组织可以使用统一量表或权重；
- AI Game Dev OS 可以被准确评为某个 Level；
- Capability Fit Review 优于所有成熟度模型；
- 具备 Self-Evolution 或 Multi-Agent 的组织更先进。

## 4. 三种结构方案比较

| 方案 | 可能收益 | 成本与失败模式 | 本轮处置 |
|---|---|---|---|
| 保留 Level 0–5，仅增加免责声明 | 熟悉、简洁、容易传播 | 读者仍会把 Level 当成目标；不同维度被误写成先后依赖；诱导功能堆叠 | 不采用 |
| 改成多维矩阵并计算总分 | 能展示多维差异 | 权重缺少自然依据；高分可能掩盖安全缺口；总分制造虚假精度 | 不采用统一总分 |
| Capability Profile + 有范围 Fit Review | 保留差异、适用范围、成本和未知；允许不同 Workload 使用不同配置 | 比单一 Level 更难一句话传播；需要明确 Scope、Evidence 与 Decision Authority | 首轮采用 |

最终书名下的章节标题建议为：

> 第22章 AI 原生工程能力适配：从成熟度阶梯到 Capability Fitness

若为了目录检索保留“成熟度”一词，应把它放在被检验的问题中，而不是继续作为排名承诺。

## 5. 最小概念模型

第22章只新增两个候选整合概念。

### 5.1 Engineering Capability Profile

**Engineering Capability Profile（工程能力配置：对具名 Scope 和时间点，描述当前
实际可用的工程机制、边界、Evidence 与已知缺口的投影）** 回答：

- 当前准备支持什么 Workload 与 Intended Use；
- 哪些能力实际存在并可被调用；
- 它们覆盖什么 Scope、Environment 与 Action；
- Authority、Permission、Human Decision Right 在哪里；
- 当前 Evidence 与 Coverage 是什么；
- Failure、Intervention、Recovery 与 Exit 怎样处理；
- 运行、等待、维护和认知成本是什么；
- 哪些状态未知、过期或发生 Drift。

Profile 是描述性投影。

它不是：

- 新的全局 Truth Store；
- Agent、组织或项目排名；
- Capability Inventory 的数量统计；
- Policy、Authority 或 Acceptance 的来源；
- 声称系统已经有效运行的证明。

### 5.2 Capability Fit Review

**Capability Fit Review（能力适配审查：针对具名 Workload、Intended Use、风险与成本，
比较所需边界和当前 Profile，并由有权角色处置差异的有范围审查）** 至少区分：

~~~text
Workload / Intent / Intended Use
          +
Risk / Impact / Reversibility / Constraints
          ↓
Required Capability Boundary
          ↕ compare
Current Engineering Capability Profile
          +
Observable Evidence / Coverage / Unknown
          ↓
Fitness Finding
          ↓ authorized decision
Fitness Disposition
          ↓
Maintain / Restrict / Experiment / Strengthen / Replace / Retire / Defer
          ↓
Adoption / Operation / Outcome / Drift
          ↺
Re-evaluation
~~~

Finding 是审查判断，Disposition 是有权决定。

Review 不自动改变 Permission、Authority、Protected Control Floor、Adoption 或 Release。

## 6. “成熟”如果保留，只能是有范围结论

本章不再问“这个组织是 Level 几”。

如果继续使用“工程成熟性”，建议将它收窄为：

> 在具名 Scope 和观察窗口内，团队能否可重复地识别能力需要，建立不低于保护底线的配置，观察其实际表现，并在失配、成本或 Drift 出现时调整或退出。

这个定义关注校准能力，而不是机制数量。

它需要同时允许：

- 增加必要能力；
- 限制过宽 Authority；
- 删除重复 Gate；
- 退出无效 Automation；
- 保持简单且已足够的流程；
- 将 Unknown 保留为 Unknown；
- 在风险或环境变化后重新审查。

一个小型项目不采用 Multi-Agent、Persistent Memory 或 Self-Evolution，仍可能对自身
Workload 形成稳定适配。一个拥有大量 Registry、Agent 和 Gate 的组织，也可能因为
Scope、Authority、Recovery 或 Outcome 不清而处于失配状态。

## 7. 候选 Capability Surface

Capability Surface（能力面：为了审查方便，把相关工程关系投影到同一问题域的候选
分组）不是新的对象层级，也不声称穷尽所有项目。

首轮可以使用八个能力面：

| Capability Surface | 核心问题 | 主要跨章接口 |
|---|---|---|
| Work and Intent | Need、Intent、Scope、Acceptance Target 与 Non-goal 是否清楚 | 第4、17、21章 |
| Context and State | 当前 Baseline、State Claim、Context、Conflict、Gap 与 Freshness 是否可见 | 第5、6章 |
| Execution and Authority | Agent 可执行什么、不能执行什么，怎样暂停、恢复与撤权 | 第7、8、13、14章 |
| Evaluation and Decision | Observation、Evidence、Coverage、Review 与 Decision 是否分离 | 第9、10章 |
| Human Control and Cognition | Human 是否能理解当前 Decision Target，并保留方向、介入与接管权 | 第11、12、14章 |
| Organization and Handoff | Work、Role、Assignment、Handoff、Conflict 与 Integration 怎样连接 | 第17章 |
| Memory, Learning and Evolution | Candidate 怎样形成、Promotion、Adoption、Expiry、Rollback 与退出 | 第15、16章 |
| Operations, Trace, Security and Economics | 运行 Baseline、Drift、Recovery、Trace、保护边界和总成本怎样观察 | 第18、19、20章 |

这些能力面可以按用途拆分或合并。

例如，受监管生产系统可能把 Security、Privacy、IP 与 Trace 独立展开；局部只读工具
可能只需一页 Profile。回答“已覆盖”的能力面数量不产生分数。

## 8. 每个能力面的共同检查项

每个能力面至少需要回答：

1. Purpose：为什么当前 Workload 需要它；
2. Scope：适用于什么 Action、Data、Environment 与 Population；
3. Mechanism：当前由哪个可观察机制承担；
4. Authority：谁可以使用、配置、Override、暂停或撤销；
5. Evidence：什么事实支持“机制存在”和“机制有效用于当前用途”；
6. Coverage：Evidence 实际观察了什么，未观察什么；
7. Failure：失败、未知、冲突、超时与误报怎样呈现；
8. Recovery：怎样隔离、回滚、接管、重新授权或退出；
9. Ownership：谁负责维护和最终处置；
10. Economics：运行、等待、Review、维护、认知和机会成本是什么；
11. Drift：什么变化会使当前配置失效；
12. Re-evaluation：何时、由谁、基于什么重新审查。

这是一组检查问题，不是要求每个能力面创建十二个字段或十二份文件。

## 9. Presence、Use、Boundary、Evidence 与 Fitness 分离

第22章需要明确区分五种判断：

| 判断 | 问题 | 不能推出 |
|---|---|---|
| Presence | 某机制是否存在 | 它被实际使用 |
| Operational Use | 它是否进入真实执行路径 | 使用范围正确 |
| Boundary Adequacy | Scope、Authority、Failure 与 Recovery 是否足够 | 它产生目标结果 |
| Evidence Adequacy | 当前 Evidence 是否支持具名 Decision | 该机制长期适配 |
| Sustained Fitness | 在观察窗口中，它是否对当前用途保持可接受结果与成本 | 跨项目普遍最优 |

例如：

- 有 Review Agent，不表示 Review 独立；
- 有测试，不表示 Acceptance Target 已覆盖；
- 有 Sandbox，不表示外部 Side Effect 可恢复；
- 有 Memory，不表示内容仍适用；
- 有 Rollback 命令，不表示 Rollback 已被验证；
- 有完整 Trace，不表示责任已经分配；
- 有 Self-Evolution Pipeline，不表示候选变化值得采用。

## 10. Finding 与 Disposition 不压成总分

Capability Fit Review 可以使用下列候选 Finding：

- fit_for_scope：当前 Evidence 足以支持具名 Scope 的适配判断；
- constrained_fit：只在更窄 Scope、期限或限制下适配；
- gap：所需边界缺失或当前机制不足；
- excess：机制相对当前用途产生不相称的成本、等待或复杂度；
- unknown：Evidence、Coverage 或当前状态不足。

随后由有权角色作出候选 Disposition：

- maintain；
- restrict；
- experiment；
- strengthen；
- replace；
- retire；
- defer。

Finding 与 Disposition 不要求形成全书统一 Enum。

一个 gap 不自动要求增加 Automation；可能的处置也包括收窄 Scope、降低 Delegation、
改回人工路径或停止当前用途。

一个 excess 也不自动要求删除控制；Protected Control Floor、法定、合同、Privacy、
Security、IP 与 Human Decision Right 不能只因成本高而被普通执行者移除。

## 11. Adoption State 与 Fitness 分离

Experiment、Pilot、Active、Sustained、Restricted 和 Deprecated 可以描述机制的采用
状态，但它们不是成熟度。

需要避免：

~~~text
active => fit
sustained => effective
deprecated => wrong
more widely adopted => more mature
~~~

机制可能已经 Active，但仍缺少 Outcome Evidence；也可能已经稳定使用，却因模型、
数据、Policy、成本或 Workload Drift 而失配。

相反，一个未采用的能力可能只是当前 Scope 不需要，不是能力缺陷。

## 12. 必要、实用与可选

### 12.1 必要

只要 Agent 被委托修改持久状态或产生外部影响，就需要形成与风险相称的最小边界：

- 具名 Intent、Scope、Non-goal 与 Decision Target；
- 当前 Baseline 或足够的 State Observation；
- Permission、Authority 与 Human Decision Right；
- 可观察的 Result、Failure 与 Unknown；
- 与 Decision Target 匹配的 Validation / Evidence；
- Pause、Intervention、Recovery 或安全退出路径；
- 不能由普通执行者静默降低的 Protected Control Floor。

“必要”描述的是控制功能，不要求独立 Registry、Dashboard 或 Gate 文件。

### 12.2 实用

在跨会话、跨角色、并发、长任务、高影响或难恢复场景中，以下能力通常有用：

- 版本化 Context / State 引用；
- Execution Contract 与 Attempt Identity；
- Handoff、Checkpoint、Rebase 与 Integration Disposition；
- 独立 Review；
- Progressive Disclosure 与 Human Decision Interface；
- 运行 Baseline、Drift Detection 与 Re-evaluation；
- Memory / Evolution Candidate 的显式 Promotion / Adoption。

### 12.3 可选

以下实现由实际需要触发，不是成熟终点：

- Multi-Agent Controller / Worker Topology；
- Persistent Cross-project Memory；
- Self-Evolution Pipeline；
- 完整 Human Control Plane Dashboard；
- 全量 Prompt / Tool Trace；
- 统一 Registry；
- 十个独立 Gate；
- Execution Epoch；
- 组织级 Capability Score。

## 13. 固定迁移顺序改成条件依赖

原大纲给出：

~~~text
Truth
→ Context
→ Evidence
→ Governance
→ Cognition
→ Memory
→ Evolution
~~~

这条顺序有两个问题：

1. Context、State、Evidence 与 Decision 在实际工作中会反复迭代，不是一次性前后关系；
2. Memory、Multi-Agent、Cognitive Interface 与 Evolution 只在部分 Workload 中需要。

首轮改为 Need-driven Dependency：

~~~text
Observed Need / Failure / Cost / Drift
                ↓
Capability Gap or Excess Hypothesis
                ↓
Bounded Candidate Change
                ↓
Evaluation + Counterevidence + Coverage
                ↓
Authorized Disposition
                ↓
Adopt / Restrict / Replace / Retire / Defer
                ↓
Operation + Outcome + Cost + Drift
                ↺
Re-evaluation
~~~

同时保留若干条件依赖：

- Delegated Side Effect 依赖 Intent、Scope、Authority、Observation 与 Recovery；
- Persistent Memory 依赖 Provenance、Scope、Promotion、Expiry 与冲突处理；
- Self-Evolution 依赖 Candidate、Evaluation、独立 Adoption、Rollback 与运行观察；
- Multi-Agent 只有在可分解性、并行性、专业边界或 Review Independence 有实际需要时才成立；
- Human Decision Interface 由 Decision Complexity、Review Bandwidth、Risk 与 Intervention 需要触发；
- Trace 强度由 Reconstruction、Decision、Retention、Privacy 与 Cost 共同决定。

这些是依赖约束，不是组织必须逐级通过的 Roadmap。

## 14. Capability Fit 需要同时处理不足与过度

传统成熟度模型通常只查“缺少什么”。

AI-native 工程还需要查“什么已经过度”：

- Context 太多导致相关信息被淹没；
- Gate 太多导致 Governance Livelock；
- Reviewer 太多但没有独立 Decision Target；
- Test 数量增加但 Acceptance Coverage 没有增加；
- Trace 太细导致 Privacy、Retention、Storage 与 Review Cost 上升；
- Memory 自动注入扩大陈旧信息或 Prompt Injection Surface；
- Multi-Agent 增加 Handoff 与 Integration Cost；
- Automation 扩大 Authority 或使恢复更困难；
- Dashboard 增加展示量却没有降低 Decision Uncertainty。

因此 Fit Review 至少比较：

~~~text
Required Boundary
Current Capability
Observed Coverage
Protected Floor
Total Production Cost
Known Failure and Recovery
Unknown / Drift
~~~

“减少治理成本”不能被简化为删除控制，“增强治理”也不能被简化为增加对象。

## 15. 三类配置示例，不形成等级

### 15.1 局部、可逆、易观察的代码修改

可能适配的配置：

- 简短 Intent / Scope / Acceptance Target；
- 当前文件和测试 Baseline；
- 一个受限 Attempt；
- 自动 Validation、Diff Review 与 Human Disposition；
- 无 Persistent Memory、Multi-Agent、Execution Epoch 或完整 Dashboard。

缺少 Level 3–5 的机制不构成“不成熟”。

### 15.2 跨会话、跨仓库的迁移

可能需要：

- 版本化 Baseline、Context Manifest 与 Dependency Boundary；
- Execution Contract、Attempt / Handoff Identity；
- Checkpoint、Rebase、Recovery 与 Integration Decision；
- Traceable Change、Evidence Plan 与运行观察；
- 必要时使用多个 Agent 或 Execution Epoch。

Multi-Agent 是否适配取决于工作可分解性和集成成本。

### 15.3 高影响、难恢复或受保护数据相关的变更

可能需要：

- 独立 Risk、Security、Privacy、Rights 与 Release Decision Target；
- Protected Control Floor；
- 更强的 State Observation、Independent Review 与 Recovery；
- Staged Rollout、Incident Path 与 Re-evaluation；
- 明确 Human Authority 和法律／合同边界。

机制更多是风险条件的结果，不是项目等级更高。

## 16. AI Game Dev OS v4.94 的案例用法

v4.94 可以为本章提供三个受限案例：

1. D-073–D-075 的 Governance Activity 增长而 Delivery Evidence 没有同步增长，说明机制和治理活动数量不能替代当前目标的进展；
2. D-079 的测试通过但实现范围未被 Human 接受，说明 Validation Result 与 Fitness / Acceptance Disposition 必须分开；
3. F1–F4a 形成 Source Freeze、Read-only Replay、Identity 与 48/48 PASS，但闭环仍为 NON_QUALIFYING，说明开发能力、验证结果与 Intended Use 的资格处置不是一个状态。

本章可以据此说明：

- Presence 不等于 Use；
- Activity 不等于 Outcome；
- Test PASS 不等于 Scope Acceptance；
- Development Closure 不等于 Qualification；
- Governance Surface 增长不等于 Capability Fit。

它不能说明：

- AI Game Dev OS 处于某个 Level；
- Function-first 是通用最优迁移顺序；
- 当前 Capability Surface 已完备；
- 新 Fit Review 模型已经降低返工、成本、等待或风险；
- 多 Agent、Memory、Evolution 或 HCP 应成为该系统的下一项功能。

这些边界沿用 RR-014 及其既有 Evidence，不分配新的正式 Claim。

## 17. 与各章的对象接口

| 章节 | 第22章复用什么 | 第22章不重新定义什么 |
|---|---|---|
| 第3章 | AI-native 触发条件与工程目标 | AI-native 定义、统一成熟度分数 |
| 第4章 | Intent、Scope、Acceptance Target | 目标事实或 Authority |
| 第5–6章 | Context / State 的 Profile、Coverage、Gap、Conflict | Truth Store 或新的 Context Registry |
| 第9–10章 | Evidence、Review、Finding、Decision Disposition | Evidence 强弱总分或自动 Acceptance |
| 第11–12章 | Review Bandwidth、Progressive Disclosure、Decision Interface | Human 判断的自动替代 |
| 第13–14章 | Authority、Autonomy Profile、Observation、Intervention、Recovery | 自治等级或 Agent 固有 Trust |
| 第15–16章 | Memory / Evolution Candidate、Promotion、Adoption、Rollback | 线性学习终点 |
| 第17章 | Work、Role、Assignment、Topology、Handoff、Integration | Agent 数量排名 |
| 第18–19章 | Trace Purpose、Security、Privacy、Supply Chain 与 IP Boundary | 完整 Trace 或统一法律结论 |
| 第20章 | Outcome、Operational Baseline、Cost、Drift、Re-evaluation | 统一经济指标 |
| 第21章 | Lifecycle Profile、Transition、Decision Target | 固定流程等级 |
| 第23章 | 具名时间序列和受限案例 | 对 AI Game Dev OS 的总分或排名 |

第22章拥有的是跨能力面的适配审查关系，不拥有这些章节的源对象。

## 18. 措辞边界

首轮工作稿应避免：

- “进入下一阶段”“升级到 Level N”；
- “更自治所以更成熟”；
- “多 Agent 是单 Agent 的高级形态”；
- “全链路 Evidence”；
- “完整 Trace”；
- “系统已经学会”；
- “组织实现自我演化”；
- “降低治理即可提高效率”；
- “具备某对象即达到成熟状态”。

建议改为：

- “在具名 Scope 内增加或限制某项能力”；
- “当前 Evidence 支持 fit / constrained / gap / excess / unknown 的有范围 Finding”；
- “该机制适用于当前 Workload，但不推广到其他风险面”；
- “该能力仍处于 Experiment / Pilot / Active 等采用状态”；
- “该 Candidate 需要独立 Adoption 与运行观察”；
- “机制数量不产生 Capability Fit”。

核心英文术语只在首次定义时提供中文语义解释，不在每次出现后重复括号。

## 19. 计划中的章节结构

1. 为什么单轴成熟度在 AI-native 工程中失效；
2. 原 Level 0–5 混合了哪些评价轴；
3. Engineering Capability Profile；
4. Capability Fit Review；
5. Scope、Workload、Intended Use 与 Required Boundary；
6. 八个候选 Capability Surface；
7. Presence、Use、Boundary、Evidence 与 Sustained Fitness；
8. Finding 与 Authorized Disposition；
9. Adoption State 不等于 Fitness；
10. 必要控制功能、实用能力与可选机制；
11. Protected Control Floor；
12. Capability Gap 与 Capability Excess；
13. Governance Economics 与 Total Production Cost；
14. 条件依赖替代固定迁移顺序；
15. Human Control、Multi-Agent、Memory 与 Evolution 的可选边界；
16. Drift、Re-evaluation 与能力退出；
17. 三类非等级配置示例；
18. AI Game Dev OS v4.94 的受限反例；
19. 跨章接口、反模式与检查清单；
20. 结论：优化适配能力，不优化 Level。

## 20. 实施顺序

1. 在 OptimizedDocs 创建第22章首轮工作稿并使用三项 Header；
2. 将原六个 Level 放入“混合维度拆解”而不是主结构；
3. 首次定义 Engineering Capability Profile 与 Capability Fit Review；
4. 将 Fitness Finding 与 Authorized Disposition 分开；
5. 将 Adoption State、机制 Presence 和实际 Outcome 分开；
6. 建立八个候选 Capability Surface，但明确它们不是完备分类；
7. 用条件依赖替换 Truth → Context → Evidence → Governance → Cognition → Memory → Evolution 的固定迁移顺序；
8. 加入 Capability Gap 与 Excess 的对称检查；
9. 以三个非等级 Profile 展示不同 Workload 的适配；
10. 只把 v4.94 用作 Presence、Activity、Validation、Acceptance 与 Qualification 分离的受限案例；
11. 不对 AI Game Dev OS 或其他项目打分；
12. 检查与第3、5、13、16–21章的对象所有权；
13. 检查核心术语首次中文语义说明、Markdown 结构、链接和 Reader-facing Header；
14. 交给 Human Review 决定标题、两个候选概念和原 Level 材料的保留方式。

## 21. Human Review Gate

作者需要裁决：

1. 是否接受把第22章从通用成熟度排名改为 Capability Fitness；
2. 是否接受原 Level 0–5 只作为“混合维度为何不可排序”的拆解材料；
3. 是否接受 Engineering Capability Profile 只描述当前配置，不产生 Authority 或 Acceptance；
4. 是否接受 Capability Fit Review 分离 Finding 与有权 Disposition；
5. 是否接受 Presence、Use、Boundary、Evidence、Adoption 与 Sustained Fitness 分开；
6. 是否接受八个 Capability Surface 只是候选投影，不是完备分类；
7. 是否接受以条件依赖取代固定迁移顺序；
8. 是否接受同时识别 Capability Gap 与 Excess；
9. 是否接受 Multi-Agent、Persistent Memory、HCP、Execution Epoch 与 Self-Evolution 保持可选；
10. 是否接受 v4.94 只承担反例与状态分离，不对系统作成熟度评级。

## 22. 2026-08-27 实施结果

[第22章首轮修订稿](../OptimizedDocs/第22章_AI_Native工程能力适配_首轮修订稿.md)已经形成，
共 22.1–22.46 四十六节。

原大纲的问题域均被保留，但不再构成单轴等级：

| 原主题 | 首轮修订位置 | 结构变化 |
|---|---|---|
| Level 0：Ad Hoc Assistant | 22.3–22.5 | 保留零散使用、连续性和人工复制问题，取消“最低级”处置 |
| Level 1：Supervised Copilot | 22.3–22.5、22.36 | 保留 Human Review 与局部协作配置，不作为通向自治的前级 |
| Level 2：Bounded Workflow Agent | 22.22、22.30、22.34、22.36–22.38 | 拆成 Authority、Evidence、Sandbox、Recovery 与 Protected Floor |
| Level 3：Governed Multi-Agent System | 22.25、22.34、22.37 | Multi-Agent 由可分解性、并行、专业边界或 Review Independence 触发 |
| Level 4：Cognitive and Evidence-driven Organization | 22.23–22.24、22.27 | Cognitive Interface、Evidence、Observability 与 Economics 分别审查 |
| Level 5：Controlled Self-Evolving Organization | 22.26、22.34–22.35 | Memory 与 Evolution 保持 Candidate、Promotion、Adoption、Observation 和退出边界 |
| 推荐迁移顺序 | 22.33–22.35 | 固定顺序改为 Need-driven Dependency 与 Candidate 校准循环 |

### 22.1 最小概念结果

正文只新增两个候选整合概念：

1. Engineering Capability Profile：对具名 Scope 和时间点的当前配置投影；
2. Capability Fit Review：比较 Required Boundary 与 Current Profile，并连接 Finding 与有权 Disposition。

以下语汇没有升级成新的全局对象或 Registry：

- Required Capability Boundary 是 Review 输入，不是最高配置；
- Capability Surface 是审查投影，不是对象层级；
- Fitness Finding 与 Fitness Disposition 是分开的审查字段；
- Adoption State 描述采用生命周期，不产生 Fitness；
- Candidate Finding / Disposition 语汇不是全书强制 Enum。

### 22.2 单轴模型修正

正文明确分开：

~~~text
Presence
≠ Operational Use
≠ Boundary Adequacy
≠ Evidence Adequacy
≠ Sustained Fitness
~~~

Adoption State 继续作为另一条轴。

本章不计算：

- 项目总 Level；
- Capability 总分；
- Agent、Gate、Registry、Trace 或 Automation 数量分；
- AI Game Dev OS 排名。

如果保留“成熟”一词，它只描述在具名 Scope 和观察窗口内持续识别、建立、观察、
调整与退出能力配置的校准能力。

### 22.3 Gap 与 Excess

工作稿同时检查：

- Gap：必要能力、边界、Evidence、Recovery 或 Authority 缺失；
- Excess：Context、Gate、Review、Trace、Memory、Multi-Agent、Automation 或 Dashboard
  相对当前 Decision Use 产生不相称成本和复杂度。

Gap 不自动要求增加 Automation，Excess 不自动允许删除 Protected Control Floor。

### 22.4 路线结果

原 Truth → Context → Evidence → Governance → Cognition → Memory → Evolution 不再作为
所有项目共享的 Roadmap。

正文保留的条件依赖包括：

- Delegated Side Effect 需要 Intent、Scope、Baseline、Authority、Observation 与 Recovery；
- Persistent Memory 需要 Provenance、Scope、Promotion、Conflict、Expiry 与退出；
- Self-Evolution 需要 Candidate、Evaluation、独立 Adoption、Activation、Observation 与 Recovery；
- Multi-Agent 需要可分解性、并行、专业隔离或 Review Independence；
- Human Decision Interface 由 Decision Complexity、Review Bandwidth、Risk 与 Intervention 需要触发。

### 22.5 AI Game Dev OS 案例边界

v4.94 只用于说明：

- Governance Activity 不等于 Delivery Outcome；
- Test PASS 不等于 Scope Acceptance；
- Development Closure 不等于 Qualification；
- Capability Presence 与 Artifact 数量不产生 Fitness。

正文没有：

- 给 AI Game Dev OS 评 Level；
- 把 Function-first 写成通用最优顺序；
- 把 HCP、Memory、Multi-Agent 或 Evolution 指定为下一项功能；
- 声称 Capability Fit Review 已降低成本、返工、等待或风险。

完整时间序列仍由第23章承担。

### 22.6 验证结果

- 三项 Reader-facing Header 已应用；
- 数字章节 Heading 连续为 22.1–22.46；
- Markdown Fence 共 40 个，成对闭合；
- 原 Level 0–5 与推荐迁移顺序均有正文落点；
- Capability Fitness、Engineering Capability Profile、Capability Fit Review、Fitness Finding、
  Fitness Disposition 与 Capability Surface 均在首次正式出现时说明中文语义；
- Reader-facing 正文没有 Claim ID、Receipt ID、Coverage Status 或 Human Status；
- 相对链接目标可解析；
- AI Game Dev OS 案例保留既有不支持边界；
- OriginalDocs 未被修改；
- 本轮未新建 Claim 或 Evidence Receipt。

## Human Disposition

- Status: accepted
- Decision by: Human Author
- Decision at: 2026-08-27
- Rationale: 作者明确回复“通过，继续”。本次接受限定于：以 Capability Fitness 替代通用 Level 0–5 排名；使用 Engineering Capability Profile 与 Capability Fit Review 连接具名用途、当前配置、Finding 与有权 Disposition；分离 Presence、Operational Use、Boundary、Evidence、Adoption 与 Sustained Fitness；同时检查 Capability Gap 与 Excess；以条件依赖替代固定迁移顺序；并保持 Multi-Agent、Persistent Memory、Human Control Plane、Execution Epoch 与 Self-Evolution 可选。接受不表示两个概念或八个 Capability Surface 已经完备、最优或普遍适用，不建立统一评分，不接受本模型已提高效率、质量、安全或成本表现，也不据此给 AI Game Dev OS 排名或指定下一项功能。工作流进入第23章 AI Game Dev OS 纵向案例。
