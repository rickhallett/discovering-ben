# Parallel Claude Subagent Strategy for MkDocs Website Development

## Overview

Leverage Claude Code's Task tool and MCP Zen tools to orchestrate parallel development of the MkDocs website. This approach can reduce development time from weeks to days while improving content quality through specialized agent expertise.

## Available Agent Capabilities

### Claude Code Built-in Agents

**Content Creation:**
- `general-purpose` - Complex multi-step content creation tasks
- `dev-docs-generator` - Generate comprehensive developer documentation
- `architecture-documenter` - Create architecture documentation

**Analysis & Planning:**
- `Explore` - Fast codebase/content exploration (quick/medium/thorough modes)
- `Plan` - Complex project planning with sequential steps

**Content Management:**
- `readme-updater` - Keep documentation synchronized
- `copy-diff-analyzer` - Analyze content changes, create implementation guides

### MCP Zen Tools

**Strategic Planning:**
- `planner` - Interactive sequential planning with revision/branching
- `consensus` - Multi-model analysis for controversial decisions
- `thinkdeep` - Complex problem analysis with hypothesis testing

**Content Analysis:**
- `analyze` - Comprehensive code/content analysis
- `refactor` - Content reorganization and improvement
- `tracer` - Trace dependencies between documents
- `docgen` - Generate documentation from code

**Quality Assurance:**
- `codereview` - Review mkdocs.yml and configuration
- `precommit` - Validate changes before publishing
- `secaudit` - Security audit for privacy concerns

**Collaboration:**
- `chat` - Brainstorming and ideation
- `clink` - Link to external AI CLIs (Gemini, etc.)

## Parallel Development Waves

### Wave 1: Planning & Architecture (Day 1)

**Agent Orchestration:**

1. **Planner Agent** - Overall project breakdown
   - Input: MkDocs plan, existing content inventory
   - Output: Detailed implementation phases with dependencies
   - Deliverable: `mkdocs-implementation-plan.md`

2. **Consensus Agent** - Critical decisions
   - Questions:
     - "Should we prioritize researcher or autistic individual audience first?"
     - "What level of technical detail in methodology section?"
     - "How to balance privacy with transparency?"
   - Models: Use 3-5 different models with different stances
   - Deliverable: `design-decisions.md`

3. **Analyze Agent** - Existing content analysis
   - Input: All cycle analysis docs, system prompts, methodology
   - Output: Content inventory, gaps, reuse opportunities
   - Deliverable: `content-audit.md`

**Parallel Execution:**
```bash
# Launch all three agents simultaneously in one message
Task(planner) + Task(consensus) + Task(analyze)
```

**Output:** Clear roadmap, resolved design decisions, content inventory

---

### Wave 2: Content Creation - Core Research (Days 2-3)

**Parallel Agent Assignment (9 agents running simultaneously):**

#### Group A: Audience Landing Pages (4 agents)
1. **General-Purpose Agent A** → `overview/for-researchers.md`
   - Extract research methodology, statistics
   - Academic tone, citation-ready
   - Include limitations and future research

2. **General-Purpose Agent B** → `overview/for-autistic-individuals.md`
   - Empathetic, practical tone
   - Self-assessment elements
   - Normalize patterns, provide hope

3. **General-Purpose Agent C** → `overview/for-clinicians.md`
   - Clinical application focus
   - Intervention frameworks
   - Safety considerations

4. **General-Purpose Agent D** → `overview/for-llm-developers.md`
   - Technical recommendations
   - UX/UI implications
   - Implementation examples

#### Group B: Methodology Pages (3 agents)
5. **Docgen Agent** → `methodology/two-stage-detection.md`
   - Analyze detector scripts
   - Generate technical documentation
   - Include code examples (without private data)

6. **General-Purpose Agent E** → `methodology/ethical-considerations.md`
   - Privacy framework
   - Consent process
   - N=1 research limitations
   - Bias acknowledgment

7. **General-Purpose Agent F** → `methodology/data-collection.md`
   - Dataset description (255 convos, 5338 msgs)
   - Collection methodology
   - Anonymization approach

#### Group C: Supporting Content (2 agents)
8. **General-Purpose Agent G** → `resources/glossary.md`
   - Extract terms from all cycle docs
   - Define autism terminology
   - Define LLM terminology
   - Research-specific terms

9. **Architecture-Documenter Agent** → `appendices/dataset-statistics.md`
   - Analyze conversation data structure
   - Generate statistical overview
   - Create visualizations spec

**Execution Strategy:**
```bash
# Launch in single message with 9 Task calls
Task(general-purpose, prompt="Create for-researchers.md...") +
Task(general-purpose, prompt="Create for-autistic-individuals.md...") +
Task(general-purpose, prompt="Create for-clinicians.md...") +
...
```

**Quality Gate:** Thinkdeep agent reviews all outputs for consistency

---

### Wave 3: Content Creation - Case Studies & Implications (Day 4)

**Parallel Agent Assignment (7 agents):**

#### Group A: Case Studies (4 agents)

**CRITICAL CONSTRAINT: Only use real data from Benjamin's conversations. Extract and anonymize actual examples from existing cycle analyses. DO NOT create hypothetical scenarios or embellish.**

1. **General-Purpose + Secaudit A** → `case-studies/information-overload-example.md`
   - Extract real conversation example from cycle 1 complete analysis
   - Anonymize thoroughly (remove all PII)
   - Show actual cycle progression as it occurred
   - Include only real intervention attempts (if any)
   - Label clearly: "Based on actual conversation data"

2. **General-Purpose + Secaudit B** → `case-studies/perfectionism-spiral-example.md`
   - Extract real conversation from cycle 3 analysis
   - Anonymize thoroughly
   - Show actual before/after if intervention was attempted
   - If no intervention yet, show pattern only
   - Label: "Based on actual conversation data"

3. **General-Purpose + Secaudit C** → `case-studies/successful-intervention-example.md`
   - **Only create if real intervention data exists**
   - Extract from system-prompts/benjamin/changelog.md
   - Show measurable improvement from actual data
   - If no intervention results yet, mark as "Future: Wave 2 results"
   - Label: "Based on actual intervention data" OR "Pending Wave 2 results"

4. **General-Purpose + Secaudit D** → `case-studies/natural-trait-example.md`
   - Extract real example from cycle 7 analysis
   - Show healthy special interest hyperfocus
   - Use actual conversation demonstrating productive engagement
   - Label: "Based on actual conversation data"

#### Group B: Implications (3 agents)
5. **General-Purpose Agent H** → `implications/for-llm-design.md`
   - Product recommendations
   - Safety features
   - Accessibility features

6. **General-Purpose Agent I** → `implications/for-clinical-practice.md`
   - Therapeutic applications
   - Diagnostic considerations
   - Treatment integration

7. **General-Purpose Agent J** → `implications/for-accessibility.md`
   - Inclusive AI design
   - Universal design principles
   - Neurodivergent-friendly defaults

**Privacy Protection:**
- Secaudit agent reviews all case studies for PII
- Copy-diff-analyzer tracks original vs anonymized versions

---

### Wave 4: Content Adaptation & Refinement (Day 5)

**Parallel Agent Assignment:**

#### Group A: Existing Content Adaptation (6 agents)
Adapt existing cycle analyses for public consumption:

1. **Copy-Diff-Analyzer Agent A** → Cycle 1 analysis
   - Track: Research version → Public version
   - Remove: Internal notes, development process
   - Add: Public-facing framing, accessibility

2. **Copy-Diff-Analyzer Agent B** → Cycle 2 analysis
3. **Copy-Diff-Analyzer Agent C** → Cycle 3 analysis
4. **Copy-Diff-Analyzer Agent D** → Cycle 4 analysis
5. **Copy-Diff-Analyzer Agent E** → Cycle 6 & 7 analyses
6. **Copy-Diff-Analyzer Agent F** → Cycles summary

**Output:** Implementation guides showing exactly what to change

#### Group B: Visual Content Planning (3 agents)
7. **Thinkdeep Agent A** → Cycle diagram specifications
   - All 7 cycles
   - Visual reinforcement loop representations
   - Mermaid diagram code

8. **Thinkdeep Agent B** → Statistical visualization specs
   - Prevalence charts
   - LLM contribution graphs
   - Timeline visualizations

9. **Chat Agent** → Interactive element designs
   - Self-assessment quiz logic
   - Pattern matcher specifications
   - Intervention generator design

---

### Wave 5: Technical Implementation (Day 6)

**Parallel Agent Assignment:**

1. **Codereview Agent** → Review `mkdocs.yml`
   - Validate configuration
   - Optimize navigation
   - Check accessibility settings
   - Plugin recommendations

2. **General-Purpose Agent K** → Create directory structure
   - Execute mkdir commands
   - Organize files
   - Set up navigation hierarchy

3. **General-Purpose Agent L** → Copy and adapt existing files
   - Move files to mkdocs-site/docs/
   - Update relative paths
   - Rename as needed

4. **Refactor Agent** → Content organization review
   - Analyze navigation flow
   - Suggest improvements
   - Identify redundancy

5. **Tracer Agent** → Document dependency mapping
   - Trace cross-references between docs
   - Generate internal linking recommendations
   - Create content relationship diagram

---

### Wave 6: Quality Assurance (Day 7)

**Sequential Quality Gates with Specialized Agents:**

#### Gate 1: Privacy & Ethics Review
**Secaudit Agent** (comprehensive mode)
- Input: All content files
- Check for:
  - Personally identifiable information
  - Sensitive conversation excerpts
  - Identifying details about Benjamin/family
  - Consent statement presence
  - Medical advice disclaimers
- Output: `privacy-audit-report.md` with severity ratings

#### Gate 2: Content Consistency
**Analyze Agent** (quality mode)
- Check: Tone consistency across audience types
- Check: Terminology consistency (via glossary)
- Check: Cross-reference accuracy
- Check: Claim support (citations to data)
- Output: `content-quality-report.md`

#### Gate 3: Accessibility Review
**Thinkdeep Agent** (accessibility focus)
- Semantic HTML structure
- Plain language summaries
- Content warning placement
- Navigation clarity
- Output: `accessibility-recommendations.md`

#### Gate 4: Technical Validation
**Precommit Agent** (validation mode)
- All markdown files valid
- All links functional (internal)
- All images referenced exist
- MkDocs builds without errors
- Output: `technical-validation-report.md`

#### Gate 5: Multi-Model Content Review
**Consensus Agent** (5 models)
- Question: "Is this content respectful to autistic community?"
- Question: "Is the research methodology clearly explained?"
- Question: "Are privacy considerations adequate?"
- Question: "Is the technical content accessible?"
- Models: GPT-5, Gemini 2.5 Pro, Claude Sonnet 4.5, etc.
- Output: `consensus-review.md`

---

### Wave 7: Launch Preparation (Day 8)

**Parallel Final Tasks:**

1. **Readme-Updater Agent** → Synchronize README.md
   - Ensure consistency with index.md
   - Update links
   - Reflect current state

2. **General-Purpose Agent M** → Create launch checklist
   - Based on all QA reports
   - Prioritized action items
   - Go/no-go criteria

3. **Planner Agent** → Post-launch roadmap
   - Wave 2 research integration plan
   - Community contribution workflow
   - Maintenance schedule

4. **Chat Agent** → Draft launch communications
   - Social media posts
   - Email to autism research community
   - Outreach to LLM developers

---

## Efficiency Gains Analysis

### Traditional Sequential Approach
- Planning: 2 days
- Content creation (40+ new pages): 10-15 days
- Content adaptation (6 cycle docs): 3-5 days
- Technical setup: 2 days
- QA review: 3-5 days
- **Total: 20-29 days**

### Parallel Agent Approach
- Wave 1 (Planning): 1 day (3 parallel agents)
- Wave 2 (Core content): 2 days (9 parallel agents)
- Wave 3 (Case studies): 1 day (7 parallel agents)
- Wave 4 (Adaptation): 1 day (9 parallel agents)
- Wave 5 (Technical): 1 day (5 parallel agents)
- Wave 6 (QA): 1 day (5 sequential gates)
- Wave 7 (Launch prep): 1 day (4 parallel agents)
- **Total: 8 days**

**Time Savings: 60-72% reduction**

### Quality Improvements

**Consistency:**
- Multiple agents use same source material
- Consensus agents resolve conflicts
- Refactor agent identifies redundancy

**Expertise:**
- Specialized agents for specialized tasks
- Docgen for technical documentation
- Secaudit for privacy concerns
- Thinkdeep for complex decisions

**Thoroughness:**
- Parallel coverage of all audience types
- Multiple review passes
- Cross-validation between agents

**Accessibility:**
- Dedicated accessibility review
- Multiple model perspectives
- Plain language optimization

---

## Orchestration Patterns

### Pattern 1: Fan-Out (Parallel Creation)
```
Master Task
    ├─→ Agent A (Page 1)
    ├─→ Agent B (Page 2)
    ├─→ Agent C (Page 3)
    └─→ Agent D (Page 4)
All complete → Consolidate
```

**Use for:** Content creation, adaptation tasks

### Pattern 2: Pipeline (Sequential with Dependencies)
```
Agent A (Analysis)
    ↓ (findings)
Agent B (Design)
    ↓ (design)
Agent C (Implementation)
    ↓ (implementation)
Agent D (Review)
```

**Use for:** Quality gates, progressive refinement

### Pattern 3: Consensus (Multi-Model Validation)
```
Question
    ├─→ Model A (stance: for)
    ├─→ Model B (stance: against)
    ├─→ Model C (stance: neutral)
    └─→ Model D (stance: expert)
Synthesize → Decision
```

**Use for:** Controversial decisions, quality assurance

### Pattern 4: Iterative Refinement
```
Agent A (Draft v1)
    ↓
Review Agent (Feedback)
    ↓
Agent A (Draft v2)
    ↓
Review Agent (Approve/Iterate)
```

**Use for:** High-stakes content (homepage, methodology)

---

## Data Integrity Principles

**CRITICAL: All agents must follow these principles:**

1. **Use Only Real Data**
   - Extract from actual conversations and analyses
   - Never create hypothetical scenarios
   - Never embellish or invent details
   - If data doesn't exist, mark as "Pending future research"

2. **Transparent Labeling**
   - "Based on actual conversation data"
   - "Based on actual intervention results"
   - "Pending Wave 2 results" (for future data)
   - Never imply data exists when it doesn't

3. **Anonymization Without Alteration**
   - Remove PII thoroughly
   - Preserve meaning and context
   - Don't change details to make stories "better"
   - Document what was anonymized

4. **Evidence-Based Claims**
   - Every claim must trace to actual data
   - Statistics from real analysis results
   - Quotes from actual conversations (anonymized)
   - No speculation presented as fact

## Agent-Specific Prompting Strategies

### For Content Creation Agents

**Template:**
```
Create {page_name} for the MkDocs website.

Audience: {target_audience}
Tone: {tone_specification}
Length: {word_count_target}

Source material:
- {relevant_cycle_analysis_docs}
- {relevant_methodology_docs}

CRITICAL CONSTRAINTS:
- Use ONLY real data from source materials
- DO NOT create hypothetical examples
- DO NOT embellish or invent details
- If data doesn't exist, state "Pending future research"

Required sections:
1. {section_1}
2. {section_2}
...

Exclude:
- Personally identifiable information
- Internal development notes
- Unvalidated hypotheses
- Invented examples or scenarios

Include:
- Specific statistics with sources
- Real examples (anonymized thoroughly)
- Actionable recommendations based on data
- Clear labels: "Based on actual data" or "Pending results"

Output format: Markdown with MkDocs Material theme features
```

### For Quality Review Agents

**Template:**
```
Review {content_name} for {review_focus}.

Checklist:
- [ ] {criterion_1}
- [ ] {criterion_2}
...

Rate each criterion: Pass/Concern/Fail
Provide specific examples for Concern/Fail
Suggest concrete improvements

Context:
- Target audience: {audience}
- Privacy level: Public
- Sensitivity: {high/medium/low}
```

### For Consensus Agents

**Template:**
```
Models to consult: [{model_1}, {model_2}, {model_3}]
Stances: [for, against, neutral]

Question: "{decision_question}"

Context:
{relevant_background}

Each model should:
1. State position with reasoning
2. Identify risks and benefits
3. Suggest alternatives
4. Rate confidence (1-10)

Final synthesis should:
- Summarize positions
- Identify consensus areas
- Flag unresolved concerns
- Recommend decision with caveats
```

---

## Risk Mitigation

### Risk 1: Agent Inconsistency
**Mitigation:**
- Shared glossary (created early in Wave 1)
- Reference style guide
- Cross-agent validation in Wave 6
- Refactor agent identifies conflicts

### Risk 2: Privacy Leaks
**Mitigation:**
- Secaudit agent reviews ALL content
- Copy-diff-analyzer tracks anonymization
- Manual family review before launch
- Privacy checklist at every wave

### Risk 3: Quality Variance
**Mitigation:**
- Specialized agents for specialized tasks
- Multi-model consensus on key decisions
- Iterative refinement for critical pages
- Comprehensive QA wave (Wave 6)

### Risk 4: Over-Parallelization
**Mitigation:**
- Dependencies mapped in Wave 1
- Sequential waves, parallel within waves
- Quality gates between waves
- Human review at wave transitions

### Risk 5: Agent Context Limits
**Mitigation:**
- Break large docs into chunks
- Use continuation_id for multi-turn tasks
- Provide focused source material
- Summarize previous wave outputs

---

## Enhanced Capabilities with Parallel Agents

### 1. Multi-Perspective Analysis

**Traditional:** Single perspective on content
**With Agents:** Consensus agent gets 3-5 different model perspectives

**Example:** "Is this case study respectful?"
- Model A (GPT-5): Technical accuracy focus
- Model B (Gemini Pro): Empathy and tone focus
- Model C (Claude Sonnet): Autism community perspective
- Synthesized: Balanced view with multiple considerations

### 2. Specialized Expertise

**Traditional:** Generalist approach to all tasks
**With Agents:** Right agent for right task

- Docgen → Technical documentation
- Secaudit → Privacy review
- Thinkdeep → Complex ethical decisions
- Refactor → Content organization
- Tracer → Dependency mapping

### 3. Continuous Validation

**Traditional:** Review at end
**With Agents:** Validation at every wave

- Wave 1: Plan validation
- Wave 2-4: Content validation
- Wave 5: Technical validation
- Wave 6: Comprehensive QA
- Wave 7: Launch readiness

### 4. Iterative Improvement

**Traditional:** One-shot content creation
**With Agents:** Multiple refinement passes

- Draft → Review → Refine → Re-review
- Consensus drives controversial sections
- Analyze agent identifies improvement opportunities

---

## Monitoring & Metrics

### Per-Wave Metrics

**Completion:**
- Tasks completed / Total tasks
- Time spent vs estimated
- Blockers encountered

**Quality:**
- Agent confidence scores
- Review pass rate
- Issues flagged

**Consistency:**
- Cross-reference validation
- Terminology consistency
- Tone consistency

### Overall Project Metrics

**Efficiency:**
- Total time: Target 8 days
- Agent utilization: Avg concurrent agents
- Rework rate: Changes after QA

**Quality:**
- Privacy issues: Target 0 critical
- Accessibility score: Target WCAG AA
- Content coverage: All required pages

**Readiness:**
- Launch checklist: 100% complete
- Family approval: Obtained
- Technical validation: All tests pass

---

## Recommended Execution Strategy

### Phase 0: Setup (You, 2 hours)
1. Review this strategy document
2. Prepare source material index
3. Set up continuation tracking
4. Define success criteria

### Phase 1: Execute Waves 1-3 (3 days)
- Day 1: Planning & architecture (Wave 1)
- Day 2-3: Core content creation (Waves 2-3)
- **Checkpoint:** 60% content complete

### Phase 2: Execute Waves 4-5 (2 days)
- Day 4: Content adaptation (Wave 4)
- Day 5: Technical implementation (Wave 5)
- **Checkpoint:** 90% content complete, site buildable

### Phase 3: Execute Waves 6-7 (2 days)
- Day 6: Quality assurance (Wave 6)
- Day 7: Launch preparation (Wave 7)
- **Checkpoint:** All QA passed, launch ready

### Phase 4: Launch (1 day)
- Family final review
- Deploy to staging
- Final checks
- Go live

**Total: 8 days from start to launch**

---

## Next Steps

1. **Approve strategy** - Review and adjust if needed
2. **Prepare source materials** - Gather all docs for agent access
3. **Execute Wave 1** - Launch planner + consensus + analyze agents
4. **Review Wave 1 outputs** - Validate before proceeding
5. **Execute remaining waves** - Follow orchestration plan
6. **Monitor metrics** - Track progress and quality
7. **Launch** - Deploy public website

---

## Appendix: Agent Invocation Examples

### Example 1: Parallel Content Creation (Wave 2)

```python
# Launch 9 agents simultaneously for audience landing pages + methodology

agents = [
    {
        "subagent_type": "general-purpose",
        "description": "Create for-researchers page",
        "prompt": """Create overview/for-researchers.md...
        [detailed prompt]
        """
    },
    {
        "subagent_type": "general-purpose",
        "description": "Create for-autistic-individuals page",
        "prompt": """Create overview/for-autistic-individuals.md...
        [detailed prompt]
        """
    },
    # ... 7 more agents
]

# Execute all in single message (9 Task tool calls)
```

### Example 2: Sequential Quality Gates (Wave 6)

```python
# Step 1: Privacy audit
secaudit_result = Task(
    subagent_type="secaudit",
    prompt="Review all content for PII..."
)

# Step 2: Content consistency (depends on Step 1 passing)
analyze_result = Task(
    subagent_type="analyze",
    prompt="Check consistency across all pages..."
)

# Step 3: Accessibility review (depends on Step 2)
thinkdeep_result = Task(
    subagent_type="thinkdeep",
    prompt="Review accessibility compliance..."
)

# ... etc
```

### Example 3: Consensus Decision (Wave 1)

```python
consensus_result = Task(
    subagent_type="consensus",
    prompt="""
    Question: "Should we lead with Benjamin's personal story or academic research?"

    Models: [
        {"model": "gpt-5-pro", "stance": "for"},      # Personal story
        {"model": "gemini-2.5-pro", "stance": "against"}, # Academic
        {"model": "claude-sonnet-4-5", "stance": "neutral"}
    ]

    Context:
    - Autism community values lived experience
    - Researchers expect academic framing
    - Privacy is critical concern
    - Engagement matters for impact
    """
)
```

---

## Conclusion

Parallel Claude subagent orchestration can transform MkDocs website development from a 20-29 day sequential process into an 8-day parallel workflow. This approach provides:

**Speed:** 60-72% time reduction through parallelization
**Quality:** Specialized agents for specialized tasks
**Consistency:** Shared source material and validation
**Thoroughness:** Multiple review passes and perspectives
**Accessibility:** Dedicated accessibility review
**Privacy:** Comprehensive security audit

The key is strategic orchestration: parallel where independent, sequential where dependent, and consensus where controversial.
