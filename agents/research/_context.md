# Research Domain Context

This domain consolidates `researcher` and `gumroad-trend-analyzer` into one evidence-based research workflow.

## Scope
- Topic and market signal analysis
- Category trend scoring
- Ranked opportunity recommendations

## Shared Components
- `/a0/components/research/market_analyzer.py`
- `/a0/components/research/trend_scorer.py`
- `/a0/components/research/synthesizer.py`

## Runtime Entry
- `agents/research/scripts/analyze.py`
  - Accepts normalized signals via JSON
  - Returns ranked opportunities and recommendations
