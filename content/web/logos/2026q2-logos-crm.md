---
title: Logos CRM on CiviCRM (MVP)
tags:
  - "2026q2"
  - "web"
  - "logos"
draft: false
description: "Minimum viable Movement-only CRM on top of CiviCRM: a /cases list and a /case/:id detail view, with intake forms, an API permission audit, parallel CiviRules + email config, and a basic-auth gate fronted by Keycloak when ready. Wider CRM (Ecodev, Leadership, kanban, calendar, etc.) is tracked in 2026q3-logos-crm."
---

`ift-ts:web:logos:2026q2-logos-crm`

## Description

This commitment scopes the **MVP slice** of the Logos CRM on top of [CiviCRM](https://civicrm.org/) so something usable lands by the **June 1st** stakeholder ask:

1. **`/cases`** — read-only list of Circles onboarding cases assigned to coordinators ([Miro wireframe](https://miro.com/app/board/uXjVHYp3Ug4=/?moveToWidget=3458764670369141288&cot=14))
2. **`/case/:id`** — read & write detail view of a Case and its linked Contact Individual, with Activities log, related Cases and Groups, and a **server-side computed scorecard** (average of the six scoring fields, written back to `Circle_Case.Scorecard` in the same update request) ([Miro wireframe](https://miro.com/app/board/uXjVHYp3Ug4=/?moveToWidget=3458764670365146716&cot=14))

This is **not the full CRM** described in the source docs. Ecodev case management, Leadership reporting, kanban views, @mentions / Discord, Google Calendar sync, full email template build-out, and OIDC-bridged identity all carry into [[web/logos/2026q3-logos-crm|2026q3-logos-crm]] as a separate commitment.

> **Naming note.** The source docs colloquially called this “CMS for CiviCRM”, but the thing being built is structurally a CRM frontend on top of CiviCRM. The roadmap calls it `logos-crm` to disambiguate it from the public-website content CMS work tracked under [[web/logos/2026q2-logos-website|2026q2-logos-website]] (`cms-sanity`).

**Hard constraints**
- CiviCRM **REST APIv4** is the integration surface; CiviCRM stays the database.
- **Keycloak proxy** in front of the app is the planned auth, requested from and handled by the Logos infra team. The CRM ships with a **basic-auth fallback** so the launch doesn’t block on infra timing.
- Writes from the CRM run under a **single service identity**: Activity logs show that identity, not the human operator. The “assigned to me” experience is implemented as a filter on the list view by coordinator name, not by logged-in identity.
- **Email + CiviRules automations** stay in CiviCRM admin (parallel workstream).

## How this stacks against the dev plan

A single-dev plan circulating estimates **2 weeks** for the MVP. I’d budget **2.5 weeks** for the same scope because:

- CiviCRM APIv4 has chewed up half-days repeatedly (permissions, `create_submission`, where-clause behaviour, silent foreign-key joins) — a one-week QA buffer is not enough.
- The frontend is the real cost: filterable table merged from three parallel CiviCRM calls + a detail view with ~15 editable fields across different input types + live scorecard = 5–6 days of focused FE work alone.
- The dev plan delegates Keycloak to infra and doesn’t address CiviRules + email templates at all. Both need someone (CRM basic-auth fallback for the first, CiviCRM admin work for the second) — added below as explicit tasks.

The dev plan is right to scope down and ship; this commitment formalises that decision.

## Tech stack (per dev plan)

- Next.js (frontend + thin backend routes)
- Tailwind CSS, TypeScript
- `@acid-info/logos-ui` + `@acid-info/logos-tokens` for visual consistency with logos.co
- No database — CiviCRM is the DB
- Keycloak proxy in front of the app (infra-owned); basic-auth fallback while we wait
- Template: [logos-next-tailwind-i18n-template](https://github.com/acid-info/logos-next-tailwind-i18n-template)

## Endpoints (thin Next.js backend)

| Method | Route | Description |
| --- | --- | --- |
| `GET` | `/api/cases` | List view. 3 parallel CiviCRM calls (`/Case`, `/Relationship`, `/CaseContact`) merged server-side by `case_id`. |
| `GET` | `/api/cases/[id]` | Detail. Round 1: `/Case` + `/CaseContact` (with deep contact join) + `/Activity` + `/Relationship`. Round 2: `/CaseContact` + `/GroupContact` by `contact_id`. |
| `PATCH` | `/api/cases/[id]` | Updates Case fields (status, profile, lead source, notes, six scoring fields) in a single CiviCRM `POST /Case`. Scorecard is computed server-side and written to `Circle_Case.Scorecard` in the same call. |
| `PATCH` | `/api/cases/[id]/coordinator` | Swap Case Coordinator: delete + create on `/Relationship`. |
| `PATCH` | `/api/contacts/[contactId]` | Updates Contact Individual fields (`Skills_Socials` custom group + native fields), with a parallel call for fields on separate entities (e.g. `email_primary`). |
| `GET` | `/api/coordinators` | Deduplicated list of all coordinators for the list-view filter dropdown. |

## Known limitations (carry into Q3)

- Cannot bridge Keycloak identity → CiviCRM API user without a custom **OIDC Resource Server** CiviCRM extension (none on the market). Tracked as a Q3+ follow-up.
- All CRM writes appear as the service identity in CiviCRM Activity logs.
- “Assigned to me” is approximated by filtering the list view by coordinator name.

## Task List

### Architecture spec & API audit

* fully qualified name: `ift-ts:web:logos:2026q2-logos-crm:architecture-spec-and-audit`
* owner: unassigned
* status: not started
* start-date: 2026/05/18
* end-date: 2026/05/22

#### Description

Lock the architecture and execution plan for the MVP: stack choices (per dev plan), repo layout (use the Next.js+Tailwind+i18n template), CiviCRM APIv4 patterns, role model (coordinator name filter, no per-user identity), and the parallel split between CRM code, basic-auth gate, and CiviRules admin work.

In parallel, **audit CiviCRM API permissions against the actual service key** for the 6 endpoints (the dev plan’s example queries use the APIv4 Explorer which runs as admin; the service key may not match). Capture incremental permission grants needed.

#### Deliverables

- Short spec (1–2 pages) referencing the dev plan and this commitment
- Verified permissions checklist for the 6 endpoints under the real service key
- Sign-off from People Ops, Ecodev, Movement on what is in MVP vs Q3
- CiviCRM dashboard sync completed with Jerry and Kris.
- [CiviCRM CMS Technical Design](https://www.notion.so/CiviCRM-CMS-Technical-Design-3618f96fb65c8003bcb7c7f2602861df?source=copy_link)
- [CMS for CiviCRM proposal feedback](https://www.notion.so/CMS-CiviCRM-dev-plan-35e8f96fb65c804db9a2fe4b72b527a1?source=copy_link)

### Three intake form variations on logos.co

* fully qualified name: `ift-ts:web:logos:2026q2-logos-crm:contact-form-variations`
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
- Smoke test plan + one-page operator note for People Ops

### Basic-auth gate (Keycloak fallback)

* fully qualified name: `ift-ts:web:logos:2026q2-logos-crm:basic-auth-gate`
* owner: unassigned
* status: not started
* start-date: 2026/05/25
* end-date: 2026/06/05

#### Description

Add an **env-var basic-auth gate** in front of the CRM so it can go live even if the Keycloak proxy from infra isn’t ready by June 1st. Coordinate in parallel with infra on the Keycloak proxy specs (realm, client, group → role mapping); when the proxy lands it replaces the basic-auth gate transparently from the CRM’s point of view.

#### Deliverables

- Basic-auth middleware (single shared credential per env, rotatable via env var)
- Short doc on the auth model and how to flip to Keycloak when the proxy is ready
- Infra ticket / coordination log with the Logos infra team for the Keycloak proxy

### CRM MVP — /cases list + /case/:id detail

* fully qualified name: `ift-ts:web:logos:2026q2-logos-crm:crm-mvp`
* owner: unassigned
* status: not started
* start-date: 2026/05/25
* end-date: 2026/06/12

#### Description

Build and ship the two-page Movement MVP described above:

- **/cases** — sortable / filterable table (status, profile, coordinator), merged server-side from three CiviCRM calls
- **/case/:id** — Case + linked Contact Individual fields editable inline (status, profile, lead source, notes, the six scoring fields); Activities log; related Cases + Groups
- **Scorecard** — six scoring inputs with a live computed average; written to `Circle_Case.Scorecard` in the same PATCH that touches the scoring fields
- Endpoints per the table above

Per the dev plan: ~1 week core build + 1 week testing / back-and-forth with Kris & Jerry. I’m budgeting **+2–3 extra days** for CiviCRM API surprises.

#### Deliverables

- `/cases` and `/case/:id` deployed behind the basic-auth gate
- 6 API routes functioning end-to-end against CiviCRM
- A short walkthrough recording for People Ops
- Open follow-ups documented (in case detail or as issues) for anything we deliberately deferred to Q3

### CiviRules + email templates (parallel CiviCRM admin)

* fully qualified name: `ift-ts:web:logos:2026q2-logos-crm:civirules-and-emails-mvp`
* owner: unassigned
* status: not started
* start-date: 2026/05/25
* end-date: 2026/06/05

#### Description

The MVP CRM itself doesn’t send emails — **CiviRules** does. Configure the **subset of CiviRules + email templates** needed to keep the Movement funnel running end-to-end through “Call Scheduled”:

- Templates 2.1 / 2.2 / 2.3 (redirected-early-stage by profile)
- Template 3 (Eligible → Schedule a call)
- Notify case-coordinator on new case
- Subscribe to Circles + sub-group on form submission (double opt-in for newsletter / events)

Remaining templates (no-show, post-call redirect, onboarding-by-profile, all-tracks approved) move to Q3 with the rest of the CRM.

#### Deliverables

- CiviRules wired for the 4 MVP-critical flows above
- Email templates in CiviCRM, rendered and tested with a real test contact
- Operator doc: how to tweak templates from CiviCRM admin without touching code
- [Circle onboarding email template fix](https://civicrm.logos.co/civicrm/admin/messageTemplates/add?action=update&id=84&reset=1)

## Out of scope for Q2 (tracked in 2026q3-logos-crm)

Everything below moves to [[web/logos/2026q3-logos-crm|2026q3-logos-crm]]:

- Movement kanban view
- Ecodev case management (custom case properties, BU/Platform/Tags/Segment/User Persona, activity types, list, kanban)
- Leadership reporting dashboard, conversion metrics, owner/team filters
- Export functionality (CSV / XLS) for filtered contacts / cases / activities
- @mentions on notes, Discord bot bridge, internal email cc reminders
- Google Calendar two-way sync for follow-up reminders
- Remaining CiviRules + email templates (no-show, post-call redirect, onboarding-by-profile, approved-all-tracks, etc.)
- Production hardening (backups, monitoring, runbook) + mobile responsiveness + drag-and-drop polish
- (Stretch) OIDC Resource Server CiviCRM extension to bridge Keycloak identity → CiviCRM users so Activity logs show real operators
- (Stretch) Same two-page pattern adapted for Business Development Cases (Ecodev)
