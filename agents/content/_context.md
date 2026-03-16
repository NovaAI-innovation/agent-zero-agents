# Content Domain

Purpose:
- Orchestrate content production stages across script, visuals, voice, and publishing.
- Provide deterministic stage outputs for planning and handoff.

Capabilities:
- Workflow summary and sequencing.
- Asset checklist and dependency mapping.
- Quality gate summary before delivery/publishing.
- End-to-end content production coverage from legacy roles:
  - script writing
  - visuals planning
  - voiceover preparation
  - sale-ready PDF export
  - platform publishing and distribution planning

Runtime entry:
- `agents/content/scripts/orchestrate_content.py`
  - Returns stage plan, generated artifacts, and readiness state.
