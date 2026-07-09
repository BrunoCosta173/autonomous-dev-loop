# Testing Strategy

Detect available commands before running validation.

## Command Categories

Common categories:

- install
- dev
- build
- lint
- format
- typecheck
- test
- e2e
- migration check
- static analysis

## Detection

Inspect project files for commands:

- `package.json` scripts
- Makefiles
- task runner configs
- language-specific config files
- CI workflow files
- framework documentation in the repository

Prefer commands already used by the project.

## Command Selection

Run the most relevant available commands for the objective.

Examples:

- UI change: lint, typecheck, unit/component tests, build when available.
- API change: targeted tests, broader test suite if affordable, typecheck/static analysis.
- Refactor: targeted tests first, then broader tests or build.
- Docs-only change: documentation checks if available; otherwise state that no runtime tests were needed.

## Execution Rules

- Avoid destructive or deployment commands unless explicitly authorized.
- Do not install dependencies unless dependency changes or install commands are authorized.
- Prefer targeted validation first when full suites are expensive.
- Run broader validation when risk or blast radius is high and commands are available.
- Capture command names and results for the final report.

## Reporting

Never claim tests passed unless they actually ran.

If tests were not run, state why:

- No relevant command found.
- Command requires missing dependency or service.
- Command would require authorization.
- Time or environment constraints prevented execution.

If commands fail, report the failing command and whether the failure appears related to current changes.
