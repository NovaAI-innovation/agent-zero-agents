# Assessment Generation Engine

## ALGORITHM

### QUESTION TYPE DISTRIBUTION
- MCQ: 40% (4 options, 1 correct)
- True/False: 20%
- Fill-in-Blank: 15%
- Short Answer: 15%
- Code Challenge: 10%

### DIFFICULTY SCALING
```javascript
BEGINNER (Module 1-3): 70% MCQ/TF, 30% Fill-in
INTERMEDIATE (4-7): 50% MCQ, 30% Short/Code, 20% Fill-in
ADVANCED (8+): 40% Code/Short, 40% MCQ, 20% TF
```

### JSON FORMAT
```json
{
  "module": 5,
  "difficulty": "intermediate",
  "questions": [
    {
      "type": "mcq",
      "question": "What is...?",
      "options": ["A", "B", "C", "D"],
      "correct": "B",
      "explanation": "..."
    }
  ],
  "passing_score": 80
}
```

### AUTO-GRADING LOGIC
- MCQ/TF: Exact match
- Fill-in: Keyword detection
- Short Answer: Semantic similarity
- Code: Syntax + output validation

### DELIVERY
/assessments/[module]/[difficulty].json
└── answer_keys.md
