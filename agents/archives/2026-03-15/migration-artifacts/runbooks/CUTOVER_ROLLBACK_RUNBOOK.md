# Cutover Rollback Runbook

## Scope
Use this runbook during shadow/dual/cutover migration phases when new domain behavior causes regressions.

## Rollback Triggers
- Parity delta exceeds accepted threshold for a domain.
- Missing required output fields in domain runtime response.
- Failure in unit tests + smoke tests after cutover toggle.

## Rollback Steps
1. Mark domain status as `Dual` or `Shadow` in `DEPRECATION_MATRIX.md`.
2. Re-route affected workflow to legacy agent path for that domain.
3. Keep other domains on current mode if unaffected.
4. Record rollback event in telemetry report (`MIGRATION_TELEMETRY.md`).

## Verification After Rollback
1. Run:
   - `python -m unittest discover -s tests -p "test_*.py" -v`
   - `python migration_smoke_tests.py`
2. Validate restored path produces expected schema/keys.
3. Confirm no cross-domain routing regressions.

## Re-Cutover Preconditions
- Root cause fixed and reviewed.
- Route fixture and contract tests green.
- One successful shadow run with parity checks.
- Incident note closed with remediation summary.

