#!/usr/bin/env python3
"""Bouwt redactie/index.html uit hoofdstukken/*.md + redactie/_sjabloon.html.
Draaien vanuit de repo-root of vanuit redactie/: python3 redactie/_build.py"""
import re, glob, os, markdown

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = lambda *p: os.path.join(REPO, *p)

def svg_figuur(m):
    naam = m.group(1).strip()
    pad = H('svg', naam)
    if not os.path.exists(pad):
        return f'<div class="notitie">[schema ontbreekt: {naam}]</div>'
    svg = open(pad).read()
    bijschrift = ''
    for k in re.findall(r'<!--(.*?)-->', svg, re.S):
        m2 = re.search(r'Naar het oorspronkelijke schema[^\n]*', k)
        if m2:
            bijschrift = m2.group(0).strip(); break
    if not bijschrift:
        bijschrift = 'Schema: ' + naam.replace('.svg', '').split('-', 1)[1].replace('-', ' ')
    svg = re.sub(r'<\?xml.*?\?>', '', svg, flags=re.S)
    svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S)
    svg = re.sub(r'(<svg[^>]*?)\s(width|height)="[^"]*"', r'\1', svg, count=4)
    return f'<figure class="schema">{svg}<figcaption>{bijschrift}</figcaption></figure>'

def html_inline(m):
    naam = m.group(1).strip()
    pad = H('blokken', naam)
    if not os.path.exists(pad):
        return f'<div class="notitie">[blok ontbreekt: {naam}]</div>'
    return open(pad).read()

def vraagblok(m):
    binnen = re.sub(r'^NIET GEVERIFIEERD[ \u2014:\-]*', '', m.group(1)).strip() or 'zie de omringende tekst'
    binnen = binnen.replace('<', '&lt;')
    return (f'\n<div class="vraag"><span class="vraaglabel">Open punt</span>'
            f'Nog niet hard te maken uit de offici\u00eble stukken. Aanvulling of bronverwijzing welkom. '
            f'<em>({binnen})</em></div>\n')

def hoofdstuk_html(pad):
    nr = os.path.basename(pad)[1]
    t = open(pad).read()
    m = re.search(r'^# (.+)$', t, re.M)
    titel = re.sub(r'^Hoofdstuk \d+ \u2014 ', '', m.group(1)) if m else pad
    t = re.sub(r'^# .+$', '', t, count=1, flags=re.M)
    t = re.sub(r'<!-- (anker|Sjabloon|Verificatiebasis|tijdgevoelig)[^>]*-->', '', t)
    t = re.sub(r'<!-- ABONNEE-BLOK:.*?-->',
               '\n<div class="notitie">Hier komt online een rekenhulp voor abonnees \u2014 niets om na te kijken.</div>\n',
               t, flags=re.S)
    t = re.sub(r'\[(NIET GEVERIFIEERD[^\]]*)\]', vraagblok, t)
    body = markdown.markdown(t, extensions=['tables'])
    body = re.sub(r'<!--\s*SVG-INLINE:\s*([^>]+?)\s*-->', svg_figuur, body)
    body = re.sub(r'<!--\s*HTML-INLINE:\s*([^>]+?)\s*-->', html_inline, body)
    # gele kaarten: naam hoort in het blok (redactieregel Anton 05-07-2026)
    body = re.sub(
        r'(<!--\s*ROB\s*-->\s*)?<blockquote>(.*?)</blockquote>(\s*<!--\s*/?ROB\s*-->)?',
        lambda m: (f'<figure class="rob"><figcaption>Rob van der Meulen \u00b7 brontekst, letterlijk overgenomen</figcaption>'
                   f'<blockquote>{m.group(2)}</blockquote></figure>'
                   if (m.group(1) or m.group(3) or '<!-- ROB -->' in m.group(2))
                   else f'<blockquote>{m.group(2)}</blockquote>'),
        body, flags=re.S)
    body = body.replace('<!-- ROB -->', '').replace('<!-- /ROB -->', '')
    body = body.replace('<table>', '<div class="tabelwrap"><table>').replace('</table>', '</table></div>')
    return nr, titel, body

def main():
    secties = [hoofdstuk_html(f) for f in sorted(glob.glob(H('hoofdstukken', 'h*.md')))]
    inhoud = ''.join(f'<section id="h{nr}"><p class="eyebrow">Hoofdstuk {nr}</p><h1>{titel}</h1>{body}</section>'
                     for nr, titel, body in secties)
    sj = open(H('redactie', '_sjabloon.html')).read()
    uit = sj.replace('{{INHOUD}}', inhoud)
    open(H('redactie', 'index.html'), 'w').write(uit)
    print(f'OK: index.html {len(uit)//1024} kB; {uit.count("<svg")} svg; '
          f'{uit.count("figure class=\"rob\"")} gele kaarten; {uit.count("tabelwrap")//2} tabellen gewrapt; '
          f'{uit.count("class=\"vraag\"")} open punten')

if __name__ == '__main__':
    main()
