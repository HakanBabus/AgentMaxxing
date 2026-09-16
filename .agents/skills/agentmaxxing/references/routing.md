# Routing

AgentMaxxing sizes work before routing. Worker count follows real execution and validation boundaries, not a desire to minimize or maximize agent count.

## Workload sizing gate

Classify the request before creating worker packets:

### Tiny

One obvious change, little new context, and one direct check. Main can usually handle it.

### Bounded

One primary outcome, one coherent ownership surface, stable inputs, and a validation method that can prove completion. Use one worker when delegation keeps useful context out of main.

### Compound

Several systems, phases, quality dimensions, environments, deliverable types, or validation methods contribute to the requested result. Create a stage map and use multiple workers across its lifecycle.

A task is not bounded merely because it targets one repository, directory, document, or artifact. A detailed requirements list can still be an overloaded packet.

Strong compound-work signals include:

- discovery plus implementation;
- architecture plus several implementation surfaces;
- correctness plus design, content, usability, performance, or polish;
- multiple platforms, user flows, migrations, or operating modes;
- a greenfield or end-to-end final deliverable;
- validation that needs different tools or an independent perspective.

When uncertain between bounded and compound, sketch the stage map first. If several independently acceptable milestones appear, route them as stages rather than hiding them inside one worker.

## Stage map

Keep the map compact:

```text
S1 — outcome | depends on: none | owner: LUNA max | acceptance: A1-A3
S2 — outcome | depends on: S1 ACCEPT | owner: fresh LUNA max | acceptance: A4-A6
S3 — outcome | depends on: S1 ACCEPT | owner: LUNA xhigh | acceptance: A7-A8
F1 — end-to-end evaluation | depends on: all ACCEPT | owner: fresh LUNA | read-only
```

Do not persist this map unless the user or project has a concrete need for it.

## Direct work

Prefer main-agent execution when:

- the change is tiny;
- the main already has the relevant files loaded;
- explaining the task would cost more than doing it;
- the work is mostly a high-level decision the main must own anyway.

## One worker

Prefer one LUNA worker when:

- the request passed the workload sizing gate as bounded;
- a bounded implementation has stable requirements;
- one log/test/research surface is heavy;
- repository exploration can be isolated and summarized;
- the worker can complete, test, and self-review one coherent outcome.

Do not use one worker for a compound request merely because its requirements are detailed or all outputs live in one place.

## Reasoning effort

Use `gpt-5.6-luna` with one of two reasoning levels:

### `xhigh`

Use for bounded implementation, focused investigation, tests, refactors, and repetitive edits when interfaces are stable and success can be proven directly.

### `max`

Use for cross-system work, consequential architecture, UI/input/render interactions, nondeterministic behavior, expensive regressions, or broad tasks that first need careful decomposition.

Choose the effort before spawning the worker. If an `xhigh` pass repeatedly misses the same material requirement, do not keep replaying the same packet. Reframe or split the task and give a fresh `max` worker only the compact facts and failed acceptance evidence it needs.

## Multiple workers

Use multiple workers across compound work. They may be sequential or parallel.

Use sequential workers when later stages depend on accepted earlier results. Use parallel workers only when workstreams are genuinely independent.

Good boundaries include:

- separate packages or modules with no shared write ownership;
- implementation and unrelated external research;
- independent failing test groups;
- separate migration targets with stable interfaces.

Before parallelizing, check:

- Does each worker have a distinct goal?
- Can each worker receive a small packet?
- Are write scopes non-overlapping?
- Can they validate independently?
- Will their combined output be easy for main to integrate?

If not, keep the work sequential.

## Sequential dependencies

If worker B needs worker A's result, do not pretend they are parallel.

Options:

1. A completes → main integrates/condenses → B receives only the necessary result.
2. Resume the same worker when the task is truly a continuation and environment support makes that cheaper.

Task A must pass the main-agent acceptance gate before task B begins. Worker completion alone does not unlock a dependent stage.

## Acceptance and correction

The implementing worker returns `ready-for-review`; the main agent returns `ACCEPT` or `REJECT`.

On `REJECT`, send the same worker a compact correction packet containing:

- failed acceptance IDs;
- concrete observed evidence;
- already-passing behavior that must be preserved;
- allowed correction scope;
- the exact recheck required.

Require a delta handoff after correction. Keep returning material defects to LUNA until accepted. Do not let the main agent silently repair rejected delegated implementation, waive a criterion, or move to a dependent stage.

If correction stalls, change the strategy rather than the standard: improve the packet, split a genuinely overloaded stage, or escalate an `xhigh` attempt to a fresh `max` LUNA worker. Stop only for acceptance or a real authorization, user-decision, or external-state blocker.

## Reviewer worker

The implementing worker must first test and self-review.

Independent review is optional for one bounded stage. It is normally expected for a compound deliverable that claims broad end-to-end or final quality, and can also be justified by:

- security-sensitive changes;
- data-loss risk;
- architecture with expensive rollback;
- unclear or suspicious test results;
- results whose quality spans different validation methods or needs an independent perspective;
- explicit user request.

Give the evaluator accepted-stage summaries, end-to-end criteria, exact commands or artifacts, and a bounded review question rather than the entire project history. It should not edit. Return defects to the worker that owns the affected stage.

## Stop rule

Stop delegating when:

- the main agent has accepted the stage because its acceptance criteria are satisfied;
- remaining work is small enough for main;
- coordination cost exceeds context saved;
- a user decision is required.

The coordination-cost rule applies before delegation or between independent stages. It must not be used to skip correction of an already-delegated, rejected stage.
