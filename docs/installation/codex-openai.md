# Codex/OpenAI Installation

Use this guide to install the Codex/OpenAI Skill target.

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
Copy the Skill from this repository into .agents/skills/autonomous-dev-loop.
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

## Update

To update manually, replace the installed folder with a newer copy of:

```text
.agents/skills/autonomous-dev-loop/
```

Review local modifications before replacing the folder. If the installed Skill was customized locally, preserve or reapply those changes intentionally.

## Uninstall

Remove the installed Skill folder from the target project or user Skill directory:

```bash
rm -rf .agents/skills/autonomous-dev-loop
```

This is a destructive command. Review the path before running it.

## Future Installer

Future versions may add:

- Terminal installer command
- Shell and PowerShell installation scripts
- Release packages
- Skill target validation during install

No installer scripts are included in version `0.0.8`.
