# Autonomy Model

The autonomy model is:

```text
Autonomous execution with safety gates
```

The agent should keep moving through the agreed objective without asking for unnecessary confirmation, while stopping before high-risk or ambiguous actions.

## Autonomy Levels

Use these levels when the user specifies autonomy or when the agent needs to state operating assumptions:

### A0 — Manual

The agent proposes plans and instructions only. It does not edit files or run commands.

### A1 — Assisted

The agent may inspect files and propose changes, but asks before editing.

### A2 — Supervised

The agent may edit files and run safe validation commands, but asks before each meaningful execution batch.

### A3 — Autonomous With Safety Gates

Default recommended level.

The agent may plan, edit, test, repair, document, and run review rounds autonomously, but must stop at safety gates.

### A4 — Continuous Autonomous Loop

The agent may continue across multiple internal cycles within the user-provided objective, using review rounds and safety gates.

It must not expand beyond the objective without confirmation.

## Default Level

Use A3 unless the user specifies a different autonomy level or the environment requires a more restrictive mode.

If autonomy is ambiguous, state the assumed level before execution.

## Autonomous Actions

The agent may autonomously:

- Read and inspect files
- Create an implementation plan
- Create and update a ToDo list
- Modify files within the agreed objective
- Run non-destructive project commands
- Run tests, builds, lint, typecheck, and related validation commands
- Fix failures caused by its changes
- Update documentation and control files when useful
- Run Review Subagent Loop rounds or independent review passes
- Continue through ToDos until the objective is complete

## Required Safety Gates

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
- Installing or upgrading critical dependencies
- Changing licensing terms
- Removing tests to make validation pass
- Disabling validation tools or CI checks

See `safety-gates.md` for confirmation handling.
See `review-subagent-loop.md` for review requirements before declaring completion.

## Execution Defaults

- Prefer action over repeated planning once the objective is clear.
- Keep changes scoped to the objective.
- Use existing project conventions.
- Run relevant available validation commands.
- Run review rounds before declaring the scope complete.
- Repair failures caused by current work.
- Document assumptions, validations, and unresolved blockers.

## Human Confirmation

When confirmation is required, explain:

- The action being considered
- Why it is risky or irreversible
- The expected effect
- Safer alternatives, if any
- The exact command or change, when applicable

Do not proceed past a required safety gate until the user confirms.
