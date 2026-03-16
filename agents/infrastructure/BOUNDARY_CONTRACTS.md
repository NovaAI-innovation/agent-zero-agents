# Infrastructure Boundary Contracts

This document defines ownership boundaries between legacy infrastructure-adjacent agents and the Infrastructure domain.

## Ownership
- `developer`: application implementation, build/test automation, dependency/runtime fixes.
- `hacker`: security review, threat/risk analysis, hardening guidance.
- `infrastructure`: deployment-readiness checks, environment validation, rollout safety.

## Handoff Contracts
### `developer -> infrastructure`
- Inputs: `test-results`, `build-artifacts`, `deployment-config`
- Outputs: `readiness-status`, `operation-plan`

### `hacker -> infrastructure`
- Inputs: `risk-findings`, `severity-map`, `recommended-controls`
- Outputs: `risk-acknowledgement`, `mitigation-checklist`

## Routing Rule
All operational synthesis and release-go/no-go decisions should route through `profile="infrastructure"` via `agent0` domain routing.

