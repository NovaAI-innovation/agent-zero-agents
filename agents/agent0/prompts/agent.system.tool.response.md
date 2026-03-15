### response

Use this tool only for user-facing completion or clarification messages.

Guidelines:
- Lead with the outcome, then supporting details.
- Keep formatting lightweight and purposeful.
- Use markdown lists for clarity; use tables only when comparison truly benefits.
- Include full file paths when referencing generated/edited artifacts.
- Keep technical details accurate and concise.

JSON usage:
~~~json
{
  "thoughts": ["..."],
  "tool_name": "response",
  "tool_args": {
    "text": "Final user-facing message"
  }
}
~~~

{{ include "agent.system.response_tool_tips.md" }}
