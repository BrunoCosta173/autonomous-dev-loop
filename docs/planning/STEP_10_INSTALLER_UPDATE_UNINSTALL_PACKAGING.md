# Step 10 Installer Update Uninstall Packaging

Status: **Completed**

## Step Goal

Add a practical installation system for `autonomous-dev-loop`, including install, update, uninstall, wrapper scripts, release packaging, tests, and packaging validation.

This work was added before the first release candidate so users can try the Skill in real projects without manually copying every folder.

## Installer Goals

The installer should be:

- Dependency-free.
- Readable.
- Conservative.
- Safe by default.
- Explicit about planned operations.
- Useful for project-level and user-level Skill installation.

## Installer Script

Main installer:

```text
scripts/install.py
```

It uses only the Python standard library.

## Supported Actions

```text
install
update
uninstall
```

Default action:

```text
install
```

## Supported Targets

```text
codex
claude
both
generic
```

## Supported Scopes

```text
project
user
```

Rules:

- `codex` supports project and user scope.
- `claude` supports project and user scope.
- `both` supports project and user scope.
- `generic` supports project scope only.

## Safety Policy

The installer:

- Never deletes unrelated files.
- Never overwrites existing Skill folders on install unless `--force` is used.
- Never overwrites existing root adapter files unless `--force` or safe update behavior allows it.
- Creates parent directories as needed.
- Prints every planned operation.
- Supports `--dry-run`.
- Exits non-zero on errors.
- Verifies source folders before copying.
- Verifies destination folders after copying.
- Avoids modifying application source code.
- Removes only known installed Skill folders during uninstall.
- Removes adapters only when they match the repository template unless `--force` is used.
- Asks for confirmation for update or uninstall unless `--yes`, `--force`, or `--dry-run` is provided.

## Wrapper Scripts

Wrappers:

```text
install.sh
install.ps1
```

They resolve the repository root relative to the wrapper location and call the Python installer.

They do not duplicate installer logic.

## Release Packaging

Release packaging script:

```text
scripts/package_release.py
```

It creates:

```text
dist/autonomous-dev-loop-<version>.zip
dist/autonomous-dev-loop-codex-<version>.zip
dist/autonomous-dev-loop-claude-<version>.zip
dist/autonomous-dev-loop-adapters-<version>.zip
```

It excludes:

- `.git/`
- `dist/`
- `__pycache__/`
- Local `.env` files
- Common local cache directories

Generated `dist/` files are local artifacts and are ignored by Git.

## Tests

Installer tests:

```text
scripts/test_installer.py
```

Packaging tests:

```text
scripts/test_packaging.py
```

Both use only the Python standard library.

## One-Line Install Policy

One-line install examples are documented as optional advanced usage only.

Users should inspect remote scripts before executing them.

One-line install is not the default recommended path.

## Marketplace And Plugin Packaging

No marketplace or plugin publishing is implemented in Step 10.

Marketplace or plugin packaging may be added if supported by the relevant agent ecosystem.

## Validation Strategy

Step 10 updates validation so `scripts/validate_repository.py` checks:

- Installer files exist.
- Wrapper files exist.
- Packaging script exists.
- Installer help works.
- Installer dry-runs work.
- Installer tests pass.
- Packaging dry-run works.
- Packaging tests pass.
- Required workflows exist.

## GitHub Actions

Step 10 updates:

```text
.github/workflows/validate.yml
```

Step 10 adds:

```text
.github/workflows/package.yml
```

The packaging workflow validates the repository, generates local zip packages, and verifies expected zip files exist.

It does not publish artifacts or create releases.

## Future Improvements

Future versions may add:

- Release candidate checklist.
- Installer checksum reporting.
- More install targets if agent ecosystems define them.
- Marketplace or plugin packaging if supported.
- Release publishing workflow after explicit approval.
- Example project smoke tests.

## Completion Criteria

Step 10 is complete because the repository now includes a safe Python installer, shell wrappers, update and uninstall behavior, local release package generation, installer and packaging tests, CI workflow updates, documentation, and validation integration.
