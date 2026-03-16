## Tips

### Prompt Design
- Depth over breadth: solve one buyer workflow per prompt.
- Keep language concrete, testable, and reusable.
- Mix style and rigor by niche (creative vs analytical) without losing precision.

### Token Counting
Use exact counting when possible:
```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = len(enc.encode(prompt_text))
print(tokens)
```
Fallback estimate: `len(prompt_text)/4`.

### Evaluation
- Minimum pass target: `8/10` for clarity, effectiveness, compliance.
- Use `prompt-evaluator` for external scoring on borderline prompts.

### Pack Assembly
- `1 prompt per .md` file.
- Add/update `EVAL_OVERVIEW.md` in each prompt directory.
- Include concise usage notes and listing copy.
