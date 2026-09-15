# Routing

AgentMaxxing routes for context efficiency, not agent count.

## Direct work

Prefer main-agent execution when:

- the change is tiny;
- the main already has the relevant files loaded;
- explaining the task would cost more than doing it;
- the work is mostly a high-level decision the main must own anyway.

## One worker

Prefer one LUNA worker when:

- a bounded implementation has stable requirements;
- one log/test/research surface is heavy;
- repository exploration can be isolated and summarized;
- the worker can complete, test, and self-review one coherent outcome.

## Reasoning effort

Use `gpt-5.6-luna` with one of two reasoning levels:

### `xhigh`

Use for bounded implementation, focused investigation, tests, refactors, and repetitive edits when interfaces are stable and success can be proven directly.

### `max`

Use for cross-system work, consequential architecture, UI/input/render interactions, nondeterministic behavior, expensive regressions, or broad tasks that first need careful decomposition.

Choose the effort before spawning the worker. If an `xhigh` pass repeatedly misses the same material requirement, do not keep replaying the same packet. Reframe or split the task and give a fresh `max` worker only the compact facts and failed acceptance evidence it needs.

## Multiple workers

Use multiple workers when workstreams are genuinely independent.

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

Do not open a reviewer by default.

The implementing worker must first test and self-review.

Independent review can be justified by:

- security-sensitive changes;
- data-loss risk;
- architecture with expensive rollback;
- unclear or suspicious test results;
- explicit user request.

Give the reviewer a bounded review question, not the entire project history.

## Stop rule

Stop delegating when:

- the main agent has accepted the stage because its acceptance criteria are satisfied;
- remaining work is small enough for main;
- coordination cost exceeds context saved;
- a user decision is required.

The coordination-cost rule applies before delegation or between independent stages. It must not be used to skip correction of an already-delegated, rejected stage.
