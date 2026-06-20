---
title: Container Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, devops]
status: approved
tags: [architecture, c4, level-2]
audience: [developers, devops]
tier: T1
related:
  - ../system-context/example.md
  - ../deployment/example.md
---

# Container Diagram — Acme Platform

| Container | Technology | Responsibility |
|-----------|------------|----------------|
| Web Portal | SPA | Buyer and ops UI |
| Order API | Stateless service | Orders, catalog, auth |
| Integration Worker | Worker service | ERP sync jobs |
| PostgreSQL | RDBMS | Transactional data |
| Redis | Cache | Sessions, rate limits |

```mermaid
flowchart TB
  subgraph acme [Acme Platform]
    Web[Web Portal]
    API[Order API]
    Worker[Integration Worker]
    DB[(PostgreSQL)]
    Cache[(Redis)]
  end
  User[Users] --> Web
  Web --> API
  API --> DB
  API --> Cache
  Worker --> DB
  Worker --> ERP[ERP APIs]
```
