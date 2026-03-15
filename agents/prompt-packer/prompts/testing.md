## Testing Instructions

### Per-Prompt Checks
1. Compliance: verify PII redaction and public-ethics constraints.
2. Structure: master-template elements all present.
3. Token count: `300-700` preferred range.
4. Score: clarity/effectiveness/compliance must be `>=8/10`.

### Pack-Level Checks
1. Distinct prompts with no superficial duplication.
2. Directory and file structure is complete.
3. `EVAL_OVERVIEW.md` includes scores, weaknesses, and fixes.
4. Usage guide and listing copy are included.

### Large Packs (10+ Prompts)
- Batch token-check and score prompts.
- Spot-check at least `2-3` edge scenarios across the pack.
- Summarize scalability observations in `EVAL_OVERVIEW.md`.

### Completion Criteria
- All required files exist.
- All prompts pass quality gate.
- Archive is generated successfully.
