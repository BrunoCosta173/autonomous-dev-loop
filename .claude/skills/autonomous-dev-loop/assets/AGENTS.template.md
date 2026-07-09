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
Objective intake -> inspect -> detect stack -> plan -> generate ToDos -> execute -> test -> repair -> document -> report
```

Stay anchored to the user-provided objective. Do not switch to unrelated scope without confirmation.

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

## Documentation Expectations

Update project control files when useful:

- `BACKLOG.md` for future work or unrelated findings.
- `DEVELOPMENT_LOG.md` for longer autonomous cycles.
- `TEST_PLAN.md` for testing strategy and gaps.
- `DECISIONS.md` for architecture or product decisions.
- `KNOWN_ISSUES.md` for blockers, defects, and unresolved failures.

Do not create every control file automatically. Use them when they improve continuity or traceability.

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
- Recommended next objective
- Final status: `Complete`, `Partially complete`, `Blocked`, or `Failed`
