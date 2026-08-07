# -*- coding: utf-8 -*-
r"""**D-1 哨兵**：資格閘 `F` 實參 ／ 靶格真G ／ 街角結局（⛔ 零碼面·不切換）。

🔒 **正對照哨兵（`==` 反向式）**——**切換前 FAIL、切換後 PASS**。
   ⛔ 只斷言「與前次相同」之哨兵不合格：**零 diff 有兩種相反解釋**
   （「改對了而該處本就不受影響」與「根本沒改到」）。

## 受測四項（D-0b §二）

| # | 受測符號 | 切換前應 | 切換後應 |
|---|---|---|---|
| (a) | `_corner_block_true_G` 之 `F_left`／`F_right` **實參**（逐格 16 格） | ＝ 側街**路寬**（R1 右 `8.00`） | ＝ 側街**長度**（R1 右 `33.27`） |
| (b) | `3.5m R1/right 628(5)` 之真G | **240.57** | **228.42** |
| (c) | `3.5m R1/right` 之結局 | winner ＝ `628(5)` | **無人過門檻 ⇒ 強制抵費地** |
| (d) | 全案街角結局 | 有 winner **12**／強制 **4** | 有 winner **11**／強制 **5** |

**期望值之出處（fixture-provenance·⛔ 非本檔現跑回填）**：
`docs/reports/W-G.8_D_期望影響表_凍存.md` §二（四象限表·來源 log `63ae86d`）
＋ `docs/reports/W-G.7_K6-A2-S6-2C_成因歸因與泛化.md` §四。

🔒 **切換順序已裁（D-0b §二）**：**D-1（F）先、D-2（幾何）後** ⇒ 本哨兵之「切換後」期望值
係在**舊門檻**下成立。⛔ 若先做 D-2，(c)(d) 之期望值不同（見凍存檔 §四之 ⚠️）。
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import _compute_v3_finance                      # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
_TAG = os.environ.get("D_PHASE", "pre")
LOG = os.path.join(OUTDIR, "probe_D1_F_slot_切換前凍存.log" if _TAG == "pre"
                   else "probe_D1_F_slot.log")

# ── 期望值（⛔ 出處見 docstring·非本檔現跑回填）───────────────────────────
EXP = {
    "F_R1_right_pre": 8.00, "F_R1_right_post": 33.27,
    "trueG_pre": 240.57, "trueG_post": 228.42,
    "win_pre": 12, "forced_pre": 4,
    "win_post": 11, "forced_post": 5,
}
TARGET = ("3.5m", "R1", "right")


def main():                                                    # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 190)
    L.append(f"【D-1 哨兵】資格閘 F 實參／靶格真G／街角結局 — 相位 ＝ "
             f"**{'切換前（凍存）' if _TAG == 'pre' else '切換後'}**")
    L.append("=" * 190)
    L.append("  🔒 **正對照（`==` 反向式）**：切換前 FAIL、切換後 PASS。"
             "⛔ 只斷言「與前次相同」者不合格——零 diff 有兩種相反解釋。")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    _sbrows = _compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)["sb_rows_by_label"]

    # ── (a) 捕捉 `_corner_block_true_G` 之 F 實參（⛔ 不改其行為）──────────
    _cap = {}
    _orig = ns["_corner_block_true_G"]

    def _cap_wrap(**kw):
        _cap[kw.get("_blk", "?")] = (float(kw.get("F_left", 0) or 0),
                                     float(kw.get("F_right", 0) or 0))
        return _orig(**kw)

    ns["_corner_block_true_G"] = _cap_wrap
    diag, tally = [], {}
    try:
        for setback in (0.0, 3.5):
            sb = f"{setback:g}m"
            _cap.clear()
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, winners, forced = run_corner_pk(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            for _dg in (_d0 or []):
                diag.append(dict(_dg, _sb=sb))
            tally[sb] = {"cap": dict(_cap), "win": winners, "forced": forced}
    finally:
        ns["_corner_block_true_G"] = _orig

    _sd_by = cad.get("side_lines_by_side", {}) or {}
    _sn = {"左": "left", "右": "right"}

    # ══ (a) F 實參逐格 ══════════════════════════════════════════════════
    L.append("")
    L.append("【a】資格閘 `F` 實參（**逐格 16 格**·自 `_corner_block_true_G` 呼叫端捕捉）")
    L.append("-" * 190)
    L.append("  🔒 取值點：`grep -n \"F_left=float(_SB_pc\" verify/selection_pipeline.py`"
             "（harness 路徑·現行取 `snapshot[blk][側]['路寬_m']`）")
    L.append("  🔒 對照：`sb_row['左側長度(m)']／['右側長度(m)']`（＝正典 `F ＝ SIDE_LINE 全長`·"
             "`.claude/skills/g-formula-rules/SKILL.md`）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'F 實參(現行)':>14}{'側長度(正典)':>14}{'差':>12}"
             f"  切換前判準(F==路寬 ∧ F!=長度)")
    L.append("-" * 190)
    _a_pre_ok = _a_post_ok = 0
    _a_n = 0
    for sb in ("0m", "3.5m"):
        for lbl in sorted(cb_by):
            for which in ("left", "right"):
                if which not in (_sd_by.get(lbl) or {}):
                    continue
                _cp = tally[sb]["cap"].get(lbl)
                if _cp is None:
                    L.append(f"{sb:<6}{lbl + '/' + which:<12}  🔴 未捕捉到該街廓之呼叫")
                    continue
                _f = _cp[0] if which == "left" else _cp[1]
                _row = _sbrows.get(lbl, {}) or {}
                _len = float(_row.get("左側長度(m)" if which == "left" else "右側長度(m)", 0) or 0)
                _a_n += 1
                _pre = (abs(_f - _len) > 1e-9)      # 切換前：F 應 != 長度
                _post = (abs(_f - _len) <= 1e-9)    # 切換後：F 應 == 長度
                _a_pre_ok += int(_pre); _a_post_ok += int(_post)
                L.append(f"{sb:<6}{lbl + '/' + which:<12}{_f:>14.2f}{_len:>14.2f}"
                         f"{_len - _f:>12.2f}  {'✅ 符合切換前態' if _pre else '🔴 已等於長度'}")
    L.append("-" * 190)
    L.append(f"  ⇒ **切換前態 {_a_pre_ok}/{_a_n}**（F != 側長度）／"
             f"**切換後態 {_a_post_ok}/{_a_n}**（F == 側長度）")

    # ══ (b)(c)(d) ══════════════════════════════════════════════════════
    _tg = None
    for _dg in diag:
        if (_dg["_sb"], str(_dg.get("街廓", "")),
                _sn.get(str(_dg.get("端", "")).strip(), "")) == TARGET \
                and str(_dg.get("候選地號", "")) == "628(5)":
            _tg = _dg
    L.append("")
    L.append("【b】靶格真G（`3.5m R1/right 628(5)`）")
    L.append("-" * 190)
    if _tg is None:
        L.append("  🔴 靶格未取得")
        _b_pre = _b_post = False
    else:
        _v = float(_tg.get("真G(㎡)") or 0)
        _thr = float(_tg.get("門檻(㎡)", 0) or 0)
        _b_pre = abs(_v - EXP["trueG_pre"]) <= 0.005
        _b_post = abs(_v - EXP["trueG_post"]) <= 0.005
        L.append(f"  真G ＝ **{_v:.2f}**　門檻 ＝ {_thr:.2f}　達標 ＝ {_tg.get('達標', '')}")
        L.append(f"  切換前應 == {EXP['trueG_pre']:.2f} ⇒ {'✅' if _b_pre else '🔴'}"
                 f"　／　切換後應 == {EXP['trueG_post']:.2f} ⇒ {'✅' if _b_post else '🔴'}")
        L.append(f"  🔒 **二值互斥**（差 {EXP['trueG_pre'] - EXP['trueG_post']:.2f}）"
                 f"⇒ ⛔ 不可能同時成立 ⇒ 本項具鑑別力。")

    L.append("")
    L.append("【c】靶格結局（`3.5m R1/right`）")
    L.append("-" * 190)
    _w = ((tally["3.5m"]["win"] or {}).get("R1") or {}).get("p2_end")
    _c_pre = (str(_w) == "628(5)")
    _c_post = (not _w)
    L.append(f"  winner ＝ **{_w or '（無人過門檻⇒強制抵費地）'}**")
    L.append(f"  切換前應 ＝ `628(5)` ⇒ {'✅' if _c_pre else '🔴'}"
             f"　／　切換後應 ＝ 無人過門檻 ⇒ {'✅' if _c_post else '🔴'}")

    L.append("")
    L.append("【d】全案街角結局（16 格）")
    L.append("-" * 190)
    _nw = _nf = 0
    _wl, _fl2 = [], []
    for sb in ("0m", "3.5m"):
        for lbl in sorted(cb_by):
            for which in ("left", "right"):
                if which not in (_sd_by.get(lbl) or {}):
                    continue
                _p = ((tally[sb]["win"] or {}).get(lbl) or {}).get(
                    "p1_end" if which == "left" else "p2_end")
                if _p:
                    _nw += 1; _wl.append(f"{sb} {lbl}/{which}")
                else:
                    _nf += 1; _fl2.append(f"{sb} {lbl}/{which}")
    _d_pre = (_nw == EXP["win_pre"] and _nf == EXP["forced_pre"])
    _d_post = (_nw == EXP["win_post"] and _nf == EXP["forced_post"])
    L.append(f"  有 winner ＝ **{_nw}**〔{'／'.join(_wl)}〕")
    L.append(f"  強制抵費地 ＝ **{_nf}**〔{'／'.join(_fl2)}〕")
    L.append(f"  切換前應 ＝ {EXP['win_pre']}／{EXP['forced_pre']} ⇒ {'✅' if _d_pre else '🔴'}"
             f"　／　切換後應 ＝ {EXP['win_post']}／{EXP['forced_post']} ⇒ {'✅' if _d_post else '🔴'}")

    # ══ 總判 ═══════════════════════════════════════════════════════════
    L.append("")
    L.append("【總判】")
    L.append("-" * 190)
    _pre_all = (_a_pre_ok == _a_n) and _b_pre and _c_pre and _d_pre
    _post_all = (_a_post_ok == _a_n) and _b_post and _c_post and _d_post
    L.append(f"  **切換前態**（a∧b∧c∧d）＝ {'✅ 全數成立' if _pre_all else '🔴 未全成立'}")
    L.append(f"  **切換後態**（a∧b∧c∧d）＝ {'✅ 全數成立' if _post_all else '🔴 未全成立'}")
    L.append("  🔒 **本哨兵之合格條件**：**恰有一態成立**（⛔ 兩態同時成立 ⇒ 哨兵無鑑別力·須重設計）。")
    L.append(f"  ⇒ 本次：切換前態 {_pre_all}／切換後態 {_post_all} ⇒ "
             f"**{'✅ 具鑑別力' if _pre_all != _post_all else '🔴 無鑑別力'}**")
    # 🔒 本行**須隨相位改寫**——寫死之結論句於另一相位即自相矛盾（失敗考古節 50 之族）
    if _TAG == "pre":
        L.append("  ⛔ 本相位為**切換前**（`app.py` 之 `F` 槽仍取路寬）⇒ 期望為**切換前態成立**。")
    else:
        L.append("  ✅ 本相位為**切換後**（`F` 槽已取側長度）⇒ 期望為**切換後態成立**。")
        L.append("  🔒 與凍存檔逐項對讀：`verify/out/probe_D1_F_slot_切換前凍存.log`"
                 "（⛔ 該檔一字不得改）。")

    txt = "\n".join(L)
    print(txt)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
