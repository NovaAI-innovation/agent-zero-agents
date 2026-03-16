# Routing Fallback Runbook

## Scope
Use this runbook when domain routing via `agent0` fails or returns mismatched domain output.

## Detection Signals
- `tests/test_route_dispatch_contract.py` failure.
- `migration_smoke_tests.py` domain dispatch failure.
- Runtime output domain differs from requested route domain.

## Immediate Actions
1. Confirm failure by rerunning:
   - `python -m unittest tests/test_route_dispatch_contract.py -v`
   - `python migration_smoke_tests.py`
2. Identify failing domain and fixture payload under `tests/fixtures/routes/`.
3. Temporarily force explicit domain with `--domain <name>` in dispatcher-based callers.
4. If failure persists, move affected domain to legacy fallback path listed in `DEPRECATION_MATRIX.md`.

## Containment
1. Keep unaffected domains on new routing path.
2. Open incident note with:
   - failing domain
   - command output summary
   - latest commit hash
   - temporary mitigation applied

## Exit Criteria
- Route contract tests pass for failed domain.
- Smoke suite passes.
- One shadow validation run shows parity with expected output shape.

