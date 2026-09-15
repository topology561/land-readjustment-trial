# -*- coding: utf-8 -*-
"""`W-G.9-295` `§三`：三量之**同次併量**與導出界 `A′`／`B′` 之判。

🔑 **本器明文准設計驗算**（單 `§三-1`）——於 `forced` 消費端以
   `_first_corner_alloc_dir(side_mid)` 取代當場之 `allocation_dir` 複算路丙之帶。
   其一切出艙冠 `【設計驗算·⛔ 非實測】`，**⛔ 與實測之數同表混列**；**⛔ 改生產碼一字**。

🔒 **⛔ 自寫第二套幾何**（單 `§三-1` 逐字）——一切原語皆取自 `ns`：
   `_block_strip`／`_strip_s_range`／`_corner_buffer_S`（其內之 bisect）／`k956_W_from_mp`；
   帶之構造式與 `W_0` 之複刻**逕行復用** `probe_WG9292_pathC` 之 `band_poly`／`_w0` 同式
   （⛔ 另寫一份·`W-G.9-292` 已以自我驗證閘 `(ii)`／`(iii)` 證其與碼面一致）。

🔒 **三量須於<u>同一次執行</u>內併得**（單 `§一-4`：⛔ 跨批轉引）：
   款 `1` `range_area` vs `area(corner_range_polys)` 之**逐位差（含正負號）**；
   款 `2` 路丙之帶與該範圍多邊形之**對稱差**（`甲` ＝ **範圍多邊形**／`乙` ＝ **路丙之帶**·
          🛑 **本單明定·⛔ 互易**——其與 `W-G.9-292` 之指派**相反**，本器逐字採本單）；
   款 `5` `buf′` 所導出之 `W_0′`／`S1_perp`／其差／該格之**跨距**。

🔒 **自我驗證閘**（承 `-292`·⛔ 省）：
   `(i)`  `|S1_par·sinθ − S1_perp| ≤ 1e-9`；
   `(ii)` 以**當場之** `allocation_dir`／`buf` 重建之帶，其面積須 ＝ `range_area`（`|Δ| ≤ tol`）；
   `(iii)` `W_0` 之重建須與包裹所錄之 `k956_W_from_mp` 實際回傳逐位相同（無錄者 **loud 具名不可驗**）。
   🛑 任一不過 ⇒ 該格之數**⛔ 出艙**。

🔒 **跨距之二式並報·取較嚴**（單⛔ 明定其式 ⇒ 依 `常規二`／自解款 `6` 取保守項）：
   `L_su`  ＝ 範圍多邊形之頂點於**切向 `su`**（SIDE 之線向）上之投影跨度；
   `L_edge` ＝ 範圍多邊形之**遠側境界線**（實邊）之長。
   **跨距 ＝ `max(L_su, L_edge)`**（愈大 ⇒ `A′` 之界愈嚴 ⇒ 保守）。

`rc`：`0` 全綠／`5` **量測器紅**（自我驗證閘或判別力三造不成立）／`6` **受詞紅**（導出界逾之）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」——二者之別於出艙處逐字具名。
用法：python verify/probes/probe_WG9295_joint.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import probe_WG9292_pathC as P                      # noqa: E402  （其 module 級已設 sys.path／chdir）

W = 132
TAG = "【設計驗算·⛔ 非實測】"
_LOG = []
RED = [0]
OVER = [0]


def say(s=""):
    print(s)
    _LOG.append(s)


def red(s):
    RED[0] = 5
    say("🔴 **量測器紅**：" + s)


def over(s):
    OVER[0] = 6
    say("🛑 **受詞紅（逾界）**：" + s)


def _w0(ns, gs, buf, dv, mp, adir):
    """`_mp_base_W0` 之**純委派式**（逐字同 `probe_WG9292_pathC.analyse` 之 `_w0`）。"""
    import numpy as np
    if gs is None or mp is None or adir is None or dv is None:
        return 0.0
    dv2 = np.asarray(dv, dtype=float)
    dn = float(np.linalg.norm(dv2))
    du = dv2 / dn if dn > 1e-9 else dv2
    bp0 = np.asarray(gs, dtype=float) + float(buf) * du
    return float(ns["k956_W_from_mp"](bp0, mp, adir, dv))


def _span(geom, u):
    """多邊形頂點於單位向量 `u` 上之投影跨度（max − min）。"""
    u = P._unit(u)
    xs = []
    gs = getattr(geom, "geoms", None)
    for g in (list(gs) if gs is not None else [geom]):
        for (x, y) in list(g.exterior.coords):
            xs.append(x * u[0] + y * u[1])
    return (max(xs) - min(xs)) if xs else None


def analyse(sb, d):
    ns, crp = d["ns"], d["crp"]
    # 🩸 **母體須扣除本器自身之輸出**（`CLAUDE.md`：「量測器之母體若含其自身輸出，自檢會自我污染」）
    #    `P.drive` 所包裹之 `k956_W_from_mp` 仍在 `ns` 內 ⇒ 本器之 `_w0` 呼叫亦會被記入 `d["K956"]`。
    #    ⇒ 閘 `(iii)` 之母體一律限於 **`drive()` 期間所錄之前綴**（＝ 生產路徑之錄）。
    n_k956_0 = len(d["K956"])
    say("")
    say("=" * W)
    say("【`SB` ＝ %s m·態甲（`WV_K6_STEP0` 未設）】"
        "`_build_corner_range_v3` **%d** 次（`run_step_g` 段 **%d**）／"
        "`_corner_buffer_S` **%d** 次（段內 **%d**）／`k956_W_from_mp` **%d** 次"
        % (repr(sb), len(d["RNG"]), len(d["RNG"]) - d["n_rng0"],
           len(d["BUF"]), len(d["BUF"]) - d["n_buf0"], len(d["K956"])))
    say("　`run_step_g` 之終局 ＝ %s" % (d["err"] or "（未拋）"))
    say("　`corner_range_polys` 之鍵 ＝ **%d** 個：%s"
        % (len(crp), sorted("%s/%s" % k for k in crp)))
    say("=" * W)

    grids = []
    for b in P.BLKS:
        L, R = d["fo"][b]
        if L:
            grids.append((b, "left"))
        if R:
            grids.append((b, "right"))
    say("🔒 `forced` 格 ＝ **%d**（%s）" % (len(grids), "、".join("%s/%s" % g for g in grids)))

    rows = []
    for blk, side in grids:
        say("")
        say("─" * W)
        say("### `%s`／`%s`＠`SB = %s`" % (blk, side, repr(sb)))
        br, nb = P._pick(d["BUF"], blk, side)
        rr, nr = P._pick(d["RNG"], blk, side)
        if br is None or rr is None:
            red("`%s/%s`：`_corner_buffer_S` 錄 %d 筆／`_build_corner_range_v3` 錄 %d 筆 ⇒ **loud 拒測**"
                % (blk, side, nb, nr))
            continue
        cp = crp.get((blk, side))
        if cp is None:
            red("`%s/%s`：`corner_range_polys[(%r, %r)]` ⇒ `None` ⇒ **loud 拒測**" % (blk, side, blk, side))
            continue

        loc = rr["loc"]
        S1_perp = float(loc.get("S1_perp"))
        S1_par = float(loc.get("S1_par"))
        sin_t = float(loc.get("_sin_t"))
        Tp = tuple(float(x) for x in loc.get("_Tp"))
        su = (float(loc.get("sux")), float(loc.get("suy")))

        g_i = abs(S1_par * sin_t - S1_perp)
        say("  **自我驗證閘 `(i)`**　`|S1_par·sinθ − S1_perp|` ＝ `%r`（期 ≤ `1e-9`）⇒ %s"
            % (g_i, "✅" if g_i <= 1e-9 else "🔴"))
        if g_i > 1e-9:
            red("`%s/%s`：閘 `(i)` 不過 ⇒ 該格之數⛔ 出艙" % (blk, side))
            continue

        bp_, dh_, fp_ = br["block_poly"], br["d_hat"], br["front_p1"]
        ad1, ra, tol, buf1 = br["allocation_dir"], float(br["range_area"]), br["tol"], br["buf"]

        # ══ 款 1：range_area（實參） vs area(corner_range_polys) ══════════════
        A_poly = float(cp.area)
        k1 = ra - A_poly                                   # **含正負號**：實參 − 實算
        say("  **款 `1`**　`range_area`（實參） vs `area(corner_range_polys[(%r, %r)])`" % (blk, side))
        say("      `range_area`（`_corner_buffer_S` 之實參·當場錄得）＝ `%r`" % ra)
        say("      `area(corner_range_polys)`（當場重得）　　　　　　＝ `%r`" % A_poly)
        say("      🔑 **逐位差（含正負號·實參 − 實算）＝ `%r`**" % k1)

        # ══ 自我驗證閘 (ii) ══════════════════════════════════════════════════
        g1, dom1, ar1 = P.band_poly(ns, bp_, dh_, fp_, ad1, buf1, side)
        ok_ii = (ar1 is not None) and abs(ar1 - ra) <= float(tol)
        say("  **自我驗證閘 `(ii)`**　以**當場之** `allocation_dir`／`buf` 重建之帶：面積 ＝ `%r`／"
            "`|Δ − range_area|` ＝ `%r`（`tol` ＝ `%r`）⇒ %s"
            % (ar1, (None if ar1 is None else abs(ar1 - ra)), tol, "✅" if ok_ii else "🔴"))
        if not ok_ii:
            red("`%s/%s`：閘 `(ii)` 不過 ⇒ 該格之數⛔ 出艙" % (blk, side))
            continue

        sl = ((d["st"].session_state.get("f3_cad_side_lines_by_side", {}) or {})
              .get(blk, {}) or {}).get(side, {}) or {}
        side_mid = sl.get("mid")
        if side_mid is None:
            red("`%s/%s`：`side_mid` ⛔ 可達 ⇒ 路丙之輸入不存在 ⇒ **loud 拒測**" % (blk, side))
            continue

        # ══ 路丙之帶（設計驗算）══════════════════════════════════════════════
        ad2 = ns["_first_corner_alloc_dir"](side_mid)
        say("  %s **路丙之輸入**　`_first_corner_alloc_dir(side_mid)` ＝ `%r`"
            % (TAG, tuple(float(x) for x in ad2)))
        try:
            buf2 = ns["_corner_buffer_S"](bp_, dh_, fp_, ad2, ra, side,
                                          tol=tol, _label="WG9295設計驗算·" + blk)
        except Exception as e:                              # noqa: BLE001
            red("`%s/%s`：%s `_corner_buffer_S` 以路丙之輸入拋出 ⇒ %s" % (blk, side, TAG, e))
            continue
        g2, dom2, ar2 = P.band_poly(ns, bp_, dh_, fp_, ad2, buf2, side)
        if g2 is None:
            red("`%s/%s`：%s 路丙之帶 ⇒ `None` ⇒ **loud 拒測**" % (blk, side, TAG))
            continue
        say("      %s 路丙 `buf′` ＝ `%r`（現行 `buf` ＝ `%r`·差 ＝ `%r`）" % (TAG, buf2, buf1, buf2 - buf1))
        say("      %s 路丙帶面積 ＝ `%r`／`s` 域 ＝ `%r`" % (TAG, ar2, dom2))

        # ══ 款 2：對稱差（🛑 甲 ＝ 範圍多邊形／乙 ＝ 路丙之帶·本單明定）══════
        def _sym(jia, yi):
            if jia is None or yi is None:
                return None, None, None
            a = float(jia.difference(yi).area)
            b = float(yi.difference(jia).area)
            return a, b, a + b

        jy2, yj2, sym2 = _sym(cp, g2)                       # 甲 ＝ cp（範圍）／乙 ＝ g2（路丙帶）
        jy1, yj1, sym1 = _sym(cp, g1)                       # 判別力[必非零]：現行之帶
        jy0, yj0, sym0 = _sym(cp, cp)                       # 判別力[必為零]
        say("  **款 `2`**　對稱差（🛑 **甲 ＝ 範圍多邊形**／**乙 ＝ 路丙之帶**·本單 `§三-2` 明定·⛔ 互易）")
        say("      | 乙 | `甲∖乙` | `乙∖甲` | **對稱差** |")
        say("      |---|---|---|---|")
        say("      | %s 路丙之帶 | `%r` | `%r` | **`%r`** |" % (TAG, jy2, yj2, sym2))
        say("      | 現行之帶（判別力[必非零]） | `%r` | `%r` | **`%r`** |" % (jy1, yj1, sym1))
        say("      | 範圍多邊形自身（判別力[必為零]） | `%r` | `%r` | **`%r`** |" % (jy0, yj0, sym0))

        # ══ 款 3：款 1 之正負號 與 款 2 之孰大 之一致性 ═══════════════════════
        sgn = "＋（實參 > 實算）" if k1 > 0 else ("−（實參 < 實算）" if k1 < 0 else "0")
        big = "`乙∖甲` 大" if yj2 > jy2 else ("`甲∖乙` 大" if jy2 > yj2 else "相等")
        # 期：實參 > 實算 ⇒ 帶（依 range_area 解得）大於範圍 ⇒ `乙∖甲` 大
        exp = "`乙∖甲` 大" if k1 > 0 else ("`甲∖乙` 大" if k1 < 0 else "相等")
        consistent = (big == exp)
        say("  **款 `3`**　款 `1` 之正負號 與 款 `2` 之 `甲∖乙`／`乙∖甲` 孰大之**一致性**")
        say("      款 `1` 之號 ＝ %s；款 `2` 實測 ＝ %s（`甲∖乙` `%r` vs `乙∖甲` `%r`）"
            % (sgn, big, jy2, yj2))
        say("      以「帶之面積 ＝ `range_area`」推之，**期** ＝ %s ⇒ **%s**"
            % (exp, "✅ 一致" if consistent else "🟡 **⛔ 一致（loud 具名·⛔ 判其成因）**"))

        # ══ 款 4：款 2 ÷ 款 1 ════════════════════════════════════════════════
        ratio = (sym2 / abs(k1)) if (k1 != 0 and sym2 is not None) else None
        say("  **款 `4`**　比值 ＝ 款 `2`（對稱差） ÷ `|`款 `1``|` ＝ `%r`／與 `1` 之差 ＝ `%r`"
            % (ratio, None if ratio is None else ratio - 1.0))

        # ══ 款 5：W_0′／S1_perp／跨距 ════════════════════════════════════════
        w0_cur = _w0(ns, fp_, buf1, dh_, side_mid, ad1)
        w0_new = _w0(ns, fp_, buf2, dh_, side_mid, ad2)

        import numpy as _np
        _bp0 = _np.asarray(fp_, dtype=float) + float(buf1) * (
            _np.asarray(dh_, dtype=float) / float(_np.linalg.norm(_np.asarray(dh_, dtype=float))))
        _hit = []
        for r in d["K956"][:n_k956_0]:                  # 🔒 **扣除本器自身之輸出**（見上）
            try:
                p = _np.asarray(r["point"], dtype=float)[:2]
                if float(_np.max(_np.abs(p - _bp0[:2]))) <= 1e-12:
                    _hit.append(r)
            except Exception:                               # noqa: BLE001
                continue
        say("      母體之界：`drive()` 期間之生產錄 ＝ **%d** 筆／本器自身已追加 ＝ **%d** 筆"
            "（**後者⛔ 入母體**）" % (n_k956_0, len(d["K956"]) - n_k956_0))
        if not _hit:
            say("  **自我驗證閘 `(iii)`**　🟡 **不可驗（loud）**——`k956_W_from_mp` 於本格**無生產之錄**"
                "（本 `SB` 之生產錄數 ＝ %d）⇒ 該格之 `W_0` 係本器之重建、**⛔ 經對拍**"
                "（🛑「無從回測」⛔ 等同「回測不過」）" % n_k956_0)
            ok_iii = None
        else:
            _dv = min(abs(float(r["out"]) - w0_cur) for r in _hit)
            ok_iii = (_dv == 0.0)
            say("  **自我驗證閘 `(iii)`**　`W_0` 之重建 vs **生產錄**之實際回傳：錄 %d 筆·最小差 ＝ `%r` ⇒ %s"
                % (len(_hit), _dv, "✅ 逐位相同" if ok_iii else "🔴"))
            if not ok_iii:
                red("`%s/%s`：閘 `(iii)` 不過 ⇒ 該格之 `W_0` ⛔ 出艙" % (blk, side))
                continue

        dW = abs(w0_new - S1_perp)
        L_su = _span(cp, su)
        er, dr = P.far_range_edge(cp, Tp, su)
        L_edge = None if er is None else P._elen(er)
        L = max(x for x in (L_su, L_edge) if x is not None)
        say("  **款 `5`**　`W_0′`／`S1_perp`／跨距")
        say("      現行 `W_0` ＝ `%r`" % w0_cur)
        say("      %s 路丙 `W_0′` ＝ `%r`／`S1_perp` ＝ `%r`／**`|W_0′ − S1_perp|` ＝ `%r`**"
            % (TAG, w0_new, S1_perp, dW))
        say("      跨距（**二式並報·取較嚴 ＝ 較大者**）：`L_su`（頂點於切向 `su` 之投影跨度）＝ `%r`／"
            "`L_edge`（遠側境界線實邊之長）＝ `%r` ⇒ **跨距 ＝ `%r`**" % (L_su, L_edge, L))

        # ══ 款 6：導出界之判（🛑 ⛔ 調界、⛔ 放寬）═══════════════════════════
        B_lim = 0.005
        A_lim = B_lim / L
        okB = (sym2 is not None) and (sym2 <= B_lim)
        okA = (dW <= A_lim)
        say("  **款 `6`**　導出界之判（界由發單側依 `range_area = round(·, 2)` 導出·🛑 ⛔ 調、⛔ 放寬）")
        say("      | 界 | 算式 | 界值 | 實測 | 比值（實測÷界） | 判 |")
        say("      |---|---|---|---|---|---|")
        say("      | `B′` | 對稱差 ≤ `0.005`（`2dp` 捨入之半個 ulp） | `%r` | `%r` | `%r` | %s |"
            % (B_lim, sym2, (None if sym2 is None else sym2 / B_lim), "✅" if okB else "🛑 **逾界**"))
        say("      | `A′` | `\\|W_0′ − S1_perp\\| ≤ 0.005 ÷ 跨距` ＝ `0.005 ÷ %r` | `%r` | `%r` | `%r` | %s |"
            % (L, A_lim, dW, dW / A_lim, "✅" if okA else "🛑 **逾界**"))
        if not okB:
            over("`%s/%s`＠`SB=%s`：`B′` 逾界（對稱差 `%r` > `%r`）" % (blk, side, repr(sb), sym2, B_lim))
        if not okA:
            over("`%s/%s`＠`SB=%s`：`A′` 逾界（`%r` > `%r`）" % (blk, side, repr(sb), dW, A_lim))

        rows.append({"sb": sb, "blk": blk, "side": side, "ra": ra, "A_poly": A_poly, "k1": k1,
                     "jy2": jy2, "yj2": yj2, "sym2": sym2, "sym1": sym1, "sym0": sym0,
                     "cons": consistent, "ratio": ratio, "buf1": buf1, "buf2": buf2,
                     "w0_new": w0_new, "S1_perp": S1_perp, "dW": dW, "L": L,
                     "A_lim": A_lim, "okA": okA, "okB": okB, "g_iii": ok_iii})
    return rows


def main():
    allrows = []
    for sb in P.SBS:
        allrows += analyse(sb, P.drive(sb))

    say("")
    say("=" * W)
    say("## 款 `7`　判別力三造之判（母體 ＝ 上開全部 `forced` 格）")
    say("=" * W)
    n = len(allrows)
    say("   | 造 | 判準 | 實測 | 判 |")
    say("   |---|---|---|---|")
    ok0 = n >= 1
    say("   | （母體） | `forced` 格數 `≥ 1` | **%d** | %s |" % (n, "✅" if ok0 else "🔴"))
    ok1 = ok0 and all(r["sym1"] is not None and r["sym1"] > 0 for r in allrows)
    say("   | [必非零] | **現行** `buf` 之對稱差 `> 0` | %s | %s |"
        % ("／".join(repr(r["sym1"]) for r in allrows), "✅" if ok1 else "🔴"))
    ok2 = ok0 and all(r["sym2"] != r["sym1"] for r in allrows)
    say("   | [必相異] | 路丙之對稱差 **異於**現行者（證款 `2` 非恆值） | %s | %s |"
        % ("／".join("%r vs %r" % (r["sym2"], r["sym1"]) for r in allrows), "✅" if ok2 else "🔴"))
    ok3 = ok0 and all(r["sym0"] == 0.0 for r in allrows)
    say("   | [必為零] | 範圍多邊形與其自身之對稱差 ＝ `0`（先自證可滿足） | %s | %s |"
        % ("／".join(repr(r["sym0"]) for r in allrows), "✅" if ok3 else "🔴"))
    if not (ok0 and ok1 and ok2 and ok3):
        red("判別力三造未全數成立 ⇒ **判器紅、停、上呈**")

    say("")
    say("=" * W)
    say("## 總表（%s·⛔ 與實測之數同表混列）" % TAG)
    say("=" * W)
    say("   | `SB` | 格 | 款 `1` 逐位差 | 款 `2` 對稱差 | 款 `3` 一致 | 款 `4` 比值 | "
        "`\\|W_0′−S1_perp\\|` | 跨距 | `A′` 界 | `A′` | `B′` | 閘 `(iii)` |")
    say("   |---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in allrows:
        say("   | `%s` | `%s/%s` | `%r` | `%r` | %s | `%r` | `%r` | `%r` | `%r` | %s | %s | %s |"
            % (repr(r["sb"]), r["blk"], r["side"], r["k1"], r["sym2"],
               "✅" if r["cons"] else "🟡", r["ratio"], r["dW"], r["L"], r["A_lim"],
               "✅" if r["okA"] else "🛑", "✅" if r["okB"] else "🛑",
               {True: "✅ 逐位相同", False: "🔴", None: "🟡 不可驗（無生產錄）"}[r["g_iii"]]))
    say("")
    say("🛑 **出艙即止**：本器⛔ 判成因是否閉合、⛔ 判路丙成立與否、⛔ 擬實作、⛔ 改碼一字、")
    say("   ⛔ 開分支、⛔ 動用 KL 之放行、⛔ 鑄任何號、⛔ 解除或收窄 `GB-170`、⛔ 提修法主張、⛔ 呈 KL。")
    rc = RED[0] or OVER[0]
    say("🔒 `rc` ＝ `%d`（`5` ＝ **量測器紅**／`6` ＝ **受詞紅（逾界）**·二者⛔ 同義）" % rc)
    say("=" * W)

    out = os.path.join(REPO, "verify", "out", "WG9295R_joint.log")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(_LOG) + "\n")
    print("\n落檔 ⇒ %s" % out)
    return rc


if __name__ == "__main__":
    sys.exit(main())
