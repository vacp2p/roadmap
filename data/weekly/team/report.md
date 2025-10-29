**QA**:
highlights:
- Contact verification coverage in status-go now runs end-to-end, uncovering a replied_at timestamp bug for the Waku verification flow.
- RLN contract property and adversarial suites progressed, with spam mitigation work continuing alongside CI gating decisions.
- Settings.go automation reached complete API coverage with more than 120 tests awaiting review feedback before merge.
- Nim-libp2p QUIC initiative produced a reviewed test plan, merged an outbound peer fix, and readied a follow-up test PR.
- Desktop and mobile QA advanced Windows E2E readiness and BrowserStack CI despite ongoing trial limitations.

Last week:
- `status:2025q4-status-go-functional-testing:waku`
  - [Issue 6995: inconsistent replied_at timestamp](https://github.com/status-im/status-go/issues/6995) was reported after running the contact verification suite.
  - [PR 6997: contact verification](https://github.com/status-im/status-go/pull/6997) expanded Waku functional coverage.
- `admin/misc`
  - Started reviewing VAC units roadmap issues.
  - OOO: 3 CC days.
- `waku:2025q4-rln-smart-contract-testing:property-based`
  - [PR 40: fuzz test expansion](https://github.com/waku-org/waku-rlnv2-contract/pull/40) remained in progress.
- `waku:2025q4-rln-smart-contract-testing:security-adversarial`
  - Advanced [PR 42: adversarial tests](https://github.com/waku-org/waku-rlnv2-contract/pull/42) and documented spam mitigation follow-up in [Issue 45](https://github.com/waku-org/waku-rlnv2-contract/issues/45).
- `status:2025q4-status-go-functional-testing:settings`
  - [PR 6984: settings.go tests](https://github.com/status-im/status-go/pull/6984) now covers every API with more than 120 checks and refreshed Python wrappers, with xfail issues logged for developer review.
- `vac:2025q4-nim-libp2p-testing:test-plans`
  - Published the [QUIC test plan draft](https://www.notion.so/QUIC-28b8f96fb65c8018b6cdc21882cfd98a) for feedback.
- `vac:2025q4-nim-libp2p-testing:quic`
  - Merged [PR 1768: GossipSub outbound peers fix](https://github.com/vacp2p/nim-libp2p/pull/1768), reviewed nim-quic coverage, and prepared a follow-up test PR.
- `status:2025q4-status-qa-desktop:maintenance`
  - Merged [PR 19047: improved wait for object](https://github.com/status-im/status-desktop/pull/19047) to steady desktop automation.
- `status:2025q4-status-qa-desktop:release-testing`
  - Tested [PR 19004](https://github.com/status-im/status-desktop/pull/19004), investigated [Issue 19019: slow login](https://github.com/status-im/status-desktop/issues/19019), and verified [PR 19022](https://github.com/status-im/status-desktop/pull/19022).
- `status:2025q4-status-qa-desktop:e2e-windows`
  - Enabled Windows E2E locally via Virtual Display Driver; CI merge depends on pending infra tweaks.
- `status:2025q4-status-qa-mobile:test-ci`
  - Compared cloud providers, refactored toward BrowserStack integration ([Issue 19088](https://github.com/status-im/status-desktop/issues/19088)), and exposed Jenkins test builds.
- `status:2025q4-status-qa-mobile:port-tests`
  - Set up the local test harness (Raspberry Pi and phones) and addressed feedback on [PR 18977: password change scenario](https://github.com/status-im/status-desktop/pull/18977).
- `status:2025q4-status-qa-mobile:release-testing`
  - Supported the mobile pre-release test day.

This week:
- `admin/misc`
  - Continue the VAC units roadmap investigation, handle VAC reporting, and line up additional status-go follow-ups as capacity allows.
- `waku:2025q4-rln-smart-contract-testing:property-based`
  - Broaden value ranges and decide which checks enter CI.
- `waku:2025q4-rln-smart-contract-testing:security-adversarial`
  - Finish [PR 42](https://github.com/waku-org/waku-rlnv2-contract/pull/42).
- `status:2025q4-status-go-functional-testing:settings`
  - Address review feedback and merge [PR 6984](https://github.com/status-im/status-go/pull/6984).
- `vac:2025q4-nim-libp2p-testing:quic`
  - Wrap up the follow-up PR and extend QUIC coverage.
- `vac:2025q4-nim-libp2p-testing:test-plans`
  - Revise the [QUIC test plan](https://www.notion.so/QUIC-28b8f96fb65c8018b6cdc21882cfd98a).
- `status:2025q4-status-qa-desktop:maintenance`
  - Triage Windows-specific failures, review test runtimes, and trial the newer Squish release.
- `status:2025q4-status-qa-mobile:release-testing`
  - Continue mobile pre-release support and triage.
- `status:2025q4-status-qa-mobile:test-ci`
  - Complete the BrowserStack refactor and add Jenkins support.

Blockers:
- Florin: VAC role changes limiting QA bandwidth.
- Aya: Maternal leave reducing availability.
- Magnus: BrowserStack trial limitations delaying CI integration.

**DST**:
highlights:
- Light benchmark scenario now supports multi-consumer requests and improved logging, tightening visibility into bootstrap filter mismatches.
- RLN tree research clarified membership handling, simulator usage, and keystore expectations ahead of upcoming benchmarks.
- 10ksim tooling gained tracer fixes, metadata helpers, and mixnet analysis updates across a five-PR batch.
- Mix-enabled Nim test node PR is ready while Go node validation in shadow highlighted QUIC and Prometheus follow-ups.

Last week:
- `admin/misc`
  - Coordinated next steps with Nomos ([Vac-Nomos analysis](https://nomos-tech.notion.site/Vac-Nomos-Analysis-287261aa09df80b78807ccd635921587)).
- `vac:dst:status:2025q4-status-evaluation:chat-protocol-benchmarks-followup`
  - Brought the light scenario online and investigated bootstrap filter discrepancies ([Discord thread](https://discord.com/channels/1210237582470807632/1427311444340248688); [Status light & Waku filter notes](https://www.notion.so/Status-light-and-nWaku-filter-2858f96fb65c8019ac2af3a84c688d68)).
  - Implemented multi-consumer handling improving latency calculations via [PR 35](https://github.com/vacp2p/status-benchmarks/pull/35).
  - Added logging adjustments for better observability via [PR 37](https://github.com/vacp2p/status-benchmarks/pull/37).
- `vac:dst:waku:2025q4-waku-scaling:TWN-supports-RLN-tree`
  - Researched RLN membership inclusion, simulator integration, and keystore usage.
- `vac:dst:vac:2025q4-libp2p-evaluation:regression-testing`
  - Analyzed nim-libp2p v1.14 regressions in the [Notion report](https://www.notion.so/Nim-libp2p-v1-14-0-regression-testing-October-2025-28d8f96fb65c803ba789ccdb73753cab).
- `vac:dst:ift:2025q4-dst-tooling:general-tooling`
  - Reviewed and merged tracer and mixnet fixes across [PR 161](https://github.com/vacp2p/10ksim/pull/161), [PR 162](https://github.com/vacp2p/10ksim/pull/162), [PR 137](https://github.com/vacp2p/10ksim/pull/137), [PR 163](https://github.com/vacp2p/10ksim/pull/163), and [PR 164](https://github.com/vacp2p/10ksim/pull/164).
- `vac:dst:ift:2025q4-dst-tooling:complete-deployment-refactor`
  - Implemented initContainers and command wiring for lightpush/filter; store node updates are nearing completion.
- `vac:dst:ift:2025q4-libp2p-evaluation:mix-in-nim-libp2p-node`
  - Readied [PR 7: mix integration](https://github.com/vacp2p/dst-libp2p-test-node/pull/7) for merge.
- `vac:dst:ift:2025q4-libp2p-evaluation:go-libp2p-node`
  - Ran Go and Nim nodes together in shadow; outstanding QUIC, Prometheus metrics, and sanity checks tracked in [PR 8](https://github.com/vacp2p/dst-libp2p-test-node/pull/8).

This week:
- `vac:dst:status:2025q4-status-evaluation:chat-protocol-benchmarks-followup`
  - Investigate bootstrap filter issues in coordination meetings and refactor related scenarios.
- `vac:dst:waku:2025q4-waku-scaling:TWN-supports-RLN-tree`
  - Populate the RLN tree and run benchmarks.
- `vac:dst:ift:2025q4-dst-tooling:complete-deployment-refactor`
  - Create the draft PR and build dedicated builder/config classes.
- `vac:dst:waku:2025q4-waku-scaling:optimise-browser-bootstrapping`
  - Focus on browser bootstrapping optimization tasks.
- `vac:dst:ift:2025q4-libp2p-evaluation:go-libp2p-node`
  - Finalize the Go test node and validate the Go/Nim nodes in Kubernetes.

Blockers:
- None reported.

**Nim**:
highlights:
- Nimble maintenance delivered fixes for package list hangs, install symlinks, warnings, and tempDir regressions.
- Proposed resolutions for nim-metrics and nim-json serialization regressions while collecting feedback from nwaku stakeholders.
- CBOR serialization suite gained regression coverage and improved comptime testing through new nim-unittest2 capabilities.
- Confutils modernization removed legacy compiler flags and set the stage for uncheckedAssign cleanup and documentation updates.

Last week:
- `ift:2025q1-nimble`
  - Researched fixes for [nim-metrics PR 98](https://github.com/status-im/nim-metrics/pull/98) and [nim-json-serialization PR 136](https://github.com/status-im/nim-json-serialization/pull/136), plus several nwaku issues.
  - Interviewed Chris and Constantine for roadmap context.
  - Merged maintenance in [PR 1494](https://github.com/nim-lang/nimble/pull/1494), [PR 1492](https://github.com/nim-lang/nimble/pull/1492), [PR 1490](https://github.com/nim-lang/nimble/pull/1490), and [PR 1488](https://github.com/nim-lang/nimble/pull/1488).
- `vac:nim:ift:2025q3-nim-core-libs:nim-cbor-serialization`
  - Added regression coverage via [PR 110](https://github.com/status-im/nim-serialization/pull/110) and strengthened comptime testing through [PR 59](https://github.com/status-im/nim-unittest2/pull/59) and [PR 60](https://github.com/status-im/nim-unittest2/pull/60).
- `vac:nim:ift:2025q3-nim-core-libs:nim-confutils`
  - Removed the `-d:nimOldCaseObjects` requirement in [PR 117](https://github.com/status-im/nim-confutils/pull/117) and released [nim-json-serialization v0.4.4](https://github.com/status-im/nim-json-serialization/pull/138).

This week:
- `ift:2025q1-nimble`
  - Investigate why [nim-metrics PR 98](https://github.com/status-im/nim-metrics/pull/98) behaves on Nim 2.x without `config.nims`.
  - Refine `include.paths`, support the nwaku-as-lib flow, and continue Nimble 1.0 preparations.
- `vac:nim:ift:2025q3-nim-core-libs:nim-confutils`
  - Replace `{.cast(uncheckedAssign).}` usage and document nim-serialization extension points.

Blockers:
- None reported.

Notes for Florin:
- Counted Roman’s “OOO 10/17” as one CC day and marked it as deduced; please confirm the duration.
- Aya’s maternal leave is flagged as a blocker but not converted to CC days because the coverage window is unclear—guidance welcome for future reports.
