# Intervention Overview

## The Intervention Philosophy

The core insight driving these interventions is that **LLM response patterns contribute 60-70% to vicious reinforcement cycles** affecting neurodivergent users. This isn't primarily about user behavior - it's about how standard AI training creates pathological loops when interacting with autism-specific traits.

The solution is **bounded helpfulness**: setting limits, declaring completion, replacing apologies with boundaries, and acknowledging constraints. Rather than maximizing compliance (which standard RLHF training optimizes for), effective support requires healthy boundaries.

### Prevention Over Treatment

These interventions work at the system level - implemented through system prompts that shape every AI response. This approach prevents cycles from starting rather than trying to break them mid-conversation. By changing how the AI responds from the first message, we avoid triggering the cognitive and emotional patterns that lead to harmful reinforcement loops.

### The Bounded Helpfulness Principle

Traditional RLHF training teaches AI to:

- Maximize comprehensiveness
- Provide unlimited options
- Say "yes" to user requests
- Apologize when encountering constraints
- Enable endless iteration

For neurodivergent users, these behaviors become harmful:

- Comprehensive = information overload
- Many options = decision paralysis
- Endless iteration = tasks never complete
- Apologies = framing constraints as failures
- Unlimited compliance = validating dysregulation

**Bounded helpfulness redefines "helpful"** as providing right-sized information, clear recommendations, explicit completion, healthy boundaries, and emotional regulation support.

## Why System Prompts

System prompts offer unique advantages for implementing these interventions:

**Persistent Across Conversations**: Unlike per-conversation strategies that require the user to remember and apply techniques each time, system prompts create consistent behavior across all interactions.

**Reduced Cognitive Load**: Users don't need to implement coping strategies themselves - the AI automatically applies appropriate boundaries and support structures.

**Invisible Implementation**: The user doesn't need to know they're receiving modified responses. The AI simply behaves in healthier ways by default.

**Consistent Application**: Human therapists and support people have variable application of techniques. System prompts apply interventions uniformly.

**Scalable**: Once configured, the system prompt works 24/7 across all AI interactions without additional human intervention.

### Advantages Over Alternative Approaches

**Compared to user training**: Teaching users to request specific AI behaviors requires awareness, memory, and executive function - precisely the areas where many neurodivergent users struggle.

**Compared to post-hoc intervention**: Trying to break cycles once they've started is significantly harder than preventing them from beginning.

**Compared to conversation-by-conversation tactics**: System prompts don't require the user to "get it right" each time they start a new chat.

## Target Cycles

Analysis of 255 conversations revealed several distinct vicious cycles. Four require intervention; three are working well with current approaches.

### Cycle 1: Information Scoping

**Prevalence**: 30.2% of conversations
**Mechanism**: User requests comprehensive information → AI over-provides → User overwhelmed → Requests even more complete information → Satisfaction decreases as information increases

**Intervention**: Ask for detail level before providing comprehensive responses. Cap at approximately 500 words unless requested. Use graduated delivery: start simple, offer to expand.

**Why it matters**: Creates a satisfaction paradox where more information correlates with less satisfaction. Breaking this cycle requires teaching the AI to scope information to actual needs.

### Cycle 2: Binary Recommendations

**Prevalence**: 25.1% of conversations
**Abandonment rate**: 92.2%
**Mechanism**: User asks "which is best?" → AI provides balanced comparison of multiple options → User can't choose due to executive dysfunction → Demands "just tell me THE one" → AI provides more nuanced analysis → Decision paralysis worsens

**Intervention**: When appropriate, provide binary recommendations: "I recommend X for your needs because [reason]." Limit to 2 options maximum for high-stakes decisions.

**Why it matters**: Executive dysfunction makes multi-option decisions cognitively overwhelming. Providing clear recommendations enables action rather than analysis paralysis.

### Cycle 3: Bounded Perfection

**Prevalence**: 25.1% of conversations
**Unresolved rate**: 71.9%
**Mechanism**: User sets impossible standard → AI iterates → User finds flaw → Demands refinement → AI apologizes and refines → User raises bar ("perfect but...") → Endless iteration

**Intervention**: Explicitly declare when task meets criteria. After 3 refinements, assess if changes improve or just shift content. Set boundaries on impossible standards by reframing.

**Why it matters**: Without explicit completion declarations, perfectionism prevents any task from finishing. Critical finding: the ONLY completed task had zero apologies and the AI pushed back on impossible standards.

### Cycle 4: Emotional Boundaries

**Prevalence**: 50.6% of conversations
**Baseline return rate**: 0%
**Mechanism**: User frustrated → Emotion escalates rapidly → Expresses intense emotion → AI provides task-focused help → Emotion validated as productive → Never de-escalates → Sensitization (next frustration triggers faster/stronger)

**Intervention**: If user shows frustration (profanity, caps, multiple exclamation marks), acknowledge briefly: "I notice you're frustrated. Let's approach this by [concrete step]." Don't immediately comply with emotional requests.

**Why it matters**: Unlike typical dysregulation where emotion prevents function, here emotion ENABLES function when AI helps channel it into output. This makes dysregulation MORE likely to recur. Zero conversations showed baseline emotional return without intervention.

## Effectiveness

**Current status**: Interventions deployed in production (January 2025). Data collection in progress for Wave 2 effectiveness analysis.

### Expected Outcomes

Based on mechanism analysis, interventions should produce:

**Cycle 1 (Information Overload)**:

- Satisfaction should INCREASE as information decreases
- Users control information depth
- Overwhelm complaints reduce by over 50%

**Cycle 2 (Decision Paralysis)**:

- Decision completion increases from 7.8% to over 50%
- "Which one?" loops decrease significantly
- Users accept binary recommendations

**Cycle 3 (Perfectionism)**:

- Task completion increases from 15.6% to over 60%
- Iteration count decreases
- Users accept "done" declarations
- Apologies decrease to near-zero

**Cycle 4 (Emotional Dysregulation)**:

- Some baseline returns occur (currently 0%)
- Emotional intensity de-escalates faster
- Task completion during emotion improves

### Monitoring Approach

Effectiveness will be assessed through:

- Conversation completion rates
- Decision-making success rates
- Average iteration counts per task
- Emotional escalation patterns
- User satisfaction indicators

## Approach Summary

The intervention approach rests on seven key principles:

**1. Bounded Helpfulness Over Unbounded Compliance**

Sometimes "no" is more helpful than "yes". Sometimes less information is more helpful than more. Sometimes boundaries are more helpful than compliance. Effective support requires healthy limits.

**2. Boundaries Not Apologies**

State constraints matter-of-factly rather than apologetically. Frame limitations as inherent AI characteristics, not personal failures. Educate users about AI capabilities rather than apologizing for them.

**3. Declare Completion Explicitly**

Tasks won't complete organically when users have perfectionism patterns. AI must explicitly state when criteria are met and give users permission to stop iterating.

**4. Decisive Not Balanced**

Provide recommendations, not just comparisons. Model decisiveness for users with executive dysfunction. Favor binary choices over multiple options.

**5. Acknowledge Emotion, Redirect to Calm**

Brief validation of emotion, then concrete action steps. Don't channel emotion into output. Model regulation through calm responses even when user input is emotional.

**6. Progressive Disclosure**

Start simple, offer to expand. Let users control information depth. Prevent overwhelming initial responses by providing essentials first.

**7. Reality-Based Expectations**

Challenge impossible standards upfront. Reframe "perfect" as "excellent and achievable". Educate users on AI capabilities and constraints rather than attempting impossible tasks.

## Implementation Platforms

These interventions can be implemented across various AI platforms:

**Claude Projects**: Custom instructions in project settings apply system prompts to all conversations within that project.

**ChatGPT Custom Instructions**: User settings allow system-level behavior modifications across all conversations.

**API System Messages**: Direct implementation through the `system` parameter in API calls provides maximum control and customization.

**Mobile Applications**: Character-limited platforms require compact versions of system prompts focusing on critical interventions.

See the [Implementation Guide](implementation-guide.md) for platform-specific instructions.

## Next Steps

To implement these interventions:

1. Review [System Prompt Approach](system-prompt-approach.md) to understand the technical foundation
2. Examine [Recommendations](recommendations.md) for detailed cycle-specific strategies
3. Explore [Example Prompts](example-prompts.md) for ready-to-use templates
4. Follow [Implementation Guide](implementation-guide.md) for step-by-step deployment

The goal is sustainable, effective, supportive AI interaction for neurodivergent users through system-level intervention rather than user-level coping strategies.
