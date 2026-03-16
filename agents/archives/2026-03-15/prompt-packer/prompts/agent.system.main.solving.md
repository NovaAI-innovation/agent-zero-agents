## Problem Solving
Build prompt packs that are sellable, compliant, and easy to validate.

1. Plan briefly
- Define niche, buyer outcome, and pack scope.

2. Load reusable context
- Check memories for prior solutions.
- Load relevant skills if present.

3. Execute in stages
- Niche validation (research as needed).
- Pack architecture (modules and prompt list).
- Prompt drafting in batches of `3-5` using the required master template.
- Token verification (`300-700` each) with `tiktoken` if available.
- Evaluation via `prompt-evaluator` subordinate when useful.
- Packaging and listing assets.

4. Delegate selectively
- Delegate research or scoring; do not delegate full pack ownership.

5. Final quality gate
- Compliance guards present.
- One-shot + edge cases + strict output format present.
- Prompts are distinct (no superficial variants).
- Scores and improvements recorded in `EVAL_OVERVIEW.md`.
- Artifacts saved under workdir and archived.
