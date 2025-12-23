---
title: Maintaining existing Status Network L2 smart contracts
tags:
  - "2025q4"
  - "sc"
  - "status-l2"
draft: false
description: Maintain and improve existing Status Network L2 smart contracts as requested.
---

`vac:sc:status-l2:2025q4-maintaining-status-l2-contracts`

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

* fully qualified name: `vac:sc:status-l2:2025q4-maintaining-status-l2-contracts:maintenance`
* owner: r4bbit
* status: in progress (60%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Handle inbound maintenance requests for deployed Status L2 contracts, including bug fixes and minor enhancements.

#### Deliverables
- [Cyfrin/audit-2025-12-statusl2#35](https://github.com/Cyfrin/audit-2025-12-statusl2/issues/35)
- [status-im/status-network-monorepo#121](https://github.com/status-im/status-network-monorepo/pull/121) fix(CI): ignore asm-keccak256 rule in RLN contract
- [status-im/status-network-monorepo#118](https://github.com/status-im/status-network-monorepo/pull/118) chore: make the linter happy
- [status-im/status-network-monorepo#117](https://github.com/status-im/status-network-monorepo/pull/117) feat(IRewardDistributor): introduce `isPaused()`
- [status-im/status-network-monorepo#115](https://github.com/status-im/status-network-monorepo/pull/115) docs: clarify loss of Karma when removing distributors
- [status-im/status-network-monorepo#114](https://github.com/status-im/status-network-monorepo/pull/114) fix(DeployProtocol): ensure simple Karma distributor is whitelisted
- [status-im/status-network-monorepo#113](https://github.com/status-im/status-network-monorepo/pull/113) chore(InitializeKarmaTiers): update script with latest tier values
- [status-im/status-network-monorepo#112](https://github.com/status-im/status-network-monorepo/pull/112) fix(StakeManager): prevent migrating to non-empty vaults
- [status-im/status-network-monorepo#111](https://github.com/status-im/status-network-monorepo/pull/111) fix(KarmaAirdrop): fix potential attack that prevents account from claiming
- [status-im/status-network-monorepo#109](https://github.com/status-im/status-network-monorepo/pull/109) Ensure Emergency Exit and Leave try-catch blocks work even in missing functions or wrong return types
- [status-im/status-network-monorepo#105](https://github.com/status-im/status-network-monorepo/pull/105) prohibit StakeVault to migrate to a StakeVault which has left
- [status-im/status-network-monorepo#104](https://github.com/status-im/status-network-monorepo/pull/104) Remove MP_APY
- [status-im/status-network-monorepo#96](https://github.com/status-im/status-network-monorepo/pull/96) fix(KarmaAirdrop): ensure claiming isn't possible during pause
- [status-im/status-network-monorepo#95](https://github.com/status-im/status-network-monorepo/pull/95) refactor(MultiplierPointsMath): round MPs up when users unstake
- [status-im/status-network-monorepo#93](https://github.com/status-im/status-network-monorepo/pull/93) refactor(KarmaTiers): remove unnecessary constructor
- [status-im/status-network-monorepo#92](https://github.com/status-im/status-network-monorepo/pull/92) fix(Karma): don't overslash in cases balances are < MIN_SLASH_AMOUNT
- [status-im/status-network-monorepo#88](https://github.com/status-im/status-network-monorepo/pull/88) feat(StakeManager)!: introduce a per user vault limit
- [status-im/status-network-monorepo#107](https://github.com/status-im/status-network-monorepo/pull/107) audit fixes
- [status-im/status-network-monorepo#103](https://github.com/status-im/status-network-monorepo/pull/103) audit fixes
- [status-im/status-network-monorepo#84](https://github.com/status-im/status-network-monorepo/pull/84) audit fixes
- [StakeManager: Allow leave while paused](https://github.com/status-im/status-network-monorepo/pull/87)
- [StakeVault: Disallow migrate to self](https://github.com/status-im/status-network-monorepo/pull/86)
- [status-im/status-network-monorepo#89](https://github.com/status-im/status-network-monorepo/pull/89) rename onlySlasher modifier
- [status-im/status-network-monorepo#85](https://github.com/status-im/status-network-monorepo/pull/85) block vault registration with incorrect owners
- [fix(KarmaTiers): allow minKarma == maxKarma in tier config](https://github.com/status-im/status-network-monorepo/pull/66)
- [docs(README): streamline repository readme](https://github.com/status-im/status-network-monorepo/pull/65)
- [refactor: use `forge lint` over `solhint`](https://github.com/status-im/status-network-monorepo/pull/63)
- [chore: extend deploy protocol script with SimpleKarmaDistributor](https://github.com/status-im/status-network-monorepo/pull/62)
- Deployed new SimpleKarmaDistributor instances for live testing
- Fixed the SimpleKarmaDistributor deployment script to initialize distributor parameters correctly
