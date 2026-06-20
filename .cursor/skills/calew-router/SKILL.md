---
name: calew-router
description: >-
  Route CALEW commands (/hey-*, /calew-*, /handoff-to, /talk-to, /make-report)
  to the correct agent persona and session state. Use when the user types any
  CALEW command or when unsure which agent to activate.
---

# CALEW Router

Central orchestration entry point for CALEW v1. Commands are **conventions** — Cursor does not register slash commands natively. Treat `/hey-manager` the same as `@10-manager`.

## When to Apply

- User types `/hey-*`, `/calew-*`, `/handoff-to`, `/talk-to`, or `/make-report`
- User is lost or asks "what should I do next?"
- Session state needs updating after invoke or mode change

## Command Alias Table

| CALEW command | Cursor rule | Agent key | Notes |
|---------------|-------------|-----------|-------|
| `/hey-manager` | `@10-manager` | `manager` | Default fallback when lost |
| `/hey-architect` | `@20-architect` | `architect` | |
| `/hey-developer` | `@30-developer` | `developer` | |
| `/hey-qa` | `@40-qa` | `qa` | Write + run tests |
| `/hey-tester` | `@40-qa` | `qa` | `active_mode: execute_only` |
| `/hey-devops` | `@50-devops` | `devops` | |

## Typo Aliases

Resolve common misspellings to the correct agent:

| Typo | Resolves to |
|------|-------------|
| `/hey-maanger`, `/hey-manger`, `/hey-maneger` | `/hey-manager` |
| `/hey-architec`, `/hey-architectt` | `/hey-architect` |
| `/hey-develper`, `/hey-devloper` | `/hey-developer` |
| `/hey-devop`, `/hey-devops` | `/hey-devops` |

## Default When Lost

If the user is unsure, confused, or asks "where do I start?":

1. Activate **Manager** (`@10-manager` / `/hey-manager`)
2. Triage the request and recommend the next agent
3. Do **not** auto-handoff — recommend `/handoff-to` when ready

## Session State

Read and update [`.cursor/session/state.yaml`](../../session/state.yaml) on every invoke:

```yaml
# After /hey-{agent}:
active_agent: <agent key>
active_mode: default | execute_only   # execute_only for /hey-tester
updated: <ISO-8601 timestamp>
workflow_phase: <discovery|design|build|test|release>  # infer from agent if unset
```

Phase hints by agent:

| Agent | Typical phase |
|-------|---------------|
| manager | discovery |
| architect | design |
| developer | build |
| qa | test |
| devops | release |

## Skill Routing

After resolving the agent, apply secondary skills if present in the user message:

| Skill flag | Delegate to |
|------------|-------------|
| `/talk-to` | [calew-talk-to](../calew-talk-to/SKILL.md) |
| `/handoff-to` | [calew-handoff](../calew-handoff/SKILL.md) |
| `/calew-status`, `/calew-reset`, `/gate-check` | [calew-status](../calew-status/SKILL.md) |
| `/make-report` | [calew-status](../calew-status/SKILL.md) |

## Question Protocol (v1 — rules-based)

Ask the user only when one of these triggers applies. Do not guess.

| Trigger | Action |
|---------|--------|
| Architectural dilemma | Architect uses `/escalate-to-manager` or `/handoff-to /hey-manager` |
| Unclear requirement | Manager clarifies with stakeholder before proceeding |
| Schedule/scope risk | Manager presents options (cut scope vs extend timeline) |
| First-time technology | Architect documents ADR and asks for confirm |
| Budget/cost impact | Manager decision before implementation |

## Safety Rules

- Never auto-handoff — only explicit `/handoff-to`
- Never skip quality gates before handoff
- No production deploy without human approval (see [project.yaml](../../config/project.yaml))
- When unsure: `/hey-manager`

## Related

- Handoffs: [handoff-procedures.md](../../workflow/handoff-procedures.md)
- Gates: [quality-gates.yaml](../../workflow/quality-gates.yaml)
- Consultation: [consultation-protocol.md](../../workflow/consultation-protocol.md)
- Human reference: [SKILLS.md](../../../SKILLS.md)
