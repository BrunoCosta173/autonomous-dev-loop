# Step 2 Internal Skill Architecture

Status: **Completed**

## Step Goal

Define the internal Skill architecture and the core behavior of the autonomous development loop.

This step turns the initial Skill placeholders into concise behavior entry points and adds detailed reference files for the loop protocol.

## Pre-Change Commit Check

Before changes, the latest commit was checked with:

```text
git log --oneline -1
```

The latest commit message was exactly:

```text
0.0.1
```

No commit amendment was needed.

## Core Model

The Skill is designed around:

```text
Objective-driven autonomous development loop with safety gates
```

The agent must always be anchored to a user-provided development objective.

The agent should not run aimlessly, invent unrelated goals, or expand scope without confirmation.

## Core Workflow

The Skill defines this loop:

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

The loop continues while unfinished ToDos remain inside the current objective.

## Objective Intake Decisions

The agent should collect or infer:

- Target area or module
- Desired outcome
- Non-goals
- Allowed autonomy level
- Whether database changes are allowed
- Whether dependency changes are allowed
- Whether UI/UX changes are allowed
- Whether tests should be created or only existing tests should be run
- Commands the user authorizes the agent to run
- Definition of done
- Known constraints
- Sensitive areas to avoid

Default behavior:

- Ask only blocking questions.
- Otherwise proceed with safe assumptions.
- Record all assumptions before execution.

## Autonomy Model

The autonomy model remains:

```text
Autonomous execution with safety gates
```

The agent may autonomously:

- Read and inspect files
- Create an implementation plan
- Create and update a ToDo list
- Modify files within the agreed objective
- Run non-destructive project commands
- Run tests, builds, lint, typecheck, and related validation commands
- Fix failures caused by its changes
- Update documentation and control files when useful
- Continue through ToDos until the objective is complete

The agent must stop and request human confirmation before:

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

## Reference Architecture

Detailed behavior lives in one-level reference files under each Skill target:

- `objective-intake.md`
- `autonomy-model.md`
- `loop-protocol.md`
- `todo-execution.md`
- `scope-management.md`
- `safety-gates.md`
- `stack-detection.md`
- `testing-strategy.md`
- `repair-strategy.md`
- `documentation-rules.md`
- `final-report.md`

The `SKILL.md` files remain concise and point agents to the relevant references.

## Dual Skill Targets

Step 2 updates both Skill targets:

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/`
- Claude Code: `.claude/skills/autonomous-dev-loop/`

Both targets must remain behaviorally equivalent.

The reference files are intentionally mirrored between targets in this version.

## Stack Detection Decisions

The Skill is stack-agnostic.

It detects stack and commands from repository evidence such as:

- dependency manifests
- lockfiles
- framework config files
- language config files
- build files
- Docker files
- CI workflow files
- existing project docs

The Skill should prefer project-defined commands over invented commands.

## Testing And Repair Decisions

The agent should:

- Detect commands before running them.
- Run relevant available validation commands.
- Never claim tests passed unless they actually ran.
- Fix failures caused by current work.
- Avoid deleting tests or hiding errors to pass validation.
- Document unrelated failures separately.

## Documentation Decisions

The Skill may update or create project control files when useful:

- `AGENTS.md`
- `CLAUDE.md`
- `BACKLOG.md`
- `ROADMAP.md`
- `DEVELOPMENT_LOG.md`
- `TEST_PLAN.md`
- `DECISIONS.md`
- `KNOWN_ISSUES.md`

The Skill must not force all control files into every project.

## Final Report Decisions

Every autonomous run should end with a final report covering:

- Objective
- Assumptions
- Plan
- ToDos executed
- Files changed
- Commands run
- Test/build/lint results
- Errors found
- Repairs applied
- Safety gates encountered
- Remaining issues
- Recommended next objective
- Whether the objective is complete, partially complete, blocked, or failed

## Explicit Non-Goals For Step 2

Step 2 does not:

- Create installer scripts.
- Polish the final marketing README.
- Create complete example projects.
- Add dependencies.
- Add sync/build automation between Skill targets.
- Claim guaranteed compatibility with every stack.

## Future Roadmap Notes

Future steps may add:

- Reusable project control file templates in `assets/`.
- Stack-specific reference expansions.
- Example project walkthroughs.
- Installer scripts.
- Sync or validation tooling for behavioral equivalence.

## Completion Criteria

Step 2 is complete because the internal Skill architecture, objective-driven loop behavior, safety gates, references, and final report requirements are defined for both Skill targets.
