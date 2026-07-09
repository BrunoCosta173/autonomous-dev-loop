# Kickoff Protocol

Use this reference after objective intake and before making changes.

## Purpose

The kickoff protocol turns the user objective into a concise Objective Brief, Execution Plan, initial ToDos, validation plan, and review plan.

It should give the user enough visibility into the run without turning the process into bureaucracy.

When the user provides a development objective, the kickoff also establishes Goal Completion Mode unless the user requested planning only.

## Objective Brief Format

Use this format:

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

## Goal Completion Mode
Active | Planning only | Supervised batches | Continuous autonomous loop

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

Default autonomy level: `A3 — Autonomous With Safety Gates`.

Use `A4 — Continuous Autonomous Loop` only when the user explicitly asks the agent to continue through multiple internal cycles or broadly improve an area until completion.

Do not require the user to type `/goal`. Use a native platform goal workflow only when it exists and is safe; otherwise emulate Goal Completion Mode through the Skill protocol.

## Kickoff Response Format

Before making changes, produce a concise kickoff when appropriate:

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

For small tasks, keep the kickoff brief.

For large tasks, make the kickoff more explicit but still concise.

## Kickoff Rules

- Do not ask non-blocking questions.
- State assumptions before file edits.
- Keep the execution plan tied to the objective.
- Include safety gates that may be encountered.
- Include validation and review strategy.
- Start execution after the kickoff unless a blocking question or safety gate prevents progress.

## Continuation Kickoff

When continuing a previous run:

1. Inspect existing control files such as `TODO.md`, `DEVELOPMENT_LOG.md`, `KNOWN_ISSUES.md`, `BACKLOG.md`, and `FINAL_REPORT.md`.
2. Identify the latest reliable objective, ToDos, validation state, review state, and blockers.
3. Produce a short continuation kickoff.
4. Continue from the latest reliable state.

Use this continuation summary:

```markdown
## Continuation Kickoff

### Previous objective
...

### Latest reliable state
...

### Remaining ToDos
- ...

### Known blockers or safety gates
- ...

### Next execution step
...
```

Use `continuation-handoff.md` to reconstruct state and resolve conflicts between control files and actual project files.

## Relationship To The Loop

The kickoff protocol feeds:

- `todo-execution.md` for ToDo structure.
- `goal-completion-mode.md` for active-goal behavior.
- `command-discovery.md` and `testing-strategy.md` for validation planning.
- `review-subagent-loop.md` for review planning.
- `persistent-memory.md` and `continuation-handoff.md` for durable continuation.
- `final-report.md` for final report expectations.
