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
* status: not started
* start-date: 2024/10/07
* end-date: 2024/10/21

#### Description
Add integration tests to build on top of existing unit tests for data availability,
focusing on functionality and using nomos-cli as the initiating node.

#### Deliverables
* PR link with added tests
* CI runs showing successful or failed executions with detailed reports

### Dispersal and Storage Tests

* fully qualified name: `vac:qa:nomos:da-testing-2024q4:dispersal-storage-tests`
* owner: romanzac
* status: not started
* start-date: 2024/10/21
* end-date: 2024/11/04

#### Description
Add integration tests focusing on the dispersal and storage interface.

#### Deliverables
* PR link with added tests
* CI runs showing successful or failed executions with detailed reports

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
* status: not started
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
* status: not started
* start-date: 2024/12/02
* end-date: 2024/12/13

#### Description
Add edge case integration tests to cover unusual system behavior.

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

