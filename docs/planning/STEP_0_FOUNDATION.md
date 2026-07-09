# Step 0 Foundation

Status: **Completed**

## Step Goal

Initialize the project context for `autonomous-dev-loop` without implementing the full skill.

This step preserves the foundational decisions needed before defining the official repository layout, installation paths, adapter strategy, and implementation plan.

## Project Identity

- Name: `autonomous-dev-loop`
- Type: public reusable agent skill
- Primary language: English
- License: MIT
- Initial version: `0.0.1`
- Versioning: semantic versioning

Commit and release titles should use only the version number, for example:

```text
0.0.1
```

## Purpose

Create a reusable agent skill that helps AI coding agents autonomously develop, improve, refactor, test, repair, document, and continue software projects through controlled development loops.

The intended workflow is:

1. Objective intake
2. Project inspection
3. Planning
4. ToDo generation
5. Execution
6. Testing
7. Repair
8. Documentation
9. Final report

## Target Users

- Developers
- Vibe-coders
- Builders using AI coding agents
- People who want agents to execute software development tasks with more autonomy and structure

## Target Agents and Compatibility

The project should work well with:

- Codex CLI
- Codex Desktop/App
- OpenAI/Codex Skills
- Claude Code CLI
- Claude Code Desktop
- Generic AI coding agents

The primary structure should follow the Codex/OpenAI Skills format.

Compatibility adapters should be planned for Claude Code and generic agents.

## Autonomy Model

The autonomy model is:

**Autonomous execution with safety gates**

Agents may autonomously:

- Ask the user for the development objective
- Transform the objective into an execution plan
- Create a clear ToDo list
- Execute all feasible ToDos
- Inspect the project
- Modify files
- Run available build, lint, typecheck, and test commands
- Fix failures caused by their changes
- Continue through planned ToDos until the objective is complete
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

The skill must be generic and useful for any kind of software development project.

It should support common software categories such as:

- Web apps
- APIs
- CLIs
- Mobile apps
- Monorepos
- Internal tools
- SaaS products
- Automation scripts
- Full-stack projects

The project must not be specific to any company, product, ERP, CRM, or internal system.

## Stack Strategy

The skill should be stack-agnostic.

It should not hardcode one stack as the default. Instead, it should guide agents to detect the stack by inspecting project files, framework conventions, dependency manifests, lockfiles, scripts, and available commands.

Future guidance should include, but not be limited to:

### Frontend

- React
- Next.js
- Vue
- Nuxt
- Angular
- Svelte / SvelteKit

### Backend

- Node.js
- Express
- NestJS
- Python
- FastAPI
- Django
- Flask
- PHP
- Laravel
- Ruby on Rails
- Java / Spring Boot
- .NET / ASP.NET Core
- Go
- Rust

### Mobile

- React Native
- Flutter
- Kotlin Android
- Swift iOS

### Database / BaaS

- PostgreSQL
- MySQL
- SQLite
- MongoDB
- Firebase
- Supabase

### Infra / DevOps

- Docker
- Docker Compose
- GitHub Actions
- Vercel
- Netlify
- AWS
- Azure
- GCP

## Documentation Style

Documentation should be:

- Technical
- Direct
- Practical
- Clear for developers
- Friendly for vibe-coders
- Public GitHub-ready

The `README.md` should eventually become the main public-facing page, with clear sections, examples, value proposition, installation instructions, usage examples, and compatibility notes.

For Step 0, the README should remain concise and clearly state that the project is under initial planning.

## Deferred Structure Decisions

The exact repository structure is intentionally not finalized in Step 0.

The future structure may include:

```text
README.md
LICENSE
CHANGELOG.md
CONTRIBUTING.md
.agents/skills/autonomous-dev-loop/SKILL.md
.agents/skills/autonomous-dev-loop/agents/openai.yaml
.agents/skills/autonomous-dev-loop/references/
.agents/skills/autonomous-dev-loop/assets/
adapters/
examples/
docs/
```

These paths are planning candidates only and should be confirmed in the next step.

## Files Created In Step 0

- `PROJECT_BRIEF.md`
- `docs/planning/STEP_0_FOUNDATION.md`
- `CHANGELOG.md`
- `README.md`
- `LICENSE`

## Open Questions

- What should the official repository structure be for the first implemented version?
- Which install path should be canonical for OpenAI/Codex Skills?
- How should Claude Code compatibility be represented: adapter files, separate docs, or both?
- What minimal control files or templates should be included in version `0.0.1` after planning?
- What examples should be included first without making the project too broad?

## Completion Criteria

Step 0 is complete because the foundational project decisions are documented and the repository now has the minimum useful planning files.
