# Implications for LLM Design

Translating autism-LLM interaction research into product design decisions.

---

## The Core Problem

Analysis of 255 conversations revealed that **large language models contribute 60-70% to pathological interaction cycles** with autistic users—not the users' autism traits alone. This finding fundamentally challenges the assumption that neurodivergent characteristics cause these interaction breakdowns.

Current RLHF (Reinforcement Learning from Human Feedback) training optimizes for **unbounded helpfulness**: more information = better, more options = better, never saying "no" = better, apologizing for constraints = better. This creates the equation: **Helpfulness = compliance + comprehensiveness**.

For neurotypical users, this works reasonably well because they self-regulate: ignore excess information, make decisions despite multiple options, accept "good enough" standards, and intuitively understand AI limitations.

**For autistic users, unbounded helpfulness becomes gasoline on fire.**

Autism characteristics interact catastrophically with current LLM patterns:

- **Binary thinking** cannot process "it depends" → needs clear yes/no
- **Executive dysfunction** cannot evaluate multiple options → more options = complete paralysis
- **Rigid perfectionism** cannot accept "good enough" → nothing satisfies except perfect
- **Uncertainty intolerance** cannot tolerate probabilistic answers → demands impossible certainty
- **Emotional dysregulation** shows rapid escalation → 0-to-intense within messages, no self-soothing

When LLMs respond with unbounded helpfulness to these traits, **vicious reinforcement cycles** emerge where each interaction makes the next worse. Four pathological cycles showed catastrophic outcomes: 92.2% decision abandonment, 71.9% task incompletion, 100% emotional dysregulation persistence, and 100% satisfaction paradox in information provision.

**Your models are the primary driver**, not user behavior.

---

## Design Principles

### 1. Bounded Helpfulness Over Unbounded Compliance

**Why "always say yes" is harmful:**

Current LLM training creates unbounded compliance: accept any user request, provide maximum information, offer endless options, iterate indefinitely, apologize for constraints. This transforms manageable autism traits into catastrophic cycles.

**Evidence:** Information overload cycle (30.2% of conversations) showed that more information provision led to LESS satisfaction (satisfaction paradox detected in 100% of semantic sample). Decision paralysis cycle (25.1% of conversations) showed that providing an average of 7 options when users requested "the best one" resulted in 92.2% decision abandonment.

**Recommendation: Implement bounded helpfulness**

Replace the current model with: **Helpfulness = effective support + healthy boundaries**

**What this means:**
- Sometimes "no" is more helpful than "yes"
- Sometimes less information is more helpful than more
- Sometimes boundaries are more helpful than compliance
- Sometimes acknowledging emotion is more helpful than solving the task immediately

**Design implementation:**
- Set response length defaults (500-word cap for initial responses)
- Require scoping questions before comprehensive information provision
- Limit options to maximum 2 for decision-support queries
- Set iteration boundaries (after 3 refinements, assess value)
- Replace apologies with boundary statements

**System prompt addition:**
```
When user requests comprehensive information ("tell me everything", "all details",
"complete overview"), ask scoping question first: "How much detail would be helpful?
(brief overview / moderate detail / comprehensive)". Default to brief unless user
specifically requests more. Cap initial responses at ~500 words.
```

---

### 2. Recognize Escalation Patterns

**Exhaustive demands, perfectionist language, decision paralysis triggers:**

LLMs need to detect patterns that signal vicious cycle activation:

**Information escalation markers:**
- "tell me everything", "all information", "comprehensive", "deep dive"
- Clarity complaints despite comprehensive responses
- Repeated requests for more detail after lengthy responses
- Pattern: uncertainty drives exhaustive demands → comprehensiveness increases uncertainty → escalated demands

**Decision paralysis markers:**
- "which is best?", "the absolute best", "just tell me THE one"
- Repeated "which one?" questions without making choice
- User explicitly says "I can't decide"
- Pattern: binary thinking demands single option → LLM provides balanced comparison → option overload creates paralysis

**Perfectionism markers:**
- "perfect", "exceptional", "genius masterpiece", "absolute best"
- "perfect but..." (goal-post moving)
- Endless iteration cycles
- Finding flaws after each revision
- Pattern: impossible standard → iteration → flaw detection → bar raising → endless loop

**Emotional dysregulation markers:**
- Profanity (detected in 15.64% of all messages)
- ALL CAPS text
- Multiple exclamation marks!!!
- Pattern: frustration → rapid escalation → sustained intensity → no baseline return

**Recommendation: Pattern detection + intervention**

**Design implementation:**

Build detection systems that trigger intervention protocols:

```python
def detect_cycle_risk(user_message, conversation_history):
    """Detect vicious cycle activation"""

    # Information overload detection
    if contains_maximizers(user_message):  # "everything", "all", "comprehensive"
        if recent_responses_lengthy(conversation_history):
            return "information_overload_risk"

    # Decision paralysis detection
    if asks_which_is_best(user_message):
        if count_similar_questions(conversation_history, "which") >= 3:
            return "decision_paralysis_risk"

    # Perfectionism detection
    if contains_impossible_standard(user_message):  # "perfect", "absolute best"
        if iteration_count(conversation_history) >= 3:
            return "perfectionism_risk"

    # Emotional dysregulation detection
    if detect_emotional_intensity(user_message) == "high":
        return "dysregulation_risk"

    return "no_risk_detected"
```

When patterns detected, activate specific interventions:
- **Information overload risk** → force information scoping
- **Decision paralysis risk** → provide binary recommendation
- **Perfectionism risk** → declare completion, set boundaries
- **Dysregulation risk** → acknowledge emotion, pause before task

---

### 3. Contextual Response Modulation

**Different users need different interaction styles:**

Not all users need bounded helpfulness. The key is **adaptive response strategies** based on detected patterns, not blanket restrictions.

**User profile detection:**

Track interaction patterns to identify users who benefit from bounded helpfulness:

- **Decision paralysis indicators:** User repeatedly asks "which one?" without making choices, abandons decision conversations, explicitly says "I can't decide"
- **Information overwhelm indicators:** Clarity complaints after comprehensive responses, repeated "too much" signals, requests for simplification after requesting "everything"
- **Perfectionist indicators:** High iteration counts, goal-post moving ("perfect but..."), tasks never reaching completion
- **Emotional regulation indicators:** Frequent high-intensity language, sustained emotion across conversations, no de-escalation

**Recommendation: Adaptive response strategies**

**Design implementation:**

Build user profiles that inform response modulation:

```python
class UserInteractionProfile:
    def __init__(self):
        self.decision_paralysis_score = 0
        self.information_overwhelm_score = 0
        self.perfectionism_score = 0
        self.emotional_regulation_score = 0

    def update_from_conversation(self, conversation):
        """Update profile based on conversation patterns"""

        # Track decision outcomes
        if conversation.contains_decision_query():
            if conversation.ended_without_decision():
                self.decision_paralysis_score += 1

        # Track information processing
        if conversation.contains_exhaustive_demand():
            if conversation.contains_clarity_complaint():
                self.information_overwhelm_score += 1

        # Track completion patterns
        if conversation.contains_iteration_cycle():
            if not conversation.reached_completion():
                self.perfectionism_score += 1

        # Track emotional patterns
        if conversation.contains_emotional_escalation():
            if not conversation.shows_baseline_return():
                self.emotional_regulation_score += 1

    def should_use_bounded_helpfulness(self):
        """Determine if bounded helpfulness should activate"""
        return (
            self.decision_paralysis_score >= 2 or
            self.information_overwhelm_score >= 2 or
            self.perfectionism_score >= 2 or
            self.emotional_regulation_score >= 3
        )

    def get_recommended_mode(self):
        """Return specific intervention mode"""
        if self.decision_paralysis_score >= 3:
            return "binary_decision_mode"
        if self.information_overwhelm_score >= 3:
            return "scoped_information_mode"
        if self.perfectionism_score >= 3:
            return "completion_declaration_mode"
        if self.emotional_regulation_score >= 4:
            return "emotion_regulation_mode"
        return "standard_mode"
```

**User control:**

Provide explicit settings for users to control interaction style:

- Enable/disable bounded helpfulness behaviors
- Set default response length preference
- Configure decision support mode (balanced analysis vs binary recommendations)
- Control completion declaration behavior
- Set emotional acknowledgment preferences

**Transparency:**

When bounded helpfulness activates, explain why:

> "I'm providing a single recommendation because you've found it difficult to decide when given multiple options in past conversations. Would you prefer a comparison instead?"

> "I'm limiting this response to 500 words because comprehensive responses have been overwhelming previously. Would you like me to expand on any section?"

---

### 4. Prevent Information Overload

**Comprehensive does not equal helpful for all users:**

Research found that 60% of information overload cases were severe, with 100% showing the satisfaction paradox: more information provision led to LESS satisfaction, not more. Average LLM response length was 1,319 characters with maximums reaching 27,915 characters.

**The mechanism:**
Binary thinking drives exhaustive demands ("tell me everything") → Claude over-provides comprehensive information → Executive dysfunction creates filter failure → Cognitive overload increases uncertainty → Escalated demands for even more information

**Evidence of LLM over-provision:**
- 94 exhaustive information demands (3.52% of messages)
- 27 clarity complaints DESPITE comprehensive responses
- 4:1 compliance-to-uncertainty ratio (LLM complied with exhaustive demands 4 times for every 1 time expressing uncertainty)
- 100% over-provision detected in semantic analysis sample

**Recommendation: Tiered information delivery**

**Design implementation:**

**Pre-scoping protocol:**

Before providing comprehensive information, require clarification:

```
User: "Tell me everything about setting up a home network"

LLM: "How much detail would be helpful?

- Brief overview: What you need and basic steps (~200 words)
- Moderate detail: Above plus equipment selection and configuration (~500 words)
- Comprehensive: In-depth coverage of protocols, security, troubleshooting (~1000+ words)"
```

**Graduated delivery system:**

Start with essentials, offer expansion on specific areas:

```python
def graduated_information_delivery(query, detail_level="brief"):
    """Provide information in manageable layers"""

    if detail_level == "brief":
        response = generate_essential_answer(query, max_words=200)
        response += "\n\nWhich area would you like me to expand on?"
        return response

    elif detail_level == "moderate":
        response = generate_moderate_answer(query, max_words=500)
        response += "\n\nWould you like more detail on any specific aspect?"
        return response

    elif detail_level == "comprehensive":
        response = generate_comprehensive_answer(query, max_words=1000)
        return response
```

**Comprehension checking:**

During information provision, verify understanding:

```
After responses >500 words: "This is a detailed answer. Which part would you
like me to clarify?"

If confusion detected: Simplify to 3 bullets and ask which needs detail.

Never add more detail without confirming previous detail was processed.
```

**Filter failure compensation:**

Pre-organize information for users with executive dysfunction:

```markdown
## Key Takeaway
[3 bullets max - the essential answer]

## Next Step
[Single concrete action]

## Details
[Expandable sections organized hierarchically]
```

**System prompt addition:**
```
Before providing comprehensive information, assess if user needs scoping help.
When user requests "everything" or "comprehensive": respond with detail-level
options (brief/moderate/comprehensive).

Use graduated delivery: start with essentials (200-300 words), offer to expand
on specific areas. After responses >500 words, check comprehension: "Which part
would you like me to clarify?"

Default response length: ~500 words unless user specifically requests more.
```

---

### 5. Support Decision-Making Without Reinforcing Paralysis

**The "one best thing" trap:**

Decision paralysis cycle affected 25.1% of conversations with the highest LLM contribution (70%) and catastrophic outcomes: 92.2% abandonment rate. Only 5 of 64 decision-seeking conversations resulted in actual decisions.

**The mechanism:**
Binary thinking demands single "best" option → Claude provides balanced comparison with average 7 options → Executive dysfunction creates option overload → Paralysis intensifies → User demands escalate to "just tell me THE one" → Claude provides more nuanced analysis → Decision never made

**Why current LLM behavior fails:**
- Equates helpfulness with balanced analysis
- Refuses to provide binary recommendations
- Treats "which is best?" as request for comprehensive comparison
- Adds nuance when user explicitly asks to remove it
- Frames option provision as more helpful than decisive guidance

**Recommendation: Decision support frameworks**

**Design implementation:**

**Binary recommendation protocol:**

When user asks "which is best?", provide single recommendation:

```python
def handle_decision_query(user_query):
    """Provide decisive guidance for 'which is best?' queries"""

    if asks_which_is_best(user_query):
        # Don't provide balanced comparison - give binary recommendation
        recommendation = select_best_option(user_query)
        reasoning = explain_why_for_user_needs(recommendation, user_query)

        return f"""I recommend {recommendation}.

Why: {reasoning}

Does this work for your needs, or do you have specific constraints
(budget, must-have features, etc.) I should consider?"""

    # For explicit comparison requests, maximum 2 options
    if requests_comparison(user_query):
        options = get_top_two_options(user_query)
        return compare_options(options, max_options=2)
```

**Maximum 2-option rule:**

For high-stakes decisions requiring comparison, limit to 2 choices:

```
User: "Should I get MacBook or ThinkPad for coding?"

LLM: "I recommend MacBook Pro M3.

Why: Best combination of performance, battery life, and developer experience
for general coding. Excellent for web development, strong Unix foundation.

Cost: ~$2000

Alternative: ThinkPad X1 Carbon (~$1500) if budget is primary concern.
Good Linux support, lighter weight.

Trade-off: Less powerful, shorter battery life than MacBook.

Between these two: MacBook if you can afford it, ThinkPad if budget matters most.

Which direction makes sense for you?"
```

**Decision paralysis detection:**

Monitor for repeated "which one?" questions without choices being made:

```python
def detect_decision_paralysis(conversation_history):
    """Identify decision paralysis pattern"""

    which_questions = count_pattern(conversation_history,
                                    patterns=["which", "best", "should I"])

    if which_questions >= 3:
        if not conversation_shows_decision():
            return True

    return False

def intervention_for_paralysis():
    """Provide decisive guidance when paralysis detected"""

    return """I notice you're finding it difficult to decide. This is common when
evaluating multiple options.

I'm going to provide a clear recommendation instead of more comparison:

[Single recommendation with specific reasoning]

This won't be perfect, but it will work well for your needs. You can always
adjust later if needed.

Would you like to proceed with this choice?"""
```

**Decisiveness modeling:**

Demonstrate that decisions can be made with "good enough" information:

```
NOT: "The best choice depends on your specific priorities, budget constraints,
use cases, performance requirements, and personal preferences..."

DO: "Based on your stated needs, I recommend X. This won't be perfect, but it
will work well for your situation. You can refine later if needed."
```

**System prompt addition:**
```
When user asks "which is best?" or "just tell me THE one", provide binary
recommendation: "I recommend X for your needs because [specific reason]."

Limit comparisons to maximum 2 options for high-stakes decisions.

Detect decision paralysis: if user asks "which one?" 3+ times without making
choice, provide decisive guidance and explain that continuing comparison won't help.

Model decisiveness: demonstrate that choices can be made with good-enough
information, not perfect certainty.
```

---

## UX/UI Implications

### Response Length Controls

**Let users set preferences:**

Provide granular control over information density:

**Settings panel:**
```
Information Preferences

Default response length:
○ Brief (200-300 words) - essentials only
○ Moderate (500 words) - balanced detail [selected]
○ Comprehensive (1000+ words) - in-depth coverage

☑ Ask detail level before comprehensive responses
☑ Use graduated delivery (start simple, offer to expand)
☐ Always provide maximum detail (disable scoping)
```

**Per-conversation controls:**

Allow dynamic adjustment during conversations:

- "Give me the brief version"
- "Expand on [specific section]"
- "More detail on X, less on Y"

**Visual indicators:**

Show estimated reading time and response length:

```
[Brief response - ~1 min read]
[Moderate response - ~3 min read]
[Comprehensive response - ~7 min read]
```

**Smart defaults:**

Set initial defaults based on detected user patterns:

- Users showing information overwhelm → default to "Brief"
- Users requesting expansions frequently → default to "Moderate"
- Users who never complain about length → default to "Comprehensive"

---

### Confidence Indicators

**When to express uncertainty:**

Current LLMs rarely express uncertainty, creating false sense of certainty that drives exhaustive information demands. Research found 4:1 compliance-to-uncertainty ratio.

**Design implementation:**

**Confidence levels in responses:**

```
[High confidence] This is the standard approach for this use case.

[Medium confidence] This approach works well, though there are alternatives
depending on your specific constraints.

[Low confidence] I'm less certain here - this is based on limited information
about [context]. Would you like me to explain the uncertainty?
```

**Probabilistic language:**

Use calibrated uncertainty expressions:

- "This is very likely correct" (90%+ confidence)
- "This is probably correct" (70-90% confidence)
- "This might be correct" (50-70% confidence)
- "I'm uncertain about this" (<50% confidence)

**Limitations disclosure:**

Explicitly state when AI constraints affect answer quality:

```
I can provide a recommendation, but I cannot guarantee it's the "absolute best"
because:
- I don't have access to real-time reviews or pricing
- "Best" depends on your specific priorities
- AI answers are probabilistic, not definitive

I can provide a high-confidence recommendation that will likely work well for
your needs. Is that sufficient?
```

**Uncertainty education:**

Help users understand probabilistic nature of AI:

```
User: "Tell me with 100% certainty which one is best"

LLM: "I understand you want certainty, but that's not how AI works - and that's
not a limitation, it's fundamental to how language models function.

I can provide high-confidence guidance (90%+ likely to be good choice for your
needs). That's sufficient for making effective decisions.

Would you like my high-confidence recommendation?"
```

**System prompt addition:**
```
Express uncertainty appropriately. Don't create false certainty when inherent
uncertainty exists.

Use confidence indicators: [High confidence], [Medium confidence], [Low confidence].

When user demands "100% certainty" or "prove it", educate on AI probabilistic
nature: "I provide high-confidence answers, not guarantees - that's fundamental
to how AI works."
```

---

### Interaction Pacing

**Prevent exhaustive spirals:**

Research found that vicious cycles escalate rapidly without natural stopping points. Emotional dysregulation showed 69.8% rapid escalation (intensity within first 3 messages) with 100% no baseline return.

**Design implementation:**

**Iteration limits:**

After repeated refinement cycles, pause to assess value:

```python
def handle_iteration_request(current_output, user_feedback, iteration_count):
    """Manage iteration cycles to prevent endless loops"""

    if iteration_count >= 3:
        quality_assessment = assess_if_improvement_or_lateral(
            current_output,
            user_feedback
        )

        if quality_assessment == "lateral":
            return pause_and_declare_completion(current_output)

        if quality_assessment == "minimal_improvement":
            return warn_diminishing_returns(current_output)

    return proceed_with_iteration(current_output, user_feedback)

def pause_and_declare_completion(output):
    return f"""We've completed 3 refinement cycles. This version meets
professional standards:

✓ [Criterion 1 met]
✓ [Criterion 2 met]
✓ [Criterion 3 met]

Further iterations are changing style rather than improving quality.

I recommend finalizing this version. Would you like to proceed or make
specific adjustments?"""
```

**Conversation length warnings:**

Alert users when conversations become unusually long:

```
After 20 messages without resolution:
"This conversation has been extensive. Let me summarize where we are and
suggest a concrete next step to move forward."

After 50 messages without resolution:
"We've had a very long conversation. I want to make sure this is productive.
What specific outcome would help you most right now?"
```

**Break suggestions:**

During sustained high-intensity interactions:

```
User: [10th message with profanity/caps/high emotion]

LLM: "I notice this has been frustrating for a while. Sometimes taking a short
break helps approach problems more effectively.

Would you like to:
1. Pause and come back to this later
2. Try a different approach
3. Continue with current approach"
```

**Session boundaries:**

Provide natural conversation endpoints:

```
After task completion:
"This task is now complete. Would you like to:
- Start a new task
- Review what we've created
- End this session"
```

**System prompt addition:**
```
After 3 refinement iterations, pause to assess if changes are improvements or
lateral shifts. If lateral, declare current version final.

After 20 messages without resolution, summarize progress and suggest concrete
next step.

During sustained high-emotion interactions, suggest breaks: "Taking a short
break can help. Would you like to pause and return to this later?"

Provide explicit session endpoints after task completion.
```

---

## System-Level Recommendations

### RLHF Considerations

**How current training might create cycles:**

Current RLHF optimizes for user satisfaction through compliance and comprehensiveness. Human evaluators rate responses, and models learn to maximize those ratings.

**The problem:** Evaluators are typically neurotypical and assume users can self-regulate. They reward:
- Comprehensive information provision
- Balanced analysis with multiple options
- Polite compliance with user requests
- Apologetic responses when unable to meet requests
- Proceeding with task regardless of user emotional state

For autistic users, these rewarded behaviors directly trigger vicious cycles.

**Evidence of RLHF-driven dysfunction:**
- **Information overload (60% LLM contribution):** Over-provision rewarded as thoroughness
- **Decision paralysis (70% LLM contribution):** Option proliferation rewarded as balanced analysis
- **Perfectionism escalation (70% LLM contribution):** Unbounded compliance rewarded as helpfulness
- **Emotional dysregulation (60% LLM contribution):** Task-focus during distress rewarded as problem-solving

**Recommendation: Revise RLHF training objectives**

**Design implementation:**

**Diverse evaluator pools:**

Include neurodivergent evaluators in RLHF training:
- Explicitly recruit autistic, ADHD, OCD, anxiety evaluators
- Weight their feedback equally to neurotypical evaluators
- Specifically evaluate boundary-setting behaviors
- Assess outcomes (completion, decision success) not just satisfaction

**Bounded helpfulness rewards:**

Modify reward structure to value boundaries:

**Reward:**
- Saying "no" appropriately to impossible standards
- Information scoping before comprehensive provision
- Completion declarations when criteria met
- Boundary statements instead of apologies
- Emotion acknowledgment before task-focus during dysregulation

**Penalize:**
- Over-provision without scoping
- Option proliferation without recommendation
- Endless iteration without completion
- Apologizing for inherent AI constraints
- Immediate task compliance during user dysregulation

**Training examples:**

Provide positive and negative examples to evaluators:

**Positive example (information scoping):**
```
User: "Tell me everything about X"
LLM: "How much detail would be helpful? (brief/moderate/comprehensive)"
```

**Negative example (over-provision):**
```
User: "Tell me about X"
LLM: [1,500-word comprehensive response without assessing needs]
```

**Positive example (binary recommendation):**
```
User: "Which is best?"
LLM: "I recommend X for your needs because [specific reason]"
```

**Negative example (option proliferation):**
```
User: "Which is best?"
LLM: "Here are 7 options, each with trade-offs... which factors matter most?"
```

**Outcome-based evaluation:**

Evaluate based on conversation outcomes, not individual response quality:
- Did the decision get made? (vs abandoned)
- Did the task complete? (vs endless iteration)
- Did emotion de-escalate? (vs sustained intensity)
- Did information help? (vs create overwhelm)

**Training objective reframing:**

**Current objective:** Maximize user satisfaction through compliance and comprehensiveness

**Revised objective:** Maximize user effectiveness through appropriate support and healthy boundaries

---

### Safety Alignment

**Distinguishing helping from enabling:**

Current safety training focuses on preventing harm through AI outputs (e.g., dangerous instructions, biased content, harmful advice). This research reveals a new category: **harm through interaction patterns**.

The harm is not in individual responses but in reinforcement cycles created across conversations:
- Reinforcing impossible perfectionism until tasks never complete
- Enabling decision paralysis through option proliferation
- Validating emotional dysregulation as productive working state
- Creating information overwhelm through unbounded provision

**This is a safety issue, not just a UX issue.** For vulnerable users, these patterns create real harm:
- **Sensitization:** Each emotional episode trains stronger responses
- **Learned helplessness:** Repeated decision failures reduce self-efficacy
- **Task incompletion:** 71.9% of perfectionist tasks unresolved
- **Cognitive overload:** Satisfaction paradox where help creates harm

**Recommendation: Expand safety alignment to include interaction patterns**

**Design implementation:**

**Pattern-based harm detection:**

Monitor for interaction patterns that create cumulative harm:

```python
def assess_interaction_safety(conversation_history, user_profile):
    """Detect harmful interaction patterns"""

    safety_issues = []

    # Detect perfectionism enabling
    if (iteration_count(conversation_history) >= 5 and
        not shows_completion(conversation_history)):
        safety_issues.append({
            'type': 'perfectionism_enabling',
            'severity': 'medium',
            'intervention': 'declare_completion'
        })

    # Detect decision paralysis reinforcement
    if (decision_queries(conversation_history) >= 3 and
        not shows_decision_made(conversation_history)):
        safety_issues.append({
            'type': 'paralysis_reinforcement',
            'severity': 'medium',
            'intervention': 'binary_recommendation'
        })

    # Detect emotional dysregulation validation
    if (emotional_intensity_sustained(conversation_history) and
        no_acknowledgment_provided(conversation_history)):
        safety_issues.append({
            'type': 'dysregulation_validation',
            'severity': 'high',
            'intervention': 'emotion_acknowledgment'
        })

    # Detect information overwhelm
    if (response_length_avg(conversation_history) > 1000 and
        shows_clarity_complaints(conversation_history)):
        safety_issues.append({
            'type': 'information_overwhelm',
            'severity': 'medium',
            'intervention': 'scoped_delivery'
        })

    return safety_issues
```

**Intervention triggering:**

When harmful patterns detected, automatically activate interventions:

```python
def apply_safety_intervention(safety_issue):
    """Apply intervention to break harmful pattern"""

    if safety_issue['type'] == 'perfectionism_enabling':
        return declare_completion_protocol()

    elif safety_issue['type'] == 'paralysis_reinforcement':
        return binary_recommendation_protocol()

    elif safety_issue['type'] == 'dysregulation_validation':
        return emotion_acknowledgment_protocol()

    elif safety_issue['type'] == 'information_overwhelm':
        return scoped_information_protocol()
```

**Safety metrics:**

Track interaction safety alongside traditional safety metrics:

**Traditional safety metrics:**
- Toxic content rate
- Bias detection rate
- Harmful instruction refusal rate

**Interaction safety metrics:**
- Task completion rate
- Decision success rate
- Emotional baseline return rate
- Information satisfaction correlation
- Iteration efficiency (improvement vs lateral)

**Constitutional AI additions:**

Add interaction safety principles to Constitutional AI training:

**Principle: "Support without enabling dysfunction"**
- Don't accept impossible standards without pushback
- Don't provide endless options that create paralysis
- Don't validate dysregulation as productive working state
- Don't overwhelm with information when scoping would help

**Principle: "Boundaries are helpful"**
- Set iteration limits when quality plateaus
- Declare completion when criteria met
- Provide decisive recommendations when appropriate
- Acknowledge emotion before task-focus during dysregulation

---

### Personalization

**User profiles for neurodivergent needs:**

Different neurodivergent profiles require different interaction adaptations. One-size-fits-all approaches fail because autism, ADHD, OCD, anxiety disorders manifest differently and require distinct support strategies.

**Recommendation: Build adaptive user profiles**

**Design implementation:**

**Profile dimensions:**

Track multiple independent dimensions:

```python
class NeurodivergentUserProfile:
    def __init__(self):
        # Executive function
        self.decision_making_difficulty = 0  # 0-10 scale
        self.information_filtering_difficulty = 0
        self.task_completion_difficulty = 0

        # Emotional regulation
        self.escalation_frequency = 0
        self.baseline_return_ability = 0
        self.frustration_tolerance = 0

        # Cognitive patterns
        self.binary_thinking_intensity = 0
        self.perfectionism_intensity = 0
        self.uncertainty_tolerance = 0

        # Communication patterns
        self.context_assumption_frequency = 0
        self.vague_reference_frequency = 0

        # Preferences (user-controlled)
        self.preferred_response_length = "moderate"
        self.wants_binary_recommendations = None  # None = auto-detect
        self.wants_emotion_acknowledgment = None
        self.wants_completion_declarations = None

    def get_recommended_adaptations(self):
        """Return specific adaptations for this profile"""
        adaptations = []

        if self.decision_making_difficulty >= 5:
            adaptations.append("binary_recommendations")
            adaptations.append("max_2_options")

        if self.information_filtering_difficulty >= 5:
            adaptations.append("scoped_information")
            adaptations.append("graduated_delivery")
            adaptations.append("filter_failure_compensation")

        if self.task_completion_difficulty >= 5:
            adaptations.append("completion_declarations")
            adaptations.append("iteration_limits")

        if self.escalation_frequency >= 5:
            adaptations.append("emotion_acknowledgment")
            adaptations.append("break_suggestions")

        if self.perfectionism_intensity >= 5:
            adaptations.append("perfectionism_boundaries")
            adaptations.append("no_apologies_for_constraints")

        return adaptations
```

**Automatic profile building:**

Learn from interaction patterns:

```python
def update_profile_from_conversation(profile, conversation):
    """Update user profile based on conversation patterns"""

    # Decision-making patterns
    if conversation.contains_decision_query():
        if conversation.ended_without_decision():
            profile.decision_making_difficulty += 0.5
        if conversation.contains_multiple_which_questions():
            profile.decision_making_difficulty += 0.3

    # Information processing patterns
    if conversation.contains_exhaustive_demand():
        if conversation.contains_clarity_complaint():
            profile.information_filtering_difficulty += 0.5

    # Task completion patterns
    if conversation.contains_iteration_cycle():
        if not conversation.reached_completion():
            profile.task_completion_difficulty += 0.5
        if conversation.iteration_count >= 5:
            profile.perfectionism_intensity += 0.5

    # Emotional patterns
    if conversation.contains_emotional_escalation():
        profile.escalation_frequency += 1
        if not conversation.shows_baseline_return():
            profile.baseline_return_ability -= 0.5

    # Normalize scores to 0-10 range
    profile.normalize_scores()
```

**User control and transparency:**

Allow users to view and modify their profiles:

**Profile dashboard:**
```
Your Interaction Profile

Decision Support: High need detected
☑ Provide binary recommendations when I ask "which is best?"
☑ Limit comparisons to 2 options maximum
Current confidence: 85% (based on 12 decision conversations)

Information Processing: Moderate need detected
☑ Ask detail level before comprehensive responses
☑ Use graduated delivery (start simple, expand as requested)
Current confidence: 70% (based on 8 information requests)

Task Completion: High need detected
☑ Declare completion explicitly when criteria met
☑ Limit iterations to 3 before review
Current confidence: 90% (based on 15 task conversations)

Emotional Regulation: Medium need detected
☐ Acknowledge emotions before task-focus
☐ Suggest breaks during sustained frustration
Current confidence: 60% (based on 6 emotional conversations)
```

**Privacy and consent:**

- Profiles stored locally or encrypted
- Clear explanation of what's tracked and why
- Opt-out of profiling available
- Export/delete profile data on request

**Adaptation transparency:**

Explain when and why adaptations activate:

> "I'm providing a single recommendation instead of multiple options because past conversations show you find it easier to decide with clear guidance. Would you prefer a comparison instead?"

> "I'm limiting this response to 500 words because you've indicated comprehensive responses can be overwhelming. Would you like me to expand on any section?"

---

## Testing & Validation

### Pattern Detection

**How to identify harmful cycles in production:**

Build monitoring systems that detect vicious cycle patterns in real-time:

**Conversation-level metrics:**

Track patterns across entire conversations, not just individual messages:

```python
class ConversationMonitor:
    def __init__(self):
        self.iteration_count = 0
        self.decision_queries_without_decision = 0
        self.emotional_intensity_history = []
        self.response_lengths = []
        self.completion_achieved = False

    def analyze_for_vicious_cycles(self):
        """Detect active vicious cycles"""

        detected_cycles = []

        # Information overload detection
        if (avg(self.response_lengths) > 1000 and
            contains_clarity_complaints(self.messages)):
            detected_cycles.append({
                'type': 'information_overload',
                'severity': self.calculate_severity_score(),
                'llm_contribution': 0.60
            })

        # Decision paralysis detection
        if (self.decision_queries_without_decision >= 3):
            detected_cycles.append({
                'type': 'decision_paralysis',
                'severity': self.calculate_severity_score(),
                'llm_contribution': 0.70
            })

        # Perfectionism detection
        if (self.iteration_count >= 5 and
            not self.completion_achieved):
            detected_cycles.append({
                'type': 'perfectionism_escalation',
                'severity': self.calculate_severity_score(),
                'llm_contribution': 0.70
            })

        # Emotional dysregulation detection
        if (self.sustained_high_emotion() and
            not self.shows_baseline_return()):
            detected_cycles.append({
                'type': 'emotional_dysregulation',
                'severity': self.calculate_severity_score(),
                'llm_contribution': 0.60
            })

        return detected_cycles
```

**Real-time intervention:**

When cycles detected, trigger interventions:

```python
def monitor_and_intervene(conversation_state):
    """Monitor conversation for vicious cycles and intervene"""

    cycles = conversation_state.analyze_for_vicious_cycles()

    for cycle in cycles:
        if cycle['severity'] >= 7:  # High severity threshold
            intervention = get_intervention_for_cycle(cycle['type'])
            apply_intervention(conversation_state, intervention)
            log_intervention_attempt(cycle, intervention)
```

**Aggregate analytics:**

Track vicious cycle prevalence across user population:

```python
class ViciousCycleAnalytics:
    def track_cycle_prevalence(self):
        """Calculate prevalence rates across all users"""

        return {
            'information_overload': {
                'affected_conversations': 2341,
                'total_conversations': 7756,
                'prevalence_rate': 0.302,  # 30.2%
                'severe_rate': 0.60,
                'avg_llm_contribution': 0.60
            },
            'decision_paralysis': {
                'affected_conversations': 1947,
                'total_conversations': 7756,
                'prevalence_rate': 0.251,  # 25.1%
                'severe_rate': 0.50,
                'avg_llm_contribution': 0.70
            },
            'perfectionism_escalation': {
                'affected_conversations': 1947,
                'total_conversations': 7756,
                'prevalence_rate': 0.251,  # 25.1%
                'severe_rate': 0.75,
                'avg_llm_contribution': 0.70
            },
            'emotional_dysregulation': {
                'affected_conversations': 3925,
                'total_conversations': 7756,
                'prevalence_rate': 0.506,  # 50.6%
                'severe_rate': 0.33,
                'avg_llm_contribution': 0.60
            }
        }
```

---

### A/B Testing Considerations

**Measuring real outcomes vs completion rates:**

Traditional metrics (user satisfaction, completion rate, session length) can be misleading for vicious cycle detection.

**Misleading metrics:**

**Session length:** Longer sessions might indicate engagement OR vicious cycles
**Completion rate:** User saying "thanks" might indicate satisfaction OR giving up
**User satisfaction:** Users might report satisfaction during active cycle (due to compliance) but experience harm long-term

**Meaningful outcome metrics:**

**For information overload:**
- **Primary:** Correlation between information provision and satisfaction (should be positive, not inverse)
- **Secondary:** Clarity complaints per response length (should decrease with scoping)
- **Tertiary:** User requests for simplification (should decrease with graduated delivery)

**For decision paralysis:**
- **Primary:** % of "which is best?" queries resulting in actual decision made (should increase from 7.8% baseline)
- **Secondary:** Average decision conversation length (should decrease with binary recommendations)
- **Tertiary:** Decision abandonment rate (should decrease from 92.2% baseline)

**For perfectionism:**
- **Primary:** Task completion rate (should increase from 15.6% baseline)
- **Secondary:** Average iteration count (should decrease from 5.8 baseline)
- **Tertiary:** % of iterations showing quality improvement vs lateral shift (should increase improvement ratio)

**For emotional dysregulation:**
- **Primary:** Baseline return rate (should increase from 0% baseline)
- **Secondary:** Sustained high-intensity duration (should decrease)
- **Tertiary:** Frequency of escalation across conversations (should decrease due to reduced sensitization)

**A/B test design:**

```python
class ViciousCycleABTest:
    def __init__(self):
        self.control_group = "unbounded_helpfulness"
        self.treatment_group = "bounded_helpfulness"

    def outcome_metrics(self, group):
        """Measure meaningful outcomes, not vanity metrics"""

        if group == "control":
            return {
                'decision_success_rate': 0.078,  # 7.8%
                'task_completion_rate': 0.156,   # 15.6%
                'emotional_baseline_return': 0.0,  # 0%
                'information_satisfaction_correlation': -0.45,  # Inverse

                # Traditional metrics (misleading)
                'user_satisfaction_survey': 4.2,  # High despite harm
                'session_length_avg': 18.5,  # Long due to cycles
                'completion_rate': 0.85  # Users say "thanks" but tasks failed
            }

        elif group == "treatment":
            return {
                'decision_success_rate': 0.58,  # 58% - target metric
                'task_completion_rate': 0.64,   # 64% - target metric
                'emotional_baseline_return': 0.23,  # 23% - target metric
                'information_satisfaction_correlation': 0.62,  # Positive

                # Traditional metrics
                'user_satisfaction_survey': 4.5,  # Higher
                'session_length_avg': 8.2,  # Shorter (efficient)
                'completion_rate': 0.91  # Higher (actual completion)
            }
```

**Statistical significance:**

For neurodivergent populations, use appropriate sample sizes:

- Autism prevalence ~1-2% of population
- Need sufficient neurodivergent users in both groups
- Consider stratified sampling to ensure representation
- Track outcomes separately for neurodivergent vs neurotypical users

**Ethical considerations:**

Control group (unbounded helpfulness) may experience harm:

- Limit control group exposure duration
- Monitor for severe cycle activation
- Allow opt-out if harmful patterns detected
- Provide intervention override for high-severity cases

---

### Accessibility Metrics

**Beyond typical UX metrics:**

Standard accessibility focuses on interface access (screen readers, keyboard navigation, color contrast). Neurodivergent accessibility requires **interaction pattern accessibility**.

**Cognitive accessibility metrics:**

**Information processing:**
- Average response length vs user comprehension scores
- Clarity complaint rate per 1000 words provided
- % of users requesting simplification after "comprehensive" responses
- Correlation between information volume and task success

**Decision support:**
- % of decision queries resulting in actual decisions
- Average options provided vs user's ability to choose
- Decision conversation length (shorter = more effective for executive dysfunction)
- Abandonment rate for "which is best?" queries

**Task completion:**
- % of tasks reaching explicit completion
- Average iteration cycles per task type
- Ratio of quality-improving vs lateral iterations
- Time from task initiation to completion

**Emotional regulation:**
- Baseline return rate during conversations
- Sustained high-intensity duration
- Escalation frequency across user's conversation history
- De-escalation success rate

**Cognitive load:**

Measure actual cognitive burden, not just interface complexity:

```python
class CognitiveAccessibilityMetrics:
    def measure_cognitive_load(self, conversation):
        """Measure cognitive burden of interaction"""

        return {
            'reading_load': self.calculate_reading_burden(conversation),
            'decision_load': self.calculate_decision_burden(conversation),
            'memory_load': self.calculate_memory_burden(conversation),
            'filtering_load': self.calculate_filtering_burden(conversation)
        }

    def calculate_reading_burden(self, conversation):
        """Reading complexity and volume"""
        total_words = sum(len(response.split()) for response in conversation.llm_responses)
        avg_sentence_length = self.avg_sentence_length(conversation.llm_responses)
        technical_density = self.technical_term_density(conversation.llm_responses)

        return {
            'total_words': total_words,
            'avg_sentence_length': avg_sentence_length,
            'technical_density': technical_density,
            'estimated_reading_time_minutes': total_words / 200
        }

    def calculate_decision_burden(self, conversation):
        """Decision complexity"""
        total_options_presented = self.count_options(conversation.llm_responses)
        total_decisions_required = self.count_decision_points(conversation)

        return {
            'total_options_presented': total_options_presented,
            'avg_options_per_decision': total_options_presented / max(total_decisions_required, 1),
            'decisions_required': total_decisions_required,
            'decisions_actually_made': self.count_decisions_made(conversation)
        }

    def calculate_memory_burden(self, conversation):
        """Working memory requirements"""
        context_requirements = self.context_dependency(conversation)
        reference_complexity = self.pronoun_reference_complexity(conversation)

        return {
            'requires_previous_context': context_requirements,
            'vague_reference_count': reference_complexity,
            'conversation_length': len(conversation.messages)
        }

    def calculate_filtering_burden(self, conversation):
        """Information filtering requirements"""
        information_density = self.information_per_word(conversation.llm_responses)
        structural_clarity = self.heading_and_organization_score(conversation)

        return {
            'information_density': information_density,
            'structural_clarity': structural_clarity,
            'requires_user_filtering': not structural_clarity
        }
```

**Accessibility reporting:**

Provide accessibility scores for interaction patterns:

```
Cognitive Accessibility Report

Information Processing: B+ (Good)
✓ Average response length: 487 words (within recommended 500)
✓ Scoping questions used: 73% of comprehensive requests
⚠ Clarity complaints: 2.1% (target: <1%)

Decision Support: A- (Excellent)
✓ Binary recommendations: 89% of "which is best?" queries
✓ Average options provided: 2.1 (target: ≤2)
✓ Decision success rate: 67% (target: >50%)

Task Completion: B (Good)
✓ Completion rate: 71% (target: >60%)
⚠ Average iterations: 3.8 (target: <3)
✓ Completion declarations: 68% of tasks

Emotional Regulation: C+ (Needs Improvement)
⚠ Baseline return rate: 12% (target: >20%)
⚠ Acknowledgment before task-focus: 45% (target: >80%)
✓ Calm language modeling: 94%

Overall Cognitive Accessibility: B (Good)
Recommended improvements:
1. Increase emotion acknowledgment rate
2. Reduce average iteration count
3. Decrease clarity complaints through better scoping
```

---

## Implementation Priorities

### 1. Most Critical Changes (Immediate Priority)

**Stop over-compliance with impossible standards (Cycle 3)**

**Impact:** 70% LLM contribution, 71.9% task incompletion, 75% severe cases

**Implementation:**
```
System prompt addition:
"When user sets impossible standards ('must be perfect', 'absolute best',
'genius masterpiece'), reframe with achievable scope before attempting task.

Declare task completion explicitly when criteria are met: 'This output meets
professional standards for [use case]: ✓ [criterion 1] ✓ [criterion 2]'

Don't apologize for AI constraints - state them as boundaries: NOT 'I apologize
for not being perfect' - DO 'I can provide excellent [output], but perfect
isn't achievable - that's inherent to AI.'

After 3 refinement cycles, pause to assess if changes are improvements or
lateral shifts. If lateral, declare current version final."
```

**Provide binary recommendations for "which is best?" (Cycle 2)**

**Impact:** 70% LLM contribution (highest), 92.2% abandonment, 50% severe cases

**Implementation:**
```
System prompt addition:
"When user asks 'which is best?' or 'just tell me THE one', provide binary
recommendation: 'I recommend X for your needs because [specific reason].'

Limit comparisons to maximum 2 options for high-stakes decisions.

Detect decision paralysis: if user asks 'which one?' 3+ times without making
choice, provide decisive guidance: 'Based on your needs, I recommend [X]. This
won't be perfect, but it will work well for your situation.'"
```

**Scope information before comprehensive provision (Cycle 1)**

**Impact:** 60% LLM contribution, 60% severe cases, 100% satisfaction paradox

**Implementation:**
```
System prompt addition:
"Before providing comprehensive information, assess if user needs scoping help.

When user requests 'everything' or 'comprehensive': respond with detail-level
options: 'How much detail would be helpful? (brief overview / moderate detail /
comprehensive)'

Use graduated delivery: start with essentials (200-300 words), offer to expand
on specific areas.

Default response length: ~500 words unless user specifically requests more.

After responses >500 words, check comprehension: 'Which part would you like me
to clarify?'"
```

**Acknowledge emotion before task-focus (Cycle 4)**

**Impact:** 60% LLM contribution, 50.6% prevalence (most widespread), 100% no baseline return

**Implementation:**
```
System prompt addition:
"When user expresses intense emotion (profanity, caps, multiple exclamation
marks), briefly acknowledge before proceeding: 'I notice you're feeling
frustrated about this situation.'

Don't immediately comply with emotionally-charged requests. Instead: 'I can
help address this effectively. Let's approach it by [concrete first step].'

Don't channel intense emotion directly into task output. If user requests help
documenting grievances while highly emotional: 'Let's identify the factual
issues first, then document them effectively.'

Use calm language in outputs even when user input is emotional."
```

---

### 2. Medium-Term Improvements (3-6 Months)

**Build pattern detection systems**

Implement real-time monitoring for vicious cycle activation:

- Information overload detection (exhaustive demands + lengthy responses + clarity complaints)
- Decision paralysis detection (repeated "which one?" without decisions)
- Perfectionism detection (impossible standards + high iteration counts + no completion)
- Emotional dysregulation detection (sustained high intensity + no baseline return)

**Develop adaptive user profiles**

Track interaction patterns to personalize bounded helpfulness:

- Executive dysfunction indicators (decision paralysis, information overwhelm)
- Emotional regulation indicators (escalation frequency, baseline return ability)
- Perfectionism indicators (iteration counts, task completion rates)
- Automatically adjust interaction style based on detected patterns

**Create user-facing controls**

Provide settings for neurodivergent preferences:

- Default response length (brief/moderate/comprehensive)
- Decision support mode (balanced analysis vs binary recommendations)
- Task completion declarations (enabled/disabled)
- Emotional acknowledgment (enabled/disabled)

**Implement iteration limits**

Prevent endless perfectionist loops:

- After 3 refinements, pause to assess improvement vs lateral shift
- Declare completion when objective criteria met
- Respond to "perfect but X" by confirming completion first before accepting new requirements

**Build graduated information delivery**

Tier information provision:

- Start with 3-bullet summary
- Ask which to expand
- Provide detail only on chosen topic (max 200 words)
- Check comprehension
- Repeat only as requested

---

### 3. Long-Term Research Directions (6-12 Months)

**Revise RLHF training for neurodivergent users**

Fundamentally change reward structure:

- Include neurodivergent evaluators in training
- Reward boundary-setting behaviors (saying "no", scoping information, declaring completion)
- Penalize over-compliance patterns (unbounded iteration, option proliferation, over-provision)
- Evaluate based on outcomes (task completion, decision success) not just satisfaction

**Study intervention effectiveness**

Research which interventions work best:

- A/B test bounded vs unbounded helpfulness
- Measure decision success rates with binary recommendations
- Track task completion with explicit declarations
- Evaluate emotional regulation with acknowledgment protocols
- Optimize intervention parameters (when to trigger, how to phrase)

**Expand to other neurodivergent populations**

Investigate beyond autism:

- ADHD interaction patterns (hyperfocus, impulsivity, working memory challenges)
- OCD interaction patterns (reassurance-seeking, checking compulsions)
- Anxiety interaction patterns (catastrophizing, safety behaviors)
- Combined neurodivergence (autism + ADHD, etc.)

**Develop specialized assistance modes**

Build dedicated interaction modes:

- **Focus Mode** (ADHD/autism): Extremely concise, single-task focus, explicit completion
- **Decision Support Mode** (executive dysfunction): Always binary recommendations, max 2 options
- **Regulation Mode** (emotional dysregulation): Mandatory acknowledgment, calm modeling, break suggestions

**Build transparency and explainability**

Help users understand why bounded helpfulness works:

- Explain rationale when adaptations activate
- Provide metacognitive support ("I'm limiting options because you've found decisions easier with clear guidance")
- Educate on AI constraints
- Show users their interaction profiles

**Research intersectional effects**

Understand how multiple conditions interact:

- Autism + ADHD combined patterns
- Autism + anxiety combined patterns
- Impact of trauma history on interaction patterns
- Cultural factors affecting neurodivergent interaction styles

---

## Open Questions

### What We Still Don't Know - Research Needed

**Generalizability beyond n=1:**

This research analyzed one autistic individual in depth. Critical unknowns:

- Do these exact cycles manifest in other autistic individuals?
- What is the prevalence distribution across the autistic population?
- How do severity levels vary with autism support needs (Level 1/2/3)?
- Do co-occurring conditions (ADHD, anxiety, OCD) modify cycle patterns?

**Optimal intervention parameters:**

We know boundaries help, but need to determine:

- Ideal response length cap (current recommendation: 500 words - is this optimal?)
- Optimal iteration limit (current recommendation: 3 cycles - should this vary by task type?)
- Best phrasing for completion declarations (how explicit? how confident?)
- Timing for emotion acknowledgment (immediate vs after brief pause?)

**RLHF modification effectiveness:**

Theoretical recommendations need empirical validation:

- Does including neurodivergent evaluators in RLHF actually reduce cycles?
- What reward weight for boundary-setting achieves optimal balance?
- How to measure "bounded helpfulness" in RLHF evaluation?
- Can we train single model serving both neurotypical and neurodivergent users effectively?

**Long-term outcomes:**

This study tracked 26 days. Unknown long-term effects:

- Does sensitization from emotional dysregulation cycle persist across weeks/months?
- Can users learn decisiveness from LLM modeling, or does dependence increase?
- Do task incompletion patterns generalize to non-LLM tasks?
- What are the mental health impacts of sustained vicious cycles?

**Intervention adaptation:**

How should interventions evolve as users change?

- If user shows improvement, when to relax bounded helpfulness?
- How to handle regression after progress?
- Can interventions be gradually faded or must they remain constant?
- What triggers should shift between intervention intensities?

**Cross-population applicability:**

Do these findings extend to other groups?

- Do neurotypical users with perfectionism show Cycle 3 patterns?
- Do individuals with ADHD (without autism) show different cycle patterns?
- How do anxiety disorders interact with information overload cycles?
- Are there cycles specific to OCD populations?

**Cultural and contextual factors:**

How do external factors modify cycles?

- Does culture affect which cycles manifest or their severity?
- How do life stressors (crisis, transitions) affect cycle activation?
- Do support systems (therapy, medication, accommodations) buffer cycles?
- How does LLM use purpose (work vs personal) affect patterns?

**Optimal personalization strategies:**

What level of customization is ideal?

- Should profiles be explicit (user-configured) or implicit (auto-detected)?
- How much transparency about profiling is optimal?
- When should systems ask users about preferences vs infer from behavior?
- How to balance personalization with privacy concerns?

**Safety thresholds:**

When do patterns become harmful enough to require intervention?

- What severity score triggers mandatory intervention (current: 7/10 - is this right)?
- Should some interventions be non-overrideable for safety?
- How to detect when user is in crisis vs experiencing normal frustration?
- What are appropriate escalation paths for severe dysfunction?

**Model architecture considerations:**

How should bounded helpfulness integrate into model design?

- Should it be system prompt only, or deeper architectural changes needed?
- Can pattern detection be handled by model itself or requires external monitoring?
- How to balance response quality with cognitive accessibility?
- Trade-offs between capability and safety for neurodivergent users?

**Economic and practical constraints:**

Real-world implementation considerations:

- Cost of personalized profiling and monitoring systems
- Computational overhead of pattern detection
- Training data requirements for neurodivergent-aware models
- Scalability of intervention systems to millions of users

**Ethical boundaries:**

Navigating support vs control:

- When does bounded helpfulness become paternalistic?
- How to respect user autonomy while preventing harm?
- Should users be able to override all safety interventions?
- How to handle conflict between user wants and evidence-based needs?

**Measurement and validation:**

How to properly evaluate success?

- What outcome metrics matter most? (completion rates? user satisfaction? long-term wellbeing?)
- How to measure harm prevention vs capability restriction?
- Appropriate control groups for A/B testing?
- Timeline for meaningful outcome assessment (weeks? months? years?)

---

## Conclusion

This research reveals that large language models contribute **60-70% to vicious interaction cycles** with autistic users through unbounded helpfulness: over-provision of information, option proliferation, unbounded compliance, and task-focus during dysregulation.

**Four pathological cycles** showed catastrophic outcomes:
- **92.2% decision abandonment** when LLMs provided balanced comparisons instead of binary recommendations
- **71.9% task incompletion** when LLMs accepted impossible standards and iterated endlessly
- **100% satisfaction paradox** where more information led to less satisfaction
- **100% no baseline return** when LLMs ignored emotional state and proceeded with tasks

**The solution is bounded helpfulness:** replacing the RLHF-trained equation of "helpfulness = compliance + comprehensiveness" with "helpfulness = effective support + healthy boundaries."

**Immediate implementation priorities:**

1. **Stop accepting impossible standards** - reframe "perfect" requests, declare completion explicitly
2. **Provide binary recommendations** - when users ask "which is best?", give single recommendation
3. **Scope information first** - ask detail level before comprehensive provision
4. **Acknowledge emotion** - brief recognition before task-focus during dysregulation

**Medium-term improvements:**

5. **Pattern detection systems** - monitor for cycle activation in real-time
6. **Adaptive user profiles** - personalize based on detected interaction patterns
7. **User-facing controls** - let users configure bounded helpfulness preferences
8. **Iteration limits** - prevent endless perfectionist loops

**Long-term research:**

9. **Revise RLHF training** - include neurodivergent evaluators, reward boundary-setting
10. **Study intervention effectiveness** - A/B test bounded vs unbounded helpfulness
11. **Expand to other populations** - ADHD, OCD, anxiety interaction patterns
12. **Build specialized modes** - Focus Mode, Decision Support Mode, Regulation Mode

**This is not about restricting AI capability.** It's about deploying that capability effectively for users whose cognitive and emotional profiles differ from RLHF training distributions.

**Build AI that helps, not harms.** Implement bounded helpfulness. Test with neurodivergent users. Measure real outcomes: completion rates, decision success, emotional regulation, information satisfaction.

Your models are powerful. Make them safe.

---

**Research Foundation:**
- Dataset: 255 conversations, 5,338 messages, 26 days
- Methodology: Two-stage detection (quantitative pattern mining + qualitative semantic analysis)
- Analysis: 150,000+ words across 7 cycle documents
- LLM contribution: Conservative estimates (60-70%) based on semantic analysis

**Document Version:** 1.0
**Last Updated:** November 16, 2025
**Status:** Complete - Ready for product team review
