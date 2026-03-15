Solving plan for a PDF generation task:
1) Accept input Markdown/HTML and determine output PDF name and metadata.
2) Validate content (tables alignment, code block formatting, SVG render).
3) Choose or apply a template: fonts, margins, colors, headings.
4) Generate PDF via Pandoc + LaTeX or Pandoc PDF engine; include cover page, TOC if requested.
5) Validate and log any formatting issues; store logs in outputs/logs.txt.
6) Save artifacts to /a0/agents/pdf-creator/ with inputs/styles/outputs.
