# Knowledge Transfer Procedures

Structured knowledge transfer (KT) between agents, team members, and releases.

---

## When KT Is Required

| Event | Minimum KT | Tier |
|-------|------------|------|
| Architect → Developer handoff | Architecture walkthrough | T1+ |
| Developer rotation / offboarding | Code + runbook session | T1+ |
| Production release | Ops runbook review | T2+ |
| Major version / breaking change | Stakeholder + support briefing | T2+ |
| Incident postmortem | Lessons learned session | P0/P1 all tiers |

---

## KT Session Structure (60–90 min)

1. **Context (10 min)** — Goals, audience, related docs
2. **Walkthrough (30 min)** — Live demo or doc tour ([INDEX.md](../../docs/INDEX.md))
3. **Hands-on (20 min)** — Recipient performs task with coach
4. **Q&A (10 min)** — Capture gaps in glossary or runbook
5. **Sign-off (5 min)** — Checklist below

---

## KT Checklist

```markdown
## KT Session Record

**Topic:** [e.g. Acme Platform deployment]
**Date:** YYYY-MM-DD
**Presenter:** [role/name]
**Audience:** [roles/names]
**Tier:** T1 | T2 | T3

### Artifacts covered
- [ ] docs/architecture/deployment/example.md
- [ ] docs/data/api-contract/example.yaml
- [ ] .cursor/agents/devops/RULE.md (rollback section)

### Recipient can independently
- [ ] Deploy to staging
- [ ] Roll back one version
- [ ] Interpret monitoring alerts
- [ ] Locate escalation contacts

### Follow-up actions
| Action | Owner | Due |
|--------|-------|-----|
| Update runbook section X | DevOps | |

**Sign-off:** Presenter ___ Recipient ___
```

---

## Onboarding Sequence (New Team Member)

| Day | Focus | Agent owner | Materials |
|-----|-------|-------------|-----------|
| 1 | Charter, glossary, tier | Manager | [project-charter](../../docs/project-management/project-charter/), [glossary](../../docs/project-management/glossary/) |
| 2 | Architecture tour | Architect | [system-context](../../docs/architecture/system-context/), [container](../../docs/architecture/container/) |
| 3 | Dev environment | Developer | [Developer RULE.md](../agents/developer/RULE.md) |
| 4 | Test approach | QA | [QA RULE.md](../agents/qa/RULE.md) |
| 5 | CI/CD and deploy | DevOps | [deployment](../../docs/architecture/deployment/), [DevOps RULE.md](../agents/devops/RULE.md) |

T1 teams may compress to 3 days; T3 adds security and compliance modules.

---

## Runbook Standards

Runbooks live in project `docs/operations/` (create per project) and must include:

- Service name and owner
- Dependencies and health checks
- Common failures and fixes
- Rollback steps (link [DevOps playbook](../agents/devops/RULE.md))
- Escalation ([escalation-matrix.md](escalation-matrix.md))

---

## Acme Platform Example

New developer KT for Acme:

1. Read [Acme charter](../../docs/project-management/project-charter/example.md)
2. Trace [order workflow sequence](../../docs/process/workflow-sequence/example.md)
3. Run API against [OpenAPI example](../../docs/data/api-contract/example.yaml)
4. Shadow staging deploy per [deployment example](../../docs/architecture/deployment/example.md)

---

## Validation

KT complete when recipient sign-off recorded and follow-up actions tracked to closure.
