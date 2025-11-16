# MkDocs Website Plan: Publishing the Research

## Overview

Create a public-facing website to share findings on autism-LLM interaction patterns, vicious reinforcement cycles, and proposed interventions.

## Target Audiences

1. **Researchers** - Academic/clinical professionals studying autism and AI interaction
2. **Clinicians** - Therapists and practitioners working with autistic clients
3. **Autistic Community** - Individuals who use LLMs and want to understand patterns
4. **Family Members** - People supporting autistic loved ones
5. **AI Safety Community** - Those interested in alignment and user wellbeing
6. **LLM Developers** - Engineers building better AI assistants

## Files to INCLUDE

### Core Research Findings

**Primary Content:**
- `README.md` → `index.md` (homepage, research overview)
- `analysis/wave-1-vicious-cycles/docs/cycles-summary-complete-analysis.md` → Key findings overview
- `analysis/wave-1-vicious-cycles/docs/cycle-1-information-overload-complete-analysis.md`
- `analysis/wave-1-vicious-cycles/docs/cycle-2-one-best-thing-complete-analysis.md`
- `analysis/wave-1-vicious-cycles/docs/cycle-3-perfectionism-escalation-complete-analysis.md`
- `analysis/wave-1-vicious-cycles/docs/cycle-4-emotional-dysregulation-complete-analysis.md`
- `analysis/wave-1-vicious-cycles/docs/cycle-6-system-building-complete-analysis.md`
- `analysis/wave-1-vicious-cycles/docs/cycle-7-special-interest-hyperfocus-complete-analysis.md`

**Background & Context:**
- `docs/background/neurodivergent-llm-interaction-analysis.md`
- `docs/findings/analysis-neurodivergent-llm-1.md`
- `docs/methodology/investigation-plan-additional-reinforcement-cycles.md`

**Interventions & Solutions:**
- `system-prompts/README.md` → Overview of intervention approach
- `system-prompts/recommendations/system-prompt-recommendations.md`
- `system-prompts/benjamin/v1-compact.md` → Example intervention (anonymized if needed)
- `system-prompts/benjamin/changelog.md` → Evolution of interventions

**Methodology:**
- `analysis/wave-1-vicious-cycles/README.md` → Research approach
- `analysis_pipeline/README.md` → Two-stage detection methodology
- `analysis_pipeline/QUICKSTART.md` → How to replicate analysis
- Create new: `methodology/data-collection.md` - How data was gathered
- Create new: `methodology/ethical-considerations.md` - Privacy, consent, bias

**Tools & Replication:**
- `tools/README.md` → Overview of analysis tools
- Create new: `tools/detector-scripts.md` - Pattern detection approach
- Create new: `tools/semantic-analysis.md` - LLM-assisted analysis
- Create new: `replication-guide.md` - How others can replicate this research

## Files to EXCLUDE

### Private/Sensitive Data
- `conversations.json` - Raw private conversation data (89MB)
- `data/raw/*` - All raw data files
- Any conversation excerpts with identifying information
- Personal details about Benjamin or family

### Internal Tools & Config
- `.claude/*` - Development tools and agents
- `.git/*` - Git history
- `archive/*` - Old files and drafts
- `repomix-output.xml` - Build artifacts
- `CLAUDE.md` - Internal instructions
- `tools/fix-paths.sh`, `tools/restructure.sh` - Internal scripts

### Development Files
- `analysis/wave-1-vicious-cycles/scripts/*` - Python detector scripts (keep descriptions, not code)
- `analysis/wave-1-vicious-cycles/outputs/*` - Raw JSON outputs
- `docs/guides/path-fix-summary.md` - Internal development docs
- `docs/guides/restructure-guide.md` - Internal development docs
- `PIPELINE_SUMMARY.md` - Internal summary (content can be integrated elsewhere)

## Proposed MkDocs Site Structure

```
docs/
├── index.md                                    # Homepage (from README.md)
│
├── overview/
│   ├── research-question.md                    # What we're investigating
│   ├── key-findings.md                         # Summary of discoveries
│   ├── for-researchers.md                      # Academic audience
│   ├── for-autistic-individuals.md             # Practical guidance
│   ├── for-clinicians.md                       # Clinical applications
│   └── for-llm-developers.md                   # Design recommendations
│
├── background/
│   ├── autism-traits.md                        # Relevant autism characteristics
│   ├── llm-behavior-patterns.md                # How LLMs typically respond
│   ├── previous-research.md                    # Related work
│   └── neurodivergent-ai-interaction.md        # From docs/background/
│
├── methodology/
│   ├── overview.md                             # Research approach
│   ├── data-collection.md                      # How data was gathered
│   ├── two-stage-detection.md                  # Quantitative → qualitative
│   ├── pattern-detection.md                    # Regex patterns used
│   ├── semantic-analysis.md                    # LLM-assisted analysis
│   ├── ethical-considerations.md               # Privacy, consent, limitations
│   └── replication-guide.md                    # How to replicate
│
├── cycles/
│   ├── overview.md                             # All 7 cycles summary
│   ├── cycle-1-information-overload.md         # 60% prevalence, 70% LLM
│   ├── cycle-2-one-best-thing.md               # 35% prevalence, 65% LLM
│   ├── cycle-3-perfectionism.md                # 25% prevalence, 60% LLM
│   ├── cycle-4-emotional-dysregulation.md      # 18% prevalence, 55% LLM
│   ├── cycle-5-mind-reading.md                 # 12% prevalence (mild)
│   ├── cycle-6-system-building.md              # 0.8% prevalence (rejected)
│   └── cycle-7-special-interests.md            # 60% prevalence (natural trait)
│
├── interventions/
│   ├── overview.md                             # Intervention philosophy
│   ├── system-prompt-approach.md               # Why system prompts
│   ├── recommendations.md                      # General recommendations
│   ├── example-prompts.md                      # Specific interventions
│   ├── implementation-guide.md                 # How to deploy
│   └── effectiveness.md                        # Future: Wave 2 results
│
├── case-studies/
│   ├── information-overload-example.md         # Detailed example (anonymized)
│   ├── perfectionism-spiral-example.md         # Detailed example
│   ├── successful-intervention-example.md      # Positive outcome
│   └── natural-trait-example.md                # Healthy special interest
│
├── implications/
│   ├── for-llm-design.md                       # Product recommendations
│   ├── for-clinical-practice.md                # Therapeutic applications
│   ├── for-accessibility.md                    # Inclusive AI design
│   ├── ethical-considerations.md               # Broader implications
│   └── future-research.md                      # Open questions
│
├── resources/
│   ├── glossary.md                             # Terms defined
│   ├── further-reading.md                      # Related resources
│   ├── contact.md                              # How to reach out
│   └── contribute.md                           # How others can participate
│
└── appendices/
    ├── dataset-statistics.md                   # 255 convos, 5338 msgs
    ├── pattern-definitions.md                  # Regex patterns used
    ├── llm-contribution-calculation.md         # How we measured LLM role
    └── limitations.md                          # What this research doesn't show
```

## MkDocs Configuration (`mkdocs.yml`)

```yaml
site_name: "Discovering Ben: Autism-LLM Interaction Patterns"
site_description: "Research on vicious reinforcement cycles in autism-LLM interactions and system prompt interventions"
site_author: "Richard Hallett & Family"
site_url: "https://discovering-ben.org"  # Or GitHub Pages URL

theme:
  name: material
  palette:
    # Light mode
    - scheme: default
      primary: indigo
      accent: deep purple
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Dark mode
    - scheme: slate
      primary: indigo
      accent: deep purple
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.tabs.link

  icon:
    repo: fontawesome/brands/github

repo_url: https://github.com/yourusername/discovering-ben
repo_name: discovering-ben

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/yourusername/discovering-ben
    - icon: fontawesome/solid/envelope
      link: mailto:contact@discovering-ben.org

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.details
  - admonition
  - tables
  - footnotes
  - attr_list
  - md_in_html
  - toc:
      permalink: true

plugins:
  - search
  - tags
  - minify:
      minify_html: true

nav:
  - Home: index.md

  - Overview:
      - Research Question: overview/research-question.md
      - Key Findings: overview/key-findings.md
      - For Researchers: overview/for-researchers.md
      - For Autistic Individuals: overview/for-autistic-individuals.md
      - For Clinicians: overview/for-clinicians.md
      - For LLM Developers: overview/for-llm-developers.md

  - Background:
      - Autism Traits: background/autism-traits.md
      - LLM Behavior: background/llm-behavior-patterns.md
      - Previous Research: background/previous-research.md
      - Neurodivergent AI Interaction: background/neurodivergent-ai-interaction.md

  - Methodology:
      - Overview: methodology/overview.md
      - Data Collection: methodology/data-collection.md
      - Two-Stage Detection: methodology/two-stage-detection.md
      - Ethical Considerations: methodology/ethical-considerations.md
      - Replication Guide: methodology/replication-guide.md

  - Vicious Cycles:
      - Summary: cycles/overview.md
      - Cycle 1 - Information Overload: cycles/cycle-1-information-overload.md
      - Cycle 2 - One Best Thing: cycles/cycle-2-one-best-thing.md
      - Cycle 3 - Perfectionism: cycles/cycle-3-perfectionism.md
      - Cycle 4 - Emotional Dysregulation: cycles/cycle-4-emotional-dysregulation.md
      - Cycle 5 - Mind Reading: cycles/cycle-5-mind-reading.md
      - Cycle 6 - System Building: cycles/cycle-6-system-building.md
      - Cycle 7 - Special Interests: cycles/cycle-7-special-interests.md

  - Interventions:
      - Overview: interventions/overview.md
      - System Prompt Approach: interventions/system-prompt-approach.md
      - Recommendations: interventions/recommendations.md
      - Example Prompts: interventions/example-prompts.md
      - Implementation Guide: interventions/implementation-guide.md

  - Case Studies:
      - Information Overload: case-studies/information-overload-example.md
      - Perfectionism Spiral: case-studies/perfectionism-spiral-example.md
      - Successful Intervention: case-studies/successful-intervention-example.md

  - Implications:
      - For LLM Design: implications/for-llm-design.md
      - For Clinical Practice: implications/for-clinical-practice.md
      - For Accessibility: implications/for-accessibility.md
      - Future Research: implications/future-research.md

  - Resources:
      - Glossary: resources/glossary.md
      - Further Reading: resources/further-reading.md
      - Contact: resources/contact.md
      - Contribute: resources/contribute.md

  - Appendices:
      - Dataset Statistics: appendices/dataset-statistics.md
      - Pattern Definitions: appendices/pattern-definitions.md
      - Limitations: appendices/limitations.md
```

## Content Adaptation Strategy

### 1. Create Audience-Specific Entry Points

**For Autistic Individuals:**
- Start with practical implications
- Include self-assessment questions
- Provide actionable recommendations
- Share success stories
- Normalize patterns ("you're not broken")

**For Researchers:**
- Lead with methodology
- Include statistical rigor
- Reference related work
- Discuss limitations
- Suggest future research

**For Clinicians:**
- Focus on clinical applications
- Provide intervention frameworks
- Include case examples
- Discuss contraindications
- Offer assessment tools

**For LLM Developers:**
- Technical recommendations
- UX/UI implications
- Safety considerations
- Implementation examples

### 2. Anonymization & Privacy

- Remove all identifying information from Benjamin's conversations
- Use pseudonyms in case studies
- Aggregate statistics rather than individual quotes where possible
- Explicit consent statement on homepage
- Privacy policy page

### 3. Content Enhancements

**Add visual elements:**
- Cycle diagrams showing reinforcement loops
- Statistical charts (prevalence, LLM contribution)
- Before/after intervention examples
- Infographics for key findings
- Flow charts for methodology

**Add interactive elements:**
- Self-assessment quiz: "Which cycles affect you?"
- Intervention generator: Input your patterns → suggested prompts
- Pattern matcher: Paste conversation → identify potential cycles

**Add narrative elements:**
- Benjamin's story (with consent)
- Family perspective
- Discovery journey
- "Aha moments"

## New Content to Create

### Essential Pages

1. **overview/research-question.md**
   - What led to this research
   - The core hypothesis
   - Why it matters

2. **overview/key-findings.md**
   - Executive summary
   - 4 pathological cycles
   - 1 mild cycle
   - 2 non-issues
   - LLM contribution percentages

3. **methodology/data-collection.md**
   - 255 conversations over 16 months
   - Benjamin's usage patterns
   - Consent and privacy

4. **methodology/ethical-considerations.md**
   - Consent process
   - Privacy protection
   - Potential biases
   - Limitations of generalizing from n=1

5. **interventions/implementation-guide.md**
   - How to deploy system prompts
   - Testing effectiveness
   - Iteration approach
   - Safety considerations

6. **case-studies/** (4 files)
   - **CRITICAL: Extract real examples only from existing analyses**
   - **DO NOT create hypothetical scenarios**
   - Thoroughly anonymize actual conversations
   - Before/after comparisons (if intervention data exists)
   - Label: "Based on actual conversation data"
   - If no data exists yet, mark "Pending Wave 2 results"

7. **implications/** (4 files)
   - Broader impact of findings
   - Recommendations for different stakeholders

8. **resources/glossary.md**
   - Autism terminology
   - LLM terminology
   - Research-specific terms

9. **resources/contact.md**
   - How to reach the research team
   - How to share your own experiences
   - Collaboration opportunities

10. **appendices/limitations.md**
    - Single subject (n=1)
    - Specific LLM (Claude)
    - Temporal limitations
    - Generalizability concerns

## Technical Setup

### Initial Setup
```bash
# Install MkDocs and Material theme
pip install mkdocs mkdocs-material

# Create mkdocs-site directory
mkdir mkdocs-site
cd mkdocs-site

# Initialize
mkdocs new .

# Copy mkdocs.yml configuration
# Create docs/ directory structure
# Copy/adapt markdown files
```

### Build & Preview
```bash
# Local preview (auto-reload)
mkdocs serve

# Build static site
mkdocs build

# Output is in site/ directory
```

### Deployment Options

**Option 1: GitHub Pages**
- Free hosting
- Custom domain support
- Automatic builds via GitHub Actions
- URL: `https://yourusername.github.io/discovering-ben/`

**Option 2: Netlify**
- Free tier available
- Custom domain
- Preview deployments for PRs
- Better performance

**Option 3: Custom Domain**
- Register `discovering-ben.org`
- Host on Netlify/Vercel/GitHub Pages
- Professional presence

## Privacy & Ethics Checklist

Before publishing:

- [ ] Remove all personally identifying information
- [ ] Obtain explicit consent from Benjamin and family
- [ ] Review conversation excerpts for sensitive content
- [ ] Add privacy policy page
- [ ] Add consent statement
- [ ] Include ethics statement about n=1 research
- [ ] Add disclaimer about medical advice
- [ ] Review with autism community for respectful language
- [ ] Consider cultural sensitivity around autism identity
- [ ] Add content warnings for potentially triggering examples

## Launch Strategy

### Phase 1: Soft Launch
- Share with autism research community
- Share with AI safety community
- Get feedback on presentation
- Iterate on content

### Phase 2: Public Launch
- Announce on social media
- Submit to relevant publications
- Reach out to autism advocacy organizations
- Contact LLM developers (Anthropic, OpenAI, etc.)

### Phase 3: Ongoing
- Add Wave 2 results (intervention effectiveness)
- Community contributions
- Case studies from others
- Updated findings

## Content Maintenance

### Regular Updates
- Add new wave findings as available
- Update intervention effectiveness data
- Incorporate community feedback
- Add new case studies (with consent)

### Version Control
- Keep source files in git repository
- Tag releases corresponding to research waves
- Maintain changelog

## Accessibility Considerations

- Use semantic HTML
- Provide alt text for all images
- Ensure color contrast meets WCAG AA
- Support keyboard navigation
- Provide plain language summaries
- Include content warnings where appropriate
- Offer multiple formats (web, PDF, EPUB?)

## Next Steps

1. **Create mkdocs-site/ directory structure**
2. **Write new essential pages** (overview, methodology additions)
3. **Adapt existing markdown files** for public consumption
4. **Create visual assets** (diagrams, charts)
5. **Set up mkdocs.yml configuration**
6. **Build and test locally**
7. **Get family consent and review**
8. **Privacy review of all content**
9. **Soft launch for feedback**
10. **Public launch**
