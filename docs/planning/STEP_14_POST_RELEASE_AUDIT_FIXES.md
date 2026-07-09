# Step 14 Post-Release Audit Fixes

Status: **In progress for 0.1.1 patch candidate**

## Audit Source

An external audit was performed with OpenCode + DeepSeek V4 Pro after the public `v0.1.0` release.

The audit found no confirmed critical release blockers, but recommended focused post-release fixes.

## Main Findings

- Some root documentation still reflected the early planning-only phase.
- The README could be more inviting and scannable for GitHub visitors.
- Loop step counts differed between public overview and detailed Skill protocol.
- The default maximum autonomous cycle count was not explicit.
- Windows/PowerShell one-command installation limitations needed clearer wording.
- Data exfiltration and external transmission should be explicit safety gates.
- No-validation-command cases needed clearer agent guidance.
- GitHub issue templates and a code of conduct were missing.
- Release package checksums were not generated.
- `dist/` tracking needed confirmation.

## Fixes Applied

- Refreshed `CONTRIBUTING.md` and `PROJECT_BRIEF.md`.
- Polished README structure with badges, quick links, tables, install sections, safety model, examples, and documentation index.
- Added `Kickoff` to the detailed loop protocol.
- Defined `Default maximum autonomous cycles: 10`.
- Clarified Linux/macOS one-command install and Windows local PowerShell/Python paths.
- Added data exfiltration and external transmission safety gates.
- Added no-validation-commands guidance.
- Added GitHub issue templates.
- Added `CODE_OF_CONDUCT.md`.
- Added SHA256 checksum generation and packaging tests.
- Added adapter fallback notes.
- Added a control-file clutter limit.

## Fixes Deferred

- Windows PowerShell one-command remote install remains deferred.
- Complete example applications remain deferred.
- Marketplace or plugin packaging remains deferred until relevant ecosystems support it.

## Why 0.1.1

These are focused post-release fixes after `0.1.0`.

They improve documentation, safety clarity, packaging verification, and contribution workflows without redesigning the Skill or changing the release model. A patch version is appropriate.

## Why v0.1.0 Was Not Rewritten

`v0.1.0` is already public. Published releases and tags must remain stable.

This step does not modify, replace, delete, unpublish, force-push, or rewrite `v0.1.0`.

## Validation Performed

Expected validation for the patch branch:

```bash
python3 scripts/install.py --help
python3 scripts/test_installer.py
python3 scripts/package_release.py --version 0.1.1 --clean
python3 scripts/test_packaging.py
python3 scripts/validate_repository.py
python3 scripts/check_skill_equivalence.py
python3 scripts/check_private_content.py
git diff --check
git ls-files dist
```

Both Skill targets should also pass the local Skill validator when available.

## Release Recommendation

After the patch PR passes CI:

1. Merge to `main`.
2. Validate `main`.
3. Create annotated tag `v0.1.1`.
4. Generate release packages and SHA256 checksums.
5. Create a GitHub release or draft release for `v0.1.1`.
6. Leave `v0.1.0` untouched.
