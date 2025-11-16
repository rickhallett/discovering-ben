#!/usr/bin/env python3
"""
Information Overload Cycle Detector
====================================

Hypothesis: Benjamin's uncertainty intolerance + LLM's detail provision creates
a cycle where he demands "everything", gets overwhelmed, feels unsatisfied,
demands more, leading to cognitive overload and increased frustration.

Cycle Mechanism:
1. Benjamin asks question (uncertainty intolerance)
2. LLM provides detailed answer (helpfulness optimization)
3. Benjamin can't filter relevant from irrelevant (executive dysfunction)
4. Feels overwhelmed but not satisfied (needs certainty)
5. Asks for "everything" or "comprehensive" information
6. LLM dumps even more information (compliance)
7. Cognitive overload increases
8. Benjamin frustrated at "not being clear enough"
9. Loop back with even more demanding request

Detection Strategy:
- Track "tell me everything" / "exhaustive" / "comprehensive" requests
- Measure Claude response length trends
- Identify complaints about clarity AFTER long responses
- Find re-asking of same questions
- Detect escalating information demands within conversations
- Measure cognitive overload markers (frustration, confusion after detail)
"""

import json
import re
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple, Any

# Load conversations
print("Loading conversations...")
with open('../../../../data/raw/conversations.json', 'r') as f:
    data = json.load(f)

# Detection patterns
EXHAUSTIVE_DEMAND_PATTERNS = [
    r'\btell me everything\b',
    r'\bevery single\b',
    r'\ball of (it|them|the)\b',
    r'\bexhaustive\b',
    r'\bcomprehensive\b',
    r'\bcomplete list\b',
    r'\bfull list\b',
    r'\ball.{0,20}detail',
    r'\bevery.{0,20}detail',
    r'\bdeep dive\b',
    r'\bgo into depth\b',
    r'\bcover everything\b',
    r'\bleave nothing out\b',
    r'\bdon\'t miss anything\b',
]

CLARITY_COMPLAINT_PATTERNS = [
    r'\bnot clear\b',
    r'\bconfusing\b',
    r'\bdon\'t understand\b',
    r'\bmake it clearer\b',
    r'\bsimplify\b',
    r'\btoo complicated\b',
    r'\btoo much\b',
    r'\boverwhelm',
    r'\bcan\'t follow\b',
    r'\blost me\b',
    r'\bwhat are you saying\b',
    r'\bmakes no sense\b',
]

REASKING_PATTERNS = [
    r'\basked (this|that) (already|before)\b',
    r'\bsame question\b',
    r'\bagain\b.*\?',
    r'\bstill (don\'t|dont) (know|understand)\b',
]

COGNITIVE_OVERLOAD_MARKERS = [
    r'\btoo much information\b',
    r'\bcan\'t process\b',
    r'\bhead (spinning|hurts)\b',
    r'\boverwhelm',
    r'\bconfused\b',
    r'\blost\b',
    r'\bdon\'t follow\b',
]

ESCALATING_DEMANDS = [
    r'\bmore detail\b',
    r'\bmore information\b',
    r'\bmore specific\b',
    r'\bbreak it down\b',
    r'\bexplain.{0,20}more\b',
    r'\bgo deeper\b',
    r'\belaborate\b',
]

# Storage for findings
findings = {
    'exhaustive_demands': [],
    'clarity_complaints': [],
    'reasking_instances': [],
    'cognitive_overload': [],
    'escalating_demands': [],
    'response_length_analysis': [],
    'conversation_cycles': [],
    'temporal_trends': defaultdict(list)
}

# Metrics
total_conversations = 0
total_user_messages = 0
total_claude_messages = 0

print("\n=== ANALYZING CONVERSATIONS FOR INFORMATION OVERLOAD PATTERNS ===\n")

for conv_idx, conv in enumerate(data):
    if not conv.get('chat_messages'):
        continue

    total_conversations += 1
    conv_name = conv.get('name', 'Unnamed')
    conv_date = conv.get('created_at', '')
    messages = conv['chat_messages']

    # Track within-conversation patterns
    user_messages = []
    claude_messages = []
    conversation_patterns = {
        'exhaustive_demands': 0,
        'clarity_complaints': 0,
        'claude_response_lengths': [],
        'escalation_detected': False,
        'overload_markers': 0
    }

    for msg_idx, msg in enumerate(messages):
        text = msg.get('text', '')
        sender = msg.get('sender', '')

        if sender == 'human':
            total_user_messages += 1
            user_messages.append((msg_idx, text))

            # Check for exhaustive demands
            for pattern in EXHAUSTIVE_DEMAND_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['exhaustive_demands'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'text': text[:300],
                        'previous_claude_response_length': len(claude_messages[-1][1]) if claude_messages else 0
                    })
                    conversation_patterns['exhaustive_demands'] += 1
                    break

            # Check for clarity complaints (especially after long Claude responses)
            for pattern in CLARITY_COMPLAINT_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    prev_claude_length = len(claude_messages[-1][1]) if claude_messages else 0
                    findings['clarity_complaints'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'text': text[:300],
                        'previous_claude_response_length': prev_claude_length
                    })
                    conversation_patterns['clarity_complaints'] += 1
                    break

            # Check for cognitive overload markers
            for pattern in COGNITIVE_OVERLOAD_MARKERS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['cognitive_overload'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'text': text[:300]
                    })
                    conversation_patterns['overload_markers'] += 1
                    break

            # Check for escalating demands
            for pattern in ESCALATING_DEMANDS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['escalating_demands'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'text': text[:300]
                    })
                    if len(user_messages) > 2:  # Escalation requires history
                        conversation_patterns['escalation_detected'] = True
                    break

        elif sender == 'assistant':
            total_claude_messages += 1
            claude_messages.append((msg_idx, text))
            response_length = len(text)
            conversation_patterns['claude_response_lengths'].append(response_length)

            # Track response lengths over time
            findings['response_length_analysis'].append({
                'conversation': conv_name,
                'date': conv_date,
                'message_index': msg_idx,
                'length': response_length,
                'word_count': len(text.split())
            })

    # Analyze conversation-level patterns
    if conversation_patterns['exhaustive_demands'] > 0 or \
       conversation_patterns['clarity_complaints'] > 0 or \
       conversation_patterns['overload_markers'] > 0:

        avg_claude_length = sum(conversation_patterns['claude_response_lengths']) / len(conversation_patterns['claude_response_lengths']) if conversation_patterns['claude_response_lengths'] else 0

        findings['conversation_cycles'].append({
            'conversation': conv_name,
            'date': conv_date,
            'exhaustive_demands': conversation_patterns['exhaustive_demands'],
            'clarity_complaints': conversation_patterns['clarity_complaints'],
            'overload_markers': conversation_patterns['overload_markers'],
            'escalation_detected': conversation_patterns['escalation_detected'],
            'avg_claude_response_length': avg_claude_length,
            'max_claude_response_length': max(conversation_patterns['claude_response_lengths']) if conversation_patterns['claude_response_lengths'] else 0,
            'user_message_count': len(user_messages),
            'claude_message_count': len(claude_messages)
        })

        # Track temporal trends
        if conv_date:
            date_key = conv_date[:10]  # YYYY-MM-DD
            findings['temporal_trends'][date_key].append({
                'conversation': conv_name,
                'exhaustive_demands': conversation_patterns['exhaustive_demands'],
                'avg_response_length': avg_claude_length
            })

print(f"Analyzed {total_conversations} conversations")
print(f"Total user messages: {total_user_messages}")
print(f"Total Claude messages: {total_claude_messages}")

# Calculate statistics
print("\n=== QUANTITATIVE FINDINGS ===\n")

print(f"EXHAUSTIVE DEMAND INSTANCES: {len(findings['exhaustive_demands'])}")
print(f"  - Rate: {len(findings['exhaustive_demands']) / total_user_messages * 100:.2f}% of user messages")
print(f"  - Conversations affected: {len(set(e['conversation'] for e in findings['exhaustive_demands']))}")

print(f"\nCLARITY COMPLAINTS: {len(findings['clarity_complaints'])}")
print(f"  - Rate: {len(findings['clarity_complaints']) / total_user_messages * 100:.2f}% of user messages")
# Calculate how many clarity complaints follow long responses
long_response_threshold = 2000  # characters
clarity_after_long = [c for c in findings['clarity_complaints'] if c['previous_claude_response_length'] > long_response_threshold]
print(f"  - After long Claude responses (>{long_response_threshold} chars): {len(clarity_after_long)} ({len(clarity_after_long)/len(findings['clarity_complaints'])*100:.1f}%)")

print(f"\nCOGNITIVE OVERLOAD MARKERS: {len(findings['cognitive_overload'])}")
print(f"  - Rate: {len(findings['cognitive_overload']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nESCALATING DEMANDS: {len(findings['escalating_demands'])}")
print(f"  - Rate: {len(findings['escalating_demands']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nCONVERSATIONS WITH OVERLOAD PATTERNS: {len(findings['conversation_cycles'])}")
print(f"  - Percentage of total: {len(findings['conversation_cycles']) / total_conversations * 100:.1f}%")

# Response length analysis
all_lengths = [r['length'] for r in findings['response_length_analysis']]
if all_lengths:
    avg_length = sum(all_lengths) / len(all_lengths)
    max_length = max(all_lengths)
    print(f"\nCLAUDE RESPONSE LENGTH STATISTICS:")
    print(f"  - Average: {avg_length:.0f} characters")
    print(f"  - Maximum: {max_length} characters")
    print(f"  - Responses >2000 chars: {len([l for l in all_lengths if l > 2000])} ({len([l for l in all_lengths if l > 2000])/len(all_lengths)*100:.1f}%)")
    print(f"  - Responses >5000 chars: {len([l for l in all_lengths if l > 5000])} ({len([l for l in all_lengths if l > 5000])/len(all_lengths)*100:.1f}%)")

# Top examples
print("\n=== TOP EXHAUSTIVE DEMAND EXAMPLES ===\n")
for i, example in enumerate(findings['exhaustive_demands'][:10], 1):
    print(f"{i}. Conversation: {example['conversation']}")
    print(f"   Pattern: {example['pattern']}")
    print(f"   Text: {example['text']}\n")

print("\n=== TOP CLARITY COMPLAINT EXAMPLES (after long responses) ===\n")
clarity_sorted = sorted(findings['clarity_complaints'], key=lambda x: x['previous_claude_response_length'], reverse=True)
for i, example in enumerate(clarity_sorted[:10], 1):
    print(f"{i}. Conversation: {example['conversation']}")
    print(f"   Previous Claude response: {example['previous_claude_response_length']} chars")
    print(f"   Text: {example['text']}\n")

# Save detailed findings
output_path = '../../outputs/cycle_1_information_overload_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'summary': {
            'total_conversations': total_conversations,
            'total_user_messages': total_user_messages,
            'total_claude_messages': total_claude_messages,
            'exhaustive_demands_count': len(findings['exhaustive_demands']),
            'clarity_complaints_count': len(findings['clarity_complaints']),
            'cognitive_overload_count': len(findings['cognitive_overload']),
            'escalating_demands_count': len(findings['escalating_demands']),
            'conversations_with_patterns': len(findings['conversation_cycles']),
            'avg_claude_response_length': avg_length if all_lengths else 0,
            'max_claude_response_length': max_length if all_lengths else 0
        },
        'detailed_findings': findings,
        'conversation_level_analysis': findings['conversation_cycles']
    }, f, indent=2)

print(f"\nDetailed findings saved to: {output_path}")
print("\nNext step: Run LLM-assisted semantic analysis for nuanced patterns")
