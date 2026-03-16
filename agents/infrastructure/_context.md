# Infrastructure Domain

Purpose:
- Centralize operational and developer-infrastructure actions.
- Provide deterministic checks for environment and deployment readiness.

Capabilities:
- Environment diagnostics and dependency checks.
- Safety-aware operation planning.
- Release/deploy readiness summaries.
- Ownership and handoff contracts for `developer` and `hacker` integration.
- Agent-ops support tasks migrated from utility workflows (profile migration checks, structure validation, archive readiness).

Runtime entry:
- `agents/infrastructure/scripts/execute_ops.py`
  - Returns operation plan and readiness checklist.
- Contract reference:
  - `agents/infrastructure/BOUNDARY_CONTRACTS.md`
