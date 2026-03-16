# Legacy Agent Deprecation Matrix

This matrix defines migration cutover criteria for legacy profiles and a rollback path.

## Status Legend
- `Shadow`: new domain path runs in parallel for validation only.
- `Dual`: both paths allowed; new path is preferred.
- `Cutover`: legacy path disabled for new work.

## Matrix
| Legacy Agent | Domain Successor | Current Mode | Cutover Criteria | Rollback Trigger | Rollback Action |
|---|---|---|---|---|---|
| `prompt-evaluator` | `quality` | Cutover | 2 consecutive CI passes (`migration_smoke_tests.py` + unit tests) and equivalent score/report shape for sampled prompts | Domain score schema mismatch or missing rubric fields | Re-enable legacy evaluator calls for affected workflow and open blocking issue |
| `agent-evaluator` | `quality` | Cutover | Agent profile evaluations match pass/fail parity on validation sample set | Regression in profile pass/fail parity | Route profile eval requests back to `agent-evaluator` temporarily |
| `prompt-packer` | `packaging` | Cutover | Required artifacts + schema validation pass for 10 sample packages | Artifact completeness regressions | Restore `prompt-packer` as packaging default and capture failing sample IDs |
| `notion-template-generator` | `packaging` | Cutover | Listing/docs bundle output accepted in manual review for 5 samples | Listing/doc format breakage | Route template packaging back to legacy path until template formatter fix lands |
| `researcher` | `research` | Cutover | Ranking + recommendations stable across fixed fixture inputs | Ranking drift outside expected tolerance | Revert research routing to `researcher` for affected category |
| `gumroad-trend-analyzer` | `research` | Cutover | Heuristic parity achieved and merged into `a0/components/research` | Missing signal category support | Keep legacy trend analyzer enabled for unsupported categories |
| `mdcourse-gen` | `course` | Cutover | Stage outputs complete and delivery readiness true for baseline fixture set | Stage contract validation failures | Route course generation to legacy monolith while stage defects are fixed |

## Cutover Procedure
1. Run shadow validation with fixed fixtures and capture deltas.
2. Move to dual mode when parity criteria are met.
3. Cut over defaults to domain successor.
4. Keep rollback window open for one release cycle.

## Current Evidence (2026-03-15)
- Full migration gate suite passing locally (`python -m unittest discover -s tests -p "test_*.py" -v` + `python migration_smoke_tests.py`).
- Route contract tests include all seven domains and research heuristic output checks.
- Migration readiness snapshot generated at `agents/reports/readiness/2026-03-15.json` with `missing_checks = 0`.
- Packaging cutover parity report: `agents/reports/parity/2026-03-15_packaging-cutover.json` (`10/10` samples passed).
- Research legacy parity report: `agents/reports/parity/2026-03-15_research-legacy-parity.json` (all legacy contract checks passed).
- Agent profile parity report: `agents/reports/parity/2026-03-15_agent-profile-parity.json` (expected pass/fail behavior matched).
- Notion template parity report: `agents/reports/parity/2026-03-15_notion-template-parity.json` (`5/5` automated review samples passed).
- Non-destructive legacy snapshots created at `agents/archives/2026-03-15/` for all currently cutover legacy profiles.
- Legacy directories removed from active agent paths after snapshot capture (2026-03-15).

## Ownership
- Quality: maintain rubric compatibility and report schema.
- Packaging: maintain manifest/schema/artifact integrity.
- Course: maintain stage contract and delivery readiness.
- Research: maintain ranking determinism and signal coverage.
