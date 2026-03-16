# Migration Status

This tracker starts execution of the domain-consolidation plan from `new-structure.md`.

## Current Phase
- Phase 2 (Quality + Packaging): in progress
- Phase 3 (Course Deconstruction): started (scaffold)
- Phase 5 (Research & Utility): started (heuristics + boundary contracts)

## Domain Mapping (Initial)
| Current Agent | Target Domain | Status | Notes |
|---|---|---|---|
| `prompt-evaluator` | Quality | Planned merge | Move rubric/scoring behavior into shared quality components |
| `agent-evaluator` | Quality | Planned merge | Consolidate evaluator prompts/policies |
| `prompt-packer` | Packaging | Planned merge | Keep packaging workflows, remove embedded evaluation duplication |
| `notion-template-generator` | Packaging | Planned merge | Consolidate template/packaging capabilities |
| `mdcourse-gen` | Course | Planned deconstruction | Split monolith into stage-oriented components |
| `script-writer` | Content | Retain + orchestrate | Keep specialization, add orchestration hooks |
| `visuals-hybrid` | Content | Retain + orchestrate | Keep specialization, add orchestration hooks |
| `voice-ai` | Content | Retain + orchestrate | Keep specialization, add orchestration hooks |
| `platform-publisher` | Content | Retain + orchestrate | Keep specialization, add orchestration hooks |
| `gumroad-trend-analyzer` | Research | Planned merge | Fold into single research domain |
| `researcher` | Research | Planned merge | Fold into single research domain |
| `branding-svg-maker` | Branding | Target domain fit | Keep with domain naming consistency |
| `developer` | Infrastructure | Target domain fit | Infrastructure utility |
| `hacker` | Infrastructure | Target domain fit | Infrastructure/security utility |

## Implemented In This Step
- Added new domain agents:
  - `quality/`
  - `packaging/`
- Added shared component scaffolds:
  - `a0/components/quality/`
  - `a0/components/packaging/`
- Implemented reusable quality modules:
  - weighted scoring and normalized reports
  - rubric files (`prompt-eval`, `agent-profile`, `packaging-default`)
  - rubric-driven evaluator entrypoint
  - deterministic score extractors for prompt, agent-profile, and package signals
- Implemented reusable packaging modules:
  - artifact requirement coverage in package manifests
  - package validation helper
  - package-type to rubric integration contract
  - listing bundle and docs bundle generators aligned with existing pack/template standards
- Added migration smoke tests:
  - `agents/migration_smoke_tests.py`
- Wired runtime entry scripts:
  - `agents/quality/scripts/evaluate.py`
  - `agents/packaging/scripts/prepare_package.py`
- Added Course domain agent and runtime entry:
  - `agents/course/agent.json`
  - `agents/course/_context.md`
  - `agents/course/prompts/*`
  - `agents/course/scripts/orchestrate.py`
- Added CI workflow:
  - `.github/workflows/migration-smoke.yml`
- Added Course component scaffold:
  - `a0/components/course/stage_contracts.py`
  - `a0/components/course/artifact_manager.py`
  - `a0/components/course/orchestrator.py`
  - `a0/components/course/stages/*.py` stage stubs
- Replaced key Course stubs with baseline migrated logic:
  - `blueprint_gen.py` (10-50 module specs + personas + success metrics)
  - `content_dev.py` (9 required sections + module_n word target formula)
  - `assessment_gen.py` (9-question distribution per module)
  - `validate_qa.py` (section/distribution validation)
- Replaced remaining Course stage stubs with baseline logic:
  - `multimedia_src.py` (per-module image/video/interactive target enforcement)
  - `marketing_strat.py` (sectioned sales page with 2000+ word baseline check)
  - `pricing_ana.py` (5+ competitor baseline + tiered pricing + ROI model)
  - `package_del.py` (platform package manifests + deployment readiness checklist)
- Added Research domain consolidation scaffold:
  - `agents/research/*` (agent, context, prompts, runtime script)
  - `a0/components/research/*` (market analyzer, trend scorer, synthesizer)
- Strengthened Packaging validation:
  - `a0/components/packaging/schemas.py`
  - extended `package_builder.py` and `validator.py` with schema/type checks
  - added `course_pack` support
- Added agent0 runtime dispatcher:
  - `agents/agent0/scripts/dispatch.py` routes to quality/packaging/course/research scripts
- Added routed-call helper (non-root mitigation):
  - `agents/agent0/scripts/routed_call_helper.py` builds canonical `profile="agent0"` route envelopes and can execute dispatch preflight
- Enforced routing policy in prompts/templates:
  - `agent0` prompts now require centralized routing via agent0
  - `agent-builder` tips now prohibit direct domain-profile subordinate calls
- Strengthened migration smoke tests:
  - guard against direct `call_subordinate(profile='quality|packaging|course|research')` patterns in prompts/docs
  - helper execution check validates route envelope + dispatch result
- Added targeted unit tests:
  - `agents/tests/test_domain_components.py` covers quality rubric load/eval, packaging schema validation, course stage input contracts, and research ranking determinism
- Added canonical route-envelope examples:
  - `agent0/prompts/agent.system.main.role.md` now includes `ROUTE_DOMAIN_V1` examples for all four domains
- Added legacy cutover planning artifact:
  - `DEPRECATION_MATRIX.md` with shadow/dual/cutover criteria and rollback triggers/actions per legacy agent
- Added route fixture regression tests:
  - `agents/tests/fixtures/routes/*.json` fixed route payload fixtures
  - `agents/tests/test_route_dispatch_contract.py` validates `dispatch.py` and `routed_call_helper.py` contracts across all domains
- Added missing domain agents:
  - `agents/branding/*` with runtime script `scripts/compose_brand.py`
  - `agents/content/*` with runtime script `scripts/orchestrate_content.py`
  - `agents/infrastructure/*` with runtime script `scripts/execute_ops.py`
- Extended dispatch contract:
  - `agent0/scripts/dispatch.py` now routes `branding`, `content`, and `infrastructure`
  - `agent0/scripts/routed_call_helper.py` accepts all seven domains
- Expanded smoke + fixture coverage:
  - route fixtures now include branding/content/infrastructure
  - smoke tests assert new domain agent/runtime paths and dispatch execution
- Implemented remaining shared component layer:
  - `a0/components/content/workflow_orchestrator.py`
  - `a0/components/content/asset_manager.py`
  - `a0/components/content/quality_checks.py`
  - `a0/components/infrastructure/readiness_checks.py`
  - `a0/components/infrastructure/ops_planner.py`
  - `a0/components/infrastructure/safety_gates.py`
- Refactored domain runtime scripts to consume shared components:
  - `agents/content/scripts/orchestrate_content.py`
  - `agents/infrastructure/scripts/execute_ops.py`
- Expanded unit/smoke validation for shared components:
  - `agents/tests/test_domain_components.py` now covers content + infrastructure components
  - `agents/migration_smoke_tests.py` now validates content + infrastructure shared-layer behavior
- Added routing policy and fixture schema gates:
  - `agents/tests/test_routing_policy.py`
  - `agents/tests/test_route_fixture_schema.py`
- Added migration operations docs:
  - `agents/runbooks/ROUTING_FALLBACK_RUNBOOK.md`
  - `agents/runbooks/CUTOVER_ROLLBACK_RUNBOOK.md`
  - `agents/MIGRATION_TELEMETRY.md`
- Enabled CI migration gates:
  - `.github/workflows/migration-smoke.yml` now runs full unit/policy/schema suite and migration smoke tests
- Migrated deeper research heuristics from legacy analyzer:
  - `a0/components/research/heuristics.py` (demand, competition, monetization, confidence)
  - extended research normalization and synthesis (`market_analyzer.py`, `synthesizer.py`) for niche ranking tables and uncertainty handling
  - `agents/research/scripts/analyze.py` now forwards creator/badge/timeframe fields
- Added Infrastructure boundary contracts:
  - `a0/components/infrastructure/contracts.py` with developer/hacker/infrastructure ownership + handoff I/O contracts
- Published first weekly telemetry report:
  - `agents/reports/telemetry/2026-W11.md`
- Added migration readiness tooling:
  - `agents/scripts/migration_readiness_report.py`
  - generated baseline snapshot: `agents/reports/readiness/2026-03-15.json`
- Added archive-execution artifact:
  - `agents/LEGACY_ARCHIVE_CHECKLIST.md` with proposed archive dates
- Added guided cutover scripts and parity reports:
  - `agents/scripts/packaging_cutover_check.py`
  - `agents/scripts/research_legacy_parity_check.py`
  - `agents/scripts/agent_profile_parity_check.py`
  - `agents/scripts/notion_template_parity_check.py`
  - generated reports under `agents/reports/parity/`
- Began phased legacy archiving (non-destructive snapshots):
  - `agents/archives/2026-03-15/` for `prompt-evaluator`, `agent-evaluator`, `prompt-packer`, `researcher`, `gumroad-trend-analyzer`
  - extended snapshots for `notion-template-generator` and `mdcourse-gen`
- Completed active legacy directory removal (post-snapshot):
  - removed: `prompt-evaluator`, `agent-evaluator`, `prompt-packer`, `notion-template-generator`, `researcher`, `gumroad-trend-analyzer`, `mdcourse-gen`
- Added explicit functional coverage mapping:
  - `agents/MIGRATION_FUNCTIONAL_COVERAGE.md` links archived agents to successor domain implementations and evidence artifacts
- Added `old.json`-driven reconciliation checks:
  - `agents/scripts/oldjson_reconciliation_check.py`
  - `agents/tests/test_oldjson_reconciliation_check.py`
  - smoke and readiness gates now fail if `old.json` capabilities are not covered
- Expanded shared components for full old-profile capability parity:
  - `a0/components/content/{script_pipeline,visuals_pipeline,voice_pipeline,pdf_pipeline,publisher_pipeline}.py`
  - `a0/components/infrastructure/{agent_profile_builder,dev_security_ops}.py`
- Completed strict domain-only profile consolidation (post-snapshot):
  - removed additional non-domain profiles: `agent-builder`, `branding-svg-maker`, `pdf-creator`, `platform-publisher`, `script-writer`, `visuals-hybrid`, `voice-ai`
  - active agent profiles now: `agent0`, `quality`, `packaging`, `course`, `research`, `branding`, `content`, `infrastructure`
- Expanded research parity validation:
  - new route fixtures: `research_sparse.json`, `research_mixed.json`
  - new test: `agents/tests/test_research_parity_cases.py`
- Added readiness-report unit coverage:
  - `agents/tests/test_migration_readiness_report.py`
- Added infrastructure consolidation doc:
  - `agents/infrastructure/BOUNDARY_CONTRACTS.md`
- Progressed cutover modes:
  - `DEPRECATION_MATRIX.md` now marks all legacy migration targets in `Cutover` mode

## Next Actions
1. Migrate deeper heuristics/signals from `gumroad-trend-analyzer` into `a0/components/research` and align scoring weights with marketplace data assumptions.
2. Start Infrastructure domain consolidation by defining `developer`/`hacker` ownership boundaries and shared tool contracts.
3. Produce week 2026-W12 telemetry and parity deltas for post-cutover monitoring.
4. Keep rollback runbooks updated for one release-cycle safety window.
5. Optional: prune/archive obsolete prompt references in non-domain agents.
6. Optional: add stricter reconciliation gate to fail on unmapped extra coverage entries if desired.
