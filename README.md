# autonomous-dev-loop

[![Validate](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/validate.yml/badge.svg)](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/validate.yml)
[![Package](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/package.yml/badge.svg)](https://github.com/BrunoCosta173/autonomous-dev-loop/actions/workflows/package.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/BrunoCosta173/autonomous-dev-loop?label=release)](https://github.com/BrunoCosta173/autonomous-dev-loop/releases)
[![Skills](https://img.shields.io/badge/AI%20Agent%20Skill-Codex%20%7C%20Claude%20Code%20%7C%20Generic-blue)](#compatibility)

A structured autonomous development loop for AI coding agents.

`autonomous-dev-loop` is a reusable Skill and instruction system that gives AI coding agents a repeatable operating system for software work.

Instead of jumping straight into edits and hoping the agent stays on track, the Skill guides the agent through clear objectives, bounded autonomy, safety gates, review rounds, persistent memory, and final reports.

Current version: `0.1.2`

## Why this exists

AI coding agents can move quickly, but they can also drift, skip tests, forget context, or declare work done too early.

`autonomous-dev-loop` exists to make agents more autonomous without making them reckless. It wraps every development run in structure so the agent:

- understands the objective before editing files;
- inspects the project and detects the stack;
- creates a plan and executable ToDo list;
- runs available validation and repairs failures;
- reviews the changed scope before declaring completion;
- documents what changed, what was deferred, and what needs attention next.

## Quick Install

> Installs the latest version from `main`.
> For reproducible installs, use a tagged release.

One-command install is Linux/macOS-oriented (`curl | sh`). Windows users should clone the repository and run `python scripts/install.py`, or use `install.ps1` locally after inspecting it.

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

### Safer install

Remote script execution is convenient, not safer. Inspect first when security matters:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target codex --scope project
```

## What this installs

Depending on the target you choose, the installer adds one or more Skill folders or adapter files to your project:

| Target | Installed files | Purpose |
|---|---|---|
| Codex / OpenAI | `.agents/skills/autonomous-dev-loop/` | Native Skill target for Codex/OpenAI-style agents |
| Claude Code | `.claude/skills/autonomous-dev-loop/` | Native Skill target for Claude Code |
| Generic agents | `AGENTS.md`, `CLAUDE.md`, or `GENERIC_AGENT.md` adapters | Lightweight instructions for agents without native Skill support |

The installer does not install application dependencies, modify your app code, run database migrations, deploy anything, or change your project behavior by itself.

It only installs instructions and templates that your AI coding agent can use when you ask it to run an autonomous development loop.

## What it does

`autonomous-dev-loop` gives an AI coding agent a structured way to work on software tasks.

Instead of jumping straight into edits, the agent is instructed to:

1. understand the objective;
2. inspect the project;
3. detect the stack and available commands;
4. create a plan and ToDo list;
5. execute changes in controlled steps;
6. run available validation;
7. repair issues found during validation;
8. review the changed scope;
9. document what changed;
10. stop, continue, or hand off safely.

The goal is not to make the agent reckless. The goal is to make it more autonomous while keeping it bounded, reviewable, and safer.

## How to use it after installing

After installation, ask your coding agent to use `autonomous-dev-loop` with a clear development objective.

```text
Use autonomous-dev-loop to improve the settings page.
Focus on layout consistency, form validation, loading states, and accessibility.
Do not change authentication, database schema, or dependencies.
Use A3 autonomy.
```

The agent should then:

- inspect your project;
- create a short objective brief;
- create or update a ToDo list when useful;
- make changes inside the requested scope;
- run available checks;
- review the result;
- summarize what changed and what still needs attention.

## When to use it

Use `autonomous-dev-loop` for tasks that benefit from structure:

| Good fit | Examples |
|---|---|
| Multi-step implementation | Add a feature, refactor a module, improve a page |
| Review and repair | Audit a module, fix validation issues, improve tests |
| UI/UX cleanup | Improve forms, states, layout, accessibility |
| Test coverage | Add tests around existing behavior |
| Documentation work | Update docs consistently across files |
| Project continuation | Continue from TODOs, logs, or previous handoffs |

## When not to use it

You probably do not need the full loop for:

- one-line code answers;
- quick explanations;
- simple syntax questions;
- small copy edits;
- tasks where you only want advice and no file changes.

For those cases, ask your agent normally or use A0/A1 autonomy.

## How the loop works

The Skill protocol runs a structured cycle:

```text
objective
  |
  v
intake + kickoff
  |
  v
inspect project + detect stack
  |
  v
plan + ToDos
  |
  v
execute changes
  |
  v
validate + repair
  |
  v
review changed scope
  |
  v
document + final report
  |
  v
continue, stop, or hand off
```

The exact depth of the loop depends on the task. Small tasks stay lightweight. Larger tasks can use persistent project memory, review rounds, and handoff files.

## Safety model

`autonomous-dev-loop` is designed for bounded autonomy with guardrails.

It does not give the agent permission to do everything. The agent must stop and request human confirmation before actions involving:

- destructive commands;
- mass deletion;
- database migrations with data-loss risk;
- authentication or permission changes;
- secrets or environment variables;
- deployment;
- major architecture rewrites;
- critical dependency changes;
- licensing changes;
- external data transmission or data exfiltration;
- removing tests or disabling validation tools to pass checks.

Safety gates are not an optional add-on. They are part of the core design.

## Project control files

For larger tasks, the agent may create or update lightweight control files. The Skill should not create every file by default — only files that are useful for the current objective.

| File | Purpose |
|---|---|
| `TODO.md` | Tracks planned and completed work |
| `DEVELOPMENT_LOG.md` | Records important implementation notes across cycles |
| `TEST_PLAN.md` | Documents validation strategy and known gaps |
| `KNOWN_ISSUES.md` | Tracks known problems and deferred items |
| `FINAL_REPORT.md` | Summarizes a completed autonomous run |
| `BACKLOG.md` | Records out-of-scope findings and future ideas |
| `ROADMAP.md` | Captures high-level project direction |
| `DECISIONS.md` | Logs architecture and product decisions |

The agent should not create more than 3 control files in one run unless the user explicitly requests more or the objective requires it.

## Review before done

The agent should not declare work complete immediately after coding.

Before completion, it runs a review cycle:

```text
implementation -> validation -> review -> score -> fix -> revalidate -> final report
```

When real subagents are available, they can be used as read-only reviewers. When they are not available, the agent performs independent review passes using the same reviewer roles and rubrics.

Real subagent support is environment-dependent and is not claimed as universal.

## Compatibility

Compatibility depends on the current agent environment. Native Skill support, real subagents, and long-run goal modes are not universal.

| Target | Skill Path | Best For |
|---|---|---|
| Codex / OpenAI | `.agents/skills/autonomous-dev-loop/` | Codex CLI, Codex Desktop/App, OpenAI Skills-style agents |
| Claude Code | `.claude/skills/autonomous-dev-loop/` | Claude Code CLI/Desktop |
| Generic agents | `AGENTS.md` / `GENERIC_AGENT.md` adapters | Agents without native Skill support |

## Usage examples

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
Use autonomous-dev-loop to review the checkout flow.
Do not edit files yet.
Create a prioritized list of issues and suggested fixes.
Use A0 autonomy.
```

```text
Use autonomous-dev-loop to continue the previous run from TODO.md and DEVELOPMENT_LOG.md.
Stay within the existing objective. Ask only blocking questions.
Run available validation commands and produce a final report.
```

## For Agents

When an AI coding agent is asked to install `autonomous-dev-loop`, it should prefer transparent installation instead of piping remote scripts into a shell.

1. Inspect the repository.
2. Confirm the target: Codex/OpenAI, Claude Code, both, or generic.
3. Use the local installer or manually copy the correct Skill folder.
4. Do not pipe remote scripts unless explicitly authorized.
5. Do not overwrite existing `AGENTS.md` or `CLAUDE.md` without asking.
6. Verify installation and summarize what changed.

See [agent-assisted installation](docs/installation/agent-assisted-installation.md).

## Install locally

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

Uninstall:

```bash
python3 scripts/install.py --action uninstall --target codex --scope project --dry-run
```

## Validation and packaging

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
python3 scripts/package_release.py --version 0.1.2 --clean
```

Expected output:

```text
dist/autonomous-dev-loop-0.1.2.zip
dist/autonomous-dev-loop-0.1.2.zip.sha256
dist/autonomous-dev-loop-codex-0.1.2.zip
dist/autonomous-dev-loop-codex-0.1.2.zip.sha256
dist/autonomous-dev-loop-claude-0.1.2.zip
dist/autonomous-dev-loop-claude-0.1.2.zip.sha256
dist/autonomous-dev-loop-adapters-0.1.2.zip
dist/autonomous-dev-loop-adapters-0.1.2.zip.sha256
```

## Documentation

| Document | Purpose |
|---|---|
| [Installation: Codex/OpenAI](docs/installation/codex-openai.md) | Install for Codex/OpenAI Skills |
| [Installation: Claude Code](docs/installation/claude-code.md) | Install for Claude Code |
| [Generic agents](docs/installation/generic-agents.md) | Use adapters with other agents |
| [Agent-assisted installation](docs/installation/agent-assisted-installation.md) | Install the Skill using an AI coding agent |
| [Compatibility matrix](docs/design/compatibility-matrix.md) | Supported targets and fallbacks |
| [Validation strategy](docs/design/validation-strategy.md) | Local and CI validation |
| [Release readiness](docs/design/release-readiness.md) | Release checklist and criteria |
| [Release checklist](docs/release/RELEASE_CANDIDATE_CHECKLIST.md) | Pre-release verification steps |
| [Release notes 0.1.2](docs/release/RELEASE_NOTES_0.1.2.md) | Patch release notes |

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
