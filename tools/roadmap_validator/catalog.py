"""Validations for roadmap directory catalog files (index/preview)."""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

from issues import ValidationIssue
from paths import ALLOWED_CONTENT_SUBDIRS, CONTENT_ROOT

INDEX_ENTRY_RE = re.compile(r"^\*\s+\[\[([^\|\]]+)\|([^\]]+)\]\]")
QUARTER_HEADING_RE = re.compile(r"^##\s+(\d{4}q[1-4])\b")
AREA_HEADING_RE = re.compile(r"^###\s+`([^`]+)`")


@dataclass
class IndexCatalog:
    entries: Dict[Tuple[str, str], Dict[str, str]]  # (quarter, area) -> {ref: label}


def _parse_index(index_path: Path) -> IndexCatalog:
    entries: Dict[Tuple[str, str], Dict[str, str]] = defaultdict(dict)
    lines = index_path.read_text(encoding="utf-8").splitlines()
    current_quarter: Optional[str] = None
    current_area: Optional[str] = None

    for line in lines:
        quarter_match = QUARTER_HEADING_RE.match(line.strip())
        if quarter_match:
            current_quarter = quarter_match.group(1)
            current_area = None
            continue

        area_match = AREA_HEADING_RE.match(line.strip())
        if area_match:
            current_area = area_match.group(1).strip().rstrip(":")
            continue

        entry_match = INDEX_ENTRY_RE.match(line.strip())
        if entry_match and current_quarter and current_area:
            ref = entry_match.group(1).strip()
            label = entry_match.group(2).strip()
            entries[(current_quarter, current_area)][ref] = label

    return IndexCatalog(entries=entries)


def _expected_entry(unit: str, relative: Path) -> Tuple[str, str, str, str]:
    """Return quarter, area, reference, label expected for a roadmap file."""
    # relative has parts like ['dst', 'waku', '2025q4-waku-scaling.md']
    if len(relative.parts) < 3:
        raise ValueError(f"Unexpected roadmap path structure: {relative}")
    area = relative.parts[1]
    stem = relative.stem
    if "-" not in stem:
        raise ValueError(f"Filename should contain quarter and slug: {relative}")
    quarter, slug = stem.split("-", 1)
    reference = f"{unit}/{area}/{stem}"
    label = slug
    return quarter, area, reference, label


def validate_catalog(files: Iterable[Path]) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    files_by_unit: Dict[str, List[Path]] = defaultdict(list)
    allowed_references: Set[str] = set()

    for file_path in files:
        try:
            relative = file_path.resolve().relative_to(CONTENT_ROOT)
        except ValueError:
            continue
        if not relative.parts:
            continue
        unit = relative.parts[0]
        files_by_unit[unit].append(file_path)
        allowed_references.add(str(relative.with_suffix("")))

    if not files_by_unit:
        return issues

    for unit in sorted(files_by_unit.keys()):
        if unit not in ALLOWED_CONTENT_SUBDIRS:
            continue
        unit_path = CONTENT_ROOT / unit
        if not unit_path.exists():
            continue

        index_path = unit_path / "index.md"
        preview_path = unit_path / "preview.md"

        has_index = index_path.exists()
        if not has_index:
            issues.append(
                ValidationIssue(
                    path=index_path,
                    line=None,
                    message=f"missing `index.md` for `{unit}` catalog",
                )
            )

        if not preview_path.exists():
            issues.append(
                ValidationIssue(
                    path=preview_path,
                    line=None,
                    message=f"missing `preview.md` for `{unit}` catalog",
                )
            )

        if not has_index:
            continue

        catalog = _parse_index(index_path)
        for file_path in files_by_unit.get(unit, []):
            try:
                relative = file_path.resolve().relative_to(CONTENT_ROOT)
            except ValueError:
                continue
            try:
                quarter, area, reference, label = _expected_entry(unit, relative)
            except ValueError as exc:
                issues.append(
                    ValidationIssue(
                        path=file_path,
                        line=None,
                        message=str(exc),
                    )
                )
                continue

            key = (quarter, area)
            entries_for_key = catalog.entries.get(key, {})
            actual_label = entries_for_key.get(reference)
            if actual_label is None:
                issues.append(
                    ValidationIssue(
                        path=index_path,
                        line=None,
                        message=(
                            f"missing catalog entry for `{file_path.relative_to(CONTENT_ROOT)}` "
                            f"under quarter `{quarter}` and area `{area}`"
                        ),
                    )
                )
            elif actual_label != label:
                issues.append(
                    ValidationIssue(
                        path=index_path,
                        line=None,
                        message=(
                            f"catalog entry `{reference}` should use label `{label}` "
                            f"(found `{actual_label}`)"
                        ),
                    )
                )
        # Ensure index entries point to existing roadmap files.
        for (quarter, area), entries_for_key in catalog.entries.items():
            for reference, label in entries_for_key.items():
                if reference not in allowed_references:
                    continue
                expected_path = (CONTENT_ROOT / (reference + ".md")).resolve()
                if not expected_path.exists():
                    issues.append(
                        ValidationIssue(
                            path=index_path,
                            line=None,
                            message=(
                                f"catalog entry `{reference}` under quarter `{quarter}` area `{area}` "
                                "points to a missing file"
                            ),
                        )
                    )

    return issues
