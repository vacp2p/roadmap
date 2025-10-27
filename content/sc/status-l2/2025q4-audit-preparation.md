---
title: Status Network L2 Audit Preparation
tags:
  - "2025q4"
  - "sc"
  - "status-l2"
draft: false
description: Prepare the Status Network L2 contracts for security audits by improving documentation, test organization, and formal verification properties.
---

`vac:sc:status-l2:2025q4-audit-preparation`

Prepare the Status Network L2 contracts for security audits by improving documentation, test organization, and formal verification properties.

## Description

As we approach the audit phase for the Status Network L2 contracts,
it's crucial to ensure that the codebase is well-documented,
properly tested,
and has clearly defined invariants.
This commitment focuses on preparing the contracts for a thorough security audit by:
- Reviewing and updating existing documentation
- Restructuring tests for better organization and clarity
- Documenting invariants based on existing formal verification work

These improvements will help auditors understand the system more quickly and thoroughly,
leading to a more effective audit process.

## Task List

### Review and update existing documentation
* fully qualified name: `vac:sc:status-l2:2025q4-audit-preparation:review-documentation`
* owner: r4bbit
* status: not started
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

Review all existing documentation for the Status Network L2 contracts,
including inline code comments,
NatSpec documentation,
and any external documentation files.
Update outdated information,
add missing documentation,
and ensure consistency across the codebase.

#### Deliverables

- [ ] Commits/PRs that update inline code comments and NatSpec
- [ ] Updated or new documentation files as needed
- [ ] Documentation review checklist

### Restructure tests into one contract per file
* fully qualified name: `vac:sc:status-l2:2025q4-audit-preparation:restructure-test-files`
* owner: r4bbit
* status: not started
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

Currently,
test files may contain multiple test contracts.
Restructure the test suite so that each test contract has its own dedicated file.
This improves test organization,
makes it easier to locate specific tests,
and follows best practices for test structure.

#### Deliverables

- [ ] Commits/PRs that split test contracts into separate files
- [ ] Updated test file naming conventions
- [ ] Tests still pass after restructuring

### Organize tests by unit and integration categories
* fully qualified name: `vac:sc:status-l2:2025q4-audit-preparation:organize-tests`
* owner: r4bbit
* status: not started
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

After restructuring test files,
organize them into clear categories:
unit tests and integration tests.
This may involve creating separate directories or using naming conventions to distinguish between test types.
Ensure that the distinction between unit and integration tests is clear and consistent.

#### Deliverables

- [ ] Commits/PRs that organize tests into unit and integration categories
- [ ] Directory structure or naming convention documentation
- [ ] Updated test running scripts/commands if needed

### Update properties.md with invariants from Certora rules
* fully qualified name: `vac:sc:status-l2:2025q4-audit-preparation:update-properties`
* owner: r4bbit
* status: not started
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

The Certora formal verification rules contain important invariants about the system.
Review the existing Certora rules and extract the key invariants.
Update the properties.md document to include these invariants,
providing clear explanations of what each invariant means and why it's important for the system's security and correctness.

#### Deliverables

- [ ] Commits/PRs that update properties.md with invariants
- [ ] Clear documentation of each invariant and its significance
- [ ] Cross-references between properties.md and Certora rules
