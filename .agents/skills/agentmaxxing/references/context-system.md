# Minimal Context System

Read this reference only when initializing or updating `.agentmaxxing/`.

## Structure

```text
.agentmaxxing/
├── state.md
├── decisions.md
└── tasks/
    └── current.md
```

SOL is the sole logical writer. Specialists may recommend context changes in a
result report but must not update these files themselves.

## `state.md`

Store current truth, not history:

```markdown
# Project State

## Project
<name>

## Current goal
<one current outcome>

## Completed
- <relevant capability or milestone>

## Working
- <current work or None>

## Blocked
- <active blocker or None>

## Next
- <next likely action>
```

Replace stale statements. Do not append activity logs, completed-task reports,
or conversations.

## `decisions.md`

Record only choices that constrain future architecture or workflow:

```markdown
# Architectural Decisions

## D-001 — <decision title>

**Status:** Accepted
**Date:** YYYY-MM-DD

**Decision:** <what was selected>

**Reason:** <why it was selected>

**Consequences:** <future constraints and tradeoffs>
```

Do not record routine implementation choices, formatting preferences, progress,
or easily reversible local decisions.

## `tasks/current.md`

Keep one active integration task:

```markdown
# Current Task

## Status
<Scoped | Assigned | Executing | Reported | Validated | Completed | Needs input>

## Goal
<one measurable outcome>

## Owner
SOL

## Affected paths
- <path or analysis boundary>

## Requirements
- <required behavior>

## Constraints
- <must preserve or approval boundary>

## Acceptance criteria
- <observable check>

## Progress
- [ ] <meaningful milestone>

## Decisions needed
None.
```

Complete, clear, or replace this file after integration. Do not use it as a
multi-task backlog.

## Initialization and updates

Initialize the three files with facts established from the user request and
repository evidence. Mark unknown facts as unknown rather than inventing them.

Update persistent context only after SOL validates the integrated result. Never
persist secrets, personal data, full prompts, raw reasoning, specialist
transcripts, token-by-token usage, or routine command output.
