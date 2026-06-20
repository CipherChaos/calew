# Cursor Agent Workflow Index

Navigable map of agent rules, playbooks, and workflow artifacts.

**Blueprint version:** 1.0.0

---

## Rules (Executable)

| File | Always apply | Invoke when |
|------|--------------|-------------|
| [rules/00-cross-agent.mdc](rules/00-cross-agent.mdc) | Yes | Every session |
| [rules/10-manager.mdc](rules/10-manager.mdc) | No | Planning, sprints, stakeholders, risks |
| [rules/20-architect.mdc](rules/20-architect.mdc) | No | Design, stack, architecture docs |
| [rules/30-developer.mdc](rules/30-developer.mdc) | No | Coding, review, refactor |
| [rules/40-qa.mdc](rules/40-qa.mdc) | No | Testing, bugs, UAT |
| [rules/50-devops.mdc](rules/50-devops.mdc) | No | CI/CD, infra, deploy |

---

## Playbooks (Comprehensive)

| Role | Playbook | Tags |
|------|----------|------|
| Manager | [agents/manager/RULE.md](agents/manager/RULE.md) | pm, sprint, risk, stakeholder |
| Architect | [agents/architect/RULE.md](agents/architect/RULE.md) | architecture, security, api, db |
| Developer | [agents/developer/RULE.md](agents/developer/RULE.md) | code, git, test, docs |
| QA | [agents/qa/RULE.md](agents/qa/RULE.md) | qa, regression, uat, security-test |
| DevOps | [agents/devops/RULE.md](agents/devops/RULE.md) | cicd, k8s, iac, monitoring |

Agent overview: [agents/README.md](agents/README.md)

---

## Workflow Artifacts

| File | Type | Purpose |
|------|------|---------|
| [workflow/communication-protocol.md](workflow/communication-protocol.md) | Process | Message formats, async norms |
| [workflow/handoff-procedures.md](workflow/handoff-procedures.md) | Process | Agent transition checklists |
| [workflow/escalation-matrix.md](workflow/escalation-matrix.md) | Process | Severity and escalation paths |
| [workflow/knowledge-transfer.md](workflow/knowledge-transfer.md) | Process | KT sessions, onboarding |
| [workflow/quality-gates.yaml](workflow/quality-gates.yaml) | Config | Pass/fail thresholds per transition |
| [workflow/architect-decision-tree.md](workflow/architect-decision-tree.md) | Process | Architect dilemma escalation vs proceed |
| [workflow/scaling-indicators.yaml](workflow/scaling-indicators.yaml) | Config | Tier detection and doc requirements |

---

## Handoff Gates

| Transition | Gate key |
|------------|----------|
| Manager → Architect | `manager_to_architect` |
| Architect → Manager | `architect_to_manager` |
| Architect → Developer | `architect_to_developer` |
| Developer → QA | `developer_to_qa` |
| QA → Developer | `qa_to_developer` |
| QA → DevOps | `qa_to_devops` |
| DevOps → Manager | `devops_to_manager` |

---

## Phase → Agent Map

| Phase | Primary agent | Key docs |
|-------|---------------|----------|
| Discovery & charter | Manager | [project-charter](../../docs/project-management/project-charter/) |
| Architecture | Architect | [architecture/](../../docs/architecture/) |
| Implementation | Developer | [api-contract](../../docs/data/api-contract/), [design-system](../../docs/ux/design-system/) |
| Verification | QA | [test strategy in qa/RULE.md](agents/qa/RULE.md) |
| Release | DevOps | [deployment](../../docs/architecture/deployment/) |

---

## Related

- [HELP.md](../HELP.md) — Agent diagrams and onboarding
- [BOOTSTRAP.md](../BOOTSTRAP.md) — AI project setup
- [docs/INDEX.md](../docs/INDEX.md) — Documentation catalog
- [docs/RELATIONSHIPS.md](../docs/RELATIONSHIPS.md) — Doc dependency graph
- [README.md](../README.md) — Repository quick start
