# autonomous-dev-loop Project Brief

## Purpose

`autonomous-dev-loop` is a public, reusable agent Skill for structured autonomous software development loops.

It helps AI coding agents develop, improve, refactor, test, repair, document, and continue software projects through a controlled workflow:

```text
Objective intake -> kickoff -> project inspection -> planning -> ToDos -> execution -> validation -> repair -> review -> documentation -> final report
```

## Current Status

The original planning foundation has been implemented.

The project has reached the public `0.1.x` release line. It remains early, but usable.

This document is both:

- A project summary for contributors and users.
- A historical intent document that records the original direction of the repository.

## Target Audience

The project is intended for:

- Developers
- Vibe-coders
- Builders using AI coding agents
- People who want agents to execute software development tasks with more autonomy and structure

## Compatibility Goals

The primary structure follows the OpenAI/Codex Skills format.

The repository also supports:

- Codex CLI
- Codex Desktop/App
- OpenAI/Codex Skills-style agents
- Claude Code CLI
- Claude Code Desktop
- Generic AI coding agents through adapters

Compatibility remains environment-dependent. The project should avoid claiming universal support for platform features such as real subagents or native goal modes.

## Repository Shape

The repository includes:

- Codex/OpenAI Skill target at `.agents/skills/autonomous-dev-loop/`
- Claude Code Skill target at `.claude/skills/autonomous-dev-loop/`
- Generic adapters in `adapters/`
- Project control templates in Skill `assets/`
- Stack and command discovery references
- Safety gates and Review Subagent Loop guidance
- Installer, update, and uninstall tooling
- Release packaging and validation scripts
- Documentation-only examples

## Autonomy Model

The autonomy model is:

**Autonomous execution with safety gates**

Agents using this Skill may:

- Ask the user for the development objective.
- Transform the objective into an execution plan.
- Create a clear ToDo list.
- Execute feasible ToDos autonomously inside scope.
- Inspect the project.
- Modify files.
- Run available build, lint, typecheck, and test commands.
- Fix failures caused by their changes.
- Run review passes before declaring work complete.
- Continue through planned ToDos until the objective is complete or blocked.
- Document everything clearly at the end.

Agents must stop and request human confirmation before:

- Destructive commands
- Mass deletion
- Database changes with data-loss risk
- Authentication or permission changes
- Secret or environment variable handling
- Data exfiltration or external transmission
- Deployment
- Major architecture rewrites
- Framework replacement
- Ambiguous product decisions
- Business-critical rule changes

## Scope

The Skill is generic and useful for many kinds of software development projects. It is not specific to any company, product, ERP, CRM, or internal system.

It supports common software categories, including:

- Web apps
- APIs
- CLIs
- Mobile apps
- Monorepos
- Internal tools
- SaaS products
- Automation scripts
- Full-stack projects

## Stack Strategy

The Skill is stack-agnostic. It does not hardcode one stack as the default.

Instead, it teaches agents to detect the project stack by inspecting repository files, package manifests, framework conventions, CI workflows, and available commands.

## Release And Versioning

- License: MIT
- Primary language: English
- Versioning strategy: semantic versioning
- Commit and release titles should use only the version number, such as `0.1.1`
- `CHANGELOG.md` documents every notable version
- Published releases and tags must not be rewritten

## Direction

Near-term work should focus on release quality, documentation clarity, safety, validation, installation reliability, examples, and compatibility maintenance.

Broad Skill redesigns, marketplace packaging, or complete example applications should be planned explicitly before implementation.
