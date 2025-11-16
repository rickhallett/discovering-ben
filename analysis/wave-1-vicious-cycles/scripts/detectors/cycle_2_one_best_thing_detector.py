#!/usr/bin/env python3
"""
Cycle 2: Finding the ONE Best Thing - Pattern Detector
========================================================

Hypothesis: Benjamin's rigid/black-white thinking creates demand for single
"best" option, but LLM's helpfulness provides nuanced comparisons with trade-offs.
This creates decision paralysis, escalating frustration, and demands for binary
certainty in non-binary domains.

Cycle Mechanism:
1. Benjamin asks "which is best?" (rigid thinking)
2. LLM provides balanced comparison of 2-5 options (helpfulness)
3. Benjamin cannot choose due to executive dysfunction + binary thinking
4. Demands "just tell me THE best one" (escalation)
5. LLM provides more nuanced analysis (more helpfulness)
6. Decision paralysis worsens (more executive dysfunction)
7. Benjamin gets frustrated, demands absolute binary answer
8. Loop continues, decision never made

Detection Strategy:
- "Which is best?" / "the best" / "which one should I" demands
- Multiple options provided by Claude
- Rejection of nuanced comparisons
- "Just tell me" demands after comparison
- Decision abandonment patterns
- Escalating frustration with trade-offs
- Binary thinking markers ("just X or Y", "which one")
"""

import json
import re
from collections import defaultdict
from datetime import datetime

print("Loading conversations...")
with open('../../../../data/raw/conversations.json', 'r') as f:
    data = json.load(f)

# Detection patterns
BEST_DEMAND_PATTERNS = [
    r'\bwhich is (the )?best\b',
    r'\bwhat\'?s (the )?best\b',
    r'\bthe best\b',
    r'\bbest (one|option|choice|product|solution)\b',
    r'\bwhich (one|option) (is|should)\b',
    r'\btop (choice|option|pick|recommendation)\b',
    r'\babsolute best\b',
    r'\bultimate (choice|option|solution)\b',
    r'\bperfect (choice|option|one)\b',
    r'\bwhich should I (buy|get|choose|pick)\b',
    r'\btell me which\b',
]

JUST_TELL_ME_PATTERNS = [
    r'\bjust tell me\b',
    r'\bjust (say|pick|choose)\b',
    r'\bsimply tell\b',
    r'\bgive me (a|one) (answer|option|choice)\b',
    r'\bstop.{0,30}(comparing|listing|giving|showing)',
    r'\bi don\'?t (care|want).{0,30}(options|choices|comparisons)',
    r'\bpick one\b',
    r'\bchoose for me\b',
    r'\bdecide for me\b',
    r'\bmake the decision\b',
]

BINARY_THINKING_MARKERS = [
    r'\bjust (yes|no)\b',
    r'\b(x|y) or (y|z)\b',
    r'\bwhich of (these )?two\b',
    r'\beither.{0,30}or\b',
    r'\bone or the other\b',
    r'\bsimple answer\b',
    r'\bstraight answer\b',
    r'\bblack (and|or) white\b',
]

OPTION_REJECTION_PATTERNS = [
    r'\bdon\'?t (give|show|tell).{0,30}(options|choices|multiple)\b',
    r'\bstop (giving|showing|listing).{0,30}(options|choices)\b',
    r'\btoo many (options|choices)\b',
    r'\bwhich (one|option)\??\s*$',  # Question ending with "which one?"
    r'\bconfusing\b',
    r'\bcan\'?t (decide|choose)\b',
    r'\bhelp me (decide|choose)\b',
]

ESCALATION_MARKERS = [
    r'\bfor (the )?love of (god|christ)\b',
    r'\bfor fuck\'?s? sake\b',
    r'\bjust.{0,20}already\b',
    r'\bstop (this|being)\b',
    r'\benough\b',
    r'\blast (time|chance)\b',
]

# Storage
findings = {
    'best_demands': [],
    'just_tell_me': [],
    'binary_thinking': [],
    'option_rejection': [],
    'escalation_markers': [],
    'conversations_with_patterns': [],
    'decision_paralysis_indicators': []
}

total_conversations = 0
total_user_messages = 0
total_claude_messages = 0

print("\n=== ANALYZING FOR 'ONE BEST THING' CYCLE PATTERNS ===\n")

for conv in data:
    if not conv.get('chat_messages'):
        continue

    total_conversations += 1
    conv_name = conv.get('name', 'Unnamed')
    conv_date = conv.get('created_at', '')
    messages = conv['chat_messages']

    # Track conversation-level patterns
    conv_patterns = {
        'best_demands': 0,
        'just_tell_me': 0,
        'binary_thinking': 0,
        'option_rejection': 0,
        'escalation': 0,
        'claude_provided_options': 0,
        'user_messages': [],
        'claude_messages': [],
        'decision_made': False,
        'abandoned': False
    }

    for msg_idx, msg in enumerate(messages):
        text = msg.get('text', '')
        sender = msg.get('sender', '')

        if sender == 'human':
            total_user_messages += 1
            conv_patterns['user_messages'].append(text)

            # Best demands
            for pattern in BEST_DEMAND_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['best_demands'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'text': text[:300]
                    })
                    conv_patterns['best_demands'] += 1
                    break

            # "Just tell me" escalation
            for pattern in JUST_TELL_ME_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['just_tell_me'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'text': text[:300],
                        'after_best_demand': conv_patterns['best_demands'] > 0
                    })
                    conv_patterns['just_tell_me'] += 1
                    break

            # Binary thinking
            for pattern in BINARY_THINKING_MARKERS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['binary_thinking'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['binary_thinking'] += 1
                    break

            # Option rejection
            for pattern in OPTION_REJECTION_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['option_rejection'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['option_rejection'] += 1
                    break

            # Escalation
            for pattern in ESCALATION_MARKERS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['escalation_markers'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['escalation'] += 1
                    break

        elif sender == 'assistant':
            total_claude_messages += 1
            conv_patterns['claude_messages'].append(text)

            # Detect if Claude provided multiple options
            # Look for numbered lists, bullet points, "or", comparison structures
            option_indicators = [
                r'\n\s*[1-9]\.',  # Numbered lists
                r'\n\s*[-*•]',    # Bullet points
                r'\b(option|choice|alternative)\s+[1-9]\b',
                r'\bversus\b',
                r'\bcompared to\b',
                r'\btrade-?offs?\b',
                r'\bpros? and cons?\b',
                r'\bon the other hand\b',
                r'\balternatively\b',
            ]

            for indicator in option_indicators:
                if re.search(indicator, text, re.IGNORECASE):
                    conv_patterns['claude_provided_options'] += 1
                    break

    # Conversation-level analysis
    if conv_patterns['best_demands'] > 0 or \
       conv_patterns['just_tell_me'] > 0 or \
       conv_patterns['option_rejection'] > 0:

        # Decision paralysis indicators
        paralysis_score = 0

        # Multiple best demands = repeated asking
        if conv_patterns['best_demands'] > 1:
            paralysis_score += 2

        # "Just tell me" after options provided = can't decide
        if conv_patterns['just_tell_me'] > 0 and conv_patterns['claude_provided_options'] > 0:
            paralysis_score += 3

        # Option rejection = overwhelmed by choices
        if conv_patterns['option_rejection'] > 0:
            paralysis_score += 2

        # Escalation = frustration building
        if conv_patterns['escalation'] > 0:
            paralysis_score += 1

        # Check if decision was made (hard to detect, look for "ordered", "bought", "chose")
        decision_markers = [r'\bordered\b', r'\bbought\b', r'\bchose\b', r'\bdecided\b', r'\bgoing with\b']
        for user_msg in conv_patterns['user_messages']:
            for marker in decision_markers:
                if re.search(marker, user_msg, re.IGNORECASE):
                    conv_patterns['decision_made'] = True
                    break

        findings['conversations_with_patterns'].append({
            'conversation': conv_name,
            'date': conv_date,
            'best_demands': conv_patterns['best_demands'],
            'just_tell_me': conv_patterns['just_tell_me'],
            'binary_thinking': conv_patterns['binary_thinking'],
            'option_rejection': conv_patterns['option_rejection'],
            'escalation': conv_patterns['escalation'],
            'claude_provided_options': conv_patterns['claude_provided_options'],
            'paralysis_score': paralysis_score,
            'decision_made': conv_patterns['decision_made'],
            'user_message_count': len(conv_patterns['user_messages']),
            'claude_message_count': len(conv_patterns['claude_messages'])
        })

print(f"Analyzed {total_conversations} conversations")
print(f"Total user messages: {total_user_messages}")
print(f"Total Claude messages: {total_claude_messages}")

# Statistics
print("\n=== QUANTITATIVE FINDINGS ===\n")

print(f"'BEST' DEMANDS: {len(findings['best_demands'])}")
print(f"  - Rate: {len(findings['best_demands']) / total_user_messages * 100:.2f}% of user messages")
print(f"  - Conversations affected: {len(set(d['conversation'] for d in findings['best_demands']))}")

print(f"\n'JUST TELL ME' ESCALATIONS: {len(findings['just_tell_me'])}")
print(f"  - Rate: {len(findings['just_tell_me']) / total_user_messages * 100:.2f}% of user messages")
after_best = len([j for j in findings['just_tell_me'] if j.get('after_best_demand')])
print(f"  - After 'best' demand: {after_best} ({after_best/len(findings['just_tell_me'])*100:.1f}%)")

print(f"\nBINARY THINKING MARKERS: {len(findings['binary_thinking'])}")
print(f"  - Rate: {len(findings['binary_thinking']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nOPTION REJECTION: {len(findings['option_rejection'])}")
print(f"  - Rate: {len(findings['option_rejection']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nESCALATION MARKERS: {len(findings['escalation_markers'])}")

print(f"\nCONVERSATIONS WITH DECISION PATTERNS: {len(findings['conversations_with_patterns'])}")
print(f"  - Percentage of total: {len(findings['conversations_with_patterns']) / total_conversations * 100:.1f}%")

# Paralysis analysis
if findings['conversations_with_patterns']:
    avg_paralysis = sum(c['paralysis_score'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])
    high_paralysis = len([c for c in findings['conversations_with_patterns'] if c['paralysis_score'] >= 5])
    decisions_made = len([c for c in findings['conversations_with_patterns'] if c['decision_made']])

    print(f"\nDECISION PARALYSIS ANALYSIS:")
    print(f"  - Average paralysis score: {avg_paralysis:.2f}")
    print(f"  - High paralysis (score ≥5): {high_paralysis} ({high_paralysis/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Decisions actually made: {decisions_made} ({decisions_made/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Abandoned/unresolved: {len(findings['conversations_with_patterns']) - decisions_made} ({(len(findings['conversations_with_patterns']) - decisions_made)/len(findings['conversations_with_patterns'])*100:.1f}%)")

# Top examples
print("\n=== TOP 'BEST' DEMAND EXAMPLES ===\n")
for i, ex in enumerate(findings['best_demands'][:15], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== TOP 'JUST TELL ME' ESCALATION EXAMPLES ===\n")
for i, ex in enumerate(findings['just_tell_me'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   After best demand: {ex.get('after_best_demand', False)}")
    print(f"   Text: {ex['text']}\n")

# High paralysis conversations
print("\n=== HIGH DECISION PARALYSIS CONVERSATIONS ===\n")
high_paralysis_convs = sorted(findings['conversations_with_patterns'],
                             key=lambda x: x['paralysis_score'],
                             reverse=True)[:10]
for i, conv in enumerate(high_paralysis_convs, 1):
    print(f"{i}. {conv['conversation']}")
    print(f"   Paralysis score: {conv['paralysis_score']}")
    print(f"   Best demands: {conv['best_demands']}, Just tell me: {conv['just_tell_me']}")
    print(f"   Decision made: {conv['decision_made']}\n")

# Save findings
output_path = '../../outputs/cycle_2_one_best_thing_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'summary': {
            'total_conversations': total_conversations,
            'total_user_messages': total_user_messages,
            'best_demands_count': len(findings['best_demands']),
            'just_tell_me_count': len(findings['just_tell_me']),
            'binary_thinking_count': len(findings['binary_thinking']),
            'option_rejection_count': len(findings['option_rejection']),
            'conversations_affected': len(findings['conversations_with_patterns']),
            'avg_paralysis_score': avg_paralysis if findings['conversations_with_patterns'] else 0,
            'high_paralysis_count': high_paralysis if findings['conversations_with_patterns'] else 0,
            'decisions_made': decisions_made if findings['conversations_with_patterns'] else 0
        },
        'detailed_findings': findings,
        'high_paralysis_conversations': high_paralysis_convs[:20]
    }, f, indent=2)

print(f"\nDetailed findings saved to: {output_path}")
print("\nNext: Run semantic analysis on high paralysis conversations")
