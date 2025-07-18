---

title: Status QA Desktop
tags:
  - "2025q3"
  - "qa"
  - "status"
draft: false
description: Status QA Desktop

---

`vac:qa:status:2025q3-status-qa-desktop`

## Description
Collaborate with Status team to ensure that the Status Desktop app behaves as expected.
Add new automated tests to the existing e2e testing framework for new features.
Oversee testing strategy around releases.


**Alignment with VAC Narratives:**
* By helping to test the Status Desktop application, 
  VAC QA contributes directly to the narrative of internal collaboration and efficiency..
* Helps maintain a high standard for both internal and external contributions 
  by detecting discrepancies early and closing testing gaps.

## Task List

### Release Testing

* fully qualified name: `vac:qa:status:2025q3-status-qa-desktop:release-testing`
* owner: nastya
* status: in progress (10%)
* start-date: 
* end-date: 

#### Description
- Oversee testing strategy for new releases.
- Ensure that the VAC QA team, Status developers, and the community 
  provide sufficient testing to support high-quality releases.

#### Deliverables
- [fixed tests in dev PR and manually tested the change on Windows](https://github.com/status-im/status-desktop/pull/18290)


### Shell view

* fully qualified name: `vac:qa:status:2025q3-status-qa-desktop:shell-view`
* owner: nastya
* status: 
* start-date: 
* end-date: 

#### Description
- Add new automated tests for the `Shell view` feature.
- Review and assist devs with feature testing.  

#### Deliverables
- PRs


### Ethereum follow protocol

* fully qualified name: `vac:qa:status:2025q3-status-qa-desktop:eth-follow-protocol`
* owner: nastya
* status: 
* start-date: 
* end-date: 

#### Description
- Add new automated tests for the `Ethereum follow protocol` feature.
- Review and assist devs with feature testing.  

#### Deliverables
- PRs


### Backup user data

* fully qualified name: `vac:qa:status:2025q3-status-qa-desktop:backup-user-data`
* owner: nastya
* status: 
* start-date: 
* end-date: 

#### Description
- Add new automated tests for the `Backup user data` feature.
- Review and assist devs with feature testing.  

#### Deliverables
- PRs


### Maintenance

* fully qualified name: `vac:qa:status:2025q3-status-qa-desktop:maintenance`
* owner: nastya
* status: in progress (15%)
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description
- Ongoing maintenance of Status Desktop tests. This includes updating tests for changes in status,
  addressing regressions, investigating and resolving issues,
  and implementing minor improvements to the testing framework as needed.

#### Deliverables
- [chore(@e2e): disable testrail for nightly job and fix nightly tests](https://github.com/status-im/status-desktop/pull/18289)
- [bug: Application crashes when trying to mint tokens with no access to data providers](https://github.com/status-im/status-desktop/issues/18291)
- [chore(@e2e): update object names / small clean up ](https://github.com/status-im/status-desktop/pull/18328)
- [chore(@e2e): do not check for exact number of toasts when not needed](https://github.com/status-im/status-desktop/pull/18317)
- [fix(@desktop/wallet): Fix Modal heights on mobile portrait](https://github.com/status-im/status-desktop/pull/18259)
- [chore(@e2e): add retries logic if hovering fails](https://github.com/status-im/status-desktop/pull/18342)
- [bug: Can't select derivation path ](https://github.com/status-im/status-desktop/issues/18315)
- [bug: Animation for rename keypair modal is abnormally slow](https://github.com/status-im/status-desktop/issues/18316)
