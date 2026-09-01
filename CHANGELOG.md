# Changelog

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
