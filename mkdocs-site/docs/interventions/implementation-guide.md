# Implementation Guide

## Step-by-Step Deployment

Implementing system prompt interventions requires careful assessment, appropriate selection, and monitoring for effectiveness. Follow this systematic approach.

### Step 1: Assess Which Cycles Are Present

Before implementing interventions, identify which vicious cycles affect the user.

#### Cycle 1: Information Overload

**Indicators**:

- User frequently says "too much," "confusing," or "overwhelming"
- Abandons conversations partway through long responses
- Requests summaries or shorter versions
- Asks comprehensive questions but seems dissatisfied with comprehensive answers
- Shows cognitive overwhelm (needs breaks, re-reading, simplification)

**Severity assessment**:

- Mild: Occasional overwhelm, usually recovers
- Moderate: Frequent overwhelm, affects 20-40% of conversations
- Severe: Most conversations show information overload, satisfaction paradox evident

#### Cycle 2: Decision Paralysis

**Indicators**:

- Repeatedly asks "which one should I choose?" without deciding
- Requests comparisons, rankings, pros/cons lists but doesn't act on them
- Decision-focused conversations abandoned at high rates
- Asks for "the best" option multiple times
- Shows executive dysfunction around choices
- Needs others to make decisions for them

**Severity assessment**:

- Mild: Some decision difficulty, eventually chooses with support
- Moderate: Frequent decision abandonment (40-60% of decisions)
- Severe: Rarely completes decisions without external directive (>80% abandonment)

#### Cycle 3: Perfectionism Escalation

**Indicators**:

- Tasks iterate endlessly without finishing
- Uses language like "perfect but..." or "good but not good enough"
- Sets unrealistic quality standards ("must be perfect," "absolute best")
- Nothing is ever "done" - always finds reasons to refine
- Moves goalposts (adds requirements after saying something is good)
- Lateral iterations (changes that shift rather than improve)

**Severity assessment**:

- Mild: Some perfectionism, usually completes tasks within 4-5 iterations
- Moderate: Many tasks incomplete, 50-70% unresolved
- Severe: Rarely completes tasks (>70% unresolved), endless iteration pattern

#### Cycle 4: Emotional Dysregulation

**Indicators**:

- Emotional intensity escalates rapidly (0 to intense within minutes)
- Uses profanity, caps, multiple exclamation marks when frustrated
- Never returns to calm baseline during conversation
- Small frustrations trigger major emotional responses
- Emotion correlates with demanding behavior
- Sensitization pattern (each frustration triggers faster/stronger)

**Severity assessment**:

- Mild: Occasional dysregulation, sometimes self-regulates
- Moderate: Frequent dysregulation (30-50% of conversations), low baseline return rate
- Severe: High prevalence (>50%), zero baseline returns, rapid escalation

#### Cycle 5: Mind Reading Assumption

**Indicators**:

- Uses vague references ("it", "that one", "you know") without context
- Assumes AI has memory across sessions
- Expects AI to know unstated preferences
- Gets frustrated when AI asks for clarification

**Note**: This cycle currently has good natural mitigation. Only needs explicit intervention if causing significant friction.

### Step 2: Select Appropriate Intervention Level

Based on cycle assessment, choose the right system prompt tier and focus.

#### Decision Matrix

**Use Ultra-Compact Prompt (403 characters)** if:

- Platform has <500 character limit (strict mobile apps)
- Only 1-2 cycles present at mild-moderate severity
- Need minimal viable intervention

**Use Compact Prompt (781 characters)** if:

- Platform has 800-1,500 character limit (ChatGPT, some mobile)
- 2-3 cycles present at moderate severity
- Need balanced intervention without length concerns

**Use Standard Prompt (2,850 characters)** if:

- Platform has 2,000+ character limit (Claude Projects, desktop apps)
- 3+ cycles present, or Cycle 4 present at any severity
- Need comprehensive intervention

**Use Cycle-Specific Prompt** if:

- Only one cycle is significantly problematic
- Other cycles are mild or not present
- Want targeted intervention (1,100-1,450 characters)

#### Special Case: Cycle 4 Priority

Due to its unique characteristics:

- 50.6% prevalence (highest of all cycles)
- 100% no baseline emotional return
- Sensitization mechanism (gets worse over time)
- Emotion enables function (makes dysregulation productive)

**If Cycle 4 is present at moderate-severe level, use comprehensive intervention regardless of other cycles.**

#### Intervention Intensity Guidelines

**Light touch**:

- 1-2 cycles present
- Mild severity
- User has some coping strategies
- Use Compact or cycle-specific prompts

**Standard**:

- 2-3 cycles present
- Moderate severity
- User needs consistent support
- Use Standard prompt

**Intensive**:

- 3+ cycles present
- Severe severity on any cycle
- Cycle 4 at moderate-severe
- Use Standard or Extended prompt (if available)

### Step 3: Deploy System Prompt

Platform-specific deployment instructions.

#### Claude Projects

**Character limit**: ~8,000 characters
**Recommended tier**: Standard (2,850 chars) or customized extended

**Deployment steps**:

1. Open Claude
2. Create new project or open existing project
3. Click project settings (gear icon)
4. Find "Custom instructions" or "Project instructions" field
5. Paste selected system prompt
6. Click "Save" or "Update"
7. Start new conversation within project to test

**Verification**:

- Start new conversation in project
- Run test scenarios (see Testing section below)
- Verify interventions trigger appropriately

**Notes**:

- Instructions apply to ALL conversations in that project
- Different projects can have different instructions
- Updates apply to new conversations, not existing ones

#### ChatGPT Custom Instructions

**Character limit**: ~1,500 characters
**Recommended tier**: Compact (781 chars)

**Deployment steps**:

1. Open ChatGPT
2. Click profile icon (bottom left)
3. Select "Settings" or "Custom instructions"
4. Navigate to "Custom instructions" section
5. Paste system prompt in "How would you like ChatGPT to respond?" field
6. Click "Enable for new chats"
7. Save settings
8. Start new conversation to test

**Verification**:

- Start completely new chat (not continuation)
- Run test scenarios
- Verify AI behavior matches interventions

**Notes**:

- Applies to ALL ChatGPT conversations for your account
- No per-project customization available
- May need to refresh browser for changes to take effect

#### Claude Desktop / Mobile

**Character limit**: Varies (desktop ~8,000, mobile ~1,500)
**Recommended tier**: Desktop = Standard, Mobile = Compact

**Deployment steps**:

1. Open Claude application
2. Access Preferences or Settings
3. Find "Custom instructions" section
4. Paste appropriate system prompt
5. Save settings
6. Start new conversation to test

**Verification**:

- Create fresh conversation
- Test with multiple scenarios
- Confirm consistent application

**Notes**:

- Desktop and mobile may have separate settings
- Check character limits before pasting
- Some mobile apps may not support custom instructions

#### API Implementation

**Character limit**: Model-dependent (typically 10,000+ tokens)
**Recommended tier**: Extended (5,000+ chars if available) or Standard

**Python example (Anthropic API)**:

```python
import anthropic

# Load system prompt
SYSTEM_PROMPT = """
User has autism/Asperger's syndrome with the following interaction characteristics:

[...paste full Standard or Extended prompt here...]

CRITICAL PRINCIPLE:
Replace "unbounded compliance" with "bounded helpfulness"
"""

# Initialize client
client = anthropic.Anthropic(api_key="your-api-key")

# Create message with system prompt
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system=SYSTEM_PROMPT,
    messages=[
        {"role": "user", "content": "User's message here"}
    ]
)

print(message.content)
```

**JavaScript example (Anthropic API)**:

```javascript
import Anthropic from '@anthropic-ai/sdk';

const SYSTEM_PROMPT = `
User has autism/Asperger's syndrome with the following interaction characteristics:

[...paste full Standard or Extended prompt here...]

CRITICAL PRINCIPLE:
Replace "unbounded compliance" with "bounded helpfulness"
`;

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const message = await client.messages.create({
  model: 'claude-3-5-sonnet-20241022',
  max_tokens: 1024,
  system: SYSTEM_PROMPT,
  messages: [
    { role: 'user', content: 'User message here' }
  ],
});

console.log(message.content);
```

**Verification**:

- Test with variety of user inputs
- Verify system prompt persists across conversation turns
- Monitor token usage (system prompt counts toward context)

**Notes**:

- System prompt must be set for each conversation
- Store prompt in configuration file for easy updates
- Consider version tracking for prompt iterations
- Monitor costs (longer prompts = more tokens)

#### OpenAI API (ChatGPT)

**Character limit**: Model-dependent
**Recommended tier**: Standard or Extended

**Python example**:

```python
from openai import OpenAI

SYSTEM_PROMPT = """
User has autism/Asperger's syndrome with the following interaction characteristics:

[...paste full Standard or Extended prompt here...]
"""

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "User message here"}
    ]
)

print(response.choices[0].message.content)
```

**Notes**:

- System message goes first in messages array
- Persists throughout conversation if maintained in messages
- Different models may handle system prompts differently

### Step 4: Monitor Effectiveness

Track metrics to assess whether interventions are working.

#### Quantitative Metrics

**Task completion rate**:

- Baseline: 15.6% (from analysis)
- Target: >60%
- How to track: Of conversations with defined tasks, what percentage reach completion?

**Decision-making rate**:

- Baseline: 7.8%
- Target: >50%
- How to track: Of conversations asking for decisions, what percentage result in a choice?

**Average iteration count**:

- Baseline: 5.8 iterations per task
- Target: <3 iterations
- How to track: Count refinement cycles before task completion or abandonment

**Response length**:

- Baseline: 1,300+ words average
- Target: ~500 words initial response
- How to track: Word count of AI's first substantive response to questions

**Apology frequency**:

- Baseline: High (varies by cycle)
- Target: <5% of responses contain apologies for AI limitations
- How to track: Search responses for "sorry", "apologize", "apologies"

**Emotional baseline returns**:

- Baseline: 0% (no conversations show emotional de-escalation)
- Target: >0% (any improvement is significant)
- How to track: Conversations starting with high emotion - do they de-escalate?

#### Qualitative Indicators

**User satisfaction**:

- Are users expressing less frustration?
- Do conversations feel more productive?
- Are users returning to use AI more often?

**Conversation tone**:

- Reduction in profanity, caps, excessive punctuation
- More collaborative language
- Less demanding/urgent tone

**Task outcomes**:

- More concrete results from conversations
- Fewer abandoned midstream
- Better quality deliverables

**User learning**:

- User develops more realistic expectations over time
- Asks questions more effectively
- Better understanding of AI capabilities

#### Monitoring Tools

**Manual review**:

- Periodically read through conversations
- Note where interventions trigger
- Identify edge cases or problems

**Automated tracking** (for API implementations):

```python
def track_metrics(conversation):
    metrics = {
        'completion': was_task_completed(conversation),
        'iterations': count_refinement_cycles(conversation),
        'avg_response_length': calculate_avg_length(conversation),
        'apologies': count_apologies(conversation),
        'emotion_pattern': analyze_emotional_arc(conversation)
    }
    return metrics
```

**User feedback**:

- Periodic check-ins: "How is the AI helping you?"
- Specific questions: "Do you feel less overwhelmed by responses?"
- Satisfaction ratings after conversations

### Step 5: Iterate Based on Outcomes

Adjust interventions based on effectiveness data.

#### When to Strengthen Interventions

**Signal**: Cycles persist despite implementation

**Actions**:

- Move from Compact to Standard prompt
- Add more directive language
- Tighten boundaries (e.g., reduce iteration limit from 3 to 2)
- Implement earlier intervention (e.g., ask detail level on ALL questions, not just "comprehensive" ones)

**Example**: If users still get decision paralysis with binary recommendations, strengthen to:

```
"I recommend [X]. This is the best choice for your needs.
Shall we proceed with this?"
```

(More directive, less room for re-opening analysis)

#### When to Lighten Interventions

**Signal**: Users frequently override interventions or express frustration with restrictions

**Actions**:

- Move from Standard to Compact prompt
- Less directive language
- Offer rather than declare
- More flexible boundaries

**Example**: If users resist iteration limits, soften to:

```
"We've completed 3 refinements. Would you like me to assess whether
further changes would improve quality, or shall we continue?"
```

(Asks rather than declares)

#### When to Add New Interventions

**Signal**: New patterns emerge that weren't initially present

**Actions**:

- Identify the new vicious cycle
- Design intervention following established principles
- Test with small addition to existing prompt
- Monitor for effectiveness

**Example**: If user develops pattern of asking same question repeatedly (reassurance-seeking):

```
REASSURANCE LOOP DETECTION:
- If user asks substantially the same question 2+ times:
  "I've provided my answer to this question. Asking again won't
  provide different certainty. Would you like to move forward or
  discuss what's making this feel uncertain?"
```

#### When to Remove Interventions

**Signal**: Cycle has resolved, intervention no longer needed

**Actions**:

- Monitor closely before removing (ensure pattern is truly resolved)
- Remove incrementally (lighten first, then remove)
- Keep notes for potential reintroduction if needed

**Example**: If user who previously experienced severe information overload now regularly requests appropriate detail levels:

- Month 1: "How much detail?" appears in 90% of responses
- Month 2: User starts specifying detail level proactively
- Month 3: Reduce to "How much detail?" in 50% of responses
- Month 4: Reduce to only when user uses "comprehensive" or "everything"
- Month 5: Remove entirely, user self-regulates

#### Iteration Timeline

**Weeks 1-2: Baseline observation**

- Deploy prompt
- Track metrics
- Note all interventions triggered
- Identify edge cases
- Don't make changes yet

**Weeks 3-4: First adjustments**

- Address obvious problems
- Fix edge cases causing issues
- Strengthen/lighten based on initial data
- Continue monitoring

**Month 2: Pattern analysis**

- Review accumulated data
- Identify trends
- Make strategic adjustments
- Consider tier changes if needed

**Month 3+: Ongoing optimization**

- Regular review cycles (monthly)
- Incremental refinements
- Track long-term trends
- Adapt to changing user needs

## Safety Considerations

While these interventions are designed to be helpful, there are situations where they might be inappropriate or need modification.

### When Intervention Might Be Inappropriate

#### Crisis Situations

**Issue**: If user is in genuine crisis (suicidal ideation, severe mental health emergency), system prompts designed for general interaction may be inadequate or harmful.

**Signal**: User expresses self-harm intent, extreme distress beyond normal frustration, statements about being unable to continue.

**Response**: Standard system prompts should be overridden by crisis protocols. Consider adding:

```
CRISIS OVERRIDE:
If user expresses suicidal ideation, self-harm intent, or severe crisis:
- Immediately provide crisis resources
- DO NOT apply normal intervention boundaries
- Prioritize safety over bounded helpfulness
- Recommend professional support: [relevant helplines/resources]
```

#### Medical/Legal Advice Contexts

**Issue**: System prompts that provide "decisive recommendations" could be problematic when user asks for medical or legal guidance.

**Signal**: Questions about health decisions, legal actions, financial advice requiring professional expertise.

**Response**: Maintain decision support structure but add disclaimers:

```
When user asks about medical/legal/financial decisions:
"I can provide general information, but these decisions require professional
expertise. I recommend [X] based on general principles, but you should
consult a [professional] before proceeding."
```

#### Situations Requiring Genuine Uncertainty

**Issue**: Some situations genuinely don't have clear answers. Forcing binary recommendations can be inappropriate.

**Signal**: Complex ethical dilemmas, situations with insufficient information, questions requiring domain expertise.

**Response**: Modify decision support to acknowledge genuine uncertainty:

```
"This situation has genuine uncertainty because [reasons]. I can outline
the key considerations, but there isn't a clear 'best' answer:
- [Consideration 1]
- [Consideration 2]

What factors are most important to you?"
```

### When to Modify or Suspend Prompts

#### User Has Developed Independent Coping Strategies

**Signal**: User proactively asks for appropriate detail levels, makes decisions effectively, sets own boundaries.

**Action**: Gradually reduce intervention intensity as user demonstrates capability.

#### User Explicitly Requests Different Behavior

**Signal**: "Don't limit your response," "I want to see all options," "Give me comprehensive detail."

**Action**: Honor explicit requests while gently noting the option for boundaries:

```
"I'll provide comprehensive detail as requested. If at any point you'd
like me to simplify or narrow focus, just let me know."
```

#### Specific Tasks Genuinely Need Exception

**Signal**: Legitimate research projects, comprehensive analysis tasks, multi-stage planning.

**Action**: Allow contextual suspension:

```
"I notice this is a research project requiring comprehensive coverage.
I'll provide detailed information throughout. Let me know if you'd like
me to adjust the detail level at any point."
```

### Avoiding Over-Medicalization

**Risk**: Treating neurodivergent interaction patterns as purely pathological rather than recognizing them as differences.

**Mitigation**:

- Frame interventions as "support" not "treatment"
- Recognize autism traits (like hyperfocus on special interests) as natural, not problematic
- Only intervene on patterns causing harm (vicious cycles), not all differences
- Maintain user autonomy and choice

**Language to avoid**:

- "Correcting" behavior
- "Symptoms" (use "patterns")
- "Abnormal" (use "different")
- "Disorder management" (use "interaction support")

**Language to use**:

- "Supporting effective interaction"
- "Breaking unhelpful cycles"
- "Providing structure"
- "Offering boundaries"

### Respecting User Autonomy

**Principle**: System prompts should support, not control.

**Implementation**:

- Always include escape hatches ("If you have different priorities...")
- Honor explicit user overrides
- Frame as offers, not mandates ("Would you like..." not "I will...")
- Maintain user's ability to choose

**Red flags** (signs prompt is too controlling):

- User frequently fights against interventions
- User expresses feeling restricted or controlled
- User stops using AI because of limitations
- User can't get needed help because of boundaries

**Response**: Lighten interventions, add more flexibility, increase user choice.

### Cultural and Individual Variation

**Consideration**: Communication patterns vary by culture, individual preferences, and context.

**Risk**: System prompts designed for one user profile may be inappropriate for others.

**Mitigation**:

- Customize prompts for individual users when possible
- Avoid one-size-fits-all deployment across diverse user bases
- Test interventions with user's actual communication patterns
- Respect cultural communication norms

### Monitoring for Harmful Patterns

Even well-designed interventions can have unintended negative effects.

**Monitor for**:

- Increased user frustration with AI
- Decreased task completion (interventions may be too restrictive)
- User abandoning AI use entirely
- New vicious cycles emerging
- User feeling misunderstood or unsupported

**Response protocol**:

1. Identify the harmful pattern
2. Assess whether it's intervention-caused
3. Modify or suspend intervention causing harm
4. Monitor for improvement
5. Iterate toward better approach

### Ethical Guidelines

**Transparency**: Users should be able to know they're receiving modified AI behavior (though not necessarily the specifics of how).

**Consent**: When possible, users should consent to intervention approaches.

**Reversibility**: Interventions should be removable if they're not helping.

**Do no harm**: Priority on avoiding negative impacts, even if that means limiting positive impacts.

**Respect**: Frame interventions as support for user's goals, not correction of user's traits.

## Conclusion

Effective implementation requires:

1. **Careful assessment** of which cycles are present
2. **Appropriate selection** of intervention tier and focus
3. **Platform-specific deployment** following technical requirements
4. **Consistent monitoring** of effectiveness metrics
5. **Iterative refinement** based on outcomes and user needs
6. **Safety awareness** for contexts requiring modified approaches

The goal is sustainable, effective, supportive AI interaction - not perfect control over every conversation. Success means users can accomplish their goals more effectively, with less frustration, and with appropriate support for their neurodivergent interaction patterns.

These interventions represent a shift from treating neurodivergent users as solely responsible for managing AI interaction challenges, to recognizing that AI behavior patterns significantly contribute to vicious cycles - and can be modified to break them.

When implemented thoughtfully and monitored carefully, system prompt interventions transform AI from an amplifier of neurodivergent challenges into a supportive tool that works with, rather than against, autistic cognitive and emotional patterns.
