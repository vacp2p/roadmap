---
title: Status Website
tags:
  - "2026q3"
  - "web"
  - "status"
draft: false
description: "Q3 continuation of Status website work — adds searchable blog at status.app/blog, a second copy / section-reduction pass after the Q2 round, and an alternative status.app deployment for A/B testing and marketing iteration."
---

`ift-ts:web:status:2026q3-status-website`

## Description

Q3 continuation of [[web/status/2026q2-status-website|2026q2-status-website]]. The Q2 commitment covers SEO, translations, copy/section reduction, and self-hosting. Q3 adds:

- **Discoverability inside the blog** at [status.app/blog](https://status.app/blog): a search field that indexes posts across the existing seven categories (News, Product, Developers, Privacy & Security, Dapps, Community, Keycard) so readers can find content by title, summary, body, and tag/category.
- A **second copy / section-reduction pass** on the main marketing pages, following up on the Q2 round once we have a few weeks of analytics + stakeholder feedback.
- An **alternative deployment of [status.app](https://status.app/)** so marketing can run A/B tests or ship different iterations of positioning, hero copy, navigation, and CTAs without touching the canonical site.

## Task List

### Blog search at status.app/blog

* fully qualified name: `ift-ts:web:status:2026q3-status-website:blog-search`
* owner: Felicio
* status: not started
* start-date: 2026/07/13
* end-date: 2026/07/31

#### Description

Add a **search experience** to [status.app/blog](https://status.app/blog). Goals:

- A search input that filters posts by **title**, **excerpt/summary**, **body**, and **category** (the seven categories visible on the index page).
- Results show the same card layout as the current grid, with the matched term highlighted where reasonable.
- **Empty / no-results** states handled.
- Choice of implementation left to the build, but two sensible paths:
  - **Client-side index** built at deploy time from the CMS source (e.g. MiniSearch / FlexSearch / pagefind) — zero infra, fast for the current blog volume.
  - **Server-side endpoint** if the CMS / hosting stack already gives us one, or if the blog grows past what a static index serves comfortably.
- Behaves with **SSR / hydration** so first paint includes the input and category filter; deep-linkable via query param (`?q=…&category=…`).
- Plays well with **i18n** if the blog is translated (search within the current language; document the fallback).

#### Deliverables

- Search input + category filter shipped on [status.app/blog](https://status.app/blog)
- Deep-linkable URL params for query + category
- Empty / no-results states
- Short doc on the indexing approach chosen (and how it’s rebuilt on new posts)

#### Open questions

- Confirm the source of truth for blog posts (CMS / repo / API) — drives whether index is built at deploy time or queried live.
- Per-language indexing if multiple translations land in Q2 ([[web/status/2026q2-status-website|status-website:translations]]).

### Copy Changes, Section Reduction

* fully qualified name: `ift-ts:web:status:2026q3-status-website:copy-changes-section-reduction`
* owner: Felicio
* status: not started
* start-date: 2026/08/17
* end-date: 2026/08/28

#### Description

Second copy / section-reduction pass on the Status website, following the Q2 round ([[web/status/2026q2-status-website|status-website:copy-changes-section-reduction]]). Use analytics + stakeholder feedback from the weeks after the Q2 update to tighten copy and prune sections that haven’t earned their place.

#### Deliverables

- Updated copy on the targeted pages
- Section reductions and content-review notes
- Brief before/after summary referencing the Q2 baseline

### Alternative status.app deployment for A/B testing

* fully qualified name: `ift-ts:web:status:2026q3-status-website:alternative-deployment-ab`
* owner: Felicio
* status: not started
* start-date: 2026/08/03
* end-date: 2026/09/04

#### Description

Deploy an **alternative version of [status.app](https://status.app/)** so marketing can run **A/B tests** or ship different iterations of positioning, hero copy, navigation, sections, and CTAs without touching the canonical production site.

#### Deliverables

- Alternative `status.app` deployment live (split-traffic mechanism or parallel URL — decided in build)
- Variant selection mechanism (feature flag, query param, cookie, or edge split) documented
- Analytics tagged per variant so the marketing team can read impact
- Operator note for marketing: how to propose, deploy, and read a new iteration
