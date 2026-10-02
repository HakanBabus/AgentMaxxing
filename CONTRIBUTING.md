# Contributing

AgentMaxxing should remain lightweight.

Good contributions usually improve:

- single-agent execution and useful delegation decisions;
- Astra low/medium routing;
- worker-packet clarity;
- context isolation;
- compact handoffs;
- failure handling;
- durable project notes and release continuity;
- examples and documentation.

Before adding code or infrastructure, explain which concrete workflow failure it solves and why instructions alone are insufficient.

When behavior changes, update both `README.md` and `README_TR.md`.

Keep worker effort at low or medium. Reuse authoritative project documents before
adding memory files, and keep ideas separate from accepted work. Preserve actual
decision history when revising current instructions.

## Documentation checks

Run Markdown lint across root, architecture, skill, and project-memory documents:

```text
npx markdownlint-cli2 "*.md" "docs/*.md" ".agents/**/*.md" ".agentmaxxing/*.md"
git diff --check
```

On Windows, use `npx.cmd` when PowerShell blocks the script shim. The lint
configuration permits the README's centered HTML wrapper and flexible line
length. Also check relative links, language alignment, and realistic routing
and memory scenarios; lint alone does not validate workflow behavior.
