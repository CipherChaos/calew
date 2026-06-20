---
title: Risk Assessment (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: manager
reviewers: [architect, devops]
status: approved
tags: [pm, risk]
audience: [stakeholders]
tier: T1
related:
  - ../../STANDARD.md
---

# Risk Assessment — Acme Platform

| ID | Risk | P | I | Score | Mitigation |
|----|------|---|---|-------|------------|
| R1 | ERP webhook delays | 3 | 4 | 12 | Retry queue + DLQ |
| R2 | SSO IdP outage | 2 | 5 | 10 | Cached session grace period |
| R3 | Scope creep on integrations | 4 | 3 | 12 | SCR process, MoSCoW |
