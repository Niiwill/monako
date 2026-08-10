# Investigation: the `herceg novi` impression drop

**Question:** why did `herceg novi` fall 605 → 114 impressions and 12.9 → 15.0
in the week of Aug 1?

**Answer:** we caused it. PR #76 — the hub expansion built to win that exact
query — is the cause. It failed on its target and took the page's profitable
attraction cluster down with it. The bigger loss is the one the original flag
did not mention: **the page lost 66% of its clicks.**

---

## 1. The timing is not ambiguous

URL Inspection on `vesti/atrakcije-herceg-novi.html`:

```
verdict         PASS
coverageState   Submitted and indexed
lastCrawlTime   2026-07-30T23:45:29Z
googleCanonical = userCanonical
```

That crawl contains **PR #76 and nothing else.** The AdSense commit, the
call-bar removal and the favicon rebuild all landed on Jul 31 — *after* the
crawl — and the page has not been recrawled since. Google has never seen
them. They cannot be involved, and neither can anything else we shipped that
week.

Daily impressions for `herceg novi`:

| Jul 29 | Jul 30 | **Jul 31** | Aug 1 | Aug 2 | Aug 3 | Aug 4 | Aug 5 | Aug 6 |
|---|---|---|---|---|---|---|---|---|
| 161 | 146 | **57** | 23 | 23 | 20 | 16 | 13 | 9 |

The step lands on the first full day after the recrawl. This is a step
function, not a demand curve — demand does not fall 60% overnight and then
decay for a week.

---

## 2. It is not seasonality, not the site, not AdSense

Every control is clean:

| Control | Jul 24–30 | Aug 1–7 | Verdict |
|---|---|---|---|
| Site-wide clicks/day | ~295 | ~277 | no cliff (Aug 2 = 337, highest in range) |
| `igalo` | 3,753 impr @ 6.8 | 3,917 @ 6.6 | flat |
| `herceg novi plaze` | 852 @ 1.5 | 762 @ 1.5 | flat |
| All queries containing "herceg novi" | 5,805 @ 5.56 | 5,119 @ **4.58** | position *improved* |
| `/vesti` as a group (all got AdSense) | CTR 6.22% | CTR 5.98% | drift, not a cliff |
| non-`/vesti` (no AdSense) | CTR 3.61% | CTR 3.63% | flat |

`/vesti` as a whole lost 6% of clicks. This one page lost 66%. It is the
outlier, not the group — and it is the only page in the group whose content
and metadata changed.

---

## 3. What actually broke: the snippet

Page totals, 7d pre-crawl vs 7d post-crawl:

| | Jul 24–30 | Aug 1–7 | Δ |
|---|---|---|---|
| Clicks | 181 | **61** | **−66%** |
| Impressions | 2,691 | 1,786 | −34% |
| CTR | 6.73% | **3.42%** | **−49%** |
| Position | 7.38 | 7.53 | +0.16 (flat) |

**Position is flat and CTR halved.** That is a snippet effect, not a ranking
effect.

The attraction cluster PR #76 explicitly promised not to risk:

| Query | Clicks | Impressions | Position |
|---|---|---|---|
| herceg novi znamenitosti | 11 → 1 | 28 → 18 | 2.5 → 4.6 |
| herceg novi sta videti | 6 → 0 | 24 → 17 | 2.1 → 3.5 |
| sta obici u herceg novom | 8 → 1 | 33 → 25 | 2.4 → 2.8 |
| šta videti u herceg novom | 6 → 1 | 17 → 5 | 2.7 → 3.4 |
| sta videti u herceg novom | 5 → 0 | 24 → 14 | 2.9 → 3.3 |
| sta posjetiti u herceg novom | 5 → 0 | 14 → 0 | 1.9 → — |
| herceg novi slike grada | 4 → 1 | 19 → 10 | **1.0 → 1.0** |
| herceg novi izleti | 2 → 0 | 26 → 6 | 6.3 → 10.5 |
| stari grad herceg novi | 3 → 2 | 196 → 153 | 6.4 → 5.9 |
| **TOTAL** | **50 → 6** | 381 → 248 | **CTR 13.1% → 2.4%** |

The decisive row is `herceg novi slike grada`: **position 1.0 before, 1.0
after, clicks 4 → 1.** Rank identical. Nothing about that query changed
except what the snippet said.

### The change

```
BEFORE  Šta videti i obići u Herceg Novom? Od Starog grada i Plave špilje
        do Gospe od Škrpjela i poluostrva Luštica — 17 nezaobilaznih
        atrakcija sa savjetima lokalaca za 2026.

AFTER   Šta videti u Herceg Novom? 17 atrakcija, kako doći, vrijeme i
        najbolje vrijeme za posjetu — vodič lokalca za 2026.
```

Someone searching *"šta videti u Herceg Novom"* wants to know **what there
is to see.** The old snippet answered that inside the snippet itself — Stari
grad, Plava špilja, Gospa od Škrpjela, Luštica. The new one names nothing and
offers logistics instead. It reads like a page about visiting rather than a
page about what to see.

---

## 4. And the target was never won

| `herceg novi` | Jul 24–30 | Aug 1–7 |
|---|---|---|
| Impressions | 602 | 114 |
| Position | 13.29 | **15.04** |
| Clicks | 6 | 2 |

The head term went **backwards**. PR #76 traded a cluster earning 13.1% CTR
for a head term it did not win. That is not a trade, it is a loss on both
sides.

**The rise was also misattributed.** The July gain predates PR #76 by four
weeks — the page moved from position 18.45 to 8.39 in the week of **Jul 4**,
and `herceg novi` went 51.7 → 20.9 → 13.8 → 12.5 across July, all before the
hub expansion merged on Jul 30. Yesterday's report credited PR #76 with
moving the query 15.1 → 13.2. It did not. It gets no credit for the rise and
full responsibility for the fall.

---

## 5. Confidence

| Claim | Confidence | Basis |
|---|---|---|
| PR #76 caused it | **High** | Sole change in the Jul 30 crawl; step function on the next day; all controls clean |
| Meta rewrite caused the CTR collapse | **High** | 50 → 6 clicks at flat position; `slike grada` identical at 1.0 |
| Content broadening caused position drift | **Moderate** | Consistent direction across 8 of 9 queries, but 14–33 impressions each is a small sample |
| Mechanism of the head-term impression collapse | **Moderate** | Timing is certain; whether it is a withdrawn evaluation or a relevance re-score is not observable in GSC |

---

## 6. Action

**Done — PR: `claude/fix-atrakcije-meta-regression`.** Meta description
restored verbatim to the pre-#76 text. Restored rather than rewritten: the
old version has a measured 13.1% cluster CTR, and a third variant would just
be another untested change. Title and H1 untouched. `sitemap.xml` lastmod
bumped to prompt a recrawl.

Expected recovery: cluster CTR 2.4% → ~13%, roughly **+40 clicks/week** on
the cluster and **+100/week** on the page, once recrawled (2–5 days).

**Deferred — the three added sections** (`Herceg Novi na prvi pogled`,
`Kako doći`, `Vrijeme`). They did not win the head term and they coincide
with the position drift, so the case for removing them is real but rests on
the moderate-confidence finding. Removing content is harder to undo than
changing a meta tag. Recommend: ship the meta revert alone, then read the
positions after recrawl. If the cluster recovers CTR but stays at 3.5–4.6
instead of returning to 2.1–2.5, the content is implicated and should move
to its own page. One variable at a time.

**Do not re-chase the head term this season.** Today's demand analysis found
pre-trip intent peaked in July and falls until spring. `herceg novi` is the
most pre-trip query on the site. The attraction cluster converts at 13% and
is what this page is for.

---

## 7. What this changes about how we work

The hub expansion was well-reasoned. It identified a real opportunity,
diagnosed the gap correctly, and deliberately protected the title and H1. It
still lost 120 clicks/week — because the meta description was treated as
incidental to the content change rather than as the live, measured asset it
was.

Two rules follow:

1. **A meta description with a known CTR is an experiment already running.**
   Changing it alongside a content change makes the result unreadable and
   risks a working asset. Change one at a time.
2. **Check `lastCrawlTime` before attributing a change.** It converted four
   competing hypotheses into one answer in a single API call, and it
   exonerated AdSense — which was otherwise the obvious suspect and would
   have sent this investigation in the wrong direction.
