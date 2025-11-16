#!/usr/bin/env python3
"""
Deep Dive Conversation Analysis - Examines individual conversations in detail
"""
import json
from datetime import datetime
from collections import defaultdict, Counter
import re

def analyze_conversations_deep(conversations_path):
    with open(conversations_path, 'r') as f:
        conversations = json.load(f)

    results = {
        'longest_conversations': [],
        'most_messages': [],
        'interaction_styles': {
            'question_types': Counter(),
            'request_types': Counter(),
        },
        'topic_breakdown': defaultdict(list),
        'conversation_outcomes': [],
    }

    # Categorize conversations
    legal_keywords = ['complaint', 'legal', 'letter', 'nhs', 'priory', 'compensation', 'sue', 'litigation']
    tech_keywords = ['apple', 'iphone', 'macbook', 'router', 'cable', 'remote', 'streaming', 'tv']
    personal_keywords = ['meditation', 'spiritual', 'supplement', 'diet', 'swimming', 'autism']
    financial_keywords = ['loan', 'benefits', 'application', 'credit', 'money', 'finance']

    for conv in conversations:
        title = conv.get('name', '').lower()
        summary = conv.get('summary', '').lower()
        messages = conv.get('chat_messages', [])

        created = datetime.fromisoformat(conv['created_at'].replace('Z', '+00:00'))
        updated = datetime.fromisoformat(conv['updated_at'].replace('Z', '+00:00'))
        duration_hours = (updated - created).total_seconds() / 3600

        conv_data = {
            'title': conv.get('name', ''),
            'created': created.strftime('%Y-%m-%d %H:%M'),
            'message_count': len(messages),
            'duration_hours': round(duration_hours, 2),
        }

        # Categorize by topic
        categories = []
        for keyword in legal_keywords:
            if keyword in title or keyword in summary:
                categories.append('legal')
                break

        for keyword in tech_keywords:
            if keyword in title or keyword in summary:
                categories.append('tech')
                break

        for keyword in personal_keywords:
            if keyword in title or keyword in summary:
                categories.append('personal')
                break

        for keyword in financial_keywords:
            if keyword in title or keyword in summary:
                categories.append('financial')
                break

        if not categories:
            categories.append('other')

        for cat in categories:
            results['topic_breakdown'][cat].append(conv_data)

        # Track longest conversations
        if duration_hours > 1:
            results['longest_conversations'].append({
                'title': conv.get('name', ''),
                'duration_hours': round(duration_hours, 2),
                'messages': len(messages),
                'date': created.strftime('%Y-%m-%d')
            })

        # Track conversations with most messages
        if len(messages) > 30:
            results['most_messages'].append({
                'title': conv.get('name', ''),
                'messages': len(messages),
                'duration_hours': round(duration_hours, 2),
                'date': created.strftime('%Y-%m-%d')
            })

        # Analyze first user message for interaction patterns
        if messages:
            first_user = next((m for m in messages if m.get('sender') == 'human'), None)
            if first_user:
                first_text = first_user.get('text', '').lower()

                # Question patterns
                if '?' in first_text:
                    results['interaction_styles']['question_types']['question'] += 1
                elif first_text.startswith(('find', 'search', 'look for', 'get')):
                    results['interaction_styles']['request_types']['search_request'] += 1
                elif first_text.startswith(('write', 'create', 'draft', 'compose')):
                    results['interaction_styles']['request_types']['creation_request'] += 1
                elif first_text.startswith(('help', 'can you', 'could you')):
                    results['interaction_styles']['request_types']['help_request'] += 1
                else:
                    results['interaction_styles']['request_types']['direct_statement'] += 1

    # Sort results
    results['longest_conversations'] = sorted(
        results['longest_conversations'],
        key=lambda x: x['duration_hours'],
        reverse=True
    )[:10]

    results['most_messages'] = sorted(
        results['most_messages'],
        key=lambda x: x['messages'],
        reverse=True
    )[:10]

    # Category statistics
    results['category_stats'] = {}
    for cat, convs in results['topic_breakdown'].items():
        results['category_stats'][cat] = {
            'count': len(convs),
            'total_messages': sum(c['message_count'] for c in convs),
            'avg_messages': round(sum(c['message_count'] for c in convs) / len(convs), 1) if convs else 0,
            'avg_duration_hours': round(sum(c['duration_hours'] for c in convs) / len(convs), 2) if convs else 0
        }

    # Remove large data before output
    del results['topic_breakdown']

    return results

if __name__ == '__main__':
    results = analyze_conversations_deep('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json')
    print(json.dumps(results, indent=2, default=str))
