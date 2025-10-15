"""Commitment identity extraction and related validation."""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from issues import ValidationIssue
from paths import CONTENT_ROOT, should_skip

IDENTIFIER_PATTERN = re.compile(r"^`([^`]+)`\s*$")
FILENAME_PATTERN = re.compile(r"^(?P<quarter>\d{4}q[1-4])-(?P<slug>.+)$")


@dataclass
class CommitmentIdentity:
    unit: str
    quarter: str
    area: str
    slug: str
    expected_tags: List[str]
    expected_identifier: str
    expected_base: str


def derive_identity(path: Path) -> Tuple[Optional[CommitmentIdentity], List[ValidationIssue]]:
    """Infer roadmap identity metadata from the file path."""
    issues: List[ValidationIssue] = []
    try:
        relative = path.resolve().relative_to(CONTENT_ROOT)
    except ValueError:
        return None, issues
    if len(relative.parts) < 3 or should_skip(path):
        return None, issues

    unit, area = relative.parts[0], relative.parts[1]
    match = FILENAME_PATTERN.match(path.stem)
    if not match:
        issues.append(
            ValidationIssue(
                path=path,
                line=None,
                message=f"filename should follow `<year>q<quarter>-<slug>.md` (found `{path.name}`)",
            )
        )
        return None, issues

    quarter = match.group("quarter")
    slug = match.group("slug")
    expected_base = f"vac:{unit}:{area}:{quarter}-{slug}"
    expected_tags = [quarter, unit, area]
    expected_identifier = expected_base
    identity = CommitmentIdentity(
        unit=unit,
        quarter=quarter,
        area=area,
        slug=slug,
        expected_tags=expected_tags,
        expected_identifier=expected_identifier,
        expected_base=expected_base,
    )
    return identity, issues


def validate_identity(
    path: Path,
    front_matter: Dict[str, object],
    lines: List[str],
    body_start: int,
    identity: CommitmentIdentity,
) -> List[ValidationIssue]:
    """Validate tags and inline identifier for a commitment."""
    issues: List[ValidationIssue] = []

    tags = front_matter.get("tags")
    if isinstance(tags, (list, tuple)):
        tag_values = [str(tag) for tag in tags]
        if tag_values != identity.expected_tags:
            issues.append(
                ValidationIssue(
                    path=path,
                    line=1,
                    message=f"tags should be {identity.expected_tags!r} (found {tag_values!r})",
                )
            )
    else:
        issues.append(
            ValidationIssue(
                path=path,
                line=1,
                message=f"tags must be a list matching {identity.expected_tags!r}",
            )
        )

    identifier_value: Optional[str] = None
    identifier_line: Optional[int] = None
    for idx in range(body_start, len(lines)):
        stripped = lines[idx].strip()
        match = IDENTIFIER_PATTERN.match(stripped)
        if match:
            identifier_value = match.group(1)
            identifier_line = idx + 1
            break

    if identifier_value is None:
        issues.append(
            ValidationIssue(
                path=path,
                line=body_start + 1,
                message=f"missing commitment identifier `{identity.expected_identifier}`",
            )
        )
    elif identifier_value != identity.expected_identifier:
        issues.append(
            ValidationIssue(
                path=path,
                line=identifier_line,
                message=(
                    f"identifier should be `{identity.expected_identifier}` (found `{identifier_value}`)"
                ),
            )
        )

    return issues
