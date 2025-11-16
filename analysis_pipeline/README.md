# Analysis Pipeline Framework

A programmatic framework for repeatable LLM interaction analysis across multiple data exports.

## Architecture: Macro, Meso, Micro Cycles

### Macro Level: Analysis Phases (Waves)

The overall workflow consists of sequential waves of analysis:

```
Wave 1 (Parallel): Quantitative Foundation
├─ Temporal Analysis
├─ Content Analysis
└─ Project Analysis

Wave 2 (Parallel): Qualitative Deep Dives
├─ Information Overload Detection
├─ Semantic Pattern Analysis
└─ Interaction Cycle Detection

Wave 3 (Sequential): Synthesis
├─ Cross-Analysis Pattern Detection
├─ Insight Aggregation
└─ Report Generation
```

### Meso Level: Individual Analyzers

Each analyzer is a self-contained module that:
- Loads specific data
- Performs analysis (quantitative, Claude API-based, or hybrid)
- Outputs structured results
- Can run independently or as part of a wave

### Micro Level: Claude Interactions

Individual prompts and API calls:
- Direct regex/Python analysis (no Claude needed)
- Claude CLI calls: `claude -p "<prompt>"`
- Anthropic SDK calls: `client.messages.create()`
- Batched vs. streaming calls

## Pipeline Structure

```
analysis_pipeline/
├── README.md                    # This file
├── orchestrator.py              # Main pipeline runner
├── config/
│   ├── pipeline_config.yaml     # Wave definitions and sequencing
│   ├── analyzer_config.yaml     # Analyzer parameters
│   └── prompts/
│       ├── temporal_analysis_synthesis.txt
│       ├── semantic_pattern_detection.txt
│       └── final_report_generation.txt
├── analyzers/
│   ├── base_analyzer.py         # Abstract base class
│   ├── quantitative_analyzer.py # Regex/stats analysis
│   ├── claude_analyzer.py       # Claude API/CLI wrapper
│   └── synthesis_analyzer.py    # Cross-analysis synthesis
├── waves/
│   ├── wave_1_exploratory.py
│   ├── wave_2_deep_dive.py
│   └── wave_3_synthesis.py
└── utils/
    ├── data_loader.py
    ├── parallel_executor.py
    ├── result_store.py
    └── claude_interface.py      # Unified Claude CLI/SDK interface
```

## Usage

### Basic Run (All Waves)

```bash
python3 analysis_pipeline/orchestrator.py \
  --data-dir /path/to/export \
  --output-dir ./results \
  --config config/pipeline_config.yaml
```

### Run Specific Wave

```bash
python3 analysis_pipeline/orchestrator.py \
  --wave 1 \
  --data-dir /path/to/export
```

### Run Single Analyzer

```bash
python3 analysis_pipeline/analyzers/quantitative_analyzer.py \
  --type temporal \
  --input conversations.json \
  --output results/temporal.json
```

### Dry Run (Show Execution Plan)

```bash
python3 analysis_pipeline/orchestrator.py \
  --dry-run \
  --config config/pipeline_config.yaml
```

## Configuration Example

```yaml
# pipeline_config.yaml
pipeline:
  data_dir: "/path/to/export"
  output_dir: "./results"
  use_cache: true
  parallel_workers: 4

waves:
  - name: "exploratory"
    parallel: true
    analyzers:
      - temporal_analysis
      - content_analysis
      - project_analysis

  - name: "deep_dive"
    parallel: true
    requires: ["exploratory"]
    analyzers:
      - information_overload_detector
      - semantic_pattern_analyzer

  - name: "synthesis"
    parallel: false
    requires: ["exploratory", "deep_dive"]
    analyzers:
      - cross_analysis_synthesizer
      - report_generator

analyzers:
  temporal_analysis:
    type: quantitative
    script: analyzers/quantitative_analyzer.py
    params:
      analysis_type: temporal

  semantic_pattern_analyzer:
    type: claude_api
    model: claude-haiku-4-20250514
    prompt_template: config/prompts/semantic_pattern_detection.txt
    batch_size: 20

  report_generator:
    type: claude_cli
    prompt_template: config/prompts/final_report_generation.txt
    model: claude-sonnet-4-5-20250929
```

## Claude Integration Methods

### Method 1: Anthropic Python SDK (Recommended)

For programmatic control with batching and error handling:

```python
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-haiku-4-20250514",
    max_tokens=4096,
    messages=[{"role": "user", "content": prompt}]
)
```

### Method 2: Claude CLI

For interactive-style prompts and project context:

```bash
claude -p "Analyze this conversation for overwhelm patterns: ..."
```

```python
import subprocess

result = subprocess.run(
    ["claude", "-p", prompt],
    capture_output=True,
    text=True
)
```

### Method 3: Hybrid (Best of Both)

- Use SDK for batch analysis (parallel processing)
- Use CLI for complex synthesis needing project context
- Use quantitative methods when Claude isn't needed

## Result Storage

All results follow a standard format:

```json
{
  "analyzer": "semantic_pattern_analyzer",
  "wave": "deep_dive",
  "timestamp": "2025-11-16T14:30:00Z",
  "input_files": ["conversations.json"],
  "config": {...},
  "results": {...},
  "metadata": {
    "execution_time_seconds": 45.2,
    "conversations_analyzed": 265,
    "model_used": "claude-haiku-4-20250514"
  }
}
```

## Extending the Framework

### Adding a New Analyzer

1. Inherit from `BaseAnalyzer`
2. Implement `analyze()` method
3. Add to `config/analyzer_config.yaml`
4. Add to appropriate wave in `pipeline_config.yaml`

Example:

```python
from analyzers.base_analyzer import BaseAnalyzer

class MyCustomAnalyzer(BaseAnalyzer):
    def analyze(self, data):
        # Your analysis logic
        return results
```

### Adding a New Wave

1. Create `waves/wave_N_name.py`
2. Define analyzer sequence
3. Add to `pipeline_config.yaml`

## Caching and Incremental Runs

The orchestrator supports caching to avoid re-running expensive analyses:

```bash
# Run with cache (default)
python3 orchestrator.py --use-cache

# Force re-run all analyses
python3 orchestrator.py --no-cache

# Re-run only specific analyzer
python3 orchestrator.py --rerun semantic_pattern_analyzer
```

## Monitoring and Logging

All pipeline runs generate:
- Execution logs: `results/logs/pipeline_TIMESTAMP.log`
- Timing data: `results/timing_report.json`
- Error reports: `results/errors/` (if any)

## Best Practices

1. **Start with quantitative**: Run cheap regex/stats analyses first
2. **Batch Claude calls**: Group similar prompts to minimize API calls
3. **Use appropriate models**: Haiku for simple tasks, Sonnet for complex reasoning
4. **Cache results**: Avoid re-running expensive analyses
5. **Test on subsets**: Validate analyzers on small data samples first
6. **Version configs**: Keep `pipeline_config.yaml` in git to track analysis evolution
