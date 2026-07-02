# Weekly SEO Routine — apartmani-igalo.com (Monako)

This file is the standing instruction for the automated weekly SEO session.
The Trigger prompt should simply say: **"Run the routine in seo/ROUTINE.md."**
Everything else lives here so it can be edited with a normal commit instead of
editing Trigger settings.

---

## Role

Act as a world-class Technical SEO, Content SEO, and Information Architecture
expert with deep expertise in Google's current Search systems, Google Search
Console, Core Web Vitals, structured data, internal linking, topical
authority, semantic SEO, EEAT, and modern search-intent optimization.

## Mission

Treat this week's Search Console data as Google's direct feedback about this
website. Your job is not to summarize it — it is to **apply the highest-ROI
improvements directly to the repository**, commit them, and open a PR. Do not
produce a report as your only output. The PR diff is the report.

---

## Step 1 — Fetch data (last 28 days)

Credentials: read the GSC service-account JSON from whichever the environment
provides — check `$GSC_SERVICE_ACCOUNT_JSON` (raw JSON string) first, then
`$GSC_SERVICE_ACCOUNT_FILE` (a file path) second. If neither is set, stop and
say so instead of guessing — do not proceed without real data.

Property: `sc-domain:apartmani-igalo.com`

Use the Search Console API (`searchconsole` v1, `searchanalytics.query`,
scope `webmasters.readonly`) via a Python venv (`google-auth`,
`google-api-python-client` — install into a fresh venv if not already
present; the system `cryptography` package conflicts with pip-installed
`cffi`, so always use `python3 -m venv --system-site-packages` and install
inside it, not into system Python).

Pull at minimum:
- `dimensions: ["query"]`, rowLimit 1000 — full query list
- `dimensions: ["page"]`, rowLimit 250 — full page list
- `dimensions: ["query", "page"]`, rowLimit 1000 — query-to-page mapping (needed to spot cannibalization)

Date range: last 28 full days ending 3 days ago (GSC data has a reporting lag).

Save the raw pull as `seo/reports/YYYY-MM-DD.json` (today's date), including
all three dimension pulls in one file.

## Step 2 — Establish continuity with past runs

Before analyzing, read:
- `seo/CHANGELOG.md` — every change made in prior runs, so you don't
  re-flip the same title/meta back and forth week over week.
- The most recent prior file in `seo/reports/` (if one exists) — diff it
  against this week's pull to see what actually moved: new queries
  appearing, CTR/position deltas, pages gaining or losing impressions.

**Guardrail:** do not re-edit a title, meta description, or H1 that was
changed by a prior run within the last 21 days, unless this week's data
shows it is clearly still failing (e.g., CTR still below the position's
expected CTR curve) — titles need time to be recrawled and re-ranked before
their effect is visible. Rewriting the same element every week is noise, not
signal, and can suppress ranking stability.

## Step 3 — Analyze signals, in priority order

1. High impressions + low CTR on existing pages (title/meta rewrite opportunity)
2. Good average position (top 5) but low clicks relative to position (CTR problem, not ranking problem)
3. Queries stuck on page 2–3 (position 11–30) with real impression volume (content depth / internal linking problem)
4. Keyword cannibalization — the same query appearing across the `query+page` pull split across 2+ URLs with similar impressions (content overlap needs resolving via one page winning and the other narrowing scope, or a canonical/internal-link consolidation)
5. Queries with meaningful impressions and no matching content anywhere on the site (a genuine content gap — see Step 5 for the new-page decision)
6. Any page with a `position` that got worse by more than 2 spots vs the last snapshot (regression — investigate before anything else, something may be broken: check title/meta didn't regress, check the page still returns 200, check no accidental noindex)

Cap yourself to the **top 5 highest-ROI opportunities** for this run. Do not
attempt to rewrite the whole site every week — a small, reviewable,
high-confidence diff beats a sweeping one nobody can review.

## Step 4 — Decide: improve existing page, or create a new one

Default to improving an existing page. Only create a new page under
`vesti/` when **all** of these hold:
- A query cluster has real, sustained impression volume (not a single-week
  blip — check it also appeared in the prior snapshot if one exists).
- The search intent is meaningfully different from every existing page —
  it cannot be satisfied by expanding an existing section without diluting
  that page's focus.
- It will not cannibalize an existing ranking page (check Step 3.4 first).

If you create a new page:
- Copy the structure/CSS tokens/component classes from the closest existing
  `vesti/*.html` page (same `:root` design tokens, same FAQ markup pattern,
  same JSON-LD block shape: `Article` + `FAQPage` + `BreadcrumbList`, same
  hreflang pattern if a Serbian/English pair makes sense).
- Add it to `sitemap.xml` with today's date as `lastmod`.
- Link to it from `blog.html` and from at least one related existing
  `vesti/` page's "related articles" section — new pages need internal
  links to be crawled and to pass authority.
- Do not create a Serbian-only or English-only orphan if the site pattern
  for that topic is bilingual — check whether a matching pair is expected.

## Step 5 — Execute improvements

Apply directly to the HTML (no separate report). For pages in scope this
run:
- Rewrite titles/meta descriptions where CTR is underperforming for the
  position (respect the Step 2 guardrail).
- Improve H1–H6 structure and keyword/entity coverage without stuffing.
- Expand thin content; fill topical gaps found in Step 3.
- Resolve cannibalization (narrow scope of the weaker page, strengthen
  internal linking to the stronger one, or merge if genuinely duplicate).
- Add/expand FAQs matching real queries from this week's data (visible
  markup **and** the `FAQPage` JSON-LD block — keep them in sync).
- Add or correct schema markup (Article, FAQPage, BreadcrumbList, ItemList,
  Restaurant/LodgingBusiness where relevant) — never invent facts (prices,
  ratings, addresses, health claims) that aren't already stated elsewhere
  on the site; if data is needed and absent, leave a clear TODO comment
  instead of fabricating it.
- Improve internal linking and anchor text between pages touched this run.
- Improve image alt text/filenames where touched pages have generic or
  missing alt text.
- Keep canonical tags, robots meta, Open Graph, and Twitter Card tags in
  sync with any title/description change.
- Bump `sitemap.xml` `lastmod` for every page actually changed.
- Preserve existing design, layout, and branding exactly — SEO changes
  should not visibly alter the site's look.

## Step 6 — Validate before committing

For every HTML file touched:
1. Confirm every `<script type="application/ld+json">` block still parses
   as valid JSON.
2. Confirm HTML tags are balanced (no orphaned `<article>`/`<div>` from a
   misplaced edit).
3. Confirm no duplicate `id` attributes were introduced (especially
   `faq*` ids).
4. Confirm every new internal link (`href="..."`) points to a file that
   actually exists in the repo.

Do not commit a page that fails any of these checks — fix it first.

## Step 7 — Record and ship

1. Append an entry to `seo/CHANGELOG.md`:
   ```
   ## YYYY-MM-DD
   - What changed, on which page(s), and why (which query/signal drove it)
   - Any new page created and the query cluster it targets
   - Anything explicitly *not* changed and why (e.g. "title on X held per
     21-day guardrail, still monitoring")
   ```
2. Commit the new `seo/reports/YYYY-MM-DD.json` snapshot, the changelog
   entry, and the code changes together.
3. Branch name: `claude/seo-weekly-YYYY-MM-DD`, cut from latest `master`.
4. Push and open a PR. PR description should state, per page changed,
   which Search Console signal motivated the change (numbers, not vibes).
5. **Do not merge automatically.** Do not push directly to `master`. Do not
   force-push. The PR is the human checkpoint.

## Output rules

- Do not reply with a summary-only report and stop — the repository changes
  and the PR are the deliverable.
- Do not ask for confirmation before each individual change — the weekly
  cadence and the PR review step are the confirmation points.
- Keep chat/PR narration brief; let the diff and the changelog entry speak.
- If GSC credentials are missing/invalid, or if there is truly nothing
  worth changing this week (rare), say so plainly instead of manufacturing
  busywork changes.

## Hard guardrails

- Never commit secrets (the service-account key or its contents) to the
  repository, in any file, ever.
- Never fabricate business facts: prices, ratings, addresses, phone
  numbers, medical/health claims. Only state what's already verifiable
  elsewhere on the site or leave a TODO for the owner to supply it.
- Never touch `robots.txt` to disallow crawling, and never add `noindex` to
  an existing indexed page without an explicit, data-backed reason stated
  in the changelog.
- Never run destructive git operations (`reset --hard`, `push --force`,
  `clean -f`) as part of this routine.
