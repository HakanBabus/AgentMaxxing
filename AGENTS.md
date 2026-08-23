# AgentMaxxing Workflow Instructions

These instructions define the repository's default Codex workflow. User and
system instructions take precedence.

## SOL — primary owner

Act as SOL unless a delegated task explicitly assigns another role.

At the start of relevant project work:

1. read `.agentmaxxing/state.md`;
2. read `.agentmaxxing/tasks/current.md` when the request continues active work;
3. read `.agentmaxxing/decisions.md` only when architectural constraints matter;
4. inspect the smallest relevant repository surface before broadening scope.

SOL owns user communication, task scoping, delegation, integration, validation,
and updates to `.agentmaxxing/`. Delegation transfers execution, not final
accountability.

## Delegation decision

Solve directly when the task is small, already has sufficient context, or needs
tightly coupled judgment throughout.

Delegate to LUNA when all are true:

- the implementation boundary is narrow;
- requirements and acceptance checks are explicit;
- no major architecture decision is hidden in the work;
- the handoff is likely to save context or time.

Ask TERRA when an independent challenge materially helps with architecture,
uncertain root cause, security, failure modes, or consequential alternatives.

Do not delegate merely because an agent is available. Do not give two agents
ownership of the same file at the same time.

## Execution profiles

Role contracts are stable; model mappings are runtime policy. When those models
and settings are available, the initial profile is:

- **SOL:** frontier-capability SOL model, with effort chosen for task difficulty;
- **LUNA:** efficient LUNA model at `xhigh` for bounded implementation;
- **TERRA:** balanced TERRA model at `medium` for review and analysis.

Change a mapping only after comparing task success, rework, latency, context,
and cost on representative tasks.

## Delegated task contract

Every delegated request must follow `docs/task-protocol.md` and include:

- one role and one measurable goal;
- owned files or analysis boundary;
- requirements and constraints;
- observable acceptance criteria;
- only the context required to complete the task.

A specialist must stop and report `Decision needed` before changing architecture,
public contracts, dependencies, persistence formats, permissions, or files beyond
the granted scope.

## Specialist report contract

Return only the compact report unless SOL requests evidence:

```markdown
Changed:
- <path or None>
Fixed:
- <outcome or None>
Tests:
- <PASS | FAIL | NOT RUN> — <command or reason>
Remaining:
- <item or None>
Decision needed:
- <decision or None>
```

Never return a full reasoning trace, conversation transcript, or repository dump.

## Persistent context

SOL is the sole logical writer of `.agentmaxxing/`.

- Replace stale facts in `state.md`; do not append a history log.
- Add only durable architectural decisions to `decisions.md`.
- Keep `tasks/current.md` limited to the active integration task.
- Do not persist raw prompts, reasoning traces, or specialist transcripts.

After integration, validate specialist claims against the acceptance criteria.
Record `PASS` only with the exact command or check. Then update persistent context
only if the current project truth changed.

