---

title: Nomos Data Availability Testing
tags:
  - "2025q2"
  - "qa"
  - "nomos"  
draft: true  
description: Implement data availability test plans for the Nomos project at the cluster level. 

---

`vac:qa:nomos:2025q2-da-testing`

## Description
Implement data availability test plans for the Nomos project at the cluster level, 
focusing on protocol compatibility, internal interactions, data confidentiality, and resilience against failures.

**Alignment with VAC Narratives:**
- By developing and constantly updating tests for data availability,
  VAC QA ensures that the feature's implementation aligns with high standards.
- This continuous testing helps identify any spec-related issues early,
  contributing to the RFC culture and improving spec quality.
- The effort also supports IFT's strategic objective of scaling the project’s capacity
  and ensuring a reliable system for future community involvement.

## Task List

### Protocol and API Compatibility Tests

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:protocol-api-compatibility`
* owner: romanzac
* status: done
* start-date: 2025/04/1
* end-date: 2025/04/15

#### Description
Add integration tests to verify DA works well with other blockchain components.

#### Deliverables
- [Test/protocol API compatibility](https://github.com/logos-co/nomos-e2e-tests/pull/14)


### Internal Interaction and Data Flow Tests

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:interaction-data-flow`
* owner: romanzac
* status: done
* start-date: 2025/04/16
* end-date: 2025/05/16

#### Description
Add integration tests to verify correct interaction of the internal DA components 
to ensure correct data flow and end-to-end processing.

#### Deliverables
- [Test/interaction data flow](https://github.com/logos-co/nomos-e2e-tests/pull/15)


### Data Confidentiality

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:data-confidentiality`
* owner: romanzac
* status: done
* start-date: 2025/05/19
* end-date: 2025/06/6

#### Description
Add integration tests to verify data confidentiality, 
ensuring secure communications, and controlling unauthorized access.

#### Deliverables
- [test: Da networking encryption - PoC](https://github.com/logos-co/nomos-security-tests/pull/1)
- [test: data confidentiality](https://github.com/logos-co/nomos-e2e-tests/pull/18)

### Data Integrity and Dispersal Process Resilience

* fully qualified name: `vac:qa:nomos:2025q2-da-testing:dispersal-resilience`
* owner: romanzac
* status: done
* start-date: 2025/06/9
* end-date: 2025/06/30

#### Description
Add integration tests to verify the robustness of internal processes against tampering or malformed inputs 
and maintaining the integrity of the data handling mechanisms.

#### Deliverables
- chore: Nomos node with mutated DA layer
    [PR 2](https://github.com/logos-co/nomos-security-tests/pull/2) -> cleanup into [PR 3](https://github.com/logos-co/nomos-security-tests/pull/3) is in progress
- Test/dispersal resilience
    [PR 19](https://github.com/logos-co/nomos-e2e-tests/pull/19)
- Dispersal not prevented for a blob with tampered data
    [Issue 1369 - open](https://github.com/logos-co/nomos/issues/1369)
- Error 'blob sampling timed out' too generic to hint about problem with RS encoding
    [Issue 1383 - open](https://github.com/logos-co/nomos/issues/1383)
- TF-IDF based log parsing 
    [PR 20 - merged](https://github.com/logos-co/nomos-e2e-tests/pull/20)
