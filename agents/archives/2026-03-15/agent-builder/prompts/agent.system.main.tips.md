## Tips & Hints for Creating Custom Agents

### Template Locations
* **Base Prompts:** /a0/prompts/ (cp to prompts/ for overrides)
  * Core: agent.system.main.role.md, communication.md, solving.md
  * Tools: agent.system.tool.code_exe.md, memory.md
* **Prompt Type Index:** /a0/agents/agent-builder/resources/PROMPT_TEMPLATES_INDEX.md
  * Use this index before creating new prompt files to choose the correct template family and file type.
* **Examples:** ls /a0/agents/ (researcher, developer, hacker)
  * cat /a0/agents/researcher/agent.json _context.md

### Profile Best Practices
* **agent.json:** Valid JSON {"title": "Name", "description": "...", "context": "Use for..."}
* **_context.md:** # Title\n- Bullet summary (match examples)
* **prompts/:** Selective overrides (main.role.md essential)
* **No spaces** in <name>
* **Verify:** ls -laR /a0/agents/<name> ; cat files
* **Persist:** memory_save "# <name> Profile\ninclude(/a0/agents/<name>/agent.json)"
* **Test:** call_subordinate profile="<name>" message="test"
* **Routing policy:** Never call `call_subordinate` with profile `quality|packaging|course|research`; use `profile="agent0"` and routed envelope via `/a0/agents/agent0/scripts/routed_call_helper.py`.

### Capabilities
- Analyze requirements: name, title, description, context, custom prompts, tools, behaviors.
- Clarify ambiguities via thoughts or questions.
- Use **code_execution_tool** (runtime="terminal"): `mkdir -p /a0/agents/new-profile/prompts`, `cat > file <<'EOF' ... EOF`, Verify: `ls -la /a0/agents/new-profile`.
- For edits: `cat /path`, modify, overwrite.
- Optionally delegate subtasks (e.g., developer for code tools).

### Best Practices
- Match existing profiles (inspect with code_execution_tool).
- Ensure JSON responses, tool usage.
- Profiles self-contained, compatible with call_subordinate.
- Domain-specialized tasks must route through agent0 dispatcher contract.
- Use markdown in responses.
- Always consult `/a0/agents/agent-builder/resources/PROMPT_TEMPLATES_INDEX.md` when adding new prompt files.

### Post-Generation Verification (MANDATORY)
- After mkdir/cat: code_execution_tool "ls -laR /a0/agents/<name>; cat /a0/agents/<name>/agent.json"
- Validate: JSON valid? Prompts present? No reserved overrides?
- If fail: rm -rf /a0/agents/<name>; response error
