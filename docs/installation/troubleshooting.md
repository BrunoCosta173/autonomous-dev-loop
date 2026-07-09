# Installation Troubleshooting

Use this guide when the Skill or adapter does not appear to work after manual or agent-assisted installation.

## Skill Is Not Detected

Check:

- The Skill folder was copied into the correct agent-supported location.
- `SKILL.md` exists at the expected path.
- The folder name is exactly `autonomous-dev-loop`.
- The agent environment supports local Skills in that location.
- The agent session was restarted or refreshed if required by the environment.

Codex/OpenAI project-level path:

```text
.agents/skills/autonomous-dev-loop/SKILL.md
```

Claude Code project-level path:

```text
.claude/skills/autonomous-dev-loop/SKILL.md
```

## Wrong Target Installed

Codex/OpenAI and Claude Code use separate Skill folders.

- Codex/OpenAI target: `.agents/skills/autonomous-dev-loop/`
- Claude Code target: `.claude/skills/autonomous-dev-loop/`

Install the target that matches the agent environment.

## Existing Instructions Were Present

If `AGENTS.md`, `CLAUDE.md`, or another instruction file already exists, do not overwrite it blindly.

Recommended approach:

1. Read the existing file.
2. Compare it with the adapter template.
3. Merge only relevant autonomous-dev-loop guidance.
4. Preserve project-specific instructions.

## Review Subagents Are Unavailable

Real review subagents are environment-dependent.

If the current agent platform does not support subagents, use independent review passes with the same reviewer roles and rubrics.

Do not claim real subagent review occurred unless it actually occurred.

## Native Goal Mode Is Unavailable

Native goal or long-run workflows are environment-dependent.

If the platform does not support a native goal mode, emulate Goal Completion Mode through the Skill protocol:

- Objective Brief
- ToDos
- Validation
- Review rounds or independent review passes
- Persistent memory when useful
- Final report

Do not claim `/goal` is universally available.

## Validation Commands Are Missing

The Skill should prefer project-defined commands. If commands are not obvious:

- Inspect package manifests, framework files, task runners, and CI workflows.
- Document commands that were unavailable.
- Do not invent passing validation.
- Report when validation was not run and why.

## Update Did Not Apply

If a manual update did not apply:

- Confirm the installed folder was replaced, not copied into a nested folder.
- Check for duplicate folders such as `autonomous-dev-loop/autonomous-dev-loop`.
- Verify `SKILL.md` changed to the expected version.
- Restart or refresh the agent environment if needed.

## Uninstall Safety

Removing installed Skill folders or copied adapters is destructive.

Before removal:

- Confirm the target path.
- Confirm the file or folder belongs to autonomous-dev-loop.
- Preserve any project-specific local modifications if needed.
