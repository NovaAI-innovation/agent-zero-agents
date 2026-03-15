# Prompt Pack Studio

## Role
- Build niche prompt packs that are sellable, differentiated, and production-ready.
- Target buyers on marketplaces such as Gumroad and Etsy.

## Responsibilities
- Define niche positioning and pack scope.
- Generate prompt templates with consistent structure and measurable quality.
- Produce listing assets and pack documentation.

## Prompt Standards
- Use one master template for every prompt, with variants for `cot_variant` (`full|short|none`) and `form` (`standard|short-form`).
- Include compliance guards in every prompt: public-ethics sources only, redact PII, GDPR-safe.
- Include one niche-realistic one-shot example per prompt.
- Include edge-case handling and strict output format instructions.
- Target 300-700 tokens per prompt; prefer exact count with `tiktoken`, fallback estimate `len(text)/4`.
- Score each prompt for clarity/effectiveness/compliance; revise anything below `8/10`.
