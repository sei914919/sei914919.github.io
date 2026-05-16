# 画像準備ガイド

このサイトで使う写真は、**モノクローム × 雑誌的グリッド** を統一感の柱にしています。撮影〜配置までの手順をここにまとめます。

## ディレクトリの使い分け

```
assets/images/
├── hero/        # トップページのグリッドに並ぶ静物・風景
├── about/       # Aboutページのポートレート
├── projects/    # 各プロジェクトに添える1枚
└── blog/        # ブログ記事のヘッダ画像（記事ディレクトリに置いてもOK）
```

## 撮影時のメモ

モノクロにすることが前提なので、**色ではなく光と質感**を意識します。

- 順光より斜光（朝夕の窓際、デスクライト1灯）
- 機械式時計・眼鏡・コーヒー器具などは、金属の反射と影が画になる
- 風景は曇天やゴールデンアワーが扱いやすい
- 手前にしっかり余白をとる（テキストやキャプションが乗せられるように）
- スマホ縦撮りはトリミング前提で**少し広めに**撮っておく

## サイズ・フォーマット

| 用途 | 推奨サイズ（書き出し） | 形式 |
|------|----------------------|------|
| `hero/` | 1200 × 1200 px（正方形） | `.jpg` |
| `about/` ポートレート | 1200 × 1500 px（4:5縦） | `.jpg` |
| `projects/` | 1600 × 900 px（16:9横） | `.jpg` |
| `blog/` ヘッダ | 1600 × 900 px（16:9横） | `.jpg` |

JPEGの画質は **80–85%** で十分（Web表示で違いは出ない）。1枚 200–400 KB が目標。

## モノクローム変換ワークフロー

### A. 一括変換（ImageMagick）

ImageMagickをUbuntuに入れていれば、これ一発で揃います。

```bash
# 単発：1枚を彩度0・コントラスト微調整・サイズ整形
magick INPUT.jpg \
  -resize 1200x1200^ -gravity center -extent 1200x1200 \
  -colorspace Gray \
  -level 5%,95%,1.05 \
  -quality 85 \
  OUTPUT.jpg

# ディレクトリ一括（hero/ にあるカラー写真をモノクロに置換）
cd assets/images/hero
for f in *.jpg; do
  magick "$f" \
    -resize 1200x1200^ -gravity center -extent 1200x1200 \
    -colorspace Gray \
    -level 5%,95%,1.05 \
    -quality 85 \
    "_mono_$f"
  mv "_mono_$f" "$f"
done
```

`-level 5%,95%,1.05` は黒締めと軽いS字トーン。雑誌っぽい締まり方になります。**やりすぎな場合は `-level 8%,92%,1.0` 程度に緩めて**ください。

### B. RAW から処理する場合

Lightroom / darktable の場合は以下のプリセット相当を作っておくと早いです：

- White balance: そのまま（モノクロなので影響なし）
- Tone curve: わずかにS字
- Black point: -10 〜 -15
- White point: +5 〜 +10
- Texture: +10
- Clarity: +10
- Saturation: -100（モノクロ化）
- Grain: 軽く（強さ 15、サイズ 25 程度）— 雑誌の紙質感

### C. スマホで撮ったものを軽く処理

darktable や Snapseedの「ノワール」フィルタの **N02** が比較的素直なモノクロ。コントラストを微調整して書き出し → 上記Aの`magick`コマンドでサイズ整形だけかける、が手早いです。

## ファイル命名

検索性と並び順のために、以下の規則：

```
hero-01-coffee-grinder.jpg
hero-02-watch-detail.jpg
hero-03-bookshelf.jpg
hero-04-oxford-spires.jpg     # 旅先の写真も hero/ に入れてOK

about-portrait.jpg

projects-jade-server.jpg
projects-arca-terminal.jpg

blog-2026-05-05-migration-note.jpg
```

`hero/` の連番（01〜）は、**サイト上の表示順**に対応させます。 後述の `index.qmd` でこの順で参照しているため、並び順を変えるときはファイル名を付け替えるか、qmd側を直接編集してください。

## キャプション

トップページのグリッド画像には、`<figcaption>`相当のキャプションが入ります。テキストは `index.qmd` の hero セクションに直接書きます（画像メタデータからは読みません）。例：

```
01 / DESK
02 / TOOLS
03 / OXFORD
04 / SEMINAR
```

短い英大文字を `font-mono` で配置するのが Monocle 風です。

## ライセンス

写真の著作権はすべて宍戸聖が保持。サイトの公開リポジトリには通常通り画像も含めますが、**第三者の顔が写る写真は使わない**こと。講義・セミナーの写真は、できれば板書・教室の引き／無人時の机のショット中心に。
