"""High-level validation orchestration."""

from pathlib import Path
from typing import List, Optional, Tuple

import yaml

from identity import derive_identity, validate_identity
from issues import ValidationIssue
from paths import should_skip
from tasks import TaskReport, parse_tasks
from templates import TemplateValidator


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

    identity, identity_issues = derive_identity(path)
    issues.extend(identity_issues)

    expected_base = None
    if identity:
        issues.extend(
            validate_identity(path, front_matter, lines, body_start, identity)
        )
        expected_base = identity.expected_base

    template_validator = TemplateValidator(path=path, lines=lines, body_start=body_start, front_matter=front_matter)
    template_issues = template_validator.run()
    issues.extend(template_issues)

    if template_validator.task_section is None:
        issues.append(ValidationIssue(path, None, "missing `## Task List` section"))
        return issues

    start, end = template_validator.task_section
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
