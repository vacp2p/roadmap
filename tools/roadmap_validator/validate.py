#!/usr/bin/env python3
"""CLI entry point for roadmap validator."""

import argparse
import os
import shlex
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Optional
from paths import REPO_ROOT, resolve_targets
from validator import validate_file
from issues import ValidationIssue

DEFAULT_TARGETS = "content"


def _relpath(path: Path) -> Path:
    if path.is_absolute():
        try:
            return path.relative_to(REPO_ROOT)
        except ValueError:
            return path
    return path


def format_issue(issue: ValidationIssue) -> str:
    location = _relpath(issue.path)
    prefix = f"{location}"
    if issue.line:
        prefix += f":{issue.line}"
    return f"{prefix}: {issue.message}"


def emit_github_annotations(issues: List[ValidationIssue]) -> None:
    if os.getenv("GITHUB_ACTIONS") != "true":
        return
    for issue in issues:
        location = _relpath(issue.path)
        file_str = str(location)
        if issue.line:
            print(f"::error file={file_str},line={issue.line}::{issue.message}")
        else:
            print(f"::error file={file_str}::{issue.message}")

    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    issues_by_file = defaultdict(list)
    for issue in issues:
        issues_by_file[str(_relpath(issue.path))].append(issue)

    unique_files = {str(_relpath(issue.path)) for issue in issues}

    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write("## Roadmap Validator Report\n\n")
        summary.write(f"Found {len(issues)} issues across {len(unique_files)} file(s).\n\n")
        for file_path, file_issues in sorted(issues_by_file.items()):
            summary.write(f"- `{file_path}`\n")
            for issue in file_issues:
                line_info = f" (line {issue.line})" if issue.line else ""
                summary.write(f"  - {issue.message}{line_info}\n")
        summary.write("\n")


def run_validator(targets: Iterable[str]) -> int:
    files = resolve_targets(targets)
    if not files:
        sys.stderr.write("No markdown files found for validation.\n")
        return 0

    all_issues: List[ValidationIssue] = []
    for file_path in files:
        all_issues.extend(validate_file(file_path))

    if all_issues:
        emit_github_annotations(all_issues)
        for issue in sorted(all_issues, key=lambda i: (str(_relpath(i.path)), i.line or 0, i.message)):
            print(format_issue(issue))
        unique_files = { _relpath(i.path) for i in all_issues }
        print(f"\nValidation failed for {len(unique_files)} file(s).")
        return 1

    print(f"All checks passed for {len(files)} file(s).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate roadmap Markdown files for actionability standards.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or directories to validate. Defaults to ROADMAP_VALIDATION_PATHS or 'content'.",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    env_paths = shlex.split(os.environ.get("ROADMAP_VALIDATION_PATHS", DEFAULT_TARGETS))
    targets = args.paths or env_paths
    return run_validator(targets)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
