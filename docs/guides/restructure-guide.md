# Repository Restructure Guide

## Overview

This guide shows how the repository will be reorganized to support multiple research waves while keeping Wave 1 findings accessible and well-organized.

---

## Before → After Migration

### Data Files

```
BEFORE:
discovering-ben/
└── conversations.json

AFTER:
discovering-ben/
├── data/
│   ├── raw/
│   │   └── conversations.json          # Copy (original preserved)
│   └── processed/
│       └── [future datasets]
```

### Python Scripts

```
BEFORE:
discovering-ben/
├── cycle_1_information_overload_detector.py
├── cycle_2_one_best_thing_detector.py
├── cycle_3_perfectionism_escalation_detector.py
├── cycle_4_emotional_dysregulation_detector.py
├── cycle_5_mind_reading_detector.py
├── cycle_6_system_building_detector.py
├── cycle_7_special_interest_detector.py
├── cycle_1_semantic_analyzer.py
├── cycle_2_semantic_analyzer.py
├── cycle_3_semantic_analyzer.py
├── cycle_4_semantic_analyzer.py
├── cycle_5_semantic_analyzer.py
├── cycle_6_semantic_analyzer.py
├── cycle_7_semantic_analyzer.py
├── pattern_search.py
└── claude_response_analysis.py

AFTER:
discovering-ben/
├── analysis/
│   └── wave-1-vicious-cycles/
│       └── scripts/
│           ├── detectors/
│           │   ├── cycle_1_information_overload_detector.py
│           │   ├── cycle_2_one_best_thing_detector.py
│           │   ├── cycle_3_perfectionism_escalation_detector.py
│           │   ├── cycle_4_emotional_dysregulation_detector.py
│           │   ├── cycle_5_mind_reading_detector.py
│           │   ├── cycle_6_system_building_detector.py
│           │   └── cycle_7_special_interest_detector.py
│           └── semantic-analyzers/
│               ├── cycle_1_semantic_analyzer.py
│               ├── cycle_2_semantic_analyzer.py
│               ├── cycle_3_semantic_analyzer.py
│               ├── cycle_4_semantic_analyzer.py
│               ├── cycle_5_semantic_analyzer.py
│               ├── cycle_6_semantic_analyzer.py
│               └── cycle_7_semantic_analyzer.py
└── tools/
    ├── pattern-search.py
    └── claude-response-analysis.py
```

### JSON Outputs

```
BEFORE:
discovering-ben/
├── cycle_1_information_overload_findings.json
├── cycle_2_one_best_thing_findings.json
├── cycle_3_perfectionism_escalation_findings.json
├── cycle_4_emotional_dysregulation_findings.json
├── cycle_5_mind_reading_findings.json
├── cycle_6_system_building_findings.json
├── cycle_7_special_interest_findings.json
├── cycle_1_semantic_findings.json
├── cycle_2_semantic_findings.json
├── cycle_3_semantic_findings.json
├── cycle_4_semantic_findings.json
├── cycle_5_semantic_findings.json
├── cycle_6_semantic_findings.json
└── cycle_7_semantic_findings.json

AFTER:
discovering-ben/
└── analysis/
    └── wave-1-vicious-cycles/
        └── outputs/
            ├── cycle_1_information_overload_findings.json
            ├── cycle_2_one_best_thing_findings.json
            ├── cycle_3_perfectionism_escalation_findings.json
            ├── cycle_4_emotional_dysregulation_findings.json
            ├── cycle_5_mind_reading_findings.json
            ├── cycle_6_system_building_findings.json
            ├── cycle_7_special_interest_findings.json
            ├── cycle_1_semantic_findings.json
            ├── cycle_2_semantic_findings.json
            ├── cycle_3_semantic_findings.json
            ├── cycle_4_semantic_findings.json
            ├── cycle_5_semantic_findings.json
            ├── cycle_6_semantic_findings.json
            └── cycle_7_semantic_findings.json
```

### Documentation

```
BEFORE:
discovering-ben/
└── docs/
    ├── cycle-1-information-overload-complete-analysis.md
    ├── cycle-2-one-best-thing-complete-analysis.md
    ├── cycle-3-perfectionism-escalation-complete-analysis.md
    ├── cycle-4-emotional-dysregulation-complete-analysis.md
    ├── cycle-6-system-building-complete-analysis.md
    ├── cycle-7-special-interest-hyperfocus-complete-analysis.md
    ├── cycles-summary-complete-analysis.md
    ├── system-prompt-recommendations.md
    ├── benjamin-custom-system-prompt.md
    ├── investigation-plan-additional-reinforcement-cycles.md
    └── neurodivergent-llm-interaction-analysis.md

AFTER:
discovering-ben/
├── analysis/
│   └── wave-1-vicious-cycles/
│       └── docs/
│           ├── cycle-1-information-overload-complete-analysis.md
│           ├── cycle-2-one-best-thing-complete-analysis.md
│           ├── cycle-3-perfectionism-escalation-complete-analysis.md
│           ├── cycle-4-emotional-dysregulation-complete-analysis.md
│           ├── cycle-6-system-building-complete-analysis.md
│           ├── cycle-7-special-interest-hyperfocus-complete-analysis.md
│           └── cycles-summary-complete-analysis.md
├── system-prompts/
│   ├── benjamin/
│   │   ├── v1-compact.md                    # benjamin-custom-system-prompt.md
│   │   └── changelog.md                     # NEW
│   └── recommendations/
│       └── system-prompt-recommendations.md
└── docs/
    ├── methodology/
    │   └── investigation-plan-additional-reinforcement-cycles.md
    └── background/
        └── neurodivergent-llm-interaction-analysis.md
```

---

## How to Run the Restructure

### Option 1: Automated Script (Recommended)

```bash
# From repository root
./restructure.sh
```

The script will:
- Create new folder structure
- Move all files to new locations
- Update file paths in Python scripts
- Create README files for each directory
- Preserve original files temporarily in archive/

### Option 2: Manual Restructure

If you prefer to review each step:

```bash
# 1. Create directories
mkdir -p data/raw data/processed
mkdir -p analysis/wave-1-vicious-cycles/{scripts/{detectors,semantic-analyzers},outputs,docs}
mkdir -p system-prompts/{benjamin,recommendations,templates}
mkdir -p docs/{methodology,background,findings,presentations}
mkdir -p tools

# 2. Copy data (preserve original)
cp conversations.json data/raw/

# 3. Move scripts
mv cycle_*_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/
mv cycle_*_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/

# 4. Move outputs
mv cycle_*_findings.json analysis/wave-1-vicious-cycles/outputs/

# 5. Move documentation
mv docs/cycle-*.md analysis/wave-1-vicious-cycles/docs/
mv docs/cycles-summary-*.md analysis/wave-1-vicious-cycles/docs/

# 6. Organize system prompts
mv docs/system-prompt-recommendations.md system-prompts/recommendations/
mv docs/benjamin-custom-system-prompt.md system-prompts/benjamin/v1-compact.md

# 7. Move methodology
mv docs/investigation-plan-*.md docs/methodology/

# 8. Move background
mv docs/neurodivergent-llm-*.md docs/background/

# 9. Move tools
mv pattern_search.py tools/pattern-search.py
mv claude_response_analysis.py tools/claude-response-analysis.py
```

---

## Path Updates Required

After restructure, update paths in scripts:

### Detector Scripts

**Old path:**
```python
with open('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json', 'r') as f:
```

**New path:**
```python
with open('../../../data/raw/conversations.json', 'r') as f:
```

**Old output path:**
```python
output_path = '/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/cycle_1_information_overload_findings.json'
```

**New output path:**
```python
output_path = '../../outputs/cycle_1_information_overload_findings.json'
```

### Running Scripts After Restructure

```bash
# Navigate to detector directory
cd analysis/wave-1-vicious-cycles/scripts/detectors

# Run detector
python3 cycle_1_information_overload_detector.py

# Navigate to semantic analyzer directory
cd ../semantic-analyzers

# Run semantic analyzer
python3 cycle_1_semantic_analyzer.py
```

---

## Benefits of New Structure

### 1. Scalability
- Clear home for future research waves
- Each wave self-contained
- Easy to compare across waves

### 2. Organization
- Related files grouped together
- Clear separation of concerns
- Predictable file locations

### 3. Discoverability
- READMEs in each directory
- Clear naming conventions
- Logical hierarchy

### 4. Collaboration
- Easy onboarding for new researchers
- Standard research repository structure
- Version control friendly

### 5. Deployment
- System prompts easy to find
- Clear versioning and changelog
- Implementation guides accessible

---

## Future Research Waves

### Wave 2: Intervention Effectiveness

After deploying system prompts, collect new conversation data to measure:
- Decision abandonment rate reduction (target: <50% from 92.2%)
- Task completion rate increase (target: >60% from 28.1%)
- Emotional baseline recovery (target: >0% from 0%)

```
analysis/wave-2-intervention-effectiveness/
├── scripts/
│   ├── compare-pre-post-metrics.py
│   └── statistical-significance-test.py
├── outputs/
│   └── effectiveness-metrics.json
└── docs/
    └── intervention-effectiveness-report.md
```

### Wave 3: Longitudinal Analysis

Track cycle patterns over 6-12 months:
- Do cycles recur at same frequency?
- Does severity decrease with interventions?
- Do new patterns emerge?

```
analysis/wave-3-longitudinal-analysis/
├── data/
│   ├── month-1-conversations.json
│   ├── month-3-conversations.json
│   ├── month-6-conversations.json
│   └── month-12-conversations.json
├── scripts/
│   ├── trend-analysis.py
│   └── recurrence-detector.py
└── docs/
    └── longitudinal-findings.md
```

### Wave 4: Cross-Model Comparison

Compare Claude vs GPT vs Gemini:
- Do other models show same cycle patterns?
- Which model best avoids vicious cycles?
- Are interventions model-specific or generalizable?

```
analysis/wave-4-cross-model-comparison/
├── data/
│   ├── claude-conversations.json
│   ├── gpt-conversations.json
│   └── gemini-conversations.json
├── scripts/
│   └── cross-model-cycle-detector.py
└── docs/
    └── model-comparison-report.md
```

### Wave 5: Generalization Study

Test findings on other neurodivergent profiles:
- ADHD users
- Dyslexia users
- Other autism spectrum profiles
- Neurotypical control group

```
analysis/wave-5-generalization-study/
├── data/
│   ├── adhd-profile/
│   ├── dyslexia-profile/
│   └── control-group/
├── scripts/
│   └── cross-profile-detector.py
└── docs/
    └── generalization-findings.md
```

---

## Verification Checklist

After running restructure:

- [ ] All scripts moved to correct locations
- [ ] All outputs preserved in outputs/ directory
- [ ] All documentation accessible
- [ ] Path updates applied to Python scripts
- [ ] Scripts run successfully from new locations
- [ ] README files created in all directories
- [ ] System prompts easy to find
- [ ] Original conversations.json preserved in data/raw/
- [ ] Git tracking updated (if using version control)
- [ ] Archive folder can be safely deleted

---

## Rollback Plan

If issues arise:

1. **Immediate rollback:**
   ```bash
   # Restore from archive
   cp -r archive/pre-restructure/* .
   ```

2. **Incremental rollback:**
   - Archive preserves original structure
   - Can selectively restore specific files
   - Original conversations.json never deleted

3. **Hybrid approach:**
   - Keep both old and new structure temporarily
   - Gradually migrate workflows
   - Delete old structure once confident

---

## Questions?

Common issues and solutions:

**Q: Scripts can't find conversations.json**
A: Update path to `../../../data/raw/conversations.json` (relative to script location)

**Q: Import errors between scripts**
A: Add parent directories to Python path or use absolute imports

**Q: Want to keep old structure**
A: Archive preserves everything - can run both structures in parallel

**Q: How to add new research wave?**
A: Create `analysis/wave-X-description/` with same structure (scripts/outputs/docs/)

**Q: Where to deploy system prompts?**
A: See `system-prompts/recommendations/system-prompt-recommendations.md`
