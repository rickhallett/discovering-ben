# Wave 1 Outputs: Planning & Architecture

**Completed:** Day 1
**Agents Used:** Planner (Gemini 2.5 Pro), Consensus (GPT-5 Pro + Gemini 2.5 Pro)

---

## 1. Consensus Decision: Homepage Structure

### Question
"Should the website homepage lead with Benjamin's personal story (humanizing, relatable) or with academic research framing (credibility, methodology)?"

### Model Perspectives

**GPT-5 Pro (FOR story-first): 8/10 confidence**
- Lead with 2-3 sentence narrative + quote
- Anchor with above-the-fold methods capsule + CTAs
- Emphasizes: engagement, community trust, accessibility
- Privacy: quote-level risk scoring, [redacted] markers
- Hybrid: Story hero → methods CTA bar

**Gemini 2.5 Pro (AGAINST, FOR academic): 9/10 confidence**
- Lead with academic abstract/research framework
- Link prominently to "Benjamin's Story" as case study
- Emphasizes: credibility, citations, long-term impact
- Privacy: simplified via aggregated data first
- Hybrid: Academic abstract → "Read Case Study" CTA

### Final Consensus Recommendation: Dual-Entry Hybrid

**Homepage Structure:**

```
┌─────────────────────────────────────────────────┐
│ HERO SECTION (Above-the-fold)                   │
│                                                  │
│ [1] Research Framing (1 sentence)               │
│     "A 16-month study of autism-LLM              │
│      interaction patterns"                       │
│                                                  │
│ [2] Story Hook (2-3 sentences)                  │
│     Brief Benjamin context                       │
│                                                  │
│ [3] Key Finding Highlight                       │
│     "4 vicious cycles identified"                │
│                                                  │
│ [4] DUAL CTAs (Equal weight, prominent)         │
│     ┌─────────────────┐  ┌──────────────────┐  │
│     │ Read Research   │  │ Benjamin's Story │  │
│     │ → Methodology   │  │ → Case Study     │  │
│     └─────────────────┘  └──────────────────┘  │
│                                                  │
│ [5] Methods Capsule (Compact, visible)          │
│     1 paragraph: n=1 longitudinal, 255 convos,  │
│     ethical considerations → Full methodology   │
│                                                  │
│ [6] Privacy Statement (Footer area)             │
│     "How we protect privacy" (expandable)       │
└─────────────────────────────────────────────────┘
```

**Rationale:**
- Satisfies Gemini's credibility concern (research framing first line)
- Satisfies GPT-5's engagement concern (story hook immediately follows)
- Gives users choice via dual equal CTAs
- Balances privacy complexity (medium-high)
- Serves all audiences

**Confidence:** 8.5/10

**Privacy Implementation:**
- Medium-high complexity (between GPT-5's high and Gemini's low)
- Quote-level anonymization for story elements
- Aggregated data for research elements
- Estimated 1.5 weeks for privacy workflow

---

## 2. Implementation Plan: 40 Pages Across 7 Waves

### Content Breakdown

**Total Pages:** 40
**Groups:** 10
**Parallel Waves:** 7

### Page Groups and Dependencies

**Group 1: Foundation Pages (CRITICAL FIRST) - 4 pages**
- resources/glossary.md → MUST complete before all others
- overview/research-question.md
- overview/key-findings.md
- index.md → depends on Consensus decision (✓ complete)

**Group 2: Audience Landing Pages - 4 pages**
- overview/for-researchers.md
- overview/for-autistic-individuals.md
- overview/for-clinicians.md
- overview/for-llm-developers.md
*Dependency: glossary.md*

**Group 3: Background Context - 4 pages**
- background/autism-traits.md (NEW)
- background/llm-behavior-patterns.md (NEW)
- background/previous-research.md (NEW)
- background/neurodivergent-ai-interaction.md (ADAPT existing)

**Group 4: Methodology - 5 pages**
- methodology/overview.md (ADAPT from wave-1 README)
- methodology/data-collection.md (NEW)
- methodology/two-stage-detection.md (NEW)
- methodology/ethical-considerations.md (NEW)
- methodology/replication-guide.md (NEW)

**Group 5: Cycle Pages - 8 pages**
- cycles/overview.md (ADAPT from cycles-summary)
- cycles/cycle-1-information-overload.md (ADAPT)
- cycles/cycle-2-one-best-thing.md (ADAPT)
- cycles/cycle-3-perfectionism.md (ADAPT)
- cycles/cycle-4-emotional-dysregulation.md (ADAPT)
- cycles/cycle-5-mind-reading.md (ADAPT)
- cycles/cycle-6-system-building.md (ADAPT)
- cycles/cycle-7-special-interests.md (ADAPT)
*Dependency: Content audit, privacy review framework*

**Group 6: Interventions - 5 pages**
- interventions/overview.md (ADAPT)
- interventions/system-prompt-approach.md (NEW)
- interventions/recommendations.md (ADAPT)
- interventions/example-prompts.md (ADAPT, heavy anonymization)
- interventions/implementation-guide.md (NEW)

**Group 7: Case Studies - 4 pages**
- case-studies/information-overload-example.md (EXTRACT from cycle 1)
- case-studies/perfectionism-spiral-example.md (EXTRACT from cycle 3)
- case-studies/successful-intervention-example.md (IF DATA EXISTS)
- case-studies/natural-trait-example.md (EXTRACT from cycle 7)
*Dependency: Secaudit review*

**Group 8: Implications - 4 pages**
- implications/for-llm-design.md (NEW)
- implications/for-clinical-practice.md (NEW)
- implications/for-accessibility.md (NEW)
- implications/future-research.md (NEW)

**Group 9: Resources - 3 pages**
- resources/further-reading.md (NEW)
- resources/contact.md (NEW)
- resources/contribute.md (NEW)

**Group 10: Appendices - 4 pages**
- appendices/dataset-statistics.md (NEW)
- appendices/pattern-definitions.md (EXTRACT)
- appendices/llm-contribution-calculation.md (EXTRACT)
- appendices/limitations.md (NEW)

---

## 3. Wave Execution Plan

### Critical Path Dependencies

```
Consensus Decision (✓) → index.md framing
                      ↓
Glossary Creation → All technical writing
                      ↓
Analyze Agent Audit → Content adaptation strategy
                      ↓
Foundation Pages → Audience landing pages
                      ↓
Privacy Framework → Case study extraction
                      ↓
All Content → QA Gates
```

### Wave 2: Core Content Creation (Days 2-3)

**Sequential:** Glossary MUST complete first
**Then Parallel:** 8 agents

```
Agent 1 (FIRST):
└─ resources/glossary.md
   │
   ├─ Extract terms from all cycle analyses
   ├─ Define autism terminology
   ├─ Define LLM terminology
   └─ Define research methodology terms

   ↓ BLOCKS until complete ↓

Agents 2-9 (PARALLEL):
├─ Agent 2: overview/research-question.md
├─ Agent 3: overview/key-findings.md
├─ Agent 4: index.md (dual-entry hybrid)
├─ Agent 5: methodology/overview.md
├─ Agent 6: overview/for-researchers.md
├─ Agent 7: overview/for-autistic-individuals.md
├─ Agent 8: overview/for-clinicians.md
└─ Agent 9: overview/for-llm-developers.md
```

### Wave 3-7 (As Per Strategy Document)

All subsequent waves proceed as planned in mkdocs-parallel-agent-strategy.md

---

## 4. Risk Assessment

### High Risk

**Privacy leaks in case studies**
- Threat: PII exposure, re-identification
- Mitigation: Secaudit agent + manual family review
- Status: Privacy framework in development

**Consensus decision delays homepage**
- Threat: Blocked Wave 2 index.md creation
- Mitigation: Running now
- Status: ✓ RESOLVED - dual-entry hybrid decided

**Cycle 5 analysis missing**
- Threat: Incomplete cycle coverage
- Mitigation: Check if analysis exists
- Status: PENDING verification

### Medium Risk

**Content consistency across 40 pages**
- Threat: Terminology conflicts, tone variation
- Mitigation: Glossary first, Refactor agent review
- Status: Glossary prioritized in Wave 2

**Timeline pressure**
- Threat: 8-day deadline too aggressive
- Mitigation: Maximum parallelization
- Status: On track with current plan

### Low Risk

**Technical setup**
- Threat: MkDocs configuration issues
- Mitigation: Well-documented, mature tool
- Status: Low concern

---

## 5. Next Immediate Actions

1. **Complete Analyze agent content audit** (remaining Wave 1 task)
   - Read cycle analysis documents
   - Identify reusable content
   - Flag privacy concerns
   - Map content gaps

2. **Document Wave 1 outputs** (✓ THIS FILE)

3. **Launch Wave 2: Glossary Agent**
   - CRITICAL FIRST
   - Extract terminology from all sources
   - Create comprehensive glossary
   - Block other Wave 2 agents until complete

4. **Monitor glossary completion**
   - When complete, launch Wave 2 Group A/B agents (8 parallel)

---

## 6. Timeline Status

```
┌──────────┬─────────────────────────────────────┐
│ Wave     │ Status                              │
├──────────┼─────────────────────────────────────┤
│ Wave 1   │ ✓ COMPLETE (Day 1)                  │
│          │ - Planner: Implementation plan      │
│          │ - Consensus: Homepage structure     │
│          │ - Analyze: PENDING content audit    │
├──────────┼─────────────────────────────────────┤
│ Wave 2-7 │ Ready to execute                    │
│          │ On track for 7-day completion       │
├──────────┼─────────────────────────────────────┤
│ Total    │ 8 days to launch (on schedule)      │
└──────────┴─────────────────────────────────────┘
```

---

## 7. Key Decisions Made

1. **Homepage: Dual-Entry Hybrid Approach**
   - Research framing (1 sentence) + story hook (2-3 sentences)
   - Dual equal CTAs: "Read Research" + "Benjamin's Story"
   - Compact methods capsule
   - Privacy statement in footer

2. **Content Strategy: 40 Pages Across 10 Groups**
   - 23 new pages
   - 13 adapted pages
   - 4 technical pages

3. **Dependencies: Glossary-First Approach**
   - Glossary must complete before technical writing begins
   - Ensures terminology consistency across 40 pages

4. **Privacy: Medium-High Complexity**
   - Quote-level anonymization for narratives
   - Aggregated data for research sections
   - 1.5 weeks estimated for privacy workflow

5. **Parallelization: Maximum Efficiency**
   - Wave 2: 9 agents (1 sequential, 8 parallel)
   - Wave 3: 7 agents parallel
   - Wave 4: 9 agents parallel
   - Waves 5-7: As planned

---

## Appendix: Agent Details

### Consensus Agent
- Models: GPT-5 Pro (for), Gemini 2.5 Pro (against)
- Claude Sonnet 4.5 unavailable (API limitation)
- Outcome: Synthesized dual-entry hybrid approach
- Confidence: 8.5/10

### Planner Agent
- Model: Gemini 2.5 Pro
- Steps: 3 (completed)
- Deliverables:
  - 40-page content breakdown
  - Dependency mapping
  - Risk assessment
  - Wave execution plan

### Analyze Agent
- Model: Gemini 2.5 Pro
- Status: Paused (awaiting file reading)
- Files to analyze: 7 cycle analysis documents
- Purpose: Content audit for adaptation strategy
