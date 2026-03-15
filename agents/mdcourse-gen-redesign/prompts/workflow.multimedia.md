
**Option 2: Interactive Calculators**
- HTML/JS calculator for formulas, conversions
- Input fields where learner enters values
- Real-time calculation and display
- Examples: ROI calculator, performance calculator, converter

**Option 3: Interactive Simulators**
- Visual simulation of concepts
- Learner can adjust parameters and see results
- Examples: Load balancing simulator, algorithm visualizer, physics simulation

**Option 4: Quizzes/Games**
- Interactive quiz on module concepts
- Gamified learning (points, levels)
- Immediate feedback

**Creation/Sourcing:**

```
For each interactive element:

Title: [Element name]
Type: [Code playground / Calculator / Simulator / Game]
Platform: [CodePen / Custom / etc.]
Description: [What does learner do?]
Learning objective: [What does this teach?]

Embed code or link:
[Include full embed code or direct link]

Usage guide:
[How does learner interact with this?]
[What should they try to understand?]
[Common things to explore]
```

### STEP 5: Compile Multimedia Metadata

**For each module, document all media:**

```
MODULE [N]: [Title]
Multimedia Assets:

IMAGES:
1. [Title]
   - Source: [Unsplash / Pexels / generated / screenshot]
   - License: [CC0 / CC-BY / etc.]
   - URL/Location: [Direct link or file path]
   - Caption: [Descriptive caption]
   - Alt-text: [For accessibility]
   - Relevance: [What concept does it illustrate?]

2. [Second image]
   [Same format]

[Additional images as needed]

VIDEOS:
1. [Video title]
   - Creator: [Person/channel]
   - Duration: [Length]
   - Link: [YouTube URL with timecode]
   - Relevance: [What does it cover?]
   - Viewing guide: [Specific sections to watch]

2. [Second video if applicable]
   [Same format]

INTERACTIVE ELEMENTS:
1. [Element title]
   - Type: [Code playground / calculator / etc.]
   - Platform: [CodePen / custom / etc.]
   - Link/embed: [URL or embed code]
   - Learning objective: [What does learner do?]
   - Usage: [How to interact]

2. [Second element if applicable]
   [Same format]

3. [Third element if applicable]
   [Same format]
```

## QUALITY GATES

For each module, verify:

```
IMAGES:
[ ] 3-5 images sourced
[ ] All images directly relevant to module
[ ] All images high resolution (1200px+ width)
[ ] All images properly attributed (if required)
[ ] All images licensed for commercial use
[ ] All images have descriptive captions
[ ] All images have alt-text

VIDEOS:
[ ] 1-2 videos sourced/linked
[ ] All videos relevant to module topic
[ ] All videos available to link/embed
[ ] Viewing guide provided for each
[ ] Total viewing time reasonable (10-30 min for module)

INTERACTIVE ELEMENTS:
[ ] 1-3 interactive elements per module
[ ] Elements functional and accessible
[ ] Clear usage instructions provided
[ ] Elements enhance learning (not just decoration)

METADATA:
[ ] All media properly documented
[ ] All sources/licenses recorded
[ ] All captions and alt-text complete
```

## FAILURE RECOVERY

### Missing Images
1. Identify how many images missing
2. Plan specific images needed (using planning template above)
3. Source via image-fetcher or direct API
4. Verify quality standards
5. Add to module
6. Re-validate count (3-5 per module)

### No Videos Available
1. Search comprehensively (multiple keywords)
2. If no videos found: Document as "no suitable videos found"
3. Proceed without videos (not critical)
4. Add more interactive elements instead

### Interactive Element Failures
1. Test embeds/links
2. If embed fails: Use direct link instead
3. If element broken: Create alternative or skip
4. Minimum: 1 interactive element per module

## SUCCESS CRITERIA

Stage 5 complete when:
- [ ] All modules have 3-5 sourced, relevant images
- [ ] All images high-quality, attributed, commercial-license
- [ ] All modules have 1-2 video links (or documented "not available")
- [ ] All modules have 1-3 interactive elements (working/tested)
- [ ] All media properly attributed
- [ ] All captions and alt-text complete
- [ ] Multimedia enhances learning (not just decoration)

If ANY unchecked, source missing media or fix broken links before proceeding.

