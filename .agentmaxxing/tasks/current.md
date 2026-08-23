# Current Task

## Status

Completed

## Goal

Make `$agentmaxxing` visible as a personal skill and validate real use.

## Owner

SOL

## Affected paths

- `.agents/skills/agentmaxxing/`
- `.agentmaxxing/`
- `tests/`
- `README.md`
- `README.tr.md`

## Requirements

- Preserve the standalone skill format without a plugin.
- Support personal installation from the public GitHub repository.
- Add deterministic context initialization and validation.
- Verify structure, scripts, documentation, and installed content.

## Constraints

- Do not overwrite existing project context during initialization.
- Do not duplicate the skill under a second tracked source path.
- Preserve user-authored documentation commits.

## Acceptance criteria

- Official skill validation passes.
- Context helper tests pass on fresh, existing, and missing context.
- Markdown lint and local-link checks pass.
- Personal installation from GitHub succeeds.
- Installed skill content matches the pushed canonical source.

## Progress

- [x] Diagnose repo-scoped versus personal discovery.
- [x] Add explicit UI invocation policy.
- [x] Add deterministic context helper and tests.
- [x] Document personal installation and restart behavior.
- [x] Run all validation and push the canonical source.
- [x] Install from GitHub and verify the personal copy.

## Decisions needed

None.
