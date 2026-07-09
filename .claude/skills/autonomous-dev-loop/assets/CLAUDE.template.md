# Claude Code Instructions

Copy this template into a user project as `CLAUDE.md`.

## Project Overview

- Project name: `[PROJECT_NAME]`
- Project type: `[WEB_APP | API | CLI | MOBILE_APP | MONOREPO | INTERNAL_TOOL | SAAS | AUTOMATION | FULL_STACK | OTHER]`
- Primary stack: `[LANGUAGES_AND_FRAMEWORKS]`
- Important modules: `[MODULES_OR_DIRECTORIES]`
- Current phase: `[PLANNING | PROTOTYPE | ACTIVE_DEVELOPMENT | MAINTENANCE | STABILIZATION]`

## Claude Workflow

Follow an objective-driven autonomous development loop with safety gates:

```text
Intake -> inspect -> detect stack -> plan -> ToDos -> execute -> test -> repair -> document -> final report
```

Ask only blocking questions. If the objective is clear enough, proceed with safe assumptions and document them before editing files.

## Preferred Workflow

1. Confirm or infer the objective.
2. Inspect the relevant project files.
3. Detect the stack and available commands.
4. Create a short plan and executable ToDo list.
5. Execute all feasible ToDos within scope.
6. Run relevant validation commands.
7. Repair failures caused by current changes.
8. Document durable context when useful.
9. Produce a final report.

## Commands

Record project commands here when known:

```text
Install:
Dev:
Build:
Lint:
Format:
Typecheck:
Test:
E2E:
Migration check:
Static analysis:
```

Prefer these project-defined commands over invented commands.

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

## Documentation Rules

Create or update project control files only when useful:

- `BACKLOG.md`
- `ROADMAP.md`
- `DEVELOPMENT_LOG.md`
- `TEST_PLAN.md`
- `DECISIONS.md`
- `KNOWN_ISSUES.md`
- `TODO.md`
- `FINAL_REPORT.md`

Do not expose secrets or private environment details.

## Final Report Requirements

End each run with:

- Objective
- Starting context
- Assumptions
- Plan
- ToDos completed
- ToDos blocked or deferred
- Files changed
- Commands run
- Test/build/lint results
- Errors found
- Repairs applied
- Safety gates encountered
- Remaining issues
- Recommended next objective
- Final status: `Complete`, `Partially complete`, `Blocked`, or `Failed`
