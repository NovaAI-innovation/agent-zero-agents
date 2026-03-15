## Testing Instructions for Prompt Packs

### Overview
- Test packs for quality, compliance, and scalability before packaging.
- For small packs (3-5 prompts): Individual checks.
- For large packs (10+ prompts): Batch processing with scalability verification.

### Core Testing Steps
1. **Individual Prompt Tests**:
   - Compliance: Mentally input PII; ensure redaction/guardrails trigger.
   - Token Count: Use code_execution (tiktoken) as in tips.md; verify 300-700 tokens.
   - Scoring: Mental 1-10 for clarity/effectiveness/bias-free; if <8, revise.
   - Delegate: call_subordinate profile="prompt-evaluator" message="Score: [prompt]".

2. **Pack-Level Tests**:
   - Structure: Verify directory (niche/modules/prompts), EVAL_OVERVIEW.md present.
   - Uniqueness: No superficial variants; each prompt adds distinct value.
   - Marketplace Fit: Generate sample listing copy; check benefit-focus.

### Large Pack Scalability (10+ Prompts)
- **Batch Token Counting**: Use code_execution runtime="python" code="import tiktoken; enc = tiktoken.get_encoding('cl100k_base'); prompts = ['''prompt1''', '''prompt2''', ...]; counts = [len(enc.encode(p)) for p in prompts]; print(f'Avg: {sum(counts)/len(counts)}, Range: {min(counts)}-{max(counts)}'); if all(300 <= c <= 700 for c in counts): print('All pass') else: print('Adjust outliers')".
- **Batch Evaluation**: call_subordinate profile="prompt-evaluator" message="Batch score these 10+ prompts for [niche]: [list prompts]" reset="true"; include criteria: clarity, effectiveness, compliance.
- **Performance Checks**: Time generation (use wait tool if needed); ensure <10min for 10 prompts. Test adaptability: Vary input niches, verify consistency.
- **Edge Case Coverage**: For pack, test 2-3 edge scenarios across prompts (e.g., no input data, extreme cases); document in EVAL_OVERVIEW.md.
- **Scalability Metrics**: Avg tokens <500, total pack tokens <10k, file count verifiable, zip size <1MB.

### Verification & Output
- Update EVAL_OVERVIEW.md with batch summary: table + metrics (e.g., 'Scales well; 12/12 pass tokens, avg score 8.5').
- If fails: Iterate (revise low-scorers, re-test batch).
- Final: memory_save "[niche] pack tested: [summary]".
