# Infra Playbooks

Use this reference for Docker, CI, deployment config, and infrastructure objectives after reading `stack-detection.md` and `command-discovery.md`.

## General Infra Flow

1. Inspect config files and CI workflows.
2. Identify whether commands are local validation, build-only, or deployment.
3. Prefer read-only checks and local build validation.
4. Stop before deployment, destructive changes, secret handling, or external system mutation.

## Docker

Signals:

- `Dockerfile`
- `.dockerignore`

Potential validation:

- Dockerfile lint if configured
- image build when relevant and not too heavy
- app-level tests outside Docker when faster and sufficient

Avoid pruning, removing volumes, or deleting images without confirmation.

## Docker Compose

Signals:

- `docker-compose.yml`
- `compose.yml`

Potential validation:

- Compose config validation when available
- Service build checks when relevant

Avoid commands that remove volumes, reset databases, or start long-running services unless needed and safe.

## GitHub Actions

Signals:

- `.github/workflows/*`

Use workflows as evidence for project-defined validation commands.

Do not assume CI-only secrets or services exist locally.

## Vercel / Netlify

Signals:

- `vercel.json`
- `netlify.toml`

Validate config or builds locally when possible.

Do not deploy, link projects, or modify remote settings without explicit authorization.

## Terraform

Signals:

- `terraform/`
- `*.tf`

Potential validation:

- formatting checks
- validation commands when initialized and safe

Stop before `apply`, `destroy`, state changes, credential handling, backend changes, or anything that mutates infrastructure.

## Safety Rules

Always ask before:

- Deployment
- Secret or environment variable handling
- State mutation
- Resource creation or deletion
- Database reset or migration with data-loss risk
- Permission or authentication changes

If a command might affect external systems, treat it as safety-gated.
