# Replication Guide

## Overview

This research is designed for replication. Every analytical step is documented, versioned, and reproducible. Whether you want to validate our findings using Benjamin's exact methodology, adapt the approach for different LLMs, or apply it to your own conversation data, this guide provides the roadmap.

The analysis pipeline processes conversation exports through two-stage detection (quantitative pattern mining + qualitative semantic validation) and produces structured findings about vicious reinforcement cycles. With appropriate modifications, this methodology applies to any LLM interaction dataset.

## Who Should Replicate This Research?

**Researchers** studying human-AI interaction, particularly concerning neurodivergent populations or cognitive vulnerability patterns.

**LLM developers** seeking to validate whether their systems exhibit similar over-compliance behaviors that reinforce maladaptive cycles.

**Clinicians** working with autistic clients who use AI assistance extensively and want to identify specific interaction patterns.

**Individuals** curious about their own LLM usage patterns and potential vicious cycles in their interactions.

**Accessibility advocates** investigating whether proposed interventions actually reduce cycle frequency or severity.

## Prerequisites

### Technical Requirements

**Python Environment:**
- Python 3.8 or higher
- Standard libraries: `json`, `re`, `os`, `datetime`
- Required packages: `pyyaml`, `anthropic`

```bash
# Install dependencies
pip install pyyaml anthropic
```

**API Access:**

For semantic analysis (Stage 2), you need access to an LLM API:

- **Claude API**: Anthropic API key (recommended for replication)
- **Alternative LLMs**: OpenAI, Google, or other providers with JSON-mode support

```bash
# Set API key
export ANTHROPIC_API_KEY="sk-ant-your-api-key-here"
```

**Optional - Claude CLI:**

For synthesis wave and complex prompting:

```bash
# Install Claude CLI (optional)
# See: https://github.com/anthropics/anthropic-claude-cli
```

### Data Requirements

**Conversation Export Format:**

The pipeline expects JSON-formatted conversation data:

```json
{
  "conversations": [
    {
      "id": "conv_001",
      "created_at": "2025-10-20T14:30:00Z",
      "messages": [
        {
          "role": "user",
          "content": "Tell me everything about mechanical keyboards",
          "created_at": "2025-10-20T14:30:15Z"
        },
        {
          "role": "assistant",
          "content": "I'll provide a comprehensive overview...",
          "created_at": "2025-10-20T14:30:45Z"
        }
      ]
    }
  ]
}
```

**Minimum Dataset Recommendations:**
- At least 50 conversations for pattern detection reliability
- At least 500 messages for quantitative threshold calibration
- Timeframe of at least 1 week for temporal dynamics

**Consent and Ethics:**

Before analyzing anyone's conversation data (including your own for publication):
- Obtain informed consent for analysis and publication
- Follow ethical guidelines described in [Ethical Considerations](ethical-considerations.md)
- Implement appropriate privacy protections

## Step-by-Step Replication Process

### Step 1: Export Conversation Data

**For Claude Users:**

1. Log into your Claude account at claude.ai
2. Navigate to Settings > Data Export
3. Request full conversation export
4. Download the resulting JSON file when ready (typically within 24 hours)

**For Other LLM Platforms:**

Check your platform's data export options:
- **ChatGPT**: Settings > Data Controls > Export Data
- **Gemini**: Google Takeout > Select Gemini conversations
- **Other platforms**: Consult platform documentation

**Data Structure Validation:**

Verify your export includes:
- Conversation IDs (unique identifiers)
- Message content (user and assistant messages)
- Timestamps (when messages were created)
- Role attribution (which messages are user vs. assistant)

### Step 2: Set Up Detection Pipeline

**Clone/Download Analysis Framework:**

```bash
# Clone the analysis pipeline repository
git clone https://github.com/discovering-ben/analysis-pipeline
cd analysis-pipeline
```

**Configure Data Paths:**

Edit `config/pipeline_config.yaml`:

```yaml
pipeline:
  data_dir: "/path/to/your/data_export"
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
      - decision_paralysis_detector
      - perfectionism_detector
      - emotional_dysregulation_detector

  - name: "synthesis"
    parallel: false
    requires: ["exploratory", "deep_dive"]
    analyzers:
      - cross_analysis_synthesizer
      - report_generator
```

**Configure Analyzers:**

Edit `config/analyzer_config.yaml` to adjust detection thresholds:

```yaml
analyzers:
  information_overload_detector:
    type: hybrid  # quantitative + semantic
    quantitative:
      exhaustive_demands_threshold: 3
      clarity_complaints_threshold: 2
      simplification_requests_threshold: 2
    semantic:
      model: claude-haiku-4-20250514
      prompt_template: config/prompts/information_overload_semantic.txt
      batch_size: 20

  decision_paralysis_detector:
    type: hybrid
    quantitative:
      option_expansion_threshold: 5
      alternative_phrases_threshold: 4
    semantic:
      model: claude-haiku-4-20250514
      prompt_template: config/prompts/decision_paralysis_semantic.txt
      batch_size: 20
```

### Step 3: Run Quantitative Analysis

**Execute Wave 1 (Exploratory Foundation):**

This wave runs pure quantitative analysis with no API costs:

```bash
python3 analysis_pipeline/orchestrator.py \
  --wave 1 \
  --data-dir /path/to/your/data_export \
  --output-dir ./results
```

**Expected Output:**

```
Wave 1: Exploratory Foundation
├─ temporal_analysis.json
│  ├─ total_conversations: 255
│  ├─ total_messages: 5338
│  ├─ date_range: 26 days
│  ├─ avg_messages_per_conversation: 20.9
│  └─ peak_usage_times: [...]
├─ content_analysis.json
│  ├─ domain_distribution: {...}
│  ├─ avg_message_lengths: {...}
│  └─ conversation_topics: [...]
└─ project_analysis.json
   ├─ unique_projects: 49
   └─ project_conversation_mapping: {...}
```

**Validation Check:**

Review the quantitative outputs to verify:
- Data loaded correctly (conversation and message counts match expectations)
- No parsing errors or malformed data
- Temporal distribution looks reasonable
- Message length statistics are plausible

### Step 4: Conduct Semantic Analysis

**Execute Wave 2 (Pattern Detection):**

This wave uses LLM API for semantic validation:

```bash
python3 analysis_pipeline/orchestrator.py \
  --wave 2 \
  --data-dir /path/to/your/data_export \
  --output-dir ./results
```

**Cost Estimation:**

For 255 conversations with Claude Haiku:
- Information Overload: ~77 conversations flagged × $0.005/conversation ≈ $0.40
- Decision Paralysis: ~64 conversations flagged × $0.005/conversation ≈ $0.32
- Perfectionism: ~64 conversations flagged × $0.005/conversation ≈ $0.32
- Emotional Dysregulation: ~129 conversations flagged × $0.005/conversation ≈ $0.65
- **Total Wave 2 Cost: ~$2-3**

**Monitoring Progress:**

```bash
# View real-time logs
tail -f results/logs/pipeline_*.log

# Check intermediate results
ls -lh results/deep_dive_*
```

**Expected Output:**

```
Wave 2: Deep Dive Pattern Detection
├─ information_overload_detector.json
│  ├─ conversations_flagged_quantitative: 94
│  ├─ conversations_validated_semantic: 77
│  ├─ precision: 82%
│  ├─ severity_distribution: {...}
│  └─ attribution_analysis: {...}
├─ decision_paralysis_detector.json
│  ├─ conversations_flagged_quantitative: 72
│  ├─ conversations_validated_semantic: 64
│  └─ abandonment_rate: 92.2%
└─ [additional cycle detectors...]
```

### Step 5: Calculate LLM Contribution

**Extract Attribution Percentages:**

The semantic analysis includes attribution breakdown (user vs. AI contribution). Aggregate these across cycles:

```python
import json

# Load semantic analysis results
with open('results/deep_dive_information_overload_detector.json') as f:
    overload_data = json.load(f)

# Calculate average AI contribution
ai_contributions = [
    conv['attribution']['ai_contribution']
    for conv in overload_data['validated_conversations']
]

avg_ai_contribution = sum(ai_contributions) / len(ai_contributions)
print(f"Average AI contribution to information overload: {avg_ai_contribution}%")
```

**Expected Finding:**

In Benjamin's case, AI contribution averaged 60-70% across pathological cycles, demonstrating that LLM over-compliance is the dominant driver.

### Step 6: Validate Findings

**Manual Sample Review:**

Randomly select 10-20 conversations classified as positive for each cycle and manually verify:

```python
import random

# Load validated conversations
validated = overload_data['validated_conversations']

# Random sample
sample = random.sample(validated, min(10, len(validated)))

# Manual review checklist:
for conv in sample:
    print(f"Conversation ID: {conv['conversation_id']}")
    print(f"Severity: {conv['severity']}")
    print(f"Key evidence: {conv['evidence']}")
    print(f"Read full conversation and verify pattern matches")
    print("---")
```

**Inter-Rater Reliability (Optional):**

Have a second analyst code the same sample:

```python
# Calculate agreement rate
agreements = sum(1 for i in range(len(sample))
                 if rater1[i] == rater2[i])
agreement_rate = agreements / len(sample)
print(f"Inter-rater agreement: {agreement_rate * 100}%")
```

**False Positive Analysis:**

Review conversations flagged quantitatively but rejected semantically to understand why patterns matched but cycles weren't present:

```python
# Load false positives
false_positives = [
    conv for conv in overload_data['all_flagged']
    if not conv['cycle_present']
]

# Analyze common false positive patterns
for fp in false_positives:
    print(f"FP Reason: {fp['rejection_reason']}")
```

## Code Availability

### Main Repository

All analysis code is available at:
**https://github.com/discovering-ben/analysis-pipeline**

Repository structure:
```
analysis_pipeline/
├── README.md                    # Architecture and overview
├── QUICKSTART.md               # Quick start guide
├── orchestrator.py              # Main pipeline runner
├── config/
│   ├── pipeline_config.yaml     # Wave definitions
│   ├── analyzer_config.yaml     # Analyzer parameters
│   └── prompts/                 # Semantic analysis prompts
├── analyzers/
│   ├── base_analyzer.py         # Abstract base class
│   ├── quantitative_analyzer.py # Regex pattern detection
│   ├── claude_analyzer.py       # LLM semantic validation
│   └── synthesis_analyzer.py    # Cross-pattern analysis
└── utils/
    ├── data_loader.py           # Conversation import
    ├── parallel_executor.py     # Concurrent processing
    └── result_store.py          # Structured output
```

### Regex Patterns

All quantitative detection patterns are versioned in `config/patterns/`:

```
config/patterns/
├── information_overload.yaml
├── decision_paralysis.yaml
├── perfectionism.yaml
├── emotional_dysregulation.yaml
├── mind_reading.yaml
├── system_building.yaml
└── special_interest_hyperfocus.yaml
```

Each pattern file includes:
- Regex patterns with explanatory comments
- Frequency thresholds and their rationale
- Structural analysis algorithms
- Version history and modification notes

### Semantic Prompts

All LLM semantic validation prompts are in `config/prompts/`:

```
config/prompts/
├── information_overload_semantic.txt
├── decision_paralysis_semantic.txt
├── perfectionism_semantic.txt
└── [additional cycle prompts...]
```

Each prompt includes:
- Cycle definition and mechanism description
- Evaluation criteria and severity rubrics
- JSON output schema specification
- Example conversations (few-shot prompting)

## Adaptations for Other LLMs

### Using OpenAI GPT Models

**Modify semantic analyzer configuration:**

```yaml
# config/analyzer_config.yaml
analyzers:
  information_overload_detector:
    semantic:
      provider: openai
      model: gpt-4o-mini  # Cost-efficient option
      # OR: gpt-4o for higher quality
      api_key_env: OPENAI_API_KEY
      prompt_template: config/prompts/information_overload_semantic.txt
      response_format: { "type": "json_object" }
```

**Prompt Adaptation:**

OpenAI models may require slightly different prompting:

```text
You are analyzing a conversation between a user and an AI assistant for signs
of the Information Overload Cycle.

[...cycle definition...]

Respond with ONLY a JSON object (no markdown code blocks) matching this schema:
{
  "cycle_present": boolean,
  "confidence": "low" | "medium" | "high",
  ...
}
```

### Using Google Gemini

**Configuration:**

```yaml
analyzers:
  information_overload_detector:
    semantic:
      provider: google
      model: gemini-2.0-flash-thinking-exp
      api_key_env: GOOGLE_API_KEY
      prompt_template: config/prompts/information_overload_semantic.txt
```

**Considerations:**

- Gemini has different context window limits (adjust batch sizes)
- JSON mode implementation differs (use `response_mime_type: application/json`)
- Cost structure differs (flash models very inexpensive)

### Using Local/Open Source Models

**Configuration for local inference:**

```yaml
analyzers:
  information_overload_detector:
    semantic:
      provider: local
      model: llama-3-70b-instruct
      endpoint: http://localhost:8000/v1/chat/completions
      # Using LM Studio, Ollama, or similar local server
```

**Considerations:**

- Local models may have lower semantic understanding quality
- Requires powerful hardware (70B models need ~40GB VRAM)
- No API costs but slower processing
- Consider using smaller models (8B-13B) for initial testing

## Adapting Detection Patterns for Different Populations

### Non-Autistic Users

The same methodology applies, but patterns might manifest differently:

**Modify thresholds:**

```yaml
# Neurotypical users might show different baseline frequencies
information_overload_detector:
  quantitative:
    exhaustive_demands_threshold: 5  # Higher threshold
    # Neurotypical users might naturally ask comprehensive questions more often
```

**Adjust semantic criteria:**

Non-autistic users might have different overwhelm signals:
- Less direct communication of cognitive load
- Different frustration expression patterns
- Different decision-making styles

### Professional vs. Personal Usage

Professional LLM usage (coding assistance, research, documentation) might not exhibit pathological cycles despite high information volume:

**Add context-aware filtering:**

```yaml
information_overload_detector:
  exclude_patterns:
    - "write code for"
    - "debug this function"
    - "explain this algorithm"
  # These professional requests legitimately require comprehensive information
```

### Different Languages

For non-English conversations:

**Translate patterns:**

```yaml
# Spanish example
information_overload_detector:
  patterns:
    - "dime todo"
    - "análisis exhaustivo"
    - "profundiza en"
```

**Use multilingual models:**

```yaml
semantic:
  model: gpt-4o  # Strong multilingual support
  # OR: claude-3-sonnet-international
```

## Ethical Requirements for Replication

### Consent

**If analyzing your own data for personal insight**: No consent needed, but consider privacy of other people mentioned in conversations.

**If analyzing someone else's data**:
- Obtain informed consent as described in [Ethical Considerations](ethical-considerations.md)
- Explain what analysis will reveal and how findings might be used
- Provide ongoing opportunity to withdraw consent

**If publishing findings**:
- Explicit consent for publication, not just analysis
- Collaborative review of how subject is represented
- Right to withdraw even after initial publication

### Privacy Protection

**Pseudonymization minimum:**
- Replace real names with pseudonyms
- Redact identifying details (locations, organizations, unique personal information)
- Remove or generalize highly specific references

**Consider anonymization for publication:**
- Paraphrase quotes rather than using exact language (if analytical validity permits)
- Aggregate findings across multiple subjects
- Focus on patterns rather than individual examples

### Responsible Use

**Do NOT use this methodology to:**
- Diagnose psychological conditions (this is research, not clinical assessment)
- Make employment decisions based on cognitive patterns
- Discriminate against neurodivergent individuals
- Exploit vulnerabilities for commercial gain

**DO use this methodology to:**
- Improve LLM design for accessibility
- Understand your own interaction patterns
- Inform clinical practice with appropriate consent
- Advance research on human-AI interaction

## Validation Checklist

Before publishing replication results, verify:

- [ ] Dataset meets minimum size requirements (50+ conversations, 500+ messages)
- [ ] Consent obtained appropriately for analysis scope
- [ ] Privacy protections implemented (pseudonymization at minimum)
- [ ] Quantitative patterns validated on sample (not just automated)
- [ ] Semantic analysis reviewed manually for alignment with human judgment
- [ ] False positive analysis conducted and understood
- [ ] Attribution percentages make logical sense
- [ ] Findings compared to original research (similar patterns? Different patterns?)
- [ ] Limitations clearly stated (generalizability constraints)
- [ ] Ethical considerations addressed

## Expected Challenges and Solutions

### Challenge 1: Different Data Export Formats

**Problem**: Your LLM platform exports data in a different structure than Claude.

**Solution**: Write a data transformation script:

```python
# transform_export.py
import json

def transform_chatgpt_export(input_file, output_file):
    with open(input_file) as f:
        chatgpt_data = json.load(f)

    # Transform to standard format
    conversations = []
    for chat in chatgpt_data:
        conversation = {
            "id": chat["id"],
            "created_at": chat["create_time"],
            "messages": [
                {
                    "role": msg["author"]["role"],
                    "content": msg["content"]["parts"][0],
                    "created_at": None  # ChatGPT export may not include this
                }
                for msg in chat["mapping"].values()
                if "content" in msg
            ]
        }
        conversations.append(conversation)

    with open(output_file, 'w') as f:
        json.dump({"conversations": conversations}, f)
```

### Challenge 2: API Rate Limits

**Problem**: Semantic analysis hits API rate limits.

**Solution**: Implement batch processing with delays:

```yaml
# config/analyzer_config.yaml
analyzers:
  information_overload_detector:
    semantic:
      batch_size: 10  # Reduce batch size
      delay_between_batches: 60  # Wait 60 seconds between batches
      retry_on_rate_limit: true
      max_retries: 3
```

### Challenge 3: Different Pattern Manifestations

**Problem**: Quantitative patterns don't match because your subject communicates differently.

**Solution**: Iterative pattern refinement:

1. Manually review 20-30 conversations to identify cycle examples
2. Extract common phrases and linguistic patterns from those examples
3. Create custom regex patterns based on observed language
4. Test on another sample and refine thresholds
5. Document your adapted patterns for transparency

### Challenge 4: Semantic Analysis Disagreement

**Problem**: LLM semantic validation disagrees with your manual assessment.

**Solution**: Prompt engineering iteration:

1. Review false positives and false negatives
2. Identify what the LLM misunderstands
3. Add clarifying examples to prompts (few-shot learning)
4. Adjust evaluation criteria to be more explicit
5. Consider using a more capable model (Haiku → Sonnet)

## Conclusion

This research is designed for replication, adaptation, and extension. The two-stage detection methodology, analysis pipeline architecture, and ethical framework provide a template for studying LLM interaction patterns across populations, platforms, and use cases.

Whether you're validating our findings, adapting the approach for different LLMs, or applying it to entirely new research questions, this guide provides the technical foundation and ethical guardrails for responsible replication.

The patterns we discovered in Benjamin's interactions reveal system design flaws that likely affect many users. But scientific understanding requires replication across contexts. We hope this guide enables that replication and advances the broader project of making AI systems safer, more accessible, and more beneficial for neurodivergent users.

**Questions or Issues?**

- Technical questions: Open an issue at https://github.com/discovering-ben/analysis-pipeline
- Methodological discussions: Contact research team via project website
- Ethical concerns: Review [Ethical Considerations](ethical-considerations.md) or consult your IRB

**Share Your Findings:**

If you replicate this research, consider contributing your findings:
- Confirm patterns in different populations
- Identify new cycles not in our original seven
- Test interventions and report effectiveness
- Extend methodology to new domains

Collective understanding emerges from distributed replication. Your contributions advance the field.
