#!/bin/bash
# Organize root level files

# Move and lowercase documentation guides
mv PATH_FIX_SUMMARY.md docs/guides/path-fix-summary.md
mv RESTRUCTURE_GUIDE.md docs/guides/restructure-guide.md

# Archive old analysis files
mv exploratory_analysis_report.md archive/
mv follow_up_priorities.md archive/
mv quick_reference_summary.md archive/

# Move scripts to tools/
mv restructure.sh tools/
mv fix-paths.sh tools/

# Archive MCP server data files (not research data)
mv claude_response_analysis.json archive/mcp-data/
mv memories.json archive/mcp-data/
mv pattern_analysis.json archive/mcp-data/
mv projects.json archive/mcp-data/
mv users.json archive/mcp-data/

echo "✓ Files organized and lowercased"
