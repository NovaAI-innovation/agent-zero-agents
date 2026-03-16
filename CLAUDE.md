# Agent Zero Profile Creation Guide

## Core Structure
Every agent profile lives in `/a0/agents/<name>/` with:
- `agent.json` - Configuration & metadata
- `_context.md` - Framework context & capabilities
- `prompts/` - Specialized prompt files (role, override, behavior)

## agent.json Essentials
```json
{
  "name": "agent-name",
  "title": "Human-readable title",
  "description": "Concise capability summary",
  "type": "specialized",
  "version": "1.0.0",
  "prompts": {
    "role": "prompts/role.md",
    "override": "prompts/override.md"
  },
  "skills": [],
  "config": {}
}
```

## Prompt File Best Practices

### role.md (Primary Identity)
- **First 2-3 lines**: Concise role statement
- **Specialization section**: Core capabilities & expertise
- **Problem-solving approach**: How this agent tackles tasks
- **Output format**: Expected response structure
- **Key constraints**: Safety boundaries

### override.md (Framework Overrides)
- Only include what differs from default
- Focus on communication style, tool preferences
- Keep behavioral adjustments minimal
- Reference framework manual sections if complex

### behavior.md (Optional)
- Agent-specific behavioral rules
- Response preferences
- Tool usage patterns
- Decision-making priorities

## Design Patterns

### Specialization Hierarchy
1. **Generic agents**: Minimal prompts, rely on defaults
2. **Specialized agents**: Domain-specific expertise, custom tools
3. **Expert agents**: Deep context, refined output, strict patterns

### Tool Integration
- List required tools in agent.json
- Explain tool usage in role.md
- Avoid redundant tool descriptions
- Reference framework capabilities

### Subordinate Agent Design
- Keep roles focused and non-overlapping
- Define clear input/output contracts
- Avoid circular delegation patterns
- Orchestrator agents coordinate, don't duplicate

## Prompt Optimization for LLMs

### Clarity Rules
- Use direct imperative language
- Structure with headers and lists
- One concept per paragraph
- Define terms upfront

### Length vs Quality
- Concise > verbose (model efficiency)
- Examples > explanations
- Constraints > suggestions
- Focus on what matters

### Framework Integration
- Reference manual sections by name
- Use replacement syntax (`§§`) for dynamic values
- Include file paths, not file contents
- Leverage built-in capabilities

## Common Mistakes to Avoid

❌ Duplicating framework documentation  
❌ Creating overlapping agent roles  
❌ Ignoring tool constraints  
❌ Verbose prompts (LLMs work better concise)  
❌ Missing error handling guidance  
❌ Circular subordinate delegation  

## Creation Workflow

1. **Define role** - What is this agent's expertise?
2. **Map to framework** - What tools/capabilities needed?
3. **Write role.md** - Concise identity & approach
4. **Configure agent.json** - Metadata & tool bindings
5. **Test with subordinate tool** - Verify behavior
6. **Refine prompts** - Optimize based on results
7. **Document constraints** - Clear limitations

## Framework References
- Agent profiles: `/a0/agents/`
- Manual section: Tools → call_subordinate
- Template index: Prompt profiles available
- Tool docs: Each tool has usage patterns

## Quick Checklist
- [ ] agent.json is valid JSON
- [ ] role.md defines clear expertise
- [ ] No framework docs duplication
- [ ] Tools listed & explained
- [ ] Test with small task
- [ ] Override.md only has differences
- [ ] Prompts are concise (<500 words ideal)
