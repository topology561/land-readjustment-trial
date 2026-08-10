# -*- coding: utf-8 -*-
"""D-2b-30 §3-3：**強制抵費地帶寬度 vs 街角規定範圍定寬** — ⛔ 只量不判·零生產碼。

## 量什麼

逐 **街廓 × 側別(left/right) × 退縮情境(0m/3.5m)**：

| 欄 | 內容 |
|---|---|
| A | `S1_par` ＝ `max(線段 P0–Ps, 退縮 ＋ 畸零地最小寬)`（街角規定範圍之**定寬**·∥SIDE 界線） |
| B | `buf` ＝ `_corner_buffer_S` bisect 反解之帶寬（**∥ALLOC** 切線） |
| C | `B − A`（公尺·**全精度·⛔ 不 round**） |
| D | 面積差 ＝ `range_area − band_area(A)`（＝**若誤以 A 充當 buf 會少算之面積**） |
| E | 該街廓該側之 **SIDE 與 ALLOC（`f3_cad_alloc_dir`）夾角**（度） |

⚠️ **A 與 B 同為「沿 FRONTLINE」之量**（`S1_par` 為路平行距·`buf` 為 s 座標量）；
**差別在切線方向**：規定範圍之界線 **∥SIDE**，強制抵費地帶之切線 **∥ALLOC**
（`_block_strip` 之 `n_hat = rot90(allocation_dir)`）。⇒ 二帶等面積**不蘊含**等寬。

## 🔒 射程聲明（§3-3 要求·⛔ 不得以幾何鄰近自行配對）

- **街廓 ↔ SIDE 線 ↔ ALLOC 方向之關聯**，一律取自 CAD 解析層之
  `cad["side_lines_by_side"][blk][side]` 與 `cad["alloc_dir_by_block"][blk]`
  （由 `run_verification.build_pipeline` → `parse_cadastral_geofile` 產出）。
  ⛔ **未以幾何鄰近、buffer 相交或最近距離自行配對**（該法已證會誤配·見 BASELINE 1:N 之戒）。
- **`range_area`** 取自 `run_verification.build_param_table` 之
  `【左/右】街角最小面積(㎡)` 欄——**與生產同源**，⛔ 非本檔自算。
- **強制抵費地之有無**取自 `selection_pipeline.run_corner_pk` 回傳之 `forced_map`
  之 `{side}_forced_offset` ——**與生產同源**（`app.py` Phase C 讀 `f3L_forced_offset` 同鍵）。
- **`allocation_dir`** ＝ `ns["alloc_normal_axis"](alloc_dir_by_block[blk])`
  ——與 `app.py:19294`／`stepg_pipeline.py:434` 之 `allocation_dir_block` **同式**；
  ⛔ 不得直傳 CAD 方向（傳錯即把帶轉 90°）。

## 🔒 自我驗證閘（碼面自身之保證·⛔ 不過不得據以下結論）

- **閘 H1**：`P0` ≡ FRONT∞ ∩ SIDE∞（`K-9-5-4` 之定義）——距 < `1e-6`。
- **閘 H2**：`Ps` 落在 FRONT∞ 上且 `Ps ≠ P0`。
- **閘 R**：`band_area(B) ≈ range_area`（`_corner_buffer_S` 自身之 bisect 保證·tol `0.01`）
  ——本閘同時驗證本檔對 `_band_area` 之複刻**與生產一致**。
- **閘 P3（登記之退化自驗）**：`R6`（`SIDE ∥ ALLOC`）之 `C` 應 ≈ 0；
  若連該格都顯著非 0 ⇒ **本量測有誤、其餘各格一律不得採信**。
  🔒 依 §3-3，`R6` **⛔ 不得作任何結論之通過憑據**。

## 紀律

⛔ 未改 `app.py`／`verify/` 任何生產檔一行；⛔ 不掛 `run_all`；⛔ 不設 `WV_BAKE`。
⛔ **不判定此差是否為缺陷、不改構造、不登記 `GB-xx`、不提修法建議**（`D-2b-30` §3-4）。
rc 恆 0；缺件即 loud raise（no-silent-fallback）。
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import LineString as _LS, Polygon as _PG      # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUT = os.path.join(VERIFY, "out", "probe_D2b30_forced_band_width.log")
_LBIG = 1e6
L = []


def say(s=""):
    L.append(s)
    print(s)


def _fail(msg):
    raise RuntimeError(f"🔴 probe_D2b30：{msg}")


def _unit(v):
    v = np.asarray(v, float)[:2]
    n = float(np.linalg.norm(v))
    if n < 1e-12:
        _fail("零向量")
    return v / n


def main():
    say("=" * 118)
    say("D-2b-30 §3-3　強制抵費地帶寬 `buf` vs 街角規定範圍定寬 `S1_par` — ⛔ 只量不判")
    say("=" * 118)

    ns, fake_st = harvest()
    _corner_buffer_S = ns["_corner_buffer_S"]
    _block_strip = ns["_block_strip"]
    _strip_s_range = ns["_strip_s_range"]
    alloc_normal_axis = ns["alloc_normal_axis"]

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    front_lines = cad.get("front_lines") or {}
    sides_by = cad.get("side_lines_by_side", {}) or {}
    alloc_by = cad.get("alloc_dir_by_block", {}) or {}

    corners = [(lbl, sd) for lbl in rv.CORNER_BLOCKS for sd in ("left", "right")
               if sd in (sides_by.get(lbl) or {})]
    if not corners:
        _fail("取不到任何街角側（side_lines_by_side 全空）⇒ 母體為空·⛔ 不得算通過")
    say("")
    say("【射程】街角側母體 = %d 個：%s"
        % (len(corners), "、".join(f"{b}/{s}" for b, s in corners)))
    say("        關聯來源 = cad['side_lines_by_side'] / cad['alloc_dir_by_block']"
        "（parse_cadastral_geofile）⛔ 非幾何鄰近配對")

    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6_raw = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6_raw, list(cb_by.values()), snapshot)

    rows = []
    gates = {"H1": [], "H2": [], "R": []}

    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        param_rows = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        by_lbl = {r.get("街廓"): r for r in param_rows}
        _diag, _sel, _off, _ws, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad,
            param_rows, temp_parcels, build_parcels, setback, snapshot=snapshot)

        for blk, side in corners:
            b = cb_by[blk]
            fl = front_lines[blk]
            F1 = np.asarray(fl["p1"], float)[:2]
            F2 = np.asarray(fl["p2"], float)[:2]
            dh = _unit(F2 - F1)
            nh = np.array([-dh[1], dh[0]])
            sd = sides_by[blk][side]
            su = _unit(np.asarray(sd["p2"], float)[:2] - np.asarray(sd["p1"], float)[:2])
            au = _unit(np.asarray(alloc_by[blk], float)[:2])
            blk_poly = _PG(b["vertices"])
            adir = alloc_normal_axis(alloc_by[blk])      # ＝ app allocation_dir_block

            # ── E：SIDE 與 ALLOC（f3_cad_alloc_dir）夾角（度·取銳角）──────────
            _cos = abs(float(np.clip(np.dot(su, au), -1.0, 1.0)))
            E = math.degrees(math.acos(_cos))

            # ── P0 / Ps（沿用 GEO-1 探針之法·附 H1/H2 閘）────────────────────
            def _st(p):
                q = np.asarray(p, float)[:2] - F1
                return float(q @ dh), float(q @ nh)

            P0 = F1 if side == "left" else F2
            _i = _LS([tuple(np.asarray(sd["p1"], float)[:2] - su * _LBIG),
                      tuple(np.asarray(sd["p1"], float)[:2] + su * _LBIG)]).intersection(
                 _LS([tuple(F1 - dh * _LBIG), tuple(F1 + dh * _LBIG)]))
            h1d = (math.hypot(_i.x - P0[0], _i.y - P0[1])
                   if getattr(_i, "geom_type", "") == "Point" else float("nan"))
            gates["H1"].append((blk, side, h1d))

            tri = ns["_make_chamfer_tri_wb"](b, side)
            if tri is None or getattr(tri, "is_empty", True):
                _fail(f"{blk}/{side} 取不到截角三角形 ⇒ Ps 不可定義")
            cands = [c for c in list(tri.exterior.coords)[:-1]
                     if math.hypot(c[0] - P0[0], c[1] - P0[1]) > 1e-9]
            cands.sort(key=lambda c: abs(_st(c)[1]))
            Ps = cands[0]
            # 🔒 **H2 為「辨別性閘」·⛔ 非絕對 1e-6**——判準逐字沿用既有 GEO-1 探針
            #   （`grep -n "H2 係辨別性閘" verify/probes/probe_K9_geo1_S1_construction.py`）：
            #   BLOCK 邊與 FRONT_LINE 係**兩個圖層**，實測相距可達 cm 級
            #   ⇒ 本閘問「所取者是否**明確**為 FRONT 側頂點」，⛔ 非「是否恰落在線上」。
            #   ⚠️ 本檔首版誤寫為絕對 `< 1e-6` ⇒ 立即閘破（max 1.483e-02 ＝ `R4` 之
            #      **CAD 圖面既有**落差 `0.014826m`·PROVENANCE §A.2）——**係閘設錯、非資料有問題**，
            #      且與 GEO-1 前版之錯**完全同型**。⛔ 不得自訂門檻。
            d_ps = abs(_st(Ps)[1])
            d_oth = abs(_st(cands[1])[1]) if len(cands) > 1 else float("nan")
            h2_ok = (d_ps < 0.05 and d_oth > d_ps * 10.0
                     and math.hypot(Ps[0] - P0[0], Ps[1] - P0[1]) > 1e-9)
            gates["H2"].append((blk, side, d_ps, d_oth, h2_ok))
            seg_P0Ps = abs(_st(Ps)[0] - _st(P0)[0])

            mw = float(ns["get_min_lot_size"](
                b["category"], float(snapshot["blocks"][blk]["正面"]["路寬_m"]))["min_width"])
            T = float(setback) + mw
            A = max(seg_P0Ps, T)

            col = "【左】街角最小面積(㎡)" if side == "left" else "【右】街角最小面積(㎡)"
            ra = (by_lbl.get(blk) or {}).get(col)
            forced = bool((forced_map.get(blk) or {}).get(f"{side}_forced_offset", False))

            rec = dict(tag=tag, blk=blk, side=side, E=E, seg=seg_P0Ps, T=T, A=A,
                       range_area=ra, forced=forced, B=None, C=None, D=None,
                       s_lo=None, s_hi=None, note="")
            if not forced:
                rec["note"] = "不適用（該側有 WINNER ⇒ 無強制抵費地）"
                rows.append(rec)
                continue
            if ra is None or float(ra) == float("inf") or float(ra) <= 0:
                rec["note"] = f"不適用（range_area={ra!r}）"
                rows.append(rec)
                continue

            B = float(_corner_buffer_S(blk_poly, dh, F1, adir, float(ra), side, _label=blk))

            # ── 複刻生產之 _band_area（⛔ 逐字同式）＋ 閘 R 驗其與生產一致 ────
            _dom = _strip_s_range(blk_poly, dh, F1, adir)
            s_min, s_max = float(_dom[0]), float(_dom[1])
            _lo = max(s_min, 0.0)

            def _band_area(buf):
                a, bb = (_lo, float(buf)) if side == "left" else (s_max - float(buf), s_max)
                w = bb - a
                if w <= 0:
                    return 0.0
                bp = F1 + a * dh
                _g, _ar = _block_strip(blk_poly, dh, bp, w, allocation_dir=adir)
                return float(_ar or 0.0)

            gates["R"].append((blk, side, tag, abs(_band_area(B) - float(ra))))
            rec.update(B=B, C=B - A, D=float(ra) - _band_area(A),
                       s_lo=s_min, s_hi=s_max)
            rows.append(rec)

    # ══════════════ 自我驗證閘 ══════════════
    say("")
    say("【閘 H1】`P0` ≡ FRONT∞ ∩ SIDE∞（須 < 1e-6）： max = %.3e  （%d 格）"
        % (max(d for _, _, d in gates["H1"]), len(gates["H1"])))
    say("【閘 H2】`Ps` 為**明確之 FRONT 側頂點**（辨別性閘·⛔ 非絕對 1e-6·沿用 GEO-1）：")
    say("        判準 = d_Ps < 0.05 ∧ d_oth > 10×d_Ps ∧ |Ps−P0| > 1e-9")
    say("        通過 %d/%d；max d_Ps = %.6f（＝R4 之 CAD 圖面既有落差量級·PROVENANCE §A.2）"
        % (sum(1 for x in gates["H2"] if x[4]), len(gates["H2"]),
           max(x[2] for x in gates["H2"])))
    say("        最劣辨別比 d_oth/d_Ps = %.1f×（須 > 10）"
        % min((x[3] / x[2]) for x in gates["H2"] if x[2] > 0))
    if gates["R"]:
        say("【閘 R 】`band_area(B) == range_area`（tol 0.01）： max|Δ| = %.6f  （%d 格）"
            % (max(d for _, _, _, d in gates["R"]), len(gates["R"])))
    else:
        say("【閘 R 】**無適用格** ⇒ ⛔ 本閘未取得證據（空集合⛔ 不算通過）")
    _bad = [x[:2] for x in gates["H1"] if not (x[2] < 1e-6)] + \
           [x[:2] for x in gates["H2"] if not x[4]]
    if _bad:
        _fail(f"H1/H2 閘破 ⇒ ⛔ 不得據本檔任何數字下結論：{_bad[:3]}")

    # ══════════════ 逐格表 ══════════════
    say("")
    say("【逐格表】鍵 ＝ 側別 ＋ s 區間（⛔ 非宗序號、⛔ 非行號）")
    say("-" * 118)
    say("%-5s %-4s %-6s %-22s %10s %10s %12s %12s %10s"
        % ("情境", "街廓", "側別", "s 區間 [s_min, s_max]", "A=S1_par", "B=buf",
           "C=B−A", "D=面積差", "E=夾角°"))
    say("-" * 118)
    for r in rows:
        sint = ("[%.4f, %.4f]" % (r["s_lo"], r["s_hi"])) if r["s_lo"] is not None else "—"
        if r["B"] is None:
            say("%-5s %-4s %-6s %-22s %10.6f %10s %12s %12s %10.6f   %s"
                % (r["tag"], r["blk"], r["side"], sint, r["A"], "—", "—", "—",
                   r["E"], r["note"]))
        else:
            say("%-5s %-4s %-6s %-22s %10.6f %10.6f %12.6f %12.6f %10.6f"
                % (r["tag"], r["blk"], r["side"], sint, r["A"], r["B"],
                   r["C"], r["D"], r["E"]))
    say("-" * 118)

    # ══════════════ 差集自證 ══════════════
    n_all = len(rows)
    n_app = len([r for r in rows if r["B"] is not None])
    n_na = len([r for r in rows if r["B"] is None])
    say("")
    say("【差集自證】母體 %d ＝ 適用 %d ＋ 不適用 %d，殘差 %d（須 0）"
        % (n_all, n_app, n_na, n_all - n_app - n_na))
    say("            母體 ＝ 街角側 %d × 情境 2 ＝ %d（⛔ 空集合不算通過）"
        % (len(corners), len(corners) * 2))
    if n_app == 0:
        say("🔴 **全部格皆「不適用」** ⇒ 依 §3-3 標為「**未取得證據**」，⛔ 不得記為通過。")
        say("   成因：逐格 note 已具名（該側有 WINNER ⇒ 無強制抵費地）。")

    # ══════════════ R6 退化自驗（⛔ 非通過憑據）══════════════
    say("")
    r6 = [r for r in rows if r["blk"] == "R6" and r["B"] is not None]
    if r6:
        say("【R6 退化自驗】（`SIDE ∥ ALLOC`）⛔ **不得作任何結論之通過憑據**")
        for r in r6:
            say("   · %s R6/%s：E=%.6f°  C=%.6e" % (r["tag"], r["side"], r["E"], r["C"]))
    else:
        say("【R6 退化自驗】R6 無適用格 ⇒ ⛔ **P3 之自我驗證閘未取得證據**"
            "（⇒ 其餘各格之 C 缺少『量測器本身正確』之獨立佐證）")

    # ══════════ 儀器自驗（⛔ 非土地事實·⛔ 不得作任何格之土地結論）══════════
    say("")
    say("=" * 118)
    say("【儀器自驗】🔒 **⛔ 非土地事實**——以下對<u>全部</u> 16 格試算 `buf`（含無強制抵費地者），")
    say("            **僅為驗「量測鏈本身是否正確」**：`SIDE ∥ ALLOC` 時二帶同向 ⇒ `C` 應 ≈ 0。")
    say("            ⛔ 不得據本段主張任何格有強制抵費地、⛔ 不得引為土地後果。")
    say("            成因：`R6` **無適用格** ⇒ 登記之 P3 自驗閘於正表上落空，故另設本段補之。")
    say("-" * 118)
    say("%-5s %-4s %-6s %12s %12s %12s %12s" % ("情境", "街廓", "側別", "A", "buf(試算)", "C", "E=夾角°"))
    say("-" * 118)
    inst = []
    for r in rows:
        b = cb_by[r["blk"]]
        fl = front_lines[r["blk"]]
        F1 = np.asarray(fl["p1"], float)[:2]
        dh = _unit(np.asarray(fl["p2"], float)[:2] - F1)
        adir = alloc_normal_axis(alloc_by[r["blk"]])
        ra = r["range_area"]
        if ra is None or float(ra) == float("inf") or float(ra) <= 0:
            say("%-5s %-4s %-6s %12.6f %12s %12s %12.6f   （range_area 不可用）"
                % (r["tag"], r["blk"], r["side"], r["A"], "—", "—", r["E"]))
            continue
        try:
            bt = float(_corner_buffer_S(_PG(b["vertices"]), dh, F1, adir,
                                        float(ra), r["side"], _label=r["blk"]))
        except Exception as e:                       # noqa: BLE001
            say("%-5s %-4s %-6s %12.6f %12s %12s %12.6f   （試算不可得：%s）"
                % (r["tag"], r["blk"], r["side"], r["A"], "—", "—", r["E"],
                   str(e)[:44]))
            continue
        say("%-5s %-4s %-6s %12.6f %12.6f %12.6f %12.6f%s"
            % (r["tag"], r["blk"], r["side"], r["A"], bt, bt - r["A"], r["E"],
               "   ← 正表適用格" if r["B"] is not None else ""))
        inst.append((r["E"], bt - r["A"], r["blk"], r["side"], r["tag"]))
    say("-" * 118)
    _r6i = [x for x in inst if x[2] == "R6"]
    if _r6i:
        say("🔒 **P3 自驗（儀器層）**：`R6`（E=%.6f°·SIDE∥ALLOC）之 |C| = %.3e"
            % (_r6i[0][0], abs(_r6i[0][1])))
        say("   ⇒ %s"
            % ("✅ ≈0 ⇒ **量測鏈通過退化自驗**（⛔ 仍非土地事實·⛔ 不作通過憑據）"
               if abs(_r6i[0][1]) < 1e-3 else
               "🔴 **顯著非 0 ⇒ 量測鏈有誤，正表各格 C 一律不得採信**"))
    else:
        say("🔴 `R6` 於儀器自驗亦不可得 ⇒ **P3 完全未取得證據**。")
    if len(inst) >= 3:
        _srt = sorted(inst, key=lambda x: x[0])
        say("")
        say("🔎 **P2 之儀器層觀察**（⛔ 非土地事實·⛔ 僅供判斷母體是否具鑑別力）：")
        say("   夾角由小到大 vs |C|：")
        for e_, c_, bl, sd_, tg in _srt:
            say("     E=%10.6f°   |C|=%12.6f   （%s %s/%s）" % (e_, abs(c_), tg, bl, sd_))
    say("=" * 118)

    say("")
    say("⛔ 本檔只量不判：不判定此差是否為缺陷、不改構造、不登記 GB、不提修法建議。")
    say("rc = 0")
    return 0


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    sys.exit(rc)
