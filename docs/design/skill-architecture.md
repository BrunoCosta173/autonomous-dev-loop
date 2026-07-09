# Skill Architecture

`autonomous-dev-loop` uses a dual Skill architecture for the initial `0.0.x` series.

The internal behavior is now defined around:

```text
Objective-driven autonomous development loop with safety gates
```

## Installation Targets

The repository maintains two Skill entry points:

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/SKILL.md`
- Claude Code: `.claude/skills/autonomous-dev-loop/SKILL.md`

Each target exists because different agent environments may expect different local installation paths and project conventions.

## Entry Point Design

Each `SKILL.md` should stay concise.

The entry point should:

- Define when the Skill activates.
- State the core model.
- List the high-level loop.
- Explain the safety-gate boundary.
- Link to reference files for phase-level detail.
- State the behavioral equivalence requirement.

Detailed procedures belong in `references/`, not in `SKILL.md`.

## Reference Design

Each Skill target includes this reference set:

- `references/objective-intake.md`
- `references/autonomy-model.md`
- `references/loop-protocol.md`
- `references/todo-execution.md`
- `references/scope-management.md`
- `references/safety-gates.md`
- `references/stack-detection.md`
- `references/command-discovery.md`
- `references/frontend-playbooks.md`
- `references/backend-playbooks.md`
- `references/mobile-playbooks.md`
- `references/infra-playbooks.md`
- `references/testing-strategy.md`
- `references/repair-strategy.md`
- `references/documentation-rules.md`
- `references/final-report.md`

This keeps the Skill usable through progressive disclosure: the entry point gives the operating model, and agents load detailed references when a phase requires them.

## Core Behavior

The Skill guides agents through:

1. Intake
2. Inspect
3. Detect stack
4. Plan
5. Generate ToDos
6. Execute
7. Test
8. Repair
9. Document
10. Report
11. Continue or stop

The loop continues while there are unfinished ToDos inside the current objective.

## Behavioral Equivalence

The Codex/OpenAI and Claude Code Skill versions must remain behaviorally equivalent.

Behavioral equivalence means:

- They describe the same purpose.
- They guide the same autonomous development loop.
- They use the same safety gate model.
- They support the same project categories.
- They use equivalent reference content.
- They differ only where the target agent environment requires different wording or metadata.

The two Skill targets should not drift into separate products.

## Stack-Agnostic Strategy

The Skill is stack-agnostic.

It should detect languages, frameworks, tools, package managers, and validation commands by inspecting repository files and existing project conventions.

It should not claim guaranteed compatibility with every stack. It adapts by using available evidence and project-defined commands.

The stack and command discovery layer is split across:

- `stack-detection.md` for file signals and detection output.
- `command-discovery.md` for command discovery policy and safe command selection.
- `frontend-playbooks.md` for frontend framework validation heuristics.
- `backend-playbooks.md` for backend, API, CLI, and service validation heuristics.
- `mobile-playbooks.md` for mobile validation heuristics.
- `infra-playbooks.md` for Docker, CI, deployment config, and infrastructure safety guidance.

Project-defined commands remain authoritative. Playbooks provide fallbacks and interpretation guidance after project inspection.

## Assets

Both Skill targets include an `assets/` directory.

The `assets/` directory contains reusable project control file templates that agents can copy or adapt into user projects when useful.

Current templates:

- `AGENTS.template.md`
- `CLAUDE.template.md`
- `BACKLOG.template.md`
- `ROADMAP.template.md`
- `DEVELOPMENT_LOG.template.md`
- `TEST_PLAN.template.md`
- `DECISIONS.template.md`
- `KNOWN_ISSUES.template.md`
- `TODO.template.md`
- `FINAL_REPORT.template.md`

The Skill should not force every template into every project. It should create or suggest templates based on the current objective, project context, missing documentation, and whether durable continuity is useful.

The template usage policy is documented in `references/documentation-rules.md`.

## Deferred Sync Strategy

No sync or build script is included in the initial `0.0.x` series.

This is intentional. The project first defines the behavior manually, then future versions may add automation to compare, sync, or generate target-specific Skill files.

Future versions may add:

- A sync script to compare or update both Skill targets.
- A build step that generates target-specific Skill files from shared source content.
- A validation command to check behavioral equivalence.
- A terminal installer for supported agent environments.

## Design Constraint

Keep installable Skill folders focused.

Public documentation, planning notes, installation guides, and contribution instructions belong in `docs/` or root-level files, not inside the Skill folders.
