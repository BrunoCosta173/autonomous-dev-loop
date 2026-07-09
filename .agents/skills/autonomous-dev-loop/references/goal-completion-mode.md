# Goal Completion Mode

Use Goal Completion Mode when the user invokes `autonomous-dev-loop` with a development objective.

## Definition

Goal Completion Mode means the agent treats the user-provided development objective as the active goal and works toward completing it in one autonomous run, subject to safety gates, blockers, configured limits, and review requirements.

The user should not need to type `/goal`.

Do not claim that `/goal`, native goal mode, or long-running goal workflows are universally available across agent platforms.

## Platform Policy

Use this order:

1. Primary mode: use the platform's native goal, long-run, or equivalent workflow when it exists and is safe.
2. Default mode: emulate Goal Completion Mode through the `autonomous-dev-loop` protocol.
3. Fallback mode: run bounded internal cycles using ToDos, validation, the Review Subagent Loop, and final reporting.

If native goal support is unavailable or unclear, emulate the behavior through this Skill.

## Goal Completion Behavior

When Goal Completion Mode is active, the agent should:

1. Parse the user's objective.
2. Create or update an Objective Brief.
3. Define the Definition of Done.
4. Create a ToDo list.
5. Execute all feasible ToDos inside the objective.
6. Run relevant validation commands.
7. Repair failures caused by current changes.
8. Run the Review Subagent Loop.
9. Apply relevant safe corrections.
10. Repeat bounded improvement rounds until the objective is complete, blocked, or stopped by a safety gate.
11. Persist progress in project control files when useful.
12. Produce a final report.

## When Not To Stop After Planning

Do not stop after planning unless:

- The user explicitly requested planning only.
- A safety gate requires approval.
- The objective is too ambiguous to start.
- Required project access is missing.
- The configured run limit is reached.
- A blocker prevents safe progress.

## Relationship To Autonomy Levels

- `A0 — Manual`: goal planning only.
- `A1 — Assisted`: goal analysis and proposed changes only.
- `A2 — Supervised`: goal execution in supervised batches.
- `A3 — Autonomous With Safety Gates`: default Goal Completion Mode with safety gates.
- `A4 — Continuous Autonomous Loop`: continuous Goal Completion Mode across multiple internal cycles, bounded by the original objective.

Use A3 by default.

Use A4 only when the user explicitly requests broad autonomous continuation, such as:

- "continue until done"
- "execute the whole implementation"
- "finish the complete scope"
- "keep improving until the objective is complete"
- "run the full loop"

A4 must still stay inside the original objective and stop at safety gates.

## Boundaries

Goal Completion Mode does not permit scope expansion.

The agent must not:

- Work on unrelated findings without confirmation.
- Continue past a safety gate.
- Treat stale control files as more reliable than current user instructions or actual project state.
- Claim completion when validation, review, or required ToDos are incomplete without explanation.

## Completion Criteria

The goal can be marked `Complete` only when:

- The Definition of Done is met.
- Feasible ToDos are done or justified.
- Relevant validation passed or unavailable validation is documented.
- Review Subagent Loop criteria are met or documented as unavailable or blocked.
- No unresolved safety gate remains.

If these criteria are not met, use `Partially complete`, `Blocked`, or `Failed` as defined in `continuation-handoff.md` and `final-report.md`.
