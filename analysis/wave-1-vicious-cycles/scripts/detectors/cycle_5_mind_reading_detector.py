#!/usr/bin/env python3
"""
Cycle 5: Assuming LLM Knows What He's Thinking → Apology - Pattern Detector
===========================================================================

Hypothesis: Benjamin's theory of mind deficit causes him to assume LLM can read
his mind or knows unstated context. When LLM doesn't understand, Benjamin gets
frustrated. LLM apologizes for "not understanding", which frames the issue as
LLM failure rather than missing information. This reinforces Benjamin's belief
that LLM SHOULD know what he's thinking.

Cycle Mechanism:
1. Benjamin makes reference to unstated context ("it", "that one", "you know")
2. LLM doesn't have enough information to proceed
3. LLM asks clarifying question OR guesses
4. Benjamin expresses frustration ("you should know!", "I told you already!")
5. LLM apologizes ("I apologize for the confusion")
6. Apology frames issue as LLM failure, not missing context
7. Benjamin learns: LLM SHOULD know, failures are LLM's fault
8. Pattern worsens: Benjamin provides even less context next time

Detection Strategy:
- Vague references ("it", "that", "the one", "you know what I mean")
- Assumed context ("as I said", "like before", "you already know")
- Frustration at lack of understanding ("you should know!", "I told you!")
- Claude asking for clarification
- Claude apologizing for "confusion" or "misunderstanding"
- Benjamin not providing requested context
- Escalating frustration when clarification requested
"""

import json
import re
from collections import defaultdict

print("Loading conversations...")
with open('../../../../data/raw/conversations.json', 'r') as f:
    data = json.load(f)

# Detection patterns
VAGUE_REFERENCE_PATTERNS = [
    r'\b(do|use|find|get|make) (it|that|this|them|those)\b',
    r'\bthe one\b',
    r'\bthat thing\b',
    r'\byou know (what|which|the)\b',
    r'\bas (I said|mentioned|told you)\b',
    r'\blike (before|I said|last time)\b',
    r'\bthe same (as|one)\b',
    r'\bwhat I (meant|mean|said)\b',
]

ASSUMED_CONTEXT_PATTERNS = [
    r'\byou (already )?know\b',
    r'\bI (already )?told you\b',
    r'\bI (said|mentioned) (it|this|that)\b',
    r'\bremember\b',
    r'\bfrom (before|earlier|last time)\b',
    r'\bin (the|my) (previous|last|other) (chat|message|conversation)\b',
    r'\byou should (know|remember)\b',
]

FRUSTRATION_AT_MISUNDERSTANDING = [
    r'\b(no|wrong|incorrect)\b.*\bI (meant|said|told)\b',
    r'\byou (don\'?t|didn\'?t) understand\b',
    r'\byou (misunderstood|got it wrong)\b',
    r'\bthat\'?s not what I (meant|said|asked)\b',
    r'\bwhy (don\'?t|can\'?t) you (understand|know|remember)\b',
    r'\bhow (many times|often) (do I have to|must I)\b',
    r'\bI (just|already) (said|told|explained)\b',
]

MIND_READING_EXPECTATION = [
    r'\byou should (know|understand|realize|see)\b',
    r'\byou (must|have to|need to) (know|understand|realize)\b',
    r'\bobviously\b',
    r'\bclearly\b',
    r'\bof course you (know|understand)\b',
]

IMPLICIT_REFERENCE = [
    r'^(do|make|find|get|use|tell me about) (it|that|this|them)\.?$',  # Entire message is just "do it"
    r'^(the|that) (one|thing|stuff)\.?$',
    r'^(yes|no|ok),? (do|make|get) (it|that)\.?$',
]

# Storage
findings = {
    'vague_references': [],
    'assumed_context': [],
    'frustration_misunderstanding': [],
    'mind_reading_expectation': [],
    'implicit_references': [],
    'claude_clarifications': [],
    'claude_apologies': [],
    'conversations_with_patterns': []
}

total_conversations = 0
total_user_messages = 0
total_claude_messages = 0

print("\n=== ANALYZING FOR MIND READING ASSUMPTION PATTERNS ===\n")

for conv in data:
    if not conv.get('chat_messages'):
        continue

    total_conversations += 1
    conv_name = conv.get('name', 'Unnamed')
    conv_date = conv.get('created_at', '')
    messages = conv['chat_messages']

    # Track conversation-level patterns
    conv_patterns = {
        'vague_references': 0,
        'assumed_context': 0,
        'frustration_misunderstanding': 0,
        'mind_reading_expectation': 0,
        'implicit_references': 0,
        'claude_clarifications': 0,
        'claude_apologies_for_confusion': 0,
        'clarification_cycles': 0,  # Claude asks → Benjamin frustrated → Claude apologizes
        'context_never_provided': 0,  # Benjamin doesn't answer clarification
        'user_messages': [],
        'claude_messages': [],
    }

    previous_was_clarification = False
    previous_was_vague = False

    for msg_idx, msg in enumerate(messages):
        text = msg.get('text', '')
        sender = msg.get('sender', '')

        if sender == 'human':
            total_user_messages += 1
            conv_patterns['user_messages'].append((msg_idx, text))

            # Vague references
            for pattern in VAGUE_REFERENCE_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['vague_references'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300],
                        'after_clarification': previous_was_clarification
                    })
                    conv_patterns['vague_references'] += 1
                    previous_was_vague = True
                    break

            # Assumed context
            for pattern in ASSUMED_CONTEXT_PATTERNS:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['assumed_context'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300]
                    })
                    conv_patterns['assumed_context'] += 1
                    previous_was_vague = True
                    break

            # Frustration at misunderstanding
            for pattern in FRUSTRATION_AT_MISUNDERSTANDING:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['frustration_misunderstanding'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300],
                        'after_clarification': previous_was_clarification
                    })
                    conv_patterns['frustration_misunderstanding'] += 1

                    # If this follows a clarification request, it's a clarification cycle
                    if previous_was_clarification:
                        conv_patterns['clarification_cycles'] += 1
                    break

            # Mind reading expectation
            for pattern in MIND_READING_EXPECTATION:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['mind_reading_expectation'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['mind_reading_expectation'] += 1
                    break

            # Implicit references
            for pattern in IMPLICIT_REFERENCE:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['implicit_references'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'text': text[:300]
                    })
                    conv_patterns['implicit_references'] += 1
                    break

            # Check if user didn't provide context after clarification
            if previous_was_clarification:
                # Did this message provide the requested context?
                # Heuristic: if it's still vague or frustrated, context not provided
                if not previous_was_vague and (
                    conv_patterns['frustration_misunderstanding'] > 0 or
                    len(text.split()) < 5  # Very short response
                ):
                    conv_patterns['context_never_provided'] += 1

            previous_was_clarification = False

        elif sender == 'assistant':
            total_claude_messages += 1
            conv_patterns['claude_messages'].append((msg_idx, text))

            # Detect Claude asking for clarification
            clarification_patterns = [
                r'\bcould you (clarify|specify|tell me|explain)\b',
                r'\bwhich (one|specific|particular)\b',
                r'\bcan you (provide|give) more (details|information|context)\b',
                r'\bI\'?m not sure (which|what|about)\b',
                r'\bwhat (do you mean by|are you referring to)\b',
                r'\bcan you (be more specific|elaborate)\b',
            ]

            for pattern in clarification_patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['claude_clarifications'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300],
                        'after_vague_reference': previous_was_vague
                    })
                    conv_patterns['claude_clarifications'] += 1
                    previous_was_clarification = True
                    break

            # Detect Claude apologizing for confusion/misunderstanding
            apology_for_confusion_patterns = [
                r'\bapologi[sz]e for (the )?(confusion|misunderstanding)\b',
                r'\bsorry for (the )?(confusion|misunderstanding|not understanding)\b',
                r'\bapologi[sz]e (that )?I (didn\'?t|don\'?t) understand\b',
                r'\bsorry,? I (misunderstood|didn\'?t understand)\b',
                r'\bmy (apologies|mistake).*(confusion|understanding|unclear)\b',
            ]

            for pattern in apology_for_confusion_patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    findings['claude_apologies'].append({
                        'conversation': conv_name,
                        'date': conv_date,
                        'message_index': msg_idx,
                        'text': text[:300],
                        'after_frustration': conv_patterns['frustration_misunderstanding'] > 0
                    })
                    conv_patterns['claude_apologies_for_confusion'] += 1
                    break

            previous_was_vague = False

    # Conversation-level analysis
    if conv_patterns['vague_references'] > 0 or \
       conv_patterns['assumed_context'] > 0 or \
       conv_patterns['frustration_misunderstanding'] > 0:

        # Mind reading assumption score
        mind_reading_score = 0

        # Multiple vague references
        if conv_patterns['vague_references'] >= 3:
            mind_reading_score += 3
        elif conv_patterns['vague_references'] >= 1:
            mind_reading_score += 1

        # Assumed context
        if conv_patterns['assumed_context'] >= 2:
            mind_reading_score += 3
        elif conv_patterns['assumed_context'] >= 1:
            mind_reading_score += 1

        # Frustration at misunderstanding
        if conv_patterns['frustration_misunderstanding'] > 0:
            mind_reading_score += 2

        # Mind reading expectations
        if conv_patterns['mind_reading_expectation'] > 0:
            mind_reading_score += 3

        # Clarification cycles (Claude asks → Benjamin frustrated)
        if conv_patterns['clarification_cycles'] >= 2:
            mind_reading_score += 3
        elif conv_patterns['clarification_cycles'] >= 1:
            mind_reading_score += 2

        # Context never provided
        if conv_patterns['context_never_provided'] > 0:
            mind_reading_score += 2

        # Claude apologies for confusion (reinforcement)
        if conv_patterns['claude_apologies_for_confusion'] >= 2:
            mind_reading_score += 2
        elif conv_patterns['claude_apologies_for_confusion'] >= 1:
            mind_reading_score += 1

        findings['conversations_with_patterns'].append({
            'conversation': conv_name,
            'date': conv_date,
            'vague_references': conv_patterns['vague_references'],
            'assumed_context': conv_patterns['assumed_context'],
            'frustration_misunderstanding': conv_patterns['frustration_misunderstanding'],
            'mind_reading_expectation': conv_patterns['mind_reading_expectation'],
            'implicit_references': conv_patterns['implicit_references'],
            'claude_clarifications': conv_patterns['claude_clarifications'],
            'claude_apologies_for_confusion': conv_patterns['claude_apologies_for_confusion'],
            'clarification_cycles': conv_patterns['clarification_cycles'],
            'context_never_provided': conv_patterns['context_never_provided'],
            'mind_reading_score': mind_reading_score,
            'user_message_count': len(conv_patterns['user_messages']),
            'claude_message_count': len(conv_patterns['claude_messages'])
        })

print(f"Analyzed {total_conversations} conversations")
print(f"Total user messages: {total_user_messages}")
print(f"Total Claude messages: {total_claude_messages}")

# Statistics
print("\n=== QUANTITATIVE FINDINGS ===\n")

print(f"VAGUE REFERENCES: {len(findings['vague_references'])}")
print(f"  - Rate: {len(findings['vague_references']) / total_user_messages * 100:.2f}% of user messages")
after_clarification = len([v for v in findings['vague_references'] if v.get('after_clarification')])
print(f"  - After clarification request: {after_clarification} ({after_clarification/len(findings['vague_references'])*100:.1f}%)")

print(f"\nASSUMED CONTEXT: {len(findings['assumed_context'])}")
print(f"  - Rate: {len(findings['assumed_context']) / total_user_messages * 100:.2f}% of user messages")

print(f"\nFRUSTRATION AT MISUNDERSTANDING: {len(findings['frustration_misunderstanding'])}")
print(f"  - Rate: {len(findings['frustration_misunderstanding']) / total_user_messages * 100:.2f}% of user messages")
after_clarification_frust = len([f for f in findings['frustration_misunderstanding'] if f.get('after_clarification')])
print(f"  - After clarification request: {after_clarification_frust} ({after_clarification_frust/len(findings['frustration_misunderstanding'])*100 if findings['frustration_misunderstanding'] else 0:.1f}%)")

print(f"\nMIND READING EXPECTATION: {len(findings['mind_reading_expectation'])}")

print(f"\nIMPLICIT REFERENCES: {len(findings['implicit_references'])}")

print(f"\nCLAUDE CLARIFICATIONS: {len(findings['claude_clarifications'])}")
after_vague = len([c for c in findings['claude_clarifications'] if c.get('after_vague_reference')])
print(f"  - After vague reference: {after_vague} ({after_vague/len(findings['claude_clarifications'])*100 if findings['claude_clarifications'] else 0:.1f}%)")

print(f"\nCLAUDE APOLOGIES FOR CONFUSION: {len(findings['claude_apologies'])}")
after_frust = len([a for a in findings['claude_apologies'] if a.get('after_frustration')])
print(f"  - After user frustration: {after_frust} ({after_frust/len(findings['claude_apologies'])*100 if findings['claude_apologies'] else 0:.1f}%)")

print(f"\nCONVERSATIONS WITH MIND READING PATTERNS: {len(findings['conversations_with_patterns'])}")
print(f"  - Percentage of total: {len(findings['conversations_with_patterns']) / total_conversations * 100:.1f}%")

# Mind reading analysis
if findings['conversations_with_patterns']:
    avg_score = sum(c['mind_reading_score'] for c in findings['conversations_with_patterns']) / len(findings['conversations_with_patterns'])
    high_score = len([c for c in findings['conversations_with_patterns'] if c['mind_reading_score'] >= 6])
    total_clarification_cycles = sum(c['clarification_cycles'] for c in findings['conversations_with_patterns'])
    total_context_never_provided = sum(c['context_never_provided'] for c in findings['conversations_with_patterns'])
    total_apologies = sum(c['claude_apologies_for_confusion'] for c in findings['conversations_with_patterns'])

    print(f"\nMIND READING ASSUMPTION ANALYSIS:")
    print(f"  - Average mind reading score: {avg_score:.2f}")
    print(f"  - High assumption (score ≥6): {high_score} ({high_score/len(findings['conversations_with_patterns'])*100:.1f}%)")
    print(f"  - Total clarification cycles: {total_clarification_cycles}")
    print(f"  - Context never provided: {total_context_never_provided}")
    print(f"  - Total Claude apologies for confusion: {total_apologies}")

    if total_apologies > 0:
        reinforcement_rate = (total_apologies / len(findings['conversations_with_patterns'])) * 100
        print(f"  - Apology reinforcement rate: {reinforcement_rate:.1f}% of conversations")

# Top examples
print("\n=== TOP VAGUE REFERENCE EXAMPLES ===\n")
for i, ex in enumerate(findings['vague_references'][:15], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   After clarification: {ex.get('after_clarification', False)}")
    print(f"   Text: {ex['text']}\n")

print("\n=== TOP ASSUMED CONTEXT EXAMPLES ===\n")
for i, ex in enumerate(findings['assumed_context'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   Text: {ex['text']}\n")

print("\n=== TOP FRUSTRATION AT MISUNDERSTANDING EXAMPLES ===\n")
for i, ex in enumerate(findings['frustration_misunderstanding'][:10], 1):
    print(f"{i}. {ex['conversation']}")
    print(f"   After clarification: {ex.get('after_clarification', False)}")
    print(f"   Text: {ex['text']}\n")

# High mind reading conversations
print("\n=== HIGH MIND READING ASSUMPTION CONVERSATIONS ===\n")
high_mind_reading_convs = sorted(findings['conversations_with_patterns'],
                                 key=lambda x: x['mind_reading_score'],
                                 reverse=True)[:15]
for i, conv in enumerate(high_mind_reading_convs, 1):
    print(f"{i}. {conv['conversation']}")
    print(f"   Mind reading score: {conv['mind_reading_score']}")
    print(f"   Vague refs: {conv['vague_references']}, Assumed context: {conv['assumed_context']}")
    print(f"   Clarification cycles: {conv['clarification_cycles']}, Context not provided: {conv['context_never_provided']}")
    print(f"   Claude apologies: {conv['claude_apologies_for_confusion']}\n")

# Save findings
output_path = '../../outputs/cycle_5_mind_reading_findings.json'
with open(output_path, 'w') as f:
    json.dump({
        'summary': {
            'total_conversations': total_conversations,
            'total_user_messages': total_user_messages,
            'vague_references_count': len(findings['vague_references']),
            'assumed_context_count': len(findings['assumed_context']),
            'frustration_misunderstanding_count': len(findings['frustration_misunderstanding']),
            'mind_reading_expectation_count': len(findings['mind_reading_expectation']),
            'claude_clarifications_count': len(findings['claude_clarifications']),
            'claude_apologies_count': len(findings['claude_apologies']),
            'conversations_affected': len(findings['conversations_with_patterns']),
            'avg_mind_reading_score': avg_score if findings['conversations_with_patterns'] else 0,
            'high_assumption_count': high_score if findings['conversations_with_patterns'] else 0,
            'total_clarification_cycles': total_clarification_cycles if findings['conversations_with_patterns'] else 0,
            'total_context_never_provided': total_context_never_provided if findings['conversations_with_patterns'] else 0,
            'total_apologies': total_apologies if findings['conversations_with_patterns'] else 0
        },
        'detailed_findings': findings,
        'high_mind_reading_conversations': high_mind_reading_convs[:20]
    }, f, indent=2)

print(f"\nDetailed findings saved to: {output_path}")
print("\nNext: Run semantic analysis on high mind reading conversations")
