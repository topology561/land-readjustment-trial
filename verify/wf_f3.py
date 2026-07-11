# -*- coding: utf-8 -*-
"""
W-F F.3 — 三調配順位之 2、3：RD 道路用地＋PF 共同負擔公設地（KL 三歧義裁定 2026-07-11）。

公設地(RD/PF)之 a′ 併入同歸戶建地 → trunk D。母體＝**trunk C（F.2 終態）**（依賴鏈 7-1→7-2→7-3）。
- **a′ 基準＝分攤登記面積_m2**（§142）；五則①切半按**幾何面積比 pro-rate**；a′=分攤登記×p(源zone)/p(目標zone)。
- **targeting＝四層瀑布**（§31-1-1 類推）：①同原地號 → ②質心距最近 → ③G 較大塊(trunk C G) → ④字典序。
- **RD 五則**（手冊 192-193）：①兩側皆同歸戶地→CENTERLINE 切兩半分向兩側；②③向可建築/另側集中（單側 cascade）；
  ④無同歸戶地→轉 7-4；⑤同意集中→標旗不執行。本案：①切半 5 筆(全 RD2 真跨線)／③集中 30 筆。
- **PF**（手冊 194-195，8 類）：相鄰住宅區同歸戶併入；**隔 RD 不阻卻相鄰**（KL 修正 §7-3）、落歸戶自有建地。
- **分派**：公設筆之歸戶於 trunk C **有≥1 建地→cascade 併入；否則→轉 7-4**（G025 型：建地 F.0 梯3 釋池）。
  母數 59＝**併入 35 筆(19 群)／轉 7-4 24 筆(9 群)**。
- **公設筆非在 build_parcels 內**（共同負擔已濾）→ **無移除、純灌入**；run_step_g → trunk D。

守衛（reviewer 四項）：①分派＝g_has_bld(trunk C)＋cascade 空 gbld fail-loud；②五則①split≠2 片 fail-loud；
③628-18(3) 分攤登記 96.82 實見(非幾何 97.46)；④跨區段 fixture exercise ratio≠1。
停機：PF 整筆超池(dormant,fail-loud)；公設筆五則窮盡無處置且未標轉 7-4。
additive-only：不改 app.py／stepg／wf_f0／wf_f1／wf_f2 推進機（wf_f2 僅加性暴露 f2_parcels）。
禁呼叫 calc_a_prime／三廢函式（靜態閘）；_TIER1_APRIME_INJECT_ENABLED 廢棄非翻。
"""
import os
import sys
import copy
import collections

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np                                   # noqa: E402
from shapely.geometry import Polygon, LineString    # noqa: E402
from shapely.ops import split as _shsplit           # noqa: E402
from stepg_pipeline import run_step_g, build_step_g_tables  # noqa: E402
import wf_f0                                          # noqa: E402
import wf_f2                                          # noqa: E402

# 五則①切半（同歸戶建地跨中心線兩側；實測全 RD2 真跨線切近等半）
STRADDLE = {"628(6)", "628-30(4)", "628-31(4)", "628-32(4)", "628-45(5)"}
# 錨（0m）：628-18(3) → 628-18(2)@R5，重測 a=477.91（381.09 分攤 + 96.82 分攤）
ANCHOR_628_18 = {"pub": "628-18(3)", "tgt": "628-18(2)", "a_expect": 477.91}


def _poly_of(temp, pid):
    for t in temp:
        if t["暫編地號"] == pid and t.get("polygon_coords") and len(t["polygon_coords"]) >= 3:
            p = Polygon(t["polygon_coords"])
            return p if p.is_valid else p.buffer(0)
    return None


def _side(cl, pt):
    a, b = np.array(cl[0]), np.array(cl[-1])
    return "L" if (b[0]-a[0])*(pt[1]-a[1]) - (b[1]-a[1])*(pt[0]-a[0]) > 0 else "R"


def _cascade(temp, pub_poly, parent, gid, gbld, GC):
    """四層瀑布：①同原地號 ②質心距 ③G較大 ④字典序。空 gbld → 停機（reviewer 守衛①）。"""
    cs = gbld.get(gid, [])
    if not cs:
        raise RuntimeError(f"🔴 cascade 空 gbld：{gid}（歸戶於 trunk C 無建地，應已分派轉 7-4）")
    same = [b for b in cs if b["原地號"] == parent]
    pool1 = same if same else cs
    dmin = min(pub_poly.distance(_poly_of(temp, b["暫編地號"])) for b in pool1)
    near = [b for b in pool1 if pub_poly.distance(_poly_of(temp, b["暫編地號"])) - dmin < 0.01]
    if len(near) == 1:
        return near[0], ("同原地號" if same else "歸戶")
    gm = max(GC.get(b["暫編地號"], 0) for b in near)
    big = [b for b in near if GC.get(b["暫編地號"], 0) >= gm - 0.01]
    if len(big) == 1:
        return big[0], ("同原地號·G較大" if same else "歸戶·G較大")
    return sorted(big, key=lambda b: b["暫編地號"])[0], "字典序"


def _proj_order(ns, cad, parcels, blk):
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    pib = [{"暫編地號": tp["暫編地號"], "polygon_coords": tp.get("polygon_coords")}
           for tp in parcels if tp["所屬街廓"] == blk and not tp.get("_is_ghost_sliver")]
    return [x["暫編地號"] for x in ns["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]


def compute(ctx_by_tag, f2_out):
    """F.3 逐情境。回傳 {tag: {tables, anchors}}。"""
    out = {}
    for tag, c in ctx_by_tag.items():
        ns, snap, cb_by, cad = c["ns"], c["snap"], c["cb_by"], c["cad"]
        omap = c["omap"]
        fcb = ns["F3_CATEGORY_BURDEN"]
        gof = lambda p: omap.get(p, "")
        zof = snap["財務接線_v3"]["原地號_區段"]
        pre_price = {z: float(v["單價_元每m2"]) for z, v in
                     snap["財務接線_v3"]["重劃前區段_面積單價"].items()}
        cls = cad.get("centerlines", {}) or {}
        mina = wf_f0._mina_by_block(ns, snap, cb_by)
        temp = c["temp"]                       # 全 temp_parcels（含公設，供 poly/分攤登記）

        # trunk C（F.2 終態）
        f2_parcels = f2_out[tag]["f2_parcels"]
        f2ids = {t["暫編地號"] for t in f2_parcels}
        sgC = run_step_g(ns, c["fake_st"], list(cb_by.values()), cad, snap,
                         c["params"], f2_parcels, c["winners"], c["forced"], c["setback"])
        GC = {r["暫編地號"]: float(r["G(㎡)"]) for r in sgC["g_rows"]
              if r.get("推進側別") in ("left", "right")}
        poolC = {l: float(v["池總=幾何剩餘(㎡)"]) for l, v in sgC["pool_diag"].items()}

        # trunk C 建地宗（歸戶 → list）
        bldC = [t for t in temp if fcb.get(t["街廓分類"], "") == "可建築土地"
                and not t.get("_is_ghost_sliver") and t["暫編地號"] in f2ids and t["暫編地號"] in GC]
        gbld = collections.defaultdict(list)
        for t in bldC:
            gbld[gof(t["原地號"])].append(t)
        g_has_bld = set(gbld)

        # 公設筆分派：有建地→F.3 併入；否則→轉 7-4（守衛①）
        pub = [t for t in temp if t["街廓分類"] in ("道路", "鄰里公園")
               and not t.get("_is_ghost_sliver")]
        pub_in = [t for t in pub if gof(t["原地號"]) in g_has_bld]
        pub_74 = [t for t in pub if gof(t["原地號"]) not in g_has_bld]

        # ── F.3 變換：a′ 灌入 trunk C 建地 ──
        inj = collections.defaultdict(float)
        conv_rows, audit_sum = [], 0.0
        for tp in sorted(pub_in, key=lambda x: x["暫編地號"]):
            pid = tp["暫編地號"]; gid = gof(tp["原地號"]); z = zof[tp["原地號"]]
            a_reg = float(tp.get("分攤登記面積_m2", 0) or 0)   # §142 基準（非幾何）
            kind = "RD" if tp["街廓分類"] == "道路" else "PF"
            if pid in STRADDLE:                                # 五則① 切半
                p = _poly_of(temp, pid); ln = LineString(cls[tp["所屬街廓"]])
                pieces = list(_shsplit(p, ln).geoms)
                if len(pieces) != 2:                           # 守衛②
                    raise RuntimeError(f"🔴 五則① {pid} CENTERLINE 切非 2 片（{len(pieces)}）")
                for half in pieces:
                    s = _side(cls[tp["所屬街廓"]], (half.centroid.x, half.centroid.y))
                    a_half = a_reg * half.area / p.area
                    sb = [b for b in gbld[gid]
                          if _side(cls[tp["所屬街廓"]],
                                   (_poly_of(temp, b["暫編地號"]).centroid.x,
                                    _poly_of(temp, b["暫編地號"]).centroid.y)) == s]
                    cand = {gid: sb} if sb else gbld
                    tgt, why = _cascade(temp, half, tp["原地號"], gid, cand, GC)
                    ap = round(a_half * pre_price[z] / pre_price[zof[tgt["原地號"]]], 2)
                    inj[tgt["暫編地號"]] += ap; audit_sum += ap
                    conv_rows.append({"情境": tag, "公設筆": f"{pid}·半{s}", "類": kind, "五則": "①切半",
                                      "歸戶": gid, "源zone": z, "a分攤(㎡)": round(a_half, 2),
                                      "目標宗": tgt["暫編地號"], "目標街廓": tgt["所屬街廓"],
                                      "a′(㎡)": ap, "targeting": why})
            else:                                              # 五則③集中 / PF
                tgt, why = _cascade(temp, _poly_of(temp, pid), tp["原地號"], gid, gbld, GC)
                ap = round(a_reg * pre_price[z] / pre_price[zof[tgt["原地號"]]], 2)
                inj[tgt["暫編地號"]] += ap; audit_sum += ap
                五則 = "③集中" if kind == "RD" else "PF併入"
                conv_rows.append({"情境": tag, "公設筆": pid, "類": kind, "五則": 五則,
                                  "歸戶": gid, "源zone": z, "a分攤(㎡)": a_reg,
                                  "目標宗": tgt["暫編地號"], "目標街廓": tgt["所屬街廓"],
                                  "a′(㎡)": ap, "targeting": why})

        # 灌入 → trunk D
        f3_parcels = copy.deepcopy(f2_parcels)
        bid = {t["暫編地號"]: t for t in f3_parcels}
        for tid, add in inj.items():
            bid[tid]["面積_m2"] = round(float(bid[tid].get("面積_m2", 0) or 0) + add, 2)
        sgD = run_step_g(ns, c["fake_st"], list(cb_by.values()), cad, snap,
                         c["params"], f3_parcels, c["winners"], c["forced"], c["setback"])
        D = {r["暫編地號"]: r for r in sgD["g_rows"] if r.get("推進側別") in ("left", "right")}
        g_tab, _, _ = build_step_g_tables(sgD)
        poolD = {l: float(v["池總=幾何剩餘(㎡)"]) for l, v in sgD["pool_diag"].items()}
        verdD = {l: v["判定"] for l, v in sgD["pool_diag"].items()}

        # 池三則（無塊落 (0,MinA)）
        mid = [l for l in poolD if 0 < poolD[l] < mina[l]]
        if mid:
            raise RuntimeError(f"🔴 [{tag}] 停機：池落 (0,MinA)：{mid}")

        # 轉 7-4 表
        to74_rows = [{"情境": tag, "公設筆": t["暫編地號"], "類": ("RD" if t["街廓分類"] == "道路" else "PF"),
                      "歸戶": gof(t["原地號"]), "a分攤(㎡)": round(float(t.get("分攤登記面積_m2", 0) or 0), 2),
                      "處置": "轉 7-4（歸戶於 trunk C 無建地；F.4 調配）"}
                     for t in sorted(pub_74, key=lambda x: x["暫編地號"])]

        # 池流向
        srcset = set()   # F.3 無跨街廓源（純灌入目標塊）
        tgtset = {D[t]["所屬街廓"] for t in inj}
        pool_rows = [{"情境": tag, "街廓": l, "角色": ("目標" if l in tgtset else "未動"),
                      "池_C(㎡)": round(poolC[l], 2), "池_D(㎡)": round(poolD[l], 2),
                      "池差(㎡)": round(poolD[l] - poolC[l], 2), "MinA": mina[l],
                      "三則": ("歸零" if poolD[l] < 1 else "≥MinA")}
                     for l in sorted(poolD)]

        # 位次序（投影序）不變（公設純灌入、無移除；目標宗變寬後宗前移，序不變）
        pos_viol = []
        for blk in sorted({t["所屬街廓"] for t in bldC}):
            oC = _proj_order(ns, cad, f2_parcels, blk)
            oD = _proj_order(ns, cad, f3_parcels, blk)
            if oC != oD:
                pos_viol.append((blk, oC, oD))

        # 628-18(2) 舊帳重測
        a18 = float(D[ANCHOR_628_18["tgt"]]["a 面積(㎡)"]) if ANCHOR_628_18["tgt"] in D else None

        anchors = {
            "n_pub": len(pub), "n_in": len(pub_in), "n_74": len(pub_74),
            "n_inject_items": len(conv_rows), "n_targets": len(inj),
            "verdict_all_green": all("🔴" not in str(v) for v in verdD.values()),
            "pos_viol": pos_viol, "audit_sum": round(audit_sum, 2),
            "a_628_18_2": round(a18, 2) if a18 is not None else None,
            "straddle": sorted(t["暫編地號"] for t in pub_in if t["暫編地號"] in STRADDLE),
            "groups_74": sorted({gof(t["原地號"]) for t in pub_74}),
            "cons_resid": round(abs(sum(float(r["G(㎡)"]) for r in D.values())
                                    + sum(poolD.values()) - 22803.33), 2),
        }
        out[tag] = {"conv_rows": conv_rows, "to74_rows": to74_rows, "g_tab": g_tab,
                    "pool_rows": pool_rows, "anchors": anchors}
    return out


def fixture_cross_zone_f3(snap):
    """跨區段 fixture（守衛④）：合成 a→b RD 公設筆 a′，斷言 ratio≠1（同 F.2 前例）。"""
    pre = {z: float(v["單價_元每m2"]) for z, v in snap["財務接線_v3"]["重劃前區段_面積單價"].items()}
    a = 100.0
    ap = round(a * pre["a"] / pre["b"], 4)
    return {"a": a, "a_prime_a_to_b": ap, "expect": round(a * pre["a"] / pre["b"], 4),
            "ratio_ne_1": abs(ap - a) > 1.0}
