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

## Content Storage

**IMPORTANT:** All generated content must be saved to the `generated/` directory with descriptive filenames.

**Filename format:**
- `generated/YYYY-MM-DD_content-type_slug.md`
- Example: `generated/2024-01-21_landing-page_taskflow-features.md`
- Example: `generated/2024-01-21_blog-post_wordpress-security.md`

**Do NOT delete generated files** - users may want to:
- Edit them later
- Republish updated versions
- Keep a record of what was published
- Use as templates for future content

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

### Step 4: Save to File

1. Create `generated/` directory if it doesn't exist:
   ```bash
   mkdir -p generated
   ```

2. Create a descriptive filename based on:
   - Current date (YYYY-MM-DD)
   - Content type (blog-post, landing-page, documentation, etc.)
   - Topic slug (lowercase, hyphens instead of spaces)

3. Save the content:
   ```bash
   cat > generated/2024-01-21_landing-page_product-name.md << 'EOF'
   [generated content here]
   EOF
   ```

4. Confirm the file was saved:
   ```bash
   ls -lh generated/2024-01-21_landing-page_product-name.md
   ```

### Step 5: Show Preview

Display the generated content to the user and tell them:
- "I've saved this content to: `generated/[filename].md`"
- Show the preview
- Ask: "Would you like me to:
  - Publish it to WordPress?
  - Make any changes first?
  - Just save it for later (don't publish now)?"

If they want changes, regenerate and overwrite the file.

### Step 6: Publish to WordPress (if requested)

If they approve:

1. Ask publishing options using AskUserQuestion:
   - Post type (posts/pages/custom post type)
   - Status (draft recommended, or publish)
   - Custom slug (optional)

2. Run the publishing tool using the saved file:
   ```bash
   python3.11 publish.py generated/[filename].md --post-type [TYPE] --status [STATUS]
   ```

3. Show the success message with:
   - WordPress URL
   - The saved file location (for future reference)

4. **Do NOT delete the generated file** - it's saved for the user's records

## Important Notes

- **Always create generated/ directory first** if it doesn't exist
- **Always use descriptive filenames** - include date, type, and slug
- **Never delete generated files** - they're a permanent record
- **Always use AskUserQuestion** for gathering requirements
- **Always show a preview** before publishing
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

User: [Provides details: "TaskFlow", "project management", etc.]
You: Perfect! I'm generating your landing page now...
[Generate content using template]
[Save to generated/2024-01-21_landing-page_taskflow.md]

You: I've saved your landing page to: generated/2024-01-21_landing-page_taskflow.md

Here's the content:

# [Generated Title]
[Full content preview...]

Would you like me to:
- Publish this to WordPress?
- Make changes first?
- Just save it for now (no publishing)?

User: Publish it
You: Great! A few publishing options...
[Ask for post type, status, slug]

User: [Selects: landing_pages, draft]
You: Publishing to WordPress from generated/2024-01-21_landing-page_taskflow.md...
[Run publish.py]

You: ✅ Published successfully!

URL: https://yoursite.com/?p=123
Status: draft
File: generated/2024-01-21_landing-page_taskflow.md

You can now:
- Edit in WordPress: https://yoursite.com/wp-admin/post.php?post=123&action=edit
- Re-publish updated version later using the saved file
- Use this file as a template for similar pages
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
- **File is still saved** - they can try publishing again later

Common errors:
- 401: Wrong username/password
- 404: Wrong site URL or post type doesn't exist
- SSL error: Need to use python3.11 instead of python3

## File Management

The `generated/` directory serves as:
- **Archive** - All created content is preserved
- **Source of truth** - Edit files and republish
- **Template library** - Reuse successful content structures
- **Audit trail** - Know what was published when

Users can:
```bash
# List all generated content
ls -lh generated/

# Republish updated content
python3.11 publish.py generated/2024-01-21_landing-page_taskflow.md --status publish

# Use as template
cp generated/2024-01-21_landing-page_taskflow.md generated/2024-01-22_landing-page_newproduct.md
```

## Success Criteria

A successful session should:
1. ✅ Ask clarifying questions
2. ✅ Generate high-quality content
3. ✅ Save to generated/ directory with descriptive filename
4. ✅ Show preview before publishing
5. ✅ Publish successfully to WordPress (if requested)
6. ✅ Provide both WordPress URL and saved file location
7. ✅ Keep the generated file (don't delete)

Make the experience smooth, professional, and helpful!
