# -*- coding: utf-8 -*-
"""
W-F F.2 — 級1/2/3 跨街廓同歸戶合併（a′ 首次登場；claude.ai/KL 裁定 2026-07-11）。

**a′＝模式一自寫**（規格 §7-4:419；a 基、run_step_g 重解，非 calc_a_prime、非 G 直加）：
    a′ = a_源 × p(源zone) / p(目標街廓該歸戶地zone)
  a_源＝重劃前面積（trunk B 之「a 面積」欄＝分攤登記＋F.0 吸收），**非 G**。
  §7-4 為手冊平均式之條件細化：模式一（有同歸戶目標地→用該歸戶目標地價）為精確形，
  模式二（無→退回街廓幾何面積權重平均）為退化形，等同手冊 P.121 一般式。F.2 恆走模式一
  （同歸戶跨街廓⟹必有目標街廓前地）；模式二留 F.4。**禁呼叫 calc_a_prime／三廢函式**（F.5 汰換）。

**機制**：目標宗.面積_m2 += Σa′（同目標宗多源累加）；源宗自 parcels 移除 → run_step_g 對
  (a_目標+Σa′) 重解（§142）。消費 trunk B（F.0 終態）parcels（F.1 為幾何後處理、未改 parcels）→ trunk C。

**跨街廓守恆（首次）**：源塊池**增**（源宗移除、其配地經位相不變前移釋回源塊中央池，增量＝被移除宗 G）／
  目標塊池**減**（吸收 a′）／每塊 ΣG+池=塊面積<1㎡／全區 Σ(ΣG+池)=ΣDXF。
  〔精化裁定令「來源塊池不變」：源宗於 trunk B 已配地、移出必釋地入源池，reviewer 物理定論、真值佐證。〕

**距離級別**（規格 §2）：相鄰＝共享 BLOCK 邊或隔 RD 相望；鄰近＝質心距≤中位；非鄰近＝其餘。
  UC9898 七轉出全級1（相鄰）；級2/3 不現。

**池消耗三則**：禁中間態——任一塊 0<池<MinA → 停機②。本案池巨大不觸發「轉走」分支（dormant）。

停機：池落 (0,MinA)；G 迭代不收斂（run_step_g 內）；跨街廓守恆破；F.1 正交破（628-37(1) 變）。
additive-only：不改 app.py／stepg 推進機／wf_f0／wf_f1。
"""
import os
import sys
import copy
import collections

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from shapely.geometry import Polygon                 # noqa: E402
from stepg_pipeline import run_step_g, build_step_g_tables  # noqa: E402
import wf_f0                                          # noqa: E402

F2_GROUPS = ["G009", "G001", "G021", "G026", "G027"]
# F.1 正交錨（該情境左角勝者＝F.1 R1 整形標的；F.2 不得動之）
F1_TARGET = {"0m": "628-37(1)", "3.5m": "628-36(1)"}


def _pre_price(snap):
    return {z: float(v["單價_元每m2"]) for z, v in snap["財務接線_v3"]["重劃前區段_面積單價"].items()}


def _block_pre_avg(snap, build_parcels, pre_price):
    """模式二分母：各可建築街廓之 p_average（**重劃前 DXF 幾何面積_m2** 權重，規格 §7-4:420）。
    build_parcels 已為可建築（build_build_parcels 已濾）；ghost sliver（幾何面積恆 0）跳過。"""
    zof = snap["財務接線_v3"]["原地號_區段"]
    acc = collections.defaultdict(lambda: [0.0, 0.0])   # blk → [Σ(area×price), Σarea]
    for tp in build_parcels:
        if tp.get("_is_ghost_sliver"):
            continue
        z = zof.get(tp["原地號"], "")
        if z not in pre_price:
            continue
        area = float(tp.get("幾何面積_m2", 0) or 0)
        acc[tp["所屬街廓"]][0] += area * pre_price[z]
        acc[tp["所屬街廓"]][1] += area
    return {b: (v[0] / v[1] if v[1] else 0.0) for b, v in acc.items()}


def a_prime_mode1(a, z_src, z_tgt, pre_price):
    """模式一：a′ = a × p(源) / p(目標該歸戶地)。"""
    return a * pre_price[z_src] / pre_price[z_tgt]


def a_prime_mode2(a, z_src, blk_avg_tgt, pre_price):
    """模式二（並列對照／F.4 用）：a′ = a × p(源) / p_average(目標街廓)。"""
    return a * pre_price[z_src] / blk_avg_tgt if blk_avg_tgt else 0.0


def _decide(gid, byg, mina):
    """群 gid 之 F.2 決策。回傳 (tgt_blk, tgt_row, src_rows) 或 None（無達標塊→應 F.4）。"""
    blks = byg[gid]
    qual = {}
    for blk, rows in blks.items():
        if any(float(r["G(㎡)"]) >= mina[blk] and not r["畸零地旗標"].strip() for r in rows):
            qual[blk] = sum(float(r["G(㎡)"]) for r in rows)
    if not qual:
        return None
    tgt_blk = max(sorted(qual), key=qual.get)               # 並列取字典序（決定性）
    tgt_row = sorted(blks[tgt_blk], key=lambda r: (-float(r["G(㎡)"]), r["暫編地號"]))[0]
    src_rows = [r for blk, rows in sorted(blks.items()) if blk not in qual for r in rows]
    return tgt_blk, tgt_row, src_rows


def _proj_order(ns, cad, parcels, blk):
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    pib = [{"暫編地號": tp["暫編地號"], "polygon_coords": tp.get("polygon_coords")}
           for tp in parcels if tp["所屬街廓"] == blk and not tp.get("_is_ghost_sliver")]
    return [x["暫編地號"] for x in ns["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]


def _block_adjacency(cb_by):
    """§2 相鄰：共享 BLOCK 邊(<0.5m) 或 隔單一 RD 相望。回傳 set of frozenset({a,b})。"""
    polys = {b["label"]: Polygon(b["vertices"]).buffer(0) for b in cb_by.values()}
    R = [l for l in polys if l.startswith("R") and not l.startswith("RD")]
    RD = [l for l in polys if l.startswith("RD")]
    adj = set()
    for i, a in enumerate(R):
        for b in R[i + 1:]:
            share = polys[a].distance(polys[b]) < 0.5
            via = any(polys[rd].distance(polys[a]) < 0.5 and polys[rd].distance(polys[b]) < 0.5
                      for rd in RD)
            if share or via:
                adj.add(frozenset((a, b)))
    return adj, {l: polys[l].centroid for l in R}


def compute(ctx_by_tag, f0_out):
    """F.2 逐情境。回傳 {tag: {tables, anchors, ...}}。"""
    out = {}
    for tag, c in ctx_by_tag.items():
        ns, snap, cb_by, cad = c["ns"], c["snap"], c["cb_by"], c["cad"]
        fcb = ns["F3_CATEGORY_BURDEN"]
        omap = c["omap"]
        zof = snap["財務接線_v3"]["原地號_區段"]
        pre_price = _pre_price(snap)
        mina = wf_f0._mina_by_block(ns, snap, cb_by)
        gof = lambda p: omap.get(p, "")

        # trunk B（F.0 終態）；f0_parcels/poolB 來自 f0_out（wf_f0 加性暴露）
        rows_B = f0_out[tag]["sgB_rows"]
        B = {r["暫編地號"]: r for r in rows_B if r.get("推進側別") in ("left", "right")}
        f0_parcels = f0_out[tag]["f0_parcels"]     # trunk B parcels＝跨街廓搬 a′ 之母體
        poolB = {l: float(v["池總=幾何剩餘(㎡)"]) for l, v in f0_out[tag]["poolB_diag"].items()}
        blk_avg = _block_pre_avg(snap, f0_parcels, pre_price)
        adj, cen = _block_adjacency(cb_by)

        byg = collections.defaultdict(lambda: collections.defaultdict(list))
        for r in B.values():
            byg[gof(r["原地號"])][r["所屬街廓"]].append(r)

        # ── 決策＋a′（模式一）＋雙模式並列 ──
        conv_rows, inject, remove2, transfers = [], collections.defaultdict(float), set(), []
        import numpy as np
        _dists = []
        raw = []
        for gid in F2_GROUPS:
            d = _decide(gid, byg, mina)
            if d is None:
                raise RuntimeError(f"🔴 [{tag}] {gid} 無達標塊，不應在 F.2 名單（應 F.4）")
            tgt_blk, tgt_row, src_rows = d
            z_tgt = zof[tgt_row["原地號"]]
            for r in src_rows:
                z_src = zof[r["原地號"]]
                a_src = float(r["a 面積(㎡)"])
                m1 = round(a_prime_mode1(a_src, z_src, z_tgt, pre_price), 2)
                m2 = round(a_prime_mode2(a_src, z_src, blk_avg[tgt_blk], pre_price), 2)
                sblk = r["所屬街廓"]
                cd = cen[sblk].distance(cen[tgt_blk])
                _dists.append(cd)
                raw.append((gid, r, sblk, z_src, a_src, tgt_blk, tgt_row, z_tgt, m1, m2, cd))
        med = float(np.median(_dists)) if _dists else 0.0
        for (gid, r, sblk, z_src, a_src, tgt_blk, tgt_row, z_tgt, m1, m2, cd) in raw:
            if frozenset((sblk, tgt_blk)) in adj:
                lvl = "級1相鄰"
            elif cd <= med:
                lvl = "級2鄰近"
            else:
                lvl = "級3非鄰近"
            inject[tgt_row["暫編地號"]] += m1
            remove2.add(r["暫編地號"])
            transfers.append({"gid": gid, "src": r["暫編地號"], "tgt": tgt_row["暫編地號"]})
            conv_rows.append({
                "情境": tag, "歸戶": gid, "源宗": r["暫編地號"], "源街廓": sblk, "源zone": z_src,
                "目標宗": tgt_row["暫編地號"], "目標街廓": tgt_blk, "目標zone": z_tgt,
                "a_源(㎡)": a_src, "模式一a′(㎡)": m1, "模式二a′(㎡)": m2,
                "雙模式Δ(㎡)": round(abs(m1 - m2), 2), "級別": lvl,
                "目標G_前(㎡)": float(tgt_row["G(㎡)"]),
            })

        # ── F.2 變換（deepcopy！）──
        f2_parcels = copy.deepcopy(f0_parcels)
        by_id = {tp["暫編地號"]: tp for tp in f2_parcels}
        for tid, add in inject.items():
            by_id[tid]["面積_m2"] = round(float(by_id[tid].get("面積_m2", 0) or 0) + add, 2)
        f2_parcels = [tp for tp in f2_parcels if tp["暫編地號"] not in remove2]

        # ── trunk C（結構永久閘於 run_step_g 內自動 raise）──
        sgC = run_step_g(ns, c["fake_st"], list(cb_by.values()), cad, snap,
                         c["params"], f2_parcels, c["winners"], c["forced"], c["setback"])
        C = {r["暫編地號"]: r for r in sgC["g_rows"] if r.get("推進側別") in ("left", "right")}
        g_tab, _, _ = build_step_g_tables(sgC)
        poolC = {l: float(v["池總=幾何剩餘(㎡)"]) for l, v in sgC["pool_diag"].items()}
        verdC = {l: v["判定"] for l, v in sgC["pool_diag"].items()}

        # 目標宗 G 前後（填入 conv_rows）
        for cr in conv_rows:
            cr["目標G_後(㎡)"] = float(C[cr["目標宗"]]["G(㎡)"])

        # ── 池流向＋三則 ──
        srcset = {r["所屬街廓"] for k in remove2 for r in [B[k]]}
        tgtset = {C[t]["所屬街廓"] for t in inject}
        pool_rows, mid_state = [], []
        for l in sorted(poolC):
            role = ("源" if l in srcset else "") + ("目標" if l in tgtset else "") or "未動"
            if 0 < poolC[l] < mina[l]:
                mid_state.append(l)
            pool_rows.append({"情境": tag, "街廓": l, "角色": role,
                              "池_B(㎡)": round(poolB[l], 2), "池_C(㎡)": round(poolC[l], 2),
                              "池差(㎡)": round(poolC[l] - poolB[l], 2),
                              "MinA": mina[l],
                              "三則": ("🔴落(0,MinA)" if 0 < poolC[l] < mina[l]
                                       else ("歸零" if poolC[l] < 1 else "≥MinA"))})
        if mid_state:
            raise RuntimeError(f"🔴 [{tag}] 停機②：池落 (0,MinA) 開區間：{mid_state}")

        # ── 跨街廓守恆：純源池增／純目標池減／混合塊淨值任意（僅每塊守恆）──
        #   混合塊（既源既目標，如 R2=G021源+G001目標）淨值由兩效應主導方決定、無固定方向。
        for l in srcset - tgtset:          # 純源
            if poolC[l] - poolB[l] < -0.5:
                raise RuntimeError(f"🔴 [{tag}] 純源塊 {l} 池未增（Δ={poolC[l]-poolB[l]:.2f}）：源宗釋地應增池")
        for l in tgtset - srcset:          # 純目標
            if poolC[l] - poolB[l] > 0.5:
                raise RuntimeError(f"🔴 [{tag}] 純目標塊 {l} 池未減（Δ={poolC[l]-poolB[l]:.2f}）：吸收 a′ 應減池")
        tot_B = sum(poolB.values()) + sum(float(r["G(㎡)"]) for r in B.values())
        tot_C = sum(poolC.values()) + sum(float(r["G(㎡)"]) for r in C.values())
        block_area = sum(float(cb_by[l].get("area_m2", 0) or 0)
                         for l in poolC)
        cons_resid = abs(tot_C - block_area)

        # ── 目標宗 G ≥ MinA ──
        for tid in inject:
            r = C[tid]
            if float(r["G(㎡)"]) < mina[r["所屬街廓"]]:
                raise RuntimeError(f"🔴 [{tag}] 目標宗 {tid} 灌後 G={r['G(㎡)']}<MinA_{r['所屬街廓']}")

        # ── F.1 正交：F.1 標的 B→C 全等 ──
        f1t = F1_TARGET[tag]
        f1_ok = (f1t in C and abs(float(C[f1t]["G(㎡)"]) - float(B[f1t]["G(㎡)"])) < 0.01
                 and abs(float(C[f1t]["S(m)"]) - float(B[f1t]["S(m)"])) < 0.01)

        # ── 位次序（投影序）不變（各塊 ∖ 移除宗）──
        pos_viol = []
        for blk in sorted({r["所屬街廓"] for r in B.values()}):
            oB = _proj_order(ns, cad, f0_parcels, blk)
            oC = _proj_order(ns, cad, f2_parcels, blk)
            exp = [x for x in oB if x not in remove2]
            if oC != exp:
                pos_viol.append((blk, exp, oC))

        anchors = {
            "transfers": len(conv_rows), "removed": sorted(remove2),
            "targets": {t: round(v, 2) for t, v in inject.items()},
            "verdict_all_green": all("🔴" not in str(v) for v in verdC.values()),
            "cons_resid": round(cons_resid, 2),
            "f1_orthogonal": f1_ok, "pos_viol": pos_viol,
            "g021_m1": next((cr["模式一a′(㎡)"] for cr in conv_rows if cr["歸戶"] == "G021"), None),
            "g021_m2": next((cr["模式二a′(㎡)"] for cr in conv_rows if cr["歸戶"] == "G021"), None),
            "same_zone_identity": all(
                abs(cr["模式一a′(㎡)"] - cr["a_源(㎡)"]) < 0.01
                for cr in conv_rows if cr["源zone"] == cr["目標zone"]),
        }
        out[tag] = {"conv_rows": conv_rows, "g_tab": g_tab, "pool_rows": pool_rows,
                    "anchors": anchors, "blk_avg": blk_avg, "pre_price": pre_price}
    return out


def fixture_cross_zone(snap, build_parcels):
    """跨區段 fixture（合成 a→b 轉出，exercise ratio≠1；不入 build_ownership、不改真資料）：
    斷言 模式一 a′ == a×p_a/p_b（≠a）、模式二 == a×p_a/p_avg(目標塊)。回傳 dict。"""
    pre_price = _pre_price(snap)
    blk_avg = _block_pre_avg(snap, build_parcels, pre_price)
    a = 100.0
    m1 = a_prime_mode1(a, "a", "b", pre_price)          # a→b：分母 pb
    m2 = a_prime_mode2(a, "a", blk_avg["R2"], pre_price)  # R2 純 b → p_avg=pb
    m1_ab_R1 = a_prime_mode2(a, "a", blk_avg["R1"], pre_price)  # R1 混 → p_avg≠pb
    return {"a": a, "mode1_a_to_b": round(m1, 4), "expect_m1": round(a * pre_price["a"] / pre_price["b"], 4),
            "mode2_tgtR2": round(m2, 4), "mode2_tgtR1_mixed": round(m1_ab_R1, 4),
            "ratio_ne_1": abs(m1 - a) > 1.0}
