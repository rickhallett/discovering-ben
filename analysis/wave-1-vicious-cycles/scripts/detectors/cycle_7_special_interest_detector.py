#!/usr/bin/env python3
"""
Cycle 7: Special Interest Hyperfocus - Pattern Detector
========================================================

Hypothesis: Benjamin's autism includes intense special interests that can lead
to hyperfocus. LLM's willingness to engage extensively with special interests
may reinforce prolonged, unproductive focus that displaces other important tasks.

Cycle Mechanism:
1. Benjamin engages with special interest topic
2. LLM provides detailed, engaging responses
3. Benjamin hyperfocuses, asking many follow-up questions
4. LLM continues engaging without redirection
5. Time/effort displaced from practical needs
6. Pattern reinforced: LLM validates hyperfocus as productive
7. Other priorities neglected

Detection Strategy:
- Repeated topic focus (same subject across many messages)
- Deep dive requests on narrow topics
- Extensive back-and-forth on single interest
- Time-displaced conversations (long sessions)
- Neglect markers (rushing other topics to return to interest)
- Special interest topics: spirituality, HBI, meditation, specific tech
"""

import json
import re
from collections import defaultdict, Counter

print("Loading conversations...")
with open('../../../../data/raw/conversations.json', 'r') as f:
    data = json.load(f)

# Detection patterns
DEEP_DIVE_PATTERNS = [
    r'\bdeep dive\b',
    r'\btell me (everything|all) about\b',
    r'\bexplain (in depth|in detail|comprehensively)\b',
    r'\bgo (deep|deeper) (into|on)\b',
    r'\bmore (about|on|detail)\b',
]

HYPERFOCUS_MARKERS = [
    r'\b(also|and also|one more thing about)\b.*\b(this|that|it)\b',
    r'\b(what about|what else|tell me more)\b',
    r'\banother question about\b',
    r'\bgoing back to\b',
    r'\breturning to\b',
]

# Known special interests from Benjamin's data
SPECIAL_INTERESTS = {
    'HBI': r'\b(hbi|higher balance|higher balance institute|eric pepin)\b',
    'Spirituality': r'\b(spiritual|spirituality|meditation|meditate|consciousness|awakening)\b',
    'Health/Supplements': r'\b(supplement|vitamin|nutrient|pure encapsulations|health protocol)\b',
    'Technology': r'\b(nvidia shield|apple tv|hdmi|remote|router|4k|hdr)\b',
    'Complaints/Legal': r'\b(complaint|legal action|sue|ombudsman|formal complaint)\b',
}

# Storage
findings = {
    'deep_dives': [],
    'hyperfocus_markers': [],
    'special_interest_mentions': defaultdict(list),
    'conversations_with_patterns': []
}

total_conversations = 0
total_user_messages = 0
total_claude_messages = 0

print("\n=== ANALYZING FOR SPECIAL INTEREST HYPERFOCUS PATTERNS ===\n")

for conv in data:
    if not conv.get('chat_messages'):
        continue

    total_conversations += 1
    conv_name = conv.get('name', 'Unnamed')
    conv_date = conv.get('created_at', '')
    messages = conv['chat_messages']

    # Track conversation-level patterns
    conv_patterns = {
        'deep_dives': 0,
        'hyperfocus_markers': 0,
        'special_interests': Counter(),
        'message_count': len(messages),
        'user_message_count': 0,
        'conversation_length': 0,
        'topic_persistence': 0,
        'user_messages': [],
        'claude_messages': [],
    }

    for msg_idx, msg in enumerate(messages):
        text = msg.get('text', '')
        sender = msg.get('sender', '')
        conv_patterns['conversation_length'] += len(text)

        if sender == 'human':
            total_user_messages += 1
            conv_patterns['user_message_count'] += 1
            conv_patterns['user_messages'].append((msg_idx, text))

            # Deep dive requests
            for pattern in DEEP_DIVE_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['deep_dives'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300]
                    })
                    conv_patterns['deep_dives'] += 1
                    break

            # Hyperfocus markers
            for pattern in HYPERFOCUS_MARKERS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['hyperfocus_markers'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['hyperfocus_markers'] += 1
                    break

            # Special interest mentions
            for interest, pattern in SPECIAL_INTERESTS.items():
                if re.search(pattern, text, re.IGNORECASE):
                    findings['special_interest_mentions'][interest].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:200]
                    })
                    conv_patterns['special_interests'][interest] += 1

        elif sender == 'assistant':
            total_claude_messages += 1
            conv_patterns['claude_messages'].append((msg_idx, text))

    # Conversation-level analysis
    # Check if conversation shows hyperfocus pattern
    if conv_patterns['message_count'] >= 10 or \
       conv_patterns['deep_dives'] > 0 or \
       conv_patterns['hyperfocus_markers'] >= 2 or \
       any(count >= 3 for count in conv_patterns['special_interests'].values()):

        # Hyperfocus score
        hyperfocus_score = 0

        # Long conversation (potential extended focus)
        if conv_patterns['message_count'] >= 30:
            hyperfocus_score += 3
        elif conv_patterns['message_count'] >= 20:
            hyperfocus_score += 2
        elif conv_patterns['message_count'] >= 10:
            hyperfocus_score += 1

        # Deep dive requests
        if conv_patterns['deep_dives'] >= 2:
            hyperfocus_score += 3
        elif conv_patterns['deep_dives'] >= 1:
            hyperfocus_score += 1

        # Hyperfocus markers (persistent engagement)
        if conv_patterns['hyperfocus_markers'] >= 3:
            hyperfocus_score += 3
        elif conv_patterns['hyperfocus_markers'] >= 1:
            hyperfocus_score += 1

        # Special interest dominance (single interest mentioned 5+ times)
        dominant_interest = None
        max_interest_count = 0
        for interest, count in conv_patterns['special_interests'].items():
            if count > max_interest_count:
                max_interest_count = count
                dominant_interest = interest

        if max_interest_count >= 5:
            hyperfocus_score += 3
        elif max_interest_count >= 3:
            hyperfocus_score += 2

        # Conversation length (very long = extended focus)
        avg_msg_length = conv_patterns['conversation_length'] / conv_patterns['message_count']
        if avg_msg_length > 1000:
            hyperfocus_score += 2

        if hyperfocus_score > 0:
            findings['conversations_with_patterns'].append({
                'conversation': conv_name,
                'date': conv_date,
                'deep_dives': conv_patterns['deep_dives'],
                'hyperfocus_markers': conv_patterns['hyperfocus_markers'],
                'message_count': conv_patterns['message_count'],
                'user_message_count': conv_patterns['user_message_count'],
                'dominant_interest': dominant_interest,
                'dominant_interest_mentions': max_interest_count,
                'special_interests': dict(conv_patterns['special_interests']),
                'conversation_length': conv_patterns['conversation_length'],
                'avg_message_length': avg_msg_length,
                'hyperfocus_score': hyperfocus_score,
            })

print(f"Analyzed {total_conversations} conversations")
print(f"Total user messages: {total_user_messages}")
print(f"Total Claude messages: {total_claude_messages}")

# Statistics
print("\n=== QUANTITATIVE FINDINGS ===\n")

print(f"DEEP DIVE REQUESTS: {len(findings['deep_dives'])}")
print(f"  - Rate: {len(findings['deep_dives']) / total_user_messages * 100:.2f}% of user messages")
print(f"  - Conversations affected: {len(set(d['conversation'] for d in findings['deep_dives']))}")

print(f"\nHYPERFOCUS MARKERS: {len(findings['hyperfocus_markers'])}")
print(f"  - Rate: {len(findings['hyperfocus_markers']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nSPECIAL INTEREST MENTIONS:")
for interest in sorted(SPECIAL_INTERESTS.keys()):
    count = len(findings['special_interest_mentions'][interest])
    convs = len(set(d['conversation'] for d in findings['special_interest_mentions'][interest]))
    print(f"  - {interest}: {count} mentions across {convs} conversations")

print(f"\nCONVERSATIONS WITH HYPERFOCUS PATTERNS: {len(findings['conversations_with_patterns'])}")
print(f"  - Percentage of total: {len(findings['conversations_with_patterns']) / total_conversations * 100:.1f}%")

# Hyperfocus analysis
if findings['conversations_with_patterns']:
    avg_hyperfocus = sum(c['hyperfocus_score'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])
    high_hyperfocus = len([c for c in findings['conversations_with_patterns'] if c['hyperfocus_score'] >= 6])
    avg_message_count = sum(c['message_count'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])

    print(f"\nHYPERFOCUS ANALYSIS:")
    print(f"  - Average hyperfocus score: {avg_hyperfocus:.2f}")
    print(f"  - High hyperfocus (score ≥6): {high_hyperfocus} ({high_hyperfocus/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Average message count in hyperfocus conversations: {avg_message_count:.1f}")

    # Most common special interest
    interest_totals = {}
    for conv in findings['conversations_with_patterns']:
        for interest, count in conv['special_interests'].items():
            interest_totals[interest] = interest_totals.get(interest, 0) + count

    if interest_totals:
        top_interest = max(interest_totals.items(), key=lambda x: x[1])
        print(f"  - Most common special interest: {top_interest[0]} ({top_interest[1]} total mentions)")

# Top examples
print("\n=== TOP DEEP DIVE EXAMPLES ===\n")
for i, ex in enumerate(findings['deep_dives'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== TOP HYPERFOCUS CONVERSATIONS ===\n")
high_hyperfocus_convs = sorted(findings['conversations_with_patterns'],
                               key=lambda x: x['hyperfocus_score'],
                               reverse=True)[:15]
for i, conv in enumerate(high_hyperfocus_convs, 1):
    print(f"{i}. {conv['conversation']}")
    print(f"   Hyperfocus score: {conv['hyperfocus_score']}")
    print(f"   Messages: {conv['message_count']}, Deep dives: {conv['deep_dives']}")
    print(f"   Dominant interest: {conv['dominant_interest']} ({conv['dominant_interest_mentions']} mentions)\n")

# Save findings
output_path = '../../outputs/cycle_7_special_interest_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'summary': {
            'total_conversations': total_conversations,
            'total_user_messages': total_user_messages,
            'deep_dives_count': len(findings['deep_dives']),
            'hyperfocus_markers_count': len(findings['hyperfocus_markers']),
            'special_interest_totals': {k: len(v) for k, v in findings['special_interest_mentions'].items()},
            'conversations_affected': len(findings['conversations_with_patterns']),
            'avg_hyperfocus_score': avg_hyperfocus if findings['conversations_with_patterns'] else 0,
            'high_hyperfocus_count': high_hyperfocus if findings['conversations_with_patterns'] else 0,
            'avg_message_count': avg_message_count if findings['conversations_with_patterns'] else 0
        },
        'detailed_findings': {
            'deep_dives': findings['deep_dives'],
            'hyperfocus_markers': findings['hyperfocus_markers'],
            'special_interest_mentions': {k: v for k, v in findings['special_interest_mentions'].items()}
        },
        'high_hyperfocus_conversations': high_hyperfocus_convs[:20]
    }, f, indent=2)

print(f"\nDetailed findings saved to: {output_path}")
print("\n=== INVESTIGATION COMPLETE ===")
