# AgentMaxxing repository guidance

This repository defines a lightweight orchestration skill. Keep it small.

## Design invariants

- Main context cleanliness is the primary goal.
- LUNA is the worker model.
- Worker count is dynamic, not artificially capped.
- More workers are justified only by real task independence.
- LUNA receives explicit worker packets because vague delegation wastes context and produces weaker results.
- Workers self-test and self-review before independent reviewers are considered.
- Worker-to-main handoffs stay compact.
- Do not add databases, daemons, dashboards, telemetry, token ledgers, persistent registries, or orchestration runtimes without a concrete demonstrated need.
- VisionOffload is not implemented in this revision.

## Repository changes

Prefer improving the skill instructions and examples over adding code.

Keep English and Turkish README content aligned when behavior changes.
