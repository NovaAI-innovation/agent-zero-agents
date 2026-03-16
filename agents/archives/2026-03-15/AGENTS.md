# Repository Guidelines

## Project Structure & Module Organization
This repository is an agent profile collection. Each top-level directory is an agent (for example `agent-builder/`, `researcher/`, `pdf-creator/`).

Expected layout per agent:
- `agent.json`: metadata, prompt bindings, and config
- `_context.md`: framework and capability context
- `prompts/`: role/override/system prompt files
- Optional support folders like `scripts/`, `assets/`, `inputs/`, `outputs/`, or `styles/`

Use kebab-case for agent directories and keep prompt files grouped by concern (`role`, `communication`, `solving`, `tools`).

## Project Instructions (Architecture Direction)
Contributors should align changes with the consolidation plan in `new-structure.md`:
- Reduce overlap by converging toward domain agents (Quality, Packaging, Course, Content, Research, Branding, Infrastructure).
- Prefer reusable shared components over duplicating logic across agents.
- Route evaluation behavior through a single Quality domain path instead of per-agent custom evaluators.
- Keep course workflows stage-oriented and composable to support pause/resume and isolated testing.
- Route domain execution through `agent0` (`agents/agent0/scripts/dispatch.py` and `agents/agent0/scripts/routed_call_helper.py`) instead of direct domain-profile subordinate calls.

When adding or editing prompt fragments, use `prompts-index.md` as the canonical reference for prompt purpose and naming expectations.

## Build, Test, and Development Commands
There is no single build system at repo root. Validate changes with lightweight checks:

```powershell
rg --files
```
List tracked files quickly to verify placement.

```powershell
Get-Content .\agent-builder\agent.json | ConvertFrom-Json | Out-Null
```
Sanity-check JSON structure for an edited agent.

```powershell
rg -n '"prompts"|"role"|"override"' .\*\agent.json
```
Confirm prompt mappings exist and are consistent.

Run agent-specific scripts only from that agent folder (example: `pdf-creator/scripts/convert_markdown_to_pdf.sh`).

## Coding Style & Naming Conventions
- Markdown: concise sections, direct instructions, no duplicated framework docs.
- JSON: 2-space indentation, stable key ordering where practical (`name`, `title`, `description`, `type`, `version`, `prompts`, `skills`, `config`).
- File/folder names: kebab-case (`prompt-packer`, `agent.system.main.role.md`).
- Keep prompts short and explicit; prefer constraints and examples over long prose.

## Testing Guidelines
Primary validation is structural and behavioral:
- Parse edited `agent.json` files.
- Verify referenced prompt files exist.
- Smoke-test with a small task in the target agent before opening a PR.
- For architecture-facing changes, include a short note on how the change supports consolidation from `new-structure.md`.

When adding scripts, include a minimal usage example in that agent's README or `_context.md`.

## Commit & Pull Request Guidelines
Follow the existing history style:
- Prefer concise imperative summaries (`Fix skills_tool load when loaded_skills is uninitialized`).
- Conventional prefixes are acceptable when useful (`feat: ...`).

For PRs:
- Describe which agent(s) changed and why.
- List file paths touched.
- Reference relevant architecture notes (`new-structure.md`) and prompt references (`prompts-index.md`) when applicable.
- Include before/after behavior for prompt or workflow changes.
- Link related issue/thread when applicable.
