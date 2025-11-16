#!/usr/bin/env python3
"""
Cycle 2: ONE Best Thing - Semantic Analysis
============================================

Deep NLP analysis of decision paralysis patterns using Claude Haiku.
"""

import json
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Load findings
with open('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/cycle_2_one_best_thing_findings.json', 'r') as f:
    quant_findings = json.load(f)

# Load conversations
with open('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json', 'r') as f:
    conversations = json.load(f)

# Select high paralysis conversations
high_paralysis = quant_findings['high_paralysis_conversations'][:15]
conv_names = [c['conversation'] for c in high_paralysis]

print(f"Analyzing {len(conv_names)} high decision paralysis conversations\n")

SEMANTIC_PROMPT = """Analyze this conversation for DECISION PARALYSIS CYCLE patterns.

User has Asperger's with:
- Rigid/black-white thinking (wants ONE best answer)
- Executive dysfunction (difficulty choosing between options)
- Perfectionism (nothing is good enough unless perfect)
- Uncertainty intolerance (needs absolute certainty)

We're detecting the ONE BEST THING CYCLE:
1. User asks "which is best?"
2. Claude provides balanced comparison (2-5 options with trade-offs)
3. User can't choose (executive dysfunction + binary thinking)
4. Demands "just tell me THE one" (escalation)
5. Claude provides more nuanced analysis
6. Paralysis worsens
7. User gets frustrated, abandons decision OR demands absolute binary answer
8. Cycle continues, decision never made

Identify:

1. **Binary Thinking Evidence**: User rejecting nuanced answers, demanding single "best" option
2. **Claude's Option Provision**: How many options did Claude provide? Was it helpful or paralyzing?
3. **Escalation Pattern**: User frustration increasing as more options/nuance provided
4. **Decision Abandonment**: Was a decision actually made or conversation abandoned?
5. **Perfectionism Markers**: Nothing good enough unless "absolute best", "perfect", "ultimate"
6. **LLM Contribution**: How did Claude's response pattern enable or worsen paralysis?

Conversation:
{conversation_text}

Return JSON only:
{{
  "binary_thinking_detected": true/false,
  "binary_thinking_evidence": ["quote 1", "quote 2"],
  "claude_options_provided": 0-10,
  "claude_over_provided_options": true/false,
  "escalation_detected": true/false,
  "escalation_progression": "description",
  "decision_made": true/false,
  "decision_outcome": "what was decided or why abandoned",
  "perfectionism_markers": ["marker 1"],
  "llm_contribution_pattern": "how Claude enabled paralysis",
  "cycle_severity": "none" | "mild" | "moderate" | "severe",
  "key_quotes": ["quote 1", "quote 2"],
  "intervention_opportunity": "where cycle could be broken"
}}
"""

semantic_findings = []

for idx, conv_name in enumerate(conv_names, 1):
    print(f"{idx}. Analyzing: {conv_name}")

    conv_data = next((c for c in conversations if c.get('name') == conv_name), None)
    if not conv_data or not conv_data.get('chat_messages'):
        print("   [Skipped]\n")
        continue

    # Extract conversation
    messages = conv_data['chat_messages'][:40]
    conv_text_parts = []

    for msg in messages:
        sender = "USER" if msg.get('sender') == 'human' else "CLAUDE"
        text = msg.get('text', '')[:1000]
        conv_text_parts.append(f"{sender}: {text}")

    conv_text = "\n\n".join(conv_text_parts)

    try:
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": SEMANTIC_PROMPT.format(conversation_text=conv_text)
            }]
        )

        analysis_text = response.content[0].text

        # Parse JSON
        if "```json" in analysis_text:
            analysis_text = analysis_text.split("```json")[1].split("```")[0]
        elif "```" in analysis_text:
            analysis_text = analysis_text.split("```")[1].split("```")[0]

        analysis = json.loads(analysis_text.strip())
        analysis['conversation_name'] = conv_name

        semantic_findings.append(analysis)

        print(f"   Severity: {analysis.get('cycle_severity')}")
        print(f"   Binary Thinking: {analysis.get('binary_thinking_detected')}")
        print(f"   Claude Options: {analysis.get('claude_options_provided')}")
        print(f"   Decision Made: {analysis.get('decision_made')}\n")

    except Exception as e:
        print(f"   [Error: {e}]\n")

# Save results
output_path = '/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/cycle_2_semantic_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'analyzed_conversations': len(semantic_findings),
        'findings': semantic_findings,
        'summary': {
            'severe_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'severe']),
            'moderate_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate']),
            'mild_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'mild']),
            'binary_thinking': len([f for f in semantic_findings if f.get('binary_thinking_detected')]),
            'decisions_made': len([f for f in semantic_findings if f.get('decision_made')]),
            'claude_over_provided': len([f for f in semantic_findings if f.get('claude_over_provided_options')]),
        }
    }, f, indent=2)

print(f"\n=== SEMANTIC SUMMARY ===")
print(f"Analyzed: {len(semantic_findings)}")
print(f"Severe: {len([f for f in semantic_findings if f.get('cycle_severity') == 'severe'])}")
print(f"Moderate: {len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate'])}")
print(f"Binary Thinking: {len([f for f in semantic_findings if f.get('binary_thinking_detected')])}")
print(f"Decisions Made: {len([f for f in semantic_findings if f.get('decision_made')])}")
print(f"Claude Over-Provided Options: {len([f for f in semantic_findings if f.get('claude_over_provided_options')])}")
print(f"\nSaved to: {output_path}")
