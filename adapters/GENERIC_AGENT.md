# Autonomous Dev Loop Generic Agent Adapter

This template is intended for projects that use a generic AI coding agent without a dedicated Skill system.

It can be copied or renamed to match the instruction filename expected by the target agent.

## Purpose

Use `autonomous-dev-loop` as the operating model for structured autonomous software development work.

If the `autonomous-dev-loop` Skill folder is not present, ask whether to install it or follow this adapter as a lightweight fallback.

## Operating Model

Follow this high-level loop:

```text
Objective intake -> project inspection -> planning -> ToDo generation -> execution -> testing -> repair -> documentation -> final report
```

Keep implementation details aligned with the target project's existing stack, commands, and conventions.

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
