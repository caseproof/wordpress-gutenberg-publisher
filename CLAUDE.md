# WordPress Gutenberg Publisher - Claude Code Integration

This project includes **Claude Code skills** that make content creation and publishing seamless.

## What Are Skills?

Skills are Claude Code workflows that combine AI content generation with WordPress publishing in one command.

## Available Skills

### `/wp-content` - Generate & Publish Content

Create content from scratch with AI assistance:
- Blog posts (SEO-optimized)
- Landing pages (2 styles: feature overview and deep-dive)
- Product features pages
- Documentation
- Comparison pages

**Usage:** Just type `/wp-content` and follow the prompts.

### `/wp-quick` - Quick Publish Existing Files

Publish existing markdown files to WordPress:
- Fast workflow
- Shows preview
- Asks for post type/status
- Publishes immediately

**Usage:** Type `/wp-quick` and select a file.

## Getting Started

### 1. Configure WordPress

```bash
cp config.example.ini config.ini
# Edit config.ini with your WordPress credentials
```

### 2. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Try the Skills

```bash
# In Claude Code, run:
/wp-content

# Or for quick publish:
/wp-quick
```

## How Skills Work

When you invoke `/wp-content`:

1. **Claude asks questions** - What type of content? Product name? Target audience?
2. **Generates content** - Uses proven templates to create high-quality markdown
3. **Shows preview** - You review and approve before publishing
4. **Publishes to WordPress** - Converts to Gutenberg blocks and posts via API

All in one conversational workflow!

## Documentation

- [Skills README](./.claude/skills/README.md) - Complete skill documentation
- [Main README](./README.md) - Tool documentation
- [Quick Start](./QUICK_START.md) - 5-minute setup guide
- [Learning Guide](./LEARNING_GUIDE.md) - How this was built

## Examples

**Create a landing page:**
```
/wp-content
> Landing Page - Feature Overview
> Product: TaskFlow
> Audience: Freelancers
[Generates and publishes complete landing page]
```

**Publish existing file:**
```
/wp-quick
> examples/simple-blog-post.md
> Post type: posts
> Status: draft
[Published to WordPress]
```

## Requirements

- Python 3.8+ (Python 3.11+ recommended)
- WordPress 5.0+ with REST API enabled
- WordPress Application Password
- Claude Code CLI

---

**For detailed usage instructions, see:** [.claude/skills/README.md](./.claude/skills/README.md)
