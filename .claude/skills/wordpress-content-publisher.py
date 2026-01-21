#!/usr/bin/env python3
"""
WordPress Content Publisher Skill

Generates content using AI templates and publishes to WordPress.
"""

import os
import json
from datetime import datetime

# Skill metadata
SKILL_NAME = "wordpress-content-publisher"
SKILL_DESCRIPTION = "Generate and publish content to WordPress (blog posts, landing pages, documentation)"
SKILL_ALIASES = ["/publish-content", "/wp-publish"]

def execute(context):
    """
    Main skill execution.
    
    This skill:
    1. Asks what type of content to create
    2. Gathers requirements via questions
    3. Generates markdown content
    4. Publishes to WordPress
    """
    
    # Step 1: Ask what type of content
    content_type = ask_content_type(context)
    
    # Step 2: Gather requirements based on type
    requirements = gather_requirements(context, content_type)
    
    # Step 3: Generate content
    markdown_content = generate_content(context, content_type, requirements)
    
    # Step 4: Preview and confirm
    if not confirm_content(context, markdown_content):
        return "Content generation cancelled."
    
    # Step 5: Publish to WordPress
    result = publish_to_wordpress(context, markdown_content, requirements)
    
    return result


def ask_content_type(context):
    """Ask user what type of content they want to create."""
    
    response = context.ask_user_question({
        "questions": [{
            "question": "What type of content do you want to create?",
            "header": "Content Type",
            "multiSelect": False,
            "options": [
                {
                    "label": "Blog Post",
                    "description": "SEO-optimized article with clear structure and actionable content"
                },
                {
                    "label": "Landing Page (Feature Overview)",
                    "description": "Grid-style page showcasing multiple features - like MemberPress features page"
                },
                {
                    "label": "Landing Page (Product Deep-Dive)",
                    "description": "Aspirational single-feature page with emotional appeal - like CoachKit page"
                },
                {
                    "label": "Product Features",
                    "description": "Showcase product capabilities with benefits and examples"
                },
                {
                    "label": "Documentation",
                    "description": "Technical how-to guide with code examples and troubleshooting"
                },
                {
                    "label": "Comparison Page",
                    "description": "Position your product vs. competitors or alternatives"
                }
            ]
        }]
    })
    
    return response["questions"][0]["answer"]


def gather_requirements(context, content_type):
    """Gather specific requirements based on content type."""
    
    requirements = {"content_type": content_type}
    
    if content_type == "Blog Post":
        response = context.ask_user_question({
            "questions": [
                {
                    "question": "What's the blog post topic or title?",
                    "header": "Topic",
                    "freeform": True
                },
                {
                    "question": "Who's the target audience?",
                    "header": "Audience",
                    "freeform": True
                },
                {
                    "question": "What's the primary keyword for SEO?",
                    "header": "Keyword",
                    "freeform": True
                },
                {
                    "question": "What tone should the article have?",
                    "header": "Tone",
                    "multiSelect": False,
                    "options": [
                        {"label": "Professional", "description": "Formal, authoritative, business-appropriate"},
                        {"label": "Casual", "description": "Conversational, friendly, approachable"},
                        {"label": "Technical", "description": "Detailed, precise, developer-focused"}
                    ]
                }
            ]
        })
        
        requirements.update({
            "topic": response["questions"][0]["answer"],
            "audience": response["questions"][1]["answer"],
            "keyword": response["questions"][2]["answer"],
            "tone": response["questions"][3]["answer"]
        })
    
    elif "Landing Page" in content_type:
        response = context.ask_user_question({
            "questions": [
                {
                    "question": "What's the product or service name?",
                    "header": "Product",
                    "freeform": True
                },
                {
                    "question": "What does it do? (brief description)",
                    "header": "Description",
                    "freeform": True
                },
                {
                    "question": "Who's the target audience?",
                    "header": "Audience",
                    "freeform": True
                },
                {
                    "question": "What's the main value proposition?",
                    "header": "Value Prop",
                    "freeform": True
                }
            ]
        })
        
        requirements.update({
            "product_name": response["questions"][0]["answer"],
            "description": response["questions"][1]["answer"],
            "audience": response["questions"][2]["answer"],
            "value_prop": response["questions"][3]["answer"]
        })
    
    # Add more content type gathering as needed
    
    return requirements


def generate_content(context, content_type, requirements):
    """Generate markdown content based on type and requirements."""
    
    # This would use the templates from prompts/ directory
    # For now, return a placeholder that the Claude agent will fill in
    
    prompt = f"""
Generate {content_type} content in markdown format.

Requirements:
{json.dumps(requirements, indent=2)}

Use the templates from prompts/landing-page-templates.md and prompts/content-generation-prompts.md as a guide.

Generate complete, high-quality markdown content that:
- Follows best practices for {content_type}
- Is SEO-optimized
- Has compelling headlines
- Includes clear CTAs
- Uses proper markdown formatting

Return ONLY the markdown content, no explanations.
"""
    
    # Return the prompt - Claude will execute this
    return prompt


def confirm_content(context, content_preview):
    """Show preview and ask for confirmation."""
    
    response = context.ask_user_question({
        "questions": [{
            "question": "Does this content look good? Ready to publish?",
            "header": "Confirm",
            "multiSelect": False,
            "options": [
                {"label": "Yes, publish it", "description": "Publish to WordPress as configured"},
                {"label": "Make changes", "description": "I want to adjust the content first"},
                {"label": "Cancel", "description": "Don't publish, cancel this workflow"}
            ]
        }]
    })
    
    answer = response["questions"][0]["answer"]
    
    if answer == "Cancel":
        return False
    elif answer == "Make changes":
        # Allow iteration
        return confirm_content(context, content_preview)  # Recursive
    else:
        return True


def publish_to_wordpress(context, markdown_content, requirements):
    """Publish the generated content to WordPress."""
    
    # Ask for publishing options
    response = context.ask_user_question({
        "questions": [
            {
                "question": "What post type should this be published as?",
                "header": "Post Type",
                "freeform": True,
                "default": "posts"
            },
            {
                "question": "What status?",
                "header": "Status",
                "multiSelect": False,
                "options": [
                    {"label": "draft", "description": "Save as draft (recommended - review before publishing)"},
                    {"label": "publish", "description": "Publish immediately (live on site)"}
                ]
            }
        ]
    })
    
    post_type = response["questions"][0]["answer"] or "posts"
    status = response["questions"][1]["answer"]
    
    # Save markdown to temporary file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"wp_content_{timestamp}.md"
    
    with open(filename, 'w') as f:
        f.write(markdown_content)
    
    # Call publish.py
    cmd = f"python3.11 publish.py {filename} --post-type {post_type} --status {status}"
    result = os.system(cmd)
    
    if result == 0:
        return f"✅ Published successfully to WordPress!\n\nCheck your WordPress dashboard to view the {status} {post_type}."
    else:
        return f"❌ Publishing failed. Check the error message above."


# Skill registration
if __name__ == "__main__":
    print(f"Skill: {SKILL_NAME}")
    print(f"Description: {SKILL_DESCRIPTION}")
    print(f"Aliases: {', '.join(SKILL_ALIASES)}")
