---
title: Logos CRM on Notion — Q3 expansion
tags:
  - "2026q3"
  - "web"
  - "logos"
draft: false
description: "Q3 Logos CRM on Notion: pivot from a custom CiviCRM dashboard to Notion as database and UI. Extend intake forms, configure Notion workspaces, funnel email via MailGun webhook, and add integrations, automations, and team support."
---

`ift-ts:web:logos:2026q3-logos-crm`

## Description

Q3 continuation of [[web/logos/2026q2-logos-crm|2026q2-logos-crm]]. We are **pivoting away from building a custom CiviCRM dashboard** and using **Notion as the database and UI** instead.

The **intake forms MVP is already live** on logos.co and continues to be built on, maintained, and adjusted. Form submissions remain the public entry point for contacts and leads. The tasks below still describe the same internal workflows — how contacts and leads are managed by People Ops, Ecodev, and Leadership — but delivery shifts from custom web pages to Notion databases, views, automations, and integrations.

**What changes**

- No custom `/cases`, `/case/:id`, or Ecodev web pages — teams work directly in Notion
- Notion databases, relations, and configured views replace the planned CiviCRM frontend
- Automations and notifications are set up in Notion (native automations, webhooks, or tools such as Make/Zapier where needed)
- Other teams already using Notion are supported with technical set-ups, syncs, or shared databases aligned to the same flows

**What stays**

- The workflow requirements from the source docs (funnel stages, scoring, coordinator assignment, Ecodev case properties, Leadership reporting, etc.)
- Ongoing maintenance and extension of the logos.co intake forms
- Cross-team visibility and the end-to-end Movement → Ecodev → Leadership coverage goal

> **Naming note.** Tracked as `logos-crm` (CRM workflow on Notion) to keep it distinct from the public-website content CMS work under [[web/logos/2026q2-logos-website|2026q2-logos-website]] (`cms-sanity`).

**Why this is its own quarter**

- Each workstream below is ≥ 2 weeks at team-of-3 pace, often with stakeholder review cycles.
- Ecodev alone is the biggest single chunk (custom case properties, BU/Platform/Tags/Segment/User Persona, activity types).
- Leadership reporting depends on Movement + Ecodev data living in a shared Notion workspace.
- Calendar / Discord integrations have their own auth + delivery reliability work.

**Risks**

- Notion native automations may not cover every conditional email branch; budget time for integration-tool workarounds (Make/Zapier).
- Custom case property surface for Ecodev is wide (dozens of fields per the doc) — Q3 v1 should ship a **scoped subset** (~10–12 highest-priority fields), with the long tail deferred to a Q4 polish pass.
- Notion API rate limits and relation cardinality grow as databases expand; monitor and adjust schema if list views slow down.

**Funnel outbound email**

People Ops / Ecodev need to **send emails to leads** in the Notion BD database as part of funnel automations. **Recommended direction:** webhook + **MailGun on a dedicated subdomain** (`funnel.logos.co` or `forms.logos.co`) rather than a Workspace `noreply@logos.co` Gmail alias:

- Avoids **reputation / blacklisting risk** for the primary `logos.co` marketing domain
- **Separate stats and logs** on the MailGun dashboard
- Can be **decommissioned** without affecting other projects
- A **project-specific subdomain** fits the funnel use case better than a generic noreply on the apex domain

Alternative considered: Gmail alias via Google Workspace (add alias domain + configure in Notion). Webhook path is cleaner if no alias exists yet; optional admin UI on [admin-acid.logos.co](https://admin-acid.logos.co/) for template editing.

## Task List

### Notion workspace architecture & Movement set-up

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:notion-workspace-setup`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/17

#### Description

Stand up the shared Notion workspace for Movement (Circles onboarding): Contacts and Cases databases, relations, scoring fields, formula-based scorecard, activities log, and configured list + detail views. Wire form submissions from logos.co into Notion (maintain and adjust the existing integration as needed).

Define the data model so Ecodev and Leadership can extend the same workspace in later Q3 tasks.

#### Deliverables

- Notion databases, relations, and Movement views deployed
- Field-mapping doc: form submission → Notion record creation/update
- Formula scorecard on Cases
- Saved views for coordinator-filtered case lists
- Short walkthrough recording for People Ops

### Movement kanban view

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:movement-kanban`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/06
* end-date: 2026/07/17

#### Description

Configure a Notion kanban view over Circles onboarding cases (`New Lead → Eligible → Call Scheduled → No Show → Approved/Redirected → Onboarding → Active`). Drag to change status (with guards via automation or property constraints), filter by coordinator/profile, cards link to the case detail page.

#### Deliverables

- Kanban board view on the Cases database
- Status change triggers the relevant automations / emails
- Coordinator + profile filter views

### Ecodev case management — databases & views

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:ecodev-case-management`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/13
* end-date: 2026/08/14

#### Description

Extend the Notion workspace with **Ecodev** sales-opportunity case management. **Scope the custom case property surface to ~10–12 highest-priority fields for v1** (e.g. Stage/Substatus, Owner, BU, Platform, Tags, Source, Priority, Notes, Last Contact, Validation Tracking). Defer the long tail (Segment, User Persona Type, full activity-type taxonomy, etc.) to a Q4 pass.

Reuse the Movement pattern: dedicated database(s), linked Contacts/Orgs, activities timeline, and configured list + detail views.

#### Deliverables

- Ecodev Cases database with sort + filter views (status, owner, BU, Platform, Priority, Tags)
- Case detail page template with editable scoped fields, activities timeline, related Contacts/Orgs
- Scoped-field decision recorded with rationale for what was deferred
- Operator note for Ecodev team on day-to-day workflow in Notion

### Ecodev kanban view

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:ecodev-kanban`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/03
* end-date: 2026/08/21

#### Description

Configure a Notion kanban view over Ecodev case Stage (`Lead → Preliminary Interest → Qualified → Negotiation → Confirmed → Future/Lost/Archive`). Status guards via automation or property constraints, owner/BU filters.

#### Deliverables

- Ecodev kanban board view
- Status change triggers relevant automations
- Owner / BU filter views

### Leadership reporting + exports

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:leadership-reporting`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/10
* end-date: 2026/09/04

#### Description

Reporting surface for Movement / Leadership inside Notion: funnel counts per status, progression metrics, active onboarding count, approved-vs-redirected, lead-source breakdown, owner/team breakdown, growth over time. Use linked databases, rollups, formulas, and dashboard pages. Add **CSV / XLS export** for filtered contacts, cases, and activity logs (Notion native export and/or integration-tool scheduled exports).

#### Deliverables

- Leadership dashboard page with filterable widgets (linked DB views, rollups, charts where Notion supports them)
- Funnel conversion metrics + onboarding completion + activity volume by team
- CSV / XLS export workflow documented and tested for filtered lists
- Cross-team visibility view (shared notes, owners, relationships, timeline)

### Notifications — @mentions + Discord bridge

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:notifications`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/17
* end-date: 2026/09/04

#### Description

Implement notification flows when team members are mentioned on case notes. Notion supports @mentions natively within the workspace; extend this with **email and/or Discord bot** notifications and a deep link back to the case page for members who live outside Notion. Coordinate with whoever owns the Discord bot for the channel/user mapping.

#### Deliverables

- @mention in Notion case notes triggers email and/or Discord notification with deep link
- Discord user mapping table (Notion person → Discord handle)
- Delivery test plan + brief operator doc

### Google Calendar two-way sync

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:google-calendar-sync`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/24
* end-date: 2026/09/18

#### Description

Reminder flow: a case-coordinator sets a follow-up date on a Notion case → an event appears in their Google Calendar with a link to the case; editing the event date in Calendar updates the case follow-up. Configure via Notion Calendar integration, Google Calendar sync, or an integration tool. Includes OAuth consent screen / Workspace admin approval where needed.

#### Deliverables

- OAuth integration (per-coordinator consent or Workspace-wide service account, decided in build)
- Bidirectional sync (case ↔ Calendar) with conflict handling documented
- Operator note covering grant flow, revocation, and limitations

### Automations, email templates & intake forms maintenance

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:emails-and-automations-rest`
* owner: JulesFiliot
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/08/07

#### Description

Configure automations and templated emails for the full Movement funnel: redirected-early-stage by profile, eligible → schedule a call, coordinator notifications on new case, no-show, post-call redirect by profile, approved-all-tracks, onboarding-by-profile, and newsletter / events subscription on form submission.

Continue maintaining and adjusting the logos.co intake forms as requirements evolve. Use Notion native automations, webhooks, and/or integration tools (Make, Zapier) as appropriate.

#### Deliverables

- [status-im/infra-sites#142](https://github.com/status-im/infra-sites/issues/142) chore(logos.co): update env variables & CSP
- [logos-co/logos-web#61](https://github.com/logos-co/logos-web/pull/61) feat: limit funnel form fields to 2000 chars
- [logos-co/logos-web#60](https://github.com/logos-co/logos-web/pull/60) chore(civi-crm): add Notion evaluation template
- [logos-co/logos-web#63](https://github.com/logos-co/logos-web/pull/63) feat(civi-crm): split funnel websites into discrete Notion columns
- [logos-co/logos-web#64](https://github.com/logos-co/logos-web/pull/64) fix(civi-crm): pin Notion writes to one data source
- All automations wired for Movement funnel end-to-end
- Email templates configured and tested with real test contacts
- Intake forms kept in sync with Notion schema changes
- Operator doc: how to tweak templates and automation rules without touching code

### Support existing Notion users & integration set-up

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:notion-team-support`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/13
* end-date: 2026/08/07

#### Description

Other internal teams already use Notion for related work. Provide technical set-up so their existing workspaces connect to (or mirror) the shared CRM data model where it makes sense: shared databases, synced views, or read-only linked databases. Document integration patterns and offer onboarding for teams aligning their Notion set-up with the shared flows.

#### Deliverables

- Inventory of teams already on Notion and their current set-up
- Integration or sync configuration for at least one cross-team use case
- Short guide: how to connect an existing Notion workspace to the shared CRM databases
- Onboarding session notes / recording

### Workspace governance + polish + maintenance hand-off

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:hardening-and-polish`
* owner: JulesFiliot
* status: not started
* start-date: 2026/09/07
* end-date: 2026/09/25

#### Description

Once the surface is feature-complete: workspace governance (permissions audit, backup/export strategy, audit log review), mobile-friendly view layouts for the most-used pages, performance pass on heavy linked-database views, and documentation for ongoing maintenance. Document hand-off to the Web maintenance commitment.

#### Deliverables

- Permissions audit + backup/export strategy documented
- Runbook (schema changes, common integration failures, how to add a new automation)
- Mobile-friendly case list and detail views verified
- Maintenance hand-off note folded into the Web maintenance commitment

### Sending domain and MailGun setup

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:mailgun-domain-setup`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/18

#### Description

Pick and provision the **sending subdomain** (`funnel.logos.co` or `forms.logos.co` — confirm with stakeholders). Infra sets up **MailGun** (DNS, SPF/DKIM, tracking domain if needed) and provides credentials for staging/production.

Document why this was chosen over a Workspace `noreply@logos.co` alias.

#### Deliverables

- Subdomain name decided and DNS/MailGun configured
- Staging credentials shared with Web for integration testing
- Short runbook: DNS records, MailGun dashboard access, rollback

### Webhook API for Notion-triggered sends

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:webhook-api`
* owner: JulesFiliot
* status: in progress (25%)
* start-date: 2026/07/14
* end-date: 2026/08/08

#### Description

Build a **webhook endpoint** Notion automations can call to send templated email to a lead (recipient, template id/key, merge fields from the Notion record). Authenticate requests (shared secret or signed payload). Send via MailGun; log message id and errors for debugging.

Host on the existing Web stack (e.g. `admin-acid.logos.co` API routes or a small service in the Logos admin repo).

#### Deliverables

- [logos-co/logos-web#109](https://github.com/logos-co/logos-web/pull/109) feat(civi-crm): forward steward submissions to n8n webhook
- POST webhook endpoint documented (payload, auth, response codes)
- MailGun integration with error handling and structured logs
- Staging test: Notion automation → webhook → delivered test message
- Rate limiting / abuse basics considered

### Funnel email templates and optional admin UI

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:funnel-email-templates-admin-ui`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/04
* end-date: 2026/08/29

#### Description

Initial **email templates** for the highest-priority BD funnel steps (coordinate with People Ops / Ecodev on copy). Optionally add a **minimal admin UI** on [admin-acid.logos.co](https://admin-acid.logos.co/) to edit template subject/body and preview merge fields — so non-engineers can adjust copy without code deploys.

If v1 is template-in-repo only, document the edit/deploy path instead of building UI in Q3.

#### Deliverables

- At least 2–3 production templates wired to the webhook
- Admin UI **or** documented repo-based template workflow (decision recorded)
- Operator note: how to add a new template and connect a Notion automation

### Funnel email — Notion automation integration and handoff

* fully qualified name: `ift-ts:web:logos:2026q3-logos-crm:funnel-email-notion-integration`
* owner: JulesFiliot
* status: in progress (10%)
* start-date: 2026/08/18
* end-date: 2026/09/05

#### Description

Wire **Notion BD database automations** to the webhook for the agreed funnel triggers (e.g. status change → send template X). Test with real-shaped test contacts. Hand off to CRM operators with monitoring pointers (MailGun logs, failed webhook retries).

#### Deliverables

- [Automated email after form submission](https://github.com/acid-info/admin-acid.logos.co/issues/52)
- Notion automations live for agreed triggers (staging → production)
- End-to-end test checklist signed off with stakeholders
- Handoff doc in CRM operator materials

## Out of scope for Q3 (stretch / Q4+)

- Custom CiviCRM dashboard or Next.js CRM frontend (superseded by Notion pivot).
- Long-tail Ecodev custom fields (Segment, User Persona Type, full activity-type taxonomy) deferred from the Q3 v1 scoping.
- Wider polish, accessibility audit, internationalization.

## Ongoing maintenance (after Q3)

Once the v1 workspace is live, expect ~**1–2 days/week** continuous maintenance: intake form adjustments, Notion schema tweaks as funnels evolve, new automations, integration-tool monitoring, occasional permission audits, and support for teams onboarding to the shared workspace. Fold into the Web maintenance commitment from Q4 onwards with an explicit slice reserved for the CRM.
