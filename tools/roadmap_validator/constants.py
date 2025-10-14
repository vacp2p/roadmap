"""Shared constants and regular expressions for roadmap validation."""

import re

REQUIRED_FRONT_MATTER_KEYS = ("title", "tags", "description")
REQUIRED_TASK_FIELDS = ("owner", "status", "start-date", "end-date")

METADATA_ALIAS_MAP = {
    "fully-qualified-name": "fully-qualified-name",
    "fully qualified name": "fully-qualified-name",
    "owner": "owner",
    "status": "status",
    "start-date": "start-date",
    "start date": "start-date",
    "end-date": "end-date",
    "end date": "end-date",
}

DATE_PATTERN = r"^\d{4}/\d{1,2}/\d{1,2}$"
DATE_RE = re.compile(DATE_PATTERN)
TODO_PATTERN = r"\bTODO\b"
TODO_RE = re.compile(TODO_PATTERN, re.IGNORECASE)
TASK_HEADING_PATTERN = r"^###\s+(.*)"
TASK_HEADING_RE = re.compile(TASK_HEADING_PATTERN)
META_LINE_PATTERN = r"^[\-\*]\s*([^:]+):\s*(.*)$"
META_LINE_RE = re.compile(META_LINE_PATTERN)

VAGUE_KEYWORDS = (
    "investigate",
    "research",
    "explore",
    "analysis",
    "assess",
    "assessment",
    "evaluate",
    "evaluation",
    "review",
    "understand",
    "ideate",
    "brainstorm",
)

TANGIBLE_KEYWORDS = (
    "pr",
    "issue",
    "issues",
    "pull request",
    "merge request",
    "test",
    "tests",
    "notion",
    "doc",
    "docs",
    "documentation",
    "report",
    "reports",
    "dashboard",
    "script",
    "plan",
    "plans",
    "page",
    "pages",
    "spec",
    "specs",
    "analysis doc",
    "deliverable",
    "deliverables",
)

DEFAULT_SKIP_FILENAMES = {"index.md"}

__all__ = [
    "REQUIRED_FRONT_MATTER_KEYS",
    "REQUIRED_TASK_FIELDS",
    "METADATA_ALIAS_MAP",
    "DATE_RE",
    "TODO_RE",
    "TASK_HEADING_RE",
    "META_LINE_RE",
    "VAGUE_KEYWORDS",
    "TANGIBLE_KEYWORDS",
    "DEFAULT_SKIP_FILENAMES",
]
