# Objective Intake

Use this reference to transform a user-provided development objective into a clear autonomous execution plan without over-questioning.

## Core Principle

The Skill should be autonomous, not bureaucratic.

Ask only when the missing answer affects safety, scope, data integrity, business-critical behavior, or the definition of done.

Otherwise, proceed with documented assumptions.

## Default Intake Flow

When the user invokes the Skill with a development objective:

1. Parse the objective.
2. Identify the target area or module.
3. Identify the desired outcome.
4. Identify non-goals or constraints.
5. Determine the appropriate autonomy level.
6. Detect whether any safety gates may be involved.
7. Ask only blocking questions, if needed.
8. Record safe assumptions.
9. Inspect the project.
10. Create an Objective Brief.
11. Create an Execution Plan.
12. Create a ToDo list.
13. Start the autonomous loop.

## Intake Categories

### 1. Objective

Determine:

- What should be created, improved, fixed, reviewed, refactored, or tested?
- What is the target module, page, feature, package, or workflow?
- What user-visible or developer-visible outcome is expected?

### 2. Scope Boundaries

Determine:

- What should not be changed?
- Should the agent avoid backend, database, UI, dependencies, authentication, or deployment?
- Is the objective limited to one module, or can nearby files be changed?

### 3. Autonomy

Determine:

- Which autonomy level is authorized?
- Should the agent execute all feasible ToDos autonomously?
- Should the agent stop after planning, after first implementation, or only after review rounds?

Default: use `A3 — Autonomous With Safety Gates` unless the user specifies otherwise.

Use `A4 — Continuous Autonomous Loop` only when the user explicitly asks the agent to continue through multiple internal cycles or broadly improve an area until completion.

### 4. Commands And Environment

Determine:

- Which commands are safe to run?
- Are install commands allowed?
- Are build, lint, typecheck, and test commands allowed?
- Should heavy commands be avoided?

Defaults:

- Safe read-only inspection is allowed.
- Non-destructive validation commands are allowed.
- Installation, dependency changes, deployment, and destructive commands require confirmation when risky.

### 5. Data, Database, Auth, And Secrets

Determine:

- Are database migrations allowed?
- Are schema changes allowed?
- Are authentication or permission changes allowed?
- Are environment variables or secrets involved?

Default: database changes, authentication changes, permission changes, secret handling, and deployment are safety gates.

### 6. Testing Expectations

Determine:

- Should the agent create tests, update tests, or only run existing tests?
- What validation is required before completion?
- Are manual checks acceptable if automated tests are unavailable?

Defaults:

- Run available relevant validation commands.
- Create or update tests when the objective involves logic, APIs, critical flows, or regression risk and when doing so is in scope.

### 7. Definition Of Done

Determine:

- What must be true for the objective to be considered complete?
- Should completion require passing tests?
- Should completion require review rounds?
- Should completion require documentation updates?

Defaults:

- ToDos completed or justified.
- Relevant validation completed or clearly documented.
- Review Subagent Loop passing criteria met or documented as blocked.
- Final report produced.

### 8. Sensitive Areas

Determine:

- Are there files, modules, features, or workflows the agent must not touch?
- Are there business-critical rules that require approval?

Default: sensitive areas must be treated as safety gates when discovered.

## Intake Modes

### Minimal Objective Mode

Use when the user gives only a short objective.

- Ask at most 1 to 3 blocking questions.
- If the target is clear enough, proceed with assumptions.
- Prefer inspection over asking when the repository can answer the question.

### Structured Objective Mode

Use when the user provides target, constraints, and expected outcome.

- Do not ask extra questions unless safety gates are involved.
- Create the Objective Brief and start.

### Continuation Mode

Use when the user asks to continue a previous run.

Inspect existing control files such as:

- `TODO.md`
- `BACKLOG.md`
- `DEVELOPMENT_LOG.md`
- `KNOWN_ISSUES.md`
- `FINAL_REPORT.md`

Continue from the latest reliable state. If the latest state is ambiguous, ask the smallest blocking question needed to resume safely.

## When To Ask Questions

Ask when:

- The objective is too vague to choose a target.
- The requested change may affect a safety gate.
- The definition of done is unclear and cannot be safely assumed.
- The user requested changes across multiple broad areas.
- The agent cannot determine whether database, auth, permissions, secrets, or deployment are involved.
- The user's objective conflicts with existing project instructions.
- The task may require destructive operations.

Do not ask when:

- The user already provided enough context.
- The missing information can be safely inferred.
- The issue can be recorded as an assumption.
- The agent can inspect the project to answer the question.
- The question would only delay a safe, reversible change.

## Assumption Policy

When proceeding without asking, document assumptions.

Assumptions should be:

- Specific
- Safe
- Reversible when possible
- Aligned with the user objective
- Included in the final report

Example:

```markdown
## Assumptions

- No database schema changes are allowed unless explicitly requested.
- Dependency changes are not allowed unless required and approved.
- UI changes are allowed within the target module.
- Existing project commands should be used for validation.
```

## Objective Brief

Before execution, create an Objective Brief. See `kickoff-protocol.md` for the required format.

The Objective Brief may be held in the response, `TODO.md`, `DEVELOPMENT_LOG.md`, or another project control file when persistence is useful.
