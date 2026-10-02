# Project Memory

Keep future intent, release obligations, and important rationale available across sessions without growing the active context into a transcript.

## Locate the source of truth

Read project instructions first. Reuse existing overview, roadmap, release, or decision documents when they serve the purpose. If several locations exist, choose one authoritative home for each kind of information and link to it from the overview. Do not maintain duplicate copies.

When continuity is needed and equivalent documents are missing, use `.agentmaxxing/project.md`, `roadmap.md`, `release.md`, and `history.md`. Create only files with useful content. Keep these project-local notes in version control when repository conventions allow it; do not ignore them merely because the directory is hidden.

An installed skill contains this reference, not the target project's memory. Resolve `.agentmaxxing/` against the project being worked on, never against the global skills folder. Do not modify Codex's personal memory store as part of this protocol.

## First use in an existing project

Missing AgentMaxxing notes do not mean the project is new or unfinished. Orient from evidence before planning changes, without requiring the user to reconstruct the whole conversation.

1. **Locate the work.** Use the requested project or component, applicable `AGENTS.md`, and the current working directory. In a monorepo, reuse the shared overview and identify the component's scope; do not create competing root/component plans. Clarify only when the actual target cannot be determined safely.
2. **Take a bounded snapshot.** Read the overview/README, relevant manifest or entrypoints, and existing roadmap, release, or decision documents. If Git is available, inspect status and the branch; inspect only relevant diffs to understand current work. In a non-Git project, use the file tree and relevant documents. Expand into source only to resolve facts the requested task depends on.
3. **Separate evidence from intent.** Record observed purpose, stack, constraints, authoritative paths, and current work with sources. Treat uncommitted edits as in-progress unless evidence says otherwise. Old plans and TODOs are existing notes with unverified status, not newly accepted commitments. Do not infer past decisions, completed validation, a release version, or a desired future from the file tree.
4. **Seed only useful notes.** Prefer existing authoritative documents. If no overview serves continuity, create a short `project.md` with sources and relevant unknowns. Add roadmap/release/history files only when there is actual content. Import explicit existing commitments with their source and certainty; never generate a speculative roadmap or an invented historical timeline to fill the tree.
5. **Continue the requested task.** Give a brief orientation when it materially affects the work, state any necessary assumption, and proceed. Ask only about a conflict or missing decision that changes the outcome. Leave unrelated unknowns marked without blocking useful work. A read-only request returns proposed notes without creating files.

Bootstrap is additive and observational. It never resets the repository, rewrites existing plans, finishes someone else's dirty work, or runs a broad build/dependency installation solely to populate notes. Normal task validation follows the task's risk and scope. Note presence is not a prerequisite for execution.

For partial memory, fill the missing relevant section instead of rebuilding all files. For stale memory, compare with current evidence, preserve durable user decisions, update observed facts with a date/source, and mark conflicts that cannot be resolved. Broken links are repaired or labeled unavailable; they are not evidence for a guessed replacement. Keep compact pointers instead of copying entire existing documents.

### Example: joining midway

Given an existing README, a package manifest, uncommitted editor changes, and no project notes, capture the documented purpose and stack, point to the existing documents, and describe the edits as unverified work in progress. If the user asks to add offline export later, record that request with its condition and source. Do not mark the editor complete, invent earlier architecture decisions, or start implementing export as part of the current task.

## What to record

| Signal | Record |
| --- | --- |
| User requests a later feature or explicitly defers work | Roadmap item with requested scope and status |
| User explores a possibility without deciding | Idea, clearly labeled tentative |
| Agent discovers a future improvement | Candidate idea with evidence; no invented user commitment |
| A change affects compatibility, migration, or release validation | Release obligation with an observable check |
| A consequential decision changes project direction | Short history entry with reason and source |
| A milestone completes or a plan is dropped | Update its current status and record a meaningful outcome |

Record explicit durable intent during the same turn in which it appears, once sufficiently clear. Do not wait for a later session or batch every note at the end of a long task. A deferred feature is a future commitment, not permission to implement it now.

Use the source's certainty. For example, "maybe add sync" is an idea; "add sync after Android stabilizes" is accepted future work with a dependency. New explicit user decisions supersede older notes. Mark the old decision superseded when the rationale matters.

## Minimal record

Each item needs a concise outcome, status, date, and source. Add a dependency, rationale, or relevant artifact only when it helps future work. A source can be a short paraphrase of the user's instruction, a repository path, or a commit reference; do not fabricate a permalink or export the conversation.

Prefer one compact entry: `ID [status] outcome | condition/dependency | date, source`. Keep meaningful rationale or exact acceptance detail when a short label would lose it. Shared dates and sources can appear once under a heading instead of being repeated per line.

Use `idea`, `accepted`, `deferred`, `done`, or `dropped` as needed. User-confirmed deferrals carry their condition or dependency. Link release checks to roadmap IDs when they describe the same obligation instead of copying the whole item.

```markdown
## Storage

- R-01 [deferred] Export saved tasks after the v2 migration is accepted.
  - Source: 2026-10-02, user requested export after migration.
  - Depends on: v2 compatibility validation.

- R-02 [idea] Explore cloud sync.
  - Source: 2026-10-02, agent suggestion; not user-approved.
```

## File responsibilities

### project.md

Keep a short overview: purpose, current direction, durable constraints, current milestone, and links to authoritative files. Link to implementation evidence instead of copying source architecture or API details that will drift.

### roadmap.md

Group future work into a small feature tree or headings with nearby, later, and tentative items when useful. Preserve conditions and dependencies. Completed work can leave the active roadmap once history or existing release documents provide a useful pointer.

### release.md

Identify the target release or use `Unreleased` when no version is set. Keep a short checklist of required validation, known limitations, compatibility/migration obligations, and user-facing notes. A checkbox becomes complete only with actual evidence; distinguish failed or unavailable checks explicitly. Review this file during release preparation before claiming readiness. Publishing still needs authorization.

### history.md

Record meaningful milestones and changes of direction with their reasons. Link code-level release details to the existing changelog. Avoid a per-turn diary, worker lifecycle log, token ledger, or duplicate Git history.

## Read and write lifecycle

1. **Start or resume:** read the overview and relevant roadmap/release sections, or bootstrap from current evidence if needed. Read historical entries only when a decision's rationale matters. Verify mutable implementation facts against current files.
2. **During work:** main records important user intent promptly. Workers return candidate memory notes; main checks and merges them. Assign one writer to shared notes even during parallel implementation.
3. **Milestone or completion:** update current status, close or defer affected items, and preserve remaining release obligations. Read back the affected notes before the final response.
4. **Release:** inspect relevant obligations, verify them, and report remaining failures or unavailable checks. Do not mark publishing complete merely because documents are ready.

Keep memory updates within the project's authorized write scope. In read-only work, return proposed durable notes without writing them. If a write fails, disclose that the note was not persisted rather than claiming capture.

This is an agent write discipline while the skill is active. It does not run after the chat closes, guarantee recovery from abrupt interruption, or auto-load itself in future sessions. A project may add a short instruction pointer to its overview for continuity without injecting the whole history.

## Keep growth small

Prefer links, deduplicate notes, and retire stale active items. When history gets cumbersome, move older entries to a dated Markdown archive and leave a short index. Create archives only when needed. Do not store secrets, raw tool payloads, or full transcripts.

Compress prose, not commitments. Preserve unique outcomes, statuses, constraints, dependencies, rationale, sources, open questions, and release evidence. Keep exact commands, migration conditions, or acceptance details in the linked authoritative document if they are too long for the active note. Before compacting, check that each unresolved item and its conditions still have a discoverable home. Do not delete useful information to satisfy a fixed line or token budget; archive detail with a pointer when needed.
