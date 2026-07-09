# Pull Request Description Draft

## Summary

Post-release audit fixes after `0.1.0`.

This PR prepares the `0.1.1` patch release candidate without modifying the published `v0.1.0` release or moving its tag.

## What Changed

- Documentation refresh
- README visual and structural polish
- Loop protocol consistency
- Max autonomous cycles default
- Windows/PowerShell install clarification
- Data exfiltration safety gate
- No-validation-commands guidance
- Issue templates
- Code of conduct
- SHA256 checksums for generated release packages
- Adapter fallback notes

## Validation

Run locally:

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

## Release Notes

See `docs/release/RELEASE_NOTES_0.1.1.md`.

## Post-Merge Tasks

- Verify GitHub Actions pass on PR.
- Merge to `main`.
- Validate `main`.
- Create annotated tag `v0.1.1`.
- Generate packages and SHA256 checksums.
- Create a GitHub release or draft release for `v0.1.1`.
- Leave `v0.1.0` untouched.
