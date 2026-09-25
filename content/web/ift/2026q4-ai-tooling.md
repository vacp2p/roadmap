---
title: AI Tooling
tags:
  - "2026q4"
  - "web"
  - "ift"
draft: false
description: Build and maintain the team's shared AI workflow tooling; ai-review, its ai-auto-fix companion, and ai-docs-sync.
---

`ift-ts:web:ift:2026q4-ai-tooling`

## Description

Three tools are in scope: [ai-review](https://github.com/acid-info/ai-review), already consumed by `status-im/status-web`, `logos-co/logos-web`, and `acid-info/admin-acid.logos.co`; an **ai-auto-fix** companion that turns accepted ai-review findings into a patch, not yet started; and [ai-docs-sync](https://github.com/acid-info/ai-docs-sync), in development.
All three ship as reusable GitHub workflows pinned to `@v1`, with zero npm dependencies, so a tool or model change is one edit in the shared repository rather than one per consumer.
Human approval before merge stays a hard requirement for every tool here.

## Task List

### ai-review maintenance and tuning

* fully qualified name: `ift-ts:web:ift:2026q4-ai-tooling:ai-review`
* owner: JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Maintain [acid-info/ai-review](https://github.com/acid-info/ai-review) as the shared PR reviewer for `logos-co`, `status-im`, and `acid-info` repositories.
Keep the dual-model review plus synthesis pipeline reliable as provider APIs and models change, tune per-repository context and guideline files to cut false positives, and refine diff packing, path filtering, and severity thresholds.
Keep the degraded paths honest: a single-model review when one provider is down, a local merge when synthesis fails, and a posted body that says the review was partial.
Onboard remaining Web repositories and keep the `@v1` tag stable for consumers.

#### Deliverables

- PRs in `acid-info/ai-review` for model updates, prompt and threshold tuning, and pipeline fixes.
- Repository-specific guideline and config files in consumer repositories.
- Additional consumer repositories onboarded via `.github/workflows/ai-review.yml`.
- A short assessment of signal versus noise, drawn from reviewed PRs, with the tuning changes it drove.

### ai-auto-fix companion

* fully qualified name: `ift-ts:web:ift:2026q4-ai-tooling:ai-auto-fix`
* owner: JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Build an **ai-auto-fix** companion to ai-review that takes review findings and produces a patch the author can accept, rather than leaving every finding as manual follow-up work.
Nothing exists yet, so the task starts from specification: which finding severities and categories are eligible, how a fix is requested (a comment command on the PR, or opt-in per finding), how the patch is delivered (a commit pushed to the PR branch, or a suggested-change comment), and what the tool must refuse to touch.
Reuse the ai-review pipeline's shape -- reusable workflow, zero npm dependencies, Node 22 `fetch`, pinned `@v1` -- and keep every produced change inside normal PR review with no branch-protection bypass.

#### Deliverables

- Written specification covering eligible findings, trigger mechanism, patch delivery, and refusal rules.
- Prototype workflow producing patches against real ai-review findings on Web repositories.
- Documented guardrails: disallowed change types, secret handling, and required human approval before merge.

### ai-docs-sync

* fully qualified name: `ift-ts:web:ift:2026q4-ai-tooling:ai-docs-sync`
* owner: JulesFiliot
* status: not started
* start-date: 2026/10/01
* end-date: 2026/12/31

#### Description

Finish [acid-info/ai-docs-sync](https://github.com/acid-info/ai-docs-sync), which keeps a repository's documentation in step with its code by triaging each push, rewriting affected docs with one model, checking the rewrite with a second, and running mechanical gates.

#### Deliverables

- Merged publishing stage: rolling branch and PR, cursor move, generated PR body, with unit tests.
- End-to-end runs on a real repository, including unmerged-edit carry-forward and collapsed-push handling.
- `v1` tag cut and the README status banner removed.
- First consumer repository onboarded via `.github/workflows/docs-sync.yml`, with the resulting docs PRs linked.
