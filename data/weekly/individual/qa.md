**Florin**:
Last week:
- `status:2025q4-status-go-functional-testing:waku`
	- [bug: Inconsistent replied_at timestamp format in GetVerificationRequestSentTo response](https://github.com/status-im/status-go/issues/6995)
	- [test: contact verification](https://github.com/status-im/status-go/pull/6997)
- `admin/misc`
	- Start looking at VAC units roadmap issues
	- 2 days OOO

This week:
- `admin/misc`
	- Continue with VAC units roadmap investigation
	- VAC reporting

Blockers:
- could not work on QA stuff because of VAC role changes

**Roman**:
Last week:

- `waku:2025q4-rln-smart-contract-testing:property-based` (70%)
    - chore: fuzz test expansion
    [PR 40 - in progress](https://github.com/waku-org/waku-rlnv2-contract/pull/40) 
- `waku:2025q4-rln-smart-contract-testing:security-adversarial` (80%)
    - chore: adversarial tests
    [PR 42 - in progress](https://github.com/waku-org/waku-rlnv2-contract/pull/42)
    - Lower the likelihood of set-filling spam attack 
    [Issue 45 - open](https://github.com/waku-org/waku-rlnv2-contract/issues/45)
- `admin/misc`
    - OOO 10/17
 	
This week:
- `waku:2025q4-rln-smart-contract-testing:property-based`
    - Broaden value ranges and see which tests to include in CI run
-  `waku:2025q4-rln-smart-contract-testing:security-adversarial`
    - Finish PR 42

       
Blockers:

**Aya**:
Last week:
- `status:2025q4-status-go-functional-testing:settings`(90%)
   - All APIs in settings.go covered in [PR](https://github.com/status-im/status-go/pull/6984) ( >120 test)
   - All wrappers done for setting.go in settings.py
   - Number of issues detected (will discuss with devs if it shall be considered ) currently marked as xfail 
   - Assign the PR for review
   
This week:
 - `status:2025q4-status-go-functional-testing:settings`
    - Fix review points & merge [PR](https://github.com/status-im/status-go/pull/6984)
 - `admin/misc`
     - Take another task in status-go or follow up with one of the open tasks 
 
Blockers:
- started the maternal leave

**Radek**:
Last week:
- `vac:2025q4-nim-libp2p-testing:test-plans` (15%)
  - created first draft of [test plan](https://www.notion.so/QUIC-28b8f96fb65c8018b6cdc21882cfd98a) for quic and asked for reviews
- `vac:2025q4-nim-libp2p-testing:quic` (5%)
  - started digging into nim-quic, protocol and existing test coverage
  - [fix(quic): GossipSub outbound peers](https://github.com/vacp2p/nim-libp2p/pull/1768) - merged - found one issue
  - working on 2nd PR with tests

This week:
- `vac:2025q4-nim-libp2p-testing:quic`
  - wrap up 2nd PR
  - continue with test coverage
- `vac:2025q4-nim-libp2p-testing:test-plans`
  - revise [test plan](https://www.notion.so/QUIC-28b8f96fb65c8018b6cdc21882cfd98a)

Blockers:

**Nastya**:
Last week:
- `status:2025q4-status-qa-desktop:maintenance` (63%)
    - merged https://github.com/status-im/status-desktop/pull/19047 to enhance the way of waiting for object
- `status:2025q4-status-qa-desktop:release-testing` (5%)
    - worked on testing https://github.com/status-im/status-desktop/pull/19004
    - investigated slow login issue https://github.com/status-im/status-desktop/issues/19019
    - tested https://github.com/status-im/status-desktop/pull/19022
- `status:2025q4-status-qa-desktop:e2e-windows` (100%)
    - spent a lot of time and effort and finally found how to make e2e working with Vitrual Display Driver on Windows. All changes committed, the PR with CI is not merged yet as it needs some tweaking on infra side

This week:
- `status:2025q4-status-qa-desktop:maintenance`
    - work on fixing some issues in tests that are windows-related so more tests could be enabled for windows
    - continue investigation of tests runtime
    - get back to task of using newer Squish release, they finally replied with solution but i did not have time to try it
     
Blockers:

**Magnus**:
Last week:

- `status:2025q4-status-qa-mobile:test-ci` (70%)
    - Discussion around cloud providers
    - Started refactor to support BrowserStack (https://github.com/status-im/status-desktop/issues/19088)
    - Test builds now available through Jenkins
- `status:2025q4-status-qa-mobile:port-tests` (35%)
    - Set up local test harness (rasp. pi & phones)
    - Addressing feedback for password change scenario https://github.com/status-im/status-desktop/pull/18977
- `status:2025q4-status-qa-mobile:release-testing` (10%)
    - Supported test day for mobile pre-release

This week:
- `status:2025q4-status-qa-mobile:release-testing`
    - Support mobile pre-release (triage calls etc.)
- `status:2025q4-status-qa-mobile:test-ci`
    - Finish refactor for BrowserStack
    - Add support for Jenkins


Blockers:
- BrowserStack trial issues 