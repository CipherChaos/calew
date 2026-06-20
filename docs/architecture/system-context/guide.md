---
title: System Context Diagram (Guide)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: architect
reviewers: [devops, manager]
status: approved
tags: [architecture, c4, level-1]
audience: [developers, stakeholders]
tier: T1
related:
  - ../container/example.md
  - ../../data/api-contract/example.yaml
  - ../../../.cursor/agents/architect/RULE.md
---

# Guide — System Context Diagram

## When to Create
First architecture artifact after charter approval (T1+).

## Steps
1. List users and external systems from requirements
2. Draw single system box for your software
3. Label relationships with verbs (Uses, Sends, Syncs)
4. Review with Manager for scope accuracy

## Tools
- **PlantUML + C4-PlantUML** (recommended for C4)
- **Mermaid** (GitHub/Cursor native preview)
- Structurizr, IcePanel (T3)

## Versioning
Minor: new external system. Major: system scope split (new product).

## Pitfalls
- **Wrong:** Internal databases shown as external systems
- **Right:** Only systems outside your boundary

## Related
- Next: [Container diagram](../container/guide.md)
- Gate: `architect_to_developer` in quality-gates.yaml
