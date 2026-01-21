---
name: wp-quick-publish
description: Quickly publish an existing markdown file to WordPress
aliases:
  - /wp-quick
---

# WordPress Quick Publish

Quickly publish existing markdown files to WordPress without content generation.

## When to Use This

Use this skill when you:
- Already have a markdown file to publish
- Want to skip content generation
- Need fast, simple publishing

Use `/wp-content` if you need to generate content first.

## Workflow

### Step 1: Identify the File

Ask the user which markdown file they want to publish:
- Let them provide the file path
- OR show files in `examples/` directory
- OR show any `.md` files in current directory

### Step 2: Preview the Content

Read and show a preview of the file:
```bash
head -50 filename.md
```

Ask: "Does this look correct? Ready to publish?"

### Step 3: Ask Publishing Options

Use AskUserQuestion to gather:
- **Post Type:** posts / pages / custom_post_type
- **Status:** draft (recommended) / publish
- **Custom Slug:** (optional)

### Step 4: Publish

Run the publishing command:
```bash
python3.11 publish.py [FILENAME] --post-type [TYPE] --status [STATUS] --slug [SLUG]
```

### Step 5: Confirm Success

Show the WordPress URL and status:
```
✅ Published successfully!
URL: https://yoursite.com/?p=123
Status: draft

Edit in WordPress: https://yoursite.com/wp-admin/post.php?post=123&action=edit
```

## Example Session

```
User: /wp-quick
You: I'll help you publish a markdown file to WordPress. Which file do you want to publish?

Options:
- examples/simple-blog-post.md
- examples/feature-overview-landing-page.md
- examples/product-feature-deep-dive.md
- Or provide a file path

User: examples/simple-blog-post.md
You: Here's a preview of the content:
[Show first 50 lines]

Ready to publish this?

User: Yes
You: Great! Publishing options:
[Ask for post type, status, slug via AskUserQuestion]

User: [Selects: pages, draft, custom-slug]
You: Publishing...
[Run publish.py]

You: ✅ Published successfully!
URL: https://yoursite.com/?page_id=123
```

## Important Notes

- Always show a preview before publishing
- Default to `draft` status for safety
- Use python3.11 for SSL compatibility
- Check that config.ini exists first

## Error Handling

If the file doesn't exist:
- Show available `.md` files in the directory
- Ask user to provide the correct path

If publishing fails:
- Show the error message
- Suggest checking config.ini
- Point to troubleshooting in README.md
