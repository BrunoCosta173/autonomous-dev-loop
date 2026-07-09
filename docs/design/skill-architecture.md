# Skill Architecture

`autonomous-dev-loop` uses a dual Skill architecture for the initial `0.0.x` series.

The internal behavior is now defined around:

```text
Objective-driven autonomous development loop with safety gates
```

Step 7 added Goal Completion Mode, persistent project memory, continuation behavior, and cross-session handoff.

Step 8 added public packaging, installation, compatibility, troubleshooting, and first usage example documentation.

Step 9 adds lightweight validation scripts, Skill equivalence checks, private-content scanning, CI validation, and release-readiness documentation.

## Installation Targets

The repository maintains two Skill entry points:

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/SKILL.md`
- Claude Code: `.claude/skills/autonomous-dev-loop/SKILL.md`

Each target exists because different agent environments may expect different local installation paths and project conventions.

Installation documentation:

- `docs/installation/codex-openai.md`
- `docs/installation/claude-code.md`
- `docs/installation/generic-agents.md`
- `docs/installation/agent-assisted-installation.md`
- `docs/installation/troubleshooting.md`

Packaging boundaries are documented in `docs/design/packaging-strategy.md`.

Compatibility expectations are documented in `docs/design/compatibility-matrix.md`.

Validation expectations are documented in `docs/design/validation-strategy.md`.

Release-readiness criteria are documented in `docs/design/release-readiness.md`.

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
- `references/kickoff-protocol.md`
- `references/goal-completion-mode.md`
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
- `references/review-subagent-loop.md`
- `references/reviewer-roles.md`
- `references/documentation-rules.md`
- `references/persistent-memory.md`
- `references/continuation-handoff.md`
- `references/final-report.md`

This keeps the Skill usable through progressive disclosure: the entry point gives the operating model, and agents load detailed references when a phase requires them.

## Core Behavior

The Skill guides agents through:

1. Intake
2. Kickoff
3. Inspect
4. Detect stack
5. Plan
6. Generate ToDos
7. Execute
8. Test
9. Repair
10. Review
11. Document
12. Report
13. Continue or stop

The loop continues while there are unfinished ToDos inside the current objective.

Completion requires relevant validation plus the Review Subagent Loop passing criteria, unless validation or review is unavailable and the limitation is explicitly documented.

## Goal Completion Mode

When the user invokes the Skill with a development objective, the agent treats that objective as the active goal and works toward completion.

The user should not need to type `/goal`. Native goal or long-run platform workflows are optional: the agent may use them when they exist and are safe, but otherwise it emulates Goal Completion Mode through the Skill protocol.

Goal Completion Mode is implemented through:

- Objective Brief
- Definition of Done
- ToDos
- Validation
- Repair
- Review Subagent Loop
- Persistent project memory when useful
- Final report and handoff

The agent should not stop after planning unless the user requested planning only, a safety gate blocks progress, the objective is too ambiguous, access is missing, limits are reached, or a blocker prevents safe progress.

Goal Completion Mode maps to the autonomy levels in `references/autonomy-model.md`, with `A3 — Autonomous With Safety Gates` as the default and `A4 — Continuous Autonomous Loop` reserved for explicit broad continuation requests.

## Intake And Kickoff Architecture

The Skill starts each autonomous run by parsing the objective, asking only blocking questions, recording assumptions, and producing a concise Objective Brief and kickoff when appropriate.

The intake model is documented in `references/objective-intake.md`.

The Objective Brief, kickoff response, and continuation kickoff formats are documented in `references/kickoff-protocol.md`.

The default autonomy level is `A3 — Autonomous With Safety Gates`. `A4 — Continuous Autonomous Loop` is used only when explicitly requested and must remain inside the user-provided objective.

## Review Architecture

The Review Subagent Loop is a quality gate after implementation and validation.

Primary mode:

- Use real review subagents when supported by the current agent environment.

Fallback mode:

- Run independent review passes using the same reviewer roles and rubrics when real subagents are unavailable.

Reviewers are read-only by default. They analyze, score, identify risks, suggest corrections, flag safety gates, and recommend approval outcomes. The main agent remains responsible for applying corrections.

Reviewer roles are documented in `references/reviewer-roles.md`.

Review loop scoring and stop conditions are documented in `references/review-subagent-loop.md`.

## Persistent Memory And Handoff

Project control files are used as persistent memory only when they improve continuity, traceability, or safe continuation.

The Skill recognizes these memory roles:

- `AGENTS.md` and `CLAUDE.md` for persistent agent instructions.
- `TODO.md` for active run state.
- `DEVELOPMENT_LOG.md` for cycle history.
- `FINAL_REPORT.md` for durable completion or partial completion reports.
- `KNOWN_ISSUES.md` and `BACKLOG.md` for blockers, bugs, and out-of-scope findings.
- `ROADMAP.md`, `TEST_PLAN.md`, and `DECISIONS.md` for durable project direction, validation strategy, and decisions.

Continuation uses this priority:

1. Explicit user instruction in the current prompt
2. Current git status and actual files
3. `TODO.md`
4. `DEVELOPMENT_LOG.md`
5. `FINAL_REPORT.md`
6. `KNOWN_ISSUES.md`
7. `BACKLOG.md`
8. `ROADMAP.md`

Actual current project state overrides stale control files.

Cross-session handoff is documented in `references/continuation-handoff.md`.

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

## Public Usage Examples

The `examples/` directory contains lightweight usage documentation, not complete apps.

Current examples:

- `examples/nextjs-app/README.md`
- `examples/fastapi-api/README.md`
- `examples/laravel-app/README.md`

Each example includes an objective prompt, suggested constraints, expected Skill behavior, example validation commands, expected final report content, and safety gates to watch.

## Deferred Sync Strategy

No sync or build script is included in the initial `0.0.x` series.

This is intentional. The project first defines the behavior manually, then future versions may add automation to compare, sync, or generate target-specific Skill files.

Future versions may add:

- A sync script to compare or update both Skill targets.
- A build step that generates target-specific Skill files from shared source content.
- A validation command to check behavioral equivalence.
- A terminal installer for supported agent environments.

## Validation Strategy

The repository includes lightweight validation scripts under `scripts/`:

- `validate_repository.py`
- `check_skill_equivalence.py`
- `check_private_content.py`

These scripts use only Python standard library dependencies.

The GitHub Actions workflow at `.github/workflows/validate.yml` runs the validation scripts on pushes and pull requests.

The workflow is validation-only. It does not publish packages, create release artifacts, or run installer automation.

## Design Constraint

Keep installable Skill folders focused.

Public documentation, planning notes, installation guides, and contribution instructions belong in `docs/` or root-level files, not inside the Skill folders.
