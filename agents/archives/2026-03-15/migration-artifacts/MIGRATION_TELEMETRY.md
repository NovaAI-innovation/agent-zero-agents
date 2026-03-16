# Migration Telemetry

## Core Metrics
- `domain`: quality | packaging | course | research | branding | content | infrastructure
- `mode`: shadow | dual | cutover
- `parity_delta`: numeric comparison against legacy baseline (lower is better)
- `fallback_count`: number of fallback events during reporting window
- `cutover_confidence`: low | medium | high
- `test_status`: pass | fail
- `smoke_status`: pass | fail

## Weekly Report Template
| Week | Domain | Mode | Parity Delta | Fallback Count | Confidence | Unit Tests | Smoke | Notes |
|---|---|---|---:|---:|---|---|---|---|
| YYYY-W## | quality | shadow | 0.00 | 0 | high | pass | pass |  |

## Logging Guidance
1. Record one row per domain each week.
2. If fallback occurs, add incident link in Notes.
3. Raise blocker if:
   - `fallback_count > 0` in two consecutive weeks, or
   - `test_status`/`smoke_status` is fail.

