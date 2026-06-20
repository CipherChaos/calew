---
title: Code Review Process (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: developer
reviewers: [architect, qa]
status: approved
tags: [process, review]
audience: [developers]
tier: T1
related:
  - ../../STANDARD.md
---

# Code Review — Acme Platform

- **PR size:** ≤400 lines preferred
- **Required reviewers:** 1 dev; Architect for API/schema changes
- **CI:** lint + unit + integration must pass
- **Branch naming:** `feature/REQ-*`, `fix/BUG-*`
