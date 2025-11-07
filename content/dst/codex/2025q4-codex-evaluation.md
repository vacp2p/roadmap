---
title: Codex Evaluation
tags:
  - "2025q4"
  - "dst"
  - "codex"
draft: false
description: "Test Codex on each new version or requested feature
and look for regressions,
learn scaling properties and run scaling studies."
---

`vac:dst:codex:2025q4-codex-evaluation`


## Description
Test Codex on each new version or requested feature
and look for regressions if this is required.
Help Codex with testing and benchmarking new features.

### Background

We want to learn specific, actionable information
about Codex's behaviour
and how it is evolving over time
with each new release
and with each thing we are specifically asked to check and test.

We will use a combination of real world testing,
theoretical analysis and experiments.

## Task List

### Codex-in-Status

* fully qualified name: `vac:dst:codex:2025q4-codex-evaluation:codex-in-status`
* owner: Alberto
* status: not started
* start-date: 2025/11/03
* end-date: 2025/11/15

#### Description

Assist the Codex team to check the functionality of
replacing bittorrent usage in status go (in the Community History Service).
Evaluate if the new feature is working as expected by trying to assert:
1. Presence of archive in filesytem
2. Presence of messages in status DB

#### Deliverables
- PRs/Issues/Docs/Reports