# autonomous-dev-loop

`autonomous-dev-loop` is a planned public agent skill for structured autonomous software development loops.

It is intended to help AI coding agents develop, improve, refactor, test, repair, document, and continue software projects through a controlled workflow:

```text
Objective intake -> project inspection -> planning -> ToDo generation -> execution -> testing -> repair -> documentation -> final report
```

## Status

This project is in initial planning, Skill architecture definition, and first public installation documentation.

The final public README, installer scripts, and complete example projects have not been created yet. The current repository documents the foundation decisions, prepares the official version `0.0.x` repository structure, and defines the initial internal Skill behavior through Goal Completion Mode, safety gates, review rounds, and cross-session handoff.

## Intended Users

- Developers
- Vibe-coders
- Builders using AI coding agents
- People who want agents to execute software development tasks with more autonomy and structure

## Compatibility Goals

The primary structure will follow the OpenAI/Codex Skills format.

The project is also intended to support:

- Codex CLI
- Codex Desktop/App
- Claude Code CLI
- Claude Code Desktop
- Generic AI coding agents

## Installation Overview

The project uses a dual Skill installation strategy:

- Codex/OpenAI Skills: `.agents/skills/autonomous-dev-loop/`
- Claude Code Skills: `.claude/skills/autonomous-dev-loop/`

Users should install the folder that matches their agent environment.

For generic agents, reusable project-local adapter templates live in:

```text
adapters/
```

Manual copy installation and agent-assisted installation are documented. Terminal installer scripts are intentionally deferred.

Start here:

- [Codex/OpenAI installation](docs/installation/codex-openai.md)
- [Claude Code installation](docs/installation/claude-code.md)
- [Generic agent installation](docs/installation/generic-agents.md)
- [Agent-assisted installation](docs/installation/agent-assisted-installation.md)
- [Troubleshooting](docs/installation/troubleshooting.md)

## Compatibility Overview

The project currently documents compatibility expectations for:

- Codex/OpenAI Skills
- Claude Code Skills
- Generic AI coding agents

Native goal modes and real review subagents are environment-dependent. The Skill always defines fallback behavior through Goal Completion Mode, ToDos, validation, independent review passes, persistent memory, and final reporting.

See the [compatibility matrix](docs/design/compatibility-matrix.md).

## Quick Usage Example

After installation, invoke the Skill with a scoped objective:

```text
Use autonomous-dev-loop to improve the user settings page.
Focus on UI consistency, form validation, loading states, and accessibility.
Do not change database schema, authentication, or dependencies.
Run available lint, typecheck, and build commands.
Use A3 autonomy.
```

## Autonomy Model

The project is based on:

**Autonomous execution with safety gates**

Agents should be able to plan, execute, test, repair, and document software tasks autonomously, while stopping for human confirmation before high-risk actions such as destructive commands, deployment, secret handling, data-loss migrations, authentication changes, major rewrites, framework replacement, ambiguous product decisions, or business-critical rule changes.

When invoked with a development objective, the Skill treats that objective as the active goal. Native goal features such as `/goal` are optional platform capabilities, not assumed universal behavior.

## Scope

The skill should be generic and stack-agnostic. It should support many project types, including web apps, APIs, CLIs, mobile apps, monorepos, internal tools, SaaS products, automation scripts, and full-stack projects.

Rather than assuming a default stack, the skill should teach agents to inspect the project and detect the stack from files, dependency manifests, scripts, framework conventions, and available commands.

## Planning Documents

- [Project brief](PROJECT_BRIEF.md)
- [Step 0 foundation](docs/planning/STEP_0_FOUNDATION.md)
- [Step 1 repository structure](docs/planning/STEP_1_REPOSITORY_STRUCTURE.md)
- [Step 2 internal Skill architecture](docs/planning/STEP_2_INTERNAL_SKILL_ARCHITECTURE.md)
- [Step 3 project control templates](docs/planning/STEP_3_PROJECT_CONTROL_TEMPLATES.md)
- [Step 4 stack detection and command discovery](docs/planning/STEP_4_STACK_DETECTION_COMMAND_DISCOVERY.md)
- [Step 5 autonomy, safety, and review loop](docs/planning/STEP_5_AUTONOMY_SAFETY_REVIEW_LOOP.md)
- [Step 6 objective intake and kickoff](docs/planning/STEP_6_OBJECTIVE_INTAKE_KICKOFF.md)
- [Step 7 goal memory handoff](docs/planning/STEP_7_GOAL_MEMORY_HANDOFF.md)
- [Step 8 packaging, installation, and examples](docs/planning/STEP_8_PACKAGING_INSTALLATION_EXAMPLES.md)
- [Repository structure design](docs/design/repository-structure.md)
- [Skill architecture design](docs/design/skill-architecture.md)
- [Packaging strategy](docs/design/packaging-strategy.md)
- [Compatibility matrix](docs/design/compatibility-matrix.md)
- [Changelog](CHANGELOG.md)

## Examples

Lightweight usage examples:

- [Next.js app](examples/nextjs-app/README.md)
- [FastAPI API](examples/fastapi-api/README.md)
- [Laravel app](examples/laravel-app/README.md)

## License

MIT
