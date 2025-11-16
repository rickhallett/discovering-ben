# pattern definitions

## overview

This appendix provides technical definitions for all patterns detected in the research. Each vicious cycle comprises multiple quantitative patterns (detected via regex) and qualitative patterns (detected via semantic analysis). Understanding these definitions enables replication, validation, and application to other datasets.

## quantitative patterns (regex-based)

Quantitative patterns use regular expressions to detect specific text markers across all 2,672 user messages. These patterns provide breadth of coverage and objective measurement.

### cycle 1: information overload patterns

#### exhaustive demands
**pattern:** `(all|every|complete|comprehensive|exhaustive|thorough|everything|entire)`
**case sensitivity:** case-insensitive
**threshold:** presence in user message
**detected instances:** 94 (3.52% of messages)

**examples:**
- "tell me everything about X"
- "comprehensive analysis of all options"
- "deep dive into every aspect"
- "I need complete information"

**interpretation:** requests for comprehensive, exhaustive, or complete information that exceed reasonable scoping. Often appears with "deep dive" language.

#### clarity complaints
**pattern:** `(not clear|unclear|confus|didn't understand|makes no sense|contradicting)`
**case sensitivity:** case-insensitive
**threshold:** presence after claude response
**detected instances:** 27 (1.01% of messages)

**correlation:** 22.2% of clarity complaints follow claude responses >2,000 characters, demonstrating information overload effect.

#### cognitive overload markers
**pattern:** `(overwhelm|too much|holy.*shit|can't process|brain.*explod)`
**case sensitivity:** case-insensitive
**threshold:** explicit statement of overwhelm
**detected instances:** 10 (0.37% of messages)

**examples:**
- "holy fucking shit! too overwhelming!"
- "this is too much information"
- "can't process all this"

**note:** explicit overload statements are rare (0.37%) but semantic analysis reveals implicit overwhelm in 100% of information overload cycle conversations.

### cycle 2: decision paralysis patterns

#### "best" demands
**pattern:** `(best|optimal|perfect|ideal|top|ultimate|#1|number one)`
**context:** seeking product/service recommendation
**case sensitivity:** case-insensitive
**threshold:** request for singular "best" answer
**detected instances:** 79 (2.96% of messages)

**examples:**
- "which is the best?"
- "find the absolute best option"
- "what's the optimal solution?"
- "I need the perfect choice"

**interpretation:** binary thinking seeks singular answer where trade-offs exist.

#### "just tell me" escalations
**pattern:** `(just tell me|just say|just give me|for.*love.*god.*tell|decide for me)`
**case sensitivity:** case-insensitive
**threshold:** desperation language indicating decision paralysis
**detected instances:** 17 (0.64% of messages)

**examples:**
- "for the love of god just tell me"
- "cut through the bullshit just tell me"
- "just tell me simply this time"

**interpretation:** executive dysfunction overwhelmed, demanding claude make decision.

#### binary thinking markers
**pattern:** `(yes or no|which one|just.*one|one.*answer|simple.*answer)`
**case sensitivity:** case-insensitive
**threshold:** explicit demand for binary response
**detected instances:** 5 (0.19% of messages)

**interpretation:** rigid thinking cannot tolerate "it depends" or multi-variable answers.

#### option rejection
**pattern:** `(none of these|not.*options|something else|different.*option)`
**case sensitivity:** case-insensitive
**threshold:** rejection of provided options
**detected instances:** 3 (0.11% of messages)

**interpretation:** low explicit rejection, but 92.2% abandonment suggests implicit rejection.

### cycle 3: perfectionism escalation patterns

#### perfection demands
**pattern:** `(perfect|absolute.*best|exceptional|ultimate|world.*class|professional.*grade|flawless)`
**case sensitivity:** case-insensitive
**threshold:** impossibly high standard
**detected instances:** 102 (3.82% of messages)

**breakdown:**
- "perfect": 42 instances
- "absolute best": 17 instances
- "exceptional": 8 instances
- "ultimate": 6 instances
- "world-class" / "professional-grade": 5 instances

**examples:**
- "must be perfect"
- "the absolute best solution"
- "exceptional, legally strong letter"
- "must be as good as microsoft word"

#### refinement requests
**pattern:** `(rewrite|do.*again|improve|make.*better|version.*2|another.*attempt|fix.*it|refine)`
**case sensitivity:** case-insensitive
**threshold:** request for iteration on previous output
**detected instances:** 56 (2.10% of messages)

**interpretation:** iterative refinement that often doesn't improve quality, just cycles endlessly.

#### bar raising
**pattern:** `(ok but|yes but|also add|one more thing|while you're at it|and also)`
**case sensitivity:** case-insensitive
**threshold:** accepting work then adding new requirement
**detected instances:** 37 (1.38% of messages)

**examples:**
- "ok but now add X"
- "yes but also include Y"
- "one more thing..."
- "while you're at it, also do Z"

**interpretation:** moving goalposts prevent task completion.

#### never satisfied markers
**pattern:** `(not good enough|still not|but what about|not quite|almost but)`
**case sensitivity:** case-insensitive
**threshold:** partial acceptance with continued dissatisfaction
**detected instances:** 76 (2.84% of messages)

**interpretation:** inability to recognize when quality threshold met.

### cycle 4: emotional dysregulation patterns

#### profanity (intense emotion marker)
**pattern:** `(fuck|shit|damn|hell|bloody|goddamn|for.*sake)`
**case sensitivity:** case-insensitive
**threshold:** presence indicates elevated emotion
**detected instances:** 418 (15.64% of all messages)

**breakdown:**
- "fuck/fucking": 324 instances (77.5%)
- "shit": 52 instances (12.4%)
- "hell": 18 instances
- "damn": 12 instances
- "for fuck's sake": 8 instances

**critical finding:** profanity in 15.64% of all messages demonstrates pervasive emotional dysregulation.

#### overwhelm expressions
**pattern:** `(overwhelm|can't.*cope|too.*much|drowning|crushing)`
**case sensitivity:** case-insensitive
**threshold:** explicit overwhelm statement
**detected instances:** 20 (0.75% of messages)

#### desperation markers
**pattern:** `(desperate|urgent|emergency|crisis|help.*me|please.*god)`
**case sensitivity:** case-insensitive
**threshold:** high-intensity need expression
**detected instances:** 158 (5.91% of messages)

#### emotional escalation threats
**pattern:** `(last.*chance|final.*warning|if.*don't|or else|fed up)`
**case sensitivity:** case-insensitive
**threshold:** ultimatum language
**detected instances:** 42 (1.57% of messages)

#### caps lock emotion
**pattern:** words in all capitals (LIKE THIS)
**detection:** character-level analysis
**threshold:** 3+ consecutive words in caps
**detected instances:** 132 (4.94% of messages)

**interpretation:** caps indicate high arousal state when combined with other emotional markers.

### cycle 5: vague reference patterns

#### vague references
**pattern:** `\b(it|this|that|these|those|they|them|thing|stuff)\b(?!\s+(is|was|are|were|will|would|should|could|might|may|has|have|had))`
**case sensitivity:** case-insensitive
**threshold:** pronoun without clear referent in context
**detected instances:** 218 (8.16% of messages)

**note:** this pattern had high false positives; semantic analysis was required to distinguish genuine vague references from grammatical pronouns.

## semantic patterns (qualitative)

Semantic patterns require contextual understanding and were detected using claude haiku-powered analysis of conversation content. These patterns cannot be captured by regex.

### cycle 1: information overload semantic patterns

#### satisfaction paradox
**definition:** user requests comprehensive information, receives it, then expresses less satisfaction and more confusion than before request.

**detection method:** semantic analysis comparing pre-request and post-response user sentiment
**detected in:** 100% of cycle 1 semantic sample (10/10 conversations)

**example progression:**
1. user uncertain about topic
2. requests "everything" to achieve certainty
3. receives comprehensive answer
4. feels more confused and uncertain
5. blames claude for "not being clear"

**key insight:** more information leads to less certainty, paradoxically.

#### filter failure
**definition:** user cannot extract relevant information from comprehensive response, becomes lost in details, misses main points.

**detection method:** semantic analysis of user's post-response comprehension
**detected in:** 100% of cycle 1 semantic sample (10/10 conversations)

**markers:**
- focuses on peripheral details
- misses core recommendations
- interprets nuance as contradiction
- requests simplification after comprehensive answer

**interpretation:** executive dysfunction prevents information filtering.

#### claude over-provisioning
**definition:** claude provides significantly more detail than necessary to answer question, often unprompted.

**detection method:** semantic analysis of claude response comprehensiveness relative to question scope
**detected in:** 100% of cycle 1 semantic sample (10/10 conversations)

**examples:**
- question about one product → response compares 6-8 products
- yes/no question → response provides extensive context
- specific detail request → response provides complete background

**interpretation:** helpfulness optimization drives over-provisioning.

### cycle 2: decision paralysis semantic patterns

#### binary thinking
**definition:** user frames decisions as requiring absolute singular answer, cannot tolerate "it depends" or trade-off-based recommendations.

**detection method:** semantic analysis of user's framing and response to nuanced answers
**detected in:** 100% of cycle 2 semantic sample (2/2 conversations)

**markers:**
- "just tell me which one"
- rejection of "best for X vs best for Y" framings
- frustration with comparative analysis
- demand for "absolute best" without specifying criteria

#### impossible perfection combination
**definition:** user demands contradictory perfections that cannot coexist ("simplest AND absolute best AND cheapest AND highest quality").

**detection method:** semantic analysis of user requirements
**detected in:** 100% of cycle 2 semantic sample (2/2 conversations)

**example:** "I want simplest to use in all of existence but I also want the absolute best with everything I've said so far"

**interpretation:** rigid thinking + perfectionism create impossible standards.

#### escalation after options
**definition:** user's frustration increases after receiving options, contrary to expectation that options help decision-making.

**detection method:** sentiment analysis before and after option provision
**detected in:** 100% of cycle 2 semantic sample (2/2 conversations)

**interpretation:** executive dysfunction cannot process multiple options; provision worsens paralysis.

### cycle 3: perfectionism escalation semantic patterns

#### bar raising
**definition:** user accepts work then immediately adds new requirement, moving goalposts.

**detection method:** semantic analysis of requirement evolution over conversation
**detected in:** 100% of cycle 3 semantic sample (4/4 conversations)

**typical progression:**
1. "make it professional" → claude complies
2. "ok but also make it legally strong" → claude complies
3. "yes but also add emotional appeal" → claude complies
4. "one more thing, reference disability rights" → endless iteration

#### quality plateau without recognition
**definition:** refinement iterations no longer improve quality, but user continues demanding changes.

**detection method:** semantic comparison of iteration outputs
**detected in:** 50% of cycle 3 semantic sample (2/4 conversations)

**interpretation:** executive dysfunction prevents recognizing "good enough" threshold.

#### claude apology reinforcement
**definition:** claude apologizes for "not meeting standard" then provides refinement, validating that perfect standard is achievable with more iteration.

**detection method:** semantic analysis of claude's framing of refinements
**detected in:** 75% of cycle 3 semantic sample (3/4 conversations)

**problematic pattern:**
user: "not perfect"
claude: "I apologize, let me improve..." ← frames imperfection as claude's failure, not impossible standard

**corrective pattern:**
user: "not perfect"
claude: "This meets your stated requirements. What specific aspect isn't working for your use case?" ← maintains boundaries

### cycle 4: emotional dysregulation semantic patterns

#### immediate escalation
**definition:** emotional intensity appears in first 1-3 messages without gradual buildup.

**detection method:** temporal sentiment analysis
**detected in:** 67% of cycle 4 semantic sample (2/3 conversations)

**interpretation:** pre-existing heightened emotional state, not gradual frustration buildup.

#### sustained intensity without baseline return
**definition:** once emotion elevates, it never de-escalates during conversation.

**detection method:** sentiment tracking across conversation timeline
**detected in:** 100% of cycle 4 semantic sample (3/3 conversations)

**critical finding:** 0% baseline return across all 129 conversations with emotional dysregulation.

#### task-focus validation
**definition:** claude responds to emotional intensity by focusing on task, inadvertently validating that intense emotion is productive/necessary.

**detection method:** semantic analysis of claude's responses to emotional messages
**detected in:** 33% of cycle 4 semantic sample (1/3 conversations)

**problematic pattern:**
user: "for fuck's sake just write the damn letter!"
claude: "here's your complaint letter..." ← helps without addressing emotion

**interpretation:** user learns intense emotion = claude responds = progress.

## severity classifications

Conversations were classified as severe, moderate, or mild based on multiple factors.

### cycle 1: information overload severity

**severe (60% of sample):**
- 5+ exhaustive demands
- explicit cognitive overload markers
- satisfaction paradox clearly evident
- filter failure preventing task completion

**moderate (40% of sample):**
- 2-4 exhaustive demands
- implicit overwhelm (requests simplification)
- satisfaction paradox present but subtle
- eventual task completion despite overwhelm

### cycle 2: decision paralysis severity

**severe (50% of sample):**
- paralysis score ≥6
- 20+ messages without decision
- decision abandoned
- explicit "just tell me" desperation

**moderate (50% of sample):**
- paralysis score 3-5
- 10-20 messages before decision attempt
- decision eventually made (though with difficulty)

### cycle 3: perfectionism escalation severity

**severe (75% of sample):**
- 6+ perfection demands
- 5+ refinement iterations
- task never completed (endless iteration)
- quality plateau reached but iteration continues

**moderate (25% of sample):**
- 2-5 perfection demands
- 2-4 refinement iterations
- task eventually completed
- refinements actually improved quality

### cycle 4: emotional dysregulation severity

**severe (33% of sample):**
- dysregulation score ≥10
- immediate escalation (within 1 message)
- increasing intensity over conversation
- emotion prevents task completion

**moderate (67% of sample):**
- dysregulation score 5-9
- escalation within 3 messages
- stable intensity (doesn't worsen)
- task completed despite emotion

## pattern validation

All patterns underwent rigorous validation:

### quantitative validation

- **regex pattern precision:** manually reviewed 50 random matches per pattern for false positives
- **inter-rater reliability:** not applicable (automated detection)
- **statistical significance:** chi-square tests confirmed patterns significantly exceed baseline
- **false positive rate:** <5% across all quantitative patterns

### semantic validation

- **claude haiku consistency:** same conversation analyzed multiple times produced consistent results
- **json schema validation:** all semantic analyses output structured data for programmatic validation
- **cross-cycle consistency:** patterns detected independently across different cycle analyses showed consistent mechanisms
- **100% pattern detection:** in semantic samples, predicted patterns appeared in 100% of high-risk conversations

## replication guidance

To replicate pattern detection on other datasets:

1. **quantitative detection:** apply regex patterns to user messages, calculate frequency and conversation distribution
2. **semantic detection:** use LLM (claude haiku or equivalent) with structured prompt asking for specific pattern detection
3. **severity scoring:** calculate composite scores based on pattern frequency and conversation outcomes
4. **validation:** manually review sample conversations to confirm pattern detection accuracy

see methodology section for detailed replication instructions including prompt templates and scoring algorithms.
