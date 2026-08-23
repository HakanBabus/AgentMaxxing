# Task Contract

Read this reference only when delegating specialist work or validating a
specialist handoff.

## Task envelope

Send every specialist a bounded envelope:

```markdown
Role: <LUNA | TERRA>
Goal: <one measurable outcome>
Scope:
- <owned path or analysis boundary>
Requirements:
- <required behavior or evidence>
Constraints:
- <must preserve, must not change, approval boundary>
Acceptance:
- <observable check>
Context:
- <only non-obvious facts needed to avoid rediscovery>
```

`Context` is optional. All other fields are required.

Do not assign an envelope when the goal combines unrelated outcomes, acceptance
depends only on an agent's claim, ownership overlaps active work, or a major
architecture choice is hidden inside implementation. Narrow the task or request
TERRA analysis first.

## Role boundaries

### LUNA

LUNA may make local implementation choices within stable interfaces. It must
stop and report before changing public APIs, architecture, persistence formats,
dependencies, permissions, or out-of-scope files.

### TERRA

TERRA returns prioritized findings, evidence, alternatives, and concrete
mitigations. Analysis does not authorize file changes.

## Result report

Require this compact handoff:

```markdown
Changed:
- <path, artifact, or None>

Fixed:
- <observable outcome or None>

Tests:
- <PASS | FAIL | NOT RUN> — <exact command or reason>

Remaining:
- <follow-up, blocker, or None>

Decision needed:
- <material decision for SOL or None>
```

Reports should normally remain within 15 lines. They must preserve failed or
skipped validation, scope deviations, unresolved risk, material assumptions,
and decisions requiring greater authority. They must omit raw reasoning and
conversation transcripts.

SOL independently checks the changed artifacts and proportionately reruns
validation before accepting completion.
