# Loop Protocol

Use this protocol for each autonomous development run.

When the user invokes the Skill with a development objective, run the loop in Goal Completion Mode unless the user explicitly requested planning only.

## Core Loop

1. Intake
2. Inspect
3. Detect stack
4. Plan
5. Generate ToDos
6. Execute
7. Test
8. Repair
9. Review
10. Document
11. Report
12. Continue or stop

## Loop Rules

- Continue while unfinished ToDos remain inside the current objective.
- Treat the user-provided objective as the active goal and drive it toward completion.
- Do not switch to unrelated scope.
- If unrelated issues are discovered, record them instead of fixing them immediately.
- Stop when the objective is complete, blocked by a safety gate, blocked by missing information, or no feasible ToDos remain.
- Do not declare completion until relevant validation has run or been documented as unavailable, and the Review Subagent Loop passing criteria are met.
- Persist progress in project control files when useful for continuation or traceability.

## Stop Conditions

Stop when:

- The objective is complete.
- The ToDo list is complete or all remaining items are blocked/deferred.
- Validation commands pass or failures are clearly unrelated and documented.
- Review Subagent Loop passing criteria are met.
- A safety gate requires human approval.
- The maximum review rounds are reached.
- The maximum autonomous cycles are reached.
- The same issue repeats twice without progress.
- The objective becomes too broad or ambiguous.
- The user's defined budget, time, or command constraints are reached.

## Phase Guidance

### Intake

Clarify the objective only as much as needed to execute safely. Ask only blocking questions. Record assumptions before file edits.

Read `objective-intake.md`, `kickoff-protocol.md`, and `goal-completion-mode.md`.

### Inspect

Read the repository structure, relevant files, existing docs, tests, and recent conventions before planning changes.

### Detect Stack

Identify languages, frameworks, package managers, test tools, build tools, and deployment or workflow hints from project files.

Read `stack-detection.md`, then `command-discovery.md`, then the relevant stack playbook:

- `frontend-playbooks.md`
- `backend-playbooks.md`
- `mobile-playbooks.md`
- `infra-playbooks.md`

### Plan

Create a short execution plan tied directly to the objective, then produce a concise kickoff when appropriate.

The kickoff should include the Objective Brief, assumptions, execution plan, initial ToDos, validation plan, review plan, and safety gates to watch.

### Generate ToDos

Convert the plan into executable ToDos with priority, status, likely files, and validation method.

Use `assets/TODO.template.md` when the active run needs a persistent `TODO.md`.

### Execute

Work through feasible ToDos autonomously. Keep edits scoped and update ToDo status as work progresses.

### Test

Run relevant available commands. Prefer project-defined commands over invented commands.

Choose the smallest relevant validation command first, then broaden only when risk or blast radius justifies it.

### Repair

Fix failures caused by current changes. Document unrelated failures separately.

### Review

Run the Review Subagent Loop after implementation and validation, before declaring scope complete.

Use real review subagents when the environment supports them. If real subagents are unavailable, run independent review passes using the same reviewer roles and rubrics.

Read `review-subagent-loop.md` and `reviewer-roles.md`.

### Document

Update useful project control files when doing so improves continuity or traceability.

Use templates from `assets/` as starting points. Do not create every template automatically.

Read `persistent-memory.md`.

### Report

Produce a final report with objective status, changed files, commands, results, issues, and next recommended objective.

Use `assets/FINAL_REPORT.template.md` when a persistent `FINAL_REPORT.md` is useful.

Include commands that were unavailable, skipped, unsafe, or not run, with reasons.

If work is incomplete or likely to continue, include or persist a handoff using `continuation-handoff.md`.

## Unrelated Findings

If the agent finds issues outside the objective, record them in `BACKLOG.md` or `KNOWN_ISSUES.md` when such a file exists or would clearly improve continuity.

Do not fix unrelated issues during the current loop unless the user confirms a scope expansion.
