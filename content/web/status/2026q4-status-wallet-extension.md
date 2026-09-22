---
title: Status Wallet Extension
tags:
  - "2026q4"
  - "web"
  - "status"
draft: false
description: Maintain the Status Wallet browser extension and deliver prioritized ad hoc requests during Q4.
---

`ift-ts:web:status:2026q4-status-wallet-extension`

## Description

Q4 support for the Status Wallet browser extension in the [status-im/status-web](https://github.com/status-im/status-web) monorepo, continuing from [[web/status/2026q3-status-wallet-extension|2026q3-status-wallet-extension]].
The quarter has no fixed feature programme: it covers keeping the shipped extension healthy across releases and store publication, and delivering requests that arrive from stakeholders during the quarter.
Select concrete work with stakeholders as needs arise and record scope and acceptance criteria in linked issues.

## Task List

### Maintenance

* fully qualified name: `ift-ts:web:status:2026q4-status-wallet-extension:maintenance`
* owner: Jinho/JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Keep the wallet extension working as dependencies, chain and RPC providers, and browser extension platforms change.
Covers release coordination and Chrome Web Store publication, extension-specific dependencies and build configuration, transaction reliability and fee estimation, session and account recovery, dApp connection handling, and balance and price data sources.
Investigate production failures reported by users or stakeholders and ship hotfixes, coordinating shared tooling changes with the Web maintenance commitment.

#### Deliverables

- PRs in `status-im/status-web` for upkeep, dependency updates, and production hotfixes.
- Published extension releases on the [Chrome Web Store](https://chromewebstore.google.com/detail/status-portfolio-wallet-b/opkfeajbclhjdneghppfnfiannideafj), with release notes and coordination threads linked.
- Tracked issues for production failures, with reproduction steps and resolution notes.

### Ad hoc requests

* fully qualified name: `ift-ts:web:status:2026q4-status-wallet-extension:ad-hoc-requests`
* owner: Jinho/JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Implement prioritized wallet extension requests raised during Q4: new chain or asset coverage, wallet flow changes, dApp integration requirements, and design or copy updates as requirements become clear.
Capture each request as an issue, agree scope and acceptance criteria with stakeholders, and schedule delivery by priority and capacity.
Create a dedicated roadmap task when a request grows into a substantial project.

#### Deliverables

- Scoped issues with acceptance criteria and stakeholder requirements.
- PRs and released changes, with tests covering the affected wallet flows.
- Validation or stakeholder sign-off recorded per delivered request.
