# Step 7 Goal Memory Handoff

Status: **Completed**

## Step Goal

Define the Skill's Goal Completion Mode, persistent project memory behavior, continuation behavior, and cross-session handoff protocol.

This step makes the Skill capable of driving a user-provided development objective toward completion without requiring the user to manually type a separate `/goal` command.

## Goal Completion Mode

Goal Completion Mode means that when the user invokes `autonomous-dev-loop` with a development objective, the agent treats that objective as the active goal and works toward completing it in one autonomous run.

The run remains subject to:

- Safety gates
- Blockers
- Configured limits
- Validation requirements
- Review Subagent Loop requirements
- The original user-provided objective

The user should not need to type `/goal`.

## Native Goal Features

The Skill must not treat `/goal` as universally available.

Policy:

1. Use the platform's native goal, long-run, or equivalent workflow when it exists and is safe.
2. Otherwise emulate Goal Completion Mode through the `autonomous-dev-loop` protocol.
3. If needed, fall back to bounded internal cycles using ToDos, validation, review rounds, and final reporting.

## Goal Completion Behavior

When active, the agent should:

1. Parse the user's objective.
2. Create or update an Objective Brief.
3. Define the Definition of Done.
4. Create a ToDo list.
5. Execute all feasible ToDos inside the objective.
6. Run relevant validation commands.
7. Repair failures caused by current changes.
8. Run the Review Subagent Loop.
9. Apply relevant safe corrections.
10. Repeat bounded improvement rounds until complete, blocked, or stopped by a safety gate.
11. Persist progress in project control files when useful.
12. Produce a final report.

The agent should not stop after planning unless the user requested planning only, a safety gate requires approval, the objective is too ambiguous, project access is missing, limits are reached, or a blocker prevents safe progress.

## Autonomy Relationship

Goal Completion Mode maps to autonomy levels:

- `A0 — Manual`: goal planning only.
- `A1 — Assisted`: goal analysis and proposed changes only.
- `A2 — Supervised`: goal execution in supervised batches.
- `A3 — Autonomous With Safety Gates`: default Goal Completion Mode.
- `A4 — Continuous Autonomous Loop`: continuous Goal Completion Mode across multiple internal cycles.

`A3` remains the default recommended level.

`A4` is used only when the user explicitly requests broad continuation, such as "continue until done", "finish the complete scope", or "run the full loop".

## Persistent Project Memory

The Skill uses project control files as persistent memory only when they improve continuity, traceability, or safe continuation.

Relevant files:

- `AGENTS.md`: persistent instructions for generic AI coding agents.
- `CLAUDE.md`: persistent instructions for Claude Code.
- `BACKLOG.md`: longer-term prioritized project work.
- `ROADMAP.md`: high-level product or project direction.
- `TODO.md`: active ToDo list for the current autonomous run.
- `DEVELOPMENT_LOG.md`: cycle-by-cycle history.
- `TEST_PLAN.md`: validation strategy and known test commands.
- `DECISIONS.md`: architecture and product decision log.
- `KNOWN_ISSUES.md`: bugs, blockers, risks, and unresolved issues.
- `FINAL_REPORT.md`: persistent report for completed or partially completed runs.

The Skill should not force all files into every project.

## Continuation Behavior

When the user asks to continue, resume, finish, or pick up previous work, the agent should:

1. Inspect existing control files.
2. Identify the latest objective.
3. Identify latest ToDos and statuses.
4. Read recent development logs.
5. Check known blockers and safety gates.
6. Inspect current git status.
7. Compare actual project state with recorded state.
8. Reconstruct the active goal.
9. Ask only blocking questions.
10. Continue from the latest reliable state.

Continuation priority:

1. Explicit user instruction in the current prompt
2. Current git status and actual files
3. `TODO.md`
4. `DEVELOPMENT_LOG.md`
5. `FINAL_REPORT.md`
6. `KNOWN_ISSUES.md`
7. `BACKLOG.md`
8. `ROADMAP.md`

Actual current project state overrides stale control files.

## Cross-Session Handoff

The agent should persist handoff information when work is incomplete or likely to continue.

Persist a handoff when:

- The objective is partially complete.
- A safety gate stopped execution.
- The maximum review rounds were reached.
- The maximum autonomous cycles were reached.
- The task is too large for a single run.
- The user explicitly asks to stop.
- Validation failures remain unresolved.
- The next step requires human input.

The handoff includes active objective, current status, completed ToDos, pending ToDos, blocked ToDos, files changed, commands run, validation status, review status, safety gates, known issues, next recommended action, and resume instruction.

## Final Statuses

Use these statuses:

- `Complete`: Definition of Done reached, validation complete or justified, review criteria met, and no blocking safety gates remain.
- `Partially complete`: meaningful progress was made, but some ToDos remain pending or deferred, or the run limit was reached.
- `Blocked`: the agent cannot safely continue without approval, access, information, working environment, or safety gate resolution.
- `Failed`: the attempted changes could not be completed and did not produce a usable partial result, or the agent stopped due to unresolved failures.

## Files Updated

New references:

- `goal-completion-mode.md`
- `persistent-memory.md`
- `continuation-handoff.md`

Updated references:

- `objective-intake.md`
- `kickoff-protocol.md`
- `loop-protocol.md`
- `autonomy-model.md`
- `todo-execution.md`
- `documentation-rules.md`
- `final-report.md`

Updated templates:

- `AGENTS.template.md`
- `CLAUDE.template.md`
- `TODO.template.md`
- `DEVELOPMENT_LOG.template.md`
- `FINAL_REPORT.template.md`
- `BACKLOG.template.md`
- `KNOWN_ISSUES.template.md`

## Explicit Non-Goals For Step 7

Step 7 does not:

- Create installer scripts.
- Create complete example projects.
- Polish the final marketing README.
- Add dependencies.
- Claim native `/goal` support exists on every agent platform.

## Future Improvements

Future steps may add:

- Concrete handoff examples.
- Project memory merge guidance.
- Optional sync tooling for duplicated Skill targets.
- Platform-specific notes for native long-running goal workflows.

## Completion Criteria

Step 7 is complete because both Skill targets now define Goal Completion Mode, persistent project memory, continuation priority, cross-session handoff, final status criteria, and template fields needed for continuation.
