# How to Build This Tool (Meta-Prompts)

This document shows the actual prompts used to build this WordPress Gutenberg Publisher tool. Use these as templates for building your own tools with AI assistance.

## Initial Project Prompt

```
I need to build a WordPress publishing tool that:
1. Takes markdown content (from files or AI-generated)
2. Converts it to WordPress Gutenberg blocks
3. Publishes to WordPress via REST API

Requirements:
- Python-based CLI tool
- Support posts, pages, and custom post types
- Interactive mode (for beginners) and script mode (for automation)
- WordPress Application Password authentication
- Simple, educational code

Create the basic project structure and core files.
```

## Core Implementation Prompts

### Gutenberg Converter

```
Create gutenberg_converter.py that:
1. Takes markdown content as input
2. Converts markdown to HTML using Python's markdown library
3. Wraps HTML elements in Gutenberg block comments
4. Preserves all links and formatting (critical!)
5. Handles: headings, paragraphs, lists, blockquotes, code blocks

IMPORTANT: Use regex pattern matching, NOT HTML parsing libraries.
HTML parsers strip or modify content. We need to preserve everything exactly.

Example output:
<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Title</h1>
<!-- /wp:heading -->
```

### WordPress Client

```
Create wordpress_client.py that wraps the WordPress REST API.

Requirements:
- Class-based design (WordPressClient)
- Constructor: site_url, username, app_password
- Authentication via Basic Auth (Base64-encoded)
- Methods: create_post, update_post, delete_post, get_post
- Proper error handling (401, 404, connection errors)
- Timeout handling (30 seconds default)

Return full JSON response from WordPress API.
```

### CLI Tool

```
Create publish.py - main CLI entry point.

Features:
1. Interactive Mode (default):
   - Prompt for: post type, status, slug
   - Show preview before publishing
   - Ask for confirmation

2. Direct Mode (command-line arguments):
   - --status, --post-type, --slug, --title

Workflow:
1. Load config from config.ini
2. Read markdown file (extract title from first H1)
3. Convert to Gutenberg blocks
4. Publish to WordPress
5. Show success message with URL

Use argparse for CLI arguments and emoji for UX.
```

## Testing Prompt

```
Test this tool on a real WordPress site with:
- Standard posts
- Custom post type (e.g., ht_kb for Heroic KB)
- Verify all links are preserved
- Check content renders correctly in Gutenberg

If anything fails, debug and fix it.
```

## Fixing Issues Prompt

```
The content is publishing but:
1. Links are being stripped
2. Content truncates mid-paragraph
3. Block comments show as visible text

I have a working reference at /path/to/project that uses:
- Simple regex wrapping (no parsing)
- Preserves everything exactly as-is

Rewrite gutenberg_converter.py to use that approach.
```

## Documentation Prompts

```
Create comprehensive documentation:

1. LEARNING_GUIDE.md:
   - Core concepts (Gutenberg, markdown, REST API)
   - System architecture
   - Content flow trace
   - Technical decisions and rationale
   - Building your own tools
   - Common patterns
   - Progressive learning path (levels 1-4)

2. Prompt templates in prompts/ directory:
   - Generic blog post generator
   - Landing page generator
   - Technical documentation generator
   - SEO optimizer
   - Social media posts

Include examples, code snippets, and best practices.
Target audience: junior developers.
```

## Key Prompt Writing Principles

### ✅ DO:
- Be specific about input/output
- Specify libraries/frameworks
- Include example output
- Explain *why* for non-obvious constraints
- Provide test cases
- Reference working implementations

### ❌ DON'T:
- Be vague ("make it better")
- Assume AI knows your context
- Skip error handling
- Forget authentication details
- Ignore edge cases

## Adapting for Your Own Tools

**Template:**
```
I need to build a [TYPE] tool that:
1. [INPUT/SOURCE]
2. [TRANSFORMATION/PROCESSING]
3. [OUTPUT/DESTINATION]

Requirements:
- [LANGUAGE/FRAMEWORK]
- [KEY FEATURES]
- [CONSTRAINTS]
- [AUDIENCE/USE CASE]

Architecture:
- [COMPONENT 1]: [RESPONSIBILITY]
- [COMPONENT 2]: [RESPONSIBILITY]
- [COMPONENT 3]: [RESPONSIBILITY]

Create [DELIVERABLE].
```

## Example Adaptations

**Ghost Publishing:**
```
I need to build a Python CLI tool that:
1. Takes markdown content
2. Converts to Ghost's Mobiledoc format
3. Publishes to Ghost via Admin API
[... requirements ...]
```

**Medium Publishing:**
```
I need to build a Node.js tool that:
1. Takes markdown content
2. Converts to Medium's JSON format
3. Publishes to Medium via Integration API
[... requirements ...]
```

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Claude Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

**Remember:** Building with AI is iterative. Start broad, drill into details, test often, document as you go.

Good prompts are: **Clear** (specific requirements), **Complete** (all context), **Concrete** (examples), **Collaborative** (build → test → refine).
