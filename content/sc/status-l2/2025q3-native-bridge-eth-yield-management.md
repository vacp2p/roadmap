---
title: SN L2 Bridge ETH Yield Management
tags:
  - "2025q3"
  - "sc"
  - "status-l2"
draft: false
description: Implement yield generation in the Status Network native bridge for bridged ETH.
---

`vac:sc:status-l2:2025q3-native-bridge-eth-yield-management`

Implement yield generation in the Status Network native bridge for bridged ETH.

## Description

After laying the groundwork for yield generation in the Status Network native bridge,
the next step is to leverage the existing architecture to implement yield generation for bridged ETH.
This commitment is about implementing yield generation for bridged ETH using the Lido protocol.


## Task List


### Lido integration
* fully qualified name: `2025q3-native-bridge-eth-yield-management:lido-integration`
* owner: 
* status: 
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description

We've implemented the necessary abstractions and proxies to allow for yield generation in the native bridge.
The next step is to integrate the Lido protocol as a yield provider for the bridge.
Part of this task is implementing deposits and withdrawals via the bridge.

#### Deliverables

- [ ] Commits/PRs that implement and integrate the Lido yield provider
- [ ] Tests that verify the functionality of the Lido yield provider integration

### Yield distribution
* fully qualified name: `2025q3-native-bridge-eth-yield-management:yield-distribution`
* owner: 
* status: 
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description

Implement the necessary changes to send and distribute the generated yield to a splitter contract on Status Network.

#### Deliverables

- [ ] Commits/PRs that implement the yield distribution logic

