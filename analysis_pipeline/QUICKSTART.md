# Quick Start: Running Analysis Pipeline

## Prerequisites

```bash
# Install dependencies
pip install pyyaml anthropic

# Set API key
export ANTHROPIC_API_KEY="your-api-key-here"

# Install Claude CLI (optional, for synthesis wave)
# See: https://github.com/anthropics/anthropic-claude-cli
```

## Running Your First Analysis

### 1. Prepare Data

Place your Claude data export in a directory:

```bash
data_export/
├── conversations.json
├── memories.json
├── projects.json
└── users.json
```

### 2. Run Complete Pipeline

```bash
cd analysis_pipeline

python3 orchestrator.py \
  --config config/pipeline_config.yaml \
  --data-dir ../path/to/data_export \
  --output-dir ./results_2025_12_01
```

This will:
1. Run Wave 1 (exploratory) - temporal, content, project analysis
2. Run Wave 2 (deep_dive) - pattern detection with Claude
3. Run Wave 3 (synthesis) - generate comprehensive report

### 3. Check Results

```bash
results_2025_12_01/
├── logs/
│   └── pipeline_20251201_143022.log
├── results/
│   ├── exploratory_temporal_analysis.json
│   ├── exploratory_content_analysis.json
│   ├── exploratory_project_analysis.json
│   ├── deep_dive_information_overload_detector.json
│   ├── deep_dive_semantic_pattern_analyzer.json
│   └── synthesis_final_report_generator.json
└── execution_summary_20251201_143045.json
```

## Running Specific Waves

### Wave 1 Only (Quantitative Foundation)

```bash
python3 orchestrator.py --wave 1 --data-dir ../data_export
```

Fast, no API costs. Run this first to validate data loading.

### Wave 2 Only (Pattern Detection)

```bash
python3 orchestrator.py --wave 2 --data-dir ../data_export
```

Requires Wave 1 results. Uses Claude API (costs ~$0.50-2.00 depending on data size).

### Wave 3 Only (Synthesis)

```bash
python3 orchestrator.py --wave 3 --data-dir ../data_export
```

Requires Wave 1 and 2 results. Generates final comprehensive report.

## Incremental Development Workflow

### 1. Start with Quantitative Analysis

Edit `config/pipeline_config.yaml` to disable expensive analyzers:

```yaml
waves:
  - name: "exploratory"
    analyzers:
      - temporal_analysis
      # Comment out others initially
      # - content_analysis
      # - project_analysis
```

Run:
```bash
python3 orchestrator.py --wave 1
```

### 2. Add One Claude Analyzer at a Time

```yaml
waves:
  - name: "deep_dive"
    analyzers:
      - information_overload_detector  # Start with this
      # - semantic_pattern_analyzer    # Add later
```

Run:
```bash
python3 orchestrator.py --wave 2
```

### 3. Use Cache for Fast Iteration

The pipeline caches results automatically:

```bash
# First run (slow)
python3 orchestrator.py

# Modify one analyzer and re-run (fast - uses cached results for others)
python3 orchestrator.py

# Force re-run specific analyzer
python3 orchestrator.py --rerun semantic_pattern_analyzer

# Disable cache entirely
python3 orchestrator.py --no-cache
```

## Testing with Sample Data

Create a small test dataset:

```python
# create_test_data.py
import json

# Load full dataset
with open('conversations.json') as f:
    all_convs = json.load(f)

# Take first 10 conversations
test_convs = all_convs[:10]

# Save test set
with open('conversations_test.json', 'w') as f:
    json.dump(test_convs, f)
```

Run pipeline on test data:

```bash
python3 orchestrator.py \
  --data-dir ./test_data \
  --output-dir ./test_results
```

## Customizing Analysis

### Adjust Batch Sizes

In `config/pipeline_config.yaml`:

```yaml
analyzers:
  semantic_pattern_analyzer:
    batch_size: 5  # Analyze only first 5 conversations (for testing)
```

### Change Models

```yaml
analyzers:
  semantic_pattern_analyzer:
    model: claude-haiku-4-20250514  # Fast and cheap

  final_report_generator:
    model: claude-sonnet-4-5-20250929  # Powerful for synthesis
```

### Add Custom Parameters

```yaml
analyzers:
  my_analyzer:
    params:
      threshold: 10
      include_metadata: true
      custom_setting: "value"
```

Access in analyzer:

```python
def analyze(self, data):
    threshold = self.config.parameters.get('threshold', 5)
    # ...
```

## Monitoring Progress

### View Logs in Real-Time

```bash
tail -f results/logs/pipeline_*.log
```

### Check Execution Summary

```bash
cat results/execution_summary_*.json | jq '.pipeline_execution'
```

### Dry Run (See What Will Execute)

```bash
python3 orchestrator.py --dry-run

# Output:
# Dry run - execution plan:
#
# Wave 1: exploratory (parallel=True)
#   - temporal_analysis (quantitative)
#   - content_analysis (quantitative)
#   - project_analysis (quantitative)
#
# Wave 2: deep_dive (parallel=True)
#   - information_overload_detector (quantitative)
#   - semantic_pattern_analyzer (claude_api)
```

## Repeating Analysis on New Data

When you get a new data export:

```bash
# 1. Export data from Claude account
# 2. Place in new directory
mkdir data_export_2025_12_15

# 3. Run exact same pipeline
python3 orchestrator.py \
  --config config/pipeline_config.yaml \
  --data-dir ../data_export_2025_12_15 \
  --output-dir ./results_2025_12_15

# 4. Compare results
diff results_2025_12_01/execution_summary_*.json \
     results_2025_12_15/execution_summary_*.json
```

The same analyzers, same prompts, same thresholds - completely repeatable.

## Troubleshooting

### API Key Not Found

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
python3 orchestrator.py
```

### Analyzer Failed

Check error details:

```bash
cat results/errors/wave_analyzer_error.txt
```

Check logs:

```bash
grep ERROR results/logs/pipeline_*.log
```

### Wave Dependencies Not Met

If you see: "Wave 'deep_dive' requires 'exploratory' which hasn't completed"

Run prerequisite wave first:

```bash
python3 orchestrator.py --wave 1  # Run exploratory first
python3 orchestrator.py --wave 2  # Then deep_dive
```

### Out of Memory

Reduce batch sizes in `config/pipeline_config.yaml`:

```yaml
analyzers:
  semantic_pattern_analyzer:
    batch_size: 10  # Reduce from 20
```

Or reduce parallel workers:

```yaml
pipeline:
  parallel_workers: 2  # Reduce from 4
```

## Cost Estimation

Approximate API costs per full pipeline run:

| Component | Model | Conversations | Cost |
|-----------|-------|---------------|------|
| Wave 1 | N/A (quantitative) | All | $0.00 |
| Semantic Analyzer | Haiku | 20 | ~$0.40 |
| Interaction Detector | Haiku | 30 | ~$0.60 |
| Synthesis | Sonnet | 1 | ~$0.20 |
| **Total** | | | **~$1.20** |

Scale with your data:
- 265 conversations (full analysis): ~$6-8
- 1000 conversations: ~$25-30

Use `batch_size` parameter to control costs during development.

## Next Steps

1. Review generated reports in `results/synthesis_final_report_generator.json`
2. Customize prompts in `config/prompts/` for your specific questions
3. Add custom analyzers following `MIGRATION_GUIDE.md`
4. Set up automated runs with cron/scheduled tasks
5. Version control your configuration to track analysis evolution
