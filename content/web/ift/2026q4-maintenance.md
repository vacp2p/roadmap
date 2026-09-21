---
title: Web Maintenance & Support
tags:
  - "2026q4"
  - "web"
  - "ift"
draft: false
description: Maintain shared Web tooling, dependencies, and deployment workflows, and improve AI-assisted development practices.
---

`ift-ts:web:ift:2026q4-maintenance`

## Description

Continue recurring Web maintenance from Q3, focusing on common tooling and workflows used by the team's websites.
Keep shared dependencies, CI, preview deployments, and hosting integrations reliable.
Build on Q3 AI review workflows and improve agent-assisted debugging, testing, and implementation across Web repositories.
Triage incoming requests with the team and track scope, priorities, and follow-up ownership.
Record site-specific upkeep and implementation under [[web/logos/2026q4-logos-website|Logos Website]] or [[web/status/2026q4-status-website|Status Website]], with shared changes tracked here once.

## Task List

### Maintenance

* fully qualified name: `ift-ts:web:ift:2026q4-maintenance:maintenance`
* owner: Jinho/JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Maintain common build tools, shared dependencies, CI checks, preview deployments, and hosting workflows.
Resolve shared infrastructure or tooling failures, coordinate with Infra where needed, and document changes that affect website development or releases.

#### Deliverables

- PRs updating shared dependencies, tooling, and CI or deployment configuration.
- Verified fixes for shared workflow failures and relevant operational documentation.

### AI and agentic workflow improvements

* fully qualified name: `ift-ts:web:ift:2026q4-maintenance:ai-agentic-improvements`
* owner: JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Continue the AI and agent-assisted development work from Q3:
- Improve the existing shared AI PR review workflow, tune repository context and instructions, and reduce false positives.
- Use agents to investigate failures, reproduce bugs, and propose fixes that developers validate.
- Draft or extend unit, integration, and E2E tests with agent assistance, reviewing assertions and checking for flakiness before adoption.
- Extend agent-authored changes for scoped maintenance work, keeping normal PR review and human approval before merge.
- Document effective workflows, handling of sensitive information, and lessons from actual usage so the team can reuse successful approaches.

#### Deliverables

- PRs improving shared AI review automation and repository-specific agent instructions.
- Documented examples of agent-assisted debugging, test coverage, and maintenance changes, linked to reviewed PRs.
- Updated team guidance for review, debugging, testing, and agent-authored changes.
- A short assessment of time saved, review quality, false positives, and remaining limitations.
