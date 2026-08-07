# -*- coding: utf-8 -*-
r"""**D-1 §B-4**：與凍存期望表逐格對帳（⛔ 不得修改凍存表）。

比對對象 ＝ `docs/reports/W-G.8_D_期望影響表_凍存.md` §二 四象限表之
**第 3 欄 `F改正×舊門檻`**（`真G／門檻／達標`〔＋`★`＝winner〕）。

🔴 **不符即為發現** ⇒ 逐格列出並停機上呈；⛔ **不得修改凍存表**。

🔒 **對帳之三個欄位皆須比**：`真G`／`門檻`／`達標`（含 `★`）——
⛔ 只比 winner 會漏掉「達標集合變了但 winner 沒變」之情形。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D1_reconcile.log")
FROZEN = os.path.join(REPO, "docs", "reports", "W-G.8_D_期望影響表_凍存.md")
COL = 2          # 0-based：F現行×舊／F現行×新／**F改正×舊**／F改正×新


def main():                                                    # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 190)
    L.append("【D-1 §B-4】與凍存期望表逐格對帳（欄 ＝ **F改正×舊門檻**）— ⛔ 不得修改凍存表")
    L.append("=" * 190)

    # ── 讀凍存表 ────────────────────────────────────────────────────────
    # 🔒 **必須把解析框限制在 §二 之四象限表內**——凍存檔另有 §三 帳目表，
    #   其列首同為 `情境 街廓/側 候選`、**鍵完全相同**，若不設框會**同鍵覆蓋** 10 列。
    #   ⚠️ 前版即如此，且因總列數**恰為 41**（與預期相同）而看起來正常 ⇒ 偽 10 格「不符」。
    _all = io.open(FROZEN, encoding="utf-8").read().splitlines()
    _s = next((i for i, l in enumerate(_all) if l.startswith("情境    街廓/側       候選")), None)
    _e = next((i for i, l in enumerate(_all) if "（★ ＝ 該情境下之 winner）" in l), None)
    if _s is None or _e is None or _e <= _s:
        raise RuntimeError("🔴 凍存檔中找不到 §二 四象限表之框（表頭／表尾）⇒ 停")
    EXP = {}
    _dup = 0
    for ln in _all[_s:_e + 1]:
        m = re.match(r"^(0m|3\.5m)\s+(R\d)/(left|right)\s+(\S+)\s+(.*)$", ln)
        if not m:
            continue
        cells = [c for c in re.split(r"\s{2,}", m.group(5).strip()) if c]
        if len(cells) <= COL:
            continue
        _k = (m.group(1), m.group(2), m.group(3), m.group(4))
        if _k in EXP:
            _dup += 1
        EXP[_k] = cells[COL].strip()
    L.append(f"  凍存表來源：`{os.path.relpath(FROZEN, REPO)}`")
    L.append(f"  🔒 解析框 ＝ §二 四象限表（檔內第 {_s + 1}〜{_e + 1} 行·⛔ 已排除 §三 帳目表）")
    L.append(f"  讀入 **{len(EXP)}** 候選列（框內重複鍵 **{_dup}** ⇒ 應為 0）")
    if _dup:
        raise RuntimeError(f"🔴 框內出現重複鍵 {_dup} 個 ⇒ 解析框仍不正確·停")

    # ── 現況（切換後）────────────────────────────────────────────────────
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    _sn = {"左": "left", "右": "right"}
    NOW = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, _w, _f = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for _dg in (_d0 or []):
            _tg = _dg.get("真G(㎡)")
            NOW[(sb, str(_dg.get("街廓", "")),
                 _sn.get(str(_dg.get("端", "")).strip(), ""),
                 str(_dg.get("候選地號", "")))] = (
                (f"{float(_tg):.2f}" if _tg not in ("", None) else "—")
                + "／" + f"{float(_dg.get('門檻(㎡)', 0) or 0):.2f}"
                + "／" + ("達標" if str(_dg.get("達標", "")) == "達標" else "未達")
                + ("★" if str(_dg.get("選中", "")) == "✅" else ""))

    # ── 逐格對帳 ────────────────────────────────────────────────────────
    L.append("")
    L.append("【A】逐候選對帳（**凍存 vs 現況**·⛔ 三欄皆比：真G／門檻／達標含★）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'候選':<13}{'凍存(F改正×舊門檻)':<26}{'現況(切換後)':<26}  判")
    L.append("-" * 190)
    _ok = _bad = 0
    _mis = []
    for k in sorted(set(EXP) | set(NOW)):
        e = EXP.get(k, "（凍存表無此列）")
        n = NOW.get(k, "—")
        _hit = (e == n)
        if _hit:
            _ok += 1
        else:
            _bad += 1
            _mis.append((k, e, n))
        L.append(f"{k[0]:<6}{k[1] + '/' + k[2]:<12}{k[3]:<13}{e:<26}{n:<26}  "
                 f"{'✅' if _hit else '🔴 **不符**'}")
    L.append("-" * 190)
    L.append(f"  ⇒ 相符 **{_ok}**／不符 **{_bad}**（母體 ＝ 凍存 ∪ 現況 之聯集 {_ok + _bad} 列）")

    L.append("")
    L.append("【B】判定")
    L.append("-" * 190)
    if _bad == 0:
        L.append("  ✅ **逐格全符** ⇒ D-1 之實跑與凍存期望表之 `F改正×舊門檻` 欄**一致**。")
        L.append("  ⇒ **未觸發** §B-4 之停機條件。")
    else:
        L.append(f"  🔴 **不符 {_bad} 格 ⇒ 依 §B-4 為「發現」⇒ 停機上呈**（⛔ 凍存表未改一字）：")
        for k, e, n in _mis:
            L.append(f"     · {k[0]} {k[1]}/{k[2]} {k[3]}　凍存 `{e}`　現況 `{n}`")
    L.append("  ⛔ **凍存表本檔全程唯讀**——未寫入、未改動（本檔僅 `io.open(..., 'r')`）。")

    txt = "\n".join(L)
    print(txt)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
