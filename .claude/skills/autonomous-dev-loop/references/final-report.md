# Final Report

End each autonomous run with a clear final report.

For a persistent report, copy or adapt `assets/FINAL_REPORT.template.md` into the target project as `FINAL_REPORT.md` when the user asks for durable output or when the run is complex enough to benefit from a saved report.

## Required Sections

Report:

- Objective
- Starting context or Objective Brief summary
- Autonomy level used
- Assumptions
- Definition of done
- Plan
- ToDos executed
- Files changed
- Commands run
- Commands unavailable or not run
- Test/build/lint results
- Errors found
- Repairs applied
- Safety gates encountered
- Review subagents or review passes used
- Number of review rounds
- Reviewer scores per round
- Average score per round
- Required fixes applied
- Suggestions deferred and why
- Final review status
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
- If commands were unavailable or not run, say why.
- Distinguish failures caused by current work from pre-existing or unrelated failures.
- Mention safety gates even if they were only encountered and not approved.
- Include review rounds, reviewer scores, required fixes, deferred suggestions, and final review status.
- Mention assumptions that influenced implementation.
- Mention any assumptions that replaced non-blocking intake questions.
- State whether the definition of done was met.
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
