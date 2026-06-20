---
title: Network Architecture (Template)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: devops
reviewers: [architect]
status: draft
tags: [architecture, network, security]
audience: [devops]
tier: T2
related:
  - ../deployment/example.md
  - ../security/example.md
---

# Network Architecture — Template

Document VPCs, subnets, ingress/egress, firewall rules.

```mermaid
flowchart TB
  subgraph public [Public Subnet]
    LB[Load Balancer]
  end
  subgraph private [Private Subnet]
    App[Application]
    DB[(Database)]
  end
  Internet --> LB --> App --> DB
```
