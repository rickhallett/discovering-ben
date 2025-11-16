#!/usr/bin/env python3
"""
Cycle 5: Mind Reading Assumption - Semantic Analysis
====================================================

Deep NLP analysis of mind reading assumption patterns using Claude Haiku.
"""

import json
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Load findings
with open('../../outputs/cycle_5_mind_reading_findings.json', 'r') as f:
    quant_findings = json.load(f)

# Load conversations
with open('../../outputs/conversations.json', 'r') as f:
    conversations = json.load(f)

# Select high mind reading conversations
high_mind_reading = quant_findings['high_mind_reading_conversations'][:15]
conv_names = [c['conversation'] for c in high_mind_reading]

print(f"Analyzing {len(conv_names)} high mind reading assumption conversations\n")

SEMANTIC_PROMPT = """Analyze this conversation for MIND READING ASSUMPTION patterns.

User has autism with theory of mind deficit - cannot model that others don't know what he knows.
This causes him to assume LLM can read his mind or knows unstated context.

We're detecting the MIND READING CYCLE:
1. User makes reference to unstated context ("it", "that one", "you know")
2. LLM doesn't have enough information
3. LLM asks clarifying question OR makes educated guess
4. User may get frustrated ("you should know!") OR provides context OR ignores
5. If LLM apologizes for "confusion", it frames issue as LLM failure
6. User learns: LLM SHOULD know, failures are LLM's fault
7. Pattern reinforced: User provides even less context next time

Identify:

1. **Vague References**: Examples of user referencing unstated context
2. **Assumed Shared Knowledge**: Does user assume LLM knows his situation/history?
3. **Claude's Response**: Ask for clarification? Guess? Apologize?
4. **User's Reaction**: Provide context? Get frustrated? Ignore?
5. **Context Ever Provided**: Did user eventually give needed information?
6. **Apology Pattern**: Did Claude apologize for "not understanding"?
7. **Reinforcement**: Did apology frame issue as Claude's failure vs missing info?
8. **LLM Contribution**: How did Claude's pattern enable/mitigate the cycle?

Conversation:
{conversation_text}

Return JSON only:
{{
  "vague_references_examples": ["example 1", "example 2"],
  "assumed_shared_knowledge": true/false,
  "assumed_knowledge_examples": ["example 1"],
  "claude_response_pattern": "clarification_request" | "educated_guess" | "apology" | "mixed",
  "claude_response_examples": ["example 1", "example 2"],
  "user_reaction": "provided_context" | "frustrated" | "ignored" | "mixed",
  "user_reaction_examples": ["example 1"],
  "context_eventually_provided": true/false,
  "context_provision_explanation": "how/when/if context was given",
  "apology_for_confusion": true/false,
  "apology_examples": ["example 1"],
  "reinforcement_mechanism": "description of how pattern was reinforced or not",
  "task_completion_impact": true/false,
  "task_completion_explanation": "did vagueness prevent task completion?",
  "llm_contribution_pattern": "description of Claude's role in cycle",
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
    messages = conv_data['chat_messages'][:50]
    conv_text_parts = []

    for msg in messages:
        sender = "USER" if msg.get('sender') == 'human' else "CLAUDE"
        text = msg.get('text', '')[:1200]
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
        print(f"   Assumed knowledge: {analysis.get('assumed_shared_knowledge')}")
        print(f"   Context provided: {analysis.get('context_eventually_provided')}")
        print(f"   Apology: {analysis.get('apology_for_confusion')}\n")

    except Exception as e:
        print(f"   [Error: {e}]\n")

# Save results
output_path = '../../outputs/cycle_5_semantic_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'analyzed_conversations': len(semantic_findings),
        'findings': semantic_findings,
        'summary': {
            'severe_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'severe']),
            'moderate_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate']),
            'mild_cycles': len([f for f in semantic_findings if f.get('cycle_severity') == 'mild']),
            'assumed_shared_knowledge': len([f for f in semantic_findings if f.get('assumed_shared_knowledge')]),
            'context_provided': len([f for f in semantic_findings if f.get('context_eventually_provided')]),
            'apologies_for_confusion': len([f for f in semantic_findings if f.get('apology_for_confusion')]),
            'task_prevented': len([f for f in semantic_findings if f.get('task_completion_impact')]),
        }
    }, f, indent=2)

print(f"\n=== SEMANTIC SUMMARY ===")
print(f"Analyzed: {len(semantic_findings)}")
print(f"Severe: {len([f for f in semantic_findings if f.get('cycle_severity') == 'severe'])}")
print(f"Moderate: {len([f for f in semantic_findings if f.get('cycle_severity') == 'moderate'])}")
print(f"Mild: {len([f for f in semantic_findings if f.get('cycle_severity') == 'mild'])}")
print(f"Assumed shared knowledge: {len([f for f in semantic_findings if f.get('assumed_shared_knowledge')])}")
print(f"Context eventually provided: {len([f for f in semantic_findings if f.get('context_eventually_provided')])}")
print(f"Apologies for confusion: {len([f for f in semantic_findings if f.get('apology_for_confusion')])}")
print(f"Task prevented: {len([f for f in semantic_findings if f.get('task_completion_impact')])}")
print(f"\nSaved to: {output_path}")
