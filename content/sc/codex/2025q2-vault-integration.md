---
title: Codex Vault Integration
tags:
  - "2025q2"
  - "sc"
  - "codex"
draft: false
description: Help reviewing and formally verifying the Codex Vault Integration.
---

`vac:sc:codex:2025q2-vault-integration`

Help reviewing and formally verifying the Codex Vault Integration.

## Description

Codex aims to extract all funds related logic of the `MarketPlace` contract into a dedicated `Vault` contract. We will help review and formally verify the integration of the `Vault` contract into the Codex marketplace.

## Task List

### Review Vault contract

* fully qualified name: `2025q1-vault-integration:review-vault-contract`
* owner: 
* status: not started
* start-date: 2025/04/01
* end-date: 2025/04/15

#### Description

Review [this pull request](https://github.com/codex-storage/codex-contracts-eth/pull/220),
which introduces a new `Vault` contract, that is then used in [this pull request](https://github.com/codex-storage/codex-contracts-eth/pull/223),
to integrate it with the Codex marketplace contracts.

#### Deliverables

- [ ] Reviews on these pull requests with feedback and suggestions

### Formally verify Vault integration

* fully qualified name: `2025q1-vault-integration:formal-verification`
* owner: 
* status: not started
* start-date: 2025/04/15
* end-date: 2025/06/30

#### Description

Ensure the correctness of the integration of the `Vault` contract with the Codex marketplace contracts by formal verification. 
This task includes creating a list of application properties and them implementing them accordingly.

#### Deliverables

- [ ] Spec files containing rules for the integration
