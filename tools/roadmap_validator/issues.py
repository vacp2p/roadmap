"""Validation issue data structures."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class ValidationIssue:
    path: Path
    line: Optional[int]
    message: str
