---
name: wp-quick-publish
description: Quickly publish existing markdown to WordPress
aliases:
  - /wp-quick
---

# WordPress Quick Publish

Publish existing markdown files to WordPress.

## Workflow

1. **Identify file** (show available or ask for path)
2. **Preview content** (`head -50 file.md`)
3. **Confirm** ("Ready to publish?")
4. **Gather options** (post type, status, slug via AskUserQuestion)
5. **Publish** (`python3.11 publish.py file.md --post-type TYPE --status STATUS`)

## Example

```
User: /wp-quick
You: Which file?
     - examples/simple-blog-post.md
     - generated/2024-01-21_landing-page_taskflow.md
User: examples/simple-blog-post.md
You: [Show preview]
     Ready to publish?
User: Yes
You: [Ask: post type, status, slug]
User: [Selects options]
You: [Run publish.py]
     ✅ Published! URL
```

## Notes

- Show preview before publishing
- Default to `draft` status
- Use `python3.11` for SSL compatibility
- Works with any post type (posts, pages, custom)

Simple and fast.
