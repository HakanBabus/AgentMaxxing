# Current Task

## Status

Completed

## Goal

Create the standalone `$agentmaxxing` v0.1 Codex skill.

## Owner

SOL

## Affected paths

- `.agents/skills/agentmaxxing/`
- `.agentmaxxing/`
- `README.md`

## Requirements

- Provide a discoverable repo-scoped `SKILL.md`.
- Preserve SOL/LUNA/TERRA role boundaries and compressed handoffs.
- Load detailed contracts progressively.
- Support minimal project context initialization and updates.

## Constraints

- Do not create a Codex plugin, MCP server, CLI, or application runtime.
- Do not add scripts without a deterministic need.
- Keep automatic skill discovery enabled.

## Acceptance criteria

- Skill structure passes the official skill validator.
- Markdown lint and local-link checks pass.
- Explicit `$agentmaxxing` invocation is represented in UI metadata.
- Documentation and project state reflect the standalone skill decision.

## Progress

- [x] Initialize the skill structure.
- [x] Implement SOL routing and integration instructions.
- [x] Add conditional task and context references.
- [x] Update public documentation and durable project context.

## Decisions needed

None.
