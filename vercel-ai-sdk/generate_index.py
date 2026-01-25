#!/usr/bin/env python3
"""
Generate an index.md file for Vercel AI SDK documentation.
Reads all markdown files, extracts frontmatter, and creates a clean index.
"""

import os
import re
from pathlib import Path


def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    frontmatter = {}

    # Check if content starts with frontmatter delimiter
    if not content.startswith('---'):
        return frontmatter

    # Find the closing delimiter
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return frontmatter

    frontmatter_text = content[3:end_match.start() + 3]

    # Extract title
    title_match = re.search(r'^title:\s*(.+)$', frontmatter_text, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        # Remove quotes if present
        if (title.startswith('"') and title.endswith('"')) or \
           (title.startswith("'") and title.endswith("'")):
            title = title[1:-1]
        frontmatter['title'] = title

    # Extract description
    desc_match = re.search(r'^description:\s*(.+)$', frontmatter_text, re.MULTILINE)
    if desc_match:
        description = desc_match.group(1).strip()
        # Remove quotes if present
        if (description.startswith('"') and description.endswith('"')) or \
           (description.startswith("'") and description.endswith("'")):
            description = description[1:-1]
        frontmatter['description'] = description

    # Extract tags - handle both inline array and multi-line array formats
    # Format 1: tags: ['tag1', 'tag2']
    # Format 2: tags:\n  [\n    'tag1',\n    'tag2',\n  ]
    # Format 3: tags:\n  - tag1\n  - tag2

    tags = []

    # Try inline array format: tags: ['tag1', 'tag2']
    inline_tags_match = re.search(r'^tags:\s*\[([^\]]+)\]', frontmatter_text, re.MULTILINE)
    if inline_tags_match:
        tags_str = inline_tags_match.group(1)
        # Extract quoted strings
        tags = re.findall(r"'([^']+)'|\"([^\"]+)\"", tags_str)
        tags = [t[0] or t[1] for t in tags]
    else:
        # Try multi-line array format
        multiline_match = re.search(r'^tags:\s*\n\s*\[(.*?)\]', frontmatter_text, re.MULTILINE | re.DOTALL)
        if multiline_match:
            tags_str = multiline_match.group(1)
            tags = re.findall(r"'([^']+)'|\"([^\"]+)\"", tags_str)
            tags = [t[0] or t[1] for t in tags]
        else:
            # Try YAML list format: - tag1\n  - tag2
            yaml_list_match = re.search(r'^tags:\s*\n((?:\s*-\s*.+\n?)+)', frontmatter_text, re.MULTILINE)
            if yaml_list_match:
                tags_block = yaml_list_match.group(1)
                tags = re.findall(r'-\s*(.+)', tags_block)
                tags = [t.strip().strip("'\"") for t in tags]

    if tags:
        frontmatter['tags'] = tags

    return frontmatter


def generate_index(split_dir: Path) -> str:
    """Generate the index markdown content."""

    # Get all markdown files except index.md
    md_files = sorted([
        f for f in split_dir.glob('*.md')
        if f.name != 'index.md' and f.name != 'generate_index.py'
    ])

    # Collect file data
    entries = []
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter = extract_frontmatter(content)
        entries.append({
            'filename': md_file.name,
            'title': frontmatter.get('title', md_file.stem.replace('-', ' ').title()),
            'description': frontmatter.get('description', ''),
            'tags': frontmatter.get('tags', [])
        })

    # Sort alphabetically by filename
    entries.sort(key=lambda x: x['filename'].lower())

    # Build the index content
    lines = [
        '# Vercel AI SDK Documentation Index',
        '',
        'This index provides a comprehensive overview of the Vercel AI SDK documentation. Each entry includes the document title, description, and relevant tags to help you quickly find the information you need for building AI-powered applications.',
        '',
        '---',
        '',
    ]

    for entry in entries:
        # Title as link
        lines.append(f"## [{entry['title']}]({entry['filename']})")
        lines.append('')

        # Description
        if entry['description']:
            lines.append(f"{entry['description']}")
            lines.append('')

        # Tags
        if entry['tags']:
            tags_formatted = ' '.join([f'`{tag}`' for tag in entry['tags']])
            lines.append(f"**Tags:** {tags_formatted}")
            lines.append('')

        lines.append('---')
        lines.append('')

    return '\n'.join(lines)


def main():
    split_dir = Path(__file__).parent

    index_content = generate_index(split_dir)

    index_path = split_dir / 'index.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Index generated: {index_path}")
    print(f"Total files indexed: {len(list(split_dir.glob('*.md'))) - 1}")


if __name__ == '__main__':
    main()
