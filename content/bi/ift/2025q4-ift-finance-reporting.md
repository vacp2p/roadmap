---
title: IFT Finance Reporting
tags:
  - "2025q4"
  - "bi"
  - "ift"
draft: false
description: Build wallet balance and activity reports for the IFT finance team.
---

`vac:bi:ift:2025q4-ift-finance-reporting`

## Description

Produce a consolidated report of wallet balances and transactional activity so the finance team can reconcile treasury movements without pulling multiple dashboards.

## Task List

### Wallet balance & activity report

* fully qualified name: `vac:bi:ift:2025q4-ift-finance-reporting:wallet-balance-report`
* owner: c2000bzh
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Model the wallet balances, inflows, and outflows, then expose the data through a sharable report for finance stakeholders.

#### Deliverables

- Drafted the wallet balances + activities dataset combining Airbyte pulls with manual annotations.
- Began assembling the Superset workbook that finance can review for the November close.
