# Repository Structure

This document explains the initial `autonomous-dev-loop` repository structure for version `0.0.1`.

## Top-Level Files

- `README.md`: concise public-facing overview and current status.
- `LICENSE`: MIT License.
- `CHANGELOG.md`: version history.
- `CONTRIBUTING.md`: contribution guidelines.
- `PROJECT_BRIEF.md`: project purpose, scope, audience, compatibility goals, and foundation decisions.
- `AGENTS.md`: instructions for AI agents contributing to this repository.
- `CLAUDE.md`: instructions for Claude Code agents contributing to this repository.

## `docs/`

The `docs/` directory contains project documentation that should not be bundled inside installable Skill folders.

- `docs/planning/`: step-by-step planning records.
- `docs/installation/`: installation notes for supported agent environments.
- `docs/design/`: design decisions for repository layout and Skill architecture.

## `.agents/`

The `.agents/` directory contains the Codex/OpenAI Skill installation target.

The canonical Codex/OpenAI Skill path is:

```text
.agents/skills/autonomous-dev-loop/
```

This folder is intended to be copied into a compatible Codex/OpenAI Skills location.

## `.claude/`

The `.claude/` directory contains the Claude Code Skill installation target.

The canonical Claude Skill path is:

```text
.claude/skills/autonomous-dev-loop/
```

This folder is intended to be copied into a compatible Claude Code Skills location.

## `adapters/`

The `adapters/` directory contains reusable project-local instruction templates for end users.

These files are not used to develop this repository itself. They are templates users can copy into their own projects:

- `adapters/AGENTS.md`: template for agent-enabled projects that use `AGENTS.md`.
- `adapters/CLAUDE.md`: template for Claude Code projects.
- `adapters/GENERIC_AGENT.md`: template for generic AI coding agents.

## `examples/`

The `examples/` directory reserves space for future example projects and walkthroughs.

Initial planned examples:

- `examples/nextjs-app/`
- `examples/fastapi-api/`
- `examples/laravel-app/`

The examples are placeholders for future documentation and should not be treated as complete sample projects yet.

## Skill Files Versus Adapters

Skill files and adapter files are different:

- Skill files live inside `.agents/skills/autonomous-dev-loop/` or `.claude/skills/autonomous-dev-loop/`.
- Skill files are installed into agent Skill systems.
- Adapter files live inside `adapters/`.
- Adapter files are copied into a user's project as local agent instructions.

The Skill should define reusable behavior. The adapters should help a project point its agent toward that behavior without duplicating the full Skill implementation.

## Repository Development Files Versus User-Facing Files

Root-level `AGENTS.md` and `CLAUDE.md` are for agents contributing to this repository.

Files under `adapters/` are for users to copy into their own projects.

Files under `.agents/skills/` and `.claude/skills/` belong inside Skill installations.

Keeping these roles separate prevents confusion between repository maintenance instructions, user project adapters, and installable Skill content.
