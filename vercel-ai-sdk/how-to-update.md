# How to Update Vercel AI SDK Documentation

This handbook documents the complete process for refreshing the Vercel AI SDK documentation from the official source.

## Overview

The documentation is sourced from `https://ai-sdk.dev/llms.txt`, a single file containing all documentation sections. This process:

1. Downloads the latest `llms.txt` file
2. Splits it into individual markdown files
3. Generates a flat index
4. Creates a two-level categorized index structure

## Prerequisites

- Python 3.9+
- `tiktoken` library (for token counting, optional)

```bash
pip3 install tiktoken
```

---

## Step 1: Download the Source File

Download the latest documentation from the official source:

```bash
cd /Users/szabvirag/projects/context/vercel-ai-sdk
curl -o llms.txt https://ai-sdk.dev/llms.txt
```

Verify the download:

```bash
wc -l llms.txt  # Should be ~30,000+ lines
wc -c llms.txt  # Should be ~1.2MB
```

---

## Step 2: Split into Individual Files

Run the split script to break `llms.txt` into individual markdown files:

```bash
python3 split-llms.py
```

This script:
- Parses YAML frontmatter blocks (delimited by `---`)
- Extracts the `title` from each section
- Converts titles to kebab-case filenames
- Handles duplicate titles by appending numbers
- Writes each section to a separate `.md` file

**Expected output:**
```
Found 126 sections
  Created: rag-agent.md
  Created: multi-modal-agent.md
  ...
Done! Created 126 files in /Users/szabvirag/projects/context/vercel-ai-sdk/split/
```

Move files to the main directory:

```bash
mv split/* .
rmdir split
```

---

## Step 3: Generate the Flat Index

Run the index generation script:

```bash
python3 generate_index.py
```

This creates `index.md` with all 125+ documents listed alphabetically, including:
- Title (as clickable link)
- Description
- Tags (if present)

---

## Step 4: Create the Two-Level Index Structure

The two-level index organizes documents into categories for easier navigation.

### Main Index: CLAUDE.md

Create the main index file that links to category indices:

```markdown
# Vercel AI SDK Documentation

Complete documentation for building AI-powered applications with the Vercel AI SDK.

---

## Categories

- [Getting Started](_index-getting-started.md)
- [Guides & Tutorials](_index-guides-tutorials.md)
- [AI SDK Core](_index-ai-sdk-core.md)
- [AI SDK UI](_index-ai-sdk-ui.md)
- [Agents](_index-agents.md)
- [Server Frameworks](_index-server-frameworks.md)
- [Providers - LLM](_index-providers-llm.md)
- [Providers - Media](_index-providers-media.md)
- [Error Reference](_index-error-reference.md)

---

## Overview

### [AI SDK by Vercel](ai-sdk-by-vercel.md)
### [Guides](guides.md)
### [Settings](settings.md)
### [DevTools](devtools.md)
```

### Category Index Files

Create an index file for each category. Files are prefixed with `_index-` to group them together.

| Category File | Contents |
|---------------|----------|
| `_index-getting-started.md` | Model-specific quickstart guides |
| `_index-guides-tutorials.md` | In-depth project tutorials |
| `_index-ai-sdk-core.md` | Core APIs: text, structured data, tools, embeddings |
| `_index-ai-sdk-ui.md` | React hooks: useChat, useCompletion, useObject |
| `_index-agents.md` | Agent building and configuration |
| `_index-server-frameworks.md` | Express, Hono, Fastify, Nest.js |
| `_index-providers-llm.md` | Language model providers |
| `_index-providers-media.md` | Speech, audio, image providers |
| `_index-error-reference.md` | All AI_*Error types |

### Category Mappings

Use these mappings to categorize documents:

**Getting Started** (pattern: `get-started-with-*`)
- get-started-with-claude-4.md
- get-started-with-gpt-5.md
- get-started-with-gemini-3.md
- get-started-with-deepseek-r1.md
- get-started-with-openai-o1.md
- openai-responses-api.md

**Guides & Tutorials** (tags: agent, rag, multi-modal)
- rag-agent.md
- multi-modal-agent.md
- slackbot-agent-guide.md
- natural-language-postgres.md
- google-gemini-image-generation.md

**AI SDK Core** (pattern: generating-*, tool-*, embed*, etc.)
- overview-1.md (AI SDK Core overview)
- generating-text.md
- generating-structured-data.md
- tool-calling.md
- embeddings.md
- image-generation.md
- transcription.md
- speech.md
- telemetry.md
- testing.md

**AI SDK UI** (pattern: chatbot-*, use* hooks)
- overview-2.md (AI SDK UI overview)
- chatbot.md
- chatbot-message-persistence.md
- chatbot-tool-usage.md
- completion.md
- object-generation.md
- generative-user-interfaces.md

**Agents**
- overview.md (agents overview)
- agents.md
- building-agents.md
- workflow-patterns.md
- loop-control.md
- configuring-call-options.md

**Server Frameworks** (tags: api servers)
- nodejs-http-server.md
- express.md
- hono.md
- fastify.md
- nestjs.md

**Providers - LLM** (major AI providers)
- openai.md, anthropic.md, google-*.md
- groq.md, mistral-ai.md, cohere.md
- deepseek.md, fireworks.md, together.md
- All OpenAI-compatible providers

**Providers - Media** (speech, audio, image)
- elevenlabs.md, lmnt.md, hume.md
- assemblyai.md, deepgram.md, gladia.md, revai.md
- fal.md, black-forest-labs.md, luma.md

**Error Reference** (pattern: `ai-*error.md`)
- All files matching `ai-*error.md`
- toolcallrepairerror.md

---

## Token Counts

After generation, verify token counts:

```bash
python3 << 'EOF'
import tiktoken
import glob

enc = tiktoken.get_encoding("cl100k_base")

# Main index
with open("CLAUDE.md", "r") as f:
    main_tokens = len(enc.encode(f.read()))
print(f"CLAUDE.md: {main_tokens:,} tokens")

# Category indices
total = main_tokens
for f in sorted(glob.glob("_index*.md")):
    with open(f, "r") as file:
        tokens = len(enc.encode(file.read()))
    total += tokens
    print(f"{f}: {tokens:,} tokens")

print(f"\nTotal index tokens: {total:,}")

# Full documentation
all_tokens = 0
for f in glob.glob("*.md"):
    with open(f, "r") as file:
        all_tokens += len(enc.encode(file.read()))
print(f"All documentation: {all_tokens:,} tokens")
EOF
```

**Expected totals:**
- Main index (CLAUDE.md): ~300 tokens
- All category indices: ~3,500 tokens
- Full documentation: ~295,000 tokens

---

## Quick Refresh Script

For a complete refresh, run:

```bash
#!/bin/bash
cd /Users/szabvirag/projects/context/vercel-ai-sdk

# 1. Download latest
curl -o llms.txt https://ai-sdk.dev/llms.txt

# 2. Remove old files (keep scripts and how-to)
find . -name "*.md" ! -name "how-to-update.md" -delete

# 3. Split into files
python3 split-llms.py
mv split/* .
rmdir split

# 4. Generate flat index
python3 generate_index.py

# 5. Manually review and update category indices if new docs added

echo "Done! Review CLAUDE.md and _index-*.md for any new documents."
```

---

## Maintenance Notes

1. **New documents**: After splitting, check for new files not in any category index
2. **Removed documents**: Check for broken links in category indices
3. **Renamed documents**: Update category indices if titles change
4. **New categories**: Create new `_index-{category}.md` and link from CLAUDE.md

To find uncategorized documents:

```bash
# List all .md files not in any index
comm -23 \
  <(ls *.md | grep -v "^_index" | grep -v "^CLAUDE" | grep -v "^index" | grep -v "^how-to" | sort) \
  <(grep -h "\.md)" _index*.md CLAUDE.md | sed 's/.*(\([^)]*\)).*/\1/' | sort -u)
```
