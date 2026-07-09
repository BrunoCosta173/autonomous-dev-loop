# Claude Code Installation

Use this guide to install the Claude Code Skill target.

## Quick Install For Users

This installs the latest version from the `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target claude --scope project
```

For reproducible installs, use a tagged release when available.

When run through a pipe, `install.sh` downloads the `main` branch archive to a temporary directory and runs the Python installer from that archive.

Inspect-first alternative:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target claude --scope project
```

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

## Python Installer

From this repository, install into a target project:

```bash
python3 scripts/install.py --target claude --scope project --project-dir path/to/target-project
```

Install into a supported user-level location:

```bash
python3 scripts/install.py --target claude --scope user
```

Preview first:

```bash
python3 scripts/install.py --target claude --scope project --project-dir path/to/target-project --dry-run
```

Install the Claude Skill and copy the reusable `CLAUDE.md` adapter when useful:

```bash
python3 scripts/install.py --target claude --scope project --project-dir path/to/target-project --with-adapters
```

The installer does not overwrite existing project instruction files unless `--force` is used.

## Shell Wrapper

The POSIX shell wrapper calls the Python installer:

```bash
./install.sh --target claude --scope project --project-dir path/to/target-project
```

## PowerShell Wrapper

The PowerShell wrapper calls the Python installer:

```powershell
./install.ps1 --target claude --scope project --project-dir path/to/target-project
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

## Update

Update an existing Claude Code project install:

```bash
python3 scripts/install.py --action update --target claude --scope project --project-dir path/to/target-project --yes
```

The update action replaces only the known installed Skill folder.

## Uninstall

Uninstall a Claude Code project install:

```bash
python3 scripts/install.py --action uninstall --target claude --scope project --project-dir path/to/target-project --yes
```

The uninstall action removes only:

```text
.claude/skills/autonomous-dev-loop/
```

It does not remove unrelated `.claude` files or project source files.

## Agent-Assisted Install

You can ask an AI coding agent to install the Skill into a target project:

```text
Install autonomous-dev-loop for Claude Code in this project.
Use manual or local installer installation.
Do not pipe remote scripts into the shell.
Copy the Skill from this repository into .claude/skills/autonomous-dev-loop, or run the local installer after inspecting it.
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

## Manual Update Or Uninstall

You can still update manually by replacing the installed folder with a newer copy of `.claude/skills/autonomous-dev-loop/`.

You can uninstall manually by removing:

```bash
rm -rf .claude/skills/autonomous-dev-loop
```

This is a destructive command. Review the path before running it.

## One-Command Install Notes

The quick install command near the top of this document uses `main` as the latest channel.

For reproducible installs, use a tagged release when available.

Piped installation requires `python3`, `tar`, and either `curl` or `wget`.

Inspect-first pattern:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target claude --scope project
```

## Future Installer

Future versions may add:

- Release packages
- Skill target validation during install
- Marketplace or plugin packaging if supported by the relevant agent ecosystem

Version `0.0.12` includes a Python installer and shell wrappers, but does not publish packages or marketplace/plugin entries automatically.
