#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`W-G.9-69` **重烤捕捉之逐格 diff**（side dir vs `verify/baselines/`）⛔ 零生產碼

🔒 **為何要先捕捉再原地烤**（施工單 §三 B-2）：`WV_BAKE=verify/baselines` 係**原地覆寫**
  ⇒ 覆寫後**再也看不到舊值**。故先烤到**側目錄**、逐格 diff、**逐格歸因**，
  待「未歸因 ＝ 0」方得原地重烤（B-2-4 之停機條件掛在此不變式上）。

🔒 **量測框**：CSV 以 `utf-8-sig` 讀（`_bake_csv` 寫 BOM）；比對**逐欄逐列之字串**，
  ⛔ 不做任何數值正規化——本器之受詞是「**哪一格變了**」，⛔ 非「變得對不對」。

🔒 **列之對位**：以**該列全部鍵欄之值**為鍵（鍵欄 ＝ 由 `--keys` 給，或預設取第 1 欄）。
  ⛔ 不以列序對位——列序若變動，位置對位會把「同一列」誤報成兩格改動。

🩸 **`W-G.9-70` A-2 之修（⛔ 原缺陷具名）**：首版以 `{keyof(r): r for r in rows}` 建表
  ⇒ **同鍵後列靜默覆寫前列**。實測 `W-D.1.2 診斷_退縮0m.csv` **18 列**而以第 1 欄
  （`街廓`）為鍵只得 **6** 個相異鍵 ⇒ **12 列從未進入比對**；全 11 檔合計
  **117 列中 54 列被靜默覆寫（覆蓋率 53.8%）**。
  ⇒ 🔒 **現行為：同鍵重複即 `raise`**（訊息含**檔名／重複之鍵／該鍵之列數**），⛔ 不再靜默。
  🔒 **鍵欄取交集**：`--keys` 所給之欄若該檔沒有則略過該欄（⇒ 一組鍵可服務全部檔）；
     略過後若**仍有重複**，一樣 `raise`。

用法：
    python verify/tools/wg969_bake_diff.py <side_dir> [--keys 欄1,欄2]
    # `W-G.9-70` A-3 之真主鍵（實測 列數 ＝ 相異鍵數·11／11）：
    #     --keys 街廓,端,候選地號
"""
import csv
import hashlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
BASELINES = os.path.join(VERIFY, "baselines")


def read_csv(p):
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def sha(p, norm=False):
    """`norm=False` ＝ 原始位元組；`norm=True` ＝ **CRLF → LF 正規化後**。

    🔒 **量測框之聲明（`CLAUDE.md`：位元組數／校驗碼須聲明量測框）**：
      本機工作樹之 `verify/baselines/*.csv` 為 **CRLF**（checkout 轉換），
      而 `_bake_csv` 寫 **LF-only** ⇒ **原始 sha256 逐檔必不同**、該欄**⛔ 不可當內容差**。
      🩸 本器首版只有原始欄，致 `W-D.1.3-a` 二檔被誤報為「變」（實則逐列全文相同）。
      ⇒ 二欄**並列**（⛔ 不以正規化欄取代原始欄——行尾差本身也是事實，只是**非內容差**）。
    """
    h = hashlib.sha256()
    with open(p, "rb") as f:
        b = f.read()
    h.update(b.replace(b"\r\n", b"\n") if norm else b)
    return h.hexdigest()


def keyof(row, keys):
    return tuple(str(row.get(k, "")).strip() for k in keys)


def index_rows(rows, ks, where):
    """以 `ks` 建索引。🔴 **同鍵重複即 `raise`**（⛔ 不得靜默覆寫·`W-G.9-70` A-2-1）。"""
    out, dup = {}, {}
    for r in rows:
        k = keyof(r, ks)
        if k in out:
            dup.setdefault(k, 1)
            dup[k] += 1
        out[k] = r
    if dup:
        det = "；".join(f"鍵={'/'.join(k)} 共 {n} 列" for k, n in sorted(dup.items())[:5])
        raise RuntimeError(
            f"🔴 同鍵重複 ⇒ 比對會漏列（⛔ 禁靜默覆寫）：{where}｜鍵欄={ks}｜"
            f"列數={len(rows)}·相異鍵={len(out)}·被覆寫={len(rows) - len(out)} 列｜{det}"
            f"{'…' if len(dup) > 5 else ''}")
    return out


def diff_one(base_p, side_p, keys, rel=""):
    """回 (變動格清單, 缺列, 多列)。變動格 ＝ (鍵, 欄, 舊, 新)。"""
    b, g = read_csv(base_p), read_csv(side_p)
    if not b:
        return [], [], []
    ks = [k for k in (keys or []) if k in b[0]] or [list(b[0].keys())[0]]
    bb = index_rows(b, ks, f"{rel}（baseline）")
    gg = index_rows(g, ks, f"{rel}（side）")
    cells = []
    for k in bb:
        if k not in gg:
            continue
        for col in bb[k]:
            ov, nv = bb[k][col], gg[k].get(col)
            if ov != nv:
                cells.append((k, col, ov, nv))
    return cells, sorted(set(bb) - set(gg)), sorted(set(gg) - set(bb))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    side = sys.argv[1]
    keys = []
    if "--keys" in sys.argv:
        keys = sys.argv[sys.argv.index("--keys") + 1].split(",")

    rels = []
    for root, _d, files in os.walk(side):
        for fn in files:
            p = os.path.join(root, fn)
            rels.append(os.path.relpath(p, side).replace("\\", "/"))
    rels.sort()

    print("=" * 118)
    print("【`W-G.9-69`】重烤捕捉之逐格 diff（side dir vs `verify/baselines/`）")
    print("=" * 118)
    print(f"  side dir ＝ {side}")
    print(f"  烤出檔數 ＝ **{len(rels)}**")
    print("")
    print("  🔒 **逐檔 sha256 對照（施工單 §六 閘 8）**　⚠️ 量測框見 `sha()` docstring")
    print(f"  {'檔':<44}{'base(原始)':<12}{'side(原始)':<12}{'原始':<7}"
          f"{'base(CRLF→LF)':<16}{'side(CRLF→LF)':<16}{'正規化後':<10}")
    print("-" * 118)
    changed, same, missing = [], [], []
    for rel in rels:
        bp = os.path.join(BASELINES, rel)
        sp = os.path.join(side, rel)
        if not os.path.exists(bp):
            missing.append(rel)
            print(f"  {rel:<44}{'（baseline 無此檔）':<12}{sha(sp)[:10]:<12}{'🆕':<7}")
            continue
        hb, hg = sha(bp)[:10], sha(sp)[:10]
        nb, ng = sha(bp, True)[:14], sha(sp, True)[:14]
        (same if nb == ng else changed).append(rel)
        print(f"  {rel:<44}{hb:<12}{hg:<12}{('同' if hb == hg else '異'):<7}"
              f"{nb:<16}{ng:<16}{('同' if nb == ng else '🔴 變'):<10}")
    print("-" * 118)
    print(f"  ⇒ **（正規化後）變 {len(changed)} 檔／不變 {len(same)} 檔／"
          f"baseline 無 {len(missing)} 檔**（合計 {len(rels)}）")
    print("  🔒 **判「變／不變」一律取<u>正規化後</u>欄**——原始欄之差含**行尾**（工作樹 CRLF "
          "vs `_bake_csv` LF），⛔ 非內容差。")
    print("")

    # 🔒 **覆蓋率普查（`W-G.9-70` A-1·⛔ 全檔·⛔ 不抽樣）**：先證「每一列都進得了比對」
    print("  🔒 **覆蓋率普查**（列數／鍵欄／相異鍵數／被覆寫）——⛔ 被覆寫 > 0 者下方即 `raise`")
    t_rows = t_lost = 0
    for rel in rels:
        bp = os.path.join(BASELINES, rel)
        if not os.path.exists(bp):
            continue
        rows = read_csv(bp)
        if not rows:
            continue
        ks = [k for k in (keys or []) if k in rows[0]] or [list(rows[0].keys())[0]]
        d = len({keyof(r, ks) for r in rows})
        t_rows += len(rows)
        t_lost += len(rows) - d
        print(f"    {rel:<44}{len(rows):>5} 列　鍵={'＋'.join(ks):<18}"
              f"相異 {d:>4}　被覆寫 {len(rows) - d:>3}")
    print(f"  ⇒ **總列數 {t_rows}／被覆寫 {t_lost} 列**"
          f"（覆蓋率 {100.0 * (t_rows - t_lost) / t_rows:.1f}%）")
    print("")

    n_cell = 0
    for rel in changed:
        bp, sp = os.path.join(BASELINES, rel), os.path.join(side, rel)
        cells, miss, extra = diff_one(bp, sp, keys, rel)
        print("=" * 118)
        print(f"【{rel}】變動格 {len(cells)}　缺列 {len(miss)}　多列 {len(extra)}")
        print("-" * 118)
        for k, col, ov, nv in cells:
            n_cell += 1
            print(f"  鍵={'/'.join(k)}　欄「{col}」：baseline={ov!r} → side={nv!r}")
        for k in miss:
            print(f"  🔴 side 缺列：{'/'.join(k)}")
        for k in extra:
            print(f"  🔴 side 多列：{'/'.join(k)}")
    print("=" * 118)
    print(f"  **變動儲存格總數 ＝ {n_cell}**")
    print("=" * 118)
    return 0


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    sys.exit(main())
