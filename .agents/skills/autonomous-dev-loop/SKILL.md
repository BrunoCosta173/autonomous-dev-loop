---
name: autonomous-dev-loop
description: "Structured autonomous software development loop with safety gates. Use when Codex should execute a user-provided development objective by inspecting a project, detecting the stack, planning ToDos, modifying files, running available validation commands, repairing failures, documenting changes, and producing a final report."
---

# autonomous-dev-loop

Use this Skill to run an objective-driven autonomous development loop with safety gates.

## Core Model

```text
Objective-driven autonomous development loop with safety gates
```

Require a user-provided development objective. If the objective is too vague, ask only blocking intake questions. If it is clear enough, proceed with safe assumptions and record them before execution.

## Workflow

Follow this loop:

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

Continue while unfinished ToDos remain inside the current objective. Do not drift into unrelated scope.

## Safety Gates

Use autonomous execution for safe, objective-scoped work. Stop for human confirmation before destructive commands, mass deletion, data-loss migrations, authentication or authorization changes, secret or environment handling, deployment, major rewrites, framework replacement, irreversible operations, business-critical rule changes, or materially ambiguous product decisions.

## References

Load the relevant reference file for each phase:

- `references/objective-intake.md`: objective intake, assumptions, and blocking questions.
- `references/autonomy-model.md`: allowed autonomous actions and confirmation boundaries.
- `references/loop-protocol.md`: complete loop protocol and stop conditions.
- `references/todo-execution.md`: ToDo format, statuses, prioritization, and validation.
- `references/scope-management.md`: scope boundaries and unrelated findings.
- `references/safety-gates.md`: mandatory human confirmation rules.
- `references/stack-detection.md`: stack and command detection guidance.
- `references/command-discovery.md`: command discovery policy and safe command selection.
- `references/frontend-playbooks.md`: frontend framework validation playbooks.
- `references/backend-playbooks.md`: backend, API, CLI, and service validation playbooks.
- `references/mobile-playbooks.md`: mobile project validation playbooks.
- `references/infra-playbooks.md`: Docker, CI, deployment config, and infrastructure playbooks.
- `references/testing-strategy.md`: command selection and validation reporting.
- `references/repair-strategy.md`: failure triage and repair rules.
- `references/documentation-rules.md`: project control file guidance.
- `references/final-report.md`: required final report structure.

## Equivalence Requirement

Keep this Codex/OpenAI Skill behaviorally equivalent to the Claude Code Skill at `.claude/skills/autonomous-dev-loop/SKILL.md`.
