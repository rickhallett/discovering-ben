# Navigation Structure Plan

## Overview

This navigation structure is designed around the principle of **progressive disclosure through multiple audience pathways**. Rather than forcing a single linear journey, the structure provides clear entry points for different stakeholder groups while maintaining logical relationships between content areas.

**Design Philosophy:**

- **Multiple entry points**: Different audiences start at different places based on their needs
- **Progressive complexity**: Surface-level overviews lead to detailed case studies and implications
- **Audience-first wayfinding**: "For [Audience]" pages serve as gateway hubs
- **Cross-linking strategy**: Related content suggestions guide users through relevant pathways
- **Mobile-first hierarchy**: Collapsible sections prevent overwhelming mobile users
- **Accessibility prioritized**: Clear structure supports screen readers and keyboard navigation

## Primary Navigation (Top Level)

```yaml
nav:
  - Home: index.md

  - About This Research:
      - Research Question: overview/research-question.md
      - Key Findings: overview/key-findings.md
      - Methodology: methodology/overview.md

  - Start Here:
      - For Autistic Individuals: overview/for-autistic-individuals.md
      - For Researchers: overview/for-researchers.md
      - For Clinicians: overview/for-clinicians.md
      - For LLM Developers: overview/for-llm-developers.md

  - The Vicious Cycles:
      - Understanding the Patterns: cycles/overview.md
      - Cycle 1 - Information Overload: cycles/information-overload.md
      - Cycle 2 - Decision Paralysis: cycles/decision-paralysis.md
      - Cycle 3 - Perfectionism Spiral: cycles/perfectionism-spiral.md
      - Cycle 4 - Emotional Dysregulation: cycles/emotional-dysregulation.md

  - Real-World Examples:
      - Case Studies Overview: case-studies/index.md
      - Information Overload in Practice: case-studies/information-overload-example.md
      - Decision Paralysis Impact: case-studies/decision-paralysis-example.md
      - Perfectionism That Worked: case-studies/perfectionism-spiral-example.md
      - Successful Intervention: case-studies/successful-intervention-example.md
      - When Traits Are Healthy: case-studies/natural-trait-example.md

  - Implications & Applications:
      - For Clinical Practice: implications/for-clinical-practice.md
      - For LLM Design: implications/for-llm-design.md
      - For Accessibility: implications/for-accessibility.md

  - Resources:
      - Glossary: resources/glossary.md
```

**Rationale for Top-Level Structure:**

1. **Home**: Single clear landing page
2. **About This Research**: Establishes credibility and context before deep content
3. **Start Here**: Explicit audience segmentation - users self-select their pathway
4. **The Vicious Cycles**: Core research findings, progressively detailed
5. **Real-World Examples**: Concrete instantiation of abstract patterns
6. **Implications & Applications**: Actionable takeaways for different stakeholders
7. **Resources**: Reference material accessible from any point

## User Journey Pathways

### Journey 1: Autistic Individual Using AI

**Goal**: Understand if their AI struggles are interaction failures vs. personal failures, get practical help

**Pathway:**
```
Home
  → For Autistic Individuals
    → Quick Self-Assessment (which cycles affect you?)
      → Specific Cycle Deep Dive (e.g., Information Overload)
        → Case Study (see real example)
          → Practical Interventions (custom prompts, techniques)
```

**Key Features:**
- Immediate validation ("You're not broken")
- Self-assessment checklist on landing page
- Practical action items prioritized over theory
- Custom prompt templates ready to copy/paste

**Cross-links to emphasize:**
- From "For Autistic Individuals" → link each cycle mentioned in self-assessment
- From each cycle page → link to relevant case study
- From case studies → link to "What Actually Helps" sections
- Sidebar: "Quick Links" box with custom prompt templates

### Journey 2: Researcher

**Goal**: Evaluate methodology rigor, understand findings validity, assess generalizability

**Pathway:**
```
Home
  → For Researchers
    → Research Question (theoretical framework)
      → Methodology (two-stage detection explained)
        → Key Findings (quantitative results)
          → Specific Cycle Analysis
            → Case Studies (qualitative validation)
              → Implications for Future Research
```

**Key Features:**
- Methodology transparency emphasized upfront
- Statistical rigor highlighted (sample sizes, effect sizes, LLM contribution %)
- Clear limitations acknowledgment
- Reproducibility documentation

**Cross-links to emphasize:**
- From "For Researchers" → direct links to Methodology and Key Findings
- From Methodology → link to each cycle's detection approach
- From Key Findings → link to supporting case studies
- Sidebar: "Research Artifacts" box (dataset info, analysis tools)

### Journey 3: Clinician

**Goal**: Assess clinical relevance, identify assessment criteria, understand intervention strategies

**Pathway:**
```
Home
  → For Clinicians
    → Understanding the 4 Pathological Cycles
      → Clinical Presentation (what you'll observe)
        → Case Studies (real-world manifestation)
          → Clinical Implications
            → Assessment Criteria
              → Intervention Recommendations
```

**Key Features:**
- Clinical presentation language (symptoms, severity, outcomes)
- DSM-adjacent framing where appropriate
- Clear distinction: pathological cycles vs. natural autism traits
- Evidence-based intervention guidance

**Cross-links to emphasize:**
- From "For Clinicians" → link to each pathological cycle
- From cycle pages → link to clinical implications
- From case studies → highlight clinical markers
- Sidebar: "Clinical Quick Reference" (severity scales, intervention checklist)

### Journey 4: LLM Developer / AI Safety Researcher

**Goal**: Understand technical failure modes, identify design improvements, assess RLHF implications

**Pathway:**
```
Home
  → For LLM Developers
    → The 60-70% LLM Contribution Finding
      → Specific Response Patterns Creating Harm
        → Cycle Technical Analysis
          → Case Studies (failure mode examples)
            → Design Implications
              → System Prompt Interventions
                → Testing & Validation Approaches
```

**Key Features:**
- Technical language (RLHF, over-provision, unbounded compliance)
- Specific AI behaviors quantified
- Concrete system prompt modifications
- Comparison: bounded vs. unbounded helpfulness

**Cross-links to emphasize:**
- From "For LLM Developers" → link to technical cycle mechanics
- From cycle pages → emphasize LLM contribution percentage
- From implications → link to specific prompt engineering solutions
- Sidebar: "Implementation Resources" (system prompt templates, detection heuristics)

## Cross-Linking Strategy

### Hub Pages (High Link Density)

**For [Audience] Pages:**
- Act as navigation hubs for each user type
- Link to 5-8 most relevant content pages
- Include "recommended reading order" guidance
- Provide "quick start" vs. "comprehensive" pathways

**Key Findings Page:**
- Links to all 4 pathological cycles
- Links to supporting case studies
- Links to methodology validation
- Links to implications sections

**Glossary:**
- Linked from every technical term mention across site
- Uses anchor links (#term-name) for direct access
- Bidirectional: glossary links back to pages using each term

### Content Pages (Moderate Link Density)

**Cycle Analysis Pages:**
- Link to relevant case study
- Link to implications for that specific cycle
- Link to glossary terms
- "Related Cycles" section (e.g., Information Overload often co-occurs with Decision Paralysis)

**Case Study Pages:**
- Link to the cycle it exemplifies
- Link to intervention strategies
- Link to implications
- "See Also" section for related examples

**Implications Pages:**
- Link back to supporting cycles
- Link to methodology for evidence basis
- Link to glossary for technical terms
- "Further Reading" section

### Inline Linking Principles

1. **First Mention Rule**: First mention of a cycle name links to full cycle page
2. **Technical Terms**: All glossary terms hyperlinked on first use per page
3. **Evidence Claims**: Quantitative findings link to methodology
4. **Practical Guidance**: Action items link to detailed intervention pages
5. **No Dead Ends**: Every page has 3+ navigation options beyond top nav

## Breadcrumbs & Wayfinding

### Breadcrumb Structure

```
Home > Start Here > For Autistic Individuals > Information Overload Cycle
```

**Implementation:**
- Auto-generated from nav hierarchy
- Shows current location context
- Each level clickable
- Mobile: Abbreviated to "< Back" on narrow screens

### "You Are Here" Indicators

**Active Section Highlighting:**
- Top nav highlights active top-level section
- Sidebar highlights active page
- Mobile hamburger menu shows current location before expanding

**Progress Indicators (for multi-page journeys):**
- Example: Reading all 4 cycle pages
  - "Reading: Cycle 2 of 4"
  - Next/Previous cycle buttons at bottom

**Contextual Navigation Boxes:**

Example on case study pages:
```markdown
**About This Example**
- Demonstrates: [Perfectionism Spiral Cycle]
- Severity: Resolved successfully
- Key Learning: Bounded compliance prevents endless iteration
- Related: [Other perfectionism examples]
```

Example on cycle pages:
```markdown
**Quick Navigation**
- Real Example: [Case Study Link]
- Clinical View: [Clinical Implications]
- Technical Analysis: [LLM Design Implications]
- Practical Help: [For Autistic Individuals - this cycle section]
```

## Search Optimization

### Taxonomy Structure

**Primary Categories:**
1. Research Foundation (methodology, questions, findings)
2. Cycle Patterns (the 4 pathological cycles)
3. Real-World Examples (case studies)
4. Implications (clinical, design, accessibility)
5. Audience-Specific Guides
6. Reference Material (glossary)

**Tags (for filtering/search):**
- By Audience: `autistic-users`, `researchers`, `clinicians`, `developers`
- By Cycle: `information-overload`, `decision-paralysis`, `perfectionism`, `emotional-dysregulation`
- By Content Type: `case-study`, `methodology`, `intervention`, `technical-analysis`
- By Severity: `pathological-cycle`, `mild-cycle`, `natural-trait`

### Search Keywords (metadata)

**For Autistic Individuals page:**
- Keywords: AI struggles, LLM difficulties, autism AI interaction, feeling broken, AI overwhelming, decision paralysis autistic, custom prompts autism
- Description: "If you use AI assistants and feel overwhelmed, unable to decide, or stuck in endless loops - you're not broken. These are interaction failures, not personal failures."

**For Researchers page:**
- Keywords: autism LLM interaction study, n=1 longitudinal research, vicious reinforcement cycles, RLHF alignment issues, neurodivergent AI safety
- Description: "Rigorous two-stage methodology analyzing 255 conversations reveals LLM response patterns contribute 60-70% to pathological interaction cycles."

**Cycle Pages:**
- Information Overload: satisfaction paradox, executive dysfunction, filter failure, cognitive overload
- Decision Paralysis: option overload, binary thinking, executive dysfunction, 92% abandonment
- Perfectionism Spiral: impossible standards, unbounded compliance, lateral iteration, 72% incomplete
- Emotional Dysregulation: baseline return failure, sensitization, task-focused compliance

### Search Result Snippets

Optimized page descriptions for search results:

**Home:**
"16-month study analyzing 255 AI conversations reveals how LLM helpfulness creates systematic harm for autistic users. Four vicious cycles identified where AI contributes 60-70% of dysfunction."

**Methodology:**
"Two-stage detection combining regex pattern mining and LLM semantic analysis. Transparent, reproducible approach for analyzing human-AI interaction at scale with qualitative depth."

**For Autistic Individuals:**
"You're not broken. Research proves 60-70% of AI interaction problems come from AI response patterns, not your autism. Practical custom prompts and techniques that actually help."

## Mobile Considerations

### Hamburger Menu Behavior

**Collapsed by Default:**
- Top-level sections visible
- Sub-sections expand on tap
- Current location pre-expanded
- "Close Menu" overlay click

**Touch Targets:**
- Minimum 48x48px tap areas
- Adequate spacing between links
- Swipe-friendly (no accidental taps)

### Collapsible Sections

**Long Pages (e.g., For Autistic Individuals):**
- Each cycle section collapsible
- "Expand All" / "Collapse All" toggle
- Smooth scroll to section headers
- Anchor links work with collapsed state

**Table of Contents:**
- Sticky TOC on desktop
- Mobile: Collapsible drawer at top
- Jump links for long-form content

### Mobile Navigation Priorities

**Reduce Cognitive Load:**
1. Show current location clearly
2. Limit visible options (progressive disclosure)
3. "Back to [Parent Section]" link always visible
4. Search bar prominent for direct navigation

**Content Adaptation:**
- Tables become vertically stacked cards
- Multi-column layouts stack to single column
- Navigation boxes become accordion sections
- Breadcrumbs abbreviate to "< Previous"

### Performance

**Lazy Loading:**
- Images load on scroll
- External links prefetch on hover (desktop)
- Search index loads progressively

**Minimal Assets:**
- Inline critical CSS
- Defer non-critical JavaScript
- Optimize navigation menu rendering

## Accessibility Navigation

### Skip Links

**Primary Skip Links (visible on keyboard focus):**
```html
<a href="#main-content">Skip to main content</a>
<a href="#nav-menu">Skip to navigation</a>
<a href="#search">Skip to search</a>
```

**Contextual Skip Links:**
- Skip to next section
- Skip to case study
- Skip to practical recommendations

### Keyboard Navigation

**Tab Order:**
1. Skip links
2. Search bar
3. Top navigation (left to right)
4. Main content links (document order)
5. Sidebar links
6. Footer links

**Keyboard Shortcuts:**
- `?` → Show keyboard shortcuts help
- `/` → Focus search
- `n` → Next page in sequence
- `p` → Previous page in sequence
- `h` → Return home

**Focus Management:**
- Visible focus indicators (2px outline)
- Focus trap in modal dialogs
- Skip redundant links in nav
- Logical tab order through collapsed sections

### Screen Reader Announcements

**Page Load:**
```
"Discovering Benjamin - [Page Title]. Main navigation: 7 sections. Page content: [brief description]."
```

**Navigation Changes:**
```
"Navigated to [Page Name]. Section: [Top-level section]. [Quick context]."
```

**Expandable Sections:**
```
"[Section Name] expanded. [N] subsections available."
```

### ARIA Landmarks

**Structural Markup:**
```html
<header role="banner">
  <nav role="navigation" aria-label="Main navigation">
<main role="main" id="main-content">
<aside role="complementary" aria-label="Related resources">
<footer role="contentinfo">
```

**Navigation Regions:**
```html
<nav aria-label="Breadcrumb" role="navigation">
<nav aria-label="Table of contents" role="navigation">
<nav aria-label="Related pages" role="navigation">
```

### Screen Reader Optimizations

**Link Text:**
- Descriptive text (not "click here")
- Context included ("Read case study: Perfectionism Spiral")
- Distinguish duplicate link text with aria-label

**Heading Hierarchy:**
- Logical nesting (h1 → h2 → h3)
- No skipped levels
- Descriptive headings for navigation

**Alternative Text:**
- Diagrams: Detailed alt text describing structure
- Decorative images: `alt=""`
- Complex visuals: Long description linked

**Tables:**
- Header rows marked with `<th scope="col">`
- Caption explains table purpose
- Summary attribute for complex tables

## Implementation Notes

### MkDocs Configuration

**Navigation YAML:**
- Explicit nav structure (don't rely on auto-generation)
- Subsection nesting max 2 levels deep (prevents mobile overwhelm)
- Descriptive titles (not filename echoes)

**Plugins:**
- `mkdocs-material` theme for mobile-responsive nav
- `mkdocs-awesome-pages-plugin` for page metadata
- `mkdocs-section-index` for section overview pages
- `mkdocs-glightbox` for accessible image zoom
- Search plugin configured for semantic ranking

**Theme Customization:**
- Custom CSS for focus indicators
- Enhanced mobile breakpoints
- Collapsible TOC configuration
- Skip link styling

### Navigation Testing Checklist

**Functional Testing:**
- [ ] All links resolve correctly
- [ ] No orphaned pages (unreachable from nav)
- [ ] Breadcrumbs accurate on all pages
- [ ] Mobile hamburger menu functions
- [ ] Search returns relevant results
- [ ] Keyboard navigation works without mouse

**Accessibility Testing:**
- [ ] Screen reader announces page changes correctly
- [ ] Focus order logical
- [ ] Skip links function
- [ ] ARIA landmarks correct
- [ ] Heading hierarchy valid
- [ ] Color contrast meets WCAG AA

**User Journey Testing:**
- [ ] Each audience pathway navigable
- [ ] Cross-links appropriate and helpful
- [ ] No dead ends (always 3+ nav options)
- [ ] Related content suggestions relevant
- [ ] Progressive disclosure coherent

**Mobile Testing:**
- [ ] Nav usable on 320px width
- [ ] Touch targets adequate size
- [ ] Collapsible sections function
- [ ] No horizontal scroll
- [ ] Performance acceptable (<3s page load)

## Metrics for Success

**Navigation Effectiveness:**
- Average pages per session (target: 3-5)
- Bounce rate by entry page
- Most common user pathways
- Search query patterns
- Exit pages (identify dead ends)

**Accessibility Metrics:**
- Keyboard-only navigation completion rate
- Screen reader user session duration
- Skip link usage rate
- WAVE accessibility score (target: 0 errors)

**Mobile Performance:**
- Mobile bounce rate (<40%)
- Average mobile session duration
- Mobile search usage rate
- Hamburger menu interaction rate

---

**Document Status:** Complete navigation plan
**Next Steps:**
1. Implement navigation structure in mkdocs.yml
2. Add cross-links to content pages
3. Configure search optimization
4. Test with target audiences
5. Iterate based on analytics

**Related Planning Documents:**
- Content inventory (separate doc)
- Style guide (separate doc)
- Accessibility compliance checklist (separate doc)
