# Release Candidate Checklist

Use this checklist before merging the release branch to `main` or publishing a tagged release.

## Required Checks

- [x] README reviewed locally
- [x] CHANGELOG reviewed locally
- [x] LICENSE exists
- [x] Installation docs reviewed locally
- [x] Compatibility matrix reviewed locally
- [x] Validation scripts pass locally
- [x] Installer tests pass locally
- [x] Packaging tests pass locally
- [x] Skill validation passes locally for both targets
- [x] Codex/OpenAI and Claude targets remain equivalent locally
- [x] No private content found locally
- [x] No external dependencies added accidentally
- [ ] GitHub Actions passing, pending PR confirmation
- [x] Generated release packages verified locally
- [x] Branch ready for PR after the `0.0.12` commit is pushed
- [ ] Main branch should remain release-ready after merge

## Manual Smoke Tests

Run or review these before release:

- [ ] Codex project install
- [ ] Claude project install
- [ ] Both project install
- [ ] Generic adapter install
- [ ] Update dry-run
- [ ] Uninstall dry-run
- [ ] Package generation
- [ ] README command review

Suggested local commands:

```bash
python3 scripts/install.py --target codex --scope project --dry-run
python3 scripts/install.py --target claude --scope project --dry-run
python3 scripts/install.py --target both --scope project --dry-run
python3 scripts/install.py --target generic --scope project --dry-run
python3 scripts/install.py --action update --target codex --scope project --dry-run
python3 scripts/install.py --action uninstall --target codex --scope project --dry-run
python3 scripts/package_release.py --version 0.0.12 --clean
```

## Release Blockers

Do not release if any of these are true:

- [ ] Validation is failing
- [ ] Installer is broken
- [ ] Skill targets diverged unexpectedly
- [ ] Private content was found
- [ ] README install instructions are unclear
- [ ] Changelog entry is missing
- [ ] Uncommitted changes remain
- [ ] CI is failing
- [ ] Generated packages are missing or incorrect
- [ ] Release notes are inaccurate

## Final Review Notes

- One-command install should be convenient, not described as safer than local/manual install.
- When piped from GitHub raw content, `install.sh` should download the `main` branch archive and run the Python installer from the temporary copy.
- Agent-assisted installation should prefer local installer or manual copy.
- `main` should be treated as the latest channel.
- Tagged releases should be used for reproducible installs when available.
- Real subagents and native goal modes must remain documented as environment-dependent.
