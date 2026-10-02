---
name: agentmaxxing
description: Keep coding work focused with single-agent execution, optional scoped GPT-6.1 Sol workers at low or medium effort, and lightweight project memory for future work and release checks. Use when the user explicitly invokes $agentmaxxing or asks to use AgentMaxxing.
---

# AgentMaxxing

Complete the user's work with one integration owner, small working context, and durable project decisions. Work directly by default. Delegate only when isolation or independent progress is worth the packet, review, and integration overhead.

## Core rules

- **Single agent first.** A substantial task may need stages without needing more agents. Keep the main session's selected model; this skill does not reconfigure it.
- **GPT-6.1 Sol workers.** For delegated work, explicitly select `gpt-6.1-sol` and `low` for simple, clearly bounded tasks or `medium` for broader reasoning and implementation. Medium is the worker ceiling, including reviewers and retries.
- **Useful delegation only.** A small task can use a low worker when isolation or parallel progress helps; do it directly when explaining it would cost more than completing it. Worker count follows real independence and the client's limits.
- **Clear ownership.** Give each active writer a non-overlapping scope and concise acceptance criteria. Main owns integration and project-memory writes.
- **Evidence before completion.** The implementing agent validates and self-reviews. Main accepts delegated results before dependent work starts. Independent review needs a concrete risk or evidence gap.
- **Remember durable intent.** Record explicit future requests, deferrals, consequential decisions, and release obligations during the turn in which they arise. Keep tentative ideas distinct from accepted work.
- **Join existing work safely.** Missing memory triggers a bounded, read-only orientation from current project evidence. Preserve in-progress edits and mark unknowns instead of inventing history or plans.
- **Stay lightweight.** Use existing project documents or a few Markdown files. Keep raw logs, transcripts, agent registries, and orchestration infrastructure out of project memory.

## Start and route

1. Read applicable project instructions and the existing project overview. If memory is missing, partial, or stale, follow the [first-use protocol](references/project-memory.md#first-use-in-an-existing-project) before making project assumptions. Read only relevant notes and verify mutable facts against current files.
2. Identify the requested outcome, constraints, and proportionate checks. For compound work, sketch stages with dependencies and acceptance; main can own every stage.
3. Decide separately whether any bounded task benefits from delegation. Read [routing.md](references/routing.md) for effort selection, concurrency, corrections, or reviewer decisions.
4. For a delegated task, read [worker-packet.md](references/worker-packet.md), set model and effort explicitly through supported spawn controls, and send only the needed inputs. A packet label alone does not change the worker model. If the requested profile is unavailable, continue directly when feasible and disclose that limitation; do not silently substitute another worker model or exceed medium.

This skill authorizes suitable optional delegation within the user's task when the client supports it. Delegation adds no permission to change external systems, publish, or broaden the task.

## Execute, validate, and accept

The implementing agent completes its bounded scope, runs relevant checks, self-reviews, and corrects material defects. Recheck after a correction when it affects the evidence. A delegated result returns `ready-for-review`, not automatic acceptance.

Main checks scope, acceptance evidence, validation, and integration-sensitive changes, then returns **ACCEPT** or **REJECT**. Missing evidence, skipped required checks, and material defects prevent acceptance. Review the targeted artifacts needed for that decision rather than replaying the entire investigation.

On rejection, identify the failed criteria, observed evidence, behavior to preserve, correction scope, and required recheck. Prefer the existing worker when its context is useful. Main may take over a small or tightly coupled correction after ending or transferring worker write ownership. Validate the final correction and decide again before dependent work starts.

If a low pass lacks necessary reasoning, improve its packet and use medium when justified. At medium, narrow or split the problem, improve the reproduction or validation, or bring the architectural decision back to main. Do not raise worker effort above medium, multiply identical attempts, or lower the quality bar. Report a real missing input or external blocker precisely.

## Compact handoff

```text
STATUS: ready-for-review | needs-input | failed
CHANGED: <paths or none>
RESULT: <concise outcome>
ACCEPTANCE: <criterion IDs, PASS/FAIL, evidence>
VALIDATION: <PASS/FAIL/SKIPPED, exact check>
SELF-REVIEW: <material correction or none>
MEMORY NOTES: <durable future/release/decision notes for main, or none>
CAVEAT: <only if material>
```

Return evidence and navigation pointers, not raw logs, full transcripts, or private reasoning. Main updates durable notes after checking worker discoveries; workers do not write shared project memory concurrently.

## Project memory

Read [project-memory.md](references/project-memory.md) when initializing memory, recording a durable note, resuming across sessions, or preparing a release.

Prefer the project's existing overview, roadmap, release checklist, and decision history. When these are missing and continuity is useful, create only the needed files under `.agentmaxxing/`:

- `project.md` — current direction, constraints, and links to authoritative documents;
- `roadmap.md` — future project shape, ideas, accepted work, and deferred work;
- `release.md` — checks and obligations for the upcoming release;
- `history.md` — meaningful milestones and decision rationale.

Record important intent as it appears, before the final response or a handoff; do not rely solely on an end-of-task summary. Close completed or dropped items and record any material remaining obligation. During release preparation, inspect the relevant release notes and verify required checks before claiming readiness.

Keep active memory brief by removing repetition and linking details. Preserve unique decisions, sources, dependencies, unresolved questions, and release conditions; move detail to its authoritative document or a linked archive instead of discarding it to meet a length target. Missing notes are not a reason to stop otherwise well-scoped work.

Memory updates happen while an agent is working with this skill. No background service or guaranteed capture after an abrupt interruption is provided. Explicit invocation remains required; an ongoing project may add a short pointer in its own instructions for subsequent tasks. Do not claim the client will auto-load these files.

## Completion and boundaries

Main reports the outcome, meaningful verification, and material limitations. Keep orchestration mechanics brief. Do not commit, push, publish, or change account configuration without user authorization. VisionOffload remains outside this revision.
