# Step 3 Project Control Templates

Status: **Completed**

## Step Goal

Create reusable project control file templates that the Skill can copy, generate, or adapt inside user projects during autonomous development loops.

The templates live in the Skill `assets/` directories and are intended to preserve context, support safe continuation across sessions, and make autonomous work easier to audit.

## Template Locations

Equivalent templates were created in both Skill targets:

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/assets/`
- Claude Code: `.claude/skills/autonomous-dev-loop/assets/`

The assets in both targets should remain behaviorally equivalent.

## Templates Created

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

## Template Purposes

- `AGENTS.template.md`: generic persistent instructions for AI coding agents working inside a user project.
- `CLAUDE.template.md`: persistent instructions for Claude Code working inside a user project.
- `BACKLOG.template.md`: prioritized project backlog for blockers, bugs, incomplete features, UX improvements, polish, refactoring, documentation, and tests.
- `ROADMAP.template.md`: high-level project direction, milestones, out-of-scope items, and release notes.
- `DEVELOPMENT_LOG.template.md`: cycle-by-cycle execution log for autonomous development runs.
- `TEST_PLAN.template.md`: project testing strategy, available commands, validation coverage, regression checks, and known gaps.
- `DECISIONS.template.md`: ADR-like architecture and product decision log.
- `KNOWN_ISSUES.template.md`: known bugs, limitations, risks, and unresolved blockers.
- `TODO.template.md`: active execution plan for the current autonomous run.
- `FINAL_REPORT.template.md`: persistent final report for an autonomous development run.

## Recommended Templates

These templates are commonly useful:

- `AGENTS.template.md` when the project uses generic agent instructions.
- `CLAUDE.template.md` when the project uses Claude Code.
- `TODO.template.md` for multi-step autonomous runs.
- `FINAL_REPORT.template.md` when the user wants a persistent run report.

## Optional Templates

These templates should be created or suggested based on project need:

- `BACKLOG.template.md`
- `ROADMAP.template.md`
- `DEVELOPMENT_LOG.template.md`
- `TEST_PLAN.template.md`
- `DECISIONS.template.md`
- `KNOWN_ISSUES.template.md`

They should not be forced into every project.

## Template Usage Policy

The Skill should not force every template into every project.

Instead:

- Create or suggest `AGENTS.md` when a generic agent instruction file is useful.
- Create or suggest `CLAUDE.md` when the user is using Claude Code.
- Create or suggest `BACKLOG.md` and `DEVELOPMENT_LOG.md` for longer autonomous work.
- Create or suggest `TEST_PLAN.md` when testing strategy is unclear or missing.
- Create or suggest `DECISIONS.md` when architectural or product decisions are being made.
- Create or suggest `KNOWN_ISSUES.md` when blockers, bugs, or unrelated issues are found.
- Create or suggest `TODO.md` for the current autonomous run when the task has multiple steps.
- Create or suggest `FINAL_REPORT.md` when the user wants a persistent run report.
- Create or suggest `ROADMAP.md` when high-level project direction is missing or actively being shaped.

## Creation Decision Rules

Before creating a control file in a user project, the agent should check:

- Whether an equivalent file already exists.
- Whether the file improves continuity, traceability, testing clarity, or future autonomous cycles.
- Whether the current objective needs a persistent artifact or an in-response note is enough.
- Whether the user requested durable documentation.

Prefer updating an existing equivalent file over creating duplicates.

## Skill Reference Updates

The following references were updated to explain template usage:

- `documentation-rules.md`
- `todo-execution.md`
- `final-report.md`
- `loop-protocol.md`

## Explicit Non-Goals For Step 3

Step 3 does not:

- Create installer scripts.
- Create complete example projects.
- Polish the final marketing README.
- Add dependencies.
- Add sync/build automation.

## Equivalence Confirmation

Both Skill targets contain the same template filenames.

The templates and updated references are intended to remain equivalent between Codex/OpenAI and Claude Code targets.

## Completion Criteria

Step 3 is complete because reusable project control file templates exist in both Skill asset directories, and the Skill references describe when and how to use them.
