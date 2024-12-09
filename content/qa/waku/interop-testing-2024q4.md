---
title: Waku Interop Testing (extended)
tags:
  - "2024q4"
  - "qa"
  - "waku"  
draft: false  
description: Extend Waku interop tests with focus on more advanced scenarios
---

`vac:qa:waku:interop-testing-2024q4`

## Description
Extend Waku interop tests with focus on more advanced scenarios

The interop testing framework already provides extensive coverage,
running hundreds of tests across both nwaku and gowaku.
Initially, the focus was on functional testing,
targeting protocols in isolation.
For this commitment, we aim to extend coverage
with more complex and edge-case scenarios.
Enhancements include identifying negative test cases,
running scenarios with multiple nodes,
and improving CI execution speed by leveraging more powerful runners.
Once the execution speed meets acceptable thresholds,
we will integrate this expanded suite or a subset of tests
into the nwaku/go-waku CI pipelines,
ensuring PR-level validation.

**Alignment with VAC Narratives:**

* The VAC QA team plays a key role in supporting internal collaboration
  and efficiency across projects by ensuring the quality of Waku’s interop framework.
* By finding issues in specs during testing,
  VAC strengthens the RFC culture,
  contributing to continuous improvement and community engagement.
* By working with developers to address known issues and enhancing CI performance,
  VAC directly contributes to IFT's strategic objective of scaling capacity and efficiency
  through community-driven efforts.

## Task List

### Edge Cases

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:edge-cases`
* owner: aya
* status: done
* start-date: 2024/10/07
* end-date: 2024/10/28

#### Description
Expand the coverage to include negative scenarios,
ensuring that all edge cases are handled appropriately.
Focus on edge cases that might not be triggered in normal operational flows,
such as protocol failures, unexpected data, or unexpected node behavior.

#### Deliverables
PRs:
* https://github.com/waku-org/waku-interop-tests/pull/76
* https://github.com/waku-org/waku-interop-tests/pull/81
* https://github.com/waku-org/waku-interop-tests/pull/79
  
CI Runs:
* https://github.com/waku-org/waku-interop-tests/actions/runs/11540778495
* https://github.com/waku-org/waku-interop-tests/actions/runs/11539734974
  
Issues found:
* https://github.com/waku-org/nwaku/issues/3135
* https://github.com/waku-org/nwaku/issues/3128

### E2E Scenarios

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:e2e-scenarios`
* owner: aya
* status: done
* start-date: 2024/10/28
* end-date: 2024/11/06

#### Description
Design and implement end-to-end test scenarios involving at least 4-5 nodes.
These tests will assess interoperability between nodes
and validate the system's ability to handle realistic use cases.
Incorporate the validation of node metrics at the conclusion of each test
to ensure performance stability.

#### Deliverables
PRs:
- https://github.com/waku-org/waku-interop-tests/pull/85
- https://github.com/waku-org/waku-interop-tests/pull/80
- https://github.com/waku-org/waku-interop-tests/pull/86

CI Runs:
- https://github.com/waku-org/waku-interop-tests/actions/runs/11763131690
- https://github.com/waku-org/waku-interop-tests/actions/runs/11762708653
- https://github.com/waku-org/waku-interop-tests/actions/runs/11716675132
- https://github.com/waku-org/waku-interop-tests/actions/runs/11722193214

Issues found:
- https://github.com/waku-org/nwaku/issues/3168
- https://github.com/waku-org/nwaku/issues/3169

### Known Issues

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:known-issues`
* owner: aya
* status: done
* start-date: 2024/11/06
* end-date: 2024/11/18

#### Description
Work closely with developers
to identify known issues that require testing.
Develop test cases for the most critical and impactful issues
and solicit input from developers for additional scenarios to cover.
Each developer or user interacts with the product in slightly different ways,
which can potentially uncover unexpected behavior.
Developers can provide valuable feedback on such cases.
They also work closely with node operators
and are often aware of the issues reported by them.
Another point is to check reported GitHub issues
and identify which tests can be automated based on those issues.
This ensures that once an issue is closed,
it doesn't resurface again.

#### Deliverables
PRs:
- https://github.com/waku-org/waku-interop-tests/pull/87

CI runs:
- https://github.com/waku-org/waku-interop-tests/actions/runs/11890542812
- https://github.com/waku-org/waku-interop-tests/actions/runs/11890003986

Issues found:
- https://github.com/waku-org/go-waku/issues/1254
- https://github.com/waku-org/go-waku/issues/1253

### Faster Runners

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:faster-runners`
* owner: aya
* status: in progress (50%)
* start-date: 2024/11/18
* end-date: 2024/12/02

#### Description
Optimize CI execution speed by leveraging more powerful runners
and improving test parallelization.
Ensure that these changes maintain or improve the quality of the tests
without compromising coverage.

#### Deliverables
* CI configuration updates with improved runners
* CI runs demonstrating reduced execution time while passing all tests

### CI Integration

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:ci-integration`
* owner: aya
* status: in progress (80%)
* start-date: 2024/12/02
* end-date: 2024/12/09

#### Description
Integrate a subset of the interop tests into the existing nwaku/go-waku CI pipelines.
The execution time should not exceed 15 minutes,
balancing speed with meaningful test coverage.
The goal is to catch issues earlier in the PR lifecycle
without adding significant overhead to CI.

#### Deliverables
* PR to nwaku/go-waku repos with CI test integration
* CI runs verifying that the interop tests complete within the set time limits

### Network Conditions

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:network-conditions`
* owner: fbarbu15
* status: not started
* start-date: 2024/12/09
* end-date: 2024/12/24

#### Description
Develop tests to simulate unusual network conditions,
such as high latency, packet loss, and low bandwidth,
particularly affecting light nodes.
The framework should be flexible enough to allow for the application
of these conditions across a full test run on-demand.
Additionally, ensure that a subset of these tests runs nightly
to catch issues that may arise under suboptimal network conditions.

#### Deliverables
* PR with network condition simulation framework
* CI configuration for on-demand full test runs with network constraints
* Nightly CI runs for a subset of tests under network strain

### Maintenance

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:maintenace`
* owner: fbarbu15
* status: started (50%)
* start-date: 2024/10/01
* end-date: 2024/12/31

#### Description
Ongoing Maintenance for Waku Interop Tests
This task involves ensuring the continued reliability 
and functionality of the Waku interop tests. 
It includes adjusting tests whenever there are changes in nwaku or go-waku, 
addressing detected regressions through investigation, reporting, and retesting, 
and resolving infrastructure issues that disrupt the tests. 
Additionally, it covers unplanned but necessary minor improvements to the testing framework 
to enhance its effectiveness.

#### Deliverables

PRs:
* https://github.com/waku-org/waku-interop-tests/pull/75
* https://github.com/waku-org/waku-interop-tests/pull/79
* https://github.com/waku-org/waku-interop-tests/pull/82
* https://github.com/waku-org/waku-interop-tests/pull/84
* https://github.com/waku-org/waku-interop-tests/pull/91
* https://github.com/waku-org/waku-interop-tests/pull/93

Issues found:
* https://github.com/waku-org/go-waku/issues/1255

### Libwaku Discovery

* fully qualified name: `vac:qa:waku:interop-testing-2024q4:discover-libwaku`
* owner: aya
* status: started (50%)
* start-date: 2024/11/25
* end-date: 2024/11/28

#### Description
Brief Discovery for Libwaku Python and Golang Bindings
Waku developers have requested support in evaluating 
the possibility of creating a test framework for libwaku testing. 
This task involves dedicating a few days to explore the requirements, 
assess the feasibility, and determine whether we have the necessary capabilities 
to work effectively with the existing implementation. 
The goal is to understand the scope of the task 
and identify the next steps for potential framework development.

#### Deliverables
PRs:

Issues found:
