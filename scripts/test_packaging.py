#!/usr/bin/env python3
"""Standard-library tests for scripts/package_release.py."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PACKAGER = ROOT / "scripts" / "package_release.py"
DIST = ROOT / "dist"
VERSION = "0.0.10"


def run_packager(*args: str) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(PACKAGER), *args]
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise AssertionError(
            f"Packaging command failed: {' '.join(command)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result


def _expected_packages() -> list[Path]:
    return [
        DIST / f"autonomous-dev-loop-{VERSION}.zip",
        DIST / f"autonomous-dev-loop-codex-{VERSION}.zip",
        DIST / f"autonomous-dev-loop-claude-{VERSION}.zip",
        DIST / f"autonomous-dev-loop-adapters-{VERSION}.zip",
    ]


def test_dry_run_does_not_create_dist() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    run_packager("--version", VERSION, "--dry-run")
    if DIST.exists():
        raise AssertionError("Dry run should not create dist/")


def test_expected_zip_files_created() -> None:
    run_packager("--version", VERSION, "--clean")
    for package in _expected_packages():
        if not package.is_file():
            raise AssertionError(f"Expected package was not created: {package}")


def test_full_package_exclusions() -> None:
    package = DIST / f"autonomous-dev-loop-{VERSION}.zip"
    with zipfile.ZipFile(package) as archive:
        names = archive.namelist()

    disallowed_fragments = ("/.git/", "/dist/", "__pycache__/", "/.env")
    for name in names:
        if any(fragment in name for fragment in disallowed_fragments):
            raise AssertionError(f"Disallowed path included in package: {name}")


def main() -> int:
    tests = [
        test_dry_run_does_not_create_dist,
        test_expected_zip_files_created,
        test_full_package_exclusions,
    ]

    for test in tests:
        test()
        print(f"[ok] {test.__name__}")

    print("Packaging tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
