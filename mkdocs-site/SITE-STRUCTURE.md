# Discovering Ben - Complete Site Structure

## Overview

Production-ready MkDocs configuration for the autism-LLM interaction research website. The site features 40+ pages organized into 8 main sections with comprehensive navigation, accessibility features, and mobile optimization.

## Navigation Hierarchy

### 1. Home
- `index.md` - Landing page

### 2. About This Research (4 pages)
- Research Question (`overview/research-question.md`)
- Key Findings (`overview/key-findings.md`)
- Methodology
  - Overview (`methodology/overview.md`)
  - Data Collection (`methodology/data-collection.md`)
- Understanding Autism (`background/autism-traits.md`)

### 3. Start Here (4 pages)
Audience-specific entry points:
- For Autistic Individuals (`overview/for-autistic-individuals.md`)
- For Researchers (`overview/for-researchers.md`)
- For Clinicians (`overview/for-clinicians.md`)
- For LLM Developers (`overview/for-llm-developers.md`)

### 4. The Vicious Cycles (5 pages)
Pathological patterns with 60-70% LLM contribution:
- Understanding the Patterns (`cycles/overview.md`)
- Cycle 1: Information Overload (`cycles/cycle-1-information-overload.md`)
- Cycle 2: The One Best Thing Paradox (`cycles/cycle-2-one-best-thing.md`)
- Cycle 3: Perfectionism Spiral (`cycles/cycle-3-perfectionism.md`)
- Cycle 4: Emotional Dysregulation (`cycles/cycle-4-emotional-dysregulation.md`)

### 5. Other Patterns (2 pages)
Non-pathological or mild patterns:
- Cycle 5: Mind Reading Expectations (`cycles/cycle-5-mind-reading.md`)
- Cycle 7: Special Interest Engagement (`cycles/cycle-7-special-interests.md`)

### 6. Real-World Examples (4 pages)
Case studies and practical examples:
- Information Overload in Practice (`case-studies/information-overload-example.md`)
- Perfectionism That Worked (`case-studies/perfectionism-spiral-example.md`)
- Successful Intervention (`case-studies/successful-intervention-example.md`)
- When Traits Are Healthy (`case-studies/natural-trait-example.md`)

### 7. Implications & Applications (3 pages)
- For Clinical Practice (`implications/for-clinical-practice.md`)
- For LLM Design (`implications/for-llm-design.md`)
- For Accessibility (`implications/for-accessibility.md`)

### 8. Interventions (2 pages)
- Overview (`interventions/overview.md`)
- System Prompt Approach (`interventions/system-prompt-approach.md`)

### 9. Resources (2 pages)
- Glossary (`resources/glossary.md`)
- Dataset Statistics (`appendices/dataset-statistics.md`)

## Site Configuration Features

### Theme: Material for MkDocs

**Color Scheme:**
- Primary: Indigo
- Accent: Deep Purple
- Light/Dark mode toggle

**Typography:**
- Text: Roboto
- Code: Roboto Mono

**Logo:** Material brain icon

### Navigation Features
- Tabbed navigation (top-level sections)
- Sticky tabs
- Section expansion
- Breadcrumb navigation paths
- Back to top button
- Footer navigation
- Table of contents integration

### Search Features
- Search suggestions
- Result highlighting
- Share search results
- Advanced separator configuration
- English language optimization

### Content Features
- Code copy buttons
- Code annotations
- Tabbed content support
- Tooltips
- Auto-hiding header
- Dismissible announcements

### Markdown Extensions Enabled

**PyMdown Extensions:**
- Arithmatex (mathematical notation)
- Better Emphasis
- Caret, Mark, Tilde (text formatting)
- Critic markup
- Details/Admonitions
- Emoji support
- Syntax highlighting with line numbers
- Inline code highlighting
- Keyboard keys
- Magic links (auto-linking)
- Smart symbols
- Code snippets
- Superfences (including Mermaid diagrams)
- Tabbed content
- Task lists

**Standard Extensions:**
- Abbreviations
- Admonitions
- Attribute lists
- Definition lists
- Footnotes
- Markdown in HTML
- Tables
- Table of Contents with permalinks

### Plugins Configured

1. **Search** - Enhanced with custom separators
2. **Tags** - Content organization (tags file: `resources/tags.md`)
3. **Minify** - HTML/CSS/JS optimization

### Accessibility Features

**Built-in:**
- ARIA landmarks
- Semantic HTML
- Screen reader support
- Keyboard navigation
- Skip links

**Custom (in extra.css):**
- Enhanced focus indicators (2px outline)
- Skip to content links
- Reduced motion support
- High contrast mode support
- Print-optimized styles

### Custom Styling

**extra.css includes:**
- Accessibility enhancements
- Responsive table improvements
- Enhanced admonition styles
- Mermaid diagram styling
- Navigation callout boxes
- Statistics highlighting
- Severity indicators (critical/high/medium/low)
- Audience-specific section styling
- Mobile optimizations
- Print styles
- Glossary term highlighting

### Analytics & Tracking

**Google Analytics:**
- Placeholder property ID (G-XXXXXXXXXX)
- User feedback on page helpfulness
- GDPR-compliant cookie consent

### Social Links
- GitHub repository
- Twitter/X

### Extra JavaScript
- MathJax configuration for mathematical notation
- Polyfill support
- LaTeX rendering

## File Organization

```
mkdocs-site/
├── mkdocs.yml                  # Main configuration (248 lines)
├── requirements.txt            # Python dependencies
├── README.md                   # Repository documentation
├── SETUP.md                    # Installation and usage guide
├── SITE-STRUCTURE.md          # This file
├── .gitignore                 # Git exclusions
│
├── docs/                      # Content directory
│   ├── index.md              # Homepage
│   │
│   ├── overview/             # About section (6 pages)
│   │   ├── research-question.md
│   │   ├── key-findings.md
│   │   ├── for-autistic-individuals.md
│   │   ├── for-researchers.md
│   │   ├── for-clinicians.md
│   │   └── for-llm-developers.md
│   │
│   ├── methodology/          # Research methods (2 pages)
│   │   ├── overview.md
│   │   └── data-collection.md
│   │
│   ├── background/           # Context (1 page)
│   │   └── autism-traits.md
│   │
│   ├── cycles/              # Vicious cycles (7 pages)
│   │   ├── overview.md
│   │   ├── cycle-1-information-overload.md
│   │   ├── cycle-2-one-best-thing.md
│   │   ├── cycle-3-perfectionism.md
│   │   ├── cycle-4-emotional-dysregulation.md
│   │   ├── cycle-5-mind-reading.md
│   │   └── cycle-7-special-interests.md
│   │
│   ├── case-studies/        # Examples (4 pages)
│   │   ├── information-overload-example.md
│   │   ├── perfectionism-spiral-example.md
│   │   ├── successful-intervention-example.md
│   │   └── natural-trait-example.md
│   │
│   ├── implications/        # Applications (3 pages)
│   │   ├── for-clinical-practice.md
│   │   ├── for-llm-design.md
│   │   └── for-accessibility.md
│   │
│   ├── interventions/       # Solutions (2 pages)
│   │   ├── overview.md
│   │   └── system-prompt-approach.md
│   │
│   ├── resources/           # Reference (2 pages)
│   │   ├── glossary.md
│   │   └── tags.md
│   │
│   ├── appendices/          # Data (1 page)
│   │   └── dataset-statistics.md
│   │
│   ├── stylesheets/         # Custom CSS
│   │   └── extra.css
│   │
│   ├── javascripts/         # Custom JS
│   │   └── mathjax.js
│   │
│   └── _planning/           # Planning docs (not in nav)
│       ├── navigation-structure.md
│       ├── mermaid-diagrams.md
│       └── statistical-visualizations.md
│
├── includes/                # Shared content
│   └── abbreviations.md    # Site-wide abbreviations
│
└── overrides/              # Theme customization (empty)
```

## Total Page Count

- **Content Pages:** 40+ markdown files
- **Navigation Sections:** 9 top-level sections
- **Maximum Nesting:** 2 levels (prevents mobile overwhelm)

## Key Design Principles

1. **Progressive Disclosure** - Multiple entry points for different audiences
2. **Mobile-First** - Responsive design with touch-friendly targets
3. **Accessibility-First** - WCAG AA compliance, screen reader support
4. **Performance** - Minified assets, lazy loading, optimized rendering
5. **SEO-Optimized** - Semantic structure, meta descriptions, sitemap
6. **User-Centric** - Clear pathways, breadcrumbs, related content

## Validation & Quality

- **Strict Mode:** Enabled - fails on broken links or missing files
- **YAML Validation:** MkDocs-specific tags properly formatted
- **Link Checking:** All internal links validated
- **Accessibility:** Focus indicators, skip links, ARIA labels

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Start dev server
mkdocs serve

# Build for production
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy

# Strict build (catch errors)
mkdocs build --strict
```

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Screen readers (NVDA, JAWS, VoiceOver)
- Keyboard-only navigation

## Performance Targets

- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Lighthouse Score: 90+
- WAVE Accessibility: 0 errors

## Future Enhancements

Potential additions documented in planning docs:
- Multi-version support (mike plugin)
- Git revision dates
- Blog/news section
- PDF export
- Additional case studies
- Video content integration

---

**Configuration Status:** Production-ready
**Last Updated:** 2024-11-16
**MkDocs Version:** >= 1.5.0
**Material Theme:** >= 9.5.0
