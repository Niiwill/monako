# Google Business Profile ↔ Website Consistency Audit

**Business:** Apartmani Igalo Monako
**Site:** https://apartmani-igalo.com/ (static HTML, 19 pages, GitHub Pages)
**GBP export:** `Ungrouped_locations` (single location, 2026-07-25)
**Audit date:** 2026-07-25

The goal of this audit is **entity consistency** — helping Google confirm that
apartmani-igalo.com and the "Apartmani Igalo Monako" Google Business Profile are
the same real-world business. Ranking tactics are secondary and are only listed
in the Green section.

---

## Implementation status — updated 2026-07-25

Everything in this report that is a **website change** has been implemented on branch
`claude/website-gbp-audit-kjiwtb`. Items marked **GBP dashboard** cannot be done from the
repository and are the remaining work.

| # | Issue | Status |
|---|---|---|
| C1 | Contradicting founding dates | **Fixed** — 2000 adopted everywhere (matches GBP + `foundingDate`) |
| C2 | Self-serving `aggregateRating`/`review` in JSON-LD | **Fixed** — removed from all 10 `#business` nodes |
| C2b | Same violation in *microdata* (found during implementation) | **Fixed** — stripped from `blatna-plaza.html` and `about.html` |
| C3 | Conflicting 4.9/24 rating pool on `Apartment` nodes | **Fixed** — markup removed, visible copy reconciled to the real 71 Google reviews |
| C4 | EN 10-reasons page disconnected | **Fixed** — rebuilt to full parity |
| M1 | GBP description empty | **GBP dashboard** — draft copy in the M1 section below |
| M2 | `VacationRental` schema type | **Fixed** — now `LodgingBusiness` on all 13 nodes |
| M3 | Contradictory GBP agency categories | **GBP dashboard** |
| M4 | WhatsApp / chat channels | **GBP dashboard** — site already publishes `wa.me/38267558240` |
| M5 | No English homepage or About | **Fixed** — added `/en/` and `/en/about.html` |
| M6 | Inconsistent brand name in titles | **Fixed** — all 19 titles standardised + `alternateName` added |
| M7 | `hotel-monako@hotmail.com` | **Deferred by decision** — kept, to avoid breaking a live address |
| G1 | Empty GBP fields / amenity attributes | **GBP dashboard** |
| G2 | `starRating` missing | **Fixed** — `3` added (matches "tri zvjezdice") |
| G3 | `knowsLanguage` missing | **Fixed** — `sr, en, ru, de` added |
| G4 | `priceRange` | **Deliberately not added** — seasonal prices are genuinely on request |
| G5 | `checkinTime`/`checkoutTime` | **Deliberately not added** — no fixed published times exist |
| G6 | `addressRegion` inconsistency | **No change — this finding was over-stated.** The business node and the `TouristAttraction` describe *different entities*, so differing address granularity is not a conflict. Leaving the business nodes without `addressRegion` keeps the exact match with GBP's empty Administrative area, which matters more. |
| G7 | hreflang granularity (`sr` vs `sr-Latn`) | **No change** — current tags are valid and reciprocal; not worth the regression risk |
| G8 | UTM on the GBP website URL | **No change needed** — standard practice, canonical resolves it |
| G9 | Video on GBP/YouTube | **GBP dashboard** |
| G10 | Dedicated contact page | **Deferred by decision** |

### Verification performed

- All 21 HTML files: JSON-LD parses, tags balanced, no `aggregateRating`, no `VacationRental`,
  no stale date claims, no broken local links or missing images.
- All 13 `#business` nodes are byte-identical on type, name, phone, address and founding date.
- hreflang confirmed reciprocal across all 9 language pairs.
- `sitemap.xml` validates as XML; 21 URLs including the two new English pages.
- New and modified pages rendered in Chromium: no JS errors, content and layout intact.

### Remaining work — GBP dashboard only

1. **Add the business description** (M1) — draft in the M1 section below.
2. **Remove the two agency categories** (M3): *Apartment rental agency*, *Vacation home rental agency*.
3. **Set the WhatsApp field** to `https://wa.me/38267558240` and pick a primary chat (M4).
4. **Set amenity attributes** matching the eight the site lists, plus store code and labels (G1).
5. Optionally publish the walkthrough video on the profile / linked YouTube channel (G9).

---

## Reference: GBP export values

| GBP field | Value |
|---|---|
| Business name | Apartmani Igalo Monako |
| Address line 1 | Dubrovačka 1 |
| Locality | Igalo |
| Administrative area | *(empty)* |
| Country / Region | ME |
| Postal code | 85347 |
| Primary phone | 067 558 240 |
| Additional phones | *(empty)* |
| Website | `https://apartmani-igalo.com/?utm_source=gbp&utm_medium=organic` |
| Primary category | Holiday apartment rental |
| Additional categories | Guest house, Holiday apartment, Serviced accommodation, Apartment rental agency, Vacation home rental agency |
| Hours (all 7 days) | 00:00–24:00 |
| Special hours | *(empty)* |
| From the business | **(empty)** |
| Opening date | **2000-07-12** |
| Store code / Labels | *(empty)* |
| Facebook | `https://www.facebook.com/apartmanimonako/` |
| Instagram | `https://www.instagram.com/apartmani.igalo/` |
| YouTube | `https://www.youtube.com/@monako-apartmaniigalo5135/` |
| Texting number | `sms:+38267558240` |
| WhatsApp / X / LinkedIn / Pinterest / TikTok | *(empty)* |
| Primary chat | *(empty)* |

---

## What is already correct

These are strong signals. Do not change them while fixing the issues below.

| Signal | Status |
|---|---|
| **Street address** | `Dubrovačka 1` — 40 occurrences site-wide, all byte-identical, matches GBP exactly. |
| **City / postal / country** | `Igalo 85347`, `Crna Gora` / `Montenegro`, `ME` in schema — consistent everywhere, matches GBP. |
| **Phone** | GBP `067 558 240` = site `+382 67 558 240` (56×) = schema `+38267558240` = `tel:+38267558240` (90×). Zero variance. |
| **Third-party phone** | `+382 69 530 869` on the bike pages belongs to *Rent a Bike Herceg Novi* and is explicitly attributed to them. Correctly handled — **not** a NAP conflict. |
| **Social profiles** | `sameAs` on 26–27 pages lists exactly the three GBP URLs (Facebook, Instagram, YouTube), character-for-character. |
| **Google Maps entity link** | `hasMap` CID `3697180737008791124` decodes to `0x334f064ab3d36e54` — the identical place ID used in the Maps `<iframe>` embed. This is the single strongest site↔GBP binding on the whole site. |
| **Founding date in schema** | `foundingDate: "2000-07-12"` matches the GBP opening date exactly. |
| **Opening hours encoding** | `opens 00:00 / closes 23:59` is Google's documented encoding for "open 24 hours", so it correctly mirrors GBP's `00:00-24:00`. Visible text ("Ponedjeljak – Nedjelja, 24/7") agrees. |
| **Canonicals** | All 19 pages self-referential and absolute. No conflicts with `og:url`. |
| **Sitemap** | All 19 HTML files present, no orphans, no 404 entries. |
| **hreflang** | Bidirectional and well-formed on all six EN/SR pairs. |
| **Schema images** | All referenced image files exist in the repo. |

---

# Critical Issues (Red)

## C1 — Three contradicting "in business since" dates

**Current situation**
The site states four different origin stories, one of which contradicts another *on the same page*:

| Claim | Implied start | Location |
|---|---|---|
| `foundingDate: "2000-07-12"` | 2000 | schema on all 11 business pages |
| "15+ Godina Iskustva" | ~2011 | `about.html:10, 11, 17, 28, 971` |
| "Više od **15 godina** pružamo smještaj" | ~2011 | `about.html:947` |
| "Naše **višedecenijsko** iskustvo u turizmu" | 2000s or earlier | `about.html` (body, "Ko smo mi" section) |
| "cijene su stabilne već **15 godina**" | ~2011 | `index.html:290, 1855, 1957, 2268` |
| "**15+ godina** iskustva" | ~2011 | `index.html:1704` |
| "**Iznajmljujemo od 2010.**" | 2010 | `mesecni-najam-igalo.html:1627` |
| "već više od **15 godina** dočekujemo goste" | ~2011 | `vesti/restorani-igalo.html:937` |

**GMB data:** Opening date `2000-07-12` → 26 years as of 2026.
**Website data:** Predominantly "15 years" (≈2011) and one "since 2010".

**Why it matters**
This is a hard factual contradiction on the single attribute Google uses to age-verify a local entity. The schema says one thing, the visible copy says another, and `about.html` contradicts itself in two adjacent paragraphs. For an accommodation business, longevity is a core trust attribute; visible copy disagreeing with your own markup *and* your GBP undermines the site's credibility as an authoritative source about its own business.

**Recommended fix**
Decide which date is true and propagate it everywhere.

- If **2000** is correct (GBP + schema already say so): change every "15 godina" / "15+" to "25+ godina" or "od 2000. godine", and change `mesecni-najam-igalo.html:1627` to "Iznajmljujemo od 2000."
- If **2010** is correct: change the GBP opening date to 2010 *and* `foundingDate` in all 11 JSON-LD blocks, then use "15+ godina" consistently.
- Remove "višedecenijsko iskustvo" from `about.html` unless you settle on 2000.

**Exact locations**
`about.html` lines 10, 11, 17, 28, 947, 971 + the "Ko smo mi" paragraph · `index.html` lines 290, 1704, 1855, 1957, 2268 · `mesecni-najam-igalo.html` line 1627 · `vesti/restorani-igalo.html` line 937.

---

## C2 — Self-serving `aggregateRating` + `review` on the business node, aggregated from third parties

**Current situation**
The `#business` node carries an `aggregateRating` of **4.9 / reviewCount 71** plus three full `Review` objects, duplicated across **ten pages**:

| File | `aggregateRating` line | `review` line |
|---|---|---|
| `index.html` | 142 | 149 |
| `about.html` | 138 | 145 |
| `blatna-plaza.html` | 141 | 148 |
| `monthly-rental-igalo.html` | 267 | 274 |
| `mesecni-najam-igalo.html` | 361 | 368 |
| `mimosa-festival-herceg-novi.html` | 183 | 190 |
| `praznik-mimoze-program.html` | 282 | 289 |
| `nova-godina-herceg-novi.html` | 245 | 252 |
| `rent-a-bike-herceg-novi-igalo.html` | 143 | 150 |
| `iznajmljivanje-bicikla-herceg-novi-igalo.html` | 143 | 150 |

The visible ratings block on `index.html` and `about.html` makes the source explicit:
`4.9/5 · 71 ocjena · Google` — alongside `10/10 · 35 ocjena · Booking.com` and `5/5 · 15 ocjena · Airbnb`.

**GMB data:** The 71 reviews live on the Google Business Profile itself.
**Website data:** Those same Google reviews are re-published and marked up as first-party `Review`/`aggregateRating` on the business's own domain.

**Why it matters**
Two of Google's review-snippet rules are engaged at once:

1. **Self-serving reviews are not allowed for `LocalBusiness` / `Organization`.** `VacationRental` inherits from `LodgingBusiness` → `LocalBusiness`, so ratings about the business, hosted on the business's own site, are ineligible for review rich results.
2. **Ratings must not be aggregated from other sites.** Re-marking Google's own 71-review average as your site's `aggregateRating` is exactly the pattern that rule targets.

So this markup earns nothing today, and it is the category of structured data that draws a *spammy structured markup* manual action. It also creates a needless conflict: Google already holds the authoritative 4.9/71 on the GBP, and the site asserts a competing copy of it on ten URLs.

**Recommended fix**
Remove the `aggregateRating` and `review` properties from the `#business` node on **all ten files** (line numbers above). Keep the visible ratings block exactly as it is — it is honest, clearly source-attributed, useful to humans, and carries no markup risk. Google will continue to surface the real 4.9/71 in the Local pack from the GBP, which is where it belongs.

---

## C3 — A second, conflicting rating pool (4.9 / 24) on the `Apartment` nodes

**Current situation**

| File | Node | `aggregateRating` | `Review` objects | Line |
|---|---|---|---|---|
| `monthly-rental-igalo.html` | `#apartment` | 4.9 / **24** | 2 ("Marija K.", "Thomas B.") | 129 / 136 |
| `mesecni-najam-igalo.html` | `#apartment` | 4.9 / **24** | 3 | 139 / 146 |

Visible copy: *"Based on 24 tenant reviews · Season 2025-2026"* (EN) and *"4.9/5 · 24 recenzije"* (SR).

**GMB data:** One review pool for this address — 71 Google reviews.
**Website data:** Two incompatible pools for the same physical property: 71 (business) and 24 (apartment), plus 35 Booking + 15 Airbnb in the visible block.

**Why it matters**
Three separate problems:

- Same physical address, same operator, two different `aggregateRating` values in the same page's markup. Google has to decide which describes the entity, and there is no correct answer.
- The two language versions declare an **identical `reviewCount` of 24 but ship different review sets** (2 vs 3). An identical count backing different content is a strong signal the number is not derived from a real review store.
- The reviewers are unverifiable placeholders — "Marija K.", "Thomas B.", "Remote developer, season 2024-2025". Anonymous first-party reviews on your own site, with no collection mechanism anywhere on the domain, fail the "ratings must be sourced directly from users" requirement.

**Recommended fix**
Remove `aggregateRating` and `review` from both `#apartment` nodes (`monthly-rental-igalo.html:129,136` and `mesecni-najam-igalo.html:139,146`). If these are genuine long-stay tenant testimonials, keep them as visible on-page content — they read well and help conversion — just without structured-data markup. Also reconcile the visible "24 tenant reviews" with a real, countable source, or soften it to "long-stay guests tell us…".

---

## C4 — `vesti/10-reasons-why-to-travel-to-herceg-novi-montenegro.html` is disconnected from the business entity

**Current situation**

| Metric | EN page | SR counterpart (`10-razloga-da-posetite-igalo.html`) |
|---|---|---|
| JSON-LD blocks | **0** | 4 (Article, ItemList, FAQPage, BreadcrumbList) |
| `#business` node | **absent** | present |
| Open Graph tags | **0** | full set |
| Twitter card tags | **0** | present |
| Footer address (`Dubrovačka 1`) | **absent** | present |
| Visible text | 5,922 chars | 10,516 chars |
| Internal links | 4 | 31 |
| File size | 10.7 KB | 84 KB |

**GMB data:** N/A — the point is that this page carries no link back to the GBP entity at all.
**Website data:** Every other page on the site carries the `#business` node, the footer NAP block and the shared design system. This one carries none of them.

**Why it matters**
This page is in the sitemap and is the `x-default` hreflang target for the EN/SR pair, so it is a genuine entry point for English searchers — and it is the one page that gives Google no address, no phone, no schema and no entity link. It also looks like a legacy page that predates the current template (10.7 KB vs 75–127 KB for its siblings), so it likely renders unstyled. Four internal links against the counterpart's 31 leaves it nearly orphaned from the rest of the site.

**Recommended fix**
Bring it to parity with `vesti/10-razloga-da-posetite-igalo.html`:
1. Add the standard `#business` JSON-LD block (copy from `vesti/beaches-herceg-novi.html`, minus the `aggregateRating`/`review` removed in C2).
2. Add `Article`, `ItemList`, `FAQPage`, `BreadcrumbList`.
3. Add the `og:*` and `twitter:*` head block.
4. Add the shared footer with the NAP block (`Dubrovačka 1, Igalo 85347, Crna Gora` + phone + email).
5. Add the shared stylesheet/template and the standard internal-link set.

**Exact location:** `vesti/10-reasons-why-to-travel-to-herceg-novi-montenegro.html` (whole file).

---

# Medium Issues (Orange)

## M1 — GBP "From the business" description is empty

**Current situation** The `From the business` column in the export is blank.
**GMB data:** No description.
**Website data:** Rich, specific descriptions in `about.html`, `index.html` and `llms.txt`.

**Why it matters** This is a free 750-character field that Google reads directly to understand what the business does, and it is one of the few places where you control the profile's own topical vocabulary. Leaving it empty while the website is dense with relevant description means the two sources are asymmetric — the site says a lot, the profile says nothing.

**Recommended fix** Populate it in the GBP dashboard, reusing language already on the site so the two agree. Draft, built from `about.html` and `llms.txt`:

> Porodični studio-apartmani Monako u Igalu, 100 m od mora i nasuprot Blatne plaže, 300 m od Instituta dr Simo Milošević. Studio apartmani za 2–4 osobe i apartmani sa odvojenom spavaćom sobom za 4–5 osoba — svi sa balkonom s pogledom na more, klima uređajem, čajnom kuhinjom, TV-om i besplatnim WiFi-jem. Besplatan parking, svakodnevno čišćenje, IDEA market u objektu. Rezervacija direktno kod vlasnika, bez provizija. Dostupni smo 24/7 na telefon i Viber. Nudimo i mjesečni najam van sezone (septembar–jun).

**Exact location:** GBP dashboard → Edit profile → From the business. No repo change.

---

## M2 — Schema type: `VacationRental` is a poor fit; `LodgingBusiness` is the better choice

**Current situation** The `#business` node uses `"@type": "VacationRental"` on all 11 pages (`index.html:56`, `about.html:52`, `blatna-plaza.html:55`, `monthly-rental-igalo.html:181`, `mesecni-najam-igalo.html:53`, `mimosa-festival-herceg-novi.html:97`, `praznik-mimoze-program.html:196`, `nova-godina-herceg-novi.html:159`, `rent-a-bike-herceg-novi-igalo.html:57`, `iznajmljivanje-bicikla-herceg-novi-igalo.html:57`).

**GMB data:** Primary category **Holiday apartment rental** — a staffed lodging category.
**Website data:** A multi-unit apartment house at one address, owner-operated, with **daily housekeeping**, **24/7 staff availability**, an **on-site IDEA market**, **airport transfers and excursions**, and a **three-star categorisation** ("Kategorisani apartmani — apartmani sa tri zvjezdice", `index.html`). Two distinct unit types are modelled via `containsPlace`.

**Why it matters**
`VacationRental` is valid schema.org, so this is not broken markup — but it is the wrong entity shape here, for two reasons:

1. **It is program-gated at Google.** Google's vacation-rental structured data is limited to participants in the Vacation Rentals program, onboarded via feed with additional required properties (stable `identifier`, per-unit `containsPlace` detail). Plain markup outside the program produces no rich result, so the type buys nothing.
2. **It describes the wrong business model.** `VacationRental` connotes a self-catering unit let without on-site service. This business has daily housekeeping, permanent staff presence, on-site retail and a star rating — that is a lodging *business*, which is also what the GBP category says.

**Recommended fix**
Change `"@type": "VacationRental"` → `"@type": "LodgingBusiness"` on all 11 nodes. `LodgingBusiness` is the direct parent of `VacationRental`, is an unambiguous `LocalBusiness` subtype handled under Google's standard Local Business documentation, and maps cleanly onto "Holiday apartment rental". Everything currently on the node — including `containsPlace` → `Accommodation` — remains valid without modification.

Keep `Apartment` on the two `#apartment` nodes; that type correctly describes the individual long-stay unit.

---

## M3 — Two GBP secondary categories contradict the website's core message

**Current situation**
**GMB data:** Additional categories include **Apartment rental agency** and **Vacation home rental agency**, plus **Guest house** and **Serviced accommodation**.
**Website data:** The site's central claim is the opposite of an agency. `index.html` title: *"Direktno od Vlasnika, Bez Provizije"*. Body copy: *"Zašto rezervisati direktno kod nas?"*, *"bez posrednika, bez naknade"*, *"Rezervišite direktno i uštedite na provizijama platformi"*. The words "guest house" / "pansion" and "serviced accommodation" appear nowhere on the site.

**Why it matters**
An "agency" category tells Google you broker other owners' properties; the website tells Google you are the owner and there is no intermediary. Google uses categories to place the profile in a competitive set, so the two agency categories can surface the profile against booking agencies rather than against accommodation — while the landing page's whole argument is that it is *not* one. "Guest house" and "Serviced accommodation" are not contradicted by the site, but they are unsupported by it, so they add category surface with no corroborating content.

**Recommended fix**
In the GBP dashboard, keep **Holiday apartment rental** (primary) and **Holiday apartment**. Remove **Apartment rental agency** and **Vacation home rental agency** unless you genuinely also let other owners' units. Keep **Guest house** / **Serviced accommodation** only if you add content supporting them. Fewer, corroborated categories model the entity better than more, uncorroborated ones.

**Exact location:** GBP dashboard → Edit profile → Categories. No repo change.

---

## M4 — Messaging channels do not line up

**Current situation**

| Channel | Website | GBP |
|---|---|---|
| Viber | Primary CTA. 150+ mentions, `viber://chat?number=%2B38267558240` deep links, dedicated buttons in the header, hero, call bar and contact block | no field exists |
| WhatsApp | `https://wa.me/38267558240` (2 pages), "WhatsApp" named 8× | **empty** |
| SMS | not surfaced | `sms:+38267558240` |
| Primary chat | — | **empty** |

**Why it matters** The channel the site pushes hardest (Viber) is invisible on the profile, and the WhatsApp link the site does publish is not declared on the profile even though the field exists and the number is already live. A searcher who finds you on Maps sees a different contact surface than one who lands on the site — and Google sees fewer corroborated contact methods than actually exist.

**Recommended fix**
- Set the GBP **WhatsApp** field to `https://wa.me/38267558240` — only because that link is already live on the site; do not add channels you don't operate.
- Set **Primary chat** so the profile has a declared default.
- GBP has no Viber field; that gap is not fixable. Compensate by keeping the phone number identical across both (it already is), since Viber resolves on that number.
- Optional: add a `contactPoint` to the `LodgingBusiness` node listing the phone with `contactType: "reservations"` and `availableLanguage`.

**Exact locations:** GBP dashboard for the first two. `wa.me` links: `index.html`, `monthly-rental-igalo.html`.

---

## M5 — No English homepage or English "About"; the GBP link lands international visitors on Serbian-only pages

**Current situation**
Pages with **no** hreflang and **no** English counterpart: `index.html`, `about.html`, `blatna-plaza.html`, `blog.html`, `nova-godina-herceg-novi.html`, `vesti/atrakcije-herceg-novi.html`.
English pages that **do** exist — `monthly-rental-igalo.html`, `rent-a-bike-herceg-novi-igalo.html`, `mimosa-festival-herceg-novi.html`, `vesti/beaches-herceg-novi.html`, `vesti/restaurants-herceg-novi.html`, `vesti/10-reasons-...html` — have no English homepage or About to link back to.

**GMB data:** The website link (`https://apartmani-igalo.com/?utm_source=gbp&utm_medium=organic`) points at the Serbian homepage for every visitor, from every country.
**Website data:** `mesecni-najam-igalo.html` states *"Govorimo SR · EN · RU · DE"*, and `llms.txt` describes the Institute's guests as coming "from across Europe and Russia".

**Why it matters** The business explicitly serves four language markets and the profile is the main discovery surface for foreign visitors — but the entry point and the credibility page (About) exist in Serbian only. The English pages are effectively orphaned: they have no English home to link to, so English sessions dead-end or bounce to a Serbian page. This is a conversion problem first and a coverage problem second.

**Recommended fix** Add, at minimum, `index-en.html` (or `/en/`) and `about-en.html`, hreflang-paired with the Serbian originals, and link them from the existing English pages' navigation. Reuse the existing template; the content already exists in `about.html` and `llms.txt`.

---

## M6 — Business-name variants are inconsistent, especially in title tags

**Current situation**

| Variant | Occurrences |
|---|---|
| Apartmani Igalo Monako *(= GBP name)* | 115 |
| Apartmani Monako | 20 |
| Monako Apartmani | 19 |
| Monako Apartments | 10 |
| Monako Igalo | 8 |

Title-tag suffixes differ page to page: `| Monako Igalo`, `| Monako Apartmani`, `| Monako`, `| Monako Apartmani`, and several pages carry no brand token at all (`mesecni-najam-igalo.html`, `monthly-rental-igalo.html`, `nova-godina-herceg-novi.html`, `praznik-mimoze-program.html`).

**GMB data:** `Apartmani Igalo Monako`
**Website data:** Five variants, no single dominant form in titles.

**Why it matters** These are all recognisably the same brand, so this is not a NAP break — but title tags are heavily weighted for brand-token association, and the brand string in SERPs currently changes shape from page to page while a third of pages omit it. Consistency here is cheap and directly reinforces the GBP name match.

**Recommended fix**
1. Standardise every title suffix to a single form. `| Apartmani Igalo Monako` is the exact GBP match; if that is too long for some titles, use `| Monako Igalo` consistently rather than mixing.
2. Add the legitimate variants to schema so Google can reconcile them, on the `LodgingBusiness` node:
   ```json
   "alternateName": ["Apartmani Monako", "Monako Igalo", "Monako Apartments"]
   ```

**Exact locations:** `<title>` in all 19 files; `alternateName` alongside `"name"` in the 11 `#business` blocks.

---

## M7 — `hotel-monako@hotmail.com` as the sole business email

**Current situation** The address appears 87 times across the site and in `llms.txt` and the schema `email` property.

**GMB data:** GBP has no email field, so there is nothing to contradict.
**Website data:** `hotel-monako@hotmail.com` everywhere.

**Why it matters** Two soft trust issues. First, the local-part says **hotel** while both the GBP primary category and every line of site copy say *apartments* — a small semantic mismatch on a string that appears 87 times. Second, a free webmail address on a business that owns its domain is a weaker credibility signal than a domain mailbox, particularly for a lodging business asking guests to book direct and transfer deposits without a booking platform's protection.

**Recommended fix** Move to `info@apartmani-igalo.com` (or `rezervacije@`), forwarding to the existing Hotmail inbox so nothing breaks operationally. Update all 87 occurrences plus `llms.txt` and the schema `email` property. Keep the Hotmail address working for a transition period. This is not urgent, but it is worth doing before the next season.

---

# Minor Improvements (Green)

## G1 — Empty GBP fields worth filling

| Field | Current | Suggested |
|---|---|---|
| Store code | Missing | Set any internal code (e.g. `MONAKO-IGALO-01`) — makes future exports/API work cleaner |
| Labels | Empty | e.g. `igalo`, `apartmani`, `direct-booking` — private, for your own filtering |
| Amenity attributes | Unset | The site lists eight amenities with direct GBP equivalents: free WiFi, free parking, daily housekeeping, air conditioning, sea-view balcony, kitchenette, airport transfer, on-site shop. Setting them corroborates the site's `amenityFeature` list |
| LGBTQ+ friendly | Empty | Set only if true |

**Location:** GBP dashboard. No repo change.

## G2 — Add `starRating` to the lodging node

`index.html` states *"Kategorisani apartmani — apartmani sa tri zvjezdice"*, but the markup does not express it. `LodgingBusiness` supports it:

```json
"starRating": { "@type": "Rating", "ratingValue": "3" }
```

Note this is an official categorisation, not a review score, so it is unaffected by C2. **Location:** the 11 `#business` blocks.

## G3 — Add `knowsLanguage`

`mesecni-najam-igalo.html` claims SR · EN · RU · DE. Supported on `LocalBusiness`:

```json
"knowsLanguage": ["sr", "en", "ru", "de"]
```

**Location:** the 11 `#business` blocks.

## G4 — `priceRange`

Currently absent. Seasonal prices are deliberately "na upit", so a precise value would be misleading — but `monthly-rental-igalo.html` publishes €500/month. Either omit `priceRange` entirely (fine) or use a broad honest band. Do not invent a nightly rate that isn't published.

## G5 — `checkinTime` / `checkoutTime`

Absent from the lodging node. `index.html` advertises *"Fleksibilnost pri dolasku i odlasku"*. Add only if real published times exist; flexible arrival is a legitimate reason to leave these out.

## G6 — `addressRegion` is inconsistent between nodes

The `TouristAttraction` node in `blatna-plaza.html` sets `addressRegion: "Herceg Novi"`, while all `#business` nodes omit `addressRegion` entirely. GBP's Administrative area is also empty, so the business node currently matches GBP — but the internal inconsistency is untidy. Either add `"addressRegion": "Herceg Novi"` to both the business nodes *and* the GBP Administrative area field, or drop it from the attraction node. Keeping site and GBP aligned matters more than which option you pick.

## G7 — hreflang granularity

Pages declare `hreflang="sr"` while `<html lang="sr-Latn-ME">`. Both are valid and Google handles the mismatch, but `hreflang="sr-Latn"` would match the declared script. Very low priority — do not touch if you would risk breaking the currently well-formed bidirectional pairs.

## G8 — GBP website URL carries UTM parameters

`https://apartmani-igalo.com/?utm_source=gbp&utm_medium=organic` versus the canonical `https://apartmani-igalo.com/`. This is standard, accepted attribution practice and the self-referential canonical prevents any duplicate-URL indexing, so **no change is required**. Noted only so it is not mistaken for an inconsistency in future audits. Leave as is unless you stop using GA/UTM reporting.

## G9 — Video assets

`index.html` carries a `VideoObject` and the repo holds `video/Monako_about.mp4` and `video/apartmani-igalo-mobile.mp4`. The GBP links a YouTube channel. Publishing the same walkthrough video on the GBP profile and on the linked YouTube channel gives Google a third corroborating media signal between the two surfaces.

## G10 — Consider a dedicated location/contact page

The NAP block currently lives in footers and in the contact section of `index.html`, `about.html`, `blog.html` and `blatna-plaza.html`. A single `kontakt.html` with the full NAP, the Maps embed, hours, directions from Herceg Novi and from the airport, and the parking note would give the GBP a natural, specific landing target and consolidate the location signals now spread across four pages.

---

## Notes on scope

- **Keyword stuffing / over-optimisation:** checked, none found. Titles and meta descriptions are within normal length (53–80 and 134–216 characters), read naturally, and the guide pages (`vesti/`) carry genuine editorial content with real local detail rather than keyword padding.
- **Thin content:** only `vesti/10-reasons-why-to-travel-to-herceg-novi-montenegro.html` qualifies (see C4). Every other page is substantive.
- **Duplicate content:** the EN/SR pairs are properly hreflang-annotated, so they are not duplicates in Google's terms.
- **Location conflicts:** none. Every address, coordinate and map reference on the site resolves to the same place as the GBP.
- **This file** is inside a GitHub Pages repository served from the root, so it is technically reachable at `apartmani-igalo.com/docs/gbp-website-audit.md`. It is not linked from any page and not in `sitemap.xml`, so it will not be discovered or indexed — but delete it once actioned if you would rather it not exist publicly.
