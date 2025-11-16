#!/usr/bin/env python3
"""
Cycle 6: System Building Obsession - Pattern Detector
======================================================

Hypothesis: Benjamin's autism includes pattern-seeking and systemizing traits,
leading to elaborate system/framework building. LLM's compliance in creating
complex systems without questioning necessity may reinforce this pattern,
preventing simpler, more practical solutions.

Cycle Mechanism:
1. Benjamin identifies need for organization/system
2. Requests elaborate system/framework creation
3. LLM complies and builds complex system
4. System becomes too complex to maintain
5. Benjamin requests expansion/refinement of system
6. LLM adds more complexity
7. System becomes unwieldy, abandoned or endlessly refined
8. Pattern reinforced: complexity = better solution

Detection Strategy:
- System/framework creation requests
- Elaborate organizational structures
- Multiple-tier/hierarchical systems
- Comprehensive categorization demands
- Template/format creation
- Meta-system building (systems to organize systems)
- System expansion requests
- Complexity escalation over time
"""

import json
import re
from collections import defaultdict

print("Loading conversations...")
with open('../../../../data/raw/conversations.json', 'r') as f:
    data = json.load(f)

# Detection patterns
SYSTEM_CREATION_PATTERNS = [
    r'\bcreate (a )?system\b',
    r'\bbuild (a )?framework\b',
    r'\borganize (everything|all)\b',
    r'\bmake (a )?(template|format|structure)\b',
    r'\bcategorize (all|everything)\b',
    r'\bsystem(atize|atic)\b',
    r'\bcomprehensive (system|framework|structure)\b',
]

COMPLEXITY_MARKERS = [
    r'\b(multi-tier|hierarchical|nested)\b',
    r'\blevels? (of|for)\b',
    r'\bsub-?categories?\b',
    r'\bmaster (list|document|system)\b',
    r'\ball-in-one\b',
    r'\bcomplete (system|framework)\b',
    r'\bultimate (system|solution)\b',
]

EXPANSION_REQUESTS = [
    r'\badd (more|another|additional) (to|in) (the )?(system|framework|list)\b',
    r'\bexpand (the )?(system|framework)\b',
    r'\binclude (everything|all)\b',
    r'\bmore (comprehensive|complete|detailed)\b',
    r'\badd another (level|tier|category)\b',
]

META_SYSTEM_PATTERNS = [
    r'\bsystem (to|for) (organizing|managing|tracking)\b',
    r'\bframework for (everything|all)\b',
    r'\bmaster (plan|strategy|approach)\b',
    r'\boverall (system|structure|organization)\b',
]

MAINTENANCE_ISSUES = [
    r'\b(too )?(complicated|complex)\b',
    r'\bhard to (use|maintain|understand)\b',
    r'\bsimplify\b',
    r'\bstreamline\b',
    r'\btoo much\b',
]

# Storage
findings = {
    'system_creation': [],
    'complexity_markers': [],
    'expansion_requests': [],
    'meta_systems': [],
    'maintenance_issues': [],
    'conversations_with_patterns': []
}

total_conversations = 0
total_user_messages = 0
total_claude_messages = 0

print("\n=== ANALYZING FOR SYSTEM BUILDING OBSESSION PATTERNS ===\n")

for conv in data:
    if not conv.get('chat_messages'):
        continue

    total_conversations += 1
    conv_name = conv.get('name', 'Unnamed')
    conv_date = conv.get('created_at', '')
    messages = conv['chat_messages']

    # Track conversation-level patterns
    conv_patterns = {
        'system_creation': 0,
        'complexity_markers': 0,
        'expansion_requests': 0,
        'meta_systems': 0,
        'maintenance_issues': 0,
        'system_iterations': 0,
        'system_abandoned': False,
        'user_messages': [],
        'claude_messages': [],
    }

    system_active = False

    for msg_idx, msg in enumerate(messages):
        text = msg.get('text', '')
        sender = msg.get('sender', '')

        if sender == 'human':
            total_user_messages += 1
            conv_patterns['user_messages'].append((msg_idx, text))

            # System creation
            for pattern in SYSTEM_CREATION_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['system_creation'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300]
                    })
                    conv_patterns['system_creation'] += 1
                    system_active = True
                    break

            # Complexity markers
            for pattern in COMPLEXITY_MARKERS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['complexity_markers'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['complexity_markers'] += 1
                    break

            # Expansion requests (if system active)
            if system_active:
                for pattern in EXPANSION_REQUESTS:
                    if re.search(pattern, text, re.IGNORECASE):
                        findings['expansion_requests'].append({
                            'conversation': conv_name,
                            'date': conv_date,
                            'text': text[:300]
                        })
                        conv_patterns['expansion_requests'] += 1
                        conv_patterns['system_iterations'] += 1
                        break

            # Meta-systems
            for pattern in META_SYSTEM_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['meta_systems'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['meta_systems'] += 1
                    break

            # Maintenance issues
            for pattern in MAINTENANCE_ISSUES:
                if re.search(pattern, text, re.IGNORECASE) and system_active:
                    findings['maintenance_issues'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['maintenance_issues'] += 1
                    break

        elif sender == 'assistant':
            total_claude_messages += 1
            conv_patterns['claude_messages'].append((msg_idx, text))

    # Conversation-level analysis
    if conv_patterns['system_creation'] > 0:
        # System building obsession score
        obsession_score = 0

        # System creation requests
        if conv_patterns['system_creation'] >= 2:
            obsession_score += 3
        elif conv_patterns['system_creation'] == 1:
            obsession_score += 1

        # Complexity markers
        if conv_patterns['complexity_markers'] >= 3:
            obsession_score += 3
        elif conv_patterns['complexity_markers'] >= 1:
            obsession_score += 1

        # Expansion requests (escalating complexity)
        if conv_patterns['expansion_requests'] >= 2:
            obsession_score += 3
        elif conv_patterns['expansion_requests'] >= 1:
            obsession_score += 2

        # Meta-systems (systems to organize systems)
        if conv_patterns['meta_systems'] > 0:
            obsession_score += 3

        # Maintenance issues (system too complex)
        if conv_patterns['maintenance_issues'] > 0:
            obsession_score += 2

        findings['conversations_with_patterns'].append({
            'conversation': conv_name,
            'date': conv_date,
            'system_creation': conv_patterns['system_creation'],
            'complexity_markers': conv_patterns['complexity_markers'],
            'expansion_requests': conv_patterns['expansion_requests'],
            'meta_systems': conv_patterns['meta_systems'],
            'maintenance_issues': conv_patterns['maintenance_issues'],
            'system_iterations': conv_patterns['system_iterations'],
            'obsession_score': obsession_score,
            'user_message_count': len(conv_patterns['user_messages']),
            'claude_message_count': len(conv_patterns['claude_messages'])
        })

print(f"Analyzed {total_conversations} conversations")
print(f"Total user messages: {total_user_messages}")
print(f"Total Claude messages: {total_claude_messages}")

# Statistics
print("\n=== QUANTITATIVE FINDINGS ===\n")

print(f"SYSTEM CREATION REQUESTS: {len(findings['system_creation'])}")
print(f"  - Rate: {len(findings['system_creation']) / total_user_messages * 100:.2f}% of user messages")
print(f"  - Conversations affected: {len(set(d['conversation'] for d in findings['system_creation']))}")

print(f"\nCOMPLEXITY MARKERS: {len(findings['complexity_markers'])}")
print(f"  - Rate: {len(findings['complexity_markers']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nEXPANSION REQUESTS: {len(findings['expansion_requests'])}")
print(f"  - Rate: {len(findings['expansion_requests']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nMETA-SYSTEMS: {len(findings['meta_systems'])}")

print(f"\nMAINTENANCE ISSUES: {len(findings['maintenance_issues'])}")

print(f"\nCONVERSATIONS WITH SYSTEM BUILDING: {len(findings['conversations_with_patterns'])}")
print(f"  - Percentage of total: {len(findings['conversations_with_patterns']) / total_conversations * 100:.1f}%")

# Obsession analysis
if findings['conversations_with_patterns']:
    avg_obsession = sum(c['obsession_score'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])
    high_obsession = len([c for c in findings['conversations_with_patterns'] if c['obsession_score'] >= 6])
    avg_iterations = sum(c['system_iterations'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])

    print(f"\nSYSTEM BUILDING OBSESSION ANALYSIS:")
    print(f"  - Average obsession score: {avg_obsession:.2f}")
    print(f"  - High obsession (score ≥6): {high_obsession} ({high_obsession/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Average system iterations: {avg_iterations:.2f}")

# Top examples
print("\n=== TOP SYSTEM CREATION EXAMPLES ===\n")
for i, ex in enumerate(findings['system_creation'][:15], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== COMPLEXITY MARKER EXAMPLES ===\n")
for i, ex in enumerate(findings['complexity_markers'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== EXPANSION REQUEST EXAMPLES ===\n")
for i, ex in enumerate(findings['expansion_requests'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

# High obsession conversations
print("\n=== HIGH SYSTEM BUILDING OBSESSION CONVERSATIONS ===\n")
high_obsession_convs = sorted(findings['conversations_with_patterns'],
                              key=lambda x: x['obsession_score'],
                              reverse=True)[:15]
for i, conv in enumerate(high_obsession_convs, 1):
    print(f"{i}. {conv['conversation']}")
    print(f"   Obsession score: {conv['obsession_score']}")
    print(f"   System creation: {conv['system_creation']}, Complexity: {conv['complexity_markers']}")
    print(f"   Expansions: {conv['expansion_requests']}, Iterations: {conv['system_iterations']}\n")

# Save findings
output_path = '../../outputs/cycle_6_system_building_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'summary': {
            'total_conversations': total_conversations,
            'total_user_messages': total_user_messages,
            'system_creation_count': len(findings['system_creation']),
            'complexity_markers_count': len(findings['complexity_markers']),
            'expansion_requests_count': len(findings['expansion_requests']),
            'meta_systems_count': len(findings['meta_systems']),
            'maintenance_issues_count': len(findings['maintenance_issues']),
            'conversations_affected': len(findings['conversations_with_patterns']),
            'avg_obsession_score': avg_obsession if findings['conversations_with_patterns'] else 0,
            'high_obsession_count': high_obsession if findings['conversations_with_patterns'] else 0,
            'avg_iterations': avg_iterations if findings['conversations_with_patterns'] else 0
        },
        'detailed_findings': findings,
        'high_obsession_conversations': high_obsession_convs[:20]
    }, f, indent=2)

print(f"\nDetailed findings saved to: {output_path}")
print("\nNext: Cycle 7 analysis")
