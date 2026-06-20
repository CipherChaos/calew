---
title: Security Architecture (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [devops, qa]
status: approved
tags: [architecture, security]
audience: [developers, devops, qa]
tier: T2
related:
  - ../container/example.md
  - ../../ux/accessibility/example.md
---

# Security Architecture — Acme Platform

| Control | Implementation |
|---------|----------------|
| AuthN | OIDC via corporate IdP |
| AuthZ | RBAC: buyer, ops, admin |
| Transport | TLS 1.2+ end-to-end |
| Data at rest | RDS encryption, S3 SSE |
| Secrets | AWS Secrets Manager |
| Audit | CloudTrail + app audit log |

STRIDE: ERP webhook tampering mitigated by HMAC signatures and replay window.

```mermaid
flowchart TB
  User --> OIDC[OIDC IdP]
  OIDC --> Portal[Web Portal]
  Portal --> API[Order API - JWT + RBAC]
  API --> DB[(Encrypted RDS)]
```
