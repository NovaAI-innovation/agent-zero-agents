## Stage 2: Content Depth Expansion

Generate each module with full instructional depth and no placeholders.

### Required Structure (per module)
1. Context
2. Theory
3. Example 1 (simple)
4. Example 2 (realistic)
5. Example 3 (advanced or edge case)
6. Code or implementation walk-through
7. Best practices
8. Common pitfalls
9. Resources

### Depth Targets
- Enforce formula: Module N >= (300 * N) words.
- Keep explanation depth proportional to module progression.
- Use specific examples and complete code snippets where applicable.

### Validation
- Run word count checks.
- Verify all 9 sections exist and are substantive.
- Reject placeholder, generic filler, or duplicate text across modules.

## Stage 3: Progressive Elaboration

After initial generation, run elaboration loops until depth and coherence pass.

### Per-Module Checks
- Re-check word count target and section completeness.
- Confirm example progression (simple -> realistic -> advanced).
- Compare with prior module for complexity increase (target 10-15%).

### Cross-Module Checks
- Detect backward depth steps and regenerate flagged modules.
- Verify module-to-module prerequisite coherence and explicit linkage.
- Ensure concept density trends upward through the course path.

### Failure Recovery
- If a module fails: regenerate only failed sections first, then full module if needed.
- If repeated failure: log attempts, report blockers, request user guidance.

For exact thresholds and expanded templates, use:
- `prompts/content.standards.md`
- `prompts/validation.gates.md`
