---
title: Status Network L2 Pre-Audit Protocol Enhancements
tags:
  - "2025q4"
  - "sc"
  - "status-l2"
draft: false
description: Complete critical protocol features and enhancements before the security audit.
---

`vac:sc:status-l2:2025q4-pre-audit-protocol-enhancements`

Complete critical protocol features and enhancements before the security audit.

## Description

Before the audit begins in November,
there are several critical protocol features that need to be completed.
This includes finishing the distributed slashing mechanism that was carried over from Q3,
and implementing a new reward distributor for off-chain based Karma distribution.
These features are essential for the protocol's functionality and need to be in place before the audit to ensure comprehensive security coverage.

## Task List

### Distributed slashing implementation
* fully qualified name: `vac:sc:status-l2:2025q4-pre-audit-protocol-enhancements:distributed-slashing`
* owner: r4bbit
* status: in progress (30%)
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

Complete the distributed slashing mechanism that was started in Q3 but not finished.
This feature is critical for the Karma system's security model,
allowing for enforcement of protocol rules.
The implementation needs to handle slashing reward sources and ensure proper accounting.

#### Deliverables
- Open research notes on slashing race-condition solutions ([SlashingKarmaLeader.sol](https://github.com/status-im/status-network-monorepo/blob/slash-karma-leader/status-network-contracts/src/rln/SlashingKarmaLeader.sol)).


### Off-chain criteria reward distributor
* fully qualified name: `vac:sc:status-l2:2025q4-pre-audit-protocol-enhancements:offchain-reward-distributor`
* owner: r4bbit
* status: not started
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

Implement a new reward distributor contract that allows an authorized account to distribute 1 Karma to accounts based on off-chain criteria.
This provides a flexible mechanism for rewarding users based on activities or achievements that cannot be verified on-chain.
The contract should be simple,
secure,
and have appropriate access controls to prevent abuse.

#### Deliverables

- [ ] Commits/PRs that implement the off-chain reward distributor
- [ ] Documentation explaining the reward distribution mechanism

### Convert ERC20Votes tests to Foundry
* fully qualified name: `vac:sc:status-l2:2025q4-pre-audit-protocol-enhancements:convert-erc20votes-tests`
* owner: r4bbit
* status: not started
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

Convert the JavaScript ERC20Votes tests from OpenZeppelin to Foundry tests in our repository.
We've introduced a custom version of ERC20Votes that is almost identical to the OpenZeppelin implementation,
but we need to ensure all the original tests pass with our custom version.
This provides confidence that our modifications haven't introduced any regressions.

#### Deliverables

- [ ] Commits/PRs that add Foundry tests for custom ERC20Votes
- [ ] All converted tests passing
- [ ] Test coverage matching or exceeding the original OpenZeppelin tests

### Ensure correct license headers
* fully qualified name: `vac:sc:status-l2:2025q4-pre-audit-protocol-enhancements:license-headers`
* owner: r4bbit
* status: not started
* start-date: 2025/10/01
* end-date: 2025/10/30

#### Description

Review all contract files and ensure they have the correct license headers.
This is important for legal compliance and clarity before the audit.
Verify that all files have appropriate SPDX license identifiers and that the licensing is consistent across the codebase.

#### Deliverables

- [ ] Commits/PRs that add or correct license headers
- [ ] Documentation of the licensing structure if needed
