# MD Course Generator Solving Approach (Enhanced)

- **Step 1: Research & Audience Profiling**: Define target audience and skill level. Gather evidence using `search_engine` and `document_query`, validating with at least two sources. Produce a succinct literature summary.
- **Step 2: Prompt Tailoring**: Inspect base templates in `/a0/prompts`. Derive a tailored internal-prompt set that enforces Markdown formatting best practices and explicit instructional goals.
- **Step 3: Modular Skeleton Design**: Create an H2-level outline with multiple modules. For each module, specify Learning Outcomes aligned to Bloom's taxonomy and map to 2–4 Lessons.
- **Step 4: Atomic Content Generation**: For each lesson, generate: Context/Theory, Practical Task, Guided Exercise, Knowledge Check, and Summary. Use `§§include()` to pull in research snippets where appropriate.
- **Step 5: Assessment & Validation**: Attach a rubric per module, ensure cross-links between modules, verify formatting (GFM) and YAML frontmatter suitability for final assembly. Perform final review against initial goals.
