# Architecture

AgentMaxxing is intentionally a behavior layer rather than a runtime.

## Objective

Reduce unnecessary growth of the main agent context while preserving one clear integration owner.

## Components

### Main agent

Owns user intent, decomposition, architectural decisions, conflict detection, and final integration.

### Worker packet

A deliberately small context envelope that turns a broad request into an independently executable bounded task.

### LUNA worker

Consumes the packet, performs the heavy work in isolation, validates and self-reviews, then returns a compact handoff.

### Compact handoff

Contains status, changed paths, result summary, validation evidence, and only material caveats.

## Dynamic worker count

AgentMaxxing does not impose a fixed maximum worker count.

Worker count is an optimization decision:

```text
benefit = isolated heavy context + useful independent progress
cost    = duplicated context + coordination + conflicting ownership
```

Spawn another worker only when expected benefit is clearly higher than cost.

This usually means:

- 0 workers for tiny work;
- 1 worker for one bounded heavy task;
- N workers for N genuinely independent heavy workstreams.

## Context boundaries

The main agent should not automatically ingest the raw material each worker processed.

Workers should not receive the complete main conversation unless the task genuinely requires it.

The architecture minimizes context movement in both directions.

## Failure modes

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

Response: require self-test/self-review first; independent review only when justified.

### Main re-reading everything

Symptom: main opens every file/log after worker completion.

Response: use the handoff as an index and inspect only integration-critical artifacts.

## VisionOffload

Visual payload isolation is planned as a later integration. It is deliberately omitted from this revision so the general context-routing behavior can stabilize first.
