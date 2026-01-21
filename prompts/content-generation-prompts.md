# AI Content Generation Prompts

Use these prompts with Claude or ChatGPT to generate markdown content, then publish to WordPress using this tool.

## Blog Post Generator

```
Write a comprehensive blog post in markdown format on: [TOPIC]

Requirements:
- Target audience: [AUDIENCE]
- Tone: [professional/casual/technical]
- Length: [800-1200 / 1500-2000 / 2500-3000 words]
- Include actionable tips, examples, real-world applications

Structure:
1. Compelling H1 title (includes primary keyword)
2. Brief introduction (2-3 paragraphs, hook the reader)
3. 3-5 main sections with H2 headings
4. Subsections with H3 headings where appropriate
5. Bullet points or numbered lists for readability
6. Conclusion with clear call-to-action

SEO Guidelines:
- Primary keyword: [KEYWORD]
- Secondary keywords: [KEYWORD 2, KEYWORD 3]
- Natural keyword density (not stuffing)
- Include link opportunities

Format: Use markdown syntax with [text](url) links
```

## Landing Page Generator

```
Write a high-converting landing page in markdown for: [PRODUCT/SERVICE]

Target Audience: [WHO]
Goal: [ACTION] (sign up, purchase, download, schedule call)

Structure:
# [Compelling Headline - Big Promise]

[Subheadline - who it's for, what they get]

## The Problem
[Pain point - be specific and empathetic]
- [Frustration 1]
- [Frustration 2]
- [Frustration 3]

## The Solution
[Your product/service as the answer]
[Key benefits]

## How It Works
1. [Step 1]
2. [Step 2]
3. [Step 3]

## What You'll Get
- [Feature → Benefit]
- [Feature → Benefit]
- [Feature → Benefit]

## Who This Is For
✅ [Ideal customer 1]
✅ [Ideal customer 2]
❌ Not for you if: [Disqualify wrong-fit]

## Social Proof
[2-3 testimonials or stats]

## Common Questions
**Q: [Objection]**
A: [Reassuring answer]

## Pricing/Offer
[Clear pricing, bonuses, guarantee]

## Call-to-Action
[Strong CTA with urgency if applicable]

Format: Markdown with clear headings and lists
```

## Technical Documentation Generator

```
Write technical documentation in markdown for: [FEATURE/API/TOOL]

Target Audience: [developers/end-users/admins]
Technical Level: [beginner/intermediate/advanced]

Structure:
# [Feature Name]
[One-sentence description]

## Overview
[What it is, why it exists, when to use it]

## Prerequisites
- [Requirement 1]
- [Requirement 2]

## Getting Started
### Installation
```bash
[commands]
```

### Basic Configuration
[Setup example with code]

### Your First [Use Case]
[Step-by-step with code examples]

## Core Concepts
### Concept 1
[Explanation with code example]

### Concept 2
[Explanation with code example]

## Common Use Cases
[Multiple examples with full code]

## Troubleshooting
### Problem: [Issue]
**Symptoms:** [What user sees]
**Solution:** [How to fix]

## Best Practices
- ✅ [Do this]
- ❌ [Don't do this]

Format: Markdown with code blocks in appropriate language
```

## SEO Optimizer

```
Optimize this content for SEO while maintaining readability.

Original Content:
[PASTE CONTENT]

Target Keyword: [PRIMARY]
Secondary Keywords: [KEYWORD 2, KEYWORD 3]

Optimization:
- Include primary keyword in title, first paragraph, 2-3 times in body
- Add secondary keywords naturally
- Create keyword-rich H2/H3 headings
- Add internal link opportunities [INTERNAL LINK: anchor]
- Add external links to authority sources
- Improve readability (short paragraphs, bullets, structure)
- Add FAQ section for featured snippets

Output:
1. SEO title (60 chars max)
2. Meta description (155 chars max)
3. Optimized body
4. FAQ section (3-5 questions)

Maintain natural tone, avoid keyword stuffing.
```

## Publishing Workflow

Once you have markdown content:

```bash
# Save markdown to file
echo "[PASTE CONTENT]" > article.md

# Publish to WordPress
python publish.py article.md

# Or direct mode
python publish.py article.md --status publish --post-type posts
```

## Pro Tips

1. **Iterate on prompts** - Start broad, refine based on output
2. **Provide examples** - Include sample output in prompts
3. **Specify constraints** - Length, tone, structure, keywords
4. **Request options** - "Generate 3 headline options"
5. **Combine prompts** - Generate → Optimize → Social posts
6. **Save good prompts** - Build your prompt library
7. **Test and measure** - Track what performs best

## Example Prompt (Complete)

```
Write a comprehensive blog post in markdown format on:
"How to Choose the Right WordPress Hosting for Your Business"

Requirements:
- Target audience: Small business owners, non-technical
- Tone: Conversational and helpful
- Length: 1500-2000 words
- Include: decision framework, comparison criteria, examples

Structure:
[Use blog post template above]

SEO Guidelines:
- Primary keyword: WordPress hosting
- Secondary: managed WordPress, website performance, hosting providers
- Link to: WordPress.org, reputable hosting reviews

[Complete template structure...]
```

---

**Next Steps:**
1. Choose a prompt template
2. Customize for your needs
3. Generate content with Claude/ChatGPT
4. Save as `.md` file
5. Publish with this tool
6. Analyze and refine

Good prompts = Good content. Take time to craft detailed, specific prompts.
