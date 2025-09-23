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
* status: in progress (90%)
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description
- Oversee testing strategy for new releases.
- Ensure that the VAC QA team, Status developers, and the community 
  provide sufficient testing to support high-quality releases.

#### Deliverables
- [fixed tests in dev PR and manually tested the change on Windows](https://github.com/status-im/status-desktop/pull/18290)
- [bug: Can't search for emoji, no items in search results](https://github.com/status-im/status-desktop/issues/18362)
- [bug: Saved address is not appearing in settings list until saved addresses section is reopened](https://github.com/status-im/status-desktop/issues/18364)
- [bug: Change password background screen is magenta](https://github.com/status-im/status-desktop/issues/18350)
- [chore: update status-go](https://github.com/status-im/status-desktop/pull/18373)
- [bug: Backup seed phrase card is missing on home page](https://github.com/status-im/status-desktop/issues/18374)
- [chore: update status-go](https://github.com/status-im/status-desktop/pull/18373)
- [helped with testing of task: `refactor: Move Community Access & Permissions to modular store architecture`](https://github.com/status-im/status-desktop/pull/18384)
- [bug: Can't send on base sepolia](https://github.com/status-im/status-desktop/issues/18395)
- [bug: fatal error: concurrent map writes](https://github.com/status-im/status-desktop/issues/18396)
- [chore: bump status-go to get fix for base chain estimations](https://github.com/status-im/status-desktop/pull/18411)
- [bug: Banned community member does not see the screen saying that he is banned from this community](https://github.com/status-im/status-desktop/issues/18412)
- [bug: Can't quit the app with right click](https://github.com/status-im/status-desktop/issues/18458)
- [chore(@e2e): small adjustments in the object references](https://github.com/status-im/status-desktop/pull/18308/commits/ae0e04fb8830d024c438fa462e654a851f926159)
- [bug: Profile showcase popup is shown after being dismissed and app is restarted](https://github.com/status-im/status-desktop/issues/18471)
- [tested: chore: Bump status-go](https://github.com/status-im/status-desktop/pull/18495)
- [bug: Changing display name a couple of times in a row stops syncing the updates](https://github.com/status-im/status-desktop/issues/18503)
- [bug: Windows: can't set any image (profile, community) ](https://github.com/status-im/status-desktop/issues/18524)
- [bug: Action buttons in banners are not working, buttons are misplaced](https://github.com/status-im/status-desktop/issues/18555)
- [tested: feat(browser): restore the main browser section](https://github.com/status-im/status-desktop/pull/18539)
- [tested: Fix banners on Mac](https://github.com/status-im/status-desktop/pull/18558)
- [bug: Login process stuck when internet connection is throttled](https://github.com/status-im/status-desktop/issues/18569)
- [bug: SSLError: HTTPSConnectionPool(host='status.app', port=443): Max retries exceeded with url](https://github.com/status-im/status-desktop/issues/18601)
- [tested: ci: fix pcsc run dir](https://github.com/status-im/status-desktop/pull/18754)
- [tested: pcscd: auto exit when not in use](https://github.com/status-im/status-desktop/pull/18767)
- [tested: fix: disable QML cache on Qt < 6.9.2](https://github.com/status-im/status-desktop/pull/18775)
- [bug: Windows: qml errors and warnings](https://github.com/status-im/status-desktop/issues/18808)
- [tested: Upgrade qt to 6.9.2](https://github.com/status-im/status-desktop/pull/18814)
- [bug: can't pair devices on windows](https://github.com/status-im/status-desktop/issues/18846)

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
* status: in progress (40%)
* start-date: 2025/09/15
* end-date: 2025/09/30

#### Description
- Add new automated tests for the `Backup user data` feature.
- Review and assist devs with feature testing.  

#### Deliverables
- PRs


### Maintenance

* fully qualified name: `vac:qa:status:2025q3-status-qa-desktop:maintenance`
* owner: nastya
* status: in progress (90%)
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
- [chore(@e2e): bring back change password test](https://github.com/status-im/status-desktop/pull/18351)
- [chore(@e2e): saved address in settings now is removed as well](https://github.com/status-im/status-desktop/pull/18368)
- [ci: add tests/e2e to GitHub jenkins jobs table](https://github.com/status-im/status-desktop/pull/18380)
- [chore(@e2e): back up seed from home](https://github.com/status-im/status-desktop/pull/18390)
- [chore(@e2e): fix editing status account test](https://github.com/status-im/status-desktop/pull/18398)
- [chore(@e2e): fix toast messages method and seed phrase import](https://github.com/status-im/status-desktop/pull/18407)
- [chore(@e2e): retry decorator logic ](https://github.com/status-im/status-desktop/pull/18414)
- [chore(@e2e): fix navigation for advanced section](https://github.com/status-im/status-desktop/pull/18427)
- [chore(@e2e): fix for keypair renaming](https://github.com/status-im/status-desktop/pull/18445)
- [chore(@e2e): shorten test images names to stop insulting jenkins](https://github.com/status-im/status-desktop/pull/18470)
- [fixed tests in dev PR https://github.com/status-im/status-desktop/pull/18672]
- [fixed tests in dev PR https://github.com/status-im/status-desktop/pull/18603]
- [fixed tests in dev PR https://github.com/status-im/status-desktop/pull/18574]
- [chore(@e2e): update method for contact selection](https://github.com/status-im/status-desktop/pull/18735)
- [tests(@e2e): update method to upload image to use base64 format](https://github.com/status-im/status-desktop/pull/18726)
- [fixed tests in dev PR https://github.com/status-im/status-desktop/pull/18532]
- [fixed tests in dev PR https://github.com/status-im/status-desktop/pull/18608]
- [chore(@e2e): update readme](https://github.com/status-im/status-desktop/pull/18787)
- [chore(@e2e): temp disable nft test, it fails because collectibles are loading more than a minute](https://github.com/status-im/status-desktop/pull/18783)
- [Tests: fix TextEdit](https://github.com/status-im/status-desktop/pull/18807)
- [tested: Upgrade qt to 6.9.2](https://github.com/status-im/status-desktop/pull/18814)
- [tested: WIP: feat(e2e): add windows pipeline](https://github.com/status-im/status-desktop/pull/18724)

### Measure app load time

* fully qualified name: `vac:qa:status:2025q3-status-qa-desktop:app-load-time`
* owner: nastya
* status: in progress (20%)
* start-date: 2025/08/14
* end-date: 2025/09/08

#### Description
- Track UI loading time of the desktop app wallet screens.

#### Deliverables
- [tests: measure load time till assets are displayed](https://github.com/status-im/status-desktop/pull/18592)
