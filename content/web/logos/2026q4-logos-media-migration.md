---
title: "Logos Media: Production Cutover and Legacy Blog Retirement"
tags:
  - "2026q4"
  - "web"
  - "logos"
draft: false
description: "Complete the Logos media migration by making the Q3 implementation merge-ready, deploying it to logos.co, moving blog.logos.co traffic and feeds without breaking readers or subscribers, and retiring the legacy blog frontend after its remaining API and preview dependencies are removed."
---

`ift-ts:web:logos:2026q4-logos-media-migration`

## Description

Finish the media migration started in [[web/logos/2026q3-logos-media-migration|Q3]]. The native article and podcast experience is implemented in [logos-co/logos-web#103](https://github.com/logos-co/logos-web/pull/103), but completing the migration still requires Infra's help with adding the required environment variables and configuring the redirect rules.

Q4 moves the project from a working preview to a completed production cutover. We will deploy the new media routes, add the required Jenkins credentials, activate the `blog.logos.co` redirects with Infra through [status-im/infra-sites#168](https://github.com/status-im/infra-sites/issues/168), and monitor the SEO, feed, search, and playback behaviour after launch.

The production route contract is:

- `https://blog.logos.co/article/<slug>` becomes `https://logos.co/media/article/<slug>`
- `https://blog.logos.co/podcasts/<show>/<slug>` becomes `https://logos.co/media/podcasts/<show>/<slug>`

The cutover must preserve query strings, feed subscriber identity, canonical URLs, and access to content. The legacy blog frontend can be retired only after build fallbacks, editor previews, and any API or static-asset dependencies have a confirmed replacement or an explicitly retained route.

**What changes**

- The Q3 migration pull request is updated, reviewed, merged, and deployed to production.
- `logos.co/media` becomes the canonical production home for articles and podcast episodes.
- `blog.logos.co` article, podcast, listing, feed, policy, and legacy paths receive agreed permanent redirects.
- The legacy blog frontend is decommissioned once no required build, CMS preview, API, or asset traffic depends on it.

**What stays**

- The existing Strapi content source remains in use. Moving content into the `logos-web` content stack is not part of this cutover.
- Article and podcast features delivered in the Q3 implementation remain: rich content, footnotes, table of contents, discussion, related content, media search, feeds, responsive images, and persistent podcast playback.
- CMS and content operations continue while the public frontend moves to `logos.co`.

**Why this is its own quarter**

- The Q3 work has become a broad migration touching rendering security, static-export reliability, search, feeds, media assets, SEO, playback, and infrastructure.
- The application deployment and the `blog.logos.co` redirect switch must be sequenced. Redirects cannot be enabled until the matching production pages and feeds are verified.
- Decommissioning the legacy frontend is a separate gate from redirecting public pages because local and CI fallbacks, CMS draft previews, `/api/*`, and legacy assets may still depend on it.

**Risks**

- **Unsafe rich content.** Interactive CMS blocks must not execute untrusted scripts with access to the `logos.co` origin. The rendering boundary must be resolved before merge without losing required article behaviour.
- **Static-export reliability.** Media generation, sitemap creation, image processing, feeds, and search indexing depend on external content services. Unbounded requests or hidden fetch failures can make production builds unreliable or publish incomplete output.
- **Redirect gaps.** The Infra issue and the redirect map in the application PR do not yet describe exactly the same path set. Feed, policy, calendar, preview, API, asset, and non-`logos-state` podcast paths need an agreed disposition before the rules are enabled.
- **Subscriber and search continuity.** Incorrect feed IDs, redirect status codes, canonicals, or sitemap entries can create duplicate podcast episodes or delay search-engine migration.
- **Premature decommissioning.** Turning off the old service while builds or CMS previews still use it would break development or editorial workflows even if public article redirects work.

**Coordination**

- **Web** owns pull request readiness, production deployment, content parity, feeds, search, SEO output, and post-launch validation.
- **Infra** owns Jenkins credentials, Cloudflare redirect rules, and decommissioning of the legacy blog service.
- **Content / CMS** confirms that editor previews and publishing workflows continue to work before the old frontend is retired.

## Task List

### Complete and merge the media migration implementation

- fully qualified name: `ift-ts:web:logos:2026q4-logos-media-migration:merge-readiness`
- owner: Jinho
- status: not started
- start-date: 2026/10/01
- end-date: 2026/10/16

#### Description

Bring [logos-co/logos-web#103](https://github.com/logos-co/logos-web/pull/103) up to date with `develop`, resolve conflicts, and close the remaining review issues that block a safe production release. This includes the rich-content execution boundary, React hook ordering, in-page and footnote links, bounded sitemap fetching, and the reported podcast navigation autoplay behaviour.

Re-run the complete static-export path with production-equivalent content access. Treat a failed content fetch as a build failure where publishing partial or false 404 output would hide an outage. Review the final diff again after conflict resolution because the pull request spans media rendering, search, feeds, image generation, metadata, and global playback state.

#### Deliverables

- PR #103 rebased or merged with current `develop`, with conflicts resolved and no accidental loss of either branch's changes.
- Remaining major review threads resolved with code, tests, or a documented accepted decision.
- Interactive media isolated from the `logos.co` origin or sanitised to an agreed security boundary, with required legacy content verified.
- Footnote and heading fragment links, existing `rel` attributes, and external links behaving correctly.
- Bounded content requests for sitemap and generated media assets, with failures visible to the build.
- Podcast navigation tested for unintended autoplay and player state regressions.
- Passing lint, type checks, tests, production build, and static-export smoke checks on the final PR head.

### Prepare and deploy the production media build

- fully qualified name: `ift-ts:web:logos:2026q4-logos-media-migration:production-deployment`
- owner: Jinho
- status: not started
- start-date: 2026/10/12
- end-date: 2026/10/30

#### Description

Work with Infra to add the Strapi and Simplecast credentials requested in [status-im/infra-sites#168](https://github.com/status-im/infra-sites/issues/168) to the Logos Jenkins job before merging. Confirm that development and production builds read the CMS directly and do not silently fall back to the old public blog API.

Merge and deploy the migration only after the credentialed Jenkins build succeeds. Before any redirect change, verify a representative set of article and podcast pages on `logos.co`, including YouTube, Spotify, Apple Podcasts or direct-audio episodes, rich interactive articles, discussions, search, responsive images, feeds, sitemap entries, metadata, and structured data.

#### Deliverables

- Required Jenkins Secret text credentials configured by Infra without exposing their values in repositories, logs, or roadmap files.
- Successful production build using the intended Strapi and Simplecast integrations.
- PR #103 merged and deployed to `logos.co`.
- Representative article and podcast URLs returning 200 with the correct content, canonical, metadata, and structured data.
- Media search, RSS and Atom feeds, sitemap, generated images, discussion, and podcast playback verified in production.
- A recorded rollback point and named owner for launch-day issues.

### Cut over blog.logos.co redirects and feeds

- fully qualified name: `ift-ts:web:logos:2026q4-logos-media-migration:redirect-cutover`
- owner: Jinho
- status: not started
- start-date: 2026/10/26
- end-date: 2026/11/13

#### Description

Reconcile [status-im/infra-sites#168](https://github.com/status-im/infra-sites/issues/168) with the redirect map in PR #103 before Infra changes Cloudflare. Agree the final first-match rule order and the destination for articles, every podcast show, listing pages, feeds, policy pages, calendar, search, the blog home, and unmatched legacy paths.

Keep the query string on every redirect. Do not redirect CMS preview, API, or asset paths until their consumers have moved. Deploy the application first, verify the destinations, then enable permanent redirects and re-crawl a representative sample.

#### Deliverables

- One approved redirect map shared by Web and Infra, including non-`logos-state` shows and explicit handling for feeds, policy pages, calendar, search, previews, APIs, assets, and unmatched paths.
- Cloudflare 301 rules implemented through Infra issue #168 with query strings preserved.
- Legacy feed paths redirected to working feeds on `logos.co` while retaining stable item identifiers so subscribers do not receive duplicate archive entries.
- Verification that old article and episode URLs return one 301 hop to a 200 destination with a self-referencing canonical.
- Verification that temporary exceptions such as required preview, API, and asset paths still return the expected response until their retirement task is complete.
- A rollback procedure for redirect or feed regressions.

### Remove legacy dependencies and retire the blog frontend

- fully qualified name: `ift-ts:web:logos:2026q4-logos-media-migration:legacy-retirement`
- owner: Jinho
- status: not started
- start-date: 2026/11/09
- end-date: 2026/12/04

#### Description

Inventory the remaining requests to `blog.logos.co` after the public cutover. Replace or deliberately retain every dependency used by local development, CI, CMS draft previews, `/api/*`, `/_next/*`, images, icons, robots, or the legacy sitemap. Give CMS editors a working preview destination before removing the old preview frontend.

When logs and workflow checks show that the legacy frontend is no longer required, coordinate its decommissioning with Infra. This task retires the public blog application, not the Strapi content service still used by `logos.co`.

#### Deliverables

- An owner and disposition for every remaining legacy API, preview, and static-asset path.
- Local, CI, preview, and production builds working without the old public blog fallback.
- CMS draft preview and publishing workflows verified against their post-migration destination.
- Traffic or request-log evidence that no required consumer still uses the legacy frontend.
- Legacy blog frontend decommissioned by Infra, with Strapi and other retained content services explicitly excluded.
- Post-decommission checks covering production pages, builds, previews, feeds, search, and redirects.

### Monitor SEO, content integrity, and operational health

- fully qualified name: `ift-ts:web:logos:2026q4-logos-media-migration:post-cutover-monitoring`
- owner: Jinho
- status: not started
- start-date: 2026/11/02
- end-date: 2026/12/31

#### Description

Monitor the migration after redirects are enabled and again after the legacy frontend is retired. Use Search Console, production crawls, analytics, server or CDN logs, and feed checks to find redirect errors, missing content, indexing regressions, broken embeds, build instability, and playback failures.

Track old URLs moving to redirect status and new `/media` URLs becoming the indexed canonical pages. Fix migration regressions during Q4 and record longer-term content-platform work separately rather than keeping the legacy frontend alive without an explicit reason.

#### Deliverables

- Search Console checks confirming new media URLs are discoverable and old blog URLs are reported as redirected.
- Production crawl covering top article and podcast URLs, redirect chains, canonicals, sitemap membership, structured data, images, and internal links.
- Feed validation showing working endpoints and no archive-wide duplicate delivery.
- Monitoring of 404s, redirect loops, media build failures, search failures, and playback errors, with issues linked and assigned.
- A migration closeout note summarising completed cutover work, retained services, known follow-ups, and final ownership.

## Out of scope for Q4

- Migrating article or podcast content out of Strapi into the `logos-web` content repository or another CMS.
- New editorial, community, or podcast features unrelated to completing and stabilising the migration.
