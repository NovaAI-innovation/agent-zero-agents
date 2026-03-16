# Legacy Archive Checklist

Use this checklist before archiving legacy agents after cutover.

## Target Legacy Agents
- `prompt-evaluator`
- `agent-evaluator`
- `prompt-packer`
- `notion-template-generator`
- `researcher`
- `gumroad-trend-analyzer`
- `mdcourse-gen`

## Target Archive Dates (Proposed)
- `prompt-evaluator`: 2026-03-22 (already in `Cutover`)
- `agent-evaluator`: 2026-03-29
- `prompt-packer`: 2026-03-29
- `notion-template-generator`: 2026-04-05
- `researcher`: 2026-04-05
- `gumroad-trend-analyzer`: 2026-04-05
- `mdcourse-gen`: 2026-04-12

## Archive Snapshot Status (2026-03-15)
- [x] `prompt-evaluator` snapshot created at `archives/2026-03-15/prompt-evaluator/`
- [x] `agent-evaluator` snapshot created at `archives/2026-03-15/agent-evaluator/`
- [x] `prompt-packer` snapshot created at `archives/2026-03-15/prompt-packer/`
- [x] `notion-template-generator` snapshot created at `archives/2026-03-15/notion-template-generator/`
- [x] `researcher` snapshot created at `archives/2026-03-15/researcher/`
- [x] `gumroad-trend-analyzer` snapshot created at `archives/2026-03-15/gumroad-trend-analyzer/`
- [x] `mdcourse-gen` snapshot created at `archives/2026-03-15/mdcourse-gen/`

## Active Path Removal Status (2026-03-15)
- [x] `prompt-evaluator` removed from active agent directories
- [x] `agent-evaluator` removed from active agent directories
- [x] `prompt-packer` removed from active agent directories
- [x] `notion-template-generator` removed from active agent directories
- [x] `researcher` removed from active agent directories
- [x] `gumroad-trend-analyzer` removed from active agent directories
- [x] `mdcourse-gen` removed from active agent directories

## Strict Domain-Only Consolidation (2026-03-15)
- [x] `agent-builder` archived and removed from active agent directories
- [x] `branding-svg-maker` archived and removed from active agent directories
- [x] `pdf-creator` archived and removed from active agent directories
- [x] `platform-publisher` archived and removed from active agent directories
- [x] `script-writer` archived and removed from active agent directories
- [x] `visuals-hybrid` archived and removed from active agent directories
- [x] `voice-ai` archived and removed from active agent directories

## Prerequisites Per Agent
- [ ] Successor domain mode is `Cutover` in `DEPRECATION_MATRIX.md`.
- [ ] Route contract tests pass (`test_route_dispatch_contract.py`).
- [ ] Policy/schema tests pass (`test_routing_policy.py`, `test_route_fixture_schema.py`).
- [ ] Smoke tests pass (`migration_smoke_tests.py`).
- [ ] One telemetry cycle recorded with `fallback_count = 0`.
- [ ] Rollback path documented in runbooks.

## Archive Steps
1. Mark agent status as archived with date and successor domain.
2. Remove direct references from active prompts/templates.
3. Preserve last known `agent.json` + key prompts under archive path.
4. Update migration docs (`MIGRATION_STATUS.md`, `DEPRECATION_MATRIX.md`).

## Post-Archive Verification
1. Run full test gate suite.
2. Validate no routing references target archived profiles.
3. Confirm telemetry report includes archive note.
