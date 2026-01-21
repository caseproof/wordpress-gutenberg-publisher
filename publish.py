#!/usr/bin/env python3
"""
WordPress Gutenberg Publisher - CLI Tool

Converts markdown to Gutenberg blocks and publishes to WordPress.

Usage:
    python publish.py content.md                    # Interactive mode
    python publish.py content.md --status publish   # Direct publish
    python publish.py content.md --post-type pages  # Publish as page
"""

import sys
import argparse
import configparser
from pathlib import Path

from gutenberg_converter import markdown_to_gutenberg
from wordpress_client import WordPressClient


def load_config(config_file: str = "config.ini") -> dict:
    """Load WordPress configuration from INI file."""
    config_path = Path(config_file)

    if not config_path.exists():
        print(f"❌ Config file not found: {config_file}")
        print("   Copy config.example.ini to config.ini and add your credentials")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(config_path)

    if 'wordpress' not in config:
        print("❌ [wordpress] section not found in config.ini")
        sys.exit(1)

    return {
        'site_url': config['wordpress']['site_url'],
        'username': config['wordpress']['username'],
        'app_password': config['wordpress']['app_password']
    }


def read_markdown_file(file_path: str) -> tuple:
    """
    Read markdown file and extract title + content.

    Assumes first H1 is the title, rest is content.
    """
    path = Path(file_path)

    if not path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    content = path.read_text(encoding='utf-8')

    # Try to extract title from first H1
    lines = content.split('\n')
    title = None

    for i, line in enumerate(lines):
        if line.startswith('# '):
            title = line[2:].strip()
            # Remove title from content
            content = '\n'.join(lines[i+1:]).strip()
            break

    if not title:
        title = path.stem.replace('-', ' ').replace('_', ' ').title()

    return title, content


def interactive_publish(
    wp_client: WordPressClient,
    title: str,
    gutenberg_content: str
):
    """Interactive mode - ask user for publish options."""
    print("\n" + "="*80)
    print(f"📄 Title: {title}")
    print(f"📏 Content length: {len(gutenberg_content)} characters")
    print("="*80 + "\n")

    # Ask for post type
    post_type = input("Post type (posts/pages/custom-type) [posts]: ").strip()
    if not post_type:
        post_type = "posts"

    # Ask for status
    status = input("Status (draft/publish/pending/private) [draft]: ").strip()
    if not status:
        status = "draft"

    # Ask for slug
    slug = input("URL slug (leave empty for auto-generate): ").strip()

    # Confirm
    print(f"\n✅ Ready to publish:")
    print(f"   Type: {post_type}")
    print(f"   Status: {status}")
    print(f"   Slug: {slug or '(auto-generated)'}")

    confirm = input("\nContinue? (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ Cancelled")
        sys.exit(0)

    # Publish
    kwargs = {}
    if slug:
        kwargs['slug'] = slug

    try:
        result = wp_client.create_post(
            title=title,
            content=gutenberg_content,
            status=status,
            post_type=post_type,
            **kwargs
        )

        print(f"\n🎉 Published successfully!")
        print(f"   ID: {result['id']}")
        print(f"   URL: {result['link']}")
        print(f"   Edit: {result['link'].rstrip('/')}/wp-admin/post.php?post={result['id']}&action=edit")

    except Exception as e:
        print(f"\n❌ Publishing failed: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Publish markdown content to WordPress as Gutenberg blocks'
    )
    parser.add_argument('file', help='Markdown file to publish')
    parser.add_argument('--config', default='config.ini', help='Config file path')
    parser.add_argument('--status', choices=['draft', 'publish', 'pending', 'private'],
                        help='Post status (default: interactive)')
    parser.add_argument('--post-type', default='posts', help='Post type')
    parser.add_argument('--slug', help='URL slug')
    parser.add_argument('--title', help='Override title from file')

    args = parser.parse_args()

    print("🚀 WordPress Gutenberg Publisher\n")

    # Load config
    print("📝 Loading configuration...")
    config = load_config(args.config)

    # Read markdown file
    print(f"📖 Reading {args.file}...")
    title, markdown_content = read_markdown_file(args.file)

    if args.title:
        title = args.title

    # Convert to Gutenberg
    print("🔄 Converting to Gutenberg blocks...")
    gutenberg_content = markdown_to_gutenberg(markdown_content)

    # Initialize WordPress client
    wp_client = WordPressClient(
        site_url=config['site_url'],
        username=config['username'],
        app_password=config['app_password']
    )

    # Interactive or direct mode
    if args.status:
        # Direct mode
        kwargs = {}
        if args.slug:
            kwargs['slug'] = args.slug

        try:
            result = wp_client.create_post(
                title=title,
                content=gutenberg_content,
                status=args.status,
                post_type=args.post_type,
                **kwargs
            )

            print(f"\n🎉 Published successfully!")
            print(f"   ID: {result['id']}")
            print(f"   URL: {result['link']}")

        except Exception as e:
            print(f"\n❌ Publishing failed: {e}")
            sys.exit(1)
    else:
        # Interactive mode
        interactive_publish(wp_client, title, gutenberg_content)


if __name__ == '__main__':
    main()
