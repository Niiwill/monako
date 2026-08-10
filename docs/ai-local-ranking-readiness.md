# Readiness check: dynamic GBP + AI local ranking

**Business:** Apartmani Igalo Monako · https://apartmani-igalo.com/
**Checked:** 2026-08-10 · 26 HTML pages, static site on GitHub Pages
**Measured against:** "The Death Of The Static GBP: Why Dynamic Profiles Are The New
Local Ranking Factor" (Search Engine Journal, Adam Heitzman, March 2026)

## Scope note first

Roughly four fifths of what that article asks for happens in the **Google Business
Profile dashboard**, not in this repository — weekly posts, twice-monthly photo
uploads, review requests, owner responses, Q&A seeding, category cleanup. Nothing in
this repo can do any of it.

What the website is responsible for is **corroboration**: giving Google and the AI
layer a consistent, machine-readable second source that agrees with the profile. On
that job this site is in the top few percent of small local sites. The gaps below are
narrow but two of them are real blockers, because the article's top two "do this"
actions each need a website asset that does not currently exist.

---

## Verdict

| Layer | State |
|---|---|
| Static/entity foundations the article calls "table stakes" | **Strong.** Better than the article's own baseline. |
| Website assets that *enable* the dynamic signals | **Two blocking gaps** — no review ask, no bookable URL. |
| Dynamic engagement itself (posts, photos, review cadence) | **Not started.** GBP-side, and the July audit's dashboard items are all still open. |
| AI-visibility layer (citation + entity signals) | **Mostly ready, one fragmentation bug.** |

---

## Ready — do not touch these

| Article factor | Site evidence |
|---|---|
| **Being open when users search** (their No. 5 factor) | `openingHoursSpecification` 00:00–23:59 × 7 days on all 13 business nodes — Google's documented encoding for 24h — matching GBP's `00:00-24:00`. A 24/7 profile is never "closed" at query time, so this factor is maximally satisfied rather than merely passed. Visible "24/7" copy agrees. |
| **Accurate hours as an AI input** | Same node, byte-identical across all 13 pages. No conflicting seasonal-closure claim anywhere (season copy refers to the *swimming* season, not to opening). |
| **Citation / entity signals** (3 of the article's top 5 AI factors) | `Dubrovačka 1` × 50 with zero variants; one phone number in three renderings with zero conflicts; geo `42.4538, 18.503` × 15; `hasMap` CID `3697180737008791124` resolving to the same place ID as the Maps embed; `sameAs` = exactly the three GBP social URLs, character-for-character. |
| **Review-snippet eligibility** | Zero `aggregateRating` and zero `Review` in JSON-LD *and* microdata site-wide. The July audit stripped the self-serving markup — that was the right call and it keeps the profile clean. |
| **Q&A raw material** | 23 `FAQPage` blocks, 154 `Question`/`Answer` pairs. The article says seed 3–5 real questions; you have 154 already written and already public. |
| **Photo infrastructure** | 250 `image:image` entries in `sitemap.xml`, 22 `ImageObject` nodes, `alt` on every `<img>`. |
| **AI discoverability** | `llms.txt` present, accurate, and carrying the full NAP + page map. |
| **Content freshness** | `dateModified` on 19 pages, newest 2026-08-01; `sitemap.xml` lastmod current to 2026-08-10. |

---

## Gaps that are the website's job

### 1. There is no way for a guest to leave a review — blocking

The article's single most emphasised action is review velocity: *ask within 24 hours,
respond within 48*. The site has **114** `tel:` links, **44** `mailto:`, **36** Viber
deep links, **4** `sms:` — and **zero** links to the Google review form. No
`g.page/r/…/review`, no `search.google.com/local/writereview?placeid=…`, no "ostavite
recenziju" anywhere in 26 pages.

So the profile displays 71 reviews and the site brags about them, but nothing on the
domain asks for the 72nd. Review velocity currently depends entirely on guests
volunteering.

**Fix:** get the short review link from the GBP dashboard (Ask for reviews → copy
link) and put it in three places: the homepage contact block, `about.html`, and a
tiny `recenzija.html` you can paste into a post-stay Viber or SMS message. The
micro-page matters more than it looks — a bare Google URL in a message looks like
spam, a page on your own domain does not.

### 2. GBP's booking field has nothing to point at — blocking

`<form>` count across all 26 pages: **0**. `potentialAction` / `ReserveAction` count:
**0**. There is no reservation page, no enquiry form, no booking engine.

The article's "closing the loop inside Google" section is therefore unavailable to
you: the GBP appointment/booking-link field needs a URL, and the site does not have
one to give it. Every conversion path is a phone call, a Viber message or an email —
all fine for humans, all invisible as the in-Google booking interaction the article
describes as an engagement signal.

**Fix:** a dedicated `rezervacija.html` / `booking.html` with a real enquiry form
(dates, guests, contact) or, if you would rather not run a form on a static host, a
Viber/phone-first reservation landing page with the dates-and-guests checklist spelled
out. Then add `potentialAction` → `ReserveAction` to the `LodgingBusiness` node
pointing at it, and paste the same URL into GBP.

### 3. The entity graph splits in two on the guide pages — highest value per minute

13 of 26 pages (all of `vesti/` plus `blog.html`) carry no `#business` node. They do
carry `publisher` and `author` as an Organization — but as a **bare** node:

```json
"publisher": {
  "@type": "Organization",
  "name": "Apartmani Igalo Monako",
  "url": "https://apartmani-igalo.com/"
}
```

No `@id`. So on exactly the pages that pull the most organic traffic, Google and the
AI layer see a *second, unlinked* organization that happens to share a name with your
business, instead of a reference to the business entity. Given the article's finding
that three of the top five AI-visibility factors are citation- and entity-based, this
is the cheapest high-value fix on the list.

**Fix:** add `"@id": "https://apartmani-igalo.com/#business"` to the `publisher` and
`author` Organization nodes on those 13 pages. One line each, no visible change, and
it welds 13 content pages onto the business entity.

### 4. No service markup

Zero `hasOfferCatalog`, `makesOffer`, or `Service` nodes site-wide. The article names
"complete service descriptions" as a direct AI input. The services exist in prose —
monthly off-season rental, airport transfer, excursions, daily housekeeping, bike
rental — but none of it is machine-readable.

**Fix:** a `hasOfferCatalog` on the `LodgingBusiness` node listing the real services.
Only list what you actually provide; this is an entity-completeness signal, not a
keyword slot.

### 5. Hardcoded review counts will go stale as velocity improves

`71 ocjena` / `71 reviews`, `35` (Booking), `15` (Airbnb) and seven instances of
`4.9/5` — including in the homepage meta and OG descriptions — are frozen in the HTML
as of late July 2026. If the review-request fix works, these numbers start
*understating* you within weeks, and a stale count is the exact opposite of the
freshness signal the article describes.

**Fix:** either put a quarterly reminder on updating them, or soften the copy to
"4.9★ na Google-u" with no count. Do **not** solve this by re-adding
`aggregateRating` markup — that is the violation the July audit removed.

### 6. The UTM tag on your GBP link measures nothing

The GBP website URL is `…/?utm_source=gbp&utm_medium=organic`, but the site has **no
analytics at all** — zero `gtag`, zero GTM, no measurement ID in 26 pages. The
article's "What To Measure" section (website clicks, and what those visitors do next)
is unmeasurable on the site side. GBP Insights still gives you calls, direction
requests and click counts; what you cannot see is what GBP traffic does after it
lands, which is the half that tells you whether the profile work is paying.

**Fix:** install GA4 (or a lighter privacy-friendly counter) and mark the `tel:`,
`viber:`, `sms:` and `mailto:` clicks as conversions. Without this, every
recommendation in this document is unfalsifiable.

### 7. Minor

- Visible 24/7 hours appear on only 6 of 26 pages. The schema carries the ranking
  signal everywhere, so this is a human-facing gap, not an algorithmic one — but the
  13 guide pages that attract traffic never mention that you answer at any hour.
- No `WebSite` node with `SearchAction` on the homepage (only `blog.html` and
  `mesecni-najam-igalo.html` carry `WebSite` nodes at all). Very low priority.

---

## Still open in the GBP dashboard

All five dashboard items from `gbp-website-audit.md` remain unactioned, and this
article raises the priority of the first two:

1. **Remove the two agency categories** (*Apartment rental agency*, *Vacation home
   rental agency*). The article restates that the primary category is still the No. 1
   local-pack factor and that categories decide which competitive set you appear in —
   while the site's entire argument is that you are *not* an agency.
2. **Fill "From the business"** — still empty. Draft copy is ready in
   `gbp-website-audit.md` § M1, already worded to match the site.
3. **Set the amenity attributes** matching the eight the site's `amenityFeature` list
   declares.
4. Optionally publish the walkthrough video (`video/Monako_about.mp4`) to the profile
   and the linked YouTube channel.
5. Leave the WhatsApp field empty — the business is Viber-only.

Plus the three ongoing cadences the article is really about, none of which touch this
repo: **a post a week**, **photos twice a month**, **a review ask within 24 hours of
every checkout and a response within 48 hours of every review**. You have an unusual
advantage on posts — 26 pages of genuine local content (beaches, restaurants, the
Mimosa Festival, sea temperature, Blatna plaža) that can each become a GBP post with
a link back.

---

## If you do only three things

1. Add the Google review link to the site and start asking at checkout. (Gap 1)
2. Add `"@id"` to the 13 guide pages' Organization nodes. (Gap 3)
3. Remove the two agency categories in GBP. (Dashboard item 1)

The first is the article's biggest lever, the second is fifteen minutes of work for
the AI-visibility category the article says is brand new this year, and the third is
the only item touching the factor it names as still No. 1.
