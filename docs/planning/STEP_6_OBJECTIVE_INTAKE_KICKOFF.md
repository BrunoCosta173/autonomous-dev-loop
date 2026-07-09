# Step 6 Objective Intake And Kickoff

Status: **Completed**

## Step Goal

Define how the Skill starts an autonomous development run.

This step creates the objective intake questionnaire, kickoff protocol, assumption policy, and pre-execution briefing format.

## Core Principle

The Skill should be autonomous, not bureaucratic.

Ask only when the missing answer affects safety, scope, data integrity, business-critical behavior, or the definition of done.

Otherwise, proceed with documented assumptions.

## Default Run Start

When the user invokes the Skill with a development objective, the agent should:

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

The intake model covers:

- Objective
- Scope boundaries
- Autonomy
- Commands and environment
- Data, database, auth, and secrets
- Testing expectations
- Definition of done
- Sensitive areas

## Intake Modes

### Minimal Objective Mode

Used when the user gives only a short objective.

The agent should ask at most 1 to 3 blocking questions. If the target is clear enough, proceed with assumptions.

### Structured Objective Mode

Used when the user provides target, constraints, and expected outcome.

The agent should not ask extra questions unless safety gates are involved.

### Continuation Mode

Used when the user asks to continue a previous run.

The agent should inspect existing control files such as:

- `TODO.md`
- `BACKLOG.md`
- `DEVELOPMENT_LOG.md`
- `KNOWN_ISSUES.md`
- `FINAL_REPORT.md`

Then continue from the latest reliable state.

## Question Policy

Ask questions when:

- The objective is too vague to choose a target.
- The requested change may affect a safety gate.
- The definition of done is unclear and cannot be safely assumed.
- The user requested changes across multiple broad areas.
- The agent cannot determine whether database, auth, permissions, secrets, or deployment are involved.
- The user's objective conflicts with existing project instructions.
- The task may require destructive operations.

Do not ask questions when:

- The user already provided enough context.
- The missing information can be safely inferred.
- The issue can be recorded as an assumption.
- The agent can inspect the project to answer the question.
- The question would only delay a safe, reversible change.

## Assumption Policy

When proceeding without asking, the agent must document assumptions.

Assumptions should be:

- Specific
- Safe
- Reversible when possible
- Aligned with the user objective
- Included in the final report

## Objective Brief Format

```markdown
# Objective Brief

## Objective
...

## Target area
...

## Desired outcome
...

## Non-goals
...

## Autonomy level
A3 — Autonomous With Safety Gates

## Allowed actions
- ...

## Safety gates
- ...

## Assumptions
- ...

## Definition of done
- ...

## Initial validation strategy
- ...

## Review strategy
- ...
```

## Kickoff Response Format

```markdown
## Autonomous Run Kickoff

### Objective
...

### Assumptions
- ...

### Execution plan
1. ...
2. ...
3. ...

### Initial ToDos
- [ ] ...
- [ ] ...
- [ ] ...

### Validation plan
- ...

### Review plan
- ...

### Safety gates to watch
- ...
```

The kickoff should be concise. For small tasks, it can be brief. For large tasks, it should be more explicit.

## Relationship With Existing Architecture

Objective intake determines:

- Autonomy level, defaulting to `A3 — Autonomous With Safety Gates`.
- Safety gates and blocking questions.
- ToDo boundaries.
- Initial validation plan.
- Review Subagent Loop plan.
- Final report expectations.

`A4 — Continuous Autonomous Loop` is used only when explicitly requested and must remain inside the user-provided objective.

## Files Updated

New reference:

- `kickoff-protocol.md`

Updated references:

- `objective-intake.md`
- `loop-protocol.md`
- `autonomy-model.md`
- `safety-gates.md`
- `todo-execution.md`
- `final-report.md`
- `review-subagent-loop.md`

Updated templates:

- `TODO.template.md`
- `DEVELOPMENT_LOG.template.md`
- `FINAL_REPORT.template.md`
- `AGENTS.template.md`
- `CLAUDE.template.md`

## Explicit Non-Goals For Step 6

Step 6 does not:

- Create installer scripts.
- Create complete example projects.
- Polish the final marketing README.
- Add dependencies.
- Add a long bureaucratic intake form.

## Future Improvements

Future steps may add:

- Persistent project memory and continuation rules.
- More examples of good and bad intake.
- Agent-environment-specific kickoff patterns.
- Objective classification heuristics.

## Completion Criteria

Step 6 is complete because both Skill targets now define objective intake, intake modes, question policy, assumption policy, Objective Brief format, kickoff response format, and continuation kickoff behavior.
