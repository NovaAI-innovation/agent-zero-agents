# Course Domain Context

This domain runs the stage-based course pipeline and owns cross-stage continuity.

## Scope
- Blueprint generation
- Module content generation
- Assessment generation
- Multimedia planning
- Marketing strategy
- Pricing analysis
- Validation and delivery packaging

## Shared Components
- `/a0/components/course/stage_contracts.py`
- `/a0/components/course/artifact_manager.py`
- `/a0/components/course/orchestrator.py`
- `/a0/components/course/stages/*.py`

## Runtime Entry
- `agents/course/scripts/orchestrate.py`
  - Executes full stage order
  - Returns per-stage outputs and artifact registry
