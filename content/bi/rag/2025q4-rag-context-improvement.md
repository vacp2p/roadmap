---
title: RAG Context
tags:
  - "2025q4"
  - "bi"
  - "rag"
draft: false
description: Add more sources to the RAG context
---

`vac:bi:rag:2025q4-rag-context-improvement`


## Description

Extract the transcript from Youtube video to use it for RAG context and other possibility

## Task List

### Add Code Chunking to the RAG

* fully qualified name: `vac:bi:rag:2025q4-rag-context-improvement:add-code-chunking`
* owner: nickninov
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

https://github.com/status-im/data-docs/issues/82

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables

- Updated the RAG upload prefix logic so freshly ingested chunks no longer collide, and backfilled the newest data through the pipeline.
- Patched the Quadrant HTTPS ingestion bug and added monitoring for data freshness as the Quadrant DB grows.
- Expanded the sources dashboard with chunk counts to make it easier to audit what has been loaded.
- Fixed the embedding pipeline regression that corrupted new chunks so fresh uploads now embed cleanly again.
- Add task to dagster ETL to include code repository to the RAG context
- Write documentation in Data-docs.
- Tested VLLM deployment for context generation to validate performance for upcoming code ingestion.

### Google Meeting transcript

* fully qualified name: `vac:bi:rag:2025q4-rag-context-improvement:google-meeting-transcript`
* owner: nickninov
* status: done
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description

Include transcript from Google Meeting to the RAG context.
https://github.com/status-im/data-docs/issues/68

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables

- Debugged the meeting transcript ingestion (YouTube metadata & evaluation pipeline) and documented the outstanding edge cases.
- Add task to dagster ETL to include meeting transcript to the RAG context.
- Write documentation in Data-docs.
