# Local SEO + GEO Audit — apartmani-igalo.com

**Scope:** how well the site's *code* communicates a clear, trustworthy, locally relevant business
entity to Google Search, Google AI Overviews, Google AI Mode, ChatGPT, Gemini and Perplexity.

**Date:** 2026-08-10 · **Commit audited:** `a8b151b` · **Files inspected:** 27 HTML pages,
`robots.txt`, `sitemap.xml`, `llms.txt`
**Prior work:** builds on `docs/gbp-website-audit.md` (2026-07-26). Where that audit made a
deliberate decision, this one either confirms it or explains what changed since.

---

## 0. A note on the source article

I was asked to start from the Search Engine Journal piece *"AI Overviews Now Answer Most Local
Searches: How To Get Your Business Cited."* **The SEJ domain is blocked by this environment's
network egress proxy, so I could not open the article itself.** Rather than guess at its contents,
I reconstructed its claims from the primary research it reports on — the
[Whitespark study on AI Overview prevalence in local search](https://whitespark.ca/blog/case-study-the-prevalence-of-ai-overviews-in-local-search/) —
plus secondary reporting and BrightLocal's consumer survey data. Everything I attribute to the
article below is a claim I could independently source. If any specific recommendation in the
article is missing here, it is because I could not verify it existed, not because I dismissed it.

---

## 1. Executive summary

**Overall: 57 / 100.** The site is technically clean, honestly written, and unusually well
structured for a family-run business. It is *not* well positioned to be cited by AI systems, for
two reasons that have nothing to do with technical SEO quality:

1. **The site refuses to answer the single question that triggers AI Overviews most often — price.**
   The Serbian homepage has a nav item called *"Cjenovnik"* (price list) pointing at a section
   titled *"Cjenovnik — cijene smještaja · Igalo"* whose entire content is *"Cijena na upit"*
   (price on request). Zero currency figures appear anywhere on `index.html`, `about.html` or
   `cesta-pitanja.html`. The meta description broadcasts *"cijene na upit"* to every crawler that
   reads it. Cost- and price-intent queries are the highest AI-Overview-density query class there
   is; a page that promises a price list and delivers none is not a candidate for those answers.

2. **Your most citable content is disconnected from your business entity.** Twelve of the thirteen
   `vesti/` guides — roughly 15,700 words of genuinely good local writing on beaches, restaurants,
   attractions, the Institute, sea temperature — carry `Article` markup whose `author` and
   `publisher` are an **inline, ID-less `Organization` stub**. They never reference
   `https://apartmani-igalo.com/#business`. To an entity-resolution system these guides are
   published by a nameless entity that happens to share a string with your business. This is
   exactly the content most likely to earn an AI citation for informational local queries, and the
   citation currently accrues to nothing.

Everything else in this report is smaller than those two items.

### Scorecard

| Dimension | Score | One-line verdict |
|---|:--:|---|
| Crawl & AI access | 9/10 | Static HTML, no JS dependency, all AI crawlers allowed. Near perfect. |
| Content coverage & local relevance | 8/10 | 17 substantive local guides. Real depth, real specifics. |
| Entity clarity (NAP, identity) | 7/10 | One address, one phone, one email, consistent everywhere. Solid. |
| Conversion path from an AI answer | 7/10 | Phone + Viber + email on every page; no online booking. |
| Trust & third-party corroboration | 5/10 | Real reviews exist off-site; markup never points at them. |
| Answerability / fact extractability | 5/10 | Strong FAQ prose; half the facts never reach the markup. |
| Freshness signals | 5/10 | Guides dated; the seven commercial pages carry no dates at all. |
| Multilingual reach | 5/10 | SR + EN only. You speak RU and DE and serve RU-speaking patients. |
| **Entity graph integrity** | **4/10** | 13 of 27 pages orphaned from `#business`. |
| **Price transparency** | **2/10** | The core AI-Overview trigger, deliberately unanswered. |

---

## 2. Validating the article against this business

The article's underlying data is sound. Its recommendations are not all equally relevant to a
seven-apartment family property in Igalo. Here is the honest split.

| Claim / recommendation | Evidence | Verdict for you |
|---|---|---|
| AI Overviews appear on 68% of local searches vs 39% for local packs | Whitespark, ~2026 | **Directionally true, but calibrate.** The study is US-query based. AI Overview density on Serbian-language queries in Montenegro is materially lower and later. Treat this as urgent for your *English/Russian/German planning traffic*, not for `apartmani Igalo`. |
| Simple local intent → AIO 15%, local pack >90% | Whitespark | **Important counterweight.** Your bread-and-butter query (`apartmani Igalo`) is still a local-pack query. **Do not de-prioritise the GBP.** |
| Informational intent → AIO 92% | Whitespark | **Highly relevant.** This is precisely your `vesti/` guide cluster. Biggest untapped surface — see §3.2. |
| Hybrid/cost intent → AIO 97% | Whitespark | **Most relevant single number in the study.** *"Average cost of an apartment in Igalo"*, *"how much is monthly rent in Herceg Novi"* — you are absent from all of it. |
| Price/cost/buy queries trigger AIO >80%; publish **ranges + the variables**, not fixed rates | SEJ | **Adopt. This is the highest-value recommendation in the article and it is compatible with your business model.** You are not being asked to publish a rate card. See §3.1. |
| 65% of AI citations do not overlap Google's top 10 | SEJ / industry | **Genuinely encouraging.** A small domain can win a citation without out-ranking Booking.com. Supports investing in the guides. |
| Consumers using AI for local recommendations: 6% (2025) → 45% (2026) | BrightLocal | Survey self-report; treat as trend, not conversion rate. Trend is real. |
| Review volume & recency drive AI citation | Industry consensus | **True, but the fix is not in this repo.** It is GBP work. And see the anti-recommendation in §5.1. |
| "150+ reviews is the AI citation threshold" | Vendor blogs | **Unverified marketing claim.** No primary source. You have 71 genuine Google reviews. Ignore the number; keep collecting reviews because it is good practice. |
| Add schema markup for AI Overview eligibility | SEJ / industry | **Half-true, and the half that's true is your weak spot.** Google states no special markup is required for AI Overview eligibility. Schema's real value is *entity disambiguation* for LLM retrieval — which is exactly what §3.2 and §3.3 are about. |
| Publish `llms.txt` | Common GEO advice | **Do not invest further.** See §5.2. |

---

## 3. Findings

### P0 — Findings that change whether you get cited at all

---

#### 3.1 The price question is asked, promised, and never answered

**Where:** `index.html` (nav `#cjenovnik`, section `Cjenovnik - cijene smještaja · Igalo`),
`en/index.html` (`#prices`), homepage FAQ `Koliko koštaju apartmani u Igalu?`,
`<meta name="description">`, `<meta property="og:description">`.

**Current state.** Every price surface resolves to *"Cijena na upit / Price on request. It depends
on your dates, length of stay and number of guests."* The only currency figure on the entire domain
that describes your own product is the €500/month long-stay rate. `index.html`, `about.html`,
`en/about.html` and `cesta-pitanja.html` contain **zero** currency figures.

**Why this matters more than it looks.** Three separate mechanisms are working against you:

- An extractive answer engine cannot cite a non-answer. When someone asks Gemini *"how much do
  apartments in Igalo cost in August"*, the model needs a number with a source. Yours is the one
  page that could give an owner-direct answer, and it declines. Booking.com and Airbnb do not
  decline.
- Your `og:description` — the string most likely to be pulled into a snippet or an embedding —
  literally reads *"cijene na upit"*. You are not merely silent; you are actively publishing
  "we won't tell you" as your summary.
- A nav item labelled *"Cjenovnik"* that leads to no prices is a small trust cost with human users
  and a mild quality signal with search systems.

**The nuance the article gets right.** The recommendation is *not* "publish a rate card". It is
publish an **honest range plus the variables that move it** — which is what you already explain in
prose, minus the numbers. Your existing copy already names every variable: dates, length of stay,
number of guests, off-peak before 1 July and after 1 September. You are one sentence of numbers
away from a complete, citable answer.

**What a citable version looks like** (illustrative — you supply the real bands):

> **Cijene 2026.** Studio za 2–4 osobe: **€35–€60 po noći** zavisno od termina. Apartman sa
> odvojenom sobom za 4–5 osoba: **€55–€90 po noći**. Cijena je po apartmanu, ne po osobi.
> Najniže cijene su do 1. jula i od 1. septembra; vrhunac sezone je od 15. jula do 20. avgusta.
> Za boravak duži od 7 noći cijena je niža. Parking, WiFi, klima, peškiri i posteljina su uključeni.
> Mjesečni najam van sezone: **€500 sve uključeno**.

Four things make that block extractable where the current one is not: a number, a unit, the
variables, and the inclusions. It is also *more* honest than "price on request", not less.

**Machine-readable counterpart.** Once real numbers exist on the page, and only then, add to the
`#business` node:

```json
"priceRange": "€35–€90",
"currenciesAccepted": "EUR",
"paymentAccepted": "Cash"
```

and give the two `Accommodation` nodes real offers:

```json
"potentialAction": null,
"offers": {
  "@type": "Offer",
  "priceSpecification": {
    "@type": "PriceSpecification",
    "minPrice": 35,
    "maxPrice": 60,
    "priceCurrency": "EUR",
    "unitText": "per night, per apartment"
  },
  "availability": "https://schema.org/InStock",
  "seller": { "@id": "https://apartmani-igalo.com/#business" }
}
```

Do the same on the monthly-rental pages. **Correction, found while implementing:** the Serbian
`mesecni-najam-igalo.html` already carried a complete `Offer` on its `Apartment` node — a proper
`UnitPriceSpecification` with `referenceQuantity`, `validFrom` and `validThrough`. Only the English
`monthly-rental-igalo.html` was missing one. The gap was half as wide as this section originally
claimed, and the fix was to mirror the existing Serbian shape rather than invent a second one.

> **This is a business decision, not a code decision.** If you have a deliberate commercial reason
> to keep seasonal prices off the web — negotiating room, undercutting OTA rate parity, avoiding
> price anchoring — that is a legitimate position and you should hold it. But it should be a
> *chosen* trade-off, priced accordingly: it costs you the entire cost-intent query class, which is
> the densest AI Overview surface that exists. A published range is compatible with rate parity
> agreements and with negotiating room; "on request" is what OTAs count on.

---

#### 3.2 Twelve local guides — your most citable asset — are orphaned from the business entity

**Where:** all of `vesti/` except `10-reasons-why-to-travel-to-herceg-novi-montenegro.html`, plus
`blog.html`.

**Current state.** These pages carry good `Article` markup — `headline`, `datePublished`,
`dateModified`, `ImageObject` with dimensions and captions, `FAQPage`, `ItemList`,
`BreadcrumbList`. But `author` and `publisher` look like this:

```json
"author":    { "@type": "Organization", "name": "Apartmani Igalo Monako", "url": "https://apartmani-igalo.com/" },
"publisher": { "@type": "Organization", "name": "Apartmani Igalo Monako", "url": "https://apartmani-igalo.com/",
               "logo": { "@type": "ImageObject", "url": "https://apartmani-igalo.com/images/monako-favicon.png" } }
```

No `@id`. No reference to `https://apartmani-igalo.com/#business`. Thirteen of your twenty-seven
pages never mention that identifier at all.

**Why this is the structural defect.** The whole point of `@id` in JSON-LD is that it lets a
consumer merge nodes into one entity. Without it, a graph builder sees a `LodgingBusiness` on
thirteen pages and a separate, property-poor `Organization` on thirteen others, and has to guess
they are the same thing from a name string. Sometimes it will guess right. It should not have to
guess.

The consequence is precise and expensive: `vesti/plaze-herceg-novi.html` is a strong, specific,
photograph-rich answer to *"best beaches in Herceg Novi"* — a 92%-AI-Overview query class. When a
model retrieves and cites it, nothing in the document connects that authority to the accommodation
business 100 m from one of the beaches it describes. You are doing the work of an authoritative
local publisher and banking none of it.

**Fix.** Two lines per file. Replace both stubs with:

```json
"author":    { "@id": "https://apartmani-igalo.com/#business" },
"publisher": { "@id": "https://apartmani-igalo.com/#business" }
```

and add a full `#business` node to each page (or, better, one `@graph` include per page carrying
`WebSite` + `LodgingBusiness` + the page node). Also add to each `Article`:

```json
"isPartOf":   { "@id": "https://apartmani-igalo.com/#website" },
"about":      { "@id": "https://apartmani-igalo.com/#business" },
"inLanguage": "sr-Latn-ME"
```

Note `vesti/plaze-herceg-novi.html` declares `"inLanguage": "sr"` while `<html lang="sr-Latn-ME">`
— harmless, but worth aligning while you are in the file.

**Also fix `cesta-pitanja.html`:** it uses `"isPartOf": { "@id": ".../#business" }`. `isPartOf`
should point at a `WebSite` or `CollectionPage`; a business is not a part-of parent for a web page.
`about` is already correct. Change `isPartOf` to target `#website` once that node exists (§3.4).

---

### P1 — Findings that reduce how confidently you are cited

---

#### 3.3 Facts you now publish in prose still have not reached the markup

The FAQ page added in PR #86 is excellent — it is the most quotable page on the site, and it
answers the operational questions guests actually ask. But those facts exist only as sentences.
The `#business` node still does not know any of them.

`docs/gbp-website-audit.md` §G5 decided *not* to add `checkinTime` / `checkoutTime` because
"no fixed published times exist". **That decision is now stale** — `cesta-pitanja.html` publishes
them explicitly.

| Fact, now published in prose | Where | Schema property that should carry it |
|---|---|---|
| Check-in from 12:00, check-out by 10:00 | `cesta-pitanja.html` | `"checkinTime": "12:00:00"`, `"checkoutTime": "10:00:00"` |
| Pets welcome | `cesta-pitanja.html` | `"petsAllowed": true` |
| Cash only, on arrival | `cesta-pitanja.html` | `"paymentAccepted": "Cash"`, `"currenciesAccepted": "EUR"` |
| No deposit, free cancellation by phone | `cesta-pitanja.html` | Prose only (no clean property) — keep as FAQ, it is already well-formed |
| No lift in the building | `cesta-pitanja.html` | `LocationFeatureSpecification` `{"name":"Lift","value":false}` — a **false** amenity is a genuine accessibility signal, and it is the honest answer for Institute patients |
| Shared washing machine | `cesta-pitanja.html` | `{"name":"Zajednička mašina za veš","value":true}` |
| Air conditioning at no extra charge | `cesta-pitanja.html`, `index.html` | Already present as `Klima uređaj` — fine |
| Price is per apartment, not per person | `cesta-pitanja.html` | Belongs in the `Offer.priceSpecification.unitText` from §3.1 |
| Airport transfer available for a fee | `index.html` | Present as an amenity, but `"Transfer od aerodroma": true` overstates it — it is paid, not included. Consider moving to `makesOffer`. |

These are cheap, they are true, and they are exactly the attribute-level facts an AI answer needs
in order to say *"yes, this one allows pets and check-in is from noon"* rather than *"contact the
property to confirm"*.

---

#### 3.4 There is no site-entity spine

- **No `WebSite` node on the homepage.** The only `WebSite` node on the domain lives on
  `mesecni-najam-igalo.html` — a deep commercial page — and carries `@id`
  `https://apartmani-igalo.com/#website` with the description *"Mesečni najam apartmana u Igalu…
  500€ sve uključeno."* A site-level entity is being defined by, and described as, one product
  page. Move it to `index.html` and `en/index.html`, give it a site-level description, and add
  `"publisher": { "@id": ".../#business" }`.
- **No `logo` on the `#business` node.** The `Article` publisher stubs reference
  `images/monako-favicon.png`, but the business node itself — the one entity that matters — has
  `image` and no `logo`. Add it.
- **`about.html` has no page-level node.** `en/about.html` correctly carries `AboutPage`;
  the Serbian `about.html` carries only `LodgingBusiness` + `BreadcrumbList`. Asymmetric.
- **No `founder` / `Person`.** The site's strongest E-E-A-T asset is that this is a named family
  running the property since 2000, and a guest review on the homepage names *Tatjana* as the host.
  `"founder": {"@type":"Person","name":"…"}` on the business node, and a named human on the About
  page, is the single cheapest experience signal available to you. Named authorship is a
  documented differentiator in AI source selection; anonymous corporate voice is not.

---

#### 3.5 Your review authority exists, and your markup never points at it

**Current state.** `sameAs` on the `#business` node lists Facebook, Instagram and YouTube. The
visible ratings block on `index.html` cites *4.9/5 · 71 ocjena · Google*, *10/10 · 35 ocjena ·
Booking.com* and *5/5 · 15 ocjena · Airbnb* — as **plain text with no links**. `hasMap` carries the
Google Maps CID, which is good. But there is no machine-followable path from your entity to the
three platforms where 121 real reviews about you actually live.

**Fix — and note what the fix is *not*.**

```json
"sameAs": [
  "https://www.facebook.com/apartmanimonako/",
  "https://www.instagram.com/apartmani.igalo/",
  "https://www.youtube.com/@monako-apartmaniigalo5135/",
  "https://www.google.com/maps?cid=3697180737008791124",
  "<your Booking.com property URL>",
  "<your Airbnb listing URL>"
]
```

Linking the visible rating figures to their sources is worth doing for humans too — an
unlinked "4.9/5 · 71 reviews" is an assertion; a linked one is verifiable. Verifiability is the
entire currency of trust signals in AI retrieval.

See §5.1 for what **not** to do here.

---

#### 3.6 Freshness is missing on exactly the pages that sell

Twenty pages carry `datePublished` / `dateModified`. The seven that do not are:
`index.html`, `en/index.html`, `about.html`, `en/about.html`, `blog.html`, `blatna-plaza.html`
(has an `Article` node with an `author` but no dates at all), and `cesta-pitanja.html`.

Those are your commercial pages. For a seasonal business, recency is a substantive claim, not
decoration: a model choosing between two Igalo sources for *"prices for summer 2026"* has no way to
know yours is current. Add `dateModified` to the `WebPage` node on each, and — on the price section
specifically — a visible *"Cijene ažurirane: avgust 2026."* line. Visible dates are read by
extractive systems; invisible-only dates are trusted less.

---

#### 3.7 Language reach stops two languages short of your actual guests

`knowsLanguage` correctly declares `sr, en, ru, de`, and the FAQ confirms you serve guests in all
four. The site exists in two. Your nearest landmark is the **Institut Dr Simo Milošević**, whose
therapy guests are disproportionately Russian- and German-speaking, and who search in those
languages — often through ChatGPT and Gemini, which are entirely language-agnostic and do not care
about Montenegrin AI Overview rollout schedules.

There is also an internal gap: **`cesta-pitanja.html` and `blatna-plaza.html` have no English
version.** The FAQ page is your best-extracting page and it is monolingual; `blatna-plaza.html` is
your unique-asset page — the therapeutic mud beach is the one thing about your location that no
competitor in Herceg Novi can claim — and international visitors cannot read it.

Priority order if you do this: EN `cesta-pitanja` → EN `blatna-plaza` → RU homepage + FAQ →
DE homepage. Machine-translated-then-human-checked is fine; leaving it monolingual is not.

*(The missing `hreflang` on `blatna-plaza.html`, `blog.html`, `nova-godina-herceg-novi.html` and
`vesti/atrakcije-herceg-novi.html` is **correct as-is** — there is no alternate to point at. The
prior audit's G7 note was right to leave it alone. The problem is the missing pages, not the tags.)*

---

### P2 — Smaller items

**3.8 English homepage is a thinner entity than the Serbian one.** `en/index.html` has 5 FAQ
entries against the Serbian page's 9, and its two `Accommodation` nodes have no `amenityFeature`
arrays while the Serbian ones do. Same property, two different levels of machine-readable detail.
Bring EN to parity — the English page serves the AI-heavier audience.

**3.9 A second phone number appears on two pages. ~~Fix this.~~ Withdrawn — it is already correct.**
`+382 69 530 869` appears on `rent-a-bike-herceg-novi-igalo.html` and
`iznajmljivanje-bicikla-herceg-novi-igalo.html` (against 221 occurrences of the primary
`+382 67 558 240`). I flagged it as a possible NAP inconsistency. **On inspection it is not one:**
the number is already attributed to a third party — *Rent a Bike Herceg Novi* — as its own
`LocalBusiness` node inside an `ItemList`, with its own name, locality and Facebook page, and the
visible copy names that company too. This is exactly the treatment the finding asked for. No change
needed; noted here so a future audit does not re-raise it.

**3.10 `starRating: 3` is self-asserted.** The page says *"Kategorisani apartmani"* — officially
categorised — which implies a real Montenegrin tourism categorisation. If so, add
`"ratingExplanation"` naming the authority. An unattributed star rating is weaker than an
attributed one, and this one appears to be genuinely earned.

**3.11 Answer-first structure is already good.** Sampled `vesti/plaze-herceg-novi.html`: every H2
is followed within ~40 words by a concrete, self-contained factual statement (surface type, size,
distance, what it is known for). That is the correct shape for extraction and it is working. Ten of
the twenty-seven pages carry `<table>` elements, which extract well. **Do not restructure this
content** — it is not the problem. Add a comparison table to the price section when §3.1 lands; that
is the one place a table would earn its keep.

**3.12 31 images carry empty `alt=""` out of 184.** All 184 have an `alt` attribute, which is
already better than most sites. Empty alt is correct for purely decorative images; spot-check that
none of the 31 are content images.

---

## 4. What is already right — do not touch it

Genuinely strong, and worth naming so it does not get "optimised" away in a later pass:

- **Static HTML, no client-side rendering.** Two `<script>` tags on the homepage; all content
  present in the initial response. This is the single most important technical property for AI
  crawlers, most of which do not execute JavaScript. You have it for free and many competitors do not.
- **`robots.txt` allows everything.** `User-agent: * / Disallow:` permits GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended and the rest. For a business that wants AI citations this is the
  correct posture. **Reject any advice to block AI crawlers.** You cannot be cited by a crawler you
  blocked.
- **NAP consistency.** One address, one primary phone in one E.164 form, one email, one geo
  coordinate pair — identical across all thirteen business nodes.
- **`hasMap` with the Google Maps CID.** A direct, unambiguous pointer from your markup to your
  Google Business Profile. Many sites get this wrong; you have the strongest available form of it.
- **`FAQPage` markup on 24 pages.** Worth being precise: Google retired FAQ rich results for
  most sites in 2023, so this earns you no SERP feature. It remains worth keeping — well-formed
  Q&A pairs are the exact shape extractive systems consume, and it costs nothing. Keep it; just
  don't expect a rich result from it.
- **Breadcrumbs on every page**, canonical on every page, one H1 per page, image sitemap,
  `ImageObject` with dimensions and real captions.
- **The guide content itself.** Specific, local, first-hand, photographed, with real prices for
  *other* businesses (restaurants, beach services). This is the raw material for AI citation. §3.2
  is about connecting it, not replacing it.

---

## 5. Anti-recommendations — advice to reject

### 5.1 Do not re-add `aggregateRating` / `Review` to the business node

Any GEO checklist will tell you to add `aggregateRating` so AI systems can see your 4.9. **Do not.**
`docs/gbp-website-audit.md` §C2/§C3 removed exactly this markup, from ten pages, for correct
reasons that have not changed:

- Self-serving reviews — reviews about the business, hosted on the business's own domain — are
  ineligible for review rich results for `LocalBusiness` and its subtypes, and `LodgingBusiness` is
  one.
- Re-publishing Google's own 71-review average as your site's first-party `aggregateRating` is
  specifically the aggregation pattern the policy targets, and is the category of markup that draws
  a spammy-structured-markup manual action.

Google already holds the authoritative 4.9/71 on your GBP and serves it in the local pack and to its
own AI systems. Asserting a competing copy gains nothing and risks a manual action that would cost
you far more than the citation is worth. **The correct version of this advice is §3.5** — link
`sameAs` to the platforms that hold the reviews, and keep the visible, source-attributed block.

### 5.2 Do not invest further in `llms.txt`

Your `llms.txt` is well written — better than most. It is also, on current evidence, doing nothing.
Google's documentation states the file has no effect on Search or AI Overviews; an Ahrefs analysis
of 137,000 sites found 97% of `llms.txt` files received no bot traffic at all; OpenAI, Anthropic and
Perplexity all document `robots.txt`, not `llms.txt`, as the control surface. John Mueller has
compared it to the keywords meta tag.

Keep the file — it costs nothing, it is accurate, and if the ecosystem ever adopts the convention
you are ready. But **do not spend another hour on it**, and treat any consultant who leads with
`llms.txt` as a signal about that consultant. The hour belongs in §3.1 or §3.2.

### 5.3 Do not abandon the Google Business Profile for GEO

The same study that reports 68% AI Overview coverage also reports that for *simple* local intent —
`apartmani Igalo`, `smještaj Igalo` — AI Overviews appear on 15% of queries while local packs appear
on over 90%. That is your highest-commercial-intent query class. GEO is additive to local SEO here,
not a replacement for it. Review volume, review recency, photos, Q&A and the "From the business"
description on the GBP remain the highest-leverage work available to you, and none of it is in this
repository.

### 5.4 Do not write more guides yet

The instinct after reading the article is "publish more content for informational queries". You
already have thirteen guides in `vesti/` plus four standalone guide pages, and twelve of the
`vesti/` guides are entity-orphaned. Fix §3.2 first — connecting
15,700 existing words to your entity is worth more than adding 2,000 disconnected ones.

---

## 6. Prioritised plan

| # | Action | Impact | Effort | Where |
|:--:|---|:--:|:--:|---|
| 1 | Publish honest seasonal price **ranges** + variables (SR + EN), update meta/OG descriptions | ★★★★★ | Business decision + 2h | §3.1 |
| 2 | Point `author`/`publisher` at `#business` on 13 orphaned pages; add the business node to each | ★★★★★ | 2h | §3.2 |
| 3 | Add `priceRange`, `currenciesAccepted`, `paymentAccepted`, and `offers` on both `Accommodation` nodes + the €500 `Apartment` node | ★★★★☆ | 1h | §3.1 |
| 4 | Add `checkinTime`, `checkoutTime`, `petsAllowed`, lift=false, shared laundry to the business node | ★★★★☆ | 1h | §3.3 |
| 5 | Add Google Maps + Booking + Airbnb URLs to `sameAs`; link the visible rating figures | ★★★★☆ | 30m | §3.5 |
| 6 | Move `WebSite` to the homepage, add `logo`, add `founder`, add `AboutPage` to `about.html` | ★★★☆☆ | 1h | §3.4 |
| 7 | Add `dateModified` to the 7 undated pages + a visible "prices updated" line | ★★★☆☆ | 45m | §3.6 |
| 8 | English `cesta-pitanja.html` and `blatna-plaza.html` | ★★★☆☆ | 3h | §3.7 |
| 9 | EN homepage parity: 9 FAQs, `amenityFeature` on `Accommodation` nodes | ★★☆☆☆ | 1h | §3.8 |
| 10 | Russian homepage + FAQ (Institute audience) | ★★★☆☆ | 1 day | §3.7 |
| 11 | Attribute the second phone; add `ratingExplanation` to `starRating` | ★☆☆☆☆ | 20m | §3.9, §3.10 |

**Outside this repository, and higher-leverage than items 6–11:** keep the GBP review flow running
(volume *and* recency both count), fill the "From the business" description, set the amenity
attributes to corroborate the site's `amenityFeature` list, and upload the walkthrough video —
all still open from `docs/gbp-website-audit.md`.

---

## 7. How to know if it worked

Ranking positions will not tell you. Track these instead:

- **Server-log citations.** Grep access logs for `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`,
  `PerplexityBot`, `ClaudeBot`, `Google-Extended`. Rising crawl frequency on `vesti/` after item 2
  is the earliest available signal.
- **Referral traffic** from `chatgpt.com`, `perplexity.ai`, `gemini.google.com` in analytics —
  small absolute numbers, but the trend is the metric.
- **Manual prompt panel.** Run the same eight prompts monthly across ChatGPT, Gemini, Perplexity and
  Google AI Mode, in Serbian, English and Russian, and record whether you are named:
  1. *Koliko koštaju apartmani u Igalu u avgustu?*
  2. *Where to stay near the Igalo Institute in Montenegro?*
  3. *Cheap apartments near Blatna plaža*
  4. *Monthly apartment rental Herceg Novi cost*
  5. *Apartments in Igalo that allow pets*
  6. *Best beaches in Herceg Novi* (does it cite your guide — and does it name you?)
  7. *Сколько стоит жилье в Игало рядом с институтом?*
  8. *Family apartments Igalo with free parking near the beach*
- **Google Search Console**, filtered to the `vesti/` directory, for impression changes after item 2.

Baseline all eight prompts **before** starting item 1, or you will not be able to prove anything.

---

## 8. Implementation status — 2026-08-10

Items 2–11 are implemented on branch `claude/local-seo-ai-overviews-laulpb`. Item 1 is a business
decision and was deliberately left alone.

| # | Item | Status |
|:--:|---|---|
| 1 | Publish seasonal price ranges | **Not done — your call.** Everything in §3.1 still stands. Nothing else on this list substitutes for it. |
| 2 | Entity linkage on the orphaned pages | **Done.** All 19 article-like nodes point `author`/`publisher` at `#business`; all 27 pages define the entity (was 13). |
| 3 | Offers and payment fields | **Partly done.** `paymentAccepted`, `currenciesAccepted` and the €500 monthly `Offer` are in. `priceRange` and the nightly `Offer`s are **blocked on item 1** — adding them without published prices would mean inventing numbers. |
| 4 | Check-in/out, pets, lift, laundry | **Done** on all 27 business nodes. Supersedes the old G5 "no fixed times exist" decision. |
| 5 | `sameAs` and linked rating figures | **Mostly done.** `sameAs` now carries Facebook, Instagram, YouTube, the Google Maps profile and the Airbnb listing. The visible Google and Facebook figures are links. **Outstanding: the Booking.com listing URL** — the owner could not locate it and will supply it later. It is a one-line addition to `sameAs` on all 31 business nodes when it arrives. |
| 6 | Site spine: `WebSite`, `logo`, `AboutPage`, `founder` | **Mostly done.** `WebSite` moved to the homepages and stopped describing the site as one product page; `logo` and the Serbian `AboutPage` added. **`founder` skipped deliberately:** no host is named anywhere on the site, and the only name available is from a guest review. Asserting it as structured data would be inventing a fact. Tell me the name and it goes in. |
| 7 | Dates on the commercial pages | **Done.** Dates taken from each file's last real content commit, not stamped as today. Visible "updated" line added to the FAQ. |
| 8 | English FAQ and Blatna Plaža | **Done** — `en/faq.html`, `en/blatna-plaza.html`, wired into hreflang, sitemap and llms.txt. |
| 9 | English homepage parity | **Done** — 10 FAQ entries and `amenityFeature` on both `Accommodation` nodes. |
| 10 | Russian homepage and FAQ | **Done** — `ru/index.html`, `ru/faq.html`, three-way hreflang. |
| 11 | Second phone; `ratingExplanation` | **Phone: withdrawn**, already correct (see §3.9). **`ratingExplanation` skipped:** it needs the name of the body that issued the three-star categorisation, which is not published anywhere. Give me the authority and it goes in. |

**Found during verification, not fixed (pre-existing, outside the approved scope):**
`monthly-rental-igalo.html` scrolls horizontally at 390px — its `.booking-compare` table is wider
than the viewport. It behaves identically before and after this work, so it is not a regression, but
it is the exact pattern §3.11 warns about: a wide table needs `overflow-x: auto` on its own
container. One line of CSS whenever you want it. That page also loads a different font pair
(Cormorant Garamond + DM Sans) from the rest of the site.

**Still waiting on a fact from the owner:** the Booking.com listing URL, the host's name for
`founder`, and the authority behind the three-star rating.

### A note on the visible rating figures

The Google and Facebook figures on the homepage are links. The **Booking.com and Airbnb figures are
deliberately left as plain text**, even though the Airbnb URL is now known. The reason is
commercial, not technical: linking them would put a click-through to the channels that charge you
15–20% commission directly beside the section arguing guests should book direct. The `sameAs` entry
does the entity-corroboration job on its own — it is invisible to visitors and sends nobody
anywhere. Reverse this only if you decide OTA traffic is worth more than the direct booking.

---

## 9. Bottom line

The code is not the problem. It is clean, static, consistent, honestly written and already carries
more correct structured data than most properties of this size. Two things are holding it back, and
neither is technical debt:

**You decline to answer the highest-value question**, and **you give away authorship of your best
content.** Fix those two and the rest of this list is maintenance.
