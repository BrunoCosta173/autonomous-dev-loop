# Next.js App Usage Example

This is a lightweight documentation example for using `autonomous-dev-loop` in a Next.js project.

It is not a complete example application.

## Example Objective Prompt

```text
Use autonomous-dev-loop to improve the user settings page.
Focus on UI consistency, form validation, loading states, and accessibility.
Do not change database schema, authentication, or dependencies.
Run available lint, typecheck, and build commands.
Use A3 autonomy.
```

## Suggested Constraints

- Keep changes inside the settings page and nearby reusable UI components.
- Do not change authentication or authorization behavior.
- Do not modify database schema or migrations.
- Do not add dependencies unless explicitly approved.
- Preserve existing design system conventions.

## Expected Skill Behavior

The agent should:

1. Inspect the project structure and relevant settings page files.
2. Detect whether the app uses Next.js, React, TypeScript, a form library, and a component system.
3. Read `package.json` scripts before choosing commands.
4. Create an Objective Brief and ToDo list.
5. Improve UI consistency, validation feedback, loading states, and accessibility within scope.
6. Run relevant validation commands when available.
7. Run review passes or review subagents when supported.
8. Produce a final report.

## Example Validation Commands

These are examples only. The agent should prefer commands defined by the project.

```bash
npm run lint
npm run typecheck
npm run build
```

If the project uses another package manager, the agent should detect it from lockfiles and scripts.

## Expected Final Report Content

The final report should include:

- Objective and assumptions
- Files changed
- UI and validation improvements made
- Accessibility considerations
- Commands run and results
- Review rounds or independent review passes
- Safety gates encountered
- Remaining issues or deferred suggestions
- Final status

## Safety Gates To Watch

- Database schema changes
- Authentication or authorization changes
- Dependency installation or upgrades
- Business-critical settings behavior
- Deployment
