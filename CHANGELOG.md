# Changelog

## Unreleased — Main-gated LUNA execution

- Kept the orchestrator role model-neutral as the main agent.
- Added a general workload-sizing gate for tiny, bounded, and compound requests.
- Required compound deliverables to become dependency-aware accepted stage maps instead of overloaded single-worker packets.
- Clarified that sequential stages can use multiple fresh workers; only concurrent workers require independence.
- Lowered the threshold for useful LUNA delegation while preserving clear ownership and compact context.
- Added adaptive LUNA routing between `xhigh` and `max` reasoning.
- Added numbered acceptance criteria and compact criterion-to-evidence handoffs.
- Required explicit main-agent `ACCEPT` or `REJECT` decisions for every delegated stage.
- Required rejected work to return to LUNA with a targeted correction packet and delta handoff.
- Prevented dependent stages from starting before their prerequisites are accepted.
- Made fresh read-only end-to-end evaluation the normal route for compound final-quality claims.
- Preserved the lightweight instruction-only design with no runtime, logs, database, telemetry, or persistent task system.

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
