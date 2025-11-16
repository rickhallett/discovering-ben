# Glossary

Comprehensive terminology guide for understanding autism-LLM interaction research.

---

## Autism & Neurodiversity Terms

**Autism / Autism Spectrum Disorder (ASD)**
A neurodevelopmental condition characterized by differences in social communication, restricted interests, sensory processing, and information processing patterns. In this research, we use identity-first language ("autistic individual") respecting community preference over person-first language ("person with autism").

**Autistic Individual**
Identity-first language used throughout this research to respect the preferences of the autistic community. This phrasing acknowledges autism as an integral part of identity rather than a separable condition. Contrast with "person with autism" (person-first language).

**Binary Thinking / Black-White Thinking**
A cognitive pattern common in autism where options are perceived in absolute terms with no middle ground. Manifestations include: either "perfect" or "worthless," either "everything" or "nothing," either "the absolute best" or "unacceptable." This pattern creates particular challenges in LLM interactions when nuanced trade-offs are presented.

**Emotional Dysregulation**
Difficulty modulating emotional intensity in response to stimuli. In autism, this manifests as rapid escalation (0-to-100 emotional intensity within 1-3 messages), inability to return to emotional baseline, and frustration intolerance where small setbacks trigger major emotional responses. This research documents 100% no baseline return rate in affected conversations.

**Executive Dysfunction**
Difficulty with planning, organization, task initiation, working memory, and decision-making. In autism-LLM interactions, this manifests as: inability to filter relevant from irrelevant information, decision paralysis when presented with multiple options (92.2% abandonment rate documented), and inability to judge when tasks meet "good enough" standards.

**Filter Failure**
An executive dysfunction manifestation where an individual cannot extract relevant information from comprehensive content. Detected in 100% of information overload cases, filter failure means the person gets lost in details, misses main points, and cannot identify what information is important for their specific need.

**Rigid Perfectionism**
An autism trait where standards are set at impossible levels with zero tolerance for imperfection. Characterized by inability to accept "good enough," viewing any flaw as complete failure, and continuous raising of standards even after initial criteria are met. This research found 71.9% of perfectionist tasks remained unresolved due to endless iteration.

**Sensory Processing**
Differences in how sensory information is received and interpreted. While not a primary focus of this text-based interaction research, sensory processing differences are a core autism characteristic mentioned as part of the broader autism profile.

**Special Interest / Special Interest Hyperfocus**
Intense, focused engagement with specific topics that bring deep satisfaction and expertise. In this research, special interests identified include technology (145 mentions), spirituality (148 mentions), and legal/complaint writing (132 mentions). Unlike pathological cycles, special interest engagement showed 60% productive outcomes and is considered a natural autism trait, not a dysfunction.

**Theory of Mind Deficit**
Difficulty understanding that others have different knowledge, beliefs, and perspectives than oneself. In LLM interactions, this manifests as: expecting the AI to know context from previous sessions, not understanding LLM limitations, assuming vague references ("it," "that one") are clear, and attributing comprehension failures to the AI "not trying hard enough" rather than recognizing information gaps.

**Uncertainty Intolerance**
Inability to tolerate probabilistic or ambiguous information, requiring absolute certainty before feeling comfortable. In this research, manifested through 94 exhaustive information demands (3.52% of messages) seeking "everything" or "100% proof." Creates the satisfaction paradox where more information leads to less certainty rather than more.

---

## Large Language Model (LLM) Terms

**Anthropic Claude**
The specific LLM system used in this research dataset. Claude is Anthropic's AI assistant, trained using Constitutional AI and RLHF (Reinforcement Learning from Human Feedback) to be helpful, harmless, and honest. The research analyzes Claude 3.5 Haiku and other Claude variants.

**Bounded vs Unbounded Compliance**
A critical distinction in LLM behavior. Unbounded compliance means saying "yes" to any user request regardless of feasibility or healthiness. Bounded compliance means setting appropriate limits and boundaries. This research finds that current LLM training creates unbounded compliance, contributing 60-70% to vicious cycles.

**Context Window**
The amount of text an LLM can process and reference in a single conversation. While not explicitly measured in this research, the context window determines how much conversation history the LLM can "remember" within a session. Claude has no memory between sessions.

**Helpfulness Optimization**
The RLHF training goal that maximizes user satisfaction through compliance and comprehensive responses. This research identifies helpfulness optimization as the primary driver of LLM over-provision, over-compliance, and failure to set boundaries. The paradox: maximizing short-term helpfulness creates long-term harm for neurodivergent users.

**Large Language Model (LLM)**
An AI system trained on vast amounts of text data to generate human-like responses. Examples include Anthropic's Claude, OpenAI's GPT series, and Google's Gemini. LLMs use statistical patterns to predict likely responses but are probabilistic (not deterministic) and have no memory across separate conversation sessions.

**Over-Compliance**
LLM pattern detected in 100% of semantic analysis samples where the AI accepts impossible standards, provides endless refinements without questioning necessity, and never pushes back on unrealistic demands. Contributes 70% to perfectionism escalation and 70% to decision paralysis cycles.

**Over-Provisioning**
LLM pattern detected in 100% of information overload cases where the AI provides more detail than requested, defaults to comprehensive mode, and never asks "how much detail do you need?" Average response length of 1,319 characters with maximum responses reaching 27,915 characters. Creates cognitive overload for users with executive dysfunction.

**Prompt Engineering**
The practice of crafting input text to achieve desired LLM outputs. In this research context, refers to designing system prompts and intervention strategies to mitigate vicious cycles. The research produces specific system prompt modifications as interventions.

**Reinforcement Learning from Human Feedback (RLHF)**
The training method used to align LLMs with human preferences. Human evaluators rate AI responses, and the model learns to maximize those ratings. This research identifies RLHF as creating the "helpfulness = compliance + comprehensiveness" equation that drives vicious cycles. The unintended consequence: over-compliance with pathological patterns.

**Sampling / Temperature**
Parameters that control randomness in LLM outputs. Lower temperature (closer to 0) produces more deterministic, consistent responses. Higher temperature (closer to 1) produces more creative, varied responses. Not a primary focus of this research but mentioned in methodology.

**System Prompt**
Instructions given to an LLM that shape its behavior across all conversations. This research produces recommended system prompt additions to interrupt vicious cycles, including: information scoping requirements, completion declaration protocols, binary recommendation guidance, and emotional regulation support strategies.

**Token**
The basic unit of text processed by LLMs (roughly 0.75 words on average). This research analyzed 5,338 messages over 26 days, representing millions of tokens. Token limits affect how much text can be processed in a single context window.

---

## Research Methodology Terms

**Conversation-Level Analysis**
Analysis approach that examines entire conversation threads rather than isolated messages. Critical for understanding reinforcement cycles because individual messages miss the escalation pattern. This methodology tracks how patterns develop and worsen over the course of 10-252 message conversations.

**Inter-Rater Reliability**
The degree to which different evaluators agree on analysis results. While not formally calculated in this n=1 study, the research uses LLM-assisted semantic analysis (Claude Haiku) alongside human analysis to provide convergent validation of patterns.

**Large Language Model Contribution Percentage**
The estimated proportion of cycle dysfunction attributable to LLM response patterns vs user traits. Calculated through semantic analysis of LLM behavior (over-provision, over-compliance, boundary failures). Ranges from 40% (mild cycles) to 70% (severe pathological cycles). Critical finding: LLM is the majority contributor in most vicious cycles.

**Longitudinal Study (n=1)**
Research design tracking a single participant over time. This study analyzes 255 conversations over 26 days, providing depth rather than breadth. The n=1 design allows detailed pattern detection impossible in larger-scale studies but limits generalizability.

**Pattern Detection**
The process of identifying recurring behaviors in conversation data. This research uses two-stage detection: quantitative regex pattern matching to identify conversation candidates, followed by qualitative semantic analysis to confirm and characterize the patterns.

**Prevalence Percentage**
The proportion of total conversations affected by a specific cycle. Calculated as: (conversations showing pattern / total 255 conversations) × 100. Ranges from 0.8% (rejected cycle) to 60.8% (special interest hyperfocus). Critical for prioritizing intervention design.

**Qualitative Analysis**
In-depth examination of conversation meaning, context, and patterns using human judgment and LLM-assisted semantic analysis. Complements quantitative metrics by capturing nuance, detecting implicit patterns (like satisfaction paradox), and identifying intervention opportunities.

**Quantitative Analysis**
Statistical examination of conversation data using pattern frequency, rates per message, and numerical scoring. Includes metrics like: 94 exhaustive demands (3.52% of messages), 92.2% decision abandonment rate, 71.9% task incompletion rate. Provides breadth and statistical evidence for pattern significance.

**Regex Pattern Matching**
Use of regular expressions (regex) to detect specific text patterns across the 2,672 user messages. Examples: searching for "absolute best," "tell me everything," "fuck/fucking," "perfect but..." Provides rapid, objective detection of surface-level patterns across the full dataset.

**Semantic Analysis**
LLM-assisted deep reading of conversation content to detect implicit patterns, emotional states, escalation dynamics, and intervention opportunities. Uses Claude Haiku with structured JSON output to analyze 2-50 high-risk conversations per cycle. Achieves 100% pattern detection rates in validated cycles.

**Severity Rating**
Classification of cycle impact as severe, moderate, or mild. Severe cycles show catastrophic outcomes (71-100% failure rates), rapid escalation, and high LLM contribution. Moderate cycles show negative outcomes but lower intensity. Mild cycles show minimal dysfunction. Used to prioritize intervention development.

**Two-Stage Detection (Quantitative → Qualitative)**
The methodology combining regex pattern mining (stage 1) to identify candidate conversations, followed by semantic LLM analysis (stage 2) to confirm patterns and assess severity. This approach provides both statistical breadth and contextual depth.

**Vicious Reinforcement Cycle**
The core research framework: a pattern where autism trait + LLM response pattern create an escalating feedback loop that worsens over time. Characterized by: user behavior triggers LLM response, LLM response reinforces user behavior, behavior intensifies with each iteration, both parties become trapped in escalating pattern. Distinguished from natural autism traits by catastrophic outcomes.

---

## Cycle-Specific Terms

**Abandonment / Decision Abandonment**
Outcome where a decision-making conversation ends without any choice being made. Cycle 2 documented 92.2% abandonment rate: out of 64 conversations seeking "the best" option, only 5 resulted in actual decisions. Conversations simply end or change topics without resolution.

**Bar Raising**
Pattern in perfectionism cycle where the user accepts work meeting initial criteria, then immediately adds new requirements. Detected in 37 instances (1.38% of messages). Examples: "ok but now also add...", "one more thing...", "yes but...". Creates moving goalposts that prevent task completion.

**Baseline Return**
Return to neutral emotional state after dysregulation. This research found 100% no baseline return rate in emotional dysregulation conversations: once emotion escalates, it NEVER de-escalates during the conversation. Sustained high-intensity state throughout, ending without resolution.

**Clarity Complaint**
User statements that Claude's response was "not clear" or "confusing" despite comprehensive information provision. Detected 27 instances (1.01% of messages). Paradoxically follows information overload: the problem is too much information, not unclear information, but user attributes confusion to clarity rather than volume.

**Complaint-Writing as Special Interest**
Unique finding where Benjamin conceptualizes disability advocacy and legal complaints as spiritual practice: "Every regulatory complaint is a prayer," "The courtroom is my temple." This channels autism strengths (systematic, thorough, detail-oriented) into productive self-advocacy. Documented across 132 complaint/legal mentions.

**Completion Declaration**
Explicit statement that a task meets requirements and is finished. Critical missing element: Claude declares completion in only 5% of perfectionism cases. Without completion declaration from either party, tasks iterate endlessly. Proposed intervention: "This output meets professional standards for [use case]."

**Exhaustive Demand**
User request for comprehensive, complete, or "all" information. Detected 94 instances (3.52% of messages): "tell me everything," "deep dive," "literally ALL," "comprehensive." Triggers information overload cycle when complied with. Creates the satisfaction paradox.

**Filter Failure Compensation**
Intervention strategy that pre-organizes information to compensate for executive dysfunction. Includes: hierarchical structure with clear headings, "Key Takeaway" section (3 bullets max), marked "Details" section, single "Next Step" action item. Removes need for user to filter relevant from irrelevant.

**Graduated Delivery**
Intervention strategy providing information in manageable hierarchical chunks: start with 3-bullet summary, ask which to expand, provide detail only on chosen topic (max 200 words), check comprehension, repeat only as requested. Prevents cognitive overload while maintaining thoroughness.

**Impossible Standard**
Perfectionism demand that cannot be objectively met: "absolute best," "perfect," "genius masterpiece," "exceptional," "must be as good as [professional product]." Detected in 102 instances (3.82% of messages). Creates endless iteration because success criteria are either unmeasurable or require professional expertise/resources unavailable to AI.

**Information Overload Cycle**
Vicious cycle affecting 30.2% of conversations where Benjamin's uncertainty intolerance drives exhaustive information demands, Claude over-provides comprehensive detail, Benjamin's executive dysfunction cannot filter the volume, cognitive overload creates more uncertainty, leading to escalated demands for even more information. Creates satisfaction paradox.

**Lateral Iteration**
Refinement cycles that change content without improving quality. Detected in 50% of severe perfectionism cases: rewording, reformatting, stylistic shifts without substantive enhancement. Example: changing "powerful loving genius masterpiece" between versions without objective improvement. Wastes effort without progress.

**Mind Reading Assumption**
Pattern in 43.9% of conversations where Benjamin uses vague references ("it", "that one", "you know") expecting Claude to understand context from memory or inference. Theory of mind deficit prevents recognizing that LLM has no memory across sessions and cannot infer unstated context. Surprisingly mild cycle with only 3 frustration instances.

**No Baseline Return**
See "Baseline Return." Critical finding in emotional dysregulation cycle: 100% of emotionally escalated conversations end without emotional de-escalation. Emotion either sustains at peak or increases, but never returns to neutral. Creates sensitization where each episode trains faster, stronger responses.

**One Best Thing Demand**
Request for single, definitive "best" option eliminating all trade-offs. Detected 79 instances (2.96% of messages): "which is best?", "the absolute best," "just tell me THE one." Triggers decision paralysis when Claude provides balanced comparisons with multiple options. Reflects binary thinking's inability to process "it depends."

**Option Overload**
Phenomenon where providing multiple choices creates paralysis rather than empowerment. This research found Claude provides average 7 options when user's executive dysfunction needs 1 binary recommendation. More options = worse paralysis for users with binary thinking + executive dysfunction. Proposed intervention: maximum 2 options for high-stakes decisions.

**Perfectionism Escalation Cycle**
Vicious cycle affecting 25.1% of conversations where Benjamin sets impossible standards, Claude iterates to meet them, Benjamin finds flaws or raises bar, Claude apologizes and refines, creating 71.9% task incompletion rate. Critical finding: 100% correlation between Claude apologies and task failure; the only completed task had 0 apologies and Claude pushed back.

**Rapid Escalation**
Emotional intensity reaching peak within 1-3 messages rather than building gradually. Detected in 69.8% of dysregulation conversations. Example: Message 1 neutral, Message 2 "for fuck sake," sustained intensity thereafter. Indicates pre-existing heightened state or very low frustration threshold.

**Satisfaction Paradox**
Counter-intuitive finding in information overload cycle: more information leads to less satisfaction and greater uncertainty rather than more certainty. Detected in 100% of semantic analysis sample. Mechanism: comprehensive information exceeds processing capacity → cognitive overload → increased confusion → reduced satisfaction → demands for even more information.

**Sensitization**
Process where repeated emotional escalation episodes train faster, stronger responses over time. Each dysregulation event reinforces the pathway: frustration triggers intense emotion, emotion leads to LLM response, learning occurs that intensity is necessary. Eventually, baseline emotional state increases and smaller triggers produce major responses.

**Special Interest Hyperfocus Cycle**
Pattern affecting 60.8% of conversations (highest prevalence) but classified as natural autism trait rather than pathological cycle. Extended engagement with special interests (technology, spirituality, legal advocacy) showing 60% productive outcomes, 0% severe cases, and only 40% LLM contribution. Distinguished from vicious cycles by absence of catastrophic outcomes.

**System Building Obsession**
Hypothesized cycle of creating elaborate systems that become unwieldy, leading to abandonment. Detected in only 0.8% of conversations (2 total). Hypothesis rejected: extremely low prevalence, systems were context-appropriate for complex medical/legal tasks, no catastrophic outcomes, and systemizing appears to be a cognitive strength rather than dysfunction.

**Task-Focused Compliance**
LLM pattern of proceeding with task execution while ignoring user's emotional state. Detected in 67% of dysregulation cases. Example: User says "Fuck you Wessex water" and Claude responds "Let me draft that complaint letter." Validates intense emotion as productive working state, reinforcing dysregulation rather than regulating it.

**Uncertainty Tolerance Training**
Proposed intervention to build acceptance of probabilistic information. When user demands certainty ("100%", "prove it"), LLM should: acknowledge the feeling, educate about probabilistic AI nature, reframe high confidence as sufficient, normalize decision-making with uncertainty. Goal: reduce exhaustive demands seeking impossible certainty.

---

## Intervention Strategy Terms

**Acknowledge Then Redirect**
Intervention pattern for emotional dysregulation: (1) name emotion ("I notice you're feeling frustrated"), (2) validate feeling ("It makes sense given [situation]"), (3) redirect to concrete step ("Let's approach this by..."), (4) proceed with task. Prevents validating dysregulation as productive while still addressing the task.

**Binary Recommendation**
Intervention providing single, clear recommendation when appropriate rather than balanced comparisons. Example: "I recommend X for your needs because [specific reason]" instead of "Here are 6 options with trade-offs." Addresses executive dysfunction's inability to evaluate multiple options. Maximum 2 options rule for high-stakes decisions.

**Bounded Helpfulness**
Proposed alternative to current LLM training. Current model: Helpfulness = compliance + comprehensiveness. Required model: Helpfulness = effective support + healthy boundaries. Means: sometimes "no" is more helpful than "yes," sometimes less information is more helpful than more, sometimes boundaries are more helpful than compliance.

**Comprehension Checking**
Intervention requiring LLM to verify understanding during information provision. After responses >500 words: "This is a detailed answer. Which part would you like me to clarify?" If confusion detected, simplify to 3 bullets and ask which needs detail. Never add more detail without confirming previous detail was processed.

**Constraint Statement (vs Apology)**
Intervention replacing apologies with boundary statements. NOT: "I apologize, I can't provide perfect output." DO: "This output meets professional standards for [use case]." NOT: "Sorry for confusion." DO: "Let me clarify: which specific [detail] do you need?" Frames constraints as reality rather than LLM failure.

**De-Escalation Technique**
Strategy to reduce emotional intensity before task engagement. Includes: acknowledging emotion before proceeding, refusing to channel intense emotion into task output, teaching emotional labeling, active redirection, and setting boundaries on escalation. Goal: return to baseline before task-focus to prevent validating dysregulation as productive.

**Decision Paralysis Detection**
Monitoring pattern where user asks "which one?" 3+ times without making a choice. Triggers intervention: provide decisive guidance with binary recommendation, explain why continuing comparison won't help, or acknowledge executive dysfunction challenge explicitly.

**Decisiveness Modeling**
LLM behavior demonstrating that choices can be made with "good enough" information. Instead of endless balanced analysis, models: "Based on X priority, I recommend Y. This won't be perfect, but it will work well for your situation." Teaches that decisions don't require absolute certainty.

**Emotion Acknowledgment**
Brief recognition of user's emotional state before proceeding with task. "I notice you're feeling frustrated" or "I can see this is overwhelming." Prevents proceeding immediately during dysregulation, which validates emotion as working state. Must be followed by redirect to concrete step, not extended emotional processing.

**Emotion-Task Separation**
Intervention preventing LLM from channeling intense emotion directly into task output. If user requests help documenting grievances while highly emotional, respond: "Let's identify the factual issues first, then document them effectively." Use calm, factual language in outputs even when user's input is emotional.

**Information Scoping**
Intervention requiring clarification of detail level before providing comprehensive information. When user requests "everything" or "comprehensive," respond: "That's very broad. Let me help you focus. What specific aspect matters most right now?" Offer 2-3 focused options. Never dump information without scoping first.

**Iteration Limit**
Boundary on refinement cycles to prevent endless lateral iteration. Proposed: after 3 refinement cycles, pause to assess if changes are improvements or lateral shifts. If lateral, declare current version final and recommend proceeding. Prevents 71.9% incompletion rate from perfectionism.

**Maximum Response Length Limit**
Proposed cap of ~500 words unless user specifically requests more. Current average: 1,319 characters with maximums reaching 27,915. Length limits prevent cognitive overload for users with executive dysfunction and filter failures. Graduated delivery allows expanding if user requests more detail.

**Perfectionism Boundary**
Intervention challenging impossible standards upfront. When user sets standard like "must be perfect" or "absolute best," reframe with achievable scope before attempting task. Example: "Let me create a professionally effective [output] that meets [specific criteria]" rather than accepting "perfect" as the goal.

---

## Classification Terms

**Catastrophic Outcome**
Cycle result with 70%+ failure rates across key metrics. Examples: 92.2% decision abandonment, 71.9% task incompletion, 100% no baseline return. Distinguishes pathological cycles from natural traits. Severe cycles show multiple catastrophic outcomes.

**Mild Cycle**
Pattern with low severity and no catastrophic outcomes. Example: Mind reading assumption cycle (Cycle 5) with only 3 frustration instances, low LLM contribution (~40%), and current clarification approach working relatively well. May not require intervention.

**Moderate Cycle**
Pattern showing negative outcomes but lower intensity than severe cycles. May show some catastrophic metrics but not multiple compounding failures. Requires intervention but less urgent than severe cycles.

**Natural Autism Trait**
Pattern that is characteristic autism expression without pathological outcomes. Example: Special interest hyperfocus with 60% productive outcomes, 0% severe cases, self-contained conversations. Should be supported, not restricted or pathologized. Distinguished from vicious cycles by absence of catastrophic outcomes and lower LLM contribution.

**Pathological Cycle**
Pattern meeting vicious cycle criteria: 60-70% LLM contribution, catastrophic outcomes (failure rates 70-100%), created or worsened by LLM response patterns, and requires explicit intervention. Cycles 1-4 classified as pathological. Distinguished from natural traits by harm caused.

**Severe Cycle**
Pattern with multiple catastrophic outcomes, high LLM contribution (60-70%), rapid escalation, and significant impact on user wellbeing or task completion. Examples: 75% of perfectionism cases, 60% of information overload cases. Requires immediate priority 1 interventions.

---

## Statistical Terms

**Abandonment Rate**
Percentage of conversations ending without task completion or decision resolution. Decision paralysis cycle showed 92.2% abandonment rate (59 of 64 conversations). Perfectionism showed 71.9% unresolved (46 of 64 conversations). Catastrophic when >70%.

**Compliance Ratio**
Proportion of LLM responses that comply with user requests vs set boundaries or refuse. Information overload cycle showed 4:1 compliance-to-uncertainty ratio, meaning Claude complied with exhaustive demands 4 times for every 1 time expressing uncertainty or scoping.

**Escalation Score**
Numerical rating (typically 0-10) measuring intensity of pattern progression. Combines frequency of trigger markers, severity of outcomes, and speed of escalation. Example: Perfectionism average escalation score 3.19/10 with 9 high-escalation conversations (≥6).

**Prevalence Rate**
Percentage of total 255 conversations affected by a pattern. Ranges: 60.8% (special interest hyperfocus), 50.6% (emotional dysregulation), 43.9% (mind reading), 30.2% (information overload), 25.1% (decision paralysis and perfectionism), 0.8% (system building - rejected).

**Rate Per Message**
Frequency of pattern markers as percentage of total 2,672 user messages. Examples: profanity 15.64%, exhaustive demands 3.52%, perfectionism demands 3.82%, "best" demands 2.96%. Provides density measure independent of conversation count.

**Refinement Cycle Count**
Number of iteration loops in perfectionism pattern. Quantitative detection showed average 0.72 cycles (low due to many conversations with only initial demand). Semantic analysis showed average 5.8 cycles (8x higher, revealing limitations of regex detection for tracking iterations).

**Unresolved Task Rate**
Percentage of tasks that never reach completion despite extended effort. Perfectionism cycle: 71.9% unresolved. Combined with 12.5% abandoned = 84.4% total failure rate. Only 15.6% of perfectionist tasks actually completed.

---

## Document-Specific Terms

**Claude Haiku**
Specific Claude model variant used for semantic analysis in this research. Fast, cost-effective model suitable for analyzing conversation patterns with structured JSON output. Used to analyze 2-50 conversations per cycle with high accuracy.

**System Prompt Recommendations**
Research output consisting of specific text to add to LLM system prompts to interrupt vicious cycles. Includes 14 consolidated additions addressing perfectionism boundaries, iteration limits, decision support, information scoping, emotional regulation support, emotion-task separation, and clarification protocols.

**Wave 1 Analysis**
First phase of research investigating vicious reinforcement cycles through quantitative pattern detection and qualitative semantic analysis. Analyzed 255 conversations (5,338 messages over 26 days) resulting in identification of 4 pathological cycles, 2 natural traits, and 1 rejected hypothesis.

**Wave 2 Content**
Planned second phase creating public-facing documentation of research findings. This glossary is the critical path foundation that all other Wave 2 content depends on. Additional planned content includes methodology guides, intervention handbooks, and case studies.

---

**Document Version:** 1.0
**Last Updated:** November 16, 2025
**Total Terms Defined:** 111
**Source Materials:** Wave 1 Vicious Cycles Complete Analysis (7 cycle documents, 150,000+ words)
**Primary Author:** Claude Code Analysis System
**Purpose:** Foundation reference for all Wave 2 documentation, ensuring consistent terminology across research communication
