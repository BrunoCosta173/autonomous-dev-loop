---
name: autonomous-dev-loop
description: "Structured autonomous software development loop with safety gates, Goal Completion Mode, review rounds, and cross-session handoff. Use when Codex should execute a user-provided development objective by inspecting a project, detecting the stack, planning ToDos, modifying files, running validation commands, repairing failures, documenting changes, and producing a final report."
---

# autonomous-dev-loop

Use this Skill to run an objective-driven autonomous development loop with safety gates.

## Core Model

```text
Objective-driven autonomous development loop with safety gates
```

Require a user-provided development objective. If the objective is too vague, ask only blocking intake questions. If it is clear enough, proceed with safe assumptions and record them before execution.

When invoked with a development objective, treat that objective as the active goal through Goal Completion Mode. Use a platform-native goal or long-run workflow only when supported and safe; otherwise emulate goal-oriented execution through this Skill.

## Workflow

Follow this loop:

1. Intake
2. Kickoff
3. Inspect
4. Detect stack
5. Plan
6. Generate ToDos
7. Execute
8. Test
9. Repair
10. Review
11. Document
12. Report
13. Continue or stop

Continue while unfinished ToDos remain inside the current objective. Do not drift into unrelated scope. Before declaring completion, run the Review Subagent Loop or independent review passes when real subagents are unavailable.

## Safety Gates

Use autonomous execution for safe, objective-scoped work. Stop for human confirmation before destructive commands, mass deletion, data-loss migrations, authentication or authorization changes, secret or environment handling, deployment, major rewrites, framework replacement, irreversible operations, business-critical rule changes, or materially ambiguous product decisions.

## References

Load the relevant reference file for each phase:

- `references/objective-intake.md`: objective intake, assumptions, and blocking questions.
- `references/kickoff-protocol.md`: Objective Brief, kickoff response, and continuation kickoff formats.
- `references/goal-completion-mode.md`: active-goal behavior, platform policy, and completion criteria.
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
- `references/review-subagent-loop.md`: review rounds, scoring, correction cycles, and completion quality gates.
- `references/reviewer-roles.md`: reviewer selection rules and role rubrics.
- `references/documentation-rules.md`: project control file guidance.
- `references/persistent-memory.md`: project memory file roles and persistence policy.
- `references/continuation-handoff.md`: continuation priority, handoff format, and final status criteria.
- `references/final-report.md`: required final report structure.

## Equivalence Requirement

Keep this Codex/OpenAI Skill behaviorally equivalent to the Claude Code Skill at `.claude/skills/autonomous-dev-loop/SKILL.md`.
