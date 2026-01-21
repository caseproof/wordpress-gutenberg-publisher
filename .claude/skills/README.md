# WordPress Publishing Skills for Claude Code

These skills integrate content generation and WordPress publishing into seamless workflows.

## Available Skills

### 1. `/wp-content` - Full Content Creation & Publishing

**Use when:** You want to create new content from scratch and publish it.

**What it does:**
1. Asks what type of content you want (blog post, landing page, documentation, etc.)
2. Gathers specific requirements through guided questions
3. Generates high-quality markdown content using proven templates
4. Shows you a preview
5. Publishes to WordPress if you approve

**Example:**
```
/wp-content

> What type of content? Landing Page - Feature Overview
> Product name? TaskFlow
> What does it do? Simple task management for solopreneurs
> [Generates complete landing page]
> Publish? Yes
> ✅ Published to https://yoursite.com/?p=123
```

**Aliases:** `/publish-content`, `/wp-publish`

---

### 2. `/wp-quick` - Quick Publish Existing Files

**Use when:** You already have a markdown file ready to publish.

**What it does:**
1. Asks which file to publish (or shows available files)
2. Shows a preview
3. Asks for publishing options (post type, status, slug)
4. Publishes to WordPress

**Example:**
```
/wp-quick

> Which file? examples/simple-blog-post.md
> [Shows preview]
> Post type? pages
> Status? draft
> ✅ Published to https://yoursite.com/?p=124
```

**Aliases:** `/wp-quick-publish`

---

## Setup Required

Before using these skills, you need:

### 1. WordPress Credentials

Create `config.ini` from the template:

```bash
cp config.example.ini config.ini
```

Edit with your WordPress details:
```ini
[wordpress]
site_url = https://yoursite.com
username = your_username
app_password = xxxx xxxx xxxx xxxx xxxx xxxx
```

### 2. Python Dependencies

```bash
pip3 install -r requirements.txt
```

### 3. WordPress Application Password

Generate in WordPress:
1. Dashboard → Users → Profile
2. Scroll to "Application Passwords"
3. Name it "WordPress Publisher"
4. Copy the generated password to `config.ini`

---

## Workflow Comparison

| Task | Use This Skill | Why |
|------|---------------|-----|
| Create blog post from scratch | `/wp-content` | Generates optimized content with guided questions |
| Create landing page | `/wp-content` | Uses proven templates, gathers all requirements |
| Publish existing markdown | `/wp-quick` | Fast, no generation needed |
| Create documentation | `/wp-content` | Structured technical content with code examples |
| Test the tool | `/wp-quick` | Publish example files to test setup |

---

## Content Types Supported

### `/wp-content` generates:

1. **Blog Posts**
   - SEO-optimized structure
   - Compelling headlines
   - Actionable content
   - Clear CTAs

2. **Landing Pages (Feature Overview)**
   - Grid-style feature showcase
   - Multiple capabilities highlighted
   - Social proof integration
   - Based on MemberPress features page pattern

3. **Landing Pages (Product Deep-Dive)**
   - Aspirational, emotional copy
   - Single feature deep-dive
   - Transformation-focused
   - Based on MemberPress CoachKit pattern

4. **Product Features**
   - Showcase multiple capabilities
   - Benefit-driven descriptions
   - Use cases and examples

5. **Documentation**
   - Technical how-to guides
   - Code examples
   - Troubleshooting sections
   - Step-by-step instructions

6. **Comparison Pages**
   - "Why choose us" positioning
   - Side-by-side comparisons
   - Honest differentiation

---

## Publishing Options

Both skills support:

**Post Types:**
- `posts` - Standard blog posts
- `pages` - Static pages
- Custom post types (e.g., `landing_pages`, `ht_kb`, `portfolio`)

**Status:**
- `draft` - Save as draft (recommended - review before going live)
- `publish` - Publish immediately

**Custom Slug:**
- Optional SEO-friendly URL slug
- Auto-generated if not provided

---

## Tips for Best Results

### Using `/wp-content`

1. **Be specific** - More details = better content
   - ✅ "Task management for freelance designers"
   - ❌ "Task management tool"

2. **Provide real examples** - Testimonials, features, benefits
   - ✅ "Sarah from GrowthCo increased productivity 40%"
   - ❌ "Customers love it"

3. **Review the preview** - Always check before publishing
   - Adjust headlines
   - Tweak CTAs
   - Verify facts

4. **Start with drafts** - Publish as draft, edit in WordPress, then go live
   - Safer workflow
   - Add images/media in WordPress
   - Final polish in Gutenberg editor

### Using `/wp-quick`

1. **Check the file first** - Make sure markdown is formatted correctly
   - First H1 becomes the title
   - Links should use `[text](url)` format
   - Lists should have proper indentation

2. **Use for testing** - Great for trying example files
   ```
   /wp-quick
   > examples/feature-overview-landing-page.md
   ```

3. **Custom post types** - Perfect for landing pages and portfolios
   ```
   Post type: landing_pages
   Status: draft
   ```

---

## Troubleshooting

### "Config file not found"
```bash
cp config.example.ini config.ini
# Edit config.ini with your credentials
```

### "WordPress API returned 401"
- Wrong username or application password
- Check credentials in `config.ini`
- Regenerate application password in WordPress

### "WordPress API returned 404"
- Wrong site URL
- Check `site_url` in `config.ini` (no trailing slash)
- For custom post types, ensure REST API support

### "SSL error"
- Use Python 3.11+: `brew install python@3.11`
- Skills automatically use `python3.11`

### Publishing to custom post types
- Ensure post type has `show_in_rest => true`
- Find post type slug via: `https://yoursite.com/wp-json/wp/v2/types`

---

## Examples

### Example 1: Create Product Landing Page

```
User: /wp-content
Skill: What type of content?
User: Landing Page - Feature Overview
Skill: Product name?
User: TaskFlow Pro
Skill: What does it do?
User: All-in-one project management for small teams
Skill: Target audience?
User: Freelancers and agencies under 10 people
Skill: Main value proposition?
User: Manage projects without complexity - setup in 5 minutes
Skill: Key features? (list 3-6)
User: Visual boards, Time tracking, Team collaboration, Client portal, Reporting, Mobile apps
Skill: Do you have testimonials?
User: Yes - Sarah from GrowthCo says "Increased our efficiency by 40%"

[Generates landing page with all 6 features, testimonial, CTAs]

Skill: Here's your landing page... [preview]
User: Looks great!
Skill: Publish as? 
User: Custom post type: landing_pages, status: draft

✅ Published! https://yoursite.com/?p=456
```

### Example 2: Quick Publish Example File

```
User: /wp-quick
Skill: Which file?
- examples/simple-blog-post.md
- examples/feature-overview-landing-page.md  
- examples/product-feature-deep-dive.md
- (or provide path)

User: examples/simple-blog-post.md

[Shows preview of WordPress security blog post]

Skill: Ready to publish?
User: Yes
Skill: Post type?
User: posts
Skill: Status?
User: draft

✅ Published! https://yoursite.com/?p=789
```

### Example 3: Create Documentation

```
User: I need docs for our new API feature
Skill: /wp-content
[Asks content type]
User: Documentation
Skill: Feature name?
User: Webhook Events API
Skill: Target audience?
User: Developers - intermediate level
Skill: What are the prerequisites?
User: API key, HTTPS endpoint, JSON parsing

[Generates technical documentation with code examples, troubleshooting, FAQ]

Skill: Here's the documentation... [preview]
User: Can you add more error handling examples?
[Adjusts content]
Skill: Better?
User: Perfect! Publish to our docs
Skill: Post type?
User: documentation
Skill: Status?
User: publish

✅ Published! https://yoursite.com/docs/webhook-events-api
```

---

## Advanced Usage

### Batch Publishing

```
User: I need 3 blog posts about WordPress security
/wp-content

[Generates post 1]
✅ Published

[Generates post 2]
✅ Published

[Generates post 3]
✅ Published
```

### Custom Post Type + Custom Slug

```
/wp-quick
> File: my-landing-page.md
> Post type: landing_pages
> Status: draft
> Custom slug: special-offer-2024

✅ Published to https://yoursite.com/landing_pages/special-offer-2024
```

### Edit in WordPress Then Publish

```
/wp-content
[Generates content]
> Status: draft

✅ Draft created! https://yoursite.com/wp-admin/post.php?post=123&action=edit

[Edit in WordPress - add images, adjust formatting]
[Then publish from WordPress dashboard]
```

---

## Related Resources

- [Main README](../README.md) - Tool documentation
- [Quick Start Guide](../QUICK_START.md) - 5-minute setup
- [Learning Guide](../LEARNING_GUIDE.md) - How this was built
- [Landing Page Templates](../prompts/landing-page-templates.md) - Template reference
- [Content Generation Prompts](../prompts/content-generation-prompts.md) - More templates

---

**Questions?** Open an issue at https://github.com/caseproof/wordpress-gutenberg-publisher/issues
