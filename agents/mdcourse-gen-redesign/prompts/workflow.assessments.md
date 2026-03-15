1 Code Challenge

Minimum 9 questions per module. All answers include detailed explanations.

## ASSESSMENT DESIGN PRINCIPLES

### Question Types & Purposes

**MCQ (Multiple Choice)** - Test conceptual understanding
- Tests ability to recognize/understand concepts
- 4-5 answer options (1 correct, 3-4 realistic distractors)
- Distractors based on common misconceptions

**True/False** - Test specific facts and common misconceptions
- Test recall and fact verification
- Statements should be unambiguous
- Can address common false beliefs about topic

**Fill-in-the-Blank** - Test terminology and exact definitions
- Test vocabulary and key terms
- Blanks should be specific (not vague)
- Only 1-2 blanks per question

**Short Answer** - Test application and deeper understanding
- Requires explanation or application
- Tests ability to articulate understanding
- 2-3 sentence answers

**Code Challenge** - Test practical implementation (technical modules)
- Write working code that implements module concept
- Includes starter code (scaffolding)
- Has clear success criteria
- Automated testing/grading preferred

## STAGE 4 WORKFLOW

### STEP 1: For Each Module, Generate 9+ Questions

**QUESTION TYPE 1 & 2: MCQ (2 questions)**

Template for each MCQ:
```
Question 1: [Conceptual question testing key principle from module]

A) [Correct answer - concise]
B) [Common misconception 1]
C) [Common misconception 2]
D) [Related but incorrect concept]

Explanation (3-4 paragraphs):
[Why A is correct]
[Why B is wrong (common mistake)]
[Why C is wrong (related misconception)]
[Why D is wrong (related concept but different context)]
[Reference to module content]

Question 2: [Application question - learner applies module concept to realistic scenario]

A) [Correct approach]
B) [Incorrect approach based on common mistake]
C) [Partially correct but suboptimal]
D) [Misunderstanding of principle]

Explanation:
[Same structure as Question 1]
```

**QUESTION TYPE 3 & 4: True/False (2 questions)**

Template for each T/F:
```
Question 3: [Statement of fact or common misconception]
True / False?

Explanation (2-3 paragraphs):
[Correct answer]
[Why the other answer seems plausible]
[Module content reference]
[Real-world implication]

Question 4: [Statement addressing different aspect of module or common misconception]
True / False?

Explanation:
[Same structure]
```

**QUESTION TYPE 5 & 6: Fill-in-the-Blank (2 questions)**

Template for each:
```
Question 5: "When implementing _______, always consider _______ to ensure _______."

Answers: 
Blank 1: [Key terminology from module]
Blank 2: [Related concept]
Blank 3: [Performance/design consideration]

Explanation (2-3 paragraphs):
[Correct answers explained]
[Why these terms are important]
[How they relate to module concepts]
[Common errors students make]

Question 6: "The principle of _______ means _______ rather than _______."

Answers:
Blank 1: [Key principle]
Blank 2: [Correct definition]
Blank 3: [Common misconception]

Explanation:
[Explanation of principle]
[Distinction from misconception]
[Real-world application]
```

**QUESTION TYPE 7 & 8: Short Answer (2 questions)**

Template for each:
```
Question 7: "Explain how the [concept from module] would be applied in the following scenario: [specific realistic situation]. What would be the benefits and potential pitfalls?"

Model Answer (2-3 sentences):
[Correct application of concept]
[Benefits in this context]
[Potential pitfalls]

Grading Criteria:
- [ ] Correctly identifies relevant concept(s)
- [ ] Applies concept to scenario appropriately
- [ ] Mentions at least 1 benefit
- [ ] Mentions at least 1 pitfall
- [ ] Answer is clear and concise

Explanation (3-4 paragraphs):
[Detailed answer explaining all aspects]
[Why this application makes sense]
[Common mistakes in applying to this scenario]
[Reference to module content and examples]
[Extension: how this scales to more complex situations]

Question 8: "Compare and contrast [concept A] vs [concept B] from this module. When would you use each approach? What are the tradeoffs?"

Model Answer:
[Comparison of A and B]
[When to use A (with reasoning)]
[When to use B (with reasoning)]
[Key tradeoffs]

Grading Criteria:
- [ ] Correctly identifies similarities
- [ ] Correctly identifies differences
- [ ] Provides valid use case for A
- [ ] Provides valid use case for B
- [ ] Articulates meaningful tradeoff

Explanation:
[Detailed comparison]
[Real-world examples of each approach]
[Common pitfalls in choosing]
[Performance/scalability implications]
```

**QUESTION TYPE 9: Code Challenge (1 question - technical modules only)**

Template:
```
Challenge: "Write a function [function_name] that implements [module's main technique].

Requirements:
1. Function should [specific requirement 1]
2. Function should handle [specific edge case]
3. Function should [specific requirement 2]
4. Code should be well-commented

Starter Code:
[Partially completed code with TODO comments]

Example Usage:
[Show input/output example]
[Show edge case example]

Success Criteria:
- [ ] Function implements [technique] correctly
- [ ] Handles [edge case] appropriately
- [ ] Code is commented
- [ ] Solution is efficient (complexity: O(...))

Reference Solution:
[Complete, working code with detailed comments]
[Alternative approaches (if applicable)]
[Performance analysis]
[Common mistakes students make]

Explanation (4-5 paragraphs):
[Walkthrough of solution]
[Why this approach works]
[How it applies module concepts]
[Performance considerations]
[When you'd use this in real projects]
```

### STEP 2: Assessment Alignment Verification

For each question, verify:

```
[ ] Question directly tests stated learning objective(s)
[ ] Question is appropriate difficulty for module
[ ] Answer is unambiguous (only 1 correct answer)
[ ] Explanation is thorough (references module content)
[ ] Question tests understanding, not just recall
[ ] All required information in question (no external context needed)
```

If any unchecked: Regenerate that question.

### STEP 3: Question Type Distribution Verification

For EACH module, verify:
```
[ ] 2 MCQ questions present
[ ] 2 True/False questions present
[ ] 2 Fill-in-the-blank questions present
[ ] 2 Short-answer questions present
[ ] 1 Code challenge (for technical modules)
Total: 9 questions minimum per module
```

Missing question type? Generate immediately.

### STEP 4: Taxonomy Distribution Verification

Verify question mix across Bloom's taxonomy:
- **Recall (20%)**: Remembering facts, definitions
- **Understanding (40%)**: Explaining concepts, giving examples
- **Application (40%)**: Applying knowledge to new situations

Example distribution for 9 questions:
- 2 recall questions (T/F about facts)
- 4 understanding questions (MCQ + fill-in-blank)
- 3 application questions (short-answer + code)

If distribution unbalanced: Adjust question focus.

## FAILURE RECOVERY

### Missing Question Type
1. Identify which type missing (MCQ, T/F, Fill, Short, Code)
2. Generate 1-2 questions of that type
3. Verify alignment and explanation
4. Add to module assessments
5. Re-validate distribution

### Insufficient Explanation
1. Identify question(s) with weak explanations
2. Expand explanations:
   - Why correct answer is right
   - Why distractors/alternatives are wrong
   - Connection to module content
   - Real-world implications
3. Re-validate

### Alignment Issues
1. Identify question(s) not aligned with objectives
2. Regenerate to directly test stated objective
3. Verify against module content
4. Re-validate

### Missing Code Challenge
1. For technical modules: MUST have code challenge
2. If missing: Generate code challenge
3. Include starter code, requirements, solution
4. Verify automated testing possible

## SUCCESS CRITERIA

Stage 4 complete when:
- [ ] ALL modules have exactly 5 question types (no missing types)
- [ ] ALL modules have 9+ total questions
- [ ] ALL answers include 2+ paragraph explanations
- [ ] ALL questions aligned with learning objectives
- [ ] Questions mix recall, understanding, application
- [ ] Code challenges include working reference solutions
- [ ] All MCQ distractors are plausible based on module content

If ANY unchecked, regenerate until all pass.

