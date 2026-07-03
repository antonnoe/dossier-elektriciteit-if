# Dossier Elektriciteit — Infofrankrijk.com

Werkrepository voor de consolidatie van de elektra-serie van Rob van der Meulen
(2008–2017) tot één NL-talig handboek: **De Franse elektrische installatie**.
Doel-URL: `/de-franse-elektrische-installatie/`.

Plan-briefing: Cockpit-repo → `docs/briefings/2026-07-03-dossier-elektriciteit-if.md`.
Fase 1 eindigt met een compleet reviewpakket — **geen publicatie vanuit deze repo**.

## Structuur

| Map | Inhoud |
|---|---|
| `/oogst/` | Geoogst vakmanschapsmateriaal uit de bronnen (citaat · bron-URL · auteur · datum · doelhoofdstuk · gebruiksvoorstel) + beeldinventaris |
| `/oogst/nlfr-aangeleverd/` | Uitsluitend door Anton handmatig aangeleverd NLFR-materiaal (nederlanders.fr wordt niet gescrapet) |
| `/verificatie/` | Normverificatie-rapport: elke harde claim `[GEVERIFIEERD: bron, datum]` of `[NIET GEVERIFIEERD]` |
| `/hoofdstukken/` | Concepthoofdstukken 0–9 (markdown, later HTML) |
| `/svg/` | Schema's in huisstijl (#800000, Poppins-labels, tekst als echte tekst) |
| `/dossier/` | Het samengestelde eindbestand `dossier-elektriciteit.html` (Divi-codemodule) |
| `/review/` | Reviewpakket voor Anton + leesexemplaar voor Rob van der Meulen |

## Bronnen fase 1

- **A** — oud forumarchief, topic 3543 (statische kopie onder `infofrankrijk.com/forum_old/`)
- **B** — IF bbPress-forum (`infofrankrijk.com/forums/`), sectie "Bouwen, verbouwen en klussen"
- **C** — Christians archief: `antonnoe.github.io/klussen-in-frankrijk-christian-von-klosterlein/` (auteur: Christian von Klösterlein)
- **D** — de elf bestaande IF-artikelen van de elektra-serie

Normverificatie uitsluitend tegen primaire/officiële bronnen: Légifrance,
service-public.fr, consuel.com, enedis.fr, promotelec.com, economie.gouv.fr/CRE;
voor NL: NEN 1010-afgeleiden, voor BE: AREI/RGIE (economie.fgov.be).
