#!/usr/bin/env python3
"""Create release zip packages for autonomous-dev-loop."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = ROOT / "dist"
PROJECT_NAME = "autonomous-dev-loop"

SKIP_DIR_NAMES = {
    ".git",
    "dist",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

SKIP_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.development",
    ".env.production",
    ".env.test",
}


class PackagingError(Exception):
    """Raised when release packaging cannot continue."""


def latest_changelog_version() -> str:
    changelog = ROOT / "CHANGELOG.md"
    text = changelog.read_text(encoding="utf-8")
    match = re.search(r"^##\s+(\d+\.\d+\.\d+)\s*$", text, flags=re.MULTILINE)
    if not match:
        raise PackagingError("Could not determine latest version from CHANGELOG.md")
    return match.group(1)


def _should_skip(path: Path) -> bool:
    rel_parts = path.relative_to(ROOT).parts
    if any(part in SKIP_DIR_NAMES for part in rel_parts):
        return True
    if path.name in SKIP_FILE_NAMES:
        return True
    return False


def _iter_files(source: Path):
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        if _should_skip(path):
            continue
        yield path


def _write_zip(zip_path: Path, source: Path, archive_root: str) -> int:
    count = 0
    with zipfile.ZipFile(zip_path, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in _iter_files(source):
            relative = path.relative_to(source)
            archive.write(path, Path(archive_root, relative).as_posix())
            count += 1
    return count


def _package_specs(version: str) -> list[tuple[str, Path, str]]:
    return [
        (
            f"{PROJECT_NAME}-{version}.zip",
            ROOT,
            f"{PROJECT_NAME}-{version}",
        ),
        (
            f"{PROJECT_NAME}-codex-{version}.zip",
            ROOT / ".agents" / "skills" / PROJECT_NAME,
            PROJECT_NAME,
        ),
        (
            f"{PROJECT_NAME}-claude-{version}.zip",
            ROOT / ".claude" / "skills" / PROJECT_NAME,
            PROJECT_NAME,
        ),
        (
            f"{PROJECT_NAME}-adapters-{version}.zip",
            ROOT / "adapters",
            "adapters",
        ),
    ]


def create_packages(version: str, clean: bool, dry_run: bool) -> list[Path]:
    if clean and DIST_DIR.exists() and not dry_run:
        shutil.rmtree(DIST_DIR)

    specs = _package_specs(version)
    expected_paths = [DIST_DIR / filename for filename, _, _ in specs]

    print("Release packaging")
    print("=================")
    print(f"Version: {version}")
    if dry_run:
        print("Dry run: no packages will be written.")

    for filename, source, archive_root in specs:
        if not source.exists():
            raise PackagingError(f"Source path does not exist: {source}")

        file_count = sum(1 for _ in _iter_files(source))
        print(f"- {filename}: {file_count} file(s) from {source.relative_to(ROOT)}")

        if not dry_run:
            DIST_DIR.mkdir(parents=True, exist_ok=True)
            zip_path = DIST_DIR / filename
            written_count = _write_zip(zip_path, source, archive_root)
            if not zip_path.is_file():
                raise PackagingError(f"Package was not created: {zip_path}")
            if written_count != file_count:
                raise PackagingError(f"Package file count mismatch: {zip_path}")

    return expected_paths


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create autonomous-dev-loop release zip packages.")
    parser.add_argument("--version", help="Version to package. Defaults to latest CHANGELOG version.")
    parser.add_argument("--clean", action="store_true", help="Remove dist/ before packaging.")
    parser.add_argument("--dry-run", action="store_true", help="Print package plan without writing zip files.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        version = args.version or latest_changelog_version()
        create_packages(version, clean=args.clean, dry_run=args.dry_run)
    except PackagingError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
