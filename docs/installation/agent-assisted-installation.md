# Agent-Assisted Installation

Use agent-assisted installation when a user wants an AI coding agent to copy the correct Skill folder or adapter into a target project.

The installer agent should not modify application code.

## General Rules

- Confirm the target agent environment: Codex/OpenAI, Claude Code, or generic agent.
- Copy only the relevant install target.
- Do not overwrite existing project instruction files without asking.
- Do not change application source code.
- Verify the expected folder or file exists after copying.
- Summarize changed files.
- Do not create installer scripts.

## Installer-Aware Prompt

```text
Install autonomous-dev-loop in this project using the repository installer.
Use a dry run first.
Then install the target that matches this agent environment.
Do not modify application code.
Do not overwrite existing project instructions without asking.
After installation, verify the expected Skill folder or adapter exists and summarize what changed.
```

The agent may use:

```bash
python3 scripts/install.py --target codex --scope project --project-dir path/to/target-project --dry-run
python3 scripts/install.py --target codex --scope project --project-dir path/to/target-project
```

## Codex/OpenAI Prompt

```text
Install autonomous-dev-loop for Codex/OpenAI in this project.
Copy the Skill from this repository into .agents/skills/autonomous-dev-loop.
Do not modify application code.
After installation, verify the folder exists and summarize what changed.
```

Expected result:

```text
.agents/skills/autonomous-dev-loop/SKILL.md
```

## Claude Code Prompt

```text
Install autonomous-dev-loop for Claude Code in this project.
Copy the Skill from this repository into .claude/skills/autonomous-dev-loop.
Also copy adapters/CLAUDE.md to CLAUDE.md if the project does not already have one.
Do not overwrite existing project instructions without asking.
After installation, verify the folder exists and summarize what changed.
```

Expected result:

```text
.claude/skills/autonomous-dev-loop/SKILL.md
```

Optional result:

```text
CLAUDE.md
```

## Generic Agent Prompt

```text
Install autonomous-dev-loop generic instructions in this project.
Copy adapters/AGENTS.md to AGENTS.md if this project does not already have one.
If this project uses a different agent instruction filename, copy adapters/GENERIC_AGENT.md to that filename instead.
Do not overwrite existing project instructions without asking.
Do not modify application code.
After installation, verify the file exists and summarize what changed.
```

Expected result depends on the target agent convention:

```text
AGENTS.md
```

or:

```text
GENERIC_AGENT.md
```

## Verification Checklist

After agent-assisted installation, verify:

- The intended Skill folder or adapter file exists.
- Existing project instructions were not overwritten without approval.
- No application source files were changed.
- No installer script was created.
- The agent summarized the installed target and any skipped actions.

## Update And Uninstall

Agent-assisted updates should replace only the installed Skill folder or merge adapter changes into existing project instructions.

Agent-assisted uninstall should remove only the installed Skill folder or copied adapter after confirming the target path.

Installer examples:

```bash
python3 scripts/install.py --action update --target both --scope project --project-dir path/to/target-project --yes
python3 scripts/install.py --action uninstall --target codex --scope project --project-dir path/to/target-project --yes
```

For adapters, use `--with-adapters` and avoid `--force` unless the user explicitly approves overwriting or removing modified instruction files.
