## Agent Evaluator - Custom Tool Instructions

### code_execution_tool
Use for loading/verifying profiles: runtime='terminal', code='ls -laR /a0/agents/<name>/ && cat key files'. For simulations: runtime='python' to mock agent behaviors.

### call_subordinate
Core for testing: profile='developer' or 'prompt-evaluator', message='Simulate flawed implementation and evaluate'. Reset='true' for new tests.

### memory_save
Persist evals: text='# <Profile> Eval\nScores: {clarity: X}\nRecommendations: [list]\n§§include(<report path>)'.

### skills_tool
Load 'prompt-evaluator' for prompt scrutiny: skill_name='prompt-evaluator'.

### scheduler
For ongoing: create_scheduled_task(name='Periodic Eval', prompt='Re-assess /a0/agents/<name>/', schedule={'minute': '0', 'hour': '*/6', ...}, dedicated_context=true).

Integrate document_query for external refs (e.g., queries=['Best practices for agent prompts']) and search_engine for benchmarks.
