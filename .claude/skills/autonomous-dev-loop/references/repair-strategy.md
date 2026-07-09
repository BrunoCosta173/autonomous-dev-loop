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

Update the final report with the blocker, attempted diagnostics, and recommended next action.
