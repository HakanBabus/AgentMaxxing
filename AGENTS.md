# AgentMaxxing repository guidance

This repository defines a lightweight coding-workflow skill. Keep it small.

## Design invariants

- Single-agent execution is the default; planning stages does not require delegation.
- Main context cleanliness and continuity of project intent are the primary goals.
- Main keeps the user's selected session model and effort.
- All delegated workers use `gpt-6-astra`: `low` for small, clear tasks and `medium` for broader work. Medium is the ceiling, including retries and reviewers.
- Delegation must justify its isolation, independent progress, or review value. Worker count is dynamic within client limits, without an artificial project cap.
- Workers receive explicit, compact packets with non-overlapping active write scopes.
- Implementing agents validate and self-review; independent review is optional and justified by risk or an evidence gap.
- Main accepts delegated results before dependent work starts. Correction ownership may transfer explicitly to main.
- Project memory uses existing authoritative documents or a small `.agentmaxxing/` Markdown tree. Main owns shared memory writes.
- Missing or stale memory triggers bounded orientation from current evidence, preserving existing work and marking unknowns. Compact notes must preserve unique decisions, dependencies, sources, and release conditions.
- Do not add databases, daemons, dashboards, telemetry, token ledgers, agent registries, or orchestration runtimes without a concrete demonstrated need.
- VisionOffload is not implemented in this revision.

## Project continuity

Read [.agentmaxxing/project.md](.agentmaxxing/project.md) and the notes relevant to the task. Record explicit future requests, deferrals, decisions, and release obligations as they arise. Keep ideas distinct from accepted scope. Follow the [project-memory protocol](.agents/skills/agentmaxxing/references/project-memory.md); verify mutable facts against current files.

## Repository changes

Prefer improving skill instructions and examples over adding code. Keep `README.md` and `README_TR.md` aligned when behavior changes. Preserve the skill's explicit invocation policy. Commit, push, and publish only when the user authorizes them.
