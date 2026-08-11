# GBP Performance Context — May–July 2026

**Business:** Apartmani Igalo Monako · Dubrovačka 1, Igalo 85347, ME
**Source:** Gemini analysis of the owner's Google Business Profile performance export,
covering May, June and July 2026. Supplied by the owner 2026-08-11.
**Purpose:** first-party demand data to reason from in future website / SEO / GBP work.
This is the only dataset in the repo describing *actual measured demand*. The two
existing audits (`gbp-website-audit.md`, `geo-ai-overviews-audit.md`) describe the
*site and profile*; this one describes the *market's behaviour toward them*.

Everything below separates three things, and future work should keep them separate:

- **DATA** — numbers straight from the GBP export. Trustworthy.
- **DERIVED** — arithmetic on that data. Trustworthy, shown so it can be re-checked.
- **HYPOTHESIS** — interpretation. Not established. Do not cite as fact.

---

## 1. The data

| Metric | May | June | July | 3-mo total |
|---|---:|---:|---:|---:|
| Mobile Search impressions | 2,666 | 7,137 | 7,305 | **17,108** |
| Mobile Maps impressions | 3,353 | 4,604 | 3,791 | **11,748** |
| Desktop Search impressions | 249 | 620 | 681 | **1,550** |
| Desktop Maps impressions | 54 | 89 | 112 | **255** |
| **Total impressions** | **6,322** | **12,450** | **11,889** | **30,661** |
| Phone calls | 68 | 132 | 192 | **392** |
| Direction requests | 67 | 105 | 120 | **292** |
| Website clicks | 38 | 77 | 113 | **228** |
| **Total actions** | **173** | **314** | **425** | **912** |
| GBP messages / bookings | 0 | 0 | 0 | **0** |

Profile state: verified, 71 Google reviews, 4.9 average, 8 reviews in June–July,
last 10 all 5-star. Owner replies to reviews.

---

## 2. Corrections to the source report

The report is broadly sound but three claims are wrong or mis-stated, and future work
should use the corrected versions.

### 2.1 Impressions did not grow through July — they peaked in June

> Report: *"scaling from 6,322 total impressions in May to 11,889 in July"*

**DERIVED:** total impressions were 6,322 → 12,450 → 11,889. June is the peak.
July was **-4.5% vs June**, not growth. Comparing May to July skips over the actual
high-water mark and turns a decline into a rise.

### 2.2 The "Maps visibility drop" is the wrong headline — July was the best month

The report names the Mobile Maps decline (4,604 → 3,791, -17.7%) as the **biggest
weakness**. The conversion data does not support that reading.

**DERIVED — action rate per impression:**

| | May | June | July |
|---|---:|---:|---:|
| Total actions ÷ total impressions | 2.74% | 2.52% | **3.57%** |
| Calls ÷ total impressions | 1.08% | 1.06% | **1.61%** |
| Website clicks ÷ total impressions | 0.60% | 0.62% | **0.95%** |
| Direction requests ÷ Maps impressions | 1.97% | 2.24% | **3.07%** |

July delivered **4.5% fewer impressions and 35% more actions** than June. Action rate
rose 42% month-on-month. Direction requests per *Maps* impression — the metric most
directly exposed to the Maps drop — rose **37%** in the very month Maps impressions fell.

**HYPOTHESIS (competing with the report's):** the report attributes the Maps decline to
competitors out-ranking the profile via ad spend or better optimisation. The data is at
least equally consistent with a **shift in impression mix**: in peak season fewer people
browse the map speculatively (they have already booked) and a larger share of those who
do are in-market and nearby. Losing low-intent discovery impressions while gaining
high-intent ones produces exactly this signature. The report's explanation is untested
and its evidence — a single month's dip in one surface — is thin.

**Rule for future work:** do not treat the Maps dip as a confirmed ranking loss or spend
effort "recovering" it until a second data point exists. Check August/September Maps
impressions *alongside* direction requests per Maps impression. If impressions fall and
the per-impression action rate also falls, it is a ranking problem. If impressions fall
and the action rate holds or rises, it is seasonal mix and needs no fix.

### 2.3 The price-query volume is overstated ~3×

> Report: *"Satisfies the 400+ monthly searches for price-related keywords"*

The cited queries are **impressions over three months**, not monthly searches, and
impressions are not searches.

**DERIVED:**

| Cluster | 3-mo impressions | ≈ per month | Share of all impressions |
|---|---:|---:|---:|
| Price-explicit (`...i cene` 234, `blatna plaza...cene` 99, `apartmani igalo cijene` 41) | 374 | ~125 | 1.22% |
| + booking-comparison (`booking igalo apartmani` 141) | 515 | ~172 | 1.68% |

So ~125 price-intent impressions/month, not 400+ searches/month. The opportunity is
real but roughly a third of the stated size, and this matters because it is the number
weighed against the owner's standing decision on pricing (§5).

---

## 3. What the funnel actually says

**DERIVED, 3-month totals:**

- Action rate overall: 912 / 30,661 = **2.97%**
- Website CTR: 228 / 30,661 = **0.74%**
- Calls : website clicks = **1.72 : 1**
- Calls : direction requests = 1.34 : 1
- **Mobile is 94.1%** of all impressions (28,856 / 30,661). The report's "over 55%"
  refers to Mobile *Search* alone; the number that should drive design decisions is 94%.
- Search 60.9% (18,658) vs Maps 39.1% (12,003)
- Desktop is **5.9%** of impressions (1,805) — desktop-first work is close to worthless here.

**The single most important structural fact:** the phone is the product's checkout.
392 calls against 228 website clicks means the profile converts *directly*, and the
website is a secondary surface that most converting users never touch. Two consequences:

1. **A low website CTR is not automatically a failure.** The report calls 0.74% "weak."
   For a profile that displays a tappable phone number to a 94%-mobile audience, users
   bypassing the site to call is the funnel working. Website clicks still grew fastest of
   the three action types in July (+47% MoM vs +45% calls, +14% directions), so the site
   is not being abandoned.
2. **Anything that improves conversion must work on the phone, in the GBP surface, or in
   the first screen of a mobile page.** Desktop layout work, long-form pages that pay off
   below the fold, and anything requiring a form fill are all fighting the grain.

**The 0 / 0 line is the clearest gap in the whole dataset.** Zero messages and zero
bookings are not a performance problem, they are an *absence of the feature* — those
channels are switched off. Every other row had to be earned; these two are a setting.

---

## 4. Demand map — which queries exist, and which page owns each

**DATA (3-month impressions)**, with the repo page that should be the answer:

| Cluster | Queries & impressions | Owner page | State |
|---|---|---|---|
| **Core brand-category** (3,071 · 10.0%) | `igalo apartmani` 1,401 · `apartmani igalo` 914 · `igalo smestaj` 756 | `index.html` | Winning. Do not disturb. |
| **Proximity / beach** (544 · 1.8%) | `apartmani igalo blizu plaze` 325 · `igalo blatna plaza` 100 · `blatna plaza igalo smestaj` 68 · `igalo apartmani na samoj plazi` 51 | `blatna-plaza.html` | **Mismatch — see §6.1** |
| **Price / commercial** (515 · 1.7%) | `privatni smestaj igalo i cene` 234 · `booking igalo apartmani` 141 · `blatna plaza igalo smestaj cene` 99 · `apartmani igalo cijene` 41 | `index.html#cjenovnik` | **Unanswered — see §5** |
| **Competitor conquest** (373 · 1.2%) | `hotel kapri igalo` 169 · `palmon bay hotel & spa` 143 · `apart hotel katunjanin` 61 | — | Winning, unexploited |
| **Long-stay / off-season** | **zero impressions** for `mesečni najam`, `dugoročni najam`, `long term rental Igalo`, winter terms | `mesecni-najam-igalo.html` + `monthly-rental-igalo.html` | **See §6.2** |

Named queries total 4,503 = 14.7% of impressions. The other 85% is long tail across
100+ queries — worth remembering before over-fitting any single keyword.

**The competitor-conquest cluster is the most under-used asset here.** 373 impressions
came from people searching *named hotels* — Palmon Bay, Kapri, Katunjanin — and getting
shown this profile as the alternative. These are users who have already decided on a
hotel-class product and are comparison-shopping. Nothing on the site speaks to them.

---

## 5. The price decision — reopened, with new evidence

This is the one place where the new data bears directly on a decision already made, so
it needs stating precisely rather than being quietly re-litigated in a future task.

**What is on the site now:** `index.html:1899-1907` — a panel headed *"Cjenovnik - cijene
smještaja · Igalo"* whose headline is **"Cijena na upit"**, plus "Zavisi od termina,
dužine boravka i broja osoba." Studio (2-4) and Jednosoban (4-5) are named with no
figures. This is the only `Cijena na upit` string on the site. No `priceRange` on any
business node. The only published prices anywhere are the €500/month rate on
`mesecni-najam-igalo.html` / `monthly-rental-igalo.html`, in visible copy and `Offer` markup.

**How it got that way (`geo-ai-overviews-audit.md` §9):** "od 35 € za noć" used to appear
on four guide pages. Three of five placements carried no "van sezone" qualifier, so a
guest planning August read an off-season rate as the general starting price. **The owner
decided seasonal prices stay off the website** and all five mentions were removed. The
audit records this explicitly as "a deliberate, informed trade-off, not an oversight,"
and notes it forfeits the cost-intent query class. `gbp-website-audit.md` G4 likewise
marks `priceRange` "deliberately not added."

**What the new data adds:** the earlier decision was made against *third-party study
data* about cost-intent query density in general. There is now **first-party evidence
that this business's own audience issues price queries** — ~125 price-explicit
impressions/month, plus 47/month explicitly comparing against Booking.com
(`booking igalo apartmani`). That did not exist as evidence when the decision was taken.

**Why the owner's objection and the recommendation are not actually in conflict:** the
thing that was removed was a **single unqualified "from" number** — precisely the format
that misleads. Both audits and the new report converge on a different format: **brackets
plus the variables that move them** (season window, length of stay, number of people).
A seasonal range with its conditions attached cannot be misread as an August rate the way
"od 35 €" was, and it answers the query class without publishing a rate card.

**Standing position for future work:** treat price transparency as an **open question the
owner decides**, not a settled no and not a to-do. If asked to improve conversion or
capture price intent, propose the bracket-plus-variables format, state the ~125/month
figure honestly (not "400+"), reference the §9 decision by name so the owner knows what
they are revisiting, and do not silently reintroduce a bare "od XX €" anywhere.

---

## 6. Report recommendations vs. what the site already is

Checked against the working tree, 2026-08-11. Several report items are already built —
future work should not rebuild them.

### 6.1 "Create a Blatna Plaža landing page" — the page exists, but targets the wrong intent

`blatna-plaza.html` and `en/blatna-plaza.html` already exist and are in the sitemap.
**But** the title is *"Blatna Plaža Igalo – Lekovito Blato"* — it is a **guide to the
beach and its medicinal mud**, i.e. informational intent. The demand in §4 is
**commercial**: `apartmani igalo blizu plaze` (325), `blatna plaza igalo smestaj` (68),
`igalo apartmani na samoj plazi` (51) — people looking for *accommodation near* the beach.

So the correct action is **not** "create a page." It is: decide whether to retarget the
existing page toward accommodation intent, or add an accommodation-near-Blatna-plaža
section to it and let it serve both. Creating a second page risks cannibalising a page
that already ranks.

### 6.2 "Add Mesečni najam as a GBP service" — the website half is already done

`mesecni-najam-igalo.html` ("Mesečni Najam Igalo – 500€ Sve Uključeno") and
`monthly-rental-igalo.html` both exist, with `Offer` markup at €500. The report's finding
of **zero impressions** for long-term terms therefore is not a content gap — it is a
**GBP gap**. Two good pages exist and the profile gives Google no signal that this
business offers the service. This is a dashboard action, not a website action.

### 6.3 "Add a floating WhatsApp/Viber button" — half already done, half must be rejected

**Reject the WhatsApp half outright.** `gbp-website-audit.md` records that the owner
confirmed the business runs **Viber only and has never operated WhatsApp**, and every
`wa.me` reference was deliberately removed on 2026-07-26 (float button, hero CTA, contact
card, four copy references, and a matching `FAQPage` JSON-LD entry). The site now has
**zero** occurrences of `whatsapp` / `wa.me`. Re-adding it would advertise a channel
nobody monitors. **Never add WhatsApp to this site.**

**The Viber half is partly done.** `viber://` links exist on 30 pages, but a *floating*
button exists on only two — `mesecni-najam-igalo.html` and `monthly-rental-igalo.html`
(`.viber-float`, Viber purple `#6B57F1`). The homepage has Viber links but no sticky
widget. Given 94% mobile traffic, extending the existing `.viber-float` pattern to
`index.html`, `en/index.html`, `ru/index.html` and `blatna-plaza.html` is a real,
narrowly-scoped opportunity — and the component already exists to copy.

### 6.4 "Highlight the IDEA market / 60m quote on the homepage" — already done

The review quote *"U prizemlju Idea minimarket, a plaža na 60 metara. Odnos cijena-usluga
je 10+."* is already a testimonial on `index.html:2358`, `about.html:1370` and
`blatna-plaza.html:1498`, with EN equivalents on `en/index.html` and `en/blatna-plaza.html`.
"IDEA market u objektu" appears in the amenity data across ~20 pages.

**Note on the distance figures:** the site's own claim is **100 m** (155 occurrences);
every **60 m** occurrence is inside a *guest review quote*. That is not a NAP
inconsistency — it is a guest's words vs. the business's measurement — and it should not
be "fixed" in a future audit. Do not edit quoted review text to match marketing copy.

### 6.5 The FAQ recommendation — already satisfied

`cesta-pitanja.html`, `en/faq.html` and `ru/faq.html` all exist and carry the IDEA market
amenity. The suggested Q ("Koliko je udaljena prodavnica?") is worth checking for
explicitly, but the FAQ infrastructure and the fact are both already in place.

### 6.6 "Link GBP to an inquiry form" — no form exists on the site

**DATA:** zero `<form>` elements across all 31 HTML files. Every conversion path is
`tel:`, `mailto:`, `sms:` or `viber://`. If a GBP booking/action link is ever pointed at
"an inquiry form on the website," the form has to be built first — and on a static
GitHub Pages site that means a third-party form handler, which is a real decision with
privacy and deliverability consequences, not a small task. Given the 1.72:1 call-to-click
ratio, pointing a GBP action link at the *phone* or *Viber* is likely to outperform a form.

---

## 7. GBP dashboard backlog — merged

Neither the website nor this repo can change any of these. Consolidated from both prior
audits and the new report, with the causal link the report missed.

| # | Action | Source | Note |
|---|---|---|---|
| 1 | **Remove the two agency categories** — *Apartment rental agency*, *Vacation home rental agency* | `gbp-website-audit.md` M3 (open since 2026-07-25) | **Do this before, or together with, #2 — see below** |
| 2 | Delete auto-added services: Bill pay, Location consulting, Tenant representation, Online rental application, Private tours | New report | See below |
| 3 | Turn on Messaging / Chat | New report | 0 conversations on 28,856 mobile impressions; this is a switch, not a project |
| 4 | Add the business description ("From the business" is empty) | `gbp-website-audit.md` M1 — draft copy exists in that file | Lead with IDEA market in the building + daily maid service |
| 5 | Add custom services: *Mesečni najam*, *Dugoročni najam*, *Smeštaj za pacijente Instituta* | New report | The landing pages already exist — §6.2 |
| 6 | Remove food-vertical "More Hours": Drive-through, Delivery, Takeout, Happy Hour, Breakfast, Brunch | New report | |
| 7 | Set amenity attributes to match the eight the site lists; set store code / labels | `gbp-website-audit.md` G1 | |
| 8 | Optionally publish the walkthrough video to the profile / YouTube | `gbp-website-audit.md` G9 | |

**HYPOTHESIS, and the most useful thing in this section — #1 causes #2.** The report
treats the irrelevant services as an independent problem and says to delete them.
But *Bill pay*, *Tenant representation*, *Location consulting* and *Online rental
application* are the standard service set Google suggests for **real-estate agency
categories** — which is exactly what M3 flagged as still active on this profile.
**Deleting the services while leaving the two agency categories in place is likely to
see them repopulate.** Remove the categories first. This also means the two audits are
describing one root cause, and #1 is higher-leverage than its "medium" priority suggests.

**Not carried over from the report:** its suggestion to keep "Senior Hours for
Dr. Simo Milošević patients." The business is open 00:00–24:00 seven days a week (GBP
export, matched by `openingHoursSpecification` on all 13 business nodes). Adding a
narrower special-hours entry would contradict the 24/7 signal that is currently
consistent everywhere.

---

## 8. Decision rules for future work

1. **Mobile or nothing.** 94.1% of impressions are mobile. Judge every change on a phone
   viewport first.
2. **The phone is the checkout.** 392 calls vs 228 website clicks. Do not optimise the
   site in ways that add steps before a `tel:` tap, and do not treat low website CTR as
   self-evidently a defect.
3. **Don't chase the July Maps dip** until a second month confirms it, and confirm it
   with *action rate*, not impressions alone (§2.2).
4. **Quote the price-intent figure honestly** — ~125 impressions/month, not "400+
   searches" (§2.3).
5. **Never add WhatsApp** (§6.3). Viber only.
6. **Check the repo before building** anything the report calls "missing" — Blatna Plaža,
   monthly rental, FAQ and the Viber float component all already exist in some form (§6).
7. **Prefer GBP dashboard actions over website work** for the current backlog. The three
   highest-leverage items — messaging, categories/services, description — are all
   off-repo, and the site is already in good technical shape per both prior audits.
8. **Keep the entity-consistency invariants** from `gbp-website-audit.md` intact: no
   `aggregateRating`/`Review` on the business node, `LodgingBusiness` not `VacationRental`,
   one NAP, `hasMap` CID `3697180737008791124`, founding date 2000-07-12.

---

## 9. What this dataset does not tell us

Worth knowing before over-reading it:

- **No attribution.** We know 392 calls happened; we do not know which queries or which
  surface produced them. Every query-to-conversion claim here is inference.
- **Three months, one season.** May–July is the ramp into peak. There is no off-season
  baseline, so no trend claim survives outside summer — this matters most for the
  long-stay/digital-nomad positioning, whose season is precisely the months not measured.
- **Zero-impression terms are ambiguous.** Zero impressions for `mesečni najam` may mean
  no demand *or* no eligibility (the profile lists no such service). §6.2 assumes the
  latter because the pages exist and the service does; that assumption is untested.
- **No competitor data.** The competitor-conquest and Maps-drop readings both concern
  rivals we have no data on.
- **The underlying export was not seen by this repo** — only the report about it. Numbers
  here are as reported. If the raw export becomes available, re-verify §1 before building
  on the derived figures.
