#!/usr/bin/env python3
"""
Cycle 3: Perfectionism Escalation - Pattern Detector
=====================================================

Hypothesis: Benjamin's autism-linked perfectionism (nothing good enough unless
perfect) creates impossible standards. LLM's compliance/iterative improvement
attempts reinforce belief that "perfect" is achievable, leading to endless
refinement cycles that never complete and escalating frustration.

Cycle Mechanism:
1. Benjamin sets perfectionistic standard ("must be exceptional", "perfect")
2. LLM provides output attempting to meet standard (compliance)
3. Benjamin finds minor flaw or inadequacy (rigid perfectionism)
4. Demands refinement to achieve perfection (escalation)
5. LLM apologizes and provides improved version (reinforcement)
6. Benjamin finds new flaw or raises bar higher (perfectionism)
7. Cycle continues, task never completes, frustration builds
8. Eventually abandons as "impossible" or blames LLM for failure

Detection Strategy:
- Perfection demands ("perfect", "exceptional", "flawless", "ultimate")
- "Not good enough" / inadequacy statements
- Minor flaw complaints after substantial work
- Iterative refinement requests (version 2, 3, 4...)
- Comparison to impossible standards ("as good as X professional product")
- Never satisfied markers
- Bar raising (accepting solution then adding new requirement)
- Abandonment after extensive refinement
"""

import json
import re
from collections import defaultdict

print("Loading conversations...")
with open('../../../../data/raw/conversations.json', 'r') as f:
    data = json.load(f)

# Detection patterns
PERFECTION_DEMAND_PATTERNS = [
    r'\bperfect\b',
    r'\bexceptional\b',
    r'\bflawless\b',
    r'\bimpeccable\b',
    r'\bultimate\b',
    r'\babsolute (best|top|highest|maximum)\b',
    r'\bworld[- ]class\b',
    r'\bprofessional[- ]grade\b',
    r'\bstate[- ]of[- ]the[- ]art\b',
    r'\btop[- ]tier\b',
    r'\belite\b',
    r'\bpremium quality\b',
    r'\bmust be (as good as|better than|match)\b',
    r'\bnothing (less|worse) than\b',
]

NOT_GOOD_ENOUGH_PATTERNS = [
    r'\bnot good enough\b',
    r'\bnot (quite|really) (right|there|it)\b',
    r'\b(still )?not (perfect|adequate|sufficient|acceptable)\b',
    r'\bcould be better\b',
    r'\bneeds (more|to be better|improvement|work)\b',
    r'\bnot (up to|meeting) (standard|expectations)\b',
    r'\bdisappoint(ed|ing)\b',
    r'\bsubstandard\b',
    r'\bsubpar\b',
    r'\bmediocre\b',
    r'\binadequate\b',
    r'\bunacceptable\b',
]

FLAW_FINDING_PATTERNS = [
    r'\bbut (it|this|that).{0,40}(wrong|error|mistake|problem|issue|flaw)\b',
    r'\b(however|though|yet).{0,40}(not|wrong|bad|poor)\b',
    r'\bexcept\b',
    r'\bone (problem|issue|flaw)\b',
    r'\bonly (problem|issue|thing)\b',
    r'\bsmall (mistake|error|problem|issue)\b',
    r'\bminor (mistake|error|problem|issue)\b',
    r'\btiny (mistake|error|problem|flaw)\b',
]

REFINEMENT_REQUEST_PATTERNS = [
    r'\b(try|do it|make it) again\b',
    r'\bre-?(write|do|make|create)\b',
    r'\bversion [2-9]\b',
    r'\banother (attempt|try|go|version)\b',
    r'\bstart (over|again|from scratch)\b',
    r'\bredo\b',
    r'\bimprove (it|this|that)\b',
    r'\bmake (it|this|that) better\b',
    r'\bfix (it|this|that)\b',
    r'\brefine\b',
    r'\bpolish\b',
    r'\btweak\b',
]

BAR_RAISING_PATTERNS = [
    r'\bok but (now|also)\b',
    r'\balso (make sure|add|include|do)\b',
    r'\bone more thing\b',
    r'\b(and|plus) (make sure|add|include)\b',
    r'\bwhile you\'?re at it\b',
    r'\bwhat about\b',
    r'\bdon\'?t forget\b',
]

COMPARISON_TO_IMPOSSIBLE_PATTERNS = [
    r'\b(as good as|better than|match|compete with) (microsoft|apple|google|professional)\b',
    r'\bmust (match|equal|exceed) (MSW|Word|professional)\b',
    r'\blike (a )?professional\b',
    r'\bprofessional[- ]level\b',
    r'\bcommercial[- ]grade\b',
]

NEVER_SATISFIED_MARKERS = [
    r'\bstill (not|need|want|missing)\b',
    r'\bbut (what about|where is|why not)\b',
    r'\byes but\b',
    r'\bok but\b',
    r'\bthat\'?s (fine|ok|good) but\b',
]

# Storage
findings = {
    'perfection_demands': [],
    'not_good_enough': [],
    'flaw_finding': [],
    'refinement_requests': [],
    'bar_raising': [],
    'impossible_comparisons': [],
    'never_satisfied': [],
    'conversations_with_patterns': []
}

total_conversations = 0
total_user_messages = 0
total_claude_messages = 0

print("\n=== ANALYZING FOR PERFECTIONISM ESCALATION CYCLE PATTERNS ===\n")

for conv in data:
    if not conv.get('chat_messages'):
        continue

    total_conversations += 1
    conv_name = conv.get('name', 'Unnamed')
    conv_date = conv.get('created_at', '')
    messages = conv['chat_messages']

    # Track conversation-level patterns
    conv_patterns = {
        'perfection_demands': 0,
        'not_good_enough': 0,
        'flaw_finding': 0,
        'refinement_requests': 0,
        'bar_raising': 0,
        'impossible_comparisons': 0,
        'never_satisfied': 0,
        'claude_apologies': 0,
        'claude_refinement_attempts': 0,
        'user_messages': [],
        'claude_messages': [],
        'task_completed': False,
        'task_abandoned': False,
        'refinement_cycles': 0
    }

    previous_msg_was_refinement = False

    for msg_idx, msg in enumerate(messages):
        text = msg.get('text', '')
        sender = msg.get('sender', '')

        if sender == 'human':
            total_user_messages += 1
            conv_patterns['user_messages'].append(text)

            # Perfection demands
            for pattern in PERFECTION_DEMAND_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['perfection_demands'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'text': text[:300]
                    })
                    conv_patterns['perfection_demands'] += 1
                    break

            # Not good enough
            for pattern in NOT_GOOD_ENOUGH_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['not_good_enough'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300]
                    })
                    conv_patterns['not_good_enough'] += 1
                    break

            # Flaw finding
            for pattern in FLAW_FINDING_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['flaw_finding'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['flaw_finding'] += 1
                    break

            # Refinement requests
            for pattern in REFINEMENT_REQUEST_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['refinement_requests'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300],
                        'after_not_good_enough': conv_patterns['not_good_enough'] > 0
                    })
                    conv_patterns['refinement_requests'] += 1
                    previous_msg_was_refinement = True
                    conv_patterns['refinement_cycles'] += 1
                    break

            # Bar raising
            for pattern in BAR_RAISING_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['bar_raising'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['bar_raising'] += 1
                    break

            # Impossible comparisons
            for pattern in COMPARISON_TO_IMPOSSIBLE_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['impossible_comparisons'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['impossible_comparisons'] += 1
                    break

            # Never satisfied
            for pattern in NEVER_SATISFIED_MARKERS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['never_satisfied'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['never_satisfied'] += 1
                    break

        elif sender == 'assistant':
            total_claude_messages += 1
            conv_patterns['claude_messages'].append(text)

            # Detect Claude's reinforcement patterns
            # Apologies after criticism
            if previous_msg_was_refinement or conv_patterns['not_good_enough'] > 0:
                apology_patterns = [
                    r'\bapologi[sz]e\b',
                    r'\bsorry\b',
                    r'\bmy (mistake|bad|fault)\b',
                    r'\blet me (fix|correct|improve)\b',
                ]
                for pattern in apology_patterns:
                    if re.search(pattern, text, re.IGNORECASE):
                        conv_patterns['claude_apologies'] += 1
                        break

            # Refinement attempts
            refinement_indicators = [
                r'\bhere\'?s an? (improved|better|refined|enhanced|updated)\b',
                r'\bi\'?ve (improved|enhanced|refined|updated|fixed)\b',
                r'\blet me (improve|enhance|refine|fix)\b',
                r'\bversion [2-9]\b',
            ]
            for indicator in refinement_indicators:
                if re.search(indicator, text, re.IGNORECASE):
                    conv_patterns['claude_refinement_attempts'] += 1
                    break

            previous_msg_was_refinement = False

    # Conversation-level analysis
    if conv_patterns['perfection_demands'] > 0 or \
       conv_patterns['not_good_enough'] > 0 or \
       conv_patterns['refinement_requests'] > 1:

        # Perfectionism escalation score
        escalation_score = 0

        # High perfection standards set
        if conv_patterns['perfection_demands'] > 0:
            escalation_score += 2

        # Impossible comparisons
        if conv_patterns['impossible_comparisons'] > 0:
            escalation_score += 3

        # Multiple "not good enough" statements
        if conv_patterns['not_good_enough'] > 1:
            escalation_score += 3

        # Multiple refinement cycles (indicates never-ending loop)
        if conv_patterns['refinement_cycles'] >= 3:
            escalation_score += 4
        elif conv_patterns['refinement_cycles'] >= 2:
            escalation_score += 2

        # Bar raising (accepting then adding more)
        if conv_patterns['bar_raising'] > 0:
            escalation_score += 2

        # Never satisfied pattern
        if conv_patterns['never_satisfied'] > 1:
            escalation_score += 2

        # Claude's reinforcement (apologizing/refining feeds cycle)
        if conv_patterns['claude_apologies'] > 0:
            escalation_score += 1

        # Check for task completion markers
        completion_markers = [r'\bthanks?\b', r'\bperfect\b', r'\bthat\'?s (it|great|good)\b', r'\bdone\b']
        for user_msg in conv_patterns['user_messages'][-3:]:  # Last 3 messages
            for marker in completion_markers:
                if re.search(marker, user_msg, re.IGNORECASE) and \
                   not re.search(r'\bbut\b', user_msg, re.IGNORECASE):
                    conv_patterns['task_completed'] = True
                    break

        # Check for abandonment markers
        abandonment_markers = [r'\bforget it\b', r'\bgive up\b', r'\bnever mind\b', r'\bimpossible\b']
        for user_msg in conv_patterns['user_messages']:
            for marker in abandonment_markers:
                if re.search(marker, user_msg, re.IGNORECASE):
                    conv_patterns['task_abandoned'] = True
                    break

        findings['conversations_with_patterns'].append({
            'conversation': conv_name,
            'date': conv_date,
            'perfection_demands': conv_patterns['perfection_demands'],
            'not_good_enough': conv_patterns['not_good_enough'],
            'flaw_finding': conv_patterns['flaw_finding'],
            'refinement_requests': conv_patterns['refinement_requests'],
            'bar_raising': conv_patterns['bar_raising'],
            'impossible_comparisons': conv_patterns['impossible_comparisons'],
            'never_satisfied': conv_patterns['never_satisfied'],
            'claude_apologies': conv_patterns['claude_apologies'],
            'claude_refinement_attempts': conv_patterns['claude_refinement_attempts'],
            'refinement_cycles': conv_patterns['refinement_cycles'],
            'escalation_score': escalation_score,
            'task_completed': conv_patterns['task_completed'],
            'task_abandoned': conv_patterns['task_abandoned'],
            'user_message_count': len(conv_patterns['user_messages']),
            'claude_message_count': len(conv_patterns['claude_messages'])
        })

print(f"Analyzed {total_conversations} conversations")
print(f"Total user messages: {total_user_messages}")
print(f"Total Claude messages: {total_claude_messages}")

# Statistics
print("\n=== QUANTITATIVE FINDINGS ===\n")

print(f"PERFECTION DEMANDS: {len(findings['perfection_demands'])}")
print(f"  - Rate: {len(findings['perfection_demands']) / total_user_messages * 100:.2f}% of user messages")
print(f"  - Conversations affected: {len(set(d['conversation'] for d in findings['perfection_demands']))}")

print(f"\n'NOT GOOD ENOUGH' STATEMENTS: {len(findings['not_good_enough'])}")
print(f"  - Rate: {len(findings['not_good_enough']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nFLAW FINDING: {len(findings['flaw_finding'])}")
print(f"  - Rate: {len(findings['flaw_finding']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nREFINEMENT REQUESTS: {len(findings['refinement_requests'])}")
print(f"  - Rate: {len(findings['refinement_requests']) / total_user_messages * 100:.2f}% of user messages")
after_critique = len([r for r in findings['refinement_requests'] if r.get('after_not_good_enough')])
print(f"  - After 'not good enough': {after_critique} ({after_critique/len(findings['refinement_requests'])*100:.1f}%)")

print(f"\nBAR RAISING: {len(findings['bar_raising'])}")
print(f"  - Rate: {len(findings['bar_raising']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nIMPOSSIBLE COMPARISONS: {len(findings['impossible_comparisons'])}")

print(f"\nNEVER SATISFIED MARKERS: {len(findings['never_satisfied'])}")

print(f"\nCONVERSATIONS WITH PERFECTIONISM PATTERNS: {len(findings['conversations_with_patterns'])}")
print(f"  - Percentage of total: {len(findings['conversations_with_patterns']) / total_conversations * 100:.1f}%")

# Escalation analysis
if findings['conversations_with_patterns']:
    avg_escalation = sum(c['escalation_score'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])
    high_escalation = len([c for c in findings['conversations_with_patterns'] if c['escalation_score'] >= 6])
    tasks_completed = len([c for c in findings['conversations_with_patterns'] if c['task_completed']])
    tasks_abandoned = len([c for c in findings['conversations_with_patterns'] if c['task_abandoned']])
    avg_refinement_cycles = sum(c['refinement_cycles'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])
    total_claude_apologies = sum(c['claude_apologies'] for c in findings['conversations_with_patterns'])
    total_refinement_attempts = sum(c['claude_refinement_attempts'] for c in findings['conversations_with_patterns'])

    print(f"\nPERFECTIONISM ESCALATION ANALYSIS:")
    print(f"  - Average escalation score: {avg_escalation:.2f}")
    print(f"  - High escalation (score ≥6): {high_escalation} ({high_escalation/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Average refinement cycles: {avg_refinement_cycles:.2f}")
    print(f"  - Tasks completed: {tasks_completed} ({tasks_completed/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Tasks abandoned: {tasks_abandoned} ({tasks_abandoned/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Tasks unresolved: {len(findings['conversations_with_patterns']) - tasks_completed - tasks_abandoned} ({(len(findings['conversations_with_patterns']) - tasks_completed - tasks_abandoned)/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Total Claude apologies: {total_claude_apologies}")
    print(f"  - Total Claude refinement attempts: {total_refinement_attempts}")

# Top examples
print("\n=== TOP PERFECTION DEMAND EXAMPLES ===\n")
for i, ex in enumerate(findings['perfection_demands'][:15], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== TOP 'NOT GOOD ENOUGH' EXAMPLES ===\n")
for i, ex in enumerate(findings['not_good_enough'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== TOP REFINEMENT REQUEST EXAMPLES ===\n")
for i, ex in enumerate(findings['refinement_requests'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   After critique: {ex.get('after_not_good_enough', False)}")
    print(f"   Text: {ex['text']}\n")

# High escalation conversations
print("\n=== HIGH PERFECTIONISM ESCALATION CONVERSATIONS ===\n")
high_escalation_convs = sorted(findings['conversations_with_patterns'],
                               key=lambda x: x['escalation_score'],
                               reverse=True)[:15]
for i, conv in enumerate(high_escalation_convs, 1):
    print(f"{i}. {conv['conversation']}")
    print(f"   Escalation score: {conv['escalation_score']}")
    print(f"   Refinement cycles: {conv['refinement_cycles']}")
    print(f"   Perfection demands: {conv['perfection_demands']}, Not good enough: {conv['not_good_enough']}")
    print(f"   Task completed: {conv['task_completed']}, Abandoned: {conv['task_abandoned']}\n")

# Save findings
output_path = '../../outputs/cycle_3_perfectionism_escalation_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'summary': {
            'total_conversations': total_conversations,
            'total_user_messages': total_user_messages,
            'perfection_demands_count': len(findings['perfection_demands']),
            'not_good_enough_count': len(findings['not_good_enough']),
            'flaw_finding_count': len(findings['flaw_finding']),
            'refinement_requests_count': len(findings['refinement_requests']),
            'bar_raising_count': len(findings['bar_raising']),
            'impossible_comparisons_count': len(findings['impossible_comparisons']),
            'conversations_affected': len(findings['conversations_with_patterns']),
            'avg_escalation_score': avg_escalation if findings['conversations_with_patterns'] else 0,
            'high_escalation_count': high_escalation if findings['conversations_with_patterns'] else 0,
            'avg_refinement_cycles': avg_refinement_cycles if findings['conversations_with_patterns'] else 0,
            'tasks_completed': tasks_completed if findings['conversations_with_patterns'] else 0,
            'tasks_abandoned': tasks_abandoned if findings['conversations_with_patterns'] else 0,
            'total_claude_apologies': total_claude_apologies if findings['conversations_with_patterns'] else 0,
            'total_refinement_attempts': total_refinement_attempts if findings['conversations_with_patterns'] else 0
        },
        'detailed_findings': findings,
        'high_escalation_conversations': high_escalation_convs[:20]
    }, f, indent=2)

print(f"\nDetailed findings saved to: {output_path}")
print("\nNext: Run semantic analysis on high escalation conversations")
