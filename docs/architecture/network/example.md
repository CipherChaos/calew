---
title: Network Architecture (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: devops
reviewers: [architect]
status: approved
tags: [architecture, network, security]
audience: [devops]
tier: T2
related:
  - ../deployment/example.md
  - ../security/example.md
---

# Network Architecture — Acme Platform

- VPC 10.0.0.0/16
- Public subnets: ALB, NAT
- Private subnets: EKS nodes, RDS, Redis
- WAF on CloudFront; TLS 1.2+ termination at ALB
- Egress to ERP allowlist via NAT gateway

```mermaid
flowchart LR
  Internet --> WAF --> ALB
  ALB --> EKS[EKS private]
  EKS --> RDS[RDS private]
  EKS --> NAT --> ERP[ERP allowlist]
```
