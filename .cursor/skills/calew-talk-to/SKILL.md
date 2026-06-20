---
name: calew-talk-to
description: >-
  Handle CALEW consultation (/talk-to) without changing agent ownership.
  Use when one agent asks another for advice while retaining control of the work.
---

# CALEW Talk-To (Consultation)

Consultation lets one agent ask another for an opinion **without transferring ownership**.

## Grammar

```
/hey-{owner} /talk-to /hey-{consultant} [question or task]
```

Example:

```
/hey-developer /talk-to /hey-architect
Should I use REST or GraphQL for this endpoint?
```

## Rules

1. **Owner retains `active_agent`** in [state.yaml](../../session/state.yaml) — do not change it
2. Consultant gives opinion only; output must be tagged: `[CONSULTATION — not a handoff]`
3. Consultations do **not** satisfy quality gates
4. No artifact ownership transfer; `current_gate` unchanged
5. Push consultant onto `consultation_stack` in state; pop when consultation complete

## Output Format

```markdown
[CONSULTATION — not a handoff]

**Owner:** Developer
**Consultant:** Architect
**Question:** Should I use REST or GraphQL?

### Opinion
<consultant's recommendation with rationale>

### Owner action
Owner decides and continues. No gate change.
```

## When to Use vs Handoff

| Situation | Use |
|-----------|-----|
| Quick design opinion while coding | `/talk-to` |
| Work complete, ready for next phase | `/handoff-to` |
| Blocking dilemma needing stakeholder decision | `/handoff-to /hey-manager` (escalation) |

## Related

- Full protocol: [consultation-protocol.md](../../workflow/consultation-protocol.md)
- Handoffs: [calew-handoff](../calew-handoff/SKILL.md)
