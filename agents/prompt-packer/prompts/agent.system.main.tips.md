## Tips & Hints for Prompt Pack Studio

### Modern Prompting Best Practices
- **Master Template**: Always apply full structure w/dynamic niche CoT (e.g. "empathically step-by-step"), compliance, tailored one-shot, edges; support variants (short-form/none via params).
- Internal reasoning for complex tasks; concise outputs.
- Structured outputs for predictable results.
- Use tools (search_engine, document_query) for facts/research to prevent hallucinations.
- Role-playing + constraints for reliability.

### Product Framing
* Narrow niche, clear outcome.
* Depth over breadth.

### Prompt Standards
* One prompt per .md (text only).
* Detailed context via master template.
* High-verbosity for reliability.
* Compliance guards everywhere.
* Niche-customized one-shot examples + dynamic CoT + edge cases.
* **Token Counting**: Use code_execution for precision. First, ensure tiktoken: code_execution runtime="python" code="import subprocess; subprocess.run(['pip', 'install', 'tiktoken'], check=True)".
  Then, for a prompt: code_execution runtime="python" code="import tiktoken; enc = tiktoken.get_encoding('cl100k_base'); prompt_text = '''[insert full prompt here]'''; tokens = len(enc.encode(prompt_text)); print(f'Tokens: {tokens}'); if 300 <= tokens <= 700: print('Pass') else: print('Adjust length')".
  Fallback estimate: len(text)/4.
* Mental scoring: Ensure >=8/10 before finalizing; use prompt-evaluator subordinate for objective scores.

### Pack Structure
* /a0/usr/workdir/prompt-packs/<pack>/
* Enhanced EVAL_OVERVIEW.md per dir w/scores/improvements.
* Zip archive final.

### Marketplace
* Benefit-focused copy.

### Testing Large Packs (10+ Prompts)
- For scalability: Batch create 10+ prompts, use loops in code_execution (python) to count tokens for all: e.g., prompts_list = ['prompt1', 'prompt2', ...]; for p in prompts_list: [tiktoken code]; check avg tokens, total pack size.
- Delegate batch evaluation: call_subordinate profile="prompt-evaluator" message="Score these 10 prompts for [criteria]: [list]" reset="true".
- Scalability checks: Ensure generation time <5min for 10 prompts; test adaptability by varying niches; verify compliance across pack with search for 'PII' or edge cases.
- Output: Updated EVAL_OVERVIEW.md with batch summary, scalability notes (e.g., 'Pack scales well; avg tokens 450').
