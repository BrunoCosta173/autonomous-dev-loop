# ToDo Execution

Use ToDos to turn the objective into executable work.

## ToDo Format

Recommended fields:

- ID
- Priority
- Task
- Rationale
- Files likely affected
- Status
- Validation method

For a persistent multi-step run, copy or adapt `assets/TODO.template.md` into the target project as `TODO.md` when it improves continuity.

Example:

```text
ID: T1
Priority: High
Task: Add server-side validation for checkout coupon codes.
Rationale: Prevent invalid discounts from reaching payment processing.
Files likely affected: src/checkout/*, tests/checkout/*
Status: Pending
Validation method: Run checkout unit tests and relevant typecheck/build command.
```

## Statuses

Use these statuses:

- Pending
- In progress
- Done
- Blocked
- Deferred

## Prioritization

Prioritize ToDos by:

1. Blocking dependencies
2. User-visible correctness
3. Safety and data integrity
4. Test coverage for changed behavior
5. Documentation and cleanup

## Execution Rules

- Execute all feasible ToDos within the objective.
- Keep only one ToDo in progress when practical.
- Update status as work progresses.
- Mark ToDos blocked when they require missing information or a safety gate.
- Mark ToDos deferred when they are useful but outside the current objective.
- Do not add unrelated ToDos to the active execution list.
- Prefer an in-response ToDo list for small tasks.
- Prefer `TODO.md` for longer runs, interrupted work, or handoff between sessions.

## Validation

Each ToDo should have a validation method, such as:

- Specific test command
- Build command
- Lint/typecheck command
- Manual inspection note
- Documentation review

Do not mark a ToDo done if its validation was skipped without documenting why.
