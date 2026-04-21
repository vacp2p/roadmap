---
title: Status Wallet Extension
tags:
  - "2026q2"
  - "web"
  - "status"
draft: false
description: "Continued development and enhancement of the browser wallet extension focused on trading and investor utility, featuring multi-chain swaps, portfolio management, and real-time token tracking."
---

`ift-ts:web:status:2026q2-status-wallet-extension`

## Description

This commitment involves continued development and enhancement of the Status Wallet Extension, building upon the MVP to add advanced features, improve trading capabilities, and expand the portfolio management functionality. The extension serves as a comprehensive trading wallet and token price tracker for casual and meme coin traders and investors.

The Status Wallet Extension development will support Status' strategic objectives by:
- **Feature Expansion**: Adding advanced trading features, social aspects, and enhanced portfolio management
- **Revenue Optimization**: Improving swap fees, bridge transactions, and subscription models
- **User Experience Enhancement**: Refining UI/UX based on user feedback and market research
- **Market Expansion**: Reaching broader audiences through improved features and marketing integration

## Task List

### Proxy API Rate Limiting

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:proxy-api-rate-limiting`
* owner: unassigned
* status: not started
* start-date: 2026/05/05
* end-date: 2026/05/19

#### Description

Implement proxy API rate limiting to manage API usage and prevent abuse.

#### Deliverables

- Rate limiting implementation
- API quota management
- Rate limit configuration

### QA Defining Test Cases Together

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:qa-defining-test-cases-together`
* owner: unassigned
* status: not started
* start-date: 2026/05/05
* end-date: 2026/05/19

#### Description

Collaborate with QA team to define comprehensive test cases for wallet extension features and functionality.

#### Deliverables

- Test case documentation
- Test plan
- QA collaboration notes

### Value Chart

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:value-chart`
* owner: unassigned
* status: not started
* start-date: 2026/05/12
* end-date: 2026/06/05

#### Description

Implement value chart functionality to display portfolio value over time.

#### Deliverables

- Value chart component
- Chart data integration
- UI implementation

### Hide Small Balances

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:hide-small-balances`
* owner: JulesFiliot
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/21

#### Description

Implement feature to hide small token balances from the wallet view for cleaner UI.

#### Deliverables

- [status-im/status-web#1087](https://github.com/status-im/status-web/pull/1087) feat(wallet/assets-list): add hide assets < 1 USD filter
- [status-im/status-web#1100](https://github.com/status-im/status-web/pull/1100) chore(wallet): change layout & messaging when hide<$1
- Hide small balances functionality
- User preference settings
- UI toggle implementation

### Send NFT

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:send-nft`
* owner: jinhojang6
* status: in progress (90%)
* start-date: 2026/04/01
* end-date: 2026/06/05

#### Description

Implement functionality to send NFTs from the wallet extension.

#### Deliverables

- Send NFT feature
- NFT transfer interface
- Transaction handling

### Multi Account

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:multi-account`
* owner: JulesFiliot
* status: in progress (20%)
* start-date: 2026/04/01
* end-date: 2026/06/19

#### Description

Implement multi-account support to allow users to manage multiple accounts within the wallet extension.

#### Deliverables

- Multi-account functionality
- Account switching interface
- Account management UI
- [status-im/status-web#1114](https://github.com/status-im/status-web/issues/1114) feat(wallet): implement multi-account support

### Multi Wallet

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:multi-wallet`
* owner: JulesFiliot
* status: in progress (90%)
* start-date: 2026/04/01
* end-date: 2026/06/19

#### Description

Implement multi-wallet support to allow users to connect and manage multiple wallets simultaneously.

#### Deliverables

- Multi-wallet functionality
- Wallet connection management
- Wallet switching interface

### Dapp Connection

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:dapp-connection`
* owner: unassigned
* status: not started
* start-date: 2026/06/05
* end-date: 2026/06/19

#### Description

Implement dApp connection functionality to enable wallet extension to connect with decentralized applications.

#### Deliverables

- dApp connection system
- Connection approval interface
- dApp integration support

### Hardware Wallets

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:hardware-wallets`
* owner: jinhojang6
* status: in progress (90%)
* start-date: 2026/04/01
* end-date: 2026/06/26

#### Description

Implement hardware wallet support with QR code-based connection and Keycard Shell integration.

#### Deliverables

- Hardware wallet integration
- QR code connection system
- Keycard Shell support

### Browser and System Notifications

* fully qualified name: `ift-ts:web:status:2026q2-status-wallet-extension:browser-system-notifications`
* owner: jinhojang6
* status: in progress (90%)
* start-date: 2026/04/01
* end-date: 2026/06/26

#### Description

Implement browser and system notifications to alert users of wallet activities and transactions.

#### Deliverables

- Notification system implementation
- Browser notification integration
- System notification support
