#!/usr/bin/env python3
"""
Projects & Memories Analysis Agent - Analyzes project usage and memory patterns
"""
import json
from datetime import datetime
from collections import Counter

def analyze_projects_and_memories(projects_path, memories_path):
    with open(projects_path, 'r') as f:
        projects = json.load(f)

    with open(memories_path, 'r') as f:
        memories = json.load(f)

    results = {
        'projects': {
            'total_count': len(projects),
            'private_count': 0,
            'starter_projects': 0,
            'custom_projects': 0,
            'projects_with_docs': 0,
            'project_names': [],
            'project_descriptions': [],
            'creation_timeline': [],
        },
        'memories': {
            'total_entries': 0,
            'project_memories_count': 0,
            'conversation_memory_present': False,
        }
    }

    # Analyze projects
    for proj in projects:
        if proj.get('is_private'):
            results['projects']['private_count'] += 1

        if proj.get('is_starter_project'):
            results['projects']['starter_projects'] += 1
        else:
            results['projects']['custom_projects'] += 1

        if proj.get('docs') and len(proj['docs']) > 0:
            results['projects']['projects_with_docs'] += 1

        results['projects']['project_names'].append({
            'name': proj.get('name', ''),
            'description': proj.get('description', '')[:100] if proj.get('description') else '',
            'created_at': proj.get('created_at', ''),
            'is_starter': proj.get('is_starter_project', False)
        })

        if proj.get('created_at'):
            created = datetime.fromisoformat(proj['created_at'].replace('Z', '+00:00'))
            results['projects']['creation_timeline'].append({
                'date': created.strftime('%Y-%m'),
                'name': proj.get('name', '')
            })

    # Sort projects by creation date
    results['projects']['project_names'].sort(key=lambda x: x['created_at'], reverse=True)

    # Analyze memories
    if memories and len(memories) > 0:
        mem = memories[0]  # Assuming single memory object

        conv_memory = mem.get('conversations_memory', '')
        if conv_memory:
            results['memories']['conversation_memory_present'] = True
            results['memories']['conversation_memory_length'] = len(conv_memory)
            results['memories']['conversation_memory_preview'] = conv_memory[:500]

        proj_memories = mem.get('project_memories', [])

        if isinstance(proj_memories, list):
            results['memories']['project_memories_count'] = len(proj_memories)
            if proj_memories:
                results['memories']['project_memory_details'] = []
                for pm in proj_memories:
                    if isinstance(pm, dict):
                        results['memories']['project_memory_details'].append({
                            'project_uuid': pm.get('project_uuid', ''),
                            'memory_length': len(pm.get('memory', '')),
                            'memory_preview': pm.get('memory', '')[:200]
                        })
        else:
            results['memories']['project_memories_count'] = 0

    return results

if __name__ == '__main__':
    results = analyze_projects_and_memories(
        '/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/projects.json',
        '/Users/richardhallett/Documents/code/clients/project-ben/discovering-ben/memories.json'
    )
    print(json.dumps(results, indent=2, default=str))
