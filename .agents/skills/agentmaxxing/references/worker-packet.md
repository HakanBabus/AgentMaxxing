# Worker Packet

LUNA performs better when ambiguity is removed before delegation.

Use the smallest packet that makes the task independently executable.

## Template

```markdown
Role: LUNA worker

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

Suggested steps:
1. <first useful step>
2. <second useful step>
3. <validation/self-review>

Constraints:
- <API / dependency / behavior / style constraint>

Done when:
- <measurable result>
- <measurable result>

Validation:
- <exact command/check if known>

Return only:
- status
- changed files
- 2–5 result bullets
- validation result
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

## When the task is too large

Do not solve an overloaded packet by dumping the entire project into LUNA.

Instead ask:

1. Can the task be split into independent outputs?
2. Can discovery be delegated separately from implementation?
3. Can the main agent decide an architecture question first?
4. Is there a smaller test or reproduction target?
5. Can another worker own a truly separate workstream?

Split only along real boundaries. Artificial fragmentation increases duplicated context.
