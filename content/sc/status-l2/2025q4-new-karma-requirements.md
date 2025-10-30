---
title: Status Network Karma Enhancements
tags:
  - "2025q4"
  - "sc"
  - "status-l2"
draft: false
description: Extend the Karma protocol with distributed slashing safeguards for the new quarter.
---

`vac:sc:status-l2:2025q4-new-karma-requirements`

## Description

Build on the Q3 Karma work by introducing distributed slashing improvements that prevent race conditions and support secure execution during reveal time.

## Task List

### Distributed slashing safeguards

* fully qualified name: `status:2025q4-new-karma-requirements:distributed-slashing`
* owner: andreacavallini
* status: in progress (35%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Design and implement mitigations that queue slash commitments to prevent front-running and improve the robustness of the distributed slashing flow.

#### Deliverables

- [PR 56: queue slash commitments to avoid front-running](https://github.com/status-im/status-network-monorepo/pull/56).
- Open research notes on slashing race-condition solutions ([SlashingKarmaLeader.sol](https://github.com/status-im/status-network-monorepo/blob/slash-karma-leader/status-network-contracts/src/rln/SlashingKarmaLeader.sol)).
