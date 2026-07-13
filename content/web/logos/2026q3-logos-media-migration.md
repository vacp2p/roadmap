---
title: "Logos Media: Blog Migration"
tags:
  - "2026q3"
  - "web"
  - "logos"
draft: false
description: "Move blog.logos.co onto logos.co/media. Build native article and podcast detail pages that keep everything the blog does today (HTML content, footnotes, table of contents, discussion, related articles, same-author lists, and the sticky podcast player with YouTube progress sync), then redirect the old blog URLs to the new /media routes."
---

`ift-ts:web:logos:2026q3-logos-media-migration`

## Description

We want to fold the standalone blog at [blog.logos.co](https://blog.logos.co) into the main site under [logos.co/media](https://logos.co/media). The blog runs today on its own repo, [acid-info/logos-press-engine](https://github.com/acid-info/logos-press-engine), which is where all the current article and podcast features live and where we'll be porting from.

The `/media` landing page already exists on `logos-co/logos-web` and pulls its data from the blog through the blog-engine (`BLOG_ORIGIN = https://blog.logos.co`, `/api/search`). The catch is that the actual reading experience still lives on `blog.logos.co`: article and podcast detail pages just link back out to the old site.

This commitment builds those detail pages natively on `logos.co/media` with the same features the blog has now, then redirects the old blog URLs to the new ones so existing links, bookmarks, and search rankings keep working.

Here's the URL mapping we're aiming for:

- `https://blog.logos.co/article/<slug>` becomes `https://logos.co/media/articles/<slug>`
- `https://blog.logos.co/podcasts/<series>/<slug>` becomes `https://logos.co/media/podcasts/<series>/<slug>`

**What changes**

- Article and podcast detail pages are served from `logos-co/logos-web` under `/media/*`, instead of from `blog.logos.co`.
- The `/media` landing cards and internal links point at the new in-site routes rather than out to `blog.logos.co`.
- `blog.logos.co/article/*` and `blog.logos.co/podcasts/*` become 301 redirects to the matching `/media` route (owned by infra).

**What stays**

- Everything a reader gets on `blog.logos.co` today: interactive HTML/CSS/JS blog content, footnotes, table of contents, Discussion, Related Articles, From The Same Authors, and the podcast sticky bottom player with its YouTube progress sync.
- The existing `/media` landing page layout and its sections (articles, podcasts, broadcast).
- The content source of truth: the existing Strapi CMS, reused as-is. We adapt the new frontend to consume it; we don't re-model the content or swap CMS this quarter.

**Why this is its own quarter**

- There are two full detail-page templates to build (article and podcast), and each one carries several sub-features. Every one of them is a couple of weeks of build plus parity QA.
- The podcast sticky player with YouTube sync is stateful and spans routes, so it needs its own testing pass on both mobile and desktop.
- The redirect layer is a coordination task with infra ([status-im/infra-sites](https://github.com/status-im/infra-sites)), and it has SEO consequences (canonicals, sitemaps, indexing) that have to land at the same time as the new pages.

**Risks**

- **Content pipeline.** The blog content lives in Strapi as interactive HTML/CSS/JS, footnotes, and heading anchors. We're reusing Strapi as-is, so the work is confirming the new frontend can pull a single post's full content from the existing Strapi API and render it faithfully. Worth checking early that Strapi returns the complete post body (not just the search summaries the `/media` landing uses today), since that gates the detail template.
- **Feature drift.** Discussion, Related Articles, and From The Same Authors probably lean on blog-side services (a comments backend, tag and author queries). We have to pin down each data source before we can port them.
- **YouTube sync.** The podcast player keeps a progress bar in step with the embedded YouTube player through the IFrame Player API. Autoplay rules, seeking, and mobile background-audio limits all need deliberate handling and test coverage.
- **SEO cutover.** Redirects, canonicals, and sitemaps have to ship together with the new pages. If they don't, we risk duplicate content and lost rankings for the window where both URLs still resolve.

**Coordination**

- **Infra** ([status-im/infra-sites](https://github.com/status-im/infra-sites)) owns the `blog.logos.co` to `logos.co/media` redirect rules and any DNS or routing changes.
- **Content / CMS.** We keep the existing Strapi CMS as-is (same content, same API) and adapt the new frontend to consume it. No content re-modelling this quarter; the work is wiring the `/media` detail pages to what Strapi already serves for content, footnotes, authors, and related-post queries.

## Task List

### Article detail page: content, footnotes, table of contents

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:article-detail-core`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Build the native article detail route at `logos.co/media/articles/<slug>` on `logos-co/logos-web`. Render the full article HTML the way the blog does (typography, images, embeds, code blocks, blockquotes), with working footnotes (in-text markers linked to the footnote list and back again) and a table of contents built from the headings, with anchor links and active-section highlighting as you scroll.

Content is fetched from the existing Strapi CMS. Handle loading, not-found (404), and error states. Render on the server so the first paint already includes the content and the TOC, and set per-slug metadata.

#### Deliverables

- `/media/articles/[slug]` route rendering the article HTML faithfully
- Footnotes: in-text markers, footnote list, and links running both directions
- Table of contents from the headings, with anchor links and active-section highlighting
- Server-rendered metadata (title, description, canonical, OG/Twitter) per article
- 404, error, and empty states
- A short note on where the content comes from (endpoint or export) and any transform applied

### Article detail page: Discussion, Related Articles, From The Same Authors

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:article-detail-secondary`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Port the supporting sections of the article page. That's **Discussion** (comments and engagement as they work on the blog today; we need to confirm the backend and whether we keep it, embed it, or replace it), **Related Articles** (queried by tag or topic), and **From The Same Authors** (queried by author). Match the layout, empty states, and card styling to the current blog and the existing `/media` sections.

#### Deliverables

- Discussion section wired to its confirmed data source, or a documented decision if we defer or replace it
- Related Articles block (tag/topic query) using the blog's card layout
- From The Same Authors block (author query) with empty-state handling
- A data-source note per section (endpoint, query params, caching)

### Podcast detail page: layout, YouTube embed, metadata

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:podcast-detail-core`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Build the native podcast detail route at `logos.co/media/podcasts/<series>/<slug>` on `logos-co/logos-web`. Render the episode metadata (series, title, guest, description, show notes, publish date), the YouTube embed, and any transcript or notes the blog shows today. Server-render the metadata per episode, and handle 404, error, and empty states.

#### Deliverables

- `/media/podcasts/[series]/[slug]` route with the episode layout and show notes
- Embedded YouTube player set up so the sticky player (below) can drive it
- Server-rendered metadata (title, description, canonical, OG/Twitter) per episode
- 404, error, and empty states

### Podcast sticky player: bottom bar and YouTube progress sync

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:podcast-player`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Rebuild the sticky bottom player from the current podcast experience: play/pause, seek, current time and duration, and a progress bar that stays in step with the embedded YouTube player. Drive it through the YouTube IFrame Player API so play, pause, and seek work in both directions and the time keeps updating. The player should stick around as you navigate within the podcast section, the way the blog does it now, and it should behave sensibly with autoplay rules and on mobile.

#### Deliverables

- Sticky bottom player with play/pause, seek, elapsed and duration, and a progress bar
- Two-way sync between the progress bar and the YouTube IFrame player (play, pause, seek, time updates)
- Autoplay rules and mobile behaviour handled and written down
- Player state that persists across podcast-section navigation, matching the current behaviour
- A test pass on desktop and mobile (Chrome, Safari, Firefox)

### Point the /media landing and internal links at the new routes

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:internal-links`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Repoint the `/media` landing cards, and any in-site links that currently go to `blog.logos.co/article/*` or `blog.logos.co/podcasts/*`, at the new `/media/*` routes. Update the blog-engine mapping so those hrefs resolve inside the site. Leave genuinely external references (like the genealogy links) pointing out where they're meant to.

#### Deliverables

- `/media` landing cards linking to `/media/articles/*` and `/media/podcasts/*`
- Updated blog-engine href mapping, with the tests adjusted to match
- An audit of the remaining `blog.logos.co` links in `logos-web`, with a reason for each one we keep external

### Redirects: blog.logos.co to logos.co/media (with infra)

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:redirects-infra`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Work with **infra** ([status-im/infra-sites](https://github.com/status-im/infra-sites)) to add 301 redirects from the old blog URLs to the new `/media` routes:

- `blog.logos.co/article/<slug>` to `logos.co/media/articles/<slug>`
- `blog.logos.co/podcasts/<series>/<slug>` to `logos.co/media/podcasts/<series>/<slug>`

Produce the full slug and path mapping, decide how to handle anything that isn't a clean one-to-one (index pages, tag pages, older URLs), and sequence the redirect rollout with the go-live of the new pages so we're never serving the same content from both.

#### Deliverables

- A complete redirect map (article and podcast paths, plus decisions for index, tag, and legacy URLs)
- 301 rules implemented in the infra or routing layer, with the infra PR linked
- A rollout note (new pages live first, then redirects on) agreed with infra
- A spot-check re-crawl confirming the top URLs land on the new pages

### SEO cutover: canonicals, sitemap, structured data

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:seo-cutover`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Make the new `/media/*` pages the canonical, indexable home for this content. That means self-referencing canonicals on the new pages, `Article` and `PodcastEpisode` structured data, and sitemap entries for the new routes. Confirm the old blog URLs drop out of the index in favour of the redirects, and validate with Search Console and rich-results tooling.

#### Deliverables

- Canonicals plus `Article` and `PodcastEpisode` JSON-LD on the new detail templates
- Sitemap updated with `/media/articles/*` and `/media/podcasts/*`
- Validation (Search Console coverage and rich-results checks) on a sample
- A short note confirming the old URLs are de-indexed via the redirects

### Parity QA and go-live

* fully qualified name: `ift-ts:web:logos:2026q3-logos-media-migration:parity-qa`
* owner: jinhojang6
* status: not started
* start-date: 2026/07/07
* end-date: 2026/07/31

#### Description

Do a side-by-side check between `blog.logos.co` and the new `/media` pages across a representative set of articles and episodes: content fidelity, footnotes, TOC, Discussion, the Related and Same-author blocks, the podcast player and its YouTube sync, metadata and OG tags, and responsive behaviour. Close the gaps, then coordinate go-live with the redirect and SEO tasks.

#### Deliverables

- The parity checklist run against a sample of articles and podcasts, with issues logged and fixed
- Cross-browser and mobile sign-off
- Go-live coordinated with the redirects (`redirects-infra`) and the SEO cutover (`seo-cutover`)
- A short post-migration check (old URLs return 301, new pages return 200 with the right canonical)

## Out of scope for Q3 (stretch / Q4+)

- A full CMS migration of the blog content into the logos-web content stack. This quarter keeps the existing source of truth and just builds the presentation and the redirects.
- Blog search on `/media`. That's tracked separately.
- Decommissioning the `blog.logos.co` hosting once the redirects have settled.
