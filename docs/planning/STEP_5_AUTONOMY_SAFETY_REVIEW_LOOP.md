# Step 5 Autonomy, Safety, And Review Loop

Status: **Completed**

## Step Goal

Define detailed autonomy levels, safety gates, approval policies, and the Review Subagent Loop.

This step makes the autonomous development loop safer and higher quality by requiring structured review rounds before a scope can be considered complete.

## Autonomy Levels

The Skill defines five autonomy levels:

### A0 — Manual

The agent proposes plans and instructions only. It does not edit files or run commands.

### A1 — Assisted

The agent may inspect files and propose changes, but asks before editing.

### A2 — Supervised

The agent may edit files and run safe validation commands, but asks before each meaningful execution batch.

### A3 — Autonomous With Safety Gates

Default recommended level.

The agent may plan, edit, test, repair, document, and run review rounds autonomously, but must stop at safety gates.

### A4 — Continuous Autonomous Loop

The agent may continue across multiple internal cycles within the user-provided objective, using review rounds and safety gates.

It must not expand beyond the objective without confirmation.

## Safety Gates

Human approval is required before:

- Destructive commands
- Mass deletion
- Database migrations with data-loss risk
- Authentication changes
- Authorization or permission changes
- Secret or environment variable handling
- Deployment
- Major architecture rewrites
- Framework replacement
- Business-critical rule changes
- Irreversible operations
- Ambiguous product decisions that materially affect behavior
- Installing or upgrading critical dependencies
- Changing licensing terms
- Removing tests to make validation pass
- Disabling validation tools or CI checks

## Approval Policy

The agent must explain the proposed action, risk, affected files or systems, safer alternatives, and exact command or change when applicable.

The agent must not proceed past a required safety gate until the user confirms.

## Review Subagent Loop

The Review Subagent Loop is a quality gate performed after implementation and applicable validation commands, before declaring a scope complete.

Primary mode:

- Use real review subagents when supported by the current agent environment.

Fallback mode:

- Run independent review passes using the same reviewer roles and rubrics when real subagents are unavailable.

Reviewers are read-only by default. They analyze, score, identify risks, suggest corrections, flag safety gates, and recommend approval outcomes. They do not directly modify files unless the user explicitly authorizes multi-agent editing.

The main agent remains responsible for deciding which suggestions to apply and executing corrections.

## Review Cycle

The review cycle should:

1. Summarize the implemented scope.
2. Identify changed files.
3. Collect test, build, lint, and typecheck results.
4. Ask relevant review subagents or review passes to evaluate the work.
5. Receive scores, risks, required fixes, and suggestions.
6. Analyze review feedback.
7. Apply only corrections that are relevant, safe, and aligned with the original objective.
8. Re-run relevant validation commands.
9. Run another review round if needed.
10. Stop when quality thresholds are met, max review rounds are reached, or a safety gate is triggered.

## Reviewer Roles

The Skill defines these reviewer roles:

- Scope Reviewer
- Code Quality Reviewer
- Test Reviewer
- Security Reviewer
- UX/UI Reviewer
- Documentation Reviewer
- Architecture Reviewer

The Skill should not call every reviewer every time.

Default selection:

- Scope Reviewer: always.
- Code Quality Reviewer: when code changed.
- Test Reviewer: when logic, tests, APIs, or validation changed.
- Security Reviewer: when authentication, permissions, inputs, APIs, data handling, secrets, or dependencies are involved.
- UX/UI Reviewer: when UI, flows, forms, layouts, copy, accessibility, or user-facing behavior changed.
- Documentation Reviewer: when docs, README, templates, specs, instructions, or public-facing content changed.
- Architecture Reviewer: when structure, cross-cutting concerns, dependencies, module boundaries, frameworks, or large refactors changed.

## Scoring Policy

Reviewers score from 0 to 10.

Default passing criteria:

- Average score >= 8/10
- No reviewer score below 7/10
- No unresolved critical issue
- No failed relevant validation command
- No unresolved safety gate
- Required fixes are either implemented or explicitly deferred with justification

## Review Round Limits

Default limits:

- Default maximum review rounds: 2
- High-autonomy maximum review rounds: 3
- Stop immediately if a safety gate is triggered
- Stop if the same issue repeats twice without progress
- Stop if further changes would exceed the original objective

If criteria are still not met after the maximum review rounds, the agent should mark the objective as partially complete, blocked, or failed and explain why.

## Stop Conditions

The loop stops when:

- The objective is complete
- The ToDo list is complete or all remaining items are blocked/deferred
- Validation commands pass or failures are clearly unrelated and documented
- Review Subagent Loop passing criteria are met
- A safety gate requires human approval
- The maximum review rounds are reached
- The same issue repeats without progress
- The objective becomes too broad or ambiguous
- The user's defined budget, time, or command constraints are reached

## Final Report Impact

Final reports now include:

- Autonomy level used
- Safety gates encountered
- Review subagents or review passes used
- Number of review rounds
- Reviewer scores per round
- Average score per round
- Required fixes applied
- Suggestions deferred and why
- Final review status
- Whether the objective is complete, partially complete, blocked, or failed

## Skill Files Updated

New references:

- `review-subagent-loop.md`
- `reviewer-roles.md`

Updated references:

- `autonomy-model.md`
- `safety-gates.md`
- `loop-protocol.md`
- `repair-strategy.md`
- `final-report.md`

Updated templates:

- `DEVELOPMENT_LOG.template.md`
- `TODO.template.md`
- `FINAL_REPORT.template.md`
- `KNOWN_ISSUES.template.md`

## Explicit Non-Goals For Step 5

Step 5 does not:

- Create installer scripts.
- Create complete example projects.
- Polish the final marketing README.
- Add dependencies.
- Assume every platform supports real subagents.
- Allow review subagents to directly modify files by default.

## Future Improvements

Future steps may add:

- More detailed reviewer prompt templates.
- Environment-specific subagent invocation examples.
- Review outcome examples.
- Automation for review score aggregation.
- Stronger approval policy examples.

## Completion Criteria

Step 5 is complete because the Skill now defines autonomy levels, safety gates, approval policies, review roles, review scoring, review round limits, stop conditions, and final report impacts in both Skill targets.
