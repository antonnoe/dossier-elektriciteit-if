#!/usr/bin/env python3
"""Assemblage dossier-elektriciteit.html uit /hoofdstukken/*.md + /svg/*.svg.

Eenvoudige, doelgerichte markdown->HTML-conversie (alleen de constructies die
in de hoofdstukken voorkomen): koppen, tabellen, lijsten, blockquotes,
bold/italic, HTML-commentaren (blijven staan), SVG-INLINE-markers.
"""
import re, html, sys
from pathlib import Path

REPO = Path(str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(REPO))
import bronnen_render  # gedeelde presentatie van het bronnenregister
HFDST = [f"h{i}.md" for i in range(10)]

CHAPTER_META = {
    "h0": ("inleiding", "0 · Inleiding: veilig klussen"),
    "h1": ("aansluiting", "1 · Aansluiting, meter en contract"),
    "h2": ("hoofdschakelaar", "2 · De hoofdschakelaar"),
    "h3": ("groepenkast", "3 · De groepenkast"),
    "h4": ("aarding", "4 · De aarding"),
    "h5": ("leidingaanleg", "5 · De leidingaanleg"),
    "h6": ("schakelingen", "6 · Schakelingen en eisen per kamer"),
    "h7": ("zwaar-verbruik", "7 · Warmtepomp, EV en boiler"),
    "h8": ("normen-keuring", "8 · Normen, keuring en papierwerk"),
    "h9": ("naslag", "9 · Naslag en woordenlijst"),
}

def inline_fmt(s: str) -> str:
    # bewaar bestaande HTML-commentaren
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*]+?)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    return s

def md_to_html(md: str, chap: str) -> str:
    lines = md.splitlines()
    out, i = [], 0
    in_table, in_ul, in_bq = False, False, False
    bq_buf = []

    def close_lists():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>"); in_ul = False

    def close_table():
        nonlocal in_table
        if in_table:
            out.append("</tbody></table></div>"); in_table = False

    def flush_bq():
        nonlocal in_bq, bq_buf
        if in_bq:
            inner = "".join(f"<p>{p}</p>" for p in bq_buf if p.strip())
            out.append(f'<blockquote>{inner}</blockquote>')
            bq_buf, in_bq = [], False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # SVG inline marker
        m = re.match(r"<!--\s*SVG-INLINE:\s*(\S+)\s*-->", stripped)
        if m:
            flush_bq(); close_lists(); close_table()
            svgfile = REPO / "svg" / m.group(1)
            if svgfile.exists():
                svg = svgfile.read_text()
                # strip de commentaarkop niet: verificatie-info mag mee (onzichtbaar)
                out.append(f'<figure class="de-svg">{svg}</figure>')
            else:
                out.append(f"<!-- ONTBREKENDE SVG: {m.group(1)} -->")
            i += 1; continue

        # HTML-fragment inline marker (los blok uit /blokken/, verbatim doorgegeven)
        m = re.match(r"<!--\s*HTML-INLINE:\s*(\S+)\s*-->", stripped)
        if m:
            flush_bq(); close_lists(); close_table()
            frag = REPO / "blokken" / m.group(1)
            if frag.exists():
                out.append(frag.read_text())
            else:
                out.append(f"<!-- ONTBREKEND BLOK: {m.group(1)} -->")
            i += 1; continue

        # anker-commentaar overslaan (id zit al op de section)
        if re.match(r"<!--\s*anker:", stripped):
            i += 1; continue

        # overige commentaren (ROB, ABONNEE-BLOK, LINK) intact doorgeven
        if stripped.startswith("<!--"):
            flush_bq()
            out.append(stripped)
            i += 1; continue

        if stripped.startswith("# "):
            flush_bq(); close_lists(); close_table()
            out.append(f"<h2>{inline_fmt(stripped[2:])}</h2>")
        elif stripped.startswith("## "):
            flush_bq(); close_lists(); close_table()
            out.append(f"<h3>{inline_fmt(stripped[3:])}</h3>")
        elif stripped.startswith("### "):
            flush_bq(); close_lists(); close_table()
            out.append(f"<h4>{inline_fmt(stripped[4:])}</h4>")
        elif stripped.startswith(">"):
            close_lists(); close_table()
            in_bq = True
            content = stripped[1:].strip()
            if content:
                bq_buf.append(inline_fmt(content))
            else:
                bq_buf.append("")
        elif stripped.startswith("|"):
            flush_bq(); close_lists()
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if re.match(r"^\|[\s\-:|]+\|$", stripped.replace(" ", "")):
                i += 1; continue
            if not in_table:
                out.append('<div class="de-tabelwrap"><table><thead><tr>' +
                           "".join(f"<th>{inline_fmt(c)}</th>" for c in cells) +
                           "</tr></thead><tbody>")
                in_table = True
            else:
                out.append("<tr>" + "".join(f"<td>{inline_fmt(c)}</td>" for c in cells) + "</tr>")
        elif stripped.startswith("- "):
            flush_bq(); close_table()
            if not in_ul:
                out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline_fmt(stripped[2:])}</li>")
        elif re.match(r"^\d+\.\s", stripped):
            flush_bq(); close_table()
            if not in_ul:
                out.append("<ul>"); in_ul = True
            item = re.sub(r"^\d+\.\s*", "", stripped)
            out.append(f"<li>{inline_fmt(item)}</li>")
        elif stripped == "":
            flush_bq(); close_lists(); close_table()
        else:
            flush_bq(); close_lists(); close_table()
            if stripped.startswith("*") and stripped.endswith("*") and stripped.count("*") == 2:
                out.append(f'<p class="de-intro">{inline_fmt(stripped.strip("*"))}</p>')
            else:
                out.append(f"<p>{inline_fmt(stripped)}</p>")
        i += 1

    flush_bq(); close_lists(); close_table()
    return "\n".join(out)


CSS = """
#dossier-elektriciteit{font-family:Mulish,sans-serif;line-height:1.8em;color:#222;max-width:100%;}
#dossier-elektriciteit h2{font-family:Poppins,sans-serif;color:#800000;font-size:1.9em;line-height:1.3em;margin:1.6em 0 .6em;padding-top:.4em;border-top:3px solid rgba(128,0,0,0.80);}
#dossier-elektriciteit h3{font-family:Poppins,sans-serif;color:#800000;font-size:1.35em;line-height:1.35em;margin:1.4em 0 .5em;}
#dossier-elektriciteit h4{font-family:Poppins,sans-serif;color:#5a0000;font-size:1.1em;margin:1.2em 0 .4em;}
#dossier-elektriciteit p{margin:0 0 1em;}
#dossier-elektriciteit .de-intro{font-style:italic;color:#555;}
#dossier-elektriciteit blockquote{margin:1.4em 0;padding:1em 1.4em;background:rgba(128,0,0,0.04);border-left:4px solid rgba(128,0,0,0.80);font-style:normal;}
#dossier-elektriciteit blockquote p{margin:0 0 .7em;}
#dossier-elektriciteit blockquote p:last-child{margin-bottom:0;}
#dossier-elektriciteit .de-tabelwrap{overflow-x:auto;margin:1.2em 0;}
#dossier-elektriciteit table{border-collapse:collapse;width:100%;font-size:.95em;line-height:1.5em;}
#dossier-elektriciteit th{font-family:Poppins,sans-serif;background:rgba(128,0,0,0.08);color:#5a0000;text-align:left;padding:.55em .8em;border:1px solid rgba(128,0,0,0.20);}
#dossier-elektriciteit td{padding:.55em .8em;border:1px solid rgba(128,0,0,0.15);vertical-align:top;}
#dossier-elektriciteit tr:nth-child(even) td{background:rgba(128,0,0,0.03);}
#dossier-elektriciteit ul{margin:0 0 1em 1.2em;padding:0;}
#dossier-elektriciteit li{margin:.3em 0;}
#dossier-elektriciteit code{background:rgba(128,0,0,0.06);padding:.1em .35em;border-radius:3px;font-size:.9em;}
#dossier-elektriciteit .de-svg{margin:1.6em 0;padding:1em;background:rgba(128,0,0,0.03);border:1px solid rgba(128,0,0,0.12);border-radius:6px;}
#dossier-elektriciteit .de-svg svg{width:100%;height:auto;display:block;}
#dossier-elektriciteit .de-nav{background:rgba(128,0,0,0.05);border:1px solid rgba(128,0,0,0.20);border-radius:6px;padding:1.2em 1.4em;margin:0 0 2em;}
#dossier-elektriciteit .de-nav strong{font-family:Poppins,sans-serif;color:#800000;display:block;margin-bottom:.5em;}
#dossier-elektriciteit .de-nav a{display:inline-block;margin:.15em .9em .15em 0;color:#800000;text-decoration:none;border-bottom:1px solid rgba(128,0,0,0.35);font-size:.95em;}
#dossier-elektriciteit .de-nav a:hover{border-bottom-color:#800000;}
#dossier-elektriciteit .de-top{font-size:.85em;margin:1.5em 0 0;}
#dossier-elektriciteit .de-top a{color:#800000;text-decoration:none;}
#dossier-elektriciteit .de-colofon{margin-top:2.5em;padding:1.2em 1.4em;background:rgba(128,0,0,0.04);border:1px solid rgba(128,0,0,0.15);border-radius:6px;font-size:.95em;}
""".strip()


def main():
    parts = []
    parts.append('<div id="dossier-elektriciteit">')
    parts.append(f"<style>{CSS}</style>")
    parts.append('<h1 style="font-family:Poppins,sans-serif;color:#800000;line-height:1.25em;">De Franse elektrische installatie</h1>')
    parts.append('<p class="de-intro">Het complete handboek voor huiseigenaren en klussers — gebaseerd op de serie van Rob van der Meulen (2008–2017), geverifieerd en geactualiseerd naar de NF C 15-100-serie van 2024.</p>')
    nav = ['<nav class="de-nav"><strong>In dit dossier</strong>']
    for h in HFDST:
        key = h[:-3]
        anchor, label = CHAPTER_META[key]
        nav.append(f'<a href="#{anchor}">{label}</a>')
    nav.append("</nav>")
    parts.append("".join(nav))

    for h in HFDST:
        key = h[:-3]
        anchor, label = CHAPTER_META[key]
        md = (REPO / "hoofdstukken" / h).read_text()
        body = md_to_html(md, key)
        parts.append(f'<section id="{anchor}">')
        parts.append(body)
        if key == "h1":
            # bronnenoverzicht onder aan het hoofdstuk (voorlopig alleen H1)
            parts.append(bronnen_render.panel_html(redactie=False))
        parts.append(f'<p class="de-top"><a href="#dossier-elektriciteit">&uarr; naar boven</a></p>')
        parts.append("</section>")

    parts.append("</div>")
    html_out = "\n".join(parts)
    html_out = bronnen_render.vervang_markers(html_out)  # {{bron:Bxx}} -> klikbare markers
    dest = REPO / "dossier" / "dossier-elektriciteit.html"
    dest.write_text(html_out)
    # sanity checks
    n_svg = html_out.count("<svg")
    n_ext = len(re.findall(r'(src|href)="https?://(?!infofrankrijk)', html_out))
    picr = "picr" in html_out
    print(f"OK: {dest} — {len(html_out)} tekens, {n_svg} inline svg's, externe verwijzingen: {n_ext}, picr: {picr}")

if __name__ == "__main__":
    main()
