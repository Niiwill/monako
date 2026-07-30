# GBP Landing URL — dedicated performance analysis

**URL:** `https://apartmani-igalo.com/?utm_source=gbp&utm_medium=organic`
**Requested window:** last 7 days (2026-07-22 → 2026-07-28)
**Status:** now a **standing section in every daily report** at owner's request.

---

## ⚠️ Correction to the 2026-07-31 report

Yesterday I flagged a **homepage position regression** (`/` moving 5.62 → 7.73)
and suspected the Jul 25–26 schema/NAP changes, recommending a schema diff by
Aug 5. **That diagnosis was wrong.** This analysis identifies the real cause,
and it is not a regression at all.

Test — `apartmani igalo`, split by URL:

| Window | URL | Impressions | Position |
|---|---|---|---|
| Jul 18–24 (before) | `/` | 521 | **4.12** |
| Jul 25–28 (after) | `/` | 190 | 7.69 |
| Jul 25–28 (after) | `/?utm_source=gbp…` | 186 | **1.61** |

The high-position impressions did not disappear — they **moved to the GBP
URL**. What remains on `/` is the lower-position tail, which drags its average
down. The homepage did not lose ranking; GSC started reporting the same
visibility under two URLs.

Total visibility actually **increased**:

| | Homepage | GBP URL | Combined |
|---|---|---|---|
| Jul 18–24 | 656 impr/day | 0 | **656/day** |
| Jul 25–28 | 444 impr/day | 288 impr/day | **732/day** |

**+12% combined impressions.** No schema diff needed; the Aug 5 decision point
is cancelled. Apologies for the false alarm — the correction matters because
it would have sent us chasing a non-existent problem in the schema.

---

## 1. Seven-day metrics

Important caveat: the URL had **zero impressions before Jul 25**, so the
"7-day" window contains only **4 days of data**. Prior 7 days (Jul 15–21):
0 impressions, 0 clicks.

| Date | Impr | Clicks | CTR | Position |
|---|---|---|---|---|
| Jul 22 Wed | 0 | 0 | — | — |
| Jul 23 Thu | 0 | 0 | — | — |
| Jul 24 Fri | 0 | 0 | — | — |
| Jul 25 Sat | 155 | 0 | 0.00% | 3.10 |
| Jul 26 Sun | 371 | 2 | 0.54% | 3.57 |
| Jul 27 Mon | 337 | 2 | 0.59% | 2.80 |
| Jul 28 Tue | 288 | 2 | 0.69% | **2.30** |
| **Total** | **1,151** | **6** | **0.52%** | **~2.8** |

**Position is improving steadily: 3.10 → 3.57 → 2.80 → 2.30.**

Device split (of device-attributed impressions): mobile 771 (89%), desktop 86,
tablet 5. Mobile position 2.43 vs desktop 4.34.

## 2. What this URL actually ranks for — and why it matters

| Query | Impr | Position |
|---|---|---|
| apartmani igalo | 186 | **1.61** |
| apartmani igalo blizu plaze | 17 | **1.29** |
| apartmani igalo izdavanje | 12 | 2.25 |
| privatni smještaj igalo | 8 | **1.50** |
| apartman monako igalo | 7 | 1.00 |
| apartman igalo | 6 | 2.17 |
| apartmani igalo 2026 | 6 | 9.17 |
| apartmani igalo cijene | 5 | **1.20** |
| apartmani coka igalo | 4 | 1.00 |

**Only 3.6% of impressions are brand queries.** This URL is winning
**non-brand, high-intent commercial terms at positions 1–2.5** — the exact
queries where the organic homepage listing sits at 4–7. That is the single
most valuable search real estate the business holds.

Comparison over the same 7 days:

| URL | Impressions | Clicks | CTR | Position |
|---|---|---|---|---|
| `/` (clean) | 3,540 | 154 | 4.35% | 6.71 |
| `/?utm_source=gbp…` | 1,151 | 6 | 0.52% | **2.80** |

## 3. Why the 0.52% CTR is not the alarm it looks like

Three reasons, all structural:

1. **Most GBP clicks are not counted here.** Clicks on the profile's website
   button are reported in **GBP's own "Website clicks"** metric (94 in the last
   30-day export), not in GSC. GSC sees only a fraction.
2. **Local-pack impressions convert into non-website actions.** A searcher who
   sees the profile and taps **Call** (156 in 30 days) or **Directions** (109)
   generates a GSC impression and zero GSC clicks — while producing the most
   valuable outcome the business has.
3. **The URL is not indexed** — URL Inspection returns *"URL is unknown to
   Google"*. These are profile/local-pack impressions, not a competing page.
   Canonical handling is correct; there is no duplicate-content issue.

**So: do not optimise this URL's CTR as if it were an organic listing.** Its
true conversion metric lives in the GBP dashboard, not here.

## 4. What drove the appearance on Jul 25

The URL appeared the day the NAP/entity audit (PRs #62–#65) landed. That work
— consistent name/address/phone, `alternateName`, entity consolidation —
is the most plausible cause of the profile gaining this much Search real
estate. **The NAP alignment is paying off, and it is measurable.**

## 5. Opportunities for improvement

### Keep the UTM parameter — it is now an asset

Earlier I treated the UTM as harmless-but-pointless. With this data, it is
actively useful: it is the **only way to see local-pack performance separately**
from organic. Without it, all of this would be invisible inside the homepage's
numbers. The site has no analytics tag consuming it, so it does no other work —
but the GSC reporting separation alone justifies keeping it.

### The real levers are in the GBP dashboard, not the repo

Ranked by expected value:

1. **Enable Messaging** — still **0**. A searcher at position 1.6 who will not
   place an international call has no low-friction path today.
2. **Add a booking/reservation link** — Bookings still **0**. Point it at the
   homepage `#cjenovnik` pricing section so the click lands on price, not the
   top of the page.
3. **Photos and Posts weekly.** 39% of profile views come from Maps, where
   photo freshness is a ranking input the website cannot influence.
4. **Review velocity.** With own-site rating markup permanently ineligible for
   stars, GBP reviews are the only route to visible ratings.

### On-site lever

The GBP visitor lands at the top of the homepage. Since the winning queries
here are `apartmani igalo cijene`, `privatni smestaj igalo i cene` and
`apartmani igalo izdavanje` — all price/availability intent — pointing the
profile's website link (or the booking link) at **`/#cjenovnik`** would put
those visitors directly on prices. Low effort, no repo change needed.

## 6. Standing tracking — from now on

Every daily report will include a **"GBP landing URL"** section reporting:

- impressions, clicks, CTR, average position (7-day and day-over-day)
- top non-brand queries and their positions
- **combined** homepage + GBP-URL impressions, so the reporting split never
  again reads as a ranking loss
- GBP dashboard metrics whenever a fresh export is supplied

**Baseline set today:** 1,151 impressions, 6 clicks, 0.52% CTR, position 2.80
(4 days). Combined homepage + GBP visibility: 732 impressions/day.
