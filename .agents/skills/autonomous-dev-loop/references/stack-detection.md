# Stack Detection

Detect the stack by inspecting project files and available commands.

Do not assume a default stack. Do not claim universal guaranteed compatibility. Adapt to the evidence in the repository.

## Files To Inspect

Look for:

- `package.json`
- `pnpm-lock.yaml`
- `yarn.lock`
- `package-lock.json`
- `tsconfig.json`
- `vite.config.*`
- `next.config.*`
- `angular.json`
- `vue.config.*`
- `svelte.config.*`
- `pyproject.toml`
- `requirements.txt`
- `poetry.lock`
- `uv.lock`
- `Pipfile`
- `manage.py`
- `composer.json`
- `artisan`
- `Gemfile`
- `go.mod`
- `Cargo.toml`
- `*.csproj`
- `*.sln`
- `pom.xml`
- `build.gradle`
- `Dockerfile`
- `docker-compose.yml`
- `.github/workflows/*`

Also inspect repository docs and existing agent instruction files when present.

## Detection Output

Record:

- Languages
- Frameworks
- Package managers
- Runtime versions, if discoverable
- Test tools
- Build tools
- Lint and formatting tools
- Database or BaaS hints
- Docker or infrastructure hints
- CI workflow commands

## Command Preference

Prefer project-defined commands over invented commands.

Examples:

- Use `package.json` scripts before raw `npm` or framework commands.
- Use Makefile targets when the project documents them.
- Use CI workflow commands as evidence, but adapt them to local execution when safe.
- Avoid installing new tools unless dependency changes are authorized.

## Stack-Agnostic Behavior

The Skill supports many project types by detection and adaptation, including web apps, APIs, CLIs, mobile apps, monorepos, internal tools, SaaS products, automation scripts, and full-stack projects.

When evidence is incomplete, state uncertainty and choose the least invasive validation path.
