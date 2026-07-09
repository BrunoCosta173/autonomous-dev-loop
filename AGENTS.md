# Agent Instructions For This Repository

These instructions are for AI coding agents contributing to the `autonomous-dev-loop` repository itself.

They are not the reusable adapter instructions for end-user projects. User-facing adapter templates live in `adapters/`.

## Project Status

The project is in release-candidate preparation for the first public release.

- Steps 0 through 11 are complete.
- Step 12 is the final pre-merge review and PR preparation step.
- Installer scripts, Skill assets, validation scripts, release packaging, installation docs, and lightweight example documentation are implemented.
- Complete example applications and release publishing are intentionally not implemented yet.

## Repository Goals

`autonomous-dev-loop` is a public, reusable agent skill for controlled autonomous software development loops.

The Skill guides:

```text
Objective intake -> project inspection -> planning -> ToDo generation -> execution -> testing -> repair -> documentation -> final report
```

## Contribution Rules

- Keep all content in English.
- Keep the project generic and public GitHub-ready.
- Do not add private, company-specific, or environment-specific information.
- Keep autonomous loop behavior aligned with the existing Skill references.
- Keep installer, validation, and packaging tooling dependency-free unless a future step explicitly changes that policy.
- Do not publish releases, create tags, merge branches, or open pull requests unless the user explicitly requests that action.
- Preserve behavioral equivalence between the Codex/OpenAI and Claude Skill versions.
- Keep Skill folders focused on installable Skill content.
- Put planning, installation, design, and contribution documentation under `docs/` or root-level files.

## File Roles

- Root `AGENTS.md`: instructions for AI agents working on this repository.
- Root `CLAUDE.md`: instructions for Claude Code working on this repository.
- `adapters/`: reusable templates for users to copy into their own projects.
- `.agents/skills/autonomous-dev-loop/`: Codex/OpenAI Skill installation target.
- `.claude/skills/autonomous-dev-loop/`: Claude Code Skill installation target.

## Versioning

Use semantic versioning.

Commit and release titles should use only the version number, such as:

```text
0.0.1
```

Update `CHANGELOG.md` for notable changes.
