"""Template adherence validation for roadmap commitments."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

from issues import ValidationIssue
from paths import ALLOWED_CONTENT_SUBDIRS, CONTENT_ROOT

TEMPLATE_PATH = CONTENT_ROOT / "templates" / "commitment-template.md"
PLACEHOLDER_PATTERN = re.compile(r"<[^>\n]+>")


def _load_placeholders() -> List[str]:
    try:
        text = TEMPLATE_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    placeholders = []
    seen = set()
    for match in PLACEHOLDER_PATTERN.finditer(text):
        token = match.group(0)
        if token not in seen:
            placeholders.append(token)
            seen.add(token)
    return placeholders


TEMPLATE_PLACEHOLDERS = _load_placeholders()


def _is_commitment_file(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(CONTENT_ROOT)
    except ValueError:
        return False
    if not relative.parts:
        return False
    if relative.parts[0] == "templates":
        return False
    return relative.parts[0] in ALLOWED_CONTENT_SUBDIRS


def validate_template_adherence(
    path: Path,
    lines: List[str],
    body_start: int,
    task_section: Optional[Tuple[int, int]],
) -> List[ValidationIssue]:
    """Validate commitment structure against the template."""
    if not _is_commitment_file(path):
        return []

    issues: List[ValidationIssue] = []

    description_idx: Optional[int] = None
    for idx in range(body_start, len(lines)):
        if lines[idx].strip().lower() == "## description":
            description_idx = idx
            break

    if description_idx is None:
        issues.append(
            ValidationIssue(
                path=path,
                line=None,
                message="missing `## Description` section",
            )
        )
    else:
        if task_section:
            task_heading_idx = task_section[0] - 1
            if description_idx > task_heading_idx:
                issues.append(
                    ValidationIssue(
                        path=path,
                        line=description_idx + 1,
                        message="`## Description` section should appear before `## Task List`",
                    )
                )
        next_heading = len(lines)
        for j in range(description_idx + 1, len(lines)):
            if lines[j].strip().startswith("## "):
                next_heading = j
                break
        if all(not lines[k].strip() for k in range(description_idx + 1, next_heading)):
            issues.append(
                ValidationIssue(
                    path=path,
                    line=description_idx + 2,
                    message="`## Description` section should contain descriptive content",
                )
            )

    if TEMPLATE_PLACEHOLDERS:
        for idx, line in enumerate(lines):
            for match in PLACEHOLDER_PATTERN.finditer(line):
                token = match.group(0)
                if token in TEMPLATE_PLACEHOLDERS:
                    issues.append(
                        ValidationIssue(
                            path=path,
                            line=idx + 1,
                            message=f"remove placeholder `{token}` copied from the template",
                        )
                    )

    return issues
