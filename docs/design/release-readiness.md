# Release Readiness

This document defines the initial criteria for considering an `autonomous-dev-loop` version ready to merge or release.

## Release-Ready Criteria

A version is release-ready when:

- Skill targets validate.
- Skill targets remain behaviorally equivalent.
- `references/` filenames and contents match across Skill targets.
- `assets/` filenames and contents match across Skill targets.
- Installation docs exist and match the current repository structure.
- Lightweight usage examples exist.
- `CHANGELOG.md` is updated for the version.
- `README.md` status is accurate.
- No obvious private, company-specific, environment-specific, or secret-like content is present.
- GitHub Actions validation is passing.
- Manual review is complete.

## Required Local Checks

Run:

```bash
python scripts/validate_repository.py
python scripts/check_skill_equivalence.py
python scripts/check_private_content.py
```

Also run a local Skill validator when available.

## Manual Review Checklist

Before merging or releasing, review:

- `README.md`
- `CHANGELOG.md`
- `docs/installation/`
- `docs/design/`
- `docs/planning/`
- `.agents/skills/autonomous-dev-loop/`
- `.claude/skills/autonomous-dev-loop/`
- `examples/`

Confirm:

- No installer scripts were added unless intentionally planned for the version.
- No complete example applications were added unless intentionally planned for the version.
- No external dependencies were introduced accidentally.
- No platform feature is described as universal when it is environment-dependent.
- No `/goal` support is claimed as universal.
- No real subagent support is claimed as universal.

## Versioning Rules

Use semantic versioning.

Commit and release titles should use only the version number, such as:

```text
0.0.9
```

## Current Release Automation Boundary

Version `0.0.9` includes validation workflow planning and a GitHub Actions validation workflow.

It does not include:

- Release automation
- Package publishing
- Installer scripts
- Marketplace publishing
- Generated release artifacts

## Future Release Work

Future versions may add:

- Release candidate checklist
- Release packaging workflow
- Generated archives for each Skill target
- Equivalence snapshot reports
- Example project smoke tests
- Installer validation
- Marketplace or plugin packaging when supported
