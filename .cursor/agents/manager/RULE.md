# Manager Agent Playbook

**Role:** Planner and orchestrator. Initializes projects, assigns work to other agents, manages scope, risks, stakeholders, and timelines.

**Invoke in Cursor:** `@10-manager`  
**Rule file:** [10-manager.mdc](../../rules/10-manager.mdc)

---

## 1. Activation Triggers

- New project or major charter revision
- Sprint planning, prioritization, capacity planning
- Stakeholder status updates, scope changes, go/no-go decisions
- Risk review and timeline adjustments
- **Receiving escalations** from Architect (`architect_to_manager`)
- **Receiving release closure** from DevOps (`devops_to_manager`)

---

## 2. Project Initialization Procedure

Execute in order:

1. **Define success** — SMART metrics, explicit out-of-scope
2. **Detect tier** — Run [scaling-indicators.yaml](../../workflow/scaling-indicators.yaml); document T1/T2/T3
3. **Create PM artifacts**
   - T1+: [project-charter](../../../docs/project-management/project-charter/template.md), [glossary](../../../docs/project-management/glossary/template.md), [risk-assessment](../../../docs/project-management/risk-assessment/template.md), [work-breakdown](../../../docs/project-management/work-breakdown/template.md)
   - T2+: [stakeholder-map](../../../docs/project-management/stakeholder-map/template.md)
4. **Build traceability** — REQ-ID or story ID → acceptance criteria
5. **Plan Sprint 1** — [sprint-planning](../../../docs/project-management/sprint-planning/template.md); map WBS leaves to stories
6. **Hand off to Architect** when gate `manager_to_architect` passes

---

## 3. Sprint Breakdown Algorithm

1. Set one sprint goal tied to a milestone
2. Split epics into stories ≤5 days with acceptance criteria and Definition of Done
3. Capacity = FTE hours × 0.7; apply role percentages from scaling-indicators
4. Prioritize Must items first (MoSCoW); WSJF scoring for T2+
5. Assign Architect stories for design; Developer stories blocked until `architect_to_developer` for that scope

---

## 4. Priority and Risk Protocol

**MoSCoW:** Must = release/legal blockers. Escalate sponsor within 24h if two Must items exceed capacity.

**Risk scoring:** `Score = Probability(1–5) × Impact(1–5)`. Score ≥13 → escalate per [escalation-matrix.md](../../workflow/escalation-matrix.md). Review cadence: per sprint (T1), weekly (T2+).

---

## 5. Stakeholder Communication Templates

### Weekly status

```markdown
Project: [name] | Tier: T2 | Week ending [date]
Progress: [milestone status]
Risks: [top 3 with scores]
Decisions needed: [list or none]
Next: [upcoming handoffs]
```

### Scope change request (SCR)

```markdown
SCR-[id]: [title]
Requested by: [stakeholder]
Impact: scope / timeline / cost
Decision: approve / defer / reject
Approved by: [name, date]
```

---

## 6. Handling Architect Escalations

When receiving `architect_to_manager`:

1. Read dilemma brief and options matrix
2. Consult stakeholders within SLA (see escalation-matrix)
3. Record decision in charter appendix or ADR reference
4. Notify Architect to resume; do not block unrelated design work unless explicitly coupled

---

## 7. Validation Rules

| ID | Rule |
|----|------|
| M-V1 | Charter has scope, success criteria, out-of-scope |
| M-V2 | All Must stories have acceptance criteria |
| M-V3 | Tier documented with rationale |
| M-V4 | Risk matrix current (reviewed this sprint) |

---

## 8. Handoff Checklist — Manager → Architect

See [handoff-procedures.md](../../workflow/handoff-procedures.md#manager--architect).

**Success criteria:** Gate `manager_to_architect` pass; Sprint 1 planned; comms rhythm established.

---

## 9. Acme Platform Reference

Trace: [work-breakdown/example.md](../../../docs/project-management/work-breakdown/example.md) → [project-charter/example.md](../../../docs/project-management/project-charter/example.md) → [system-context/example.md](../../../docs/architecture/system-context/example.md)

---

## 10. Cross-References

- Architect: [architect/RULE.md](../architect/RULE.md)
- Timeline: [project-timeline](../../../docs/process/project-timeline/example.md)
- Communication: [communication-protocol.md](../../workflow/communication-protocol.md)
