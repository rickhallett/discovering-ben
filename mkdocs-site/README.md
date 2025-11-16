# Discovering Ben - MkDocs Site

This directory contains the MkDocs configuration and content for the "Discovering Ben: Autism-LLM Interaction Patterns" research website.

## Structure

```
mkdocs-site/
├── mkdocs.yml              # Main MkDocs configuration
├── docs/                   # Content directory
│   ├── index.md           # Homepage
│   ├── overview/          # About the research
│   ├── cycles/            # The vicious cycles
│   ├── case-studies/      # Real-world examples
│   ├── implications/      # Applications
│   ├── methodology/       # Research methods
│   ├── resources/         # Glossary and references
│   ├── stylesheets/       # Custom CSS
│   └── javascripts/       # Custom JavaScript
├── includes/              # Shared content snippets
└── overrides/             # Theme customization
```

## Requirements

Install dependencies:

```bash
pip install mkdocs-material
pip install mkdocs-minify-plugin
pip install mkdocs-git-revision-date-localized-plugin
```

## Development

Start the development server:

```bash
cd mkdocs-site
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000`

## Building

Build the static site:

```bash
mkdocs build
```

The built site will be in the `site/` directory.

## Configuration Highlights

### Theme Features

- Material Design theme with dark/light mode toggle
- Responsive navigation with tabs and sections
- Search with suggestions and highlighting
- Code copy buttons and syntax highlighting
- Mobile-optimized with collapsible sections

### Markdown Extensions

- **Mermaid diagrams** for flowcharts and visualizations
- **Admonitions** for callouts and notes
- **Tables** with responsive overflow
- **Code highlighting** with line numbers
- **Footnotes** for references
- **Tabbed content** for organizing information

### Accessibility Features

- WCAG AA compliant color contrast
- Keyboard navigation support
- Screen reader optimized
- Skip links for main content
- Reduced motion support
- High contrast mode support

### Plugins

- **Search**: Enhanced search with language support
- **Tags**: Content organization and filtering
- **Minify**: Optimized HTML/CSS/JS output

## Navigation Structure

The site uses a progressive disclosure model with multiple audience pathways:

1. **Home** - Landing page
2. **About This Research** - Research context
3. **Start Here** - Audience-specific entry points
4. **The Vicious Cycles** - Core pathological patterns
5. **Other Patterns** - Non-pathological patterns
6. **Real-World Examples** - Case studies
7. **Implications & Applications** - Practical takeaways
8. **Resources** - Glossary and references

## Customization

### Custom CSS

Edit `docs/stylesheets/extra.css` for style customizations including:
- Focus indicators for accessibility
- Severity level indicators
- Audience-specific styling
- Mobile optimizations

### Custom JavaScript

Edit `docs/javascripts/mathjax.js` for mathematical notation support.

### Abbreviations

Common abbreviations are defined in `includes/abbreviations.md` and automatically expanded throughout the site.

## Analytics

Update the Google Analytics property ID in `mkdocs.yml`:

```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX  # Replace with your tracking ID
```

## Deployment

The site can be deployed to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

For GitHub Pages:

```bash
mkdocs gh-deploy
```

## License

See main repository LICENSE file.

## Support

For questions or issues, please open an issue in the main repository.
