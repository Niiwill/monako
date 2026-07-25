# Redesign brief - apartmani-igalo.com

Paste the block below into a fresh session. Fill in the two `<>` slots first.

---

I have loaded the `design-taste-frontend` skill (tasteskill) as my only source of
design rules. Do not fall back on general design instincts where the skill has a rule.

## Brief

- **Site:** `/home/user/monako` - static site, GitHub Pages, live at
  https://apartmani-igalo.com. Hand-written HTML with inline `<style>` per page.
  No build step, no framework, no JS.
- **Target page(s) this round:** `<index.html / about.html / all 19 routes / ...>`
- **Mode:** `<preserve brand / overhaul / unsure>`
- **Audience:** Serbian and Montenegrin speaking holidaymakers booking a summer
  apartment in Igalo, plus Russian and English visitors on the translated routes.
  They are one tab away from Booking.com. The page has to earn a direct
  phone/Viber booking from strangers, so trust beats novelty at every fork.
  Treat this as a trust-first commerce brief (skill Section 0.A.6).
- **Business model note:** the whole value prop is "direct from the owner, no
  Booking commission." Anything that makes the site feel less like a real family
  business and more like a template works against the product.

### What works today, keep it

1. **Real photography throughout.** Every image is an actual photo of the
   apartments, Blatna plaža, or Herceg Novi. No stock, no placeholders, no
   div-based fakes. WebP with JPG fallbacks.
2. **Self-hosted fonts with Serbian subsets** (`fonts/*-serbian.woff2`). Local
   diacritics render correctly with no Google Fonts request. Keep the
   self-hosting and keep the Serbian subset coverage whatever the type stack becomes.
3. **Accessibility groundwork already in place:** skip-link
   ("Preskoči na glavni sadržaj"), `aria-labelledby` on every section pointing at
   real heading IDs, and two `prefers-reduced-motion` blocks. Do not regress any
   of it (skill Section 11.C).
4. **Fluid `clamp()` type scale** (`--step--1` through `--step-5`) and a working
   spacing token set. The token architecture is sound even if the values change.

### What is broken today, fix it

1. **Type stack is two skill violations in one line.** `--ff-display: 'Fraunces'`
   is explicitly banned as a default display serif (Section 4.1), and this is a
   holiday-rental brief, not editorial or heritage, so the serif has no
   justification. `--ff-body: 'Inter'` is the discouraged default. This is
   modernisation lever 1 and the biggest lift available.
2. **80 banned dash characters in `index.html` alone** - 55 em-dashes and 25
   en-dashes. Section 9.G is binary: zero. They are in headings, meta
   descriptions, and body copy. Sweep every route, not just the homepage.
3. **No dark mode anywhere.** Zero `prefers-color-scheme` blocks across the site.
   Section 6.C makes it mandatory for consumer-facing pages.
4. **`MOTION_INTENSITY` is effectively 1.** No keyframes, no scripts, nothing
   moves. On a page selling a seaside summer holiday that reads as unfinished
   rather than as restraint.
5. **Ten sections, roughly two layout families.** Everything is a full-width
   stack alternating `--c-bg` white and `--c-sand`. Section 4.7 wants at least
   four families across eight-plus sections.

### SEO constraint - none of this changes without my explicit approval

This site's rankings are the business. Section 11.F is hard law here.

- **All 19 routes keep their exact filenames.** Root: `index.html`, `about.html`,
  `blog.html`, `blatna-plaza.html`, `mesecni-najam-igalo.html`,
  `monthly-rental-igalo.html`, `nova-godina-herceg-novi.html`,
  `praznik-mimoze-program.html`, `mimosa-festival-herceg-novi.html`,
  `iznajmljivanje-bicikla-herceg-novi-igalo.html`,
  `rent-a-bike-herceg-novi-igalo.html`. Plus all 8 files under `vesti/`.
  Also untouchable: `CNAME`, `sitemap.xml`, `robots.txt`, `llms.txt`, `ads.txt`.
- **Anchor IDs stay.** `#cjenovnik` is linked from the nav and from other pages.
  `#main`, `#hero-title`, `#faq1` through `#faq8`, and every `*-heading` ID is
  wired to an `aria-labelledby`. Renaming one silently breaks a screen reader
  and possibly an inbound link.
- **Nav labels stay in Serbian, exactly as written:** Početna, O nama, Cjenovnik,
  Vesti, Blatna plaža, Mesečni najam.
- **Copy voice stays.** Visual modernisation is not a content rewrite
  (Section 11.C). The only copy edits I am pre-approving are the dash
  replacements from item 2 above.
- **Contact details are load-bearing conversion paths, not decoration:**
  `+382 67 558 240` (tel and Viber) and `hotel-monako@hotmail.com`. There are no
  `<form>` elements on this site, so every booking runs through those two links.
  Do not restyle them into something less obviously tappable on mobile.
- **Titles and meta descriptions** on all routes stay as-is apart from dash
  replacement.

## Process - stop at each gate, wait for my OK

**Step 1.** Run the Section 11.B audit and post it in writing:
- Brand tokens currently in use (primary, accent, type stack, radii)
- Information architecture (page tree, nav, conversion paths)
- Patterns to preserve (signature interactions, recognisable hero, copy voice)
- Patterns to retire (slop tells, broken layouts, dead links)
- Inferred dial reading of the current site
  (`DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY`)
- SEO baseline (ranking pages, titles, anchors)

Then stop.

**Step 2.** After my OK: declare the mode (Preserve, Overhaul, or
Greenfield-with-content-preserved), the target dial values with reasoning, and
which Section 11.D modernisation levers you will apply, in priority order.
Then stop.

**Step 3.** After my OK: implement. URL structure, nav labels, anchor IDs,
contact links, brand logo, and any legal copy stay unchanged unless I explicitly
approved the change in Step 2. Work one page at a time and show me the diff.

**Step 4.** Post in writing, before declaring done:
- **Em-dash audit** - `grep -c '—\|–'` across every `.html` file, per file. Any
  non-zero count is a Fail.
- **Pre-Flight Check** (Section 14) - every box, ticked or failed explicitly.
  "Not applicable" needs a reason.
- **Preservation audit** - every URL, nav label, anchor ID, and contact link
  changed. This list must be empty unless I approved the change in Step 2.
- **Brand fidelity audit** - confirm the Adriatic blue `#0E5EA6`, its dark
  variant `#094880`, the gold `#E8A020`, and the Serbian font subset coverage all
  survived. If the mode is Preserve, confirm the type stack change is the only
  brand-level change.
- **Dark mode proof** - confirm you rendered and checked both modes
  (Section 8.D), not just the light one.

Any Fail blocks completion. Do not report done with an open Fail.

---

## Notes on what I changed from the generic template

- **Dropped "v2 (experimental)"** from the opening line. The installed
  `SKILL.md` carries no version marker, so claiming one would be inventing a fact
  the skill file does not support. It is named by skill name instead.
- **Added a target-page slot.** The original assumed one site, one pass. This
  repo is 19 hand-written HTML files with duplicated inline CSS, so scope has to
  be stated per round or the agent will either do one page and call it done or
  try all 19 at once.
- **Split the SEO constraint into routes / anchors / nav / copy / contact.** The
  generic "which routes, headings, or anchors must not change" is too loose for a
  site where `#cjenovnik` is cross-linked and the anchors double as
  `aria-labelledby` targets.
- **Added the no-forms fact.** The template's Step 4 asks for a form-field audit.
  This site has zero `<form>` elements, so that check is replaced with the
  contact-link check, which is where the actual conversion risk sits.
- **Added the dark-mode proof to Step 4.** Section 8.D requires viewing both
  modes; the generic template's Step 4 does not ask for it, and it is the easiest
  requirement to silently skip.
