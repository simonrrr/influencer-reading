"""Build index.html from sources.py: python3 build.py"""
import html, os, re
from sources import SECTIONS

HERE = os.path.dirname(os.path.abspath(__file__))
PUNCT = re.compile(r"([.,;:?!()&’‘“”])")
KINDS = {"free": "free", "web": "free", "borrow": "borrow", "paywall": "paywall", "buy": "buy"}


def esc(s):
    return html.escape(s, quote=True)


def accent(s):
    """House style for display type: punctuation in the accent colour."""
    return "".join(f'<span class="p">{esc(t)}</span>' if PUNCT.fullmatch(t) else esc(t) for t in PUNCT.split(s) if t)


def md(s):
    """*italics* in citations."""
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", esc(s))


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("’", "")).strip("-")


nav, body, n = [], [], 0
for title, entries in SECTIONS:
    sid = slug(title.split(":")[0])
    nav.append(f'<a href="#{sid}">{esc(title.split(":")[0])}</a>')
    items = []
    for e in entries:
        n += 1
        kinds = sorted({KINDS[k] for k, _, _ in e["links"]})
        links = "".join(f'<a class="btn {k}" href="{esc(u)}" rel="noopener">{esc(label)}</a>' for k, label, u in e["links"])
        slides = "".join(f"<li>{esc(s)}</li>" for s in e["slides"])
        caveat = f'<p class="caveat"><b>Caveat</b> {md(e["caveat"])}</p>' if e.get("caveat") else ""
        items.append(f'''<article class="card" data-kinds="{' '.join(kinds)}">
  <p class="cite">{md(e["cite"])}</p>
  <ul class="slides" aria-label="On the slides">{slides}</ul>
  <p class="what">{md(e["what"])}</p>{caveat}
  <p class="links">{links}</p>
</article>''')
    body.append(f'<section id="{sid}"><h2>{accent(title)}</h2>\n<div class="list">\n' + "\n".join(items) + "\n</div></section>")

src = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
out = src.replace("<!--NAV-->", "\n".join(nav)).replace("<!--BODY-->", "\n".join(body)).replace("<!--N-->", str(n))
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(out)
print(n, "entries;", os.path.getsize(os.path.join(HERE, "index.html")) // 1024, "KB")
