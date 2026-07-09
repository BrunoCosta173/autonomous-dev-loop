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
- Installer tests pass.
- Packaging tests pass.
- Expected release zip packages can be generated locally.
- Release candidate checklist is reviewed.
- GitHub Actions validation is passing.
- Manual review is complete.

## Required Local Checks

Run:

```bash
python scripts/validate_repository.py
python scripts/check_skill_equivalence.py
python scripts/check_private_content.py
python scripts/test_installer.py
python scripts/package_release.py --version 0.0.11 --clean
python scripts/test_packaging.py
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

- Installer scripts remain dependency-free, conservative, and readable.
- No complete example applications were added unless intentionally planned for the version.
- No external dependencies were introduced accidentally.
- No platform feature is described as universal when it is environment-dependent.
- No `/goal` support is claimed as universal.
- No real subagent support is claimed as universal.
- Marketplace or plugin packaging is documented only as future ecosystem-dependent work.
- Public README one-command install uses `main` as the latest channel.
- Agent-assisted installation documentation prefers manual or local installer workflows.
- Tagged releases are recommended for reproducible installs when available.

## Versioning Rules

Use semantic versioning.

Commit and release titles should use only the version number, such as:

```text
0.0.11
```

## Current Release Automation Boundary

Version `0.0.11` includes release-candidate README structure, release checklist, draft release notes, local installer, update, uninstall, and package-generation scripts plus GitHub Actions validation and packaging checks.

It does not include:

- Release automation
- Package publishing
- Marketplace publishing
- Automatic GitHub release creation

## Release Candidate Checklist

Use `docs/release/RELEASE_CANDIDATE_CHECKLIST.md` before merging to `main` or publishing a tagged release.

The checklist covers required checks, manual smoke tests, and release blockers.

## Future Release Work

Future versions may add:

- Release candidate checklist
- Generated archives for each Skill target
- Equivalence snapshot reports
- Example project smoke tests
- Installer validation
- Marketplace or plugin packaging when supported
