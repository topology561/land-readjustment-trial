r"""**D-2b-24 commit C**：抵費地面積之逐格增加量 ＋ 守恆式逐格重驗 —— ⛔ **零生產碼變更**

## 靶（claude.ai 增補單 補-2·**事前登記於 `4aebbfe`**·⛔ 不得改）

| 情境·街廓 | 預測：池面積增加 |
|---|---|
| `0m R4`／`3.5m R4` | `+58.4792` |
| `3.5m R1` | `+5.3881` |
| `0m R1` | `+0.0046` |
| `0m R3` | `+0.0001` |
| 其餘七格 | **逐位不變**（`0`） |

## 量法：一次跑取得「校回前／後」兩個池

🔑 `probe_D2b17_dual.replicate_pieces` 係**步驟 1–5 之無閘複本**——其**不含** D-2b-24 新增之
**步驟 5b（幾何餘）** ⇒ 恰為**校回前（甲後）**之池。
而 spy 所攔之**真實回傳**係**含 5b** 之池 ⇒ **校回後**。
⇒ **增加量 ＝ Σ(真實回傳) − Σ(replicate)**，⛔ 不需第二個碼態、⛔ 不需另跑 worktree。

⚠️ **真實函式會 raise**（類 A 之 `②-宗` 於 R2／R5 仍破）⇒ 以 `try` 攔截並**具名記錄**，
⛔ 不得靜默略過（該二格之「增加量」記為**不可得**，非 0）。

## 守恆式逐格重驗（補-3·**承重閘換位**）

現行守恆閘之原理式（`grep -n "def _acct_geom_tol_block" app.py`）：
`|ΣG ＋ 池幾何 − 街廓| ≤ 宗數 × (tol ＋ 0.005)`。
校回後 `池幾何 ＝ 街廓 − Σ宗幾何` ⇒ 化為 **`|ΣG − Σ宗幾何|`**。
⇒ 本檔逐格列 `ΣG`／`Σ宗幾何`／差／該格容差／判。
🔒 容差**取自生產** `ns["_acct_geom_tol_block"]`，⛔ 不新訂、⛔ 不調整。

## ⛔ 本檔不做

⛔ 不改生產碼。⛔ 不改期望 FAIL 名單。⛔ 不重烤 baseline。⛔ 不動財務。
⛔ `①' 覆蓋閘` 之 `0` **不得**作為憑據（自 D-2b-24 起構造恆真）。
"""
import contextlib
import io
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                       # noqa: E402
import run_verification as rv                                         # noqa: E402
from selection_pipeline import run_corner_pk                          # noqa: E402
from stepg_pipeline import run_step_g                                 # noqa: E402
from probe_D2b17_dual import replicate_pieces                         # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 200

# 事前登記之靶（【倉】`docs/reports/W-G.8_D-2b-24A2_靶之更正與事前登記.md` 補-2）
TARGET = {("0m", "R4"): 58.4792, ("3.5m", "R4"): 58.4792, ("3.5m", "R1"): 5.3881,
          ("0m", "R1"): 0.0046, ("0m", "R3"): 0.0001}


def _resolve_out(default_name):
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError(f"🔴 拒絕覆寫既有 log：{path}　⇒ 請設 WV_OUT_NAME=<新檔名>")
    return path


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                             # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    out = _resolve_out("probe_D2b24C_pool.log")
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-24 commit C】抵費地增加量 ＋ 守恆式逐格重驗 — ⛔ 零生產碼變更")
    P("=" * W)

    ns, fake_st = harvest()
    CAP = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        key = (_spy.tag, _label)
        if key not in CAP:
            rec = {"blk_area": float(block_poly.area),
                   "biz_area": float(sum(g.area for g in (biz_polys or []) if g is not None)),
                   "n_biz": len([g for g in (biz_polys or []) if g is not None])}
            try:                        # 校回前（步驟 1–5·⛔ 不含 5b）
                _pc, _bz = replicate_pieces(ns, block_poly, d_hat, corner_pt,
                                            allocation_dir, biz_polys)
                rec["pool_before"] = float(sum(p.area for p in _pc))
                rec["n_before"] = len(_pc)
            except Exception as e:                                    # noqa: BLE001
                rec["pool_before"] = None
                rec["err_before"] = f"{type(e).__name__}: {e}"
            try:                        # 校回後（真實回傳·含 5b）
                _real = _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                              _label=_label, _depth=_depth, _verbose=False)
                rec["pool_after"] = float(sum(p.area for p in _real))
                rec["n_after"] = len(_real)
            except Exception as e:                                    # noqa: BLE001
                rec["pool_after"] = None
                rec["err_after"] = f"{type(e).__name__}: {e}"
            CAP[key] = rec
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)
    _spy.tag = ""

    # ΣG：自 `_solve_G_one` 之回傳逐宗累加（⛔ 與池之量測互相獨立）
    GSUM = {}
    _origG = ns["_solve_G_one"]

    def _spyG(**kw):
        r, lab = _origG(**kw)
        GSUM.setdefault((_spyG.tag, _spyG.blk), []).append(
            (float(r.get("G", 0.0) or 0.0), float(r.get("area_geom", 0.0) or 0.0)))
        return r, lab
    _spyG.tag = _spyG.blk = ""

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)

    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in blks:
            _spy.tag = _spyG.tag = sb
            _spyG.blk = lbl
            ns["_pool_strips_for_block"] = _spy
            ns["_solve_G_one"] = _spyG
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                                 # noqa: BLE001
                        pass
            finally:
                ns["_pool_strips_for_block"] = _orig
                ns["_solve_G_one"] = _origG
            print(f"    [{sb}] {lbl} 擷取完畢", file=sys.stderr)

    if not CAP:
        raise RuntimeError("🔴 母體為空 ⇒ ⛔ 不得據此下任何結論")

    # ══ 補-2：逐格增加量 ══
    P("")
    P("【補-2】抵費地面積之逐格增加量（⛔ 靶為事前登記·commit `4aebbfe`）")
    P("-" * W)
    P(f"  母體 ＝ {len(CAP)} 格（⛔ 非空）")
    P(f"  {'情境':<6}{'街廓':<5}{'池(校回前)':>13}{'池(校回後)':>13}{'實測增加':>11}"
      f"{'靶':>11}{'差':>11}   判")
    P("-" * W)
    _bad = []
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            r = CAP.get((sb, lbl))
            if r is None:
                P(f"  {sb:<6}{lbl:<5}　🔴 未擷取")
                continue
            b, a = r.get("pool_before"), r.get("pool_after")
            tgt = TARGET.get((sb, lbl), 0.0)
            if b is None or a is None:
                note = f"🔴 **不可得**（{r.get('err_before') or r.get('err_after')}）"[:70]
                P(f"  {sb:<6}{lbl:<5}{str(b):>13}{str(a):>13}{'—':>11}{tgt:>11.4f}{'—':>11}   {note}")
                _bad.append((sb, lbl, "不可得"))
                continue
            inc = a - b
            d = inc - tgt
            ok = abs(d) <= 5e-4
            if not ok:
                _bad.append((sb, lbl, f"{inc:.4f} vs 靶 {tgt:.4f}"))
            P(f"  {sb:<6}{lbl:<5}{b:>13.4f}{a:>13.4f}{inc:>11.4f}"
              f"{tgt:>11.4f}{d:>+11.6f}   {'✅' if ok else '🔴 **不符 ⇒ 停機**'}")
    P("")
    P(f"  🔑 判準：|實測增加 − 靶| ≤ 5e-4（＝靶之列印精度 4dp 之半量子·⛔ 非新訂閘寬）")
    P(f"  🔴 不符／不可得 ＝ {len(_bad)} 格：{_bad if _bad else '（無）'}")

    # ══ 補-3：守恆式逐格（承重閘換位） ══
    P("")
    P("【補-3】守恆式逐格重驗：校回後 `|ΣG ＋ 池幾何 − 街廓|` 化為 `|ΣG − Σ宗幾何|`")
    P("-" * W)
    P("  容差取自生產 `ns[\"_acct_geom_tol_block\"]`（⛔ 不新訂、⛔ 不調整）")
    P(f"  {'情境':<6}{'街廓':<5}{'宗數':>5}{'ΣG':>13}{'Σ宗幾何':>13}{'|差|':>11}"
      f"{'容差':>11}   判")
    P("-" * W)
    _cbad = []
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            rec = GSUM.get((sb, lbl))
            cap = CAP.get((sb, lbl))
            if not rec or cap is None:
                P(f"  {sb:<6}{lbl:<5}　🔴 未擷取")
                continue
            n = cap["n_biz"]
            gs = sum(g for g, _ in rec[-n:]) if n and len(rec) >= n else sum(g for g, _ in rec)
            ar = cap["biz_area"]
            d = abs(gs - ar)
            tol = float(ns["_acct_geom_tol_block"](n, 45.0))
            ok = d <= tol
            if not ok:
                _cbad.append((sb, lbl, round(d, 4), round(tol, 4)))
            P(f"  {sb:<6}{lbl:<5}{n:>5}{gs:>13.4f}{ar:>13.4f}{d:>11.4f}{tol:>11.4f}"
              f"   {'✅' if ok else '🔴 **破 ⇒ 停機上呈**'}")
    P("")
    P("  ⚠️ **ΣG 之取法**：自 `_solve_G_one` 回傳逐宗累加，取**末 n 筆**（n ＝ 傳入池之宗數）")
    P("     ——⛔ 這是**近似之對齊**（推進跑多趟），若與 `Σ宗幾何` 之差異常大，")
    P("     **應先疑本取法、⛔ 不得逕判守恆破**。真守恆閘在生產路徑內、由 `run_all` 把關。")
    P(f"  🔴 破 ＝ {len(_cbad)} 格：{_cbad if _cbad else '（無）'}")

    P("")
    P("  🔒 **`①' 覆蓋閘` 之 `0` 自 D-2b-24 起<u>構造恆真</u>·⛔ 非證據**——本檔未引用之。")

    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"\n📄 {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
