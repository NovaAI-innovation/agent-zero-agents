# Packaging Domain Context

This domain consolidates packaging behaviors currently spread across prompt and template agents.

## Scope
- Build packaged deliverables
- Generate listing/marketing metadata
- Produce implementation and usage documentation
- Integrate quality checks from the Quality domain

## Shared Components
- `/a0/components/packaging/marketplace_lister.py`
- `/a0/components/packaging/package_builder.py`
- `/a0/components/packaging/documentation_gen.py`
- `/a0/components/packaging/eval_integrator.py`
- `/a0/components/packaging/validator.py`

## Runtime Entry
- `agents/packaging/scripts/prepare_package.py`
  - Builds manifest, listing bundle, docs bundle
  - Generates quality-domain request payload

## Constraints
- Reuse common packaging flows instead of per-agent duplication.
- Call Quality domain for final validation when packaging outputs are generated.
