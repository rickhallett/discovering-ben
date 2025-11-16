# Path Fix Summary

## Issue

When moving scripts to the new structure, the relative paths needed updating. The initial restructure script had an error calculating the correct number of directory levels.

## What Was Fixed

### Problem
Scripts in `analysis/wave-1-vicious-cycles/scripts/detectors/` and `semantic-analyzers/` couldn't find `conversations.json` because the path calculation was wrong.

**Incorrect path (3 levels up):**
```python
'../../../data/raw/conversations.json'
```

**Correct path (4 levels up):**
```python
'../../../../data/raw/conversations.json'
```

### Directory Structure
```
discovering-ben/                                    # Root
├── data/
│   └── raw/
│       └── conversations.json                      # Target file
└── analysis/
    └── wave-1-vicious-cycles/
        └── scripts/
            ├── detectors/
            │   └── cycle_1_*.py                    # Scripts here
            └── semantic-analyzers/
                └── cycle_1_*.py                    # Scripts here
```

**From detectors/ to conversations.json:**
1. `../` → scripts/
2. `../../` → wave-1-vicious-cycles/
3. `../../../` → analysis/
4. `../../../../` → discovering-ben/ (root)
5. `../../../../data/raw/conversations.json` ✓

## Solution Applied

### Automated Fix Script

Created `fix-paths.sh` to update all 14 scripts (7 detectors + 7 semantic analyzers):

```bash
#!/bin/bash
# Updates all detector and analyzer scripts with correct paths

for file in analysis/wave-1-vicious-cycles/scripts/detectors/*.py; do
    sed -i.bak "s|'../../../data/raw/|'../../../../data/raw/|g" "$file"
    rm "${file}.bak"
done

for file in analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/*.py; do
    sed -i.bak "s|'../../../data/raw/|'../../../../data/raw/|g" "$file"
    rm "${file}.bak"
done
```

**Run with:**
```bash
./fix-paths.sh
```

### Files Updated

**Detector Scripts (7):**
- ✓ `cycle_1_information_overload_detector.py`
- ✓ `cycle_2_one_best_thing_detector.py`
- ✓ `cycle_3_perfectionism_escalation_detector.py`
- ✓ `cycle_4_emotional_dysregulation_detector.py`
- ✓ `cycle_5_mind_reading_detector.py`
- ✓ `cycle_6_system_building_detector.py`
- ✓ `cycle_7_special_interest_detector.py`

**Semantic Analyzer Scripts (7):**
- ✓ `cycle_1_semantic_analyzer.py`
- ✓ `cycle_2_semantic_analyzer.py`
- ✓ `cycle_3_semantic_analyzer.py`
- ✓ `cycle_4_semantic_analyzer.py`
- ✓ `cycle_5_semantic_analyzer.py`
- ✓ `cycle_6_semantic_analyzer.py`
- ✓ `cycle_7_semantic_analyzer.py`

### Also Updated

**restructure.sh** - Fixed the automated migration script so future restructures work correctly.

## Verification

Tested successfully:
```bash
cd analysis/wave-1-vicious-cycles/scripts/detectors
python3 cycle_1_information_overload_detector.py
# ✓ Loaded conversations successfully
# ✓ Saved output to ../../outputs/
```

## Current Paths (All Correct)

**Data Input:**
- Detectors: `../../../../data/raw/conversations.json`
- Semantic analyzers: `../../../../data/raw/conversations.json`

**Findings Input (for semantic analyzers):**
- `../../outputs/cycle_X_*_findings.json`

**Output:**
- Detectors: `../../outputs/cycle_X_*_findings.json`
- Semantic analyzers: `../../outputs/cycle_X_semantic_findings.json`

## For Future Reference

When adding new scripts to:
- `analysis/wave-1-vicious-cycles/scripts/detectors/` or
- `analysis/wave-1-vicious-cycles/scripts/semantic-analyzers/`

Use these paths:
```python
# Data input
with open('../../../../data/raw/conversations.json', 'r') as f:

# Output
output_path = '../../outputs/filename.json'
```

## Quick Reference

From any detector or semantic analyzer script location:

```
Current location:  analysis/wave-1-vicious-cycles/scripts/{detectors|semantic-analyzers}/
Up 1 level (../):  scripts/
Up 2 levels (../../):  wave-1-vicious-cycles/
Up 3 levels (../../../):  analysis/
Up 4 levels (../../../../):  discovering-ben/ (ROOT)

Data:    ../../../../data/raw/conversations.json
Outputs: ../../outputs/
```
