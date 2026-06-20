---
title: Workflow Sequence Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: draft
tags: [process, sequence]
audience: [developers]
tier: T1
related:
  - ../../STANDARD.md
---

# Workflow Sequence — Template

Document request/response flows for key use cases.

```mermaid
sequenceDiagram
  participant User
  participant API
  participant DB
  User->>API: Request
  API->>DB: Query
  DB-->>API: Result
  API-->>User: Response
```
