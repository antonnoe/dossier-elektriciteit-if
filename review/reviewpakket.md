# Reviewpakket — Dossier Elektriciteit (fase 1)

Opgeleverd 04-07-2026 door Claude Code (bouwprompt stap 3–5). **Niets is gepubliceerd**; alle onderstaande acties zijn aan Anton, ná review.

## 1. Wat er ligt

- `/hoofdstukken/h0.md` t/m `h9.md` — tien hoofdstukken volgens het vaste sjabloon (snel antwoord → Robs kern → verdieping → NL–BE–FR → Uit de praktijk → tijdgevoelig blok).
- `/svg/` — 12 schema's, huisstijl (#800000, Poppins, tekst als tekst), elk met verificatiebron en attributie in de commentaarkop.
- `/dossier/dossier-elektriciteit.html` — één Divi-codemodule-blok: 153 kB, ankernavigatie, alle 12 SVG's inline, **nul externe afhankelijkheden** (geen picr.de, geen hotlinks, geen fonts-import — Poppins/Mulish komen uit het thema). Reproduceerbaar via `/dossier/_build_dossier.py`.
- `/review/leesexemplaar-rob.md` — het leesstuk voor Rob.

### Samenvatting per hoofdstuk

| H | Kern | Robs stem | Nieuw/geactualiseerd |
|---|---|---|---|
| 0 | Veiligheidsritueel + "mag ik dit zelf?" NL/BE/FR | Intro + veiligheidsritueel + kniptang-anekdote integraal | 83%-anomaliecijfer (ONSE) vervangt het oude brandcijfer; rode draad "Hollandse reflex" geïntroduceerd |
| 1 | Aansluiting, mono/tri, puissance souscrite, tariefopties | Toevoer-artikel + headroom-uitleg 2021 | Linky als uitgangspunt; heures-creuses-hervorming 2025–2027 als tijdgevoelig blok |
| 2 | DB/AGCP: drie functies | Hoofdschakelaar-artikel vrijwel integraal geconserveerd | 30 mA-verwijzing naar actuele norm; Linky-tolerantieverschil |
| 3 | Groepenkast: ID-regels, typen, parafoudre, GTL/ETEL | Ontvlechtwerk, U-vorm-tip, plomb sauté, prijsvergelijking | Type F verplicht / AFDD aanbevolen (2024); parafoudre hierheen verhuisd (woningregels ongewijzigd, V6) |
| 4 | Aarding: elektrode→barrette→répartiteur, LES | Aarding-artikel + overtuig-citaat + heggenschaar | 100/50/10 Ω-band; 2 Ω-regel met V3-precisering |
| 5 | Leidingaanleg, buizen, spanningsval, kleuren | Leidingaanleg-artikel (dominos/Wago, boîte de combles) | Draadkleurentabel NL/BE/FR prominent (V13); décompte-regel expliciet als VEROUDERD gemarkeerd |
| 6 | Schakelingen + eisen per kamer + badkamer | Sinterklaas-anekdote, auditief spoorzoeken, F/F-waarschuwing | Volumes bevestigd ongewijzigd (V4); rolluiken-circuit nieuw (2024); telregel 1=1 |
| 7 | **Geheel nieuw**: warmtepomp, EV, boiler, V2G | EV-gesprek 2020 + V2G-café + thuisbatterij-nuchterheid | IRVE-plicht, 7-722, type F/B, subsidiestand per 04-07-2026 |
| 8 | Normen, Consuel, diagnostic | Normgeschiedenis-citaten 2016 + dec 2024; gloeilamp indirect via leesexemplaar | 2024-refonte (21 delen) + norm-vs-verplichtstelling-nuance; Consuel-tarieven en -historie (dancing 5-7) |
| 9 | Naslag: woordenlijst, boeken, websites, colofon | Boekenoordelen + France-profonde-slotkader + dankwoord Christian | Elektra-kernwoordenlijst (verwijst naar de grote woordenlijst, dupliceert niet); AFNOR-boek 2026; colofon exact conform briefing + archiefvoorspelling 2012 |

## 2. Alle [NIET GEVERIFIEERD]-punten op één lijst

**Beleidsgevoelig — kunnen inhoud kantelen, vóór publicatie beslechten:**
1. Monophasé > 12 kVA niet meer leverbaar voor nieuwe aansluitingen (Rob 2020, o.v.v. Enedis §15.2.2) — raakt H1 én H7.
2. Afschaffing Base-optie ≥ 9 kVA per 01-02-2025 (één bron; V11-restpunt).
3. Actuele kVA-reeksen mono/tri + kosten ombouw tri↔mono (Enedis Catalogue des Prestations).
4. Linky: actueel uitrolpercentage + regeling/meerkosten niet-communicerende meters (V10-rest).

**Normdetails (deel 10-hertoets, laag risico maar netjes afmaken):**
5. Bereikbaarheids-/binnenshuis-eis van de DB in de 2024-serie (H2).
6. Promotelec-spanningsvaltabellen DB→tableau: actuele waarden (H2/H5).
7. ETEL/GTL-maatvoering en detailbepalingen deel 10 (H3).
8. Tabel 10-1G: ID-kaliber bij zonnepanelen/thuisbatterij (H3).
9. Buis-vulregeltabellen actueel (H5).
10. Spanningsval 3%/5%-formulering + non-accolé-halvering in actuele tekst (H5).
11. Sortie-de-câble-aansluitregels en DCL-uitzonderingen in actuele tekst (H6).
12. LES-elementenlijst: wat is er precies aangepast in de 2024-serie (H6; V4-rest).
13. Obturateurs/spreidklem-jaartallen (2004) — individuele data (H4).

**NL/BE-kolommen:**
14. NL: formele Bbl-artikelverwijzing zelf klussen/NEN 1010-doorwerking (H0/V14-rest).
15. NL: actuele NEN 1010-stand (4-groepenregel, AC-verbod) (H3).
16. BE: AREI-artikelen hoofddifferentieel/30 mA + keuringsdetails bij verkoop (termijnen, kosten) (H2/H0).
17. FR-historische draadkleuren (rood/zwart als fase) + landvergelijkende draaddiktentabel (H5; V13-rest).

**Klein/naslag:**
18. RTE-productiemix indien groene-stroom-passage blijft (H1).
19. V2G-marktstand Frankrijk 2026 (H7).
20. Gallauziaux & Fedullo: is er al een druk op de 2024-serie? + drukstand fabrikantengidsen (H9).
21. Linkcheck website-lijst H9 (schema-electrique, volta, forum-electricite).

**Bewust weggelaten (loggen conform opdracht):**
- Robs brandcijfer 2012 (250.000/80.000) — vervangen door ONSE-cijfers [V12]; oude cijfer expliciet gedeactiveerd in H0.
- Robs décompte-teltip — VEROUDERD (V5.1), alleen als historische voetnoot met correctie in H5.
- Oppervlakteregels ID's (2/3/4 naar m²) — vervallen sinds A5, alleen historisch (H3).
- Bewering "Franse armaturenfabrikanten zijn aandeelhouder van de Consuel" (Bram van Zanten) — governance niet verifieerbaar; weggelaten. Zijn praktijkanekdotes (7 keuringen/40 jaar; baguette-afkeuring) zijn wél gebruikt.
- UK-doorstroomverwarmer-draaddikten (4/6 mm²) alleen als indicatie in kader, niet als normclaim.

## 3. Beeldbesluiten

Basis: `/oogst/beeldinventaris.md` (61 lokale afbeeldingen, 88 externe picr.de-verwijzingen) en het geredde beeldarchief in `/oogst/beeldarchief/`.

| Categorie | Besluit |
|---|---|
| **Alle 88 picr.de-verwijzingen** | **Vervallen.** De instructieve schema's daaruit zijn herbouwd als 12 SVG's tegen de geverifieerde normstand (niet overgetrokken). Originelen blijven bewaard in `/oogst/beeldarchief/` (erfgoed + naslag voor eindredactie Rob). |
| **Instructieve scans/tekeningen lokaal** (o.a. Elektriciteit4/8/12–25-serie) | Vervangen door de SVG's; niet terugplaatsen (tonen deels verouderde normdetails). |
| **Robs eigen foto's** (meterkast, groepenkasten, aardingsmateriaal, boîtes, plinthe) | **Behouden als herkenningsbeeld — keuze Anton welke.** Voorstel: frankrijk-meterkast (H1), 2× groepenkast-detail (H3), regard de visite/aardklem (H4), boîte d'encastrement + plinthe (H5). Het dossier-HTML is bewust zonder foto's opgeleverd; foto's kunnen als Divi-afbeeldingsmodules tussen de secties. |
| **Pexels-stockfoto** (aanbevolen-websites) | Vervallen. |
| **picr-PDF's** (o.a. Promotelec-scans) | Niet herpubliceren (auteursrecht); in beeldarchief laten als naslag. |

## 4. Open keuzes voor Anton

1. **Foto-selectie** (zie beeldbesluiten) — welke Rob-foto's terug als herkenningsbeeld?
2. **`/forum_old/`**: alle paden geven 404 terwijl GSC er nog clicks op toont. Bewust verwijderd? Zo nee: terugzetten; zo ja: 404 laten of meenemen in de 301-operatie (bronstatus.md, actiepunt).
3. **Gerichte 301's van oude elektra-forumtopics**: /forums/ redirect nu álles naar de homepage (SEO-lek). Voorstel: de bekende elektra-topic-URL's gericht naar dossier-ankers (lijst kan uit `/oogst/forumdump/_topicindex.md` worden samengesteld zodra jij het wilt).
4. **Twee redirect-doelen invullen**: de slug van het dode belastingvoordelen-bericht (2017) en de exacte URL van het Dossier Internet (regels 12–13 hieronder).
5. **NLFR-citaten**: nederlanders.fr-inhoud valt onder CC BY-NC-SA én is van de eigen uitgever; citaten staan er nu met naam + bron + datum. Akkoord zo, of aanvullende vermelding onderaan het dossier?
6. **H0-vergelijking**: er staat een alternatieve H0 uit de claude.ai-sessie in `/review/h0-alternatief-claudeai.md` — kies of meng bij eindredactie.
7. **Freemium-plekken**: 7 `<!-- ABONNEE-BLOK -->`-placeholders (H0, H1×1 in tijdblok, H2, H3, H5, H7, H9). Akkoord met plaatsing?

## 5. De veertien 301-regels (klaar om over te nemen)

Doel-URL: `https://infofrankrijk.com/de-franse-elektrische-installatie/`

| # | Van | Naar |
|---|---|---|
| 1 | `/elektriciteitsaanvoer-en-elektriciteitsmeter/` | `/de-franse-elektrische-installatie/#aansluiting` |
| 2 | `/de-hoofdschakelaar/` | `/de-franse-elektrische-installatie/#hoofdschakelaar` |
| 3 | `/de-groepenkast/` | `/de-franse-elektrische-installatie/#groepenkast` |
| 4 | `/de-aarding/` | `/de-franse-elektrische-installatie/#aarding` |
| 5 | `/de-leidingaanleg/` | `/de-franse-elektrische-installatie/#leidingaanleg` |
| 6 | `/speciale-schakelingen/` | `/de-franse-elektrische-installatie/#schakelingen` |
| 7 | `/nog-losse-tips-en-nieuwe-regels-amendement-5-2015/` | `/de-franse-elektrische-installatie/#normen-keuring` |
| 8 | `/aanbevolen-boeken/` | `/de-franse-elektrische-installatie/#naslag` |
| 9 | `/aanbevolen-websites-en-veranderende-nf-c-15-100-normen/` | `/de-franse-elektrische-installatie/#naslag` |
| 10 | `/de-elektrische-installatie/` (duplicaat 2017) | `/de-franse-elektrische-installatie/` |
| 11 | `/klussen/elektriciteit/` (alias toevoer-artikel, oude permalinkstructuur) | `/de-franse-elektrische-installatie/#aansluiting` |
| 12 | *(slug belastingvoordelen-bericht 2017 — door Anton aan te leveren)* | `/de-franse-elektrische-installatie/#zwaar-verbruik` |
| 13 | `/telefoon-internettechniek/` | *(URL Dossier Internet — door Anton in te vullen)* |
| 14 | `/woordenlijst-bouwkundige-termen/` (404 zonder redirect; NLFR + Google linken ernaar) | `/woordenlijst-klussen-bouwen-nl-⇄-fr/` |

Let op ankernamen: `#inleiding · #aansluiting · #hoofdschakelaar · #groepenkast · #aarding · #leidingaanleg · #schakelingen · #zwaar-verbruik · #normen-keuring · #naslag`.

## 6. Canonical-checklist (deze pagina, bij publicatie)

- [ ] Canonical van `/de-franse-elektrische-installatie/` = exact `https://infofrankrijk.com/de-franse-elektrische-installatie/` — **niet** het tempurl.host-stagingdomein (lekt wisselend/situationeel; bij de meting van 03-07 waren de canonicals correct, maar het blijft controlepunt).
- [ ] `og:url` en sitemap-vermelding op hetzelfde adres.
- [ ] Na het doorvoeren van de 301's: de 13 oude URL's uit de sitemap; GSC-inspectie op de doel-URL.
- [ ] Stagingdomein: indexatiestatus tempurl.host controleren (site-query) — sitewide sanering apart agenderen, maar déze pagina moet schoon zijn.
- [ ] Divi-codemodule: controleren dat het thema Poppins + Mulish laadt op deze pagina (het dossier importeert bewust géén fonts).

## 7. Verificatie-restpunten uit normverificatie.md (V-nummers)

- **V10-rest**: Linky-uitrol% + niet-communicerende-meterregeling (→ lijstpunt 4).
- **V11-rest**: puissance-reeksen + ombouwkosten + Base-afschaffing tweede bron (→ punten 1–3).
- **V13-rest**: FR-historische kleuren + draaddiktentabel NL/BE/FR (→ punt 17).
- **V14-rest**: NL-Bbl-verwijzing; BE-keuringsdetails (→ punten 14–16).
- V6 is afgerond (parafoudre-tegenstrijdigheid opgelost); V12 afgerond (ONSE-pinbron).

## 8. Telling voor het stop-punt

- Geoogste items: **72** (oogstdocument): artikelserie 20 · IF-forum incl. WXR-dump ±29 · nederlanders.fr ±19 · oud archief/3543-fragmenten 2 · Christians archief 0 (geen elektra aangetroffen; wel colofon-vermelding).
- Verificatie: **14 V-blokken**, waarvan 10 volledig geverifieerd, 4 met restpunten (V10, V11, V13, V14). In de dossiertekst: alle harde claims dragen een status; **21 open [NIET GEVERIFIEERD]-punten** (lijst §2), waarvan 4 beleidsgevoelig.
- SVG's: **12** (h1×2, h2, h3×2, h4×2, h5, h6×2, h7, h8).
- Rob-conservering: alle `<!-- ROB -->`-passages gemarkeerd in de bron-markdown én in de HTML (44 markeringen).
