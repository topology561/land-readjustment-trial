# -*- coding: utf-8 -*-
"""
W-F F.0 — 前置與級0/0'（同街廓同歸戶合併）＋梯3 二群釋池。行為波第一子波。

**架構＝雙 trunk**（KL 裁定 2026-07-10、reviewer 複審後）：
  trunk A（v3 錨）：原 build_parcels → run_step_g，對拍 baselines/v3/（證基礎引擎零漂移）。
  trunk B（F.0 終態）：deepcopy build_parcels → F.0 變換 → run_step_g，對拍 baselines/wf/f0/。
本檔 additive-only：**不改 app.py、不改 stepg_pipeline 推進機、不碰 build_ownership 指紋**。
解算一律走 app 真函式 run_step_g（F.0 僅為 Step G 前之 parcels 資料變換）。

**KL 正典（位相不變＝原位次序不變，2026-07-10）**：集中合併時，標的宗於原位次原地變寬，
變寬面積以調配池結算；標的宗左右毗鄰不變；全體剩餘宗相對位次序不變。同街廓合併中被併宗消失
使其原鄰居重新接鄰＝幾何必然、非違規；判準只看標的宗鄰居＋全體位次序（**投影序**，k*-無關）。
§8：斜交街廓＋solve_G_binary 幾何驅動下平移致不動點微移（0.01–1.02㎡）為法定公式內生、非 bug；
逐宗 G 凍結閘刪除（reviewer BLOCKED#1）。

**級0/0'（先併再判，不停機）**：
  達標宗 = G_i ≥ MinA_blk 且無畸零旗標。
  有達標宗 → 級0：標的=達標宗 G 最大者；被併=全部未達標宗。
  無達標宗 → 級0'：標的=全格 G 最大者；被併=其餘。
  合併＝標的宗.面積_m2 += Σ(被併宗 a)（a′ 累加器；分攤登記面積_m2 唯讀）→ run_step_g 對 Σa 重解。
  合併後仍不達標＝標旗轉出（G009→F.2、G014→F.4；停機#4「下一級」＝§7 全鏈），不停機。
tie-break：標的=G 最大者，並列取暫編地號字典序最小（決定性）。

**梯3 二群釋池**：G025（628-53(1)@R6、628-53(2)@R5）＋G030（628-27(1)@R2、628-27(2)@R3）＝57.48㎡，
  不配地、自 parcels 移除、G 全額由池吸收。
"""
import os
import sys
import csv
import json
import copy

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from app_harvest import harvest                    # noqa: E402
import run_verification as rv                       # noqa: E402
from selection_pipeline import (                    # noqa: E402
    build_ownership, build_build_parcels, run_corner_pk)
from stepg_pipeline import run_step_g, build_step_g_tables  # noqa: E402

OUTDIR = os.path.join(HERE, "out")
F0DIR = os.path.join(HERE, "baselines", "wf", "f0")

# 梯3 二群（F.0-pre 定；ΣG=57.48㎡，唯一釋池對象）
TIER3_LOTS = ["628-53(1)", "628-53(2)", "628-27(1)", "628-27(2)"]

# 六格 G(Σa) 期望錨（雙情境；步2 自檢「烤值==錨」±0.01）
GSA_EXPECT = {
    "0m":   {"G006": 378.81, "G007": 375.78, "G009": 148.21,
             "G010": 290.02, "G014": 131.67, "G017": 415.96},
    "3.5m": {"G006": 378.80, "G007": 382.54, "G009": 148.21,
             "G010": 293.80, "G014": 133.88, "G017": 415.96},
}
# 合併後不達標之標旗轉出（KL (A) 追認）
ROUTE_OUT = {"G009": "轉F.2(同歸戶R4有達標宗·級1相鄰街廓)",
             "G014": "轉F.4(逃生門·2×G≥MinA_區·7-5≥½增配)"}
MINA_QU = 114.07


def _mina_by_block(ns, snap, cb_by):
    fcb = ns["F3_CATEGORY_BURDEN"]
    m = {}
    for b in cb_by.values():
        if fcb.get(b.get("category", ""), "") == "可建築土地":
            lbl = b["label"]
            d = float(snap["blocks"][lbl]["街廓分配深度_m"])
            mw = float(ns["get_min_lot_size"](
                b["category"], float(snap["blocks"][lbl]["正面"]["路寬_m"]))["min_width"])
            m[lbl] = round(d * mw, 2)
    return m


def _decide(ns, snap, cb_by, omap, g_rows_A, mina):
    """級0/0' 決策（吃 trunk A 之 g_rows）。回傳 decisions[list]。
    每筆＝{gid, blk, kind, target, merged[list], zones[set]}。"""
    g = lambda p: omap.get(p, "")
    A = {r["暫編地號"]: r for r in g_rows_A if r.get("推進側別") in ("left", "right")}
    zone_of = snap["財務接線_v3"]["原地號_區段"]
    cell = {}
    for r in A.values():
        cell.setdefault((g(r["原地號"]), r["所屬街廓"]), []).append(r)
    decisions = []
    for (gid, blk), lots in sorted(cell.items()):
        if len(lots) < 2:
            continue
        zones = {zone_of[l["原地號"]] for l in lots}

        def _key(r):   # G 最大；並列取暫編字典序最小
            return (-float(r["G(㎡)"]), r["暫編地號"])
        qual = [l for l in lots
                if float(l["G(㎡)"]) >= mina[blk] and not l["畸零地旗標"].strip()]
        unq = [l for l in lots if l not in qual]
        if not unq:
            kind, target, merged = "全達標·無須併", None, []
        elif qual:
            kind = "級0"
            target = sorted(qual, key=_key)[0]
            merged = unq
        else:
            kind = "級0'"
            target = sorted(lots, key=_key)[0]
            merged = [l for l in lots if l is not target]
        decisions.append({
            "gid": gid, "blk": blk, "kind": kind,
            "target": (target["暫編地號"] if target else None),
            "merged": [l["暫編地號"] for l in merged],
            "zones": sorted(zones),
        })
    return decisions


def _transform(build_parcels, decisions):
    """F.0 變換（deepcopy）：標的宗吞被併宗 a → 面積_m2；移除被併宗＋梯3 4 宗。
    回傳 (f0_parcels, removed_set)。"""
    f0 = copy.deepcopy(build_parcels)
    by_id = {tp["暫編地號"]: tp for tp in f0}
    for d in decisions:
        if not d["target"]:
            continue
        add = 0.0
        for m in d["merged"]:
            add += (float(by_id[m].get("分攤登記面積_m2", 0) or 0)
                    + float(by_id[m].get("面積_m2", 0) or 0))
        t = by_id[d["target"]]
        t["面積_m2"] = round(float(t.get("面積_m2", 0) or 0) + add, 2)
    removed = set(TIER3_LOTS) | {m for d in decisions for m in d["merged"]}
    f0 = [tp for tp in f0 if tp["暫編地號"] not in removed]
    return f0, removed


def _proj_order(ns, cad, parcels, blk):
    """該街廓之投影序（暫編地號 list）。"""
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    pib = [tp for tp in parcels if tp["所屬街廓"] == blk
           and not tp.get("_is_ghost_sliver")]
    return [tp["暫編地號"] for tp in ns["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]


def compute(ctx_by_tag):
    """F.0 逐情境。ctx_by_tag[tag] = {ns, fake_st, cb_by, cad, snap, build,
    params, winners, forced, setback, gA(trunk A g_rows)}。
    回傳 {tag: {...tables, anchors}}。"""
    out = {}
    for tag, c in ctx_by_tag.items():
        ns, snap, cb_by, cad = c["ns"], c["snap"], c["cb_by"], c["cad"]
        omap = c["omap"]
        mina = _mina_by_block(ns, snap, cb_by)
        decisions = _decide(ns, snap, cb_by, omap, c["gA"], mina)

        # 停機閘（決策層；破即 RuntimeError）
        for d in decisions:
            if d["target"] and len(d["zones"]) != 1:
                raise RuntimeError(
                    f"🔴 停機#2 區段不一致：{d['gid']}/{d['blk']} zones={d['zones']}"
                    "（A 折算係數≠1，須域裁 7-4 雙模式）")
        # 停機#3：被併宗 ∩ 街角 winners / forced 保留地
        win_set = {v for w in c["winners"].values()
                   for v in (w.get("p1_end"), w.get("p2_end")) if v}
        forced_set = set()
        for lbl, fo in (c["forced"] or {}).items():
            pass   # forced 保留地為「街廓端」概念，被併宗非保留地本體；winner 交集為主閘
        all_merged = {m for d in decisions for m in d["merged"]}
        _wconf = sorted(all_merged & win_set)
        if _wconf:
            raise RuntimeError(f"🔴 停機#3 被併宗為街角 winner：{_wconf}")

        f0_parcels, removed = _transform(c["build"], decisions)

        # trunk B：F.0 終態（結構不變量永久閘於 run_step_g 內自動適用）
        sgB = run_step_g(ns, c["fake_st"], list(cb_by.values()), cad, snap,
                         c["params"], f0_parcels, c["winners"], c["forced"], c["setback"])
        B = {r["暫編地號"]: r for r in sgB["g_rows"] if r.get("推進側別") in ("left", "right")}
        g_tab, diag_tab, slot_tab = build_step_g_tables(sgB)

        # 六格 G(Σa) 自檢（±0.01；避 #14 刀口）
        gsa = {}
        for d in decisions:
            if not d["target"]:
                continue
            G = float(B[d["target"]]["G(㎡)"])
            gsa[d["gid"]] = G
            exp = GSA_EXPECT[tag].get(d["gid"])
            if exp is not None and abs(G - exp) > 0.01:
                raise RuntimeError(
                    f"🔴 六格錨破：{d['gid']} G(Σa)={G:.2f} ≠ 錨 {exp}（{tag}）")

        # 合併決策表（含 verdict/去向；診斷 Δ 非閘）
        A = {r["暫編地號"]: r for r in c["gA"] if r.get("推進側別") in ("left", "right")}
        dec_rows = []
        for d in decisions:
            if not d["target"]:
                dec_rows.append({"情境": tag, "歸戶": d["gid"], "街廓": d["blk"],
                                 "級別": d["kind"], "標的宗": "—", "被併宗": "",
                                 "Σa(㎡)": "", "G(Σa)(㎡)": "", "MinA_街廓": mina[d["blk"]],
                                 "達標": "—", "去向": "全達標·留置原位", "Δ非線性(㎡)": ""})
                continue
            G = gsa[d["gid"]]
            sa = round(float(B[d["target"]]["a 面積(㎡)"]), 2)
            sG_naive = round(float(A[d["target"]]["G(㎡)"])
                             + sum(float(A[m]["G(㎡)"]) for m in d["merged"]), 2)
            ok = G >= mina[d["blk"]]
            dest = ("達標·留置原位" if ok else ROUTE_OUT.get(d["gid"], "🔴無下一級·停機"))
            dec_rows.append({
                "情境": tag, "歸戶": d["gid"], "街廓": d["blk"], "級別": d["kind"],
                "標的宗": d["target"], "被併宗": ";".join(d["merged"]),
                "Σa(㎡)": sa, "G(Σa)(㎡)": round(G, 2), "MinA_街廓": mina[d["blk"]],
                "達標": ("✅" if ok else "🔴"), "去向": dest,
                "Δ非線性(㎡)": round(abs(G - sG_naive), 2),
            })
            # 停機#4：不達標且無去向
            if not ok and d["gid"] not in ROUTE_OUT:
                raise RuntimeError(
                    f"🔴 停機#4：{d['gid']} 合併後 G(Σa)={G:.2f}<MinA 且無下一級可走（§7 全鏈窮盡）")

        # 旗標消長歸因
        fa = {k for k, r in A.items() if r["畸零地旗標"].strip()}
        fb = {k for k, r in B.items() if r["畸零地旗標"].strip()}
        flag_rows = []
        for k in sorted(fa | fb):
            if k in fa and k in removed:
                cat = "因移除消失"
            elif k in fa and k not in fb:
                cat = "因合併脫旗"
            elif k in fb and k not in fa:
                cat = "新生"
            else:
                cat = "沿用"
            flag_rows.append({"情境": tag, "暫編地號": k, "歸因": cat,
                              "trunkA旗標": ("有" if k in fa else ""),
                              "trunkB旗標": ("有" if k in fb else "")})

        # 位次序不變（投影序，k*-無關；gate#9）＋標的宗毗鄰（KL 具名原則，gate#10）。
        #   毗鄰於**約簡序**（oA 去 block-wide 移除宗）上取——非原序 i±1 濾除（後者丟空、漏 i-2）。
        #   gate#9（oB==約簡序）為序不變之強式，數學上蘊含毗鄰；gate#10 為 KL「標的宗左右毗鄰不變」之具名複述。
        pos_viol, adj_viol = [], []
        blocks = sorted({r["所屬街廓"] for r in A.values()})

        def _nbrs(seq, x):
            k = seq.index(x)
            return seq[max(0, k-1):k] + seq[k+1:k+2]
        for blk in blocks:
            oA = _proj_order(ns, cad, c["build"], blk)
            oB = _proj_order(ns, cad, f0_parcels, blk)
            exp = [x for x in oA if x not in removed]   # 約簡序
            if oB != exp:
                pos_viol.append((blk, exp, oB))
            for d in decisions:
                if d["blk"] != blk or not d["target"]:
                    continue
                nb_exp = _nbrs(exp, d["target"])         # 標的宗於約簡序之左右鄰
                nb_B = _nbrs(oB, d["target"])
                if nb_exp != nb_B:
                    adj_viol.append((d["target"], nb_exp, nb_B))

        # 池差（釋池量＝area_geom；真閘＝池差 baseline）
        poolB = {lbl: round(float(v["池總=幾何剩餘(㎡)"]), 2)
                 for lbl, v in sgB["pool_diag"].items()}
        poolA = {lbl: round(float(v["池總=幾何剩餘(㎡)"]), 2)
                 for lbl, v in c["poolA"].items()}
        pool_rows = [{"情境": tag, "街廓": lbl,
                      "池_v3(㎡)": poolA[lbl], "池_F.0(㎡)": poolB[lbl],
                      "池差(㎡)": round(poolB[lbl] - poolA[lbl], 2)}
                     for lbl in sorted(poolB)]

        kstar = {lbl: v["k*"] for lbl, v in sgB["pool_diag"].items()}
        verd = {lbl: v["判定"] for lbl, v in sgB["pool_diag"].items()}
        out[tag] = {
            "g_tab": g_tab, "diag_tab": diag_tab, "slot_tab": slot_tab,
            "sgB_rows": sgB["g_rows"],   # 🆕 F.1 消費（原始列含 cut_coords；純加性，12 檔 f0 baseline byte 不動）
            "dec_rows": dec_rows, "flag_rows": flag_rows, "pool_rows": pool_rows,
            "decisions": decisions, "removed": sorted(removed), "gsa": gsa,
            "kstar": kstar, "verdict": verd,
            "pos_viol": pos_viol, "adj_viol": adj_viol,
            "n_flag_A": len(fa), "n_flag_B": len(fb),
            "mina": mina,
        }
    return out
