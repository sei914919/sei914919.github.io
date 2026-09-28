-- 業績記事（work: true）の本文冒頭に、種別・掲載先・本文リンクを表示する。
-- 書誌情報は frontmatter だけで管理し、本文に重複して書かなくてよいようにする。
local function str(v)
  return v and pandoc.utils.stringify(v) or ""
end

function Pandoc(doc)
  local m = doc.meta
  if not m.work then return doc end
  local parts = {}
  local function add(inlines)
    if #parts > 0 then table.insert(parts, pandoc.Str(" · ")) end
    for _, i in ipairs(inlines) do table.insert(parts, i) end
  end
  if str(m.type) ~= "" then add({ pandoc.Span(str(m.type), { class = "work-type" }) }) end
  if str(m.venue) ~= "" then add({ pandoc.Str(str(m.venue)) }) end
  if str(m.isbn) ~= "" then add({ pandoc.Str("ISBN " .. str(m.isbn)) }) end
  if str(m["external-url"]) ~= "" then
    add({ pandoc.Link("本文を読む ↗", str(m["external-url"])) })
  end
  if #parts > 0 then
    table.insert(doc.blocks, 1, pandoc.Div(pandoc.Para(parts), { class = "work-meta" }))
  end
  return doc
end
