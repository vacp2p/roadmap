---
title: Admin Acid
tags:
  - "2026q4"
  - "web"
  - "ift"
draft: false
description: Maintain the Logos admin dashboard -- Notion infrastructure, Notion-linked emailing, and ad hoc requests from operators.
---

`ift-ts:web:ift:2026q4-admin-acid`

## Description

[admin-acid.logos.co](https://admin-acid.logos.co/) ([acid-info/admin-acid.logos.co](https://github.com/acid-info/admin-acid.logos.co)) is the internal admin dashboard behind the BD funnel, newsletters, calendar, and contributor data.
Q4 keeps the two surfaces that operators depend on daily working: the Notion integration layer (client, data sources, webhooks, block rendering, file uploads) and the emailing features built on top of it (auto-reply templates, funnel profile emails, internal notification templates, one-pager delivery).
The funnel and email lineage is recorded in [[web/logos/2026q3-logos-crm|Logos CRM]]; this commitment covers upkeep and incoming requests rather than new CRM scope.
Work arrives from operators and stakeholders during the quarter, so scope is agreed per request and tracked in repository issues.

## Task List

### Notion infrastructure maintenance

* fully qualified name: `ift-ts:web:ift:2026q4-admin-acid:notion-infrastructure`
* owner: JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Keep the Notion integration layer working as the Notion API, the workspace schema, and operator usage change.
Covers the Notion client and authentication, data source and database queries, incoming Notion webhooks and automations, block rendering, and file uploads.
Absorb Notion API version bumps and deprecations, repair syncs that drift when operators rename or restructure properties, and harden error handling and logging so failures surface instead of silently dropping records.

#### Deliverables

- PRs in [acid-info/admin-acid.logos.co](https://github.com/acid-info/admin-acid.logos.co) updating the Notion client, data source queries, webhook handling, and file uploads.
- Verified fixes for broken Notion syncs and automations, with tracked issues and resolution notes.
- Operator documentation for Notion property and database changes that require a code or configuration update.

### Notion-linked emailing features

* fully qualified name: `ift-ts:web:ift:2026q4-admin-acid:notion-emailing`
* owner: JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Maintain and extend the emailing features driven by Notion records and automations: endpoint-based auto-reply templates for form submissions, funnel profile emails, internal notification templates with per-template recipients, one-pager delivery, and Ghost newsletter subscription flows.
Keep template editing usable for non-engineers, keep merge fields in step with the Notion schema, and keep delivery observable through MailGun message ids and structured logs.
Ship the template and trigger changes stakeholders request during the quarter, and fix delivery failures, bounces, and mis-addressed sends.

#### Deliverables

- PRs for auto-reply, profile email, and internal notification template changes.
- Verified end-to-end sends from Notion automation trigger to delivered email, with failures logged and resolved.
- Updated operator notes covering how to add a template, edit copy, and connect a Notion automation.

### Ad hoc requests

* fully qualified name: `ift-ts:web:ift:2026q4-admin-acid:ad-hoc-requests`
* owner: Jinho/JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Handle requests that reach the admin dashboard during Q4 outside the two maintenance tracks above: new dashboard views, calendar and contributor data changes, newsletter operations, access and configuration changes, and small features asked for by People Ops, Ecodev, or BD.
Capture each request as an issue, agree scope and acceptance criteria with the requester, and schedule delivery by priority and capacity.
Create a dedicated roadmap task when a request grows into a substantial project.

#### Deliverables

- Scoped issues with acceptance criteria for each accepted request.
- PRs and deployed changes, validated with the requester.
- Tracked list of declined or deferred requests with the reason recorded.
