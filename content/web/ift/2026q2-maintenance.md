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
* end-date: 2026/05/12

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
- [Guidelines for Uploading Dynamic HTML Content](https://docs.google.com/document/d/1s565y_bS81R_ZhHU8VhOmmwRttCaOVQRul2zVgQQpSs/edit?usp=sharing)
- Merged fixes and improvements on shipped repos (PRs as appropriate)
- Stable CI/deploy and platform operations for maintained properties
- Support and stakeholder questions addressed or documented with clear next steps
- Issues created or updated for planning; hotfixes verified and briefly recorded

### Merge Vercel teams under IFT-TS

* fully qualified name: `ift-ts:web:ift:2026q2-maintenance:merge-vercel-teams-ift-ts`
* owner: unassigned
* status: not started
* start-date: 2026/05/19
* end-date: 2026/06/12

#### Description

Consolidate the two Vercel teams the Web unit currently uses into a single team named **IFT-TS** (IFT Technical Services). Vercel confirmed teams can’t be merged literally; instead, **keep one as the recipient**, migrate the other team’s projects and domains in, then **rename** the recipient. Their recommendation captured in the support thread:

**Why also (besides one team to manage):** members who currently sit on **both** teams are billed **twice** under [Vercel’s per-seat pricing](https://vercel.com/pricing). Consolidating to one team means each person counts as **one paid seat**, not two — straightforward cost reduction proportional to how many people overlap.


> *“It is not possible for us to ‘merge accounts or teams.’ You would need to create a new team and then migrate the projects and resources as you’d like. My recommendation would be to keep one of the teams, and then migrate all the projects and domains from the other team into the one you decide is the ‘main one.’ After that, you can rename the team.”*

> Pricing: per [Vercel pricing](https://vercel.com/pricing) — no special behaviour or rates for merged members. Switching to Pro: see [Switching to Pro](https://vercel.com/docs/plans/pro-plan/switching). No breaking changes expected.

Source teams:
- [vercel.com/status-im-web](https://vercel.com/status-im-web)
- [vercel.com/acidinfo](https://vercel.com/acidinfo)

Plan (per Vercel):
1. **Pick the recipient team** (proposed: `status-im-web` — larger project inventory; confirm before migrating).
2. **Inventory** projects, domains, env vars, integrations, deploy hooks, and team members on both sides; flag anything that needs special handling.
3. **Transfer projects** from the other team into the recipient — [project transfer docs](https://vercel.com/docs/projects/transferring-projects).
4. **Transfer domains** alongside or after each project — [domain transfer docs](https://vercel.com/docs/domains/working-with-domains/transfer-your-domain). Watch DNS / TLS continuity.
5. **Re-add integrations, env vars, deploy hooks** on the recipient as needed; verify CI / preview deploys per project after move.
6. **Switch the recipient to the new Pro plan** if not already on it — [Switching to Pro](https://vercel.com/docs/plans/pro-plan/switching).
7. **Rename** the recipient team to `IFT-TS` (slug `ift` if available; otherwise `ift-ts`). Update any hardcoded `vercel.com/<team>` references in docs / READMEs / CI.
8. **Close** the now-empty source team.
9. **Announce** the change to project owners and anyone with deploy access.

#### Deliverables

- Inventory note (projects, domains, env vars, integrations, members on both teams) with migration mapping
- All projects + domains moved to the recipient team; per-project sanity check that deploys + previews + custom domains still work
- Recipient team switched to the right Pro plan
- Recipient team renamed to **IFT-TS** (`vercel.com/ift` or `vercel.com/ift-ts`)
- Source team closed
- Brief operator note: who/what to ping for Vercel access under the new team, including the support-thread context
