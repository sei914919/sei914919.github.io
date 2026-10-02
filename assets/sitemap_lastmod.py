# sitemap.xml の lastmod を、ビルド時刻ではなく元ファイルの最終コミット日時にする
# 一覧ページ（listing）は、一覧の対象になっている記事の更新も含めて最新の日時をとる
import os
import re
import subprocess
from pathlib import Path

SITE_URL = "https://sei914919.github.io/"
out = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
sitemap = out / "sitemap.xml"


def last_commit(*paths):
    r = subprocess.run(["git", "log", "-1", "--format=%cI", "--", *map(str, paths)],
                       capture_output=True, text=True)
    return r.stdout.strip()


def source_of(url):
    rel = url[len(SITE_URL):]
    for cand in (re.sub(r"\.html$", ".qmd", rel), re.sub(r"\.html$", ".md", rel)):
        if Path(cand).exists():
            return Path(cand)
    return None


def listed_dirs(src):
    front = src.read_text(encoding="utf-8").split("\n---", 1)[0]
    if "listing:" not in front:
        return []
    return [os.path.normpath(src.parent / m) for m in re.findall(r"[\w./-]*posts\b", front)]


def lastmod(match):
    src = source_of(match.group(1))
    date = src and last_commit(src, *listed_dirs(src))
    return match.group(0) if not date else re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{date}</lastmod>", match.group(0))


if sitemap.exists():
    xml = sitemap.read_text(encoding="utf-8")
    sitemap.write_text(re.sub(r"<url>\s*<loc>([^<]+)</loc>.*?</url>", lastmod, xml, flags=re.S), encoding="utf-8")
