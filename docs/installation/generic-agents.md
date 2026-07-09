# Generic Agent Installation

Use this guide when an AI coding agent does not support Codex/OpenAI Skills or Claude Code Skills directly, but can read project-local instruction files.

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

To update manually, replace the copied adapter or merge changes from the newer template. Prefer merging when the target project has local instructions.

## Uninstall

Remove the copied adapter file only after confirming it is not used for other project instructions.

Example:

```bash
rm AGENTS.md
```

This is a destructive command. Review the file before running it.

## Future Installer

Future versions may add terminal commands or scripts to help install adapters and selected control file templates.

No installer scripts are included in version `0.0.8`.
