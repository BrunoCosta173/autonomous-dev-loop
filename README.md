# autonomous-dev-loop

[![Validate](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/validate.yml/badge.svg)](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/validate.yml)
[![Package](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/package.yml/badge.svg)](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/package.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/BrunoCosta173/autonomous-dev-loop?label=release)](https://github.com/BrunoCosta173/autonomous-dev-loop/releases)
[![Skills](https://img.shields.io/badge/AI%20Agent%20Skill-Codex%20%7C%20Claude%20Code%20%7C%20Generic-blue)](#compatibility)

A structured autonomous development loop for AI coding agents.

Turn a development objective into a controlled agent workflow:

```text
intake -> kickoff -> plan -> todo -> execute -> test -> repair -> review -> document -> continue safely
```

AI coding agents are powerful, but they can drift, skip tests, forget context, or declare work done too early.

`autonomous-dev-loop` gives agents a repeatable operating system for software work: clear objectives, bounded autonomy, safety gates, review rounds, persistent memory, and final reports.

Current development version: `0.1.1`

## Quick Links

| Section | Description |
| --- | --- |
| [Quick install](#quick-install) | Install with one command |
| [How it works](#how-it-works) | Understand the development loop |
| [Usage examples](#usage-examples) | Prompts you can copy |
| [Compatibility](#compatibility) | Codex, Claude Code, and generic agents |
| [Safety model](#safety-model) | Safety gates and approval rules |
| [Documentation](#documentation) | Full docs and references |

## Quick Install

> Installs the latest version from `main`.
> For reproducible installs, use a tagged release when available.

The one-command install path is Linux/macOS-oriented and uses `curl | sh`. Windows users should clone the repository and run `python scripts/install.py`, or use local `install.ps1` after inspecting it.

### Codex / OpenAI Skills

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

### Claude Code

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target claude --scope project
```

### Both

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target both --scope project
```

### Safer Install

Remote script execution is convenient, not safer. Inspect first when security matters:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target codex --scope project
```

## Features

| Feature | What It Does |
| --- | --- |
| Goal Completion Mode | Treats a user objective as the active goal and drives it toward completion |
| Safety Gates | Stops before risky actions like destructive commands, secrets, auth, database, deployment, or data exfiltration |
| Review Subagent Loop | Uses real subagents when available, or independent review passes as fallback |
| Persistent Memory | Uses project control files to preserve context across sessions |
| Stack Detection | Inspects project files and commands instead of assuming a stack |
| Installer | Supports install, update, uninstall, dry-run, project scope, and user scope |
| Dual Skill Targets | Supports Codex/OpenAI Skills and Claude Code Skills |

## Compatibility

Compatibility depends on the current agent environment. Native Skill support, real subagents, and long-run goal modes are not universal.

| Target | Skill Path | Best For |
| --- | --- | --- |
| Codex / OpenAI | `.agents/skills/autonomous-dev-loop/` | Codex CLI, Codex Desktop/App, OpenAI Skills-style agents |
| Claude Code | `.claude/skills/autonomous-dev-loop/` | Claude Code CLI/Desktop |
| Generic agents | `AGENTS.md` / `GENERIC_AGENT.md` adapters | Agents without native Skill support |

## How It Works

This is the detailed Skill protocol:

```text
1. Objective intake
2. Kickoff
3. Project inspection
4. Stack and command discovery
5. Execution plan
6. ToDo generation
7. Implementation
8. Validation
9. Repair
10. Review Subagent Loop
11. Documentation
12. Handoff
13. Continue or stop
```

The simplified flow at the top of this README is only a public overview.

## For Humans

Use one-command install, then ask your coding agent to use `autonomous-dev-loop` with a clear development objective.

Good objectives name the target area, desired outcome, constraints, and validation expectations.

## For Agents

Prefer transparent installation:

1. Inspect the repository.
2. Confirm the target agent: Codex/OpenAI, Claude Code, both, or generic.
3. Use the local installer or manually copy the correct Skill folder.
4. Do not pipe remote scripts unless explicitly authorized.
5. Do not overwrite existing `AGENTS.md` or `CLAUDE.md` without asking.
6. Verify installation and summarize what changed.

See [agent-assisted installation](docs/installation/agent-assisted-installation.md).

## Install Locally

From a local clone:

```bash
python3 scripts/install.py --target codex --scope project
python3 scripts/install.py --target claude --scope project
python3 scripts/install.py --target both --scope project
python3 scripts/install.py --target generic --scope project
```

Preview first:

```bash
python3 scripts/install.py --target both --scope project --dry-run
```

Update:

```bash
python3 scripts/install.py --action update --target both --scope project --yes
```

Uninstall dry-run:

```bash
python3 scripts/install.py --action uninstall --target codex --scope project --dry-run
```

## Usage Examples

```text
Use autonomous-dev-loop to improve the user settings page.
Focus on UI consistency, validation, loading states, and accessibility.
Do not change database schema, authentication, or dependencies.
Use A3 autonomy.
```

```text
Use autonomous-dev-loop to add tests for the orders API.
Focus on request validation, success responses, and error cases.
Do not change database schema or authentication rules.
Run available test and lint commands.
```

```text
Use autonomous-dev-loop to review this module and create a prioritized ToDo list.
Do not edit files yet. Use A0 autonomy.
```

```text
Use autonomous-dev-loop to continue the previous run from TODO.md and DEVELOPMENT_LOG.md.
Ask only blocking questions.
Stop at safety gates.
```

## Safety Model

`autonomous-dev-loop` is designed for autonomy with guardrails.

The agent must stop and ask for approval before actions involving:

- destructive commands
- mass deletion
- database migrations with data-loss risk
- authentication or permission changes
- secrets or environment variables
- deployment
- major architecture rewrites
- critical dependencies
- licensing changes
- external data transmission or data exfiltration

## Review Before Done

The agent should not declare work complete immediately after coding.

Before completion, it runs a review cycle:

```text
implementation -> validation -> review -> score -> fix -> revalidate -> final report
```

When real subagents are available, they can be used as read-only reviewers.
When they are not available, the agent performs independent review passes using the same reviewer roles and rubrics.

## Persistent Memory

The Skill can create or update project control files when useful:

- `TODO.md`
- `DEVELOPMENT_LOG.md`
- `TEST_PLAN.md`
- `DECISIONS.md`
- `KNOWN_ISSUES.md`
- `FINAL_REPORT.md`
- `BACKLOG.md`
- `ROADMAP.md`

It should not force every file into every project. By default, it should not create more than 3 project control files in one run unless the user explicitly requests more or the objective clearly requires it.

## Validation And Packaging

Run local validation:

```bash
python3 scripts/validate_repository.py
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
python3 scripts/test_installer.py
python3 scripts/test_packaging.py
```

Generate release packages and SHA256 checksums:

```bash
python3 scripts/package_release.py --version 0.1.1 --clean
```

Expected package examples:

```text
dist/autonomous-dev-loop-0.1.1.zip
dist/autonomous-dev-loop-0.1.1.zip.sha256
dist/autonomous-dev-loop-codex-0.1.1.zip
dist/autonomous-dev-loop-codex-0.1.1.zip.sha256
```

## Documentation

| Document | Purpose |
| --- | --- |
| [Installation: Codex/OpenAI](docs/installation/codex-openai.md) | Install for Codex/OpenAI Skills |
| [Installation: Claude Code](docs/installation/claude-code.md) | Install for Claude Code |
| [Generic agents](docs/installation/generic-agents.md) | Use adapters with other agents |
| [Compatibility matrix](docs/design/compatibility-matrix.md) | Supported targets and fallbacks |
| [Validation strategy](docs/design/validation-strategy.md) | Local and CI validation |
| [Release readiness](docs/design/release-readiness.md) | Release checklist and criteria |
| [Release checklist](docs/release/RELEASE_CANDIDATE_CHECKLIST.md) | Pre-release checks |
| [Release notes 0.1.1](docs/release/RELEASE_NOTES_0.1.1.md) | Patch release notes |

## Limitations

- Real subagent support is environment-dependent.
- Native `/goal` support is environment-dependent.
- One-command install is Linux/macOS-oriented.
- Example folders are documentation examples, not complete applications.
- Marketplace or plugin packaging is not currently published.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

Keep content public, generic, and stack-agnostic. Preserve behavioral equivalence between Codex/OpenAI and Claude Skill targets.

## License

MIT. See [LICENSE](LICENSE).
