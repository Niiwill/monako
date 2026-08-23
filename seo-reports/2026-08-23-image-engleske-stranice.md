# Istraga: engleske stranice u image kanalu

**Povod:** dnevni izvještaj 23.8. izdvojio je engleske stranice kao uzrok pada
image pozicije. Ovo je provjera šta se tačno dešava.
**Podaci:** GSC image + web, 24.7 – 20.8.2026. protiv istog prozora 2025.

---

## 1. Nalaz u jednoj tabeli

| Stranica | WEB 2025 → 2026 | IMAGE 2025 → 2026 |
|---|---|---|
| **EN `beaches-herceg-novi`** | 6,54 → 6,82 (**+0,28**) | 9,66 → **30,79** (**+21,13**) |
| **EN `restaurants-herceg-novi`** | 8,14 → 8,48 (**+0,35**) | 10,80 → **33,18** (**+22,37**) |
| EN `10-reasons-…` | 13,07 → 9,13 (−3,94) | 22,01 → 23,69 (+1,68) |
| SR `plaze-herceg-novi` | 14,23 → 4,48 (−9,74) | 8,64 → **7,61** (−1,03) |
| SR `restorani-herceg-novi` | 6,55 → 6,67 (+0,11) | 11,75 → 16,67 (+4,92) |
| SR `10-razloga` | 7,86 → 6,51 (−1,35) | 4,81 → 7,42 (+2,62) |

**Nije „engleske stranice" kao kategorija — nego dvije određene stranice.**
`beaches` i `restaurants` su izgubile 21 i 22 mjesta u slikama. Treća engleska
stranica (`10-reasons`) je praktično nepromijenjena.

**I nije stranica, nego njene slike.** Web pozicija obje je ravna na desetinku
mjesta. Iste stranice, isti tekst, isti rang u web pretrazi — a slike su pale
za dvadeset mjesta.

---

## 2. Nije kompozicija — iste riječi, dvadeset mjesta niže

Prva pretpostavka je bila da su stranice ušle u nove, šire upite na lošim
pozicijama. Provjerio sam po pravilu od 22.8. i **pretpostavka ne stoji.**

`beaches-herceg-novi`, isti upiti u oba prozora:

| Upit | Avg 2025 | Avg 2026 |
|---|---|---|
| `herceg novi beach montenegro` | **6,09** (324 im) | **47,96** (214 im) |
| `igalo montenegro beach` | **2,68** (149 im) | **17,31** (191 im) |
| `herceg novi beaches montenegro` | **6,67** (1.109 im) | **41,70** (69 im) |

Ovo su isti upiti, ne novi. Stranica je držala **poziciju 1,87 do 6,67** na
engleskim upitima za plaže, a danas je na 17 do 52.

Razlaganje na dvije korpe potvrđuje da je pad svuda:

| Korpa | 2025 | 2026 |
|---|---|---|
| Upiti koje ima i srpska stranica | 13,66 (55% impresija) | **20,87** |
| Upiti koje ima samo engleska | **6,66** (45%) | **39,54** |

Korpa u kojoj je engleska stranica bila najjača — engleski upiti koje srpska
uopšte ne dodiruje — pala je sa **6,66 na 39,54**.

---

## 3. Kad je počelo

Mjesečna image pozicija:

| Mjesec | EN beaches | SR plaze | EN restaurants | SR restorani |
|---|---|---|---|---|
| Jul 2025 | 10,2 | 9,0 | 12,4 | 12,5 |
| Avg 2025 | **9,0** | **8,4** | **10,3** | **11,7** |
| Jan 2026 | 12,7 | 10,3 | 30,0 | 20,2 |
| Maj 2026 | 49,8 | 23,9 | 46,5 | 20,3 |
| **Jul 2026** | 25,7 | **8,6** | 31,6 | 17,2 |
| **Avg 2026** | **31,4** | **7,5** | **34,4** | 16,7 |

Do januara 2026. engleske i srpske stranice su išle **zajedno**. Krah u
februaru je oborio sve. **U julu su se srpske vratile, engleske nisu** — i to
je cijela priča u jednom redu.

`plaze` je danas bolja nego prošlog avgusta (7,5 naspram 8,4). `beaches` je
tri i po puta gora.

---

## 4. Šta sam isključio

| Pretpostavka | Provjera | Ishod |
|---|---|---|
| Kompozicija upita | isti upiti, oba prozora | **isključeno** (§2) |
| Veličina slika | SR koristi **manje** slike (650 px webp), EN pune JPG (960–2048 px) — a SR rangira bolje | **isključeno** |
| Canonical | obje samoreferentne, ispravne | **isključeno** |
| hreflang | prisutan na obje (4–6 unosa) | **isključeno** |
| Interni linkovi | EN restaurants ima **12**, SR restorani **9** | **isključeno** |
| Kravl | obje kravlovane 22.8. | **isključeno** |
| Stranica kao takva | web pozicija ravna (+0,28 / +0,35) | **isključeno** |
| Obrisane slike | uklanjanje 9.7. nije dotaklo nijednu od ovih | **isključeno** |

Osam pretpostavki, osam isključenih. Ono što ostaje je jedna strukturna
osobina koju ove dvije stranice imaju, a `10-reasons` nema u istoj mjeri.

---

## 5. Šta sam našao: iste slike na dvije stranice

**`restaurants-herceg-novi` i `restorani-herceg-novi` koriste 19 od 19
identičnih URL-ova slika.** Ne sličnih — istih fajlova.

`beaches` i `plaze` dijele 8 od 9 fajlova, a u sitemapu **4 od 7 slika su
navedene pod obje stranice sa istim URL-om** (`zanjice.jpg`,
`plaza-topla.jpg`, `plaza-tunel.jpg`, `zalo.jpg`).

Za jedan URL slike Google bira **jednu** odredišnu stranicu. Ovdje mu dajemo
dvije i ne kažemo koja je prava.

Šire od ovog para: **35 od 74 slike u sitemapu je prijavljeno pod više
URL-ova.**

Ima i konkretna nedosljednost: `plaze-herceg-novi.html` u `ImageObject` schemi
tvrdi `plaza-herceg-novi.jpg` i `kruso.jpg` — **dvije slike koje ta stranica
ne prikazuje** (prikazuje `-650.webp` varijante). Obje te slike prikazuje
engleska `beaches` stranica.

### Ograda koju moram staviti

**Ovo ne dokazuje uzrok.** Image sitemap i ImageObject schema su dodati
**10.8.2026.**, a razilaženje je počelo u maju. Dijeljenje samih fajlova
postoji odavno — i u 2025., kad je engleska stranica bila na poziciji 9,0.

Dakle: našao sam stvaran strukturni nedostatak koji **danas pojačava** problem,
ali nisam našao šta se promijenilo u maju–julu. To ostaje neobjašnjeno i neću
se pretvarati da nije.

Najjača korelacija koju imam: dvije stranice sa najpotpunijim dupliranjem
(19/19 i 4/7) su tačno one dvije koje su pale, a treća engleska stranica sa
najmanje dupliranja je jedina koja nije.

---

## 6. Prijedlog: kontrolisan eksperiment, ne popravka naslijepo

Dvije opcije, različite po cijeni:

**A — jeftina.** Razdvojiti vlasništvo nad slikama u signalima: svaka slika u
sitemapu i schemi prijavljena pod tačno jednom stranicom, i to onom koja je
zaista prikazuje. Nema novih fajlova, potpuno reverzibilno.

**B — skupa.** Dati engleskim stranicama vlastite kopije dijeljenih slika sa
engleskim imenima fajlova. Oko 1,3 MB u repozitorijumu, ali uklanja
dvosmislenost u korijenu.

**Preporučujem A prvo**, jer ako je hipoteza tačna, A bi trebalo da bude
dovoljna; ako nije, ništa nismo potrošili.

### Pre-registrovano, prije podataka

| | Vrijednost |
|---|---|
| **Test stranica** | `beaches-herceg-novi` (image pozicija **30,79**) |
| **Kontrola** | `restaurants-herceg-novi` (**33,18**) — ostaje netaknuta |
| **Srpski parnjak** | `plaze-herceg-novi` (**7,61**) — ne smije se pogoršati |
| **Potvrda** | EN beaches ≤ **20,00** u 4 sedmice od rekravla, uz kontrolu koja ostaje ≥ 30 |
| **Odbacivanje** | EN beaches > 25,00 poslije 4 sedmice, ili `plaze` gora od 9,00 |

Kontrola je ugrađena u dizajn — ako obje stranice porastu, bila je sezona ili
Google, ne naša izmjena. To je tačno ono što je nedostajalo julskom testu sa
meta opisima, gdje je kontrolna stranica bila izložena istoj sili kao i test.

---

## 7. Koliko ovo vrijedi

Umjereno, i treba to reći otvoreno. Image kanal je **742 klika naspram 7.444
web klikova** — 9% saobraćaja. Ove dvije stranice zajedno nose 47 klikova u
28 dana.

Ali: `plaze-herceg-novi` sam u slikama nosi **502 klika**, na poziciji 7,4.
Engleske stranice su prije godinu dana bile na 9,0 i 10,3 — dakle na nivou na
kojem su srpske danas. Ako je razlika naša greška u signalima, to je nekoliko
stotina klikova godišnje na engleskom tržištu, koje je jedino tržište gdje
`apartmani-igalo.com` nema domaću konkurenciju u pretrazi.

**Ne šaljem ništa danas.** Izbor između A i B je vaš, a razlika je materijalna.
