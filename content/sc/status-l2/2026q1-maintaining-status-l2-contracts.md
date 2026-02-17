---
title: Maintaining existing Status Network L2 smart contracts
tags:
  - "2026q1"
  - "sc"
  - "status-l2"
draft: false
description: Maintain and improve existing Status Network L2 smart contracts as requested.
---

`ift-ts:sc:status-l2:2026q1-maintaining-status-l2-contracts`

Maintain and improve existing Status Network L2 smart contracts as requested.

## Description

Smart contracts for Status Network L2 that have already been implemented and deployed might still need maintenance.
This includes upgrading systems,
fixing bugs that might be discovered after the contracts have been deployed,
and implementing minor enhancements that don't fall under specific commitments.

The Smart Contracts team commits to providing maintenance service for existing Status Network L2 smart contracts,
such as:

- Karma Token
- Karma Airdrop
- Staking and reward distribution contracts

## Task List

There are no concrete tasks associated to this commitment.
As requests come in,
they will be addressed by our team.

### Contract maintenance (recurring)

* fully qualified name: `ift-ts:sc:status-l2:2026q1-maintaining-status-l2-contracts:maintenance`
* owner: r4bbit
* status: in progress (5%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Handle inbound maintenance requests for deployed Status L2 contracts, including bug fixes and minor enhancements.

#### Deliverables
- [status-im/status-network-token-v2#7](https://github.com/status-im/status-network-token-v2/pull/7) chore: add deployment config for hoodi
- [status-im/status-network-monorepo#138](https://github.com/status-im/status-network-monorepo/pull/138) docs: add admin guide to contracts documentation
- [status-im/status-network-monorepo#128](https://github.com/status-im/status-network-monorepo/pull/128) chore: update smart contracts changelog
- [status-im/status-network-monorepo#125](https://github.com/status-im/status-network-monorepo/pull/125) refactor(StakeVault): make use of ExcessivelySafeCall
