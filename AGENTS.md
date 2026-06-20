# Agents

This project uses five Cursor agents for agentic/loop engineering.

**Start here:** [HELP.md](HELP.md) — role diagrams, lifecycle, and how to invoke each agent.

## Quick Reference

| Agent | Rule | Playbook |
|-------|------|----------|
| Manager | [`.cursor/rules/10-manager.mdc`](.cursor/rules/10-manager.mdc) | [`.cursor/agents/manager/RULE.md`](.cursor/agents/manager/RULE.md) |
| Architect | [`.cursor/rules/20-architect.mdc`](.cursor/rules/20-architect.mdc) | [`.cursor/agents/architect/RULE.md`](.cursor/agents/architect/RULE.md) |
| Developer | [`.cursor/rules/30-developer.mdc`](.cursor/rules/30-developer.mdc) | [`.cursor/agents/developer/RULE.md`](.cursor/agents/developer/RULE.md) |
| QA | [`.cursor/rules/40-qa.mdc`](.cursor/rules/40-qa.mdc) | [`.cursor/agents/qa/RULE.md`](.cursor/agents/qa/RULE.md) |
| DevOps | [`.cursor/rules/50-devops.mdc`](.cursor/rules/50-devops.mdc) | [`.cursor/agents/devops/RULE.md`](.cursor/agents/devops/RULE.md) |

Cross-agent rules: [`.cursor/rules/00-cross-agent.mdc`](.cursor/rules/00-cross-agent.mdc) (always applied)

## Workflow

```
Manager → Architect → Developer → QA → DevOps → Manager
         ↗ dilemma    ↖ fail
```

Bootstrap a new project: [BOOTSTRAP.md](BOOTSTRAP.md)
