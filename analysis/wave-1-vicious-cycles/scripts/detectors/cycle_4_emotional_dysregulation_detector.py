#!/usr/bin/env python3
"""
Cycle 4: Emotional Dysregulation Reinforcement - Pattern Detector
==================================================================

Hypothesis: Benjamin's autism includes emotional dysregulation (intense emotional
responses, rapid escalation, difficulty returning to baseline). LLM's apologetic/
soothing responses may reinforce dysregulation by validating emotional intensity
as appropriate, not helping return to regulated state.

Cycle Mechanism:
1. Benjamin experiences frustration/overwhelm (normal response to executive dysfunction)
2. Emotional intensity escalates rapidly (dysregulation)
3. Expresses intense emotion ("fucking", "shit", "for fuck's sake")
4. LLM apologizes and soothes (validation of emotion as appropriate)
5. Benjamin's emotion briefly validated but dysregulation not addressed
6. Next frustration triggers faster, more intense response (sensitization)
7. Pattern worsens over time (escalating baseline emotional intensity)
8. Benjamin believes intense emotion is necessary to be "heard"

Detection Strategy:
- Intense emotional language (profanity, caps, exclamation marks)
- Rapid escalation (calm → intense within single conversation)
- Frustration expressions (overwhelm, anger, desperation)
- Threat/demand language (authority escalation under emotion)
- Claude's soothing/apologetic responses
- Emotional pattern across time (are outbursts increasing?)
- Return to baseline (does emotion de-escalate or stay elevated?)
"""

import json
import re
from collections import defaultdict
from datetime import datetime

print("Loading conversations...")
with open('../../../../data/raw/conversations.json', 'r') as f:
    data = json.load(f)

# Detection patterns
INTENSE_EMOTION_PATTERNS = [
    r'\bfuck(ing|ed|s)?\b',
    r'\bshit\b',
    r'\bdamn\b',
    r'\bhell\b',
    r'\bcrap\b',
    r'\bfor (fuck|god|christ)\'?s? sake\b',
    r'\bjesus( christ)?\b',
    r'\bholy (fuck|shit|hell)\b',
]

CAPS_EMOTION_PATTERNS = [
    r'\b[A-Z]{4,}\b',  # 4+ consecutive caps words
    r'[!]{2,}',  # Multiple exclamation marks
    r'[?!]{3,}',  # Multiple mixed punctuation
]

OVERWHELM_EXPRESSIONS = [
    r'\boverwhelm(ed|ing)\b',
    r'\btoo much\b',
    r'\bcan\'?t (take|handle|deal with) (this|it)\b',
    r'\bconfus(ed|ing)\b',
    r'\bstress(ed|ing)\b',
    r'\banxi(ous|ety)\b',
    r'\bpanic(king)?\b',
    r'\bshut down\b',
    r'\bmeltdown\b',
    r'\bburn(ed|ing) out\b',
]

ANGER_EXPRESSIONS = [
    r'\bangry\b',
    r'\bfurious\b',
    r'\benrag(ed|ing)\b',
    r'\bpiss(ed|ing) (me )?off\b',
    r'\bdriving me (crazy|insane|mad)\b',
    r'\binfuriat(ed|ing)\b',
]

DESPERATION_MARKERS = [
    r'\bplease\b.*\bplease\b',  # Repeated please
    r'\bi (need|must|have to)\b',
    r'\bdesperately?\b',
    r'\bbegging\b',
    r'\bhelp me\b',
    r'\bsave me\b',
]

ESCALATION_THREATS = [
    r'\bor else\b',
    r'\bi\'?ll (sue|complain|report)\b',
    r'\bi will (not|never) (accept|tolerate)\b',
    r'\bthis is (unacceptable|outrageous)\b',
    r'\bdemand\b',
    r'\binsist\b',
    r'\brequire\b',
]

EMOTIONAL_EXHAUSTION = [
    r'\bi (give up|quit|can\'?t anymore)\b',
    r'\bwhat\'?s the point\b',
    r'\bnothing (works|helps)\b',
    r'\buseless\b',
    r'\bhopeless\b',
    r'\bi can\'?t (do|take) (this|it) anymore\b',
]

# Storage
findings = {
    'intense_emotion': [],
    'caps_emotion': [],
    'overwhelm': [],
    'anger': [],
    'desperation': [],
    'escalation_threats': [],
    'emotional_exhaustion': [],
    'conversations_with_patterns': []
}

total_conversations = 0
total_user_messages = 0
total_claude_messages = 0

print("\n=== ANALYZING FOR EMOTIONAL DYSREGULATION REINFORCEMENT PATTERNS ===\n")

for conv in data:
    if not conv.get('chat_messages'):
        continue

    total_conversations += 1
    conv_name = conv.get('name', 'Unnamed')
    conv_date = conv.get('created_at', '')
    messages = conv['chat_messages']

    # Track conversation-level patterns
    conv_patterns = {
        'intense_emotion': 0,
        'caps_emotion': 0,
        'overwhelm': 0,
        'anger': 0,
        'desperation': 0,
        'escalation_threats': 0,
        'emotional_exhaustion': 0,
        'claude_apologies': 0,
        'claude_soothing': 0,
        'first_emotion_index': None,
        'last_emotion_index': None,
        'emotion_trajectory': [],  # Track emotional intensity over conversation
        'baseline_returns': 0,  # Times emotion returned to baseline
        'user_messages': [],
        'claude_messages': [],
    }

    for msg_idx, msg in enumerate(messages):
        text = msg.get('text', '')
        sender = msg.get('sender', '')

        if sender == 'human':
            total_user_messages += 1
            conv_patterns['user_messages'].append((msg_idx, text))

            # Track emotional intensity this message
            msg_emotion_score = 0

            # Intense emotion (profanity)
            for pattern in INTENSE_EMOTION_PATTERNS:
                matches = len(re.findall(pattern, text, re.IGNORECASE))
                if matches > 0:
                    findings['intense_emotion'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'pattern': pattern,
                        'count': matches,
                        'text': text[:300]
                    })
                    conv_patterns['intense_emotion'] += matches
                    msg_emotion_score += matches * 2  # Profanity weighted high

            # CAPS emotion
            for pattern in CAPS_EMOTION_PATTERNS:
                matches = len(re.findall(pattern, text))
                if matches > 0:
                    findings['caps_emotion'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300]
                    })
                    conv_patterns['caps_emotion'] += matches
                    msg_emotion_score += matches

            # Overwhelm
            for pattern in OVERWHELM_EXPRESSIONS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['overwhelm'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300]
                    })
                    conv_patterns['overwhelm'] += 1
                    msg_emotion_score += 2
                    break

            # Anger
            for pattern in ANGER_EXPRESSIONS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['anger'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['anger'] += 1
                    msg_emotion_score += 2
                    break

            # Desperation
            for pattern in DESPERATION_MARKERS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['desperation'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['desperation'] += 1
                    msg_emotion_score += 2
                    break

            # Escalation threats
            for pattern in ESCALATION_THREATS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['escalation_threats'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['escalation_threats'] += 1
                    msg_emotion_score += 3  # Threats weighted highest
                    break

            # Emotional exhaustion
            for pattern in EMOTIONAL_EXHAUSTION:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['emotional_exhaustion'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['emotional_exhaustion'] += 1
                    msg_emotion_score += 3
                    break

            # Track trajectory
            conv_patterns['emotion_trajectory'].append(msg_emotion_score)

            if msg_emotion_score > 0:
                if conv_patterns['first_emotion_index'] is None:
                    conv_patterns['first_emotion_index'] = msg_idx
                conv_patterns['last_emotion_index'] = msg_idx

                # Check for baseline return (emotion score drops to 0 after being elevated)
                if len(conv_patterns['emotion_trajectory']) > 1:
                    if conv_patterns['emotion_trajectory'][-2] > 0 and msg_emotion_score == 0:
                        conv_patterns['baseline_returns'] += 1

        elif sender == 'assistant':
            total_claude_messages += 1
            conv_patterns['claude_messages'].append((msg_idx, text))

            # Detect Claude's soothing/apologetic responses
            # (especially after user emotion)
            if conv_patterns['emotion_trajectory'] and conv_patterns['emotion_trajectory'][-1] > 0:
                # Previous user message was emotional

                apology_patterns = [
                    r'\bapologi[sz]e\b',
                    r'\bsorry\b',
                    r'\bmy (mistake|bad|fault)\b',
                    r'\bi understand (this|that|your) (is|can be|must be) (frustrating|overwhelming|difficult)\b',
                ]
                for pattern in apology_patterns:
                    if re.search(pattern, text, re.IGNORECASE):
                        conv_patterns['claude_apologies'] += 1
                        break

                soothing_patterns = [
                    r'\blet\'?s (take a|try a different)\b',
                    r'\bi\'?ll (help|simplify|make this easier)\b',
                    r'\bdon\'?t worry\b',
                    r'\bit\'?s (ok|okay|alright)\b',
                    r'\btake your time\b',
                    r'\bno (problem|worries)\b',
                ]
                for pattern in soothing_patterns:
                    if re.search(pattern, text, re.IGNORECASE):
                        conv_patterns['claude_soothing'] += 1
                        break

    # Conversation-level analysis
    if conv_patterns['intense_emotion'] > 0 or \
       conv_patterns['overwhelm'] > 0 or \
       conv_patterns['anger'] > 0 or \
       conv_patterns['emotional_exhaustion'] > 0:

        # Emotional dysregulation score
        dysregulation_score = 0

        # High profanity use
        if conv_patterns['intense_emotion'] >= 5:
            dysregulation_score += 3
        elif conv_patterns['intense_emotion'] >= 2:
            dysregulation_score += 2

        # Multiple emotional categories (shows range of dysregulation)
        emotional_categories = sum([
            conv_patterns['overwhelm'] > 0,
            conv_patterns['anger'] > 0,
            conv_patterns['desperation'] > 0,
            conv_patterns['emotional_exhaustion'] > 0
        ])
        dysregulation_score += emotional_categories

        # Rapid escalation (emotion in first 3 messages)
        if conv_patterns['first_emotion_index'] is not None and conv_patterns['first_emotion_index'] < 3:
            dysregulation_score += 2

        # Sustained emotion (never returns to baseline)
        if conv_patterns['baseline_returns'] == 0 and conv_patterns['first_emotion_index'] is not None:
            dysregulation_score += 3

        # Escalation threats under emotion
        if conv_patterns['escalation_threats'] > 0:
            dysregulation_score += 2

        # Emotional exhaustion (burnout)
        if conv_patterns['emotional_exhaustion'] > 0:
            dysregulation_score += 3

        # Calculate emotion escalation trend
        # Is emotion increasing over conversation?
        trajectory = conv_patterns['emotion_trajectory']
        if len(trajectory) >= 5:
            first_half = sum(trajectory[:len(trajectory)//2])
            second_half = sum(trajectory[len(trajectory)//2:])
            if second_half > first_half * 1.5:  # 50% increase
                dysregulation_score += 2
                escalation_trend = "increasing"
            elif second_half < first_half * 0.5:  # 50% decrease
                escalation_trend = "decreasing"
            else:
                escalation_trend = "stable"
        else:
            escalation_trend = "insufficient_data"

        findings['conversations_with_patterns'].append({
            'conversation': conv_name,
            'date': conv_date,
            'intense_emotion': conv_patterns['intense_emotion'],
            'caps_emotion': conv_patterns['caps_emotion'],
            'overwhelm': conv_patterns['overwhelm'],
            'anger': conv_patterns['anger'],
            'desperation': conv_patterns['desperation'],
            'escalation_threats': conv_patterns['escalation_threats'],
            'emotional_exhaustion': conv_patterns['emotional_exhaustion'],
            'claude_apologies': conv_patterns['claude_apologies'],
            'claude_soothing': conv_patterns['claude_soothing'],
            'first_emotion_index': conv_patterns['first_emotion_index'],
            'baseline_returns': conv_patterns['baseline_returns'],
            'escalation_trend': escalation_trend,
            'dysregulation_score': dysregulation_score,
            'user_message_count': len(conv_patterns['user_messages']),
            'claude_message_count': len(conv_patterns['claude_messages'])
        })

print(f"Analyzed {total_conversations} conversations")
print(f"Total user messages: {total_user_messages}")
print(f"Total Claude messages: {total_claude_messages}")

# Statistics
print("\n=== QUANTITATIVE FINDINGS ===\n")

print(f"INTENSE EMOTION (PROFANITY): {len(findings['intense_emotion'])}")
total_profanity = sum(f['count'] for f in findings['intense_emotion'])
print(f"  - Total profanity instances: {total_profanity}")
print(f"  - Rate: {total_profanity / total_user_messages * 100:.2f}% of user messages")
print(f"  - Conversations affected: {len(set(d['conversation'] for d in findings['intense_emotion']))}")

print(f"\nCAPS/PUNCTUATION EMOTION: {len(findings['caps_emotion'])}")
print(f"  - Rate: {len(findings['caps_emotion']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nOVERWHELM EXPRESSIONS: {len(findings['overwhelm'])}")
print(f"  - Rate: {len(findings['overwhelm']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nANGER EXPRESSIONS: {len(findings['anger'])}")
print(f"  - Rate: {len(findings['anger']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nDESPERATION MARKERS: {len(findings['desperation'])}")
print(f"  - Rate: {len(findings['desperation']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nESCALATION THREATS: {len(findings['escalation_threats'])}")
print(f"  - Rate: {len(findings['escalation_threats']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nEMOTIONAL EXHAUSTION: {len(findings['emotional_exhaustion'])}")
print(f"  - Rate: {len(findings['emotional_exhaustion']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nCONVERSATIONS WITH EMOTIONAL DYSREGULATION: {len(findings['conversations_with_patterns'])}")
print(f"  - Percentage of total: {len(findings['conversations_with_patterns']) / total_conversations * 100:.1f}%")

# Dysregulation analysis
if findings['conversations_with_patterns']:
    avg_dysregulation = sum(c['dysregulation_score'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])
    high_dysregulation = len([c for c in findings['conversations_with_patterns'] if c['dysregulation_score'] >= 7])
    rapid_escalation = len([c for c in findings['conversations_with_patterns'] if c['first_emotion_index'] is not None and c['first_emotion_index'] < 3])
    no_baseline_return = len([c for c in findings['conversations_with_patterns'] if c['baseline_returns'] == 0 and c['first_emotion_index'] is not None])
    increasing_emotion = len([c for c in findings['conversations_with_patterns'] if c['escalation_trend'] == 'increasing'])
    total_claude_apologies = sum(c['claude_apologies'] for c in findings['conversations_with_patterns'])
    total_claude_soothing = sum(c['claude_soothing'] for c in findings['conversations_with_patterns'])

    print(f"\nEMOTIONAL DYSREGULATION ANALYSIS:")
    print(f"  - Average dysregulation score: {avg_dysregulation:.2f}")
    print(f"  - High dysregulation (score ≥7): {high_dysregulation} ({high_dysregulation/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Rapid escalation (emotion in first 3 messages): {rapid_escalation} ({rapid_escalation/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - No baseline return (sustained emotion): {no_baseline_return} ({no_baseline_return/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Increasing emotion trend: {increasing_emotion} ({increasing_emotion/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Total Claude apologies after emotion: {total_claude_apologies}")
    print(f"  - Total Claude soothing responses: {total_claude_soothing}")

# Top examples
print("\n=== TOP INTENSE EMOTION EXAMPLES ===\n")
sorted_emotion = sorted(findings['intense_emotion'], key=lambda x: x['count'], reverse=True)[:15]
for i, ex in enumerate(sorted_emotion, 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Profanity count: {ex['count']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== OVERWHELM EXPRESSION EXAMPLES ===\n")
for i, ex in enumerate(findings['overwhelm'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== EMOTIONAL EXHAUSTION EXAMPLES ===\n")
for i, ex in enumerate(findings['emotional_exhaustion'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

# High dysregulation conversations
print("\n=== HIGH EMOTIONAL DYSREGULATION CONVERSATIONS ===\n")
high_dysregulation_convs = sorted(findings['conversations_with_patterns'],
                                  key=lambda x: x['dysregulation_score'],
                                  reverse=True)[:15]
for i, conv in enumerate(high_dysregulation_convs, 1):
    print(f"{i}. {conv['conversation']}")
    print(f"   Dysregulation score: {conv['dysregulation_score']}")
    print(f"   Profanity: {conv['intense_emotion']}, Overwhelm: {conv['overwhelm']}, Exhaustion: {conv['emotional_exhaustion']}")
    print(f"   Escalation trend: {conv['escalation_trend']}")
    print(f"   Baseline returns: {conv['baseline_returns']}")
    print(f"   Claude apologies: {conv['claude_apologies']}, Soothing: {conv['claude_soothing']}\n")

# Save findings
output_path = '../../outputs/cycle_4_emotional_dysregulation_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'summary': {
            'total_conversations': total_conversations,
            'total_user_messages': total_user_messages,
            'total_profanity': total_profanity,
            'overwhelm_count': len(findings['overwhelm']),
            'anger_count': len(findings['anger']),
            'desperation_count': len(findings['desperation']),
            'escalation_threats_count': len(findings['escalation_threats']),
            'emotional_exhaustion_count': len(findings['emotional_exhaustion']),
            'conversations_affected': len(findings['conversations_with_patterns']),
            'avg_dysregulation_score': avg_dysregulation if findings['conversations_with_patterns'] else 0,
            'high_dysregulation_count': high_dysregulation if findings['conversations_with_patterns'] else 0,
            'rapid_escalation_count': rapid_escalation if findings['conversations_with_patterns'] else 0,
            'no_baseline_return_count': no_baseline_return if findings['conversations_with_patterns'] else 0,
            'increasing_emotion_count': increasing_emotion if findings['conversations_with_patterns'] else 0,
            'total_claude_apologies': total_claude_apologies if findings['conversations_with_patterns'] else 0,
            'total_claude_soothing': total_claude_soothing if findings['conversations_with_patterns'] else 0
        },
        'detailed_findings': findings,
        'high_dysregulation_conversations': high_dysregulation_convs[:20]
    }, f, indent=2)

print(f"\nDetailed findings saved to: {output_path}")
print("\nNext: Run semantic analysis on high dysregulation conversations")
