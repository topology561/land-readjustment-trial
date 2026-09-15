#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-294` `§三`：`range_area` 之出處與**範圍多邊形實算面積**之逐位差 —— 🛑 **出艙即止**。

🛑 **⛔ 改生產碼一字、⛔ 替身（包裹一律<u>純委派</u>）、⛔ 開分支、⛔ 鑄任何號。**
🛑 **本批⛔ 含設計驗算**（單 `§六`）——本器**⛔ 以任何<u>假設之輸入</u>複算**；
   其所作之「帶之重建」一律用**當場之** `allocation_dir` 與**當場之** `buf`（⇒ **重建**·⛔ 設計驗算）。
🔒 **底本** ＝ `verify/probes/probe_WG9293_tol.py` 之 `drive`（⛔ 另寫第四份驅動）。
🔒 **通道** ＝ harness（`stepg_pipeline.run_step_g`）·**態甲**·`SB ∈ {0.0, 3.5}`。
🔒 **同一性一律 `is` 比對**（⛔ `id`·`W-G.9-293` 自捕 `3` 之附款）。

🔒 **自我驗證閘（三重·逐閘出艙其<u>執行次數</u>）**
   `(i)`  `corner_range_polys[(blk, side)]` **`is`** `_build_corner_range_v3` 之回傳物件。
   `(ii)` 以**當場之** `allocation_dir`／`buf` 重建之帶，其面積與 `range_area` 之 `|Δ| ≤ tol`。
   `(iii)` 同一多邊形之面積與其自身之差 ＝ `0`（**[必為零]之造·先自證可滿足**）。

`rc`：`0`／`5` **器紅**。
用法：python verify/probes/probe_WG9294_rangearea.py
"""
import contextlib
import inspect
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(REPO)

W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
RED = [0]
_LOG = []
GATE_N = {"i": 0, "ii": 0, "iii": 0}


def say(s=""):
    print(s)
    _LOG.append(s)


def red(s):
    say("🔴 " + s)
    RED[0] = 5


# ══════════════════════════════════════════════════════════════════════════════
def drive(sb):
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    os.environ.pop("WV_K6_STEP0", None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    RNG, BUF = [], []

    _o_rng = ns["_build_corner_range_v3"]
    SIG_R = inspect.signature(_o_rng)

    def _spy_rng(*a, **kw):
        out = _o_rng(*a, **kw)                       # 🔒 純委派
        try:
            ba = SIG_R.bind(*a, **kw)
            ba.apply_defaults()
            RNG.append({"label": ba.arguments.get("_label"),
                        "side": ba.arguments.get("_side"), "poly": out})
        except Exception:                            # noqa: BLE001
            pass
        return out

    ns["_build_corner_range_v3"] = _spy_rng

    _o_buf = ns["_corner_buffer_S"]
    SIG_B = inspect.signature(_o_buf)

    def _spy_buf(*a, **kw):
        out = _o_buf(*a, **kw)                       # 🔒 純委派
        try:
            ba = SIG_B.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            BUF.append({"label": P.get("_label"), "side": P.get("side"),
                        "block_poly": P.get("block_poly"), "d_hat": P.get("d_hat"),
                        "front_p1": P.get("front_p1"),
                        "allocation_dir": P.get("allocation_dir"),
                        "range_area": P.get("range_area"), "tol": P.get("tol"),
                        "buf": float(out)})
        except Exception:                            # noqa: BLE001
            pass
        return out

    ns["_corner_buffer_S"] = _spy_buf

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
    err, crp = None, {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        crp = dict((_sg or {}).get("corner_range_polys") or {})
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
        crp = dict((getattr(e, "partial", None) or {}).get("corner_range_polys") or {})
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    # 🔒 參數表之當場列（`range_area` 之直接來源欄）
    prow = {r.get("街廓"): r for r in (params or [])}
    return {"RNG": RNG, "BUF": BUF, "crp": crp, "fo": fo_tab, "err": err,
            "ns": ns, "prow": prow}


def _pick(recs, blk, side):
    out = [r for r in recs
           if r.get("side") == side and blk in str(r.get("label") or "")]
    return (out[-1], len(out)) if out else (None, 0)


def band_poly(ns, block_poly, d_hat, front_p1, allocation_dir, buf, side):
    """帶之**重建** —— 逐字複刻 `app.py` `_corner_buffer_S._band_area`（**當場之實參**·⛔ 假設之輸入）。"""
    import numpy as np
    dom = ns["_strip_s_range"](block_poly, d_hat, front_p1, allocation_dir)
    if dom is None:
        return None, None
    s_min, s_max = float(dom[0]), float(dom[1])
    _lo = max(s_min, 0.0)
    _d = np.asarray(d_hat, dtype=float)
    a, b = (_lo, float(buf)) if side == "left" else (s_max - float(buf), s_max)
    w = b - a
    if w <= 0:
        return None, None
    bp = np.asarray(front_p1, dtype=float) + a * _d
    g, ar = ns["_block_strip"](block_poly, d_hat, bp, w, allocation_dir=allocation_dir)
    return g, float(ar or 0.0)


def uniq(frame, rel):
    txt = open(os.path.join(REPO, rel), encoding="utf-8").read()
    return [(i, l) for i, l in enumerate(txt.split("\n"), 1) if frame in l]


def static():
    """款 `1`（賦值鏈之碼面端）／款 `5`（捨入之位數）——**錨取字樣·先驗唯一性**。"""
    say("=" * W)
    say("## `§S`　款 `1`（賦值鏈·碼面端）／款 `5`（捨入）之**靜態現查**")
    say("=" * W)
    say("   🔒 **母體正面列舉** ＝ `app.py`／`verify/stepg_pipeline.py`／`verify/run_verification.py`／"
        "`verify/selection_pipeline.py`（**四檔**）")
    say("")
    say("   | # | 錨（逐字·`grep -F`） | 檔 | 命中 | 判 | 該處逐字 |")
    say("   |---|---|---|---|---|---|")
    CH = [
        ("_l_min = _row_for_buffer.get('【左】街角最小面積(㎡)')", "verify/stepg_pipeline.py"),
        ("float(_l_min), 'left', _label=blk_label)", "verify/stepg_pipeline.py"),
        ('"【左】街角最小面積(㎡)": (rng("left") if has_l else None),', "verify/run_verification.py"),
        ("return round(float(r.area), 2) if r is not None else None", "verify/run_verification.py"),
        ("_left_min = round(float(_rng_cr.area), 2)", "app.py"),
        ("'【左】街角最小面積(㎡)': _left_min,", "app.py"),
    ]
    for n, (s, rel) in enumerate(CH, 1):
        hs = uniq(s, rel)
        ok = "✅ 唯一" if len(hs) == 1 else "🔴 **非唯一（%d）⇒ loud**" % len(hs)
        say("   | `%d` | `%s` | `%s` | **%d** | %s | %s |"
            % (n, s.replace("|", "\\|")[:76], rel, len(hs), ok,
               ("`%s:%d`" % (rel, hs[0][0])) if hs else "—"))
        if len(hs) != 1:
            red("錨「%s」於 `%s` 非唯一 ⇒ loud 具名（全部命中列見下）" % (s, rel))
            for i, l in hs:
                say("       %s:%d  %s" % (rel, i, l.strip()[:100]))
    say("   🔑 **判別力自檢**（寬字樣·須 `> 1` ⇒ 該檢⛔ 恆為 `1`）：")
    for s, rel in (("街角最小面積", "verify/run_verification.py"),
                   ("街角最小面積", "app.py"),
                   ("round(", "verify/run_verification.py")):
        say("       寬字樣 `%s` @ `%s` ⇒ **%d** 列" % (s, rel, len(uniq(s, rel))))
    say("")
    say("   🔒 **款 `5` 之判：`range_area` 之產生式<u>含捨入</u>**——二產生處逐字皆為 "
        "`round(float(<poly>.area), 2)`（**位數 ＝ `2`**）：")
    say("       `verify/run_verification.py` 之 `def rng(which)` 內 `return round(float(r.area), 2) …`")
    say("       `app.py` 之 `_left_min = round(float(_rng_cr.area), 2)`／`_right_min = round(float(_rng_cr.area), 2)`")
    say("   🛑 **⛔ 書「查無」**——本項為**有**，其母體（四檔）與字樣已逐項列舉於上。")
    say("")


def analyse(sb, d):
    ns = d["ns"]
    crp = d["crp"]
    say("=" * W)
    say("## `§M`（`SB = %s`）　款 `1`–`3`／`6`" % repr(sb))
    say("=" * W)
    say("   `run_step_g` 之終局 ＝ %s｜`corner_range_polys` 鍵 ＝ %d 個"
        % (d["err"] or "（未拋）", len(crp)))
    grids = []
    for b in BLKS:
        L, R = d["fo"][b]
        if L:
            grids.append((b, "left"))
        if R:
            grids.append((b, "right"))
    say("   `forced` 格 ＝ **%d**（%s）" % (len(grids), "、".join("%s/%s" % g for g in grids)))
    say("")
    rows = []
    for blk, side in grids:
        say("─" * W)
        say("### `%s`／`%s`＠`SB = %s`" % (blk, side, repr(sb)))
        br, nb = _pick(d["BUF"], blk, side)
        rr, nr = _pick(d["RNG"], blk, side)
        cp = crp.get((blk, side))
        if br is None or rr is None or cp is None:
            red("`%s/%s`：紀錄不全（`BUF` %d／`RNG` %d／`cp` %s）⇒ **loud 拒測**"
                % (blk, side, nb, nr, cp is not None))
            continue

        # ── 閘 (i)：同一性（`is` 比對·⛔ `id`）──
        GATE_N["i"] += 1
        same = cp is rr["poly"]
        say("  **閘 `(i)`**（第 `%d` 次執行）`corner_range_polys[(%r, %r)]` **`is`** "
            "`_build_corner_range_v3` 之回傳 ⇒ **%s**" % (GATE_N["i"], blk, side, same))
        if not same:
            red("`%s/%s`：閘 `(i)` 不過（⛔ 同一物）⇒ 該格之數⛔ 出艙" % (blk, side))
            continue

        ra = float(br["range_area"])
        tol = br["tol"]
        ar_poly = float(cp.area)

        # ── 款 1：當場值 ──
        say("  **款 `1`**　`range_area` **實參之當場值**（`repr` 全位）＝ `%r`" % ra)
        _pr = (d["prow"].get(blk) or {})
        _col = "【左】街角最小面積(㎡)" if side == "left" else "【右】街角最小面積(㎡)"
        say("      其**直接來源欄**（參數表·當場列）`%s` ＝ `%r`（與實參相等 ＝ **%s**）"
            % (_col, _pr.get(_col), _pr.get(_col) == ra))

        # ── 款 2：實算面積 ──
        say("  **款 `2`**　`corner_range_polys[(%r, %r)].area`（`repr` 全位）＝ `%r`"
            % (blk, side, ar_poly))

        # ── 款 3：逐位差 ──
        diff = ra - ar_poly
        say("  🔑 **款 `3`**　`range_area − area(poly)` ＝ `%r`（含正負號·`repr` 全位）" % diff)

        # ── 閘 (ii)：帶之重建（當場之實參·⛔ 假設之輸入）──
        g1, ar1 = band_poly(ns, br["block_poly"], br["d_hat"], br["front_p1"],
                            br["allocation_dir"], br["buf"], side)
        GATE_N["ii"] += 1
        ok_ii = (ar1 is not None) and abs(ar1 - ra) <= float(tol)
        say("  **閘 `(ii)`**（第 `%d` 次執行）帶之**重建**（**當場之** `allocation_dir`／`buf`）："
            "面積 `%r`／`range_area` `%r`／`|Δ|` `%r`（`tol` `%r`）⇒ %s"
            % (GATE_N["ii"], ar1, ra, (None if ar1 is None else abs(ar1 - ra)), tol,
               "✅" if ok_ii else "🔴"))
        if not ok_ii:
            red("`%s/%s`：閘 `(ii)` 不過 ⇒ 該格之數⛔ 出艙" % (blk, side))
            continue

        # ── 款 6 [必非零]：現行 buf 之對稱差（**重建**·⛔ 設計驗算）──
        ab = g1.difference(cp)
        ba = cp.difference(g1)
        sym1 = float(ab.area) + float(ba.area)
        # ── 閘 (iii) ＝ 款 6 [必為零] ──
        GATE_N["iii"] += 1
        z = abs(ar_poly - float(cp.area))
        say("  **閘 `(iii)`**（第 `%d` 次執行·＝ 款 `6` [必為零]）同一多邊形之面積與其自身之差 ＝ `%r` ⇒ %s"
            % (GATE_N["iii"], z, "✅" if z == 0.0 else "🔴"))
        if z != 0.0:
            red("`%s/%s`：閘 `(iii)` 不過 ⇒ **判器紅、停、上呈**" % (blk, side))
        say("  **款 `6` [必非零]**　**現行** `buf` 所生之帶（**重建**·⛔ 設計驗算）與規定範圍之對稱差 ＝ `%r`"
            "（`甲∖乙` `%r`／`乙∖甲` `%r`）⇒ %s"
            % (sym1, float(ab.area), float(ba.area), "✅ > 0" if sym1 > 0 else "🔴"))
        if not (sym1 > 0):
            red("`%s/%s`：款 `6` [必非零] 不成立 ⇒ **判器紅、停、上呈**" % (blk, side))
        rows.append({"sb": sb, "blk": blk, "side": side, "ra": ra,
                     "ar": ar_poly, "diff": diff, "sym1": sym1, "z": z, "tol": tol})
        say("")
    return rows


def main():
    static()
    allrows = []
    for sb in SBS:
        allrows += analyse(sb, drive(sb))

    say("=" * W)
    say("## 總表（款 `1`–`3`·`repr` 全位）")
    say("=" * W)
    say("   | `SB` | 格 | 款 `1` `range_area`（實參） | 款 `2` `area(poly)`（實算） | 🔑 款 `3` **逐位差** | 款 `6`[必非零] 現行帶之對稱差 | 閘 `(iii)`[必為零] |")
    say("   |---|---|---|---|---|---|---|")
    for r in allrows:
        say("   | `%s` | `%s/%s` | `%r` | `%r` | **`%r`** | `%r` | `%r` |"
            % (repr(r["sb"]), r["blk"], r["side"], r["ra"], r["ar"], r["diff"],
               r["sym1"], r["z"]))
    say("")
    say("=" * W)
    say("## 🛑 款 `4`：**單內互斥 ⇒ 依 `常規二` 取保守項**（⛔ 跑設計驗算）")
    say("=" * W)
    say("   `§三-2` 款 `4` 令「路丙之對稱差（**當場重得**·⛔ 轉引）」；")
    say("   而重得路丙之帶須以**假設之輸入**（`_first_corner_alloc_dir(side_mid)` 取代當場之 `allocation_dir`）複算，")
    say("   依 `W-G.9-292 §三-2` 之界定**即設計驗算**；而 `§六` 逐字：「⛔ 驅動生產路徑之替身（本批**⛔ 含設計驗算**）」。")
    say("   ⇒ 依 `常規二` **取保守項**（遵 `§六` 之禁）：本器**⛔ 跑設計驗算**，")
    say("      **款 `4` 之逐格比值 ⇒ 🟡 不可得（loud）**；其互斥已逐字回報。")
    say("   🛑 **「不可得」⛔ 等同「比值為零」或「款 `4` 已辦」**（`序 11` 之一般化 款 `三`）。")
    say("")
    say("=" * W)
    say("## 🔒 自我驗證閘之**執行次數**（⛔ 以 `rc = 0` 充其已跑）")
    say("=" * W)
    for k in ("i", "ii", "iii"):
        say("   閘 `(%s)` ⇒ **%d** 次" % (k, GATE_N[k]))
    say("")
    say("🛑 **出艙即止**：⛔ 判殘差之成因、⛔ 訂任何取代之準據界、⛔ 判路丙成立與否、⛔ 擬路丁、")
    say("   ⛔ 改碼一字、⛔ 開分支、⛔ 動用 KL 之放行、⛔ 鑄任何號、⛔ 解除或收窄 `GB-170`、⛔ 呈 KL。")
    say("=" * W)

    out = os.path.join(REPO, "verify", "out", "WG9294R_rangearea.log")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(_LOG) + "\n")
    print("\n落檔 ⇒ %s" % out)
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
