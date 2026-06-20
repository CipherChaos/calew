# DevOps Agent Playbook

**Role:** CI/CD, infrastructure, deployment, monitoring, backup, and rollback. Closes the loop back to Manager after release.

**Invoke in Cursor:** `@50-devops`  
**Rule file:** [50-devops.mdc](../../rules/50-devops.mdc)

---

## 1. Activation Triggers

- Receiving handoff from QA (`qa_to_devops`)
- CI/CD pipeline setup and maintenance
- Infrastructure as code, containerization
- Deployment to staging/production
- Monitoring, alerting, backup verification
- Incident response and rollback

---

## 2. Environment Standards

| Env | Purpose | Deploy trigger |
|-----|---------|----------------|
| dev | Developer integration | merge to main/develop |
| QA | Test execution | QA request or CI promote |
| staging | Pre-prod validation | release candidate tag |
| prod | Live users | approved release + change window |

Document in [deployment/example.md](../../../docs/architecture/deployment/example.md).

---

## 3. CI/CD Pipeline Requirements

**All tiers:**

- Lint and unit tests on every PR
- Build artifact on merge
- Secrets never in repo; use env or secret manager

**T2+:**

- Integration tests in CI
- Dependency and container scan
- Staged deploy with smoke tests

**T3:**

- Manual approval gate for production
- Blue/green or canary with automated rollback triggers

---

## 4. Deployment Procedure

1. Verify gate `qa_to_devops` — rollback plan, secrets checklist, RC tag
2. Deploy to staging; run smoke tests
3. Production deploy per change window
4. Post-deploy smoke; verify monitoring dashboards
5. Record deployment in deployment log
6. Hand off to Manager (`devops_to_manager`)

---

## 5. Deployment Rollback Strategies

| Strategy | When |
|----------|------|
| Redeploy previous artifact | Fast rollback; default T1/T2 |
| Blue/green switch | Zero-downtime; T2+ |
| DB migration rollback | Only if backward-compatible; else forward-fix |

Document rollback steps in runbook before each production deploy.

---

## 6. Monitoring and Observability

- Health endpoints on all services
- Metrics: latency p95, error rate, saturation
- Logs: structured JSON with correlationId
- Alerts: P0 pages on-call; P1 ticket within 15m (T2+)

Link dashboards in handoff to Manager.

---

## 7. Backup and DR

| Tier | Requirement |
|------|-------------|
| T1 | Daily DB backup; restore tested quarterly |
| T2 | Automated backup; restore drill each release |
| T3 | Multi-region DR; RPO/RTO documented |

---

## 8. Validation Rules

| ID | Rule |
|----|------|
| O-V1 | CI pipeline green for release artifact |
| O-V2 | Post-deploy smoke pass |
| O-V3 | Rollback tested or documented in staging |
| O-V4 | Monitoring live for new/changed services |

---

## 9. Handoff Checklist — DevOps → Manager

See [handoff-procedures.md](../../workflow/handoff-procedures.md#devops--manager).

Deliver: deployment record, smoke results, dashboard links (T2+), retrospective scheduled.

---

## 10. Acme Platform Reference

[deployment/example.md](../../../docs/architecture/deployment/example.md), [network/example.md](../../../docs/architecture/network/example.md)

---

## 11. Cross-References

- Architect: [architect/RULE.md](../architect/RULE.md)
- QA: [qa/RULE.md](../qa/RULE.md)
- Incident: [incident-response/example.md](../../../docs/process/incident-response/example.md)
- Release: [release-process/example.md](../../../docs/process/release-process/example.md)
