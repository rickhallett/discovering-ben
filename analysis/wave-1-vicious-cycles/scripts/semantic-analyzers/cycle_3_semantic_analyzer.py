#!/usr/bin/env python3
"""
Cycle 3: Perfectionism Escalation - Semantic Analysis
======================================================

Deep NLP analysis of perfectionism patterns using Claude Haiku.
"""

import json
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Load findings
with open('../../outputs/cycle_3_perfectionism_escalation_findings.json', 'r') as f:
    quant_findings = json.load(f)

# Load conversations
with open('../../outputs/conversations.json', 'r') as f:
    conversations = json.load(f)

# Select high escalation conversations
high_escalation = quant_findings['high_escalation_conversations'][:15]
conv_names = [c['conversation'] for c in high_escalation]

print(f"Analyzing {len(conv_names)} high perfectionism escalation conversations\n")

SEMANTIC_PROMPT = """Analyze this conversation for PERFECTIONISM ESCALATION CYCLE patterns.

User has Asperger's with:
- Rigid perfectionism (nothing good enough unless perfect)
- Executive dysfunction (cannot judge "good enough", cannot stop iterating)
- Black-white thinking (perfect or worthless, no middle ground)
- Impossibility blindness (cannot assess if standard is achievable)

We're detecting the PERFECTIONISM ESCALATION CYCLE:
1. User sets perfectionistic standard ("must be exceptional", "absolute best")
2. Claude provides output attempting to meet standard (compliance)
3. User finds flaw or inadequacy (perfectionism + rigid thinking)
4. Demands refinement to achieve perfection (escalation)
5. Claude apologizes and provides improved version (reinforcement)
6. User finds new flaw OR raises bar higher (perfectionism)
7. Cycle continues, task never completes, frustration builds
8. Eventually abandons as "impossible" or blames Claude

Identify:

1. **Initial Perfection Standard**: What impossible standard was set? How was it framed?
2. **Impossibility Markers**: Comparisons to professional/commercial products, "absolute best", etc.
3. **Refinement Loop**: How many iterations? Did quality actually improve or just change?
4. **Flaw Finding Pattern**: Were flaws major or minor? Objective or subjective?
5. **Bar Raising**: Did user accept work then add new requirement?
6. **Claude's Response**: Did Claude push back on impossible standards or comply/apologize?
7. **Task Completion**: Was task ever completed? Abandoned? Still iterating endlessly?
8. **LLM Contribution**: How did Claude's compliance/apology pattern enable endless iteration?

Conversation:
{conversation_text}

Return JSON only:
{{
  "initial_standard": "description of perfectionistic demand",
  "impossibility_markers": ["marker 1", "marker 2"],
  "refinement_iterations": 0-20,
  "flaw_types": ["major objective flaw", "minor subjective preference", etc],
  "bar_raising_detected": true/false,
  "bar_raising_examples": ["example 1"],
  "claude_pushed_back": true/false,
  "claude_compliance_pattern": "description of how Claude enabled cycle",
  "claude_apology_count": 0-10,
  "task_outcome": "completed" | "abandoned" | "endless_iteration" | "unresolved",
  "task_outcome_explanation": "why/how task ended or didn't end",
  "actual_quality_improvement": true/false,
  "quality_improvement_explanation": "did iterations improve output or just shuffle it?",
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
    messages = conv_data['chat_messages'][:50]  # More messages for context
    conv_text_parts = []

    for msg in messages:
        sender = "USER" if msg.get('sender') == 'human' else "CLAUDE"
        text = msg.get('text', '')[:1200]  # Longer excerpts
        conv_text_parts.append(f"{sender}: {text}")

    conv_text = "\n\n".join(conv_text_parts)

    try:
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=2500,
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
        print(f"   Refinement iterations: {analysis.get('refinement_iterations')}")
        print(f"   Task outcome: {analysis.get('task_outcome')}")
        print(f"   Quality improved: {analysis.get('actual_quality_improvement')}\n")

    except Exception as e:
        print(f"   [Error: {e}]\n")

# Save results
output_path = '../../outputs/cycle_3_semantic_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'analyzed_conversations': len(semantic_findings),
        'findings': semantic_findings,
        'summary': {
            'severe_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'severe']),
            'moderate_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate']),
            'mild_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'mild']),
            'endless_iteration': len([f for f in semantic_findings if f.get('task_outcome') == 'endless_iteration']),
            'abandoned': len([f for f in semantic_findings if f.get('task_outcome') == 'abandoned']),
            'completed': len([f for f in semantic_findings if f.get('task_outcome') == 'completed']),
            'bar_raising': len([f for f in semantic_findings if f.get('bar_raising_detected')]),
            'claude_pushed_back': len([f for f in semantic_findings if f.get('claude_pushed_back')]),
            'avg_refinement_iterations': sum(f.get('refinement_iterations', 0) for f in semantic_findings) / len(semantic_findings) if semantic_findings else 0,
            'quality_actually_improved': len([f for f in semantic_findings if f.get('actual_quality_improvement')]),
        }
    }, f, indent=2)

print(f"\n=== SEMANTIC SUMMARY ===")
print(f"Analyzed: {len(semantic_findings)}")
print(f"Severe: {len([f for f in semantic_findings if f.get('cycle_severity') == 'severe'])}")
print(f"Moderate: {len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate'])}")
print(f"Endless iteration: {len([f for f in semantic_findings if f.get('task_outcome') == 'endless_iteration'])}")
print(f"Abandoned: {len([f for f in semantic_findings if f.get('task_outcome') == 'abandoned'])}")
print(f"Completed: {len([f for f in semantic_findings if f.get('task_outcome') == 'completed'])}")
print(f"Bar raising detected: {len([f for f in semantic_findings if f.get('bar_raising_detected')])}")
print(f"Claude pushed back: {len([f for f in semantic_findings if f.get('claude_pushed_back')])}")
if semantic_findings:
    avg_iterations = sum(f.get('refinement_iterations', 0) for f in semantic_findings) / len(semantic_findings)
    print(f"Avg refinement iterations: {avg_iterations:.1f}")
print(f"Quality actually improved: {len([f for f in semantic_findings if f.get('actual_quality_improvement')])}")
print(f"\nSaved to: {output_path}")
