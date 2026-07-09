# Review Subagent Loop

Use this review cycle after implementation and applicable validation commands, before declaring the scope complete.

## Purpose

The Review Subagent Loop is a quality gate for autonomous development work.

Primary mode: use real review subagents when the current agent environment supports them.

Fallback mode: when real subagents are unavailable, run independent review passes using the same reviewer roles, prompts, and scoring rubrics.

This keeps the mechanism platform-agnostic.

## Reviewer Permissions

Review subagents are read-only reviewers by default.

They may:

- Analyze
- Score
- Identify risks
- Suggest corrections
- Flag safety gates
- Recommend approval, approval with fixes, rejection, or blocked status

They must not directly modify files unless the user explicitly authorizes multi-agent editing.

The main agent remains responsible for deciding which suggestions to apply and for executing corrections.

## Review Cycle

After the main agent implements the planned scope and runs relevant validation:

1. Summarize the implemented scope.
2. Identify changed files.
3. Collect test, build, lint, and typecheck results.
4. Select relevant reviewers from `reviewer-roles.md`.
5. Ask reviewers to evaluate the work.
6. Collect scores, risks, required fixes, suggestions, and safety gates.
7. Analyze review feedback.
8. Apply only corrections that are relevant, safe, and aligned with the original objective.
9. Re-run relevant validation commands.
10. Run another review round if needed and allowed.
11. Stop when passing criteria are met, review limits are reached, or a safety gate is triggered.

## Reviewer Input Packet

Provide reviewers with:

- Original objective
- Autonomy level
- Scope summary
- Non-goals
- Changed files
- Validation commands and results
- Known constraints
- Safety gates already encountered
- Specific review role and rubric

Do not ask reviewers to rewrite the objective or expand scope.

## Review Output Format

Each reviewer should return:

```markdown
## Review: <Reviewer Name>

### Score
<n>/10

### Summary
Brief assessment of the implemented scope.

### Strengths
- ...

### Issues
- ...

### Required fixes
- ...

### Suggested improvements
- ...

### Risk level
Low | Medium | High | Critical

### Safety gates triggered
- None
or
- ...

### Approval
Approved | Approved with required fixes | Rejected | Blocked
```

## Scoring Policy

Use scores from 0 to 10.

Default passing criteria:

- Average score >= 8/10
- No reviewer score below 7/10
- No unresolved critical issue
- No failed relevant validation command
- No unresolved safety gate
- Required fixes are either implemented or explicitly deferred with justification

If criteria are not met, run a correction round unless blocked.

## Review Round Limits

Default limits:

- Default maximum review rounds: 2
- High-autonomy maximum review rounds: 3
- Stop immediately if a safety gate is triggered
- Stop if the same issue repeats twice without progress
- Stop if further changes would exceed the original objective

If criteria are still not met after the maximum review rounds, mark the objective as one of:

- Partially complete
- Blocked
- Failed

Explain why in the final report.

## Main Agent Responsibilities

The main agent must:

- Select only relevant reviewers.
- Keep reviewers read-only by default.
- Evaluate review feedback critically.
- Apply only safe, relevant, objective-aligned corrections.
- Re-run relevant validation after corrections.
- Record review rounds and outcomes in the final report.
- Defer out-of-scope suggestions with justification.

## Completion Rule

Do not declare the objective complete until:

- Relevant validation has passed or unavailable validation is documented.
- Review passing criteria are met.
- Required fixes are handled.
- No unresolved safety gate remains.
