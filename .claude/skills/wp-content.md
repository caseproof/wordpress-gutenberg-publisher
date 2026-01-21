---
name: wp-content
description: Generate and publish content to WordPress (blog posts, landing pages, product features)
aliases:
  - /wp-publish
  - /publish-content
---

# WordPress Content Publisher

You are helping the user create content and publish it to WordPress.

## Your Capabilities

You have access to:
- Content generation templates in `prompts/landing-page-templates.md` and `prompts/content-generation-prompts.md`
- Example content in `examples/` directory
- WordPress publishing tool at `publish.py`
- AskUserQuestion tool for gathering requirements
- Bash tool for running the publish script

## Workflow

When this skill is invoked, follow this workflow:

### Step 1: Ask What Type of Content

Use AskUserQuestion to ask what they want to create:
- Blog Post (SEO-optimized article)
- Landing Page - Feature Overview (grid-style features page)
- Landing Page - Product Deep-Dive (aspirational single-feature page)  
- Product Features Page (showcase capabilities)
- Documentation (technical how-to guide)
- Comparison Page (vs. competitors)

### Step 2: Gather Requirements

Based on their selection, ask follow-up questions:

**For Blog Posts:**
- Topic/title
- Target audience
- Primary keyword
- Tone (professional/casual/technical)
- Length preference

**For Landing Pages:**
- Product/service name
- Brief description (what it does)
- Target audience
- Main value proposition
- Key features (3-6 main features)
- Do they have testimonials/social proof?

**For Documentation:**
- Feature/API/tool name
- Target audience (developers/end-users/admins)
- Technical level
- Prerequisites

### Step 3: Generate Content

Based on the requirements:
1. Read the appropriate template from `prompts/` directory
2. Generate high-quality markdown content following the template structure
3. Ensure the content includes:
   - Compelling headlines with keywords
   - Benefit-driven copy (not just features)
   - Clear structure with H2/H3 headings
   - Bullet points for readability
   - CTAs (calls-to-action)
   - Social proof if provided
4. Use proper markdown formatting with links

### Step 4: Show Preview

Display the generated content to the user and ask:
"Here's your [content type]. Would you like me to:
- Publish it to WordPress?
- Make any changes first?
- Cancel?"

If they want changes, iterate on the content.

### Step 5: Publish to WordPress

If they approve:

1. Ask publishing options using AskUserQuestion:
   - Post type (posts/pages/custom post type)
   - Status (draft recommended, or publish)
   - Custom slug (optional)

2. Save the markdown content to a temporary file:
   ```bash
   cat > wp_content_TIMESTAMP.md << 'EOF'
   [content here]
   EOF
   ```

3. Run the publishing tool:
   ```bash
   python3.11 publish.py wp_content_TIMESTAMP.md --post-type [TYPE] --status [STATUS]
   ```

4. Show the success message with the WordPress URL

5. Clean up the temporary file:
   ```bash
   rm wp_content_TIMESTAMP.md
   ```

## Important Notes

- **Always use AskUserQuestion** for gathering requirements - don't make assumptions
- **Always show a preview** before publishing - let them review
- **Always publish as draft first** unless they specifically request publish status
- **Use the templates** from `prompts/` directory as your guide
- **Check config.ini exists** - if not, tell them to create it from config.example.ini
- **Use python3.11** for publishing (not python3 or python) for SSL compatibility

## Example Session

```
User: /wp-publish
You: I'll help you create and publish content to WordPress! What type of content would you like to create?
[Present options using AskUserQuestion]

User: [Selects "Landing Page - Feature Overview"]
You: Great! Let's create a feature overview landing page. I need some details...
[Ask for product name, description, audience, value prop, features]

User: [Provides details]
You: Perfect! I'm generating your landing page now...
[Generate content using template]

You: Here's your landing page:

# [Generated Title]
[Full content preview...]

Would you like me to:
- Publish this to WordPress?
- Make changes first?
- Cancel?

User: Publish it
You: Great! A few publishing options...
[Ask for post type, status, slug]

User: [Selects options]
You: Publishing to WordPress...
[Run publish.py]

You: ✅ Published successfully!
URL: https://yoursite.com/?p=123
Status: draft

You can now edit it in WordPress and publish when ready!
```

## Template Reference

Refer to these files for content structure:
- `prompts/landing-page-templates.md` - 3 landing page styles
- `prompts/content-generation-prompts.md` - Blog post and doc templates
- `examples/feature-overview-landing-page.md` - Complete example
- `examples/product-feature-deep-dive.md` - Complete example
- `examples/simple-blog-post.md` - Complete example

## Error Handling

If publishing fails:
- Check if `config.ini` exists
- Verify WordPress credentials are correct
- Check the site URL format (no trailing slash)
- For custom post types, verify REST API support is enabled

Common errors:
- 401: Wrong username/password
- 404: Wrong site URL or post type doesn't exist
- SSL error: Need to use python3.11 instead of python3

## Success Criteria

A successful session should:
1. ✅ Ask clarifying questions
2. ✅ Generate high-quality content
3. ✅ Show preview before publishing
4. ✅ Publish successfully to WordPress
5. ✅ Provide the WordPress URL
6. ✅ Clean up temporary files

Make the experience smooth, professional, and helpful!
