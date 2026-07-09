# Release Notes 0.0.11 Draft

Status: **Draft**

These notes are a draft for the first release candidate review. They are not a published GitHub release.

## Overview

`autonomous-dev-loop` is a reusable agent Skill for structured autonomous software development loops with safety gates, validation, review, persistent memory, and final reporting.

Version `0.0.11` prepares the project for first release candidate review by organizing the public README, release checklist, install positioning, and pre-release documentation.

## What Is Included

- Codex/OpenAI Skill target
- Claude Code Skill target
- Generic agent adapter templates
- Project control file templates
- Objective intake and kickoff protocol
- Goal Completion Mode
- Autonomy levels and safety gates
- Review Subagent Loop with independent review-pass fallback
- Stack detection and command discovery guidance
- Persistent memory and continuation handoff
- Python installer with install, update, and uninstall actions
- Shell and PowerShell installer wrappers
- Local release packaging script
- Repository validation scripts
- GitHub Actions validation and package checks
- Lightweight usage examples

## Installation

One-command install from `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

This installs the latest version from the `main` branch. For reproducible installs, use a tagged release when available.

Safer inspect-first pattern:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target codex --scope project
```

Local installer:

```bash
python3 scripts/install.py --target codex --scope project
python3 scripts/install.py --target claude --scope project
python3 scripts/install.py --target both --scope project
python3 scripts/install.py --target generic --scope project
```

## Supported Targets

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/`
- Claude Code: `.claude/skills/autonomous-dev-loop/`
- Both Skill targets
- Generic adapter templates

## Known Limitations

- No GitHub release is published yet.
- No branch has been merged to `main` as part of this step.
- No marketplace or plugin package is published.
- Example folders contain documentation examples, not complete applications.
- Real review subagents are environment-dependent.
- Native `/goal` support is environment-dependent.
- One-command install uses the latest `main` branch and is less reproducible than a tagged release.

## Validation Status

Release candidate validation should include:

```bash
python3 scripts/install.py --help
python3 scripts/test_installer.py
python3 scripts/package_release.py --version 0.0.11 --clean
python3 scripts/test_packaging.py
python3 scripts/validate_repository.py
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
```

Both Skill targets should also pass the local Skill validator when available.

## Upgrade And Update Notes

Update an existing Codex/OpenAI project install:

```bash
python3 scripts/install.py --action update --target codex --scope project --yes
```

Update an existing Claude Code project install:

```bash
python3 scripts/install.py --action update --target claude --scope project --yes
```

Run a dry-run before updating when reviewing changes:

```bash
python3 scripts/install.py --action update --target both --scope project --dry-run
```

## Next Planned Improvements

- Final pre-merge review
- Release candidate validation
- PR preparation
- First tagged release
- More example walkthroughs
- Additional release packaging polish
