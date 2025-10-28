"""Filesystem helpers for roadmap validation."""

import os
import sys
from pathlib import Path
from typing import Iterable, List, Optional

from constants import SKIP_FILENAMES

ALLOWED_CONTENT_SUBDIRS = {
    "dst",
    "qa",
    "nim",
    "p2p",
    "rfc",
    "sc",
    "sec",
    "web",
}

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_ROOT = REPO_ROOT / "content"


def _is_allowed_content_path(path: Path) -> bool:
    """Return True when the path resides in an allowed content subdirectory."""
    try:
        relative = path.resolve().relative_to(CONTENT_ROOT)
    except ValueError:
        return True
    parts = relative.parts
    if not parts:
        return False
    return parts[0].lower() in ALLOWED_CONTENT_SUBDIRS


def should_skip(path: Path) -> bool:
    """Return True if the file should be ignored by the validator."""
    return path.name.lower() in SKIP_FILENAMES


def resolve_user_path(raw_target: str) -> Optional[Path]:
    """Resolve a user-supplied path relative to cwd, repo root, or content root."""
    raw_path = Path(raw_target).expanduser()
    search_paths: List[Path] = []
    if raw_path.is_absolute():
        search_paths.append(raw_path)
    else:
        search_paths.extend(
            [
                Path.cwd() / raw_path,
                REPO_ROOT / raw_path,
                CONTENT_ROOT / raw_path,
            ]
        )
    for candidate in search_paths:
        if candidate.exists():
            return candidate.resolve()
    return None


def resolve_targets(targets: Iterable[str]) -> List[Path]:
    """Expand iterable of target paths into unique Markdown files."""
    md_files: List[Path] = []
    seen: set[Path] = set()
    for raw_target in targets:
        target = resolve_user_path(raw_target)
        if target is None:
            sys.stderr.write(f"Warning: skipping unknown path {raw_target!r}\n")
            continue
        if target.is_dir():
            for file_path in sorted(target.rglob("*.md")):
                if (
                    should_skip(file_path)
                    or file_path in seen
                    or not _is_allowed_content_path(file_path)
                ):
                    continue
                md_files.append(file_path)
                seen.add(file_path)
        elif target.is_file() and target.suffix.lower() == ".md":
            if should_skip(target) or target in seen or not _is_allowed_content_path(target):
                continue
            md_files.append(target)
            seen.add(target)
        else:
            sys.stderr.write(f"Warning: skipping non-markdown path {raw_target!r}\n")
    return md_files
