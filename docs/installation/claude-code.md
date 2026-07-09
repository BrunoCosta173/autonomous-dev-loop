# Claude Code Installation

Use this guide to install the Claude Code Skill target.

## Purpose

Use this installation target for Claude Code-compatible Skill workflows, including project-level Skill folders and personal Claude Skill directories when supported by the user's Claude Code setup.

This guide does not claim that every Claude Code environment supports the same discovery paths. Install into the location supported by the Claude Code setup you use.

## Installable Package

The installable Claude Code Skill folder is:

```text
.claude/skills/autonomous-dev-loop/
```

This folder contains the Claude Skill entrypoint, references, and reusable assets.

## Project-Level Manual Install

From inside the target project:

```bash
mkdir -p .claude/skills
cp -R path/to/autonomous-dev-loop/.claude/skills/autonomous-dev-loop .claude/skills/
```

Replace `path/to/autonomous-dev-loop` with the local path to this repository.

After copying, verify:

```bash
test -f .claude/skills/autonomous-dev-loop/SKILL.md
```

## Optional `CLAUDE.md`

Claude Code projects often benefit from a project-local `CLAUDE.md`.

This repository contains two different `CLAUDE.md` files with different roles:

- Root `CLAUDE.md`: instructions for Claude Code agents contributing to this repository.
- `adapters/CLAUDE.md`: reusable template users can copy into their own projects.

The installable Claude Skill entrypoint is separate:

```text
.claude/skills/autonomous-dev-loop/SKILL.md
```

Do not confuse repository maintenance instructions, reusable project adapters, and Skill installation files.

To add a user-project adapter when the target project does not already have one:

```bash
cp path/to/autonomous-dev-loop/adapters/CLAUDE.md ./CLAUDE.md
```

Do not overwrite an existing `CLAUDE.md` without reviewing it first.

## Agent-Assisted Install

You can ask an AI coding agent to install the Skill into a target project:

```text
Install autonomous-dev-loop for Claude Code in this project.
Copy the Skill from this repository into .claude/skills/autonomous-dev-loop.
Also copy adapters/CLAUDE.md to CLAUDE.md if the project does not already have one.
Do not overwrite existing project instructions without asking.
After installation, verify the folder exists and summarize what changed.
```

See [agent-assisted installation](agent-assisted-installation.md) for more examples.

## Usage

After installation, ask Claude Code to use the Skill with a scoped development objective:

```text
Use autonomous-dev-loop to add tests for the orders API.
Focus on request validation, success responses, and error cases.
Do not change database schema or authentication rules.
Run available test and lint commands.
Use A3 autonomy.
```

## Update

To update manually, replace the installed folder with a newer copy of:

```text
.claude/skills/autonomous-dev-loop/
```

Review local modifications before replacing the folder. If the installed Skill was customized locally, preserve or reapply those changes intentionally.

## Uninstall

Remove the installed Skill folder from the target project or user Skill directory:

```bash
rm -rf .claude/skills/autonomous-dev-loop
```

This is a destructive command. Review the path before running it.

## Future Installer

Future versions may add:

- Terminal installer command
- Shell and PowerShell installation scripts
- Release packages
- Skill target validation during install

No installer scripts are included in version `0.0.8`.
