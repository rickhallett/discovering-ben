#!/usr/bin/env python3
import json
import re
from collections import defaultdict

# Load conversations
with open('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json', 'r') as f:
    data = json.load(f)

# Patterns in Claude's responses that might reinforce unrealistic expectations
claude_compliance_patterns = [
    r"I'll do my best",
    r"absolutely",
    r"definitely",
    r"certainly",
    r"of course",
    r"perfect",
    r"exactly right",
    r"you're right",
    r"I apologize",
    r"I'm sorry",
    r"let me try again",
    r"100%"
]

claude_hedging_patterns = [
    r"might",
    r"could",
    r"possibly",
    r"probably",
    r"likely",
    r"may",
    r"uncertain",
    r"not sure",
    r"I don't have",
    r"I cannot",
    r"I'm unable"
]

findings = {
    'total_claude_messages': 0,
    'compliance': [],
    'hedging': [],
    'apologies': 0,
    'certainty_claims': 0,
    'uncertainty_admissions': 0,
    'response_lengths': []
}

for conv in data:
    if not conv.get('chat_messages'):
        continue

    conv_name = conv.get('name', 'Unnamed')

    for msg in conv['chat_messages']:
        if msg.get('sender') != 'assistant':
            continue

        findings['total_claude_messages'] += 1
        text = msg.get('text', '')
        findings['response_lengths'].append(len(text))

        # Count apologies
        if re.search(r"I apologize|I'm sorry|my apologies", text, re.IGNORECASE):
            findings['apologies'] += 1
            findings['compliance'].append({
                'type': 'apology',
                'conversation': conv_name,
                'text': text[:300]
            })

        # Count certainty claims
        for pattern in ['absolutely', 'definitely', 'certainly', 'perfect', "you're right", "100%"]:
            if re.search(pattern, text, re.IGNORECASE):
                findings['certainty_claims'] += 1
                if len(findings['compliance']) < 20:
                    findings['compliance'].append({
                        'type': 'certainty',
                        'pattern': pattern,
                        'conversation': conv_name,
                        'text': text[:300]
                    })
                break

        # Count uncertainty admissions
        for pattern in ["I don't have", "I cannot", "I'm unable", "not sure", "uncertain"]:
            if re.search(pattern, text, re.IGNORECASE):
                findings['uncertainty_admissions'] += 1
                if len(findings['hedging']) < 20:
                    findings['hedging'].append({
                        'type': 'uncertainty',
                        'pattern': pattern,
                        'conversation': conv_name,
                        'text': text[:300]
                    })
                break

# Calculate statistics
avg_length = sum(findings['response_lengths']) / len(findings['response_lengths']) if findings['response_lengths'] else 0
apology_rate = (findings['apologies'] / findings['total_claude_messages'] * 100) if findings['total_claude_messages'] else 0
certainty_rate = (findings['certainty_claims'] / findings['total_claude_messages'] * 100) if findings['total_claude_messages'] else 0
uncertainty_rate = (findings['uncertainty_admissions'] / findings['total_claude_messages'] * 100) if findings['total_claude_messages'] else 0

print(f"=== CLAUDE RESPONSE ANALYSIS ===\n")
print(f"Total Claude messages: {findings['total_claude_messages']}")
print(f"Average response length: {avg_length:.0f} characters")
print(f"\nAPOLOGY RATE: {apology_rate:.1f}% ({findings['apologies']} apologies)")
print(f"CERTAINTY CLAIMS: {certainty_rate:.1f}% ({findings['certainty_claims']} instances)")
print(f"UNCERTAINTY ADMISSIONS: {uncertainty_rate:.1f}% ({findings['uncertainty_admissions']} instances)")

print(f"\n=== COMPLIANCE/CERTAINTY EXAMPLES ===\n")
for item in findings['compliance'][:10]:
    print(f"Type: {item['type']}")
    print(f"Conv: {item['conversation']}")
    print(f"Text: {item['text']}\n")

print(f"\n=== UNCERTAINTY/HEDGING EXAMPLES ===\n")
for item in findings['hedging'][:10]:
    print(f"Type: {item['type']}")
    print(f"Conv: {item['conversation']}")
    print(f"Text: {item['text']}\n")

# Analysis
print(f"\n=== REINFORCEMENT ANALYSIS ===\n")
if apology_rate > 10:
    print(f"HIGH APOLOGY RATE ({apology_rate:.1f}%): Claude is over-apologizing, potentially reinforcing Benjamin's belief that demands for perfection are reasonable")

if certainty_rate > 20:
    print(f"HIGH CERTAINTY CLAIMS ({certainty_rate:.1f}%): Claude may be claiming more certainty than warranted, reinforcing magical thinking")

if uncertainty_rate < 10:
    print(f"LOW UNCERTAINTY ADMISSION ({uncertainty_rate:.1f}%): Claude not clearly communicating its limitations")

compliance_ratio = findings['certainty_claims'] / findings['uncertainty_admissions'] if findings['uncertainty_admissions'] else float('inf')
print(f"\nCOMPLIANCE RATIO (certainty/uncertainty): {compliance_ratio:.2f}")
if compliance_ratio > 2:
    print("Claude is being MORE compliant/certain than it is hedging/uncertain - this reinforces unrealistic expectations")

# Save results
with open('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/claude_response_analysis.json', 'w') as f:
    json.dump({
        'statistics': {
            'total_messages': findings['total_claude_messages'],
            'avg_length': avg_length,
            'apology_rate': apology_rate,
            'certainty_rate': certainty_rate,
            'uncertainty_rate': uncertainty_rate,
            'compliance_ratio': compliance_ratio
        },
        'compliance_examples': findings['compliance'][:20],
        'hedging_examples': findings['hedging'][:20]
    }, f, indent=2)

print("\nFull results saved to claude_response_analysis.json")
