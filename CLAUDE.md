# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a research project analyzing Claude account data export for Benjamin Hallett (codename: "Benjamin"). The analysis explores usage patterns, interaction behaviors, and neurodivergent AI interaction dynamics from 265 conversations spanning October-November 2025.

## Data Files (Not in Git)

The repository works with large JSON data exports:

- `conversations.json` (89.5 MB) - Full conversation history
- `memories.json` (82.6 KB) - Conversation memory system
- `projects.json` (50.4 KB) - Custom project metadata
- `users.json` (158 bytes) - User profile data

These files are private and excluded from version control.

## Analysis Scripts

All analysis scripts are Python 3 and use standard libraries plus Anthropic SDK where needed.

### Core Analysis Tools (in `.claude/` directory)

- `analysis_temporal.py` - Temporal patterns (activity hours, session durations)
- `analysis_content.py` - Content categorization and keyword extraction
- `analysis_projects.py` - Project organization analysis
- `deep_dive_conversations.py` - Individual conversation deep dives

### Specialized Analysis (root directory)

- `cycle_1_information_overload_detector.py` - Pattern detection for cognitive overload cycles
- `cycle_1_semantic_analyzer.py` - Uses Anthropic API for qualitative analysis
- `pattern_search.py` - Keyword and pattern extraction utilities
- `claude_response_analysis.py` - Response quality and length analysis

### Running Scripts

All Python scripts are designed to be run from the repository root:

```bash
python3 cycle_1_information_overload_detector.py
python3 .claude/analysis_temporal.py
```

Scripts that use the Anthropic API require `ANTHROPIC_API_KEY` environment variable.

## Key Research Findings

Reference these documents for context when developing new analyses:

- `exploratory_analysis_report.md` - Comprehensive initial findings (614 lines)
- `follow_up_priorities.md` - Prioritized investigation areas
- `quick_reference_summary.md` - At-a-glance summary of Benjamin's usage
- `docs/neurodivergent-llm-interaction-analysis.md` - Deep dive into interaction patterns
- `docs/benjamin-custom-system-prompt.md` - Recommended custom prompt for Benjamin

## Analysis Approach

This project uses a wave-based parallel analysis methodology:

1. **Wave 1**: Multiple specialized scripts run simultaneously (temporal, content, projects)
2. **Wave 2**: Deep-dive analysis building on Wave 1 results
3. **Synthesis**: Cross-analysis pattern detection and insight aggregation

When creating new analysis scripts:

- Output results to JSON files in `.claude/results_*.json` format
- Keep scripts focused on single analysis dimensions
- Use descriptive variable names (Benjamin has autism - clarity matters)
- Include docstrings explaining the hypothesis being tested

## Subject Profile: Benjamin

When analyzing data, context matters:

- **Neurodivergent user** (autism/Asperger's) with theory of mind challenges
- **Power user**: 265 conversations in 26 days (10.2/day average)
- **Primary use cases**: Legal advocacy (62%), wellness (36%), technology (30%), financial (29%)
- **Communication style**: Direct, directive, quality-obsessive
- **Peak activity**: Evenings (18:00-21:00), especially Saturdays/Thursdays

## File Naming Conventions

Follow lowercase convention with underscores:

```
cycle_1_information_overload_detector.py  # Correct
Cycle1InformationOverloadDetector.py      # Incorrect
```

Documentation files use kebab-case:

```
exploratory-analysis-report.md  # Acceptable
exploratory_analysis_report.md  # Also acceptable (current format)
```

## Output Conventions

Analysis results should include:

1. **Hypothesis**: What pattern are you looking for and why?
2. **Methodology**: How are you detecting it?
3. **Findings**: What did you discover?
4. **Confidence**: How certain are you about the results?
5. **Limitations**: What can't this analysis tell you?

See `cycle_1_information_overload_detector.py` for a good example structure.

## Common Analysis Patterns

### Loading Conversation Data

```python
import json

with open('conversations.json', 'r') as f:
    data = json.load(f)

conversations = data  # Array of conversation objects
```

### Conversation Structure

Each conversation has:
- `uuid`: Unique identifier
- `name`: Conversation title
- `created_at`: ISO timestamp
- `updated_at`: ISO timestamp
- `chat_messages`: Array of message objects

Each message has:
- `sender`: "human" or "assistant"
- `text`: Message content
- `created_at`: ISO timestamp

### Pattern Detection

Use regex patterns with case-insensitive matching:

```python
import re

pattern = r'\btell me everything\b'
matches = re.findall(pattern, text, re.IGNORECASE)
```

### Temporal Analysis

Convert ISO timestamps to datetime objects:

```python
from datetime import datetime

timestamp = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
```

## Anthropic API Usage

For semantic analysis requiring AI:

```python
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-haiku-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
)
```

Use Haiku for fast batch analysis, Sonnet for complex reasoning.

## Privacy and Ethics

This is private research data analyzing a real person's AI interactions. When working with this codebase:

- Never expose raw conversation content publicly
- Aggregate and anonymize findings for any shared output
- Focus on patterns, not individual messages
- Treat subject with dignity (Benjamin is a real person with autism)

## Analysis Goals

The overarching research questions:

1. How do neurodivergent individuals use AI assistants differently?
2. What interaction patterns indicate cognitive overload?
3. Can we detect maladaptive usage cycles?
4. How should AI assistants adapt to neurodivergent users?
5. What makes AI effective as an accessibility tool?

Keep these questions in mind when developing new analyses.
