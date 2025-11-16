#!/usr/bin/env python3
"""
Cycle 6: System Building Obsession - Semantic Analyzer
Uses Claude Haiku to analyze conversations for system building patterns
"""

import json
import os
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

print("Loading quantitative findings...")
with open('../../outputs/cycle_6_system_building_findings.json', 'r') as f:
    quant_findings = json.load(f)

print("Loading full conversations...")
with open('../../outputs/conversations.json', 'r') as f:
    all_conversations = json.load(f)

# Get conversations with highest obsession scores
high_obsession_convs = quant_findings.get('high_obsession_conversations', [])[:5]

print(f"\n=== SEMANTIC ANALYSIS OF SYSTEM BUILDING OBSESSION ===")
print(f"Analyzing {len(high_obsession_convs)} conversations with highest obsession scores\n")

semantic_findings = []

ANALYSIS_PROMPT = """Analyze this conversation for system building obsession patterns.

Look for:
1. **System creation requests**: Does user request elaborate systems/frameworks?
2. **Complexity escalation**: Does complexity increase over conversation?
3. **Meta-systems**: Systems to organize other systems?
4. **Expansion requests**: Does user keep adding to the system?
5. **Maintenance issues**: Does system become too complex to maintain?
6. **Claude response pattern**: Does Claude encourage or enable complexity?
7. **Task completion**: Was a usable system created or abandoned?
8. **LLM contribution**: How much did Claude's responses reinforce this pattern?

Respond with JSON (no other text):
{
  "system_creation_requests": <int count>,
  "system_creation_examples": [<list of text snippets>],
  "complexity_markers": <int count>,
  "complexity_examples": [<list>],
  "expansion_requests": <int count>,
  "meta_system_detected": <bool>,
  "claude_response_pattern": "<encouraged_complexity|questioned_necessity|provided_simple_alternative|neutral>",
  "claude_response_examples": [<list>],
  "user_reaction_to_complexity": "<satisfied|overwhelmed|kept_expanding|abandoned>",
  "task_completion_status": "<completed|abandoned|ongoing|over_engineered>",
  "system_actually_used": <bool>,
  "evidence_of_use": "<string or null>",
  "llm_contribution_pattern": "<string describing how Claude contributed>",
  "cycle_severity": "<non_issue|mild|moderate|severe>",
  "key_quotes": [<list>],
  "intervention_opportunity": "<string>",
  "conversation_name": "<string>"
}

Conversation:"""

for i, conv_summary in enumerate(high_obsession_convs, 1):
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
    print(f"   Obsession score: {conv_summary['obsession_score']}")

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
        print(f"   - System creation requests: {analysis.get('system_creation_requests', 0)}")
        print(f"   - Complexity markers: {analysis.get('complexity_markers', 0)}")
        print(f"   - Task completion: {analysis.get('task_completion_status', 'unknown')}")
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
        "systems_completed": len([f for f in semantic_findings if f.get('task_completion_status') == 'completed']),
        "systems_abandoned": len([f for f in semantic_findings if f.get('task_completion_status') == 'abandoned']),
        "systems_over_engineered": len([f for f in semantic_findings if f.get('task_completion_status') == 'over_engineered']),
        "claude_encouraged_complexity": len([f for f in semantic_findings if 'encouraged' in f.get('claude_response_pattern', '')]),
    }
}

output_path = '../../outputs/cycle_6_semantic_findings.json'
with open(output_path, 'w') as f:
    json.dump(output, f, indent=2)

print(f"\n=== SEMANTIC ANALYSIS SUMMARY ===")
print(f"Analyzed conversations: {output['analyzed_conversations']}")
print(f"Severity breakdown:")
print(f"  - Severe: {output['summary']['severe_cycles']}")
print(f"  - Moderate: {output['summary']['moderate_cycles']}")
print(f"  - Mild: {output['summary']['mild_cycles']}")
print(f"  - Non-issue: {output['summary']['non_issue']}")
print(f"\nTask completion:")
print(f"  - Completed: {output['summary']['systems_completed']}")
print(f"  - Abandoned: {output['summary']['systems_abandoned']}")
print(f"  - Over-engineered: {output['summary']['systems_over_engineered']}")
print(f"\nClaude encouraged complexity: {output['summary']['claude_encouraged_complexity']}")

print(f"\nFindings saved to: {output_path}")
print("\n=== ANALYSIS COMPLETE ===")
