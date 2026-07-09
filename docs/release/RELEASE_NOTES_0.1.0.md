# Release Notes 0.1.0

Status: **Draft release notes for the first public release**

## Overview

`autonomous-dev-loop` `0.1.0` is the first public release candidate/stable initial release.

It provides a reusable Skill and instruction system for objective-driven autonomous software development loops with safety gates, validation, review rounds, persistent project memory, and final reporting.

## Key Features

- Codex/OpenAI Skill target
- Claude Code Skill target
- Generic AI coding agent adapters
- Goal Completion Mode for user-provided development objectives
- Autonomy levels from manual planning through continuous autonomous loops
- Safety gates for destructive, sensitive, deployment, permission, secret, and ambiguous product changes
- Review Subagent Loop with independent review-pass fallback when real subagents are unavailable
- Stack-agnostic stack detection and command discovery guidance
- Project control file templates for ToDos, logs, test plans, decisions, known issues, and final reports
- Persistent memory and cross-session handoff guidance
- Dependency-free Python installer
- Shell and PowerShell wrappers
- Local release package generation
- Repository validation, Skill equivalence checks, and private-content scanning
- GitHub Actions validation and packaging workflows

## Installation

One-command install from `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

Claude Code install:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target claude --scope project
```

Install both Skill targets:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target both --scope project
```

The `main` branch is the latest channel. For reproducible installs, use a tagged release when available.

Inspect-first pattern:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target codex --scope project
```

## Supported Targets

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/`
- Claude Code: `.claude/skills/autonomous-dev-loop/`
- Both Skill targets
- Generic adapters: `AGENTS.md`, `CLAUDE.md`, and `GENERIC_AGENT.md` templates

## Installer Commands

Install:

```bash
python3 scripts/install.py --target codex --scope project
python3 scripts/install.py --target claude --scope project
python3 scripts/install.py --target both --scope project
python3 scripts/install.py --target generic --scope project
```

Update:

```bash
python3 scripts/install.py --action update --target both --scope project --yes
```

Uninstall dry-run:

```bash
python3 scripts/install.py --action uninstall --target codex --scope project --dry-run
```

## Validation Status

Release validation should include:

```bash
python3 scripts/install.py --help
python3 scripts/test_installer.py
python3 scripts/package_release.py --version 0.1.0 --clean
python3 scripts/test_packaging.py
python3 scripts/validate_repository.py
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
git diff --check
```

Both Skill targets should also pass the local Skill validator when available.

## Known Limitations

- Real review subagents are environment-dependent and are not guaranteed.
- Native `/goal` support is environment-dependent and is not assumed.
- Example folders contain lightweight documentation examples, not complete applications.
- Marketplace or plugin packaging is not published.
- One-command install from `main` follows the latest branch state; tagged releases are preferred for reproducible installs.

## Upgrade And Update Notes

Update an existing Codex/OpenAI install:

```bash
python3 scripts/install.py --action update --target codex --scope project --yes
```

Update an existing Claude Code install:

```bash
python3 scripts/install.py --action update --target claude --scope project --yes
```

Preview an update first:

```bash
python3 scripts/install.py --action update --target both --scope project --dry-run
```

## Next Planned Improvements

- Verify one-command install from `main` after release review.
- Add more example walkthroughs.
- Add deeper release validation around generated packages.
- Add optional sync tooling for Skill target maintenance if needed.
- Explore marketplace or plugin packaging only if supported by the relevant agent ecosystem.
