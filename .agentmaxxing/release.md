# Release Checks

Target: Unreleased | Updated: 2026-10-02.

## This revision

- [x] Skill Creator validation and UI metadata checks.
- [x] Markdown lint, local links/anchors, and bilingual behavior alignment.
- [x] First-use fixtures: existing dirty Git project and read-only non-Git project.
- [x] Review current GPT-6.1 Sol low/medium rules and run `git diff --check`.
- [x] Apply the user's model correction across skill, docs, and installed files;
  verify installed file hashes and skill metadata after the update.
- [x] User authorized commit/push and local skill update for this revision.

## Evidence and limits

Skill validation passed; 14 Markdown files linted and 48 local links resolved.
First-use fixtures preserved source/read-only hashes, reused existing plans,
recorded a conditional deferral, and left migration checks pending. These checks
do not establish general model quality or cost savings. Memory is captured during active work, not by a
background service; abrupt interruption can still lose unwritten information.
Profile availability is client-dependent; see the [skill](../.agents/skills/agentmaxxing/SKILL.md).

Local delivery: installed skill updated, all five file hashes match the validated
repository source, and the previous installation is backed up outside skills.
Repository delivery: GitHub CLI authentication was renewed and the revision was
pushed to origin/main. This publishes repository changes, not a tagged release.
