---
title: Data Lifecycle (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [devops, manager]
status: approved
tags: [data, lifecycle]
audience: [architect, devops]
tier: T3
related:
  - ../../STANDARD.md
---

# Data Lifecycle — Acme Platform

| Data class | Retention | Archive | Delete |
|------------|-----------|---------|--------|
| Orders | 7 years | S3 Glacier after 2y | Secure wipe after retention |
| Audit logs | 3 years | — | — |
| Session tokens | 24 hours | — | Auto-expire |
