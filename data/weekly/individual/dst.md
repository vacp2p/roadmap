**Alberto**:
Last week:
- `admin/misc`
    - Talking with Nomos about next steps:
        - [Nomos notion <> DST](https://nomos-tech.notion.site/Vac-Nomos-Analysis-287261aa09df80b78807ccd635921587)
- `vac:dst:status:2025q4-status-evaluation:chat-protocol-benchmarks-followup` (60%)
    - Make simple light scenario to work
        - Discovered an issue where Status has information that a bootstrap node has filter-subscribe when this is not true. Further investigation.
        - [Discord: Thread](https://discord.com/channels/1210237582470807632/1427311444340248688)
        - [Notion: Status Light and Waku Filter](https://www.notion.so/Status-light-and-nWaku-filter-2858f96fb65c8019ac2af3a84c688d68)
    - Create structure for multiple consumers when working with requests
        - [Github PR: Multiple consumers #35](https://github.com/vacp2p/status-benchmarks/pull/35)
        - This automatically fixes latency calculation
    - Created new log level for better debugging
        - Also adjusted other logs for easier tracking of events
        - [Github PR: Logger adjustments #37](https://github.com/vacp2p/status-benchmarks/pull/37)
- `vac:dst:waku:2025q4-waku-scaling:TWN-supports-RLN-tree` (30%)
    - Check how to include memberships in the RLN tree
    - Check how RLN is used in waku simulator
    - Check how RLNKeystore works
- `vac:dst:vac:2025q4-libp2p-evaluation:regression-testing` (recurrent)
    - Analysis nim-libp2p v1.14
        - [Notion Report](https://www.notion.so/Nim-libp2p-v1-14-0-regression-testing-October-2025-28d8f96fb65c803ba789ccdb73753cab)
- Review:
    - [Github PR: mix-integeration # 7](https://github.com/vacp2p/dst-libp2p-test-node/pull/7)
    - [Github PR: Fix nimlibp2p tracer #161](https://github.com/vacp2p/10ksim/pull/161)
    - [Github PR: Move metadata helpers to base_experiment #162](https://github.com/vacp2p/10ksim/pull/162)
    - [Github PR: nimlibp2p mix node deployment changes #137](https://github.com/vacp2p/10ksim/pull/137)
    - [Github PR: Mixnet analysis changes #163](https://github.com/vacp2p/10ksim/pull/163)
    - [Github PR: Allow multiple match groups for the same query in victoria_reader.py #164](https://github.com/vacp2p/10ksim/pull/164)

This week:
- `vac:dst:status:2025q4-status-evaluation:chat-protocol-benchmarks-followup`
    - Investigate bootstrap filter issue in meeting
    - Refactor other scenarios
- `vac:dst:waku:2025q4-waku-scaling:TWN-supports-RLN-tree`
    - Fill RLN tree and do benchmark

Blockers:

**Pearson**:
Last week:
- `admin/misc`
    - Document issues in [notion: DST Results summary](https://www.notion.so/DST-Results-summary-d7f0381afba343c98f0d8b1ef0193044)
    - Added [notion: jswaku issues](https://www.notion.so/DST-Results-summary-d7f0381afba343c98f0d8b1ef0193044?source=copy_link#28e8f96fb65c80768f78d65040ce29f3)
    - Added [notion: mixnet issues](https://www.notion.so/DST-Results-summary-d7f0381afba343c98f0d8b1ef0193044?source=copy_link#2918f96fb65c80609a36d8d50b56ff21)
- `vac:dst:ift:2025q4-dst-tooling:general-tooling` (recurrent)
    - [Github PR: Fix nimlibp2p tracer #161](https://github.com/vacp2p/10ksim/pull/161)
    - [Github PR: Move metadata helpers to base_experiment #162](https://github.com/vacp2p/10ksim/pull/162)
    - [Github PR: nimlibp2p mix node deployment changes #137](https://github.com/vacp2p/10ksim/pull/137)
    - [Github PR: Mixnet analysis changes #163](https://github.com/vacp2p/10ksim/pull/163)
    - [Github PR: Allow multiple match groups for the same query in victoria_reader.py #164](https://github.com/vacp2p/10ksim/pull/164)
- `vac:dst:ift:2025q4-dst-tooling:complete-deployment-refactor` (30%)
    - initContainers, commands, etc. working for lightpush, filter
    - Store node need a few tweaks, but near complete
- Review `vac:dst:ift:2025q4-libp2p-evaluation:mix-in-nim-libp2p-node`:
    - [Github PR: added mix support to test node #7](https://github.com/vacp2p/dst-libp2p-test-node/pull/7#pullrequestreview-3340450178)
- Review `vac:dst:status:2025q4-status-evaluation:chat-protocol-benchmarks-followup`
    - [Github PR: Multiple consumers #35](https://github.com/vacp2p/status-benchmarks/pull/35)


This week:
- `vac:dst:ift:2025q4-dst-tooling:complete-deployment-refactor`
    - Create draft PR as early as possible
    - "Frontend": Builder class and Config class. Right now it's helper/utility functions.
- `vac:dst:waku:2025q4-waku-scaling:optimise-browser-bootstrapping`

Blockers:

**Farooq**:
Last week:
- `vac:dst:ift:2025q4-libp2p-evaluation:mix-in-nim-libp2p-node` (100%)
    - Finalized work on mix integeration PR for the refactored node. The PR is ready for merging
		- [Github PR: mix-integeration # 7](https://github.com/vacp2p/dst-libp2p-test-node/pull/7) 	
- `vac:dst:ift:2025q4-libp2p-evaluation:go-libp2p-node` (60%)
    - Worked on running go-libp2p node alongside nim node.  
		- Both, nim refactored node and go-libp2p nodes are working fine in shadow (using yamux. mplex is obsolete in go-libp2p)
		- Still need to finalize work on quic in go test node
		- Still need to log prometheus metrics in go test node
		- doing sanity checks in go-libp2p test node.
		- [Github PR: go-libp2p-test-node # 8](https://github.com/vacp2p/dst-libp2p-test-node/pull/8)

This week:
- `vac:dst:ift:2025q4-libp2p-evaluation:go-libp2p-node`
    - Finalize go-libp2p test node
    - Test go, refactored nim test nodes in k8s

Blockers:
