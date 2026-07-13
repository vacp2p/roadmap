---
title: "Web Maintenance & Support"
tags:
  - "2026q3"
  - "web"
  - "ift"
draft: false
description: "Planned upkeep, fixes, and improvements on shipped web properties—distinct from weekly channel duty, which triages inbound requests. Includes AI-assisted review, debugging, testing, and guarded agent commits."
---

`ift-ts:web:ift:2026q3-maintenance`

## Description

**Maintenance vs duty.** These two commitments are complementary but not the same:

- **[[web/ift/2026q3-duty|Duty rotation]]** answers *who is “on call” for communication channels this week*: first response, triage, classifying bugs vs feature requests vs questions, filing or routing issues, and protecting teammates’ deep-work time. Duty is about **throughput of inbound signal**, not about personally fixing every item during that week.
- **This maintenance commitment** is the **actual engineering and follow-through** on already-delivered web work if duty cannot keep up: dependency and security updates, CI/deploy and platform reliability, implementing fixes and small improvements from the backlog, documenting support outcomes, logging work for planning, and shipping **hotfixes** when production issues require code or config changes. Maintenance is **scheduled, executed work** on shipped properties—not defined by the duty calendar.

The Web unit keeps previously delivered applications, sites, and tools healthy across the IFT ecosystem.

The maintenance commitment supports IFT's strategic objectives by:
- **Project Sustainability**: Shipped products stay secure, compatible, and operable
- **User Experience Continuity**: Regressions and rough edges are addressed deliberately
- **Technical Debt Management**: Post-launch issues are fixed or tracked rather than forgotten
- **Clear handoff from duty**: Issues triaged on duty land here (or in project backlogs) as **concrete maintenance work**
- **AI-assisted delivery**: Copilot / Claude / Cursor used for PR review, debugging, testing, and guarded low-risk commits — always with human approval before merge; no secrets in prompts

## Task List

### Maintenance

* fully qualified name: `ift-ts:web:ift:2026q3-maintenance:maintenance`
* owner: Felicio/Jinho/JulesFiliot
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description

Execute upkeep across delivered web properties for Q3: dependency and security bumps where needed; CI, preview deploy, and hosting workflows; bugfixes and small improvements that come from backlog, support, or duty triage; GitHub hygiene (issues, labels, planning links); urgent hotfixes when production is affected. Coordinate with **duty** so inbound items become tracked work here rather than orphaned chat threads.

#### Deliverables

- Merged fixes and improvements on shipped repos (PRs as appropriate)
- Stable CI/deploy and platform operations for maintained properties
- Support and stakeholder questions addressed or documented with clear next steps
- Issues created or updated for planning; hotfixes verified and briefly recorded
- Removed sample Cloudinary assets
- [Operator sunset Discord thread](https://discord.com/channels/864066763682218004/1522722281736896603/1522722529674919947)

### Merge Vercel teams under IFT-TS

* fully qualified name: `ift-ts:web:ift:2026q3-maintenance:merge-vercel-teams-ift-ts`
* owner: Felicio
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/24

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

### Merge Figma teams under IFT-TS

* fully qualified name: `ift-ts:web:ift:2026q3-maintenance:merge-figma-teams-ift-ts`
* owner: Felicio
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/24

#### Description

Consolidate the Figma teams the Web unit currently uses into a single team named **IFT-TS** (IFT Technical Services), mirroring the same change being made on Vercel ([[#Merge Vercel teams under IFT-TS|merge-vercel-teams-ift-ts]] above). One team means a single source of truth for files, projects, libraries, and member access.

#### Deliverables

- Inventory note (projects, files, libraries, plugins, members on both teams) with migration mapping
- All projects + files moved to the recipient team; per-project sanity check that shared libraries, prototypes, comments, and Dev Mode handoffs still work
- Recipient team renamed to **IFT-TS**

### Review workflows — Copilot, Claude, and agent PR review

* fully qualified name: `ift-ts:web:ift:2026q3-maintenance:review-workflows`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/18

#### Description

Define and roll out **PR review workflows** that combine GitHub Copilot review with Claude / Cursor (or equivalent) agent review for Web repos. Document when to use each tool, what to expect from automated review vs human review, and how to triage false positives.

#### Deliverables

- Written workflow: Copilot review + agent review checklist for Web PRs
- Enabled on at least the primary repos (`status-im/status-web`, `logos-co/logos-web`)
- Example PRs reviewed with both tools; notes on signal vs noise
- Team agreement on minimum human review before merge

### Agent-assisted debugging

* fully qualified name: `ift-ts:web:ift:2026q3-maintenance:agent-debugging`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/25

#### Description

Use agents for **debugging support**: summarising errors, proposing hypotheses, suggesting minimal repro steps, and drafting fix diffs — always validated by a developer before merge. Fold into duty/maintenance triage where it speeds up first response without skipping reproduction.

#### Deliverables

- Short guide: effective debugging prompts and repo context (AGENTS.md / rules where useful)
- At least two real bugs triaged or fixed with agent assistance, documented briefly
- Guardrails doc: what not to paste into prompts (tokens, PII, prod credentials)

### Agent-assisted testing

* fully qualified name: `ift-ts:web:ift:2026q3-maintenance:agent-testing`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/14
* end-date: 2026/08/01

#### Description

Use agents to **draft and extend tests** — unit, integration, and E2E where the stack supports it — with developers reviewing assertions and flakiness. Prioritise high-traffic paths (wallet extension, marketing pages, forms) and regressions found on duty.

#### Deliverables

- Testing guide: when agent-generated tests are acceptable vs hand-written
- At least one merged PR with agent-drafted or agent-extended test coverage
- Notes on CI integration and required human edits before merge

### Guarded agent commits

* fully qualified name: `ift-ts:web:ift:2026q3-maintenance:guarded-agent-commits`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/04
* end-date: 2026/08/22

#### Description

Pilot **agent-authored commits** for low-risk, scoped work: lint/format fixes, dependency bump PRs with clear changelogs, copy or config updates, and roadmap/doc edits. Every agent commit goes through normal PR review; no bypass of branch protection.

#### Deliverables

- Policy: allowed vs disallowed agent commit types
- At least three merged PRs authored primarily by an agent, with human review recorded
- Retrospective note: time saved, quality issues, adjustments for Q4