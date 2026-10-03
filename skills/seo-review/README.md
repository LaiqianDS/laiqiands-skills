# SEO Review

Reviews a website against 23 fixed SEO checks, writes the result with evidence, then fixes the failures you accept.

## What it does

An SEO audit from memory says what a site probably gets wrong.
This skill fetches the site and reads the code, and each result quotes what it found.

- **Crawl and index**: server-side rendering, sitemap, Search Console, `robots.txt`, `noindex`, redirect chains, 404s
- **On-page**: canonical tags, a unique title and a meta description for each page, one H1 for each page, `hreflang` on sites in more than one language
- **Structured data and links**: FAQ schema, breadcrumbs, orphan pages
- **Media and speed**: alt text, WebP images, works on a phone, layout shift, load time under 2 seconds
- **Content and authority**: AI slop, a real author bio, quality backlinks

Each check gets one of four statuses: `Pass`, `Fail`, `Manual` or `Not checked`.
Indexing checks come first, because a page Google cannot index gains nothing from the rest.

## What you get

A report in the chat: each check with its status, evidence and fix.
The skill writes no file.
Ask for one if you want to keep the report.

After the report, Claude fixes the failures you choose, one at a time, and checks each fix again.

## Use cases

- An audit before you launch a site
- Finding why a site does not appear in Google
- A review of a Next.js, Astro, Vite or plain HTML project, with or without a live URL
- Not for keyword research or for writing marketing copy

## Example prompts

- "Do an SEO review of https://example.com"
- "SEO audit of this project, the live site is https://example.com"
- "Why is my blog not indexed by Google?"

## Design choices

- **Evidence or no status.** A check that Claude could not open is `Not checked`, with the reason, never a guess.
- **Two checks are yours.** Claude cannot submit to Search Console or earn backlinks. It checks what the code can show and tells you the steps.
- **`noindex` is not always wrong.** You name the pages that must stay out of Google, such as admin or cart, and they keep it.
- **FAQ schema comes with a warning.** Since 2023 Google shows FAQ rich results only for well-known government and health sites, so the skill adds the markup only for questions the page shows, and says it may not change the result.
- **No invented people.** The author bio comes from you. Claude marks each missing fact `[ASK USER]`.
- **Real tools only.** Speed and layout shift come from Lighthouse or PageSpeed Insights. Without them, those checks are `Not checked`.

## Install

**Claude Code**:

```bash
# The whole collection
claude plugin marketplace add LaiqianDS/laiqiands-skills
claude plugin install laiqiands-skills@laiqiands

# Or this skill alone, from a clone
ln -s "$PWD/laiqiands-skills/skills/seo-review" ~/.claude/skills/seo-review
```

**Claude.ai**: zip the folder, not the files inside it, and upload the zip in **Customize > Skills**.
Without a shell, Claude uses web fetch, so the checks that need headers, redirect hops or Lighthouse are `Not checked`.

```bash
cd skills && zip -r seo-review.zip seo-review
```
