# Page-2 Quick-Win Analysis — target: "herceg novi"

**Data:** GSC Search Analytics, dimensions `query` + `page`, 2026-07-01 → 2026-07-28
(2,589 query+page rows; 246 rows in positions 11–20 totalling 3,271 impressions)

## Steps 1–3: page-2 opportunities, sorted by impressions

| # | Query | Impr | Pos | CTR | Clicks | Page |
|---|---|---|---|---|---|---|
| 1 | **herceg novi** | **1,215** | **15.1** | 1.2% | 14 | `/vesti/atrakcije-herceg-novi.html` |
| 2 | blatna plaza igalo | 473 | 11.7 | 2.1% | 10 | `/vesti/plaze-herceg-novi.html` |
| 3 | igalo montenegro | 282 | 13.3 | 0.0% | 0 | `/vesti/10-reasons-why…` (EN) |
| 4 | igalo vrijeme | 251 | 12.0 | 0.0% | 0 | `/vesti/plaze-herceg-novi.html` |
| 5 | igalo herceg novi | 75 | 16.3 | 1.3% | 1 | `/vesti/plaze-herceg-novi.html` |

Note on #2: `blatna plaza igalo` also ranks **4.2 on `/blatna-plaza.html`** with
11.6% CTR — the position-11.7 row is a second, weaker URL competing for the
same query. That is cannibalisation, not an opportunity, and is excluded.

## Step 4: selected target

**Query:** `herceg novi` — 1,215 impressions, position 15.1, 1.2% CTR
**Page:** `vesti/atrakcije-herceg-novi.html`

Chosen because it has 4× the impressions of the next genuine candidate **and**
a strong upward trajectory:

| Fortnight | Impr | Position |
|---|---|---|
| Jun 1–14 | 34 | 54.7 |
| Jun 15–28 | 69 | 51.9 |
| Jun 29 – Jul 12 | 340 | 18.8 |
| **Jul 13–28** | **979** | **13.7** |

Google is actively promoting this page for the head term. Reinforcing it now
works with that momentum rather than against it.

## Step 5: diagnosis — why it stalls at ~15

The page is a **1,780-word attractions listicle** titled "Šta Videti u Herceg
Novom – Top 17". It has 12 `TouristAttraction` nodes, 5 `Restaurant` nodes, a
4-question `FAQPage` and a `BreadcrumbList`.

### It already dominates its own cluster

| Query | Impr | Pos | CTR |
|---|---|---|---|
| sta posjetiti u herceg novom | 26 | 2.8 | **30.8%** |
| šta videti u herceg novom | 69 | 3.7 | **26.1%** |
| sta obici u herceg novom | 102 | 3.5 | **16.7%** |
| herceg novi znamenitosti | 114 | 4.0 | **14.0%** |
| herceg novi izleti | 73 | 6.5 | 13.7% |

**Critical implication: do not re-purpose this page.** Rewriting its title/H1
toward the bare head term would put a ~14–30% CTR cluster at risk to chase a
1.2% one. The correct move is to *broaden* the page while leaving its winning
identity intact.

### Weak topical coverage — the actual gap

For a bare-city-name query, searchers want orientation before attractions.
Coverage audit of the current page:

| Subtopic | Mentions | Verdict |
|---|---|---|
| where it is / geography | 0 | **missing** |
| how to get there (`kako doći`) | 0 | **missing** |
| bus / autobuska stanica | 0 | **missing** |
| parking | 0 | **missing** |
| weather / climate | 0 | **missing** |
| map | 0 | **missing** |
| history | 5 | thin |
| accommodation | 1 | thin |
| beaches | 14 | ok (links out) |
| restaurants | 26 | ok |

At 1,780 words it is also thin for a head term whose SERP is held by
Wikipedia, the municipal tourism portal and OTA city pages — all of which
function as comprehensive destination hubs.

### Entity queries underperform badly — a second, separable problem

| Query | Impr | Pos | CTR | Expected at that position |
|---|---|---|---|---|
| herceg novi stari grad | 508 | 4.8 | **3.0%** | ~8% |
| stari grad herceg novi | 462 | 6.1 | **1.9%** | ~5% |
| herceg novi centar | 174 | 3.6 | **2.3%** | ~9% |
| herceg novi centar grada | 62 | 3.1 | **1.6%** | ~11% |

The pattern is consistent: **question** queries convert at 14–31%, **place-entity**
queries at 1.6–3.0% from equal or better positions. Searchers typing
"stari grad herceg novi" want a page about the Old Town and get item 8 of 17.
~1,200 impressions are affected.

### Competitor gap (inferred, not measured)

Ahrefs and Semrush both require re-authorisation in this session, so the live
SERP for `herceg novi` could not be pulled. The gap analysis above is derived
from GSC behaviour patterns — treat the competitor characterisation as
informed inference, not verified data. Verifying the actual top 10 should be
the first step before the build.

## Step 6: five recommended improvements

**1. Add an orientation block above the attraction list** (~250–350 words)
Answer, in the first screen: where Herceg Novi is (Boka Kotorska, distance to
Tivat and Dubrovnik airports), what it is known for (Grad sunca i stepenica,
mimosa, fortresses), and when to visit. Head-term searchers bounce without
this; it is also the block most likely to win a featured snippet.

**2. Add "Kako doći do Herceg Novog" with practical logistics**
Airports and drive times, the Kamenari–Lepetane ferry vs the Bay road, bus
station, and parking in the centre. Currently zero coverage of bus and
parking. Supporting demand already exists: `herceg novi autobuska stanica`
(pos 1.0), `meljine igalo udaljenost` (15 impr, 6.7% CTR).

**3. Add "Vrijeme i najbolje vrijeme za posjetu"**
A genuine adjacent gap with measurable demand: **`igalo vrijeme` 284
impressions at position 12.0 with 0.0% CTR**, plus `vrijeme u herceg novom`.
The site currently serves these with a beaches article, which answers nothing.
A short climate/season table converts this from wasted impressions to clicks.

**4. Split out a dedicated Stari Grad page** — the single largest sub-gap
Target `herceg novi stari grad` + `stari grad herceg novi` (970 impressions,
1.9–3.0% CTR). A page about the Old Town itself, linked from the roundup's
Stari Grad section, resolves the specificity mismatch and gives the hub a
strong internal link target. Requires real local knowledge — must not be
fabricated.

**5. Add a neighbourhoods section (Igalo, Meljine, Zelenika, Đenovići)**
Each is already generating impressions the site half-serves: `djenovici plaza
slike` (23 impr, pos 6.7), `plaze zelenika` (9, pos 6.2), `meljine plaza mapa`
(7, 14.3% CTR), `djenovici plaza` (13, pos 19.2). A short "where to stay /
what each area is like" section adds the topical breadth a destination hub
needs — and creates a natural, non-spammy link to the apartment pages.

### Internal linking — the cheapest lever, currently under-used

Pages linking to `atrakcije-herceg-novi.html` today: `blog.html` (4),
`praznik-mimoze-program.html` (3), `plaze-herceg-novi.html` (2),
`iznajmljivanje-bicikla…` (1), `10-reasons-why…` (1).

**The homepage does not link to it at all**, nor do the site's two
highest-authority article pages beyond a passing reference. Recommended
additions, with varied descriptive anchors:

| From | Anchor suggestion |
|---|---|
| `index.html` | "šta videti u Herceg Novom" |
| `vesti/10-razloga-da-posetite-igalo.html` | "atrakcije Herceg Novog" |
| `blatna-plaza.html` | "znamenitosti Herceg Novog" |
| `vesti/restorani-herceg-novi.html` | "šta obići u Herceg Novom" |
| `vesti/restorani-igalo.html` | "Herceg Novi i okolina" |

`plaze-herceg-novi.html` carries 40,789 impressions and 10.15% CTR — a
contextual link from it is the highest-value single addition.

## Step 7: re-indexing

**Yes — request indexing after the update, but not immediately.**

Recommended sequence:
1. Ship the content additions in one PR (not drip-fed — Google should see one
   substantially improved page, not five small edits).
2. Update `sitemap.xml` `lastmod` for the page.
3. Then use **URL Inspection → Request indexing** in Search Console for
   `atrakcije-herceg-novi.html`, plus the new Stari Grad page if built.
4. Do **not** request indexing for every internally-linked page; the sitemap
   handles those.

Reason for sequencing: requesting indexing mid-edit wastes the request on a
half-finished page. One request after a complete update is worth more.

## Realistic expectation — stated honestly

**Top 5 for the bare term `herceg novi` is unlikely.** That SERP is a
destination head term contested by Wikipedia, the official municipal tourism
site and OTA city pages, against a domain whose authority score is 10 with
123 referring domains. Promising top 5 would be overselling.

A credible target is **positions 8–12**, which is worth having:

| Scenario | Position | CTR | Clicks/28d |
|---|---|---|---|
| Now | 15.1 | 1.2% | 14 |
| Realistic | 9–10 | ~2.8% | ~34 |
| Good | 8 | ~3.3% | ~40 |

Plus the larger, more attainable prize alongside it: fixing the entity-query
CTR gap (Stari Grad + centar, ~1,200 impressions at 1.6–3.0%) and capturing
`igalo vrijeme` (284 impressions currently at 0.0%). **Those two are worth
more combined than the head term itself**, and are far less dependent on
domain authority.

## Suggested build order

1. Verify the live `herceg novi` SERP (needs Ahrefs/Semrush re-auth).
2. Expand `atrakcije-herceg-novi.html`: orientation block, how-to-get-there,
   weather, neighbourhoods. Keep title/H1 unchanged.
3. Add the internal links in the table above.
4. Build the dedicated Stari Grad page (separate PR, needs local knowledge).
5. Update sitemap, request indexing.
