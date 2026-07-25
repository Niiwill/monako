# Google Business Profile — SEO Audit & Optimization

**Profile:** Igalo Apartmani Monako · Dubrovacka 1, Igalo 85347, ME
**Export analysed:** `Ungrouped_locations` (25 Jul 2026)
**Cross-referenced against:** live site `apartmani-igalo.com` (`index.html` LodgingBusiness schema)
**Goal keywords:** apartments Igalo · apartments Herceg Novi · vacation rental Igalo

---

## Section 1 — Critical issues (fix immediately)

### 1.1 The business description is completely empty
`From the business` is blank. This is 750 characters of free, indexable, keyword-relevant
text — the single largest unused ranking surface on the profile. **Fix in Section 3.1.**

### 1.2 "Herceg Novi" does not appear anywhere in the profile
| Field | Value |
|---|---|
| Locality | Igalo |
| Administrative area | *(empty)* |
| Address line 1 | Dubrovacka 1 |

The profile carries **zero** "Herceg Novi" tokens, yet "apartments Herceg Novi" is a stated
goal keyword. Meanwhile the website schema already declares `"addressRegion": "Herceg Novi"`
— so the site and the profile disagree.

**Fix:** set `Administrative area` = `Herceg Novi`, and seed the term into the description
and services (Section 3).

### 1.3 Business name is inconsistent across three properties
| Source | Name |
|---|---|
| GBP export | `Igalo Apartmani Monako` |
| `index.html` schema `name` | `Monako Apartmani Igalo` |
| `index.html` `<title>` | `Apartmani Igalo Monako` |
| Facebook handle | `apartmanimonako` |

Three different word orders for one entity. Google resolves entities by matching the GBP
name against the name on the website, and mismatches weaken that link.

**Fix:** standardise on **`Apartmani Monako Igalo`** everywhere. Make the schema `name`
match the GBP name byte-for-byte, and move the other variants into `alternateName`
(the schema already has an `alternateName` array — keep them there).

> **Risk note, stated plainly:** the geo-modifier "Igalo" is only compliant if it appears on
> your physical signage. It is a real ranking help and it is what everyone in the market
> does, but a competitor can file a redressal to strip it. Defend it by uploading an
> exterior photo where the sign is legible. If the sign says only "MONAKO", the safe name is
> `Apartmani Monako` — and you recover the lost keyword through categories and services,
> which carry more weight than the name anyway.

### 1.4 Street name spelling does not match the site or the postal record
GBP has `Dubrovacka 1`; the site has `Dubrovačka 1`. Set GBP to **`Dubrovačka 1`** (with
diacritics) so the address string matches the site, the postal record, and citations.

### 1.5 The two categories are near-duplicates
`Holiday apartment rental` (primary) + `Holiday apartment` (secondary) describe the same
thing. You are using 1 of your 9 secondary slots and getting no additional query coverage
from it. **Fix in Section 3.2.**

### 1.6 `Status: Missing store code`
The only status flag Google raised on the export. It has **no direct ranking effect** on a
single-location profile, but it blocks clean bulk re-upload and API/Insights joins — and you
are re-uploading this sheet as part of this optimization. Set it to `MONAKO-IGALO-01`.

---

## Section 2 — Quick wins (high impact, low effort)

| # | Field | Now | Change to | Why it moves ranking |
|---|---|---|---|---|
| 1 | From the business | *empty* | Section 3.1 text | Keyword relevance for all 3 goal terms |
| 2 | Administrative area | *empty* | `Herceg Novi` | Only way to earn "Herceg Novi" proximity relevance |
| 3 | Additional categories | 1 duplicate | 5–7 from 3.2 | Each valid category = a new query set you're eligible for |
| 4 | Services | *empty* | Section 3.3 | Custom service names are free-text and indexed |
| 5 | WhatsApp URL | *empty* | `https://wa.me/38267558240` | Your own EN page pushes WhatsApp 8×; clicks are an engagement signal |
| 6 | Primary chat | *empty* | WhatsApp | Surfaces a chat button on Maps |
| 7 | Store code | *empty* | `MONAKO-IGALO-01` | Clears the export's only status flag |
| 8 | LGBTQ+ friendly | *empty* | `TRUE` | A user-facing filter in Maps — free eligibility |
| 9 | Special hours | *empty* | New Year + Mimosa Festival dates | You already have landing pages for both events |
| 10 | Website | root URL | add `?utm_source=gbp&utm_medium=organic` | Lets you actually prove GBP traffic in GA4 |

**Leave alone — already correct:**
- `Opening date: 2000-07-12` — a 26-year operating history is a trust signal. Keep it.
- `00:00-24:00` seven days — correct for lodging; keeps you eligible for the "Open now" filter.
- `Primary category: Holiday apartment rental` — already the best match. **Do not change it.**
  Changing a primary category triggers re-review and can reset ranking stability.
- `Labels` — internal filtering only, **zero** ranking effect. Don't spend time here.

---

## Section 3 — Optimized fields (ready to paste)

### 3.1 Business description

**Recommended (English, 694 / 750 chars)** — keyword-front-loaded so the goal terms survive
the ~250-char "read more" truncation:

```
Apartmani Monako rents self-catering holiday apartments in Igalo, Herceg Novi, 100 m from Blatna beach and directly opposite the Dr Simo Milošević Institute. Family-run since 2000, our sea-view studio and one-bedroom apartments include free WiFi, free private parking, air conditioning, kitchenette, balcony and daily housekeeping. Book direct with the owner - no agency commission and no hidden fees. Ideal for beach holidays in Herceg Novi, spa and rehabilitation stays at the Igalo Institute, monthly winter rentals and long-stay guests. Airport transfers from Tivat and Dubrovnik on request, bike rental available, and a mini-market inside the building. English, Russian and Serbian spoken.
```

**Alternative (Serbian, 625 / 750 chars):**

```
Apartmani Monako izdaju privatni smještaj u Igalu, Herceg Novi - 100 m od Blatne plaže i preko puta Instituta Dr Simo Milošević. Porodični objekat od 2000. godine nudi studio i jednosobne apartmane s pogledom na more, besplatnim WiFi-jem, besplatnim parkingom, klimom, čajnom kuhinjom, balkonom i redovnim čišćenjem. Rezervišite direktno kod vlasnika - bez provizije agencija i bez skrivenih troškova. Idealno za ljetovanje u Herceg Novom, boravak i rehabilitaciju u Institutu Igalo, mjesečni najam tokom zime i duži boravak. Transfer sa aerodroma Tivat i Dubrovnik na upit, iznajmljivanje bicikala i market u sklopu objekta.
```

**Which one:** your stated goals are English keywords, and your Serbian relevance is already
covered by the word "Apartmani" in the business name plus the Serbian website — so **use the
English version**. Then check GBP Insights → search terms after 30 days; if the majority of
queries come in Cyrillic or Serbian, swap to the Serbian version.

**Two rules I followed that you should keep if you edit this:**
- **No URLs and no phone number in the description.** Google's description guidelines reject
  URLs, and phone numbers frequently trip the promotional-content filter. Your number is
  already a structured field — repeating it there risks the whole description being rejected.
- Keyword density stays natural. "Apartments Igalo / Herceg Novi" appears as normal prose,
  not as a list. Stuffed descriptions get suspended, not ranked.

### 3.2 Categories

**Primary — keep unchanged:**
```
Holiday apartment rental
```

**Additional categories — replace the single duplicate with these:**

| Priority | Category (EN-GB label) | Justification |
|---|---|---|
| Core | Holiday apartment | keep — already set |
| Core | Serviced accommodation | daily housekeeping is a service you actually provide |
| Core | Guest house | matches owner-occupied private accommodation in ME |
| Core | Vacation home rental agency | catches US-English "vacation rental" queries |
| Strong | Apartment rental agency | justified by your monthly-rental pages |
| Optional | Extended stay hotel | only if monthly rental is a real product line |
| Optional | Lodging | broad safety net |

> Your GBP UI is in Serbian, so the picker will show these as `Iznajmljivanje apartmana za
> odmor`, `Pansion`, etc. Type the English term into the picker to find the match — and only
> add a category you genuinely qualify for. Irrelevant categories dilute primary-category
> relevance and can get the profile filtered.

### 3.3 Services (add under your categories — free-text, indexed)

```
Sea view apartment rental Igalo
Studio apartment rental Herceg Novi
Family apartment rental Igalo
Monthly apartment rental Igalo
Long-term winter rental Herceg Novi
Apartments near Igalo Institute (Dr Simo Milošević)
Apartments near Blatna beach
Spa and rehabilitation stay accommodation
Airport transfer Tivat and Dubrovnik
Bike rental Herceg Novi and Igalo
Free private parking
Daily housekeeping
Self check-in
New Year stay Herceg Novi
Mimosa Festival accommodation Herceg Novi
```

Each of these is a keyword surface *and* a real service you deliver — the last two map
directly to `nova-godina-herceg-novi.html` and `mimosa-festival-herceg-novi.html`, so the
profile and the site reinforce each other seasonally.

### 3.4 Attributes to enable

**Enable (all verifiable from your own site copy):**
`Free Wi-Fi` · `Free parking` · `Air conditioning` · `Kitchen / kitchenette` · `Balcony` ·
`Beach access` · `Housekeeping` · `Airport shuttle` · `Family-friendly` · `Non-smoking` ·
`Luggage storage` · `Self check-in` · `LGBTQ+ friendly`

**The high-leverage one nobody in your market sets:**
You are *directly opposite the Dr Simo Milošević rehabilitation institute*. A large share of
Igalo's off-season demand is medical-rehabilitation guests with mobility needs, and they
filter Maps hard on accessibility. Set — **only if truthfully accurate**:

`Wheelchair accessible entrance` · `Wheelchair accessible parking` · `Step-free access`

Do not claim these if the property has stairs; a false accessibility attribute earns edits
and one-star reviews. If only some units qualify, say so in the description instead.

**Languages spoken:** Serbian, English, Russian — the Russian setting matters, see 5.3.

### 3.5 Other fields

```
Store code:            MONAKO-IGALO-01
Address line 1:        Dubrovačka 1
Administrative area:   Herceg Novi
Business name:         Apartmani Monako Igalo
WhatsApp URL:          https://wa.me/38267558240
Primary chat:          WhatsApp
LGBTQ+ friendly:       TRUE
Website:               https://apartmani-igalo.com/?utm_source=gbp&utm_medium=organic
```

A re-uploadable version of the full sheet with all of the above applied is at
`seo/gbp-optimized-upload.csv`.

---

## Section 4 — "Google updates" vs "My data"

**There are no pending Google updates in this export.** The `Google updates` column is empty
on your only data row, and the `Status` column reads `Missing store code` — not
`Google updated` / `Pending edit`. So there is nothing to accept or reject today. I'm not
going to invent a comparison table for updates that don't exist.

What that column *is*: when Google's algorithms, a Street View pass, or a public "Suggest an
edit" propose a change, the value appears there and you approve or discard it in
**Profile → Updates from Google**. Once you make the Section 3 edits, expect edits to start
arriving — this is the decision rule to apply for a lodging profile in Montenegro:

| Update type | Decision | Why |
|---|---|---|
| Hours changed to a limited range (e.g. `09:00-17:00`) | **Reject** | Kills your "Open now" eligibility. 24h is correct for lodging. |
| Category changed to `Hotel` / `Apart hotel` | **Reject** | Moves you into the hotel pack, where you compete against Hunguest/Palmon on price feeds you don't have. Stay in the rental category. |
| Category changed to `Apartment building` | **Reject** | Signals residential housing, not short-stay. Loses "vacation rental" intent entirely. |
| "Permanently closed" / "Temporarily closed" | **Reject immediately** | Almost always a competitor attack or a seasonal misread. Highest-damage edit that exists. |
| Address normalised to `Dubrovačka 1` with diacritics | **Accept** | Matches your site — this is 1.4 already fixed for you. |
| Administrative area filled in as `Herceg Novi` / `Opština Herceg Novi` | **Accept** | Exactly what 1.2 asks for. |
| Phone reformatted to `+382 67 558 240` | **Accept** | E.164 is what Google matches citations against. |
| Pin/marker moved | **Verify, then decide** | Check it against 42.4538, 18.5030 (your schema `geo`). Accept only if it lands on the building; a wrong pin destroys proximity ranking. |
| Website changed to a Booking.com/Airbnb listing | **Reject** | Hands your GBP link equity and your commission to an OTA. |
| Name changed to strip "Igalo" | **Judgement call** | See the risk note in 1.3. If your signage says "MONAKO", accept it and compensate via services. |

---

## Section 5 — Advanced improvements (beyond the spreadsheet)

### 5.1 Fix the website↔profile entity link (`index.html`)
These are code changes on this repo, none of them applied yet:

- **`name` mismatch** (line 59): schema says `Monako Apartmani Igalo`, GBP says
  `Igalo Apartmani Monako`. Make them identical.
- **`sameAs` is incomplete** (lines 85–88): it lists only Facebook and Instagram. Your GBP
  carries a YouTube channel too. Add YouTube **and your Google Maps place URL** —
  `sameAs` pointing back at the Maps listing is the strongest entity-consolidation signal
  available to you, and it's currently missing.
- **`hasMap`** (line 132) is a *search query* URL (`maps?q=Apartmani+Igalo+smjestaj+MONAKO`),
  not a place URL. Replace with the canonical place/CID link from your profile.
- **`priceRange: "Na upit"`** (line 66) is not machine-parseable. Use `"€€"` or a real range
  like `"€35-€90"`.
- **`aggregateRating` 4.9/71** (lines 105–111) is self-serving markup on your own
  `LodgingBusiness`. Google has not shown review stars for self-serving LocalBusiness reviews
  since 2019 — it isn't a penalty, but don't count on it. Your real review asset is the 71 on
  the GBP itself.

### 5.2 There is no English homepage
`index.html` is `lang="sr-Latn-ME"` and there are **no hreflang tags anywhere on the site**.
You have English variants for subpages (`monthly-rental-igalo.html`,
`rent-a-bike-herceg-novi-igalo.html`) but not for the homepage. You cannot realistically rank
for **"apartments Igalo"** or **"vacation rental Igalo"** — both English queries — with a
Serbian-only homepage. Build `/en/` and wire reciprocal `hreflang` (`sr-Latn-ME`, `en`,
`x-default`). This is the highest-effort item here and also the one that most directly blocks
two of your three goal keywords.

### 5.3 Add Russian
Herceg Novi's off-season and shoulder-season demand is heavily Russian- and
Ukrainian-speaking. `апартаменты Игало` has meaningful volume and near-zero optimized
competition. Set Russian in languages-spoken, and consider a `/ru/` page.

### 5.4 Ongoing (this is what actually holds a #1 position)
- **Review velocity + keyword-rich replies.** Steady beats bursty. In every reply, write the
  location naturally: *"Hvala! Drago nam je da vam se svidio apartman u Igalu…"*. Your replies
  are indexed; the reviewer's text is not something you control, but your reply is.
- **Weekly GBP Posts** linking to the seasonal pages you already have (Mimosa Festival, New
  Year, Blatna plaža, monthly rental). Posts decay after ~7 days — cadence matters more than
  polish.
- **Seed the Q&A section yourself.** Ask and answer: *"How far is the beach?"*, *"Is it near
  the Igalo Institute?"*, *"Do you offer monthly rental in winter?"*. Owner-answered Q&A is
  keyword-bearing content you fully control.
- **Geotagged photos, 3–5 per month.** Exterior with legible signage first — that photo also
  defends the "Igalo" name modifier from 1.3.
- **Citations:** consistent NAP on Montenegro directories and tourism portals. Use the exact
  Section 3.5 strings, diacritics included, everywhere.

---

## Section 6 — Three competitor keywords to target

1. **`privatni smještaj Igalo`** — the phrase the regional market actually types; "apartmani"
   is the crowded head term, "privatni smještaj" is where the booking intent sits. Your site
   already uses it in one `alternateName` but ranks nothing on it.
2. **`apartmani kod Instituta Igalo`** / **`accommodation near Igalo Institute`** — you are
   *literally opposite it*, demand is year-round rather than seasonal, and essentially nobody
   optimizes for it. Highest-conviction, lowest-competition term on this list.
3. **`apartmani Herceg Novi blizu plaže`** / **`apartments near Blatna beach`** — you own
   `blatna-plaza.html` already and you're 100 m away. Convert that page into the ranking
   asset for the modifier, not just an info page.

**Bonus:** `апартаменты Игало` — see 5.3.
