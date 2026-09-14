# Teach Me

Turns Claude into a one to one tutor instead of an explainer: it probes what you already hold, maps the subject as a dependency graph, then teaches one node at a time and makes you prove it stuck.

## What it does

Most explanations feel clear and are then forgotten.
Nodding along is recognition, and recognition feels like understanding without being it.
This skill is built to break that illusion.

- **It probes before it teaches**: eight to twelve questions that make you produce something, to find where you actually stop.
- **It maps the subject as a graph**: a Mermaid graph ordered by dependency and coloured by what you hold. You can be solid on promises and weak on the event loop underneath them.
- **One node per lesson**: never a concept whose prerequisites you do not hold.
- **Lessons that read like a class**: why the concept matters to your goal, the idea, a worked example with its real output, how it works, a diagram, the common mistakes and a summary, with two or three primary sources whose links were opened. The file still teaches you a month later.
- **You prove it**: explain from memory, predict an unseen case, or find the fault in a broken example. "It makes sense" is not evidence.
- **A page only when text is not enough**: a self-contained HTML page for something that moves, a state to step through or a knob to turn. The page shows, it never grades.
- **It picks up where you left off**: it reopens the map, re-probes something you learned a while ago, and teaches the next node.

## What you get

```
<subject>/
├── COURSE.md              why you are learning it, how you want it explained, what is out of scope
├── MAP.md                 the graph, one evidence line per node touched, the sources
└── lessons/
    ├── 0001-<slug>.md     the class, the check, and the verdict
    └── 0001-<slug>.html   only when the node has something the text cannot show
```

File names and headings are always English, so every course has the same shape.
What you read inside them is in your language.

## Use cases

- Learning a subject over weeks, without re-explaining your level every time
- Finding out what you actually know before you start studying
- Being quizzed on cases the explanation did not walk through
- Reviving a course you abandoned a month ago
- Not for a single factual answer. Ask the question directly instead.

## Example prompts

You start it by typing `/teach-me`.
Claude never starts it on its own, because a tutor that starts teaching whenever a question sounds like a question is a tutor that interrupts.

- "Teach me how the JavaScript event loop actually works"
- "I want to learn linear algebra for machine learning, start by working out what I already know"
- "Quiz me on what I said I understood last week"
- "Reopen my concurrency course and carry on"

## Design choices

- **State lives only in the graph.** The evidence list records what you produced, never whether a node is solid. A fact written in two places drifts.
- **The frontier is never stored.** It is derived from the graph, so it cannot go stale.
- **Pages copy a template instead of sharing a stylesheet.** A self-contained page cannot link one, and `references/lesson-template.html` keeps the pages looking like one course.

## Install

**Claude.ai**: zip the folder, not the files inside it, and upload the zip in **Customize > Skills**.
Needs code execution enabled in **Settings > Capabilities**, which is what lets Claude read the reference files and write the workspace.

```bash
cd skills && zip -r teach-me.zip teach-me
```

**Claude Code**:

```bash
# The whole collection
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands

# Or this skill alone, from a clone
ln -s "$PWD/laiqiands-skills/skills/teach-me" ~/.claude/skills/teach-me
```

## Credits

The workspace idea, the mission-first rule, the self-contained HTML lesson, and the equal-length answers rule come from the `teach` skill by [Matt Pocock](https://github.com/mattpocock).
The three-phase shape, the level triage, and the concept graph as a planning output come from personal notes by [Laiqian Ji](https://github.com/LaiqianDS).
The learning principles underneath are Bjork's storage strength against retrieval fluency, and Vygotsky's zone of proximal development.
