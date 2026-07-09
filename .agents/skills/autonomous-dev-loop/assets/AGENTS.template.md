# Agent Instructions

Copy this template into a user project as `AGENTS.md`.

## Project Overview

- Project name: `[PROJECT_NAME]`
- Project type: `[WEB_APP | API | CLI | MOBILE_APP | MONOREPO | INTERNAL_TOOL | SAAS | AUTOMATION | FULL_STACK | OTHER]`
- Primary stack: `[LANGUAGES_AND_FRAMEWORKS]`
- Current phase: `[PLANNING | PROTOTYPE | ACTIVE_DEVELOPMENT | MAINTENANCE | STABILIZATION]`
- Important modules: `[MODULES_OR_DIRECTORIES]`

## Project Inspection

Before changing files:

- Read this file and any other project-local agent instructions.
- Inspect the repository structure.
- Identify the stack from project files and dependency manifests.
- Identify available commands from package scripts, task runners, Makefiles, framework files, and CI workflows.
- Prefer existing project conventions over new patterns.

## Development Loop

Use an objective-driven autonomous development loop:

```text
Objective intake -> kickoff -> inspect -> detect stack -> plan -> generate ToDos -> execute -> test -> repair -> review -> document -> report
```

Stay anchored to the user-provided objective. Do not switch to unrelated scope without confirmation.

## Goal Completion Mode

When a user provides a development objective, treat it as the active goal and work toward completion unless the user requests planning only, a safety gate blocks progress, or the configured run limits are reached.

Do not assume a native `/goal` command is available. Use platform-native goal workflows only when supported and safe; otherwise emulate goal completion through ToDos, validation, review rounds, documentation, and final reporting.

## Intake And Kickoff

- Ask only blocking questions.
- Proceed with safe assumptions when missing information can be inferred or safely documented.
- Use `A3 — Autonomous With Safety Gates` by default.
- Use `A4 — Continuous Autonomous Loop` only when explicitly requested.
- Produce a concise kickoff for non-trivial tasks, including objective, assumptions, plan, ToDos, validation plan, review plan, and safety gates to watch.

## Planning Expectations

- Ask only blocking questions.
- Record assumptions before execution.
- Create a structured ToDo list for multi-step work.
- Keep each ToDo scoped, testable, and tied to the objective.
- Update ToDo status as work progresses.

## Testing Expectations

- Detect available validation commands before running them.
- Prefer project-defined commands.
- Run relevant tests, build, lint, typecheck, or other checks when available.
- Never claim tests passed unless they actually ran.
- If validation is unavailable or skipped, state why.

## Review Expectations

- Run review rounds before declaring non-trivial implementation work complete.
- Use real review subagents when supported.
- Use independent review passes when real subagents are unavailable.
- Keep reviewers read-only unless the user explicitly authorizes multi-agent editing.

## Documentation Expectations

Update project control files when useful:

- `BACKLOG.md` for future work or unrelated findings.
- `DEVELOPMENT_LOG.md` for longer autonomous cycles.
- `TEST_PLAN.md` for testing strategy and gaps.
- `DECISIONS.md` for architecture or product decisions.
- `KNOWN_ISSUES.md` for blockers, defects, and unresolved failures.

Do not create every control file automatically. Use them when they improve continuity or traceability.

Use project control files as persistent memory. Actual files and current user instructions override stale notes.

## Continuation And Handoff

When resuming work:

1. Read the current user instruction.
2. Inspect current git status and actual files.
3. Review `TODO.md`, `DEVELOPMENT_LOG.md`, `FINAL_REPORT.md`, `KNOWN_ISSUES.md`, `BACKLOG.md`, and `ROADMAP.md` when present.
4. Continue from the latest reliable state.

Persist a handoff when work is partially complete, blocked, stopped by a safety gate, or likely to continue later.

## Safety Gates

Stop and request human confirmation before:

- Destructive commands
- Mass deletion
- Database migrations with data-loss risk
- Authentication changes
- Permission or authorization changes
- Secret or environment variable handling
- Deployment
- Major architecture rewrites
- Framework replacement
- Business-critical rule changes
- Irreversible operations
- Ambiguous product decisions that materially affect behavior

## Scope Control

- Keep work inside the current objective.
- Record unrelated issues instead of fixing them immediately.
- Ask before expanding scope materially.
- Preserve user changes unless explicitly asked to modify them.

## Final Report

End each run with:

- Objective
- Assumptions
- Plan
- ToDos completed
- ToDos blocked or deferred
- Files changed
- Commands run
- Validation results
- Repairs applied
- Safety gates encountered
- Remaining issues
- Handoff or resume instruction when incomplete
- Recommended next objective
- Final status: `Complete`, `Partially complete`, `Blocked`, or `Failed`
