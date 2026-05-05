---
title: DEX Logos Module
tags:
  - "2026q2"
  - "sc"
  - "logos"
draft: false
description: Build the privacy-preserving DEX as a logos module (C++ Qt plugin) providing swap, liquidity management, and pool analytics for end users.
---

`ift-ts:sc:logos:2026q2-dex-logos-module`

## Description

Build the DEX mini-app as a logos module using the [logos-module](https://github.com/logos-co/logos-module) C++ Qt plugin framework.
This is the end-user facing application that enables swapping tokens, managing liquidity positions, and viewing pool analytics on the LEZ privacy-preserving DEX.

The logos module is a Qt plugin implementing `PluginInterface` and is loaded by the Logos platform at runtime.
Pool discoverability is handled in the UI: before creating a new pool, the app checks whether an LP token PDA already exists for the given token pair.
LEZ's native deshield/re-shield privacy model is exposed transparently to users through the interface.

## Task List

### Understand logos-module framework and define DEX module interface

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-logos-module:research-logos-module`
* owner: r4bbit
* status: in progress (25%)
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Study the logos-module framework: the `PluginInterface` contract, the metadata system, Qt plugin loading mechanisms, and the `lm` CLI introspection tool.
Determine what interface the DEX plugin must implement and what data types and signals are needed for the swap, liquidity, and analytics flows.
Produce a findings document that captures the integration approach.

#### Deliverables

- [ ] Findings document describing the logos-module integration approach for the DEX
- [ ] List of required PluginInterface methods and signals for the DEX module

### Design DEX logos module architecture

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-logos-module:design-dex-module`
* owner: TBD
* status: not started
* start-date: 2026/04/15
* end-date: 2026/04/30

#### Description

Design the DEX logos module architecture: plugin interface methods, metadata, Qt signals/slots for UI state, and how the module integrates with the DEX SDK.
Define the data structures passed between the plugin and the Logos platform host.

#### Deliverables

- [ ] Architecture design document for the DEX logos module
- [ ] Plugin interface definition (methods, signals, metadata)

### Implement pool analytics view

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-logos-module:pool-analytics`
* owner: Andrea
* status: in progress (25%)
* start-date: 2026/05/01
* end-date: 2026/05/31

#### Description

Implement the pool analytics view showing pool reserves, fee tier, total value locked (TVL), and volume statistics.
This view helps users understand pool health and select which pool to interact with.

#### Deliverables

- [ ] Pool analytics view implemented in the DEX logos module
- [ ] Pool reserves, fee tier, TVL, and volume displayed
- [ ] PR with code review

### Implement swap UI with pre-swap confirmation

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-logos-module:swap-ui`
* owner: TBD
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/15

#### Description

Implement the token swap interface with a pre-swap confirmation step showing the expected output amount, price impact, and fees (using the SDK's pre-swap simulation).
Support both exact input and exact output swap modes.
Display public vs. private information clearly per RFP-004 requirements.

#### Deliverables

- [ ] Swap UI with token input/output fields and fee tier display
- [ ] Pre-swap confirmation screen showing output amount, price impact, and fee cost
- [ ] Support for exact input and exact output swap modes
- [ ] PR with code review
- [logos-blockchain/lez-programs#77](https://github.com/logos-blockchain/lez-programs/pull/77) updated swap UI styles to match the liquidity page
- [logos-blockchain/lez-programs#68](https://github.com/logos-blockchain/lez-programs/pull/68) chore(amm-ui): add basic swap UI for Token Pair Selector and Swap Direction

### Implement liquidity management UI

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-logos-module:liquidity-ui`
* owner: Ricardo
* status: in progress (50%)
* start-date: 2026/05/15
* end-date: 2026/06/15

#### Description

Implement the liquidity management interface supporting add and remove liquidity operations.
Include pool discoverability: when a user attempts to create a new pool for a token pair, check whether an LP token PDA already exists for that pair and surface the existing pool if found.

#### Deliverables

- [ ] Add liquidity UI with token pair selection and amount inputs
- [ ] Remove liquidity UI showing current LP position and expected return
- [ ] Pool discoverability: check LP token PDA existence before pool creation
- [ ] PR with code review
- [logos-blockchain/lez-programs#59](https://github.com/logos-blockchain/lez-programs/issues/59) Liquidity Provider UI for AMM Program
- [logos-blockchain/lez-programs#66](https://github.com/logos-blockchain/lez-programs/pull/66) feat(amm-ui): add liquidity pool management flow

### Package and deploy DEX logos module

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-logos-module:deploy-logos-module`
* owner: TBD
* status: not started
* start-date: 2026/06/15
* end-date: 2026/06/30

#### Description

Package the completed DEX logos module as a distributable Qt plugin and deploy it against the testnet 0.2 deployment of the AMM programs.
Verify the full end-to-end flow: swap, add/remove liquidity, and pool analytics working against live testnet programs.

#### Deliverables

- [ ] DEX logos module packaged as a distributable Qt plugin
- [ ] End-to-end verification of swap, liquidity, and analytics against testnet 0.2
- [ ] Deployment notes and plugin installation instructions
