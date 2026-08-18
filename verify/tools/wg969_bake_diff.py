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

用法：
    python verify/tools/wg969_bake_diff.py <side_dir> [--keys 欄1,欄2]
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


def diff_one(base_p, side_p, keys):
    """回 (變動格清單, 缺列, 多列)。變動格 ＝ (鍵, 欄, 舊, 新)。"""
    b, g = read_csv(base_p), read_csv(side_p)
    if not b:
        return [], [], []
    ks = keys or [list(b[0].keys())[0]]
    ks = [k for k in ks if k in b[0]] or [list(b[0].keys())[0]]
    bb = {keyof(r, ks): r for r in b}
    gg = {keyof(r, ks): r for r in g}
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

    n_cell = 0
    for rel in changed:
        bp, sp = os.path.join(BASELINES, rel), os.path.join(side, rel)
        cells, miss, extra = diff_one(bp, sp, keys)
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
