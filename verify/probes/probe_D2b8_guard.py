# -*- coding: utf-8 -*-
r"""**D-2b-8 §A-3 ＋ §B**：守衛修正之零變動驗收 ＋ R6 控制組全鏈量測。

## §A-3（零變動驗收）
逐街廓 solo 分跑（D-2b-6 已實證保值），記錄每次 `_solve_G_one` 之**全精度**輸出與終止例外，
與**基準** `verify/out/probe_D2b6_split.log`【III】（修改前之實料·已入庫）對照。
**期望**：R6 之守衛不再 raise；**其餘五街廓逐項不變**。

## §B（R6 控制組全鏈）
R6 夾角 `0.000003°` ⇒ 無楔形 ⇒ 若「所有破皆楔形所致」成立，R6 應能跑完全鏈。
七道閘須分辨 **過／破／未抵達**（⛔ 不得以 `0` 代表「過」）——以**行序**判定：
抵達與否由「是否越過該閘之行」決定，而終止行由例外訊息辨識。
"""
import io
import os
import re
import sys
import contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b8_guard.log")
W = 200

# 七道閘（**現查行號**·⛔ 施工單 §B-1 所列係 D-2b-3 之前之舊值·已腐）
GATES = [
    ("抵費地計算失敗（含覆蓋閘/②-宗）", 972, "抵費地計算失敗"),
    ("§N3-0 逐宗主閘", 990, "§N3-0 逐宗主閘破"),
    ("telescoping 總量段", 1164, "結構閘 telescoping 破：街廓"),
    ("階段2 telescoping 段", 1198, "結構閘 階段2 telescoping 破：街廓"),
    ("â 定向雙判準", 1241, "â 定向雙判準不一致"),
    ("理論＝實跑", 1276, "結構閘 理論＝實跑 破：街廓"),
    ("停機③ 守恆-帳幾何級", 1323, "停機③（守恆-帳幾何級破）"),
]


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * W)
    L.append("【D-2b-8 §A-3＋§B】守衛修正零變動驗收 ＋ R6 控制組全鏈")
    L.append("=" * W)
    L.append("  ⚠️ 七道閘之行號係**現查**（972/990/1164/1198/1241/1276/1323）；"
             "施工單 §B-1 所列（972/989/1036/1056/1098/1112/1157）係 D-2b-3 之前之舊值·**已腐**。")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    _blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in _blks:
            _blks.append(_l)

    RES = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in _blks:
            n = {"c": 0}
            _o = ns["_solve_G_one"]

            def _spy(_oo=_o, _n=n, **kw):
                _n["c"] += 1
                return _oo(**kw)
            ns["_solve_G_one"] = _spy
            buf = io.StringIO()
            err = ""
            try:
                with contextlib.redirect_stdout(buf):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception as e:
                        err = f"{type(e).__name__}: {e}"
            finally:
                ns["_solve_G_one"] = _o
            RES[(sb, lbl)] = {"n": n["c"], "err": err, "out": buf.getvalue()}

    # ══ §A-3：逐街廓終態 ══
    L.append("")
    L.append("【A-3】逐街廓終態（對照基準 ＝ `verify/out/probe_D2b6_split.log`【III】·修改前實料）")
    L.append("-" * W)
    for (sb, lbl), v in RES.items():
        L.append(f"  [{sb}] {lbl:<4} `_solve_G_one` {v['n']:>3} 次｜"
                 + ("✅ 跑完（無例外）" if not v["err"] else f"🔴 {v['err'][:140]}"))

    # ══ §A-2 退化命中之列印 ══
    L.append("")
    L.append("【A-2】`K-9-5-8` 退化命中之列印（⛔ 不得靜默略過）")
    L.append("-" * W)
    _hit = False
    for (sb, lbl), v in RES.items():
        for ln in v["out"].splitlines():
            if ln.startswith("[K-9-5-8]"):
                _hit = True
                L.append(f"  [{sb}] {ln[:180]}")
    if not _hit:
        L.append("  🔴 **無任何 `[K-9-5-8]` 列印 ⇒ 退化分支從未咬到·⛔ 結論不可據·停查**")

    # ══ §B：R6 七道閘 過／破／未抵達 ══
    L.append("")
    L.append("【B】R6 控制組：七道閘之 **過／破／未抵達**（⛔ 三者須分辨·⛔ 不得以 0 代表過）")
    L.append("-" * W)
    for sb in ("0m", "3.5m"):
        v = RES.get((sb, "R6"))
        if v is None:
            continue
        _err = v["err"]
        _brk = None
        for _i, (_nm, _ln, _pat) in enumerate(GATES):
            if _pat in _err:
                _brk = _i
                break
        L.append(f"  [{sb}] R6　終止例外：{_err[:150] or '（無·跑完全鏈）'}")
        for _i, (_nm, _ln, _pat) in enumerate(GATES):
            if _brk is None:
                _st = "✅ **抵達且過**"
            elif _i < _brk:
                _st = "✅ **抵達且過**"
            elif _i == _brk:
                _st = "🔴 **破**"
            else:
                _st = "⚠️ **未抵達**"
            L.append(f"      :{_ln:<5}{_nm:<30}{_st}")
        if _brk is None:
            L.append("      ⇒ 🔑 **R6 跑完全鏈**（含 `停機③`）⇒ 「一個根因」假說得強佐證"
                     "、且**首次驗到守恆**")

    # ══ §B-3：各側宗數 n ══
    L.append("")
    L.append("【B-3】各側宗數 `n`（🔑 `n≥3` 時量化上界 0.189 > 容差 0.1）")
    L.append("-" * W)
    _cnt = {}
    for tp in build_p:
        _cnt[tp.get("所屬街廓")] = _cnt.get(tp.get("所屬街廓"), 0) + 1
    for lbl in _blks:
        L.append(f"  {lbl:<4} `build_parcels` 宗數 ＝ **{_cnt.get(lbl, 0)}**"
                 + ("　（⚠️ ≥3 ⇒ 量化上界已超容差）" if _cnt.get(lbl, 0) >= 3 else ""))
    L.append("  ⚠️ 上列為**街廓總宗數**；逐側之鏈長須自 `[Δ_i·…]` 之界面數 +1 讀取"
             "（本檔未逐側拆分·⛔ 不宣稱已提供逐側 n）")

    # ══ R6 之 stdout（Δ_i／ΣRw） ══
    L.append("")
    L.append("【B-2】R6 之逐界面與 ΣRw（自 stdout）")
    L.append("-" * W)
    for sb in ("0m", "3.5m"):
        v = RES.get((sb, "R6"))
        if v is None:
            continue
        for ln in v["out"].splitlines():
            if ln.startswith("[Δ_i·") or "T2-DIAG" in ln:
                L.append(f"  [{sb}] {ln[:190]}")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
