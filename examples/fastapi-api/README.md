# FastAPI API Usage Example

This is a lightweight documentation example for using `autonomous-dev-loop` in a FastAPI project.

It is not a complete example application.

## Example Objective Prompt

```text
Use autonomous-dev-loop to add tests for the orders API.
Focus on request validation, success responses, and error cases.
Do not change database schema or authentication rules.
Run available test and lint commands.
Use A3 autonomy.
```

## Suggested Constraints

- Focus on the orders API routes, schemas, services, and tests.
- Do not change database schema or migrations.
- Do not change authentication, authorization, or permission rules.
- Do not add dependencies unless explicitly approved.
- Preserve existing test style and fixtures.

## Expected Skill Behavior

The agent should:

1. Inspect the FastAPI project structure and existing test layout.
2. Detect Python tooling from `pyproject.toml`, `requirements.txt`, lockfiles, and test configuration.
3. Identify project-defined test and lint commands.
4. Create an Objective Brief and ToDo list.
5. Add or update tests for request validation, success responses, and error cases.
6. Run relevant validation commands when available.
7. Repair failures caused by the new tests or code changes.
8. Run review passes or review subagents when supported.
9. Produce a final report.

## Example Validation Commands

These are examples only. The agent should prefer commands defined by the project.

```bash
pytest
ruff check .
mypy .
```

If the project uses a task runner, containerized workflow, or different commands, the agent should use the project-defined commands.

## Expected Final Report Content

The final report should include:

- Objective and assumptions
- Test cases added or updated
- Files changed
- Commands run and results
- Failures found and repairs applied
- Review rounds or independent review passes
- Safety gates encountered
- Remaining test gaps
- Final status

## Safety Gates To Watch

- Database schema changes
- Authentication or authorization rule changes
- Secret or environment variable handling
- Production data assumptions
- Dependency installation or upgrades
