# Analysis Pipeline - Implementation Summary

This document summarizes the programmatic analysis framework created to make your Claude usage analysis repeatable.

## What Was Created

### Framework Architecture (Macro, Meso, Micro Levels)

```
analysis_pipeline/
├── README.md                          # Architecture overview
├── QUICKSTART.md                      # Getting started guide
├── MIGRATION_GUIDE.md                 # Converting existing scripts
├── orchestrator.py                    # Main pipeline coordinator
│
├── config/
│   ├── pipeline_config.yaml          # Wave and analyzer definitions
│   └── prompts/
│       ├── semantic_pattern_detection.txt
│       ├── cross_analysis_synthesis.txt
│       └── final_report_generation.txt
│
├── analyzers/
│   └── base_analyzer.py              # Base classes for all analyzers
│
└── utils/
    └── claude_interface.py           # Unified Claude API/CLI interface
```

## The Three Levels of Analysis

### Macro Level: Analysis Waves

Defined in `config/pipeline_config.yaml`:

```yaml
waves:
  - name: "exploratory"        # Wave 1: Quantitative foundation
    parallel: true
    analyzers: [temporal, content, projects]

  - name: "deep_dive"          # Wave 2: Claude API pattern detection
    parallel: true
    requires: ["exploratory"]
    analyzers: [overload_detector, semantic_analyzer]

  - name: "synthesis"          # Wave 3: Claude CLI comprehensive report
    parallel: false
    requires: ["exploratory", "deep_dive"]
    analyzers: [cross_synthesis, final_report]
```

### Meso Level: Individual Analyzers

Each analyzer is configured with:
- Type (quantitative, claude_api, claude_cli)
- Script or model to use
- Prompt template (for Claude-based analyzers)
- Parameters and batch sizes

### Micro Level: Claude Interactions

Two methods provided:

**1. Anthropic Python SDK** (`ClaudeAPIInterface`)
- For batch processing
- Parallel API calls
- Cost-optimized with Haiku for simple tasks

**2. Claude CLI** (`ClaudeCLIInterface`)
- For synthesis tasks needing project context
- Interactive-style prompts
- Leverages Claude CLI conversation management

## How to Use

### First Time Setup

```bash
# Install dependencies
pip install pyyaml anthropic

# Set API key
export ANTHROPIC_API_KEY="your-key"

# Make orchestrator executable
chmod +x analysis_pipeline/orchestrator.py
```

### Running on New Data Export

When you get a new Claude data export (e.g., December 2025):

```bash
cd analysis_pipeline

# Run complete pipeline
python3 orchestrator.py \
  --config config/pipeline_config.yaml \
  --data-dir /path/to/new/export \
  --output-dir ./results_2025_12_01

# This will:
# 1. Run Wave 1 (quantitative analysis) - $0 cost
# 2. Run Wave 2 (Claude API analysis) - ~$2-5 cost
# 3. Run Wave 3 (synthesis report) - ~$0.50 cost
# Total: ~$2.50-5.50 per complete analysis
```

### Incremental Development

```bash
# Test with just Wave 1 (free, fast)
python3 orchestrator.py --wave 1 --data-dir ../test_data

# Add Wave 2 (Claude API)
python3 orchestrator.py --wave 2 --data-dir ../test_data

# Final synthesis
python3 orchestrator.py --wave 3 --data-dir ../test_data

# See execution plan without running
python3 orchestrator.py --dry-run
```

### Customizing for Your Needs

**Adjust batch sizes** (in `config/pipeline_config.yaml`):
```yaml
analyzers:
  semantic_pattern_analyzer:
    batch_size: 10  # Analyze only first 10 conversations
```

**Change Claude models**:
```yaml
analyzers:
  semantic_pattern_analyzer:
    model: claude-haiku-4-20250514  # Fast and cheap

  final_report_generator:
    model: claude-sonnet-4-5-20250929  # Powerful for synthesis
```

**Edit prompts** (in `config/prompts/`):
- Modify existing prompt templates
- Add new analysis dimensions
- Customize output formats

## Migrating Existing Analyzers

Your existing scripts can be migrated into the framework:

### Before (cycle_1_information_overload_detector.py)
```python
# Standalone script
# Loads data directly
# Prints to stdout
# No standard format
```

### After (analyzers/information_overload_analyzer.py)
```python
class InformationOverloadAnalyzer(QuantitativeAnalyzer):
    @property
    def metadata(self):
        return AnalyzerMetadata(
            analyzer_name="information_overload_detector",
            analyzer_type="quantitative",
            version="2.0.0",
            description="Detects overload patterns"
        )

    def analyze(self, conversations):
        # Your analysis logic
        return results  # Standardized format
```

See `MIGRATION_GUIDE.md` for complete examples.

## Key Benefits

### 1. Repeatability
Run the exact same analysis on new data exports:
```bash
python3 orchestrator.py --data-dir /path/to/new/export
```

### 2. Parallelization
Wave 1 analyzers run in parallel (4 workers by default):
- Temporal analysis
- Content analysis
- Project analysis

All complete ~4x faster than sequential execution.

### 3. Caching
Results are cached automatically:
```bash
# First run: All analyzers execute
python3 orchestrator.py

# Second run: Cached results used
python3 orchestrator.py

# Force re-run specific analyzer
python3 orchestrator.py --rerun semantic_pattern_analyzer
```

### 4. Cost Control
Control Claude API costs:
```yaml
analyzers:
  semantic_pattern_analyzer:
    batch_size: 5  # Test with 5 conversations
    model: claude-haiku-4-20250514  # Use cheaper model
```

### 5. Composition
Mix quantitative and Claude-based analyses:
- Wave 1: Fast regex/stats (free)
- Wave 2: Claude API for nuanced patterns ($)
- Wave 3: Claude CLI for synthesis ($$)

### 6. Versioning
Configuration files in git track analysis evolution:
```bash
git log config/pipeline_config.yaml
# See how analysis approach changed over time
```

## Example: Repeating Your Work

Your current analysis involved:

1. **Exploratory phase** - temporal, content, project analysis
2. **Deep dive phase** - information overload detection, semantic analysis
3. **Synthesis phase** - cross-analysis, final reports

This is now captured in `config/pipeline_config.yaml` and can be run as:

```bash
python3 orchestrator.py --data-dir /path/to/export
```

Same prompts, same thresholds, same analysis - completely reproducible.

## Future Data Exports

When Benjamin's next export is available (e.g., January 2026):

```bash
# 1. Place new export in directory
mkdir ../benjamin_export_2026_01

# 2. Run identical analysis
python3 orchestrator.py \
  --data-dir ../benjamin_export_2026_01 \
  --output-dir ./results_2026_01

# 3. Compare results
# Temporal patterns changed?
diff results_2025_11/exploratory_temporal_analysis.json \
     results_2026_01/exploratory_temporal_analysis.json

# Overload patterns improved?
diff results_2025_11/deep_dive_information_overload_detector.json \
     results_2026_01/deep_dive_information_overload_detector.json
```

Track Benjamin's usage evolution over time with identical analysis methodology.

## Extending the Framework

### Adding New Analyzers

1. Create analyzer class in `analyzers/`
2. Add to `config/pipeline_config.yaml`
3. Create prompt template if using Claude
4. Test standalone, then in pipeline

### Adding New Waves

1. Define new wave in config
2. Specify dependencies
3. Add analyzers to wave
4. Set parallel vs. sequential execution

### Adding New Prompts

1. Create `.txt` file in `config/prompts/`
2. Use `{variable}` placeholders
3. Reference in analyzer config
4. Test with small data sample

## Cost and Performance

### Typical Full Pipeline Run

| Wave | Analyzers | Model | Time | Cost |
|------|-----------|-------|------|------|
| 1 (Exploratory) | 3 | Python | 30s | $0.00 |
| 2 (Deep Dive) | 2 | Haiku | 2-5min | $2-5 |
| 3 (Synthesis) | 2 | Sonnet | 1-2min | $0.50 |
| **Total** | **7** | **Mixed** | **3-8min** | **$2.50-5.50** |

### Optimization Tips

- Use `batch_size` to limit Claude API calls during development
- Run Wave 1 first to validate data (free)
- Use Haiku for pattern detection (10x cheaper than Sonnet)
- Use Sonnet only for final synthesis
- Cache results to avoid re-running expensive analyses

## Documentation

- `analysis_pipeline/README.md` - Architecture and concepts
- `analysis_pipeline/QUICKSTART.md` - Step-by-step guide
- `analysis_pipeline/MIGRATION_GUIDE.md` - Converting existing scripts
- `CLAUDE.md` - Updated with pipeline section

## Next Steps

1. **Test the framework**:
   ```bash
   cd analysis_pipeline
   python3 orchestrator.py --dry-run  # See execution plan
   python3 orchestrator.py --wave 1   # Test Wave 1 only
   ```

2. **Migrate an existing analyzer**:
   - Pick one (e.g., `cycle_1_information_overload_detector.py`)
   - Follow `MIGRATION_GUIDE.md`
   - Test standalone and in pipeline

3. **Customize prompts**:
   - Edit `config/prompts/*.txt`
   - Add research-specific questions
   - Refine analysis dimensions

4. **Run on new data**:
   - Get next Benjamin export
   - Run identical pipeline
   - Compare results over time

## Questions?

The framework is designed to answer your original question:

> "How can we create a programmatic way of repeating analyses on new data exports, expressing the macro, meso, and micro cycles of Claude calls?"

- **Macro**: Waves in `pipeline_config.yaml`
- **Meso**: Analyzers in `analyzers/` and config
- **Micro**: Claude API/CLI calls in `utils/claude_interface.py`

All working together in `orchestrator.py` to make your analysis work repeatable.
