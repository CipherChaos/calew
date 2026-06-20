---
title: Work Breakdown Structure (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: manager
reviewers: [architect, developer]
status: approved
tags: [pm, wbs, planning]
audience: [team, stakeholders]
tier: T1
related:
  - ../project-charter/example.md
  - ../sprint-planning/example.md
  - ../../DIAGRAMS.md
---

# Work Breakdown Structure — Acme Platform

```mermaid
mindmap
  root((Acme Platform))
    1 Foundation
      1.1 Charter and glossary
      1.2 Risk and tier
    2 Architecture
      2.1 C4 L1/L2
      2.2 ERD API ESD
      2.3 ERP integration design
    3 Implementation
      3.1 Order API
      3.2 Portal UI
      3.3 Integration worker
    4 Verification
      4.1 Test automation
      4.2 UAT
    5 Release
      5.1 CI/CD
      5.2 Production deploy
```

## Text tree

```
Acme Platform
├── 1. Foundation (Manager)
│   ├── 1.1 Charter & glossary
│   └── 1.2 Risk & tier
├── 2. Architecture (Architect)
│   ├── 2.1 C4 + ERD + API
│   └── 2.2 Integration design
├── 3. Implementation (Developer)
│   ├── 3.1 Order API
│   └── 3.2 Portal UI
├── 4. Verification (QA)
└── 5. Release (DevOps)
```

Leaf tasks map to [sprint-planning/example.md](../sprint-planning/example.md) stories.
