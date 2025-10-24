---
title: Finance Wallet monitoring
tags:
  - "2025q4"
  - "bi"
  - "finance"
draft: false
description: Monitoring Wallets activity for Finance team
---

`vac:bi:finance:2025q3-finance-wallets-monitoring`


## Description

It is a continuous task to extracts and monitore Crypto wallets for the Finance team.

## Task List

### Extract Ethereum base wallets

* fully qualified name: `vac:bi:finance:2025q3-finance-wallets-extractions`
* owner: apentori
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

https://github.com/status-im/data-docs/issues/83

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables

* [Airbyte connector to extract wallets informations](https://github.com/status-im/airbyte-custom-connector/commit/ea693a01f266b714677d7aadb6633102ab07cc1a)
* [Dashboard PoC](https://superset.bi.status.im/superset/dashboard/wallets)

### Improve Dashboard


* fully qualified name: `vac:bi:finance:2025q3-finance-wallets-visualization`
* owner: 
* status: wait for information 
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Continue on the [issue](https://github.com/status-im/data-docs/issues/83), waiting for finance feedback.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables

* Adapted visualization dashboard
* Alerting system
