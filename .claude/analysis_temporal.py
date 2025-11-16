#!/usr/bin/env python3
"""
Temporal Analysis Agent - Analyzes usage patterns over time
"""
import json
from datetime import datetime
from collections import defaultdict, Counter
import statistics

def analyze_temporal_patterns(conversations_path):
    with open(conversations_path, 'r') as f:
        conversations = json.load(f)

    results = {
        'total_conversations': len(conversations),
        'date_range': {},
        'monthly_activity': defaultdict(int),
        'weekly_activity': defaultdict(int),
        'hourly_activity': defaultdict(int),
        'conversation_lengths': [],
        'message_counts': [],
        'session_gaps': [],
        'peak_periods': {},
    }

    timestamps = []

    for conv in conversations:
        created = datetime.fromisoformat(conv['created_at'].replace('Z', '+00:00'))
        updated = datetime.fromisoformat(conv['updated_at'].replace('Z', '+00:00'))

        timestamps.append(created)

        # Monthly aggregation
        month_key = created.strftime('%Y-%m')
        results['monthly_activity'][month_key] += 1

        # Weekly aggregation (day of week)
        day_name = created.strftime('%A')
        results['weekly_activity'][day_name] += 1

        # Hourly aggregation
        hour = created.hour
        results['hourly_activity'][hour] += 1

        # Conversation characteristics
        message_count = len(conv.get('chat_messages', []))
        results['message_counts'].append(message_count)

        # Calculate conversation duration
        duration = (updated - created).total_seconds() / 3600  # hours
        results['conversation_lengths'].append(duration)

    # Calculate date range
    if timestamps:
        timestamps.sort()
        results['date_range'] = {
            'first_conversation': timestamps[0].isoformat(),
            'last_conversation': timestamps[-1].isoformat(),
            'span_days': (timestamps[-1] - timestamps[0]).days
        }

        # Calculate gaps between conversations
        for i in range(1, len(timestamps)):
            gap_hours = (timestamps[i] - timestamps[i-1]).total_seconds() / 3600
            results['session_gaps'].append(gap_hours)

    # Statistics on conversation lengths
    if results['conversation_lengths']:
        results['conversation_duration_stats'] = {
            'mean_hours': statistics.mean(results['conversation_lengths']),
            'median_hours': statistics.median(results['conversation_lengths']),
            'max_hours': max(results['conversation_lengths']),
            'min_hours': min(results['conversation_lengths'])
        }

    # Statistics on message counts
    if results['message_counts']:
        results['message_stats'] = {
            'mean': statistics.mean(results['message_counts']),
            'median': statistics.median(results['message_counts']),
            'max': max(results['message_counts']),
            'min': min(results['message_counts']),
            'total_messages': sum(results['message_counts'])
        }

    # Identify peak activity periods
    if results['hourly_activity']:
        sorted_hours = sorted(results['hourly_activity'].items(), key=lambda x: x[1], reverse=True)
        results['peak_periods']['top_hours'] = sorted_hours[:5]

    if results['weekly_activity']:
        sorted_days = sorted(results['weekly_activity'].items(), key=lambda x: x[1], reverse=True)
        results['peak_periods']['top_days'] = sorted_days[:3]

    if results['monthly_activity']:
        sorted_months = sorted(results['monthly_activity'].items(), key=lambda x: x[1], reverse=True)
        results['peak_periods']['top_months'] = sorted_months[:5]

    # Convert defaultdicts to regular dicts for JSON serialization
    results['monthly_activity'] = dict(sorted(results['monthly_activity'].items()))
    results['weekly_activity'] = dict(results['weekly_activity'])
    results['hourly_activity'] = dict(sorted(results['hourly_activity'].items()))

    return results

if __name__ == '__main__':
    results = analyze_temporal_patterns('/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/conversations.json')
    print(json.dumps(results, indent=2, default=str))
