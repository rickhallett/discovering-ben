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
