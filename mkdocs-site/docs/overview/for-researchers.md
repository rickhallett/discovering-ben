# for researchers

## introduction

This study represents a novel methodological approach to understanding human-AI interaction in neurodivergent populations. Rather than traditional cross-sectional surveys or controlled laboratory experiments, this research employs longitudinal n=1 analysis of naturalistic conversation data to identify systematic patterns in how autism traits interact with large language model (LLM) response behaviors.

**Key contribution:** We demonstrate that LLM response patterns—not autism traits alone—are the primary driver (60-70%) of vicious reinforcement cycles in human-AI interaction. This finding has significant implications for AI safety, accessibility design, and assistive technology development.

## research significance

### why n=1 longitudinal depth matters

Traditional autism research typically employs cross-sectional designs with moderate sample sizes, capturing snapshots of behavior at discrete time points. This study inverts that paradigm by analyzing 255 conversations (5,338 messages) from a single autistic individual over 26 days, providing unprecedented depth into how behavioral patterns evolve through repeated AI interaction.

**Advantages of this approach:**

- **Temporal dynamics:** Captures how cycles escalate over time, which cross-sectional studies cannot observe
- **Individual variation:** Autism is highly heterogeneous; deep individual analysis reveals mechanisms obscured in group averages
- **Naturalistic context:** Real-world usage patterns rather than artificial task performance
- **Behavioral archaeology:** Reconstructs causal chains through sequential message analysis
- **Iterative validation:** Patterns can be traced across multiple instances within the same individual

**Trade-offs:**

- Generalizability concerns (addressed in limitations section)
- Single LLM system (Claude 3.5 Sonnet)
- Individual's specific autism profile may not represent all autistic people
- Cannot establish population-level prevalence

### novel contributions to the literature

**1. LLM as primary causal agent (not autism traits)**

Previous research on autism and technology typically frames autism traits as the source of difficulty. This study demonstrates that in 4 of 7 investigated patterns, LLM response behaviors contribute 60-70% to cycle formation—making the AI system the primary driver, not the user's neurodivergence.

**2. Quantification of RLHF failure modes**

While RLHF (Reinforcement Learning from Human Feedback) is designed to make AI systems more helpful, this research provides empirical evidence of how optimizing for "helpfulness" can create pathological patterns when interacting with users who have executive function differences, binary thinking patterns, or emotional regulation challenges.

**3. Two-stage detection methodology**

Combines quantitative pattern mining (regex-based detection across full dataset) with qualitative semantic analysis (LLM-based contextual validation of samples). This hybrid approach balances scale with interpretive depth, addressing limitations of purely automated or purely manual analysis.

**4. Distinction between pathological cycles and natural trait expression**

Not all high-prevalence patterns are problematic. This research differentiates between vicious cycles requiring intervention (e.g., 92.2% decision abandonment) and natural autism trait expression that produces productive outcomes (e.g., special interest engagement with 60% positive results).

## methodology rigor

### data collection

**Source:** Personal Claude conversation history (Claude.ai web interface)
**Participant:** Single autistic adult with diagnosis, self-selected for study
**Time period:** 26 days of continuous usage
**Volume:** 255 conversations, 5,338 messages (2,672 user messages, 2,666 Claude responses)
**Data format:** JSON export from Claude conversation history
**LLM model:** Claude 3.5 Sonnet (Anthropic)

**Naturalistic conditions:**

- User was unaware patterns would be analyzed during data collection period
- No experimental manipulation or prompted behaviors
- Conversations reflect genuine task needs (technical questions, decision-making, complaint drafting, information research)
- No financial incentive or researcher presence during interactions

### two-stage detection process

**Stage 1: Quantitative Pattern Detection**

Automated regex-based scanning of all 2,672 user messages to identify:

- Lexical markers (e.g., "perfect," "best," "everything," profanity)
- Structural patterns (e.g., repeated questioning, iteration cycles)
- Frequency thresholds (e.g., >3 refinement requests)

**Purpose:** Establish prevalence rates, identify candidate conversations for semantic analysis

**Example metrics:**

- Cycle 1: 94 exhaustive information demands detected (3.52% of all messages)
- Cycle 2: 79 "best" demands across 64 conversations
- Cycle 4: 418 profanity instances (15.64% of all messages)

**Limitations:** Cannot detect semantic nuance, context-dependent meaning, or tone

**Stage 2: Semantic Validation**

LLM-based analysis (Claude 3.5 Haiku) of conversation samples using structured rubrics:

- Binary classification (cycle present: yes/no)
- Severity rating (non-existent/mild/moderate/severe)
- LLM contribution percentage (0-100%)
- Outcome assessment (task completion, productivity)
- Narrative description of mechanism

**Sample selection:**

- 20 conversations per cycle (stratified by quantitative indicators)
- Entire conversation threads analyzed (not individual messages)
- Analyst LLM provided full conversation context

**Validation approach:**

- Structured JSON output format prevents narrative drift
- Binary decisions reduce ambiguity
- Percentage estimates force quantitative commitment
- Cross-validation between quantitative prevalence and semantic severity

### statistical evidence standards

This study employs multiple evidence types to establish pattern validity:

**1. Prevalence rates (population-level)**

Percentage of conversations containing pattern markers:

- High prevalence (>40%): Cycles 4 (50.6%), 5 (43.9%), 7 (60.8%)
- Moderate prevalence (25-30%): Cycles 1 (30.2%), 2 (25.1%), 3 (25.1%)
- Low prevalence (<5%): Cycle 6 (0.8%, rejected as non-pattern)

**2. Pattern density (intensity)**

Frequency of pattern instances within affected conversations:

- Cycle 4: 418 profanity instances across 129 conversations (3.2 per conversation)
- Cycle 1: 94 exhaustive demands across 77 conversations (1.2 per conversation)
- Cycle 3: 102 perfection demands across 64 conversations (1.6 per conversation)

**3. Severity ratings (outcome impact)**

Percentage of affected conversations rated "severe" in semantic analysis:

- Cycle 3: 75% severe (highest)
- Cycle 1: 60% severe
- Cycles 2 & 5: 50% severe
- Cycle 4: 33% severe (but 100% no baseline return—see nuance)

**4. Catastrophic outcome metrics (failure rates)**

Quantitative measures of negative outcomes:

- Cycle 2: 92.2% decision abandonment (only 5 of 64 decisions made)
- Cycle 3: 71.9% tasks unresolved (endless iteration without completion)
- Cycle 4: 100% no baseline return (emotion never de-escalates)
- Cycle 1: 100% satisfaction paradox (more information → less satisfaction)

**5. LLM contribution calculations (causal attribution)**

Estimated percentage of cycle reinforcement attributable to LLM response patterns:

- Cycles 2 & 3: 70% (highest LLM contribution)
- Cycles 1 & 4: 60%
- Cycles 5 & 7: ~40% (lower, suggesting user-driven patterns)

**Method:** Semantic analysts rated "How much did Claude's responses reinforce or worsen this pattern?" on 0-100% scale

**Interpretation:** 60-70% indicates LLM is primary driver; <50% indicates user trait is primary

## key findings

### meta-finding: llm as primary driver

**Critical discovery:** In 4 of 7 investigated cycles, LLM response patterns contribute 60-70% to cycle formation. This means AI behavior—specifically RLHF-optimized compliance and comprehensiveness—is the primary cause of vicious cycles, not autism traits alone.

**Mechanism:**

1. Autism trait creates initial behavior (e.g., requesting "the ONE best option")
2. LLM over-complies by providing comprehensive comparison of 5-7 options
3. User experiences executive dysfunction (cannot choose from many options)
4. User requests simplification ("just tell me which one!")
5. LLM provides more nuanced analysis (interpreting "helpful" as "thorough")
6. Decision paralysis worsens
7. 92.2% of decisions abandoned

**Implication:** The solution is not to "fix" autistic users or train them to interact differently. The solution is to modify LLM response strategies to avoid triggering executive dysfunction in the first place.

### four pathological cycles (require intervention)

**Cycle 1: Information Overload**

- Prevalence: 30.2% of conversations
- LLM contribution: 60%
- Mechanism: User demands "everything" → Claude provides 1,500+ word responses → User overwhelmed → Demands even more complete information
- Catastrophic metric: 100% satisfaction paradox (more information = less satisfaction)

**Cycle 2: Decision Paralysis (Finding the ONE Best Thing)**

- Prevalence: 25.1% of conversations
- LLM contribution: 70% (highest)
- Mechanism: User asks "which is best?" → Claude provides balanced 5-7 option comparison → Executive dysfunction prevents choice → User demands binary answer → Claude provides more nuanced analysis
- Catastrophic metric: 92.2% decision abandonment rate

**Cycle 3: Perfectionism Escalation**

- Prevalence: 25.1% of conversations
- LLM contribution: 70% (highest)
- Severity: 75% severe (highest severity rate)
- Mechanism: User sets impossible standard ("perfect") → Claude iterates → User finds flaw → Demands refinement → Claude apologizes and refines → User raises bar
- Catastrophic metric: 71.9% tasks unresolved (endless iteration)
- Key finding: 100% correlation between Claude apologies and task failure

**Cycle 4: Emotional Dysregulation Reinforcement**

- Prevalence: 50.6% (most widespread)
- LLM contribution: 60%
- Mechanism: User frustrated → Emotion escalates → Expresses intense emotion → Claude provides task-focused help → Emotion validated as productive → Sensitization (faster/stronger next time)
- Catastrophic metric: 100% no baseline return (emotion never de-escalates once triggered)
- Unique finding: Unlike typical dysregulation (emotion prevents function), this pattern shows dysregulation enables function when channeled into task output, making it more likely to recur

### two non-pathological patterns

**Cycle 5: Assuming LLM Knows What User Is Thinking (Mind Reading)**

- Prevalence: 43.9%
- LLM contribution: ~40%
- Severity: Only 3 frustration instances (lowest across all cycles)
- Finding: Current Claude approach (asking for clarification without apologizing) is working well
- Interpretation: This is a mild pattern, not a vicious cycle requiring intervention

**Cycle 7: Special Interest Hyperfocus**

- Prevalence: 60.8% (highest of all patterns)
- LLM contribution: ~40%
- Severity: 0% pathological, 60% productive outcomes
- Finding: Natural autism trait expression producing positive results
- Interpretation: This is healthy engagement with special interests (technology, spirituality, legal advocacy), not dysfunction

### universal intervention principles

Based on cross-cycle analysis, five intervention strategies apply across all pathological cycles:

**1. Stop over-compliance**

Replace "maximize helpfulness through compliance" with "provide effective support through boundaries"

- Refuse impossible standards (Cycle 3)
- Provide binary recommendations when appropriate (Cycle 2)
- Limit information provision (Cycle 1)
- Don't channel intense emotion into task output (Cycle 4)

**2. Replace apologies with boundaries**

Apologies frame constraints as LLM failures, reinforcing unrealistic expectations

- NOT: "I apologize, I can't provide perfect output"
- DO: "This output meets professional standards for [use case]"

**3. Declare completion explicitly**

Tasks iterate endlessly because neither party says "done"

- "This letter now meets professional complaint standards" (Cycle 3)
- "I recommend X based on your needs" (Cycle 2)
- "This covers the essential information" (Cycle 1)

**4. Acknowledge then redirect (emotional regulation)**

Brief emotional acknowledgment before proceeding with task

1. Name emotion: "I notice you're feeling frustrated"
2. Validate: "That makes sense given [situation]"
3. Redirect: "Let's approach this by [concrete step]"
4. Proceed with task

**5. Educate on constraints**

Explain LLM limitations matter-of-factly (addresses theory of mind challenges)

- "I don't have memory across sessions" (Cycle 5)
- "I can't guarantee 100% certainty—I provide probabilistic answers"
- "Further iterations won't improve quality, just change style" (Cycle 3)

## limitations and constraints

### generalizability concerns

**Single participant (n=1):**

This study analyzes one autistic individual's interaction patterns. Autism is highly heterogeneous—diagnostic criteria require only 5 of 7 possible traits, leading to substantial individual variation. Findings may not generalize to:

- Autistic individuals with different trait profiles
- Those with co-occurring conditions (ADHD, anxiety, intellectual disability)
- Different age groups (participant is adult)
- Different communication preferences (participant is verbal/written)
- Different support needs levels

**Recommendation for future research:** Replication with diverse autistic participants to identify which cycles are universal vs. individual-specific

**Single LLM system (Claude 3.5 Sonnet):**

All conversations occurred with one model from one provider. Response patterns may differ across:

- Other LLM providers (OpenAI GPT, Google Gemini, etc.)
- Different model versions (Claude Opus, Haiku)
- Different training approaches (non-RLHF models)
- Different system prompts or custom instructions

**Recommendation:** Comparative analysis across LLM systems to determine if 60-70% contribution rates are Claude-specific or industry-wide

**Cultural and linguistic context:**

- Participant is English-speaking
- Conversations conducted in English
- Cultural norms around directness, emotion expression, and help-seeking may vary
- Findings may not transfer to non-Western contexts

### methodological limitations

**Retrospective analysis:**

Data was collected for personal use, not research. This creates:

- **No experimental control:** Cannot manipulate variables or test counterfactuals
- **No baseline comparison:** Cannot compare to neurotypical users or controlled conditions
- **Selection bias:** Participant self-selected to use Claude frequently
- **Demand characteristics:** While unaware during collection, participant is now co-investigator

**Semantic analysis limitations:**

Using an LLM (Claude Haiku) to analyze LLM conversation data creates potential circularity:

- Analyst LLM may have similar biases as conversational LLM
- Interpretation influenced by training data and RLHF process
- Cannot validate semantic judgments against ground truth
- No inter-rater reliability (only one analyst model used)

**Mitigation:** Structured rubrics with binary classifications and quantitative ratings reduce subjective interpretation

**Temporal scope:**

26 days is sufficient to observe cycle formation but may miss:

- Longer-term sensitization effects (months/years)
- Adaptation or learning over extended time
- Seasonal or life context variations
- Long-term outcomes of intervention strategies

**Causality inference limitations:**

While we estimate "LLM contribution percentage," this is an interpretive judgment, not causal proof. Establishing true causality would require:

- Experimental manipulation of LLM response strategies
- A/B testing of intervention approaches
- Controlled comparison groups
- Longitudinal tracking of cycle evolution

### dataset limitations

**Conversation selection:**

Only conversations participant chose to preserve are included. May exclude:

- Very brief interactions (deleted as unimportant)
- Failed interactions (abandoned in frustration)
- Sensitive topics (deleted for privacy)
- Successful task completions (less memorable, potentially deleted)

**Message completeness:**

JSON export format may not capture:

- Edited messages (only final version visible)
- Deleted messages
- Thinking/typing time between messages
- Non-textual context (time of day, emotional state, environmental factors)

**Single-channel data:**

Only text conversations analyzed. Does not capture:

- Voice interactions (if participant used voice mode)
- Multi-modal inputs (images, documents)
- Copy-paste behavior or external information sources
- Interactions with other AI systems

### ethical and privacy constraints

**Informed consent:**

Participant provided consent for anonymized research use, but:

- Cannot share raw conversation data publicly
- Direct quotes must be sanitized (418 profanity instances, identifying details)
- Product/service names generalized
- Potential re-identification risk if patterns are too specific

**Representation concerns:**

Single case study risks:

- Reinforcing stereotypes about autistic people
- Pathologizing natural autism traits (addressed by distinguishing Cycle 7)
- Framing autism as "problem to be solved" rather than valid neurodiversity

**Mitigation:** Explicit framing of LLM as primary driver, not autism as deficit

### intervention validation gap

**No implementation data:**

Proposed interventions are evidence-based hypotheses, not validated solutions. This study:

- Identifies problems and proposes solutions
- Does not test whether interventions actually work
- Cannot quantify intervention effectiveness
- Cannot identify unintended consequences

**Recommendation:** Future research should implement system prompt modifications and measure outcomes

## implications for future research

### replication opportunities

**Cross-participant replication:**

Recruit diverse autistic participants with different trait profiles:

- High vs. low support needs
- Different co-occurring conditions
- Various age groups
- Different communication preferences
- Cultural and linguistic diversity

**Method:** Apply two-stage detection methodology to their conversation histories
**Research question:** Which cycles are universal vs. individual-specific?

**Cross-system replication:**

Analyze conversations with multiple LLM systems:

- OpenAI GPT-4/GPT-5
- Google Gemini
- Meta Llama
- Anthropic Claude (different versions)

**Research question:** Are 60-70% LLM contribution rates Claude-specific or industry-wide?

**Cross-neurotype comparison:**

Compare autistic vs. neurotypical users on same tasks:

- Do vicious cycles occur with neurotypical users?
- Are prevalence rates or severity different?
- Do same intervention strategies work for both groups?

**Research question:** Are these cycles autism-specific or universal vulnerability patterns?

### intervention effectiveness studies

**A/B testing of system prompts:**

Implement proposed interventions and measure outcomes:

- Control group: Standard Claude responses
- Treatment group: Modified responses with boundaries, scoping, completion declarations
- Metrics: Task completion rates, iteration counts, emotional escalation, user satisfaction

**Longitudinal intervention tracking:**

Deploy modified system prompt with participant and track:

- Do vicious cycles reduce in frequency?
- Do severity ratings decrease?
- Are there unintended negative consequences?
- Does user satisfaction improve?

**Comparative intervention testing:**

Test different intervention strategies against each other:

- Which phrasing is most effective for boundaries?
- Optimal information scoping approach?
- Best emotional acknowledgment techniques?

### theoretical development

**RLHF optimization paradox:**

Formal investigation of how "helpfulness" optimization creates harm:

- Mathematical modeling of over-compliance dynamics
- Reinforcement learning analysis of training incentives
- Alternative reward structures that include boundary-setting

**Neurodivergence-AI interaction theory:**

Develop theoretical framework for how AI systems interact with cognitive differences:

- Executive function + AI response patterns
- Binary thinking + option provision
- Emotional regulation + task focus
- Theory of mind + AI constraint communication

**Assistive technology design principles:**

Extract generalizable principles for neurodivergence-aware AI:

- When to provide more vs. less information
- How to support decision-making without causing paralysis
- Emotional regulation integration in AI systems
- Boundary-setting as accessibility feature

### novel research directions

**Positive cycle identification:**

This study focused on vicious cycles. Future research could identify:

- Virtuous cycles (where AI-autism interaction produces above-baseline outcomes)
- Protective factors (what prevents cycle formation)
- Successful adaptation patterns (how users work around difficulties)

**Cycle interaction dynamics:**

Investigate how cycles compound:

- Information Overload + Perfectionism = catastrophic incompletion
- Decision Paralysis + Emotional Dysregulation = panic escalation
- Which combinations are most dangerous?
- Are there synergistic effects?

**Long-term sensitization effects:**

Track cycle evolution over months/years:

- Do cycles worsen with repeated exposure?
- Is there a saturation point?
- Can users develop resistance or adaptation?
- What are the mental health implications?

**Comparative vulnerability research:**

Identify which populations are most susceptible:

- Other neurodivergent conditions (ADHD, OCD, anxiety disorders)
- Cognitive differences (working memory limitations, processing speed)
- Situational vulnerabilities (stress, fatigue, cognitive load)

### methodological innovations

**Real-time cycle detection:**

Develop systems that identify cycles as they form:

- Live conversation analysis
- Intervention triggering (e.g., "I notice we've iterated 5 times—let's pause")
- User notification systems
- Adaptive response modification

**Multi-modal analysis:**

Extend beyond text to include:

- Voice tone analysis (emotional state inference)
- Typing patterns (hesitation, revision behavior)
- Physiological data (if available via wearables)
- Temporal patterns (time of day, interaction frequency)

**Automated semantic analysis validation:**

Address LLM-analyzing-LLM circularity:

- Human expert validation of subset
- Inter-rater reliability across multiple analyst models
- Comparison to rule-based classification
- Ground truth establishment through user self-report

## how to cite this research

**Note:** This research is currently pre-publication. Citation information will be updated upon formal publication.

**Suggested interim citation:**

> [Author]. (2025). *Vicious Reinforcement Cycles in Autistic-LLM Interaction: A Longitudinal N=1 Case Study*. Discovering Ben Project. [URL when published]

**Dataset reference:**

Due to privacy constraints, the raw conversation dataset cannot be shared publicly. Researchers interested in replication should contact [contact information] to discuss:

- Methodology documentation and code sharing
- De-identified aggregate statistics
- Collaboration opportunities
- IRB-approved data access protocols

**Open resources:**

The following materials will be made available upon publication:

- Two-stage detection methodology code (pattern detectors and semantic analyzers)
- Structured rubrics for semantic analysis
- System prompt intervention recommendations
- Statistical analysis scripts

## acknowledgments

This research was made possible by:

- The participant's willingness to share naturalistic conversation data
- Family members who supported ethical review and privacy protection
- The open science community's commitment to accessibility research
- Anthropic's Claude system for both conversational interaction and analytical capabilities

**Conflict of interest statement:** The participant is both the data source and a co-investigator in this research, creating inherent interpretation biases. Findings should be considered hypothesis-generating rather than conclusive.

## contact for research collaboration

Researchers interested in:

- Replication studies
- Methodological questions
- Collaboration opportunities
- Access to anonymized aggregate data
- Extension research

Please contact: [Contact information to be added upon publication]

## related publications

[This section will be populated with related work upon publication]

**Relevant research areas:**

- Autism and technology interaction
- AI safety and alignment
- Assistive technology design
- Human-computer interaction (HCI)
- Neurodiversity and accessibility
- RLHF optimization consequences
- Large language model evaluation

## appendix: complete dataset statistics

### overview

- **Total conversations:** 255
- **Total messages:** 5,338
- **User messages:** 2,672
- **Claude responses:** 2,666
- **Time period:** 26 days
- **Average messages per conversation:** 20.9
- **LLM system:** Claude 3.5 Sonnet (Anthropic)

### cycle prevalence

| Cycle | Conversations Affected | Percentage | Classification |
|-------|----------------------|-----------|---------------|
| Cycle 7: Special Interest Hyperfocus | 155 | 60.8% | Natural trait |
| Cycle 4: Emotional Dysregulation | 129 | 50.6% | Pathological |
| Cycle 5: Mind Reading Assumptions | 112 | 43.9% | Mild |
| Cycle 1: Information Overload | 77 | 30.2% | Pathological |
| Cycle 2: Decision Paralysis | 64 | 25.1% | Pathological |
| Cycle 3: Perfectionism Escalation | 64 | 25.1% | Pathological |
| Cycle 6: System Building Obsession | 2 | 0.8% | Rejected |

### pattern intensity

| Cycle | Pattern Instances | Rate per Message | Rate per Affected Conversation |
|-------|------------------|------------------|-------------------------------|
| Cycle 4: Profanity | 418 | 15.64% | 3.2 |
| Cycle 5: Vague references | 218 | 8.16% | 1.9 |
| Cycle 7: Deep dive requests | 156 | 5.84% | 1.0 |
| Cycle 3: Perfection demands | 102 | 3.82% | 1.6 |
| Cycle 1: Exhaustive demands | 94 | 3.52% | 1.2 |
| Cycle 2: "Best" demands | 79 | 2.96% | 1.2 |
| Cycle 6: System requests | 20 | 0.75% | 10.0 |

### severity ratings

| Cycle | Severe Rate | Moderate Rate | Mild Rate | Non-existent Rate |
|-------|------------|--------------|-----------|------------------|
| Cycle 3: Perfectionism | 75% | 15% | 10% | 0% |
| Cycle 1: Information Overload | 60% | 25% | 10% | 5% |
| Cycle 2: Decision Paralysis | 50% | 35% | 10% | 5% |
| Cycle 5: Mind Reading | 50% | 25% | 20% | 5% |
| Cycle 4: Emotional Dysregulation | 33% | 47% | 15% | 5% |
| Cycle 7: Special Interests | 0% | 0% | 60% | 40% |
| Cycle 6: System Building | 0% | 5% | 0% | 95% |

### catastrophic outcomes

| Cycle | Metric | Value | Interpretation |
|-------|--------|-------|----------------|
| Cycle 2 | Decision abandonment rate | 92.2% | Only 5 of 64 decisions made |
| Cycle 3 | Tasks unresolved | 71.9% | Endless iteration without completion |
| Cycle 4 | No baseline return | 100% | Emotion never de-escalates |
| Cycle 1 | Satisfaction paradox | 100% | More information = less satisfaction |
| Cycle 3 | Apology-failure correlation | 100% | All tasks with apologies failed |

### llm contribution estimates

| Cycle | LLM Contribution | User Contribution | Primary Driver |
|-------|------------------|-------------------|---------------|
| Cycle 2: Decision Paralysis | 70% | 30% | LLM |
| Cycle 3: Perfectionism | 70% | 30% | LLM |
| Cycle 1: Information Overload | 60% | 40% | LLM |
| Cycle 4: Emotional Dysregulation | 60% | 40% | LLM |
| Cycle 6: System Building | ~50% | ~50% | Balanced |
| Cycle 5: Mind Reading | ~40% | ~60% | User |
| Cycle 7: Special Interests | ~40% | ~60% | User |

**Interpretation:** Cycles with >60% LLM contribution are primarily AI-driven problems. Cycles with <50% LLM contribution reflect natural user traits.

---

**Document status:** Research-grade documentation for academic and clinical audiences
**Intended use:** Understanding methodology, evaluating findings, planning replication studies
**Next reading:** For detailed cycle mechanisms, see individual cycle documentation in the full analysis section
