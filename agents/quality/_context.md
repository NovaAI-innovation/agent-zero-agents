# Quality Domain Context

This domain centralizes quality evaluation to remove duplicated scoring logic across evaluator and packaging agents.

## Scope
- Prompt evaluation
- Agent profile evaluation
- Package/listing quality checks

## Shared Components
- `/a0/components/quality/scoring_engine.py`
- `/a0/components/quality/feedback_generator.py`
- `/a0/components/quality/report_formatter.py`
- `/a0/components/quality/signal_extractors.py`
- `/a0/components/quality/evaluator.py`

## Runtime Entry
- `agents/quality/scripts/evaluate.py`
  - `prompt`: evaluate prompt text/file
  - `agent-profile`: evaluate an agent directory
  - `package`: evaluate package manifest JSON

## Constraints
- Use explicit rubrics and criteria.
- Keep evaluations reproducible and comparable.
- Do not embed separate scoring systems in other domains.
