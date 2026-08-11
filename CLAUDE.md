# Apartmani Igalo Monako — apartmani-igalo.com

Static HTML site (31 pages, GitHub Pages, no build step) for a family-run
seven-apartment property at Dubrovačka 1, Igalo 85347, Montenegro.
Languages: SR (primary), EN, RU.

## This repository is the live site

`master` publishes directly to apartmani-igalo.com via GitHub Pages (`CNAME`),
and `robots.txt` allows all crawling. **Anything committed to `master` is
publicly fetchable and indexable.** The repo itself is public, so anything
committed here stays readable in git history even after deletion.

Never commit SEO analysis, GSC exports, keyword research or competitive audits
to this repository. They belong in the private archive below.

## Read these before SEO, content or GBP work

These live in the **private** [`Niiwill/monako-seo`](https://github.com/Niiwill/monako-seo)
repository, which must be attached to the session to read them.

| File (in `monako-seo`) | What it establishes |
|---|---|
| `docs/gbp-performance-2026-q3.md` | **First-party demand data** (GBP, May–Jul 2026) — what users actually search, click and call. Start here for any "should we build X" question. |
| `docs/gbp-website-audit.md` | Entity consistency site ↔ Google Business Profile. NAP, schema, brand-name invariants. |
| `docs/geo-ai-overviews-audit.md` | AI Overview / GEO positioning, and the recorded pricing decision (§9). |
| `seo-reports/` | Daily GSC analyses and raw snapshots, 2026-07-04 onward. New analysis goes here, never in this repo. |

## Standing constraints

- **94% of impressions are mobile.** Judge every change on a phone viewport first.
- **The phone is the checkout** — 392 calls vs 228 website clicks in the last quarter.
  Don't add steps before a `tel:` tap; low website CTR is not automatically a defect.
- **Viber only. Never add WhatsApp** — the business has never operated it, and every
  `wa.me` reference was deliberately removed on 2026-07-26.
- **Seasonal prices are off the site by owner decision**
  (`monako-seo:docs/geo-ai-overviews-audit.md` §9). Never reintroduce a bare "od XX €".
  Price transparency is an open question for the owner, not a settled no — see
  `monako-seo:docs/gbp-performance-2026-q3.md` §5 before raising it.
- **Entity invariants — do not break:** no `aggregateRating`/`Review` on the business
  node, `LodgingBusiness` (not `VacationRental`), one NAP everywhere,
  `hasMap` CID `3697180737008791124`, `foundingDate` 2000-07-12.
- **Guest review quotes are verbatim.** The site claims 100 m to the beach; review text
  saying 60 m is a guest's words and must not be edited to match marketing copy.
- **Meta descriptions: do not shorten for length alone.** A late-July batch of "meta
  length fixes" cost 16.5% CTR across five pages at flat position (~82 clicks/week) and
  was reverted. Evidence in `monako-seo:seo-reports/2026-08-12-analysis.md`.

## Before building anything described as "missing"

Blatna Plaža, monthly rental, FAQ and the floating Viber component **already exist** in
some form. Check the working tree first — see
`monako-seo:docs/gbp-performance-2026-q3.md` §6.
