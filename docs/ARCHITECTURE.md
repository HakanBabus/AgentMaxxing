# Architecture

AgentMaxxing is intentionally a behavior layer rather than a runtime.

## Objective

Reduce unnecessary growth of the main agent context while preserving one clear integration owner.

## Components

### Workload sizing gate

Classifies the request as tiny, bounded, or compound before worker packets are created. It considers systems, lifecycle phases, quality dimensions, environments, and validation methods rather than counting output files or directories.

### Stage map

Represents a compound deliverable as dependency-aware bounded outcomes. Each stage records ownership, effort, accepted prerequisites, scope, acceptance, validation, and work deliberately deferred to later stages. The map stays compact in main context and is not a persistent orchestration registry.

### Main agent

Owns user intent, decomposition, architectural decisions, conflict detection, acceptance decisions, and final integration. The role name remains model-neutral; AgentMaxxing does not depend on how the user started the main session.

### Worker packet

A deliberately small context envelope that turns a broad request into an independently executable bounded task.

### LUNA worker

Consumes the packet, performs the heavy work in isolation, validates and self-reviews, then returns a compact handoff. Workers use `xhigh` for bounded, directly verifiable work and `max` for complex or cross-system work.

### Compact handoff

Contains status, changed paths, acceptance evidence, validation evidence, and only material caveats.

### Acceptance gate

The main agent returns `ACCEPT` or `REJECT` for every delegated stage. Rejected work returns to LUNA with failed acceptance IDs, concrete evidence, a narrow correction scope, and an exact recheck. A dependent stage cannot start before its prerequisite is accepted.

```text
main packet → LUNA execute/self-review → ready-for-review
     ▲                                      │
     └──── targeted correction ← REJECT ────┤
                                            └── ACCEPT → integrate/unlock next stage
```

This loop preserves role separation: main reviews and integrates; LUNA implements and corrects. If a strategy stalls, main improves or splits the packet or escalates a fresh worker from `xhigh` to `max`; it does not lower the acceptance standard.

## Dynamic worker count

AgentMaxxing does not impose a fixed maximum worker count.

Worker count is an optimization decision:

```text
benefit = isolated heavy context + useful independent progress
cost    = duplicated context + coordination + conflicting ownership
```

LUNA's low marginal cost lowers the threshold for useful delegation. Spawn another worker when it creates a clearer ownership, context, execution, correction, or validation boundary. Avoid workers whose only effect is duplicated reading or conflicting ownership.

This usually means:

- 0 workers for tiny work;
- 1 worker for one bounded heavy task;
- several sequential workers for a compound dependency chain;
- parallel workers only for genuinely independent workstreams;
- a fresh read-only evaluator for broad end-to-end quality claims.

## Context boundaries

The main agent should not automatically ingest the raw material each worker processed.

Workers should not receive the complete main conversation unless the task genuinely requires it.

The architecture minimizes context movement in both directions.

## Failure modes

### Under-decomposition

Symptom: one worker receives a detailed end-to-end specification spanning several systems, lifecycle phases, quality dimensions, or validation methods.

Response: stop treating one output location as one bounded task. Build a stage map, keep corrections with each stage owner, and unlock dependent stages only after acceptance.

### Vague packet

Symptom: LUNA wanders, broadens scope, or returns generic work.

Response: improve goal, inputs, constraints, and acceptance criteria before adding more context.

### Artificial parallelism

Symptom: several workers read the same files and produce overlapping changes.

Response: merge the workstream or sequence dependencies.

### Second giant context

Symptom: one worker gets reused across many unrelated tasks.

Response: use fresh workers for new independent tasks.

### Reviewer multiplication

Symptom: every worker gets another worker just to review it.

Response: require self-test/self-review first. Use independent review for compound end-to-end quality or other cases where a fresh perspective has concrete evidence value, not mechanically for every bounded stage.

### Main re-reading everything

Symptom: main opens every file/log after worker completion.

Response: use the handoff as an index and inspect only integration-critical artifacts.

### Premature stage progression

Symptom: a dependent stage begins because a worker reported success even though a required behavior is unverified or defective.

Response: treat worker completion as `ready-for-review`; continue correction until main explicitly accepts the stage or a real authorization, user-decision, or external-state blocker is reached.

## VisionOffload

Visual payload isolation is planned as a later integration. It is deliberately omitted from this revision so the general context-routing behavior can stabilize first.
