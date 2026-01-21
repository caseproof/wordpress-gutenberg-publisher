"""
Gutenberg Block Converter
Converts markdown content to WordPress Gutenberg blocks.

This preserves all formatting, links, and content structure.
"""

import re
import json
from typing import List
from markdown import markdown as md_to_html


def create_paragraph_block(content: str) -> str:
    """Create a properly formatted WordPress paragraph block."""
    return f'''<!-- wp:paragraph -->
<p>{content}</p>
<!-- /wp:paragraph -->'''


def create_heading_block(content: str, level: int = 2) -> str:
    """Create a properly formatted WordPress heading block."""
    return f'''<!-- wp:heading {{"level":{level}}} -->
<h{level}>{content}</h{level}>
<!-- /wp:heading -->'''


def create_list_block(content: str, ordered: bool = False) -> str:
    """Create a properly formatted WordPress list block."""
    attrs = json.dumps({"ordered": ordered}) if ordered else ""
    if attrs:
        attrs = " " + attrs
    return f'''<!-- wp:list{attrs} -->
{content}
<!-- /wp:list -->'''


def markdown_to_gutenberg(markdown_content: str) -> str:
    """Convert markdown content to WordPress Gutenberg blocks."""
    html_content = md_to_html(
        markdown_content,
        extensions=['extra', 'nl2br'],
        output_format='html5'
    )

    blocks = []

    # Process headings
    for match in re.finditer(r'<h([1-6])>(.*?)</h\1>', html_content, re.DOTALL):
        level = int(match.group(1))
        content = match.group(2)
        block = create_heading_block(content, level)
        blocks.append((match.start(), block))

    # Process paragraphs
    for match in re.finditer(r'<p>(.*?)</p>', html_content, re.DOTALL):
        content = match.group(1)
        if content.strip():
            block = create_paragraph_block(content)
            blocks.append((match.start(), block))

    # Process unordered lists
    for match in re.finditer(r'<ul>(.*?)</ul>', html_content, re.DOTALL):
        full_list = match.group(0)
        block = create_list_block(full_list, ordered=False)
        blocks.append((match.start(), block))

    # Process ordered lists
    for match in re.finditer(r'<ol>(.*?)</ol>', html_content, re.DOTALL):
        full_list = match.group(0)
        block = create_list_block(full_list, ordered=True)
        blocks.append((match.start(), block))

    # Process blockquotes
    for match in re.finditer(r'<blockquote>(.*?)</blockquote>', html_content, re.DOTALL):
        content = match.group(1)
        block = f'''<!-- wp:quote -->
<blockquote class="wp-block-quote">{content}</blockquote>
<!-- /wp:quote -->'''
        blocks.append((match.start(), block))

    # Process code blocks
    for match in re.finditer(r'<pre><code>(.*?)</code></pre>', html_content, re.DOTALL):
        content = match.group(1)
        block = f'''<!-- wp:code -->
<pre class="wp-block-code"><code>{content}</code></pre>
<!-- /wp:code -->'''
        blocks.append((match.start(), block))

    blocks.sort(key=lambda x: x[0])
    gutenberg_blocks = [block[1] for block in blocks]
    return '\n\n'.join(gutenberg_blocks)
