---
title: "Web Maintenance & Support"
tags:
  - "2026q2"
  - "web"
  - "ift"
draft: false
description: "Planned upkeep, fixes, and improvements on shipped web properties—distinct from weekly channel duty, which triages inbound requests."
---

`ift-ts:web:ift:2026q2-maintenance`

## Description

**Maintenance vs duty.** These two commitments are complementary but not the same:

- **[[web/ift/2026q2-duty|Duty rotation]]** answers *who is “on call” for communication channels this week*: first response, triage, classifying bugs vs feature requests vs questions, filing or routing issues, and protecting teammates’ deep-work time. Duty is about **throughput of inbound signal**, not about personally fixing every item during that week.
- **This maintenance commitment** is the **actual engineering and follow-through** on already-delivered web work if duty cannot keep up: dependency and security updates, CI/deploy and platform reliability, implementing fixes and small improvements from the backlog, documenting support outcomes, logging work for planning, and shipping **hotfixes** when production issues require code or config changes. Maintenance is **scheduled, executed work** on shipped properties—not defined by the duty calendar.

The Web unit keeps previously delivered applications, sites, and tools healthy across the IFT ecosystem.

The maintenance commitment supports IFT's strategic objectives by:
- **Project Sustainability**: Shipped products stay secure, compatible, and operable
- **User Experience Continuity**: Regressions and rough edges are addressed deliberately
- **Technical Debt Management**: Post-launch issues are fixed or tracked rather than forgotten
- **Clear handoff from duty**: Issues triaged on duty land here (or in project backlogs) as **concrete maintenance work**

## Task List

### Maintenance

* fully qualified name: `ift-ts:web:ift:2026q2-maintenance:maintenance`
* owner: Jinho/JulesFiliot
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Execute upkeep across delivered web properties for Q2: dependency and security bumps where needed; CI, preview deploy, and hosting workflows; bugfixes and small improvements that come from backlog, support, or duty triage; GitHub hygiene (issues, labels, planning links); urgent hotfixes when production is affected. Coordinate with **duty** so inbound items become tracked work here rather than orphaned chat threads.

#### Deliverables

- [acid-info/lpe-cms#5](https://github.com/acid-info/lpe-cms/pull/5) Add og_image field and auto-generate JPEG OG images on post publish
- [acid-info/logos-press-engine#267](https://github.com/acid-info/logos-press-engine/pull/267) Pre-generate OG images as JPEG via Strapi lifecycle and serve static URLs
- [acid-info/logos-press-engine#268](https://github.com/acid-info/logos-press-engine/pull/268) feat(calendar): shift dates and times according to browser's time zone
- [acid-info/admin-acid.logos.co#43](https://github.com/acid-info/admin-acid.logos.co/pull/43) refactor(calendar): make time field mandatory
- Merged fixes and improvements on shipped repos (PRs as appropriate)
- Stable CI/deploy and platform operations for maintained properties
- Support and stakeholder questions addressed or documented with clear next steps
- Issues created or updated for planning; hotfixes verified and briefly recorded
