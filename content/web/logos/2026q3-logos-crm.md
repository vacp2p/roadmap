---
title: Logos CRM on CiviCRM — Q3 expansion
tags:
  - "2026q3"
  - "web"
  - "logos"
draft: false
description: "Q3 continuation of the Logos CRM on CiviCRM: extend beyond the Movement MVP to cover Ecodev case management, Leadership reporting, kanban views, notifications, Calendar sync, and full email template build-out."
---

`ift-ts:web:logos:2026q3-logos-crm`

## Description

Q3 continuation of [[web/logos/2026q2-logos-crm|2026q2-logos-crm]], which ships only the Movement MVP (`/cases` list + `/case/:id` detail). This commitment covers the rest of the requirements doc — Ecodev, Leadership, kanban, notifications, Calendar sync, and full email automation — so all three teams (People Ops / Ecodev / Leadership) end Q3 with a usable v1.

> **Naming note.** Tracked as `logos-crm` (CRM frontend on top of CiviCRM) to keep it distinct from the public-website content CMS work under [[web/logos/2026q2-logos-website|2026q2-logos-website]] (`cms-sanity`).

**Why this is its own quarter**
- Each Q3 workstream below is ≥ 2 weeks at team-of-3 pace, often with stakeholder review cycles.
- Ecodev alone is the biggest single chunk (custom case properties, BU/Platform/Tags/Segment/User Persona, activity types).
- Leadership reporting depends on Ecodev + Movement data already living in the new shape.
- Calendar / Discord integrations have their own auth + delivery reliability work.

**Risks (carried over)**
- CiviCRM APIv4 quirks continue to be a recurring source of half-day detours; budget per task accordingly.
- Custom case property surface for Ecodev is wide (dozens of fields per the doc) — Q3 v1 should ship a **scoped subset** (~10–12 highest-priority fields), with the long tail deferred to a Q4 polish pass.
- The OIDC ↔ CiviCRM identity bridge remains unsolved without a custom extension; Activity logs continue to show the service identity unless that extension lands.

## Task List

### Movement kanban view

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:movement-kanban`
* owner: unassigned
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/17

#### Description

Kanban over Circles onboarding cases (`New Lead → Eligible → Call Scheduled → No Show → Approved/Redirected → Onboarding → Active`). Drag to change status (with guards), filter by coordinator/profile, cards link to `/case/:id`. Builds on the MVP shipped in Q2.

#### Deliverables

- Kanban page over Circles onboarding cases
- Status change wired to the same `PATCH /api/cases/[id]` and the relevant CiviRules emails
- Coordinator + profile filters

### Ecodev case management — list + detail

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:ecodev-case-management`
* owner: unassigned
* status: not started
* start-date: 2026/07/06
* end-date: 2026/08/14

#### Description

Bring up the same shape (list + detail) for **Ecodev** sales-opportunity cases. **Scope the custom case property surface to ~10–12 highest-priority fields for v1** (e.g. Stage/Substatus, Owner, BU, Platform, Tags, Source, Priority, Notes, Last Contact, Validation Tracking). Defer the long tail (Segment, User Persona Type, full activity-type taxonomy, etc.) to a Q4 pass.

#### Deliverables

- `/ecodev/cases` list with sort + filter (status, owner, BU, Platform, Priority, Tags)
- `/ecodev/case/:id` detail with editable scoped fields, activities timeline, related Contacts/Orgs
- Endpoints documented; permissions audit notes for any new entities touched
- Scoped-field decision recorded with rationale for what was deferred

### Ecodev kanban view

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:ecodev-kanban`
* owner: unassigned
* status: not started
* start-date: 2026/08/03
* end-date: 2026/08/21

#### Description

Kanban over Ecodev case Stage (`Lead → Preliminary Interest → Qualified → Negotiation → Confirmed → Future/Lost/Archive`). Status guards, owner/BU filters, drag-to-update. Drag-and-drop richness is a polish item if time allows.

#### Deliverables

- Ecodev kanban page
- Status change wired through `/api/cases/[id]` (or `/api/ecodev/cases/[id]` if the route shape diverges)
- Owner / BU filters

### Leadership reporting + exports

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:leadership-reporting`
* owner: unassigned
* status: not started
* start-date: 2026/08/10
* end-date: 2026/09/04

#### Description

Reporting surface for Movement / Leadership: funnel counts per status, progression metrics, active onboarding count, approved-vs-redirected, lead-source breakdown, owner/team breakdown, growth over time. Add **CSV / XLS export** for filtered contacts, cases, and activity logs.

#### Deliverables

- `/reporting` dashboard with filterable widgets
- Funnel conversion metrics + onboarding completion + activity volume by team
- CSV / XLS export endpoints + UI for filtered lists
- Cross-team visibility view (shared notes, owners, relationships, timeline)

### Notifications — @mentions + Discord bridge

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:notifications`
* owner: unassigned
* status: not started
* start-date: 2026/08/17
* end-date: 2026/09/04

#### Description

CiviCRM doesn’t do @-mentions natively. Implement an in-app @mention syntax on case notes that notifies the mentioned team member by **email and/or Discord bot** message with a deep link back to the case. Coordinate with whoever owns the Discord bot for the channel/user mapping.

#### Deliverables

- Note input with @username autocomplete (sourced from `/api/coordinators` + a Discord mapping table)
- Email + Discord notifications dispatched on mention, with deep link to `/case/:id`
- Delivery test plan + brief operator doc

### Google Calendar two-way sync

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:google-calendar-sync`
* owner: unassigned
* status: not started
* start-date: 2026/08/24
* end-date: 2026/09/18

#### Description

Reminder flow: a case-coordinator sets a follow-up date in the CRM → an event appears in their Google Calendar with a link to the case; editing the event date in Calendar updates the case follow-up. Includes OAuth consent screen / Workspace admin approval.

#### Deliverables

- OAuth integration (per-coordinator consent or Workspace-wide service account, decided in build)
- Bidirectional sync (case ↔ Calendar) with conflict handling documented
- Operator note covering grant flow, revocation, and limitations

### Email template build-out + remaining CiviRules

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:emails-and-civirules-rest`
* owner: unassigned
* status: not started
* start-date: 2026/07/13
* end-date: 2026/08/07

#### Description

Configure the remaining CiviRules and templated emails left out of the Q2 MVP slice: no-show (4), post-call redirect by profile (5.1.1 / 5.1.2 / 5.1.3), approved-all-tracks (5.2), onboarding-by-profile (6.1 / 6.2 / 6.3). Hardening pass on the Q2 MVP rules at the same time.

#### Deliverables

- All CiviRules wired for Movement funnel end-to-end
- ~8+ email templates in CiviCRM, rendered and tested with real test contacts
- Updated operator doc on template editing without touching code

### Production hardening + mobile + polish

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:hardening-and-polish`
* owner: unassigned
* status: not started
* start-date: 2026/09/07
* end-date: 2026/09/25

#### Description

Once the surface is feature-complete: backups, monitoring, runbook for incidents, mobile-responsive layout for the most-used views, drag-and-drop niceties on kanban, performance pass on the list endpoints (cache where it earns its keep). Document hand-off to ongoing maintenance.

#### Deliverables

- Backup + monitoring set up (with infra)
- Runbook in the repo (deploy, rollback, common CiviCRM API failures)
- Mobile-responsive `/cases` list and `/case/:id` detail
- Kanban drag-and-drop polished where it pays off
- Maintenance hand-off note folded into the Web maintenance commitment

## Out of scope for Q3 (stretch / Q4+)

- **OIDC Resource Server CiviCRM extension** to bridge Keycloak identity → CiviCRM users so Activity logs show real operators (instead of the single service identity). Large piece of work without a market option; track as a Q4+ research spike.
- Long-tail Ecodev custom fields (Segment, User Persona Type, full activity-type taxonomy) deferred from the Q3 v1 scoping.
- Wider polish, accessibility audit, internationalization.

## Ongoing maintenance (after Q3)

Once the v1 surface is live, expect ~**1–2 days/week** continuous maintenance: CiviCRM monthly upgrades + plugin compatibility, mailing template tweaks, new CiviRules as funnels evolve, occasional schema changes, role/permission audits. Fold into the Web maintenance commitment from Q4 onwards with an explicit slice reserved for the CRM.
