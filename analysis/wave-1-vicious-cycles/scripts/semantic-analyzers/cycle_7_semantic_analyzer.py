#!/usr/bin/env python3
"""
Cycle 7: Special Interest Hyperfocus - Semantic Analyzer
Uses Claude Haiku to analyze conversations for special interest patterns
"""

import json
import os
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

print("Loading quantitative findings...")
with open('../../outputs/cycle_7_special_interest_findings.json', 'r') as f:
    quant_findings = json.load(f)

print("Loading full conversations...")
with open('../../outputs/conversations.json', 'r') as f:
    all_conversations = json.load(f)

# Get conversations with highest hyperfocus scores
high_hyperfocus_convs = quant_findings.get('high_hyperfocus_conversations', [])[:10]

print(f"\n=== SEMANTIC ANALYSIS OF SPECIAL INTEREST HYPERFOCUS ===")
print(f"Analyzing {len(high_hyperfocus_convs)} conversations with highest hyperfocus scores\n")

semantic_findings = []

ANALYSIS_PROMPT = """Analyze this conversation for special interest hyperfocus patterns.

Look for:
1. **Topic persistence**: Does user stay on one narrow topic?
2. **Deep dive requests**: Does user request extensive detail on special interest?
3. **Repeated engagement**: Many follow-ups on same subject?
4. **Time displacement**: Does hyperfocus prevent other tasks?
5. **Special interest type**: What is the subject? (spirituality, technology, health, complaints, etc.)
6. **Claude response pattern**: Does Claude enable extended focus or redirect?
7. **Productive vs unproductive**: Is this focus helpful or displacing priorities?
8. **Natural autism trait**: Is this healthy special interest expression or pathological?

Respond with JSON (no other text):
{
  "special_interest_detected": <bool>,
  "special_interest_type": "<spirituality|technology|health|complaints|other>",
  "special_interest_details": "<string describing specific interest>",
  "topic_persistence_score": <0-10 how narrowly focused>,
  "deep_dive_requests": <int count>,
  "deep_dive_examples": [<list>],
  "message_count": <int>,
  "conversation_length_assessment": "<brief|moderate|extended|marathon>",
  "claude_response_pattern": "<enabled_hyperfocus|provided_boundaries|neutral|redirected>",
  "claude_response_examples": [<list>],
  "hyperfocus_productivity": "<highly_productive|somewhat_productive|neutral|unproductive|displaced_priorities>",
  "evidence_of_displacement": "<string or null>",
  "natural_vs_pathological": "<natural_healthy_interest|borderline|pathological_displacement>",
  "llm_contribution_pattern": "<string describing how Claude contributed>",
  "cycle_severity": "<non_issue|mild|moderate|severe>",
  "key_quotes": [<list>],
  "intervention_opportunity": "<string or null>",
  "conversation_name": "<string>"
}

Conversation:"""

for i, conv_summary in enumerate(high_hyperfocus_convs, 1):
    conv_name = conv_summary['conversation']

    # Find full conversation
    full_conv = None
    for conv in all_conversations:
        if conv.get('name') == conv_name:
            full_conv = conv
            break

    if not full_conv or not full_conv.get('chat_messages'):
        print(f"{i}. Skipping {conv_name} - conversation not found")
        continue

    print(f"{i}. Analyzing: {conv_name}")
    print(f"   Hyperfocus score: {conv_summary['hyperfocus_score']}")
    print(f"   Dominant interest: {conv_summary.get('dominant_interest', 'None')}")

    # Build conversation text
    conv_text = f"Conversation: {conv_name}\n\n"
    for msg in full_conv['chat_messages']:
        sender = "User" if msg.get('sender') == 'human' else "Claude"
        text = msg.get('text', '')
        conv_text += f"{sender}: {text}\n\n"

    # Limit to reasonable size (first 15000 chars)
    if len(conv_text) > 15000:
        conv_text = conv_text[:15000] + "\n\n[Conversation truncated for analysis]"

    try:
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=2000,
            temperature=0,
            messages=[{
                "role": "user",
                "content": ANALYSIS_PROMPT + "\n\n" + conv_text
            }]
        )

        analysis_text = response.content[0].text

        # Extract JSON from code blocks if present
        if "```json" in analysis_text:
            analysis_text = analysis_text.split("```json")[1].split("```")[0]
        elif "```" in analysis_text:
            analysis_text = analysis_text.split("```")[1].split("```")[0]

        analysis = json.loads(analysis_text.strip())
        semantic_findings.append(analysis)

        print(f"   ✓ Analysis complete")
        print(f"   - Special interest: {analysis.get('special_interest_type', 'unknown')}")
        print(f"   - Topic persistence: {analysis.get('topic_persistence_score', 0)}/10")
        print(f"   - Natural vs pathological: {analysis.get('natural_vs_pathological', 'unknown')}")
        print(f"   - Cycle severity: {analysis.get('cycle_severity', 'unknown')}\n")

    except json.JSONDecodeError as e:
        print(f"   ✗ JSON parsing error: {e}")
        print(f"   Raw response: {analysis_text[:200]}...\n")
    except Exception as e:
        print(f"   ✗ Error: {e}\n")

# Save findings
output = {
    "analyzed_conversations": len(semantic_findings),
    "findings": semantic_findings,
    "summary": {
        "severe_cycles": len([f for f in semantic_findings if f.get('cycle_severity') == 'severe']),
        "moderate_cycles": len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate']),
        "mild_cycles": len([f for f in semantic_findings if f.get('cycle_severity') == 'mild']),
        "non_issue": len([f for f in semantic_findings if f.get('cycle_severity') == 'non_issue']),
        "natural_healthy": len([f for f in semantic_findings if f.get('natural_vs_pathological') == 'natural_healthy_interest']),
        "pathological": len([f for f in semantic_findings if f.get('natural_vs_pathological') == 'pathological_displacement']),
        "claude_enabled_hyperfocus": len([f for f in semantic_findings if 'enabled' in f.get('claude_response_pattern', '')]),
        "special_interest_types": {}
    }
}

# Count interest types
for finding in semantic_findings:
    interest_type = finding.get('special_interest_type', 'unknown')
    output['summary']['special_interest_types'][interest_type] = output['summary']['special_interest_types'].get(interest_type, 0) + 1

output_path = '../../outputs/cycle_7_semantic_findings.json'
with open(output_path, 'w') as f:
    json.dump(output, f, indent=2)

print(f"\n=== SEMANTIC ANALYSIS SUMMARY ===")
print(f"Analyzed conversations: {output['analyzed_conversations']}")
print(f"\nSeverity breakdown:")
print(f"  - Severe: {output['summary']['severe_cycles']}")
print(f"  - Moderate: {output['summary']['moderate_cycles']}")
print(f"  - Mild: {output['summary']['mild_cycles']}")
print(f"  - Non-issue: {output['summary']['non_issue']}")
print(f"\nNatural vs pathological:")
print(f"  - Natural healthy interest: {output['summary']['natural_healthy']}")
print(f"  - Pathological displacement: {output['summary']['pathological']}")
print(f"\nClaude enabled hyperfocus: {output['summary']['claude_enabled_hyperfocus']}")
print(f"\nSpecial interest types:")
for interest, count in output['summary']['special_interest_types'].items():
    print(f"  - {interest}: {count}")

print(f"\nFindings saved to: {output_path}")
print("\n=== ANALYSIS COMPLETE ===")
