# Claude Code Installation

This document describes the initial installation strategy for Claude Code-compatible Skills.

## Purpose

Use this installation target when working with:

- Claude Code CLI
- Claude Code Desktop
- Claude-compatible Skill workflows

## Skill Folder

The Claude Code Skill lives at:

```text
.claude/skills/autonomous-dev-loop/
```

## Manual Installation

For version `0.0.1`, install manually by copying the Skill folder into the target Claude Code Skills location used by your agent environment.

Copy this folder:

```text
.claude/skills/autonomous-dev-loop/
```

The exact destination may depend on the Claude Code environment.

## Role Of `CLAUDE.md`

This repository has two different `CLAUDE.md` files with different roles:

- Root `CLAUDE.md`: instructions for Claude Code agents contributing to this repository.
- `adapters/CLAUDE.md`: reusable template users can copy into their own projects.

The installable Claude Skill entry point is separate:

```text
.claude/skills/autonomous-dev-loop/SKILL.md
```

Do not confuse repository maintenance instructions, reusable project adapters, and Skill installation files.

## Agent-Assisted Installation

An AI coding agent can install the Skill by copying `.claude/skills/autonomous-dev-loop/` into the target project's compatible Claude Skills directory.

The agent may also copy `adapters/CLAUDE.md` into the user's project when project-local Claude Code instructions are desired.

## Future Installer

A terminal installation command or executable installer is planned for a future version.

No installation scripts are included in version `0.0.1`.
