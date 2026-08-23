# Architecture

## 1. Purpose

AgentMaxxing coordinates specialized AI agents while keeping project context
small, current, and auditable. Its architecture begins as a workflow protocol.
Automation added in later phases must implement this protocol rather than
replace it with an opaque agent loop.

## 2. System boundaries

AgentMaxxing owns:

- role definitions and delegation rules;
- the minimal persistent context contract;
- task and result message formats;
- validation and integration responsibilities;
- future routing and context-budget policies.

AgentMaxxing does not own:

- model hosting or model internals;
- source-control hosting;
- a repository's build and test tools;
- full conversation storage;
- autonomous permission escalation.

This boundary keeps the project portable across Codex environments and avoids
coupling the workflow to a single model snapshot.

## 3. Components

### 3.1 SOL — orchestration control plane

SOL owns the user goal and the final result. Its responsibilities are to:

1. load only the project state needed for the request;
2. classify the task and choose direct work or delegation;
3. create a bounded task envelope;
4. prevent overlapping ownership between agents;
5. verify reports and integrate results;
6. update persistent context when the project state truly changed.

SOL must not treat delegation as mandatory. For small or tightly coupled work,
the coordination overhead can exceed the context saved.

### 3.2 LUNA — bounded execution plane

LUNA performs implementation work with a fixed scope and acceptance criteria.
It may make local implementation choices that do not alter public contracts or
architecture. When a major decision is required, it stops and reports the
decision needed instead of silently expanding scope.

### 3.3 TERRA — independent review plane

TERRA challenges assumptions, investigates failures, and identifies risks or
alternatives. Its output is advisory and prioritized. TERRA does not become a
second orchestrator and does not modify implementation unless a separate task
explicitly grants that scope.

### 3.4 Persistent context plane

The `.agentmaxxing/` directory is the only project-owned persistent context:

- `state.md` answers **Where are we now?**
- `decisions.md` records only durable architectural decisions and reasons.
- `tasks/current.md` describes the single active integration task.

SOL is the sole logical writer. Other agents may propose an update in their
report, but cannot independently mutate durable project truth. This prevents
conflicting summaries and unreviewed decisions.

### 3.5 Communication plane

Delegation uses two small messages:

- a **task envelope** containing goal, scope, requirements, constraints, and
  acceptance criteria;
- a **result report** containing changed items, outcome, validation evidence,
  remaining work, and any decision request.

Raw reasoning traces and full conversations are not part of the contract.

## 4. Core invariants

All future implementations must preserve these rules:

1. **SOL remains accountable.** Delegation transfers work, not final ownership.
2. **Context is selected, not dumped.** An agent receives only sufficient files
   and constraints.
3. **Scopes do not overlap.** Concurrent agents cannot own the same file unless
   SOL defines an explicit handoff.
4. **Claims are verifiable.** A `PASS` result identifies the command or check.
5. **Durable memory stays durable.** Progress logs and low-level choices do not
   enter `decisions.md`.
6. **Roles are model-independent.** Model mapping is replaceable policy.
7. **Permissions do not expand through delegation.** A worker inherits the
   task's action boundary and no more.

## 5. Routing policy

Phase 1 defines routing conceptually; Phase 3 will implement and evaluate it.

SOL should work directly when the task is small, context is already loaded, or
delegation would create a tightly coupled handoff.

LUNA is appropriate when the work is:

- narrowly scoped and implementation-heavy;
- repetitive or parallelizable;
- governed by stable interfaces;
- testable with explicit acceptance criteria.

TERRA is appropriate when the work needs:

- an independent architectural challenge;
- root-cause analysis under uncertainty;
- security or failure-mode review;
- comparison of consequential alternatives.

Routing must eventually be measured against task success, total context, cost,
latency, and rework. Model price alone is not a sufficient optimization target.

## 6. Task lifecycle

```text
Requested -> Scoped -> Assigned -> Executing -> Reported -> Validated
                                                       |          |
                                                       v          v
                                                   Needs input  Completed
```

- **Requested:** SOL receives a user goal.
- **Scoped:** success, files, constraints, and approval boundaries are known.
- **Assigned:** SOL either owns the work or delegates it to one specialist.
- **Executing:** the owner works only within the envelope.
- **Reported:** the owner returns a compressed result with evidence.
- **Validated:** SOL reviews changes and runs proportionate verification.
- **Completed:** SOL updates current state and clears or replaces the task.
- **Needs input:** a material ambiguity or scope expansion returns to SOL.

## 7. Failure modes and mitigations

| Failure mode | Consequence | Mitigation |
| --- | --- | --- |
| Delegating vague goals | Rework and architectural drift | Require scope and acceptance criteria before assignment |
| Overlapping file ownership | Conflicts and lost changes | Assign one owner per file and define explicit handoffs |
| Trusting summary-only test claims | False completion | Require exact command and result; SOL revalidates critical work |
| Writing every event to memory | Context recreates the problem | Store only current truth and durable decisions |
| Locking roles to model names | Brittle workflow | Keep role contracts stable and model mapping configurable |
| Too many agents | Coordination costs exceed savings | Delegate only when task shape justifies it |
| Reviewer becomes implementer | Blurred accountability | Separate advisory review from authorized change tasks |

## 8. Planned implementation layers

Phase 2 can introduce a small core with four replaceable modules:

- **ContextLoader:** reads and validates the three context documents.
- **StateManager:** applies reviewed state transitions atomically.
- **TaskManager:** creates, advances, completes, and clears the active task.
- **MessageCodec:** validates task envelopes and result reports.

Phase 3 adds a **Router** above these modules. Phase 4 adds budget measurement
and compression. No module should require a vector database or transcript store.

The concrete language and runtime will be selected only when Phase 2 acceptance
criteria are defined; Phase 1 does not create a placeholder stack decision.

