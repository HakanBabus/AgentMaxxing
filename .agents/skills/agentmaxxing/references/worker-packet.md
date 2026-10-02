# Worker Packet

Use the smallest packet that makes one outcome independently executable. Set model and effort in the client's spawn controls as well as stating them in the packet.

## Packet

```text
MODEL: gpt-6.1-sol
EFFORT: low | medium (choose one before spawning)
GOAL: <one observable outcome>
WHY DELEGATED: <isolation, independent progress, or specific review need>
INPUTS: <exact paths, commands, artifacts, or accepted prerequisite facts>
SCOPE: <may inspect, may edit, must preserve; exclude shared project memory>
DEPENDENCIES: <accepted prerequisite or none>
DONE WHEN: <observable acceptance criteria>
VALIDATION: <exact checks when known>
RETURN: <compact handoff from SKILL.md, including durable memory notes>
```

Add suggested steps or critical review surfaces only when they remove a real ambiguity. Do not send the full conversation or repository dump. Acceptance describes behavior: "reload preserves completion state" is stronger than "added storage code."

For low, keep the task small and clearly verifiable. For medium, retain one coherent outcome even if it spans related files. Split overloaded work along actual dependencies; do not fragment one coupled change just to increase worker count.

## Example: low

```text
MODEL: gpt-6.1-sol
EFFORT: low
GOAL: Fix the installation links in the English and Turkish README files.
WHY DELEGATED: This edit can proceed independently of an unrelated CLI fix.
INPUTS: README.md, README_TR.md, docs/INSTALL.md
SCOPE: Edit only README.md and README_TR.md; preserve their feature claims.
DEPENDENCIES: None; docs/INSTALL.md is the accepted installation guide.
DONE WHEN: A1 both installation links resolve; A2 both languages agree.
VALIDATION: Check local link targets and Markdown lint.
RETURN: Compact handoff; note any durable documentation obligation for main.
```

## Example: medium

```text
MODEL: gpt-6.1-sol
EFFORT: medium
GOAL: Preserve saved tasks while migrating storage format v1 to v2.
WHY DELEGATED: Storage migration has an independent write scope.
INPUTS: src/storage/, tests/storage/, docs/storage-format.md
SCOPE: Edit storage code and its tests; preserve unrelated UI behavior.
DEPENDENCIES: Main accepted the v2 format and compatibility contract.
DONE WHEN: A1 v1 data migrates; A2 invalid input preserves original bytes;
           A3 repeated migration is safe.
VALIDATION: Run the existing storage migration and recovery tests.
RETURN: Compact handoff with evidence per criterion and release notes for main.
```

Paths and commands in these examples belong to hypothetical target projects. Adapt them to actual inputs before spawning.

## Correction

```text
REVIEW: REJECT
FAILED: <criterion ID and observed evidence>
PRESERVE: <already-passing behavior>
CORRECTION OWNER: <existing worker or main after explicit ownership transfer>
SCOPE: <allowed files and behavior>
RECHECK: <exact validation>
RETURN: <delta, updated evidence, material blocker>
```

Prefer the same worker for a useful continuation. If main takes over, stop or finish the worker's writing before main edits. Medium remains the ceiling during corrections. An unmet requirement returns `needs-input` or `failed` with its exact cause; it never becomes a passing criterion because another attempt would be inconvenient.
