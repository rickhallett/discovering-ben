#!/bin/bash
# Quick fix script to update paths in moved detector and analyzer scripts
# Run from repository root

set -e

echo "Fixing paths in detector scripts..."

# Update all detector scripts
for file in analysis/wave-1-vicious-cycles/scripts/detectors/*.py; do
    if [ -f "$file" ]; then
        echo "  Updating $(basename $file)..."
        # Fix conversations.json path (3 levels -> 4 levels)
        sed -i.bak "s|'../../../data/raw/conversations.json'|'../../../../data/raw/conversations.json'|g" "$file"
        sed -i.bak "s|\"../../../data/raw/conversations.json\"|\"../../../../data/raw/conversations.json\"|g" "$file"
        rm "${file}.bak" 2>/dev/null || true
    fi
done

echo "Fixing paths in semantic analyzer scripts..."

# Update all semantic analyzer scripts
for file in analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/*.py; do
    if [ -f "$file" ]; then
        echo "  Updating $(basename $file)..."
        # Fix findings input paths
        sed -i.bak "s|'../../outputs/|'../../outputs/|g" "$file"
        sed -i.bak "s|\"../../outputs/|\"../../outputs/|g" "$file"
        # Fix conversations.json path (3 levels -> 4 levels)
        sed -i.bak "s|'../../../data/raw/conversations.json'|'../../../../data/raw/conversations.json'|g" "$file"
        sed -i.bak "s|\"../../../data/raw/conversations.json\"|\"../../../../data/raw/conversations.json\"|g" "$file"
        rm "${file}.bak" 2>/dev/null || true
    fi
done

echo ""
echo "✓ Path fixes complete!"
echo ""
echo "All scripts updated to use:"
echo "  - Data: ../../../../data/raw/conversations.json"
echo "  - Outputs: ../../outputs/"
echo ""
echo "Test with:"
echo "  cd analysis/wave-1-vicious-cycles/scripts/detectors"
echo "  python3 cycle_1_information_overload_detector.py"
