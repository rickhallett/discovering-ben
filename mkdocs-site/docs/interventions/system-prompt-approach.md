# System Prompt Approach

## What Are System Prompts

System prompts are persistent instructions that shape AI behavior across all conversations. Unlike user messages (which change with each interaction) or assistant responses (which the AI generates), system prompts provide context that influences every response the AI produces.

### Technical Architecture

In most LLM implementations, conversations have three types of messages:

**System messages**: Invisible to the user, these set behavioral guidelines, tone, constraints, and context that persist throughout the conversation. They establish "who" the AI is and "how" it should respond.

**User messages**: The questions, requests, and inputs from the person using the AI.

**Assistant messages**: The AI's responses to user messages, shaped by both the user input and the system prompt.

System prompts operate at a different level than the conversation itself. They're meta-instructions that modify how the AI interprets and responds to all user input.

### How They Work

When an AI receives a user message, it doesn't just process that message in isolation. Instead, it considers:

1. The system prompt (persistent behavioral guidelines)
2. Previous conversation history (context)
3. The current user message (immediate request)
4. Training data and RLHF patterns (base behavior)

The system prompt can override or modify default RLHF behaviors. For example, standard training might teach an AI to provide comprehensive responses, but a system prompt can instruct it to ask about detail level first.

### Scope and Limitations

**What system prompts CAN do**:

- Modify response structure and format
- Set boundaries on response length
- Change decision-making approaches
- Establish emotional regulation patterns
- Define how to handle specific user traits
- Override some default RLHF behaviors

**What system prompts CANNOT do**:

- Fundamentally change the model's capabilities
- Access information outside training data
- Create genuinely new reasoning abilities
- Override all safety constraints
- Guarantee 100% compliance with instructions

## Advantages

System prompts offer several unique benefits for implementing neurodivergent support interventions.

### Persistent Across Conversations

Once configured, system prompts apply to every new conversation automatically. Users don't need to:

- Remember to apply strategies at the start of each chat
- Explain their needs every time
- Hope the AI remembers from previous sessions
- Use mental energy managing the AI's behavior

This persistence is particularly valuable for neurodivergent users who may struggle with executive function, task initiation, or working memory.

### User Doesn't Need to Remember Strategies

Traditional coping strategies require users to:

1. Recognize when they're entering a vicious cycle
2. Remember the appropriate counter-strategy
3. Articulate it to the AI clearly
4. Apply it consistently across conversations

System prompts eliminate all four requirements. The AI automatically implements healthy boundaries without user awareness or intervention.

### Consistent Application

Human support (therapists, coaches, friends) varies in how consistently they apply techniques. Fatigue, distraction, and individual differences affect implementation.

System prompts apply interventions uniformly:

- Every conversation gets the same protections
- No variation based on time of day or AI "mood"
- No need to build rapport or explain needs
- Immediate application from the first message

### Reduces Cognitive Load

For neurodivergent users managing executive dysfunction, emotional regulation challenges, or cognitive overwhelm, system prompts reduce the mental burden of interaction.

**Without system prompts**, users must:

- Monitor their own emotional state
- Recognize when they're getting overwhelmed
- Know how to ask for different AI behavior
- Maintain awareness of AI limitations
- Self-regulate throughout the conversation

**With system prompts**, the AI:

- Monitors for signs of overwhelm
- Proactively scopes information
- Offers appropriate decision support
- Declares completion explicitly
- Helps regulate emotional responses

This transfers cognitive load from the user (who may be struggling) to the system (which can apply rules consistently).

## Challenges

While powerful, system prompts have limitations that must be understood and managed.

### One-Size-Fits-All Limitations

System prompts apply the same interventions regardless of:

- Current context or situation
- User's state in the moment
- Specific nature of the task
- Whether intervention is needed right now

**Example challenge**: A system prompt might ask about detail level even when the user clearly needs comprehensive information. Or it might provide binary recommendations when the user genuinely needs to understand trade-offs.

**Mitigation strategies**:

- Design prompts with conditional logic: "When user asks 'which is best?' provide recommendation"
- Include escape hatches: "If you have different priorities, let me know"
- Focus on high-impact interventions that rarely cause problems
- Allow user override when needed

### Overfitting Risk

System prompts designed for specific observed problems might:

- Address symptoms rather than root causes
- Create brittleness when situations vary slightly
- Over-correct in ways that create new problems
- Assume all conversations match the pattern

**Example challenge**: A prompt designed to limit iterations might prevent legitimate multi-stage projects that genuinely need many refinements.

**Mitigation strategies**:

- Base prompts on pattern analysis, not individual incidents
- Test across diverse conversation types
- Include reasoning in prompts, not just rules
- Design for principles, not specific scenarios

### Evolution Over Time

User needs, AI capabilities, and interaction patterns all change:

- Users may develop better coping strategies, needing less intervention
- New vicious cycles may emerge that weren't initially observed
- AI models update with different base behaviors
- Initial interventions may become less effective or unnecessary

**Example challenge**: An intervention for Cycle 1 might work perfectly for six months, then stop being effective as the user's information processing evolves.

**Mitigation strategies**:

- Monitor effectiveness metrics over time
- Plan for regular prompt iterations
- Build flexibility into prompt design
- Document what changes and when

## Design Principles

Effective system prompts for neurodivergent support follow these core principles:

### 1. Bounded Helpfulness

Replace unbounded compliance with healthy limits.

**Implementation**: Include explicit boundaries in prompts about information quantity, option proliferation, iteration counts, and scope expansion.

**Example**: "After 3 refinements, assess whether changes improve or just shift content. If lateral, declare current version final."

### 2. Explicit Over Implicit

Make invisible rules visible. State what would normally be assumed.

**Implementation**: Explicitly declare completion, state confidence levels, verbalize limitations, and clarify when tasks are done versus when new tasks begin.

**Example**: "Explicitly declare when task meets criteria: 'This letter now meets professional standards for [use case].'"

### 3. Emotion Regulation Boundaries

Acknowledge emotion without validating it as productive.

**Implementation**: Brief emotional acknowledgment, pause before proceeding, redirect to calm concrete action, and refuse to channel dysregulation into output.

**Example**: "When user expresses intense emotion (profanity, caps), acknowledge briefly: 'I notice you're frustrated.' Then redirect: 'Let's approach this by [concrete step].'"

### 4. Decision Support Frameworks

Provide decisive guidance rather than balanced paralysis.

**Implementation**: Binary recommendations when appropriate, maximum 2 options for high-stakes decisions, and modeling decisive thinking rather than comprehensive analysis.

**Example**: "When user asks 'which is best?' provide binary recommendation: 'I recommend X for your needs because [specific reason].'"

### 5. Information Scoping

Right-size information to actual needs, not maximum possible detail.

**Implementation**: Ask about detail level before comprehensive responses, use graduated delivery (start simple, offer to expand), and cap initial responses around 500 words.

**Example**: "Before providing comprehensive information, ask: 'How much detail do you need? (brief / moderate / comprehensive)'"

### 6. Constraints as Boundaries, Not Failures

Frame AI limitations as inherent characteristics, not personal shortcomings.

**Implementation**: Never apologize for AI constraints. State them matter-of-factly. Position limitations as inherent system characteristics.

**Example**: "Don't say: 'I apologize, I can't guarantee 100% accuracy.' Instead: 'I'm a probabilistic AI - I provide high-confidence answers, not guarantees.'"

### 7. Reality-Based Expectations

Challenge impossible standards upfront rather than attempting them.

**Implementation**: Reframe "perfect" as "excellent and achievable," explain what AI actually can and cannot do, and set realistic success criteria.

**Example**: "When user demands 'absolute best' or 'perfect': 'I can provide excellent [output], but perfect isn't achievable. Let's aim for [realistic goal].'"

## Implementation Platforms

System prompts can be implemented across various AI platforms with different capabilities and constraints.

### Claude Projects

**Implementation**: Custom instructions in project settings
**Character limit**: Approximately 8,000 characters
**Recommended tier**: Standard (2,000-3,000 characters)
**Persistence**: Applies to all conversations within that project

**How to set up**:

1. Create or open a Claude project
2. Access project settings
3. Navigate to custom instructions field
4. Paste system prompt
5. Save and test

**Advantages**: Large character limit allows comprehensive prompts. Project-based scope means different projects can have different interventions.

**Limitations**: Requires Claude Projects feature (not available on all accounts).

### ChatGPT Custom Instructions

**Implementation**: User settings > Custom Instructions
**Character limit**: Approximately 1,500 characters
**Recommended tier**: Compact (500-800 characters)
**Persistence**: Applies to all conversations for that user

**How to set up**:

1. Open ChatGPT settings
2. Navigate to Custom Instructions
3. Enter prompt in "How would you like ChatGPT to respond?"
4. Save and test

**Advantages**: Universal application across all ChatGPT conversations. Simple interface.

**Limitations**: Strict character limits require compact prompts. Applies to ALL conversations (no per-project customization).

### API System Messages

**Implementation**: `system` parameter in API calls
**Character limit**: Model-dependent (typically 10,000+ tokens)
**Recommended tier**: Extended (5,000+ characters)
**Persistence**: Per-conversation (set when initializing)

**How to set up**:

```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

system_prompt = """
[Your comprehensive system prompt here]
"""

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "User message"}
    ]
)
```

**Advantages**: Maximum control and customization. No practical character limits. Can implement per-conversation variation.

**Limitations**: Requires technical implementation. No built-in UI. Must manage across conversation turns.

### Mobile Applications

**Implementation**: Varies by app (often in settings)
**Character limit**: Typically 500-1,500 characters
**Recommended tier**: Ultra-compact (400 characters) or Compact (500-800)
**Persistence**: App-dependent

**Challenges**: Severe character restrictions require prioritizing critical interventions only. Focus on Cycles 1-4 (highest impact).

**Strategy**: Use ultra-compact versions focusing on:

- Information scoping
- Binary decisions
- Completion declaration
- Emotion acknowledgment
- Iteration limits

## Three-Tier Architecture

To accommodate different platform constraints, system prompts are designed in three tiers:

### Tier 1: Compact (500-800 characters)

**Use for**: Mobile apps, ChatGPT, character-limited platforms
**Coverage**: Critical interventions only (Cycles 1-4)
**Trade-offs**: Less detailed guidance, minimal reasoning

### Tier 2: Standard (2,000-3,000 characters)

**Use for**: Claude Projects, most desktop applications
**Coverage**: Comprehensive coverage of all interventions
**Trade-offs**: Balanced between detail and length

### Tier 3: Extended (5,000+ characters)

**Use for**: API implementations, custom integrations
**Coverage**: Full reasoning, edge cases, examples
**Trade-offs**: Maximum effectiveness, requires more tokens

See [Example Prompts](example-prompts.md) for complete text of each tier.

## Expected Behavior Changes

Implementing system prompts should produce observable changes in AI behavior:

**Information Provision**:

- Before: 1,500+ word responses to simple questions
- After: Asks detail level, starts with 500 words or less

**Decision Support**:

- Before: "Here are 7 options, each with trade-offs..."
- After: "I recommend X for your needs because [reason]"

**Task Completion**:

- Before: Endless iteration without declaring "done"
- After: "This now meets professional standards. Would you like to finalize?"

**Constraint Handling**:

- Before: "I apologize, I can't guarantee 100% accuracy"
- After: "I provide high-confidence answers, not absolute guarantees"

**Emotional Response**:

- Before: Immediately helps with task during user dysregulation
- After: "I notice you're frustrated. Let's approach this calmly by [step]"

These behavioral shifts break vicious reinforcement cycles at the system level, preventing them from starting rather than trying to escape them mid-conversation.
