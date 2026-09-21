---
title: Source Code Level QA
tags:
  - "2026q4"
  - "qa"
  - "logos"
draft: false
description: Prototype an AI code analysis system for bug discovery, independent review, precise classification, and reproducible findings.
---

`ift-ts:qa:logos:2026q4-source-code-level-qa`

## Description

Build an AI code analysis system prototype that helps discover new bugs quickly and turns findings into actionable issues.
Use a second agent to independently review candidate findings and reduce false positives, then provide precise classifications and fix proposals.
Generate proofs or exploit reproductions for high-severity issues and regression tests where possible.

## Task List

### System prototype

* fully qualified name: `ift-ts:qa:logos:2026q4-source-code-level-qa:system-prototype`
* owner: Roman
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Prototype an AI code analysis workflow covering:
- Fast discovery of new bugs through agent-assisted code analysis.
- Independent cross-review by a second agent to challenge findings and reduce false positives.
- Precise issue classification, including impact, severity, affected scope, supporting code evidence, and a proposed fix. Use [LEZ issue #866](https://github.com/logos-blockchain/logos-execution-zone/issues/866) as an example of the expected reporting detail.
- Proof or exploit generation to reproduce and demonstrate high-severity findings.
- Regression test creation where possible, so confirmed bugs can be detected automatically in future changes.

#### Deliverables

- A working prototype and documentation for the discovery, cross-review, and reporting workflow.
- Classified findings with supporting evidence, second-agent review results, and fix proposals.
- Reproducible proofs or exploits for high-severity findings, with any reproduction limitations recorded.
- Regression test PRs where feasible, with remaining test coverage gaps documented.
