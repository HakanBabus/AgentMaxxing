# Changelog

## Unreleased — Single-agent work and project memory

- Made direct single-agent execution the default, including compound staged work.
- Replaced LUNA delegation with optional `gpt-6-astra` workers: low for small,
  clear tasks and medium for broader work; medium is the worker ceiling.
- Kept the main session's user-selected model and effort unchanged.
- Separated task decomposition from worker creation and made independent review
  conditional on concrete risk or missing evidence.
- Preserved compact packets, self-checks, evidence handoffs, and main acceptance
  before dependent work.
- Allowed explicit transfer of correction ownership to main when appropriate.
- Added a lightweight project-memory protocol for future work, release checks,
  current direction, and decision history, with existing-document reuse.
- Added this repository's project notes and aligned both README languages.
- Added safe first-use orientation for existing projects with missing, partial,
  or stale memory, without guessing history or disturbing in-progress work.
- Made memory compaction preserve unique information and link retained detail.
- Redesigned both README files with quick navigation, workflow diagrams,
  first-use examples, and a compact memory guide.
- Preserved the instruction-only design and explicit skill invocation policy.

## 0.2.0 — Context-first redesign

- Reframed AgentMaxxing around main-context isolation instead of multi-agent complexity.
- Removed TERRA routing from the core workflow.
- Standardized delegated execution on LUNA workers.
- Removed the artificial idea of a fixed worker count; worker count now follows real task independence.
- Added a strict worker-packet contract to compensate for limited worker context and reduce vague delegation.
- Made worker self-test and self-review the default before independent review.
- Replaced verbose specialist reports with compact handoffs.
- Removed the persistent `.agentmaxxing` state/task system and helper-script requirement.
- Deferred VisionOffload integration to a later revision.
