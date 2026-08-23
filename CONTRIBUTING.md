# Contributing to AgentMaxxing

Thank you for helping build a smaller, more accountable multi-agent workflow.
The project is intentionally protocol-first; additions should solve an observed
workflow problem without creating a large memory or orchestration system.

## Before opening a change

For small documentation corrections, a pull request is enough. For new runtime
code, persistence formats, role changes, dependencies, or public interfaces,
open a proposal first and include:

- the concrete problem and a representative task;
- why the existing protocol is insufficient;
- the smallest proposed change;
- effects on context size, cost, validation, and permissions;
- alternatives considered and migration impact.

## Development workflow

1. Read `README.md` and `docs/architecture.md`.
2. Check `.agentmaxxing/decisions.md` for relevant constraints.
3. Scope one outcome with observable acceptance criteria.
4. Keep changes within one architectural concern.
5. Run relevant checks and review `git diff --check`.
6. Update documentation and context only when current truth changed.
7. Open a pull request using a clear, imperative title.

During Phase 1, validation is documentation-focused. Confirm that local Markdown
links resolve, role names are used consistently, examples follow the task
protocol, and no document contradicts the architecture invariants.

## Design requirements

Contributions must preserve:

- SOL's final accountability and single-writer project context;
- narrow specialist scopes and non-overlapping file ownership;
- exact validation evidence in result reports;
- model-independent role contracts;
- user approval boundaries across delegation;
- minimal persistence without transcripts or raw reasoning.

Avoid adding databases, telemetry, background services, or abstraction layers
without evidence that a simpler protocol or local module cannot solve the need.

## Commit and pull request quality

Use small commits that each leave the repository understandable. Prefer
imperative commit subjects such as `Add task envelope validation`. Do not mix
formatting sweeps with behavioral changes.

A pull request should state:

- what problem it solves;
- what changed and what intentionally did not;
- how it was validated;
- any remaining risk, follow-up, or durable decision.

## Updating persistent context

Do not use `.agentmaxxing/` as a changelog.

- Replace stale current facts in `state.md`.
- Add a decision only when it constrains future architecture or workflow.
- Keep `tasks/current.md` focused on the current integration task.
- Never commit prompts, transcripts, reasoning traces, secrets, or user data.

## Reporting bugs and security issues

Public issues should include a minimal reproduction, expected behavior, actual
behavior, and relevant environment information. Report vulnerabilities through
the private process described in `SECURITY.md`.

By participating, you agree to follow `CODE_OF_CONDUCT.md`.
