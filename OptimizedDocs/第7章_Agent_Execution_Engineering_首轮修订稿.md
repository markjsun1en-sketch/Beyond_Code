# 第7章 Agent Execution Engineering
## 把 Work 转化为有边界、可停止、可继续的 Attempt

> 工作稿状态：Phase D 最小完整正文；依据 [全书大纲](../OringinalDocs/beyond_code_ai_native_software_engineering_outline_zh.md) 重构，不把规划条目当作已验证事实。
> 回接说明：[RR-037](../RevisedResult/RR-037_全书对象模型冻结与P1修订规格.md)。
> 适用边界：本章提出 Work、Execution Contract、Attempt、Checkpoint 与 Bounded Execution 的候选工程关系；不要求每个任务持久化完整 Schema，也不把 Execution Epoch、Controller / Worker 或固定治理等级写成普遍必要条件。

前六章依次处理了 Intent、Context、Claim、State、Decision、Assumption 与 Evidence 的边界。

但“知道当前目标与状态”并不等于“已经允许某个 Agent 开始行动”。

执行开始前还需要回答：

- 当前究竟在做哪一项 Work；
- 哪一次执行正在发生；
- 它依据哪个 Intent、Baseline 与 Context；
- 哪些动作和影响面被允许；
- 哪个 Human 或 System Authority 授权了什么；
- 什么情况必须停止、恢复、重新裁决或安全丢弃当前 Attempt；
- 结果将由谁、以什么 Evidence 继续判断。

Agent Execution Engineering（Agent 执行工程：把有适应性的工具调用与环境行动组织成具名、有边界、可观察且可停止的执行）处理的就是这组问题。

它不要求预测 Agent 的每一步内部推理，也不把自由度全部消除。它治理的是外部可观察的目标、输入、授权、动作边界、状态变化与停止条件。

---

# 7.1 Agent 与传统自动化不是非黑即白的二分

传统自动化常被概括为：

~~~text
fixed input
→ fixed procedure
→ output
~~~

Agent 常被概括为：

~~~text
goal
→ plan
→ act
→ observe
→ revise
~~~

这两个图有教学价值，但不能被理解成严格分类。

传统自动化也可以包含分支、重试和动态输入；Agent 也可以被限制在极窄的确定性路径。真正改变执行设计的，不是系统是否被命名为 Agent，而是它是否能够在运行中选择工具、改变路径、读取新信息并产生外部影响。

当这些自由度增加时，工程系统不能只保存最终输出。它需要让执行本身能够被定位：哪项 Work、哪份 Contract、哪次 Attempt、哪组边界、哪条停止与恢复路径。

---

# 7.2 执行链先分开四个对象

本章采用以下最小关系：

~~~text
Intent Artifact
→ Work
→ Execution Contract
→ Attempt
→ Attempt Outcome / Target Result / Evaluation Result
~~~

最后三类结果由第8章正式定义。

前四个对象不能压成一个“Task”：

| 对象 | 回答的问题 | 不代表什么 |
|---|---|---|
| Intent Artifact | 为什么要发生这次变化，希望达到什么 | 当前执行已经获准 |
| Work | 哪个可追踪工作单元需要被推进 | 某次运行本身 |
| Execution Contract | 一次或一类 Attempt 在什么边界内可以进行 | Authority Grant 本身 |
| Attempt | 哪一次有身份的执行实际发生 | Work 已经完成 |

第4章中的 Task 可以继续作为分解、排期或分配单位。第17章中的 Assignment 可以把 Role 绑定到某段 Work。只有当项目需要跨运行追踪目标、Owner、Scope 与关闭语义时，才需要把它稳定地称为 Work。

---

# 7.3 Work 是跨 Attempt 持续存在的工作单元

**Work（工作单元：具有具名目标、Scope、Owner、约束和关闭语义的可引用工程工作）** 回答：

> 项目正在推进的，究竟是哪一项可追踪工作？

一个 Work 至少需要能够定位：

- Identity；
- 目标与当前 Scope；
- Owner 或负责推进的角色；
- Non-goal 与禁止扩张面；
- 关键依赖和当前 Blocker；
- 用于判断关闭的 Target 或 Criterion；
- 当前允许的下一步。

Work 不是一次执行本身。

同一项 Work 可以经历：

~~~text
Attempt A → blocked before target
Attempt B → candidate produced but rejected for scope
Attempt C → narrower candidate accepted for named use
~~~

Attempt A 的失败不会自动关闭 Work；Attempt C 的 Test PASS 也不会自动关闭 Work。Work 是否完成，要根据它的具名关闭目标以及后续有权处置判断。

低风险局部编辑可以把 Work Identity、Scope 与关闭语义压缩进一条 Issue、Commit message 或工作说明。只有当工作跨时间、跨主体、跨环境或被多个下游决定依赖时，才值得持久化更完整的 Work Record。

---

# 7.4 Execution Contract 约束执行，但不创造 Authority

**Execution Contract（执行契约：描述某次或某类 Attempt 的 Target、允许动作、输入边界、Context、资源、停止条件、Evidence 要求与恢复边界的规范性执行接口）** 回答：

> 在当前目标和授权下，这次执行可以做什么，不能做什么，遇到变化时怎么办？

一个 Contract 可以引用：

| 关系 | 作用 |
|---|---|
| Work / Intent / Acceptance Target | 说明执行服务什么目标 |
| Execution Baseline | 固定当前 State、Decision、Assumption、Conflict 与 Source 引用 |
| Context Contract / Manifest | 说明可访问什么信息、来源与时效 |
| Subject / Tool / Environment | 说明谁或什么在什么环境执行 |
| Allowed Action / Effect | 限定文件、数据、网络、部署与其他副作用 |
| Authority Grant / Permission | 引用有效授权与技术能力边界 |
| Budget | 限定时间、成本、调用或影响上限 |
| Evidence Requirement | 说明执行后需要产生什么可检查材料 |
| Stop / Escalation Trigger | 说明何时暂停、阻断或请求裁决 |
| Recovery Boundary | 说明 Rollback、Forward Correction、Fallback 或安全丢弃条件 |

Execution Contract 不是 Authority Grant。

Contract 可以写“允许修改 `src/parser/`”，但这句话只有在其引用或服从的 Authority 与 Permission 有效时才具有执行意义。反过来，Agent 即使技术上拥有写权限，也不能据此推断当前 Work 已经授权写入。

Contract 也不是复制所有上游对象的大型 Manifest。它应优先保存稳定引用和当前差异：Intent 引用、Baseline 引用、Context 引用、Authority 引用，以及本次执行特有的边界。

---

# 7.5 Plan 是路径提案，不等于 Execution Contract

Plan 回答“准备怎样做”；Execution Contract 回答“允许在什么边界内做”。

Plan 可以在执行中调整：

- 改变搜索顺序；
- 替换等价工具；
- 将一个步骤拆成多个步骤；
- 在允许范围内增加检查；
- 因局部失败选择另一条实现路径。

但 Plan 不能自行改变：

- Work 的目标和 Non-goal；
- Authority Grant；
- 被保护的 Policy Floor；
- 允许的外部影响面；
- 已触发的 Hard Stop；
- 必须由具名主体作出的 Decision。

因此，自适应执行并不要求每次路径变化都重写 Contract。只有变化跨越了 Contract 的语义边界，才需要收窄、重新授权、Rebase 或创建新的 Attempt。

---

# 7.6 Bounded Execution 是控制性质，不是第二个 Attempt 对象

**Bounded Execution（有边界执行：能够识别当前执行身份、允许影响面、具名 Authority、结果可见性以及停止／恢复或安全丢弃条件的执行性质）** 不需要成为一份独立记录。

其最低控制功能是：

1. Work / Attempt Identity；
2. Scope 与 Allowed Effects；
3. 具名 Human / System Authority；
4. Result、Failure、Unknown 或 `non-result` 可见；
5. Stop / Recovery，或能够安全丢弃当前 Attempt 的边界。

这五项是语义功能，不是五个必须分别持久化的对象。

一个本地、只读、可丢弃的短任务，可能只需要一条清楚的工作说明和一个退出条件。一个会写生产数据、跨多个环境或持续数小时的任务，则可能需要版本化 Contract、Checkpoint、独立授权与恢复演练。

控制强度由持续时间、并发、影响、可逆性、不确定性、Policy、合同、Rights、下游 Decision Use 与恢复要求触发；不是由“用了 Agent”这一标签自动触发。

---

# 7.7 Attempt 是一次有身份的实际执行

**Attempt（执行尝试：在具名 Work 与 Execution Contract 或等价边界下，由可识别主体从具体起点发起的一次有身份执行）** 回答：

> 这一次实际执行是哪一次？

每次 Attempt 至少应能够定位：

- Attempt Identity；
- Work 与当前 Contract 或等价 Scope / Allowed Effects；
- 可识别执行主体与当前 Authority 边界；
- Start / Stop 边界；
- 输出、Unknown、Failure 或 `non-result` 可见性，以及第8章定义的 Outcome / Result 引用。

当风险、持续时间、环境差异、外部副作用、恢复或下游 Decision Use 使其重要时，Attempt 还可以关联 Start Baseline / Input Snapshot、Context Manifest、Agent / Model / Tool / Environment、Permission / Credential Scope、完整时间、可观察 Action / Change / External Effect、Checkpoint、Handoff 与 Stop Event。这些关系不要求每项低风险工作分别持久化。

Attempt 不是隐藏 Chain-of-thought 的容器。

它保存的是外部可检查的执行环境、动作边界和状态关系。项目可以记录 Plan revision、Tool call、关键 Decision 与 Observation，但不能声称这些记录恢复了模型未外显的内部推理。

当以下任一关键引用发生实质变化时，通常应创建新的 Attempt Identity：

- Intent 或 Work Scope；
- Baseline 或输入身份；
- Contract Version；
- Subject、Agent、Tool 或 Environment；
- Permission、Authority 或 Policy Floor；
- Evaluation Requirement；
- Recovery Path。

是否一定创建新 Attempt，取决于项目的身份规则；但过去的失败、停止或 `non-result` 不能被新运行静默覆盖。

---

# 7.8 Agent Loop 在 Contract 内自适应

一个常见执行循环是：

~~~text
understand current target
→ propose or revise plan
→ select allowed tool
→ act within scope
→ observe external result
→ compare with contract and stop conditions
→ continue / retrieve / pause / escalate / close
~~~

并非每个步骤都需要单独记录。

应该外显的是会改变后续判断的事件，例如：

- 目标或 Scope 解释发生变化；
- 新依赖使 Baseline 失效；
- Tool 产生未预期副作用；
- Agent 请求更高 Permission；
- 成本、时间或影响超过预算；
- Checkpoint 形成；
- Stop、Escalation 或 Handoff 被触发；
- Target 没有被实际触达。

执行记录的目标是支持控制、恢复、Evidence 与责任解释，不是最大化日志数量。

---

# 7.9 Tool Use 必须区分能力、权限与当前授权

一个 Tool 出现在 Agent 的工具列表中，只说明技术能力可能存在。

执行前仍要区分：

| 问题 | 由什么回答 |
|---|---|
| Tool 能否执行某类动作 | Capability / technical permission |
| 平台是否允许当前主体调用 | Permission / credential boundary |
| 当前 Work 是否授权调用 | Authority Grant + Execution Contract |
| 调用结果是否符合目标 | Observation、Result 与后续 Evidence |

同一个“写文件”动作可能作用于：

- 可丢弃 Sandbox；
- 当前 Worktree；
- 共享 Branch；
- 生产配置；
- 外部服务或用户数据。

动作名称相同，影响面并不相同。Contract 应约束 Action Sink，而不是只列 Tool 名称。

当 Tool 会产生外部副作用时，执行记录还需要区分请求已发出、对方已接收、动作已执行、结果已观察和补偿已完成。一次 API 返回成功不自动证明下游状态符合预期。

---

# 7.10 Stop、Pause 与 Escalation 是有效执行结果

Agent 不是只有“继续”和“完成”两种动作。

以下情况通常应停止新的副作用：

- 当前 Authority 不覆盖所需动作；
- Baseline、Intent 或 Contract 已过期；
- Scope 正在向 Non-goal 扩张；
- Tool、Environment 或 Credential 身份不确定；
- Evidence Generator 改变了自己的关键输入或受保护表面；
- 不可逆动作缺少所需 Checkpoint 或授权；
- 成本、时间、重试或影响达到上限；
- 已触发必须由 Human 或其他 Authority 处理的条件。

Stop 不等于 Work Failure。

它可能意味着：

- 当前 Attempt 被安全关闭；
- Work 等待更多 Context；
- Contract 需要收窄或更新；
- 需要新的 Authority；
- 下一次 Attempt 从新的 Baseline 开始；
- 当前 Work 不值得继续，应被有权主体取消。

把 Stop 设计为显式路径，比要求 Agent 在缺失条件下继续制造输出更可靠；但本章不据此声称 Stop 机制已经改善任何项目效果。

---

# 7.11 Checkpoint 保存恢复所需边界，不表示完成比例

**Checkpoint（检查点：在 Work 或 Attempt 过程中保存当前 Baseline、可观察状态、开放风险、Evidence 引用、Authority 边界和下一允许动作的恢复参照）** 回答：

> 如果执行现在暂停，后来者从哪里、依据什么条件继续？

一个有用的 Checkpoint 可以包含：

- Work / Attempt / Contract Reference；
- 当前 Baseline 与已知 Dirty Change；
- 已完成和未完成的可观察动作；
- 当前 Output、Unknown 与 Blocker；
- 已产生的 Evidence 及其适用范围；
- 当前 Permission、Authority 与已触发 Stop；
- 下一允许动作、恢复前置条件与 Owner。

Checkpoint 不等于：

- `50% complete`；
- 当前结果已经通过 Review；
- Work 已被接受；
- Snapshot 能完整重建隐藏推理；
- 所有外部副作用都可回滚。

短任务可以没有独立 Checkpoint。长任务、跨会话任务、多 Agent Handoff、不可逆动作前后或高成本运行，更可能需要它。

---

# 7.12 Resume、Retry、Rebase 与 Restart 不能互相替代

这些动作描述不同变化：

| 动作 | 适用语义 |
|---|---|
| Resume | Contract 与关键 Baseline 仍有效，从 Checkpoint 继续当前 Attempt |
| Retry | 对同一目标发起新的执行尝试；失败分类与次数边界由第8章处理 |
| Rebase | 外部 State、Intent、Decision 或 Context 改变后，显式更新依赖基线与 Contract |
| Restart | 放弃当前运行状态，以新的 Attempt Identity 从明确起点重新执行 |

Rebase 不能重写过去的执行依据。Retry 不能把前一次失败变成“从未发生”。Resume 也不能在 Authority 或 Baseline 已变化时假装执行连续。

如果变化只影响非关键检索顺序，可以继续当前 Attempt；如果变化影响目标身份、允许影响面、Authority、Policy Floor 或结果解释，则应重新裁决边界。

---

# 7.13 与可选 Execution Epoch 的接口

第21章把 **Execution Epoch** 定义为可选的 Lifecycle 组织区间：在一段较长执行中，使 Execution Contract Version 与关键 Intent、Baseline、Context 和 Policy 引用保持明确，直到关闭、重启或显式 Rebase。本章只说明它与 Attempt 的接口，不取得该对象的定义所有权。

它适合：

- 长时间运行；
- 多个兼容 Attempt 共享固定引用；
- 外部状态频繁变化但不能静默进入当前执行；
- 需要记录风险升级、Rebase 与关闭原因；
- Sprint、Batch、Migration 或持续 Agent Session 需要稳定边界。

Epoch 不是新的超级 Manifest。它引用 Contract 与 Baseline，不复制 Intent、Context、Authority、Environment bytes、运行结果和历史 Replay。

同一 Epoch 内，执行 Agent 可以主动增加检查、暂停或请求更高权限，但不能自行：

- 扩大 Authority；
- 降低 Policy Floor；
- 忽略已触发的强制 Gate；
- 删除已记录的风险或冲突。

有权主体仍可依据新 Evidence 调整非关键检查。所谓“单调”只约束执行者不能自我降级 Guardrail，不表示所有治理活动只能增加。

多数短任务不需要显式 Epoch。是否采用它，应由持续时间、并发、外部变化与恢复成本决定。

---

# 7.14 Controller / Worker 是可选拓扑，不是执行前提

原始大纲使用 Controller / Worker 解释目标保持与局部执行分离：

- Controller 维护 Work、边界、分配、冲突与升级；
- Worker 在限定 Scope 内行动、返回 Evidence、报告 Blocker，不擅自扩张任务。

这是一种可用拓扑，不是所有项目的必要组织。

同一个 Agent 可以在低风险任务中同时承担规划和执行；多个 Agent 也可以通过其他 Role Contract 协作。真正需要保持的是：

- 谁维护 Work 与 Contract；
- 谁被允许执行哪些 Action；
- 谁可以修改 Scope 或 Authority；
- 谁检查 Evidence；
- 谁处理冲突、停止与 Handoff。

独立 Role 有时能增加挑战和隔离，但增加 Agent 数量也会增加 Context 分叉、Handoff 与 Integration 成本。组织设计由第17章展开。

---

# 7.15 最小实现按风险裁剪

## 局部、只读、可丢弃

可以是一句话：

> 检查当前 parser 错误路径，只读；以当前 Commit 为 Baseline；输出 Finding 和未知，不修改文件，缺少复现条件时停止。

## 可逆的普通修改

通常还需要：

- Work / Attempt Identity；
- 文件或模块 Scope；
- 允许的 Tool 与写入面；
- Acceptance Target 与 Evidence Requirement；
- 回滚或安全丢弃方式；
- 超范围时的 Owner。

## 高影响、长时或跨边界执行

可能进一步需要：

- 版本化 Contract 与 Baseline；
- 独立 Authority Grant；
- Checkpoint 与 Handoff；
- Credential、Network、Data 与 Environment Boundary；
- 预演、Fallback、Compensation 与人工接管；
- Execution Epoch 或等价的固定引用区间。

复杂度来自风险与恢复要求，不来自模板偏好。

---

# 7.16 常见反模式

1. **把 Work 与 Attempt 合并。** 一次运行结束就把长期目标写成完成。
2. **把 Permission 当 Authority。** 工具能写，不表示当前任务允许写。
3. **把 Plan 当 Contract。** 路径提案静默改变 Scope 或保护底线。
4. **复用 Attempt Identity。** 重试覆盖失败、停止或 `non-result`。
5. **只列 Tool，不列 Action Sink。** 相同命令在 Sandbox 与生产环境具有不同影响。
6. **Checkpoint 只保存摘要。** 没有 Baseline、Open Risk、Authority 或恢复条件。
7. **把 Stop 写成异常。** Agent 在缺失授权或条件时被迫继续。
8. **默认 Controller / Worker。** 为短任务引入不必要的协调对象。
9. **把 Epoch 做成超级容器。** 重复复制 Intent、Context、State 与 Evidence。
10. **记录隐藏推理。** 用外部 Trace 冒充可恢复的 Chain-of-thought。

---

# 7.17 与相邻章节的接口

| 章节 | 第7章复用 | 第7章不重新定义 |
|---|---|---|
| 第4章 | Intent、Scope、Acceptance Target | 目标 Authority 与 Requirement 生命周期 |
| 第5章 | Context Contract、Manifest、Access | Context Truth 或完整知识库 |
| 第6章 | State Claim、Decision、Assumption、Conflict、Execution Baseline | Truth 或 Authority 上位模型 |
| 第8章 | Outcome、Result、Failure、Recovery | 本章只产生可被这些对象解释的 Attempt |
| 第9章 | Evidence Use、Acceptance、Adoption、Release Authorization | Test PASS 的下游裁决 |
| 第10章 | Review Target、Finding、Review Budget | Review 方法与处置 |
| 第13章 | Permission、Authority Grant、Autonomy Profile | 自治与授权来源 |
| 第17章 | Role、Assignment、Handoff、Integration | 组织拓扑 |
| 第18章 | Trace、Attribution、Release Execution / Outcome | 追踪与 Accountability |
| 第21章 | Lifecycle Profile、Transition 与可选 Execution Epoch | 生命周期整合与 Epoch 定义，不由第7章复制 |

第7章拥有 Work、Execution Contract、Attempt、Checkpoint 与 Bounded Execution 的首次正式定义。其他章节可以建立 Target-specific 引用，但不应重新创建这些上位对象。

---

# 7.18 检查清单

## 打开 Work

- Work 是否有具名目标、Scope、Owner 与关闭语义？
- Intent、Acceptance Target 与 Non-goal 是否可引用？
- 一个 Attempt 结束是否会被误写成 Work 自动关闭？

## 打开 Attempt

- Contract、Baseline、Context 与 Subject 是否有明确身份？
- Allowed Effects、Permission 与 Authority 是否分开？
- Stop、Escalation 与 Recovery / Safe Discard 是否存在？
- Attempt 是否有独立 Identity？

## 执行中

- Plan 变化是否仍在 Contract 内？
- 新风险、外部变化和 Scope 扩张是否可见？
- Tool Action 的实际 Sink 与结果是否被观察？
- 需要暂停、Checkpoint、Handoff 或 Rebase 吗？

## 关闭 Attempt

- 实际发生了什么，而不是 Agent 声称什么？
- Target 是否真的被执行和观察？
- Unknown、Failure 与 `non-result` 是否保留？
- 后续判断需要哪些 Evidence 和 Authority？

---

# 7.19 本章结论

Agent Execution Engineering 的中心不是让 Agent 按固定脚本行动，而是让自由度存在于清楚边界内。

~~~text
named Work
→ bounded Execution Contract
→ identifiable Attempt
→ observable action, stop and checkpoint
→ explicit handoff to Outcome / Result
~~~

Work 让目标跨多次运行保持身份；Execution Contract 连接允许动作与上游边界；Attempt 记录哪一次执行实际发生；Checkpoint 保存恢复所需条件；Bounded Execution 确保执行可以被停止、解释或安全丢弃。

这些对象仍不能回答执行是否成功、Target 是否被观察、Verifier 是否有效、Failure 属于哪里，以及应该 Retry、Recover 还是停止 Work。

这些问题由下一章的 Agent Reliability Engineering 接手。
