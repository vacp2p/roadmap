---
title: New Karma Requirements for SN L2
tags:
  - "2025q3"
  - "sc"
  - "status-l2"
draft: false
description: Extend the Karma token with new features and requirements for Status Network L2.
---

`vac:sc:status-l2:2025q3-new-karma-requirements`

Extend the Karma token with new features and requirements for Status Network L2.

## Description

The Karma token is a core component of the Status ecosystem, 
used for various purposes including governance, 
and incentivization. 
As we continue to develop and expand the Status Network L2,
there are new requirements and features that need to be implemented in the Karma token to support these advancements.
A reference document describing the requirements can be found [here](https://www.notion.so/Product-Requirements-Document-PRD-Karma-Architecture-25d8f96fb65c8010aa43f867e85c8e21).
This commitment focuses on extending the Karma token and related contracts to meet these new requirements.

## Task List

### Karma Voting capabilities
* fully qualified name: `2025q3-new-karma-requirements:votes`
* owner: gravityblast 
* status: done
* start-date: 2025/09/01
* end-date: 2025/09/30

#### Description

Karma tokens should have voting capabilities similar to those found in governance tokens like COMP or UNI.
This requires conversion of virtual karma to actual karma.

#### Deliverables

- [x] [Initial votes implementation](https://github.com/status-im/status-network-monorepo/pull/26)
- [x] [Custom votes implementation incl. tests](https://github.com/status-im/status-network-monorepo/pull/39)

### Virtual Karma to actual Karma conversion
* fully qualified name: `2025q3-new-karma-requirements:virtual-karma-conversion`
* owner: r4bbit 
* status: done
* start-date: 2025/09/01
* end-date: 2025/09/30

#### Description

In order to allow earned Karma to be tranferable for whitelisted addresses,
we need to implement a mechanism to convert virtual Karma (Karma that lives in reward distributors like the staking system) to actual Karma.
This requires whitelisted addresses to mint actual Karma and likely requires changes in the current slashing algorithm.

#### Deliverables

- [x] [Commits/PRs that implement the conversion mechanism](https://github.com/status-im/status-network-monorepo/pull/28)
- [x] [Tests that verify the functionality](https://github.com/status-im/status-network-monorepo/pull/28)


### Whitelist transferability
* fully qualified name: `2025q3-new-karma-requirements:whitelist-transferability`
* owner: r4bbit
* status: done
* start-date: 2025/09/01
* end-date: 2025/09/30

#### Description

Karma is non-transferable by default.
However,
as part of the new requirements,
we need to implement a whitelist mechanism that allows certain addresses to transfer Karma tokens.

#### Deliverables

- [x] [Commits/PRs that implement the whitelist transferability feature](https://github.com/status-im/status-network-monorepo/pull/27)
- [x] [Tests that verify the functionality](https://github.com/status-im/status-network-monorepo/pull/27)

### Design native app distribution system 
* fully qualified name: `2025q3-new-karma-requirements:design-native-app-distribution-system`
* owner: r4bbit
* status: done
* start-date: 2025/09/01
* end-date: 2025/09/30

#### Description

A whitelisted account should be able to send Karma to what are called "native app teams".
These are teams that are building native apps on Status Network L2.
For doing so, they'll get Karma from a whitelisted account.
A certain amount of that Karma should be reserved for onboarding new users (e.g., 50%).
One idea is to provide a contract that allows for merkle tree based airdrops to onboard new users.
This task is about designing such a system in collaboation with the Status L2 team.

#### Deliverables

- [x] Document or virsual representation of the designed system

### Implement native app distribution system 
* fully qualified name: `2025q3-new-karma-requirements:implement-native-app-distribution-system`
* owner: r4bbit
* status: done
* start-date: 2025/09/01
* end-date: 2025/09/30

#### Description

Implement the native app distribution system as designed in the previous task.

#### Deliverables

- [x] [Initial Karma Airdrop contract](https://github.com/status-im/status-network-monorepo/pull/37)
- [x] [Merkleroot updates and pausability](https://github.com/status-im/status-network-monorepo/pull/38)
- [x] [Default vote delegation on claim](https://github.com/status-im/status-network-monorepo/pull/40)

### Documentation
* fully qualified name: `2025q3-new-karma-requirements:documentation`
* owner: r4bbit
* status: done
* start-date: 2025/09/01
* end-date: 2025/09/30

#### Description

Document the new features and changes made to the Karma token and related contracts.

#### Deliverables

- [x] [Commits/PRs that add documentation](https://github.com/status-im/status-network-monorepo/pull/32)
