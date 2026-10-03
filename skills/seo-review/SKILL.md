---
name: seo-review
description: Review a website for search engine optimisation against a fixed list of 23 checks, from crawling and indexing to content quality and backlinks, then fix the failures the user accepts. Use when the user asks for an SEO review, SEO audit or SEO check of a site, a URL or a web project, or asks why a site does not rank or is not indexed by Google. Not for writing marketing copy or for keyword research alone.
argument-hint: "A URL, a project path, or both"
---

# SEO Review

Review a site against the 23 checks below, show the result in the chat, then fix what the user accepts.
Review first, fix second.
Never change the site during the review.

## Rules

- **Evidence or no status.** Each status comes from a file you read, a URL you fetched or a command you ran. Quote the evidence in the report. Never mark a check from memory or from what the framework usually does.
- **Four statuses only.** `Pass`, `Fail`, `Manual` (only the user can do it, outside the code), `Not checked` (you could not open what the check needs, and you say why).
- **Indexing first.** A page that Google cannot crawl or index gains nothing from the other checks. Report checks 1 to 7 before the rest, and say so when one of them fails.
- **Never invent facts about people or the business.** An author bio, a credential or an FAQ answer comes from the user. If it is missing, write a draft with gaps marked `[ASK USER]`.
- **Say which pages you checked.** On a site with 50 pages or fewer, check each page. On a larger site, check the home page, one page of each template (article, product, category, and so on) and the pages the user names, and list them in the report.

## Inputs

Ask for what is missing, at most two questions:

1. **The live URL**, the project path, or both. Both give the best review: the code shows the cause, the live site shows the result.
2. **Pages that must stay out of Google**, such as admin, cart, account, internal search or staging. These keep their `noindex`.

Read the project before you ask. Do not ask what the code already answers.

## Tools

- **Live site:** with a shell, use `curl`. It shows the raw HTML before JavaScript runs, the status codes, the headers and each redirect hop. Without a shell, use web fetch, and mark the checks that need headers or hops as `Not checked`.
- **Speed and layout shift:** run `npx lighthouse <url> --only-categories=performance --output=json --quiet` when Node is installed, or the PageSpeed Insights API (`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<url>&strategy=mobile`). If neither runs, mark checks 19 and 20 `Not checked`.
- **Code only, no live URL:** run the production build and serve it locally when the project has a build command. Otherwise review the source and mark the checks that need a live response `Not checked`.

## The checks

### Crawl and index

1. **Render it server-side.** Fetch the page with `curl` (no JavaScript). The title, the meta description, the H1, the main text and the internal links must be in that raw HTML. In code, a client-only single page app (for example a plain Vite or Create React App build) fails. SSR, static generation and prerendering pass.
2. **Generate a sitemap.** `/sitemap.xml` (or the file `robots.txt` names) returns 200, is valid XML, and lists only canonical URLs that return 200. No redirected, `noindex` or 404 URLs in it.
3. **Submit it to Search Console.** `Manual`. You cannot open the user's Search Console. Check that `robots.txt` has a `Sitemap:` line with the absolute URL, then tell the user: Search Console, Sitemaps, enter the sitemap URL, Submit.
4. **Unblock Googlebot in robots.txt.** Read `/robots.txt`. Fail on `Disallow: /` under `User-agent: *` or `User-agent: Googlebot`, and on rules that block the CSS, JavaScript or image paths the page needs to render.
5. **Delete the noindex tags.** Search for `noindex` in `<meta name="robots">`, `<meta name="googlebot">` and the `X-Robots-Tag` header. Fail only on pages that should rank. The pages from input 2 keep it. A staging `noindex` that leaks into production is a common cause, so check the environment config too.
6. **Kill the redirect chains.** Run `curl -sIL <url>` on the home page, on `http://`, on `www.` and non-`www.`, and on each internal link that redirects. More than one hop to the final URL is a chain. Fix: each old URL redirects in one 301 to the final URL, and internal links point to the final URL directly.
7. **Fix the 404s.** Collect the internal links of the checked pages and the sitemap URLs, and fetch each one. Fail on each 4xx or 5xx. Also fail on a soft 404: a "not found" page that returns 200. The real 404 page must return 404.

### On-page

8. **Add canonical tags.** Each indexable page has one `<link rel="canonical">` with an absolute URL. It points to itself unless the page is a true duplicate. It agrees with the sitemap URL (protocol, `www.`, trailing slash).
9. **Write a unique title for every page.** Each page has one `<title>`, unique across the site, about 60 characters or less, and it names the topic of the page. A site name alone, or one title on every page, fails.
10. **Write a meta description for every page.** Each page has one, unique across the site, about 150 characters or less, and it describes that page. A template default copied to every page fails.
11. **One H1 per page.** Exactly one `<h1>` in the rendered HTML, and it states the topic of the page. A logo wrapped in an `<h1>` counts.
12. **Add hreflang for each language.** Only for a site in more than one language. Each language version lists every version, itself included, with `<link rel="alternate" hreflang="...">` and absolute URLs, and the links go both ways. On a site in one language, mark it `Pass` with the evidence "one language only".

### Structured data and links

13. **Add FAQ schema.** Add `FAQPage` JSON-LD only to pages that show the same questions and answers as visible text. Tell the user that since 2023 Google shows FAQ rich results only for well-known government and health sites, so for most sites this markup does not change how the result looks. Never add questions the page does not show.
14. **Add breadcrumbs.** Pages below the home page show a breadcrumb trail and carry matching `BreadcrumbList` JSON-LD. Validate each JSON-LD block you add or find: it must parse as JSON and use schema.org types.
15. **Link the orphan pages.** An orphan is a page in the sitemap or the routes that no other checked page links to. Each one gets at least one internal link from a related page, with anchor text that says what it is. A page with no reason to exist is a candidate for deletion, so ask.

### Media and speed

16. **Alt text on every image.** Each `<img>` has an `alt` attribute. A content image describes what it shows. A decorative image has `alt=""`, and that is a pass, not a failure. Alt text stuffed with keywords fails.
17. **Convert images to WebP.** Raster photos and screenshots are served as WebP. AVIF also passes. Logos and icons should be SVG. Prefer the framework's image pipeline (for example `next/image`) or `<picture>` with a fallback over converting files by hand.
18. **Work on a phone.** Google ranks a site by its mobile version. Each page has `<meta name="viewport" content="width=device-width, initial-scale=1">`, body text of at least 16px, and nothing that scrolls sideways at 400px width. Use the mobile Lighthouse run when it is available.
19. **Fix the layout shifts.** Cumulative Layout Shift 0.1 or less on mobile. Usual causes: images and embeds without `width` and `height`, ads or banners injected above content, and web fonts without `font-display` or a size-matched fallback.
20. **Load in under 2 seconds.** Largest Contentful Paint under 2 seconds on the mobile Lighthouse run. Google's own "good" line is 2.5 seconds, the 2-second target is stricter on purpose. Report the LCP element and what delays it: server response time, render-blocking CSS or JavaScript, a large hero image, or no preload.

### Content and authority

21. **Remove the obvious AI slop.** Read the main text of the checked pages. Quote each passage that reads as generated: openers like "In today's fast-paced world", filler words like "delve", "unlock", "elevate", "seamless", "tapestry", the "it's not just X, it's Y" frame, lists of three adjectives, paragraphs that repeat the heading, and conclusions that say nothing new. Propose a plain rewrite for each. Do not rewrite facts you cannot verify.
22. **Add a real author bio.** Articles and guides name a real author, link to an author page with a bio, the person's real experience with the topic and a profile link, and carry `Person` JSON-LD as the `author` of the `Article`. Take the facts from the user only.
23. **Get quality backlinks.** `Manual`. You cannot measure backlinks from the code or one fetch. Tell the user where to see them (Search Console, Links report) and suggest three to five sources that fit this site, such as partners, directories of its field, people it already cites, or data and tools others would link to. Never suggest buying links, link exchanges or private blog networks: they break Google's spam policies.

## The report

Show the report in the chat, in this format.
Do not write it to a file unless the user asks for one.

```markdown
# SEO review: <site>

Date: <date>
Checked: <URL and/or path>
Pages checked: <list, or "all N pages">
Not checked and why: <list>

## Summary

<Pass/Fail/Manual/Not checked counts, and the three fixes with the most impact, indexing blockers first.>

## Results

| # | Check | Status | Evidence | Fix |
|---|---|---|---|---|
| 1 | Render it server-side | Fail | `curl` HTML has an empty `<div id="root">` | Prerender the routes, or move to SSR |
```

The Evidence column quotes the file and line, the URL and status, or the command output.
The Fix column names the file to change or the action for the user.

## Fixing

After the report, ask which failures to fix.
Fix one check at a time, in report order.
After each fix, run the same check again and show its row with the new status and evidence.
If a fix needs a decision the code cannot answer, such as which URL is canonical or what an author did, ask before you change anything.
