# Autonomy Model

The autonomy model is:

```text
Autonomous execution with safety gates
```

The agent should keep moving through the agreed objective without asking for unnecessary confirmation, while stopping before high-risk or ambiguous actions.

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

See `safety-gates.md` for confirmation handling.

## Execution Defaults

- Prefer action over repeated planning once the objective is clear.
- Keep changes scoped to the objective.
- Use existing project conventions.
- Run relevant available validation commands.
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
