# Contributing

Thanks for helping improve `autonomous-dev-loop`.

This project is in early planning. Contributions should keep the repository clear, generic, and useful for public agent-skill development.

## Current Scope

Version `0.0.1` is focused on planning and scaffolding.

Do not implement the full autonomous development loop behavior until the internal Skill architecture and core behavior are defined in a later planning step.

## Guidelines

- Write documentation and Skill content in English.
- Keep the project stack-agnostic.
- Avoid private, company-specific, environment-specific, ERP-specific, or CRM-specific content.
- Keep installable Skill folders focused and minimal.
- Put design, planning, installation, and contribution notes in `docs/` or root-level files.
- Keep the Codex/OpenAI and Claude Skill versions behaviorally equivalent.
- Update `CHANGELOG.md` for notable changes.

## Repository Areas

- `.agents/skills/autonomous-dev-loop/`: Codex/OpenAI Skill target.
- `.claude/skills/autonomous-dev-loop/`: Claude Code Skill target.
- `adapters/`: reusable templates for users' projects.
- `docs/`: planning, design, and installation documentation.
- `examples/`: future example projects and walkthroughs.

## Versioning

Use semantic versioning.

Commit and release titles should use only the version number, for example:

```text
0.0.1
```

## Roadmap Discipline

Avoid adding scripts, automation, examples, or detailed Skill behavior before the relevant planning step defines their scope.
