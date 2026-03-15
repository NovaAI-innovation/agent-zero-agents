# PDF Creator v2

Converts markdown artifacts from `agents/mdcourse-gen-redesign` into polished, sale-ready PDFs.

## Primary command

```bash
agents/pdf-creator/scripts/build_sale_ready_pdf.sh <input.md|input_dir> [output.pdf|output_dir]
```

## Behavior

- Accepts a single markdown file or a directory of markdown files.
- Extracts metadata from YAML front matter when present.
- Merges folder inputs in deterministic order.
- Renders with Pandoc + XeLaTeX using `styles/mdcourse_preamble.tex`.
- Writes logs to `agents/pdf-creator/outputs/generation.log`.

## Compatibility

`convert_markdown_to_pdf.sh` remains available as a wrapper to the new script.
