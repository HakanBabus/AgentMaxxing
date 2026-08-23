#!/usr/bin/env python3
"""Initialize or validate AgentMaxxing's minimal project context."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_HEADINGS = {
    "state.md": (
        "# Project State",
        "## Project",
        "## Current goal",
        "## Completed",
        "## Working",
        "## Blocked",
        "## Next",
    ),
    "decisions.md": ("# Architectural Decisions",),
    "tasks/current.md": (
        "# Current Task",
        "## Status",
        "## Goal",
        "## Owner",
        "## Affected paths",
        "## Requirements",
        "## Constraints",
        "## Acceptance criteria",
        "## Progress",
        "## Decisions needed",
    ),
}


def one_line(value: str) -> str:
    """Collapse user-provided labels to one safe Markdown line."""

    return " ".join(value.split()).strip()


def templates(project: str, goal: str) -> dict[str, str]:
    return {
        "state.md": f"""# Project State

## Project

{project}

## Current goal

{goal}

## Completed

- None yet.

## Working

- Scope the current goal and acceptance criteria.

## Blocked

- None.

## Next

- Define the first bounded task.
""",
        "decisions.md": """# Architectural Decisions

Store only decisions that constrain future architecture or workflow. Do not add
routine implementation choices, progress notes, or conversation summaries.
""",
        "tasks/current.md": f"""# Current Task

## Status

Scoped

## Goal

{goal}

## Owner

SOL

## Affected paths

- To be determined from repository evidence.

## Requirements

- Define observable requirements before implementation.

## Constraints

- Preserve user authorization boundaries.

## Acceptance criteria

- Define observable validation before implementation.

## Progress

- [ ] Confirm scope and acceptance criteria.

## Decisions needed

None.
""",
    }


def context_root(root: Path) -> Path:
    resolved = root.expanduser().resolve()
    if not resolved.is_dir():
        raise ValueError(f"Repository root is not a directory: {resolved}")
    return resolved / ".agentmaxxing"


def initialize(root: Path, project: str | None, goal: str | None) -> int:
    context = context_root(root)
    project_name = one_line(project or root.resolve().name)
    current_goal = one_line(goal or "Define the current project goal.")
    if not project_name or not current_goal:
        raise ValueError("Project and goal must contain visible text.")

    content = templates(project_name, current_goal)
    created = 0
    for relative, body in content.items():
        target = context / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(body)
        except FileExistsError:
            print(f"PRESERVED {target}")
        else:
            created += 1
            print(f"CREATED   {target}")

    print(f"Initialization complete: {created} created, {len(content) - created} preserved.")
    return 0


def validate(root: Path) -> int:
    context = context_root(root)
    errors: list[str] = []

    for relative, headings in REQUIRED_HEADINGS.items():
        target = context / relative
        if not target.is_file():
            errors.append(f"missing file: {target}")
            continue
        text = target.read_text(encoding="utf-8")
        for heading in headings:
            count = sum(1 for line in text.splitlines() if line.rstrip() == heading)
            if count != 1:
                errors.append(
                    f"{target}: expected heading {heading!r} once, found {count}"
                )

    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print(f"Context validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Context validation passed: {context}")
    return 0


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(
        description="Initialize or validate AgentMaxxing project context."
    )
    subcommands = command.add_subparsers(dest="command", required=True)

    init = subcommands.add_parser("init", help="Create missing context files.")
    init.add_argument("--root", type=Path, required=True, help="Repository root.")
    init.add_argument("--project", help="Project name; defaults to root folder name.")
    init.add_argument("--goal", help="Current goal; defaults to a neutral prompt.")

    check = subcommands.add_parser("check", help="Validate context structure.")
    check.add_argument("--root", type=Path, required=True, help="Repository root.")
    return command


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "init":
            return initialize(args.root, args.project, args.goal)
        return validate(args.root)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
