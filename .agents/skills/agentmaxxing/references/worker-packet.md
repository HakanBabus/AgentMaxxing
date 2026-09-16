# Worker Packet

LUNA performs better when ambiguity is removed before delegation.

Use the smallest packet that makes the task independently executable.

## Template

```markdown
Role: LUNA worker

Reasoning:
xhigh | max

Stage:
<stage ID and bounded outcome>

Depends on:
<accepted prerequisite IDs or none>

Goal:
<one concrete outcome>

Why delegated:
<what heavy context/work should stay outside main>

Inputs:
- <exact file, directory, log, command, URL, artifact>

Scope:
- May inspect: <...>
- May edit: <...>
- Must not edit: <...>

Later stages / not this task:
- <work deliberately excluded from this packet>

Suggested steps:
1. <first useful step>
2. <second useful step>
3. <validation/self-review>

Constraints:
- <API / dependency / behavior / style constraint>

Done when:
- A1 — <measurable result>
- A2 — <measurable result>

Critical review surfaces:
- <integration boundary, risky behavior, or artifact the main should inspect>

Validation:
- <exact command/check if known>

Return only:
- status: ready-for-review | needs-input | failed
- changed files
- 2–5 result bullets
- acceptance result and concise evidence for every acceptance ID
- validation result
- self-review result
- material caveat or decision needed
```

## Packet quality rules

A packet is weak when it says things like:

- "fix the app"
- "review the backend"
- "make this better"
- "look around and find problems"

A packet is strong when the worker knows:

- what success looks like;
- where to begin;
- what it owns;
- what it must preserve;
- how to prove completion;
- how little it should send back.

Acceptance criteria must describe observable outcomes, not implementation activity. "Added a handler" is not sufficient; "losing and regaining window focus does not produce a camera jump" is.

## Correction packet

When the main agent rejects a result, keep the retry small and specific:

```markdown
Review result: REJECT

Failed:
- A2 — <concrete observed failure>

Preserve:
- <already-passing behavior>

Correction scope:
- <allowed files and behavior>

Required recheck:
- <exact command, interaction, or artifact>

Return only:
- changed paths in this correction
- delta summary
- updated acceptance evidence
- validation result
- material blocker, if any
```

Return the correction to the same worker while the bounded context remains useful. Do not mark the stage complete or begin a dependent stage until the main agent accepts it. If the correction requires new authorization, user input, unavailable external state, or a materially different scope, report `needs-input` rather than pretending the criterion passed.

## When the task is too large

Do not solve an overloaded packet by dumping the entire project into LUNA.

One directory, repository, document, migration, release, or final artifact is not automatically one bounded task. Do not combine several lifecycle phases or materially different quality and validation surfaces merely because they contribute to one requested outcome.

Instead ask:

1. Can the task be split into independent outputs?
2. Can discovery be delegated separately from implementation?
3. Can the main agent decide an architecture question first?
4. Is there a smaller test or reproduction target?
5. Can another worker own a truly separate workstream?

Split only along real boundaries. Artificial fragmentation increases duplicated context.

Prefer a dependency-aware sequence when later work relies on earlier accepted output. A fresh worker can own the next stage; the same worker should retain corrections within its current stage. For compound final-quality claims, add a separate read-only evaluation packet after all prerequisite stages are accepted.
