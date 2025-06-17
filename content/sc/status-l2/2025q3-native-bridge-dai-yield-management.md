---
title: SN L2 Bridge DAI Yield Management
tags:
  - "2025q3"
  - "sc"
  - "status-l2"
draft: false
description: Implement yield generation in the Status Network native bridge for bridged DAI.
---

`vac:sc:status-l2:2025q3-native-bridge-dai-yield-management`

Implement yield generation in the Status Network native bridge for bridged DAI.

## Description

Once ETH yield management is implemented and working,
the next step is to implement yield generation for bridged DAI.
This commitment is about implementing yield generation for bridged DAI using the DSR module of MakerDAO.


## Task List


### DSR integration
* fully qualified name: `2025q3-native-bridge-eth-yield-management:dsr-integration`
* owner: 
* status: 
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description

We've implemented the necessary abstractions and proxies to allow for yield generation in the native bridge.
The next step is to integrate the DSR protocol as a yield provider for the bridge.
Part of this task is implementing deposits and withdrawals via the bridge.

#### Deliverables

- [ ] Commits/PRs that implement and integrate the DAI yield provider
- [ ] Tests that verify the functionality of the DAI yield provider integration

### Yield distribution
* fully qualified name: `2025q3-native-bridge-dai-yield-management:yield-distribution`
* owner: 
* status: 
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description

Implement the necessary changes to send and distribute the generated yield to the splitter contract on Status Network.

#### Deliverables

- [ ] Commits/PRs that implement the yield distribution logic
