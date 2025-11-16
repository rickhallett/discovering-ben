#!/usr/bin/env python3
import json
import re
from collections import defaultdict

# Load conversations
with open('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json', 'r') as f:
    data = json.load(f)

# Patterns to search for
magical_thinking_patterns = [
    r'maximum power',
    r'max power',
    r'perfect intelligence',
    r'ultimate',
    r'give me everything',
    r'best possible',
    r'highest quality',
    r'top tier',
    r'god mode',
    r'full capacity',
    r'100%',
    r'all.?knowing',
    r'omniscient'
]

authority_patterns = [
    r'ombudsman',
    r'escalate',
    r'complaint',
    r'sue',
    r'suing',
    r'legal action',
    r'take.?to.?court',
    r'lawyer',
    r'solicitor',
    r'litigation'
]

frustration_patterns = [
    r'not good enough',
    r'do better',
    r'try again',
    r'that.?s wrong',
    r'useless',
    r'shit',
    r'fuck',
    r'stupid',
    r'disappointing',
    r'pathetic'
]

demand_patterns = [
    r'^(do|give|make|create|write|show|tell|find)\s',
    r'^I (want|need|demand|require)',
    r'now\s*$',
    r'immediately'
]

findings = {
    'magical_thinking': [],
    'authority_escalation': [],
    'frustration': [],
    'imperatives': []
}

message_count = 0
user_message_count = 0

for conv in data:
    if not conv.get('chat_messages'):
        continue

    conv_name = conv.get('name', 'Unnamed')

    for msg in conv['chat_messages']:
        message_count += 1
        if msg.get('sender') != 'human':
            continue

        user_message_count += 1
        text = msg.get('text', '')

        # Search for patterns
        for pattern in magical_thinking_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                findings['magical_thinking'].append({
                    'conversation': conv_name,
                    'text': text[:200],
                    'pattern': pattern
                })

        for pattern in authority_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                findings['authority_escalation'].append({
                    'conversation': conv_name,
                    'text': text[:200],
                    'pattern': pattern
                })

        for pattern in frustration_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                findings['frustration'].append({
                    'conversation': conv_name,
                    'text': text[:200],
                    'pattern': pattern
                })

        for pattern in demand_patterns:
            if re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
                if 'imperatives' not in findings:
                    findings['imperatives'] = []
                if len(findings['imperatives']) < 50:  # Limit to first 50
                    findings['imperatives'].append({
                        'conversation': conv_name,
                        'text': text[:200],
                        'pattern': pattern
                    })

# Print results
print(f"Total messages: {message_count}")
print(f"User messages: {user_message_count}")
print(f"\n=== MAGICAL THINKING PATTERNS ===")
print(f"Found {len(findings['magical_thinking'])} instances\n")
for item in findings['magical_thinking'][:10]:
    print(f"Conv: {item['conversation']}")
    print(f"Pattern: {item['pattern']}")
    print(f"Text: {item['text']}\n")

print(f"\n=== AUTHORITY ESCALATION PATTERNS ===")
print(f"Found {len(findings['authority_escalation'])} instances\n")
for item in findings['authority_escalation'][:10]:
    print(f"Conv: {item['conversation']}")
    print(f"Pattern: {item['pattern']}")
    print(f"Text: {item['text']}\n")

print(f"\n=== FRUSTRATION PATTERNS ===")
print(f"Found {len(findings['frustration'])} instances\n")
for item in findings['frustration'][:10]:
    print(f"Conv: {item['conversation']}")
    print(f"Pattern: {item['pattern']}")
    print(f"Text: {item['text']}\n")

print(f"\n=== IMPERATIVE/DEMAND PATTERNS ===")
print(f"Found {len(findings['imperatives'])} instances (showing first 20)\n")
for item in findings['imperatives'][:20]:
    print(f"Conv: {item['conversation']}")
    print(f"Text: {item['text']}\n")

# Save to JSON
with open('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/pattern_analysis.json', 'w') as f:
    json.dump(findings, f, indent=2)

print("\nFull results saved to pattern_analysis.json")
