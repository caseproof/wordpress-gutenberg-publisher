# WordPress Content Publisher Skill

**Skill Name:** `wordpress-content-publisher`  
**Alias:** `/publish-content`

## Description

Generate high-quality content with AI and publish directly to WordPress - all in one workflow. Handles blog posts, landing pages, product features, and documentation.

## What This Skill Does

1. **Asks what type of content** you want to create
2. **Gathers requirements** through guided questions
3. **Generates markdown content** using proven templates
4. **Shows you a preview** before publishing
5. **Publishes to WordPress** (if you approve)

## Usage

```
/publish-content
```

Or invoke directly:
```
I want to create a landing page for my product
```

## Workflow

### Step 1: Content Type Selection

The skill asks what you want to create:
- **Blog Post** - SEO-optimized article with structure
- **Landing Page (Feature Overview)** - Grid-style features page
- **Landing Page (Product Deep-Dive)** - Aspirational single-feature page
- **Product Features Page** - Showcase multiple capabilities
- **Documentation** - Technical how-to guide
- **Comparison Page** - "Why choose us" positioning

### Step 2: Requirement Gathering

Based on your selection, asks specific questions:

**For Blog Posts:**
- Topic/title
- Target audience
- Primary keyword
- Tone (professional/casual/technical)
- Length (800-1200 / 1500-2000 / 2500-3000 words)

**For Landing Pages:**
- Product/service name
- What it does (brief description)
- Target audience
- Main value proposition
- Key features (3-6)
- Social proof (testimonials, ratings)

**For Documentation:**
- Feature/API/tool name
- Target audience (developers/end-users/admins)
- Technical level (beginner/intermediate/advanced)
- Prerequisites

### Step 3: Content Generation

Generates markdown content using proven templates and best practices:
- SEO-optimized structure
- Compelling headlines
- Benefit-driven copy
- Clear CTAs
- Social proof integration

### Step 4: Preview & Edit

Shows you the generated content and asks:
- "Does this look good?"
- "Want me to adjust anything?"
- "Ready to publish?"

### Step 5: WordPress Publishing

If approved:
- Saves markdown to file
- Publishes to WordPress using the publishing tool
- Shows you the draft URL
- You can edit in WordPress before making it live

## Configuration Required

The skill requires WordPress credentials configured in `config.ini`:

```ini
[wordpress]
site_url = https://yoursite.com
username = your_username
app_password = xxxx xxxx xxxx xxxx xxxx xxxx
```

## Publishing Options

When publishing, you'll be asked:
- **Post Type:** posts / pages / custom_post_type
- **Status:** draft / publish
- **Custom Slug:** (optional)

## Examples

**Example 1: Blog Post**
```
User: /publish-content
Skill: What type of content do you want to create?
User: Blog post
Skill: What's the topic?
User: How to choose WordPress hosting
Skill: Who's the target audience?
User: Small business owners, non-technical
[Skill generates content]
Skill: Here's your blog post... [preview]
Skill: Ready to publish?
User: Yes, as a draft
Skill: ✅ Published! https://yoursite.com/?p=123
```

**Example 2: Landing Page**
```
User: I need a landing page for my new coaching product
Skill: Great! I'll create a landing page. What's the product name?
User: CoachMaster Pro
Skill: What does it do?
User: Online coaching platform with progress tracking
[Skill asks more questions, generates content]
Skill: Here's your landing page... [preview]
User: Can you make the headline more compelling?
[Skill adjusts]
Skill: Better? Ready to publish?
User: Yes
Skill: ✅ Published as draft! https://yoursite.com/?p=456
```

## Advanced Features

### Custom Post Types

Publish to any custom post type:
```
Skill: What post type? (posts/pages/custom)
User: landing_pages
Skill: ✅ Publishing to custom post type 'landing_pages'
```

### Batch Publishing

Create multiple pieces of content in one session:
```
User: I need 3 blog posts about WordPress security
[Skill generates all 3, publishes each as draft]
```

### Template Customization

The skill uses templates from `prompts/landing-page-templates.md` and `prompts/content-generation-prompts.md`. You can customize these templates to match your brand voice.

## Troubleshooting

**"Config file not found"**
- Create `config.ini` from `config.example.ini`
- Add your WordPress credentials

**"Publishing failed: 401"**
- Check your WordPress application password
- Verify the password is correct in `config.ini`

**"Publishing failed: 404"**
- Check the site URL in `config.ini`
- For custom post types, ensure REST API support is enabled

## Tips for Best Results

1. **Be specific** - More details = better content
2. **Review before publishing** - Always check the preview
3. **Start with drafts** - Publish as draft, edit in WordPress, then publish live
4. **Use custom post types** - Great for landing pages, documentation, portfolios
5. **Iterate** - Ask for adjustments until it's perfect

## Related Resources

- [WordPress Publishing Tool Documentation](../README.md)
- [Landing Page Templates](../prompts/landing-page-templates.md)
- [Content Generation Prompts](../prompts/content-generation-prompts.md)
- [Example Content](../examples/)
