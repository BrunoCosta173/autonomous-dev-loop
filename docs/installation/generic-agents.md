# Generic Agent Installation

This document describes the initial strategy for generic AI coding agents.

## Purpose

Use this path when an agent does not support Codex/OpenAI Skills or Claude Code Skills directly, but can read project-local instruction files.

## Adapter Files

Generic agents can use the reusable templates in:

```text
adapters/
```

Available templates:

- `adapters/AGENTS.md`
- `adapters/GENERIC_AGENT.md`

Claude Code users should prefer:

- `adapters/CLAUDE.md`

## Manual Installation

Copy the adapter file that matches your agent into the target project.

For example:

- Copy `adapters/AGENTS.md` when the agent reads `AGENTS.md`.
- Copy `adapters/GENERIC_AGENT.md` when the agent supports custom instruction files but has no named convention.

## Agent-Assisted Installation

An AI coding agent can install a generic adapter by copying the selected file into the target project and, if needed, renaming it to the filename the target agent expects.

The agent should keep the adapter concise and should not copy repository development instructions from the root `AGENTS.md` or root `CLAUDE.md`.

## Future Installer

A terminal installation command or executable installer is planned for a future version.

No installation scripts are included in version `0.0.1`.
