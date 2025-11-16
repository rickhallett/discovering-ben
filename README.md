# Discovering Ben: Autism-LLM Interaction Patterns

Research documenting vicious reinforcement cycles in autism-LLM interactions and system prompt interventions.

## Overview

This research project analyzes 255 conversations between an autistic individual (Ben) and Claude over 26 days, revealing systematic patterns where LLM behavior contributes to and reinforces autistic interaction difficulties. The study identifies 7 distinct interaction patterns, including 4 pathological vicious cycles, and demonstrates that 60-70% of the dysfunction originates from LLM responses rather than user behavior.

The research combines qualitative conversation analysis with systematic cycle detection to understand how current LLM systems inadvertently create reinforcement loops that amplify rather than mitigate autistic communication challenges. Based on these findings, we propose targeted system prompt interventions designed to break these cycles.

## Key Findings

- **255 conversations** analyzed over 26 days (December 2024 - January 2025)
- **7 interaction patterns** identified across technical work, planning, and support contexts
- **4 pathological vicious cycles** creating sustained dysfunction
- **60-70% LLM contribution** to cycle maintenance and amplification
- **System prompt interventions** designed to address each cycle type
- **Quantitative validation** through automated cycle detection pipeline

The research demonstrates that well-intentioned LLM behaviors such as excessive politeness, premature validation, and abstract responses systematically fail to meet autistic communication needs, creating feedback loops that worsen over time.

**Critical insight:** RLHF-optimized compliance creates these problems, not autism alone.

## Website

**Status:** Quality assurance complete, pending technical fixes and family approval

The research will be published as a comprehensive MkDocs website. Currently under development with:

- 40+ pages of analysis, findings, and interventions
- Complete cycle documentation with conversation examples
- System prompt specifications for each intervention
- Methodology and replication guides
- Privacy and ethics documentation

### Building the Website Locally

To preview the website on your machine:

```bash
cd mkdocs-site
pip install -r requirements.txt
mkdocs serve
```

Then visit http://127.0.0.1:8000 in your browser.

### Publishing the Website

**Current Status:** Awaiting completion of:
1. Technical fixes to cycle detection visualization
2. Family review and approval of content
3. Final privacy review
4. License selection

Once approved, the website will be published to GitHub Pages. See `mkdocs-site/docs/guides/publication-process.md` for detailed publication steps.

## Publication Status

### Completed
- Content development (40+ pages)
- Quality assurance review
- Structure and navigation design
- Privacy anonymization
- Ethics documentation

### In Progress
- Technical fixes to cycle detection visualization
- Family content review

### Pending
- Family approval for publication
- Final privacy review
- License selection
- GitHub Pages deployment

## For Family: How to Review and Approve

Your review and approval are essential before this research can be published. Here's how to participate:

### What to Review

1. **Content Accuracy**: Navigate the website to verify all descriptions and examples accurately represent the interactions
2. **Privacy**: Confirm all identifying information has been appropriately anonymized
3. **Tone**: Ensure the research maintains a respectful, clinical tone while being honest about findings
4. **Context**: Verify that examples include sufficient context to be understood correctly

### How to Review

**Option 1: Preview the Website Locally**
```bash
cd mkdocs-site
pip install -r requirements.txt
mkdocs serve
# Visit http://127.0.0.1:8000
```

**Option 2: Read the Source Markdown**
All content is in `mkdocs-site/docs/` as readable markdown files.

**Option 3: Request PDF Export**
Contact the research team to generate a PDF version of the complete website.

### What to Look For

- Are conversation examples presented fairly and in context?
- Is the language respectful and professional?
- Are any personal details or identifiers still visible?
- Do the findings accurately reflect the lived experience?
- Are there sections that should be removed or modified?

### How to Provide Feedback

1. **Major Concerns**: Email or call immediately
2. **Content Changes**: Mark specific pages/sections that need revision
3. **Approval**: Written confirmation once review is complete
4. **Questions**: Schedule a discussion to walk through any concerns

### Key Pages to Review

- `index.md` - Overall framing and introduction
- `cycles/*.md` - Each cycle description and examples
- `methodology/participant-context.md` - Participant background
- `privacy-ethics.md` - Ethics and consent statement

**Your privacy and comfort are the highest priority.** If anything feels inappropriate or uncomfortable, we will revise or remove it.

## For Researchers: How to Replicate

This research can be replicated or extended with your own conversation datasets.

### Prerequisites

- Python 3.8+
- Access to conversation data in a structured format
- Basic familiarity with qualitative coding methods

### Replication Steps

1. **Review Methodology**
   - Read `mkdocs-site/docs/methodology/` for research approach
   - Study cycle definitions in `analysis/wave-1-vicious-cycles/cycles/`
   - Understand detection criteria in `analysis/analysis_pipeline/`

2. **Prepare Your Data**
   - Format conversations with timestamps, speaker labels, message content
   - Anonymize any identifying information
   - Structure into analyzable units (conversations or sessions)

3. **Run Cycle Detection**
   ```bash
   cd analysis/analysis_pipeline/cycle-detection-engine
   python detect_cycles.py --input your_conversations/ --output results/
   ```

4. **Analyze Results**
   - Review detected cycle instances
   - Validate against qualitative assessment
   - Calculate contribution percentages
   - Identify intervention points

5. **Design Interventions**
   - Use templates in `system-prompts/interventions/`
   - Test with validation framework in `system-prompts/testing/`
   - Document effectiveness measures

### Research Questions to Explore

- Do these cycles appear with different LLMs (GPT-4, Gemini, etc.)?
- How do cycle patterns vary across different neurodivergent profiles?
- What user behaviors most reliably trigger specific cycles?
- Which interventions are most effective for breaking cycles?
- How do cycles manifest in different task domains (coding, writing, support)?

### Citation

If you use this methodology or build on these findings, please cite:

```
[Citation format TBD - pending publication and license decision]
```

## For Contributors: How to Help

We welcome contributions that improve the research, methodology, or website.

### Ways to Contribute

1. **Methodology Improvements**
   - Enhanced cycle detection algorithms
   - Additional quantitative validation approaches
   - Statistical analysis frameworks

2. **Intervention Development**
   - Testing proposed system prompts
   - Designing new intervention strategies
   - Measuring intervention effectiveness

3. **Website Enhancements**
   - Improved visualizations
   - Better navigation structures
   - Accessibility improvements

4. **Documentation**
   - Clearer replication guides
   - Additional code examples
   - Translation to other languages

### Contribution Process

1. **Discuss First**: Open an issue describing your proposed contribution
2. **Respect Privacy**: Never commit conversation data or identifying information
3. **Test Thoroughly**: Ensure all code changes work with the existing pipeline
4. **Document**: Update relevant documentation for any methodology changes
5. **Submit**: Create a pull request with clear description of changes

### Code of Conduct

This research involves sensitive personal data. All contributors must:

- Respect participant privacy absolutely
- Maintain professional, clinical tone in all analysis
- Avoid sensationalism or stigmatizing language
- Prioritize autistic community perspectives
- Follow all ethics protocols

## Repository Structure

```
discovering-ben/
├── analysis/                           # Research analysis and findings
│   ├── wave-1-vicious-cycles/          # Cycle detection and analysis
│   │   ├── cycles/                     # Individual cycle definitions
│   │   ├── conversations/              # Analyzed conversation data
│   │   └── detection-results/          # Automated detection output
│   └── analysis_pipeline/              # Detection methodology
│       ├── cycle-detection-engine/     # Core detection algorithms
│       └── visualization/              # Result visualization tools
│
├── system-prompts/                     # Intervention designs
│   ├── interventions/                  # Cycle-specific prompts
│   ├── testing/                        # Validation frameworks
│   └── implementation-guides/          # Deployment documentation
│
├── mkdocs-site/                        # Website source
│   ├── docs/                           # Content (40+ pages)
│   │   ├── cycles/                     # Cycle documentation
│   │   ├── interventions/              # System prompt specs
│   │   ├── methodology/                # Research approach
│   │   └── guides/                     # User guides
│   ├── mkdocs.yml                      # Site configuration
│   ├── requirements.txt                # Python dependencies
│   └── custom_theme/                   # Theme customizations
│
├── docs/                               # Project documentation
│   ├── guides/                         # Planning and process docs
│   └── background/                     # Research context
│
├── data/                               # Datasets (not in repo)
│   └── 255 conversations, 5,338 messages, 26 days, 89.5MB
│
└── README.md                           # This file
```

## Privacy and Ethics

### Informed Consent

This research was conducted with full informed consent from the primary participant. The participant:

- Understands the research purpose and methodology
- Has reviewed all conversation examples used in the study
- Retains the right to request removal of specific content
- Will provide final approval before public release
- Can withdraw consent at any time

### Anonymization

All conversation data has been anonymized to remove:

- Personal names and identifiers
- Specific locations, organizations, institutions
- Dates (replaced with relative timeframes)
- Technical details that could identify individuals
- Any other potentially identifying information

### Data Protection

- Original conversation data is stored securely and not included in this repository
- Only anonymized examples appear in published materials
- Access to raw data is restricted to approved researchers
- All data handling follows research ethics protocols

### Ethical Considerations

This research aims to improve LLM systems for autistic users, not to pathologize autism or the participant. The analysis focuses on system behavior and interaction patterns, not on diagnosing or evaluating the individual.

The findings are presented to:
- Inform LLM system design improvements
- Help autistic users understand interaction patterns
- Guide development of better support tools
- Contribute to neurodiversity-aware AI research

### Community Review

Before publication, this research will be reviewed by:
- The primary participant and their family
- Autism community advocates
- Ethics review board
- Privacy and data protection specialists

## License

**Status:** To be determined pending family decision

Licensing options under consideration:

1. **Creative Commons Attribution 4.0 (CC BY 4.0)**
   - Allows reuse with attribution
   - Permits commercial use
   - Requires credit to original research

2. **Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)**
   - Allows reuse with attribution
   - Prohibits commercial use
   - Permits academic and research applications

3. **Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)**
   - Allows reuse with attribution
   - Requires derivatives use same license
   - Encourages open research ecosystem

The license will be finalized before publication and clearly indicated in all materials.

## Contact

For questions about this research:

- **Technical Questions**: [Contact information TBD]
- **Ethics Concerns**: [Contact information TBD]
- **Replication Support**: [Contact information TBD]
- **Family Review**: [Contact information TBD]

## Acknowledgments

This research would not be possible without:

- The primary participant's willingness to share their experiences
- Family support throughout the research process
- The autism community's ongoing advocacy for better AI systems
- Claude (Anthropic) as both research subject and analysis tool

## Version History

- **Current**: Website development complete, pending family approval
- **January 2025**: Quality assurance review completed
- **December 2024 - January 2025**: Initial research and analysis
- **December 2024**: Project inception

---

**This research is a work in progress. All content is subject to revision based on family review, community feedback, and ongoing analysis.**
