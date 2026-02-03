---
title: Status Wallet Extension
tags:
  - "2026q1"
  - "web"
  - "status"
draft: false
description: "Continued development and enhancement of the browser wallet extension focused on trading and investor utility, featuring multi-chain swaps, portfolio management, and real-time token tracking."
---

`ift-ts:web:status:2026q1-status-wallet-extension`

## Description

This commitment involves continued development and enhancement of the Status Wallet Extension, building upon the MVP to add advanced features, improve trading capabilities, and expand the portfolio management functionality. The extension serves as a comprehensive trading wallet and token price tracker for casual and meme coin traders and investors.

The Status Wallet Extension development will support Status' strategic objectives by:
- **Feature Expansion**: Adding advanced trading features, social aspects, and enhanced portfolio management
- **Revenue Optimization**: Improving swap fees, bridge transactions, and subscription models
- **User Experience Enhancement**: Refining UI/UX based on user feedback and market research
- **Market Expansion**: Reaching broader audiences through improved features and marketing integration

## Task List

### Proxy API Rate Limiting

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:proxy-api-rate-limiting`
* owner: jinhojang6
* status: not started
* start-date: 2026/02/05
* end-date: 2026/02/19

#### Description

Implement proxy API rate limiting to manage API usage and prevent abuse.

#### Deliverables

- Rate limiting implementation
- API quota management
- Rate limit configuration
- [status-im/status-web#855](https://github.com/status-im/status-web/issues/855) Using the browser extension does not work while VPN is turned on

### QA Defining Test Cases Together

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:qa-defining-test-cases-together`
* owner: jkbktl
* status: not started
* start-date: 2026/02/05
* end-date: 2026/02/19

#### Description

Collaborate with QA team to define comprehensive test cases for wallet extension features and functionality.

#### Deliverables

- Test case documentation
- Test plan
- QA collaboration notes
- [status-im/status-web#783](https://github.com/status-im/status-web/issues/783) Browser wallet QA testing - Beta
- [status-im/status-web#771](https://github.com/status-im/status-web/issues/771) QA testing - build #93
- [status-im/status-web#768](https://github.com/status-im/status-web/issues/768) Browser extension wallet QA checklist

### Value Chart

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:value-chart`
* owner: JulesFiliot
* status: not started
* start-date: 2026/02/12
* end-date: 2026/03/05

#### Description

Implement value chart functionality to display portfolio value over time.

#### Deliverables

- Value chart component
- Chart data integration
- UI implementation

### Hide Small Balances

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:hide-small-balances`
* owner: jinhojang6
* status: not started
* start-date: 2026/02/12
* end-date: 2026/02/26

#### Description

Implement feature to hide small token balances from the wallet view for cleaner UI.

#### Deliverables

- Hide small balances functionality
- User preference settings
- UI toggle implementation

### LI.FI Swap Integration

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:lifi-swap-integration`
* owner: JulesFiliot
* status: in progress (5%)
* start-date: 2026/02/12
* end-date: 2026/03/05

#### Description

Integrate LI.FI swap functionality to enable multi-chain token swaps within the wallet extension.

#### Deliverables

- LI.FI integration
- Swap interface
- Multi-chain support
- [status-im/status-web#966](https://github.com/status-im/status-web/pull/966) Integrate LI.FI widget to swap token on ETH network

### Send NFT

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:send-nft`
* owner: JulesFiliot
* status: in progress (5%)
* start-date: 2026/02/19
* end-date: 2026/03/05

#### Description

Implement functionality to send NFTs from the wallet extension.

#### Deliverables

- Send NFT feature
- NFT transfer interface
- Transaction handling

### Global Password

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:global-password`
* owner: JulesFiliot
* status: in progress (30%)
* start-date: 2026/02/19
* end-date: 2026/03/05

#### Description

Implement global password functionality for unified authentication across wallet features.

#### Deliverables

- Global password system
- Authentication integration
- Password management UI
- [status-im/status-web#995](https://github.com/status-im/status-web/issues/995) Session-based keys management for wallet
- [Status wallet architecture response](https://github.com/status-im/status-web/issues/995#issuecomment-3821551558)

### Multi Account

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:multi-account`
* owner: jkbktl
* status: not started
* start-date: 2026/02/26
* end-date: 2026/03/19

#### Description

Implement multi-account support to allow users to manage multiple accounts within the wallet extension.

#### Deliverables

- Multi-account functionality
- Account switching interface
- Account management UI

### Multi Wallet

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:multi-wallet`
* owner: JulesFiliot
* status: not started
* start-date: 2026/02/26
* end-date: 2026/03/19

#### Description

Implement multi-wallet support to allow users to connect and manage multiple wallets simultaneously.

#### Deliverables

- Multi-wallet functionality
- Wallet connection management
- Wallet switching interface

### Dapp Connection

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:dapp-connection`
* owner: jinhojang6
* status: not started
* start-date: 2026/03/05
* end-date: 2026/03/19

#### Description

Implement dApp connection functionality to enable wallet extension to connect with decentralized applications.

#### Deliverables

- dApp connection system
- Connection approval interface
- dApp integration support

### Hardware Wallets

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:hardware-wallets`
* owner: jkbktl
* status: not started
* start-date: 2026/03/05
* end-date: 2026/03/26

#### Description

Implement hardware wallet support with QR code-based connection and Keycard Shell integration.

#### Deliverables

- Hardware wallet integration
- QR code connection system
- Keycard Shell support

### Browser and System Notifications

* fully qualified name: `ift-ts:web:status:2026q1-status-wallet-extension:browser-system-notifications`
* owner: JulesFiliot
* status: not started
* start-date: 2026/03/12
* end-date: 2026/03/26

#### Description

Implement browser and system notifications to alert users of wallet activities and transactions.

#### Deliverables

- Notification system implementation
- Browser notification integration
- System notification support
