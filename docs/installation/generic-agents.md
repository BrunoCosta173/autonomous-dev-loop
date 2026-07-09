# Generic Agent Installation

Use this guide when an AI coding agent does not support Codex/OpenAI Skills or Claude Code Skills directly, but can read project-local instruction files.

## Quick Install For Users

This installs generic adapter files from the latest version on the `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target generic --scope project
```

For reproducible installs, use a tagged release when available.

Inspect-first alternative:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target generic --scope project
```

## Purpose

Generic installation gives an agent durable project instructions and optional control file templates. It does not install a native Skill runtime.

## Adapter Package

Generic agents can use:

- `adapters/AGENTS.md`
- `adapters/GENERIC_AGENT.md`
- Control file templates from either Skill asset directory

Claude Code users should prefer:

- `adapters/CLAUDE.md`

## Manual Install

Copy the adapter file that matches your agent into the target project.

For agents that read `AGENTS.md`:

```bash
cp path/to/autonomous-dev-loop/adapters/AGENTS.md ./AGENTS.md
```

For Claude Code:

```bash
cp path/to/autonomous-dev-loop/adapters/CLAUDE.md ./CLAUDE.md
```

For agents with no named convention, copy `GENERIC_AGENT.md` to the instruction filename the agent expects:

```bash
cp path/to/autonomous-dev-loop/adapters/GENERIC_AGENT.md ./GENERIC_AGENT.md
```

Do not overwrite existing project instructions without reviewing them first.

## Python Installer

Generic adapters support project scope only.

From this repository, install generic adapters into a target project:

```bash
python3 scripts/install.py --target generic --scope project --project-dir path/to/target-project
```

Preview first:

```bash
python3 scripts/install.py --target generic --scope project --project-dir path/to/target-project --dry-run
```

By default, the generic target installs:

- `AGENTS.md`
- `GENERIC_AGENT.md`

To also copy `CLAUDE.md`, use:

```bash
python3 scripts/install.py --target generic --scope project --project-dir path/to/target-project --with-adapters
```

The installer does not overwrite existing adapter files unless `--force` is used.

## Shell Wrapper

```bash
./install.sh --target generic --scope project --project-dir path/to/target-project
```

## PowerShell Wrapper

```powershell
./install.ps1 --target generic --scope project --project-dir path/to/target-project
```

## Optional Control File Templates

The Skill asset directories contain reusable project control file templates:

```text
.agents/skills/autonomous-dev-loop/assets/
.claude/skills/autonomous-dev-loop/assets/
```

Copy or adapt only the templates that help the target project, such as:

- `TODO.template.md` -> `TODO.md`
- `DEVELOPMENT_LOG.template.md` -> `DEVELOPMENT_LOG.md`
- `TEST_PLAN.template.md` -> `TEST_PLAN.md`
- `KNOWN_ISSUES.template.md` -> `KNOWN_ISSUES.md`
- `FINAL_REPORT.template.md` -> `FINAL_REPORT.md`

Do not force every template into every project.

## Agent-Assisted Install

You can ask an AI coding agent to install a generic adapter:

```text
Install autonomous-dev-loop generic instructions in this project.
Use manual or local installer installation.
Do not pipe remote scripts into the shell.
Copy adapters/AGENTS.md to AGENTS.md if this project does not already have one.
If an instruction file already exists, summarize the conflict and ask before overwriting it.
Do not modify application code.
After installation, verify the file exists and summarize what changed.
```

## Usage

After installation, provide a scoped objective:

```text
Use the autonomous-dev-loop instructions to refactor the project command documentation.
Do not change application behavior.
Run available documentation or lint checks if present.
Use A3 autonomy.
```

## Update

Update copied adapters:

```bash
python3 scripts/install.py --action update --target generic --scope project --project-dir path/to/target-project --yes
```

The update action does not overwrite user-modified adapters unless `--force` is used.

You can also update manually by replacing or merging from the newer adapter template. Prefer merging when the target project has local instructions.

## Uninstall

Uninstall copied adapters:

```bash
python3 scripts/install.py --action uninstall --target generic --scope project --project-dir path/to/target-project --with-adapters --yes
```

The uninstall action removes adapter files only when they match the repository template, unless `--force` is used.

You can also remove copied adapter files manually after confirming they are not used for other project instructions:

```bash
rm AGENTS.md
```

This is a destructive command. Review the file before running it.

## One-Command Install Notes

The quick install command near the top of this document uses `main` as the latest channel.

For reproducible installs, use a tagged release when available.

Inspect-first pattern:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target generic --scope project
```

## Future Installer

Future versions may add richer terminal commands to help install selected control file templates.

Version `0.0.11` includes a Python installer and shell wrappers, but does not publish packages or marketplace/plugin entries automatically.
