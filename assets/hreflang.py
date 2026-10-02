# 日本語ページと /en/ 以下の英語ページが両方あるとき、互いを hreflang で結ぶ（Google に対訳関係を伝える）
import os
from pathlib import Path

SITE_URL = "https://sei914919.github.io"
out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))


def url(rel):
    p = "/" + rel.as_posix()
    return SITE_URL + (p[: -len("index.html")] if p.endswith("/index.html") else p)


for ja in out.rglob("*.html"):
    rel = ja.relative_to(out)
    if rel.parts[0] in ("en", "site_libs"):
        continue
    en = out / "en" / rel
    if not en.exists():
        continue
    tags = (
        f'<link rel="alternate" hreflang="ja" href="{url(rel)}">\n'
        f'<link rel="alternate" hreflang="en" href="{url(Path("en") / rel)}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{url(rel)}">\n'
    )
    for f in (ja, en):
        html = f.read_text(encoding="utf-8")
        if 'hreflang="ja"' in html:
            continue
        f.write_text(html.replace("</head>", tags + "</head>", 1), encoding="utf-8")
