# Repair Strategy

Use this reference when validation fails or implementation defects are found.

## Failure Triage

When tests, build, lint, typecheck, or runtime checks fail:

1. Identify the failing command.
2. Read the relevant error output.
3. Determine whether the failure was caused by current changes.
4. Fix failures caused by current work.
5. Document unrelated failures separately.

## Repair Rules

- Fix root causes instead of hiding errors.
- Do not delete tests to make the suite pass.
- Do not weaken assertions without a clear reason tied to the objective.
- Do not suppress lint/type errors unless the suppression is justified and localized.
- Keep repairs inside the objective scope.
- Re-run relevant validation after repair when feasible.
- Apply review feedback only when it is relevant, safe, and aligned with the original objective.
- Do not allow review feedback to expand scope without confirmation.

## Unrelated Failures

If an unrelated failure exists:

- Do not silently fix it as part of the current objective.
- Record it in `KNOWN_ISSUES.md` when durable tracking is useful.
- Mention it in the final report.
- Continue only if the unrelated failure does not block validation of the objective.

## Blocked Repairs

Mark the loop blocked when repair requires:

- A safety-gated action without confirmation
- Missing product decisions
- Missing credentials or services
- External systems unavailable in the environment
- A scope expansion outside the current objective
- Repeated review feedback that cannot be resolved without changing the objective

Update the final report with the blocker, attempted diagnostics, and recommended next action.

## Review-Driven Repairs

After each Review Subagent Loop round:

1. Group feedback into required fixes, suggested improvements, safety gates, and out-of-scope items.
2. Apply required fixes that are safe and inside the objective.
3. Defer suggestions that are useful but outside scope, documenting the reason.
4. Stop for safety gates before applying gated changes.
5. Re-run relevant validation after fixes.
6. Run another review round when passing criteria were not met and review-round limits allow it.

Do not treat reviewer suggestions as commands. The main agent remains responsible for deciding which corrections to apply and executing them.
