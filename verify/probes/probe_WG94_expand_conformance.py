# -*- coding: utf-8 -*-
"""`W-G.9-4` 合成測試：`E1`（新產生者 ≡ 變更前之 `_mp_base_W0`）＋ `E2`（新式 − 舊式 ＝ `W_0`）。

⛔ 只量不改。⛔ **本檔不呼叫 `stepg._mp_base_W0` 作為 `E1` 之參照**——
   該函式已於本批改為**委派**至新產生者，拿它對拍即**恆真**（考古 60 族之形狀）。
🔒 **`E1` 之參照 ＝ 變更前 `6ab9e86` 之原式**，本檔**逐字轉錄**之為 `_mp_base_W0_ORIG`，
   並以 `git show 6ab9e86:verify/stepg_pipeline.py` **實文比對**自證轉錄無誤（閘 T）。

## 🔒 射程

- **母體 ＝ (情境 2) × (街角側 8) ＝ 16 格**，⛔ **含不觸發格與退化格**（`R6/right`）。
- 街廓 ↔ SIDE ↔ ALLOC 之關聯取自 `cad["side_lines_by_side"]`／`cad["alloc_dir_by_block"]`
  （`parse_cadastral_geofile` 產出）；⛔ 未以幾何鄰近自行配對。
- **為何須合成測試**：`app.py` 之族②③ 落點**巢狀於 `main()`**，`run_all` **永不執行之**
  （`W-G.9-1` §3-8 已證）⇒ ⛔ `run_all` 結果**不得**充作該處之證據。
"""
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon as _PG                         # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUT = os.path.join(VERIFY, "out", "probe_WG94_expand_conformance.log")
BASE = "6ab9e86"
L = []


def say(s=""):
    L.append(s)
    print(s)


def _mp_base_W0_ORIG(_gs, _buf, _dv, _mp, _adir):
    """⛔ **逐字轉錄自 `6ab9e86:verify/stepg_pipeline.py`**（變更前之原式）。

    🔒 轉錄之正確性由**閘 T** 自證（與 `git show` 之實文比對），⛔ 非憑記憶。
    """
    if _gs is None or _mp is None or _adir is None or _dv is None:
        return 0.0
    _a = np.asarray(_adir, dtype=float); _an = float(np.linalg.norm(_a))
    if _an < 1e-9:
        return 0.0
    _a = _a / _an
    _dv2 = np.asarray(_dv, dtype=float); _dn = float(np.linalg.norm(_dv2))
    _du = _dv2 / _dn if _dn > 1e-9 else _dv2
    _ao = _a if float(np.dot(_du, _a)) >= 0 else -_a
    _bp0 = np.asarray(_gs, dtype=float) + float(_buf) * _du
    return float(np.dot(_bp0 - np.asarray(_mp, dtype=float), _ao))


def _unit(v):
    v = np.asarray(v, float)[:2]
    n = float(np.linalg.norm(v))
    if n < 1e-12:
        raise RuntimeError("🔴 零向量")
    return v / n


def gate_T():
    """閘 T：`_mp_base_W0_ORIG` 之轉錄與 `6ab9e86` 之實文**逐關鍵行相符**。"""
    src = subprocess.run(["git", "show", f"{BASE}:verify/stepg_pipeline.py"],
                         cwd=REPO, capture_output=True, text=True,
                         encoding="utf-8").stdout
    keys = ["def _mp_base_W0(_gs, _buf, _dv, _mp, _adir):",
            "_a = _np_d.asarray(_adir, dtype=float); _an = float(_np_d.linalg.norm(_a))",
            "_du = _dv2 / _dn if _dn > 1e-9 else _dv2",
            "_ao = _a if float(_np_d.dot(_du, _a)) >= 0 else -_a",
            "_bp0 = _np_d.asarray(_gs, dtype=float) + float(_buf) * _du",
            "return float(_np_d.dot(_bp0 - _np_d.asarray(_mp, dtype=float), _ao))"]
    miss = [k for k in keys if k not in src]
    return keys, miss


def main():
    say("=" * 120)
    say("W-G.9-4 合成測試　E1（新產生者 ≡ 變更前原式）／E2（新式 − 舊式 ＝ W_0）")
    say("=" * 120)

    keys, miss = gate_T()
    say("")
    say("【閘 T】`_mp_base_W0_ORIG` 之轉錄自證（對 `git show %s:verify/stepg_pipeline.py` 之實文）"
        % BASE)
    say("   關鍵行 %d 條，缺 **%d** 條 ⇒ **%s**"
        % (len(keys), len(miss), "轉錄正確 ✅" if not miss else "🔴 轉錄有誤"))
    for m in miss:
        say("   🔴 缺：%s" % m)
    if miss:
        raise RuntimeError("🔴 閘 T 破 ⇒ ⛔ 不得據本檔任何數字下結論")

    ns, fake_st = harvest()
    k956 = ns["k956_W_from_mp"]
    _corner_buffer_S = ns["_corner_buffer_S"]
    alloc_normal_axis = ns["alloc_normal_axis"]
    _oblique_s_max = ns["_oblique_s_max"]

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    fls = cad.get("front_lines") or {}
    sides_by = cad.get("side_lines_by_side", {}) or {}
    alloc_by = cad.get("alloc_dir_by_block", {}) or {}
    corners = [(b, s) for b in rv.CORNER_BLOCKS for s in ("left", "right")
               if s in (sides_by.get(b) or {})]
    say("")
    say("【射程】街角側 %d × 情境 2 ＝ **%d 格**（⛔ 含不觸發與退化）"
        % (len(corners), len(corners) * 2))

    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    tp, bp_, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)

    W0_EXPECT = {("R1", "left"): +0.161877, ("R1", "right"): +0.200569,
                 ("R2", "left"): -1.693924, ("R3", "right"): +1.691802,
                 ("R4", "left"): -0.787529, ("R4", "right"): +0.651126,
                 ("R5", "left"): -1.640252, ("R6", "right"): +0.000001}

    rows = []
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        prm = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        by_lbl = {r.get("街廓"): r for r in prm}
        *_, forced_map = run_corner_pk(ns, fake_st, list(cb_by.values()), cad,
                                       prm, tp, bp_, setback, snapshot=snapshot)
        for blk, side in corners:
            b = cb_by[blk]
            fl = fls[blk]
            F1 = np.asarray(fl["p1"], float)[:2]
            dh = _unit(np.asarray(fl["p2"], float)[:2] - F1)
            mp = np.asarray(sides_by[blk][side]["mid"], float)[:2]
            adir = np.asarray(alloc_normal_axis(alloc_by[blk]), float)[:2]
            ah = adir if float(np.dot(dh, adir)) >= 0 else -adir
            cos_dn = abs(float(np.dot(dh, adir)))
            poly = _PG(b["vertices"])
            forced = bool((forced_map.get(blk) or {}).get(f"{side}_forced_offset", False))
            col = "【左】街角最小面積(㎡)" if side == "left" else "【右】街角最小面積(㎡)"
            ra = (by_lbl.get(blk) or {}).get(col)
            rec = dict(tag=tag, blk=blk, side=side, forced=forced,
                       new=None, orig=None, old=None, W0=None, new_p=None, orig_p=None,
                       W0_p=None, exp=W0_EXPECT[(blk, side)])
            if ra is not None and float(ra) != float("inf") and float(ra) > 0:
                buf = float(_corner_buffer_S(poly, dh, F1, adir, float(ra), side, _label=blk))
                if side == "left":
                    gs = F1
                else:
                    smax = _oblique_s_max(b["vertices"], dh, F1, adir)
                    gs = F1 + float(smax) * dh
                # ── 口徑甲：**+d̂**（＝事前登記表之口徑·`W-G.9-2` 所用）────────────
                #   P = gs + buf·d̂、â 由 +d̂ 定號 ⇒ 恆等式 `新 = W_0 + buf·cos_dn` 之代數檢定。
                P_a = gs + buf * dh
                # ── 口徑乙：**生產口徑**（`stepg:821`／`:822` 之實呼）─────────────
                #   🔴 右組傳 `_dhr_o = −d_hat`（`grep -n "_dhr_o = -_np_d.asarray" verify/stepg_pipeline.py`）
                #   ⇒ `â_定向` 隨之翻號 ⇒ 其 `W_0` 與口徑甲**差一個負號**。
                dv_p = dh if side == "left" else -dh
                ah_p = adir if float(np.dot(dv_p, adir)) >= 0 else -adir
                P_p = gs + buf * (dv_p / float(np.linalg.norm(dv_p)))
                rec.update(new=float(k956(P_a, mp, adir, dh)),
                           orig=float(_mp_base_W0_ORIG(gs, buf, dh, mp, adir)),
                           old=buf * cos_dn,
                           W0=float(np.dot(gs - mp, ah)),
                           new_p=float(k956(P_p, mp, adir, dv_p)),
                           orig_p=float(_mp_base_W0_ORIG(gs, buf, dv_p, mp, adir)),
                           W0_p=float(np.dot(gs - mp, ah_p)))
            rows.append(rec)

    # ═══════ E1 ═══════
    say("")
    say("#" * 120)
    say("## E1　新產生者 `k956_W_from_mp` ≡ **變更前**之 `_mp_base_W0`（逐位）")
    say("#" * 120)
    ok = [r for r in rows if r["new"] is not None]
    say("   ⛔ 參照**非**現行 `stepg._mp_base_W0`（其已委派 ⇒ 對拍恆真），係閘 T 所驗之原式轉錄。")
    _e1a = max(abs(r["new"] - r["orig"]) for r in ok)
    _e1p = max(abs(r["new_p"] - r["orig_p"]) for r in ok)
    say("   口徑甲（+d̂·登記表口徑）  逐格 max|新 − 原式| = **%.3e**（%d 格）" % (_e1a, len(ok)))
    say("   口徑乙（**生產口徑**·右組 −d̂）逐格 max|新 − 原式| = **%.3e**（%d 格）" % (_e1p, len(ok)))
    say("   ⇒ **E1 %s**（二口徑皆須逐位相等·⛔ 不得只驗其一）"
        % ("✅ 成立" if (_e1a == 0.0 and _e1p == 0.0) else "🔴 破（非逐位相等）"))

    # ═══════ E2 ═══════
    say("")
    say("#" * 120)
    say("## E2　新式 − 舊式 ＝ `W_0`（⛔ 16 格全列·含不觸發與退化）")
    say("#" * 120)
    say("%-5s %-4s %-6s %-7s %12s %12s %12s %12s %12s"
        % ("情境", "街廓", "側別", "forced", "新式", "舊式(buf·cos)", "新−舊", "W_0(實測)", "W_0(期望)"))
    say("-" * 120)
    for r in rows:
        if r["new"] is None:
            say("%-5s %-4s %-6s %-7s %12s %12s %12s %12s %12.6f"
                % (r["tag"], r["blk"], r["side"], r["forced"], "—", "—", "—", "—", r["exp"]))
            continue
        say("%-5s %-4s %-6s %-7s %12.6f %12.6f %12.6f %12.6f %12.6f"
            % (r["tag"], r["blk"], r["side"], r["forced"], r["new"], r["old"],
               r["new"] - r["old"], r["W0"], r["exp"]))
    say("-" * 120)
    say("   【口徑甲·＝事前登記表之口徑】")
    say("     max|(新 − 舊) − W_0(實測)| = **%.3e**   ← 恆等式之代數檢定"
        % max(abs((r["new"] - r["old"]) - r["W0"]) for r in ok))
    say("     max|W_0(實測) − W_0(期望·事前寫死)| = **%.6f**"
        % max(abs(r["W0"] - r["exp"]) for r in ok))
    _e2 = max(abs(r["W0"] - r["exp"]) for r in ok) < 5e-6
    say("   ⇒ **E2 %s**（期望表為 6 位小數 ⇒ 判準取 `5e-6`）"
        % ("✅ 成立" if _e2 else "🔴 破"))
    say("")
    say("   🔴 **【口徑乙·生產口徑】之併記（⛔ 事前登記未涵蓋·CC 現查）**")
    say("     `stepg:822` 右組傳 `_dhr_o = −d_hat` ⇒ `â_定向` 翻號 ⇒ 其 `W_0` 與口徑甲**差一負號**：")
    say("     %-14s %14s %14s %14s" % ("格", "W_0(甲·+d̂)", "W_0(乙·生產)", "甲＋乙"))
    for r in ok[:8]:
        say("     %-14s %14.6f %14.6f %14.3e"
            % ("%s/%s" % (r["blk"], r["side"]), r["W0"], r["W0_p"], r["W0"] + r["W0_p"]))
    _lr = [r for r in ok if r["side"] == "right"]
    _ll = [r for r in ok if r["side"] == "left"]
    say("     左側 max|甲 − 乙| = %.3e（同號·同值）" % max(abs(r["W0"] - r["W0_p"]) for r in _ll))
    say("     右側 max|甲 ＋ 乙| = %.3e（**恰為相反數**）" % max(abs(r["W0"] + r["W0_p"]) for r in _lr))
    say("     ⇒ **事前登記之 `W_0` 表係口徑甲**；右側之生產值為其**負值**。")
    say("     🔒 二口徑之 `E1` 皆逐位相等 ⇒ **本批之委派無論何口徑皆語意不變**；")
    say("     ⛔ 惟 `W-G.9-5` 切換時**必須指明所用口徑**，否則右側符號會翻。")
    say("   🔒 `R6/right` 為**退化格**（`W_0 ≈ +1e-6`）：已正面列出，"
        "⛔ 不作任何結論之通過憑據。")

    say("")
    say("rc = 0")
    return 0


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    sys.exit(rc)
