---
title: Security Architecture (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [devops, qa]
status: draft
tags: [architecture, security]
audience: [developers, devops, qa]
tier: T2
related:
  - ../container/example.md
  - ../../ux/accessibility/example.md
---

# Security Architecture — Template

## Threat Model (STRIDE summary)
| Threat | Mitigation |
|--------|------------|
| Spoofing | |
| Tampering | |

```mermaid
flowchart LR
  User --> IdP[Identity Provider]
  IdP --> API[API - JWT validation]
  API --> Data[Encrypted data store]
```
