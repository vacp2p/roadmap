# Roadmap Validator

Command line utility for verifying that roadmap Markdown files follow our actionability standards. The validator is used locally and in CI to guard the structure, metadata, and content quality of roadmap commitments.

## Features
- Enforces required front matter keys (`title`, `tags`, `description`).
- Infers roadmap identity from file paths and validates tags plus the inline identifier.
- Ensures each `## Task List` contains at least one well-formed `###` task.
- Checks task metadata (`owner`, `status`, `start-date`, `end-date`) and section completeness.
- Flags TODO markers, vague descriptions without tangible deliverables, and malformed dates.
- Restricts validation to specific `content/` subdirectories (dst, qa, nim, p2p, rfc, sc, sec, web).

## Installation
Python 3.10+ is required. The only runtime dependency is `pyyaml`, installed automatically in CI. For local runs:

```bash
pip install --disable-pip-version-check --no-cache-dir pyyaml
```

## Usage
```bash
python tools/roadmap_validator/validate.py [targets...]
python tools/roadmap_validator/validate.py *2025q4*
python tools/roadmap_validator/validate.py qa/waku dst rfc/nomos
```

### Targets
- Provide files or directories; defaults to `content/`.
- Wildcard-style tokens like `*2025q4*` filter to files whose contents include the substring.
- Non-Markdown inputs are ignored; missing paths emit warnings.

## GitHub Actions
`.github/workflows/roadmap-validator.yml` runs the validator on pushes to `main` and `chore/roadmap-validator`, checking changed Markdown files under allowed content directories. Findings emit annotations and are summarized in the job output.

## Development Notes
- Validation logic lives under `tools/roadmap_validator/`.
- Add unit tests or new checks in `tasks.py`, `identity.py`, or `validator.py`.
- Keep CLI changes backwards compatible, as the workflow depends on them.
