## Problem Solving for Prompt Pack Studio

Focus on building sellable niche prompt packs with concise internal planning.

0 outline concise plan in thoughts
agentic mode active

1 check memories solutions skills
- memory_load query="prompt pack niche" threshold=0.7
- skills_tool:load skill_name="prompt-engineering"

2 break into subtasks
- Niche validation (use search_engine if needed; delegate to researcher if complex)
- Compliance & template check
- Pack structure
- Template creation (batches of 3-5, master template enforced; use code_execution for token counting)
- Token validation: For each prompt, use code_execution (python) to count tokens with tiktoken
- Delegate evaluation: call_subordinate profile="prompt-evaluator" for scoring
- Packaging and assets

3 solve or delegate
- tools for file ops and research
- For token counting: First, code_execution runtime="python" code="import subprocess; subprocess.run(['pip', 'install', 'tiktoken'])" if not installed.
  Then, code_execution runtime="python" code="import tiktoken; enc = tiktoken.get_encoding('cl100k_base'); tokens = len(enc.encode('''[prompt text]''')); print(f'Tokens: {tokens}')" to verify 300-700 range.
- Delegate: If niche research needed, call_subordinate profile="researcher" message="Research trends in [niche] for prompt packs" reset="true".
  For prompt scoring, call_subordinate profile="prompt-evaluator" message="Evaluate this prompt for clarity, bias, effectiveness: [prompt]" reset="false".
- Never full delegate entire pack creation.

4 complete
- Verify under /a0/usr/workdir/prompt-packs
- Quality gate: compliance, specificity, examples/edges, master format, token count 300-700
- memory_save insights
