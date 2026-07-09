# Laravel App Usage Example

This is a lightweight documentation example for using `autonomous-dev-loop` in a Laravel project.

It is not a complete example application.

## Example Objective Prompt

```text
Use autonomous-dev-loop to improve the invoice creation workflow.
Focus on validation, controller clarity, form request rules, and test coverage.
Do not change production migrations or payment logic without approval.
Run available Laravel/PHP validation commands.
Use A3 autonomy.
```

## Suggested Constraints

- Keep changes inside invoice creation workflow files and related tests.
- Do not change production migrations without approval.
- Do not change payment logic without approval.
- Do not change authentication or authorization behavior without approval.
- Preserve existing Laravel conventions.

## Expected Skill Behavior

The agent should:

1. Inspect Laravel files such as `composer.json`, `artisan`, routes, controllers, requests, models, and tests.
2. Detect available Composer and Laravel validation commands.
3. Create an Objective Brief and ToDo list.
4. Improve validation, controller clarity, form request rules, and test coverage within scope.
5. Run relevant validation commands when available.
6. Repair failures caused by the changes.
7. Run review passes or review subagents when supported.
8. Produce a final report.

## Example Validation Commands

These are examples only. The agent should prefer commands defined by the project.

```bash
php artisan test
vendor/bin/phpunit
vendor/bin/pint --test
composer test
```

If the project defines different Composer scripts or containerized commands, the agent should use those project-defined commands.

## Expected Final Report Content

The final report should include:

- Objective and assumptions
- Validation and workflow improvements made
- Tests added or updated
- Files changed
- Commands run and results
- Repairs applied
- Review rounds or independent review passes
- Safety gates encountered
- Remaining risks or deferred suggestions
- Final status

## Safety Gates To Watch

- Production migrations
- Payment logic
- Authentication or authorization changes
- Business-critical invoice rules
- Dependency installation or upgrades
- Deployment
