# GBP export — 2026-07-23 → 2026-08-19

**Izvor:** vlasnički export „Business Profile Overview" (28 redova).
**Prethodni export za poređenje:** 2026-07-03 → 2026-07-30
(`seo-reports/2026-08-01-gbp-export-analysis.md`).
**Unakrsna provjera:** GSC, `?utm_source=gbp&utm_medium=organic`.

Ovo je prvi export koji pokriva **puni period poslije 25. jula**, kada se GBP
URL pojavio u pretrazi. Prošli je imao samo tri dana poslije toga i zaključak
je tada bio „ne može se pročitati". Sada može.

---

## 1. Koji dani su upotrebljivi — i zašto ne 25

Zadnja tri reda (17–19.8.) su nule na svim kanalima. To je poznato kašnjenje
izvještavanja i tako sam ga tretirao i prošli put.

**Ali ovaj put rep je duži od tri dana, i to se može dokazati.**

| Datum | GBP export: klikovi na sajt | GSC: klikovi na GBP URL |
|---|---|---|
| 13.8. | 3 | 2 |
| 14.8. | 1 | 4 |
| **15.8.** | **0** | **3** |
| **16.8.** | **0** | **1** |

GSC bilježi klikove 15. i 16. avgusta na tačno onom URL-u koji GBP broji kao
„website clicks". Export za te dane pokazuje nulu. **Rep nije stvarnost, nego
nedovršena obrada.**

Isto se vidi i po strukturi kanala u zadnja četiri dana:

| Sedmica | Interakcije | Pozivi | Sajt | Rute | Poruke |
|---|---|---|---|---|---|
| 23–29.7. | 98 | 45 | 24 | 29 | 9 |
| 30.7–5.8. | 116 | 57 | 22 | 37 | 16 |
| 6–12.8. | 132 | **79** | 22 | 31 | 17 |
| 13–19.8. | 38 | **4** | 4 | **30** | **0** |

Pozivi padaju sa 79 na 4, poruke sa 17 na 0, klikovi sa 22 na 4 — a **rute
ostaju 30, najviše ili drugo najviše u cijelom prozoru.** Da je pad stvaran,
pale bi i rute. Rute se očigledno obračunavaju brže od ostalih kanala.

**Zaključak: računam na prozoru 23.7 – 12.8. (21 dan).** Ispod dajem i
brojke na svih 25 dana, jer je prošli izvještaj tako računao — svi zaključci
su isti u oba tretmana.

---

## 2. Glavna tabela

**Poravnati prozor (23.7 – 12.8, 21 dan) protiv prethodnog exporta
(3–24.7, 22 dana — posljednji potpuno obračunat blok tamo):**

| Kanal | Ranije (/dan) | **Sada (/dan)** | Ukupno | Δ |
|---|---|---|---|---|
| **Pozivi** | 6,32 | **8,62** | 181 | **+36%** |
| Rute | 3,68 | **4,62** | 97 | **+26%** |
| **Poruke** | 1,50 | **2,00** | 42 | **+33%** |
| Klikovi na sajt | 3,86 | **3,24** | 68 | **−16%** |
| Interakcije | 13,86 | **16,48** | 346 | **+19%** |
| **Rezervacije** | 0,00 | **0,00** | **0** | — |
| Meni | 0,00 | 0,00 | 0 | — |

**Isto na svih 25 dana** (metod prošlog izvještaja): interakcije 384
(15,36/dan, +11%), pozivi 185 (7,40/dan, **+19%**), rute 127 (5,08/dan, +25%),
poruke 42 (1,68/dan, +17%), klikovi 72 (2,88/dan, −20%).

Smjer je isti u oba tretmana na svakom kanalu. Zaključci ne zavise od toga
gdje sam povukao granicu.

### Ograda: 8. avgust

8.8. ima **27 poziva** naspram medijane od 8. To je subota, u GSC-u je taj dan
potpuno običan (259 impresija, pozicija 3,01), dakle objašnjenje nije u
pretrazi. Bez tog dana pozivi su 7,70/dan — i dalje **+22%**.

**Ovo je pitanje za vas: da li se 8. avgusta nešto desilo** — grupna
rezervacija, preporuka, nešto van interneta? Ako ne, treba ga tretirati kao
izuzetak.

---

## 3. Telefon je kasa — sada i brojčano

| | Pozivi | Klikovi na sajt | Odnos |
|---|---|---|---|
| 3–24.7. | 6,32/dan | 3,86/dan | **1,64×** |
| **23.7–12.8.** | **8,62/dan** | **3,24/dan** | **2,66×** |

Na svakih 100 ljudi koji kliknu na sajt, **266 pozove**. Prije mjesec dana ih
je bilo 164.

**Klikovi na sajt su 19,7% svih interakcija sa profilom.** To znači da sve što
mjerim u GSC-u o GBP URL-u pokriva **manje od petine** onoga što taj profil
zapravo radi. Kada u dnevnom izvještaju napišem „GBP URL: 22 klika ove
sedmice", stvarni obim te iste površine je oko 115 kontakata.

Za proporciju, na poravnatom prozoru: GSC bilježi **5.813 impresija** na GBP
URL-u, prosječna pozicija **2,77**. Od toga 68 klikova na sajt (CTR 1,07%) —
ali 346 interakcija sa profilom. Interakcije dolaze i sa Mapa i sa direktnih
pregleda profila, pa ovo nije čista stopa konverzije; ali red veličine je
jasan: **ljudi mnogo češće djeluju unutar profila nego što odu na sajt.**

To je argument protiv svakog budućeg rada čiji je cilj „povećati CTR ka
sajtu" sa ove površine. Nije to gdje je novac.

---

## 4. Unakrsna provjera: GSC i GBP mjere istu stvar

| Prozor | GBP „website clicks" | GSC klikovi na `utm_source=gbp` | Razlika |
|---|---|---|---|
| 23.7 – 12.8. (obračunato) | 68 | 62 | +9,7% |
| 23.7 – 16.8. (sa repom) | 72 | 72 | 0,0% |

Dnevno se razilaze zbog vremenske zone i atribucije. Poklapanje na 72:72 je
slučajno — GBP blago pretiče kroz cijeli prozor, a nedovršeni rep to poništi.
**Ali dvije nezavisne mjere se slažu unutar 10%,** što potvrđuje ono što sam
dosad izvodio posredno: red `?utm_source=gbp&utm_medium=organic` u GSC-u
**jeste** površina klikova sa Business Profila, a ne neki artefakt.

Uz to, tri dana preklapanja sa prošlim exportom (25–27.7.) poklapaju se
**tačno na svih pet kanala** (pozivi 16, sajt 5, rute 21, poruke 3,
interakcije 42). Podaci su konzistentni između izvoza.

---

## 5. ⭐ Uklanjanje call bara sa `/vesti` — hipoteza o šteti odbačena

Ovo je otvorena stavka od 26. jula. Call bar je uklonjen sa članaka, a rizik
je bio da će pozivi pasti. Do sada se nije moglo izmjeriti bez exporta.

**Pozivi su porasli 22–36%, ni u jednom tretminu podataka nisu pali.**

Šta ovo jeste: **odbacivanje hipoteze o šteti.** Uklanjanje nije koštalo
poziva.

Šta ovo **nije**: dokaz da je uklanjanje pomoglo. Kraj jula i sredina avgusta
su vrhunac sezone, a prethodni prozor je hvatao slabiji period — isti sezonski
konfaund koji sam prošli put naveo u suprotnom smjeru. Rast poziva pripisujem
sezoni dok se ne pokaže suprotno.

Stavka se zatvara sa ishodom: **nema mjerljive štete.**

---

## 6. Rezervacije: nula, osma sedmica zaredom

Jedini kanal koji je i dalje prazan. Dolazna namjera je eksplicitno o cijeni i
raspoloživosti — GBP URL drži poziciju 1,20 na `apartmani igalo cijene` i 2,50
na `privatni smestaj igalo i cene`.

Uz **2,00 poruke dnevno** (kanal koji prije šest sedmica nije postojao i sada
je treći po veličini), ljudi već traže način da pitaju za termin. Rezervaciono
dugme uperano na `/#cjenovnik` bi ih dočekalo direktno.

Napomena o cijenama: sekcija `#cjenovnik` postoji na naslovnoj i ne prikazuje
sezonske cijene — vaša odluka. Rezervaciono dugme ne traži da se to mijenja;
vodi na kontakt i uslove, ne na cjenovnik po noćenju.

---

## 7. Šta se iz ovih podataka **ne** može zaključiti

- **Dan u sedmici.** Poravnati prozor daje samo 3 opažanja po danu (srijeda
  12,0 poziva/dan, petak 4,3). Sa n=3 i jednim danom od 27 poziva u uzorku, to
  nije mjerenje. Ne planirajte ništa po tome.
- **Uzročnost bilo kog SEO rada.** Prozori se razlikuju i po sezoni i po
  sadržaju. Jedini čist rezultat i dalje je poruke — kanal koji je otišao sa
  nepostojećeg na 2/dan.
- **Poređenje sa prošlom godinom.** GBP export ne ide unazad; nemamo lanjske
  brojke za profil. U GSC-u je sezona −42,5% YoY, pa je rast poziva u opadajućoj
  sezoni utoliko zanimljiviji — ali to je nagovještaj, ne nalaz.

---

## 8. Nove osnove za sljedeći export

| Metrika | Osnova (/dan, 23.7 – 12.8.) |
|---|---|
| Pozivi | **8,62** (7,70 bez 8.8.) |
| Rute | 4,62 |
| Poruke | 2,00 |
| Klikovi na sajt | 3,24 |
| Interakcije | 16,48 |
| Rezervacije | 0,00 |

**Sljedeći export tražiti tek početkom oktobra, sa početnim datumom 13.8.**,
tako da pokrije i dane koje sam ovdje morao odbaciti. I dalje ostaviti zadnjih
5–7 dana neupotrebljenih.

---

## 9. Šta slijedi

1. **Rezervaciono dugme na profilu → `/#cjenovnik`.** Jedini prazan kanal,
   osma sedmica. Najjeftinija izmjena u cijelom spisku.
2. **Odgovor na pitanje o 8. avgustu.** Ako je bio jednokratan događaj,
   osnova za pozive je 7,70, ne 8,62.
3. **Ništa na sajtu.** Ovi podaci ne traže nijednu izmjenu koda. Odnos
   2,66 : 1 u korist telefona potvrđuje postojeće pravilo — ne dodavati korake
   prije `tel:` dodira.
