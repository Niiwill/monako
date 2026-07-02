# SEO Change Log

Running record of changes made by the weekly SEO routine (`seo/ROUTINE.md`).
Newest entries at the top. Read this before making new changes so past
decisions aren't repeated or reversed without new data.

---

## 2026-07-02 (manual run, pre-automation)

Based on manual GSC XLSX export (last 28 days, ending 2026-06-30).

- **index.html**: rewrote title/meta for CTR (price + rating cues), added
  "Koliko je Igalo udaljeno od Herceg Novog?" FAQ (visible + schema).
- **vesti/plaze-herceg-novi.html**: added 9th beach entry (Plaža Instituta
  Dr Simo Milošević), added "Stara Banja" alias to Blatna plaža entry,
  added 3 FAQs (sandy beaches, beaches for kids, Igalo–HN distance),
  added internal links to attractions/restaurants guides.
- **vesti/restorani-herceg-novi.html**: added Restoran Promenada Igalo
  (was ranking with impressions and zero coverage on the page), added
  "Igalo" to title, added "Gdje jesti u Igalu?" FAQ, updated to Top 9.
- **blatna-plaza.html**: added "Koje bolesti liječi blato u Igalu?" FAQ,
  fixed stray Cyrillic characters in JSON-LD text.
- **vesti/atrakcije-herceg-novi.html**: added "znamenitosti" entity to intro.
- **robots.txt**: fixed sitemap URL (was pointing at `www.` subdomain,
  canonical domain is non-www).
- **sitemap.xml**: bumped `lastmod` for all changed pages.
- Site-wide: updated stale "Top 8" references to "Top 9" across 6 pages
  after the beach/restaurant guides grew by one entry each.

Titles/metas touched above should not be re-edited before **2026-07-23**
(21-day guardrail) unless data clearly shows continued underperformance.
