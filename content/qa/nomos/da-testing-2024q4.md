---

title: Nomos Data Availability Testing  
tags:
  - "2024q4"
  - "qa"
  - "nomos"  
draft: false  
description: Implement data availability test plans for the Nomos project
  and continuously updating them due to evolving specs.

---

`vac:qa:nomos:da-testing-2024q4`

## Description
Implement data availability test plans for the Nomos project
and continuously update them due to evolving specs.

Since this feature is still in development,
tests will be conducted at multiple levels,
including unit and integration tests.
Given that the specifications for this feature are frequently changing,
the test cases will need to be regularly updated to reflect those changes.

**Alignment with VAC Narratives:**
- By developing and constantly updating tests for data availability,
  VAC QA ensures that the feature's implementation aligns with high standards.
- This continuous testing helps identify any spec-related issues early,
  contributing to the RFC culture and improving spec quality.
- The effort also supports IFT's strategic objective of scaling the project’s capacity
  and ensuring a reliable system for future community involvement.

## Task List

### Basic Functionality Tests

* fully qualified name: `vac:qa:nomos:da-testing-2024q4:basic-functionality-tests`
* owner: romanzac
* status: done
* start-date: 2024/10/07
* end-date: 2024/11/08

#### Description
Add integration tests to build on top of existing unit tests for data availability,
focusing on functionality and using nomos-cli as the initiating node.

#### Deliverables
PRs:
- [PR #819](https://github.com/logos-co/nomos-node/pull/819) - pending on issue 902
  - TC1.16: Verify that Dispersal can prepare data correctly.
  - TC1.17: Verify that Dispersal can send and await response correctly.  
  - TC1.26: Ensure that DA nodes can correctly connect to their assigned subnets.

- [PR #898](https://github.com/logos-co/nomos-node/pull/898) - postponed to time when transation data protection in place 
  - TC1.4: Verify that Kate commitments are correctly implemented.
  - TC1.20: Verify the correct initialization of global parameters and roots of unity.
  - TC1.6: Verify that the DAEncoder can correctly chunkify the input data.
  - TC1.22: Verify FK20 proof generation for polynomials.
  - TC1.23: Verify KZG commitment generation from byte data.
  - TC1.24: Verify the generation and verification of element proofs in KZG.
  - TC1.25: Verify the encoding of polynomials using RS code and subsequent decoding.

CI Runs:
- [Run #11660035391](https://github.com/logos-co/nomos-node/actions/runs/11660035391)    
- [Run #11734644660](https://github.com/logos-co/nomos-node/actions/runs/11734644660)

Issues Found:
- [Executor behaviour connects to other executor behaviour for dispersal](https://github.com/logos-co/nomos-node/issues/900)
- [Dispersal messages have not reached the validator on self-hosted runner](https://github.com/logos-co/nomos-node/issues/902)

### Dispersal and Storage Tests

* fully qualified name: `vac:qa:nomos:da-testing-2024q4:dispersal-storage-tests`
* owner: romanzac
* status: done
* start-date: 2024/10/21
* end-date: 2024/11/04

#### Description
Add integration tests focusing on the dispersal and storage interface.

#### Deliverables
PRs:
- [PR #921](https://github.com/logos-co/nomos-node/pull/921)
  - TC2.2: Ensure that DA nodes hold chunks in memory until the block with related BlobInfo is received.
  - TC2.3: Confirm that attestations about received chunks are correctly sent back to the Zone.

CI Runs:
  - [Run #12066967078](https://github.com/logos-co/nomos-node/actions/runs/12066967078)    

Issues Found:
  - [Unwrap on non-existent blob_col_idx](https://github.com/logos-co/nomos-node/issues/922)

### Certification and Verification Tests

* fully qualified name: `vac:qa:nomos:da-testing-2024q4:certification-verification-tests`
* owner: romanzac
* status: not started
* start-date: 2024/11/04
* end-date: 2024/11/22

#### Description
Add integration tests focusing on certificate completeness.

#### Deliverables
* PR link with added tests
* CI runs showing successful or failed executions with detailed reports

### Data Integrity Tests

* fully qualified name: `vac:qa:nomos:da-testing-2024q4:data-integrity-tests`
* owner: romanzac
* status: in progress (5%)
* start-date: 2024/11/22
* end-date: 2024/12/02

#### Description
Add integration tests focusing on the system's ability
to reconstruct or retrieve data.

#### Deliverables
* PR link with added tests
* CI runs showing successful or failed executions with detailed reports

### Edge Cases

* fully qualified name: `vac:qa:nomos:da-testing-2024q4:edge-cases`
* owner: romanzac
* status: in progress (50%)
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description
This is an ongoing task.
Add edge case integration tests to cover unusual system behavior.
Test edge cases for behaviours implemented for dispersal, replication and sampling.

#### Deliverables
* PR link with added tests
* CI runs showing successful or failed executions with detailed reports

### Test Optimization

* fully qualified name: `vac:qa:nomos:da-testing-2024q4:test-optimization`
* owner: romanzac
* status: not started
* start-date: 2024/12/13
* end-date: 2024/12/20

#### Description
Optimize existing tests to run on data sets with greater variance.
Consider using frameworks with fixture support like `rstest`
to simplify existing code.

#### Deliverables
* PR link with redesigned tests
* CI runs showing successful or failed executions with detailed reports

