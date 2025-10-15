"""High-level validation orchestration."""

from pathlib import Path
from typing import List, Optional, Tuple

import yaml

from constants import REQUIRED_FRONT_MATTER_KEYS
from identity import derive_identity, validate_identity
from issues import ValidationIssue
from paths import should_skip
from tasks import TaskReport, parse_tasks


def parse_front_matter(lines: List[str]) -> Tuple[dict, int]:
    if not lines:
        return {}, 0
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx >= len(lines) or lines[idx].strip() != "---":
        return {}, 0
    end_idx = idx + 1
    while end_idx < len(lines) and lines[end_idx].strip() != "---":
        end_idx += 1
    if end_idx >= len(lines):
        raise ValueError("Unterminated YAML front matter")
    data = yaml.safe_load("\n".join(lines[idx + 1 : end_idx])) or {}
    if not isinstance(data, dict):
        raise ValueError("Front matter must parse to a mapping")
    return data, end_idx + 1


def validate_front_matter(path: Path, data: dict) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    for key in REQUIRED_FRONT_MATTER_KEYS:
        if key not in data or data[key] in (None, "", []):
            issues.append(ValidationIssue(path, 1, f"missing `{key}` in front matter"))
    if "tags" in data and not isinstance(data["tags"], (list, tuple)):
        issues.append(ValidationIssue(path, 1, "`tags` must be a list"))
    return issues


def find_task_section(lines: List[str], start: int) -> Optional[Tuple[int, int]]:
    for idx in range(start, len(lines)):
        if lines[idx].strip().lower() == "## task list":
            end = len(lines)
            for j in range(idx + 1, len(lines)):
                if lines[j].startswith("## "):
                    end = j
                    break
            return idx + 1, end
    return None


def validate_file(path: Path) -> List[ValidationIssue]:
    if should_skip(path):
        return []

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    issues: List[ValidationIssue] = []

    try:
        front_matter, body_start = parse_front_matter(lines)
    except Exception as exc:  # pragma: no cover - defensive guard
        return [ValidationIssue(path, 1, f"failed to parse front matter: {exc}")]

    issues.extend(validate_front_matter(path, front_matter))

    identity, identity_issues = derive_identity(path)
    issues.extend(identity_issues)

    expected_base = None
    if identity:
        issues.extend(
            validate_identity(path, front_matter, lines, body_start, identity)
        )
        expected_base = identity.expected_base

    section = find_task_section(lines, body_start)
    if not section:
        issues.append(ValidationIssue(path, None, "missing `## Task List` section"))
        return issues

    start, end = section
    tasks: List[TaskReport] = parse_tasks(lines, start, end, expected_base)
    if not tasks:
        issues.append(ValidationIssue(path, None, "no tasks found under `## Task List`"))
        return issues

    for task in tasks:
        for task_issue in task.issues:
            issues.append(
                ValidationIssue(
                    path=path,
                    line=task_issue.line,
                    message=f"Task `{task.name}` {task_issue.message}",
                )
            )
    return issues
