# Agent Workflow

## Operating model

AgentMaxxing uses a hub-and-spoke workflow. SOL is the integration hub; LUNA and
TERRA are specialists with bounded authority. Specialists communicate through
SOL rather than building their own long-lived project context.

This structure trades unrestricted agent autonomy for clearer accountability,
smaller prompts, and easier validation.

## 1. Load minimal context

SOL starts with `.agentmaxxing/state.md`. It loads the active task when the user
continues current work and loads architectural decisions when they constrain the
request. Repository inspection begins at named or likely affected paths.

SOL should widen inspection only when evidence shows that the task crosses those
boundaries. “Read everything first” is not a default strategy.

## 2. Classify the request

SOL identifies:

- desired outcome and acceptance evidence;
- relevant project and file boundaries;
- whether the action is analysis, implementation, or review;
- approval boundaries and destructive or external effects;
- uncertainty that could change the solution materially.

The result is either a direct SOL task or a task envelope from
`docs/task-protocol.md`.

## 3. Choose the execution route

```text
Is the task small or tightly coupled to SOL's current context?
├── Yes -> SOL executes and validates.
└── No
    ├── Is it bounded implementation with stable constraints?
    │   └── Yes -> LUNA executes; SOL validates.
    ├── Does it need independent criticism or uncertain analysis?
    │   └── Yes -> TERRA analyzes; SOL decides the next action.
    └── Otherwise -> SOL narrows the task before delegation.
```

A single request may use TERRA before LUNA when a consequential design must be
challenged first. This is a deliberate sequential handoff, not two agents sharing
the same task.

## 4. Execute with bounded ownership

The assigned agent owns only the envelope's scope. Discovering a related problem
does not expand that scope. The agent reports it under `Remaining` or
`Decision needed` unless the original task explicitly authorizes the change.

Concurrent work is safe only for independent scopes. SOL records which agent
owns each path and defines a handoff when one task consumes another's artifact.

## 5. Compress the handoff

Specialists report changed artifacts, observable outcomes, verification, and
remaining work. They omit narration and raw reasoning. SOL may request a small
evidence excerpt when a claim cannot otherwise be checked.

Compression must not remove:

- failed or skipped validation;
- scope deviations;
- unresolved risks;
- material assumptions;
- decisions that require SOL or user authority.

## 6. Validate and integrate

SOL treats the specialist report as an index to the work, not as proof. SOL:

1. reviews affected artifacts;
2. checks scope and architectural constraints;
3. runs proportionate validation;
4. resolves or exposes remaining work;
5. presents the integrated outcome to the user.

Critical or high-risk changes may return to TERRA for a focused review after
implementation. The review receives the diff and acceptance criteria, not the
entire conversation.

## 7. Persist only changed truth

After validation, SOL replaces stale state, records any durable architectural
decision, and completes or replaces the active task. If nothing durable changed,
SOL does not touch persistent context.

## Example: feature with review and implementation

```text
User asks for a cache invalidation feature
  -> SOL scopes public behavior and affected module
  -> TERRA reviews consistency and failure risks
  -> SOL selects an approach and records a durable decision if needed
  -> LUNA implements the bounded change and tests
  -> SOL reviews the diff, reruns checks, and updates current state
```

Each handoff contains only the proposal or files needed for that step. No agent
receives the previous agent's full transcript.

## Measuring whether delegation helped

Phase 3 routing and Phase 4 optimization should collect task-level aggregates,
not conversation archives:

- acceptance criteria passed;
- validation retries and rework;
- total input and output tokens;
- elapsed time and model cost;
- scope violations or user interventions.

A cheaper or faster route is better only when the final result still meets the
same quality bar.

