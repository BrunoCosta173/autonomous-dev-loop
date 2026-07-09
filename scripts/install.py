#!/usr/bin/env python3
"""Install, update, or uninstall autonomous-dev-loop Skill targets."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import shutil
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "autonomous-dev-loop"


@dataclass(frozen=True)
class Operation:
    action: str
    source: Path | None
    destination: Path
    description: str


class InstallerError(Exception):
    """Raised when installer input or state is unsafe."""


def _skill_source(target: str) -> Path:
    if target == "codex":
        return REPO_ROOT / ".agents" / "skills" / SKILL_NAME
    if target == "claude":
        return REPO_ROOT / ".claude" / "skills" / SKILL_NAME
    raise InstallerError(f"Unsupported Skill target: {target}")


def _skill_destination(target: str, scope: str, project_dir: Path) -> Path:
    if target == "codex":
        if scope == "project":
            return project_dir / ".agents" / "skills" / SKILL_NAME
        return Path.home() / ".agents" / "skills" / SKILL_NAME
    if target == "claude":
        if scope == "project":
            return project_dir / ".claude" / "skills" / SKILL_NAME
        return Path.home() / ".claude" / "skills" / SKILL_NAME
    raise InstallerError(f"Unsupported Skill target: {target}")


def _adapter_sources(include_claude: bool) -> dict[str, Path]:
    adapters = {
        "AGENTS.md": REPO_ROOT / "adapters" / "AGENTS.md",
        "GENERIC_AGENT.md": REPO_ROOT / "adapters" / "GENERIC_AGENT.md",
    }
    if include_claude:
        adapters["CLAUDE.md"] = REPO_ROOT / "adapters" / "CLAUDE.md"
    return adapters


def _targets(selected_target: str) -> list[str]:
    if selected_target == "both":
        return ["codex", "claude"]
    if selected_target in {"codex", "claude"}:
        return [selected_target]
    return []


def _validate_sources(paths: list[Path]) -> None:
    for path in paths:
        if not path.exists():
            raise InstallerError(f"Source path does not exist: {path}")


def _same_file(source: Path, destination: Path) -> bool:
    if not source.is_file() or not destination.is_file():
        return False
    return source.read_bytes() == destination.read_bytes()


def _plan_skill_copy(
    action: str,
    target: str,
    scope: str,
    project_dir: Path,
    force: bool,
    dry_run: bool,
) -> list[Operation]:
    source = _skill_source(target)
    destination = _skill_destination(target, scope, project_dir)
    _validate_sources([source, source / "SKILL.md"])

    if source.resolve() == destination.resolve():
        return [
            Operation(
                action="skip",
                source=None,
                destination=destination,
                description=f"source and destination are the same; already present: {destination}",
            )
        ]

    if action == "install" and destination.exists() and not force:
        if dry_run:
            return [
                Operation(
                    action="skip",
                    source=None,
                    destination=destination,
                    description=f"destination exists; install would require --force: {destination}",
                )
            ]
        raise InstallerError(
            f"Destination already exists. Use --force or --action update: {destination}"
        )

    return [
        Operation(
            action="copy_tree",
            source=source,
            destination=destination,
            description=f"{action} {target} Skill to {destination}",
        )
    ]


def _plan_adapter_copy(
    action: str,
    project_dir: Path,
    force: bool,
    include_claude: bool,
    dry_run: bool,
) -> list[Operation]:
    operations: list[Operation] = []

    for filename, source in _adapter_sources(include_claude).items():
        destination = project_dir / filename
        _validate_sources([source])

        if destination.exists():
            if action == "install" and not force:
                if dry_run:
                    operations.append(
                        Operation(
                            action="skip",
                            source=None,
                            destination=destination,
                            description=f"adapter exists; install would require --force: {destination}",
                        )
                    )
                    continue
                raise InstallerError(
                    f"Adapter already exists. Use --force to overwrite: {destination}"
                )
            if action == "update" and not force and not _same_file(source, destination):
                print(f"Skipping user-modified adapter during update: {destination}")
                continue

        operations.append(
            Operation(
                action="copy_file",
                source=source,
                destination=destination,
                description=f"{action} adapter {filename} to {destination}",
            )
        )

    return operations


def _plan_skill_uninstall(target: str, scope: str, project_dir: Path) -> list[Operation]:
    destination = _skill_destination(target, scope, project_dir)
    if destination.resolve() == _skill_source(target).resolve():
        return [
            Operation(
                action="skip",
                source=None,
                destination=destination,
                description=f"skip repository source Skill folder: {destination}",
            )
        ]
    return [
        Operation(
            action="remove_tree",
            source=None,
            destination=destination,
            description=f"remove {target} Skill from {destination}",
        )
    ]


def _plan_adapter_uninstall(
    project_dir: Path,
    force: bool,
    include_claude: bool,
) -> list[Operation]:
    operations: list[Operation] = []

    for filename, source in _adapter_sources(include_claude).items():
        destination = project_dir / filename
        _validate_sources([source])

        if not destination.exists():
            operations.append(
                Operation(
                    action="skip",
                    source=None,
                    destination=destination,
                    description=f"adapter is not installed: {destination}",
                )
            )
            continue

        if not force and not _same_file(source, destination):
            operations.append(
                Operation(
                    action="skip",
                    source=None,
                    destination=destination,
                    description=f"skip user-modified adapter: {destination}",
                )
            )
            continue

        operations.append(
            Operation(
                action="remove_file",
                source=None,
                destination=destination,
                description=f"remove adapter {destination}",
            )
        )

    return operations


def build_plan(args: argparse.Namespace) -> list[Operation]:
    project_dir = args.project_dir.resolve()
    if args.target == "generic" and args.scope != "project":
        raise InstallerError("Generic adapters support project scope only.")
    if args.with_adapters and args.no_adapters:
        raise InstallerError("Use either --with-adapters or --no-adapters, not both.")
    if args.target == "generic" and args.no_adapters:
        raise InstallerError("Generic target requires adapter installation.")

    operations: list[Operation] = []

    if args.action in {"install", "update"}:
        for target in _targets(args.target):
            operations.extend(
                _plan_skill_copy(
                    args.action,
                    target,
                    args.scope,
                    project_dir,
                    args.force,
                    args.dry_run,
                )
            )

        if args.target == "generic":
            operations.extend(
                _plan_adapter_copy(
                    args.action,
                    project_dir,
                    args.force,
                    include_claude=args.with_adapters,
                    dry_run=args.dry_run,
                )
            )
        elif args.with_adapters:
            operations.extend(
                _plan_adapter_copy(
                    args.action,
                    project_dir,
                    args.force,
                    include_claude=args.target in {"claude", "both"},
                    dry_run=args.dry_run,
                )
            )

    if args.action == "uninstall":
        for target in _targets(args.target):
            operations.extend(_plan_skill_uninstall(target, args.scope, project_dir))

        if args.with_adapters:
            operations.extend(
                _plan_adapter_uninstall(
                    project_dir,
                    args.force,
                    include_claude=args.target in {"claude", "both", "generic"},
                )
            )

    if not operations:
        print("No operations selected.")

    return operations


def print_plan(operations: list[Operation], dry_run: bool) -> None:
    prefix = "Planned operations"
    if dry_run:
        prefix += " (dry run)"
    print(prefix + ":")
    if not operations:
        print("- None")
        return
    for operation in operations:
        print(f"- {operation.description}")


def _confirm_if_needed(args: argparse.Namespace, operations: list[Operation]) -> None:
    if args.dry_run or args.yes or args.force:
        return
    if args.action not in {"update", "uninstall"}:
        return
    if not operations:
        return

    answer = input(f"Proceed with {args.action}? [y/N] ").strip().lower()
    if answer not in {"y", "yes"}:
        raise InstallerError("Operation cancelled.")


def _copy_tree(source: Path, destination: Path, force: bool) -> None:
    if destination.exists():
        if not force:
            shutil.rmtree(destination)
        else:
            shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    if not (destination / "SKILL.md").is_file():
        raise InstallerError(f"Copy verification failed: {destination / 'SKILL.md'}")


def _copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    if not destination.is_file():
        raise InstallerError(f"Copy verification failed: {destination}")


def apply_plan(operations: list[Operation], args: argparse.Namespace) -> None:
    if args.dry_run:
        print("Dry run complete. No files changed.")
        return

    for operation in operations:
        if operation.action == "copy_tree":
            assert operation.source is not None
            _copy_tree(operation.source, operation.destination, args.force)
            print(f"Copied: {operation.destination}")
        elif operation.action == "copy_file":
            assert operation.source is not None
            _copy_file(operation.source, operation.destination)
            print(f"Copied: {operation.destination}")
        elif operation.action == "remove_tree":
            if operation.destination.exists():
                shutil.rmtree(operation.destination)
                print(f"Removed: {operation.destination}")
            else:
                print(f"Skipped missing Skill folder: {operation.destination}")
        elif operation.action == "remove_file":
            if operation.destination.exists():
                operation.destination.unlink()
                print(f"Removed: {operation.destination}")
            else:
                print(f"Skipped missing adapter: {operation.destination}")
        elif operation.action == "skip":
            print(f"Skipped: {operation.destination}")
        else:
            raise InstallerError(f"Unknown operation: {operation.action}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install, update, or uninstall autonomous-dev-loop Skill targets."
    )
    parser.add_argument(
        "--action",
        choices=("install", "update", "uninstall"),
        default="install",
        help="Action to perform. Default: install.",
    )
    parser.add_argument(
        "--target",
        choices=("codex", "claude", "both", "generic"),
        required=True,
        help="Installation target.",
    )
    parser.add_argument(
        "--scope",
        choices=("project", "user"),
        default="project",
        help="Install scope for Skill targets. Default: project.",
    )
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=Path.cwd(),
        help="Target project directory. Default: current working directory.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite or remove safely known destinations.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned operations without changing files.")
    parser.add_argument("--with-adapters", action="store_true", help="Also install, update, or uninstall adapter files.")
    parser.add_argument("--no-adapters", action="store_true", help="Do not install adapters.")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation for update or uninstall actions.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        operations = build_plan(args)
        print_plan(operations, args.dry_run)
        _confirm_if_needed(args, operations)
        apply_plan(operations, args)
    except InstallerError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
