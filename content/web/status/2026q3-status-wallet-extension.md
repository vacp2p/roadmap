---
title: Status Wallet Extension
tags:
  - "2026q3"
  - "web"
  - "status"
draft: false
description: "Continued development of the browser wallet extension into Q3 — non-EVM chain coverage (BTC, SOL send/receive), recovery phrase accessibility, and broader non-EVM balance support."
---

`ift-ts:web:status:2026q3-status-wallet-extension`

## Description

Q3 continuation of the wallet extension focused on **non-EVM chain coverage** (BTC and SOL send/receive flows), an **accessible recovery phrase** input, and **general support for non-EVM balances** across the wallet. Builds on the Q2 work tracked in [[web/status/2026q2-status-wallet-extension|2026q2-status-wallet-extension]].

Paired send/receive flows ship per chain (BTC first, then SOL) so end-to-end testing can happen chain by chain; the broader non-EVM balance abstraction caps the quarter.

## Task List

### Receive BTC

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:receive-btc`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/01
* end-date: 2026/07/17

#### Description

Implement Receive BTC flow in the wallet extension (address generation/display, QR, copy, basic validation). Tracked in [#982](https://github.com/status-im/status-web/issues/982).

#### Deliverables

- Receive BTC UI integrated in wallet flows
- Address generation/display and QR
- Smoke tests for receive flow

### Recovery Phrase Accessible Form

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:recovery-phrase-accessible-form`
* owner: Jinho
* status: in progress (25%)
* start-date: 2026/07/13
* end-date: 2026/07/24

#### Description

Replace the single recovery phrase input field with an accessible per-word form. Tracked in [#981](https://github.com/status-im/status-web/issues/981).

#### Deliverables

- [status-im/status-web#1286](https://github.com/status-im/status-web/pull/1286) feat(wallet): recovery phrase word grid input
- [status-im/status-web#1280](https://github.com/status-im/status-web/pull/1280) feat(wallet): create account from the wallet selector
- Per-word recovery phrase input component (12/24 words)
- Accessibility review (keyboard nav, screen-reader labels, paste handling)
- Updated UX in onboarding and import flows

### Send BTC

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:send-btc`
* owner: JulesFiliot
* status: not started
* start-date: 2026/07/20
* end-date: 2026/07/31

#### Description

Implement Send BTC flow in the wallet extension (address input, amount, fee estimate, sign + broadcast). Tracked in [#979](https://github.com/status-im/status-web/issues/979).

#### Deliverables

- Send BTC transaction flow
- Fee estimation and confirmation
- End-to-end test against testnet

### Receive SOL

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:receive-sol`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/03
* end-date: 2026/08/14

#### Description

Implement Receive SOL flow in the wallet extension. Tracked in [#983](https://github.com/status-im/status-web/issues/983).

#### Deliverables

- Receive SOL UI integrated in wallet flows
- Address display and QR
- Smoke tests for receive flow

### Send SOL

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:send-sol`
* owner: JulesFiliot
* status: not started
* start-date: 2026/08/17
* end-date: 2026/08/28

#### Description

Implement Send SOL flow in the wallet extension (address input, amount, fee, sign + broadcast). Tracked in [#980](https://github.com/status-im/status-web/issues/980).

#### Deliverables

- Send SOL transaction flow
- Fee estimation and confirmation
- End-to-end test against testnet

### Support Non-EVM Balances

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:support-non-evm-balances`
* owner: JulesFiliot
* status: not started
* start-date: 2026/09/01
* end-date: 2026/09/25

#### Description

Generalize non-EVM balance support across the wallet (portfolio totals, per-account views, refresh logic) so balances for BTC, SOL, and similar chains read like first-class citizens alongside EVM assets. Tracked in [#978](https://github.com/status-im/status-web/issues/978).

#### Deliverables

- Non-EVM balance fetch + cache abstraction
- Portfolio and account views surface non-EVM balances
- Tests covering portfolio aggregation with mixed EVM + non-EVM assets

### Dapp Connection

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:dapp-connection`
* owner: JulesFiliot
* status: done
* start-date: 2026/08/10
* end-date: 2026/08/25

#### Description

Persist dApp connections independently for each wallet account so switching accounts does not leak or discard connection state.

#### Deliverables

- [status-im/status-web#1136](https://github.com/status-im/status-web/issues/1136) Status Wallet Extension: dApp connection RPC methods parity
- [status-im/status-web#1303](https://github.com/status-im/status-web/pull/1303) feat(wallet): route dApp reads to the chain the dApp is on
- [status-im/status-web#1302](https://github.com/status-im/status-web/pull/1302) feat(wallet): support eth_sendTransaction for dApps
- [status-im/status-web#1301](https://github.com/status-im/status-web/pull/1301) feat(wallet): sign EIP-712 typed data for dApps
- [status-im/status-web#1299](https://github.com/status-im/status-web/pull/1299) fix(wallet): gate dApp RPC on granted permission
- [status-im/status-web#1298](https://github.com/status-im/status-web/pull/1298) fix(wallet): persist dApp connections per account
- Per-account dApp connection persistence
- Coverage for account switching and connection restoration

### Maintenance

* fully qualified name: `ift-ts:web:status:2026q3-status-wallet-extension:maintenance`
* owner: JulesFiliot
* status: done
* start-date: 2026/08/24
* end-date: 2026/09/01

#### Description

Maintain the Status Wallet Extension through release coordination, store
publication work, and fixes for transaction reliability and session recovery.

#### Deliverables

- [Release coordination thread](https://discord.com/channels/864066763682218004/1542559377377075360/1542559399615275008)
- [status-im/status-web#1315](https://github.com/status-im/status-web/pull/1315) fix(wallet): stop underpricing transactions in the fee estimator
- [status-im/status-web#1316](https://github.com/status-im/status-web/pull/1316) fix(wallet): recover from stuck transactions instead of breaking the session
