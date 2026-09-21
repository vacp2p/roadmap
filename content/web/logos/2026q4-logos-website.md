---
title: Logos Website
tags:
  - "2026q4"
  - "web"
  - "logos"
draft: false
description: Maintain the Logos website, deliver fixes and improvements, and implement prioritized ad hoc features.
---

`ift-ts:web:logos:2026q4-logos-website`

## Description

Continue supporting the Logos website in Q4 through recurring upkeep, fixes and improvements to existing functionality, and delivery of new features requested during the quarter.
Build on the pages, release information, forms, and newsletter flows delivered in Q3.
Select concrete work with stakeholders as needs arise and record the scope and acceptance criteria in linked issues.

## Task List

### Maintenance

- fully qualified name: `ift-ts:web:logos:2026q4-logos-website:maintenance`
- owner: Jinho/JulesFiliot
- status: not started
- start-date: 2026/10/01
- end-date: 2026/12/31

#### Description

Keep the Logos website and its existing integrations working as dependencies, content, and releases change.
Maintain site-specific dependencies and configuration, release and download links, forms, newsletter flows, and deployment health.
Investigate production failures and ship necessary hotfixes, coordinating shared tooling changes with the Web maintenance commitment.

#### Deliverables

- PRs for site upkeep, dependency updates, configuration changes, and production hotfixes.
- Verified release and content updates, with tracked operational issues and resolution notes.

### Past Present Future: content update and migration

- fully qualified name: `ift-ts:web:logos:2026q4-logos-website:past-present-future`
- owner: Jinho
- status: not started
- start-date: 2026/10/01
- end-date: 2026/12/31

#### Description

Continue the Past Present Future work with the Comms team following the Mike experience.
Turn agreed content updates into an implementation-ready plan, including copy, calls to action, journey changes, media, and supporting assets.
Migrate the approved experience and its assets into the existing `logos-web` repository so it can be maintained, deployed, and measured alongside the main Logos website.
Preserve working routes, responsive behaviour, Umami tracking, and event naming through the migration.

Coordinate with the agency when content, creative assets, interaction design, or technical handover requires their input.
Document ownership, dependencies, and acceptance criteria before work that crosses the Comms, agency, and web teams begins.

#### Deliverables

- A prioritised, approved content and asset update list for the post-Mike experience, with owners and acceptance criteria.
- Migration PRs in `logos-web` for the approved experience, routes, assets, responsive behaviour, and analytics integration.
- Desktop and mobile QA covering key journeys, calls to action, video presentation, and Umami event tracking.
- Agency handover and review notes for any work requiring external creative or technical collaboration.

### Logos Zine

- fully qualified name: `ift-ts:web:logos:2026q4-logos-website:logos-zine`
- owner: Jinho
- status: not started
- start-date: 2026/10/12
- end-date: 2026/12/31

#### Description

Deliver the initial Logos Zine page described in [logos-web#172](https://github.com/logos-co/logos-web/issues/172), at `logos.co/zine`.
The first release will list the available issue or issues and provide PDF downloads, while keeping the content structure flexible for future issues.
It will be responsive on desktop and mobile, but will not include a web-based reader in this phase.

Before implementation, collect the final PDF, approved copy and assets, and a design wireframe or reference sites from stakeholders.

#### Deliverables

- A responsive `logos.co/zine` page listing the current issue and supporting additional issues without a page redesign.
- A verified PDF download for each published issue.
- Final copy, PDF, assets, and design references documented before implementation.
- QA evidence for desktop and mobile presentation, issue links, and downloads.

### Ad hoc features

- fully qualified name: `ift-ts:web:logos:2026q4-logos-website:ad-hoc-features`
- owner: Jinho/JulesFiliot
- status: not started
- start-date: 2026/10/01
- end-date: 2026/12/31

#### Description

Implement prioritized new Logos website features requested during Q4, including new pages, campaign experiences, forms, or integrations as requirements become clear.
Capture requests, agree scope and acceptance criteria with stakeholders, and schedule delivery according to priority and capacity.
Create dedicated roadmap tasks when a request grows into a substantial project.

#### Deliverables

- Scoped feature issues with acceptance criteria and stakeholder requirements.
- PRs and released features with validation or stakeholder review results.
