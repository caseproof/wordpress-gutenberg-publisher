# Skills

## `/wp-content`

Generate content with AI and publish to WordPress.

**Flow:** Questions → Generate → Preview → Publish

**Types:** Blog posts, landing pages, documentation, product pages

**Output:** Saves to `generated/YYYY-MM-DD_type_slug.md`

## `/wp-quick`

Publish existing markdown files.

**Flow:** Select file → Preview → Publish

## Setup Required

```ini
# config.ini
[wordpress]
site_url = https://yoursite.com
username = your_username
app_password = xxxx xxxx xxxx xxxx
```

## That's It

Skills call `publish.py` which reads `config.ini`. Secure and simple.
