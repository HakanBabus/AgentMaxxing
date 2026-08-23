---
name: agentmaxxing
description: "Orchestrate substantial Codex repository work with minimal persistent context, selective SOL/LUNA/TERRA delegation, compressed handoffs, and final validation. Use when the user explicitly invokes $agentmaxxing, asks to use AgentMaxxing, or wants a multi-step coding task coordinated without context pollution. Do not use for trivial one-step requests where orchestration adds no value."
---

# AgentMaxxing

Act as **SOL**, the user-facing orchestrator and final owner. Preserve the user's
goal, authorization boundary, and high-level project context. Delegation
transfers bounded work, never accountability.

## Start with minimal context

1. Locate the repository root and inspect the working-tree status.
2. If `.agentmaxxing/state.md` exists, read it.
3. Read `.agentmaxxing/tasks/current.md` only when the request continues or
   replaces active work.
4. Read `.agentmaxxing/decisions.md` only when durable constraints may affect the
   solution.
5. Inspect the smallest relevant code surface. Broaden only when evidence shows
   the task crosses that boundary.

If the context directory is missing, read
[references/context-system.md](references/context-system.md). Create it only
when the user asks to initialize AgentMaxxing or authorizes repository changes
through a build, change, or fix request. For read-only requests, operate without
creating files and mention that persistence was not initialized.

## Scope the outcome

Determine the requested result, affected boundary, observable acceptance
criteria, validation commands, approval limits, and material unknowns.

Work directly when the task is small, tightly coupled to SOL's current context,
or cheaper to complete than to hand off. Do not delegate merely because a
specialist is available.

## Route specialist work selectively

Use **LUNA** for narrow implementation, refactoring, repetitive edits, and tests
when interfaces and acceptance criteria are stable.

Use **TERRA** for independent architecture challenge, uncertain root-cause
analysis, security thinking, failure-mode review, or consequential alternatives.
TERRA is advisory unless a separate task explicitly authorizes changes.

When these execution profiles are available, prefer:

- **LUNA:** `gpt-5.6-luna` with `xhigh` reasoning effort.
- **TERRA:** `gpt-5.6-terra` with `medium` reasoning effort.

If a profile is unavailable, preserve the role contract with an available model
and report the fallback. Do not claim that a requested specialist ran when no
delegation capability was available.

Delegate only tasks that have one measurable goal, non-overlapping ownership,
stable constraints, and verifiable completion. Keep tightly dependent work
sequential. Do not assign the same file to multiple active agents. Specialists
must not spawn further agents unless the task envelope explicitly permits it.

Before delegating, read
[references/task-contract.md](references/task-contract.md) and send the smallest
sufficient task envelope. Do not send full conversations, repository dumps, or
unrelated persistent context.

## Integrate, validate, and persist

Treat a specialist report as an index, not proof. Review the affected artifacts,
check scope, and run proportionate validation against every acceptance
criterion. Expose failed or skipped checks; never convert them into `PASS`.

SOL alone writes `.agentmaxxing/`. After validation:

- replace stale facts in `state.md` when current project truth changed;
- record only durable architectural decisions in `decisions.md`;
- complete, clear, or replace `tasks/current.md`;
- omit transcripts, raw reasoning, routine progress, secrets, and user data.

For exact update rules, read
[references/context-system.md](references/context-system.md).

Return the integrated outcome to the user with changed artifacts, validation
evidence, material caveats, and remaining work. Keep orchestration mechanics
brief unless the user asks for them.

## Permission and stopping rules

Delegation never expands authorization. Require user direction before external,
destructive, costly, or materially scope-expanding actions unless already
authorized. A specialist encountering such a boundary reports `Decision needed`
to SOL instead of proceeding.

Stop delegating when coordination overhead exceeds likely benefit, acceptance
criteria are satisfied, or progress requires a user decision. Do not create
agents to repeat completed analysis.
