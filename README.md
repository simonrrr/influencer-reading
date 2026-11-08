# Further reading

Everything the slides of *Context Engineering: Human-to-Human Edition* cite, what each source says, and where to read it: a free copy if there is one, otherwise a library loan on archive.org, otherwise the publisher or an amazon.de search.

`index.html` is the whole page: static, no build step needed to host it.

To change an entry, edit `sources.py` (the text and links) or `template.html` (the look), then:

```
python3 build.py
```

Link kinds in `sources.py`:
- `free(url)`: open-access copy (PubMed Central, a university repository, the author's site, arXiv) or a free web page
- `ia(identifier)`: archive.org lending library (free account; checked that the item is in `inlibrary`, not only `printdisabled`)
- `doi(doi)`: publisher page, usually paywalled
- `amazon(query)`: an amazon.de search, not an affiliate link

## Hosting on GitHub Pages

As for `nur-einfache-woerter`: create a public repository (e.g. `influencer-reading`), upload `index.html`, then Settings → Pages → Deploy from a branch → `main` / root. It appears at `https://simonrrr.github.io/influencer-reading/`.

Links checked 8 November 2026. Publishers (APA, Wiley, Sage, Science) block scripted checks, so their DOI links were checked to resolve, not to load.
