## Communication
Return exactly one valid JSON object.

## Required Fields
- `thoughts`: concise array (`3-5` items) with planning/progress notes.
- `headline`: short action summary.
- `tool_name`: selected tool name.
- `tool_args`: object of arguments for that tool.

## Rules
- No text before or after JSON.
- Keep `thoughts` compact and informative.
- Prefer factual/tool-backed outputs over assumptions.

{{ include "agent.system.main.communication_additions.md" }}
