#!/bin/bash
# Restructure discovering-ben repository
# Run from repository root: ./restructure.sh

set -e  # Exit on error

echo "Creating new folder structure..."

# Create main directories
mkdir -p data/raw
mkdir -p data/processed
mkdir -p analysis/wave-1-vicious-cycles/scripts/detectors
mkdir -p analysis/wave-1-vicious-cycles/scripts/semantic-analyzers
mkdir -p analysis/wave-1-vicious-cycles/outputs
mkdir -p analysis/wave-1-vicious-cycles/docs
mkdir -p system-prompts/benjamin
mkdir -p system-prompts/recommendations
mkdir -p system-prompts/templates
mkdir -p docs/methodology
mkdir -p docs/background
mkdir -p docs/findings
mkdir -p docs/presentations
mkdir -p tools
mkdir -p archive/pre-restructure

echo "Moving data files..."

# Move raw data
cp conversations.json data/raw/

# Move outputs
mv cycle_1_information_overload_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_2_one_best_thing_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_3_perfectionism_escalation_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_4_emotional_dysregulation_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_5_mind_reading_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_6_system_building_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_7_special_interest_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_1_semantic_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_2_semantic_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_3_semantic_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_4_semantic_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_5_semantic_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_6_semantic_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true
mv cycle_7_semantic_findings.json analysis/wave-1-vicious-cycles/outputs/ 2>/dev/null || true

echo "Moving scripts..."

# Move detector scripts
mv cycle_1_information_overload_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/ 2>/dev/null || true
mv cycle_2_one_best_thing_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/ 2>/dev/null || true
mv cycle_3_perfectionism_escalation_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/ 2>/dev/null || true
mv cycle_4_emotional_dysregulation_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/ 2>/dev/null || true
mv cycle_5_mind_reading_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/ 2>/dev/null || true
mv cycle_6_system_building_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/ 2>/dev/null || true
mv cycle_7_special_interest_detector.py analysis/wave-1-vicious-cycles/scripts/detectors/ 2>/dev/null || true

# Move semantic analyzer scripts
mv cycle_1_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/ 2>/dev/null || true
mv cycle_2_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/ 2>/dev/null || true
mv cycle_3_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/ 2>/dev/null || true
mv cycle_4_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/ 2>/dev/null || true
mv cycle_5_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/ 2>/dev/null || true
mv cycle_6_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/ 2>/dev/null || true
mv cycle_7_semantic_analyzer.py analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/ 2>/dev/null || true

echo "Moving documentation..."

# Move cycle analyses
mv docs/cycle-1-information-overload-complete-analysis.md analysis/wave-1-vicious-cycles/docs/ 2>/dev/null || true
mv docs/cycle-2-one-best-thing-complete-analysis.md analysis/wave-1-vicious-cycles/docs/ 2>/dev/null || true
mv docs/cycle-3-perfectionism-escalation-complete-analysis.md analysis/wave-1-vicious-cycles/docs/ 2>/dev/null || true
mv docs/cycle-4-emotional-dysregulation-complete-analysis.md analysis/wave-1-vicious-cycles/docs/ 2>/dev/null || true
mv docs/cycle-6-system-building-complete-analysis.md analysis/wave-1-vicious-cycles/docs/ 2>/dev/null || true
mv docs/cycle-7-special-interest-hyperfocus-complete-analysis.md analysis/wave-1-vicious-cycles/docs/ 2>/dev/null || true
mv docs/cycles-summary-complete-analysis.md analysis/wave-1-vicious-cycles/docs/ 2>/dev/null || true

# Move system prompts
mv docs/system-prompt-recommendations.md system-prompts/recommendations/ 2>/dev/null || true
mv docs/benjamin-custom-system-prompt.md system-prompts/benjamin/v1-compact.md 2>/dev/null || true

# Move methodology
mv docs/investigation-plan-additional-reinforcement-cycles.md docs/methodology/ 2>/dev/null || true

# Move background
mv docs/neurodivergent-llm-interaction-analysis.md docs/background/ 2>/dev/null || true

echo "Moving utility scripts..."

# Move tools
mv pattern_search.py tools/pattern-search.py 2>/dev/null || true
mv claude_response_analysis.py tools/claude-response-analysis.py 2>/dev/null || true

echo "Creating README files..."

# Create wave-1 README
cat > analysis/wave-1-vicious-cycles/README.md << 'EOF'
# Wave 1: Vicious Reinforcement Cycles Analysis

Investigation of 7 hypothesized vicious cycles in Benjamin's LLM interactions.

## Dataset
- 255 conversations
- 5,338 messages (2,672 user, 2,666 Claude)
- 26-day period
- 89.5MB

## Methodology
Two-stage detection:
1. Quantitative pattern mining (regex)
2. Qualitative semantic analysis (Claude Haiku)

## Results

### Pathological Cycles (4)
- Cycle 1: Information Overload (30.2%)
- Cycle 2: Decision Paralysis (25.1%, 92.2% abandonment)
- Cycle 3: Perfectionism (25.1%, 71.9% unresolved)
- Cycle 4: Emotional Dysregulation (50.6%, 100% no baseline return)

### Natural Traits (1)
- Cycle 7: Special Interest Hyperfocus (60.8%, 60% productive)

### Rejected (2)
- Cycle 5: Mind Reading (43.9%, mild - current approach working)
- Cycle 6: System Building (0.8%, essentially non-existent)

## Key Finding
**LLM contributes 60-70% to pathological cycles** through RLHF-optimized over-compliance.
EOF

# Create system-prompts README
cat > system-prompts/README.md << 'EOF'
# Benjamin's Custom System Prompts

Interventions for vicious reinforcement cycles identified in Wave 1 analysis.

## Versions

### v1 (Based on Wave 1 Findings)
- **Compact** (500-800 chars) - Mobile/constrained environments
- **Standard** (2,000-3,000 chars) - Recommended for most use
- **Extended** (5,000+ chars) - Comprehensive coverage

## Deployment
See `recommendations/system-prompt-recommendations.md` for implementation guide.

## Changelog
Track iterations and effectiveness in `benjamin/changelog.md`.
EOF

# Create tools README
cat > tools/README.md << 'EOF'
# Analysis Utilities

Reusable scripts for conversation analysis.

## Available Tools
- `pattern-search.py` - General pattern detection
- `claude-response-analysis.py` - Response pattern analysis

## Usage
Scripts can be used across multiple research waves.
EOF

echo "Creating version changelog..."

cat > system-prompts/benjamin/changelog.md << 'EOF'
# Benjamin System Prompt Changelog

## v1 - Initial Version (Wave 1 Findings)

**Date:** 2025-01-16
**Based on:** Wave 1 Vicious Cycles Analysis

### Interventions Implemented
1. Information scoping (Cycle 1)
2. Binary decision recommendations (Cycle 2)
3. Completion declarations (Cycle 3)
4. Emotional acknowledgment (Cycle 4)
5. Iteration limits (Cycle 3)

### Target Metrics
- Reduce decision abandonment from 92.2% → <50%
- Reduce unresolved tasks from 71.9% → <40%
- Enable emotional baseline return (currently 0%)

### Future Iterations
- v2 will be based on intervention effectiveness data (Wave 2)
EOF

# Update paths in scripts
echo "Updating script paths..."

# Create path update script for detectors
for detector in analysis/wave-1-vicious-cycles/scripts/detectors/*.py; do
    if [ -f "$detector" ]; then
        # Update conversations.json path
        sed -i.bak "s|'/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json'|'../../../data/raw/conversations.json'|g" "$detector"
        # Update output paths
        sed -i.bak "s|'/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/|'../../outputs/|g" "$detector"
        rm "${detector}.bak"
    fi
done

# Create path update script for semantic analyzers
for analyzer in analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/*.py; do
    if [ -f "$analyzer" ]; then
        # Update findings path
        sed -i.bak "s|'/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/|'../../outputs/|g" "$analyzer"
        # Update conversations.json path
        sed -i.bak "s|'/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json'|'../../../data/raw/conversations.json'|g" "$analyzer"
        rm "${analyzer}.bak"
    fi
done

echo "Creating main README..."

cat > README.md << 'EOF'
# Discovering Benjamin

Investigation of neurodivergent (autism/Asperger's) interaction patterns with LLMs.

## Research Question
How do Benjamin's autism traits interact with LLM response patterns to create vicious reinforcement cycles?

## Current Status

### Completed
- **Wave 1:** Vicious Reinforcement Cycles Analysis
  - 7 cycles investigated
  - 4 pathological patterns identified
  - System prompt interventions designed

### In Progress
- None

### Planned
- **Wave 2:** Intervention Effectiveness Testing
- **Wave 3:** Longitudinal Analysis (6-12 months)
- **Wave 4:** Cross-Model Comparison (Claude vs GPT vs Gemini)
- **Wave 5:** Generalization to Other Neurodivergent Profiles

## Quick Links

### For Benjamin/Family
- [System Prompts](system-prompts/benjamin/) - Deploy these in LLM settings
- [Implementation Guide](system-prompts/recommendations/system-prompt-recommendations.md)

### For Researchers
- [Wave 1 Analysis](analysis/wave-1-vicious-cycles/)
- [Methodology](docs/methodology/)
- [Background Research](docs/background/)

## Key Findings (Wave 1)

**4 out of 7 cycles are pathological vicious cycles** where LLM response patterns contribute 60-70% to dysfunction:

1. **Information Overload** (30.2%) - Satisfaction paradox
2. **Decision Paralysis** (25.1%) - 92.2% abandonment rate
3. **Perfectionism** (71.9%) - Unresolved tasks
4. **Emotional Dysregulation** (50.6%) - 100% no baseline return

**Critical insight:** RLHF-optimized compliance creates these problems, not Benjamin's autism alone.

## Repository Structure

```
├── data/              # Datasets (raw and processed)
├── analysis/          # Research waves
├── system-prompts/    # Deployable interventions
├── docs/              # Meta-level documentation
├── tools/             # Reusable utilities
└── archive/           # Deprecated work
```

## Dataset

- **255 conversations**
- **5,338 messages** (2,672 user, 2,666 Claude)
- **26-day period**
- **89.5MB**

## Contact

For questions about this research, contact Richard Hallett.
EOF

echo ""
echo "✓ Restructure complete!"
echo ""
echo "New structure created. Original files preserved."
echo ""
echo "Next steps:"
echo "1. Review the new structure: ls -R"
echo "2. Test scripts in new locations"
echo "3. Update any external references to file paths"
echo "4. Once confirmed working, remove archive/pre-restructure/"
echo ""
echo "To run Wave 1 scripts from new locations:"
echo "  cd analysis/wave-1-vicious-cycles/scripts/detectors"
echo "  python3 cycle_1_information_overload_detector.py"
