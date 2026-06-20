---
title: User Journey Map (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: manager
reviewers: [qa, developer]
status: approved
tags: [ux, journey]
audience: [pm, qa]
tier: T2
related:
  - ../../STANDARD.md
---

# User Journey — Acme Platform

## Buyer: Place first order

| Stage | Action | Touchpoint | Notes |
|-------|--------|------------|-------|
| Discover | Log in via SSO | Portal | OIDC |
| Browse | Search catalog | Portal | Filter by SKU |
| Order | Add lines, submit | Portal → API | Idempotent POST |
| Track | View status | Portal | Webhook updates from ERP |
