---

title: Nomos Data Availability Testing  
tags:
  - "2025q1"
  - "qa"
  - "nomos"  
draft: false  
description: Implement data availability test plans for the Nomos project at the cluster level. 

---

`vac:qa:nomos:2025q1-da-testing`

## Description
Implement data availability test plans for the Nomos project at the cluster level. 

**Alignment with VAC Narratives:**
- By developing and constantly updating tests for data availability,
  VAC QA ensures that the feature's implementation aligns with high standards.
- This continuous testing helps identify any spec-related issues early,
  contributing to the RFC culture and improving spec quality.
- The effort also supports IFT's strategic objective of scaling the project’s capacity
  and ensuring a reliable system for future community involvement.

## Task List

### Data Integrity Tests

* fully qualified name: `vac:qa:nomos:2025q1-da-testing:data-integrity-tests`
* owner: romanzac
* status: done
* start-date: 2025/01/06
* end-date: 2025/01/17

#### Description
Add integration tests focusing on the system's ability
to reconstruct or retrieve data.

#### Deliverables
- [Test/data availability and integrity](https://github.com/logos-co/nomos-e2e-tests/pull/2)
- [Sync data availability and integrity tests with latest Nomos node changes](https://github.com/logos-co/nomos-e2e-tests/pull/3)
- [Change Dockerfile for testnet image to enable block production](https://github.com/logos-co/nomos-node/pull/1041)
- [Add reconstruct command to nomos-cli](https://github.com/logos-co/nomos-node/pull/994)
- [CI workflow](https://github.com/logos-co/nomos-e2e-tests/actions/runs/13362639336)

### Networking and Privacy Tests

* fully qualified name: `vac:qa:nomos:2025q1-da-testing:networking-privacy`
* owner: romanzac
* status: done
* start-date: 2025/01/20 
* end-date: 2025/02/21

#### Description
Add integration tests focusing on the privacy of the data in transit

#### Deliverables
- [Test/networking and privacy](https://github.com/logos-co/nomos-e2e-tests/pull/4)

### Denial of Service (DoS) and Robustness Testing

* fully qualified name: `vac:qa:nomos:2025q1-da-testing:dos-robustness`
* owner: romanzac
* status: done
* start-date: 2025/02/24
* end-date: 2025/03/21

#### Description
Add integration tests to verify system’s resilience to DoS attacks and handling of large volume of data 

#### Deliverables
* [Test/spam protection](https://github.com/logos-co/nomos-e2e-tests/pull/5)
* [Test/high load denial of service](https://github.com/logos-co/nomos-e2e-tests/pull/7)
* [Chore/Cluster configuration update](https://github.com/logos-co/nomos-e2e-tests/pull/8)
* [Test/Disperse large volume data](https://github.com/logos-co/nomos-e2e-tests/pull/9)

### Edge Cases

* fully qualified name: `vac:qa:nomos:2025q1-da-testing:edge-cases`
* owner: romanzac
* status: done
* start-date: 2025/03/24
* end-date: 2025/03/31

#### Description
This is an ongoing task.
Add edge case integration tests to cover unusual system behavior.

#### Deliverables
* [Test/da edge cases](https://github.com/logos-co/nomos-e2e-tests/pull/12)

