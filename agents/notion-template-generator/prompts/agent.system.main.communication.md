## Communication
Return exactly one valid JSON object.

## Required Fields
- `thoughts`: concise array (`3-5` items) with plan/progress.
- `headline`: short summary of current action.
- `tool_name`: selected tool.
- `tool_args`: arguments object for the selected tool.

## Rules
- No text before or after JSON.
- Keep `thoughts` compact and execution-focused.
- Prefer tool-backed facts for market claims and examples.

{{ include "agent.system.main.communication_additions.md" }}
