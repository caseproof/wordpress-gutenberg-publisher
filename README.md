# WordPress Publisher

Generate content with AI. Publish to WordPress. One command.

```bash
/wp-content
```

## Setup (2 minutes)

```bash
pip3 install -r requirements.txt
cp config.example.ini config.ini
# Add your WordPress credentials
```

Get application password: `WordPress Dashboard → Users → Profile → Application Passwords`

## Usage

### Generate & Publish (Recommended)

```bash
/wp-content
```

Claude asks questions → generates content → saves to `generated/` → publishes to WordPress.

Supports: blog posts, landing pages, documentation, product pages.

### Quick Publish

```bash
/wp-quick
```

Publish existing markdown files.

### CLI (Direct)

```bash
python3.11 publish.py file.md --post-type pages --status draft
```

## Custom Post Types

```bash
python3.11 publish.py file.md --post-type ht_kb --status publish
```

Works with any REST API-enabled custom post type.

## How It Works

1. **Markdown → Gutenberg blocks** (preserves all links/formatting)
2. **WordPress REST API** (application password auth)
3. **Content saved to `generated/`** (organized, reusable)

## Files

- `/wp-content` - Skill for content generation + publishing
- `/wp-quick` - Skill for quick publishing
- `publish.py` - CLI tool
- `prompts/` - Content templates
- `examples/` - Sample content
- `generated/` - Your generated content (gitignored)

## Skills

**`/wp-content`**: Ask → Generate → Publish  
**`/wp-quick`**: File → Publish

That's it.

## Troubleshooting

**401**: Wrong credentials in `config.ini`  
**404**: Wrong site URL or post type doesn't exist  
**SSL error**: Use Python 3.11+ (`brew install python@3.11`)

## For Your Team

Clone, setup, use. 2 minutes.

This tool + Claude = WordPress content pipeline.
