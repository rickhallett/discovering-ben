#!/bin/bash
# Remove files from unrelated web development project

echo "Removing unrelated agents..."
rm -f .claude/agents/aceternity-ui-builder.md
rm -f .claude/agents/aceternity-ui-designer.md
rm -f .claude/agents/logging-integration-advisor.md
rm -f .claude/agents/axiom-setup-guide.md
rm -f .claude/agents/logging-integration-recommendations.md
rm -f .claude/agents/prd-breakdown-reviewer.md
rm -f .claude/agents/copy-diff-analyzer.md

echo "Removing unrelated commands..."
rm -f .claude/commands/create-prd.md
rm -f .claude/commands/variant.md
rm -f .claude/commands/implement-prd.md
rm -f .claude/commands/feature-status.md
rm -f .claude/commands/prd-review.md

echo "Removing analysis scripts from other project..."
rm -f .claude/analysis_content.py
rm -f .claude/analysis_projects.py
rm -f .claude/analysis_temporal.py
rm -f .claude/deep_dive_conversations.py
rm -f .claude/results_content.json
rm -f .claude/results_deep_dive.json
rm -f .claude/results_projects.json
rm -f .claude/results_temporal.json

echo "✓ Cleanup complete"
echo ""
echo "Kept (relevant to any project):"
echo "  - commands/ai-commit.md"
echo "  - commands/build-fix.md"
echo "  - agents/readme-updater.md"
echo "  - agents/architecture-documenter.md"
