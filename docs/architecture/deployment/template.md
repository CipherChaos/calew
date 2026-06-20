---
title: Deployment Diagram (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: devops
reviewers: [architect]
status: draft
tags: [architecture, deployment, infra]
audience: [devops, developers]
tier: T1
related:
  - ../network/example.md
---

# Deployment Diagram — Template

## Environments
| Env | Purpose | URL pattern |
|-----|---------|-------------|
| dev | | |
| staging | | |
| prod | | |

```mermaid
flowchart TB
  subgraph cloud [Cloud Region]
    LB[Load Balancer] --> App[App Instances]
    App --> DB[(Database)]
  end
  Users[Users] --> LB
```
