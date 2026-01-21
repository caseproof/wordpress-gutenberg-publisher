# Claude Code Skills - Quick Start Guide

**TL;DR:** Type `/wp-content` in Claude Code to generate and publish content to WordPress in one workflow.

## What Are Skills?

Skills are conversational workflows that combine AI content generation with WordPress publishing. No manual file creation, no switching tools—just a conversation that results in published content.

## Two Skills Available

### 1. `/wp-content` - Generate & Publish Content

**Perfect for:** Creating new content from scratch

**What happens:**
1. Claude asks what type (blog post, landing page, documentation, etc.)
2. Asks specific questions based on your choice
3. Generates professional content using proven templates
4. Saves to `generated/` directory with descriptive filename
5. Shows preview and asks for approval
6. Publishes to WordPress if you approve

**Example conversation:**
```
You: /wp-content

Claude: What type of content would you like to create?
- Blog Post
- Landing Page (Feature Overview)
- Landing Page (Product Deep-Dive)
- Product Features
- Documentation
- Comparison Page

You: Landing Page - Feature Overview

Claude: Great! What's the product name?
You: TaskFlow Pro

Claude: What does it do?
You: Project management for small teams

Claude: Who's the target audience?
You: Freelancers and agencies

Claude: Main value proposition?
You: Manage projects without complexity

Claude: List 3-6 key features:
You: Visual boards, Time tracking, Collaboration, Reporting

[Generates complete landing page]

Claude: I've saved this to: generated/2024-01-21_landing-page_taskflow-pro.md

Here's your landing page:
# Manage Projects Without the Complexity
[Full preview of generated content...]

Would you like me to:
- Publish to WordPress?
- Make changes first?
- Just save for later?

You: Publish it

Claude: Post type?
You: landing_pages

Claude: Status?
You: draft

Claude: ✅ Published!
URL: https://yoursite.com/?p=456
File: generated/2024-01-21_landing-page_taskflow-pro.md
```

### 2. `/wp-quick` - Quick Publish Existing Files

**Perfect for:** Publishing markdown files you already have

**What happens:**
1. Shows available markdown files (or you provide a path)
2. Displays preview
3. Asks for post type and status
4. Publishes to WordPress

**Example:**
```
You: /wp-quick

Claude: Which file would you like to publish?
- examples/simple-blog-post.md
- examples/feature-overview-landing-page.md
- generated/2024-01-20_landing-page_previous.md
- Or provide a file path

You: examples/simple-blog-post.md

Claude: [Shows preview]
Ready to publish?

You: Yes

Claude: Post type?
You: posts

Claude: Status?
You: draft

Claude: ✅ Published!
URL: https://yoursite.com/?p=789
```

## Setup (One-Time)

### 1. Configure WordPress

```bash
cp config.example.ini config.ini
```

Edit `config.ini`:
```ini
[wordpress]
site_url = https://yoursite.com
username = your_username
app_password = xxxx xxxx xxxx xxxx
```

**Get Application Password:**
1. WordPress Dashboard → Users → Profile
2. Scroll to "Application Passwords"
3. Add "WordPress Publisher"
4. Copy the generated password

### 2. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Test It

```bash
/wp-quick
> examples/simple-blog-post.md
> Post type: posts
> Status: draft
```

## Content Types

The `/wp-content` skill generates:

| Type | Use Case | Style | Example |
|------|----------|-------|---------|
| **Blog Post** | Articles, guides, how-tos | SEO-optimized, structured | "10 WordPress Security Tips" |
| **Landing Page (Feature Overview)** | Main product pages | Grid-style features | MemberPress features page |
| **Landing Page (Deep-Dive)** | Single feature/add-on | Aspirational, emotional | CoachKit page |
| **Product Features** | Capability showcase | Benefit-driven | Feature comparison |
| **Documentation** | Technical guides | Code examples, troubleshooting | API docs |
| **Comparison** | "Why choose us" pages | Honest differentiation | vs. competitors |

## File Organization

Skills save all generated content to `generated/` directory:

```
generated/
├── README.md
├── 2024-01-21_blog-post_wordpress-security.md
├── 2024-01-21_landing-page_taskflow-features.md
└── 2024-01-22_documentation_api-webhooks.md
```

**Filename format:** `YYYY-MM-DD_content-type_slug.md`

**Benefits:**
- Archive of all generated content
- Easy to republish updated versions
- Template library for future content
- Source markdown preserved

## Publishing Options

Both skills support:

**Post Types:**
- `posts` - Blog posts
- `pages` - Static pages
- Custom types (e.g., `landing_pages`, `ht_kb`, `portfolio`)

**Status:**
- `draft` - Review in WordPress first (recommended)
- `publish` - Go live immediately

**Custom Slug:**
- Optional SEO-friendly URL
- Auto-generated if not provided

## Advanced Usage

### Republish Updated Content

```bash
# Edit the file
nano generated/2024-01-21_landing-page_taskflow.md

# Republish
python3.11 publish.py generated/2024-01-21_landing-page_taskflow.md --status publish
```

### Use as Template

```bash
# Copy successful content
cp generated/2024-01-21_landing-page_taskflow.md generated/2024-01-22_landing-page_newproduct.md

# Edit and publish
/wp-quick
> generated/2024-01-22_landing-page_newproduct.md
```

### Batch Create Content

```
/wp-content
[Generate blog post 1]
✅ Published

/wp-content  
[Generate blog post 2]
✅ Published

/wp-content
[Generate blog post 3]
✅ Published
```

## Tips for Best Results

### Content Generation (`/wp-content`)

1. **Be specific** in your answers
   - ✅ "Freelance designers who manage 3-5 clients"
   - ❌ "People who need project management"

2. **Provide real examples**
   - ✅ "Sarah from GrowthCo increased productivity 40%"
   - ❌ "Users love our product"

3. **Review the preview** before publishing
   - Adjust headlines if needed
   - Verify facts and claims
   - Check CTAs make sense

4. **Start with drafts**
   - Publish as draft
   - Add images in WordPress
   - Final edits in Gutenberg
   - Then publish live

### Quick Publishing (`/wp-quick`)

1. **Check markdown formatting** first
   - First H1 becomes the title
   - Links: `[text](url)`
   - Lists need proper indentation

2. **Use for testing**
   ```
   /wp-quick
   > examples/feature-overview-landing-page.md
   ```

3. **Great for custom post types**
   ```
   Post type: landing_pages
   Status: draft
   ```

## Troubleshooting

### "Config file not found"
```bash
cp config.example.ini config.ini
# Edit with your credentials
```

### "WordPress API returned 401"
- Wrong credentials in `config.ini`
- Regenerate application password

### "WordPress API returned 404"
- Wrong site URL (no trailing slash)
- Custom post type doesn't exist or lacks REST API support

### "SSL error"
- Use Python 3.11+
- Skills automatically use `python3.11`

## How It Works Behind the Scenes

1. **Skills use templates** from `prompts/` directory
2. **Generate markdown** based on your answers
3. **Save to `generated/`** with descriptive filename
4. **Call `publish.py`** which:
   - Reads `config.ini` for credentials
   - Converts markdown to Gutenberg blocks
   - Posts to WordPress via REST API
5. **Return WordPress URL** and file location

**Security:** Skills never see your WordPress credentials. They call `publish.py` which reads `config.ini` directly.

## Quick Reference

| Task | Command | Where It Goes |
|------|---------|---------------|
| Create blog post | `/wp-content` → Blog Post | Posts or custom type |
| Create landing page | `/wp-content` → Landing Page | Pages or custom type |
| Create documentation | `/wp-content` → Documentation | Pages or custom type |
| Publish existing file | `/wp-quick` → [file] | Any post type |
| Republish edited content | `python3.11 publish.py generated/file.md --status publish` | Same or different type |

## Full Documentation

- [Skills README](./.claude/skills/README.md) - Complete skill documentation
- [Main README](./README.md) - Tool documentation
- [Landing Page Templates](./prompts/landing-page-templates.md) - Template reference
- [Generated Content](./generated/README.md) - About the generated/ directory

---

**Questions?** Open an issue at https://github.com/caseproof/wordpress-gutenberg-publisher/issues

**Just want to try it?** Type `/wp-quick` and publish an example file!
