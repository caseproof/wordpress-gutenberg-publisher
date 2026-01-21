# Learning Guide: Building AI-Powered WordPress Tools

**What you'll learn:** How to build production-ready tools that integrate AI content generation with WordPress publishing.

This guide explains the concepts, architecture, and techniques used to build this WordPress Gutenberg Publisher. Use this as a foundation to build your own custom tools.

---

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [System Architecture](#system-architecture)
3. [How Content Flows](#how-content-flows)
4. [Key Technical Decisions](#key-technical-decisions)
5. [Building Your Own Tools](#building-your-own-tools)
6. [Common Patterns](#common-patterns)
7. [Next Steps](#next-steps)

---

## Core Concepts

### What is Gutenberg?

WordPress's **Gutenberg editor** uses a **block-based system** where content is broken into individual blocks (paragraphs, headings, images, etc.).

**Traditional WordPress HTML:**
```html
<h1>My Title</h1>
<p>Some content here</p>
```

**Gutenberg Block Format:**
```html
<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">My Title</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Some content here</p>
<!-- /wp:paragraph -->
```

**Why it matters:** Gutenberg blocks give you fine-grained control over layout, styling, and editing. They're the modern WordPress standard.

### Markdown as the Bridge

**Markdown** is a lightweight markup language that's:
- ✅ Easy to write (no complex syntax)
- ✅ Human-readable (looks good as plain text)
- ✅ AI-friendly (Claude/ChatGPT generate markdown naturally)
- ✅ Portable (works everywhere)

**Example:**
```markdown
# My Heading

This is a paragraph with a [link](https://example.com).

- List item 1
- List item 2
```

**This tool's job:** Convert markdown → HTML → Gutenberg blocks → WordPress

### WordPress REST API

The **WordPress REST API** lets you interact with WordPress programmatically (no browser needed).

**Key endpoints:**
- `GET /wp-json/wp/v2/posts` - List posts
- `POST /wp-json/wp/v2/posts` - Create post
- `GET /wp-json/wp/v2/pages` - List pages
- `POST /wp-json/wp/v2/pages` - Create page
- `POST /wp-json/wp/v2/{custom_post_type}` - Create custom post type

**Authentication:** Application Passwords (secure, revocable, doesn't expose main password)

---

## System Architecture

This tool has **3 core components:**

```
┌─────────────────────────────────────────────────────────────┐
│                      publish.py (CLI)                        │
│  • Reads markdown file                                       │
│  • Handles user input (interactive/direct mode)              │
│  • Orchestrates the workflow                                 │
└────────────┬────────────────────────────────────────────────┘
             │
             ├──────────────> gutenberg_converter.py
             │                • Converts markdown → HTML
             │                • Wraps HTML in Gutenberg blocks
             │                • Preserves links and formatting
             │
             └──────────────> wordpress_client.py
                              • WordPress REST API wrapper
                              • Authentication (Basic Auth)
                              • Create/update/delete operations
```

### Why This Architecture?

**Separation of Concerns:**
- `publish.py` - User interface (CLI)
- `gutenberg_converter.py` - Business logic (conversion)
- `wordpress_client.py` - External API (WordPress)

**Benefits:**
1. **Easy to test** - Each component can be tested independently
2. **Easy to extend** - Want a web UI? Swap out `publish.py`
3. **Easy to understand** - Each file has one clear purpose
4. **Reusable** - `gutenberg_converter.py` can be used in other projects

---

## How Content Flows

Let's trace a piece of content from markdown to WordPress:

### Step 1: Markdown Input
```markdown
# Amazing Guide

This is an introduction with a [helpful link](https://example.com).

## Section 1

Some content here.
```

### Step 2: Markdown → HTML
Using Python's `markdown` library:
```html
<h1>Amazing Guide</h1>
<p>This is an introduction with a <a href="https://example.com">helpful link</a>.</p>
<h2>Section 1</h2>
<p>Some content here.</p>
```

### Step 3: HTML → Gutenberg Blocks
Using regex patterns to find and wrap elements:
```html
<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Amazing Guide</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This is an introduction with a <a href="https://example.com">helpful link</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">Section 1</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Some content here.</p>
<!-- /wp:paragraph -->
```

### Step 4: Gutenberg Blocks → WordPress
POST to WordPress REST API:
```python
{
    "title": "Amazing Guide",
    "content": "<!-- wp:heading... (full Gutenberg content)",
    "status": "draft",
    "slug": "amazing-guide"
}
```

### Step 5: WordPress Stores and Displays
WordPress saves the content and renders it in the Gutenberg editor with full editing capabilities.

---

## Key Technical Decisions

### Decision 1: Regex vs HTML Parser

**Why regex for Gutenberg conversion?**

We use **regex pattern matching** instead of HTML parsing libraries (like `BeautifulSoup` or `HTMLParser`).

**Reason:** We need to preserve HTML **exactly as-is** without modification.

**HTML Parsers do:**
- Parse HTML into a tree structure
- "Fix" what they think is broken HTML
- Strip or modify tags they don't recognize
- Can lose inline elements (like `<a>` tags)

**Regex does:**
- Find patterns in text
- Wrap matched content without modifying it
- Preserve all links, formatting, attributes

**Example:**
```python
# Find all <h1> tags and their content
for match in re.finditer(r'<h1>(.*?)</h1>', html_content, re.DOTALL):
    content = match.group(1)  # The inside of the tag
    block = f'<!-- wp:heading {{"level":1}} -->\n<h1 class="wp-block-heading">{content}</h1>\n<!-- /wp:heading -->'
    blocks.append(block)
```

### Decision 2: Basic Auth vs OAuth

**Why Application Passwords (Basic Auth)?**

WordPress offers multiple authentication methods:
- Application Passwords (Basic Auth)
- OAuth 1.0a
- OAuth 2.0 (via plugins)
- JWT (via plugins)

**We chose Application Passwords because:**
- ✅ Built into WordPress core (no plugins)
- ✅ Simple to implement (just Base64 encoding)
- ✅ Secure (revocable, doesn't expose main password)
- ✅ Easy for users to generate (WordPress Dashboard → Profile)

**Implementation:**
```python
credentials = f"{username}:{app_password}"
token = base64.b64encode(credentials.encode()).decode()
headers = {"Authorization": f"Basic {token}"}
```

### Decision 3: CLI First, Web UI Later

**Why start with CLI?**

1. **Simpler to build** - No frontend framework needed
2. **Easy to test** - Just run `python publish.py file.md`
3. **Scriptable** - Can be used in automation/cron jobs
4. **Universal** - Works on any OS with Python
5. **Educational** - Shows core logic without UI complexity

**Future extensions:**
- Web UI (Flask/FastAPI + HTML)
- Desktop app (Electron/PyQt)
- WordPress plugin (PHP)
- GitHub Action (automated publishing)

### Decision 4: Config File vs Environment Variables

**Why config.ini instead of .env?**

Both are valid approaches. We chose `config.ini` because:
- ✅ Python's built-in `configparser` module
- ✅ Structured sections `[wordpress]`
- ✅ Easy for non-developers to edit
- ✅ Clear what each field means

**Could easily switch to `.env`:**
```bash
WORDPRESS_SITE_URL=https://example.com
WORDPRESS_USERNAME=admin
WORDPRESS_APP_PASSWORD=xxxx xxxx xxxx
```

---

## Building Your Own Tools

### Pattern: CLI Tool for Any API

**Generic structure:**
```
your-tool/
├── main.py              # CLI entry point
├── converter.py         # Business logic
├── api_client.py        # External API wrapper
├── config.ini           # Configuration
├── requirements.txt     # Dependencies
└── README.md           # Documentation
```

**Steps:**
1. Identify the API you want to use (docs, endpoints, auth)
2. Create `api_client.py` to wrap the API
3. Create `converter.py` for data transformation
4. Create `main.py` for user interaction
5. Test with real data
6. Document with examples

### Pattern: AI Content Generation → Publishing

**Flow:**
```
AI (Claude/ChatGPT) → Markdown → [Your Converter] → [Target Platform]
```

**Examples:**
- WordPress (this tool)
- Medium (via API)
- Ghost (via API)
- Notion (via API)
- Static site generators (Hugo, Jekyll, 11ty)

**Key insight:** Markdown is the universal format. Build converters from markdown to your target platform.

### Pattern: Interactive vs Script Modes

**Always support both:**

```python
if args.status:
    # Direct mode (for scripts)
    create_post(title, content, args.status)
else:
    # Interactive mode (for humans)
    status = input("Status (draft/publish): ")
    create_post(title, content, status)
```

**Why both?**
- Interactive: Great for first-time users, testing, manual work
- Script mode: Great for automation, CI/CD, batch operations

---

## Common Patterns

### Pattern: Read → Transform → Publish

**Most content tools follow this pattern:**
```python
# 1. READ
content = read_file(file_path)

# 2. TRANSFORM
transformed = transform_content(content)

# 3. PUBLISH
api_client.publish(transformed)
```

**Variations:**
- Read from API instead of file
- Multiple transformation steps
- Publish to multiple destinations

### Pattern: Error Handling

**Always handle common errors:**
```python
try:
    result = api_client.create_post(data)
except requests.exceptions.ConnectionError:
    print("❌ Can't connect to WordPress. Check site_url.")
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 401:
        print("❌ Authentication failed. Check username/password.")
    elif e.response.status_code == 404:
        print("❌ Endpoint not found. Check post type.")
    else:
        print(f"❌ Error {e.response.status_code}: {e.response.text}")
```

### Pattern: Configuration Validation

**Validate config before running:**
```python
def load_config(config_file):
    if not Path(config_file).exists():
        print("❌ Config file not found")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(config_file)

    required_fields = ['site_url', 'username', 'app_password']
    for field in required_fields:
        if field not in config['wordpress']:
            print(f"❌ Missing required field: {field}")
            sys.exit(1)

    return config
```

---

## Next Steps

### Level 1: Use This Tool
1. Follow the [QUICK_START.md](./QUICK_START.md) guide
2. Publish your first post
3. Try different post types (posts, pages, custom)
4. Experiment with AI-generated content

### Level 2: Customize This Tool
1. Add support for featured images
2. Add support for categories/tags
3. Add support for custom fields
4. Create a web UI (Flask/FastAPI)

### Level 3: Build Your Own Tool
1. Pick a platform with an API (Medium, Ghost, Notion, etc.)
2. Read their API documentation
3. Follow the architecture patterns from this tool
4. Start with read-only operations (GET requests)
5. Add write operations (POST/PUT requests)
6. Build a CLI tool
7. Add automation/scripting support

### Level 4: Build AI-Powered Workflows
1. Use Claude/ChatGPT to generate content
2. Use this tool (or your own) to publish
3. Create prompt templates for different content types
4. Automate the entire process (see `prompts/` directory)
5. Build feedback loops (content analytics → better prompts)

---

## Resources

### WordPress Development
- [WordPress REST API Handbook](https://developer.wordpress.org/rest-api/)
- [Gutenberg Block Editor Handbook](https://developer.wordpress.org/block-editor/)
- [WordPress Code Reference](https://developer.wordpress.org/reference/)

### Python Development
- [Python Requests Library](https://requests.readthedocs.io/)
- [Python Markdown Library](https://python-markdown.github.io/)
- [Python ConfigParser](https://docs.python.org/3/library/configparser.html)
- [Python argparse](https://docs.python.org/3/library/argparse.html)

### AI Content Generation
- [Claude API Documentation](https://docs.anthropic.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Building CLI Tools
- [Click (Python CLI Framework)](https://click.palletsprojects.com/)
- [Rich (Beautiful Terminal Output)](https://rich.readthedocs.io/)
- [Typer (Modern CLI Framework)](https://typer.tiangolo.com/)

---

## Questions to Explore

As you learn, consider these questions:

1. **How could you batch-publish multiple files at once?**
2. **How could you update existing posts instead of creating new ones?**
3. **How could you handle images in markdown (upload to WordPress)?**
4. **How could you add SEO metadata (meta descriptions, keywords)?**
5. **How could you schedule posts for future publication?**
6. **How could you sync content between WordPress sites?**
7. **How could you use AI to optimize content before publishing?**
8. **How could you build a feedback loop (publish → analytics → insights)?**

Experiment, break things, rebuild them. That's how you learn.

---

**Remember:** Every complex system is just a collection of simple patterns. Master the patterns, and you can build anything.

**Next:** Check out the [prompts/](./prompts/) directory to see the actual prompts used to generate content and build this tool.
