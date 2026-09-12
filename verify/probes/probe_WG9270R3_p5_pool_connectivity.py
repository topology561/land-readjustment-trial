# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令二（KL 序改二）序 `3` ＝ **`p5` 中央池之連通性量測**（零生產碼）。

🛑 **本器⛔ 作任何處置主張、⛔ 判其為缺陷**——KL 已述之應然為
   「街廓最多只有左右兩側街角地及中間**集中**配餘地，⛔ 有中間穿插之零星片」；
   **量得之事實候發單側與 KL**。

🔒 **受詞** ＝ `got_滑池槽診斷_*.csv` 之「**中央池**」，其在**幾何上之各片**。

🛑 **幾何自生產碼取**（單之明令）——**⛔ 自 `got_G值_*.csv` 之 `推進側別` 欄推定**：
   該欄與**正典落檔** `got_抵費地_*.csv` **同名而異物**（發單側 `自誤 369`）。
   🔒 **本器當場坐實其異物**：`got_抵費地_*.csv` 之列係 `指配 = 強制抵費地`（`0m` `1` 列／`3.5m` `2` 列），
   而 `got_G值_*.csv` 之 `推進側別 = 抵費地` 者係**幾何剩餘**片（`0m` `13` 列／`3.5m` `14` 列）。

🔑 **真相源（單一·⛔ 器內重導）** ＝ `app.py` 之 `_pool_strips_for_block`
   （`verify/stepg_pipeline.py:385` 逐字 `_pool_strips_for_block = ns["_pool_strips_for_block"]`
   ·其註解載「§N3-0 T2：池片**單一真相源**」「stepg／app／wf_f1／wf_f4 **四處同源**」）。
   ⇒ 本器以**間諜法**包裹 `ns["_pool_strips_for_block"]`，逐街廓錄其**回傳之 `Polygon` 清單**；
   **⛔ 改生產碼一字**（包裹逕行委派並原樣回傳）。

🔒 **「中央池之片」之界定（機械·⛔ 推定）**
   `池片全集` ＝ `offset_geoms`（＝ `幾何片明細(㎡)`／`片數` 之來源·逐字見 `stepg_pipeline.py:1625-1627`）；
   `中央池` ＝ `池總 − 角落抵費地L − 角落抵費地R`（逐字見 `:1617`）
   ⇒ **中央池之片 ＝ 池片全集 扣除「面積相符於 `got_抵費地_*.csv` 之強制抵費地」者**。
   🛑 其相符須**唯一**（容差**具名** ＝ `0.005 ㎡` ＝ `2dp` 之半個單位）；`0` 或 `≥2` 個候選 ⇒ **loud 拒測**。

🔒 **連通之判準（逐字）**：二片「相接」⇔ `a.intersection(b)` 之 **`length > 0`**；
   `是否連通為單一區域` ⇔ 以「相接」為邊之圖恰有 **`1`** 個連通分量。
   🔒 併報 `a.distance(b)`（⛔ 相接者之最近距）與交集之型別——**⛔ 只給一個布林**。

🔒 **判別力二造（單之明令）**：人造**二相接**之片須判**連通** ⋀ 人造**二分離**之片須判**不連通**。
   🛑 二造同色 ⇒ **量測器紅** ⇒ ⛔ 出艙任何判（`rc = 5`）。

⚠️ **正典之併記（照實·⛔ 本器之判）**：`_pool_strips_for_block` 之 docstring 逐字載
   **`N0-19`（KL 裁 `2026-07-16` 晚）**「原子＝s-帶；**池片＝相鄰池 s-帶之極大聯集**…
   **連通分量＝舊 boolean 實作之 artifact，不再作為片之定義**」
   ⇒ **「片」之定義係 s-區間，⛔ 幾何連通**。本器**只量幾何連通之事實**，⛔ 據以改動任何定義。

用法：`python verify/probes/probe_WG9270R3_p5_pool_connectivity.py [倉根]`
`rc`：`0`／`3` 母體為 `0`（loud 拒測）／`4` 強制抵費地之相符非唯一（loud 拒測）／`5` **量測器紅**。
"""
import contextlib
import csv
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

BT = chr(96)
W = 118
SBS = (0.0, 3.5)
TOL_AREA = 0.005          # 🔒 具名：`2dp` 之半個單位（⛔ 放寬）
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]


def say(s=""):
    print(s)


def drive_spy(sb):
    """驅動生產管線一次，並以**間諜法**錄 `_pool_strips_for_block` 之逐街廓回傳。"""
    ns, fake_st = harvest()
    rec = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label="", _depth=None, _verbose=True):
        out = _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                    _label=_label, _depth=_depth, _verbose=_verbose)
        rec.setdefault(str(_label), []).append(list(out))
        return out                      # 🛑 **逐位原樣回傳**（⛔ 改一字）

    ns["_pool_strips_for_block"] = _spy

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build_p, wins, forced, sb,
                       eff_min_build_by_blk={})
    except RuntimeError:
        pass                            # 其 partial 不影響本受詞（池片於各街廓結算時即已錄）
    return rec


def read_csv(p):
    with io.open(p, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def forced_offsets(tag):
    """自**正典落檔** `got_抵費地_退縮{tag}.csv` 取強制抵費地（`街廓 → [面積]`）。"""
    p = os.path.join(REPO, "verify", "out", "got_抵費地_退縮%s.csv" % tag)
    if not os.path.exists(p):
        return None, "🛑 `%s` ⛔ 存在" % os.path.basename(p)
    rr = read_csv(p)
    hdr = list(rr[0].keys()) if rr else []
    k_blk = next((h for h in hdr if "街廓" in h), None)
    k_a = next((h for h in hdr if "面積" in h), None)
    k_z = next((h for h in hdr if "指配" in h), None)
    if not (k_blk and k_a):
        return None, "🛑 缺欄（街廓 ＝ %r／面積 ＝ %r）" % (k_blk, k_a)
    m = {}
    for r in rr:
        m.setdefault((r.get(k_blk) or "").strip(), []).append(
            (float(r.get(k_a) or 0.0), (r.get(k_z) or "").strip() if k_z else ""))
    return m, ("✅ 自 `%s` 取得 **%d** 列（欄 ＝ %s／%s／%s）"
               % (os.path.basename(p), len(rr), k_blk, k_a, k_z))


def pool_csv(tag):
    p = os.path.join(REPO, "verify", "out", "got_滑池槽診斷_退縮%s.csv" % tag)
    if not os.path.exists(p):
        return None
    return {(_r.get("街廓") or "").strip(): _r for _r in read_csv(p)}


def touch_len(a, b):
    """二片之關係。回 `(相接長, 重疊面積, 型別, 最近距, 類)`。

    🩸 **本函式之初版為<u>錯</u>——已於出艙前自捕並修正**：其逕取 `a.intersection(b).length`，
    而 **`shapely` 之 `Polygon.length` ＝ <u>周長</u>，⛔ 相接長**。
    實見 `R1`＠`3.5m` 之 `#1↔#2` 印出「相接長 `66.528`·型 `Polygon`·最近距 `0`」
    ——其真相係**二片之交集為 2D（重疊）**，而該 `66.528` 係**重疊區之周長**。
    🔴 **其徵候與「共用一條 `66.5 m` 長之邊」完全相同**，且**使之被判為「相接」⇒ 連通**。

    🔒 **修正後之三分類（互斥且窮盡）**
      `空`      ＝ `it.is_empty`                         ⇒ **⛔ 相接**
      `重疊(2D)` ＝ `it.area > 0`                         ⇒ **⛔ 相接**（另報其**面積**·須單獨呈）
      `線/點`   ＝ 其餘（`area == 0`）                     ⇒ **相接 ⇔ `length > 0`**
    """
    it = a.intersection(b)
    ar = float(getattr(it, "area", 0.0) or 0.0)
    ln = float(getattr(it, "length", 0.0) or 0.0)
    d = float(a.distance(b))
    if it.is_empty:
        kind = "空"
        ln = 0.0
    elif ar > 0.0:
        kind = "重疊(2D)"
        ln = 0.0                        # 🛑 **⛔ 以周長充相接長**
    else:
        kind = "線/點"
    return ln, ar, it.geom_type, d, kind


def components(n, edges):
    """連通分量（union-find）。"""
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for i, j in edges:
        ri, rj = find(i), find(j)
        if ri != rj:
            par[ri] = rj
    comp = {}
    for i in range(n):
        comp.setdefault(find(i), []).append(i)
    return list(comp.values())


def main():
    from shapely.geometry import Polygon as _P
    rc = 0
    say("=" * W)
    say("【`W-G.9-270` 補令二 序 `3`（KL 序改二）】**`p5` 中央池之連通性量測**")
    say("=" * W)
    say("🛑 **本器⛔ 作任何處置主張、⛔ 判其為缺陷**——量得之事實候發單側與 KL。")
    say("🔒 真相源 ＝ `app.py` `_pool_strips_for_block`（間諜法自 `ns` 取·⛔ 器內重導）")
    say("🛑 **⛔ 自 `got_G值_*.csv` 之 `推進側別` 欄推定**（`自誤 369`：與正典落檔同名而異物）")
    say("")

    # ── 判別力二造（**先於**任何實測·`常規五`）──────────────────────────
    say("─" * W)
    say("【判別力二造】（單之明令·二造同色 ⇒ 量測器紅 ⇒ ⛔ 出艙任何判）")
    say("─" * W)
    A = _P([(0, 0), (1, 0), (1, 1), (0, 1)])
    B_touch = _P([(1, 0), (2, 0), (2, 1), (1, 1)])          # 共用一整條邊
    B_apart = _P([(2, 0), (3, 0), (3, 1), (2, 1)])          # 相距 1 m
    B_over = _P([(0.5, 0), (1.5, 0), (1.5, 1), (0.5, 1)])   # **重疊** 0.5 ㎡
    l1, a1, t1, d1, k1 = touch_len(A, B_touch)
    l2, a2, t2, d2, k2 = touch_len(A, B_apart)
    l3, a3, t3, d3, k3 = touch_len(A, B_over)
    c1 = components(2, [(0, 1)] if l1 > 0 else [])
    c2 = components(2, [(0, 1)] if l2 > 0 else [])
    say("   造甲［人造**二相接**之片］⇒ 類 `%s`·相接長 **%.9f m**·重疊面積 %.9f（型 `%s`·最近距 %.9f）"
        "⇒ 連通分量 **%d** ⇒ %s"
        % (k1, l1, a1, t1, d1, len(c1), "✅ 判連通" if len(c1) == 1 else "🔴"))
    say("   造乙［人造**二分離**之片］⇒ 類 `%s`·相接長 **%.9f m**·重疊面積 %.9f（型 `%s`·最近距 %.9f）"
        "⇒ 連通分量 **%d** ⇒ %s"
        % (k2, l2, a2, t2, d2, len(c2), "✅ 判不連通" if len(c2) == 2 else "🔴"))
    say("   造丙［人造**二重疊**之片·重疊 `0.5 ㎡`］⇒ 類 `%s`·相接長 **%.9f m**·重疊面積 **%.9f ㎡**"
        "（型 `%s`）⇒ %s"
        % (k3, l3, a3, t3, "✅ 判**重疊**、⛔ 判相接（其 `Polygon.length` ＝ 周長 `%.6f`·⛔ 相接長）"
           % _P([(0.5, 0), (1, 0), (1, 1), (0.5, 1)]).length
           if (k3 == "重疊(2D)" and l3 == 0.0) else "🔴"))
    if not (len(c1) == 1 and len(c2) == 2 and k3 == "重疊(2D)" and l3 == 0.0):
        say("   🛑 **三造不如預期 ⇒ 量測器紅** ⇒ ⛔ 出艙任何判")
        sys.exit(5)
    say("   ⇒ **器非紅**（一造連通、一造不連通、一造重疊 ⇒ 三類皆可分辨）✅")
    say("")

    for sb in SBS:
        tag = "%gm" % sb
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        rec = drive_spy(sb)
        say("🔒 間諜所錄 `_pool_strips_for_block` 之街廓 ＝ **%d**：%s"
            % (len(rec), "／".join(sorted(rec))))
        if not rec:
            say("🛑 母體 `0` ⇒ **loud 拒測**")
            sys.exit(3)

        fo, fdiag = forced_offsets(tag)
        say("🔒 強制抵費地（**正典落檔**）：%s" % fdiag)
        if fo is None:
            sys.exit(3)
        for b, lst in sorted(fo.items()):
            say("      %s ⇒ %s" % (b, "／".join("%.2f（%s）" % (a, z) for a, z in lst)))
        pc = pool_csv(tag)
        say("🔒 `got_滑池槽診斷_退縮%s.csv` %s" % (tag, "✅ 在" if pc else "🛑 ⛔ 在"))
        say("")

        for blk in BLKS:
            if blk not in rec:
                say("   🛑 `%s` **⛔ 在間諜所錄之母體** ⇒ 其量 **⛔ 可得**（坑 `z`：⛔ 印 `0`）" % blk)
                continue
            calls = rec[blk]
            geoms = calls[-1]                 # 🔒 取**最末一次**（＝結算態）；併報呼叫次數
            say("   ── `%s` ──（`_pool_strips_for_block` 呼叫 **%d** 次·取**最末一次**之回傳）"
                % (blk, len(calls)))
            areas = [float(g.area) for g in geoms]
            say("      **池片全集** ＝ **%d** 片；面積（依回傳序·＝面積遞減）＝ %s"
                % (len(geoms), "[" + ", ".join("%.6f" % a for a in areas) + "]"))
            if pc and blk in pc:
                r = pc[blk]
                say("      落檔對拍：`片數` ＝ %s ⇒ %s ｜ `幾何片明細(㎡)` ＝ %s"
                    % (r.get("片數"), "✅" if str(r.get("片數")) == str(len(geoms)) else "🔴 相異",
                       r.get("幾何片明細(㎡)")))
                say("      落檔之 `池總` ＝ %s ｜ `角落抵費地L/R` ＝ %s／%s ｜ **`中央池`** ＝ %s"
                    % (r.get("池總=幾何剩餘(㎡)"), r.get("角落抵費地L(㎡)"),
                       r.get("角落抵費地R(㎡)"), r.get("中央池(㎡)")))

            # ── 扣除強制抵費地（相符須唯一）────────────────────────────
            drop = set()
            for fa, fz in fo.get(blk, []):
                cand = [i for i, a in enumerate(areas)
                        if i not in drop and abs(a - fa) <= TOL_AREA]
                if len(cand) != 1:
                    say("      🛑 強制抵費地 `%.2f`（%s）於池片全集之相符候選 ＝ **%d**（期 `1`）"
                        " ⇒ **loud 拒測**（⛔ 猜）" % (fa, fz, len(cand)))
                    sys.exit(4)
                drop.add(cand[0])
                say("      扣除強制抵費地：片 `#%d`（%.6f ㎡）⟷ 落檔 `%.2f` ⇒ ✅ 唯一相符"
                    % (cand[0] + 1, areas[cand[0]], fa))
            idx = [i for i in range(len(geoms)) if i not in drop]
            cg = [geoms[i] for i in idx]
            say("      🔑 **中央池之片 ＝ %d** 片；其面積 ＝ %s；Σ ＝ **%.6f ㎡**"
                % (len(cg), "[" + ", ".join("%.6f" % areas[i] for i in idx) + "]",
                   sum(areas[i] for i in idx)))
            if pc and blk in pc:
                try:
                    _cp = float(pc[blk].get("中央池(㎡)") or 0.0)
                    _d = abs(sum(areas[i] for i in idx) - _cp)
                    say("      **二數並報**：本器 Σ ＝ `%.6f` ／ 落檔 `中央池` ＝ `%.2f` ⇒ |Δ| ＝ `%.6f` %s"
                        % (sum(areas[i] for i in idx), _cp, _d,
                           "✅（≤ 2dp 捨入量子 0.005×片數）" if _d <= 0.005 * max(1, len(geoms))
                           else "🔴 **相異**·照實"))
                except (TypeError, ValueError):
                    say("      **二數並報** ⇒ 落檔之 `中央池` **⛔ 可得**")

            # ── 兩兩相接 ＋ 連通 ──────────────────────────────────────
            if len(cg) <= 1:
                say("      **兩兩相接**：⛔ 可比之對（片數 ≤ 1）；**連通分量 ＝ %d** ⇒ %s"
                    % (len(cg), "🟢 單一區域" if len(cg) == 1 else "⛔ 可得"))
                say("")
                continue
            say("      **兩兩關係**（判準：交集為**線/點**且 `length > 0` ⇒ 相接；"
                "交集**有面積** ⇒ **重疊**·⛔ 相接）")
            say("         %-10s %-10s %-18s %-16s %-14s %-16s %s"
                % ("對", "類", "相接長(m)", "重疊面積(㎡)", "交集型", "最近距(m)", "判"))
            edges, overlaps = [], []
            for i in range(len(cg)):
                for j in range(i + 1, len(cg)):
                    L, AR, T, D, K = touch_len(cg[i], cg[j])
                    if L > 0:
                        edges.append((i, j))
                    if K == "重疊(2D)":
                        overlaps.append((idx[i] + 1, idx[j] + 1, AR))
                    say("         %-10s %-10s %-18.9f %-16.9f %-14s %-16.9f %s"
                        % ("#%d↔#%d" % (idx[i] + 1, idx[j] + 1), K, L, AR, T, D,
                           "🟢 相接" if L > 0 else
                           ("🔴 **重疊**" if K == "重疊(2D)" else "⛔ 相接")))
            if overlaps:
                say("      🔴 **重疊之對（⛔ 相接·須單獨呈）**：%s"
                    % "／".join("#%d↔#%d ＝ %.9f ㎡" % o for o in overlaps))
            comps = components(len(cg), edges)
            say("      🔑 **連通分量 ＝ %d** ⇒ %s"
                % (len(comps),
                   "🟢 **連通為單一區域**" if len(comps) == 1
                   else "🔴 **⛔ 連通為單一區域**（分量之成員：%s）"
                        % "／".join("{" + ",".join("#%d" % (idx[k] + 1) for k in c) + "}"
                                    for c in comps)))
            say("")

    say("=" * W)
    say("🛑 **本器⛔ 作任何處置主張、⛔ 判其為缺陷**。")
    say("⚠️ **正典之併記（照實）**：`_pool_strips_for_block` 之 docstring 逐字載 `N0-19`")
    say("   （KL 裁 `2026-07-16` 晚）「原子＝s-帶；**池片＝相鄰池 s-帶之極大聯集**…")
    say("   **連通分量＝舊 boolean 實作之 artifact，不再作為片之定義**」")
    say("   ⇒ **「片」之定義係 s-區間，⛔ 幾何連通**；本器只量幾何連通之**事實**。")
    sys.exit(rc)


if __name__ == "__main__":
    main()
