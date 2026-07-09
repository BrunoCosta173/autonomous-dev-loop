# Step 4 Stack Detection And Command Discovery

Status: **Completed**

## Step Goal

Teach the Skill how to detect software stacks, discover available commands, choose safe commands, and adapt validation workflows across common project types.

This step keeps the Skill stack-agnostic. It does not make one framework the default, and it does not claim guaranteed compatibility with every stack.

## Why Stack Detection Matters

Autonomous development work is safer and more useful when the agent understands the project before choosing commands.

Stack detection helps the agent:

- Avoid invented commands.
- Prefer project-defined scripts and documented workflows.
- Select the smallest relevant validation command.
- Avoid destructive or deployment commands.
- Explain when commands are unavailable or not run.
- Produce accurate final reports.

## Detection Files

The Skill now documents stack signals for these families.

### JavaScript / TypeScript

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

### Python

- `pyproject.toml`
- `requirements.txt`
- `poetry.lock`
- `uv.lock`
- `Pipfile`
- `setup.py`
- `manage.py`

### PHP

- `composer.json`
- `composer.lock`
- `artisan`

### Ruby

- `Gemfile`
- `Gemfile.lock`
- `config/routes.rb`

### Java / JVM

- `pom.xml`
- `build.gradle`
- `settings.gradle`
- `gradlew`

### .NET

- `*.sln`
- `*.csproj`
- `global.json`

### Go

- `go.mod`
- `go.sum`

### Rust

- `Cargo.toml`
- `Cargo.lock`

### Mobile

- `pubspec.yaml`
- `android/`
- `ios/`
- `react-native.config.js`
- `expo.*`
- `app.json`

### Infra / DevOps

- `Dockerfile`
- `docker-compose.yml`
- `compose.yml`
- `.github/workflows/*`
- `vercel.json`
- `netlify.toml`
- `terraform/`
- `*.tf`

## Package Manager Detection Strategy

For JavaScript and TypeScript projects:

- `pnpm-lock.yaml` means prefer `pnpm`.
- `yarn.lock` means prefer `yarn`.
- `package-lock.json` means prefer `npm`.
- `bun.lockb` means prefer `bun`.

The agent should still read `package.json` scripts before running commands.

## Command Discovery Policy

The Skill now instructs agents to:

1. Read project instructions and docs.
2. Inspect manifests, lockfiles, framework config, task runner files, and CI workflows.
3. Identify package manager and workspace boundaries.
4. Identify available command categories.
5. Choose the smallest relevant safe command.
6. Run broader validation only when the objective risk justifies it.

Command categories include:

- install
- dev
- build
- lint
- format
- typecheck
- test
- unit test
- integration test
- e2e test
- migration check
- static analysis

## Safety Rules For Commands

The agent must stop for confirmation before commands that:

- Delete files or data in bulk
- Reset databases
- Rewrite Git history
- Force push
- Deploy, publish, or release
- Modify secrets or environment variables
- Change authentication, permissions, or authorization state
- Affect external systems

If command safety is unclear, the agent should ask before running it.

## Supported Stack Families

The Skill now includes playbooks for:

- Frontend frameworks
- Backend/API/server frameworks
- Mobile projects
- Infrastructure and DevOps files

These playbooks are practical heuristics. They do not replace project-defined commands.

## Validation Expectations

The agent should:

- Run the smallest relevant validation command first.
- Prefer targeted validation for narrow changes.
- Run broader validation when shared behavior, public APIs, build configuration, or core flows are affected.
- Document all commands run and their results.
- Clearly report when commands are unavailable, unsafe, unauthorized, skipped, or not run.
- Never claim tests passed unless they actually ran and passed.

## Skill Files Updated

Updated references:

- `stack-detection.md`
- `testing-strategy.md`
- `loop-protocol.md`
- `final-report.md`

New references:

- `command-discovery.md`
- `frontend-playbooks.md`
- `backend-playbooks.md`
- `mobile-playbooks.md`
- `infra-playbooks.md`

Both Codex/OpenAI and Claude Code Skill targets were updated.

## Explicit Non-Goals For Step 4

Step 4 does not:

- Create installer scripts.
- Create complete example projects.
- Polish the final marketing README.
- Add dependencies.
- Claim guaranteed compatibility with every stack.

## Future Improvements

Future steps may add:

- More detailed stack-specific recipes.
- Monorepo-focused command discovery.
- CI workflow interpretation examples.
- Validation matrix examples.
- Tooling to check behavior equivalence between Skill targets.

## Completion Criteria

Step 4 is complete because the Skill now has stack detection, command discovery, safe command selection, and stack-family playbook guidance in both Skill targets.
