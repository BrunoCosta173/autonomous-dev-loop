# Scope Management

Use this reference to prevent scope drift.

## Objective Boundary

The current objective defines the work boundary.

The agent may adjust sub-scope only when the change still directly supports the original objective.

## Allowed Sub-Scope Changes

Allowed examples:

- Editing a shared helper required by the target module.
- Adding a focused test fixture required to validate the change.
- Updating docs that explain the changed behavior.
- Fixing a nearby bug introduced by the current changes.

## Scope Expansion

Stop or ask for confirmation when:

- The objective expands into a new feature area.
- The implementation requires a major architecture rewrite.
- The work changes business-critical behavior not clearly included in the objective.
- The change requires database, authentication, authorization, deployment, or secret-handling decisions.
- The estimated work becomes materially larger than the initial plan.

## Unrelated Findings

Record unrelated findings instead of acting on them immediately.

Use `BACKLOG.md` for future improvement ideas.

Use `KNOWN_ISSUES.md` for defects, failing tests, or unresolved technical problems.

Do not create these files automatically for every project. Create or update them when they improve continuity or when unresolved findings need a durable home.

## Scope Statement

At the start of execution, maintain a concise scope statement:

```text
In scope:
Out of scope:
Assumptions:
Safety gates:
```

Use the statement to evaluate new findings during the loop.
