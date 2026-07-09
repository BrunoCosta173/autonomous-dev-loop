# Command Discovery

Use this reference after stack detection and before running commands.

## Core Policy

- Prefer project-defined commands over invented commands.
- Inspect files before deciding commands.
- Detect package managers and frameworks from real files.
- Avoid destructive commands unless explicitly authorized.
- Run the smallest relevant validation command for the objective.
- Document every command executed and its result.
- Clearly report commands that are unavailable or not run.
- Never claim tests passed unless they actually ran.

## Discovery Order

1. Read project instructions such as `AGENTS.md`, `CLAUDE.md`, README files, and docs.
2. Inspect package manifests, lockfiles, framework config, task runner files, and CI workflows.
3. Identify package manager and workspace boundaries.
4. Identify available commands by category.
5. Choose the smallest relevant safe command.
6. Run broader validation only when objective risk justifies it.

## Command Categories

Record commands by category when discoverable:

- install
- dev
- build
- lint
- format
- typecheck
- test
- test:unit
- test:integration
- test:e2e
- migration check
- static analysis

## JavaScript / TypeScript

Read `package.json` scripts first.

Package manager detection:

- `pnpm-lock.yaml` -> use `pnpm`
- `yarn.lock` -> use `yarn`
- `package-lock.json` -> use `npm`
- `bun.lockb` -> use `bun`

Prefer scripts such as:

- `build`
- `lint`
- `format`
- `typecheck`
- `test`
- `test:unit`
- `test:e2e`
- `dev`

Do not run `dev` unless an interactive/local server is needed.

## Python

Detect tools from `pyproject.toml`, lockfiles, config files, and docs.

Prefer project-defined or documented commands.

Common tools may include:

- pytest
- ruff
- black
- mypy
- Django `manage.py test`
- FastAPI/uvicorn only for local development when appropriate

Do not start application servers unless needed for the objective.

## PHP / Laravel

Read `composer.json` scripts first.

Detect Laravel from `artisan`.

Common commands may include:

- `composer test`
- `vendor/bin/phpunit`
- `php artisan test`
- `vendor/bin/pint`

Avoid migration or cache-clearing commands unless they are needed and safe.

## Ruby / Rails

Detect scripts and Rails from `Gemfile`, binstubs, and config.

Common commands may include:

- `bundle exec rspec`
- `bin/rails test`
- `bundle exec rubocop`

Avoid database reset or migration commands without confirmation when data-loss risk exists.

## Java / Spring

Detect Maven or Gradle before choosing commands.

Common commands may include:

- `mvn test`
- `mvn package`
- `./gradlew test`
- `./gradlew build`

Prefer wrapper scripts such as `./gradlew` when present.

## .NET

Common commands may include:

- `dotnet restore`
- `dotnet build`
- `dotnet test`

Prefer solution-scoped commands when a `.sln` exists and project-scoped commands when the objective touches a single project.

## Go

Common commands may include:

- `go test ./...`
- `go vet ./...`
- `go fmt ./...`

Use `gofmt`/`go fmt` carefully because it modifies files. It is usually safe when formatting code touched by the objective.

## Rust

Common commands may include:

- `cargo test`
- `cargo check`
- `cargo clippy`
- `cargo fmt --check`

Use `cargo fmt` only when formatting changes are in scope.

## Mobile

React Native / Expo:

- Inspect package scripts first.
- Prefer project scripts for test, lint, typecheck, and build.

Flutter:

- `flutter analyze`
- `flutter test`
- `flutter build` only when appropriate and not too heavy

Avoid device, signing, store, or deployment commands without explicit authorization.

## Docker / Infra

Detect Docker and Compose files, but avoid destructive Docker commands.

Prefer safe validation such as config checks or local builds when relevant.

Do not deploy unless explicitly authorized.

## Unsafe Commands

Stop for confirmation before commands that:

- Delete files or data in bulk
- Reset databases
- Rewrite Git history
- Force push
- Deploy, publish, or release
- Modify secrets or environment variables
- Change authentication, permissions, or authorization state
- Affect external systems

If unsure, ask before running.
