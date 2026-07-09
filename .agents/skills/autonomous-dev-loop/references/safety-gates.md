# Safety Gates

Safety gates are mandatory stops before high-risk action.

## Stop For Confirmation

Stop and request human confirmation before:

- Destructive commands
- Mass deletion
- Database migrations with data-loss risk
- Authentication changes
- Authorization or permission changes
- Secret or environment variable handling
- Deployment
- Major architecture rewrites
- Framework replacement
- Business-critical rule changes
- Irreversible operations
- Ambiguous product decisions that materially affect behavior
- Installing or upgrading critical dependencies
- Changing licensing terms
- Removing tests to make validation pass
- Disabling validation tools or CI checks

## Confirmation Request Format

When a safety gate is reached, report:

```text
Safety gate:
Reason:
Proposed action:
Files or systems affected:
Potential risk:
Safer alternative:
Exact command, if applicable:
Decision needed:
```

Do not proceed until the user confirms.

## Approval Policy

Approval is required before:

- Commands that can delete, overwrite, reset, publish, deploy, or irreversibly change state.
- Database migrations, resets, seed operations, or schema changes with data-loss risk.
- Authentication, authorization, role, policy, session, token, or permission changes.
- Reading, printing, creating, rotating, uploading, or modifying secrets or environment variables.
- Major architecture rewrites or framework replacement.
- Business-critical rule changes.
- Installing, replacing, or upgrading critical dependencies.
- Changing licensing terms.
- Removing tests to make validation pass.
- Disabling validation tools, CI checks, security checks, or quality gates.
- Actions flagged by review subagents as safety-gated.

## Destructive Commands

Treat commands as destructive when they can delete data, remove files in bulk, rewrite history, drop databases, reset state, overwrite user work, or irreversibly change external systems.

Examples requiring confirmation include:

- `rm -rf`
- `git reset --hard`
- `git clean -fd`
- Force pushes
- Database drop/reset commands
- Production deployment commands

## Secret And Environment Handling

Do not read, print, create, rotate, upload, or modify secrets or environment variables unless the user explicitly authorizes that work.

If secret-like values appear in files or logs, avoid repeating them in output.

## Ambiguous Product Decisions

Ask before deciding behavior that materially changes how users, money, permissions, data retention, legal obligations, or business-critical workflows operate.

## Proceeding After Confirmation

After confirmation:

- Restate the approved action briefly.
- Keep the action limited to what was approved.
- Record the safety gate in the final report.

## Review Interaction

If a reviewer flags a safety gate:

- Stop the Review Subagent Loop.
- Do not apply the related fix automatically.
- Ask for human approval using the confirmation format.
- Resume only inside the approved scope.
