# WordPress Gutenberg Publisher

**Convert markdown to WordPress Gutenberg blocks and publish automatically.**

Perfect for:
- 📄 Landing pages
- 📚 Documentation
- 📝 Blog posts
- 🔧 Custom post types
- 🤖 AI-generated content (Claude/ChatGPT)

## What This Does

1. Takes markdown content (write it or generate with AI)
2. Converts to proper WordPress Gutenberg blocks
3. Publishes to your WordPress site via REST API
4. Preserves all links, formatting, and structure

## Quick Start (5 Minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure WordPress
cp config.example.ini config.ini
# Edit config.ini with your WordPress details

# 3. Publish content
python publish.py examples/landing-page-example.md
```

See [QUICK_START.md](./QUICK_START.md) for detailed setup.

## Usage

### Interactive Mode (Recommended for First Time)
```bash
python publish.py my-content.md
```

You'll be prompted for:
- Post type (posts/pages/custom type)
- Status (draft/publish)
- URL slug

### Direct Mode (For Scripts/Automation)
```bash
# Publish as draft
python publish.py content.md --status draft

# Publish immediately as page
python publish.py content.md --status publish --post-type pages

# Custom post type with slug
python publish.py content.md --post-type landing_pages --slug my-page
```

## Features

✅ **Gutenberg Block Conversion**
- Headings (H1-H6)
- Paragraphs with links
- Unordered/ordered lists
- Block quotes
- Code blocks

✅ **WordPress Integration**
- Posts, pages, custom post types
- Draft, publish, pending, private status
- Custom slugs
- Application password authentication

✅ **AI-Friendly**
- Works with Claude/ChatGPT generated markdown
- See `prompts/` directory for content generation prompts

## Directory Structure

```
wordpress-gutenberg-publisher/
├── README.md              # This file
├── QUICK_START.md         # 5-minute setup guide
├── LEARNING_GUIDE.md      # Learn to build systems like this
│
├── config.ini             # Your WordPress credentials (create from .example)
├── requirements.txt       # Python dependencies
│
├── publish.py             # Main CLI tool
├── gutenberg_converter.py # Markdown → Gutenberg converter
├── wordpress_client.py    # WordPress REST API wrapper
│
├── prompts/               # AI prompts for content + system building
│   ├── HOW_TO_BUILD_THIS.md
│   ├── content-generation.md
│   ├── landing-page-generator.md
│   └── documentation-generator.md
│
└── examples/              # Sample content + usage
    ├── landing-page-example.md
    └── documentation-example.md
```

## Learning Resources

Want to build your own tools like this? See:
- [LEARNING_GUIDE.md](./LEARNING_GUIDE.md) - How this tool was built
- [prompts/HOW_TO_BUILD_THIS.md](./prompts/HOW_TO_BUILD_THIS.md) - The actual prompts used

## Requirements

- Python 3.8+
- WordPress 5.0+ with REST API enabled
- WordPress Application Password (or Basic Auth)

## Security Notes

- **NEVER commit `config.ini`** to git (it contains credentials)
- Use WordPress Application Passwords (not your account password)
- Consider using environment variables for production

## Troubleshooting

**"Config file not found"**
```bash
cp config.example.ini config.ini
# Edit config.ini with your details
```

**"WordPress API returned 401"**
- Check your username and application password
- Verify application passwords are enabled in WordPress

**"WordPress API returned 404"**
- Check your site_url in config.ini
- Verify REST API is enabled
- For custom post types, ensure they have REST API support

**Content looks wrong in WordPress**
- Check the Gutenberg block format in WordPress editor
- Try publishing as draft first to preview

## Contributing

Issues and pull requests welcome at https://github.com/caseproof/wordpress-gutenberg-publisher

## License

MIT License - See LICENSE file for details

---

**Need help?** Check out:
- [QUICK_START.md](./QUICK_START.md) - Setup guide
- [LEARNING_GUIDE.md](./LEARNING_GUIDE.md) - Learn the concepts
- [prompts/](./prompts/) - AI prompts for content and building
