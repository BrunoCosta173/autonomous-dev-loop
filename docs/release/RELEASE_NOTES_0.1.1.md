# Release Notes 0.1.1

Status: **Patch release candidate**

## Overview

`autonomous-dev-loop` `0.1.1` is a focused post-release patch candidate after the first public `0.1.0` release.

The existing `v0.1.0` release remains unchanged. This patch prepares follow-up fixes based on an external OpenCode + DeepSeek V4 Pro audit.

## What Changed

- Fixed stale `CONTRIBUTING.md` language from the planning-only phase.
- Refreshed `PROJECT_BRIEF.md` to reflect the public `0.1.x` release line.
- Improved README structure, scanability, badges, install sections, compatibility, safety, and documentation links.
- Reconciled loop protocol consistency by adding explicit `Kickoff` to the detailed loop.
- Defined the default maximum autonomous cycles as 10.
- Clarified that one-command `curl | sh` installation is Linux/macOS-oriented.
- Clarified that Windows users should use clone plus `python scripts/install.py`, or local `install.ps1` after inspection.
- Added data exfiltration and external transmission as explicit safety gates.
- Added guidance for runs where no validation commands are available.
- Added GitHub issue templates.
- Added `CODE_OF_CONDUCT.md`.
- Added SHA256 checksum generation for release packages.
- Added adapter fallback guidance when Skill folders are unavailable.
- Added a control-file clutter limit for autonomous runs.

## Installation

One-command install from `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

This form is Linux/macOS-oriented. Windows users should clone the repository and run:

```powershell
python scripts/install.py --target codex --scope project
```

or inspect and run local `install.ps1`.

For reproducible installs, use a tagged release when available.

## Supported Targets

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/`
- Claude Code: `.claude/skills/autonomous-dev-loop/`
- Generic adapters: `AGENTS.md`, `CLAUDE.md`, and `GENERIC_AGENT.md`

## Validation Status

Release validation should include:

```bash
python3 scripts/install.py --help
python3 scripts/test_installer.py
python3 scripts/package_release.py --version 0.1.1 --clean
python3 scripts/test_packaging.py
python3 scripts/validate_repository.py
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
git diff --check
git ls-files dist
```

Both Skill targets should also pass the local Skill validator when available.

## Package Checksums

The packaging script now generates `.sha256` files next to each release zip:

```text
dist/autonomous-dev-loop-0.1.1.zip
dist/autonomous-dev-loop-0.1.1.zip.sha256
dist/autonomous-dev-loop-codex-0.1.1.zip
dist/autonomous-dev-loop-codex-0.1.1.zip.sha256
dist/autonomous-dev-loop-claude-0.1.1.zip
dist/autonomous-dev-loop-claude-0.1.1.zip.sha256
dist/autonomous-dev-loop-adapters-0.1.1.zip
dist/autonomous-dev-loop-adapters-0.1.1.zip.sha256
```

Checksum format:

```text
<sha256>  <filename>
```

## Known Limitations

- Real review subagents are environment-dependent.
- Native `/goal` support is environment-dependent.
- Windows one-command PowerShell install is not implemented.
- Example folders contain documentation examples, not complete applications.
- Marketplace or plugin packaging is not published.

## Upgrade And Update Notes

Update an existing project install:

```bash
python3 scripts/install.py --action update --target both --scope project --yes
```

Preview first:

```bash
python3 scripts/install.py --action update --target both --scope project --dry-run
```

## Next Planned Improvements

- Merge the `0.1.1` patch PR after checks pass.
- Validate `main`.
- Create annotated tag `v0.1.1`.
- Generate packages and checksums.
- Create a GitHub release or draft release for `v0.1.1`.
- Leave `v0.1.0` untouched.
