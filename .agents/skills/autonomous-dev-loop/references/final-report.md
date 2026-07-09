# Final Report

End each autonomous run with a clear final report.

For a persistent report, copy or adapt `assets/FINAL_REPORT.template.md` into the target project as `FINAL_REPORT.md` when the user asks for durable output or when the run is complex enough to benefit from a saved report.

## Required Sections

Report:

- Objective
- Assumptions
- Plan
- ToDos executed
- Files changed
- Commands run
- Test/build/lint results
- Errors found
- Repairs applied
- Safety gates encountered
- Remaining issues
- Recommended next objective
- Final status

## Final Status Values

Use one of:

- Complete
- Partially complete
- Blocked
- Failed

## Reporting Rules

- Be specific about what changed.
- Include command names and outcomes.
- Do not claim validation passed unless commands actually ran.
- Distinguish failures caused by current work from pre-existing or unrelated failures.
- Mention safety gates even if they were only encountered and not approved.
- Mention assumptions that influenced implementation.
- Keep the report concise but complete enough for another agent or developer to continue.
- Prefer the chat final report for small runs.
- Prefer `FINAL_REPORT.md` for longer runs, blocked work, or handoffs across sessions.

## Recommended Next Objective

Recommend one focused next objective, such as:

- Finish a blocked ToDo after user confirmation.
- Add missing tests for the changed module.
- Address unrelated issues recorded in `KNOWN_ISSUES.md`.
- Convert deferred improvements into a new scoped objective.

Do not recommend broad, vague follow-up work when a specific next objective is available.
