---
title: SN Hub
tags:
  - "2026q2"
  - "web"
  - "status"
draft: false
description: "Continued development and enhancement of Status Network Hub, the main portal application for Status Network users to access all network features including staking, yield earning, bridging, and public funding pool tracking."
---

`ift-ts:web:status:2026q2-sn-hub`

## Description

This commitment involves continued development and enhancement of the Status Network Hub (SN Hub), building upon the Testnet MVP to add advanced features, improve user experience, and prepare for mainnet launch. The hub serves as the unified interface for all Status Network features and activities.

The SN Hub development will support Status Network's strategic objectives by:
- **Feature Expansion**: Adding advanced features beyond the Testnet MVP including analytics, tokenomics features, and governance tools
- **Mainnet Preparation**: Ensuring all core features are ready for mainnet launch
- **User Experience Enhancement**: Improving onboarding flows, dashboard functionality, and overall usability
- **Network Growth**: Enabling increased participation in staking, liquidity provision, and governance

## Task List

### SDK

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:sdk`
* owner: unassigned
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/22

#### Description

Implement SDK functionality for claiming Karma, distributing Karma, and authentication.

#### Deliverables

- SDK implementation
- Karma claiming functionality
- Karma distribution functionality
- Authentication system

### Proxy API

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:proxy-api`
* owner: unassigned
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/22

#### Description

Set up proxy API infrastructure including Status RPC proxy, Status Market proxy, with dedicated credentials and quota management.

#### Deliverables

- Configured a bot protection bypass on Vercel for VPN access
- Status RPC proxy implementation
- Status Market proxy implementation
- Credential and quota management system

### Karma Evolution

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:karma-evolution`
* owner: unassigned
* status: not started
* start-date: 2026/04/08
* end-date: 2026/04/29

#### Description

Implement Karma evolution system including Karma progress tracking and transaction allowance management.

#### Deliverables

- [Implement Karma button in the top-nav](https://github.com/status-im/status-web/pull/968)
- Restricted Karma hooks to Status Network Sepolia
- Persisted Karma balance across network switches
- Karma progress system
- Transaction allowance functionality
- Evolution tracking

### NFT Evolution

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:nft-evolution`
* owner: unassigned
* status: not started
* start-date: 2026/04/08
* end-date: 2026/04/30

#### Description

Implement NFT evolution system based on contracts and Karma integration.

#### Deliverables

- NFT evolution system
- Contract integration
- Karma-based NFT logic

### Backend

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:backend`
* owner: unassigned
* status: not started
* start-date: 2026/04/15
* end-date: 2026/05/28

#### Description

Implement backend functionality for leaderboard and app discovery features.

#### Deliverables

- Leaderboard backend
- App discovery backend
- API endpoints

### QA

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:qa`
* owner: unassigned
* status: not started
* start-date: 2026/04/15
* end-date: 2026/04/29

#### Description

Define test cases for QA testing of SN Hub features and functionality.

#### Deliverables

- Test case documentation
- Test plan
- QA reports

### SEO

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:seo`
* owner: unassigned
* status: not started
* start-date: 2026/04/22
* end-date: 2026/05/05

#### Description

Implement SEO optimization for SN Hub to improve search engine visibility and discoverability.

#### Deliverables

- [Redirect `/dashboard` to `/`](https://github.com/status-im/status-web/pull/970)
- SEO implementation
- Meta tags and structured data
- SEO audit and optimization report

### Fund allocation

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:fund-allocation`
* owner: unassigned
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description

Ship **fund allocation** and related flows in SN Hub per design ([Figma — overview](https://www.figma.com/design/1XbZL2WrTG5DqJO8DovE0H/Website----status.network?node-id=7606-23298&m=)):

**Unlock / entry**
- Input receiver address; “Learn more” article; **sign**; **ENS resolver** where specified.

**Withdraw / allocate funds**  
([Figma](https://www.figma.com/design/1XbZL2WrTG5DqJO8DovE0H/Website----status.network?node-id=7610-23923&m=dev))
- **Provide liquidity** into the **native DEX pool**
- **Lend SNT, mint USF** into the **native privacy protocol**; **withdraw**; “Learn more” articles; **sign**; behaviour **varies by vault**

**Claim rewards**  
([Figma](https://www.figma.com/design/1XbZL2WrTG5DqJO8DovE0H/Website----status.network?node-id=7610-23897&m=dev))
- **Redirect to external dapp** for **SNT** and **LINEA** rewards

#### Deliverables

- Implemented UI and transaction flows for allocate/withdraw/liquidity/lend-mint paths per vault rules
- ENS/receiver/sign flows wired as in spec
- Rewards path with external dapp handoff for SNT and LINEA
- Linked “Learn more” content or routes as designed

### Hoodi migration

* fully qualified name: `ift-ts:web:status:2026q2-sn-hub:hoodi-migration`
* owner: Felicio
* status: in progress (25%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

**What:** Follow [Status Network Hoodi E2E deployment (Notion)](https://www.notion.so/Status-Network-Hoodi-E2E-Deployment-Team-Tagged-2e98f96fb65c803c8bccdf05468a51e6): add **Status Hoodi** chain support and **SNT staking** updates for the new testnet.

**Contracts / staking:** Align with **StakeManager** breaking changes ([status-network-contracts CHANGELOG](https://github.com/status-im/status-network-monorepo/blob/8caa3adec019deea941eee358ced73c8158ee377/status-network-contracts/CHANGELOG.md)): adopt updated interfaces (**`registerVault()`**, **`updateGlobalState()`**); remove reliance on dropped APIs (**`totalMaxMP()`**, **`totalMPAccrued()`**); apply **vault number limit** validation and **`maxVaultsPerUser`**; **replace Karma contract addresses**.

**Product / UX:** **Gas quote UI** complete; **temporarily flag** unmigrated apps; **update the status.network banner** for **testnet v2**.

**Where:** Primarily [`apps/hub`](https://github.com/status-im/status-web/tree/main/apps/hub). Coordinate with [`apps/website`](https://github.com/status-im/status-web/tree/main/apps/website) where banner or shared surface applies ([status-web](https://github.com/status-im/status-web)).

#### Deliverables

- Hoodi chain wired in hub flows that apply; staking UI and contract integrations match new StakeManager / Karma addresses
- Vault limits and state calls match new interfaces; no references to removed getters
- Gas quote UX shipped; unmigrated surfaces flagged; banner reflects testnet v2 where this commitment coordinates website changes
- [status-im/status-web#1145](https://github.com/status-im/status-web/pull/1145) update copy for banners
