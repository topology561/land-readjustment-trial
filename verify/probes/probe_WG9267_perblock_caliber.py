# -*- coding: utf-8 -*-
"""W-G.9-267 工項三：**逐街廓獨立口徑**（口徑乙）vs **全區連跑**（口徑甲）之逐格對拍。唯讀探針。

🔒 唯讀：⛔ 動 `app.py` 與 `verify/` 生產路徑一字；⛔ 寫入任何 tracked 檔。

【受詞】`SB = 3.5m`；口徑甲 ＝ `run_verification` 之全區連跑落檔
  `verify/out/got_G值_退縮3.5m_partial.csv`（**獨立行程**）；
  口徑乙 ＝ 本探針於**全新行程**逐街廓獨立呼叫 `run_step_g`（承 `probe_D2b22_attrib.py` 之形·⛔ 新造）。

【驗收綁性質】「二口徑於**皆可產出**之街廓，其逐宗逐欄值**相同**」，
  ⛔ 綁「相異格數 ＝ 0」此一計數 ⇒ **逐格出艙**。

【比較欄（自擬·逐字列出）】
  `G(㎡)`／`W(m)`／`累積S(m)`／`幾何面積(㎡)`／`街角地`／`第1筆街角`／`推進側別`
  數值正規化 ＝ `'%.6f'`；非數值欄取 `str(...).strip()`。

【否證對照（同格載判定集基數）】
  必紅 ＝ 任取一宗之 `G` 人造 `+1` 後對拍須偵得相異（基數 1）；
  必綠 ＝ CSV **自比**逐格相同（基數 ＝ 共有宗數）。基數 `0` ⇒ **loud 拒測**。

【停機款（單 `§四`）】任一**非首街廓**相異格 `≥ 1` ⇒ **停機上呈**（蘊含跨街廓相依·可能有土地後果）。

【射程界（照實）】`R3` 於口徑甲**結構上不可達**（全區連跑止於 `R5`）⇒ 其值**⛔ 有第二來源**
  ⇒ 一律標「**單源·歸納支持**」，**⛔ 已證**。
"""
import contextlib
import csv
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUT = os.path.join(VERIFY, "out")
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

SB = 3.5
TAG = "3.5m"
CSVP = os.path.join(OUT, "got_G值_退縮%s_partial.csv" % TAG)
COLS = ["G(㎡)", "W(m)", "累積S(m)", "幾何面積(㎡)", "街角地", "第1筆街角", "推進側別"]
NUMC = {"G(㎡)", "W(m)", "累積S(m)", "幾何面積(㎡)"}


def norm(col, v):
    s = "" if v is None else str(v).strip()
    if col in NUMC:
        try:
            return "%.6f" % float(s)
        except (TypeError, ValueError):
            return s
    return s


def key_of(r):
    return (str(r.get("所屬街廓", "")).strip(), str(r.get("暫編地號", "")).strip())


def load_csv():
    if not os.path.exists(CSVP):
        return None
    with io.open(CSVP, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def cmp_tables(A, B, label_a, label_b):
    """回傳 (共有鍵序, 逐格結果 list[(key,col,va,vb,same)], 相異數)。"""
    ka = {key_of(r): r for r in A}
    kb = {key_of(r): r for r in B}
    common = sorted(set(ka) & set(kb))
    cells, diff = [], 0
    for k in common:
        for c in COLS:
            va, vb = norm(c, ka[k].get(c)), norm(c, kb[k].get(c))
            same = (va == vb)
            if not same:
                diff += 1
            cells.append((k, c, va, vb, same))
    return common, cells, diff


def main():
    import run_verification as rv
    from app_harvest import harvest
    from stepg_pipeline import run_step_g
    from selection_pipeline import run_corner_pk

    print("=" * 116)
    print("【W-G.9-267 工項三】逐街廓獨立口徑（乙）vs 全區連跑（甲）之逐格對拍　SB ＝ %s" % TAG)
    print("=" * 116)

    gia = load_csv()
    if gia is None:
        print("🔴 **loud 拒測**：口徑甲之落檔不存在 ⇒ %s" % CSVP)
        return 6
    print("   口徑甲 ＝ %s（**獨立行程**·`run_verification` 所產）｜%d 列" % (CSVP, len(gia)))

    # ── 口徑乙：全新行程內逐街廓獨立呼叫 run_step_g ──
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        l = tp.get("所屬街廓")
        if l and l not in blks:
            blks.append(l)
    print("   口徑乙 ＝ 本探針（**全新行程**）逐街廓獨立呼叫 `run_step_g`｜街廓處理序 ＝ %s" % blks)

    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB, snapshot=snapshot)

    gib, per_blk = [], {}
    for lbl in blks:
        rows, note = [], ""
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                sg = run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                wins, forced, SB, eff_min_build_by_blk={})
            g_tab, _dg, _sl = rv.build_step_g_tables(sg) if hasattr(rv, "build_step_g_tables") \
                else (sg.get("g_rows", []), None, None)
            rows = [r for r in g_tab if str(r.get("所屬街廓", "")).strip() == lbl]
            note = "正常回傳"
        except RuntimeError as e:
            pt = getattr(e, "partial", None)
            if pt is None:
                note = "🔴 例外未帶 partial：%s" % str(e)[:80]
            else:
                rows = [r for r in (pt.get("g_rows") or [])
                        if str(r.get("所屬街廓", "")).strip() == lbl]
                note = "中止（%s）⇒ 取 e.partial｜%s" % (pt.get("aborted_blk"), str(e)[:70])
        per_blk[lbl] = (len(rows), note)
        gib.extend(rows)
        print("     [%s] %-4s 產出 %2d 列｜%s" % (TAG, lbl, len(rows), note))

    # ── 逐格對拍 ──
    common, cells, diff = cmp_tables(gia, gib, "甲", "乙")
    print()
    print("── 逐格對拍（母體 ＝ 二口徑**共有**之宗；比較欄 %d 欄·逐字 ＝ %s）──"
          % (len(COLS), "／".join("`%s`" % c for c in COLS)))
    byblk = {}
    for (k, c, va, vb, same) in cells:
        b = k[0]
        d = byblk.setdefault(b, [0, 0])
        d[0] += 1
        if not same:
            d[1] += 1
    first = blks[0] if blks else None
    print("| 街廓 | 共有宗 | 逐格 | 相異 | 鑑別力 |")
    print("|---|---|---|---|---|")
    tot_c = tot_n = tot_d = 0
    nonfirst_diff = 0
    for b in sorted(byblk, key=lambda x: blks.index(x) if x in blks else 99):
        n = len({k for (k, _c, _a, _b2, _s) in cells if k[0] == b})
        c_, d_ = byblk[b]
        tot_c += c_
        tot_n += n
        tot_d += d_
        if b != first:
            nonfirst_diff += d_
        print("| %s | %d | %d | **%d** | %s |"
              % (b, n, c_, d_, "首街廓·⛔ 鑑別力" if b == first else "**非首·具鑑別力**"))
    print("| **合計** | **%d** | **%d** | **%d** | 判定集基數 %d |" % (tot_n, tot_c, tot_d, tot_n))

    print()
    print("── 逐格出艙（單 `(b)` 明令·⛔ 只給計數）──")
    for (k, c, va, vb, same) in cells:
        print("   %-4s %-14s %-12s 甲 %-14s 乙 %-14s %s"
              % (k[0], k[1], c, va, vb, "＝" if same else "🔴 **≠**"))

    # ── 否證對照 ──
    print()
    print("── 否證對照（同格載判定集基數·基數 `0` ⇒ loud 拒測）──")
    rc = 0
    if tot_n == 0:
        print("   🔴 共有宗 ＝ 0 ⇒ **loud 拒測**")
        return 7
    _c2, _cells2, d_self = cmp_tables(gia, [dict(r) for r in gia], "甲", "甲")
    print("   ✅ 必綠 ＝ 口徑甲 CSV **自比**　判定集基數 **%d**　相異格 **%d**（須 0）⇒ %s"
          % (len(_c2), d_self, "如預期" if d_self == 0 else "🔴 器紅"))
    if d_self != 0:
        rc = 8
    inj = [dict(r) for r in gib]
    tgt = None
    for r in inj:
        if str(r.get("G(㎡)", "")).strip():
            try:
                r["G(㎡)"] = float(r["G(㎡)"]) + 1.0
                tgt = key_of(r)
                break
            except (TypeError, ValueError):
                continue
    if tgt is None:
        print("   🔴 必紅 ＝ 人造 `G +1`：**判定集基數 0 ⇒ loud 拒測**")
        rc = 9
    else:
        _c3, _cells3, d_inj = cmp_tables(gia, inj, "甲", "乙+1")
        print("   %s 必紅 ＝ 一宗之 `G` 人造 `+1`（受詞 %s）　判定集基數 **1**　相異格 **%d**（須 ≥1）⇒ %s"
              % ("✅" if d_inj >= 1 else "🔴", tgt, d_inj, "如預期" if d_inj >= 1 else "**器紅**"))
        if d_inj < 1:
            rc = 10

    # ── 射程界 ＋ 停機款 ──
    print()
    only_b = sorted({key_of(r) for r in gib} - {key_of(r) for r in gia})
    print("── 射程界（照實·⛔ 頂替）──")
    print("   口徑乙獨有之宗（口徑甲**結構上不可達**）＝ **%d** 宗" % len(only_b))
    kb = {key_of(r): r for r in gib}
    for k in only_b:
        vals = "／".join("%s=%s" % (c, norm(c, kb[k].get(c))) for c in COLS)
        print("     %s %s　🔒 **單源·歸納支持**（⛔ 已證·⛔ 有第二來源可對拍）｜%s" % (k[0], k[1], vals))
    print()
    print("── 停機款（單 `§四`）──")
    print("   非首街廓（首 ＝ `%s`）之相異格合計 ＝ **%d**　⇒ %s"
          % (first, nonfirst_diff,
             "✅ 未觸發" if nonfirst_diff == 0 else "🛑 **觸發 ⇒ 停機上呈**"))
    if nonfirst_diff:
        rc = 11
    return rc


if __name__ == "__main__":
    sys.exit(main())
