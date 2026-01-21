"""
WordPress REST API Client
Simple wrapper for publishing content to WordPress.
"""

import requests
import base64
from typing import Optional, Dict


class WordPressClient:
    """Simple WordPress REST API client for publishing content."""

    def __init__(self, site_url: str, username: str, app_password: str):
        """
        Initialize WordPress client.

        Args:
            site_url: WordPress site URL (e.g., https://example.com)
            username: WordPress username
            app_password: WordPress application password
        """
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.app_password = app_password

        # Create auth header
        credentials = f"{username}:{app_password}"
        token = base64.b64encode(credentials.encode()).decode()
        self.headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json"
        }

    def create_post(
        self,
        title: str,
        content: str,
        status: str = "draft",
        post_type: str = "posts",
        **kwargs
    ) -> Dict:
        """
        Create a new WordPress post.

        Args:
            title: Post title
            content: Post content (Gutenberg blocks)
            status: Post status (draft, publish, pending, private)
            post_type: Post type slug (posts, pages, or custom post type)
            **kwargs: Additional post fields (slug, excerpt, meta, etc.)

        Returns:
            WordPress API response

        Raises:
            requests.RequestException: If API call fails
        """
        endpoint = f"{self.site_url}/wp-json/wp/v2/{post_type}"

        post_data = {
            "title": title,
            "content": content,
            "status": status,
            **kwargs
        }

        response = requests.post(
            endpoint,
            json=post_data,
            headers=self.headers,
            timeout=30
        )

        if response.status_code not in [200, 201]:
            error_msg = f"WordPress API returned {response.status_code}"
            try:
                error_data = response.json()
                error_msg += f": {error_data.get('message', 'Unknown error')}"
            except:
                pass
            raise requests.RequestException(error_msg)

        return response.json()

    def update_post(
        self,
        post_id: int,
        title: Optional[str] = None,
        content: Optional[str] = None,
        status: Optional[str] = None,
        post_type: str = "posts",
        **kwargs
    ) -> Dict:
        """
        Update an existing WordPress post.

        Args:
            post_id: WordPress post ID
            title: New title (optional)
            content: New content (optional)
            status: New status (optional)
            post_type: Post type slug
            **kwargs: Additional fields to update

        Returns:
            WordPress API response
        """
        endpoint = f"{self.site_url}/wp-json/wp/v2/{post_type}/{post_id}"

        post_data = {}
        if title:
            post_data["title"] = title
        if content:
            post_data["content"] = content
        if status:
            post_data["status"] = status
        post_data.update(kwargs)

        response = requests.post(
            endpoint,
            json=post_data,
            headers=self.headers,
            timeout=30
        )

        if response.status_code != 200:
            raise requests.RequestException(
                f"WordPress API returned {response.status_code}"
            )

        return response.json()

    def get_post(self, post_id: int, post_type: str = "posts") -> Dict:
        """Get a post by ID."""
        endpoint = f"{self.site_url}/wp-json/wp/v2/{post_type}/{post_id}"
        response = requests.get(endpoint, headers=self.headers, timeout=10)

        if response.status_code != 200:
            raise requests.RequestException(
                f"WordPress API returned {response.status_code}"
            )

        return response.json()

    def list_posts(
        self,
        post_type: str = "posts",
        per_page: int = 10,
        page: int = 1
    ) -> list:
        """List posts."""
        endpoint = f"{self.site_url}/wp-json/wp/v2/{post_type}"
        params = {"per_page": per_page, "page": page}

        response = requests.get(
            endpoint,
            headers=self.headers,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            raise requests.RequestException(
                f"WordPress API returned {response.status_code}"
            )

        return response.json()
