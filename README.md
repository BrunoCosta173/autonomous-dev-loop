# autonomous-dev-loop

Structured autonomous software development loops for AI coding agents.

`autonomous-dev-loop` is a reusable Skill and instruction system that helps AI coding agents plan, implement, test, repair, review, document, and continue software development work with clear safety gates.

Current version: `0.0.12`

## What It Does

`autonomous-dev-loop` turns a user-provided development objective into a controlled agent workflow:

```text
Objective intake -> project inspection -> planning -> ToDos -> execution -> validation -> repair -> review -> documentation -> final report
```

It is designed for:

- Developers who want more structured AI coding runs.
- Vibe-coders who want agents to keep moving without losing safety.
- Builders using Codex, Claude Code, or generic coding agents.
- Projects that need repeatable autonomous development loops across sessions.

## Why It Exists

AI coding agents can move quickly, but long development tasks often need more structure:

- Clear objective intake
- Scoped execution
- Validation before completion
- Safety gates for risky changes
- Review passes before final status
- Persistent memory for continuation
- Transparent final reporting

This project packages that operating model into installable Skill targets, adapter templates, validation scripts, installer tooling, and release-ready documentation.

## Key Features

- Objective-driven autonomous development loop
- Goal Completion Mode without requiring a universal `/goal` command
- Autonomy levels from manual planning to continuous autonomous loops
- Safety gates for destructive, sensitive, or ambiguous changes
- Review Subagent Loop with independent review-pass fallback
- Stack-agnostic stack and command detection guidance
- Persistent project memory templates
- Codex/OpenAI and Claude Code Skill targets
- Generic agent adapter templates
- Dependency-free Python installer
- Update and uninstall commands
- Local release package generation
- Repository validation and CI workflows

## How It Works

The Skill starts from a development objective, such as:

```text
Improve the user settings page.
```

The agent then:

1. Parses the objective and asks only blocking questions.
2. Inspects the project.
3. Detects the stack and available commands.
4. Creates a plan and executable ToDos.
5. Executes feasible work inside scope.
6. Runs relevant validation commands.
7. Repairs failures caused by its changes.
8. Runs review subagents when available, or independent review passes when not.
9. Updates project memory when useful.
10. Produces a final report.

The agent must stop for safety gates instead of silently performing high-risk work.

## Quick Install

For end users and vibe-coders, one-command install is the easiest path.

These commands install the latest version from the `main` branch. For reproducible installs, use a tagged release when available.

When run through a pipe, `install.sh` downloads the `main` branch archive to a temporary directory and then runs the dependency-free Python installer from that archive.

### Codex/OpenAI

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target codex --scope project
```

### Claude Code

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target claude --scope project
```

### Both Skill Targets

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh | sh -s -- --target both --scope project
```

One-command install is convenient, but it is still remote script execution. Inspect scripts before running them when security matters.

Safer inspect-first pattern:

```bash
curl -fsSL https://raw.githubusercontent.com/BrunoCosta173/autonomous-dev-loop/main/install.sh -o install.sh
cat install.sh
sh install.sh --target codex --scope project
```

## Install For Codex/OpenAI

Install into the current project:

```bash
python3 scripts/install.py --target codex --scope project
```

Install into a supported user-level location:

```bash
python3 scripts/install.py --target codex --scope user
```

Manual project-level install:

```bash
mkdir -p .agents/skills
cp -R path/to/autonomous-dev-loop/.agents/skills/autonomous-dev-loop .agents/skills/
```

Codex/OpenAI Skill folder:

```text
.agents/skills/autonomous-dev-loop/
```

See [Codex/OpenAI installation](docs/installation/codex-openai.md).

## Install For Claude Code

Install into the current project:

```bash
python3 scripts/install.py --target claude --scope project
```

Install into a supported user-level location:

```bash
python3 scripts/install.py --target claude --scope user
```

Manual project-level install:

```bash
mkdir -p .claude/skills
cp -R path/to/autonomous-dev-loop/.claude/skills/autonomous-dev-loop .claude/skills/
```

Claude Code Skill folder:

```text
.claude/skills/autonomous-dev-loop/
```

See [Claude Code installation](docs/installation/claude-code.md).

## Install For Generic Agents

Generic agents can use adapter templates when they do not support Skill folders.

Install adapters into the current project:

```bash
python3 scripts/install.py --target generic --scope project
```

Manual install:

```bash
cp path/to/autonomous-dev-loop/adapters/AGENTS.md ./AGENTS.md
```

Available adapters:

- `adapters/AGENTS.md`
- `adapters/CLAUDE.md`
- `adapters/GENERIC_AGENT.md`

See [generic agent installation](docs/installation/generic-agents.md).

## Agent-Assisted Installation

Agents should prefer transparent installation instead of piping remote scripts directly into a shell.

Recommended agent flow:

1. Inspect the repository.
2. Confirm the target agent: Codex/OpenAI, Claude Code, both, or generic.
3. Use the local installer or copy the proper folder.
4. Avoid overwriting existing project instructions without asking.
5. Verify installed files.
6. Report what changed.

Example prompt:

```text
Install autonomous-dev-loop for Codex/OpenAI in this project.
Use manual or local installer installation.
Do not pipe remote scripts into the shell.
Do not overwrite existing AGENTS.md or CLAUDE.md without asking.
Verify the installed Skill folder and summarize what changed.
```

See [agent-assisted installation](docs/installation/agent-assisted-installation.md).

## Basic Usage Examples

### UI Improvement

```text
Use autonomous-dev-loop to improve the user settings page.
Focus on UI consistency, form validation, loading states, and accessibility.
Do not change database schema, authentication, or dependencies.
Run available lint, typecheck, and build commands.
Use A3 autonomy.
```

### API Testing

```text
Use autonomous-dev-loop to add tests for the orders API.
Focus on request validation, success responses, and error cases.
Do not change database schema or authentication rules.
Run available test and lint commands.
Use A3 autonomy.
```

### Workflow Improvement

```text
Use autonomous-dev-loop to improve the invoice creation workflow.
Focus on validation, controller clarity, form request rules, and test coverage.
Do not change production migrations or payment logic without approval.
Run available framework validation commands.
Use A3 autonomy.
```

More examples:

- [Next.js app](examples/nextjs-app/README.md)
- [FastAPI API](examples/fastapi-api/README.md)
- [Laravel app](examples/laravel-app/README.md)

## Autonomy Levels

- `A0 — Manual`: the agent proposes plans and instructions only.
- `A1 — Assisted`: the agent inspects and proposes changes, but asks before editing.
- `A2 — Supervised`: the agent edits and validates in approved batches.
- `A3 — Autonomous With Safety Gates`: default recommended mode.
- `A4 — Continuous Autonomous Loop`: broad continuation inside the original objective, only when explicitly requested.

`A3` is the default. `A4` still stops at safety gates and must not expand beyond the user-provided objective.

## Safety Gates

The agent must stop and request confirmation before:

- Destructive commands
- Mass deletion
- Data-loss migrations
- Authentication, authorization, or permission changes
- Secret or environment variable handling
- Deployment
- Major architectural rewrites
- Framework replacement
- Business-critical rule changes
- Irreversible operations
- Ambiguous product decisions that materially affect behavior

Safety gates are part of the core design, not an optional add-on.

## Review Subagent Loop

Before declaring non-trivial work complete, the Skill requires review.

Primary mode:

- Use real review subagents when the current environment supports them.

Fallback mode:

- Run independent review passes with the same reviewer roles and rubrics.

Real subagent support is environment-dependent and is not claimed as universal.

## Goal Completion Mode

When the user invokes `autonomous-dev-loop` with a development objective, the agent treats that objective as the active goal and works toward completion.

The user does not need to type `/goal`.

If a platform has a native goal or long-run workflow, the agent may use it when appropriate. If not, the Skill emulates goal-oriented execution through ToDos, validation, review, documentation, and final reporting.

Native `/goal` support is not assumed to be universal.

## Persistent Project Memory

The Skill can create or update project control files when useful:

- `AGENTS.md`
- `CLAUDE.md`
- `BACKLOG.md`
- `ROADMAP.md`
- `TODO.md`
- `DEVELOPMENT_LOG.md`
- `TEST_PLAN.md`
- `DECISIONS.md`
- `KNOWN_ISSUES.md`
- `FINAL_REPORT.md`

It should not force every file into every project. These files are used when they improve continuity, traceability, or cross-session handoff.

## Supported Stacks

The Skill is stack-agnostic.

It detects project structure, stack, package managers, and validation commands from files such as:

- `package.json`, lockfiles, framework config files
- `pyproject.toml`, `requirements.txt`, `manage.py`
- `composer.json`, `artisan`
- `Gemfile`, Rails files
- `pom.xml`, Gradle files
- `.sln`, `.csproj`
- `go.mod`
- `Cargo.toml`
- mobile project files
- Docker, Compose, CI, and infrastructure files

It prefers project-defined commands over invented commands and never claims validation passed unless validation actually ran.

## Validation And CI

Run all repository checks:

```bash
python3 scripts/validate_repository.py
```

Focused checks:

```bash
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
python3 scripts/test_installer.py
python3 scripts/test_packaging.py
```

GitHub Actions workflows:

- `.github/workflows/validate.yml`
- `.github/workflows/package.yml`

Release readiness:

- [Validation strategy](docs/design/validation-strategy.md)
- [Release readiness](docs/design/release-readiness.md)
- [Release candidate checklist](docs/release/RELEASE_CANDIDATE_CHECKLIST.md)

## Packaging

Generate local release packages:

```bash
python3 scripts/package_release.py --version 0.0.12 --clean
```

Expected output:

```text
dist/autonomous-dev-loop-0.0.12.zip
dist/autonomous-dev-loop-codex-0.0.12.zip
dist/autonomous-dev-loop-claude-0.0.12.zip
dist/autonomous-dev-loop-adapters-0.0.12.zip
```

The packaging workflow validates package generation, but does not publish artifacts or create GitHub releases.

Draft release notes:

- [Release notes 0.0.12](docs/release/RELEASE_NOTES_0.0.12.md)

## Roadmap

Near-term:

- Final pre-merge release candidate validation
- PR preparation for `main`
- First tagged release
- More example walkthroughs

Future possibilities:

- Skill target sync tooling
- Example project smoke tests
- More stack-specific playbooks
- Marketplace or plugin packaging if supported by the relevant agent ecosystem

Marketplace or plugin packaging is future ecosystem-dependent work, not current functionality.

## Contributing

Read:

- [Contributing](CONTRIBUTING.md)
- [Project brief](PROJECT_BRIEF.md)
- [Repository structure](docs/design/repository-structure.md)
- [Skill architecture](docs/design/skill-architecture.md)

Development rules:

- Keep content generic and public.
- Keep Skill targets behaviorally equivalent.
- Keep installer and validation tooling dependency-free.
- Update `CHANGELOG.md` for notable changes.

## License

MIT. See [LICENSE](LICENSE).
