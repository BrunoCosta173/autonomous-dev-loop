# Codex/OpenAI Installation

Use this guide to install the Codex/OpenAI Skill target.

## Quick Install For Users

This installs the latest version from the `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

For reproducible installs, use a tagged release when available.

When run through a pipe, `install.sh` downloads the `main` branch archive to a temporary directory and runs the Python installer from that archive.

Inspect-first alternative:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target codex --scope project
```

## Purpose

Use this installation target for Codex/OpenAI-compatible Skill environments, including project-level Skill folders and personal Skill directories when supported by the user's agent setup.

This guide does not claim that every Codex/OpenAI environment supports the same discovery paths. Install into the location supported by the agent setup you use.

## Installable Package

The installable Codex/OpenAI Skill folder is:

```text
.agents/skills/autonomous-dev-loop/
```

This folder contains the Skill entrypoint, references, metadata, and reusable assets.

## Project-Level Manual Install

From inside the target project:

```bash
mkdir -p .agents/skills
cp -R path/to/autonomous-dev-loop/.agents/skills/autonomous-dev-loop .agents/skills/
```

Replace `path/to/autonomous-dev-loop` with the local path to this repository.

After copying, verify:

```bash
test -f .agents/skills/autonomous-dev-loop/SKILL.md
```

## Python Installer

From this repository, install into a target project:

```bash
python3 scripts/install.py --target codex --scope project --project-dir path/to/target-project
```

Install into a supported user-level location:

```bash
python3 scripts/install.py --target codex --scope user
```

Preview first:

```bash
python3 scripts/install.py --target codex --scope project --project-dir path/to/target-project --dry-run
```

## Shell Wrapper

The POSIX shell wrapper calls the Python installer:

```bash
./install.sh --target codex --scope project --project-dir path/to/target-project
```

## PowerShell Wrapper

The PowerShell wrapper calls the Python installer:

```powershell
./install.ps1 --target codex --scope project --project-dir path/to/target-project
```

## Update

Update an existing Codex/OpenAI project install:

```bash
python3 scripts/install.py --action update --target codex --scope project --project-dir path/to/target-project --yes
```

The update action replaces only the known installed Skill folder.

## Uninstall

Uninstall a Codex/OpenAI project install:

```bash
python3 scripts/install.py --action uninstall --target codex --scope project --project-dir path/to/target-project --yes
```

The uninstall action removes only:

```text
.agents/skills/autonomous-dev-loop/
```

It does not remove unrelated `.agents` files or project source files.

## Personal Skill Directory Install

Some Codex/OpenAI-compatible environments may support personal or user-level Skill directories.

If your environment supports that, copy:

```text
.agents/skills/autonomous-dev-loop/
```

into the user-level Skill location documented by that environment.

Do not assume the same personal directory works for all agents.

## Agent-Assisted Install

You can ask an AI coding agent to install the Skill into a target project:

```text
Install autonomous-dev-loop for Codex/OpenAI in this project.
Use manual or local installer installation.
Do not pipe remote scripts into the shell.
Copy the Skill from this repository into .agents/skills/autonomous-dev-loop, or run the local installer after inspecting it.
Do not modify application code.
After installation, verify the folder exists and summarize what changed.
```

See [agent-assisted installation](agent-assisted-installation.md) for more examples.

## Usage

After installation, ask the agent to use the Skill with a scoped development objective:

```text
Use autonomous-dev-loop to improve the user settings page.
Focus on UI consistency, form validation, loading states, and accessibility.
Do not change database schema, authentication, or dependencies.
Run available lint, typecheck, and build commands.
Use A3 autonomy.
```

## Manual Update Or Uninstall

You can still update manually by replacing the installed folder with a newer copy of `.agents/skills/autonomous-dev-loop/`.

You can uninstall manually by removing:

```bash
rm -rf .agents/skills/autonomous-dev-loop
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
sh install.sh --target codex --scope project
```

## Future Installer

Future versions may add:

- Release packages
- Skill target validation during install
- Marketplace or plugin packaging if supported by the relevant agent ecosystem

Version `0.1.0` includes a Python installer and shell wrappers, but does not publish packages or marketplace/plugin entries automatically.
