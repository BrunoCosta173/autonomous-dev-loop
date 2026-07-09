# Step 9 Validation Release Readiness

Status: **Completed**

## Step Goal

Add lightweight repository validation, equivalence checks, and release-readiness planning for `autonomous-dev-loop`.

The main risk is drift between the two Skill targets:

- Codex/OpenAI: `.agents/skills/autonomous-dev-loop/`
- Claude Code: `.claude/skills/autonomous-dev-loop/`

## Core Decisions

Step 9 uses Python scripts with only standard library dependencies.

The validation approach is intentionally lightweight:

- No installer scripts.
- No release automation.
- No external dependencies.
- No complete example applications.
- No package publishing.

## Scripts Created

### `scripts/validate_repository.py`

Main validation script.

It checks:

- Both Skill target directories exist.
- Both Skill targets contain `SKILL.md`.
- Both Skill entrypoints have valid frontmatter shape.
- Skill references and assets match across targets.
- Private-content scanning passes.
- Required repository docs exist.
- Required installation docs exist.
- Required planning docs exist.
- Required example README files exist.
- `CHANGELOG.md` includes the current version.
- Text hygiene passes.

### `scripts/check_skill_equivalence.py`

Dedicated Skill target equivalence script.

It checks:

- Matching `references/` filenames.
- Matching `assets/` filenames.
- Matching reference file contents.
- Matching asset file contents.

Allowed differences:

- `SKILL.md` may contain platform-specific wording.
- `agents/openai.yaml` exists only in the Codex/OpenAI target.

### `scripts/check_private_content.py`

Conservative private-content scan.

It checks for:

- Obvious secret-like filenames.
- Common token and key formats.
- Absolute local paths.
- Private key blocks.
- Suspicious secret assignments.
- Private company placeholder markers.

The scan is intentionally not aggressive enough to block normal policy documentation that uses words like "secret" or "private".

## Workflow Created

Step 9 adds:

```text
.github/workflows/validate.yml
```

The workflow runs on pushes and pull requests.

It uses Python and runs:

```bash
python scripts/validate_repository.py
python scripts/check_skill_equivalence.py
python scripts/check_private_content.py
```

The workflow does not publish packages, create artifacts, or run release automation.

## Documentation Created

Step 9 adds:

- `docs/design/validation-strategy.md`
- `docs/design/release-readiness.md`
- `docs/planning/STEP_9_VALIDATION_RELEASE_READINESS.md`

## Known Limitations

Current validation does not:

- Execute example project smoke tests.
- Validate installer scripts.
- Publish release artifacts.
- Prove compatibility with every agent platform.
- Prove real subagent support exists.
- Prove native goal mode support exists.

## Future Improvements

Future versions may add:

- Release candidate checklist.
- Example project smoke tests.
- Sync script for Skill targets.
- More detailed frontmatter validation.
- Generated equivalence reports.
- Release packaging workflow.
- Installer validation when installers exist.

## Completion Criteria

Step 9 is complete because the repository now has lightweight local validation scripts, a GitHub Actions validation workflow, equivalence checks, private-content scanning, validation strategy documentation, and release-readiness criteria.
