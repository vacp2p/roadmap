---
title: RLN Smart Contract Testing
tags:
  - "2025q4"
  - "qa"
  - "waku"
draft: false
description: Test and validate the reliability of the Waku RLN Smart Contract
---

`vac:qa:waku:2025q4-rln-smart-contract-testing`

## Description

Test and validate the reliability of the Waku RLN Smart Contract in accordance to [Waku2 RLN Contract Specification](https://github.com/waku-org/specs/blob/master/standards/core/rln-contract.md).   
Ensure the smart contract main workflow is functional. Test corner cases and potential attack vectors.   
Test on selected blockchains to ensure uniform behavior across different deployments.

**Alignment with VAC Narratives:**

- By testing the Waku RLN Smart Contract,
  VAC QA ensures robust and predictable behavior across different deployments and blockchains.
- This initiative supports VAC’s commitment to building reliable and scalable testing frameworks
  that foster collaboration and confidence in the Waku ecosystem.
- Reliability-focused testing directly aligns with the strategic objective of ensuring resilience in communication protocols.

## Task List

### Property-based Fuzz Testing

- fully qualified name: `vac:qa:waku:2025q4-rln-smart-contract-testing:property-based`
- owner: romanzac
- status: not started
- start-date: 2025/10/1
- end-date: 2025/10/31

#### Description

Implement tests to verify behaviors that must always hold. Run these tests with high iterations to find unexpected edge cases.

#### Deliverables

- PRs with tests using calls to contract's ABI
- Documentation outlining tested scenarios
