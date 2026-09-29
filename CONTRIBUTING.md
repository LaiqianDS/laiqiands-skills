# Contributing

Bug reports, fixes to existing skills and new skills are all welcome.

- **A skill gives a bad result:** open an issue with the prompt you used and the output you got.
- **Docs:** fix typos, add examples, or clarify instructions in a pull request.
- **A new skill:** open an issue first, see [Proposing a new skill](#proposing-a-new-skill).

## Anatomy of a Skill
Every skill lives in its own directory under `skills/` and adheres to the Agent Skills standard:

```
skills/
└── skill-name/       # Directory must be named after the skill (kebab-case)
    ├── SKILL.md      # Required. The Claude prompt containing YAML frontmatter
    ├── README.md     # Required. Instructions for human users on how to use it
    └── references/   # Optional. Extra markdown the model reads only when it needs it
```

Keep the body of `SKILL.md` under 5k tokens, which is the budget Anthropic documents for it.
It loads in full every time the skill triggers, so anything that only one branch of the skill needs belongs in `references/` with an explicit instruction in `SKILL.md` telling the model when to read it.
A reference file nobody is told to open never gets opened.

The `skills/` directory is the plugin's source.
Anything you put there ships to everyone who installs the plugin, so nothing else belongs in it.
The `_template/` folder sits outside `skills/` on purpose, which is what keeps it from installing as a real skill.

## Proposing a New Skill
1. **Open an Issue:** Before spending time building out a complex skill or porting existing knowledge bases, open an Issue or Discussion to see if it aligns with the goals of this repo and isn't a duplicate.
2. **Copy the Template:** Copy `_template/` into `skills/` and rename it to your skill idea.
3. **Write the SKILL.md:** Include the required YAML frontmatter (with `name` and `description`). Write clear, structured instructions mapping out the behavioral adjustments or knowledge. Keep the instructions directed at the AI agent (Claude).
4. **Write the README.md:** Write instructions directed at the human user explaining the value it gives, trigger examples, and how it works under the hood.

You do not need to register the skill anywhere.
The plugin discovers every directory in `skills/` automatically, so `plugin.json` never has to change.

### The `SKILL.md` Frontmatter Requirement
To ensure the skill imports cleanly into Claude.ai, your `SKILL.md` must start with the following YAML frontmatter:

```yaml
---
name: your-skill-name
description: Explicit trigger conditions and details stating exactly when Claude should utilize this skill.
---
```

The `name` must match the directory name exactly.
CI fails the build when they differ.

## Validation
Run these three checks before opening a PR.
CI runs the same ones on every pull request.

```bash
claude plugin validate . --strict      # marketplace and plugin manifests
claude plugin validate skills --strict # frontmatter of every skill
python3 scripts/check_skill_names.py   # name matches directory, no orphan directories
```

The first two need the Claude Code CLI.
The third needs only Python 3, with no packages to install.

## Pull Request Process
1. Fork the repository and create your feature branch from `main`.
2. Run the validation checks above and fix anything they report.
3. Submit a Pull Request. Ensure the description clearly outlines the changes made and the problem the skill addresses.
4. Wait for a review.

## Code of Conduct
Be respectful in issues and pull requests.
