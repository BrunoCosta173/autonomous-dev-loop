# Autonomous Dev Loop Adapter

This `AGENTS.md` template is intended for end-user projects that use AI coding agents with project-local instructions.

It is not the contributor instruction file for the `autonomous-dev-loop` repository.

## Purpose

Use this adapter to point an AI coding agent toward the `autonomous-dev-loop` workflow when working inside this project.

## Expected Skill

When available, use the installed `autonomous-dev-loop` Skill for structured autonomous development loops.

The Skill should guide objective intake, project inspection, planning, ToDo generation, execution, testing, repair, documentation, and final reporting with safety gates.

If the Skill folder is not present, ask whether to install it or follow this adapter as a lightweight fallback.

## Safety Gates

Stop and request human confirmation before:

- Destructive commands
- Mass deletion
- Database schema changes with data-loss risk
- Authentication or permission changes
- Deployment
- Secret or environment variable handling
- Data exfiltration or external transmission
- Major architectural rewrites
- Framework replacement
- Ambiguous product decisions
- Business-critical rule changes

## Project Notes

Add project-specific instructions below this line.
