"""Task parsing and validation routines."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from constants import (
    DATE_RE,
    META_LINE_RE,
    METADATA_ALIAS_MAP,
    REQUIRED_TASK_FIELDS,
    TANGIBLE_KEYWORDS,
    TASK_HEADING_RE,
    TODO_RE,
    VAGUE_KEYWORDS,
)


@dataclass
class TaskIssue:
    message: str
    line: int


@dataclass
class TaskReport:
    name: str
    line: int
    metadata: Dict[str, Tuple[str, int]] = field(default_factory=dict)
    had_description: bool = False
    description_lines: int = 0
    description_line: Optional[int] = None
    description_texts: List[Tuple[str, int]] = field(default_factory=list)
    deliverables_sections: int = 0
    deliverables_items: int = 0
    deliverables_line: Optional[int] = None
    deliverables_texts: List[Tuple[str, int]] = field(default_factory=list)
    todo_hits: List[Tuple[str, int]] = field(default_factory=list)
    issues: List[TaskIssue] = field(default_factory=list)
    expected_base: Optional[str] = None

    def add_issue(self, message: str, line: Optional[int] = None) -> None:
        self.issues.append(TaskIssue(message, line or self.line))

    def record_metadata(self, key: str, value: str, line: int) -> None:
        canonical = METADATA_ALIAS_MAP.get(key, key)
        self.metadata[canonical] = (value.strip(), line)

    def finalize(self) -> None:
        for field_name in REQUIRED_TASK_FIELDS:
            if field_name not in self.metadata:
                self.add_issue(f"missing `{field_name}` metadata", self.line)
                continue
            value, line = self.metadata[field_name]
            if not value:
                self.add_issue(f"`{field_name}` value is empty", line)
            elif field_name in ("start-date", "end-date") and not DATE_RE.match(value):
                self.add_issue(
                    f"`{field_name}` should use YYYY/MM/DD format (found `{value}`)", line
                )

        if not self.had_description or self.description_lines == 0:
            line = self.description_line or self.line
            self.add_issue("missing populated `#### Description` section", line)

        if self.deliverables_sections == 0:
            line = self.deliverables_line or self.line
            self.add_issue("missing `#### Deliverables` section", line)
        elif self.deliverables_sections > 1:
            line = self.deliverables_line or self.line
            self.add_issue("multiple `#### Deliverables` sections found", line)
        elif self.deliverables_items == 0:
            line = self.deliverables_line or self.line
            self.add_issue("`#### Deliverables` section is empty", line)

        for text, line in self.todo_hits:
            self.add_issue(f"contains TODO marker: `{text.strip()}`", line)

        description_vague_hits = [
            (text, line)
            for text, line in self.description_texts
            if any(keyword in text.lower() for keyword in VAGUE_KEYWORDS)
        ]
        has_tangible_deliverable = any(
            any(keyword in text.lower() for keyword in TANGIBLE_KEYWORDS)
            for text, _ in self.deliverables_texts
        )
        if description_vague_hits and not has_tangible_deliverable:
            text, line = description_vague_hits[0]
            self.add_issue(
                "uses vague wording without tangible deliverables; clarify scope "
                f"(`{text.strip()}`)",
                line,
            )

        fq_entry = self.metadata.get("fully-qualified-name")
        if fq_entry and self.expected_base:
            raw_value, line = fq_entry
            normalized = raw_value.strip().strip("`")
            expected = self.expected_base
            if not (
                normalized == expected or normalized.startswith(f"{expected}:")
            ):
                self.add_issue(
                    f"`fully qualified name` should start with `{expected}` (found `{normalized}`)",
                    line,
                )


def parse_tasks(
    lines: List[str],
    start: int,
    end: int,
    expected_base: Optional[str],
) -> List[TaskReport]:
    tasks: List[TaskReport] = []
    current: Optional[TaskReport] = None
    in_description = False
    in_deliverables = False

    def flush_current() -> None:
        nonlocal current, in_description, in_deliverables
        if current is not None:
            current.finalize()
            tasks.append(current)
        current = None
        in_description = False
        in_deliverables = False

    for idx in range(start, end):
        line = lines[idx]
        stripped = line.strip()
        heading_match = TASK_HEADING_RE.match(stripped)
        if stripped.startswith("## "):
            flush_current()
            break
        if heading_match:
            flush_current()
            task_name = heading_match.group(1).strip()
            current = TaskReport(name=task_name, line=idx + 1, expected_base=expected_base)
            continue
        if current is None:
            continue

        if stripped.lower().startswith("#### "):
            in_description = False
            in_deliverables = False
            section_title = stripped[4:].strip().lower()
            if section_title == "description":
                current.had_description = True
                current.description_line = idx + 1
                current.description_lines = 0
                current.description_texts = []
                in_description = True
            elif section_title == "deliverables":
                current.deliverables_sections += 1
                current.deliverables_line = idx + 1
                current.deliverables_items = 0
                current.deliverables_texts = []
                in_deliverables = True
            continue

        if stripped == "---":
            in_description = False
            in_deliverables = False
            continue

        meta_match = META_LINE_RE.match(stripped)
        if meta_match:
            field_key = meta_match.group(1).strip().lower().replace("_", " ")
            value = meta_match.group(2)
            current.record_metadata(field_key, value, idx + 1)
            continue

        if in_description:
            if stripped:
                current.description_lines += 1
                current.description_texts.append((stripped, idx + 1))
                if TODO_RE.search(stripped):
                    current.todo_hits.append((stripped, idx + 1))
            continue

        if in_deliverables:
            if stripped:
                if TODO_RE.search(stripped):
                    current.todo_hits.append((stripped, idx + 1))
                if stripped != "---":
                    current.deliverables_items += 1
                    current.deliverables_texts.append((stripped, idx + 1))
            continue

        if stripped and TODO_RE.search(stripped):
            current.todo_hits.append((stripped, idx + 1))

    flush_current()
    return tasks
