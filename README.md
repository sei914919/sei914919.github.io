# sei-shishido.github.io

宍戸聖（成蹊大学法学部）の個人サイト。Quarto + GitHub Pages で構築。

## 構成

```
.
├── _quarto.yml             # サイト全体設定
├── index.qmd               # トップページ
├── about.qmd               # 自己紹介
├── publications/           # 研究業績
│   ├── index.qmd           # 業績一覧
│   ├── items/              # 業績エントリ（1ファイル＝1業績）
│   └── references.bib      # BibTeX（任意）
├── projects/index.qmd      # ポートフォリオ
├── blog/
│   ├── index.qmd           # ブログ一覧
│   └── posts/              # 記事（1ディレクトリ＝1記事）
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

`publications/items/YYYY-MM-DD-slug.qmd` を新規作成し、frontmatter のみ書く：

```yaml
---
title: "論文タイトル"
date: "2026-05-05"
type: "論説"
venue: "公正取引"
categories: [論説]
external-url: https://example.com/article-pdf
---
```

`type` には `論説 / 評釈 / 報告 / 文献紹介 / 解説 / コラム` を使用。

## ブログ記事を追加する

`blog/posts/<slug>/index.qmd` を作成して書くだけ。画像は同じディレクトリに置けば相対パスで参照可能。

## 公開

`main` に push すると GitHub Actions が自動でビルドして Pages にデプロイ。
