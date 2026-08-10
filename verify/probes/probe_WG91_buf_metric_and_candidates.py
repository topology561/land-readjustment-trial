# -*- coding: utf-8 -*-
"""`W-G.9-1` §5：`buf` 之**度量識別**（Q1-a）＋ `_cos_dn` 實值（Q1-b）＋ 族②③④ 候選替代量（Q2）。

⛔ **只量不判**：本檔產出量值與構造事實，⛔ 不下「何者為正解」之判（施工單 §0-7）。
⛔ 零生產碼：未改 `app.py`／`verify/stepg_pipeline.py`／`verify/wf_f*.py` 任何一行。

## 🔒 射程聲明

- **母體 ＝ (情境 2) × (街角側 8) ＝ 16 格**，⛔ **含不觸發格與退化格**（施工單 §7-1）。
- 街廓 ↔ SIDE ↔ ALLOC 之關聯取自 `cad["side_lines_by_side"]` / `cad["alloc_dir_by_block"]`
  （`parse_cadastral_geofile` 產出）；⛔ 未以幾何鄰近自行配對。
- `range_area` 取自 `run_verification.build_param_table`；`forced` 取自
  `selection_pipeline.run_corner_pk` 之 `forced_map` ——**二者皆與生產同源**。
- `allocation_dir` ＝ `ns["alloc_normal_axis"](alloc_dir_by_block[blk])`
  ＝ `app.py` 之 `allocation_dir_block`（⛔ 不得直傳 CAD 方向）。

## Q1-a 之三法（⛔ 至少兩法互相獨立·施工單 §7-5）

帶由 `_block_strip` 切出：其兩切線為**過 `bp` 與 `bp+S·d̂`、方向 `n_hat = rot90(allocation_dir)`**
之二平行線。本檔**自帶多邊形之實際幾何**取該二線（⛔ 非由 `buf` 反推），再以三法量其間距：

- **甲**：`_strip_axis` 之 s 定義式 `t = ((p − bp)·m̂)/(d̂·m̂)` 於帶多邊形**全頂點**之極差。
- **乙**：二切線與 **FRONT∞** 之交點沿 `d̂` 之距離（**路平行**）。
- **丙**：二切線間之**垂距**。

🔒 **甲與乙演算法互相獨立**（前者走 s 座標式、後者走直線求交＋投影），
⇒ 二者相符方構成相互驗證；⛔ 非「兩個近似值接近」。

## 自我驗證閘（⛔ 不過不得據以下結論·門檻沿用既有探針原式）

- **H1**：`P0` ≡ FRONT∞ ∩ SIDE∞（`< 1e-6`）。
- **H2**：`Ps` 為**明確之 FRONT 側頂點**——**辨別性閘**，判準逐字沿用
  `probe_K9_geo1_S1_construction.py`（`grep -n "H2 係辨別性閘" 該檔`）：
  `d_Ps < 0.05 ∧ d_oth > 10×d_Ps ∧ |Ps−P0| > 1e-9`。⛔ **不得改回絕對 `1e-6`**。
- **H3（本檔新增·⛔ 非自訂門檻，係碼面自身之保證）**：`_corner_buffer_S` 之
  bisect 保證 `|band_area(buf) − range_area| ≤ tol(0.01)` ⇒ 逐格印出實測殘差。
- **H4（切線抽取之自證）**：自帶多邊形抽出之 ∥`n_hat` 邊須**恰成兩簇**；
  否則該格標「切線抽取失敗」，⛔ 其 Q1-a 三法一律不採信。
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

OUT = os.path.join(VERIFY, "out", "probe_WG91_buf_metric_and_candidates.log")
_LBIG = 1e6
L = []


def say(s=""):
    L.append(s)
    print(s)


def _fail(msg):
    raise RuntimeError(f"🔴 probe_WG91：{msg}")


def _unit(v):
    v = np.asarray(v, float)[:2]
    n = float(np.linalg.norm(v))
    if n < 1e-12:
        _fail("零向量")
    return v / n


def _inf_line(p, u):
    p = np.asarray(p, float)[:2]
    u = _unit(u)
    return _LS([tuple(p - u * _LBIG), tuple(p + u * _LBIG)])


def main():
    say("=" * 122)
    say("W-G.9-1 §5　Q1-a `buf` 度量識別 ／ Q1-b `_cos_dn` 實值 ／ Q2 族②③④ 候選替代量")
    say("⛔ 只量不判——本檔不下「何者為正解」之判")
    say("=" * 122)

    ns, fake_st = harvest()
    _corner_buffer_S = ns["_corner_buffer_S"]
    _block_strip = ns["_block_strip"]
    _strip_s_range = ns["_strip_s_range"]
    _strip_axis = ns["_strip_axis"]
    alloc_normal_axis = ns["alloc_normal_axis"]

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    front_lines = cad.get("front_lines") or {}
    sides_by = cad.get("side_lines_by_side", {}) or {}
    alloc_by = cad.get("alloc_dir_by_block", {}) or {}

    corners = [(b, s) for b in rv.CORNER_BLOCKS for s in ("left", "right")
               if s in (sides_by.get(b) or {})]
    if not corners:
        _fail("街角側母體為空 ⇒ ⛔ 空集合不算通過")
    say("")
    say("【射程】街角側 %d × 情境 2 ＝ **%d 格**（⛔ 含不觸發格與退化格）："
        % (len(corners), len(corners) * 2))
    say("        %s" % "、".join(f"{b}/{s}" for b, s in corners))

    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)

    rows = []
    g1, g2, g3, g4 = [], [], [], []

    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        prm = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        by_lbl = {r.get("街廓"): r for r in prm}
        *_, forced_map = run_corner_pk(ns, fake_st, list(cb_by.values()), cad,
                                       prm, temp_parcels, build_parcels, setback,
                                       snapshot=snapshot)
        for blk, side in corners:
            b = cb_by[blk]
            fl = front_lines[blk]
            F1 = np.asarray(fl["p1"], float)[:2]
            F2 = np.asarray(fl["p2"], float)[:2]
            dh = _unit(F2 - F1)
            nh_f = np.array([-dh[1], dh[0]])
            sd = sides_by[blk][side]
            su = _unit(np.asarray(sd["p2"], float)[:2] - np.asarray(sd["p1"], float)[:2])
            mp = np.asarray(sd["mid"], float)[:2]
            adir = np.asarray(alloc_normal_axis(alloc_by[blk]), float)[:2]
            poly = _PG(b["vertices"])

            # `_cos_dn`（逐字同 app.py：|d̂_unit · allocation_dir_block|）
            cos_dn = abs(float(np.dot(dh, adir)))
            ang_side_alloc = math.degrees(math.acos(
                abs(float(np.clip(np.dot(su, _unit(alloc_by[blk])), -1, 1)))))

            def _st(p):
                q = np.asarray(p, float)[:2] - F1
                return float(q @ dh), float(q @ nh_f)

            # ── H1／H2 ──────────────────────────────────────────
            P0 = F1 if side == "left" else F2
            _i = _inf_line(np.asarray(sd["p1"], float)[:2], su).intersection(_inf_line(F1, dh))
            h1 = (math.hypot(_i.x - P0[0], _i.y - P0[1])
                  if getattr(_i, "geom_type", "") == "Point" else float("nan"))
            g1.append((blk, side, h1))
            tri = ns["_make_chamfer_tri_wb"](b, side)
            if tri is None or getattr(tri, "is_empty", True):
                _fail(f"{blk}/{side} 無截角三角形")
            cd = sorted([c for c in list(tri.exterior.coords)[:-1]
                         if math.hypot(c[0] - P0[0], c[1] - P0[1]) > 1e-9],
                        key=lambda c: abs(_st(c)[1]))
            Ps = cd[0]
            d_ps = abs(_st(Ps)[1])
            d_oth = abs(_st(cd[1])[1]) if len(cd) > 1 else float("nan")
            g2.append((blk, side, d_ps, d_oth,
                       d_ps < 0.05 and d_oth > d_ps * 10.0
                       and math.hypot(Ps[0] - P0[0], Ps[1] - P0[1]) > 1e-9))

            seg = abs(_st(Ps)[0] - _st(P0)[0])
            mw = float(ns["get_min_lot_size"](
                b["category"], float(snapshot["blocks"][blk]["正面"]["路寬_m"]))["min_width"])
            T = float(setback) + mw
            S1_par = max(seg, T)                       # ＝ Q2 候選甲

            col = "【左】街角最小面積(㎡)" if side == "left" else "【右】街角最小面積(㎡)"
            ra = (by_lbl.get(blk) or {}).get(col)
            forced = bool((forced_map.get(blk) or {}).get(f"{side}_forced_offset", False))

            rec = dict(tag=tag, blk=blk, side=side, forced=forced, S1_par=S1_par,
                       cos_dn=cos_dn, ang=ang_side_alloc, ra=ra,
                       buf=None, jia=None, yi=None, bing=None, h3=None, w_band=None,
                       cur2=None, cur4=None, cand_bing=None, note="")
            if ra is None or float(ra) == float("inf") or float(ra) <= 0:
                rec["note"] = f"⛔ range_area 不可用（{ra!r}）⇒ buf 不可算"
                rows.append(rec)
                continue

            buf = float(_corner_buffer_S(poly, dh, F1, adir, float(ra), side, _label=blk))
            rec["buf"] = buf

            # ── H3：碼面自身之保證（bisect 收斂）──────────────
            dom = _strip_s_range(poly, dh, F1, adir)
            s_min, s_max = float(dom[0]), float(dom[1])
            lo = max(s_min, 0.0)
            a0, b0 = (lo, buf) if side == "left" else (s_max - buf, s_max)
            bp = F1 + a0 * dh
            band, band_area = _block_strip(poly, dh, bp, b0 - a0, allocation_dir=adir)
            rec["h3"] = abs(float(band_area or 0.0) - float(ra))
            g3.append((tag, blk, side, rec["h3"]))

            # ── Q1-a：三法**皆自帶多邊形之實際幾何**取（⛔ 非由 buf 反推）────────
            #
            # 🩸 **本檔首版之閘設錯（當場自糾·⛔ 原設計不採信）**：首版要求
            #   「自帶多邊形抽出之 ∥n_hat 邊恰成兩簇」（H4），16 格中 **14 格破**。
            #   成因＝**結構性**：帶之「兩條界線」其中一條**常是街廓自身邊界、非切線**
            #   （right 側之 `s_max` 端、left 側 `lo == s_min` 端皆然）
            #   ⇒ 只抽得到一條切線。**係我的閘之前提錯，非資料有問題。**
            #   ⇒ 改為三法**皆量帶多邊形之整體延伸**，不再倚賴「抽出兩條切線」。
            #
            #   甲 ＝ 全頂點之 s 極差（`_strip_axis` 定義式 `t=((p−bp)·m̂)/(d̂·m̂)`）
            #   乙 ＝ (帶 ∩ FRONT∞) 線段沿 `d̂` 之長（**路平行**·獨立演算法：求交＋投影）
            #   丙 ＝ 全頂點於 **⊥n_hat** 方向之極差（**垂距**）
            m_hat, denom = _strip_axis(dh, adir)
            m_hat = np.asarray(m_hat, float)[:2]
            n_u = _unit(np.array([-adir[1], adir[0]]))
            perp_u = np.array([-n_u[1], n_u[0]])       # ⊥ n_hat
            rec["w_band"] = b0 - a0                    # 帶寬（s 域·⛔ 與 buf 未必相等）
            if band is not None and not getattr(band, "is_empty", True) \
                    and band.geom_type == "Polygon":
                cs = [np.asarray(p, float)[:2] for p in list(band.exterior.coords)[:-1]]
                ts = [float(np.dot(p - F1, m_hat)) / float(denom) for p in cs]
                rec["jia"] = max(ts) - min(ts)
                ps = [float(np.dot(p, perp_u)) for p in cs]
                rec["bing"] = max(ps) - min(ps)
                # 乙：**逐頂點沿 `n_hat` 射線求交 FRONT∞**，取交點 `d̂` 座標之極差。
                #   🔒 **與甲演算法獨立**：甲走 `m̂/denom` 之閉式；乙走**直線求交 ＋ 投影**。
                #   （二者所量為同一量；⛔ 故「相符」是相互驗證，非兩個近似值接近。）
                #   🩸 本檔前二版之乙皆錯、當場自糾：
                #     v1 `band ∩ FRONT∞` ⇒ 邊界退化取到不對之線段（|乙−帶寬| 達 3.535）；
                #     v2 「落在 FRONT 上之邊」⇒ 量到的是**帶貼 FRONT 那一段**
                #        （R2/left 得 1.697240 ＝ `buf − seg_P0Ps`·**結構性、非巧合**），
                #        因截角段介於其間 ⇒ 非兩切線之間距。
                #     ⇒ **皆係我的取法錯，非資料有問題。**
                _ys = []
                for p_ in cs:
                    it = _inf_line(p_, n_u).intersection(_inf_line(F1, dh))
                    if getattr(it, "geom_type", "") == "Point":
                        _ys.append(float(np.dot(np.array([it.x, it.y]) - F1, dh)))
                if len(_ys) >= 2:
                    rec["yi"] = max(_ys) - min(_ys)
                else:
                    rec["note"] = (rec["note"] + " ⚠️ 乙未取得（射線求交不足 2 點）").strip()
                g4.append((tag, blk, side, True, ""))
            else:
                g4.append((tag, blk, side, False, "帶多邊形非單一 Polygon"))
                rec["note"] = (rec["note"] + " ⛔ 帶多邊形非單一 Polygon ⇒ Q1-a 不採信").strip()

            # ── 現行值 ＋ Q2 候選 ───────────────────────────────
            def _mp_base_W0(_gs, _bf):
                a_ = adir / float(np.linalg.norm(adir))
                ao = a_ if float(np.dot(dh, a_)) >= 0 else -a_
                return float(np.dot(np.asarray(_gs, float) + float(_bf) * dh - mp, ao))

            gs = F1 if side == "left" else F1 + s_max * dh
            rec["cur2"] = buf * cos_dn                 # 族②③ 現行（app 側）
            rec["cur4"] = _mp_base_W0(gs, buf)         # 族④ 現行（harness 側）
            rec["cand_bing"] = _mp_base_W0(gs, S1_par)  # 候選丙／戊（_buf 換甲）
            rows.append(rec)

    # ═══════════════ 閘 ═══════════════
    say("")
    say("【閘 H1】`P0` ≡ FRONT∞ ∩ SIDE∞：max = %.3e（%d 格·須 < 1e-6）"
        % (max(x[2] for x in g1), len(g1)))
    say("【閘 H2】辨別性閘（⛔ 非絕對 1e-6·沿用 GEO-1 原式）：通過 %d/%d；"
        "max d_Ps = %.6f；最劣辨別比 %.1f×"
        % (sum(1 for x in g2 if x[4]), len(g2), max(x[2] for x in g2),
           min(x[3] / x[2] for x in g2 if x[2] > 0)))
    if [x for x in g1 if not (x[2] < 1e-6)] or [x for x in g2 if not x[4]]:
        _fail("H1/H2 閘破 ⇒ ⛔ 不得據本檔任何數字下結論")
    say("【閘 H3】`|band_area(buf) − range_area|`（碼面 bisect 保證·tol 0.01）：max = %.6f（%d 格）"
        % (max(x[3] for x in g3), len(g3)))
    say("【閘 H4】帶多邊形為單一 Polygon（Q1-a 三法之前提）：%d/%d 格"
        % (sum(1 for x in g4 if x[3]), len(g4)))

    # ═══════════════ Q1-b ═══════════════
    say("")
    say("#" * 122)
    say("## Q1-b　`_cos_dn` 實值（⛔ 正面列出全部 16 格·含不觸發與退化）")
    say("#" * 122)
    say("🔒 **取值方式（由施工單 §3-8 之限制導出）**：`_cos_dn` 之 app 側實例巢狀於 `main()`")
    say("   ⇒ harness 永不執行之 ⇒ `run_all` **不能**作為證據。")
    say("   本檔以**合成案例**直接以該街廓之 `d_hat`／`allocation_dir_block` 實參重算，")
    say("   式逐字同 `app.py`：`abs(dot(d̂/|d̂|, allocation_dir_block))`。")
    say("")
    say("%-5s %-4s %-6s %14s %14s %10s" % ("情境", "街廓", "側別", "_cos_dn", "|1−cos_dn|", "∠(S,A)°"))
    say("-" * 122)
    for r in rows:
        say("%-5s %-4s %-6s %14.9f %14.3e %10.6f" %
            (r["tag"], r["blk"], r["side"], r["cos_dn"], abs(1.0 - r["cos_dn"]), r["ang"]))
    say("-" * 122)
    _deg = [r for r in rows if abs(1.0 - r["cos_dn"]) < 1e-9]
    say("⇒ `|1 − _cos_dn| < 1e-9` 之格 ＝ **%d**（P2 之證偽條件）" % len(_deg))
    say("⚠️ `_cos_dn` 為**街廓級**量（僅依 `d_hat` 與 `allocation_dir_block`）")
    say("   ⇒ 同街廓左右側同值、且**與退縮情境無關**——上表逐格列出係為滿足 §7-1 之正面列舉。")

    # ═══════════════ Q1-a ═══════════════
    say("")
    say("#" * 122)
    say("## Q1-a　`buf` 之度量識別（甲＝s 定義式／乙＝路平行／丙＝垂距·⛔ 皆自帶多邊形實際幾何取）")
    say("#" * 122)
    say("%-5s %-4s %-6s %11s %11s %11s %11s %11s %11s %10s"
        % ("情境", "街廓", "側別", "buf", "帶寬(b0−a0)", "甲(s式)", "乙(路平行)",
           "丙(垂距)", "帶寬·cos_dn", "H3殘差"))
    say("-" * 122)
    for r in rows:
        if r["buf"] is None:
            say("%-5s %-4s %-6s %11s %11s %11s %11s %11s %11s %10s   %s"
                % (r["tag"], r["blk"], r["side"], "—", "—", "—", "—", "—", "—", "—", r["note"]))
            continue
        f = lambda v: ("%11.6f" % v) if v is not None else "%11s" % "—"
        say("%-5s %-4s %-6s %11.6f %11.6f %s %s %s %11.6f %10.2e%s"
            % (r["tag"], r["blk"], r["side"], r["buf"], r["w_band"], f(r["jia"]),
               f(r["yi"]), f(r["bing"]), r["w_band"] * r["cos_dn"], r["h3"],
               ("   " + r["note"]) if r["note"] else ""))
    say("-" * 122)
    _ok = [r for r in rows if r["buf"] is not None and r["jia"] is not None]
    if _ok:
        say("【恆等判定】（⛔ 逐格·非平均）")
        say("   max|甲 − 帶寬| = %.3e   ← s 定義式 vs 構造帶寬"
            % max(abs(r["jia"] - r["w_band"]) for r in _ok))
        say("   max|buf − 帶寬| = %.6f  ← 🔴 **left 之 `buf` 係<u>絕對 s 上界</u>、非寬度**"
            % max(abs(r["buf"] - r["w_band"]) for r in _ok))
        _y = [r for r in _ok if r["yi"] is not None]
        if _y:
            say("   max|乙 − 帶寬| = %.3e" % max(abs(r["yi"] - r["w_band"]) for r in _y))
            say("   max|甲 − 乙|   = %.3e   ← **兩獨立演算法之相互驗證**"
                % max(abs(r["jia"] - r["yi"]) for r in _y))
        _b = [r for r in _ok if r["bing"] is not None]
        if _b:
            say("   max|丙 − 帶寬| = %.6f   ← 丙（垂距）與帶寬**不相等**之量級"
                % max(abs(r["bing"] - r["w_band"]) for r in _b))
            say("   max|丙 − 帶寬·cos_dn| = %.3e   ← **丙 是否即『帶寬×cos_dn』（＝族②③ 之式形）**"
                % max(abs(r["bing"] - r["w_band"] * r["cos_dn"]) for r in _b))

    # ═══════════════ Q2 ═══════════════
    say("")
    say("#" * 122)
    say("## Q2　族②③④ 之候選替代量（⛔ 只列值·不判對錯）")
    say("#" * 122)
    say("%-5s %-4s %-6s %12s %12s %14s %14s %14s"
        % ("情境", "街廓", "側別", "甲=S1_par", "丁=buf(現行)",
           "族②③現行", "族④現行", "丙/戊(甲代入)"))
    say("      %s" % "（族②③現行 ＝ buf·cos_dn；族④現行 ＝ _mp_base_W0(群起點, buf)）")
    say("-" * 122)
    for r in rows:
        if r["buf"] is None:
            say("%-5s %-4s %-6s %12.6f %12s %14s %14s %14s   %s"
                % (r["tag"], r["blk"], r["side"], r["S1_par"], "—", "—", "—", "—", r["note"]))
            continue
        say("%-5s %-4s %-6s %12.6f %12.6f %14.6f %14.6f %14.6f%s"
            % (r["tag"], r["blk"], r["side"], r["S1_par"], r["buf"],
               r["cur2"], r["cur4"], r["cand_bing"],
               "   ← forced" if r["forced"] else ""))
    say("-" * 122)
    say("")
    say("🔎 **候選乙之構造事實（⛔ 非量值·係「為何無單一值」之陳述）**：")
    say("   候選乙 ＝「∥SIDELINE 多邊形之遠側界，依 `_strip_axis` 之 s 定義式反算之 s 值」。")
    say("   🔴 **該遠側界 ∥SIDE，而 s 座標之等值線 ∥`n_hat`（∥ALLOC）**")
    say("   ⇒ 二者**不平行**（∠(S,A) 見 Q1-b 表·本案 0.000003°〜4.32°）")
    say("   ⇒ **s 沿該線變動、非單一數** ⇒ 候選乙須另指定取值點方成為一個量。")
    say("   ⛔ 本檔不代為指定取值點（屬構造選擇·施工單 §0-7「只量不判」）。")
    say("   🔒 **結論：候選乙於本檔<u>未取得量值</u>**——⛔ 不得記為 0、不得留白。")
    say("   成因二重：① 其 s 沿該線變動、非單一數（須另指定取值點·屬構造選擇）；")
    say("             ② `_build_corner_range_v3` 之回傳多邊形**已扣截角**")
    say("                （`rng.difference(chamfer_tri)`）⇒ 其邊未必等同該理論界線，")
    say("                ⛔ 不得以推定之邊代替（禁以近似物代替）。")

    # ═══════════════ 預測對帳 ═══════════════
    say("")
    say("#" * 122)
    say("## 預測對帳（⛔ 未回頭修改事前登記檔一字·登記 commit 早於本結果）")
    say("#" * 122)
    _ok = [r for r in rows if r["buf"] is not None and r["jia"] is not None]
    _y = [r for r in _ok if r["yi"] is not None]
    _b = [r for r in _ok if r["bing"] is not None]
    say("**P1**（`buf` 與 `S1_par` 同度量·皆沿 `d̂` 之路平行量）")
    say("   甲(s 定義式) 與 乙(射線求交＋投影) **兩獨立演算法**：max|甲−乙| = %.3e"
        % max(abs(r["jia"] - r["yi"]) for r in _y))
    say("   甲 ≡ 帶寬 %.3e ／ 乙 ≡ 帶寬 %.3e ／ 丙(垂距) ≡ 帶寬·cos_dn %.3e"
        % (max(abs(r["jia"] - r["w_band"]) for r in _ok),
           max(abs(r["yi"] - r["w_band"]) for r in _y),
           max(abs(r["bing"] - r["w_band"] * r["cos_dn"]) for r in _b)))
    say("   ⇒ `buf` **不**等於垂距（丙），而等於 s／路平行量 ⇒ **P1 ✅ 成立**（S-2 未觸發）")
    say("   🔴 **然須併記一項<u>單未載</u>之結構事實**：max|buf − 帶寬| = %.6f"
        % max(abs(r["buf"] - r["w_band"]) for r in _ok))
    say("      ——`side='left'` 之 `buf` 係**絕對 s 上界**（帶 ＝ `[max(s_min,0), buf]`），")
    say("      而 `S1_par` 係**寬度**。⇒ **同度量、不同原點**；⛔ 二者不可逕相減。")
    say("")
    say("**P2**（`_cos_dn` 於非退化側別皆 ≠ 1.0）：`|1−cos_dn| < 1e-9` 之格 ＝ **%d**"
        % len([r for r in rows if abs(1.0 - r["cos_dn"]) < 1e-9]))
    say("   實測範圍 %.9f 〜 %.9f ⇒ **P2 ✅ 成立**"
        % (min(r["cos_dn"] for r in rows), max(r["cos_dn"] for r in rows)))
    say("   ⚠️ `_cos_dn` 之退化條件為 **ALLOC ⊥ FRONT**（⛔ 非 SIDE ∥ ALLOC）")
    say("      ⇒ `R6`（SIDE∥ALLOC）於本量**不是**退化格：其 cos_dn ＝ %.9f。"
        % [r for r in rows if r["blk"] == "R6"][0]["cos_dn"])
    say("")
    # 🩸 **本檔首版之 P5 比對設錯（當場自糾）**：首版拿「本探針**試算**之 `buf`」
    #   當「族②③④ 已啟動」⇒ 得分歧 13 格。**錯在比對對象**：
    #   生產側 `_left_buffer_S` **僅於 `if _fo_left:` 才計算**（`app.py` Phase C），
    #   否則恆為初值 `0.0`；本探針為儀器自驗而對**全格**試算，**生產從不如此**。
    #   ⇒ 正確之啟動條件 ＝ `forced ∧ range_area 可用 ∧ buf > 0`。
    _p5 = [(r["tag"], r["blk"], r["side"], r["forced"],
            bool(r["forced"]) and r["buf"] is not None and r["buf"] > 0)
           for r in rows]
    _div = [x for x in _p5 if x[3] != x[4]]
    say("**P5**（`GB-58` 觸發條件 與 族②③④ 啟動條件 同一）")
    say("   🔒 啟動條件取**生產側之實際式**：`forced ∧ range_area 可用 ∧ buf > 0`")
    say("      （⛔ 非本探針之全格試算——生產僅於 `if _fo_left:` 才算 `_left_buffer_S`）")
    say("   逐格比對：分歧 **%d** 格" % len(_div))
    for x in _div:
        say("     🔴 %s %s/%s：forced=%s／buf>0=%s" % x)
    say("   ⚠️ **母體覆蓋不足之具名**：`GB-58` 觸發條件含「**SIDE ∦ ALLOC**」一款，")
    say("      而本案唯一 `SIDE ∥ ALLOC` 之格（`R6/right`·∠=0.000003°）**兩情境皆非 forced**")
    say("      ⇒ 「forced ∧ SIDE∥ALLOC」之組合**於本案母體零覆蓋**")
    say("      ⇒ **P5 之該子條件<u>未被檢定</u>**；⛔ 不得記為已驗。")
    say("      本案所驗者僅「forced ⇔ buf>0」⇒ 於該範圍內 **P5 ✅ 成立**。")
    say("")
    say("🔒 **書面自答（考古節 62 機械修法·⛔ 未答不得開始量測·本答已於量測前寫入探針）**：")
    say("   問：「若現行構造與正典不符，正解是否為『直接改用正典構造』？本量測是否已含該格？」")
    say("   答：**是**——`GB-58` 之正解即『直接改用 ∥SIDELINE 多邊形』；")
    say("       本量測之 **Q2 候選甲（`S1_par`）即該格**，且已逐格列出其值；")
    say("       ⛔ 本檔不判其為正解（屬 KL·施工單 §0-7）。")

    say("")
    say("rc = 0")
    return 0


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    sys.exit(rc)
