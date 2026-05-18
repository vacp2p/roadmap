---
title: Logos CMS on CiviCRM
tags:
  - "2026q2"
  - "web"
  - "logos"
draft: false
description: "Custom operational layer on top of CiviCRM serving People Ops / Movement, Ecodev, and Leadership; integrates contact-form intake, role-aware views, Keycloak auth, and starts the longer Q2→Q3 build of the full CMS."
---

`ift-ts:web:logos:2026q2-logos-cms`

## Description

A **custom operational layer on top of [CiviCRM](https://civicrm.org/)** that gives three Logos teams **role-tailored views** over the same contact and case data, until the org decentralizes onto Logos App infrastructure:

1. **People Operations / Movement** — Circles onboarding (intake, review, scheduling, scorecard, redirect / approve, onboarding tracking)
2. **Ecosystem Development (Ecodev)** — Sales-opportunity case management (org/individual contacts, custom fields, statuses, activity types, kanban)
3. **Movement / Leadership** — Funnel and pipeline reporting (filters, conversion metrics, exports, cross-team visibility)

CiviCRM is already deployed and seeded with EcoDev data migrated from Notion; the contact form on [logos.co/contact](https://logos.co/contact) already feeds into CiviCRM. This commitment is about building **what CiviCRM cannot do natively or comfortably**: role-aware UI, automated weighted scorecard, @mention notifications, automation on case conditions, Keycloak SSO, and a CMS layer on top that EcoDev / People Ops / Leadership actually want to use.

**Hard constraints we’re building around**
- CiviCRM REST APIv4 is the integration surface.
- **Keycloak** is the planned SSO (coordinated with the Logos infra team).
- Email + mailing lists stay in CiviCRM; templating and CiviRules trigger emails on case state changes.
- The full CMS is **not a Q2-only delivery** — Q2 ships the urgent forms + Movement foundation and locks the architecture; Ecodev and Leadership views land in Q3.

## Build estimate & timeline (deep dive)

Team of **3 developers** (front-end heavy, with one full-stack able to land Keycloak / CiviCRM API glue).

| Workstream | Size | Notes |
|------------|------|-------|
| Discovery, architecture spec, CiviCRM API audit | 2 weeks | Lock data model, role permissions, stack choices |
| 3 intake form variations on logos.co | 2–3 weeks | In flight; hCaptcha already done |
| Auth scaffolding (Keycloak / OIDC) | 3–4 weeks | Dependent on Logos infra; can run in parallel |
| Movement (People Ops) list + case view + status flow | 4–6 weeks | Includes notes, profile tag edits, eligibility outcomes |
| Movement kanban view | 2–3 weeks | Drag to change status, filter by owner/profile |
| Ecodev case management (custom fields, statuses, activity types) | 5–7 weeks | Largest single workstream; rich custom case props |
| Ecodev kanban + list views | 2–3 weeks | Drag-and-drop is nice-to-have |
| Leadership reporting + analytics + exports (CSV/XLS) | 3–4 weeks | Funnel metrics, owner/team filters, time series |
| Notifications: @mentions + Discord bridge | 2–3 weeks | CiviCRM lacks @-mention semantics natively |
| Custom calculated scorecard field (weighted) | 1–2 weeks | Backend calc + UI display per case |
| Google Calendar two-way sync for reminders | 2–3 weeks | Edit deadline in Calendar reflects on case |
| Email template build-out + CiviRules hardening | 2–3 weeks | Approx. 12 templated emails per the doc |
| Testing (manual + automated UAT) + last-minute edits | 3–4 weeks | Folded across phases, not a single block |
| Production hardening + handoff | 2 weeks | Backups, monitoring, runbook |

**Sequential calendar wall-time** with a team of three working in parallel (parallelization roughly 1.8×, not 3×, given review/design/UAT bottlenecks):

- **Q2 2026 (now → 2026-06-30):** 3 forms live; Movement list + case view + early kanban; Keycloak SSO integrated; architecture spec frozen.
- **Q3 2026 (2026-07 → 09):** Ecodev case management + kanban; Leadership reporting + exports; notifications + scorecard + Calendar; email template build-out.
- **Q4 2026:** Polish, mobile responsiveness, drag-and-drop niceties, production hardening, handoff to ongoing maintenance.

**Realistic v1 “usable by all three teams”:** **end of Q3 2026** (≈ 4.5 months from today).
**Polished v1.x:** mid-Q4 2026.

**Ongoing maintenance (post-launch):** ~**0.3–0.5 FTE** continuous — CiviCRM monthly upgrades, plugin compatibility, new automation rules, mailing template tweaks, permission changes per team, role/permission audits, occasional schema changes as funnels evolve. This should fold into the Web maintenance commitment in subsequent quarters with an explicit slice reserved for the CMS.

**Risks (sized into the estimates above)**
- **CiviCRM API quirks** for case types + custom fields can eat weeks unexpectedly.
- **Keycloak ↔ CiviCRM session bridging** depends on Logos infra timeline.
- **Scope creep on Ecodev** custom case properties (BU, Platform, Tags, Segment, User Persona, …) — the doc lists dozens.
- **Notifications + Calendar** are easy to start, hard to make reliable (delivery + auth flows).
- Migration of in-flight data from Notion / spreadsheets if the new CMS displaces them.

## Task List (Q2 only — Q3 continuation noted)

### Architecture spec & build plan

* fully qualified name: `ift-ts:web:logos:2026q2-logos-cms:architecture-spec`
* owner: unassigned
* status: not started
* start-date: 2026/05/18
* end-date: 2026/05/29

#### Description

Lock the architecture and execution plan: stack choices (front-end framework, server/runtime, deployment target), CiviCRM APIv4 integration patterns, role model, auth boundaries, where custom logic lives vs. CiviRules, and a phased delivery plan that covers Q2 + Q3 + Q4. Get sign-off from People Ops, Ecodev, and Leadership.

#### Deliverables

- Written spec covering data flow, roles, integrations, and what is custom vs. what stays in CiviCRM
- Phased plan with named milestones tied to the team-of-three estimate above
- API and permission audit notes
- Sign-off from stakeholders captured in writing

### Three intake form variations on logos.co

* fully qualified name: `ift-ts:web:logos:2026q2-logos-cms:contact-form-variations`
* owner: unassigned
* status: not started
* start-date: 2026/05/18
* end-date: 2026/05/29

#### Description

Ship three variations of the contact form on logos.co (Activist Leader / Steward, Activist Builder, Coalition Partner) per the briefed [form spec](https://docs.google.com/document/d/1LnPSFyv3Lxcm-iU0yOwCQPoXwMfwn3iOaUP6TfWickc/edit?tab=t.0). Submissions feed CiviCRM as new contacts, set `Profile` + `Lead Source` tags, store long-form answers, set funnel stage to `New Lead`, auto-create a Circles onboarding case, subscribe to Circles contact groups, and notify the relevant internal reviewer. hCaptcha is already in place.

#### Deliverables

- Three form variants embedded on logos.co
- CiviCRM submission flow exercises all required tags, case creation, and notification rules
- Double opt-in subscription for general newsletter / local events
- Smoke test plan + a one-page operator note for People Ops

### Keycloak SSO for the CMS

* fully qualified name: `ift-ts:web:logos:2026q2-logos-cms:keycloak-sso`
* owner: unassigned
* status: not started
* start-date: 2026/05/25
* end-date: 2026/06/19

#### Description

Wire **Keycloak** as the SSO provider for the upcoming CMS surface. Coordinate with the Logos infra team on realm, clients, and group → role mapping. Stand up an OIDC-enabled session in the CMS app shell so all subsequent role-aware views can rely on a single auth model.

#### Deliverables

- OIDC client(s) configured in Keycloak (dev + prod)
- CMS app shell authenticates against Keycloak; role claims drive view access
- Short auth runbook for infra and developers

### Movement / People Ops list + case view (v1)

* fully qualified name: `ift-ts:web:logos:2026q2-logos-cms:movement-list-and-case-view`
* owner: unassigned
* status: not started
* start-date: 2026/05/25
* end-date: 2026/06/26

#### Description

First usable People Ops surface on top of CiviCRM: a **list view** of Circles onboarding cases (default entry point per the [wireframes](https://miro.com/app/board/uXjVHYp3Ug4=/?share_link_id=230116715431&)) and a **case detail page** for reading form responses, adding internal notes, editing the `Profile` tag, and recording the eligibility outcome (`Eligible` or `Redirected - Early Stage`). Wires the CiviRules-driven email branches per profile (templates 2.1 / 2.2 / 2.3 and 3) so the funnel can run end-to-end up to “Call Scheduled”.

#### Deliverables

- Cases list with status, owner, profile filters
- Case detail page with notes, profile tag edit, eligibility outcome action
- Email branches (CiviRules) verified for redirected-early-stage and eligible flows
- Walkthrough recording for People Ops

### Movement kanban view (foundation)

* fully qualified name: `ift-ts:web:logos:2026q2-logos-cms:movement-kanban`
* owner: unassigned
* status: not started
* start-date: 2026/06/15
* end-date: 2026/06/30

#### Description

Kanban view over Circles onboarding case status (`New Lead → Eligible → Call Scheduled → No Show → Approved/Redirected → Onboarding → Active`). Drag to change status (with status guards), filter by owner/profile, and link into the case detail page from each card. v1 can rely on click-to-change status if drag is too costly in the window; drag-and-drop and richer card content can land in Q3.

#### Deliverables

- Kanban over Circles onboarding cases, columns = funnel stages
- Status change action wired to CiviRules (sends correct templated email)
- Owner / profile filters

## Out of scope for Q2 (planned for Q3 continuation, tracked separately)

These appear in the source docs and the funnel walkthrough but **will not be shipped in Q2** at a team-of-three pace. They become a 2026q3 commitment (carry-over):

- Ecodev case management view (custom case properties, BU/Platform/Tags/Segment/User Persona, activity types)
- Ecodev list + kanban views with filters
- Leadership reporting dashboard, conversion metrics, owner/team filters
- Export functionality (CSV / XLS) for filtered contacts / cases / activities
- Notification system: @mentions on notes, Discord bot bridge, internal email cc reminders
- Custom calculated weighted scorecard field on case detail
- Google Calendar two-way sync for follow-up reminders
- Mobile responsiveness and drag-and-drop niceties
- Email template build-out for remaining flows (no-show, post-call redirect, onboarding-by-profile)
- Production hardening (backups, monitoring, runbook) + maintenance handoff
