# autonomous-dev-loop

`autonomous-dev-loop` is a planned public agent skill for structured autonomous software development loops.

It is intended to help AI coding agents develop, improve, refactor, test, repair, document, and continue software projects through a controlled workflow:

```text
Objective intake -> project inspection -> planning -> ToDo generation -> execution -> testing -> repair -> documentation -> final report
```

## Status

This project is in initial planning and Skill architecture definition.

The final public README, installer scripts, and complete example projects have not been created yet. The current repository documents the foundation decisions, prepares the official version `0.0.1` repository structure, and defines the initial internal Skill behavior.

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

## Installation Strategy

Version `0.0.1` uses a dual installation strategy:

- Codex/OpenAI Skills: `.agents/skills/autonomous-dev-loop/`
- Claude Code Skills: `.claude/skills/autonomous-dev-loop/`

Users should install the folder that matches their agent environment.

For generic agents, reusable project-local adapter templates live in:

```text
adapters/
```

Manual copy installation and agent-assisted installation are planned for the first usable versions. Terminal installer scripts are intentionally deferred.

## Autonomy Model

The project is based on:

**Autonomous execution with safety gates**

Agents should be able to plan, execute, test, repair, and document software tasks autonomously, while stopping for human confirmation before high-risk actions such as destructive commands, deployment, secret handling, data-loss migrations, authentication changes, major rewrites, framework replacement, ambiguous product decisions, or business-critical rule changes.

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
- [Repository structure design](docs/design/repository-structure.md)
- [Skill architecture design](docs/design/skill-architecture.md)
- [Changelog](CHANGELOG.md)

## License

MIT
