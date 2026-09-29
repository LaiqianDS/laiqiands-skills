# Cold Email

Generate cold emails, DMs, and follow-up sequences framed around the recipient.

## What it does

When you ask Claude to write a cold email, DM, or outreach message, this skill kicks in and enforces a proven framework:

- **Five-line structure**: Hook, why them, your offer, low-friction CTA, sign off
- **Recipient-framed**: Every sentence passes the "so what?" test from their perspective
- **Platform-aware**: Adjusts tone and length for email, Twitter/X DM, LinkedIn, investor outreach
- **Follow-up sequences**: Day 3, Day 7, Day 14+ cadence with escalation logic
- **Research-driven**: When you provide a URL or profile, Claude extracts personalization hooks

## Use cases

- B2B sales outreach
- Job applications and networking
- Investor emails (pre-seed, seed)
- Scholarship and funding requests
- Reaching busy/famous people
- Cold DMs on Twitter/X and LinkedIn
- Follow-up sequences

## Example prompts

- "Write a cold email to the CTO of [company] pitching my AI consulting services"
- "Help me DM this VC on Twitter. I have 500 users and $8k MRR."
- "I need to email my university asking for more scholarship money"
- "Draft a follow-up sequence for my outreach to [person]"

## Install

**Claude.ai**: zip the folder, not the files inside it, and upload the zip in **Customize > Skills**.

```bash
cd skills && zip -r cold-email.zip cold-email
```

**Claude Code**:

```bash
# The whole collection
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands

# Or this skill alone, from a clone
ln -s "$PWD/laiqiands-skills/skills/cold-email" ~/.claude/skills/cold-email
```

## Credits

Framework based on [Adrianna Lakatos's cold email thread](https://x.com/adriannalakatos) combined with established outreach principles (Sahil Bloom, PAS, AIDA).
