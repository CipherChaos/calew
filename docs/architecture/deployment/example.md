---
title: Deployment Diagram (Example)
version: 1.0.0
created: 2026-06-20
updated: 2026-06-20
owner: devops
reviewers: [architect]
status: approved
tags: [architecture, deployment, infra]
audience: [devops, developers]
tier: T1
related:
  - ../network/example.md
---

# Deployment Diagram — Acme Platform

Production: AWS eu-west-1, EKS cluster, RDS PostgreSQL Multi-AZ, ElastiCache Redis.

```mermaid
flowchart TB
  Users[Users] --> CF[CloudFront]
  CF --> ALB[Application LB]
  ALB --> EKS[EKS - Order API + Worker pods]
  EKS --> RDS[(RDS PostgreSQL)]
  EKS --> Redis[(ElastiCache)]
  Worker[Worker pods] --> ERP[ERP endpoints]
```

| Env | Cluster | DB |
|-----|---------|-----|
| staging | acme-stg | db.t3.medium |
| prod | acme-prod | db.r6g.large Multi-AZ |
