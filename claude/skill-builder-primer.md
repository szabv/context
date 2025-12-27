# Skill Builder Primer

Quick reference for building Claude Code skills.

## What is a Skill?

A skill is a package of instructions, resources, and optional code that gives Claude specialized capabilities. Skills are auto-discovered based on their description and loaded progressively to optimize token usage.

## Minimal Skill Structure

```
~/.claude/skills/my-skill/
└── SKILL.md              # Required: Instructions with YAML frontmatter
```

## Full Skill Structure

```
~/.claude/skills/my-skill/
├── SKILL.md              # Required: Main instructions
├── REFERENCE.md          # Optional: Detailed reference docs
├── scripts/              # Optional: Python/JS utilities
│   └── helper.py
└── resources/            # Optional: Data files, schemas, templates
    ├── schema.yaml
    └── template.md
```

## SKILL.md Format

```yaml
---
name: my-skill-name
description: What this skill does and when Claude should use it (max 1024 chars)
---

# Skill Title

## When This Skill Applies
- Trigger conditions (user mentions X, provides Y, asks for Z)

## Instructions
Step-by-step guidance for Claude

## Input Format
What the skill expects

## Output Format
What the skill produces

## Examples
Concrete usage examples
```

## Naming Rules

- **name**: max 64 chars, lowercase + hyphens only, no "anthropic" or "claude"
- **description**: max 1024 chars, must describe WHAT it does and WHEN to use it

## Progressive Loading (3 Levels)

1. **Metadata** (~100 tokens) - Always loaded at startup (name + description)
2. **Instructions** (<5K tokens) - Loaded when skill is triggered (SKILL.md body)
3. **Resources** (unlimited) - Loaded on demand (REFERENCE.md, scripts, resources/)

## Skill Locations

| Location | Scope |
|----------|-------|
| `~/.claude/skills/` | User-level, all projects |
| `.claude/skills/` | Project-level, this repo only |

## Key Principles

1. **Auto-Discovery**: Claude finds skills by matching user requests to descriptions
2. **Self-Contained**: Skills should work without external dependencies
3. **Progressive**: Load only what's needed, when needed
4. **Deterministic**: Scripts execute without loading code into context

## Useful Resources

| Resource | Location | Description |
|----------|----------|-------------|
| Skills Cookbook | `context/claude/skills-cookbook/` | Production-ready examples |
| Agent Skills Docs | `context/claude/agent-skills.md` | Comprehensive architecture docs |
| Example: Financial Analysis | `skills-cookbook/custom_skills/analyzing-financial-statements/` | Real skill example |
| Example: Brand Guidelines | `skills-cookbook/custom_skills/applying-brand-guidelines/` | Instruction-focused example |

## Quick Checklist

- [ ] SKILL.md exists with valid YAML frontmatter
- [ ] Description explains WHAT and WHEN
- [ ] Instructions are clear and actionable
- [ ] Examples show concrete usage
- [ ] Resources are referenced (not duplicated in SKILL.md)
- [ ] Total SKILL.md body < 5K tokens

## Example: build-plan-decomposer

A real skill at `~/.claude/skills/build-plan-decomposer/`:

```
build-plan-decomposer/
├── SKILL.md                          # 6-phase decomposition workflow
├── REFERENCE.md                      # Full mechanical decision system
└── resources/
    ├── schemas/                      # TaskCard, VerificationItem schemas
    ├── taxonomy/                     # Subsystem taxonomy, guardrails
    ├── decision-system/              # Points formula, split strategies
    └── examples/                     # Worked decision traces
```

Key design choices:
- Frontmatter triggers on "decompose", "break down", "parallel tasks"
- SKILL.md contains workflow overview (~350 lines)
- REFERENCE.md has full details (loaded on demand)
- Resources contain YAML schemas (loaded when validating output)