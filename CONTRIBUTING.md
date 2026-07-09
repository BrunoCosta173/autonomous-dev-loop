# Contributing

Thanks for helping improve `autonomous-dev-loop`.

This project is in the public `0.1.x` release line. It is early, but usable.

## Current Scope

The repository includes:

- Codex/OpenAI Skill target
- Claude Code Skill target
- Generic agent adapters
- Project control file templates
- Dependency-free installer
- Release packaging
- Validation scripts
- GitHub Actions validation
- Documentation-only examples

Complete example applications, marketplace packaging, and broad Skill redesigns should be proposed before implementation.

## Contribution Guidelines

- Write documentation and Skill content in English.
- Keep the project stack-agnostic and useful across common software projects.
- Avoid private, company-specific, environment-specific, ERP-specific, CRM-specific, or confidential content.
- Preserve behavioral equivalence between Codex/OpenAI and Claude Skill targets.
- Keep installable Skill folders focused on Skill content.
- Keep installer, packaging, and validation scripts dependency-free unless a future proposal explicitly changes that policy.
- Update `CHANGELOG.md` for notable changes.
- Do not modify, delete, replace, unpublish, rewrite, or move already published releases or tags.
- Do not force-push shared release branches or tags.

## Before Opening A Pull Request

Run the local validation suite:

```bash
python3 scripts/install.py --help
python3 scripts/test_installer.py
python3 scripts/package_release.py --version <version> --clean
python3 scripts/test_packaging.py
python3 scripts/validate_repository.py
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
git diff --check
```

Also validate both Skill targets with a local Skill validator when available.

## Repository Areas

- `.agents/skills/autonomous-dev-loop/`: Codex/OpenAI Skill target.
- `.claude/skills/autonomous-dev-loop/`: Claude Code Skill target.
- `adapters/`: reusable templates for users' projects.
- `docs/`: planning, design, installation, release, and validation documentation.
- `examples/`: lightweight documentation examples, not complete apps.
- `scripts/`: dependency-free installer, packaging, validation, and tests.

## Versioning

Use semantic versioning.

Commit and release titles should use only the version number, for example:

```text
0.1.1
```

Patch releases should be used for focused fixes that do not alter the core Skill model.

## Pull Request Expectations

- Explain the objective and scope.
- List validation commands run.
- Mention whether Skill references or assets changed.
- Note any safety, installation, or compatibility impact.
- Keep changes focused and reviewable.
