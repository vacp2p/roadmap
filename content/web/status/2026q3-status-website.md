---
title: Status Website
tags:
  - "2026q3"
  - "web"
  - "status"
draft: false
description: "Q3 continuation of Status website work — blog search, copy/section reduction, A/B deployment, and a technical SEO audit-and-fix pass (errors, redirects, indexing, CWV, canonicals, internal linking, structured data)."
---

`ift-ts:web:status:2026q3-status-website`

## Description

Q3 continuation of [[web/status/2026q2-status-website|2026q2-status-website]]. The Q2 commitment covers SEO, translations, copy/section reduction, and self-hosting. Q3 adds:

- **Discoverability inside the blog** at [status.app/blog](https://status.app/blog): a search field that indexes posts across the existing seven categories (News, Product, Developers, Privacy & Security, Dapps, Community, Keycard) so readers can find content by title, summary, body, and tag/category.
- A **second copy / section-reduction pass** on the main marketing pages, following up on the Q2 round once we have a few weeks of analytics + stakeholder feedback.
- An **alternative deployment of [status.app](https://status.app/)** so marketing can run A/B tests or ship different iterations of positioning, hero copy, navigation, and CTAs without touching the canonical site.
- A **technical SEO audit-and-fix** pass on [status.app](https://status.app/) and related Status marketing properties in `status-im/status-web` — server errors, broken URLs, indexing blocks, mobile Core Web Vitals, canonicals, redirect chains, internal linking, and structured data (separate from copy/i18n).

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

### 5xx server error fix

* fully qualified name: `ift-ts:web:status:2026q3-status-website:5xx-server-errors`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/11

#### Description

Investigate **5xx server errors** reported in Search Console / crawl tools: identify root cause (app, edge, origin, CMS), resolve, and re-crawl to validate clean responses.

#### Deliverables

- Root-cause note per error class
- Fixes merged and deployed
- Post-fix validation (Search Console or equivalent)

### 404 audit and redirects

* fully qualified name: `ift-ts:web:status:2026q3-status-website:404-audit-redirects`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/25

#### Description

**404 audit + redirects** — map **217 broken URLs**, decide per URL: **301 redirect**, restore content, or intentional removal. Implement redirects in the hosting/routing layer with a tracked mapping sheet.

#### Deliverables

- Spreadsheet or doc mapping all 217 URLs → action (301 / restore / ignore)
- 301 rules implemented for agreed URLs
- Sample re-crawl confirming top-traffic 404s resolved

### noindex audit

* fully qualified name: `ift-ts:web:status:2026q3-status-website:noindex-audit`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/14
* end-date: 2026/07/25

#### Description

**noindex audit** — crawl all **322 excluded pages**, classify intentional vs accidental `noindex` (meta, headers, CMS defaults). Remove unintentional tags so valuable pages can index.

#### Deliverables

- Audit list with intentional / fix / defer per URL group
- Unintentional noindex removed where agreed
- Re-submit or validate indexing on a sample of fixed URLs

### robots.txt review

* fully qualified name: `ift-ts:web:status:2026q3-status-website:robots-txt-review`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/14
* end-date: 2026/07/18

#### Description

**robots.txt review** — confirm disallow rules match intent; **whitelist any mistakenly blocked** pages or paths that should be crawled.

#### Deliverables

- Current robots.txt documented with rationale per rule
- Fixes deployed for mistaken blocks
- Short operator note for future robots changes

### Mobile Core Web Vitals improvements

* fully qualified name: `ift-ts:web:status:2026q3-status-website:mobile-cwv`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/21
* end-date: 2026/08/15

#### Description

**Mobile CWV improvements** — address LCP, INP, and CLS on **143 affected mobile URLs**. Prioritise templates and routes with the most traffic and worst field/lab scores.

#### Deliverables

- Prioritised URL list with before metrics
- Fixes merged (images, fonts, JS deferral, layout stability, etc. as needed)
- After metrics on a representative sample

### Canonical tag cleanup

* fully qualified name: `ift-ts:web:status:2026q3-status-website:canonical-cleanup`
* owner: jinhojang6
* status: not started
* start-date: 2026/08/04
* end-date: 2026/08/15

#### Description

**Canonical tag cleanup** — resolve **17 alternate canonical** and **7 duplicate canonical** issues so each indexable URL has one clear preferred canonical.

#### Deliverables

- Inventory of affected URLs and chosen canonical target
- Template or CMS fixes applied
- Re-crawl validation on fixed set

### Redirect chain consolidation

* fully qualified name: `ift-ts:web:status:2026q3-status-website:redirect-chains`
* owner: jinhojang6
* status: not started
* start-date: 2026/08/11
* end-date: 2026/08/22

#### Description

**Redirect chain consolidation** — reduce **21 multi-hop redirects** to direct **301**s where possible (A → B → C becomes A → C).

#### Deliverables

- Chain map for all 21 cases
- Direct 301s implemented
- Verification that final URLs return 200 and correct canonical

### Internal linking to orphaned pages

* fully qualified name: `ift-ts:web:status:2026q3-status-website:internal-linking-orphans`
* owner: jinhojang6
* status: not started
* start-date: 2026/08/18
* end-date: 2026/09/05

#### Description

**Internal linking to orphaned pages** — target the **116 discovered-not-indexed** URLs that lack inbound internal links. Add contextual links from hub pages, nav, sitemap prominence, or related content blocks as appropriate.

#### Deliverables

- List of 116 URLs grouped by fix strategy (link in / sitemap / noindex intentionally)
- Internal links added for agreed orphans
- Follow-up crawl showing improved discovery on sample

### Structured data expansion

* fully qualified name: `ift-ts:web:status:2026q3-status-website:structured-data`
* owner: jinhojang6
* status: not started
* start-date: 2026/08/25
* end-date: 2026/09/12

#### Description

**Structured data expansion** — beyond existing breadcrumbs, implement **Article** and **FAQ** schema (and related types where they apply) on blog, help, and key landing pages. Validate with Rich Results / schema testing tools.

#### Deliverables

- Schema map: page types → JSON-LD templates
- Article + FAQ schema live on agreed templates
- Validation screenshots or Search Console rich-result checks
