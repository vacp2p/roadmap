#!/usr/bin/env python3
"""CLI entry point for roadmap validator."""

import argparse
import os
import shlex
import sys
from typing import Iterable, List, Optional
from paths import resolve_targets
from validator import validate_file

DEFAULT_TARGETS = "acz dst qa nes nim p2p rfc sc sec tke web"


def run_validator(targets: Iterable[str]) -> int:
    files = resolve_targets(targets)
    if not files:
        sys.stderr.write("No markdown files found for validation.\n")
        return 0

    all_issues: List[str] = []
    for file_path in files:
        all_issues.extend(validate_file(file_path))

    if all_issues:
        sys.stderr.write("\n".join(all_issues) + "\n")
        sys.stderr.write(f"\nValidation failed for {len(files)} file(s).\n")
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
        help="Files or directories to validate. Defaults to ROADMAP_VALIDATION_PATHS or 'qa'.",
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
