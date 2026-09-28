# sei-shishido.github.io

宍戸聖（成蹊大学法学部）の個人サイト。Quarto + GitHub Pages で構築。

## 構成

```
.
├── _quarto.yml             # サイト全体設定
├── index.qmd               # トップページ
├── about.qmd               # 自己紹介
├── publications/           # 研究業績
│   ├── index.qmd           # 業績一覧（blog/posts の work: true を表示）
│   └── references.bib      # BibTeX（任意）
├── projects/index.qmd      # ポートフォリオ
├── blog/
│   ├── index.qmd           # ブログ一覧
│   └── posts/              # 記事（1ディレクトリ＝1記事。業績もここ）
├── assets/                 # CSS / SCSS / favicon
└── .github/workflows/      # 自動デプロイ
```

## ローカルで動かす

```bash
# Quarto のインストール（Ubuntu）
wget https://quarto.org/download/latest/quarto-linux-amd64.deb
sudo dpkg -i quarto-linux-amd64.deb

# プレビュー
quarto preview         # ファイル保存ごとに自動再ビルド

# ビルドのみ
quarto render          # _site/ に出力
```

## 業績を追加する

業績も含め、すべてのコンテンツは `blog/posts/<slug>/index.qmd` の記事として管理する。
frontmatter に `work: true` を付けると Works ページとトップの Recent Works にも載る。

```yaml
---
title: "論文タイトル"
subtitle: "English title（任意）"
date: "2026-05-05"
work: true
type: "論説"
venue: "公正取引 no.900 pp.1–10"
external-url: https://example.com/article.pdf   # 任意。記事冒頭に「本文を読む」リンクが出る
categories: [論説]
---

（本文は任意。書誌情報は assets/work-meta.lua が記事冒頭に自動表示する）
```

`type` には `著書 / 論文（査読あり） / 論説 / 評釈 / 解説・紹介 / 報告 / 学位論文` を使用し、`categories` にも同じ値を入れる。

## ブログ記事を追加する

`blog/posts/<slug>/index.qmd` を作成して書くだけ。画像は同じディレクトリに置けば相対パスで参照可能。

## 公開

`main` に push すると GitHub Actions が自動でビルドして Pages にデプロイ。
