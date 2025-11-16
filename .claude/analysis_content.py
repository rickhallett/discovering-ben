#!/usr/bin/env python3
"""
Content Analysis Agent - Analyzes conversation topics, themes, and content patterns
"""
import json
import re
from collections import Counter, defaultdict

def extract_keywords(text, min_length=4):
    """Extract meaningful keywords from text"""
    if not text:
        return []

    # Remove common words
    stop_words = {
        'the', 'this', 'that', 'with', 'from', 'have', 'been', 'were', 'will',
        'your', 'what', 'how', 'can', 'could', 'would', 'should', 'about',
        'into', 'through', 'than', 'them', 'these', 'those', 'their', 'which',
        'when', 'where', 'who', 'why', 'all', 'each', 'other', 'some', 'such'
    }

    words = re.findall(r'\b[a-z]+\b', text.lower())
    keywords = [w for w in words if len(w) >= min_length and w not in stop_words]
    return keywords

def analyze_content_patterns(conversations_path):
    with open(conversations_path, 'r') as f:
        conversations = json.load(f)

    results = {
        'conversation_titles': [],
        'conversation_summaries': [],
        'title_keywords': Counter(),
        'summary_keywords': Counter(),
        'topic_clusters': defaultdict(list),
        'message_patterns': {
            'user_message_lengths': [],
            'assistant_message_lengths': [],
            'total_user_messages': 0,
            'total_assistant_messages': 0,
        },
        'conversation_starters': [],
        'tech_stack_mentions': Counter(),
        'domain_indicators': Counter(),
    }

    # Technology and domain keywords to track
    tech_keywords = {
        'python', 'javascript', 'typescript', 'react', 'vue', 'angular', 'node',
        'django', 'flask', 'fastapi', 'api', 'rest', 'graphql', 'sql', 'nosql',
        'mongodb', 'postgres', 'mysql', 'redis', 'docker', 'kubernetes', 'aws',
        'azure', 'gcp', 'cloud', 'machine learning', 'ml', 'ai', 'data', 'analytics'
    }

    domain_keywords = {
        'business', 'startup', 'product', 'design', 'architecture', 'system',
        'security', 'performance', 'testing', 'deployment', 'infrastructure',
        'frontend', 'backend', 'database', 'mobile', 'web', 'application'
    }

    for conv in conversations:
        # Analyze titles
        title = conv.get('name', '')
        if title:
            results['conversation_titles'].append(title)
            title_words = extract_keywords(title)
            results['title_keywords'].update(title_words)

        # Analyze summaries
        summary = conv.get('summary', '')
        if summary:
            results['conversation_summaries'].append(summary)
            summary_words = extract_keywords(summary)
            results['summary_keywords'].update(summary_words)

        # Analyze messages
        messages = conv.get('chat_messages', [])
        if messages and len(messages) > 0:
            # Get first user message as conversation starter
            first_user_msg = next((m for m in messages if m.get('sender') == 'human'), None)
            if first_user_msg:
                first_text = first_user_msg.get('text', '')[:200]  # First 200 chars
                results['conversation_starters'].append({
                    'title': title,
                    'first_message': first_text
                })

        for msg in messages:
            sender = msg.get('sender', '')
            text = msg.get('text', '')

            if sender == 'human':
                results['message_patterns']['total_user_messages'] += 1
                results['message_patterns']['user_message_lengths'].append(len(text))
            elif sender == 'assistant':
                results['message_patterns']['total_assistant_messages'] += 1
                results['message_patterns']['assistant_message_lengths'].append(len(text))

            # Track technology mentions
            text_lower = text.lower()
            for tech in tech_keywords:
                if tech in text_lower:
                    results['tech_stack_mentions'][tech] += 1

            # Track domain mentions
            for domain in domain_keywords:
                if domain in text_lower:
                    results['domain_indicators'][domain] += 1

    # Get top keywords
    results['top_title_keywords'] = results['title_keywords'].most_common(30)
    results['top_summary_keywords'] = results['summary_keywords'].most_common(30)
    results['top_tech_mentions'] = results['tech_stack_mentions'].most_common(20)
    results['top_domains'] = results['domain_indicators'].most_common(20)

    # Calculate message statistics
    if results['message_patterns']['user_message_lengths']:
        import statistics
        results['message_patterns']['user_avg_length'] = statistics.mean(
            results['message_patterns']['user_message_lengths']
        )
        results['message_patterns']['user_median_length'] = statistics.median(
            results['message_patterns']['user_message_lengths']
        )

    if results['message_patterns']['assistant_message_lengths']:
        import statistics
        results['message_patterns']['assistant_avg_length'] = statistics.mean(
            results['message_patterns']['assistant_message_lengths']
        )
        results['message_patterns']['assistant_median_length'] = statistics.median(
            results['message_patterns']['assistant_message_lengths']
        )

    # Remove large arrays before output, keep only samples
    results['conversation_titles_sample'] = results['conversation_titles'][:20]
    results['conversation_starters_sample'] = results['conversation_starters'][:10]
    del results['conversation_titles']
    del results['conversation_summaries']
    del results['conversation_starters']
    del results['title_keywords']
    del results['summary_keywords']
    del results['tech_stack_mentions']
    del results['domain_indicators']
    del results['message_patterns']['user_message_lengths']
    del results['message_patterns']['assistant_message_lengths']

    return results

if __name__ == '__main__':
    results = analyze_content_patterns('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json')
    print(json.dumps(results, indent=2, default=str))
