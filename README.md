<div align="center">

# ⚡ AgentMaxxing

### Keep the main agent sharp. Push heavy work outward.

**Context-efficient delegation for Codex-style coding workflows.**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Workers](https://img.shields.io/badge/workers-LUNA-7c3aed)

[English](README.md) · [Türkçe](README_TR.md)

</div>

---

AgentMaxxing is a lightweight orchestration skill built around one rule:

> **The main agent keeps the goal, decisions, acceptance, and integration context. Heavy bounded work goes to LUNA workers.**

Workers receive small, explicit task packets and return compact, verifiable results. AgentMaxxing does not maximize agent count; it minimizes duplicated context.

## Core model

```mermaid
flowchart LR
    U([User]) --> M["MAIN<br/>goal · decisions · integration"]
    M --> R{"Delegate?"}
    R -- No --> D[Work directly]
    R -- Yes --> P[Build bounded packet]
    P --> W1[LUNA]
    P --> W2[LUNA]
    P --> WN["LUNA …"]
    W1 --> H[Evidence handoff]
    W2 --> H
    WN --> H
    H --> G{"ACCEPT?"}
    G -- Yes --> M
    G -- No --> C[Targeted correction packet]
    C --> OW[Same owning LUNA]
    OW --> H
    D --> M
```

There is no fixed worker limit. Use another worker only when its work is genuinely independent and the context saved is worth the coordination cost.

Worker completion is not automatic acceptance. A dependent stage stays locked until the main agent explicitly accepts its prerequisite.

## Routing

| Work | Default route |
| --- | --- |
| Tiny or tightly coupled task | Main handles it directly |
| One heavy, bounded task | One LUNA worker |
| Independent heavy workstreams | Multiple LUNA workers |
| Sequential dependencies | Accept the prerequisite before starting the next stage |
| Security-sensitive or high-risk review | Add an independent reviewer only when justified |

Avoid overlapping write ownership, repeated repository discovery, and workers that receive the full conversation without a concrete need.

## Responsibilities

### Main agent

The main agent owns:

- user intent and constraints;
- architectural decisions;
- task decomposition and worker ownership;
- conflict detection;
- final integration and validation;
- explicit `ACCEPT` or `REJECT` decisions for delegated stages;
- the final answer.

### LUNA worker

A LUNA worker owns one bounded outcome. It should:

1. inspect only the required inputs;
2. complete the task within its scope;
3. run relevant validation;
4. self-review and correct every material issue it finds;
5. map concise evidence to each acceptance criterion;
6. return `ready-for-review` with a compact handoff.

Reasoning profile when available:

```text
model: gpt-5.6-luna
reasoning: xhigh | max
```

Use **xhigh** for bounded work with stable interfaces and direct validation. Use **max** for cross-system implementation, architecture-heavy work, UI/input/render interactions, nondeterministic failures, and expensive regressions. If xhigh repeatedly misses the same material requirement, reframe or split the task and send the smallest sufficient correction context to a fresh max worker.

## Worker packet

Before delegating, remove ambiguity. A useful packet looks like this:

```markdown
Role: LUNA worker

Reasoning:
xhigh | max

Goal:
<one concrete outcome>

Why delegated:
<heavy context or workload that should stay isolated>

Inputs:
- <exact files, directories, logs, commands, URLs, or artifacts>

Scope:
- May inspect: <...>
- May edit: <...>
- Must not edit: <...>

Suggested steps:
1. <first useful step>
2. <validation and self-review>

Constraints:
- <behavior, API, dependency, style, or permission boundary>

Done when:
- A1 — <measurable acceptance criterion>
- A2 — <measurable acceptance criterion>

Critical review surfaces:
- <integration boundary, risky behavior, or artifact the main should inspect>

Validation:
- <exact command or check>

Return only:
- status
- changed files
- 2–5 result bullets
- acceptance evidence for every criterion
- validation result
- self-review result
- material caveat or decision needed
```

See [worker packet guidance](.agents/skills/agentmaxxing/references/worker-packet.md) and [routing guidance](.agents/skills/agentmaxxing/references/routing.md) for edge cases.

## Compact handoff

Workers should return an integration index, not a transcript:

```text
STATUS: ready-for-review | needs-input | failed

CHANGED:
- <paths or none>

RESULT:
- <2–5 concise bullets>

ACCEPTANCE:
- A1 PASS/FAIL — <concise evidence>
- A2 PASS/FAIL — <concise evidence>

VALIDATION:
- PASS/FAIL/SKIPPED — <exact command or check>

SELF-REVIEW:
- <material issue corrected, or none>

CAVEAT / DECISION NEEDED:
- <only if material>
```

The main agent opens only the diffs or artifacts needed for integration.

## Acceptance and correction

The main agent checks changed paths, acceptance evidence, required validation, declared critical surfaces, and only the integration-sensitive diff or artifacts needed for a decision.

- **ACCEPT** when every required criterion has credible evidence and no material issue is ignored.
- **REJECT** when evidence is missing, validation is insufficient, scope drift exists, or a material defect remains.

On rejection, the main agent sends the same LUNA worker the failed acceptance IDs, observed evidence, behavior to preserve, correction scope, and exact recheck. LUNA returns a delta handoff and the main agent decides again. The loop continues until acceptance or a real authorization, user-decision, or external-state blocker. The main agent does not waive the criterion, silently repair the rejected delegated implementation, or unlock a dependent stage.

## Installation

The repo-scoped skill lives at:

```text
.agents/skills/agentmaxxing/
```

Install it with the Codex skill installer or copy that directory into a supported skills location. Invoke it explicitly:

```text
$agentmaxxing <your repository task>
```

Implicit invocation is disabled so ordinary small tasks do not change workflow unexpectedly.

## Repository

```text
AgentMaxxing/
├── .agents/skills/agentmaxxing/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── routing.md
│       └── worker-packet.md
├── docs/ARCHITECTURE.md
├── AGENTS.md
├── CHANGELOG.md
├── README.md
└── README_TR.md
```

AgentMaxxing is an instruction layer, not a runtime. It has no daemon, database, telemetry service, token ledger, or persistent task registry.

## VisionOffload

VisionOffload is intentionally not included yet. It will be developed separately and can later reuse the same context-isolation principles.

## License

Apache License 2.0. AgentMaxxing is an independent open-source project and is not affiliated with or endorsed by OpenAI.
