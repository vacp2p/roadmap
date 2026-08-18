---
title: Logos Website
tags:
  - "2026q3"
  - "web"
  - "logos"
draft: false
description: "Q3 continuation of the Logos website work — campaign and roadmap pages, release updates, newsletter flows, and self-hosting infrastructure."
---

`ift-ts:web:logos:2026q3-logos-website`

## Description

Q3 continuation of [[web/logos/2026q2-logos-website|2026q2-logos-website]]: deliver new campaign and roadmap pages, keep release and newsletter content current, and move the Logos website onto **self-hosted infrastructure** with a clean deployment story.

## Task List

### Build the Parallel

* fully qualified name: `ift-ts:web:logos:2026q3-logos-website:build-the-parallel`
* owner: Jinho
* status: done
* start-date: 2026/08/03
* end-date: 2026/08/18

#### Description

Build the `/build-the-parallel` campaign landing page from the approved design and content, with responsive behavior and production-ready integration in the Logos website.

#### Deliverables

- [logos-co/logos-web#128](https://github.com/logos-co/logos-web/pull/128) feat: add /build-the-parallel landing page
- [Build the Parallel preview](https://logos-co-web-git-web-build-the-parallel-status-im-web.vercel.app/build-the-parallel)
- Responsive landing-page implementation ready for production review

### Past Present Future

* fully qualified name: `ift-ts:web:logos:2026q3-logos-website:past-present-future`
* owner: Jinho
* status: done
* start-date: 2026/08/10
* end-date: 2026/08/18

#### Description

Host the Past Present Future museum experience on `logos.co`, integrate analytics and anchored navigation, and make its media work under production constraints.

#### Deliverables

- [logos-co/logos-web#142](https://github.com/logos-co/logos-web/pull/142) feat(web): add Museum anchor links
- [logos-co/logos-web#141](https://github.com/logos-co/logos-web/pull/141) fix(web): prevent ambiguous Umami events
- [logos-co/logos-web#138](https://github.com/logos-co/logos-web/pull/138) Fix blocked museum video embeds
- [logos-co/logos-web#137](https://github.com/logos-co/logos-web/pull/137) Fix museum YouTube embeds for production CSP
- [logos-co/logos-web#136](https://github.com/logos-co/logos-web/pull/136) Fix museum CTA links
- [logos-co/logos-web#133](https://github.com/logos-co/logos-web/pull/133) Optimise Past Present Future background video
- [logos-co/logos-web#132](https://github.com/logos-co/logos-web/pull/132) feat: host Past Present Future static site
- [Past Present Future](https://logos.co/past-present-future) production deployment

### Roadmap

* fully qualified name: `ift-ts:web:logos:2026q3-logos-website:roadmap`
* owner: Jinho
* status: done
* start-date: 2026/07/08
* end-date: 2026/08/10

#### Description

Add a content-backed `/roadmap` page with release timelines, overview cards, FAQs, responsive layouts, and page-specific SEO metadata.

#### Deliverables

- [logos-co/logos-web#101](https://github.com/logos-co/logos-web/pull/101) Add roadmap page
- [Roadmap page preview](https://logos-co-web-git-web-roadmap-page-status-im-web.vercel.app/roadmap)
- Roadmap content schema, route, sitemap entry, and responsive page sections

### Testnet v0.2.1

* fully qualified name: `ift-ts:web:logos:2026q3-logos-website:testnet-v0.2.1`
* owner: Jinho
* status: done
* start-date: 2026/08/05
* end-date: 2026/08/05

#### Description

Update logos.co links and copy for Logos Testnet v0.2.1 and Basecamp v0.2.3 while preserving automatic platform downloads and release-page fallbacks.

#### Deliverables

- [logos-co/logos-web#127](https://github.com/logos-co/logos-web/pull/127) Update links and copy for Testnet v0.2.1 and basecamp v0.2.3
- Updated homepage banner and Basecamp download links
- Regression coverage and repository guidance for future release-link updates

### Newsletters

* fully qualified name: `ift-ts:web:logos:2026q3-logos-website:newsletters`
* owner: JulesFiliot
* status: done
* start-date: 2026/07/29
* end-date: 2026/08/18

#### Description

Complete the Logos newsletter signup flow by forwarding submitted form data, subscribing funnel opt-ins, and sending consistent data-driven welcome replies from the Logos forms domain.

#### Deliverables

- [acid-info/admin-acid.logos.co#62](https://github.com/acid-info/admin-acid.logos.co/pull/62) fix(newsletters): sign unsubscribe links
- [acid-info/admin-acid.logos.co#63](https://github.com/acid-info/admin-acid.logos.co/pull/63) fix(newsletters): require a POST to unsubscribe, add one-click headers
- [acid-info/admin-acid.logos.co#65](https://github.com/acid-info/admin-acid.logos.co/pull/65) feat(newsletters): add unsubscribeUrl template placeholder
- [logos-co/logos-web#121](https://github.com/logos-co/logos-web/pull/121) feat: forward submitted form data on newsletter signup
- [acid-info/admin-acid.logos.co#61](https://github.com/acid-info/admin-acid.logos.co/pull/61) fix newsletter sender configuration
- [acid-info/admin-acid.logos.co#57](https://github.com/acid-info/admin-acid.logos.co/issues/57) data-driven auto-reply flow tested end to end
- Auto-reply templates configured for each `logos.co` newsletter subscription

### Selfhosting

* fully qualified name: `ift-ts:web:logos:2026q3-logos-website:selfhosting`
* owner: Jinho/JulesFiliot
* status: in progress (90%)
* start-date: 2026/08/24
* end-date: 2026/09/04

#### Description

Set up self-hosting infrastructure and deployment processes for the Logos website.

#### Deliverables

- [logos-co/logos-web#118](https://github.com/logos-co/logos-web/pull/118) chore: update technology stack with mix repo details
- [logos-co/logos-web#115](https://github.com/logos-co/logos-web/pull/115) fix(web): honor URL hash on initial load
- [logos-co/logos-web#114](https://github.com/logos-co/logos-web/pull/114) Increase small text to 12px
- [logos-co/logos-web#113](https://github.com/logos-co/logos-web/pull/113) Align λ lockup to brand guide
- [acid-info/admin-acid.logos.co#56](https://github.com/acid-info/admin-acid.logos.co/issues/56) Recurring meeting landing page
- [logos-co/logos-web#107](https://github.com/logos-co/logos-web/pull/107) Track Get Started card clicks
- Self-hosting configuration
- Deployment documentation
- Infrastructure setup
- [cms.logos.co](https://cms.logos.co/) deployed with the infra team
- [logos-co/logos-web#62](https://github.com/logos-co/logos-web/pull/62) refactor: make @repo/content the single source for home, get-started & movement page copy
- [logos-co/logos-web#68](https://github.com/logos-co/logos-web/pull/68) feat: add Logos Field Guide (#65) and rename Brand Kit to Design Guide (#66)
- [logos-co/logos-web#70](https://github.com/logos-co/logos-web/pull/70) refactor(civi-crm): write affiliated orgs to Mvmt Organization text field
- [logos-co/logos-web#71](https://github.com/logos-co/logos-web/pull/71) Fix favicon visibility
- [logos-co/logos-web#72](https://github.com/logos-co/logos-web/pull/72) Fix Field Guide chapter links
- [logos-co/logos-web#77](https://github.com/logos-co/logos-web/pull/77) Add node operator guide CTA
- [logos-co/logos-web#78](https://github.com/logos-co/logos-web/pull/78) Fix CMS deployed Server Actions
- [logos-co/logos-web#85](https://github.com/logos-co/logos-web/pull/85) Update testnet legal copy and add highlight modal to homepage
- [status-im/infra-sites#146](https://github.com/status-im/infra-sites/issues/146) chore(dev.logos.co): edit CSP rules
- [status-im/infra-sites#147](https://github.com/status-im/infra-sites/issues/147) chore(admin-acid.logos.co): add new environment variables
