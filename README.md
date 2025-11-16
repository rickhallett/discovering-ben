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

## Analysis Pipeline Framework

### Repeatable Analysis System

The `analysis_pipeline/` directory contains a programmatic framework for repeating analyses on new data exports. This captures the macro, meso, and micro cycles of LLM-assisted analysis:

- **Macro Level**: Analysis waves (exploratory → deep dive → synthesis)
- **Meso Level**: Individual analyzers (temporal, semantic, synthesis)
- **Micro Level**: Claude API/CLI calls with specific prompts

### Quick Start

```bash
cd analysis_pipeline

# Run complete pipeline on new data export
python3 orchestrator.py \
  --config config/pipeline_config.yaml \
  --data-dir /path/to/new/export \
  --output-dir ./results_YYYY_MM_DD

# Run specific wave
python3 orchestrator.py --wave 1  # Exploratory (quantitative, $0)
python3 orchestrator.py --wave 2  # Deep dive (Claude API, ~$2-5)
python3 orchestrator.py --wave 3  # Synthesis (Claude CLI, ~$0.50)

# View execution plan
python3 orchestrator.py --dry-run
```

### Features

- **Automatic parallelization** - Concurrent execution within waves
- **Result caching** - Skip re-running expensive analyses
- **Cost control** - Configurable batch sizes and model selection
- **Standardized output** - Consistent JSON format across analyzers
- **Migrable scripts** - Convert existing analysis scripts to framework

### Documentation

- `analysis_pipeline/README.md` - Architecture and concepts
- `analysis_pipeline/QUICKSTART.md` - Getting started guide
- `analysis_pipeline/MIGRATION_GUIDE.md` - Converting existing scripts
- `PIPELINE_SUMMARY.md` - Complete implementation overview

### Cost & Performance

Typical full pipeline run:
- **Time**: 3-8 minutes
- **Cost**: $2.50-5.50 (265 conversations)
- **Waves**: 3 (exploratory, deep dive, synthesis)
- **Analyzers**: 7 (quantitative + Claude API + Claude CLI)

## Repository Structure

```
├── analysis_pipeline/  # Programmatic analysis framework (new!)
│   ├── orchestrator.py        # Main pipeline coordinator
│   ├── analyzers/             # Analyzer implementations
│   ├── config/                # Wave and analyzer definitions
│   ├── utils/                 # Claude API/CLI interfaces
│   └── *.md                   # Documentation (README, QUICKSTART, MIGRATION_GUIDE)
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
