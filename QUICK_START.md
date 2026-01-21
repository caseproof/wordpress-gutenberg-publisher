# Quick Start Guide

Get publishing to WordPress in 5 minutes.

## Step 1: Install Dependencies (1 minute)

```bash
cd wordpress-gutenberg-publisher
pip install -r requirements.txt
```

This installs:
- `markdown` - Converts markdown to HTML
- `requests` - Makes HTTP requests to WordPress REST API

## Step 2: Setup WordPress Application Password (2 minutes)

1. Log into your WordPress Dashboard
2. Go to **Users → Profile**
3. Scroll to **Application Passwords**
4. Enter name: "Gutenberg Publisher"
5. Click **Add New Application Password**
6. **COPY THE PASSWORD** (you'll only see it once!)

The password looks like: `xxxx xxxx xxxx xxxx xxxx xxxx`

## Step 3: Configure (1 minute)

```bash
# Copy the example config
cp config.example.ini config.ini

# Edit with your details
nano config.ini  # or use your favorite editor
```

Fill in:
```ini
[wordpress]
site_url = https://yoursite.com
username = your_wordpress_username
app_password = xxxx xxxx xxxx xxxx xxxx xxxx
```

**Important:** Do NOT commit `config.ini` to git (it's in `.gitignore`)

## Step 4: Test It (1 minute)

```bash
# Try the example file
python publish.py examples/landing-page-example.md
```

You'll see:
```
🚀 WordPress Gutenberg Publisher

📝 Loading configuration...
📖 Reading examples/landing-page-example.md...
🔄 Converting to Gutenberg blocks...

================================================================================
📄 Title: Amazing Landing Page
📏 Content length: 1847 characters
================================================================================

Post type (posts/pages/custom-type) [posts]: pages
Status (draft/publish/pending/private) [draft]: draft
URL slug (leave empty for auto-generate): 

✅ Ready to publish:
   Type: pages
   Status: draft
   Slug: (auto-generated)

Continue? (y/n): y

🎉 Published successfully!
   ID: 123
   URL: https://yoursite.com/amazing-landing-page/
```

## Step 5: Check WordPress

1. Go to your WordPress Dashboard
2. Navigate to **Pages → All Pages** (or Posts)
3. Find your newly created page
4. Click **Edit** to see the Gutenberg blocks!

## Next Steps

### Publish More Content

```bash
# Create your own markdown file
echo "# My First Post\n\nThis is amazing!" > my-post.md

# Publish it
python publish.py my-post.md
```

### Use with AI (Claude/ChatGPT)

1. Ask Claude/ChatGPT to generate markdown content
2. Save the output to a `.md` file
3. Run `python publish.py filename.md`

See [prompts/content-generation.md](./prompts/content-generation.md) for AI prompts.

### Automate Publishing

```bash
# Publish directly without prompts
python publish.py content.md --status publish --post-type posts

# In a script
for file in content/*.md; do
    python publish.py "$file" --status draft --post-type posts
done
```

### Custom Post Types

```bash
# If you have a custom post type "landing_pages"
python publish.py content.md --post-type landing_pages --status publish
```

## Troubleshooting

### "Config file not found"
You forgot step 3. Run: `cp config.example.ini config.ini`

### "WordPress API returned 401"
Your username or application password is wrong. Double-check `config.ini`.

### "WordPress API returned 404"
Check your `site_url` in config.ini. Make sure it doesn't have a trailing slash and is the correct URL.

### Content Looks Weird
The Gutenberg conversion works best with:
- Standard markdown (headings, paragraphs, lists)
- Avoid complex HTML
- Test with draft first

## What's Next?

- **Learn to build tools like this:** [LEARNING_GUIDE.md](./LEARNING_GUIDE.md)
- **Get AI content prompts:** [prompts/content-generation.md](./prompts/content-generation.md)
- **See how this was built:** [prompts/HOW_TO_BUILD_THIS.md](./prompts/HOW_TO_BUILD_THIS.md)

---

**Need help?** Open an issue at https://github.com/caseproof/wordpress-gutenberg-publisher/issues
