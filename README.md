# AgentMaxxing

**Cost-efficient multi-agent orchestration workflow for Codex.**

> Status: Phase 1 — foundation and workflow design. No runtime or CLI is
> published yet.

AgentMaxxing is a small, explicit protocol for running AI coding work like a
focused development team. A primary agent keeps the goal and project state,
then delegates only the work that benefits from a specialist.

The guiding principle is simple:

> Use the right agent for the right task.

## Why AgentMaxxing?

Long AI coding sessions often accumulate repository dumps, repeated analysis,
stale decisions, and unrelated implementation details. That context makes work
slower and more expensive without making it better.

AgentMaxxing addresses this with three constraints:

- persist only the current state, important decisions, and active task;
- delegate narrow work with explicit acceptance criteria;
- return compressed, evidence-bearing reports instead of transcripts.

It deliberately avoids vector databases, conversation archives, and large
project wikis.

## Roles

| Role | Purpose | Typical work |
| --- | --- | --- |
| **SOL** | Orchestrator and final owner | Clarify goals, plan, route, integrate, review |
| **LUNA** | Focused implementation worker | Code, refactor, test, and bounded repetitive work |
| **TERRA** | Reviewer and critical analyst | Architecture review, debugging analysis, security thinking |

The role names describe responsibilities, not a permanent model lock. A runtime
may map them to suitable models and reasoning levels based on capability, cost,
and measured results.

## How it works

```text
User request
    |
    v
SOL loads minimal project state
    |
    +-- solve directly when delegation adds no value
    |
    +-- send a bounded implementation task to LUNA
    |
    +-- request challenge or analysis from TERRA
    |
    v
SOL validates and integrates a compressed report
    |
    v
Update only durable project context
```

Persistent context stays intentionally small:

```text
.agentmaxxing/
├── state.md
├── decisions.md
└── tasks/
    └── current.md
```

## Example delegation

```markdown
Role: LUNA
Goal: Correct refresh-token expiry validation.
Scope: src/auth/token.ts, tests/auth/token.test.ts
Requirements:
- Keep the public API unchanged.
- Add tests for expired and valid tokens.
Constraints:
- Do not change session storage.
Acceptance:
- Targeted tests pass.
- Report the exact validation command.
```

The worker returns a short handoff:

```markdown
Changed:
- src/auth/token.ts
- tests/auth/token.test.ts

Fixed:
- Expired refresh tokens are rejected before rotation.

Tests:
- PASS — npm test -- tests/auth/token.test.ts

Remaining:
- None.
```

## Architecture

AgentMaxxing separates orchestration, execution, review, and persistence. SOL is
the only component responsible for user-facing integration and durable context;
workers receive the smallest sufficient task context and do not write project
memory independently.

Core documentation:

- [Architecture](docs/architecture.md) — boundaries, invariants, and failure
  modes.
- [Task protocol](docs/task-protocol.md) — task envelopes, result reports, and
  lifecycle.
- [Agent workflow](docs/workflow.md) — routing, execution, integration, and
  measurement.

## Start using the workflow

1. Copy the `.agentmaxxing/` directory and `AGENTS.md` into a repository.
2. Replace the example project state and active task with current truth.
3. Keep SOL as the integration owner and delegate only bounded tasks.
4. Use the task and result formats in the task protocol.
5. Review and validate every specialist result before updating project state.

This manual workflow is the Phase 1 reference implementation. Future tooling
will automate it without changing its ownership and context guarantees.

## Roadmap

- **Phase 1 — Foundation:** repository structure, documentation, context
  templates, and workflow contracts.
- **Phase 2 — Core system:** task manager, state manager, context loader, and
  machine-readable agent messages.
- **Phase 3 — Routing:** evidence-based SOL/LUNA/TERRA selection and delegation
  rules.
- **Phase 4 — Optimization:** token budgets, context compression, and routing
  evaluation.

Progress between phases is acceptance-driven. A later phase starts only after
the preceding contracts have been exercised on representative tasks.

## Project principles

- **Minimal by default:** every persistent field must justify its context cost.
- **Explicit ownership:** one agent owns each file change at a time.
- **Evidence over claims:** validation reports include commands and outcomes.
- **Replaceable models:** workflow roles survive changes in model availability.
- **Human control:** external, destructive, or scope-expanding actions require
  an explicit approval boundary.

## Contributing

Phase 1 is focused on the protocol and its invariants. Before proposing an
automation layer, open a discussion that explains which manual failure it
removes and how it preserves the minimal-context design. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md). Security concerns
should use the private process in [SECURITY.md](SECURITY.md), not a public issue.

## License

Licensed under the [Apache License 2.0](LICENSE).

AgentMaxxing is an independent open-source project and is not affiliated with
or endorsed by OpenAI.
