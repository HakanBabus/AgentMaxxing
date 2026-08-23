# Security Policy

## Supported versions

AgentMaxxing is currently in a pre-release foundation phase. Security fixes are
applied to the latest commit on the `main` branch; there are no supported release
branches yet.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability or include secrets,
personal data, exploit details, or repository credentials in public discussion.

Use GitHub's **Report a vulnerability** private reporting feature when it is
enabled for this repository. If private reporting is unavailable, contact the
repository owner privately through their GitHub profile and share only enough
information to establish a secure follow-up channel.

Include, when possible:

- affected component or workflow;
- impact and required attacker capabilities;
- minimal reproduction steps;
- suggested mitigation;
- whether the issue has been disclosed elsewhere.

Maintainers should acknowledge a report, assess scope and severity, coordinate a
fix, and agree on disclosure timing with the reporter. Response-time guarantees
will be published after the project has an established maintainer process.

## Security boundaries

Agent delegation never expands user authorization. Treat credentials, prompts,
source code, tool outputs, and persistent context as potentially sensitive.
Agents must not persist secrets or raw reasoning in `.agentmaxxing/` files.
