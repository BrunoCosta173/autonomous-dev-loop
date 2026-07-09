# Autonomous Dev Loop Adapter For Claude Code

This `CLAUDE.md` template is intended for end-user projects that use Claude Code.

It is not the contributor instruction file for the `autonomous-dev-loop` repository.

## Purpose

Use this adapter to point Claude Code toward the `autonomous-dev-loop` workflow when working inside this project.

## Expected Skill

When available, use the installed Claude Skill:

```text
.claude/skills/autonomous-dev-loop/
```

The Skill should guide objective intake, project inspection, planning, ToDo generation, execution, testing, repair, documentation, and final reporting with safety gates.

## Safety Gates

Stop and request human confirmation before:

- Destructive commands
- Mass deletion
- Database schema changes with data-loss risk
- Authentication or permission changes
- Deployment
- Secret or environment variable handling
- Major architectural rewrites
- Framework replacement
- Ambiguous product decisions
- Business-critical rule changes

## Project Notes

Add project-specific Claude Code instructions below this line.
