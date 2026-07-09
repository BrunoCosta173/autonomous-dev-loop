# Stack Detection

Detect the stack by inspecting project files and available commands before choosing implementation or validation commands.

Do not assume a default stack. Do not claim guaranteed compatibility with every stack. Adapt to evidence in the repository.

## Core Principles

- Inspect project files before deciding commands.
- Prefer project-defined commands over invented commands.
- Detect package managers and frameworks from real files.
- Avoid destructive commands unless explicitly authorized.
- Choose the smallest relevant validation commands for the objective.
- Document uncertainty when evidence is incomplete.

## JavaScript / TypeScript Signals

Look for:

- `package.json`
- `pnpm-lock.yaml`
- `yarn.lock`
- `package-lock.json`
- `bun.lockb`
- `tsconfig.json`
- `vite.config.*`
- `next.config.*`
- `nuxt.config.*`
- `angular.json`
- `vue.config.*`
- `svelte.config.*`
- `astro.config.*`

Package manager detection:

- `pnpm-lock.yaml` -> pnpm
- `yarn.lock` -> yarn
- `package-lock.json` -> npm
- `bun.lockb` -> bun

See `frontend-playbooks.md` for frontend-specific command guidance.

## Python Signals

Look for:

- `pyproject.toml`
- `requirements.txt`
- `poetry.lock`
- `uv.lock`
- `Pipfile`
- `setup.py`
- `manage.py`

Common tool hints include pytest, ruff, black, mypy, Django, Flask, FastAPI, uv, Poetry, and Pipenv.

See `backend-playbooks.md` for Python command guidance.

## PHP Signals

Look for:

- `composer.json`
- `composer.lock`
- `artisan`

`artisan` usually indicates Laravel.

## Ruby Signals

Look for:

- `Gemfile`
- `Gemfile.lock`
- `config/routes.rb`

`config/routes.rb` with Rails gems usually indicates Ruby on Rails.

## Java / JVM Signals

Look for:

- `pom.xml`
- `build.gradle`
- `settings.gradle`
- `gradlew`

Use Maven or Gradle evidence before selecting commands.

## .NET Signals

Look for:

- `*.sln`
- `*.csproj`
- `global.json`

Use solution and project files to identify build/test boundaries.

## Go Signals

Look for:

- `go.mod`
- `go.sum`

## Rust Signals

Look for:

- `Cargo.toml`
- `Cargo.lock`

## Mobile Signals

Look for:

- `pubspec.yaml`
- `android/`
- `ios/`
- `react-native.config.js`
- `expo.*`
- `app.json`

See `mobile-playbooks.md` for React Native, Expo, and Flutter guidance.

## Infra / DevOps Signals

Look for:

- `Dockerfile`
- `docker-compose.yml`
- `compose.yml`
- `.github/workflows/*`
- `vercel.json`
- `netlify.toml`
- `terraform/`
- `*.tf`

See `infra-playbooks.md` for safe infrastructure command guidance.

## Detection Output

Record:

- Languages and frameworks
- Package managers
- Runtime versions, if discoverable
- Test tools
- Build tools
- Lint and formatting tools
- Database or BaaS hints
- Docker or infrastructure hints
- CI workflow commands
- Unknowns or ambiguous signals

## Command Discovery

After stack detection, read `command-discovery.md`.

Use stack playbooks only after inspecting the project. Playbooks are heuristics, not permission to ignore project-defined commands.
