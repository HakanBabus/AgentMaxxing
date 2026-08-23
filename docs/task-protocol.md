# Task Protocol

## Purpose

The task protocol is the smallest complete handoff between SOL and a specialist.
It prevents a delegated agent from reconstructing the entire project context or
guessing what completion means.

Phase 1 uses Markdown. A machine-readable representation may be introduced in
Phase 2 only if it preserves the same fields and semantics.

## Task envelope

A task is ready to assign only when the following fields are known.

| Field | Required | Meaning |
| --- | --- | --- |
| `Role` | Yes | One accountable recipient: SOL, LUNA, or TERRA |
| `Goal` | Yes | One outcome stated as a result, not a broad theme |
| `Scope` | Yes | Owned files, directories, or analysis boundary |
| `Requirements` | Yes | Behaviors or evidence the result must include |
| `Constraints` | Yes | APIs, permissions, or areas that must not change |
| `Acceptance` | Yes | Observable checks that define completion |
| `Context` | Optional | Only non-obvious facts needed to avoid rediscovery |

Template:

```markdown
Role: <SOL | LUNA | TERRA>
Goal: <single measurable outcome>
Scope:
- <owned path or analysis boundary>
Requirements:
- <required behavior or evidence>
Constraints:
- <must preserve, must not change, approval boundary>
Acceptance:
- <observable check>
Context:
- <small project fact the assignee cannot cheaply discover>
```

### Readiness rules

SOL does not assign a task when:

- the goal contains unrelated outcomes;
- acceptance depends only on an agent saying it is complete;
- file ownership overlaps another active assignment;
- a major architectural choice is hidden inside an implementation task;
- the necessary action exceeds the user's approval boundary.

SOL either narrows the envelope, requests TERRA analysis, or asks the user for a
material missing decision.

## Role-specific additions

### LUNA task

A LUNA envelope should name the implementation surface and test expectation.
LUNA may discover adjacent details, but must report before changing public APIs,
architecture, persistence formats, dependencies, or out-of-scope files.

```markdown
Role: LUNA
Goal: Reject expired refresh tokens before rotation.
Scope:
- src/auth/token.ts
- tests/auth/token.test.ts
Requirements:
- Cover valid and expired tokens.
Constraints:
- Preserve the public API and session storage behavior.
Acceptance:
- Targeted tests pass.
- Existing auth tests remain green.
```

### TERRA task

A TERRA envelope should name the proposal, evidence, or failure boundary being
reviewed. It should request ranked findings and concrete mitigations rather than
an unbounded opinion.

```markdown
Role: TERRA
Goal: Identify the highest-risk failure modes in the token rotation proposal.
Scope:
- docs/proposals/token-rotation.md
- src/auth/token.ts
Requirements:
- Rank findings by impact and likelihood.
- Cite the relevant file or proposal section.
Constraints:
- Analysis only; do not modify files.
Acceptance:
- Each reportable finding includes a specific mitigation.
```

## Result report

Specialists return outcomes, evidence, and unresolved work—not a reasoning log.

```markdown
Changed:
- <path, artifact, or None>

Fixed:
- <observable outcome or None>

Tests:
- <PASS | FAIL | NOT RUN> — <exact command or reason>

Remaining:
- <follow-up, blocker, or None>

Decision needed:
- <material decision for SOL or None>
```

### Report rules

- `Changed` lists only actual changes or analysis artifacts.
- `Fixed` describes behavior, not activity such as “updated code.”
- `Tests` never says only `PASS`; it includes the command or verification.
- `NOT RUN` is valid when the reason is explicit.
- `Remaining` exposes incomplete scope, failing checks, and discovered risk.
- `Decision needed` is used instead of silently choosing outside the envelope.

Reports should normally fit within 15 lines. A finding may include a short
evidence block when SOL cannot validate it from the summary alone.

## Lifecycle and transitions

| Current status | Allowed next status | Owner of transition |
| --- | --- | --- |
| Requested | Scoped | SOL |
| Scoped | Assigned | SOL |
| Assigned | Executing, Needs input | Assignee |
| Executing | Reported, Needs input | Assignee |
| Needs input | Scoped, Assigned, Cancelled | SOL |
| Reported | Validated, Assigned | SOL |
| Validated | Completed, Assigned | SOL |

`Assigned` after a report means SOL has issued a corrected or follow-up envelope;
it does not mean the specialist may expand the original task independently.

## Validation and completion

SOL reviews the diff or analysis evidence, runs proportionate checks, and
compares the result against every acceptance criterion. A specialist's passing
report is input to validation, not proof of completion.

After successful validation, SOL:

1. updates `.agentmaxxing/state.md` if the project state changed;
2. records a decision only when it has durable architectural consequences;
3. marks or replaces `.agentmaxxing/tasks/current.md`;
4. gives the user the integrated result and material caveats.

## Concurrency

Independent tasks may run concurrently only when their owned paths and outputs
do not overlap. If two tasks share a dependency, SOL must define ordering or a
specific artifact handoff. Parallelism is an optimization, not a default.
