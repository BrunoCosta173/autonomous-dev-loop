# Loop Protocol

Use this protocol for each autonomous development run.

## Core Loop

1. Intake
2. Inspect
3. Detect stack
4. Plan
5. Generate ToDos
6. Execute
7. Test
8. Repair
9. Document
10. Report
11. Continue or stop

## Loop Rules

- Continue while unfinished ToDos remain inside the current objective.
- Do not switch to unrelated scope.
- If unrelated issues are discovered, record them instead of fixing them immediately.
- Stop when the objective is complete, blocked by a safety gate, blocked by missing information, or no feasible ToDos remain.

## Phase Guidance

### Intake

Clarify the objective only as much as needed to execute safely. Record assumptions before file edits.

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

Create a short execution plan tied directly to the objective.

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

### Document

Update useful project control files when doing so improves continuity or traceability.

Use templates from `assets/` as starting points. Do not create every template automatically.

### Report

Produce a final report with objective status, changed files, commands, results, issues, and next recommended objective.

Use `assets/FINAL_REPORT.template.md` when a persistent `FINAL_REPORT.md` is useful.

Include commands that were unavailable, skipped, unsafe, or not run, with reasons.

## Unrelated Findings

If the agent finds issues outside the objective, record them in `BACKLOG.md` or `KNOWN_ISSUES.md` when such a file exists or would clearly improve continuity.

Do not fix unrelated issues during the current loop unless the user confirms a scope expansion.
