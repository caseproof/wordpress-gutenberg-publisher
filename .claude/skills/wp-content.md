---
name: wp-content
description: Generate and publish WordPress content
aliases:
  - /wp-publish
  - /publish-content
---

# WordPress Content Publisher

Generate content using AI templates and publish to WordPress.

## Workflow

1. **Ask content type** (blog post, landing page, documentation, etc.)
2. **Gather requirements** via AskUserQuestion
3. **Generate content** using templates from `prompts/`
4. **Save to `generated/YYYY-MM-DD_type_slug.md`**
5. **Preview and confirm**
6. **Publish to WordPress** via `python3.11 publish.py`

## Content Types

- Blog Post: SEO-optimized articles
- Landing Page (Feature Overview): Grid-style features page
- Landing Page (Deep-Dive): Aspirational single-feature page
- Product Features: Capability showcase
- Documentation: Technical guides with code examples
- Comparison: vs. competitors positioning

## File Storage

Save all generated content to `generated/` directory:
```bash
mkdir -p generated
cat > generated/YYYY-MM-DD_type_slug.md << 'EOF'
[content]
EOF
```

**Never delete generated files** - users may edit and republish.

## Publishing

```bash
python3.11 publish.py generated/file.md --post-type [TYPE] --status [STATUS]
```

Post types: `posts`, `pages`, or custom (e.g., `landing_pages`, `ht_kb`)  
Status: `draft` (recommended) or `publish`

## Templates

Reference templates from:
- `prompts/landing-page-templates.md`
- `prompts/content-generation-prompts.md`
- `examples/*.md`

Generate high-quality, benefit-driven content. Include CTAs and social proof.

## Example Session

```
User: /wp-content
You: Content type? [Show options]
User: Landing Page - Feature Overview
You: [Ask: product name, description, audience, value prop, features]
User: [Provides details]
You: [Generate content, save to generated/]
     Preview: [Show content]
     Publish to WordPress?
User: Yes
You: [Ask: post type, status]
     [Run publish.py]
     ✅ Published! URL + file location
```

## Important

- Use AskUserQuestion for all requirements gathering
- Always preview before publishing
- Default to `draft` status
- Use `python3.11` (not python3) for SSL compatibility
- Check `config.ini` exists before publishing

That's it. Keep it simple.
