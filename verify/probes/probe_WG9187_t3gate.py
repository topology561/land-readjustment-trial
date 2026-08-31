# -*- coding: utf-8 -*-
r"""**`W-G.9-187` `N-3`／`M-L-5`**：`[T3-GATE]` 之驅動 ＋ 藍影八格對拍 ＋ 選邊判別力

## 受詞

施工單 `§一 N-3`（觀測模式 1 逐字）：

> 閘之結果**只寫入診斷輸出**（建議新增 `[T3-GATE]` 列·逐街廓逐宗一列：暫編地號／`G`／
> `area(藍影)`／閘一三條件各自之布林／閘二布林／綜合判）

施工單 `§一 N-3 M-L-5`：

> ① 六街廓左右側**八格**逐格量 `area(藍影)`，與【倉】`K-9-23-a` 八格表對拍（容差 `±0.0005 ㎡`）；
>   ⚠️ 該表係 `blob@b4cc3083` 態·**跨態** ⇒ 若不符，**先具名為跨態差、⛔ 不停機**，並以本批之量為新錨。
> ② **選邊**：`area(藍影 ∩ 街角地) ≤ 1e-6 ㎡`；**判別力**：故意改取另一半 ⇒ 該值應躍至
>   `O(10) ㎡` 必轉紅（二造皆出艙）。

🛑 停機款 `X-3`（逐字）：

> `M-L-5 ②` 之選邊判別力：故意取另一半後該交集面積若**仍 ≤ 1e-6** ⇒ **先判量測器紅並停機**。

## 🔑 本檔與 `probe_WG9156_pred_inputs.py` 之分工（⛔ 二者不重複）

`-9156` 係**獨立復現**端：其幾何原語**自寫**、⛔ 未取自 `app.py`（該檔 docstring 逐字）。
🔒 **本檔相反**——本檔之藍影／閘一／閘二／`[T3-GATE]` **一律呼叫 `app.py` 之生產函式**
（`_blue_shadow_tri`／`_k923_gate1`／`_k923_gate2`／`_t3_gate_line`／`_t3_gate_emit`），
本檔只**餵資料與印**。⇒ 二者構成「生產實作 vs 獨立復現」之對拍偶，
與【倉】`K-9-23-a` 八格表**三方**互證（`常規八 二 ①`：與獨立來源對拍）。

## 情境

🔒 `SB = 0.0`（退縮 `0m`）——**與【倉】`K-9-23-a` 同情境**（該表逐字：「情境 `0m`／`STEP0=on`」）。
⚠️ `X-T` 之 `[T2-DIAG]` 基準量係 `3.5m` 情境，**二者⛔ 非同一受詞**、⛔ 不得互代。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不辦遞補（`K-9-17`·第二批）。⛔ 不以閘之結果改變任何配地結果。
⛔ 不跑 `run_all`／跨態重跑。⛔ 不寫死本機絕對路徑。
"""
import contextlib
import io
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

OUTDIR = os.path.join(VERIFY, "out")
SB = 0.0
LOCAL_ORIGIN = np.array([310450.0, 2651900.0])   # 🔒 `GB-82` 之重心化平移量（同 `-9156`）
EPS_ZERO = 1e-6
REF_TOL = 0.0005

# ── 【倉】`K-9-23-a` 八格藍影（態 `blob@b4cc3083`）──────────────────────────
#    出處：`docs/rulings/K-6_街角地分配程序與可分配判準.md:3284-3291`（＝規格書 `:121-129`）
#    🔒 **⛔ 非由本批新碼回填**（`fixture-provenance`）——係倉內既有錨，逐值可 grep。
REF_BLUE = {
    ("R1", "left"): 5.384991697,
    ("R1", "right"): 6.667129053,
    ("R2", "left"): 76.205568190,
    ("R3", "right"): 75.626739110,
    ("R4", "left"): 26.093820432,
    ("R4", "right"): 27.442490499,
    ("R5", "left"): 72.455256336,
    ("R6", "right"): 0.000045364,
}

L = []


def say(s=""):
    L.append(s)
    print(s, file=sys.stderr)


def Lc(p):
    return np.asarray(p, dtype=float)[:2] - LOCAL_ORIGIN


def drive():
    """逐街廓 `run_step_g`（`X-5` 🔓 授權）＋ `spy_pool` 擷取（體例同 `-9156 drive()`）。"""
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g
    import probe_WG981_scope as w81

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    o_pool = ns["_pool_strips_for_block"]
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _sw = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)
    w81.CAP.clear()
    w81.SOLVE.clear()
    w81.CUR["setback"] = SB
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB, snapshot=snapshot)
    ns["_pool_strips_for_block"] = w81.spy_pool(o_pool)
    gate = {}
    try:
        for lbl in blks:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, SB)
                    gate[lbl] = ("過", "")
                except Exception as e:                          # noqa: BLE001
                    # 🩸 ⛔ 不得把任何例外都記成「②-宗 破」（`-9156` 首版之自捕）
                    msg = "%s: %s" % (type(e).__name__, e)
                    gate[lbl] = (("破" if "②-宗 圍堵閘破" in msg else "過"), msg)
    finally:
        ns["_pool_strips_for_block"] = o_pool
    CAP = {r["label"]: r for r in w81.CAP}
    if not CAP:
        raise RuntimeError("🔴 CAP 為空——管線未產生任何街廓（no-silent-fallback）")
    return ns, CAP, cad, wins, params, gate, blks


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                            # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    name = os.environ.get("WV_OUT_NAME") or "probe_WG9187_t3gate.log"
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)

    from shapely.geometry import Polygon as SPoly

    say("=" * 132)
    say("【W-G.9-187 N-3／M-L-5】[T3-GATE] 驅動 ＋ 藍影八格對拍 ＋ 選邊判別力（🛑 觀測模式·⛔ 零配地變更）")
    say("=" * 132)
    import shapely
    say("  環境：shapely %s | GEOS %s | 情境 SB = %.1f m（⛔ 非 X-T 之 3.5m）"
        % (shapely.__version__, shapely.geos_version, SB))
    say("  🔒 本檔之藍影／二閘／[T3-GATE] **一律呼叫 app.py 之生產函式**（⛔ 非自寫複本）")
    say("")

    ns, CAP, cad, wins, params, gate, blks = drive()
    blue_tri_f = ns["_blue_shadow_tri"]
    gate1_f = ns["_k923_gate1"]
    gate2_f = ns["_k923_gate2"]
    line_f = ns["_t3_gate_line"]
    NA = ns["_T3_NA"]          # 🔒 「不適用」之哨兵（⛔ 與 None＝無從判定分立）
    emit_f = ns["_t3_gate_emit"]
    gmls = ns["get_min_lot_size"]
    say("  自 ns 取得生產符號：_blue_shadow_tri／_k923_gate1／_k923_gate2／"
        "_t3_gate_line／_t3_gate_emit／get_min_lot_size ✅")
    say("  逐街廓 run_step_g 之 ②-宗 圍堵閘：%s"
        % {b: gate.get(b, ("?", ""))[0] for b in blks})
    say("")

    par_by = {r.get("街廓"): r for r in params if isinstance(r, dict)}
    ROWS = []
    CELLS = []
    X3_BAD = []
    REF_BAD = []

    for lbl in blks:
        rec = CAP.get(lbl)
        if rec is None:
            say("  🔴 %s：CAP 未攔到 ⇒ 逐字具名為射程外，⛔ 不以推定代之" % lbl)
            continue
        if not rec.get("names"):
            say("  🔴 %s：names 未對上（%s）⇒ 射程外" % (lbl, rec.get("align")))
            continue
        fl = cad["front_lines"].get(lbl)
        bl = cad["baselines"].get(lbl)
        if fl is None or bl is None:
            say("  🔴 %s：缺 FRONT_LINE／BASELINE ⇒ 射程外" % lbl)
            continue
        import math as _mm
        bang = _mm.radians(float(bl["angle_deg"]))
        bdir = np.array([_mm.cos(bang), _mm.sin(bang)])
        ahat = np.asarray(cad["alloc_dir_by_block"][lbl], dtype=float)[:2]
        names = list(rec["names"])
        polys = [SPoly([tuple(Lc(c)) for c in p.exterior.coords]) for p in rec["biz"]]
        ress = list(rec["ress"] or [])
        Gs = [((ress[i] or {}).get("G") if i < len(ress) else None)
              for i in range(len(polys))]
        block = SPoly([tuple(Lc(c)) for c in rec["block"].exterior.coords])
        pr = par_by.get(lbl) or {}
        tbl = gmls(str(pr.get("分類", "")), float(pr.get("正面路寬(m)", 0) or 0))
        W_t, D_t = float(tbl["min_width"]), float(tbl["min_depth"])

        for side in ("left", "right"):
            sl = (cad["side_lines_by_side"].get(lbl) or {}).get(side)
            if sl is None:
                continue
            wname = (wins.get(lbl) or {}).get("p1_end" if side == "left" else "p2_end")
            if wname not in names:
                say("  🔴 %s/%s：winner %r 不在母體 ⇒ 射程外" % (lbl, side, wname))
                continue
            wi = names.index(wname)
            rw = (wins.get(lbl) or {}).get("p2_end")
            k = names.index(rw) if (rw in names) else len(names)
            grp = list(range(0, k)) if side == "left" else list(range(k, len(names)))
            if wi not in grp:
                say("  🔴 %s/%s：winner 不在該側組 ⇒ 射程外" % (lbl, side))
                continue
            seq = [i for i in grp if i > wi]     # 🔒 街角重排後序列之次一位起（`K-9-17`）

            bs = blue_tri_f(
                polys[wi], Lc(fl["p1"]), Lc(fl["p2"]), Lc(bl["point"]), bdir,
                Lc(sl["p1"]), Lc(sl["p2"]), Lc(sl["mid"]), ahat,
                (block.centroid.x, block.centroid.y), _label=lbl, _side=side)
            blue = float(bs["blue_area"])

            # ── `M-L-5 ①` 與【倉】八格對拍（跨態 ⇒ 不符只具名·⛔ 不停機）──
            ref = REF_BLUE.get((lbl, side))
            dref = None if ref is None else abs(blue - ref)
            if ref is not None and dref > REF_TOL:
                REF_BAD.append((lbl, side, blue, ref, dref))

            # ── `M-L-5 ②` 選邊之二造（🛑 `X-3`）──
            picked_int = bs["iA"] if bs["pick"] == "A" else bs["iB"]
            other_int = bs["iB"] if bs["pick"] == "A" else bs["iA"]
            if not (other_int > EPS_ZERO):
                X3_BAD.append((lbl, side, picked_int, other_int))
            CELLS.append({
                "lbl": lbl, "side": side, "blue": blue, "ref": ref, "dref": dref,
                "pick": bs["pick"], "sigma_pick": bs["sigma_rule_pick"],
                "iA": bs["iA"], "iB": bs["iB"], "areaA": bs["areaA"],
                "areaB": bs["areaB"], "sigma": bs["sigma"], "ds": bs["ds"],
                "sds": bs["sigma_ds"], "picked_int": picked_int,
                "other_int": other_int, "wname": wname, "W": W_t, "D": D_t})

            # ── `[T3-GATE]`：逐宗一列（街角地本身⛔ 不走閘二·`K-9-12-e`）──
            for rank, i in enumerate(grp):
                is_corner = (i == wi)
                if is_corner:
                    g1, g1d = NA, {"G": Gs[i], "why": "街角地（第 0 宗）⛔ 不走閘一"}
                    g2, g2d = NA, {"W": W_t, "D": D_t,
                                   "reason": "街角地⛔ 不走閘二（K-9-12-e／K-9-13 四段）"}
                else:
                    is_first = (seq and i == seq[0])
                    if is_first:
                        g1, g1d = gate1_f(polys[i], Gs[i], blue,
                                          bs["front_pt"], bs["front_dir"],
                                          bs["base_pt"], bs["base_dir"])
                    else:
                        g1, g1d = NA, {"G": Gs[i],
                                       "why": "第 2 宗以後⛔ 不走閘一（K-9-17 四：不交叉恆真）"}
                    g2, g2d = gate2_f(polys[i], W_t, D_t,
                                      _label="%s/%s/%s" % (lbl, side, names[i]))
                ROWS.append(line_f(lbl, side, rank, names[i], g1, g1d, g2, g2d, blue))

    # ── 出艙 ────────────────────────────────────────────────────────────
    say("── 一、`M-L-5 ①` 藍影八格 vs【倉】`K-9-23-a`（容差 ±%.4f ㎡·跨態 ⇒ 不符只具名） ──"
        % REF_TOL)
    say("  %-4s %-6s %18s %18s %13s %6s" % ("街廓", "側", "本批量", "【倉】b4cc3083", "|Δ|", "判"))
    for c in CELLS:
        say("  %-4s %-6s %18.9f %18s %13s %6s"
            % (c["lbl"], c["side"], c["blue"],
               ("—" if c["ref"] is None else "%.9f" % c["ref"]),
               ("—" if c["dref"] is None else "%.3e" % c["dref"]),
               ("—" if c["dref"] is None else ("✅" if c["dref"] <= REF_TOL else "🔴 跨態差"))))
    say("  格數 = %d（【倉】表為 8 格）" % len(CELLS))
    say("")

    say("── 二、`M-L-5 ②` 選邊之二造（🛑 `X-3`：所取之半 ∩ ≤ 1e-6；另一半須躍至 O(10)） ──")
    say("  %-4s %-6s %6s %6s %16s %16s %14s" %
        ("街廓", "側", "定義取", "σ·Δs取", "所取半 ∩街角地", "另一半 ∩街角地", "σ·Δs"))
    for c in CELLS:
        say("  %-4s %-6s %6s %6s %16.9f %16.9f %14.9f"
            % (c["lbl"], c["side"], c["pick"], c["sigma_pick"],
               c["picked_int"], c["other_int"], c["sds"]))
    say("  🔒 定義選邊 vs `σ·Δs` 規則之一致格數 = %d/%d"
        % (sum(1 for c in CELLS if c["pick"] == c["sigma_pick"]), len(CELLS)))
    say("  🛑 `X-3` 之判：另一半 ∩ **仍 ≤ 1e-6** 之格 = %s" % (X3_BAD or "無 ⇒ ✅ 判別力成立"))
    say("")

    say("── 三、`[T3-GATE]`（逐街廓逐宗一列·🛑 觀測模式·⛔ 未改變任何配地結果） ──")
    emit_f(ROWS, _stream=sys.stderr)
    L.extend(ROWS)
    say("")
    say("  [T3-GATE] 總列數 = %d" % len(ROWS))
    _bad = [r for r in ROWS if "綜合 不配地" in r]
    say("  綜合判「不配地」之列數 = %d" % len(_bad))
    for r in _bad:
        say("    ▸ " + r.split("｜綜合")[0][:150])
    say("")

    say("=" * 132)
    say("🛑 `X-3`：%s" % ("🔴 觸發（量測器紅）" if X3_BAD else "✅ 未觸發"))
    say("⚠️ `M-L-5 ①` 跨態不符格：%s" % (REF_BAD or "無"))
    say("=" * 132)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path, file=sys.stderr)
    return 1 if X3_BAD else 0


if __name__ == "__main__":
    sys.exit(main())
