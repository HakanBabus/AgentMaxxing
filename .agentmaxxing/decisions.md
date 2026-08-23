# Architectural Decisions

Store only decisions that constrain future architecture or workflow. Do not add
routine implementation choices, progress notes, or conversation summaries.

## D-001 — Begin as a protocol, not a runtime

**Status:** Accepted  
**Date:** 2026-08-23

**Decision:** Phase 1 defines the workflow and context contracts before a CLI,
service, or model API integration is selected.

**Reason:** A premature runtime would hard-code untested assumptions about task
routing, persistence, and Codex integration. The contracts can first be tested
manually and then automated with evidence.

**Consequences:** Phase 1 contains no placeholder application code. Phase 2 must
publish acceptance criteria and a runtime decision before implementation.

## D-002 — Keep roles independent from model mappings

**Status:** Accepted  
**Date:** 2026-08-23

**Decision:** SOL, LUNA, and TERRA are stable responsibility contracts. Their
model and reasoning-level mappings are replaceable execution policy.

**Reason:** Model availability, pricing, and capability change faster than the
workflow's accountability boundaries.

**Consequences:** Documentation may recommend model profiles, but core formats
must not depend on a specific model identifier.

## D-003 — Use a single-writer persistent context

**Status:** Accepted  
**Date:** 2026-08-23

**Decision:** SOL is the sole logical writer of `.agentmaxxing/` context files.
Specialists may recommend changes in their result reports.

**Reason:** Multiple agents updating project truth independently can introduce
conflicting status, unreviewed decisions, and noisy history.

**Consequences:** Context updates occur after SOL validates an integrated result.

## D-004 — Ship as a standalone Codex skill

**Status:** Accepted
**Date:** 2026-08-23

**Decision:** AgentMaxxing v0.1 is a repo-scoped Codex skill under
`.agents/skills/agentmaxxing/`. A Codex plugin is out of scope.

**Reason:** The workflow needs reusable instructions and selective references,
not connectors, distribution metadata, or an additional application runtime.

**Consequences:** Development targets the skill format directly. Plugin
packaging must not be added unless this decision is explicitly revisited.
