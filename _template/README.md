# [Skill Name]

Brief, one-sentence description of what this skill does and the problem it solves.

## What it does

Explain the core value proposition of the skill. When should a user invoke this? What does it improve?

- **Key feature 1**: Description
- **Key feature 2**: Description

## Use cases

- Example scenario 1
- Example scenario 2
- When *not* to use this skill

## Example prompts

- "Use the [skill-name] skill to..."
- "Help me [task] using [skill-name] guidelines..."

## Install

**Claude.ai**: zip the folder, not the files inside it, and upload the zip in **Customize > Skills**.

```bash
cd skills && zip -r skill-name.zip skill-name
```

**Claude Code**:

```bash
# The whole collection
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands

# Or this skill alone, from a clone
ln -s "$PWD/laiqiands-skills/skills/skill-name" ~/.claude/skills/skill-name
```

## Credits

If based on existing work, frameworks, or ideas, credit the original author here. Skill definition by [Author Name].