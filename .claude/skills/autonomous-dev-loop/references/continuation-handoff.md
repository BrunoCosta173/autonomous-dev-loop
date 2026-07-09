# Continuation And Handoff

Use this reference when a user asks to continue, resume, finish, or pick up prior autonomous development work, or when a run ends before the objective is fully complete.

## Continuation Behavior

When continuing work across sessions:

1. Inspect existing control files.
2. Identify the latest objective.
3. Identify latest ToDos and their statuses.
4. Read recent development logs.
5. Check known blockers and safety gates.
6. Inspect current git status.
7. Compare current project state with recorded state.
8. Reconstruct the active goal.
9. Ask only blocking questions.
10. Continue from the latest reliable state.

## Continuation Priority

When reconstructing state, use this priority:

1. Explicit user instruction in the current prompt
2. Current git status and actual files
3. `TODO.md`
4. `DEVELOPMENT_LOG.md`
5. `FINAL_REPORT.md`
6. `KNOWN_ISSUES.md`
7. `BACKLOG.md`
8. `ROADMAP.md`

The actual current project state must override stale control files.

## Blocking Questions On Resume

Ask only when continuation cannot proceed safely, such as:

- The latest objective cannot be identified.
- The recorded state conflicts with actual files in a way that affects safety.
- Pending work touches a safety gate.
- The next action could overwrite user changes.
- The Definition of Done is unknown and cannot be safely inferred.

## Handoff Persistence Conditions

Persist a handoff when:

- The objective is partially complete.
- A safety gate stopped execution.
- The maximum review rounds were reached.
- The maximum autonomous cycles were reached.
- The task is too large for a single run.
- The user explicitly asks to stop.
- Validation failures remain unresolved.
- The next step requires human input.

## Handoff Format

Use this format:

```markdown
# Autonomous Development Handoff

## Active objective
...

## Current status
Complete | Partially complete | Blocked | Failed

## Completed ToDos
- ...

## Pending ToDos
- ...

## Blocked ToDos
- ...

## Files changed
- ...

## Commands run
- ...

## Validation status
...

## Review status
...

## Safety gates
...

## Known issues
...

## Next recommended action
...

## Resume instruction
Use `autonomous-dev-loop` to continue from this handoff and the existing project control files.
```

Store the handoff in `DEVELOPMENT_LOG.md`, `FINAL_REPORT.md`, or another appropriate project control file when durable continuation is useful.

## Final Status Criteria

Use these statuses:

### Complete

The objective reached the Definition of Done, validation is complete or justified, Review Subagent Loop criteria are met, and no blocking safety gates remain.

### Partially complete

Meaningful progress was made, but some ToDos remain pending or deferred, or the run limit was reached.

### Blocked

The agent cannot safely continue without human approval, missing access, missing information, a working environment, or resolution of a safety gate.

### Failed

The attempted changes could not be completed and did not produce a usable partial result, or the agent had to stop due to unresolved failures.

## Resume Instruction

When ending with incomplete work, include a clear next action and a short resume instruction. The resume instruction should tell a future agent to use `autonomous-dev-loop`, inspect current files, read relevant control files, and continue from the latest reliable state.
