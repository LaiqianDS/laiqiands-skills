# Design With Me

Walks you through one design, step by step, across Claude Code and Claude Design: from a brief and a reference design system to a built interface with its own `DESIGN.md`.

## What it does

A design made in one prompt looks like every other design made in one prompt.
This skill slows the work down into six steps, and each step has a result you approve before the next one starts.

1. **Brief**: what you are designing, who uses it, the stack, and the real text, because filler text hides the real design.
2. **Reference**: you choose a design system from [Refero Styles](https://styles.refero.design/) or [getdesign.md](https://getdesign.md/), and Claude saves it as the starting `DESIGN.md`.
3. **Explore**: Claude writes the prompt for [Claude Design](https://claude.ai/design), where you compare directions before any code exists.
4. **Build**: Claude builds the chosen direction in your stack, and checks it against the Apple Human Interface Guidelines, accessibility, the empty, loading and error states, phone and desktop width, [React Bits](https://reactbits.dev/) for component behaviour, one icon family, and SVG where it fits.
5. **Polish**: a design review skill, `/hallmark` or `/impeccable:impeccable`, finds what looks generated.
6. **Record**: Claude rewrites `DESIGN.md` from the code that shipped.

You can skip a step, and Claude tells you what the design loses.

## What you get

```
DESIGN.md    the design system of what was built, with its sources and icon attribution
```

The interface itself is in your project, in your stack.

## Use cases

- Designing a landing page or an app screen from zero, with a real reference instead of a default look
- Redesigning a page and keeping a record of the system that came out
- Learning a repeatable design workflow with Claude Code and Claude Design
- Not for a single visual fix. Ask for the fix directly instead.

## Example prompts

You start it by typing `/design-with-me`.
Claude never starts it on its own, because a guided workflow that starts on each design question gets in the way.

- "Design the landing page for my note-taking app"
- "Redesign the settings screen of this project"
- "I have a DESIGN.md from getdesign.md, carry on from there"

## Design choices

- **The references are optional.** React Bits, Flaticon and SVG are checks, so the skill works in any stack and with no paid plan.
- **`DESIGN.md` is written twice.** The first one is the intention, and the last one is read from the code, because a plan that was never updated describes a design that does not exist.
- **One template for each `DESIGN.md`.** `references/design-template.md` gives the sections, so the file has the same shape when you skip the reference.
- **Video is not a step.** Hyperframes and Remotion render a video file, so they come after the design, and only when you ask for a video.
- **The review skills are not bundled.** `/hallmark` and `/impeccable:impeccable` are separate installs. Without them, Claude reviews against `DESIGN.md` by hand and tells you.

## Install

**Claude Code**:

```bash
# The whole collection
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands

# Or this skill alone, from a clone
ln -s "$PWD/laiqiands-skills/skills/design-with-me" ~/.claude/skills/design-with-me
```

**Claude.ai**: zip the folder, not the files inside it, and upload the zip in **Customize > Skills**.

```bash
cd skills && zip -r design-with-me.zip design-with-me
```
