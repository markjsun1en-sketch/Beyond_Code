# AI Native Software Engineering：Cognitive Control、Trust 与 Human Control Plane

> 讨论整合稿 / v0.1  
> 适用范围：AI Native Software Engineering、长期 Agentic Development、AI-assisted Production System、AI Game Development OS 等复杂 AI 工程系统。  
> 核心问题：当 AI 的生成、执行和维护能力远高于人的阅读与验证带宽时，如何仍然保持系统的可控性、可信性与长期一致性。

---

## 0. Executive Summary

AI 软件工程正在产生一个越来越明显的结构性矛盾：

```text
AI Generation / Execution Throughput
                >>>>>>>>>>
Human Review / Understanding Throughput
```

AI 可以在很短时间内生成大量：

- Code
- Rules
- Tests
- Documentation
- Validators
- Gates
- Workflows
- Agents
- Skills
- Refactors
- Evidence
- Configuration
- Memory / Knowledge

但人的注意力、工作记忆、理解能力和高质量 judgment 并不会同比增长。

因此，传统的：

```text
AI / Human produces
        ↓
Human reads everything
        ↓
Human understands everything
        ↓
Human approves
```

无法长期扩展。

未来更合理的控制模型不是让人继续尝试理解全部执行细节，而是建立一个：

> **受治理、可观察、可验证、可回退、具有长期记忆和动态信任的 AI Production System。**

系统负责：

- 执行；
- 记录；
- 验证；
- 暴露异常；
- 压缩复杂度；
- 校准 workflow；
- 管理低风险自治；
- 提供 evidence。

人负责：

- Intent；
- Boundary；
- Creative / Strategic Judgment；
- Authority；
- 关键风险；
- 关键例外；
- 不可委托的最终决策。

最终的目标不是 **Human-out-of-the-loop**，而是从：

```text
Human-in-every-loop
```

演化到：

```text
Human-on-the-loop
```

也就是：

> **Human controls the system, rather than inspecting every output of the system.**

---

# 1. 问题起点：AI Output 已经超过 Human Review Capacity

传统软件开发里，一个开发者或一个小团队通常还能通过代码审查、测试和设计讨论保持较强的 mental model。

AI 改变了这个比例。

一次简单自然语言请求，可能隐含地产生：

```text
3 rules
5 workflow changes
2 Python validators
4 gates
10 tests
6 docs updates
1 registry migration
```

对于 AI 而言，这只是一次执行。

对于人而言，这意味着十几个新的认知对象。

因此，AI 时代出现了一个基本不等式：

```text
Generation Cost ↓↓↓
Verification Cost ↓（远慢于 Generation）
Human Judgment Capacity ≈ Constant
```

这意味着：

> **Generation cheap ≠ Verification cheap。**

一个成熟的 AI engineering system 不能继续假设“人最终会把所有东西看完”。

---

# 2. Cognitive Overload 不只是“信息太多”

这里的 cognitive overload 可以进一步分成五种。

## 2.1 Output Overload

AI 生成太多输出物：

```text
Code
Docs
Rules
Tests
Evidence
Assets
Plans
Reports
```

人无法全部阅读。

---

## 2.2 State Overload

随着系统长期演进，人逐渐无法记住：

- 当前有哪些规则；
- 哪些 workflow 仍然有效；
- 哪些 gate 已经废弃；
- 哪些 agent contract 最近变化；
- 哪些 capability 已经获得自治权；
- 哪些 assumption 仍成立。

问题从：

> “我有没有看过？”

变成：

> “我现在是否还能维持一份完整的 system mental model？”

---

## 2.3 Dependency Overload

一个局部变化可能经过：

```text
Governance
   ↓
Workflow
   ↓
Agent
   ↓
Skill
   ↓
Tool
   ↓
Runtime
   ↓
Evidence
```

人很难持续维护完整因果关系。

---

## 2.4 Judgment Overload

真正昂贵的不是“阅读”，而是判断：

```text
这个设计是否必要？
这个 gate 是否过度？
这个 validator 是否真的保护重要风险？
这个 architecture refactor 值得吗？
这次变化是优化还是局部最优？
```

AI 越强，越可能一天生成更多“值得考虑的候选项”。

因此真正稀缺的资源逐渐变成：

> **Human Judgment**

而不是 token、GPU 或 code generation capacity。

---

## 2.5 Meta-level Overload

再往上，用户甚至需要判断：

```text
Agent 本身合理吗？
Workflow 本身合理吗？
Governance 本身是否过度？
Trust mechanism 是否可信？
LTM 有没有污染？
Self-evolution 是否在产生错误强化？
```

这已经从 implementation overload 演化成：

```text
Systems Design Overload
+
Governance Overload
+
Judgment Overload
```

---

# 3. 控制的定义必须发生变化

早期的控制是：

```text
Line-level / Implementation Control
```

即：

> 我知道每一段代码、规则、脚本为什么这么写。

随着系统复杂度增加，这种控制一定会下降。

更成熟的控制应逐渐迁移到：

```text
Implementation Control
        ↓
Component Control
        ↓
System Control
        ↓
Governance Control
        ↓
Constitutional Control
```

最终，人不需要知道：

```text
manifest_validator.py 第 417 行为什么这么写
```

但必须能够快速回答：

```text
它为什么存在？
保护什么 invariant？
什么时候触发？
拥有什么 authority？
失败会影响什么？
谁批准它？
怎么 bypass？
怎么 disable？
怎么 rollback？
```

这意味着控制从：

> **理解全部实现**

升级为：

> **理解系统行为、权限、风险、证据和恢复能力。**

---

# 4. Human Control Plane

Human Control Plane 是整个框架的核心。

它不是新的执行层，而是：

> **把机器级复杂度压缩成人类可管理复杂度的控制界面。**

推荐总体结构：

```text
                         HUMAN
                           │
             Intent / Creative Judgment
                           │
                  Human Control Plane
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
 Constitution        Authority / Risk     Attention
        │                  │                  │
 Decision Ledger      Trust Engine       Control Brief
        │                  │                  │
 Known-Good          Rollback / Kill      Exception
        └──────────────────┼──────────────────┘
                           │
                    Project System
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
  Governance            Workflow             LTM
       │                   │                   │
       └───────────── Agents + Skills ─────────┘
                           │
                     Model Adapter
                           │
               GPT / Claude / Local LLM
                           │
                 Software / Project Outcome
                           │
                  Evidence / Feedback
                           │
                    back into system
```

这里不再使用 `Game` 作为最底层结果，因为整个框架适用于：

- 游戏项目；
- 软件产品；
- SaaS；
- 内部工具；
- 内容生产系统；
- AI-assisted engineering organization；
- 其他长期 Agentic Project。

对于 AGDOS，可以把 `Software / Project Outcome` 具体化为 `Game / Project Outcome`。

---

# 5. Human Control Plane 的主要组成

## 5.1 Constitution

Constitution 不是几百条 rule，而是少量不可轻易突破的最高原则。

例如：

```text
C01 Code / Runtime is operational truth.
C02 Docs express intent, not runtime fact.
C03 AI may not silently expand its own authority.
C04 Blocking gates require explicit protected risk.
C05 Governance cost must be proportional to project risk.
C06 High-impact changes require reversible paths.
C07 AI-generated evidence may not be the sole proof of its own assumptions.
C08 Automation must preserve human override.
C09 New autonomous capability starts with bounded authority.
C10 Human authority dominates automated governance.
```

目的：

> 把几千个 implementation objects 压缩成少数核心 invariants。

---

## 5.2 Authority Matrix

系统必须明确：

```text
谁能做什么？
在哪些范围内？
需要什么 evidence？
什么时候必须 escalation？
谁能 override？
```

典型自治等级：

```text
ADVISORY
   ↓
SUPERVISED
   ↓
LIMITED AUTO
   ↓
AUTO + AUDIT
```

任何重大事故都可以降级：

```text
AUTO
 ↓
SUPERVISED
 ↓
ADVISORY
 ↓
OFF
```

---

## 5.3 Decision Ledger

真正长期值得记录的不是所有 code diff，而是：

> **为什么做了这个决定。**

示例：

```text
Decision D-0241

Problem:
Manifest validator blocks normal iteration.

Decision:
Move validation from iteration gate to release gate.

Reason:
Protected risk only exists during packaging.

Alternatives:
1. Keep blocking behavior
2. Advisory warning
3. Release-only blocking ← selected

Tradeoff:
Some errors may be discovered later.

Rollback:
Restore previous trigger policy.
```

Decision Ledger 提供：

> **institutional memory of intent。**

---

## 5.4 Known-Good Baseline

所有关键系统都应该维护 Known-Good：

```text
Known-Good
   +
Bounded Change
   +
Evidence
   =
Candidate
```

而不是：

```text
Current
  ↓
AI modifies everything
  ↓
new Current
```

Known-Good 的价值：

- 可比较；
- 可验证；
- 可回滚；
- 可做 controlled experiment；
- 防止长期 drift。

---

## 5.5 Rollback / Kill / Downgrade

真正的 control 必须意味着：

> “我可以停止它。”

所有高影响 capability 至少应具备：

```text
disable
bypass
rollback
freeze
downgrade
```

信任不是来自“它不会犯错”，而是：

> **即使犯错，也被限制在可接受 failure envelope 内。**

---

# 6. Trust：最终信任的是 System，而不是 Agent

AI engineering 里最危险的信任模型是：

```text
我相信 Codex
我相信这个 Agent
它过去表现不错
```

更成熟的 trust object 应该是：

```text
Trustworthy System
=
System Configuration
+ Institutional Memory
+ Current Evidence
+ Operational History
+ Authority Boundaries
+ Recovery Capability
```

也就是说：

> **信任的是一个系统配置，而不是 AI 的“人格”。**

如果以下任意东西发生重大变化：

- Model；
- Agent Contract；
- Context；
- Rules；
- Workflow；
- Tool Permissions；
- Authority；
- Skill；
- Verification Strategy；

都可能意味着 trust 需要重新校准。

---

# 7. LTM：连续性来源，但不能成为 Truth

LTM 的价值是让系统从：

```text
聪明但失忆
```

升级成：

```text
聪明
+
有组织历史
+
有长期知识
```

但 LTM 不能成为绝对 Truth。

推荐区分：

```text
Code / Runtime
= current operational truth

Registry / Contract
= declared current state

Decision Ledger
= historical decision truth

LTM
= accumulated knowledge / interpretation

Producer Soul / Identity
= long-term preference / judgment tendency
```

如果 LTM 中的错误总结被自动强化，会产生：

> **memory-amplified error**

因此 LTM 应支持：

- provenance；
- confidence；
- scope；
- validity；
- superseded state；
- contradiction detection。

---

# 8. Trust 不应该只依赖 Runtime History

新 workflow / 新 capability 天生没有大量历史数据。

这是一个 cold-start problem。

但：

> **No history ≠ No information**

即使第一次运行，我们通常仍知道：

- blast radius；
- reversibility；
- authority；
- failure severity；
- observability；
- deterministic verification availability。

因此 Trust 最好拆成两类。

---

## 8.1 Assured Trust

来自结构设计：

```text
Bounded Authority
Sandbox
Acceptance Test
Deterministic Check
Rollback
Observability
Known-Good Baseline
```

这是第一次运行也可以拥有的。

---

## 8.2 Earned Trust

来自实际运行历史：

```text
Runs
Rework
Failure
Rollback
Human Intervention
QA Reopen
Defect Escape
Audit Result
Incident History
```

随着时间积累。

因此：

```text
Early Confidence
≈ Assured Trust

Mature Confidence
≈ Assured Trust
+ Earned Trust
```

不是简单数学加法，而是两个独立信任来源。

---

# 9. 不要一开始做“Trust Score = 87.3”

数据很少时，精确分数会制造虚假数学确定性。

早期更适合：

```text
Design Confidence:       HIGH
Evidence Confidence:     MEDIUM
Operational Confidence: LOW

Authority:
SUPERVISED
```

或者：

```text
UNPROVEN
PROVISIONAL
TRUSTED
WATCH
RESTRICTED
```

样本增加以后，再引入趋势性指标。

---

# 10. 历史数据必须自动记录，而不是用户手工维护

如果系统要求用户每次填写：

```text
这次 workflow 好不好？
是否成功？
返工多少？
```

长期一定失败。

Telemetry 应该成为 workflow execution 的自然副产品：

```text
workflow_id
workflow_version
started
completed
failed
rejected
reworked
rolled_back
human_intervention
qa_reopened
acceptance_result
exception
```

系统自动统计：

```text
Runs                 31
Direct acceptance    24
Minor rework          5
Major rework          2
Rollback              1
Human escalation      3
```

用户平时不需要看到这些原始数据。

只有产生异常趋势时，才进入 Human Attention Queue。

---

# 11. 小样本阶段：寻找 Red Flag，而不是计算成功率

例如：

```text
3 / 3 successful runs
```

不能说明：

```text
100% reliable
```

Cold Start 阶段更应该检查：

```text
Major failure?
Unexpected authority?
Silent failure?
Rollback failed?
Evidence missing?
Human intervention?
Unsafe side effect?
```

因此早期重点是：

> **Failure Discovery**

而不是：

> **Performance Optimization**

---

# 12. Earned Autonomy

Trust 的最终用途不是制造漂亮分数，而是决定：

> **系统应该获得多少 autonomy。**

建议能力成长路径：

```text
ADVISORY
   │
   │ structural checks passed
   ↓
SUPERVISED
   │
   │ clean execution history
   ↓
LIMITED AUTO
   │
   │ operational evidence accumulated
   ↓
AUTO + RANDOM AUDIT
```

出现事故可以反向移动。

关键原则：

> **Autonomy is earned, not assumed.**

---

# 13. 新能力 = 新角色，而不是自动继承旧 Trust

一个 Agent 可能已经证明：

```text
Gameplay implementation
→ highly reliable
```

但这不意味着：

```text
Governance modification
→ highly reliable
```

同一 Agent 获得新 capability 时，应视为新的 trust domain。

例如：

```text
Program Agent
├── gameplay coding       TRUSTED
├── refactoring           PROVISIONAL
├── architecture change   SUPERVISED
└── governance changes    ADVISORY
```

Trust 应绑定：

```text
Role
+
Capability
+
Workflow
+
Configuration
```

而不是绑定 Agent 人格。

---

# 14. AI Review 不应该变成 AI 自证

危险模式：

```text
Builder AI
    ↓
Reviewer AI
    ↓
Validator written by AI
    ↓
Gate designed by AI
    ↓
PASS
```

看起来有四层验证，但可能共享同一个错误 assumption。

这叫：

> **correlated validation failure**

因此最好至少拆成：

```text
                Builder
                   │
                   ▼
            Implementation
                   │
          ┌────────┴────────┐
          ▼                 ▼
      Verifier          Challenger
          │                 │
  Does it satisfy     Should this solution /
      the spec?       spec exist at all?
          └────────┬────────┘
                   ▼
                Evidence
```

AI 的自然语言判断：

```text
"Looks good."
```

只能算 Weak Evidence。

---

# 15. Evidence 分级

## Weak Evidence

```text
AI says implementation is correct
AI says tests look sufficient
AI says architecture is reasonable
```

## Medium Evidence

```text
Executed tests
Schema validation
Static analysis
Deterministic checks
Invariant verification
```

## Strong Evidence

```text
Independent acceptance tests
Black-box behavioral tests
Fault injection
Adversarial challenge
Production observation
Human sampling
```

核心原则：

> **Natural-language agreement is not equivalent to independent evidence.**

---

# 16. Random Audit：人不可能检查 100%，但也不应该检查 0%

推荐：

```text
Low Risk
→ AI autonomous
→ Human random audit 2–5%

Medium Risk
→ higher sampling

High Risk
→ mandatory review / approval
```

抽查的价值：

- 检测 AI review blind spot；
- 校准 trust；
- 发现 correlated failure；
- 建立真实 operational reputation。

Trust 必须可以通过审计历史“挣出来”。

---

# 17. Workflow 是减少 Cognitive Overload 的关键，但不是靠用户手工维护

最初容易得到这样的结论：

```text
调优 workflow
→ 信任 workflow
→ 少看执行过程
```

但这个逻辑不完整。

因为：

- 用户可能不会设计 workflow；
- 用户不一定会正确调优；
- AI 自己调优可能产生局部最优；
- Workflow 越调越复杂，也会形成新的 overload。

因此：

> **Workflow 本身也必须被治理。**

---

# 18. Workflow Optimization 应改成 Workflow Calibration

不存在全局最优 workflow。

Prototype：

```text
Speed
Exploration
Tolerance for discarded work
```

Production：

```text
Consistency
Maintainability
Predictability
```

Release：

```text
Stability
Verification
Risk control
```

因此真正的问题是：

> “这个 workflow 现在是否仍适合当前 context？”

而不是：

> “这个 workflow 是否越来越 optimized？”

推荐术语：

> **Workflow Calibration**

---

# 19. Workflow Change 是 Hypothesis，不是 Improvement

错误表达：

```text
I optimized the QA workflow.
```

更正确：

```text
I created QA Workflow v12 candidate.

Hypothesis:
Reduce duplicate triage.

Expected benefit:
Lower interruption cost.

Guardrails:
No increase in missed critical defects.
No increase in late reopen rate.
```

推荐变化流程：

```text
Current Workflow
      │
      ▼
Observed Problem
      │
      ▼
Optimization Hypothesis
      │
      ▼
Candidate Workflow
      │
      ▼
Controlled Evaluation
      │
  ┌───┴────────┐
better     worse/unclear
  │             │
adopt        rollback
```

---

# 20. 永远保留 Known-Good Workflow

例如：

```text
Gameplay Workflow v7
= KNOWN GOOD

Gameplay Workflow v8
= CANDIDATE
```

不是：

```text
v7 → overwrite → v8
```

而是：

```text
              v7 Known Good
              │
              ├────── Production
              │
              └────── v8 Candidate
                         │
                      Evaluate
                     /        \
                  better      worse
                    │           │
                  adopt       discard
```

这让 workflow evolution 从 mutation 变成 controlled experimentation。

---

# 21. Workflow 评价必须是 Multi-objective

单一目标容易产生 Goodhart's Law。

例如：

```text
Human Interruption ↓
```

不能直接说明：

```text
Workflow Quality ↑
```

因为最简单的降低 interruption 方法是：

> 不告诉人任何问题。

所以 workflow candidate 必须有：

```text
Primary Objective
+
Guardrail Metrics
```

示例：

```text
Goal:
Reduce human interruption.

Guardrails:
Major defect rate must not rise.
Late rework must not rise materially.
No authority escalation.
Creative diversity must not collapse.
```

---

# 22. 游戏 / 创意软件还需要 Human Creative Calibration

一些关键目标无法完全量化：

```text
好不好玩？
有没有 taste？
是否有惊喜？
有没有调性？
是不是正确但无聊？
```

因此：

```text
Machine Metrics
+
Evidence
+
Periodic Human Judgment
```

必须长期共存。

不是每次都看，而是 periodic calibration sampling。

---

# 23. Production Workflow 与 Exploration Workflow 应分开

历史数据天然奖励：

```text
最稳定
最安全
最高成功率
```

如果让 system 只追求这些，最终会逐渐消灭探索性。

因此可以明确区分：

```text
Known-Good Production Path
+
Controlled Exploration Path
```

概念上可能类似：

```text
80% exploitation
20% exploration
```

比例不是固定要求。

关键是：

> Exploration Budget 必须是被明确保护的系统能力。

---

# 24. Governance、Workflow、Agents、Skills 分别决定什么

最终 Project Outcome 并不是由某一个 Agent 决定。

可以理解为：

```text
Project Outcome
≈
Project Governance
× Workflow
× Agents
× Skills
× Project Identity
× Memory
× Evidence / Feedback
× Model Capability
× Human Judgment
```

更重要的是各层职责：

## Governance

决定：

```text
Search Space
Authority
Risk Boundary
What is locked
What may change
What requires approval
```

---

## Workflow

决定：

```text
How problems are explored
How hypotheses are generated
How candidates are compared
How results are validated
```

---

## Agents

决定：

```text
Role
Perspective
Responsibility
Decision Lens
```

---

## Skills

决定：

```text
Method
Technique
Production Capability
```

可以简单理解为：

```text
Agent = role + judgment perspective
Skill = method + capability
```

---

## Project Identity / Producer Soul / Creative Direction

决定：

```text
Long-term preference
Aesthetic direction
Creative bias
Project-specific judgment tendency
```

---

## LTM

决定：

```text
What the organization remembers
What it has learned
What failed before
Why earlier decisions existed
```

---

## Evidence

回答：

```text
Why should the system believe it succeeded?
```

---

## Human

保留：

```text
Intent
Boundary
Strategic Judgment
Creative Judgment
Final Authority
```

---

# 25. “你的”系统与 External Capability Layer

从系统能力归属角度，可以分成：

```text
YOUR OPERATING INTELLIGENCE
──────────────────────────
Intent
Taste
Project Identity
Governance
Workflow
Agent Contracts
Skills
Memory Architecture
Decision History
Evidence Model
Trust Model
Self-Evolution Rules
Production Knowledge
Human Control Plane


EXTERNAL CAPABILITY LAYER
──────────────────────────
LLMs
Game Engines
Image Models
Third-party Tools
MCP Services
Libraries
Cloud
Git / CI Infrastructure
```

长期核心价值应尽可能集中在上层。

底层模型最好：

```text
replaceable
adapter-based
vendor-neutral
```

因此：

```text
AGDOS / AI Native System
        │
   Model Adapter
   ┌────┼─────┐
  GPT Claude Local
```

模型更像 execution / reasoning provider。

---

# 26. Human Role Migration

人的角色会经历明显迁移。

早期：

```text
Human
 ↓
does work
```

然后：

```text
Human
 ↓
reviews AI work
```

再然后：

```text
Human
 ↓
designs workflows
 ↓
AI executes
```

成熟状态：

```text
Human
 ↓
defines intent / boundaries / judgment
 ↓
System manages workflow + execution
 ↓
Human handles exceptions / calibration / key decisions
```

这不是 Human-out-of-the-loop。

而是：

> **Human-on-the-loop。**

---

# 27. Attention Router：系统真正要优化的是 Human Judgment Load

Human Control Plane 不应该成为新的 Dashboard Overload。

它的目的应该是：

```text
10,000 implementation objects
        ↓
100 managed components
        ↓
20 subsystems
        ↓
8 core invariants
        ↓
3 important changes
        ↓
1–2 decisions
        ↓
HUMAN
```

可以定义一个非常有价值的指标：

## HJL — Human Judgment Load

例如：

```text
100 AI Tasks
→ 42 human decisions
```

与：

```text
100 AI Tasks
→ 7 human decisions
```

如果质量和事故率相当，后者才是更成熟的系统。

---

# 28. TTE — Time To Explain

另一个核心指标：

> **任何重要行为，人类是否能在 5 分钟以内理解？**

必须能回答：

```text
WHAT
发生了什么？

WHY
为什么发生？

WHO / WHAT
谁或什么授权？

EVIDENCE
基于什么？

IMPACT
影响什么？

STOP
如何停止？

ROLLBACK
如何回退？
```

这可以定义为：

> **TTE — Time To Explain**

TTE 越长，系统越难控。

---

# 29. Progressive Disclosure

用户不应该默认看到所有细节。

建议：

```text
Level 0
System health

Level 1
Important changes / attention

Level 2
Decision + impact

Level 3
Evidence + history

Level 4
Execution trace / logs / code
```

日常停留在 L0–L1。

需要判断时进入 L2–L3。

异常时才下钻 L4。

原则：

> **不是“不看过程”，而是“不默认看全过程”。**

---

# 30. Brief：Human Control Plane 的主要人机接口

最终 Human Control Plane 不应该只是后台基础设施。

对人的主要接口应该是 Brief。

---

## 30.1 Production Daily Brief

回答：

> **Project 做得怎么样？**

示例：

```text
PROJECT DAILY

Overall:
Healthy

Current milestone:
SP132

Progress:
- 3 features completed
- 2 bugs fixed
- 1 UX issue remains

Current risk:
Stage readability

Human decisions:
1
```

---

## 30.2 Control Daily Brief

回答：

> **负责做 Project 的 AI System 本身健康吗？**

示例：

```text
CONTROL DAILY

SYSTEM
Overall: Stable

WORKFLOW TRUST
Stable                17
Under Observation      3
Needs Attention        1

ATTENTION

Governance Proposal Workflow
- 2 / 5 recent runs proposed unnecessary blocking gates
- no production incident resulted from rejecting them
- confidence declining

Recommendation:
AUTO → SUPERVISED

AUTHORITY CHANGES
None

ANOMALIES
Manifest validation runtime +31%

HUMAN DECISIONS REQUIRED
1
```

---

## 30.3 Learning / Evolution Weekly Brief

回答：

> **这个 AI organization 最近学到了什么？**

例如：

```text
LEARNING WEEKLY

2 lessons promoted to LTM
1 workflow candidate proposed
1 obsolete rule candidate detected
No major identity drift
No major governance drift
```

因此可以形成：

```text
Daily
├── How is the PROJECT?
└── How is the SYSTEM?

Weekly
└── What did the SYSTEM LEARN?
```

---

# 31. Control Brief 必须是 Exception-driven

Control Brief 不应该每天列：

```text
Workflow A stable
Workflow B stable
Workflow C stable
Workflow D stable
...
```

否则它自己就成为新的 cognitive overload。

正常情况下甚至可以只有：

```text
SYSTEM STABLE

No human action required.
```

只有出现异常才展开。

原则：

> **Silence should mean healthy.**

---

# 32. Human Control Plane 的最终信息压缩链

系统内部可能拥有：

```text
537 executions
41 workflow metrics
19 agents
63 gates
1,200 evidence records
82 LTM changes
```

但人的接口应该是：

```text
Huge System State
       ↓
Telemetry
       ↓
Risk Classification
       ↓
Evidence Compression
       ↓
Exception Detection
       ↓
Attention Routing
       ↓
2 things worth human judgment
       ↓
HUMAN
```

这才是真正意义上的 cognitive compression。

---

# 33. 推荐的 Human Control Plane MVP

不应一次构建完整 Trust/Telemetry 平台。

建议先落地最小闭环。

## P0 — Control Foundation

```text
1. Constitution
2. Authority Matrix
3. Risk Classification
4. Managed Component Registry
5. Decision Ledger
6. Known-Good Baseline
7. Rollback / Disable
8. Human Attention Queue
```

目的：

> 先保证“知道谁能做什么、为什么存在、出事怎么停”。

---

## P1 — Trust & Observability

```text
9. Basic Workflow Telemetry
10. Assured / Earned Trust
11. Workflow Trust State
12. Human Random Audit
13. Control Brief
14. TTE
15. Exception Detection
```

目的：

> 从人工 inspection 迁移到 evidence-based supervision。

---

## P2 — Workflow Calibration

```text
16. Workflow Known-Good
17. Candidate Workflow
18. Calibration Experiments
19. Guardrail Metrics
20. Workflow Drift Detection
21. Auto downgrade recommendation
22. Phase-aware workflow profiles
```

目的：

> 让 workflow 能演化，但不会 silent mutation。

---

## P3 — Institutional Intelligence

```text
23. LTM provenance
24. Decision / Evidence linkage
25. Learning Brief
26. LTM contradiction detection
27. Governance drift
28. Project identity drift
29. Self-evolution proposals
```

目的：

> 建立长期 AI organization continuity。

---

# 34. Anti-patterns

## 34.1 AI Self-certification

```text
AI creates
AI reviews
AI validates
AI approves
```

风险：

> correlated failure + false confidence

---

## 34.2 Trust Everything Because Tests Pass

Tests 只能证明被测试的 assumption。

不能证明：

> 这个 solution 本身值得存在。

---

## 34.3 Metric-driven Blind Optimization

例如：

```text
Human interruption ↓
```

不能直接代表：

```text
Workflow improved
```

---

## 34.4 Workflow Mutation Without Known-Good

长期会导致：

```text
unknown drift
+
hard rollback
+
loss of causal history
```

---

## 34.5 Manual Telemetry

如果依赖用户长期填报，几乎必然失效。

---

## 34.6 Dashboard Everything

“把所有信息可视化”不等于减少认知负担。

Human Control Plane 应以 exception routing 为核心。

---

## 34.7 LTM as Absolute Truth

错误记忆会被系统长期放大。

---

## 34.8 More Gates = Safer

Gate 本身有：

```text
runtime cost
false positive cost
human interruption cost
dependency complexity
deadlock risk
```

治理机制必须计算 Governance Cost，而不仅仅是 Risk Prevented。

---

# 35. 更一般的 AI Native Software Engineering 演化

可以粗略理解为四代。

## Generation 1 — AI as Copilot

```text
Human writes
AI assists
```

---

## Generation 2 — AI as Coder

```text
Human specifies
AI implements
Human reviews
```

---

## Generation 3 — AI as Engineering System

```text
Human specifies
AI plans
AI codes
AI tests
AI documents
Human supervises
```

---

## Generation 4 — AI as Governed Software Organization

```text
Human defines:
Intent
Constraints
Authority
Risk
Strategic / Creative Judgment

AI manages:
Planning
Execution
Verification
Maintenance
Learning
Calibration
```

Human Control Plane 正是从 Generation 3 进入 Generation 4 时越来越必要的基础设施。

---

# 36. 核心设计原则

整套讨论最终可以收敛为以下原则。

## Principle 1

> **Human attention is the scarce resource.**

---

## Principle 2

> **Human should control the system, not inspect every output of the system.**

---

## Principle 3

> **Trust the governed system, not the personality of the agent.**

---

## Principle 4

> **No history → constrain, don't guess.  
> More history → earn autonomy, don't assume it.**

---

## Principle 5

> **Workflow change is a hypothesis, not an improvement.**

---

## Principle 6

> **Known-Good + Candidate + Evidence + Rollback is safer than continuous silent mutation.**

---

## Principle 7

> **Natural-language agreement is weak evidence.**

---

## Principle 8

> **Automation is valuable only when Human Judgment Load decreases without unacceptable quality or risk degradation.**

---

## Principle 9

> **The goal is not maximum autonomy; the goal is appropriate autonomy.**

---

## Principle 10

> **Normal system complexity should be hidden; meaningful exceptions should be surfaced.**

---

# 37. Final Model

最终可以把 AI Native Engineering System 理解为：

```text
                         HUMAN
                           │
                Intent / Judgment
                           │
                  Human Control Plane
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
     Control            Trust            Attention
        │                  │                  │
 Constitution       Assured Trust       Brief
 Authority          Earned Trust        Exception
 Risk               Audit History       Decisions
 Rollback           Evidence            Escalation
        └──────────────────┼──────────────────┘
                           │
                    Project System
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
 Governance            Workflow              LTM
        │                  │                  │
        │          Workflow Calibration       │
        │                  │                  │
        └────────── Agents + Skills ──────────┘
                           │
                     Model Adapter
                           │
             GPT / Claude / Local / Future LLM
                           │
                Software / Project Outcome
                           │
                Evidence / Feedback
                           │
             Telemetry / Learning / History
                           │
                     back into system
```

这里真正长期存在的是：

```text
Governance
Workflow
Agents
Skills
Memory
Identity
Evidence
Trust
Control
Historical Learning
```

模型只是当前使用的 reasoning / execution engine。

---

# 38. 最终结论

AI Native Software Engineering 的长期问题不会只是：

> “AI 能不能写出更多代码？”

更重要的问题会逐渐变成：

> **当机器能够生成和维护远超人类可阅读规模的软件系统时，人类如何仍然拥有可信、可解释、可撤回的最终控制权？**

因此，Cognitive Overload 不应该通过：

```text
让人学会看更多
```

解决。

而应该通过：

```text
机器复杂度
      ↓
Governance
      ↓
Workflow
      ↓
Evidence
      ↓
Trust
      ↓
Exception Detection
      ↓
Attention Compression
      ↓
Human Judgment
```

解决。

最终理想状态不是：

```text
AI 做很多
Human 什么都不知道
```

也不是：

```text
AI 做很多
Human 仍然检查全部
```

而是：

```text
AI executes at machine scale
        ↓
System governs and compresses complexity
        ↓
Human receives only high-value decisions
        ↓
Human preserves final authority
```

这才是可长期扩展的 **AI-native cognitive control model**。
