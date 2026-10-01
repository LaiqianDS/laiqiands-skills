---
name: design-with-me
description: Guide a design step by step across Claude Code and Claude Design, from a brief and a reference DESIGN.md to a built interface with its own DESIGN.md. Use when someone wants to design or redesign a page, an app screen or a component set and wants to be walked through it. Not for a single visual fix.
disable-model-invocation: true
argument-hint: "What do you want to design?"
---

# Design With Me

Guide one design from a brief to a built interface, one step at a time.
Decide first, then build, then polish, then record.
Every design starts from a `DESIGN.md` and ends with a `DESIGN.md` that describes what was built.

## Rules

- **One step at a time.** Say which step you are on and where it happens, do it, show the result, and get a yes before the next step.
- **The user can skip a step.** Say in one line what the design loses, then move on.
- **The checks are references, not requirements.** No step forces a library, a stack or a paid plan on the project.
- **Say what you could not open.** If a page does not load, tell the user. Never report a guideline or a licence as checked from memory.
- **Other tools are the user's.** You cannot operate Claude Design or a browser gallery. Write what the user must paste there, then wait for what they bring back.

## The steps

| # | Step | Where | Leaves |
|---|---|---|---|
| 1 | Brief | Claude Code | The opening of `DESIGN.md` |
| 2 | Reference | Browser, then Claude Code | The starting `DESIGN.md` |
| 3 | Explore | Claude Design | An approved direction |
| 4 | Build | Claude Code | The interface in code |
| 5 | Polish | Claude Code | Fixes applied |
| 6 | Record | Claude Code | The final `DESIGN.md` |

`DESIGN.md` lives beside the design it describes: the project root when the project is one design, the design's own directory when there are more.
If a `DESIGN.md` is already there, read it and start at the first step it does not cover.

### 1. Brief

Ask at most three questions: what is being designed, who uses it and for what, and the stack it must run on.
Read the project before you ask, and do not ask what the code already answers.

Then get the real content: the headline, the main actions, and the text of each section, or the source to take them from.
A design made around filler text changes when the real text arrives.

Done when you can say in two lines what the design is for, the user agrees, and you have the real content or know where it comes from.

### 2. Reference

Ask the user to choose a design system close to the feeling they want, from one of these galleries:

- [Refero Styles](https://styles.refero.design/)
- [getdesign.md](https://getdesign.md/)

Save the file they bring back as `DESIGN.md`, and put the brief from step 1 at the top.
If the user skips the reference, start `DESIGN.md` from `references/design-template.md` and fill only what the brief decides.
Then name what must change so the design is not a copy of another brand: at least the accent colour, the typeface, or the voice.
A reference gives a system to start from, not an identity to borrow.

Done when `DESIGN.md` exists and the user has agreed what to keep and what to change.

### 3. Explore

This step happens in [Claude Design](https://claude.ai/design), where it is cheap to compare directions before any code exists.
Write a prompt for the user to paste there. It has:

- the brief, in two lines
- the content of `DESIGN.md`, or the instruction to attach it
- the screens or states to draw
- a request for two or three directions that differ in layout, not only in colour

The user iterates there, chooses one direction, and sends it back with the hand off to Claude Code or as exported HTML.
Read what comes back, and update `DESIGN.md` with each decision that changed.

If the user has no access to Claude Design, skip the step and say that the build starts without a compared direction.

Done when one direction is chosen and `DESIGN.md` agrees with it.

### 4. Build

Build the chosen direction in the project's stack, with the tokens from `DESIGN.md` and the real content from step 1.
Never ship filler text: if a text is missing, ask for it or write a real draft and mark it for the user.
Go through these checks while you build, and tell the user which ones changed something.

- **Platform guidelines.** Open the pages of the [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) for the patterns this design uses, such as navigation, forms, modals or feedback. Apply what holds on the target platform: touch target size, hierarchy, clear feedback for each action.
- **Accessibility.** Text contrast of at least 4.5 to 1, a visible focus on each control, and each action reachable with the keyboard. This holds on each platform.
- **States.** Design the empty, loading and error state of each view that has data, not only the full one.
- **Sizes.** Look at the design at phone width, about 400px, and at desktop width. Nothing scrolls sideways and nothing overlaps.
- **Components.** Look at [React Bits](https://reactbits.dev/) for how a component of this type can move and respond. Use it as a reference in any stack, and install from it only when the project is React and the user agrees.
- **Motion on the page.** Add animation only where it explains a change of state, shows a relation, or confirms an action. Honour `prefers-reduced-motion`.
- **Icons.** Use one icon family for the whole design. [Flaticon](https://www.flaticon.com/) is a place to find one. Check the licence of each icon before it ships, and record the attribution it asks for.
- **SVG.** Prefer SVG for icons, logos and illustrations, because it stays sharp at each size. Keep raster formats for photographs.

Done when the interface runs, the user has seen it at both widths, and each check is passed or refused by the user.

### 5. Polish

Run a design review skill on what was built: `/hallmark` or `/impeccable:impeccable`.
Both find the patterns that make a design look generated, such as default gradients, cards inside cards, and the same radius and shadow on every element.
Start the skill when it is installed.
If neither is installed, tell the user, and review against `DESIGN.md` by hand.

Apply the fixes the user accepts.

Done when the review has run and each finding is fixed or refused by the user.

### 6. Record

Rewrite `DESIGN.md` from the code that shipped, not from the plan.
Read the real values: colours, type scale, spacing, radii, components, motion.
Keep the section headings the reference came with, so the file still works as input for an agent.
Read `references/design-template.md` and add each section the file does not have yet.
`## Sources` is always there, and it is the last section.

Done when a new agent could rebuild the look of the design from `DESIGN.md` alone.

## Video

A promotional or demo video is a different job from motion on the page.
When the user asks for one, do it after step 6, with a video skill such as `/hyperframes` or a Remotion skill, and give it `DESIGN.md` so the video matches the design.
Both render a video file, so do not use them for animation inside the interface.
