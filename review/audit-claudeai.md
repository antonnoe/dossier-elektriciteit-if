# Eindaudit dossier (claude.ai-sessie, 04-07-2026)

## 1. De vier beleidsgevoelige punten — ALLE VIER BESLECHT en in de tekst verwerkt
| Punt | Uitslag | Bron |
|---|---|---|
| 12 kVA-grens monophasé | **BEVESTIGD**: Enedis-plafond mono = 12 kVA voor nieuwe aansluitingen; >12 → 36 kVA tri; legacy 13–18 kVA mono gedoogd | Enedis barème raccordement + référentiel (primair) |
| Base-optie ≥ 9 kVA | **BEVESTIGD + verder gevorderd**: dicht voor nieuwe TRV-klanten 9–15 kVA per 01-02-2025; hele band 9–36 kVA "mis en extinction" per 01-02-2026; 18+ bestaand → gedwongen HP/HC per 01-02-2027. Alleen Tarif Bleu; marktaanbod behoudt Base | EDF (particulier.edf.fr) + CRE-deliberatie 2026-06 + Que Choisir |
| kVA-reeksen & ombouwkosten | Reeksen vastgelegd; puissance-wissel = téléoperatie ±4,28 €, raccordement-wijziging = offerte (Catalogue des Prestations/F180); geen vaste bedragen citeren | Enedis référentiel |
| Linky-stand | ±95% / 37,6 mln; weigeraars sinds 01-08-2025: 6,48 € HT/2 mnd + 4,14 € HT bij >1 jr geen index; grondslag L341-4 | Enedis-persbericht feb 2026 + CRE 2025-78 |

Verwerkt in H1 (vier passages) en H7 (één passage); HTML opnieuw geassembleerd (open punten 28 → 23). Verificatierapport afgesloten met audit-blok.

## 2. Claimcontrole hoofdstukken tegen V-blokken
Steekproef harde getallen (83%, 2 Ω, 100/50/10 Ω, type F-verplichting, 8-circuits-regel, Consuel-tarieven, IRVE >3,7 kW, heures-creuses-kalender): consistent met de V-punten; geen afwijkingen aangetroffen. Resterende [NIET GEVERIFIEERD]-punten (23) zijn alle bewust en juist gemarkeerd; blokkerend voor publicatie zijn er daarvan twee categorieën: V13-rest (FR-historische draadkleuren, draaddiktentabel) en V14-rest (NL-Bbl-verwijzing, BE-keuringsdetails).

## 3. ROB-conservering
40 markeringen in de hoofdstukken (rapportage CCode: 47 incl. HTML-duplicaten). Citaat-audit: geautomatiseerde matching vindt 14/27 blockquotes letterlijk; handmatige controle van de niet-matches wijst op (…)-inkortingen als oorzaak (toegestaan per briefing) — deelcontrole tegen de brontekst (o.a. de-aarding.txt) bevestigt letterlijke overname. Geen geherformuleerde passages onder ROB-vlag aangetroffen. NB: markerconventie is enkelvoudig `<!-- ROB -->` (niet open/dicht) — bij eindredactie consistent houden.

## 4. SVG's
12 stuks, inline, geen externe verwijzingen, geen picr. 7 dragen de attributieregel naar het oorspronkelijke schema; 5 zonder attributie zijn nieuw ontwerp zonder origineel (id-typen/type F, EV-beslisboom, Consuel-flow, circuits-tabel, mono-vs-tri) — legitiem. Inhoudscheck id-typen en groepenkast tegen V2 (type A/F, 8-regel): correct.

## 5. Huisstijl & assemblage
Poppins/Mulish/1.8em/#800000 + rgba-varianten aanwezig; één Divi-blok, ankernavigatie, ABONNEE-BLOK-placeholders intact. Buildscript `_build_dossier.py` gerepareerd (hardcoded /workspace-pad → padonafhankelijk), her-assemblage draait.

## 6. Redirects
14 regels aanwezig incl. woordenlijst-slug. Open voor Anton: slug regel 12 (dood belastingbericht), URL regel 13 (Dossier Internet), besluit forum-topic-301's.

## Resterend vóór publicatie (volgorde)
1. Anton: twee slugs + forumtopic-301-besluit + CC BY-NC-SA-afweging NLFR-citaten.
2. Sessie: V13-rest + V14-rest wegwerken en de laatste [NIET GEVERIFIEERD]-punten aflopen.
3. Anton: inhoudelijke eindredactie + leesexemplaar naar Rob.
4. Publicatie WordPress/Divi + 14×301 + canonical-fix (Anton, handmatig).
