---
title: SN Hub
tags:
  - "2025q4"
  - "web"
  - "status"
draft: false
description: "Development of Status Network Hub, the main portal application for Status Network users to access all network features including staking, yield earning, bridging, and public funding pool tracking in a unified interface."
---

`vac:web:status:2025q4-sn-hub`

## Description

This commitment involves developing the Status Network Hub (SN Hub), the main portal application through which users of the Status Network can access all network-related features including onboarding, staking, yield earning, bridging, and public funding pool tracking. The hub consolidates fragmented blockchain ecosystem functionalities into a single, user-friendly interface designed for beginner users and those just starting on the network.

The Status Network Hub will support Status Network's strategic objectives by:
- **Ecosystem Consolidation**: Providing a unified interface for all Status Network features and activities
- **User Onboarding**: Guiding new users through wallet connection and network tutorial processes
- **Feature Accessibility**: Making complex DeFi operations simple and accessible to beginner users
- **Network Engagement**: Encouraging participation in staking, liquidity provision, and governance activities

**Core Features (Testnet MVP Priority):**
- **Bridge UI**
- **Provide Liquidity**
- **Swap**
- **Wallet Connect**
- **Staking Dashboard**
- **Feedback Mechanisms**

**User Experience Focus:**
- **Beginner-Friendly**: Simple interfaces designed for users new to the network
- **Dashboard Overview**: Asset overview, recent activity, and quick access to core features
- **Side Navigation**: Seamless navigation between different hub features
- **Mobile Responsive**: Accessible across all devices for maximum user reach

## Task List

### Wallet Connect

* fully qualified name: `vac:web:status:2025q4-sn-hub:wallet-connect`
* owner: jkbktl
* status: in progress (70%)
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Ship the WalletConnect onboarding and session management flows so users can safely link their wallets.

#### Deliverables
- Fixed connect wallet experience for SN Hub.

### Staking

* fully qualified name: `vac:web:status:2025q4-sn-hub:staking`
* owner: nnachionuwa
* status: in progress (90%)
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Build the staking dashboard that displays yields, validator options, and lets users manage deposits.

#### Deliverables
- [add external links](https://github.com/status-im/status-web/issues/781) - created [PR#818](https://github.com/status-im/status-web/pull/818)
- synced with Filip regarding API and [review of API design](https://github.com/status-im/sn-api/pull/7)
- testing & debugging [Withdraw feature](https://github.com/status-im/status-web/pull/813)

### Feedback

* fully qualified name: `vac:web:status:2025q4-sn-hub:feedback`
* owner: jkbktl
* status: in progress (90%)
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Implement in-app feedback capture so newcomers can report issues and suggest improvements.

#### Deliverables
- [PR 809: addressed SN Hub feedback actions](https://github.com/status-im/status-web/pull/809).

### Deposit

* fully qualified name: `vac:web:status:2025q4-sn-hub:deposit`
* owner: jkbktl
* status: in progress (10%)
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Design the deposit flow that guides users through bridging assets into the Status Network.

#### Deliverables
- PRs/Issues/Docs/Reports

### Discovery

* fully qualified name: `vac:web:status:2025q4-sn-hub:discovery`
* owner: jkbktl
* status: in progress (70%)
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Surface curated dApps, pools, and governance opportunities in a discovery view tailored to new users.

#### Deliverables
- PRs/Issues/Docs/Reports

### Karma

* fully qualified name: `vac:web:status:2025q4-sn-hub:karma`
* owner: jkbktl
* status: in progress (70%)
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Implement the Karma scoring module that rewards participation and unlocks network perks.

#### Deliverables
- PRs/Issues/Docs/Reports

### Notifications

* fully qualified name: `vac:web:status:2025q4-sn-hub:notifications`
* owner: nnachionuwa
* status: not started
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Add notification preferences and delivery so users receive timely updates about their network activity.

#### Deliverables
- PRs/Issues/Docs/Reports

### Withdraw

* fully qualified name: `vac:web:status:2025q4-sn-hub:withdraw`
* owner: jkbktl
* status: in progress (60%)
* start-date: 2025/09/05
* end-date: 2025/11/30

#### Description
Create the withdrawal flow that lets users exit positions and transfer assets back to their wallets.

#### Deliverables
- PRs/Issues/Docs/Reports

> https://www.figma.com/design/1XbZL2WrTG5DqJO8DovE0H/Website----status.network?node-id=1940-3359&p=f&m=dev
> https://github.com/orgs/status-im/projects/94/views/5?sliceBy%5Bvalue%5D=September+2025+%28Status+Network%29
