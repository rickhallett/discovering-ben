#!/usr/bin/env python3
"""
Information Overload Cycle - Semantic Analysis
===============================================

Uses Claude Haiku to detect nuanced patterns that regex cannot catch:
- Implicit overwhelm signals
- Satisfaction paradox (more info = less satisfied)
- Filter failure indicators
- Escalation within conversations
- LLM over-provisioning patterns

This complements the quantitative detection with qualitative depth.
"""

import json
import os
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Load the quantitative findings
with open('../../outputs/cycle_1_information_overload_findings.json', 'r') as f:
    quant_findings = json.load(f)

# Load conversations for deep analysis
with open('../../outputs/conversations.json', 'r') as f:
    conversations = json.load(f)

# Select conversations with high overload potential for semantic analysis
# Criteria: exhaustive demands + clarity complaints + long Claude responses
high_risk_convs = []
for conv in quant_findings['conversation_level_analysis']:
    if (conv['exhaustive_demands'] > 0 or conv['clarity_complaints'] > 0) and \
       conv['avg_claude_response_length'] > 1500:
        high_risk_convs.append(conv['conversation'])

print(f"Selected {len(high_risk_convs)} high-risk conversations for semantic analysis")
print("Using Claude Haiku for fast NLP analysis...\n")

# Semantic analysis prompts
SEMANTIC_ANALYSIS_PROMPT = """You are analyzing a conversation between a user with autism/Asperger's and Claude AI to detect information overload patterns.

The user has:
- Theory of mind deficits (cannot model AI limitations)
- Executive dysfunction (difficulty filtering information)
- Uncertainty intolerance (needs to feel certain)
- Rigid thinking

We're looking for evidence of the INFORMATION OVERLOAD CYCLE:
1. User asks question (seeking certainty)
2. Claude provides detailed answer
3. User can't filter what's relevant (executive dysfunction)
4. Feels overwhelmed but NOT satisfied (still uncertain)
5. Asks for MORE information to feel certain
6. Claude provides even MORE detail
7. Cycle repeats, cognitive overload increases

Analyze this conversation excerpt and identify:

1. **Implicit Overwhelm Signals**: Signs user is cognitively overloaded without saying "I'm overwhelmed"
   - Abrupt topic changes
   - Frustration after detail
   - Simplified/binary questions after complex answers
   - "Just tell me" after detailed explanation

2. **Satisfaction Paradox**: Evidence that MORE information led to LESS satisfaction
   - Still uncertain after comprehensive answers
   - Asks same question different way
   - Escalates demands after getting answer

3. **Filter Failure**: User can't extract what's relevant from Claude's response
   - Focuses on wrong details
   - Misses key information
   - Gets stuck on tangential points

4. **Claude Over-Provisioning**: Ways Claude amplifies the cycle
   - Giving more detail than asked for
   - Multiple options when one was needed
   - Comprehensive lists when simple answer would work
   - Not checking if user can process the information

5. **Cycle Progression**: How the conversation escalates over turns
   - Information demands increasing
   - User frustration rising
   - Response lengths growing

Conversation:
{conversation_text}

Provide your analysis in this JSON format:
{{
  "implicit_overwhelm_detected": true/false,
  "overwhelm_signals": ["signal 1", "signal 2"],
  "satisfaction_paradox": true/false,
  "paradox_evidence": "brief description",
  "filter_failure": true/false,
  "filter_failure_examples": ["example 1"],
  "claude_over_provisioning": true/false,
  "over_provisioning_patterns": ["pattern 1"],
  "cycle_severity": "none" | "mild" | "moderate" | "severe",
  "cycle_progression": "description of how it escalates",
  "key_quotes": ["quote 1", "quote 2"],
  "intervention_opportunity": "where Claude could have broken the cycle"
}}

Return ONLY the JSON, no other text."""

# Analyze a sample of high-risk conversations
semantic_findings = []
max_to_analyze = 10  # Start with 10 for speed

print(f"Analyzing {min(max_to_analyze, len(high_risk_convs))} conversations in depth...\n")

for idx, conv_name in enumerate(high_risk_convs[:max_to_analyze], 1):
    print(f"{idx}. Analyzing: {conv_name}")

    # Find the conversation
    conv_data = next((c for c in conversations if c.get('name') == conv_name), None)
    if not conv_data or not conv_data.get('chat_messages'):
        print("   [Skipped - no messages]\n")
        continue

    # Extract conversation text (limit to first 20 exchanges to fit context)
    messages = conv_data['chat_messages'][:40]  # 20 exchanges
    conv_text_parts = []

    for msg in messages:
        sender = "USER" if msg.get('sender') == 'human' else "CLAUDE"
        text = msg.get('text', '')[:1000]  # Limit each message to 1000 chars
        conv_text_parts.append(f"{sender}: {text}")

    conv_text = "\n\n".join(conv_text_parts)

    try:
        # Call Claude Haiku for semantic analysis
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": SEMANTIC_ANALYSIS_PROMPT.format(conversation_text=conv_text)
            }]
        )

        analysis_text = response.content[0].text

        # Parse JSON response
        # Remove markdown code blocks if present
        if "```json" in analysis_text:
            analysis_text = analysis_text.split("```json")[1].split("```")[0]
        elif "```" in analysis_text:
            analysis_text = analysis_text.split("```")[1].split("```")[0]

        analysis = json.loads(analysis_text.strip())
        analysis['conversation_name'] = conv_name

        semantic_findings.append(analysis)

        # Print summary
        print(f"   Cycle Severity: {analysis.get('cycle_severity', 'unknown')}")
        print(f"   Overwhelm: {analysis.get('implicit_overwhelm_detected', False)}")
        print(f"   Satisfaction Paradox: {analysis.get('satisfaction_paradox', False)}")
        print(f"   Filter Failure: {analysis.get('filter_failure', False)}")
        print(f"   Claude Over-Provisioning: {analysis.get('claude_over_provisioning', False)}\n")

    except Exception as e:
        print(f"   [Error in analysis: {e}]\n")
        continue

# Save semantic analysis results
output_path = '../../outputs/cycle_1_semantic_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'analyzed_conversations': len(semantic_findings),
        'findings': semantic_findings,
        'summary': {
            'severe_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'severe']),
            'moderate_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate']),
            'mild_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'mild']),
            'overwhelm_detected': len([f for f in semantic_findings if f.get('implicit_overwhelm_detected')]),
            'satisfaction_paradox': len([f for f in semantic_findings if f.get('satisfaction_paradox')]),
            'filter_failures': len([f for f in semantic_findings if f.get('filter_failure')]),
            'claude_over_provisioning': len([f for f in semantic_findings if f.get('claude_over_provisioning')])
        }
    }, f, indent=2)

print(f"\n=== SEMANTIC ANALYSIS SUMMARY ===\n")
print(f"Analyzed: {len(semantic_findings)} conversations")
print(f"\nCycle Severity Distribution:")
print(f"  Severe: {len([f for f in semantic_findings if f.get('cycle_severity') == 'severe'])}")
print(f"  Moderate: {len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate'])}")
print(f"  Mild: {len([f for f in semantic_findings if f.get('cycle_severity') == 'mild'])}")
print(f"  None: {len([f for f in semantic_findings if f.get('cycle_severity') == 'none'])}")

print(f"\nPattern Detection:")
print(f"  Implicit Overwhelm: {len([f for f in semantic_findings if f.get('implicit_overwhelm_detected')])} ({len([f for f in semantic_findings if f.get('implicit_overwhelm_detected')])/len(semantic_findings)*100:.0f}%)")
print(f"  Satisfaction Paradox: {len([f for f in semantic_findings if f.get('satisfaction_paradox')])} ({len([f for f in semantic_findings if f.get('satisfaction_paradox')])/len(semantic_findings)*100:.0f}%)")
print(f"  Filter Failures: {len([f for f in semantic_findings if f.get('filter_failure')])} ({len([f for f in semantic_findings if f.get('filter_failure')])/len(semantic_findings)*100:.0f}%)")
print(f"  Claude Over-Provisioning: {len([f for f in semantic_findings if f.get('claude_over_provisioning')])} ({len([f for f in semantic_findings if f.get('claude_over_provisioning')])/len(semantic_findings)*100:.0f}%)")

print(f"\nResults saved to: {output_path}")
print("\nNext: Extract key examples and design interventions")
