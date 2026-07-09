# Installation Troubleshooting

Use this guide when the Skill or adapter does not appear to work after manual or agent-assisted installation.

## One-Command Install Notes

README one-command install examples use the `main` branch as the latest channel.

For reproducible installs, use a tagged release when available.

If a one-command install fails:

- Download and inspect `install.sh`.
- Run the script locally with the same arguments.
- Try the Python installer directly.
- Confirm the target project directory is correct.
- Confirm `curl` or `wget`, `tar`, and `python3` are available. Piped installation uses them to download the `main` branch archive and run the Python installer from a temporary directory.

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

If installer update did not apply:

- Re-run with `--dry-run` and inspect the planned operation.
- Confirm `--project-dir` points to the target project.
- Use `--yes` for non-interactive update confirmation.
- Use `--force` only when intentionally replacing an existing destination.

## Uninstall Safety

Removing installed Skill folders or copied adapters is destructive.

Before removal:

- Confirm the target path.
- Confirm the file or folder belongs to autonomous-dev-loop.
- Preserve any project-specific local modifications if needed.

The installer removes only known Skill folders and adapter files. User-modified adapters are skipped unless `--force` is used.

## Packaging Troubleshooting

Generate release packages:

```bash
python3 scripts/package_release.py --version 0.1.0 --clean
```

Expected files:

```text
dist/autonomous-dev-loop-0.1.0.zip
dist/autonomous-dev-loop-codex-0.1.0.zip
dist/autonomous-dev-loop-claude-0.1.0.zip
dist/autonomous-dev-loop-adapters-0.1.0.zip
```

If packaging fails:

- Run `python3 scripts/validate_repository.py`.
- Confirm Skill target folders exist.
- Confirm `CHANGELOG.md` has the expected version.
- Remove stale `dist/` output with `--clean`.
