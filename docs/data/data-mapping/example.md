---
title: Data Mapping (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: developer
reviewers: [architect]
status: approved
tags: [data, mapping]
audience: [developers]
tier: T3
related:
  - ../../STANDARD.md
---

# Data Mapping — Acme Platform

| Acme field | ERP field | Transform |
|------------|-----------|----------|
| order.id | external_ref | UUID string |
| order.status | state | enum map: PENDING→open |
| order_line.quantity | qty | integer |
