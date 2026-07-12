# -*- coding: utf-8 -*-
"""
W-F F.1 — S=0 碎片遞補形狀調整（域裁 (B)；KL 縮圍裁定 2026-07-11）。

**縮圍 R1**（雙情境錨：0m→628-37(1)、3.5m→628-36(1)，皆該情境左角勝者＝左組第一宗、與楔形相鄰）。
**機制＝等 G 幾何重切＋後續宗前移**（非再跑負擔引擎）：
  標的宗新形 = strip(S′) ∪ 楔形，S′ 由 bisect 解 union.area == G_B（W2：權威量＝union.area）；
  後續左組宗於前移後 baseline 以定面積重切（area == G_B_i，G 精確全等）；右側宗不動；
  釋出之等 G 臨街帶因前移自然接續居中主池（R1 池片 2→1）。
**R3/R6 楔形＝標記制**（裁示 1(b) F.1 段）：標記「待 F.4 終態遞補整形」、零幾何動作——
  其角落失格業主（628-1(2)→F.2、628-42(2)/628-29(1)→F.4）尚未離場，碎片地景屆時重生成
  （規格排序修訂，記 PROVENANCE_F1）。
**Rw/S 負擔欄不重算**：負擔已定讞於 trunk B；F.1 為定負擔後之等面積形狀交換。

停機（RuntimeError）：碎片-標的不相鄰／搜尋結果≠錨／S′×cos_dn < min_width（整形不得製造新畸零）／
重切造成他宗新生畸零／幾何原語自檢破／MultiPolygon（W3）／池片 S=0 殘留（R1）。
additive-only：不改 app.py／stepg／wf_f0 推進機；幾何原語依 stepg 同式重建（W1）＋自檢閘。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np                                   # noqa: E402
from shapely.geometry import Polygon, LineString, Point  # noqa: E402
from shapely.ops import unary_union                  # noqa: E402

TARGET_ANCHOR = {"0m": "628-37(1)", "3.5m": "628-36(1)"}   # KL 裁定錨
WEDGE_AREA_ANCHOR = 5.30                                    # R1 楔形斷言錨（±0.05；量測為準，W2）
PERP_TOL = 0.10


def _seg(dd):
    p1, p2 = (dd or {}).get("p1"), (dd or {}).get("p2")
    return LineString([tuple(p1), tuple(p2)]) if (p1 and p2) else None


def _edge_on(a, b, seg):
    if seg is None or seg.length <= 0:
        return False
    pa, pb = Point(a), Point(b)
    if pa.distance(seg) > PERP_TOL or pb.distance(seg) > PERP_TOL:
        return False
    ta, tb = seg.project(pa), seg.project(pb)
    return min(ta, tb) > -PERP_TOL and max(ta, tb) < seg.length + PERP_TOL


def _front_len_of(poly, fseg, bpoly):
    L = 0.0
    coords = list(poly.exterior.coords)
    for i in range(len(coords) - 1):
        a, b = coords[i], coords[i + 1]
        if Point(a).distance(Point(b)) < 1e-6:
            continue
        mid = Point((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        if mid.distance(bpoly.exterior) >= PERP_TOL:
            continue
        if _edge_on(a, b, fseg):
            L += Point(a).distance(Point(b))
    return L


def _poly_of(row):
    cs = row.get("cut_coords") or []
    if len(cs) < 3:
        return None
    p = Polygon(cs)
    return p if p.is_valid else p.buffer(0)


def _classify_fragments(ns, snap, cb_by, cad, rows_B, forced):
    """trunk B 抵費地列之碎片三分類（wd3 同判準；W-D.3 單一真相源前例）。"""
    flm = cad.get("front_lines", {}) or {}
    alloc = cad.get("alloc_dir_by_block", {}) or {}
    gm = ns["get_min_lot_size"]
    frags = []
    for r in rows_B:
        if r.get("推進側別") != "抵費地":
            continue
        lbl = r["所屬街廓"]
        poly = _poly_of(r)
        if poly is None or poly.is_empty:
            continue
        fseg = _seg(flm.get(lbl))
        bpoly = Polygon(cb_by[lbl]["vertices"])
        if not bpoly.is_valid:
            bpoly = bpoly.buffer(0)
        cen = poly.representative_point()
        s_rel = (fseg.project(Point(cen.x, cen.y)) / fseg.length
                 if (fseg is not None and fseg.length > 0) else None)
        adir = alloc.get(lbl)
        ax, ay = float(adir[0]), float(adir[1])
        nrm = (ax * ax + ay * ay) ** 0.5 or 1.0
        ax, ay = ax / nrm, ay / nrm
        cs = list(poly.exterior.coords)
        depth_a = max(c[0] * ax + c[1] * ay for c in cs) - min(c[0] * ax + c[1] * ay for c in cs)
        width_a = max(c[0] * -ay + c[1] * ax for c in cs) - min(c[0] * -ay + c[1] * ax for c in cs)
        ml = gm(cb_by[lbl]["category"], float(snap["blocks"][lbl]["正面"]["路寬_m"]))
        L_front = _front_len_of(poly, fseg, bpoly)
        fail = (L_front < 0.5) or (width_a < ml["min_width"]) or (depth_a < ml["min_depth"])
        fm = (forced or {}).get(lbl, {})
        at_forced = ((fm.get("left_forced_offset") and s_rel is not None and s_rel < 0.12)
                     or (fm.get("right_forced_offset") and s_rel is not None and s_rel > 0.88))
        if at_forced and width_a >= ml["min_width"]:
            cat = "forced角落鎖定"
        elif fail:
            cat = "碎片"
        else:
            cat = "池主體"
        frags.append({"街廓": lbl, "暫編": r["暫編地號"], "poly": poly,
                      "面積": round(poly.area, 2), "s": s_rel, "三分類": cat})
    return frags


def _bisect_area(fn, target, lo, hi, tol=0.005, iters=80):
    a_hi = fn(hi)
    if a_hi < target - tol:
        raise RuntimeError(f"🔴 bisect 上界不足：fn({hi:.3f})={a_hi:.3f} < 目標 {target:.3f}")
    for _ in range(iters):
        mid = (lo + hi) / 2.0
        a = fn(mid)
        if abs(a - target) <= tol:
            return mid, a
        if a > target:
            hi = mid
        else:
            lo = mid
    mid = (lo + hi) / 2.0
    return mid, fn(mid)


def compute(ctx_by_tag, f0_out):
    """F.1 逐情境。回傳 {tag: {reshape_rows, frag_rows, pool_rows, anchors...}}。"""
    out = {}
    for tag, c in ctx_by_tag.items():
        ns, snap, cb_by, cad = c["ns"], c["snap"], c["cb_by"], c["cad"]
        rows_B = f0_out[tag]["sgB_rows"]
        lots_B = [r for r in rows_B if r.get("推進側別") in ("left", "right")]
        gm = ns["get_min_lot_size"]
        _block_strip = ns["_block_strip"]

        # ── R1 幾何原語重建（W1；stepg 同式） ──
        lbl = "R1"
        blk = cb_by[lbl]
        block_poly = Polygon(blk["vertices"])
        if not block_poly.is_valid:
            block_poly = block_poly.buffer(0)
        fl = (cad.get("front_lines") or {}).get(lbl) or {}
        p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
        L_fl = float(np.linalg.norm(p2 - p1))
        d_hat = (p2 - p1) / L_fl
        corner_pt = p1.copy()
        alloc_dir = ns["alloc_normal_axis"]((cad.get("alloc_dir_by_block") or {}).get(lbl))
        if alloc_dir is None:
            raise RuntimeError("🔴 R1 缺 alloc_dir（宗地分配線），F.1 停")
        cos_dn = abs(float(np.dot(d_hat, np.asarray(alloc_dir, float))))
        mw = float(gm(blk["category"], float(snap["blocks"][lbl]["正面"]["路寬_m"]))["min_width"])
        avg_depth = float(snap["blocks"][lbl]["街廓分配深度_m"])
        # left buffer（通式，依 forced_map；R1 雙情境實為 0 但不寫死）
        fo = (c["forced"] or {}).get(lbl, {}) or {}
        left_buffer_S = 0.0
        if fo.get("left_forced_offset"):
            _ma = fo.get("left_corner_min_area", 0.0)
            left_buffer_S = float(_ma) / avg_depth if avg_depth > 0 else 0.0

        def strip_at(cum_S, S):
            cut, area = _block_strip(block_poly, d_hat,
                                     corner_pt + (left_buffer_S + cum_S) * d_hat,
                                     S, allocation_dir=alloc_dir)
            if cut is None or cut.is_empty:
                return None, 0.0
            if cut.geom_type != "Polygon":
                raise RuntimeError(f"🔴 W3：strip 非單一 Polygon（{cut.geom_type}），R1 幾何異常，停")
            return cut, float(area)

        # ── 碎片三分類（trunk B）＋處置分流 ──
        frags = _classify_fragments(ns, snap, cb_by, cad, rows_B, c["forced"])
        frag_rows, r1_frag = [], None
        for f in [x for x in frags if x["三分類"] == "碎片"]:
            if f["街廓"] == "R1":
                r1_frag = f
                frag_rows.append({"情境": tag, "碎片": f["暫編"], "街廓": "R1",
                                  "面積(㎡)": f["面積"],
                                  "處置": "已整形吞納（域裁(B)：等G重切＋後續宗前移）",
                                  "標的宗": TARGET_ANCHOR[tag]})
            else:
                frag_rows.append({"情境": tag, "碎片": f["暫編"], "街廓": f["街廓"],
                                  "面積(㎡)": f["面積"],
                                  "處置": "標記·待 F.4 終態遞補整形（角落失格業主未離場，KL 裁定 2026-07-11）",
                                  "標的宗": "—"})
        if r1_frag is None:
            raise RuntimeError(f"🔴 [{tag}] trunk B 無 R1 碎片（預期 R1-抵費地-2≈5.30㎡），偵察前提破")
        wedge = r1_frag["poly"]
        if abs(wedge.area - WEDGE_AREA_ANCHOR) > 0.05:
            raise RuntimeError(f"🔴 [{tag}] R1 楔形面積 {wedge.area:.2f} ≠ 錨 {WEDGE_AREA_ANCHOR}±0.05")

        # ── 左組／右組（trunk B 序） ──
        r1_lots = [r for r in lots_B if r["所屬街廓"] == "R1"]
        left = sorted([r for r in r1_lots if r["推進側別"] == "left"],
                      key=lambda x: float(x.get("累積S(m)", 0) or 0))
        right = [r for r in r1_lots if r["推進側別"] == "right"]
        flagged_B = {r["暫編地號"] for r in r1_lots if str(r.get("畸零地旗標", "")).strip()}

        # 搜尋規則（域裁§二）：沿分配序第一筆有效宗（S≠0 且寬≥mw，跳失格）
        target_row, skipped = None, []
        for r in left:
            if (float(r.get("S(m)", 0) or 0) > 0.01
                    and float(r.get("宗地寬度(m)", 0) or 0) >= mw
                    and r["暫編地號"] not in flagged_B):
                target_row = r
                break
            skipped.append(r["暫編地號"])
        if target_row is None or target_row["暫編地號"] != TARGET_ANCHOR[tag]:
            raise RuntimeError(f"🔴 [{tag}] 搜尋標的 {target_row and target_row['暫編地號']} ≠ 裁定錨 "
                               f"{TARGET_ANCHOR[tag]}（跳過 {skipped}）")
        tgt_poly_B = _poly_of(target_row)
        if wedge.distance(tgt_poly_B) >= 0.05:
            raise RuntimeError(f"🔴 [{tag}] 楔形與標的 {TARGET_ANCHOR[tag]} 不相鄰"
                               f"（dist={wedge.distance(tgt_poly_B):.3f}），機制前提破，停")

        # ── 幾何原語自檢（W1，反解式）：bisect 解 strip.area == 幾何面積_B 之 S_chk，
        #    斷言 |S_chk − S_B| ≤ 0.01。（trunk B 之 S_B/幾何面積 皆 2dp 捨入顯示值，
        #    直接以捨入 S 重切會差 ~0.05㎡＝捨入幾何效應非原語不一致——首烤已實證。）──
        S_B = float(target_row["S(m)"])
        G_B = float(target_row["G(㎡)"])
        area_B = float(target_row["幾何面積(㎡)"])
        S_chk, _ = _bisect_area(lambda S: strip_at(0.0, S)[1], area_B, 0.0, S_B + 2.0)
        if abs(S_chk - S_B) > 0.01:
            raise RuntimeError(f"🔴 [{tag}] 原語自檢破：反解 S_chk={S_chk:.4f} ≠ trunk B S_B={S_B}"
                               "（重建幾何與 stepg 不一致）")

        # ── 標的重切：bisect fuse(strip(S′), wedge).area == G_B（W2） ──
        #   楔形＝trunk B 池殘片、已被 stepg `allocated_union.buffer(0.001)` 侵蝕 1mm
        #   → 與 strip 有 1mm 縫、裸 union 成 MultiPolygon（首烤實證）。
        #   閉運算（buffer +0.0011/−0.0011）彌合侵蝕縫成單一 Polygon；縫面積（~0.03㎡）
        #   由 bisect 對 G_B 定面積吸收（本就屬未侵蝕前之真實池楔），正確 by construction。
        def _fuse(a, b):
            u = unary_union([a, b])
            if u.geom_type != "Polygon":
                u = u.buffer(0.0011).buffer(-0.0011)
            return u

        def union_area(S):
            cut, _ = strip_at(0.0, S)
            if cut is None:
                return wedge.area
            return float(_fuse(cut, wedge).area)
        S_new, a_new = _bisect_area(union_area, G_B, 0.0, S_B)
        w_new = S_new * cos_dn                     # 引擎正典宗地寬度（W4）
        if abs(a_new - G_B) > 0.01:
            raise RuntimeError(f"🔴 [{tag}] 標的 G 全等破：union={a_new:.3f} ≠ G_B={G_B}")
        if w_new < mw:
            raise RuntimeError(f"🔴 [{tag}] 停機：標的整形後寬 {w_new:.2f} < min_width {mw}"
                               "（整形不得製造新畸零）")
        cut_new, _ = strip_at(0.0, S_new)
        tgt_shape = _fuse(cut_new, wedge)
        if tgt_shape.geom_type != "Polygon":
            raise RuntimeError(f"🔴 [{tag}] 標的新形非單一 Polygon（{tgt_shape.geom_type}）——"
                               "楔形與 strip 未連續（閉運算後仍斷），停")

        # ── 後續左組宗前移重切（定面積，G 精確全等） ──
        new_polys = {target_row["暫編地號"]: tgt_shape}
        reshape_rows = [{
            "情境": tag, "街廓": "R1", "暫編地號": target_row["暫編地號"], "角色": "標的(吞楔形)",
            "G_B(㎡)": G_B, "新形面積(㎡)": round(float(tgt_shape.area), 2),
            "S_B(m)": S_B, "S_new(m)": round(S_new, 2),
            "宗地寬度_new(m)": round(w_new, 2),
            "實測寬⊥A(m)": round(max(c[0] * -alloc_dir[1] + c[1] * alloc_dir[0]
                                      for c in tgt_shape.exterior.coords)
                                  - min(c[0] * -alloc_dir[1] + c[1] * alloc_dir[0]
                                        for c in tgt_shape.exterior.coords), 2),
            "Δ面積(㎡)": round(float(tgt_shape.area) - G_B, 3),
        }]
        cum = S_new
        for r in left:
            if r["暫編地號"] == target_row["暫編地號"]:
                continue
            G_i = float(r["G(㎡)"])
            S_i_B = float(r["S(m)"])

            def area_i(S, _cum=cum):
                _, a = strip_at(_cum, S)
                return a
            S_i, a_i = _bisect_area(area_i, G_i, 0.0, S_i_B + 2.0)
            if abs(a_i - G_i) > 0.01:
                raise RuntimeError(f"🔴 [{tag}] 前移宗 {r['暫編地號']} G 全等破：{a_i:.3f}≠{G_i}")
            w_i = S_i * cos_dn
            if w_i < mw and r["暫編地號"] not in flagged_B:
                raise RuntimeError(f"🔴 [{tag}] 前移宗 {r['暫編地號']} 新生畸零：寬 {w_i:.2f}<{mw}")
            cut_i, _ = strip_at(cum, S_i)
            new_polys[r["暫編地號"]] = cut_i
            reshape_rows.append({
                "情境": tag, "街廓": "R1", "暫編地號": r["暫編地號"], "角色": "前移",
                "G_B(㎡)": G_i, "新形面積(㎡)": round(float(cut_i.area), 2),
                "S_B(m)": S_i_B, "S_new(m)": round(S_i, 2),
                "宗地寬度_new(m)": round(w_i, 2), "實測寬⊥A(m)": "",
                "Δ面積(㎡)": round(float(cut_i.area) - G_i, 3),
            })
            cum += S_i
        for r in right:   # 右側 byte 不動
            new_polys[r["暫編地號"]] = _poly_of(r)
            reshape_rows.append({
                "情境": tag, "街廓": "R1", "暫編地號": r["暫編地號"], "角色": "右側·未動",
                "G_B(㎡)": float(r["G(㎡)"]), "新形面積(㎡)": round(float(_poly_of(r).area), 2),
                "S_B(m)": float(r["S(m)"]), "S_new(m)": float(r["S(m)"]),
                "宗地寬度_new(m)": float(r["宗地寬度(m)"]), "實測寬⊥A(m)": "",
                "Δ面積(㎡)": "",
            })

        # ── 位次序（投影序）不變 ──
        def _order(polys_by_id):
            pseudo = [{"暫編地號": k, "polygon_coords": list(v.exterior.coords)}
                      for k, v in polys_by_id.items()]
            return [tp["暫編地號"] for tp in ns["_projection_order"](pseudo, fl["p1"], fl["p2"])]
        oB = _order({r["暫編地號"]: _poly_of(r) for r in r1_lots})
        oN = _order(new_polys)
        if oB != oN:
            raise RuntimeError(f"🔴 [{tag}] R1 位次序變動：{oB} → {oN}")

        # ── 池重算（stepg 同式：buffer(0.001) 差集、≥1㎡）＋裁示 1(b) F.1 段 ──
        alloc_union = unary_union(list(new_polys.values())).buffer(0.001)
        pool = block_poly.difference(alloc_union)
        if not pool.is_valid:
            pool = pool.buffer(0)
        pieces = ([g for g in pool.geoms if g.area >= 1.0] if pool.geom_type == "MultiPolygon"
                  else ([pool] if pool.area >= 1.0 else []))
        fseg_r1 = _seg(fl)
        pool_rows, s0_left = [], 0
        for i, g in enumerate(pieces):
            Lf = _front_len_of(g, fseg_r1, block_poly)
            if Lf < 0.5:
                s0_left += 1
            pool_rows.append({"情境": tag, "街廓": "R1", "池片": i + 1,
                              "面積(㎡)": round(g.area, 2), "臨正街長(m)": round(Lf, 2),
                              "S=0殘留": ("是" if Lf < 0.5 else "否")})
        if s0_left:
            raise RuntimeError(f"🔴 [{tag}] 裁示1(b) F.1 段破：R1 仍有 {s0_left} 片 S=0 池片")
        pool_B = next(float(p["池_F.0(㎡)"]) for p in f0_out[tag]["pool_rows"] if p["街廓"] == "R1")
        pool_new = sum(g.area for g in pieces)
        anchors = {
            "target": target_row["暫編地號"], "S_new": round(S_new, 2),
            "w_new": round(w_new, 2), "wedge_area": round(wedge.area, 2),
            "pool_pieces_B": sum(1 for r in rows_B if r.get("推進側別") == "抵費地"
                                 and r["所屬街廓"] == "R1"),
            "pool_pieces_new": len(pieces),
            "pool_B": round(pool_B, 2), "pool_new": round(pool_new, 2),
            "pool_delta": round(pool_new - pool_B, 2),
        }
        out[tag] = {"reshape_rows": reshape_rows, "frag_rows": frag_rows,
                    "pool_rows": pool_rows, "anchors": anchors,
                    # 🆕 G.2 消費（R1 整形新形＋楔形本體座標；純加性·tuple 凍結防 UI 反灌）
                    "reshape_polys": {k: tuple(map(tuple, v.exterior.coords))
                                      for k, v in new_polys.items()},
                    "wedge_coords": tuple(map(tuple, wedge.exterior.coords))}
    return out
