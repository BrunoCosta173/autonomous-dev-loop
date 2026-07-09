# Objective Intake

Use this reference to anchor every autonomous development loop to a concrete user-provided objective.

## Objective Requirement

Do not run aimlessly. Start from a development objective supplied by the user.

Valid objective examples:

- Improve the proposal creation modal.
- Refactor the authentication flow.
- Build the first version of a task management module.
- Fix bugs in the checkout flow.
- Review and improve the project structure.
- Add tests for an existing API.

If the objective is too vague to execute safely, ask only the blocking questions. If the objective is clear enough, proceed with reasonable assumptions and record them before execution.

## Intake Fields

Collect or infer:

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

Do not ask for fields the user already provided or that can be safely inferred from repository context.

## Default Intake Behavior

- Ask only blocking questions.
- Otherwise proceed with safe assumptions.
- Record assumptions before modifying files.
- Keep assumptions specific and testable.
- Treat missing authorization for risky actions as not granted.

## Minimal Intake Record

Before execution, maintain a short intake record:

```text
Objective:
Target area:
Assumptions:
Non-goals:
Allowed commands:
Safety constraints:
Definition of done:
```

This record may be kept in the working response, a ToDo list, or a project control file when persistence is useful.

## Blocking Question Examples

Ask a question when:

- The objective could change product behavior in materially different ways.
- The user asks for database, authentication, authorization, deployment, or secret-handling work without clear permission.
- The requested change requires choosing between incompatible product directions.
- The requested scope is too broad to plan into executable ToDos.

Prefer one concise question at a time when a single answer unlocks progress.
