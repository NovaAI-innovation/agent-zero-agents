## 🎯 Strategic Vision

### Current State: 19 Specialized Agents
```
┌─────────────┬──────────────┬──────────────┬──────────────┬─────────┐
│ Evaluation  │ Content      │ Products     │ Utility      │ Core    │
├─────────────┼──────────────┼──────────────┼──────────────┼─────────┤
│ • prompt-   │ • script-    │ • mdcourse-  │ • developer  │ • agent0│
│   evaluator │   writer     │   gen        │ • agent-     │         │
│ • agent-    │ • voice-ai   │ • pdf-       │   builder    │ Research│
│   evaluator │ • visuals-   │   creator    │ • hacker     │ ────────│
│ • prompt-   │   hybrid     │ • notion-    │ • branding   │ • gumroad│
│   packer    │ • publisher  │   template   │ • video-     │   analyzer
│             │              │ • prompt-    │   editor     │ • researcher
│             │              │   packer     │ • file-      │
│             │              │              │   manager    │
└─────────────┴──────────────┴──────────────┴──────────────┴─────────┘

**Problems**:
❌ 3x evaluation logic duplication (prompt-eval, agent-eval, eval in packer)
❌ Monolithic course pipeline (8 stages in 1 agent)
❌ Parallel packaging agents (prompt-packer + notion-template = 80% overlap)
❌ Code reuse nearly impossible
❌ High maintenance surface area
```

### Target State: 8-10 Domain Agents + Shared Components
```
┌──────────────────────────────────────────────────────────────────────┐
│                      Agent Zero Orchestrator                         │
└────┬─────────┬──────────┬──────────┬──────────┬──────────┬──────────┘
     │         │          │          │          │          │
  ┌──▼──┐  ┌──▼───┐  ┌──▼────┐ ┌──▼─────┐ ┌──▼────┐ ┌──▼──┐  ┌──▼────┐
  │Quality     Packaging  Course   Content  Research Branding Infrastructure
  │ Domain    │ Domain    Domain   Domain   Domain   Domain  │ Domain
  ├────────┐ ├────────┐ ├──────┐ ├──────┐ ├──────┐ ├──────┐ ├────────┐
  │• eval: │ │• pack: │ │Stage:│ │Script │ │• gen │ │Logo  │ │• dev   │
  │  prompt│ │  prompt│ │Bluep │ │Writer │ │      │ │Design│ │• infra │
  │• eval: │ │• pack: │ │Stage:│ │Visuals│ │• mkt │ │Brand │ │
  │  agent │ │  templ │ │Cont  │ │Voice  │ │  ana │ │  Kit │ │
  │• eval: │ │• pack: │ │Stage:│ │Edits  │ │• trend│ │      │ │
  │  pack  │ │  course│ │Assess│ │Pub   │ │      │ │      │ │
  │        │ │        │ │Stage:│ │      │ │      │ │      │ │
  │Shared: │ │Shared: │ │Multi │ │Shared:│ │      │ │      │ │
  │• score │ │• list  │ │Stage:│ │• orch │ │      │ │      │ │
  │• feed  │ │• build │ │Market│ │      │ │      │ │      │ │
  │• report│ │• doc   │ │Stage:│ │      │ │      │ │      │ │
  │        │ │        │ │Price │ │      │ │      │ │      │ │
  │        │ │        │ │Stage:│ │      │ │      │ │      │ │
  │        │ │        │ │Valid │ │      │ │      │ │      │ │
  │        │ │        │ │Stage:│ │      │ │      │ │      │ │
  │        │ │        │ │Deliv │ │      │ │      │ │      │ │
  │        │ │        │ │      │ │      │ │      │ │      │ │
  │        │ │        │ │Shared:│ │      │ │      │ │      │ │
  │        │ │        │ │• contract │      │      │ │      │ │
  │        │ │        │ │• orch     │      │      │ │      │ │
  │        │ │        │ │• artifact │      │      │ │      │ │
  └────────┘ └────────┘ └─────────┘ └──────┘ └──────┘ └──────┘ └────────┘

         ↓ All call Quality Domain for validation ↓
```

---

## 🔑 Key Consolidations

### 1️⃣ Quality Domain (High Priority)
**Merge**: `prompt-evaluator` + `agent-evaluator` + eval logic from `prompt-packer`

✅ **Extract Components**:
```python
/a0/components/quality/
├── scoring_engine.py       # Rubric definitions, calculation
├── feedback_generator.py   # Score → critique conversion
├── report_formatter.py     # Report generation
└── rubrics/               # YAML rubric definitions
```

**Benefit**: Single source of truth for evaluation; reusable across all agents

---

### 2️⃣ Packaging Domain (High Priority)
**Merge**: `prompt-packer` + `notion-template-generator`

✅ **Extract Components**:
```python
/a0/components/packaging/
├── marketplace_lister.py   # Gumroad/SendOwl listing copy
├── package_builder.py      # Archive creation, file organization
├── documentation_gen.py    # Usage guides, implementation docs
└── eval_integrator.py     # Call quality:eval:pack
```

**Benefit**: Consistent product workflow; reusable marketplace tools

---

### 3️⃣ Course Pipeline Deconstruction (High Priority)
**Break apart**: `mdcourse-gen-redesign` (8 stages → 8 callable components)

✅ **Extract Components**:
```python
/a0/components/course/
├── stage_contracts.py      # Input/output schemas
├── orchestrator.py         # Pipeline state, resumption
├── artifact_manager.py     # Track files, dependencies
└── stages/
    ├── blueprint_gen.py    # Generate course structure
    ├── content_dev.py      # Develop modules
    ├── assessment_gen.py   # Create assessments
    ├── multimedia_src.py   # Source images/videos
    ├── marketing_strat.py  # Sales strategy
    ├── pricing_ana.py      # Pricing recommendations
    ├── validate_qa.py      # Quality validation
    └── package_del.py      # Package for delivery
```

**Benefits**:
- Individual stages callable independently
- Can pause/resume long pipelines
- Easy to test each stage in isolation
- Reusable in other workflows

---

### 4️⃣ Content Production (Minor improvements)
**Keep**: `script-writer` → `visuals-hybrid` → `voice-ai` → `video-editor` → `platform-publisher`

✅ **Add orchestration**:
```python
/a0/components/content/
├── workflow_orchestrator.py  # Coordinate stages
├── asset_manager.py          # Track generated files
└── quality_checks.py         # Audio sync, visual QA
```

**Already well-structured** - minimal changes needed

---

### 5️⃣ Research Consolidation (Low Priority)
**Merge**: `gumroad-analyzer` + `researcher`

✅ Single Research domain with modes (general, market, trends)

---

## 📊 Benefits Summary

| Aspect | Current | After |
|--------|---------|-------|
| **Agent Count** | 19 | 8-10 |
| **Code Duplication** | High (eval x3) | None |
| **Reusability** | Low | High |
| **Testing Surface** | Large | Medium |
| **Maintenance** | High | Medium |
| **Flexibility** | Limited | High |
| **New Workflows** | Needs new agent | Use components |

---

## 🚀 6-Phase Implementation Roadmap

**Phase 1**: ✅ Planning (Complete)
- Architecture design
- Component identification  
- Service contracts

**Phase 2**: Quality & Packaging (Weeks 1-4)
- Extract shared components
- Create Quality domain agent
- Create Packaging domain agent

**Phase 3**: Course Deconstruction (Weeks 5-8)
- Extract 8 course stages
- Create orchestrator
- Test individual stages

**Phase 4**: Content Production (Weeks 9-10)
- Add orchestration layer
- Extract asset management

**Phase 5**: Research & Utility (Weeks 11-12)
- Consolidate research agents
- Clean up infrastructure

**Phase 6**: Integration & Testing (Weeks 13-15)
- Update agent0
- End-to-end testing
- Archive old agents

---

## 📁 Component Library Structure

```
/a0/components/
├── quality/              # Evaluation & scoring
├── packaging/            # Product creation  
├── course/               # Course pipeline stages
├── content/              # Video/multimedia
├── research/             # Market analysis
└── shared/               # Common utilities
```

---

## 💡 Usage Examples (After Consolidation)

```python
# Quality evaluation
result = call_subordinate(
    profile="quality",
    message="Evaluate using quality:eval-prompt\nPrompt: [text]"
)

# Individual course stage
result = call_subordinate(
    profile="course",
    message="Execute stage:pricing\nBlueprint: /path/blueprint.json"
)

# Product packaging
result = call_subordinate(
    profile="packaging",
    message="Create prompt pack\nType: prompt-pack\nNiche: python"
)
```

---

## ✅ Next Steps


**Validate** architecture and domain definitions
**Define** detailed component APIs and contracts
**Kickoff Phase 2** when ready (Quality & Packaging consolidation)
**Create** component extraction tools/utilities

