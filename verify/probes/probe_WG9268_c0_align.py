# -*- coding: utf-8 -*-
"""W-G.9-268 `c0`：受詞母體之對位（`A` ＝ `K-9-9 二` 不交叉之違反宗集／`B` ＝ 覆蓋帳違反組之逐重疊對）。唯讀探針。

🔒 唯讀：⛔ 動 `app.py` 與 `verify/` 生產路徑一字；⛔ 寫入任何 tracked 檔。

【`A` 之權威源（⛔ 另造第二份判準·同源聲明）】
  `verify/probes/probe_WG988_nocross.py`（`GB-67` 就地加註 `W-G.9-88` 所裁之**權威源**）
  ——本檔**⛔ 重判不交叉**，只**沿用其結論**（違反 ＝ `R2 左 序1` ／ `R5 左 序1`）
  並補其**⛔ 出艙之暫編地號**（該探針之 `暫編地號` 命中 ＝ `0`）。
  🔴 其**情境母體 ＝ 僅 `0m`**（該探針逐字自載）且其驅動為
  **逐街廓獨立呼叫** `run_step_g`（`for lbl in blks: … except Exception: pass`）。

【`B` 之來源】
  `verify/out/got_G值_退縮{0m,3.5m}_partial.csv`（**全區連跑**·`run_verification` 所產）
  ——與 `verify/probes/probe_WG9265_coverage_account.py` **同一母體、同一判準**
  （`Σarea − area(∪) > 1e-6`；逐對 ＝ `宗ᵢ ∩ 宗ⱼ` 之面積）。

【🔴 二母體之口徑相異（本檔之核心出艙）】
  `A` ＝ **逐街廓獨立呼叫**·**僅 `0m`**；`B` ＝ **全區連跑**·`0m`（止於 `R2`）＋ `3.5m`（止於 `R5`）。
  ⇒ `0m·R5` 於 `B` 之口徑下**結構上不存在** ⇒ 二者**⛔ 得逕取交集**，須先具名其口徑。

【自我驗證閘（`探針還原內部幾何須設自我驗證閘` 所令）】
  本檔以**逐街廓獨立·`0m`** 重建之 `R2 左 序1`／`R5 左 序1`，其**面積**須復現權威源所印之
  `3.8082`／`0.9867 ㎡`（容差 ＝ `±0.05 ㎡`·`GB-101` KL 裁 `2026-09-10` 之跨環境容差；
  本檔為**同主機**故另報其全精度差）。**閘不過 ⇒ ⛔ 得據以下任何結論。**

【否證對照（同格載判定集基數·基數 `0` ⇒ loud 拒測）】
  必綠 ＝ `0m·R2·left` 之 `序1` 於**二口徑**（逐街廓獨立 vs 全區連跑落檔）須為**同一暫編地號**；
  必紅 ＝ 人造把 `A` 之一宗改名 ⇒ `A ∩ B` 須改變。
"""
import ast
import contextlib
import csv
import io
import itertools
import os
import sys

from shapely.geometry import Polygon

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUT = os.path.join(VERIFY, "out")
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

# 🔒 權威源之結論（`probe_WG988_nocross.py` 之「必答 1」逐字·⛔ 本檔重判）
A_AUTH = [("R2", "left", 1, 3.8082), ("R5", "left", 1, 0.9867)]
A_SUM = 4.7950
TOL_AREA = 0.05          # GB-101（KL 裁 2026-09-10）之跨環境容差；同主機另報全精度差
OV_TOL = 1e-6            # 承 probe_WG9265_coverage_account.py（⛔ 新造）
SCEN = [("0m", "got_G值_退縮0m_partial.csv"), ("3.5m", "got_G值_退縮3.5m_partial.csv")]


def poly(c):
    p = Polygon(c)
    return p if p.is_valid else p.buffer(0)


def parse(s):
    """🩸 `cut_coords` 有**二形**：落檔（CSV）為**字串**；`run_step_g` 之記憶體回傳為 **list**。
    ⛔ 靜默退路——取不到即回 `None`，由呼叫端 **loud** 具名（`no-silent-fallback`）。"""
    if s is None:
        return None
    if isinstance(s, (list, tuple)):
        v = s
    else:
        if not str(s).strip():
            return None
        try:
            v = ast.literal_eval(s)
        except Exception:
            return None
    try:
        return [(float(a), float(b)) for a, b in v] if v and len(v) >= 3 else None
    except Exception:
        return None


def load_csv(fn):
    p = os.path.join(OUT, fn)
    if not os.path.exists(p):
        return None
    with io.open(p, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def groups_of(rows):
    """(街廓, 側) → 依 `累積S(m)` 昇冪之列（＝ K-9-15 二 之宗序·⛔ 硬編）。"""
    g = {}
    for r in rows:
        side = (r.get("推進側別") or "").strip()
        if side == "抵費地":
            continue
        g.setdefault(((r.get("所屬街廓") or "").strip(), side), []).append(r)
    for k in g:
        g[k].sort(key=lambda r: float(r.get("累積S(m)") or 0))
    return g


def main():
    import run_verification as rv
    from app_harvest import harvest
    from stepg_pipeline import run_step_g
    from selection_pipeline import run_corner_pk

    print("=" * 116)
    print("【W-G.9-268 `c0`】受詞母體之對位　`A`（不交叉之違反）vs `B`（覆蓋帳之重疊對）")
    print("=" * 116)

    # ── B：全區連跑落檔（口徑甲）──
    print()
    print("── `B` 母體：覆蓋帳違反組之**逐重疊對**（口徑 ＝ **全區連跑**·來源 ＝ harness 落檔）──")
    B_pairs, B_lots, B_groups = [], set(), []
    n_groups = 0
    for tag, fn in SCEN:
        rows = load_csv(fn)
        if rows is None:
            print("🔴 **loud 拒測**：落檔不存在 ⇒ %s" % fn)
            return 6
        for (blk, side), its in groups_of(rows).items():
            P = {}
            for i, r in enumerate(its):
                cc = parse(r.get("cut_coords"))
                if cc is None:
                    continue
                P[(r.get("暫編地號") or "").strip()] = (poly(cc), i)
            if len(P) < 2:
                n_groups += 1
                continue
            n_groups += 1
            tot, pairs = 0.0, []
            for a, b in itertools.combinations(P, 2):
                ov = P[a][0].intersection(P[b][0]).area
                if ov > OV_TOL:
                    tot += ov
                    pairs.append((a, P[a][1], b, P[b][1], ov))
            if pairs:
                B_groups.append((tag, blk, side, len(P), tot))
                for (a, ia, b, ib, ov) in pairs:
                    B_pairs.append((tag, blk, side, a, ia, b, ib, ov))
                    B_lots.add(a)
                    B_lots.add(b)
    print("| 情境 | 街廓 | 側 | 宗 A（序） | 宗 B（序） | 重疊面積 ㎡ |")
    print("|---|---|---|---|---|---|")
    for (tag, blk, side, a, ia, b, ib, ov) in B_pairs:
        print("| %s | %s | %s | `%s`（第%d宗） | `%s`（第%d宗） | **%.4f** |"
              % (tag, blk, side, a, ia, b, ib, ov))
    print("   違反組 ＝ %s" % [(t, b, s, "%.4f" % v) for (t, b, s, _n, v) in B_groups])
    print("   🔒 `B` 之**宗集** ＝ %s（**%d** 宗）" % (sorted(B_lots), len(B_lots)))
    print("   判定集基數：組 ＝ **%d**／重疊對 ＝ **%d**" % (n_groups, len(B_pairs)))

    # ── A：逐街廓獨立·僅 0m（＝ 權威源之口徑）──
    print()
    print("── `A` 母體：不交叉之違反宗（口徑 ＝ **逐街廓獨立呼叫**·情境 ＝ **僅 `0m`**）──")
    print("   🔒 判定（違反與否）**⛔ 本檔重判**，逐字沿用權威源 `probe_WG988_nocross.py` 之「必答 1」；")
    print("   本檔只補其⛔ 出艙之**暫編地號**（該探針之 `暫編地號` 命中 ＝ `0`）。")
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
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, 0.0, snapshot=snapshot)
    rows0 = []
    for lbl in blks:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                sg = run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                wins, forced, 0.0, eff_min_build_by_blk={})
            g_tab, _dg, _sl = rv.build_step_g_tables(sg)
        except RuntimeError as e:
            pt = getattr(e, "partial", None)
            g_tab = list((pt or {}).get("g_rows") or [])
        rows0 += [r for r in g_tab if str(r.get("所屬街廓", "")).strip() == lbl]
    G0 = groups_of(rows0)
    print("   逐街廓獨立·`0m` 可達 ＝ %s" % sorted({k[0] for k in G0}))

    A_rows, gate_ok, gate_lines = [], True, []
    for (blk, side, ordi, exp_area) in A_AUTH:
        its = G0.get((blk, side))
        if not its or len(its) <= ordi:
            print("   🔴 **loud 拒測**：`%s·%s` 之第 %d 宗不可得（判定集基數 %d）"
                  % (blk, side, ordi, 0 if not its else len(its)))
            return 7
        r = its[ordi]
        lot = (r.get("暫編地號") or "").strip()
        cc = parse(r.get("cut_coords"))
        if cc is None:
            print("   🔴 **loud 拒測**：`%s·%s` 第 %d 宗 `%s` 之 `cut_coords` 取不到"
                  "（型別 ＝ %s）⇒ ⛔ 以任何預設幾何代之"
                  % (blk, side, ordi, lot, type(r.get("cut_coords")).__name__))
            return 11
        area = poly(cc).area
        g = float(r.get("G(㎡)") or 0)
        d = abs(area - exp_area)
        ok = d <= TOL_AREA
        gate_ok &= ok
        gate_lines.append((blk, side, ordi, lot, area, exp_area, d, ok))
        A_rows.append((blk, side, ordi, lot, g, area))
    print()
    print("| 街廓 | 側 | 宗序 | **暫編地號** | `G(㎡)` | 分配範圍面積 ㎡ |")
    print("|---|---|---|---|---|---|")
    for (blk, side, ordi, lot, g, area) in A_rows:
        print("| %s | %s | 第%d宗 | **`%s`** | %.4f | %.4f |" % (blk, side, ordi, lot, g, area))
    A_lots = {x[3] for x in A_rows}
    print("   🔒 `A` 之**宗集** ＝ %s（**%d** 宗）；判定集基數（權威源 `POPULATION`）＝ **35**"
          % (sorted(A_lots), len(A_lots)))

    print()
    print("── 自我驗證閘（本檔之重建 vs 權威源所印之面積）──")
    for (blk, side, ordi, lot, area, exp, d, ok) in gate_lines:
        print("   %s %s·%s 第%d宗 `%s`：本檔 %.6f ㎡ ／ 權威源 %.4f ㎡ ｜ |Δ| ＝ %.6f ⇒ %s"
              % ("✅" if ok else "🔴", blk, side, ordi, lot, area, exp, d,
                 "相符（≤ %.2f）" % TOL_AREA if ok else "**不符 ⇒ ⛔ 得據以下任何結論**"))
    print("   ⇒ 自我驗證閘 %s" % ("✅ 過" if gate_ok else "🔴 **不過**"))
    if not gate_ok:
        return 8

    # ── 對位 ──
    print()
    print("── `A` ／ `B` 之對位（逐宗具名·各載判定集基數）──")
    inter, a_only, b_only = sorted(A_lots & B_lots), sorted(A_lots - B_lots), sorted(B_lots - A_lots)
    print("   `A ∩ B` ＝ %s（**%d** 宗）　判定集基數 ＝ |A| %d ＋ |B| %d"
          % (inter or "**∅**", len(inter), len(A_lots), len(B_lots)))
    print("   `A ∖ B` ＝ %s（**%d** 宗）" % (a_only or "∅", len(a_only)))
    print("   `B ∖ A` ＝ %s（**%d** 宗）" % (b_only or "∅", len(b_only)))

    print()
    print("── 🔴 口徑之對位（本檔之核心出艙·⛔ 逕取交集之前必先具名）──")
    print("| 母體 | 口徑 | 情境 | 受詞之組 |")
    print("|---|---|---|---|")
    print("| `A` | **逐街廓獨立呼叫** | **僅 `0m`** | `0m·R2·left` 第1宗／`0m·R5·left` 第1宗 |")
    print("| `B` | **全區連跑** | `0m`（止於 `R2`）＋ `3.5m`（止於 `R5`）| %s |"
          % "／".join("`%s·%s·%s`" % (t, b, s) for (t, b, s, _n, _v) in B_groups))
    print("   🔴 `0m·R5` 於 `B` 之口徑下**結構上不存在**（`0m` 可達 ＝ %s）"
          % sorted({k[0] for k in groups_of(load_csv(SCEN[0][1]))}))

    # ── 否證對照 ──
    print()
    print("── 否證對照（同格載判定集基數·基數 `0` ⇒ loud 拒測）──")
    rc = 0
    csv0 = load_csv(SCEN[0][1])
    g_csv = groups_of(csv0).get(("R2", "left"))
    if not g_csv or len(g_csv) < 2:
        print("   🔴 必綠之判定集基數 ＝ 0 ⇒ **loud 拒測**")
        rc = 9
    else:
        lot_csv = (g_csv[1].get("暫編地號") or "").strip()
        lot_own = next(x[3] for x in A_rows if x[0] == "R2")
        ok = lot_csv == lot_own
        print("   %s 必綠 ＝ `0m·R2·left` 第1宗於二口徑同名　判定集基數 **1**　"
              "全區連跑 `%s` ／ 逐街廓獨立 `%s` ⇒ %s"
              % ("✅" if ok else "🔴", lot_csv, lot_own, "如預期" if ok else "**未如預期**"))
        if not ok:
            rc = 10
    # 🩸 必紅須**真能翻面**：注入 `B` 之一宗入 `A` ⇒ 交集須由 ∅ 轉為非空
    if not B_lots:
        print("   🔴 必紅之判定集基數 ＝ 0 ⇒ **loud 拒測**")
        rc = 11
    else:
        inj = sorted(B_lots)[0]
        A2 = A_lots | {inj}
        ok = len(A2 & B_lots) > len(inter)
        print("   %s 必紅 ＝ 注入 `B` 之一宗（`%s`）入 `A`　判定集基數 **1**　"
              "`|A ∩ B|` 由 **%d** 轉為 **%d** ⇒ %s"
              % ("✅" if ok else "🔴", inj, len(inter), len(A2 & B_lots),
                 "如預期（⇒ 交集運算子確能翻面·本檢⛔ 恆為 ∅）" if ok else "**未如預期 ⇒ 器紅**"))
        if not ok:
            rc = 12

    # ── 同口徑之對位（B′ ＝ 於 `A` 之口徑重算覆蓋帳）──
    print()
    print("── 🔑 同口徑之對位：`B′` ＝ **逐街廓獨立·`0m`** 之覆蓋帳（⇒ 與 `A` 同口徑同情境）──")
    Bp_pairs, Bp_lots, Bp_groups = [], set(), []
    n_gp = 0
    for (blk, side), its in G0.items():
        P = {}
        for i, r in enumerate(its):
            cc = parse(r.get("cut_coords"))
            if cc is None:
                continue
            P[(r.get("暫編地號") or "").strip()] = (poly(cc), i)
        n_gp += 1
        if len(P) < 2:
            continue
        tot, pr = 0.0, []
        for a, b in itertools.combinations(P, 2):
            ov = P[a][0].intersection(P[b][0]).area
            if ov > OV_TOL:
                tot += ov
                pr.append((a, P[a][1], b, P[b][1], ov))
        if pr:
            Bp_groups.append((blk, side, len(P), tot))
            for (a, ia, b, ib, ov) in pr:
                Bp_pairs.append((blk, side, a, ia, b, ib, ov))
                Bp_lots.add(a)
                Bp_lots.add(b)
    print("| 街廓 | 側 | 宗 A（序） | 宗 B（序） | 重疊面積 ㎡ |")
    print("|---|---|---|---|---|")
    for (blk, side, a, ia, b, ib, ov) in Bp_pairs:
        print("| %s | %s | `%s`（第%d宗） | `%s`（第%d宗） | **%.4f** |" % (blk, side, a, ia, b, ib, ov))
    print("   違反組 ＝ %s　判定集基數：組 ＝ **%d**／重疊對 ＝ **%d**"
          % ([(b, s, "%.4f" % v) for (b, s, _n, v) in Bp_groups], n_gp, len(Bp_pairs)))
    ip = sorted(A_lots & Bp_lots)
    print("   🔒 `A ∩ B′` ＝ %s（**%d** 宗）／`A ∖ B′` ＝ %s／`B′ ∖ A` ＝ %s"
          % (ip or "**∅**", len(ip), sorted(A_lots - Bp_lots) or "∅",
             sorted(Bp_lots - A_lots) or "∅"))

    # ── 組層之對位（⛔ 只看宗層）──
    print()
    print("── 🔑 **組層**之對位（`A` 之宗是否落在 `B`／`B′` 之違反<u>組</u>內）──")
    Bg = {(t, b, s) for (t, b, s, _n, _v) in B_groups}
    Bpg = {(b, s) for (b, s, _n, _v) in Bp_groups}
    for (blk, side, ordi, lot, g, area) in A_rows:
        inB = any(bb == blk and ss == side for (_t, bb, ss) in Bg)
        inBp = (blk, side) in Bpg
        print("   `%s`（`0m·%s·%s` 第%d宗）：落在 `B` 之違反組？ **%s**（同街廓側）／"
              "落在 `B′` 之違反組？ **%s**" % (lot, blk, side, ordi,
                                            "是" if inB else "否", "是" if inBp else "否"))
    print("   ⇒ 🔒 **宗層交集為 ∅，而組層⛔ 為 ∅** ——`A` 之二宗皆位於違反組**之內**，"
          "惟**⛔ 為任一重疊對之成員**。")

    print()
    print("── 🛑 停機款（單 `§八`）──")
    if not inter:
        print("   🛑 **`A ∩ B` ＝ ∅ ⇒ 觸發停機款** ——其意謂「閘一轉主動」未必使覆蓋帳歸零，")
        print("      方法與受詞須重新對位。**⛔ 續辦 `c1`〜`c4`。**")
        rc = 20
    else:
        print("   ✅ `A ∩ B` ≠ ∅ ⇒ 未觸發")
    return rc


if __name__ == "__main__":
    sys.exit(main())
