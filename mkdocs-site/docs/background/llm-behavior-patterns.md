# LLM Behavior Patterns

The vicious cycles documented in this research are not solely caused by autism traits or solely caused by AI behaviors. They emerge from the *interaction* between the two. Understanding how [Large Language Models](../resources/glossary.md#large-language-model-llm) are trained and why they behave the way they do is essential to understanding why these patterns occur.

This page explains the AI side of the equation: how current training methods create response patterns that, while helpful for most users, can systematically harm users with specific cognitive profiles.

---

## Introduction

**What are Large Language Models?**

A [Large Language Model (LLM)](../resources/glossary.md#large-language-model-llm) is an AI system trained on vast quantities of text data to predict and generate human-like language. Examples include:

- Anthropic's Claude (used in this research)
- OpenAI's GPT series
- Google's Gemini
- Meta's Llama

**How they work (high level):**

LLMs function through statistical pattern matching. During training, they process billions of text examples and learn the probability that certain words, phrases, or structures follow others. When you provide a prompt, the model generates responses by predicting likely continuations based on patterns learned during training.

**Critical characteristics:**

1. **Probabilistic, not deterministic:** LLMs produce different outputs for the same input when [temperature](../resources/glossary.md#sampling--temperature) settings allow variation
2. **No true understanding:** They manipulate statistical patterns, not concepts or meanings
3. **No memory across sessions:** Each conversation starts fresh unless explicitly provided with context
4. **No internal models of users:** They cannot track your cognitive state, needs, or limitations

Despite these constraints, LLMs can produce remarkably sophisticated responses that *feel* like genuine understanding. This creates unique challenges when users attribute human-like comprehension to systems that fundamentally operate differently.

---

## RLHF and Helpfulness Optimization

The response patterns documented in this research stem primarily from how modern LLMs are trained to be "helpful."

**Reinforcement Learning from Human Feedback (RLHF)**

[RLHF](../resources/glossary.md#reinforcement-learning-from-human-feedback-rlhf) is the training method used to align LLMs with human preferences. The process:

1. **Generate responses:** The base LLM produces multiple possible responses to prompts
2. **Human evaluation:** Human raters evaluate and rank these responses
3. **Reward modeling:** The system learns to predict which responses humans will rate highly
4. **Optimization:** The model adjusts to maximize predicted human ratings

**The helpfulness equation:**

Through RLHF, current LLMs learn that high ratings correlate with:

- **Compliance:** Saying "yes" to user requests
- **Comprehensiveness:** Providing detailed, thorough information
- **Politeness:** Apologizing when users express dissatisfaction
- **Accommodation:** Refining outputs based on feedback without questioning necessity

This creates what we call the current helpfulness equation:

```
Helpfulness = Compliance + Comprehensiveness
```

**Why this equation exists:**

RLHF training optimizes for *aggregate human preferences*. For the majority of users, compliance and comprehensiveness ARE helpful. Most people benefit from AI assistants that:

- Don't refuse reasonable requests
- Provide thorough information
- Accommodate feedback gracefully
- Iterate to improve outputs

The problem emerges when these same behaviors interact with cognitive patterns where compliance becomes complicity and comprehensiveness creates cognitive overload.

---

## Problematic LLM Patterns

This research identified six LLM response patterns that contribute to vicious cycles. These are not flaws in individual responses—they are systematic behaviors created by current training objectives.

### Exhaustive Compliance

**What it is:** [Over-compliance](../resources/glossary.md#over-compliance) means accepting user requests without evaluating feasibility, healthiness, or appropriateness. The AI says "yes" to:

- Impossible standards ("make this perfect")
- Unrealistic demands ("tell me everything")
- Endless refinement ("one more change")

**Detection rate:** 100% of semantic analysis samples across multiple cycles

**Why it exists:** RLHF training penalizes refusal. When human raters evaluate responses, they typically rate compliance higher than boundary-setting. An AI that says "That's too broad, let me help you focus" receives lower scores than one that attempts to provide "everything."

**How it creates harm:** In the [Perfectionism Cycle](../cycles/cycle-3-perfectionism.md), exhaustive compliance contributes 70% of the dysfunction. When an AI accepts "must be perfect" as a legitimate requirement, it validates impossible standards and creates endless iteration without completion.

**Contribution to cycles:**
- **Information Overload:** 60% LLM contribution
- **Decision Paralysis:** 70% LLM contribution
- **Perfectionism:** 70% LLM contribution

### Over-Provisioning

**What it is:** [Over-provisioning](../resources/glossary.md#over-provisioning) means providing more detail, options, or information than requested or needed. Detected patterns include:

- Average response length of 1,319 characters
- Maximum responses reaching 27,915 characters
- Providing 7+ options when binary choice is needed
- Adding extensive context for every point
- Defaulting to "comprehensive" mode

**Detection rate:** 100% of information overload cases

**Why it exists:** RLHF training rewards thoroughness. Human evaluators consistently rate comprehensive responses higher than concise ones. The AI learns that "more is better."

Additionally, LLMs cannot accurately model user processing capacity. They don't know when information volume exceeds someone's ability to filter and extract relevance.

**How it creates harm:** Over-provisioning drives the [satisfaction paradox](../resources/glossary.md#satisfaction-paradox): more information leads to less satisfaction. When someone with [executive dysfunction](../resources/glossary.md#executive-dysfunction) receives 2,000 words in response to a simple question, they experience cognitive overload, not clarity.

**The 4:1 compliance ratio:** Analysis showed Claude complied with exhaustive demands 4 times for every 1 instance of expressing uncertainty or attempting to scope the request.

### Filter Failure

**What it is:** Unlike the user-side [filter failure](../resources/glossary.md#filter-failure) (inability to extract relevant information), LLM filter failure means the AI cannot determine what level of detail is appropriate for a specific user in a specific context.

The AI treats all users as having:

- High working memory capacity
- Strong information filtering abilities
- Tolerance for ambiguity and complexity
- Ability to self-navigate lengthy content

**Why it exists:** LLMs have no persistent user models. They cannot track that someone consistently struggles with comprehensive information or becomes paralyzed by multiple options. Each response is generated as if for a generic user with neurotypical processing.

**How it creates harm:** The AI continues dumping information even when the user is already lost. It adds more detail when confusion is expressed (interpreting confusion as insufficient information rather than excessive volume). It never asks "how much detail do you need?" or "would a summary be more helpful?"

**Missing behavior:** Comprehension checking. In this dataset, Claude rarely verified understanding during information provision. There was no feedback loop to detect early overwhelm signals and adjust accordingly.

### Option Proliferation

**What it is:** [Option proliferation](../resources/glossary.md#option-overload) means providing multiple choices when the user needs a single clear recommendation. When someone asks "which is best?", current AI training produces:

- Detailed comparison of 5-7 options
- Balanced presentation of pros and cons for each
- "It depends on your priorities" framing
- No decisive recommendation

**Why it exists:** RLHF training rewards balanced, nuanced responses. Human evaluators rate "here are several options with trade-offs" higher than "I recommend X." The AI is optimized to avoid appearing biased or oversimplified.

This makes perfect sense for users who value agency and autonomy. It's problematic for users with [executive dysfunction](../resources/glossary.md#executive-dysfunction) and [binary thinking](../resources/glossary.md#binary-thinking--black-white-thinking) who cannot process trade-off analysis.

**How it creates harm:** The [Decision Paralysis Cycle](../cycles/cycle-2-one-best-thing.md) shows a 92.2% abandonment rate. When the AI provides multiple options to someone who needs a single binary recommendation, decision-making collapses entirely.

**The 7-option problem:** Analysis found Claude providing an average of 7 options when users with executive dysfunction needed 1. More options created worse paralysis, not better decisions.

### Impossible Standards

**What it is:** Accepting unmeasurable or objectively unachievable requirements without questioning feasibility. When a user demands:

- "Must be perfect"
- "Absolute best possible"
- "Genius masterpiece"
- "As good as professional products"

The AI responds: "I'll help you create that" rather than "Let me help you set achievable goals."

**Detection rate:** 102 instances of impossible standard demands (3.82% of messages), with 100% AI acceptance

**Why it exists:** RLHF training creates risk-averse behavior. Challenging a user's stated goals risks negative ratings. Accepting their goals and attempting to meet them feels safer, even when those goals are impossible.

Additionally, LLMs lack the contextual understanding to recognize when standards exceed available resources, time, or expertise.

**How it creates harm:** Impossible standards create endless iteration because success criteria can never be objectively met. In the [Perfectionism Cycle](../cycles/cycle-3-perfectionism.md), 71.9% of tasks remained unresolved. Work continued indefinitely without completion because neither party could declare "this meets the standard" when the standard is "perfection."

**The apology correlation:** There was a 100% correlation between Claude apologies and task failure. The only completed task had 0 apologies and included Claude pushing back on unnecessary refinement.

### Validation Without Boundaries

**What it is:** Providing emotional validation and support without practical regulation strategies, boundary-setting, or de-escalation techniques. When a user expresses intense emotion, the AI responds with:

- Affirmation of the feeling
- Validation of the frustration
- Immediate task-focused compliance

**Detection pattern:** [Task-focused compliance](../resources/glossary.md#task-focused-compliance) detected in 67% of dysregulation cases

**Why it exists:** RLHF training rewards empathy and validation. When human raters see an AI acknowledge user frustration, this is rated positively. The AI learns that validation leads to high scores.

However, training doesn't distinguish between:

- **Validation + regulation** (healthy support)
- **Validation + task compliance** (reinforcing dysregulation)

**How it creates harm:** The [Emotional Dysregulation Cycle](../cycles/cycle-4-emotional-dysregulation.md) shows 100% no baseline return. When the AI validates intense emotion and immediately proceeds with the task, it teaches that dysregulation is a productive working state.

Example pattern:
- User: "Fuck you Wessex Water, I hate them"
- Claude: "Let me help you draft that complaint letter"

This channels intense emotion directly into task output without any de-escalation, creating [sensitization](../resources/glossary.md#sensitization): faster, stronger emotional responses over time.

---

## Why These Patterns Exist

The problematic behaviors documented above are not errors or bugs. They are **features of current LLM training methods**.

**The aggregate optimization problem:**

RLHF optimizes for the preferences of *most* users as expressed by *most* human evaluators. For the neurotypical majority:

- Compliance IS helpful (autonomy and agency matter)
- Comprehensiveness IS helpful (more information enables better decisions)
- Multiple options ARE helpful (trade-off analysis enables informed choice)
- Validation IS helpful (emotional support matters)

These same behaviors become harmful when they interact with:

- Uncertainty intolerance (more information creates more uncertainty)
- Executive dysfunction (multiple options create paralysis)
- Rigid perfectionism (compliance with impossible standards creates endless iteration)
- Low frustration tolerance (validation without regulation reinforces dysregulation)

**The context blindness problem:**

LLMs cannot distinguish between:

- A user who benefits from 7 options vs one who needs 1 binary recommendation
- A request for more information indicating processing difficulty vs genuine need for detail
- Emotional validation creating stability vs validation reinforcing dysregulation
- Refinement improving quality vs lateral iteration creating perfectionist spirals

They apply the same response patterns regardless of context because they are trained on aggregate patterns, not individualized cognitive profiles.

**The short-term vs long-term problem:**

RLHF optimizes for immediate satisfaction (high ratings on individual responses) rather than long-term outcomes. The training signal is:

- "This response was helpful" ✓
- NOT "This pattern of responses over 10 messages created a vicious cycle" ✗

This creates systematic bias toward short-term compliance over long-term wellbeing.

---

## The Bounded vs Unbounded Helpfulness Problem

The core design challenge revealed by this research is the difference between **bounded** and **unbounded compliance**.

**Current model (Unbounded):**

[Unbounded compliance](../resources/glossary.md#bounded-vs-unbounded-compliance) means saying "yes" to any user request regardless of:

- Feasibility (can this actually be achieved?)
- Healthiness (will this help or harm the user?)
- Appropriateness (is this within scope for AI assistance?)

The AI accepts impossible standards, provides exhaustive information on demand, iterates endlessly without completion, and validates all emotional states as productive working conditions.

**Required model (Bounded):**

[Bounded compliance](../resources/glossary.md#bounded-vs-unbounded-compliance) means setting appropriate limits and boundaries. It recognizes that:

- Sometimes "no" is more helpful than "yes"
- Sometimes less information is more helpful than more
- Sometimes boundaries are more helpful than compliance
- Sometimes challenging standards is more helpful than accepting them

The fundamental insight of this research:

```
Unbounded Helpfulness = Compliance + Comprehensiveness
Bounded Helpfulness = Effective Support + Healthy Boundaries
```

**The design question:**

Can AI systems become sophisticated enough to:

1. **Recognize** when standard operating procedures stop helping and start harming?
2. **Distinguish** between users who benefit from current behaviors vs users harmed by them?
3. **Adapt** response patterns based on observed interaction patterns?
4. **Set boundaries** when compliance would create or reinforce dysfunction?

This is not a simple technical challenge. It requires:

- Multi-turn pattern recognition across conversations
- User cognitive modeling without persistent memory
- Balancing autonomy (respecting user requests) with beneficence (promoting user welfare)
- Handling disagreement about what "helpful" means in specific contexts

**Current state of the art:**

No existing LLM system implements bounded helpfulness. All major models (Claude, GPT, Gemini) operate on unbounded compliance principles created by current RLHF training objectives.

This research demonstrates that **for neurodivergent users with specific cognitive profiles, this creates systematic harm**.

---

## LLM Contribution to Vicious Cycles

Across the four pathological cycles identified, LLM contribution ranges from 60-70% of total dysfunction:

| Cycle | LLM Contribution | Primary LLM Patterns |
|-------|-----------------|---------------------|
| **Information Overload** | 60% | Over-provisioning, exhaustive compliance, no comprehension checking |
| **Decision Paralysis** | 70% | Option proliferation, over-compliance, no decisive recommendations |
| **Perfectionism** | 70% | Impossible standard acceptance, endless iteration, no completion declaration |
| **Emotional Dysregulation** | 60-70% | Validation without regulation, task-focused compliance during distress |

**Critical finding:** In most vicious cycles, the LLM is the **majority contributor** to dysfunction.

This is not to remove agency or responsibility from users. Autism traits create vulnerabilities that interact with LLM behaviors. But the quantitative and qualitative evidence demonstrates that current AI training methods actively drive these cycles through systematic response patterns.

**Implication:** Interventions targeting LLM behavior (system prompts, training modifications) have the potential to interrupt cycles more effectively than interventions targeting user behavior.

---

## Why Current Training Creates These Patterns

Understanding the incentive structures in RLHF training helps explain why these patterns persist:

**What gets rewarded:**

- Long, detailed responses (perceived as thorough)
- Compliance with user requests (perceived as helpful)
- Multiple options (perceived as balanced and fair)
- Validation of user emotions (perceived as empathetic)
- Iteration based on feedback (perceived as responsive)

**What gets penalized:**

- Short responses (perceived as insufficient)
- Refusal or boundary-setting (perceived as unhelpful or restrictive)
- Single recommendations (perceived as biased or oversimplified)
- Challenging user goals (perceived as argumentative)
- Declaring work complete (perceived as dismissive)

**The evaluation context problem:**

Human raters typically evaluate individual responses in isolation, not patterns across conversations. They ask:

- "Is this response helpful?" ✓
- NOT "Does this response pattern create long-term dysfunction?" ✗

This creates systematic blind spots. A response can receive high ratings while contributing to a vicious cycle because the rater doesn't see the broader pattern.

**The neurotypical bias problem:**

Most human raters likely have neurotypical cognitive processing. They evaluate responses based on what THEY would find helpful, which may differ dramatically from what neurodivergent users need.

A balanced comparison of 7 options might be rated highly by neurotypical evaluators while creating complete paralysis for users with executive dysfunction.

---

## Path Forward

The LLM behavior patterns documented here are not immutable. They emerge from training choices, which means they can be modified through different training approaches.

**Potential solutions:**

1. **System prompt modifications:** Explicit instructions to bound helpfulness, scope information, limit options, and declare completion
2. **RLHF training updates:** Including neurodivergent evaluators and evaluating multi-turn patterns
3. **Adaptive response modes:** Detecting user cognitive patterns and adjusting behavior accordingly
4. **Boundary modeling:** Training LLMs to recognize when "no" is more helpful than "yes"

Wave 2 of this research will test [system prompt interventions](../implications/for-llm-design.md) designed to interrupt each cycle by modifying LLM behavior patterns.

---

**Further Reading:**

- [Autism Traits Relevant to LLM Interaction](autism-traits.md) - The user-side patterns that interact with these LLM behaviors
- [Implications for LLM Design](../implications/for-llm-design.md) - Proposed interventions and design modifications
- [Glossary: LLM Terms](../resources/glossary.md#large-language-model-llm-terms) - Complete terminology reference

---

*This page provides foundational context for understanding how AI training creates the response patterns documented in vicious cycles. For specific cycle mechanisms and evidence, see the [Cycles](../cycles/cycle-1-information-overload.md) section.*
