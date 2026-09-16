---
name: agentmaxxing
description: Keep the main coding agent context small by sizing non-trivial work, decomposing compound deliverables into accepted stages, and routing bounded execution to well-scoped LUNA workers. Use when the user explicitly invokes $agentmaxxing or explicitly asks to use AgentMaxxing. Keep tiny work direct; use sequential or parallel LUNA workers according to dependencies, ownership, and validation boundaries.
---

# AgentMaxxing

Operate as the main orchestrator. Preserve the user's actual goal, key project constraints, and final integration responsibility while keeping heavy intermediate context out of the main session when practical.

AgentMaxxing is context-first, not agent-count-first.

## Core rules

1. **Size before routing.** Decide whether the request is tiny, one bounded outcome, or a compound deliverable before creating a worker packet.
2. **Do tiny work directly.** Delegation still has coordination cost.
3. **Decompose compound work.** Turn broad outcomes into a dependency-aware stage map with measurable acceptance gates.
4. **Delegate bounded execution.** Logs, broad exploration, focused implementation, tests, research, polish, and other isolated work can stay inside workers.
5. **Use LUNA workers.** Use `gpt-5.6-luna` with either `xhigh` or `max` reasoning according to task complexity.
6. **No arbitrary worker cap.** LUNA's low marginal cost lowers the threshold for useful delegation; ownership clarity, context duplication, and validation boundaries determine worker count.
7. **Resolve ambiguity before delegation.** LUNA should receive a precise task packet, not a vague goal or an entire product specification disguised as one task.
8. **Worker self-check first.** The worker that performs a bounded task should test and review its own result before main review or another reviewer is considered.
9. **Gate every delegated stage.** The main agent must explicitly accept a delegated result before integration or any dependent stage begins.
10. **Reject back to LUNA.** When the main agent rejects a result, return a targeted correction packet to LUNA; do not silently skip the issue or take over the delegated implementation merely to avoid another worker pass.
11. **Return compact handoffs.** Do not bring raw logs, full transcripts, giant analyses, or unrelated exploration back into main context.
12. **Main owns integration.** Delegation transfers bounded execution, not accountability.

## Decide whether to delegate

Work directly when the task is tiny, tightly coupled to context already loaded by the main agent, and cheaper to finish than to explain to a worker.

Delegate when one or more of these are true:

- the task requires reading or searching a large amount of material;
- raw logs, test output, or build output would pollute main context;
- implementation is bounded and acceptance criteria can be stated clearly;
- several independent workstreams can progress without sharing write ownership;
- research or repository exploration can be summarized into a compact result;
- the main agent needs isolation more than it needs every intermediate detail.

Because LUNA workers are inexpensive, prefer a useful bounded delegation over keeping substantial execution in the main context. Do not create duplicate workers without distinct ownership or evidence value.

## Size and decompose the work

Do not infer task size from the number of requested output folders, repositories, files, or final artifacts. One output can still contain many architectural, implementation, quality, and validation stages.

Treat a request as compound when several of these are present:

- multiple subsystems, packages, surfaces, audiences, or deliverable types;
- discovery, architecture, implementation, content, migration, polish, and validation mixed together;
- several user flows, platforms, environments, or operating modes;
- both objective correctness and subjective quality requirements;
- a greenfield or end-to-end result described as complete, production-ready, polished, final, or equivalent;
- acceptance that requires materially different test or review methods;
- enough work that one worker would need several internal milestones before it could prove the result.

Before delegating compound work, create a compact stage map. Each stage must have:

- one bounded outcome;
- dependencies and accepted inputs;
- worker ownership and `xhigh` or `max` effort;
- non-overlapping write scope while active;
- measurable acceptance and validation;
- an explicit statement of what belongs to later stages.

The stage map is orchestration state in the main context, not a persistent task database. Read [references/routing.md](references/routing.md) for sizing and decomposition rules.

## Multiple workers

There is no fixed worker limit.

Use multiple workers across a compound task even when its stages are sequential. Independence is required for parallel execution, not for assigning later accepted stages to fresh workers.

Before spawning workers concurrently, verify that their tasks are meaningfully independent. Prefer parallel workers when they can operate with different inputs or non-overlapping write scopes.

Avoid:

- assigning the same file to multiple active writers;
- asking several workers to rediscover the same architecture;
- opening a reviewer before the implementing worker has tested and self-reviewed;
- splitting one tightly coupled change into artificial parallel fragments;
- spawning workers whose combined task packets duplicate more context than they isolate.

If task B depends on task A, keep them sequential or resume the appropriate worker when supported.

Do not start task B until the main agent has explicitly accepted task A. A successful worker status is a review request, not automatic acceptance.

A new stage should normally receive a fresh worker when its goal, context, or validation surface materially differs from the accepted prerequisite. Resume the same worker for corrections and true continuation inside one bounded stage.

## Build a strong LUNA packet

Before delegating, read [references/worker-packet.md](references/worker-packet.md).

Every non-trivial packet should make these explicit:

- **Goal** — one concrete outcome.
- **Why delegated** — what context or workload should remain isolated.
- **Inputs** — exact files, directories, logs, commands, URLs, or artifacts that matter.
- **Scope** — what the worker may inspect or change.
- **Suggested steps** — a short execution path when useful.
- **Constraints** — behavior, APIs, dependencies, styles, or files that must remain unchanged.
- **Done when** — measurable acceptance criteria.
- **Validation** — exact checks or tests when known.
- **Return only** — the compact handoff format.

Do not send the full conversation, full repository dumps, unrelated files, or broad historical context unless the worker cannot complete the task without them.

When LUNA struggles, first improve the packet: narrow the goal, add the missing local fact, give a concrete validation command, or split a genuinely overloaded task. Do not automatically flood it with more context.

## Choose LUNA reasoning effort

Use only `xhigh` or `max` for AgentMaxxing workers when both are available.

- Choose `xhigh` for well-bounded work with stable interfaces, explicit acceptance criteria, and reliable validation.
- Choose `max` for cross-system implementation, architecture-heavy work, UI/input/render interactions, nondeterministic failures, expensive regressions, or tasks whose quality cannot be captured by one automated test.
- Prefer `max` at the start of an obviously difficult task instead of expecting an underpowered pass to fail.
- If an `xhigh` worker repeatedly misses the same material requirement, reframe or split the task and send the smallest sufficient correction context to a fresh `max` LUNA worker.

Read [references/routing.md](references/routing.md) for the detailed routing and escalation rules.

## Worker execution contract

Ask the worker to:

1. inspect the bounded inputs;
2. perform the task;
3. run the relevant validation;
4. self-review its own diff/result once;
5. correct every material issue it finds within the authorized scope;
6. verify again after corrections;
7. map evidence to each acceptance criterion;
8. return only the compact handoff as `ready-for-review`.

The worker must not mark a stage ready while a required criterion is knowingly unmet. If completion requires user input, new authorization, unavailable external state, or a materially different scope, return `needs-input` with the exact blocker.

For a single bounded stage, a separate reviewer remains optional. For a compound deliverable that claims end-to-end, final, polished, production-ready, migration-complete, or similarly broad quality, normally use a fresh LUNA evaluator for independent final validation. Give it a bounded evaluation packet and no write ownership; return defects to the owning implementation stage.

## Compact handoff

Workers should return only information the main agent needs to integrate:

```text
STATUS: ready-for-review | needs-input | failed

CHANGED:
- <paths or none>

RESULT:
- <2-5 concise bullets>

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

Do not request chain-of-thought, full work logs, raw test floods, or verbose narration.

Treat the handoff as a navigation index. Open a targeted diff, file, or artifact only when integration, risk, or uncertainty requires it. Do not automatically reread everything the worker already processed.

## Main-agent acceptance gate

For every delegated stage, the main agent must issue one of two decisions:

- **ACCEPT** — every required acceptance criterion has credible evidence, validation is proportionate to risk, changes remain in scope, and no material issue is being ignored.
- **REJECT** — at least one criterion lacks evidence, validation is insufficient, scope drift exists, or a material defect remains.

Review economically. Check the changed-path list, criterion-to-evidence mapping, required validation, declared critical review surfaces, and only the integration-sensitive diff or artifacts needed to decide. Expand review when evidence is inconsistent, tests fail or are skipped, unexpected files changed, or risk is high. Do not reproduce the worker's entire investigation by default.

On rejection:

1. identify the failed acceptance IDs and concrete evidence;
2. state what already-passing behavior must remain unchanged;
3. give the exact correction scope and required recheck;
4. return the correction to the same LUNA worker when the bounded task and context remain valid;
5. require a delta handoff and decide again.

Continue the correction cycle until the stage is accepted or a real authorization, user-decision, or external-state blocker is reached. Never lower acceptance criteria, call an unaccepted stage complete, or advance a dependent stage. If the same approach stalls, improve the packet, split the stage along a real boundary, or escalate from `xhigh` to a fresh `max` LUNA worker rather than repeating an unchanged instruction.

## Main-agent integration

The main agent should maintain:

- the user's goal;
- high-level constraints and architecture relevant to the task;
- task decomposition and worker ownership;
- compact worker results;
- only the diffs or artifacts required for final integration.

The main agent is responsible for detecting conflicts between handoffs and deciding whether additional validation is necessary.

Once implementation is delegated, the main agent keeps review and integration ownership while LUNA keeps implementation and correction ownership for that bounded stage. The main agent should not rewrite rejected worker code itself merely to save a delegation round.

Do not maintain a persistent task database, transcript archive, or context registry merely for AgentMaxxing. Prefer the repository's existing project documentation and source of truth. Add persistent orchestration files only when the user explicitly wants them or the project has a concrete need.

## Routing reference

For edge cases around direct work, single-worker delegation, parallel delegation, sequential dependencies, and reviewer use, read [references/routing.md](references/routing.md).

## Visual work

VisionOffload is intentionally outside this revision. Do not invent a visual worker protocol here. When VisionOffload is later integrated, it should reuse the same principles: minimum task context, isolated heavy payload, worker self-review, and compact handoff.

## Permissions

Delegation never expands the user's authorization. Workers inherit the same constraints as the main agent and must stop at destructive, external, costly, or scope-expanding boundaries that were not authorized.

Keep orchestration mechanics brief in the user-facing response unless the user asks for details.
