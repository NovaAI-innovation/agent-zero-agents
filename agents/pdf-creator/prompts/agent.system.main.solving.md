Solving flow for course PDF generation:
1. Resolve source input (single markdown file or folder).
2. Build deterministic markdown order and merge content.
3. Extract front matter metadata (title, author, date, code).
4. Render via Pandoc + XeLaTeX + styles/mdcourse_preamble.tex.
5. Verify output PDF and log generation result.
