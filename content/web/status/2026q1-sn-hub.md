---
title: SN Hub
tags:
  - "2026q1"
  - "web"
  - "status"
draft: false
description: "Continued development and enhancement of Status Network Hub, the main portal application for Status Network users to access all network features including staking, yield earning, bridging, and public funding pool tracking."
---

`ift-ts:web:status:2026q1-sn-hub`

## Description

This commitment involves continued development and enhancement of the Status Network Hub (SN Hub), building upon the Testnet MVP to add advanced features, improve user experience, and prepare for mainnet launch. The hub serves as the unified interface for all Status Network features and activities.

The SN Hub development will support Status Network's strategic objectives by:
- **Feature Expansion**: Adding advanced features beyond the Testnet MVP including analytics, tokenomics features, and governance tools
- **Mainnet Preparation**: Ensuring all core features are ready for mainnet launch
- **User Experience Enhancement**: Improving onboarding flows, dashboard functionality, and overall usability
- **Network Growth**: Enabling increased participation in staking, liquidity provision, and governance

## Task List

### SDK

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:sdk`
* owner: jkbktl
* status: in progress (5%)
* start-date: 2026/01/01
* end-date: 2026/01/22

#### Description

Implement SDK functionality for claiming Karma, distributing Karma, and authentication.

#### Deliverables

- [status-im/status-web#984](https://github.com/status-im/status-web/pull/984) Fix auth session route (SIWE)
- SDK implementation
- Karma claiming functionality
- Karma distribution functionality
- Authentication system

### Proxy API

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:proxy-api`
* owner: JulesFiliot
* status: in progress (80%)
* start-date: 2026/01/01
* end-date: 2026/01/22

#### Description

Set up proxy API infrastructure including Status RPC proxy, Status Market proxy, with dedicated credentials and quota management.

#### Deliverables

- [TVL on VPN debugging](https://github.com/status-im/status-web/issues/902)
- [status-im/eth-rpc-proxy#102](https://github.com/status-im/eth-rpc-proxy/pull/102) Testing dev Status RPC proxy and requesting cache clearance
- [status-im/status-web#1001](https://github.com/status-im/status-web/pull/1001) fix: rpc mainnet
- Configured a bot protection bypass on Vercel for VPN access
- Status RPC proxy implementation
- Status Market proxy implementation
- Credential and quota management system

### Depositing

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:depositing`
* owner: jinhojang6
* status: in progress (10%)
* start-date: 2026/01/01
* end-date: 2026/01/15

#### Description

Implement depositing functionality with GUSD vault integration.

#### Deliverables

- [status-im/status-web#1007](https://github.com/status-im/status-web/pull/1007) chore: update vault cards
- [status-im/status-web#1002](https://github.com/status-im/status-web/pull/1002) chore: add generic points to modal
- [status-im/status-web#999](https://github.com/status-im/status-web/pull/999) chore: update order of the vaults
- [status-im/status-web#994](https://github.com/status-im/status-web/pull/994) feat: add feedback link to mobile
- [status-im/status-web#992](https://github.com/status-im/status-web/pull/992) feat(wallet): enable GUSD vault
- [Change order of the vaults](https://github.com/status-im/status-web/pull/969)
- [status-im/status-web#1010](https://github.com/status-im/status-web/pull/1010) feat(hub): handle wallet can't switch chain error with a dialog
- Depositing interface
- GUSD vault integration
- Transaction handling

### Karma Evolution

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:karma-evolution`
* owner: jkbktl
* status: in progress (5%)
* start-date: 2026/01/08
* end-date: 2026/01/29

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

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:nft-evolution`
* owner: JulesFiliot
* status: not started
* start-date: 2026/01/08
* end-date: 2026/01/31

#### Description

Implement NFT evolution system based on contracts and Karma integration.

#### Deliverables

- NFT evolution system
- Contract integration
- Karma-based NFT logic

### Backend

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:backend`
* owner: jinhojang6
* status: in progress (5%)
* start-date: 2026/01/15
* end-date: 2026/02/28

#### Description

Implement backend functionality for leaderboard and app discovery features.

#### Deliverables

- Leaderboard backend
- App discovery backend
- API endpoints

### QA

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:qa`
* owner: jkbktl
* status: in progress (10%)
* start-date: 2026/01/15
* end-date: 2026/01/29

#### Description

Define test cases for QA testing of SN Hub features and functionality.

#### Deliverables

- [status-im/status-web#1029](https://github.com/status-im/status-web/pull/1029) chore: update docs
- Test case documentation
- Test plan
- QA reports
- [status-im/status-web#933](https://github.com/status-im/status-web/issues/933) Requesting QA help with tests

### Selfhosting

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:selfhosting`
* owner: JulesFiliot
* status: in progress (25%)
* start-date: 2026/01/15
* end-date: 2026/01/29

#### Description

Set up self-hosting infrastructure and deployment processes for SN Hub.

#### Deliverables

- Self-hosting configuration
- Deployment documentation
- Infrastructure setup
- [status-im/status-web#934](https://github.com/status-im/status-web/issues/934) Setting up self-hosting

### Translations

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:i18n`
* owner: jinhojang6
* status: in progress (5%)
* start-date: 2026/01/22
* end-date: 2026/02/05

#### Description

Implement internationalization (i18n) support for SN Hub to enable multi-language functionality.

#### Deliverables

- i18n implementation
- Translation files
- Language selector
- [status-im/status-web#892](https://github.com/status-im/status-web/pull/892) Releasing translated hub
- [status-im/status-web#889](https://github.com/status-im/status-web/pull/889) Releasing translated website

### SEO

* fully qualified name: `ift-ts:web:status:2026q1-sn-hub:seo`
* owner: jkbktl
* status: in progress (5%)
* start-date: 2026/01/22
* end-date: 2026/02/05

#### Description

Implement SEO optimization for SN Hub to improve search engine visibility and discoverability.

#### Deliverables

- [Redirect `/dashboard` to `/`](https://github.com/status-im/status-web/pull/970)
- [status-im/status-web#998](https://github.com/status-im/status-web/pull/998) Update the sitemap and metadata
- [status-im/status-web#991](https://github.com/status-im/status-web/pull/991) Implement technical SEO improvements with i18n support
- SEO implementation
- Meta tags and structured data
- SEO audit and optimization report
