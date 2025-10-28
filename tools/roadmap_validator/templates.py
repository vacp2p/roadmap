"""Unified template validation for roadmap commitments."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from constants import REQUIRED_FRONT_MATTER_KEYS
from issues import ValidationIssue
from paths import ALLOWED_CONTENT_SUBDIRS, CONTENT_ROOT

TEMPLATE_PATH = CONTENT_ROOT / "templates" / "commitment-template.md"
PLACEHOLDER_PATTERN = re.compile(r"<[^>\n]+>")


def _load_template_placeholders() -> List[str]:
    try:
        text = TEMPLATE_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    placeholders: List[str] = []
    seen = set()
    for match in PLACEHOLDER_PATTERN.finditer(text):
        token = match.group(0)
        if token not in seen:
            placeholders.append(token)
            seen.add(token)
    return placeholders


TEMPLATE_PLACEHOLDERS = _load_template_placeholders()


def _is_commitment_file(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(CONTENT_ROOT)
    except ValueError:
        return False
    if len(relative.parts) < 3:
        return False
    if relative.parts[0] == "templates":
        return False
    if path.suffix.lower() != ".md":
        return False
    if path.stem in ("index", "preview"):
        return False
    return relative.parts[0] in ALLOWED_CONTENT_SUBDIRS


@dataclass
class TemplateValidator:
    path: Path
    lines: List[str]
    body_start: int
    front_matter: Dict[str, object]
    task_section: Optional[Tuple[int, int]] = None

    def run(self) -> List[ValidationIssue]:
        issues: List[ValidationIssue] = []
        if not _is_commitment_file(self.path):
            return issues

        issues.extend(self._validate_front_matter())
        self.task_section = self._find_task_section()
        issues.extend(self._validate_description_section())
        issues.extend(self._validate_placeholders())
        return issues

    def _validate_front_matter(self) -> List[ValidationIssue]:
        issues: List[ValidationIssue] = []
        for key in REQUIRED_FRONT_MATTER_KEYS:
            value = self.front_matter.get(key)
            if value in (None, "", []):
                issues.append(
                    ValidationIssue(
                        path=self.path,
                        line=1,
                        message=f"missing `{key}` in front matter",
                    )
                )
        tags = self.front_matter.get("tags")
        if tags is not None and not isinstance(tags, (list, tuple)):
            issues.append(
                ValidationIssue(
                    path=self.path,
                    line=1,
                    message="`tags` must be a list",
                )
            )
        return issues

    def _find_task_section(self) -> Optional[Tuple[int, int]]:
        for idx in range(self.body_start, len(self.lines)):
            if self.lines[idx].strip().lower() == "## task list":
                end = len(self.lines)
                for j in range(idx + 1, len(self.lines)):
                    if self.lines[j].startswith("## "):
                        end = j
                        break
                return idx + 1, end
        return None

    def _validate_description_section(self) -> List[ValidationIssue]:
        issues: List[ValidationIssue] = []
        description_idx: Optional[int] = None
        for idx in range(self.body_start, len(self.lines)):
            if self.lines[idx].strip().lower() == "## description":
                description_idx = idx
                break

        if description_idx is None:
            issues.append(
                ValidationIssue(
                    path=self.path,
                    line=None,
                    message="missing `## Description` section",
                )
            )
            return issues

        if self.task_section:
            task_heading_idx = self.task_section[0] - 1
            if description_idx > task_heading_idx:
                issues.append(
                    ValidationIssue(
                        path=self.path,
                        line=description_idx + 1,
                        message="`## Description` section should appear before `## Task List`",
                    )
                )

        next_heading = len(self.lines)
        for j in range(description_idx + 1, len(self.lines)):
            if self.lines[j].strip().startswith("## "):
                next_heading = j
                break

        if all(
            not self.lines[k].strip() for k in range(description_idx + 1, next_heading)
        ):
            issues.append(
                ValidationIssue(
                    path=self.path,
                    line=description_idx + 2,
                    message="`## Description` section should contain descriptive content",
                )
            )
        return issues

    def _validate_placeholders(self) -> List[ValidationIssue]:
        if not TEMPLATE_PLACEHOLDERS:
            return []

        issues: List[ValidationIssue] = []
        for idx, line in enumerate(self.lines):
            for match in PLACEHOLDER_PATTERN.finditer(line):
                token = match.group(0)
                if token in TEMPLATE_PLACEHOLDERS:
                    issues.append(
                        ValidationIssue(
                            path=self.path,
                            line=idx + 1,
                            message=f"remove placeholder `{token}` copied from the template",
                        )
                    )
        return issues
