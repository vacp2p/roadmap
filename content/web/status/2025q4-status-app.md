---
title: Status App
tags:
  - "2025q4"
  - "web"
  - "status"
draft: false
description: "Supporting continued development of Status App by ensuring web applications, interfaces, and extensions remain functional during native app upgrades, refactoring, and protocol improvements."
---

`vac:web:status:2025q4-status-app`

## Description

This commitment involves supporting the continued development of the Status App by ensuring that web applications, interfaces, and extensions remain functional and compatible during native app upgrades, refactoring, and protocol improvements. As the Status App undergoes significant changes including Waku protocol upgrades, community sharding implementation, and store optimization, the Web unit ensures that all web-based components continue to work seamlessly.

**The Status App web support will support Status' strategic objectives by:**
- **Compatibility Maintenance**: Ensuring web applications and interfaces remain functional during native app upgrades
- **User Experience Continuity**: Preventing disruption to web-based user experiences during development

## Task List

### Upgrade Waku

* fully qualified name: `vac:web:status:2025q4-status-app:upgrade-waku`
* owner: JulesFiliot
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Align Status web surfaces with the upcoming Waku upgrade, covering SDK updates and UI/UX regression checks.

#### Deliverables
- [Unblocking task](https://github.com/status-im/status-web/pull/847)
- [status-im/status-web#875](https://github.com/status-im/status-web/pull/875) adjust shards for communities
- [status-im/community-dapp#119](https://github.com/status-im/community-dapp/pull/119) community shards adjustments

### Community Shards

* fully qualified name: `vac:web:status:2025q4-status-app:community-shards`
* owner: JulesFiliot
* status: in progress (98%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Support the web-facing changes needed for community shards, including shard UI, configuration, and QA cycles.

#### Deliverables
- PRs/Issues/Docs/Reports
