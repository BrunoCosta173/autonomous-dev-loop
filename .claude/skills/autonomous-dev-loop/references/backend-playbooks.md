# Backend Playbooks

Use this reference for API, service, CLI, and server-side objectives after reading `stack-detection.md` and `command-discovery.md`.

## General Backend Flow

1. Inspect manifests, framework files, and tests.
2. Identify package manager, language toolchain, and service boundaries.
3. Prefer targeted tests for changed modules.
4. Run broader validation when shared behavior or public APIs change.
5. Avoid database, auth, permission, and deployment commands without confirmation when risk exists.

## Node.js / Express / NestJS

Signals:

- `package.json`
- TypeScript config
- Express/Nest dependencies

Likely validation:

- `test`
- `test:unit`
- `test:e2e`
- `lint`
- `typecheck`
- `build`

Prefer package scripts and workspace-scoped commands.

## Python / FastAPI / Django / Flask

Signals:

- `pyproject.toml`
- `requirements.txt`
- `poetry.lock`
- `uv.lock`
- `Pipfile`
- `manage.py`

Likely validation:

- pytest command from docs or config
- ruff check
- black check
- mypy
- Django `manage.py test`

Use app servers such as uvicorn only when local runtime validation is necessary.

## PHP / Laravel

Signals:

- `composer.json`
- `composer.lock`
- `artisan`

Likely validation:

- `composer test`
- `vendor/bin/phpunit`
- `php artisan test`
- `vendor/bin/pint`

Treat migrations, seeders, queue workers, and cache commands carefully. Ask before data-risking actions.

## Ruby / Rails

Signals:

- `Gemfile`
- `Gemfile.lock`
- `config/routes.rb`

Likely validation:

- `bundle exec rspec`
- `bin/rails test`
- `bundle exec rubocop`

Ask before database reset, destructive migrations, or credential changes.

## Java / Spring Boot

Signals:

- `pom.xml`
- `build.gradle`
- `settings.gradle`
- `gradlew`

Likely validation:

- `mvn test`
- `mvn package`
- `./gradlew test`
- `./gradlew build`

Prefer wrappers when present. Use targeted module builds in multi-module repos when available.

## .NET / ASP.NET Core

Signals:

- `*.sln`
- `*.csproj`
- `global.json`

Likely validation:

- `dotnet build`
- `dotnet test`
- `dotnet restore` only when dependencies must be restored

Prefer solution-level validation for shared changes and project-level validation for focused changes.

## Go

Signals:

- `go.mod`
- `go.sum`

Likely validation:

- `go test ./...`
- `go vet ./...`
- `go fmt ./...`

For narrow changes, targeted package tests may be enough before broader `go test ./...`.

## Rust

Signals:

- `Cargo.toml`
- `Cargo.lock`

Likely validation:

- `cargo check`
- `cargo test`
- `cargo clippy`
- `cargo fmt --check`

Use workspace flags only when the repository structure indicates a workspace.

## Database-Related Work

Migration checks may be useful, but stop for confirmation before migrations with data-loss risk, resets, drops, or commands that mutate shared data.

When database validation is blocked by missing services, document the blocker and any safe checks that were run.
