# Validation Strategy

This document describes the lightweight validation strategy for `autonomous-dev-loop`.

## Goals

Validation should keep the repository release-ready without adding external dependencies or heavy automation.

The main risk is drift between the two Skill targets:

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/`
- Claude Code: `.claude/skills/autonomous-dev-loop/`

## Local Commands

Run all repository checks:

```bash
python scripts/validate_repository.py
```

Run the Skill target equivalence check:

```bash
python scripts/check_skill_equivalence.py
```

Run the private content scan:

```bash
python scripts/check_private_content.py
```

Run installer tests:

```bash
python scripts/test_installer.py
```

Run package tests:

```bash
python scripts/test_packaging.py
```

If a local environment does not provide `python`, use the available Python command for that system, such as `python3`.

## What Is Validated

`scripts/validate_repository.py` checks:

- Both Skill target directories exist.
- Both Skill target directories contain `SKILL.md`.
- Both Skill entrypoints have valid frontmatter shape.
- Both Skill targets contain matching `references/` filenames.
- Both Skill targets contain matching `assets/` filenames.
- Matching reference files are equivalent.
- Matching asset templates are equivalent.
- No obvious private, company-specific, environment-specific, or secret-like content appears in repository text files.
- Required repository docs exist.
- Required installation docs exist.
- Required issue templates exist.
- Required planning docs exist.
- Required example README files exist.
- Release candidate checklist, draft release notes, and PR description draft exist.
- README includes quick install, agent-assisted installation, and release readiness links.
- `CHANGELOG.md` includes the current version.
- Basic text hygiene passes for repository text files.
- Installer scripts, wrappers, tests, and workflows exist.
- Installer help and dry-runs work.
- Installer tests pass.
- Packaging dry-run works.
- Packaging tests pass.
- Release packages include SHA256 checksum files.

`scripts/check_skill_equivalence.py` focuses on Skill target equivalence.

`scripts/check_private_content.py` focuses on conservative private-content scanning.

## Why Equivalence Matters

The Codex/OpenAI and Claude Code Skill targets should remain behaviorally equivalent.

Behavioral equivalence means:

- They describe the same autonomous loop.
- They use equivalent references and assets.
- They preserve the same safety gates.
- They preserve the same review, validation, documentation, and handoff behavior.
- They differ only where the target platform requires different wording or metadata.

For now:

- `references/` should match exactly.
- `assets/` should match exactly.
- `SKILL.md` may contain platform-specific wording.
- `agents/openai.yaml` exists only in the Codex/OpenAI target.

## What Failures Mean

Validation failures should be treated as release blockers until reviewed.

Common failure types:

- Missing required docs usually means the repository structure is incomplete.
- Reference or asset differences may indicate Skill drift.
- Frontmatter failures may prevent Skill discovery.
- Private-content findings may indicate sensitive data or local machine details were accidentally committed.
- Text hygiene failures may indicate merge conflicts or formatting issues.

## Handling Intentional Differences

Intentional platform-specific differences should be narrow and documented.

Allowed differences:

- `SKILL.md` wording that names Codex/OpenAI or Claude Code.
- `agents/openai.yaml` existing only in the Codex/OpenAI target.

If future versions need additional differences, update:

- `scripts/check_skill_equivalence.py`
- This validation strategy document
- The release-readiness checklist

## What Is Not Validated Yet

Current validation does not:

- Execute example project smoke tests.
- Publish packages.
- Validate every possible agent platform.
- Prove that real review subagents are available.
- Prove that native goal modes are available.
- Validate third-party marketplace or plugin packaging.
- Publish GitHub releases.
- Prove that the `main` branch remote install command is appropriate for every user's security posture.

Future versions may add deeper validation when those workflows exist.
