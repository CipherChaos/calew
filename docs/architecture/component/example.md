---
title: Component Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer]
status: approved
tags: [architecture, c4, level-3]
audience: [developers]
tier: T2
related:
  - ../container/example.md
---

# Component Diagram — Acme Order API

```mermaid
flowchart LR
  OC[OrderController] --> OS[OrderService]
  OS --> OR[OrderRepository]
  OS --> EP[EventPublisher]
  OS --> VS[ValidationService]
  OR --> DB[(PostgreSQL)]
  EP --> Q[Message Queue]
```

| Component | Responsibility |
|-----------|----------------|
| OrderController | HTTP layer, auth check |
| OrderService | Business rules, transactions |
| OrderRepository | Persistence |
| EventPublisher | Async ERP notifications |
