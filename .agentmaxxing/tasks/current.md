# Current Task

## Status

Completed

## Goal

Require explicit `$agentmaxxing` invocation in repository and personal scopes.

## Owner

SOL

## Affected paths

- `.agents/skills/agentmaxxing/`
- `.agentmaxxing/`
- `README.md`
- `README.tr.md`

## Requirements

- Disable implicit activation through the supported skill policy.
- Keep `$agentmaxxing` and explicit UI selection available.
- Synchronize the canonical and personal skill copies.
- Document the explicit-only behavior in both languages.

## Constraints

- Preserve the standalone skill format without a plugin.
- Do not change routing behavior after the skill is explicitly invoked.
- Keep the GitHub skill folder as the canonical tracked source.

## Acceptance criteria

- `policy.allow_implicit_invocation` is `false` in both skill copies.
- Official skill validation passes for canonical and personal installations.
- Documentation and context checks pass.
- Installed tracked skill content matches the canonical source.

## Progress

- [x] Confirm the supported explicit-only invocation policy.
- [x] Disable implicit invocation in canonical and personal metadata.
- [x] Narrow the skill description to explicit requests.
- [x] Document the behavior in English and Turkish.
- [x] Run validation and publish the canonical update.

## Decisions needed

None.
