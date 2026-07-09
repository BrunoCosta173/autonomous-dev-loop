# autonomous-dev-loop Project Brief

## Purpose

`autonomous-dev-loop` is a public, reusable agent skill for structured autonomous software development loops.

The project will help AI coding agents develop, improve, refactor, test, repair, document, and continue software projects through a controlled workflow:

1. Objective intake
2. Project inspection
3. Planning
4. ToDo generation
5. Execution
6. Testing
7. Repair
8. Documentation
9. Final report

## Target Audience

The project is intended for:

- Developers
- Vibe-coders
- Builders using AI coding agents
- People who want agents to execute software development tasks with more autonomy and structure

## Compatibility Goals

The primary structure should follow the OpenAI/Codex Skills format.

The project should also plan compatibility for:

- Codex CLI
- Codex Desktop/App
- OpenAI/Codex Skills
- Claude Code CLI
- Claude Code Desktop
- Generic AI coding agents

Compatibility adapters for Claude Code and generic agents should be planned after the primary Codex/OpenAI skill structure is defined.

## Autonomy Model

The autonomy model is:

**Autonomous execution with safety gates**

Agents using this skill should be allowed to:

- Ask the user for the development objective
- Transform the objective into an execution plan
- Create a clear ToDo list
- Execute all feasible ToDos autonomously
- Inspect the project
- Modify files
- Run available build, lint, typecheck, and test commands
- Fix failures caused by their changes
- Continue through the planned ToDos until the objective is complete
- Document everything clearly at the end

Agents must stop and request human confirmation before:

- Destructive commands
- Mass deletion
- Database schema changes with data-loss risk
- Authentication or permission changes
- Deployment
- Secret or environment variable handling
- Major architectural rewrites
- Framework replacement
- Ambiguous product decisions
- Business-critical rule changes

## Scope

The skill must be generic and useful for any kind of software development project. It should not be specific to any company, product, ERP, CRM, or internal system.

The skill should support common software categories, including:

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

The skill should be stack-agnostic. It must not hardcode one stack as the default.

Instead, it should teach agents to detect the project stack by inspecting repository files, package manifests, framework conventions, and available commands.

The skill should eventually include guidance for common stacks across:

- Frontend frameworks
- Backend frameworks
- Mobile platforms
- Databases and BaaS providers
- Infrastructure and DevOps tooling

## Initial Repository Decisions

- Project name: `autonomous-dev-loop`
- Primary language: English
- License: MIT
- Initial version: `0.0.1`
- Versioning strategy: semantic versioning
- Commit and release titles should use only the version number, such as `0.0.1`
- `CHANGELOG.md` should document every version
- The current phase is planning only
- The full skill implementation should not be created yet

## Next Planning Step

Define the official repository and installation structure, including the placement of the OpenAI/Codex Skill, Claude Code compatibility files, generic adapters, examples, templates, references, and documentation.
