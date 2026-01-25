#!/usr/bin/env python3
"""
Split llms.txt into individual markdown files named after the title in kebab-case.
Each section is delimited by --- frontmatter blocks.
"""

import re
import os
from typing import Optional, List, Tuple

def to_kebab_case(title: str) -> str:
    """Convert a title to kebab-case filename."""
    # Insert hyphen before uppercase letters that follow lowercase letters (camelCase)
    s = re.sub(r'([a-z])([A-Z])', r'\1-\2', title)
    # Insert hyphen before uppercase letters that are followed by lowercase (handle acronyms like APICall -> API-Call)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', s)
    # Remove special characters, keep alphanumeric, spaces, and hyphens
    s = re.sub(r'[^\w\s-]', '', s)
    # Replace spaces and underscores with hyphens, convert to lowercase
    s = re.sub(r'[\s_]+', '-', s.strip()).lower()
    # Remove consecutive hyphens
    s = re.sub(r'-+', '-', s)
    return s

def extract_title(frontmatter: str) -> Optional[str]:
    """Extract title from frontmatter content."""
    match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
    if match:
        return match.group(1).strip().strip('"\'')
    return None

def parse_sections(content: str) -> List[Tuple[str, str]]:
    """Parse the file into sections, each with frontmatter and body."""
    sections = []

    # Split by lines for easier processing
    lines = content.split('\n')
    i = 0
    n = len(lines)

    while i < n:
        # Look for start of frontmatter (--- on its own line)
        if lines[i].strip() == '---':
            frontmatter_start = i + 1

            # Find the closing ---
            frontmatter_end = None
            j = frontmatter_start
            while j < n:
                if lines[j].strip() == '---':
                    frontmatter_end = j
                    break
                j += 1

            if frontmatter_end is None:
                # No closing ---, skip
                i += 1
                continue

            # Extract frontmatter
            frontmatter = '\n'.join(lines[frontmatter_start:frontmatter_end])

            # Check if this looks like valid frontmatter (has title:)
            if 'title:' not in frontmatter:
                i += 1
                continue

            # Body starts after the closing ---
            body_start = frontmatter_end + 1

            # Find where this section ends (next --- that starts a frontmatter block)
            body_end = n
            k = body_start
            while k < n:
                if lines[k].strip() == '---':
                    # Check if this could be the start of new frontmatter
                    # Look ahead for title: within next few lines
                    lookahead = '\n'.join(lines[k:min(k+20, n)])
                    if re.search(r'^---\s*\ntitle:', lookahead, re.MULTILINE):
                        body_end = k
                        break
                k += 1

            # Extract body
            body = '\n'.join(lines[body_start:body_end]).strip()

            # Reconstruct the full section
            full_section = f"---\n{frontmatter}\n---\n\n{body}"

            title = extract_title(frontmatter)
            if title:
                sections.append((title, full_section))

            # Move to where the body ended
            i = body_end
        else:
            i += 1

    return sections

def split_llms_file(input_path: str, output_dir: str):
    """Split the llms.txt file into individual markdown files."""

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = parse_sections(content)

    print(f"Found {len(sections)} sections")

    # Track filenames to handle duplicates
    filename_counts = {}

    for title, section_content in sections:
        base_filename = to_kebab_case(title)

        # Handle duplicate filenames
        if base_filename in filename_counts:
            filename_counts[base_filename] += 1
            filename = f"{base_filename}-{filename_counts[base_filename]}.md"
        else:
            filename_counts[base_filename] = 0
            filename = f"{base_filename}.md"

        output_path = os.path.join(output_dir, filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(section_content)

        print(f"  Created: {filename}")

    print(f"\nDone! Created {len(sections)} files in {output_dir}/")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "llms.txt")
    output_dir = os.path.join(script_dir, "split")

    split_llms_file(input_file, output_dir)
