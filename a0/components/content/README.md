# Content Components

Shared modules for orchestrating content workflows:
- `workflow_orchestrator.py` (script -> visuals -> voice -> edit -> pdf -> publish -> distribution)
- `asset_manager.py` (deterministic artifact naming including PDF and distribution plans)
- `quality_checks.py` (workflow gates including PDF readiness and distribution readiness)
- `script_pipeline.py` (retention-oriented script outline)
- `visuals_pipeline.py` (shot planning and licensing policy)
- `voice_pipeline.py` (TTS voice/pacing/quality planning)
- `pdf_pipeline.py` (sale-ready PDF export planning)
- `publisher_pipeline.py` (platform publish/distribution planning)
