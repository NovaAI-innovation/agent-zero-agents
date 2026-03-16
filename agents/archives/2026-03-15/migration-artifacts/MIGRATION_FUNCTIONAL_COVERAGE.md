# Migration Functional Coverage

This report maps archived agent functionality to successor domain implementations.

## Coverage Matrix
| Archived Agent | Successor Domain | Migrated Functionality | Evidence |
|---|---|---|---|
| `prompt-evaluator` | `quality` | Prompt rubric scoring, pass/fail reporting, actions | `a0/components/quality/evaluator.py`, `rubrics/prompt-eval.json`, parity reports |
| `agent-evaluator` | `quality` | Agent profile evaluation parity and pass/fail behavior | `a0/components/quality/signal_extractors.py`, `scripts/agent_profile_parity_check.py` |
| `prompt-packer` | `packaging` | Prompt pack manifest/schema validation and listing/docs flow | `a0/components/packaging/*`, `scripts/packaging_cutover_check.py` |
| `notion-template-generator` | `packaging` | Template-pack validation + listing/docs generation | `package_builder.py`, `validator.py`, `documentation_gen.py`, `marketplace_lister.py`, `scripts/notion_template_parity_check.py` |
| `researcher` | `research` | Ranked opportunities, recommendations, confidence-aware synthesis | `a0/components/research/synthesizer.py`, parity reports |
| `gumroad-trend-analyzer` | `research` | Badge/timeframe/creator-aware heuristics, niche ranking table | `a0/components/research/heuristics.py`, `market_analyzer.py`, `scripts/research_legacy_parity_check.py` |
| `mdcourse-gen-redesign` | `course` | Stage-based generation (blueprint/content/assessment/multimedia/marketing/pricing/validate/delivery) | `a0/components/course/stages/*.py`, `agents/course/scripts/orchestrate.py` |
| `agent0` | `agent0` | Orchestration, domain routing, and response contract governance | `agents/agent0/prompts/*`, `agents/agent0/scripts/dispatch.py` |
| `developer` | `infrastructure` | Development operation planning for feature/bugfix/refactor workloads | `a0/components/infrastructure/dev_security_ops.py` (`developer_ops_plan`) |
| `hacker` | `infrastructure` | Security operations planning and severity policy integration | `a0/components/infrastructure/dev_security_ops.py` (`security_ops_plan`) |
| `branding-svg-maker` | `branding` | Brand kit + SVG logo guidance/output checklist | `agents/branding/scripts/compose_brand.py`, `agents/branding/_context.md` |
| `script-writer` | `content` | Script stage orchestration and retention planning | `a0/components/content/script_pipeline.py`, `agents/content/scripts/orchestrate_content.py` |
| `visuals-hybrid` | `content` | Visual shot planning and licensing policy | `a0/components/content/visuals_pipeline.py` |
| `voice-ai` | `content` | Voiceover style/pacing/quality planning | `a0/components/content/voice_pipeline.py` |
| `pdf-creator` | `content` | Sale-ready PDF export stage and artifact naming | `a0/components/content/pdf_pipeline.py`, `a0/components/content/asset_manager.py` |
| `platform-publisher` | `content` | Platform publish checklist and distribution planning | `a0/components/content/publisher_pipeline.py`, `workflow_orchestrator.py` (`publish`,`distribution`) |
| `agent-builder` | `infrastructure` | Agent profile scaffold generation, validation, and infra-level agent ops planning | `a0/components/infrastructure/agent_profile_builder.py`, `agents/infrastructure/scripts/execute_ops.py` (`mode=agent-build`) |

## Verification Signals
- Unit tests: `python -m unittest discover -s tests -p "test_*.py" -v` (green).
- Smoke tests: `python migration_smoke_tests.py` (`MIGRATION_SMOKE_OK`).
- Readiness snapshot: `reports/readiness/2026-03-15.json` (`missing_checks = 0`).
- Cutover/parity reports under `reports/parity/`.
