# Persistent Project Memory

Use project control files as persistent memory when they improve continuity, traceability, or safe continuation across autonomous development runs.

Do not force every control file into every project.

## Memory Policy

Create, update, or suggest only files that are useful for the current objective and likely future work.

Prefer existing equivalent files over creating duplicates.

Do not store secrets, private environment details, credentials, tokens, or machine-specific paths in project memory.

## Memory File Roles

- `AGENTS.md`: persistent instructions for generic AI coding agents in the project.
- `CLAUDE.md`: persistent instructions for Claude Code in the project.
- `BACKLOG.md`: longer-term prioritized project work and out-of-scope findings.
- `ROADMAP.md`: high-level product or project direction.
- `TODO.md`: active ToDo list for the current autonomous run.
- `DEVELOPMENT_LOG.md`: cycle-by-cycle history of what was done.
- `TEST_PLAN.md`: validation strategy, known commands, and test gaps.
- `DECISIONS.md`: architecture and product decision log.
- `KNOWN_ISSUES.md`: bugs, blockers, risks, and unresolved issues.
- `FINAL_REPORT.md`: persistent report for a completed or partially completed autonomous run.

## When To Persist

Persist memory when:

- The run has multiple steps or may continue later.
- Work is partially complete.
- A safety gate, blocker, or unresolved validation failure stops progress.
- The agent discovers unrelated issues that should not be fixed in the current scope.
- Testing strategy, commands, or project conventions need durable documentation.
- Architectural or product decisions are made.
- The user asks for a saved report or durable handoff.

## When Not To Persist

Avoid creating control files when:

- The task is small and the final response is enough.
- The project already has equivalent docs that should be updated instead.
- The file would contain speculative, low-value, or stale information.
- The information is private, secret, environment-specific, or unsafe to store.

## Latest Reliable State

When updating memory, identify the latest reliable state:

- Current objective
- Current git status or changed files
- Completed ToDos
- Pending or blocked ToDos
- Validation status
- Review status
- Safety gates
- Known blockers
- Next concrete action

The actual project state and current user instruction override stale memory files.

## Template Usage

Use templates from `assets/` as starting points:

- `assets/AGENTS.template.md`
- `assets/CLAUDE.template.md`
- `assets/BACKLOG.template.md`
- `assets/ROADMAP.template.md`
- `assets/DEVELOPMENT_LOG.template.md`
- `assets/TEST_PLAN.template.md`
- `assets/DECISIONS.template.md`
- `assets/KNOWN_ISSUES.template.md`
- `assets/TODO.template.md`
- `assets/FINAL_REPORT.template.md`

Adapt placeholders to the target project before treating a copied template as authoritative.

## Memory Quality Rules

- Keep entries factual and concise.
- Separate assumptions from verified facts.
- Include validation results only when commands actually ran or were explicitly unavailable.
- Record safety gates and approval decisions.
- Keep unresolved items actionable.
- Include resume instructions when work may continue.
