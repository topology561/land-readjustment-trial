# -*- coding: utf-8 -*-
r"""**D-2b-6 §一**：逐街廓分跑之**保值性實證**（⛔ 不得採信結構論證·須逐欄 `==`）。

## 假說（施工單 §〇-3）

限縮 `parcels_by_block` 為單一街廓、`cb` **維持全集**（`compute_total_burden_rate` 之母體
＝ `cb` 中 `category` 屬「共同負擔」者 ＋ `snapshot["財務接線_v3"]`，**與 `parcels_by_block` 無關**）
⇒ 各街廓可各自跑完，**且其輸出與全跑時逐欄相同**。

## 手法（⛔ 全精度比·⛔ 不得先 round·⛔ 禁「差在容差內即通過」）

同一情境跑兩次：
- **A 全跑**：`build_parcels` 原樣（R1 仍於閘中止）
- **B 單跑**：`build_parcels` 濾為 `所屬街廓 == R1`

兩次皆：
1. spy `_solve_G_one`——記錄**每次呼叫之全部入參 ＋ 全精度回傳欄**（⛔ 非 2dp 顯示欄）
2. 攔截 `run_step_g` 之 **stdout 逐字**（含 `[T2-DIAG]`／`[Δ_i·…]`）
3. 記錄**終止例外之逐字**

**驗收 ＝ 三者逐字／逐值 `==`**。任一不符 ⇒ 🛑 停機上呈（§九-1）。

⚠️ spy 只在 `run_step_g` 期間掛上——`run_corner_pk`（PK）亦呼叫 `_solve_G_one`，
若不隔離會把 PK 之 132 次混入母體、使比對失去鑑別力。
"""
import io
import os
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
LOG = os.path.join(OUTDIR, "probe_D2b6_split.log")
TARGET = "R1"
W = 200

# 全精度欄（⛔ 非 2dp 顯示欄）＋ 供對照之顯示欄
KEYS = ("S_raw", "W_far_raw", "Rw_raw", "W_rw_start_raw",
        "G", "S", "W", "W_far", "W_near", "Rw_pct", "area_geom",
        "iterations", "converged", "_alloc_dir_used")


def _snap(res):
    out = {}
    for k in KEYS:
        v = res.get(k)
        out[k] = repr(v)
    return out


def _run_once(ns, fake_st, cb_all, cad, snapshot, params, build_p, wins, forced,
              setback, only_block=None):
    """回傳 (spy_records, stdout_text, err_text)。"""
    bp = build_p if only_block is None else [
        tp for tp in build_p if tp.get("所屬街廓") == only_block]
    rec = []
    _orig = ns["_solve_G_one"]

    def _spy(**kw):
        _r, _lbl = _orig(**kw)
        rec.append({
            "in": {k: repr(kw.get(k)) for k in
                   ("a_m2", "A", "l_front", "l_side", "F", "S_max",
                    "is_corner", "side", "avg_depth", "B", "C",
                    "tab6_burden", "allocation_dir", "side_mid", "W_prev")},
            "out": _snap(_r), "solver": _lbl})
        return _r, _lbl

    ns["_solve_G_one"] = _spy
    buf = io.StringIO()
    err = ""
    try:
        with contextlib.redirect_stdout(buf):
            try:
                run_step_g(ns, fake_st, cb_all, cad, snapshot,
                           params, bp, wins, forced, setback)
            except Exception as e:
                err = f"{type(e).__name__}: {e}"
    finally:
        ns["_solve_G_one"] = _orig
    return rec, buf.getvalue(), err


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * W)
    L.append(f"【D-2b-6 §一】逐街廓分跑保值性實證（靶街廓 ＝ {TARGET}）— ⛔ 逐欄 `==`·禁容差")
    L.append("=" * W)
    L.append("  🔒 全精度比（`S_raw`／`W_far_raw`／`Rw_raw`／`W_rw_start_raw`）·⛔ 不得先 round")
    L.append("  🔒 spy 僅於 `run_step_g` 期間掛上（隔離 PK 之呼叫·否則母體混入、失鑑別力）")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())

    _tot_fail = 0
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)

        recA, outA, errA = _run_once(ns, fake_st, cb_all, cad, snapshot,
                                     params, build_p, wins, forced, setback, None)
        recB, outB, errB = _run_once(ns, fake_st, cb_all, cad, snapshot,
                                     params, build_p, wins, forced, setback, TARGET)

        L.append("")
        L.append(f"【{sb}】A 全跑 vs B 單跑（{TARGET}）")
        L.append("-" * W)
        L.append(f"  `_solve_G_one` 呼叫數：A ＝ **{len(recA)}**　B ＝ **{len(recB)}**"
                 + ("　✅ 相同" if len(recA) == len(recB) else "　🔴 **不同**"))
        if len(recA) == 0:
            L.append("  🔴 **A 之呼叫數為 0 ⇒ 母體為空、比對無鑑別力·停查**")
            _tot_fail += 1

        # 1) 逐呼叫逐欄比對
        _n = min(len(recA), len(recB))
        _bad = []
        for i in range(_n):
            for sec in ("in", "out"):
                for k, v in recA[i][sec].items():
                    if recB[i][sec].get(k) != v:
                        _bad.append((i, sec, k, v, recB[i][sec].get(k)))
            if recA[i]["solver"] != recB[i]["solver"]:
                _bad.append((i, "solver", "-", recA[i]["solver"], recB[i]["solver"]))
        L.append(f"  ① 逐呼叫逐欄比對：母體 **{_n}** 次 × {len(KEYS) + 15} 欄"
                 f"　不符 **{len(_bad)}**"
                 + ("　✅ **逐欄 ==**" if not _bad and _n > 0 else ""))
        for b in _bad[:20]:
            L.append(f"      🔴 #{b[0]} {b[1]}.{b[2]}：A={b[3]} ／ B={b[4]}")
        if _bad:
            _tot_fail += 1
        if _n == 0:
            L.append("      🔴 **母體 0 ⇒ 「不符 0」係<u>空真</u>·⛔ 不得判過**")
            _tot_fail += 1

        # 2) stdout 逐字
        _sameout = (outA == outB)
        L.append(f"  ② `run_step_g` stdout 逐字：A {len(outA)} 字／B {len(outB)} 字"
                 + ("　✅ **逐字 ==**" if _sameout else "　🔴 **不同**"))
        if not _sameout:
            _tot_fail += 1
            _la, _lb = outA.splitlines(), outB.splitlines()
            for i in range(max(len(_la), len(_lb))):
                a = _la[i] if i < len(_la) else "（無）"
                b = _lb[i] if i < len(_lb) else "（無）"
                if a != b:
                    L.append(f"      🔴 line {i + 1}：")
                    L.append(f"        A: {a[:170]}")
                    L.append(f"        B: {b[:170]}")
                    break

        # 3) 終止例外逐字
        _sameerr = (errA == errB)
        L.append(f"  ③ 終止例外逐字："
                 + ("✅ **==**" if _sameerr else "🔴 **不同**"))
        L.append(f"      A: {errA[:170] or '（無例外）'}")
        if not _sameerr:
            L.append(f"      B: {errB[:170] or '（無例外）'}")
            _tot_fail += 1

    # ══ 【II】🔑 真正有鑑別力之測：**兩個非首街廓** solo vs 同跑 ══
    #   【I】之靶為 R1 ＝ 迴圈**第一個**街廓 ⇒ 其「不受他塊影響」是**平凡**的。
    #   真問題是「**B 街廓之結果會不會因為 A 街廓也在跑而改變**」——須以**兩個都能跑完**
    #   之街廓對測（R1 會中止、不可用）。
    L.append("")
    L.append("【II】🔑 非首街廓之兩兩獨立性（**本節才有鑑別力**·【I】之 R1 為首塊·平凡）")
    L.append("-" * W)
    _all_lbl = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in _all_lbl:
            _all_lbl.append(_l)
    L.append(f"  `build_parcels` 之街廓序（＝迴圈序）：{_all_lbl}")
    _cands = [x for x in _all_lbl if x != TARGET]
    if len(_cands) < 2:
        L.append("  🔴 可用街廓不足 2 個 ⇒ 本節無法執行")
        _tot_fail += 1
    else:
        _p, _q = _cands[0], _cands[1]
        setback = 0.0
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)

        def _solo(lbl):
            return _run_once(ns, fake_st, cb_all, cad, snapshot, params,
                             [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                             wins, forced, setback, None)

        recP, outP, errP = _solo(_p)
        recQ, outQ, errQ = _solo(_q)
        recPQ, outPQ, errPQ = _run_once(
            ns, fake_st, cb_all, cad, snapshot, params,
            [tp for tp in build_p if tp.get("所屬街廓") in (_p, _q)],
            wins, forced, setback, None)
        L.append(f"  0m｜solo {_p} ＝ {len(recP)} 次（例外：{errP[:60] or '無'}）")
        L.append(f"  0m｜solo {_q} ＝ {len(recQ)} 次（例外：{errQ[:60] or '無'}）")
        L.append(f"  0m｜同跑 {_p}+{_q} ＝ {len(recPQ)} 次（例外：{errPQ[:60] or '無'}）")
        # 🔑 同跑於**第一個**街廓即中止（每塊目前皆撞閘）⇒ 呼叫數必 < solo 之和。
        #   ⇒ 改比 **prefix**：同跑之前 len(recPQ) 次，須逐欄等於 solo(_p) 之對應次。
        #   ⚠️ 這**只能**證「前塊不受後塊影響」；「後塊不受前塊影響」在**每塊皆中止**之現狀
        #      **無法直接測**（同跑永遠到不了第二塊）——⛔ 照實聲明、不得含糊。
        _pref = min(len(recPQ), len(recP))
        if _pref == 0:
            L.append("  🔴 prefix 母體 0 ⇒ **空真**·⛔ 不得判過")
            _tot_fail += 1
        else:
            _bad2 = []
            for i in range(_pref):
                for sec in ("in", "out"):
                    for k, v in recP[i][sec].items():
                        if recPQ[i][sec].get(k) != v:
                            _bad2.append((i, sec, k, v, recPQ[i][sec].get(k)))
            L.append(f"  **prefix 比對**（solo {_p} vs 同跑之前 {_pref} 次）：不符 **{len(_bad2)}**"
                     + (f"　✅ **逐欄 ==** ⇒ {_p} 不受 {_q} 在列影響" if not _bad2 else ""))
            for b in _bad2[:15]:
                L.append(f"      🔴 #{b[0]} {b[1]}.{b[2]}：solo={b[3]} ／ 同跑={b[4]}")
            if _bad2:
                _tot_fail += 1
            L.append(f"  ⚠️ **鑑別力界限**：同跑於 {_p} 即中止（{len(recPQ)} 次 < solo 之和 "
                     f"{len(recP) + len(recQ)}）⇒ **到不了 {_q}**")
            L.append(f"     ⇒ 本測**只證「前塊不受後塊影響」**；"
                     f"「**後塊不受前塊影響**」於現狀（每塊皆中止）**無法直接測**。")
            L.append(f"     ⇒ 分跑之保值性目前建立於：①【I】R1 全跑 vs 單跑逐欄 == ；"
                     f"②本節 prefix == ；③`cb`／`snapshot`（唯一跨塊輸入）**兩模式皆全集不變**。")

    # ══ 【III】全街廓 solo 掃描（＝ §五 之前置·首次取得 R2–R6 之診斷）══
    L.append("")
    L.append("【III】全街廓 solo 掃描（0m／3.5m）— **首次取得 R2–R6**")
    L.append("-" * W)
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in _all_lbl:
            _r, _o, _e = _run_once(
                ns, fake_st, cb_all, cad, snapshot, params,
                [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                wins, forced, setback, None)
            _st = "✅ 跑完（無例外）" if not _e else f"🔴 {_e}"
            L.append(f"  [{sb}] {lbl:<4} `_solve_G_one` {len(_r):>3} 次｜{_st[:150]}")

    L.append("")
    L.append("【判定】")
    L.append("-" * W)
    L.append("  ⚠️ **【I】② 之鑑別力聲明**：A／B 之 `run_step_g` stdout **皆為 0 字**"
             "（覆蓋閘於 `_pool_strips_for_block` 內先 raise、早於 `[T2-DIAG]` 之列印）")
    L.append("     ⇒ 該項之「逐字 ==」係**空真**、**無鑑別力**，⛔ 不得列為佐證。"
             "有鑑別力者為 ①（29 欄 × 10 次）與 ③。")
    if _tot_fail == 0:
        L.append("  ✅ **分跑保值性成立**——A 全跑與 B 單跑於靶街廓之"
                 "**入參／全精度輸出／stdout／例外** 皆逐欄逐字相同。")
        L.append("  ⇒ 施工單 §〇-3 之結構論證**經實證確認**；D-2b-2「分跑不保值」之判斷**確為錯誤**。")
    else:
        L.append(f"  🛑 **不符 {_tot_fail} 項 ⇒ 依 §九-1 停機上呈**（⛔ 不得續行 §四／§五）")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
