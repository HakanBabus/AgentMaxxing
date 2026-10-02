# Routing

Plan the work before choosing agents. Single-agent execution is the default at every task size; staging and delegation are separate decisions.

## Choose direct work or delegation

| Situation | Route |
| --- | --- |
| Small change with context already loaded | Main completes and checks it |
| Small independent task worth isolating | Optional GPT-6.1 Sol low worker |
| Broader bounded implementation or investigation | Optional GPT-6.1 Sol medium worker |
| Tightly coupled architecture and implementation | Main works through accepted milestones |
| Independent research, log analysis, or implementation scopes | Optional parallel workers with effort chosen per task |
| Concrete risk or missing independent evidence | Optional read-only GPT-6.1 Sol reviewer |

Useful delegation isolates heavy intermediate material, makes independent progress, or brings an independent perspective to a specific uncertainty. A task being large, a worker being capable, or a deliverable being called final does not by itself justify more agents.

## Model and effort

All AgentMaxxing workers use **`gpt-6.1-sol`**. Set the model and effort explicitly in the client's supported spawn controls; do not rely on inheritance or a prose role label. This profile covers implementing workers, researchers, reviewers, and correction workers. Main keeps the user's selected session model and effort.

### Low

Use `low` for small tasks with clear inputs, stable interfaces, few decisions, and direct validation:

- a localized fix with a known reproduction;
- a repetitive edit or focused documentation update;
- a narrow code search or log summary;
- an independent check with known commands.

A small task still stays direct when the packet and integration would cost more than the execution.

### Medium

Use `medium` for broader bounded work with interacting requirements or meaningful uncertainty:

- an implementation spanning related files or interfaces;
- diagnosis that must compare multiple causes;
- a migration step or architecture proposal with explicit constraints;
- review that must trace behavior across components.

**Medium is the ceiling.** If low misses a material reasoning requirement, improve the packet and move to medium when justified. If medium stalls, improve the evidence, isolate a smaller reproduction, split at real boundaries, or let main resolve the coupled decision. Never exceed medium or switch to another model as an implicit fallback.

If GPT-6.1 Sol or the chosen effort is unavailable, main may continue directly within its existing settings. Disclose the worker-profile limitation and ask only if the user's requirements cannot otherwise be met.

## Compound tasks and stages

Consider subsystems, dependencies, migration steps, user flows, and validation surfaces rather than counting files. Use a compact stage map when independently verifiable milestones make completion clearer:

```text
S1 — define interface | depends: none | owner: main | check: approved contract
S2 — implement flow | depends: S1 accepted | owner: main | check: behavior tests
S3 — update examples | depends: S1 accepted | owner: optional GPT-6.1 Sol low | check: examples match contract
S4 — investigate migration | depends: S2 accepted | owner: optional GPT-6.1 Sol medium | check: migration cases
```

Only spawn optional owners after deciding delegation adds value. Keep transient stage ownership in working context. Persist future commitments and durable decisions in project memory, not every spawn, wait, or acceptance event.

## Concurrency and ownership

AgentMaxxing imposes no fixed worker count; the host's concurrency limits still apply. Parallel tasks need distinct outcomes, small input packets, non-overlapping write scopes, and independent validation. Avoid duplicate architecture discovery or concurrent edits to the same files.

Main owns shared project-memory writes. Workers return candidate memory notes in their handoffs. Use fresh workers when context materially differs; reuse a worker for useful continuation and corrections. Sequential stages can remain with main or one worker instead of spawning a fresh worker for each milestone.

Dependent work starts only after main accepts its delegated prerequisite. Keep dependent tasks sequential and pass only the accepted facts the next stage needs.

## Corrections and reviewers

Workers validate and self-review before returning. Main rejects missing evidence, material defects, and scope drift, then sends a targeted correction. Reuse the worker when its context is useful, or explicitly transfer write ownership to main for a smaller correction. Recheck the result and accept before proceeding.

Independent review is optional and needs a concrete reason: security or data-loss risk, costly rollback, unclear evidence, cross-stage behavior not covered by existing checks, or an explicit user request. Select low or medium by the actual review scope. Give the reviewer read-only ownership and a bounded question. Main assigns any defects to one correction owner.

Stop adding workers when coordination exceeds useful isolation or progress. This never permits leaving a known defect unaddressed or claiming an unmet criterion passed.
