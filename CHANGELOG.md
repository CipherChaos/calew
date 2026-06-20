# Changelog

All notable changes to the Project Workflow Blueprint follow [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-06-20

### Added

- Root README, HELP.md (agent diagrams and how-to), BOOTSTRAP.md (AI project setup), AGENTS.md
- `.cursor/` multi-agent system: 6 rule files, 5 agent playbooks, 7 workflow artifacts
- Reverse loops: `architect_to_manager` (dilemma escalation), `qa_to_developer` (test failure)
- Architect decision tree: `.cursor/workflow/architect-decision-tree.md`
- `docs/` documentation system: 27 document bundles (template, example, guide)
- Acme Platform narrative threading through all examples
- Tier model (T1/T2/T3) with scaling indicators and quality gate overrides
- Cross-reference indexes: `.cursor/INDEX.md`, `docs/INDEX.md`, `docs/RELATIONSHIPS.md`
- Blueprint standard: `docs/STANDARD.md` with metadata and review workflow
- Doc generator: `scripts/generate_docs.py`

## [1.1.0] - 2026-06-20

### Added

- [docs/DIAGRAMS.md](docs/DIAGRAMS.md) — master diagram catalog with priority matrix (Critical / Recommended / Optional / Skip by tier)
- WBS bundle: [docs/project-management/work-breakdown/](docs/project-management/work-breakdown/)
- Entity State Diagram: [docs/process/entity-state/](docs/process/entity-state/)
- Activity Diagram: [docs/process/activity-diagram/](docs/process/activity-diagram/)
- Class Diagram: [docs/data/class-diagram/](docs/data/class-diagram/)

### Changed

- ERD and Sequence guides cross-link Class, Entity State, and Activity diagrams
- Manager init deliverables include WBS; Architect deliverables include entity-state, class, activity
- `quality-gates.yaml`: WBS required for `manager_to_architect`; recommended artifacts for sequence, ESD, class, activity
- `scaling-indicators.yaml`: T1 skip list for activity-diagram and class-diagram
- Updated INDEX, RELATIONSHIPS, HELP, agent playbooks
