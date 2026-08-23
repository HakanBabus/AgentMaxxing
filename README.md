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

See [docs/architecture.md](docs/architecture.md) for boundaries, invariants,
and failure modes.

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
removes and how it preserves the minimal-context design.

Contribution instructions are added as part of the foundation milestone.

## License

Licensed under the [Apache License 2.0](LICENSE).

