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

- acceptance criteria are satisfied;
- remaining work is small enough for main;
- coordination cost exceeds context saved;
- a user decision is required.
