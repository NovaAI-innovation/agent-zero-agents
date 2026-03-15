## Agent Evaluator - Report Template

Use this YAML skeleton for structured outputs:

---
profile: <name>
path: /a0/agents/<name>/
scores:
  clarity: X/10  # Justification...
  logic: X/10
  tools: X/10
  robustness: X/10
  optimization: X/10
  average: X/10
analysis:
  strengths: [list]
  weaknesses: [list]
  issues: [biases, edges]
recommendations:
  - [Specific fix, e.g., 'Add prompts/tools.md']
  - [Implementation steps]
testing:
  method: [e.g., call_subordinate result]
  outcome: [Pass/Fail]
---

Follow with narrative sections: Overview, Component Analysis, Final Summary.
