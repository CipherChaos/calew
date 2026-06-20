---
title: Data Flow Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: approved
tags: [data, dfd]
audience: [developers, architect]
tier: T2
related:
  - ../../STANDARD.md
---

# Data Flow — Acme Platform

```mermaid
flowchart LR
  Portal[Web Portal] --> API[Order API]
  API --> PG[(PostgreSQL)]
  API --> Q[Message Queue]
  Worker[Integration Worker] --> Q
  Worker --> ERP[Customer ERP]
```
