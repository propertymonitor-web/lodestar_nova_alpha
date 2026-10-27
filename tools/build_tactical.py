#!/usr/bin/env python3
"""Make docs/tactical.html (ORION TACTICAL DASHBOARD) from docs/index.html: no pet, no tank, tactical skin, status strip, radar."""
import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
t = root / "tools" / "tactical"
h = (root / "docs" / "index.html").read_text(encoding="utf-8")
h = re.sub(r'<script id="tank-js">.*?</script>\n?', '', h, flags=re.S)
h = re.sub(r'<style id="tank-css">.*?</style>\n?', '', h, flags=re.S)
h = re.sub(r'<!--TANK-HTML-BEGIN-->.*?<!--TANK-HTML-END-->\n?', '', h, flags=re.S)
def sub1(a, b):
    global h
    if h.count(a) != 1: sys.exit("expected exactly one: " + a[:60])
    h = h.replace(a, b)
sub1("<title>LODESTAR NOVA dashboard</title>", "<title>ORION TACTICAL DASHBOARD</title>")
sub1('<h1 class="brand">LODESTAR NOVA<small>companion dashboard</small></h1>', '<h1 class="brand">LODESTAR ORION<small>tactical dashboard</small></h1>')
sub1('document.title = "LODESTAR ORION dashboard"; document.querySelector(".brand").innerHTML = "LODESTAR ORION<small>wardriving dashboard</small>";', 'document.title = "ORION TACTICAL DASHBOARD";')
sub1('<button id="btnPet" aria-label="Go to the pet screen">Pet</button>', '<button id="btnPet" aria-label="Go to the pet screen" hidden>Pet</button><a class="btn stdbtn" id="stdBtn" href="index.html" title="Go back to the standard dashboard (pet or shark tank)">Standard dashboard</a>')
sub1('<p id="notice" hidden></p>', '<p id="notice" hidden></p>' + (t / "tactical.html").read_text(encoding="utf-8"))
sub1('<html lang="en">', '<html lang="en" data-theme="dark">') if '<html lang="en">' in h else None
h = h.replace('</head>', '<style id="tactical-css">' + (t / "tactical.css").read_text(encoding="utf-8") + '</style>\n</head>', 1)
i = h.rindex('</body>')
h = h[:i] + '<script id="tactical-js">' + (t / "tactical.js").read_text(encoding="utf-8") + '</script>\n' + h[i:]
(root / "docs" / "tactical.html").write_text(h, encoding="utf-8"); print("docs/tactical.html", len(h))
