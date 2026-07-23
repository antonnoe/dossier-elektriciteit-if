#!/usr/bin/env python3
"""Presentatie van het bronnenregister voor beide uitvoerkanalen.

Gedeeld door dossier/_build_dossier.py en redactie/_build.py. Levert:
  - panel_html(redactie): het uitklapbare bronnenoverzicht uit bronnen.json,
    huisstijl (Poppins/Mulish, regelafstand 1.8em, #800000 + rgba-varianten,
    witte kaarten), CSS strikt afgeschermd onder .if-dossier-wrapper. Elke
    bronregel heeft id="bron-Bxx" als sprongdoel voor de inline-markers. In de
    redactie-variant krijgt elke regel de klasse mg-deel, zodat het bestaande
    klik-opmerkingenmechanisme er een opmerking bij kan plaatsen.
  - vervang_markers(html, geldige_ids): zet {{bron:Bxx}}-tokens uit de lopende
    tekst om in een klikbare superscript-marker die naar #bron-Bxx springt.
"""
import os
import re
import json

_HIER = os.path.dirname(os.path.abspath(__file__))
_MARKER = re.compile(r"\{\{\s*bron:\s*(B\d+)\s*\}\}")

_STYLE = """
.if-dossier-wrapper .if-bronnen{font-family:Mulish,sans-serif;line-height:1.8em;color:#2a2622;margin:2.4em 0;border:1px solid rgba(128,0,0,0.20);border-radius:8px;background:rgba(128,0,0,0.03);padding:0 1.3em;}
.if-dossier-wrapper .if-bronnen>summary{font-family:Poppins,sans-serif;color:#800000;font-weight:700;font-size:1.1em;cursor:pointer;padding:.9em 0;list-style:none;}
.if-dossier-wrapper .if-bronnen>summary::-webkit-details-marker{display:none;}
.if-dossier-wrapper .if-bronnen>summary::before{content:"\\25B8 ";color:rgba(128,0,0,0.80);}
.if-dossier-wrapper .if-bronnen[open]>summary::before{content:"\\25BE ";}
.if-dossier-wrapper .if-bronnen .toel{font-size:.9em;color:#6b635c;margin:0 0 1em;}
.if-dossier-wrapper .if-bron{background:#ffffff;border:1px solid rgba(128,0,0,0.15);border-left:3px solid rgba(128,0,0,0.80);border-radius:6px;padding:.7em .9em;margin:0 0 .7em;scroll-margin-top:5em;}
.if-dossier-wrapper .if-bron .kop{font-family:Poppins,sans-serif;color:#5a0000;font-weight:600;}
.if-dossier-wrapper .if-bron .doc{}
.if-dossier-wrapper .if-bron .meta{font-size:.85em;color:#6b635c;margin-top:.2em;}
.if-dossier-wrapper .if-bron .tier{font-family:Poppins,sans-serif;font-weight:700;color:#800000;}
.if-dossier-wrapper .if-bron .status{font-style:italic;}
.if-dossier-wrapper .if-bron a{color:#800000;}
.if-dossier-wrapper .if-bron.is-target{background:rgba(128,0,0,0.06);}
""".strip()

# inline stijl (geen losse CSS-regel nodig, dus geen lek buiten .if-dossier-wrapper)
_SUP = ('<sup class="if-bronref" style="font-family:Poppins,sans-serif;line-height:0;">'
        '<a href="#bron-{bid}" style="color:#800000;text-decoration:none;font-size:.72em;'
        'font-weight:700;padding:0 .1em;" title="Bron {bid} — {titel}">[{bid}]</a></sup>')


def laad_register():
    with open(os.path.join(_HIER, "bronnen.json"), encoding="utf-8") as f:
        return json.load(f)


def _esc(s):
    if s is None:
        return ""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def geldige_ids():
    return {b["id"] for b in laad_register()["bronnen"]}


def titel_van(bid):
    for b in laad_register()["bronnen"]:
        if b["id"] == bid:
            return b.get("instantie", "")
    return ""


def vervang_markers(html, ids=None):
    if ids is None:
        ids = geldige_ids()
    titels = {b["id"]: b.get("instantie", "") for b in laad_register()["bronnen"]}

    def sub(m):
        bid = m.group(1)
        if bid not in ids:
            return m.group(0)  # laat staan; de validator meldt een dangling verwijzing
        return _SUP.format(bid=bid, titel=_esc(titels.get(bid, "")))

    return _MARKER.sub(sub, html)


def panel_html(redactie=False):
    reg = laad_register()
    bronnen = reg["bronnen"]
    rijklasse = "if-bron mg-deel" if redactie else "if-bron"
    rijen = []
    for b in bronnen:
        url = b.get("url")
        link = f'<a href="{_esc(url)}" target="_blank" rel="noopener">bron openen</a>' if url else "<span>geen URL</span>"
        datum = _esc(b.get("datum")) or "—"
        gc = _esc(b.get("gecontroleerd_op")) or "niet gecontroleerd"
        status = _esc(b.get("status") or "")
        rijen.append(
            f'<div class="{rijklasse}" id="bron-{b["id"]}">'
            f'<span class="kop">{b["id"]} · {_esc(b.get("instantie"))}</span> — '
            f'<span class="doc">{_esc(b.get("document"))}</span>'
            f'<div class="meta">datum {datum} · tier <span class="tier">{_esc(b.get("tier"))}</span>'
            f' · <span class="status">{status}</span> · gecontroleerd {gc} · {link}</div>'
            f'</div>'
        )
    peildatum = _esc(reg.get("peildatum"))
    body = (
        f'<div class="if-dossier-wrapper">'
        f'<style>{_STYLE}</style>'
        f'<details class="if-bronnen" open>'
        f'<summary>Bronnenregister ({len(bronnen)} bronnen · peildatum {peildatum})</summary>'
        f'<p class="toel">Elke gemarkeerde claim in de tekst verwijst met [Bxx] naar een regel hieronder. '
        f'Harde gegevens steunen uitsluitend op tier AAA of AA.</p>'
        + "".join(rijen) +
        f'</details></div>'
    )
    return body
