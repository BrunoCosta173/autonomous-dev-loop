# Claude Code Instructions For This Repository

These instructions are for Claude Code agents contributing to the `autonomous-dev-loop` repository itself.

Do not copy this file into end-user projects. Use `adapters/CLAUDE.md` as the reusable project template.

## Current Status

The project is in early planning and scaffolding.

- Step 0 foundation is complete.
- Step 1 repository structure is complete.
- Step 2 internal Skill architecture is complete.
- Installer scripts, asset templates, and complete examples are intentionally deferred.

## Repository Purpose

`autonomous-dev-loop` will become a public, reusable agent skill for autonomous software development loops with safety gates.

The target workflow is:

```text
Objective intake -> project inspection -> planning -> ToDo generation -> execution -> testing -> repair -> documentation -> final report
```

## Claude-Specific Guidance

- Keep root `CLAUDE.md` focused on repository contribution behavior.
- Keep `adapters/CLAUDE.md` focused on reusable instructions for users' projects.
- Keep `.claude/skills/autonomous-dev-loop/SKILL.md` focused on the installable Claude Skill.
- Do not merge these three roles.

## Contribution Rules

- Write in English.
- Keep the Skill generic and stack-agnostic.
- Avoid private, company-specific, product-specific, ERP-specific, or CRM-specific assumptions.
- Keep autonomous loop behavior aligned with the existing Skill references.
- Do not create installer scripts yet.
- Keep the Claude Skill behaviorally equivalent to the Codex/OpenAI Skill.
- Update `CHANGELOG.md` when making notable changes.

## Versioning

Use semantic versioning.

Commit and release titles should use only the version number, for example:

```text
0.0.1
```
