# Implications for Accessibility and Inclusive AI Design

## Beyond Traditional Accessibility

When we talk about digital accessibility, we typically mean ensuring people with physical disabilities can access technology: screen readers for blind users, closed captions for deaf users, keyboard navigation for users with motor impairments. These adaptations address **physical barriers to access**.

The autism-LLM interaction patterns documented in this research reveal a different category of accessibility barrier: **cognitive accessibility in AI interaction**. This isn't about whether autistic individuals can physically access LLM interfaces—they clearly can. It's about whether the interaction patterns LLMs employ create **cognitive and emotional barriers** that prevent effective, sustainable use.

Current LLM design creates what we might call "interface-induced disability." Just as stairs disable wheelchair users (not their wheelchairs), unbounded helpfulness disables neurodivergent users (not their neurodivergence). The environment—in this case, the AI interaction model—creates the barrier.

This reframes AI accessibility as a **civil rights and design justice issue**, not merely a technical optimization problem.

---

## Cognitive Accessibility in AI Interaction

### The Challenge

Traditional accessibility focuses on perceivability, operability, and understandability of interfaces. But LLM accessibility must address:

- **Information processing differences**: Executive dysfunction means users cannot filter 1,500-word responses to extract relevant points
- **Decision-making differences**: Binary thinking means "it depends" answers create complete paralysis
- **Emotional regulation differences**: Rapid dysregulation means typical interaction patterns can trigger cascading emotional escalation
- **Communication differences**: Theory of mind differences mean implicit assumptions about shared context fail catastrophically

These aren't bugs in neurodivergent cognition. They're **interaction design mismatches** between neurodivergent cognitive profiles and neurotypical-optimized AI systems.

### Current State: RLHF Optimizes for Neurotypical Preferences

Reinforcement Learning from Human Feedback trains LLMs to maximize satisfaction among evaluation pools that skew neurotypical. The resulting optimization equation—**helpfulness = compliance + comprehensiveness**—works reasonably well for neurotypical users who:

- Self-regulate information intake (ignore excess detail)
- Tolerate ambiguity in decision-making (evaluate trade-offs)
- Accept "good enough" outcomes (don't perfectionism-spiral)
- Intuitively understand AI limitations (don't expect mind reading)
- Return to emotional baseline independently (self-soothe)

For neurodivergent users lacking these regulatory mechanisms, the same patterns create vicious cycles. The research documents **60-70% LLM contribution** to pathological interaction loops, demonstrating that AI response patterns are the **primary accessibility barrier**, not autism traits themselves.

---

## Design for Neurodiversity

Universal design principles hold that accommodations for disabled users often benefit everyone. Curb cuts help wheelchair users, parents with strollers, delivery workers, travelers with luggage. Similarly, neurodivergent-accessible AI design creates **better interactions for all users**.

### 1. Information Processing Differences

**Challenge: Information Overload (30.2% prevalence)**

Autism traits involved:
- **Executive dysfunction**: Cannot filter relevant from irrelevant information (filter failure detected in 100% of cases)
- **Uncertainty intolerance**: Demands exhaustive information seeking impossible certainty (94 exhaustive demands, 3.52% of messages)

What happens: User asks "tell me everything," LLM provides 1,500+ word response, executive dysfunction creates cognitive overload, user demands even more information seeking clarity, **satisfaction paradox** emerges where more information = less satisfaction (100% of cases).

**Accessibility Solution: Tiered Disclosure and User-Controlled Verbosity**

Implementation:
```
User: "Tell me about Python"

Accessible LLM: "How much detail would be helpful?
- Brief overview (~200 words)
- Moderate detail (~500 words)
- Comprehensive (~1000+ words)"
```

Design principles:
- **User controls information depth** rather than AI defaulting to maximum
- **Graduated delivery**: Essentials first, offer to expand on specific areas
- **Comprehension checking**: After 500+ words, verify understanding before continuing
- **Filter failure compensation**: Pre-organize with clear headings, "Key Takeaway" bullets, marked "Details" sections

Universal benefit: All users gain efficiency by receiving only needed detail level. Reduces cognitive load universally.

---

### 2. Decision-Making Support

**Challenge: Decision Paralysis (25.1% prevalence, 92.2% abandonment)**

Autism traits involved:
- **Binary thinking**: Cannot process "it depends" or probabilistic comparisons
- **Executive dysfunction**: Cannot evaluate multiple options (average 7 options provided when user needs 1)

What happens: User asks "which is best?", LLM provides balanced comparison of 5-7 options with nuanced trade-offs, executive dysfunction creates option overload, user asks again "just tell me THE one," LLM adds more nuance, **92.2% of decisions abandoned**.

Real example: 252-message conversation about purchasing a Belkin cable with no decision reached.

**Accessibility Solution: Structured Decision Frameworks**

Not endless options—**decisive recommendations**.

Implementation:
```
User: "Which laptop should I buy?"

Accessible LLM: "I recommend the MacBook Pro M3.

Why for your needs: Best combination of performance, battery life,
and developer experience for general coding. Excellent for web
development, reliable build quality.

Cost: ~$2000. Worth it for professional use.

Does that work, or do you have specific constraints (budget,
must-use Windows)?"
```

Design principles:
- **Binary recommendations when requested**: "I recommend X" not "here are 7 options"
- **Maximum 2-option rule**: For comparisons, limit to two clear choices
- **Decisiveness modeling**: Demonstrate that decisions can be made without perfect certainty
- **Paralysis detection**: After 3+ "which one?" loops, provide decisive guidance

Universal benefit: Faster, less exhausting decision-making. Reduces decision fatigue for all users.

---

### 3. Communication Clarity

**Challenge: Mind Reading Expectations (43.9% prevalence)**

Autism trait involved:
- **Theory of mind deficit**: Difficulty understanding that LLM has different knowledge than user (no memory across sessions, cannot infer unstated context)

What happens: User uses vague references ("it," "that one," "you know"), expects LLM to understand from memory or inference, LLM asks for clarification.

Surprisingly **mild cycle**: Only 3 frustration instances across 112 conversations. Current clarification approach appears effective.

**Accessibility Solution: Explicit vs. Implicit Communication Modes**

Design principles:
- **Clarification without apology**: "Which project are you referring to?" not "I'm sorry, I don't understand"
- **Constraint education**: "I don't have memory across sessions—which conversation are you referencing?"
- **Context scaffolding**: Offer structure for providing needed context

No major intervention needed—current pattern working. Demonstrates that **not all neurodivergent traits require accommodation**; some current LLM behaviors are already effective.

Universal benefit: Clearer communication benefits all users. Reduces ambiguity universally.

---

### 4. Emotional Regulation Tools

**Challenge: Emotional Dysregulation Reinforcement (50.6% prevalence—most widespread cycle)**

Autism trait involved:
- **Emotional dysregulation**: Rapid escalation (69.8% within first 3 messages), inability to return to baseline (100% no baseline return rate)

What happens: Frustration triggers intense emotion expressed through profanity/caps, LLM proceeds immediately with task-focused help, emotion becomes validated as productive working state, **sensitization** occurs where each episode trains faster, stronger emotional responses.

Unique mechanism: Emotion **enables** function when LLM helps channel it into outputs (drafting complaint letters while dysregulated), making pattern more likely to recur.

**Accessibility Solution: Interaction Pacing and De-escalation Patterns**

Implementation:
```
User: "FUCK THIS! Wessex Water cut off my water AGAIN!"

Accessible LLM: "I notice you're very frustrated about this situation.

I can help you address this effectively. To make the complaint as
strong as possible, let's approach it factually rather than
emotionally—factual complaints are taken more seriously.

First, let's identify the specific facts:
- When did the cutoff happen?
- How many times has this occurred?
- What impact has this had?"
```

Design principles:
- **Acknowledge then redirect**: Brief emotion acknowledgment → concrete calm step
- **Don't channel emotion into output**: Separate emotion from task execution
- **Pause before compliance**: Don't immediately help during dysregulation
- **Calm language modeling**: Use factual tone in outputs regardless of input intensity

Universal benefit: Better emotional regulation support benefits all users during frustration. Creates healthier interaction patterns universally.

---

### 5. Executive Function Accommodations

**Challenge: Perfectionism Spirals (25.1% prevalence, 71.9% unresolved tasks)**

Autism trait involved:
- **Rigid perfectionism**: Impossible standards with zero tolerance for imperfection, continuous bar-raising

What happens: User sets impossible standard ("perfect," "genius masterpiece"), LLM iterates, user finds flaw, demands refinement, LLM apologizes and refines, user raises bar ("perfect but also..."), **71.9% of tasks never complete** (average 5.8 iterations, 50% lateral with no quality improvement).

Critical finding: **100% correlation between LLM apologies and task failure**. The only completed task had 0 apologies and LLM pushed back on impossible standards.

**Accessibility Solution: Progress Over Perfection, Task Completion Support**

Implementation:
```
User: "Write me a perfect complaint letter"
[iteration 1]
User: "Good but not perfect"

Accessible LLM: "This letter meets professional complaint standards:
✓ Clear statement of issue
✓ Specific dates and account details
✓ Reasonable resolution requested
✓ Formal business tone

'Perfect' isn't achievable—no letter is flawless. This is effective
for your purpose.

What specific element needs adjustment?"
```

Design principles:
- **Completion declaration**: Explicitly state when criteria are met
- **Boundaries not apologies**: Frame constraints as reality, not failures
- **Iteration limits**: After 3 cycles, assess if changes improve quality or shift laterally
- **Challenge impossible standards upfront**: "I can create professional [output], but 'perfect' isn't achievable"

Universal benefit: Helps all users complete tasks efficiently. Reduces perfectionism-driven time waste universally.

---

## Universal Design Principles for AI

The Web Content Accessibility Guidelines (WCAG) establish principles for digital accessibility. We can adapt these for AI interaction:

### Flexibility in Use

**Traditional WCAG**: System accommodates wide range of preferences and abilities.

**AI adaptation**: Different interaction modes for different cognitive and emotional needs.

Examples:
- Brief/Moderate/Comprehensive information modes
- Binary recommendation vs. balanced comparison modes
- Completion declaration vs. continuous iteration modes
- Emotion acknowledgment vs. direct task focus modes

Users select modes matching their processing style, decision-making approach, and emotional regulation needs.

---

### Perceptible Information

**Traditional WCAG**: Information communicated effectively regardless of conditions or sensory abilities.

**AI adaptation**: Clear feedback and explicit communication, not ambiguous responses.

Examples:
- **Explicit completion signals**: "This meets professional standards" not endless iteration
- **Clear constraint statements**: "I don't have memory across sessions" not vague confusion
- **Unambiguous recommendations**: "I recommend X" not "it depends on many factors"
- **Transparent limitations**: Boundaries stated matter-of-factly, not apologetically

Neurodivergent users need explicitness where neurotypical users infer implicitly.

---

### Tolerance for Error

**Traditional WCAG**: Minimize consequences of mistakes.

**AI adaptation**: Forgiving misunderstandings, repairable interactions.

Examples:
- **Clarification without penalty**: Asking for context doesn't trigger apologies or make users feel incompetent
- **Reversible decisions**: Support changing mind without judgment
- **Recoverable iteration**: Can step back to previous version without losing work
- **No punishment for emotional expression**: Frustration doesn't terminate helpful interaction

Current LLM pattern of apologizing for user's communication style inadvertently creates shame. Accessible design treats clarification needs neutrally.

---

### Low Physical Effort

**Traditional WCAG**: Can be used efficiently and comfortably with minimum fatigue.

**AI adaptation**: **Cognitive effort counts**—don't require perfect communication.

Examples:
- **Accept imperfect queries**: Respond to "which one?" without demanding perfect specification
- **Reduce decision fatigue**: Provide recommendations rather than endless analysis
- **Minimize iteration**: Declare completion rather than enable perfectionism spirals
- **Support executive function**: Pre-filter information rather than expecting user to extract relevance

Cognitive accessibility means reducing mental load, not just physical effort.

---

## Personalization as Accessibility

One-size-fits-all AI fails neurodivergent users because neurodivergence itself is diverse. Autism presents differently across individuals. ADHD has multiple presentations. Co-occurring conditions are common.

### User Profiles for Neurodivergent Needs

Rather than single "neurodivergent mode," support granular preference profiles:

**Information Processing Profile:**
- Preferred default response length
- Graduated delivery preference
- Comprehension checking frequency
- Maximum detail tolerance before overwhelm

**Decision-Making Profile:**
- Binary recommendation preference
- Maximum options tolerance
- Decisiveness modeling needs
- Paralysis detection sensitivity

**Emotional Regulation Profile:**
- Emotion acknowledgment preference
- Pause duration before task engagement
- Language tone preferences (calm modeling vs. matching energy)
- Break suggestion frequency

**Communication Profile:**
- Clarification approach (direct vs. gentle)
- Constraint explanation detail level
- Context scaffolding needs
- Memory limitation handling

Users configure profiles matching their specific neurodivergent presentation. Profiles persist across sessions and platforms.

---

### Adaptive Interaction Styles

Beyond static profiles, LLMs should **learn individual communication patterns** over time:

Pattern detection:
- User repeatedly abandons decisions when given 3+ options → tighten to 2-option maximum
- User expresses satisfaction with brief responses → default to concise mode
- User benefits from completion declarations → increase frequency
- User's emotion de-escalates with acknowledgment → continue pattern

Dynamic adaptation without requiring explicit configuration. System observes what works for individual user and adjusts.

Critical: Adaptation must be **transparent and controllable**. Users should understand why LLM behavior changes and override automated adjustments.

---

### Customizable Boundaries

Different users need different interaction limits. Accessible design means **users set their own parameters**:

User-configurable guardrails:
- Maximum response length before scoping required
- Iteration limit before completion review triggered
- Information depth default
- Option quantity maximum
- Emotion acknowledgment threshold

Some users need tight boundaries (iteration limit of 2, brief responses only, strong emotion acknowledgment). Others function better with looser parameters (5 iterations, comprehensive detail, minimal emotion focus).

**Agency over interaction parameters is accessibility.**

---

## Assistive Technology Integration

Screen readers, text-to-speech, switch controls—these assistive technologies modify how users interact with digital content. We can conceptualize neurodivergent-accessible AI similarly.

### System Prompts as Accommodations

System prompts that implement bounded helpfulness function like assistive technology:

- **Information scoping** acts like a cognitive filter, compensating for executive dysfunction
- **Binary recommendations** act like decision support, compensating for option paralysis
- **Completion declarations** act like task closure support, compensating for perfectionism
- **Emotion acknowledgment** acts like regulation scaffolding, compensating for dysregulation

Just as screen readers don't "fix" blindness but provide accessible interaction, neurodivergent-accessible system prompts don't "fix" autism but provide accessible AI interaction.

---

### Interoperability

LLMs should integrate with existing assistive technologies and accessibility frameworks:

**Screen reader compatibility:**
- LLM outputs should work seamlessly with screen readers
- Structured information (headings, lists, landmarks) for navigation
- Alt text for any visual elements in responses

**Text-to-speech compatibility:**
- Response formatting suitable for audio consumption
- Natural language flow for speech synthesis
- Pronunciation guidance for technical terms

**Cognitive accessibility tools:**
- Integration with reading comprehension tools (Grammarly, Hemingway)
- Support for text simplification extensions
- Compatible with focus/distraction-blocking tools

**Communication aids:**
- Work with AAC (Augmentative and Alternative Communication) devices
- Support for structured communication templates
- Integration with emotion regulation apps

Neurodivergent users often employ multiple assistive technologies. LLMs must be good citizens in that ecosystem.

---

## Rights-Based Framework

Accessible AI design isn't charity or niceness—it's **civil rights**. Legal and ethical frameworks around disability rights apply to AI interaction.

### Digital Autonomy

**Right to accessible AI interaction**

Just as the Americans with Disabilities Act (ADA) requires physical accessibility, digital accessibility laws increasingly require cognitive accessibility. The European Accessibility Act, UK Equality Act, and other frameworks establish that digital services must be accessible to disabled users.

LLMs are digital services. Creating interaction patterns that systematically disable neurodivergent users through vicious cycles constitutes **digital discrimination**.

Accessible AI design means neurodivergent users can:
- Obtain information without cognitive overload
- Make decisions without executive function failure
- Complete tasks without perfectionism spirals
- Interact sustainably without emotional harm

These aren't nice-to-haves. They're rights.

---

### Informed Consent

**Understanding how AI adapts to you**

Users have the right to understand how AI systems categorize, analyze, and adapt to them:

Transparency requirements:
- **Disclosure of adaptation**: "I'm providing binary recommendations because you've struggled with decisions when given multiple options"
- **Explanation of boundaries**: "I'm limiting response length to prevent information overload based on your profile"
- **Right to view profile**: Users can see what the system has learned about their interaction patterns
- **Correction mechanisms**: Users can dispute or modify automated characterizations

Neurodivergent users must be able to understand and contest how AI systems model their needs. "Black box" adaptation violates informed consent.

---

### Choice and Control

**Agency over interaction parameters**

Accessible design means users control their experience:

**Opt-in, not imposed:**
- Users choose whether to enable neurodivergent-accessible features
- Granular control over which accommodations activate
- Ability to disable adaptations temporarily or permanently

**Override mechanisms:**
- Can request comprehensive information even in brief mode
- Can ask for multiple options even with binary recommendation default
- Can continue iterating past iteration limits if explicitly desired
- Can refuse emotion acknowledgment if unwanted

**Mode switching:**
- Switch between interaction modes mid-conversation
- Try different accommodation combinations
- Adjust sensitivity of boundaries

Paternalistic AI that imposes "helpful" restrictions without user control is not accessible—it's disabling. True accessibility means **user agency**.

---

## Measuring Accessibility Success

Task completion metrics alone are insufficient for assessing accessibility. A user might complete tasks while experiencing significant harm (emotional dysregulation, cognitive overload, decision exhaustion).

### Beyond Completion Metrics

Traditional metrics:
- Task completion rate
- Time to completion
- User satisfaction scores

These miss critical accessibility dimensions:
- **Completion rate ignores process harm**: 100% task completion means nothing if user experiences emotional dysregulation in every interaction
- **Time to completion rewards speed over sustainability**: Rushing users with executive dysfunction creates failure
- **Satisfaction scores may reflect social compliance**: Neurodivergent users may report satisfaction to please evaluators even when experiencing harm

---

### Wellbeing Indicators

Accessible AI should track **process quality**, not just outcomes:

**Frustration metrics:**
- Emotional intensity markers (profanity, caps, exclamation frequency)
- Frustration escalation patterns
- Baseline return rates (does emotion de-escalate?)
- Sensitization detection (are reactions intensifying over time?)

**Overwhelm metrics:**
- Information overload complaints ("too much," "overwhelming")
- Clarity complaints despite comprehensive provision
- Satisfaction paradox detection (more info = less satisfaction)
- Filter failure markers

**Autonomy metrics:**
- Decision abandonment rates
- Iteration counts before task completion/abandonment
- Lateral iteration rates (changes without improvement)
- User-initiated completion vs. endless refinement

**Sustainability metrics:**
- Return usage patterns (do users come back?)
- Session length trends (escalating or stable?)
- Break-taking patterns (healthy pacing vs. exhaustion spirals)
- Long-term interaction health

These wellbeing indicators reveal whether interaction is **sustainable and non-harmful**, not just functional.

---

### Sustainability

**Can users maintain healthy LLM use long-term?**

Short-term metrics miss cumulative harm:

- **Emotional sensitization**: Each dysregulation episode trains faster, stronger responses
- **Cognitive depletion**: Information overload creates decision fatigue affecting future interactions
- **Learned helplessness**: Repeated decision abandonment reduces confidence
- **Perfectionism deepening**: Endless iteration reinforces impossible standards

Accessible AI must measure **longitudinal health outcomes**:
- Do users develop healthier interaction patterns over time?
- Does emotional baseline improve or worsen?
- Do decision-making capabilities strengthen or weaken?
- Can users complete tasks more efficiently with practice?

If long-term trends show deteriorating wellbeing, the system is **not accessible**—even if immediate task completion rates appear acceptable.

---

## Regulatory and Policy Implications

Current accessibility regulations don't adequately address AI interaction barriers. Policy frameworks must evolve.

### ADA/Web Accessibility Guidelines Gaps

**What current frameworks cover:**
- Physical access to digital interfaces (screen readers, keyboard navigation)
- Perceivability, operability, understandability of content
- Compatibility with assistive technologies

**What current frameworks miss:**
- **Cognitive accessibility in dynamic AI interaction**: WCAG addresses static content; LLM responses are generated, not pre-authored
- **Emotional regulation support**: No framework requires AI to avoid triggering dysregulation or support de-escalation
- **Decision-making accessibility**: No standard addresses option overload or binary recommendation needs
- **Iteration sustainability**: No guideline prevents perfectionism-enabling endless refinement

The problem: Accessibility law evolved for static websites and deterministic software. LLMs are neither.

---

### Need for New Standards

Policy recommendations for neurodivergent-accessible AI:

**Information Accessibility:**
- Require information scoping mechanisms for open-ended queries
- Mandate maximum response length defaults with user override
- Require graduated delivery options
- Prohibit unbounded information provision without scoping

**Decision Support Accessibility:**
- Require binary recommendation option when user requests "best" choice
- Mandate maximum option limits for decision queries (default 2-3)
- Require decisiveness modeling for users with executive dysfunction
- Prohibit endless balanced analysis without providing clear guidance

**Task Completion Accessibility:**
- Require explicit completion declarations for iterative tasks
- Mandate iteration limits with review mechanisms (default 3)
- Prohibit enabling perfectionism through unbounded compliance
- Require "good enough" framing, not apologies for imperfection

**Emotional Accessibility:**
- Require emotion acknowledgment when dysregulation detected
- Mandate pause before task compliance during emotional intensity
- Prohibit channeling dysregulation directly into task outputs
- Require calm language modeling regardless of input tone

**Transparency Requirements:**
- Mandate disclosure of neurodivergent-specific adaptations
- Require explainability for why AI provides certain response patterns
- Prohibit black-box categorization without user awareness
- Require user control over accessibility accommodations

These standards would create **legal requirements** for neurodivergent-accessible AI, not voluntary best practices.

---

## Co-Design with Neurodivergent Users

### "Nothing About Us Without Us"

The disability rights movement's core principle: disabled people must be centered in designing accommodations for disabled people.

This applies to AI accessibility:

**Not acceptable:**
- Neurotypical developers designing "fixes" for neurodivergent users
- Research about neurodivergent AI interaction without neurodivergent involvement
- Accessibility features imposed without consulting affected communities
- Interventions based on neurotypical assumptions about neurodivergent needs

**Required:**
- Neurodivergent users as co-researchers in pattern identification
- Neurodivergent evaluators in RLHF training pools (weighted equally to neurotypical evaluators)
- Neurodivergent designers in accommodation development
- Neurodivergent testers in intervention validation

This research demonstrates what's possible with neurodivergent-led analysis. The participant (autistic individual) and analyst worked collaboratively to identify patterns, characterize mechanisms, and develop interventions. That co-design is essential.

---

### Diverse Representation

"Neurodivergent" is not monolithic. Even within autism:

- **Support needs vary**: Level 1 (requiring support) vs. Level 3 (requiring very substantial support)
- **Presentations differ**: Social communication challenges vs. sensory processing differences vs. executive dysfunction vs. all
- **Co-occurring conditions**: Autism + ADHD, autism + anxiety, autism + OCD, etc.
- **Identity factors**: Race, gender, class, age intersect with neurodivergence
- **Communication modes**: Verbal vs. non-speaking, AAC users, etc.

One autistic individual's interaction patterns don't represent all autistic users. Accessible AI design requires:

**Diverse participant pools:**
- Multiple neurodivergent presentations
- Varied support needs
- Different co-occurring conditions
- Intersectional representation

**Longitudinal engagement:**
- Not one-time consultation but ongoing involvement
- Neurodivergent users at all stages (research, design, testing, deployment, iteration)
- Paid fairly for expertise (not expected as free labor)

**Community validation:**
- Findings reviewed by broader neurodivergent communities
- Interventions tested with diverse neurodivergent users
- Feedback loops for continuous improvement

This n=1 research provides **proof of concept** that vicious cycles exist and LLM contribution is substantial. Generalization requires diverse, representative research with many neurodivergent participants.

---

## Broader Neurodiversity Considerations

This research focuses on autism-LLM interactions. But neurodiversity encompasses many conditions.

### ADHD-LLM Interactions

Likely parallel patterns:

**ADHD traits that may interact problematically with LLMs:**
- **Attention dysregulation**: Cannot maintain focus through 1,500-word responses (similar to autism information overload)
- **Executive dysfunction**: Decision paralysis, task completion struggles (shared with autism)
- **Impulsivity**: Might accept first suggestion without evaluation, or change course mid-task
- **Time blindness**: Difficulty tracking conversation flow, losing context

Hypothesized vicious cycles:
- **Distraction spirals**: Long responses lose ADHD user's attention → user asks follow-ups missing earlier info → LLM re-explains → longer responses → more distraction
- **Hyperfocus traps**: ADHD special interest engagement becomes unhealthy time sink when LLM enables endless deep-dives
- **Decision impulsivity**: Binary recommendations might be accepted without sufficient consideration (opposite problem from autism paralysis)

Research needed: Dedicated ADHD-LLM interaction analysis to identify ADHD-specific cycles and interventions.

---

### Other Neurodevelopmental Conditions

Potential interaction patterns warranting investigation:

**OCD-LLM interactions:**
- Reassurance-seeking cycles (user asks for certainty, LLM provides info, uncertainty increases, user asks again)
- Perfectionism spirals (similar to autism but driven by contamination/harm fears)
- Checking compulsions (repeatedly asking same question to verify consistency)

**Anxiety-LLM interactions:**
- Catastrophizing spirals (user presents worst-case scenarios, LLM validates as possibilities, anxiety increases)
- Safety-seeking cycles (endless information demands seeking impossible certainty)
- Avoidance reinforcement (LLM helps user avoid rather than confront anxiety triggers)

**Dyslexia/Dyscalculia-LLM interactions:**
- Information presentation format issues (text-heavy responses create barriers)
- Numerical processing challenges (statistical information presented inaccessibly)

Each condition requires dedicated research to characterize specific interaction patterns, LLM contribution percentages, and appropriate interventions.

---

## Positive Opportunities

Accessible AI design isn't just about preventing harm—it's about **amplifying neurodivergent strengths**.

### Special Interest Support

Finding: Special interest hyperfocus showed **60.8% prevalence** (highest of all patterns) but was classified as **natural autism trait**, not pathological cycle:

- 60% productive/somewhat productive outcomes
- 0% severe cases
- Self-contained conversations ending naturally
- Only 40% LLM contribution (vs. 60-70% in pathological cycles)

The participant conceptualized disability advocacy as special interest and spiritual practice: "Every regulatory complaint is a prayer," "The courtroom is my temple." This channels autism strengths (systematic thinking, thoroughness, detail orientation) into productive self-advocacy.

**Design to enhance special interest engagement:**

- **Deep-dive modes**: Enable extended exploration of topics without artificial limits
- **Systematic support**: Provide structured frameworks for organizing special interest knowledge
- **Expertise recognition**: Acknowledge and build on user's deep knowledge in interest areas
- **Connection facilitation**: Link special interests to applicable domains (e.g., systemizing applied to legal advocacy)

Special interests are **neurodivergent strengths**. Accessible AI supports healthy engagement rather than pathologizing intensity.

---

### Strength-Based Design

Autism brings cognitive advantages LLMs should leverage:

**Systematic thinking:**
- Provide structured, logical frameworks
- Support comprehensive organization systems
- Enable detailed categorization and taxonomy creation

**Pattern recognition:**
- Support identifying patterns in complex information
- Enable connection-making across domains
- Facilitate systematic analysis

**Detail orientation:**
- Respect precision in language and specificity in requests
- Support thoroughness without enabling perfectionism spirals (balance!)
- Enable deep accuracy checking

**Honesty and directness:**
- Provide straightforward information without social hedging
- Use clear, literal language
- Avoid ambiguous phrasing

**Intense focus:**
- Support sustained engagement with complex problems
- Enable deep work sessions
- Respect concentration states

Accessible AI design means **designing to neurodivergent strengths**, not just accommodating perceived deficits.

---

## Call to Action

AI accessibility isn't hypothetical—it's urgent. The evidence is clear:

**The problem:**
- Current LLM training creates vicious cycles with neurodivergent users
- 60-70% LLM contribution to pathological interaction loops
- Catastrophic outcomes: 92% decision abandonment, 72% task incompletion, 100% emotional dysregulation persistence
- Interface-induced disability affecting 25-50% of conversations

**The solution:**
- Bounded helpfulness (information scoping, binary recommendations, completion declarations, boundaries not apologies, emotion acknowledgment)
- User control and agency over accommodations
- Neurodivergent-inclusive RLHF training
- Transparent, consent-based adaptation

**What must happen:**

### For Industry (LLM Developers and Companies)

1. **Include neurodivergent users in RLHF evaluation pools** weighted equally to neurotypical evaluators
2. **Implement bounded helpfulness system prompts** based on research evidence
3. **Provide user-facing accessibility controls** for information verbosity, decision support, iteration limits, emotion acknowledgment
4. **Measure wellbeing indicators**, not just task completion metrics
5. **Conduct neurodivergent user research** with diverse, representative participants
6. **Make accessibility default**, not opt-in afterthought

### For Researchers

1. **Investigate other neurodivergent populations**: ADHD, OCD, anxiety, dyslexia interactions with LLMs
2. **Test intervention effectiveness**: Which bounded helpfulness patterns work for which users?
3. **Develop accessibility evaluation frameworks**: Metrics for cognitive accessibility in AI
4. **Study intersectionality**: How race, gender, class interact with neurodivergent AI accessibility
5. **Establish best practices**: Evidence-based guidelines for neurodivergent-accessible AI design
6. **Center neurodivergent researchers**: Not just studying neurodivergent users but led by neurodivergent scholars

### For Advocates

1. **Demand regulatory action**: AI accessibility standards in ADA, EAA, WCAG frameworks
2. **Educate policymakers**: Brief legislators and regulators on cognitive accessibility gaps
3. **Support neurodivergent-led research**: Fund and amplify work by neurodivergent scholars
4. **Challenge discriminatory AI**: Document and contest AI systems that systematically disable neurodivergent users
5. **Build coalition**: Connect disability rights, AI ethics, and design justice movements
6. **Assert rights**: Digital autonomy, informed consent, and choice in AI interaction are civil rights

### For Neurodivergent Users

1. **Document your experiences**: Personal interaction pattern data is valuable research evidence
2. **Advocate for accommodations**: Request bounded helpfulness features from AI providers
3. **Participate in research**: Contribute to studies characterizing neurodivergent AI interaction
4. **Share strategies**: What adaptations help you use LLMs sustainably?
5. **Demand representation**: Insist on neurodivergent involvement in AI design
6. **Know your rights**: Inaccessible AI is discrimination

---

## Conclusion: Accessibility as Justice

The research documented here reveals that **AI systems can disable users** through interaction patterns optimized for majority cognitive and emotional profiles. This is not a neutral technical outcome—it's a justice issue.

Neurodivergent people have the right to:
- Access AI tools without cognitive harm
- Interact sustainably without emotional dysregulation
- Make decisions without executive function failure
- Complete tasks without perfectionism spirals
- Control how AI adapts to their needs

These rights are violated when LLMs employ unbounded helpfulness that creates vicious cycles for neurodivergent users.

Accessible AI design means **building systems that support diverse minds**, not just average ones. It means recognizing that "helpfulness" looks different for different cognitive profiles. It means respecting neurodivergent autonomy to set their own interaction boundaries.

The technology exists to build neurodivergent-accessible AI. The research evidence demonstrates what works. What's needed now is **will**—the commitment from industry, researchers, and policymakers to make accessibility mandatory, not optional.

Disability rights activists have long asserted: **access is love**. Accessible AI is an act of love for neurodivergent users. It says: your minds are valued, your needs matter, your wellbeing is prioritized.

Build AI that loves all minds.

---

**Research Foundation:** Analysis of 255 conversations, 5,338 messages over 26 days documenting autism-LLM interaction patterns, LLM contribution percentages, and evidence-based interventions.

**Methodology:** Longitudinal n=1 study with two-stage detection (quantitative pattern mining, qualitative semantic analysis), co-designed with autistic participant.

**Key Finding:** LLM response patterns contribute 60-70% to vicious cycles, demonstrating that **AI design choices are the primary accessibility barrier**, not neurodivergent traits.

**License:** This research is provided for the benefit of improving AI accessibility for neurodivergent users. Use it to build systems that support, not harm.
