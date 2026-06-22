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
* status: done
* start-date: 2026/04/01
* end-date: 2026/05/26

#### Description

Execute upkeep across delivered web properties for Q2: dependency and security bumps where needed; CI, preview deploy, and hosting workflows; bugfixes and small improvements that come from backlog, support, or duty triage; GitHub hygiene (issues, labels, planning links); urgent hotfixes when production is affected. Coordinate with **duty** so inbound items become tracked work here rather than orphaned chat threads.

#### Deliverables

- [acid-info/logos-press-engine#269](https://github.com/acid-info/logos-press-engine/pull/269) fix(home): load all highlighted posts so "Show More" doesn't skip content
- [acid-info/admin-acid.logos.co#31](https://github.com/acid-info/admin-acid.logos.co/issues/31) Use BI's GitHub data instead of ours
- [acid-info/lpe-cms#5](https://github.com/acid-info/lpe-cms/pull/5) Add og_image field and auto-generate JPEG OG images on post publish
- [acid-info/logos-press-engine#267](https://github.com/acid-info/logos-press-engine/pull/267) Pre-generate OG images as JPEG via Strapi lifecycle and serve static URLs
- [acid-info/logos-press-engine#268](https://github.com/acid-info/logos-press-engine/pull/268) feat(calendar): shift dates and times according to browser's time zone
- [acid-info/admin-acid.logos.co#43](https://github.com/acid-info/admin-acid.logos.co/pull/43) refactor(calendar): make time field mandatory
- [status-im/status-web#1106](https://github.com/status-im/status-web/pull/1106) Remove legacy iOS app associations from the AASA file
- [status-im/status-web#1109](https://github.com/status-im/status-web/pull/1109) Upgrade `nixpkgs` to version 25.11 in `flake.nix`
- [status-im/status-web#1102](https://github.com/status-im/status-web/pull/1102) Add `/karma-tokenomics` page
- [status-im/status-web#1103](https://github.com/status-im/status-web/issues/1103) fix(wallet): swaps not working
- [acid-info/logos#36](https://github.com/acid-info/logos/pull/36) Add active circles page
- [status-im/status-web#1144](https://github.com/status-im/status-web/pull/1144) fix(wallet): pending-then-dropped transactions
- [vacp2p/research.logos.co#178](https://github.com/vacp2p/research.logos.co/pull/178) chore: rebrand Vac to Logos Research & update docusaurus-preset
- [acid-info/logos-docusaurus-plugins#316](https://github.com/acid-info/logos-docusaurus-plugins/pull/316) chore(docusaurus-preset): update vac assets
- [acid-info/logos-docusaurus-plugins#314](https://github.com/acid-info/logos-docusaurus-plugins/pull/314) fix(docusaurus-theme): make white X icon actually white & resize
- [acid-info/logos#38](https://github.com/acid-info/logos/pull/38) Patch Next.js high severity CVE
- [acid-info/admin-acid.logos.co#44](https://github.com/acid-info/admin-acid.logos.co/pull/44) Patch Next.js high severity CVE
- [status-im/status-web#1157](https://github.com/status-im/status-web/pull/1157) chore: upgrade next to version 15.5.16 across all projects
- [Guidelines for Uploading Dynamic HTML Content](https://docs.google.com/document/d/1s565y_bS81R_ZhHU8VhOmmwRttCaOVQRul2zVgQQpSs/edit?usp=sharing)
- Merged fixes and improvements on shipped repos (PRs as appropriate)
- Stable CI/deploy and platform operations for maintained properties
- Support and stakeholder questions addressed or documented with clear next steps
- Issues created or updated for planning; hotfixes verified and briefly recorded
- [acid-info/logos-press-engine#270](https://github.com/acid-info/logos-press-engine/pull/270) Update domain references from press.logos.co to blog.logos.co
- [status-im/status-web#1192](https://github.com/status-im/status-web/pull/1192) ci(website): scope workspace build to hub
- [status-im/status-software-legal-documents#28](https://github.com/status-im/status-software-legal-documents/pull/28) feat(sn): add withdrawal disclaimer
- [status-im/status-software-legal-documents#29](https://github.com/status-im/status-software-legal-documents/pull/29) chore(sn): update withdrawal disclaimer formatting
- [status-im/status-web#1189](https://github.com/status-im/status-web/pull/1189) chore(sn-legal): add pre-deposit withdrawal disclaimer and update legal-external remote
- [status-im/status-web#1191](https://github.com/status-im/status-web/pull/1191) chore(sn/status.app): withdrawal updates
- [acid-info/admin-acid.logos.co#45](https://github.com/acid-info/admin-acid.logos.co/pull/45) chore: deprecate projects routes and remove supporting pipeline
- [Brave Search re-indexing request for logos.co pages](https://discord.com/channels/973324189794697286/1508951064471408742/1509380170216247356)
- [acid-info/free.technology#21](https://github.com/acid-info/free.technology/pull/21) Remove Status Network homepage references
- [acid-info/logos-press-engine#271](https://github.com/acid-info/logos-press-engine/pull/271) Logos blog maintenance
- [acid-info/logos-press-engine#272](https://github.com/acid-info/logos-press-engine/pull/272) Logos blog maintenance
- [status-im/status-web#1198](https://github.com/status-im/status-web/pull/1198) self-host `apps/get.status.app`
- [status-im/status-web#1210](https://github.com/status-im/status-web/pull/1210) update `get.status.app`
- [status-im/status-web#1197](https://github.com/status-im/status-web/pull/1197) self-host `apps/status.network`
- [status-im/status-web#1199](https://github.com/status-im/status-web/pull/1199) self-host `apps/status.app`
- [status-im/status-web#1214](https://github.com/status-im/status-web/pull/1214) Deleting unnecessary ref url "ref=our.status.im"
- [acid-info/logos#42](https://github.com/acid-info/logos/pull/42) logos.co: Track sitewide button and link clicks in Umami
