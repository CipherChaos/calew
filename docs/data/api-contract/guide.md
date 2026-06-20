---
title: API Contract (OpenAPI) (Guide)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [developer, qa]
status: approved
tags: [data, api, openapi]
audience: [developers, qa]
tier: T1
related:
  - ../entity-relationship/example.md
  - ../../architecture/container/example.md
---

# Guide — API Contract

OpenAPI is source of truth. Gate: `architect_to_developer`.

- Version breaking changes with `/v2` prefix
- Include standard error envelope with correlationId
- Idempotency-Key header on POST /orders
