# Quick Start Guide

## Installation (30 seconds)

```bash
cd mkdocs-site
pip install -r requirements.txt
```

## Run Development Server (5 seconds)

```bash
mkdocs serve
```

Visit: `http://127.0.0.1:8000`

## Build for Production

```bash
mkdocs build
```

Output: `site/` directory

## Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

## Project Stats

- **Total Pages:** 32 content pages + 1 home
- **Navigation Sections:** 9 top-level
- **Languages:** Markdown, YAML, CSS, JavaScript
- **Theme:** Material for MkDocs
- **Status:** Production-ready

## Key Files

| File | Purpose |
|------|---------|
| `mkdocs.yml` | Main configuration (259 lines) |
| `requirements.txt` | Python dependencies |
| `docs/index.md` | Homepage |
| `docs/stylesheets/extra.css` | Custom styling |
| `includes/abbreviations.md` | Site-wide abbreviations |

## Navigation Structure

```
Home
├── About This Research (7 pages)
├── Start Here (4 pages - audience-specific)
├── The Vicious Cycles (5 pages)
├── Other Patterns (2 pages)
├── Real-World Examples (4 pages)
├── Implications & Applications (3 pages)
├── Interventions (2 pages)
└── Resources (3 pages)
```

## Features Enabled

- Light/dark mode toggle
- Mermaid diagrams
- Code syntax highlighting
- Search with suggestions
- Mobile-responsive
- Accessibility optimized
- GDPR cookie consent
- Google Analytics ready
- Social links (GitHub, Twitter)

## Common Commands

```bash
# Development
mkdocs serve              # Start dev server
mkdocs serve --strict     # Strict mode (catch errors)

# Building
mkdocs build              # Build static site
mkdocs build --strict     # Build with validation

# Deployment
mkdocs gh-deploy          # Deploy to GitHub Pages
```

## Customization Quick Tips

### Change Colors
Edit `mkdocs.yml` line 23-24:
```yaml
primary: indigo      # Change to: red, blue, green, etc.
accent: deep purple  # Change to: orange, pink, etc.
```

### Add Google Analytics
Edit `mkdocs.yml` line 152:
```yaml
property: G-XXXXXXXXXX  # Replace with your tracking ID
```

### Add New Page
1. Create markdown file: `docs/section/page.md`
2. Add to `mkdocs.yml` nav section:
   ```yaml
   - Section Name:
       - Page Title: section/page.md
   ```

## Troubleshooting

**Issue:** Port 8000 already in use
**Fix:** `mkdocs serve -a localhost:8001`

**Issue:** Plugin not found
**Fix:** `pip install mkdocs-[plugin-name]-plugin`

**Issue:** Broken links
**Fix:** Run `mkdocs build --strict` to find them

## Support Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material Theme Docs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)

## Next Steps

1. Review content in `docs/` directory
2. Customize theme colors in `mkdocs.yml`
3. Add Google Analytics ID
4. Update social links
5. Test locally with `mkdocs serve`
6. Build with `mkdocs build --strict`
7. Deploy with `mkdocs gh-deploy`

---

For detailed information, see:
- `SETUP.md` - Complete setup guide
- `README.md` - Project overview
- `SITE-STRUCTURE.md` - Full site architecture
