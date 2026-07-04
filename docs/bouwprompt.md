# BOUWPROMPT — Dossier Elektriciteit, fase 1 stap 3–5 (Claude Code)

Je schrijft het Dossier Elektriciteit voor Infofrankrijk.com. **Alles wat je
nodig hebt staat in deze repo** — je hebt géén internettoegang nodig en doet
géén eigen webonderzoek. Werk autonoom door tot het STOP-PUNT; vraag geen
tussentijdse bevestigingen voor lezen, schrijven of committen binnen deze repo.

## Lees eerst, in deze volgorde
1. Cockpit-briefing: `antonnoe/antonnoe-antons-cockpit---private` →
   `docs/briefings/2026-07-03-dossier-elektriciteit-if.md` (het plan; als die
   repo niet bereikbaar is: de kern staat hieronder herhaald, werk door).
2. `verificatie/normverificatie.md` — **de enige toegestane bron voor elke
   normclaim, tarief, drempel of verplichting.**
3. `oogst/oogstdocument.md` (72 items incl. VEROUDERD-markeringen),
   `oogst/bronstatus.md`, `oogst/verwante-assets.md`.
4. `oogst/bronteksten/` (Robs volledige artikelen), `oogst/forumdump/`
   (complete threads + Robs losse reacties), `oogst/beeldarchief/` (originelen).

## HARDE REGELS
- **Elke feitelijke claim moet herleidbaar zijn tot een V-punt in
  normverificatie.md.** Staat iets daar niet in → schrijf het niet, of markeer
  het in de tekst als `[NIET GEVERIFIEERD]` en zet het op de openpuntenlijst
  van het reviewpakket. Nooit gissen, nooit uit eigen kennis aanvullen.
- Respecteer alle VEROUDERD-markeringen in het oogstdocument (o.a. item 30).
- Forumcitaten: attributie uitsluitend op de ondertekening ín de tekst
  (zie migratienotitie in het oogstdocument); anders "forumdeelnemer".
- Robs geconserveerde passages markeren met `<!-- ROB -->`; niet gladstrijken.
- Verboden woord: "ecosysteem". CTA exact: "Word abonnee".
- Niets publiceren; geen WordPress, geen redirects, geen canonicals — dat is
  aan Anton, ná review.
- Tijdgevoelige feiten (tarieven, subsidies, hervormingskalender) uitsluitend
  in gemarkeerde blokken met verificatiedatum (04-07-2026).

## Stap 3 — Hoofdstukken 0–9
Structuur en sjabloon per hoofdstuk conform de briefing: snel antwoord
(tabel/checklist) → Robs kern → verdieping → NL–BE–FR-blok → kader "Uit de
praktijk" → tijdgevoelig blok. Schrijf in `/hoofdstukken/h0.md` t/m `h9.md`.
Vaste ankers uit de verificatie, o.a.: H0 opent met het 83%-anomaliecijfer
(V12), H1 verwerkt de heures-creuses-hervorming (V11) en Linky-als-standaard
(V10), H3 type F + AFDD-onderscheid (V2), H4 de 100/50/10 Ω-band en de
2 Ω-regel (V3), H5 de kleuren-valkuil oud-NL-groen=fase (V13), H6 volumes +
LES (V4/V5), H7 IRVE-plicht >3,7 kW en het gestopte crédit d'impôt (V7),
H8 de 2024-serie + regelgevingsnuance + Consuel (V1/V8/V9), rode draad
"de Hollandse reflex" (oogst-aanvulling 4). Colofon exact zoals in de
briefing; verwerk oogst-item 61 (Robs 2012-voorspelling) in de verantwoording.

## Stap 4 — SVG's
10–13 schema's conform briefing: inline-SVG, lijnen #800000, labels Poppins
(fallback sans-serif), transparante achtergrond, tekst als tekst, responsieve
viewBox. Inhoud uitsluitend op basis van geverifieerde V-punten; per SVG een
commentaarregel met V-verwijzing én bijschrift-attributie: "Naar het
oorspronkelijke schema van [maker] ([jaar]), geactualiseerd naar
NF C 15-100 (2024)" — makers herleiden via oogst/beeldarchief + bronteksten.
Opslaan in `/svg/` en inline verwerken in de hoofdstukken.

## Stap 5 — Assemblage en reviewpakket
1. `/dossier/dossier-elektriciteit.html`: één compleet HTML-blok voor een
   Divi-codemodule; Poppins (H1/H2), Mulish (body), regelafstand 1.8em,
   #800000 + rgba-varianten (0.04–0.80); ankernavigatie per hoofdstuk;
   alle SVG inline; nul externe afhankelijkheden (géén picr.de);
   abonnee-plekken als `<!-- ABONNEE-BLOK: ... -->`.
2. `/review/reviewpakket.md`: samenvatting per hoofdstuk; complete
   `[NIET GEVERIFIEERD]`-lijst; de veertien 301-regels (dertien uit de
   briefing + oude woordenlijst-slug → nieuwe, zie verwante-assets);
   canonical-checklist; de V10/V11/V13/V14-restpunten uit de verificatie.
3. `/review/leesexemplaar-rob.md`: alle "Uit de praktijk"-kaders met bron,
   als leesstuk zonder procesjargon.

## STOP-PUNT
Klaar = reviewpakket compleet in de repo. Meld dan: aantal hoofdstukken,
aantal SVG's, aantal [NIET GEVERIFIEERD]-punten, en de drie punten die de
meeste aandacht van Anton vragen. Commit atomair per hoofdstuk.
