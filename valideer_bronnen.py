#!/usr/bin/env python3
"""Validator voor het bronnenregister van het dossier De Franse elektrische installatie.

Draait vóór dossier/_build_dossier.py in de bouwketen (zie bouw.sh). Faalt met een
niet-nul exitcode zodra een harde regel wordt geschonden, zodat de build niet groen
wordt op een openstaand punt. Waarschuwingen laten de build wél doorgaan.

Bronregister : bronnen.json (repo-root)
Claimbestanden: verificatie/*-claims.json  (nu H1; generiek voor H0/H2..H9 later)

FAALREGELS (exitcode != 0)
  1. Een bronverwijzing in een hoofdstuk (claim.bron_id, of een inline-marker in
     een hoofdstuk-/blokbestand) die naar een niet-bestaand bron-id wijst.
  2. Een claim van een hard type (bedrag, percentage, aantal, datum, wetsartikel,
     normreferentie, termijn, specificatie) die als LIVE (actie ongewijzigd /
     corrigeren / herformuleren) aan een bron met tier A, B of C hangt.
  3. Een bron die door een LIVE claim wordt aangehaald en geen gecontroleerd_op
     heeft, of waarvan geldig_tot in het verleden ligt (t.o.v. de peildatum).
  4. Een bron met verificatie "op_te_halen" die aan een claim met actie
     "ongewijzigd" hangt.

WAARSCHUWINGEN (exitcode 0)
  - Een bron (aangehaald door een LIVE claim) waarvan gecontroleerd_op ouder is
    dan twaalf maanden t.o.v. de peildatum.
  - Een URL die geen HTTP 200 geeft. Alleen met --check-urls (netwerk), zodat de
    build ook offline draait.

De faalregels 2/3/4 zijn bewust gekoppeld aan LIVE claims: een claim op actie
open_punt of schrappen wordt (nog) niet als gepubliceerde bron behandeld. Een
openstaand punt los je dus op door de claim op actie open_punt te zetten, niet
door een regel te versoepelen.
"""
import json
import sys
import glob
import os
import re
import argparse
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))

HARDE_TYPES = {
    "bedrag", "percentage", "aantal", "datum",
    "wetsartikel", "normreferentie", "termijn", "specificatie",
}
LIVE_ACTIES = {"ongewijzigd", "corrigeren", "herformuleren"}
LAGE_TIERS = {"A", "B", "C"}
INLINE_MARKER = re.compile(r'(?:data-bron-id="|\{\{\s*bron:\s*)(B\d+)')


def parse_datum(s):
    if not s:
        return None
    for fmt in ("%Y-%m-%d",):
        try:
            return date.fromisoformat(s)
        except ValueError:
            pass
    # jaar-only of jaar-maand: niet als harde datum bruikbaar voor vergelijking
    return None


def maanden_verschil(vroeger, later):
    return (later.year - vroeger.year) * 12 + (later.month - vroeger.month)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-urls", action="store_true",
                    help="controleer HTTP-status van elke URL (netwerk; alleen waarschuwing)")
    args = ap.parse_args()

    fouten = []
    warns = []

    # --- register laden ---
    reg_pad = os.path.join(REPO, "bronnen.json")
    if not os.path.exists(reg_pad):
        print(f"FOUT: register niet gevonden: {reg_pad}", file=sys.stderr)
        return 2
    reg = json.load(open(reg_pad, encoding="utf-8"))
    bronnen = {b["id"]: b for b in reg["bronnen"]}
    peildatum = parse_datum(reg.get("peildatum")) or date.today()

    # --- claimbestanden laden ---
    claimbestanden = sorted(glob.glob(os.path.join(REPO, "verificatie", "*-claims.json")))
    claims = []
    for cb in claimbestanden:
        d = json.load(open(cb, encoding="utf-8"))
        for c in d.get("claims", []):
            c["_bestand_claims"] = os.path.relpath(cb, REPO)
            claims.append(c)

    # --- regel 1: dangling bron_id in claims ---
    for c in claims:
        bid = c.get("bron_id")
        if bid and bid not in bronnen:
            fouten.append(
                f"[regel 1] claim {c['id']} ({c.get('bestand')}:{c.get('regel')}) "
                f"verwijst naar niet-bestaand bron-id '{bid}'")

    # --- regel 1: dangling bron_id in inline-markers in hoofdstuk-/blokbestanden ---
    bron_bestanden = (glob.glob(os.path.join(REPO, "hoofdstukken", "*.md")) +
                      glob.glob(os.path.join(REPO, "blokken", "*.html")))
    for f in bron_bestanden:
        tekst = open(f, encoding="utf-8").read()
        for m in INLINE_MARKER.finditer(tekst):
            if m.group(1) not in bronnen:
                fouten.append(
                    f"[regel 1] {os.path.relpath(f, REPO)} bevat een inline-verwijzing "
                    f"naar niet-bestaand bron-id '{m.group(1)}'")

    # --- regels 2/3/4 over LIVE claims ---
    live_bron_refs = {}  # bron_id -> lijst van claim-id's (live)
    for c in claims:
        actie = c.get("actie")
        bid = c.get("bron_id")
        if not bid or bid not in bronnen:
            continue
        bron = bronnen[bid]

        # regel 4: op_te_halen bron aan actie ongewijzigd
        if actie == "ongewijzigd" and bron.get("verificatie") == "op_te_halen":
            fouten.append(
                f"[regel 4] claim {c['id']} heeft actie 'ongewijzigd' maar bron {bid} "
                f"heeft verificatie 'op_te_halen' — eerst ophalen of claim op open_punt zetten")

        if actie in LIVE_ACTIES:
            live_bron_refs.setdefault(bid, []).append(c["id"])
            # regel 2: hard type aan lage tier
            if c.get("type") in HARDE_TYPES and bron.get("tier") in LAGE_TIERS:
                fouten.append(
                    f"[regel 2] claim {c['id']} (type {c.get('type')}) hangt aan bron {bid} "
                    f"met tier {bron.get('tier')} — harde gegevens vereisen tier AAA of AA")

    # --- regel 3 + waarschuwing ouderdom: over bronnen die een LIVE claim aanhaalt ---
    for bid, claim_ids in sorted(live_bron_refs.items()):
        bron = bronnen[bid]
        gc = bron.get("gecontroleerd_op")
        if not gc:
            fouten.append(
                f"[regel 3] bron {bid} (aangehaald door {', '.join(claim_ids)}) "
                f"heeft geen gecontroleerd_op")
        else:
            gcd = parse_datum(gc)
            if gcd and maanden_verschil(gcd, peildatum) > 12:
                warns.append(
                    f"[waarschuwing] bron {bid} laatst gecontroleerd op {gc} — ouder dan 12 maanden")
        gt = parse_datum(bron.get("geldig_tot"))
        if gt and gt < peildatum:
            fouten.append(
                f"[regel 3] bron {bid} (aangehaald door {', '.join(claim_ids)}) "
                f"heeft geldig_tot {bron.get('geldig_tot')} in het verleden (peildatum {peildatum})")

    # --- optionele URL-controle (netwerk) ---
    if args.check_urls:
        import urllib.request
        for bid, bron in sorted(bronnen.items()):
            url = bron.get("url")
            if not url:
                continue
            try:
                req = urllib.request.Request(url, method="HEAD",
                                             headers={"User-Agent": "bronnen-validator"})
                code = urllib.request.urlopen(req, timeout=15).status
                if code != 200:
                    warns.append(f"[waarschuwing] {bid} URL geeft HTTP {code}: {url}")
            except Exception as e:
                warns.append(f"[waarschuwing] {bid} URL niet bereikbaar ({e.__class__.__name__}): {url}")

    # --- rapport ---
    print(f"Validatie bronnenregister — peildatum {peildatum}")
    print(f"  {len(bronnen)} bronnen, {len(claims)} claims uit {len(claimbestanden)} claimbestand(en)")
    for w in warns:
        print("  " + w)
    if fouten:
        print(f"\nGEFAALD: {len(fouten)} fout(en):", file=sys.stderr)
        for f in fouten:
            print("  " + f, file=sys.stderr)
        return 1
    print(f"  {len(warns)} waarschuwing(en), 0 fouten — OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
