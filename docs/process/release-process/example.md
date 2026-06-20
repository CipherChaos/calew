---
title: Release Process (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: devops
reviewers: [manager, qa]
status: approved
tags: [process, release]
audience: [devops, developers]
tier: T2
related:
  - ../../STANDARD.md
---

# Release Process — Acme Platform

- **Cadence:** Bi-weekly, Tuesday 02:00 UTC
- **RC tag:** `v{major}.{minor}.{patch}-rc1`
- **Approval:** Manager + QA for T2+
- **Rollback:** Redeploy previous artifact within 15 minutes
