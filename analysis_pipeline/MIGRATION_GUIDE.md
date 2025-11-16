# Migration Guide: Converting Existing Analyzers

This guide shows how to migrate existing analysis scripts into the pipeline framework.

## Example: Information Overload Detector

### Original Script (cycle_1_information_overload_detector.py)

The original script was a standalone Python file that:
1. Loaded conversations.json directly
2. Ran regex pattern matching
3. Printed results to stdout
4. Had no standard output format

### Migrated Version

Create `analysis_pipeline/analyzers/information_overload_analyzer.py`:

```python
#!/usr/bin/env python3
"""
Information Overload Analyzer
Migrated from cycle_1_information_overload_detector.py
"""

import re
from collections import defaultdict
from analyzers.base_analyzer import QuantitativeAnalyzer, AnalyzerMetadata, AnalysisConfig


class InformationOverloadAnalyzer(QuantitativeAnalyzer):
    """
    Detects information overload cycles in conversations.

    Hypothesis: User's uncertainty intolerance + LLM's detail provision creates
    a cycle where user demands "everything", gets overwhelmed, feels unsatisfied,
    demands more, leading to cognitive overload.
    """

    @property
    def metadata(self) -> AnalyzerMetadata:
        return AnalyzerMetadata(
            analyzer_name="information_overload_detector",
            analyzer_type="quantitative",
            version="2.0.0",
            description="Detects information overload patterns using regex and statistics"
        )

    def __init__(self, config: AnalysisConfig):
        super().__init__(config)

        # Pattern definitions (from original script)
        self.exhaustive_demand_patterns = [
            r'\btell me everything\b',
            r'\bevery single\b',
            r'\ball of (it|them|the)\b',
            r'\bexhaustive\b',
            r'\bcomprehensive\b',
            r'\bcomplete list\b',
            # ... rest of patterns
        ]

        self.clarity_complaint_patterns = [
            r'\bnot clear\b',
            r'\bconfusing\b',
            # ... rest of patterns
        ]

        # Compile patterns
        self.exhaustive_regex = re.compile(
            '|'.join(self.exhaustive_demand_patterns),
            re.IGNORECASE
        )

        self.clarity_regex = re.compile(
            '|'.join(self.clarity_complaint_patterns),
            re.IGNORECASE
        )

    def analyze(self, conversations: list) -> dict:
        """Run information overload detection"""
        self.logger.info(f"Analyzing {len(conversations)} conversations for overload patterns")

        results = {
            "summary": {},
            "conversation_level": [],
            "high_risk_conversations": []
        }

        total_exhaustive = 0
        total_clarity_complaints = 0
        high_risk_conversations = []

        for conv in conversations:
            conv_analysis = self._analyze_conversation(conv)

            results["conversation_level"].append(conv_analysis)

            total_exhaustive += conv_analysis["exhaustive_demands"]
            total_clarity_complaints += conv_analysis["clarity_complaints"]

            # High risk: exhaustive demands + clarity complaints + long responses
            if (conv_analysis["exhaustive_demands"] > 0 or
                conv_analysis["clarity_complaints"] > 0) and \
               conv_analysis["avg_claude_response_length"] > 1500:
                high_risk_conversations.append(conv_analysis)

        # Summary statistics
        results["summary"] = {
            "total_conversations": len(conversations),
            "conversations_with_exhaustive_demands": sum(
                1 for c in results["conversation_level"] if c["exhaustive_demands"] > 0
            ),
            "conversations_with_clarity_complaints": sum(
                1 for c in results["conversation_level"] if c["clarity_complaints"] > 0
            ),
            "total_exhaustive_demands": total_exhaustive,
            "total_clarity_complaints": total_clarity_complaints,
            "high_risk_conversations_count": len(high_risk_conversations),
            "high_risk_percentage": (len(high_risk_conversations) / len(conversations) * 100) if conversations else 0
        }

        results["high_risk_conversations"] = high_risk_conversations

        return results

    def _analyze_conversation(self, conv: dict) -> dict:
        """Analyze single conversation for overload patterns"""
        messages = conv.get('chat_messages', [])

        user_messages = [m for m in messages if m.get('sender') == 'human']
        claude_messages = [m for m in messages if m.get('sender') == 'assistant']

        # Count pattern occurrences
        exhaustive_demands = 0
        clarity_complaints = 0

        for msg in user_messages:
            text = msg.get('text', '')
            exhaustive_demands += len(self.exhaustive_regex.findall(text))
            clarity_complaints += len(self.clarity_regex.findall(text))

        # Calculate Claude response metrics
        claude_lengths = [len(m.get('text', '')) for m in claude_messages]
        avg_length = sum(claude_lengths) / len(claude_lengths) if claude_lengths else 0

        return {
            "conversation": conv.get('name', 'Untitled'),
            "uuid": conv.get('uuid'),
            "exhaustive_demands": exhaustive_demands,
            "clarity_complaints": clarity_complaints,
            "avg_claude_response_length": avg_length,
            "total_messages": len(messages),
            "user_messages": len(user_messages),
            "claude_messages": len(claude_messages)
        }


# Command-line interface for standalone execution
if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to conversations.json")
    parser.add_argument("--output", required=True, help="Path to output JSON")
    args = parser.parse_args()

    config = AnalysisConfig(
        input_files=[args.input],
        output_file=args.output,
        parameters={}
    )

    analyzer = InformationOverloadAnalyzer(config)
    result = analyzer.run()

    print(f"Analysis complete. Results saved to {args.output}")
```

## Migration Checklist

When migrating an existing analyzer:

- [ ] Inherit from appropriate base class:
  - `QuantitativeAnalyzer` for regex/stats
  - `ClaudeAPIAnalyzer` for API-based analysis
  - `SynthesisAnalyzer` for multi-result synthesis

- [ ] Implement required methods:
  - [ ] `metadata` property
  - [ ] `analyze(data)` method

- [ ] Move pattern definitions to `__init__`

- [ ] Update `analyze()` to return dict (not print)

- [ ] Add command-line interface for standalone execution

- [ ] Add to `config/pipeline_config.yaml`

- [ ] Create prompt template if using Claude API

- [ ] Test standalone execution:
  ```bash
  python3 analyzers/my_analyzer.py --input data.json --output results.json
  ```

- [ ] Test pipeline execution:
  ```bash
  python3 orchestrator.py --wave 2
  ```

## Converting Claude API Calls

### Original Pattern

```python
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

for conv in conversations:
    response = client.messages.create(
        model="claude-haiku-4-20250514",
        messages=[{"role": "user", "content": prompt}]
    )
```

### Migrated Pattern

```python
from analyzers.base_analyzer import ClaudeAPIAnalyzer, AnalyzerMetadata, AnalysisConfig
from utils.claude_interface import ClaudeAPIInterface


class MySemanticAnalyzer(ClaudeAPIAnalyzer):

    @property
    def metadata(self) -> AnalyzerMetadata:
        return AnalyzerMetadata(
            analyzer_name="semantic_analyzer",
            analyzer_type="claude_api",
            version="1.0.0",
            description="Semantic analysis using Claude API"
        )

    def analyze(self, conversations: list) -> dict:
        # Load prompt template
        prompt_template_path = self.config.parameters.get('prompt_template')
        with open(prompt_template_path) as f:
            prompt_template = f.read()

        # Use Claude interface
        claude = ClaudeAPIInterface(model=self.model)

        results = claude.batch_analyze(
            conversations=conversations,
            prompt_template=prompt_template,
            batch_size=self.config.parameters.get('batch_size', 20)
        )

        return results
```

## Adding to Pipeline

After migrating, add to `config/pipeline_config.yaml`:

```yaml
analyzers:
  my_new_analyzer:
    type: quantitative  # or claude_api, claude_cli
    script: analyzers/my_analyzer.py
    params:
      # analyzer-specific parameters
      threshold: 5
      include_metadata: true
```

Add to appropriate wave:

```yaml
waves:
  - name: "deep_dive"
    analyzers:
      - my_new_analyzer
```

## Testing Migration

```bash
# Test standalone
python3 analysis_pipeline/analyzers/my_analyzer.py \
  --input conversations.json \
  --output test_results.json

# Test in pipeline (dry run)
python3 analysis_pipeline/orchestrator.py --dry-run

# Run specific wave
python3 analysis_pipeline/orchestrator.py --wave 2

# Run full pipeline
python3 analysis_pipeline/orchestrator.py
```

## Benefits of Migration

1. **Standardization**: All analyzers follow same interface
2. **Orchestration**: Automatic parallel execution and dependency management
3. **Caching**: Avoid re-running expensive analyses
4. **Logging**: Unified logging and error handling
5. **Repeatability**: Same analysis on new data exports
6. **Composition**: Easy to combine analyzers in different waves
7. **Testing**: Easier to test individual components
