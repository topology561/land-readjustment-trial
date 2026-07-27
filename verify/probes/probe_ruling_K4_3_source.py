# -*- coding: utf-8 -*-
"""W-G.5 K-4-3 — **街角救援之來源母體**（六變體·兩情境·逐候選逐來源）。

## 題（KL 裁 2026-07-27）

來源須**同時**滿足 (a) 同歸戶 (b) **未達**其所在街廓可分配面積
(c) 其應分配面積 **<** 該街角地候選之應分配面積（「小往較大集中」）；**街廓別不設限**
——M-2「其他可建築街廓」要件於本操作**排除適用**。

## 為何要六變體（**兩處改動方向相反**）

刪同塊排除 ⇒ **放大**來源池；加 (c) ⇒ **縮小**。淨效果不可預判 ⇒ 必須分開量。

| 變體 | 同塊排除 | (c) | 用途 |
|---|---|---|---|
| **A** | 有 | 無 | K-4-3 **前**之現況 |
| **A′** | 有 | 無 | **patch 載具自檢**——以**獨立重寫**之述詞重現 A；須與 A 逐格全等 |
| **B** | 無 | 無 | 只刪同塊排除 |
| **C** | 有 | gtrue | 只加 (c) |
| **D** | 無 | gtrue | ＝ **K-4-3**（＝生產碼現況） |
| **D′** | 無 | **A₀** | (c) 右式改「原位次應分配面積」——供 KL 判 **U-K3** |

⚠️ **A′ 之寫法**（reviewer 明令）：**禁**由生產 `_source_ok` 反向包一層，
否則自檢亦恆真。本檔之六個述詞**皆為獨立閉包**，與生產碼無共用分支。

## 為何逐**候選**而非逐**被救端**（reviewer BLOCKED-2）

本案唯一被救端之來源集在各變體**相同** ⇒ 只看被救端會印出六張一模一樣的表
＝**假綠**（「把綠當過」之形狀）。差異全部落在**未取得資格的候選**上
⇒ 本檔逐 **①候選** 輸出，含 `救援池 ∅` 與 `供給全上仍不足` 者，
並逐來源記下**被 (a)/(b)/(c)/registry 哪一條擋掉**。

## 措辭鐵律（M-5(1) 概念更正）

forced 解鎖 **≠ 抵費地減少**——係**位置由街角移回中間**。
本檔一律用「**抵費地位置移轉**」，**禁「釋回／減少抵費地」語**。

## 重跑
    python verify/probes/probe_ruling_K4_3_source.py     # rc=0 綠／1 紅

⚠️ **零注入·唯讀**：`build_plan` 之輸入 deepcopy；patch 於 finally 還原。
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import m_rescue as m5                                              # noqa: E402
import run_verification as rv                                      # noqa: E402
from app_harvest import harvest                                    # noqa: E402
from selection_pipeline import run_corner_pk                       # noqa: E402
from stepg_pipeline import run_step_g                              # noqa: E402

LOG = os.path.join(VERIFY, "out", "probe_ruling_K4_3_source.log")


def _mk_pred(*, same_block_excl, c_rule, rec):
    """獨立重寫之來源述詞（**不呼生產 `_source_ok`**）。`c_rule` ∈ {None,'gtrue','a0'}。
    每次評估把 (spid, pid, 判定, 擋掉之條件) 記入 `rec`。"""
    def _pred(spid, sr, *, pid, gid, gid_of, u0, reg, gtrue, _A=None, _tgt_blk=None):
        why = None
        if spid == pid or gid_of.get(spid, "") != gid:
            why = "(a)非同歸戶"
        elif same_block_excl and sr.get("所屬街廓") == (_tgt_blk or ""):
            why = "同塊排除(M-2·K-4-3 已廢)"
        elif spid not in u0:
            why = "(b)已達其街廓可分配面積"
        elif c_rule == "gtrue" and not (float(sr.get("G(㎡)", 0) or 0) < float(gtrue)):
            why = f"(c)G_A₀ {float(sr.get('G(㎡)',0) or 0):.2f} ≥ gtrue {float(gtrue):.2f}"
        elif c_rule == "a0" and not (float(sr.get("G(㎡)", 0) or 0)
                                     < float((_A or {}).get(pid, {}).get("G(㎡)", 0) or 0)):
            why = (f"(c′)G_A₀ {float(sr.get('G(㎡)',0) or 0):.2f} ≥ "
                   f"候選A₀ {float((_A or {}).get(pid, {}).get('G(㎡)',0) or 0):.2f}")
        elif reg.is_target(spid):
            why = "registry:已為target"
        elif reg.remaining(spid) <= 1e-6:
            why = "registry:餘量0"
        if why is None or not why.startswith("(a)"):
            rec.append({"cand": pid, "src": spid, "src_blk": sr.get("所屬街廓"),
                        "same_blk": sr.get("所屬街廓") == (_tgt_blk or ""),
                        "G_A0": round(float(sr.get("G(㎡)", 0) or 0), 2),
                        "gtrue": round(float(gtrue), 2), "ok": why is None, "why": why})
        return why is None
    return _pred


def _run_variant(name, *, same_block_excl, c_rule, ctx):
    """跑一次 `build_plan`；回 (plan|None, err, rec)。patch 於 finally 還原。"""
    rec = []
    _A_hint = {}
    _orig = m5._source_ok

    def _patched(spid, sr, *, pid, gid, gid_of, u0, reg, gtrue):
        return _mk_pred(same_block_excl=same_block_excl, c_rule=c_rule, rec=rec)(
            spid, sr, pid=pid, gid=gid, gid_of=gid_of, u0=u0, reg=reg, gtrue=gtrue,
            _A=_A_hint, _tgt_blk=(_A_hint.get(pid) or {}).get("所屬街廓", ""))

    _A_hint.update({r["暫編地號"]: r for r in ctx["gA_rows"]
                    if r.get("推進側別") in ("left", "right")})
    m5._source_ok = _patched
    try:
        plan = m5.build_plan(
            tag=ctx["tag"], gA_rows=copy.deepcopy(ctx["gA_rows"]),
            mina_by_blk=ctx["mina"], gid_of=ctx["gid_of"],
            corner_ctx=copy.deepcopy(ctx["corner_ctx"]), zone_of=ctx["zone_of"],
            pre_price=ctx["pre_price"], true_g_fn=ctx["true_g_fn"],
            diag_rows=ctx["diag"])
        return plan, None, rec
    except Exception as e:
        return None, f"{type(e).__name__}: {e}", rec
    finally:
        m5._source_ok = _orig


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    L, bad = [], []
    L.append("=" * 118)
    L.append("【K-4-3】街角救援來源母體 —— 六變體 × 兩情境（逐 ①候選 逐來源）")
    L.append("=" * 118)

    snap = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fs = harvest()
    cb_by, cad = rv.build_pipeline(ns, fs, snap)
    rv.build_ownership(ns, fs, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    tp, bp, _ = rv.build_build_parcels(ns, fs, v6, list(cb_by.values()), snap)
    mina = rv.wf_f0_mina(ns, snap, cb_by)
    _zof = snap["財務接線_v3"]["原地號_區段"]
    _pre = {z: float(v["單價_元每m2"]) for z, v in
            snap["財務接線_v3"]["重劃前區段_面積單價"].items()}

    VARIANTS = (("A  現況(K-4-3 前)", True, None),
                ("A′ patch 載具自檢", True, None),
                ("B  只刪同塊排除", False, None),
                ("C  只加 (c)·gtrue", True, "gtrue"),
                ("D  ＝K-4-3（生產碼）", False, "gtrue"),
                ("D′ (c) 右式改 A₀", False, "a0"))

    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fs, cb_by, cad, snap, setback)
        diag, sel, off, win, fo = run_corner_pk(
            ns, fs, list(cb_by.values()), cad, params, tp, bp, setback, snapshot=snap)
        _fo_ends = [(b, s) for b, f_ in (fo or {}).items()
                    for s in ("left", "right") if f_.get(f"{s}_forced_offset")]
        L.append("")
        L.append(f"── 情境 {tag} ──  強制抵費地端（趟0）＝ {sorted(_fo_ends) or '∅'}")
        if not _fo_ends:
            L.append("    ⚠️ 該情境 **無 forced 端 ⇒ M-5 根本不執行**；六變體必然全空，"
                     "**此空表不得讀為「K-4-3 無衝擊」之證據**。")
            continue
        sg0 = run_step_g(ns, fs, list(cb_by.values()), cad, snap,
                         params, bp, win, fo, setback)
        _bp_by = {b.get("暫編地號"): b for b in bp}
        _omap = fs.session_state.get("t8_ownership_map", {}) or {}
        ctx = {
            "tag": tag, "gA_rows": sg0["g_rows"], "mina": mina,
            "gid_of": {p: _omap.get((_bp_by.get(p) or {}).get("原地號", ""), "") for p in _bp_by},
            "zone_of": {p: _zof.get((_bp_by.get(p) or {}).get("原地號", ""), "") for p in _bp_by},
            "pre_price": _pre, "diag": diag,
            "corner_ctx": rv._m5_corner_ctx(diag, sel, _fo_ends),
            "true_g_fn": rv._m5_true_g_fn(ns, fs, cb_by, cad, snap, params, bp, setback),
        }
        _base = None
        for _nm, _sbe, _cr in VARIANTS:
            plan, err, rec = _run_variant(_nm, same_block_excl=_sbe, c_rule=_cr, ctx=ctx)
            _aw = (plan or {}).get("awards", []) if plan else []
            _reg = ((plan or {}).get("registry").summary() if plan else {})
            _t2_raise = bool(err and "M-5 ②" in str(err))
            _sig = json.dumps({"awards": [{k: a[k] for k in
                                           ("blk", "side", "winner", "need_p", "g_at",
                                            "stage3", "n_qualified")} for a in _aw],
                               "allocs": [[a["blk"], a["side"],
                                           sorted((x["src"], x["a_prime"], x["stage"])
                                                  for x in a["allocs"])] for a in _aw],
                               "reg": _reg}, ensure_ascii=False, sort_keys=True)
            _same_blk_used = sorted({r["src"] for r in rec if r["ok"] and r["same_blk"]})
            L.append("")
            L.append(f"  【{_nm}】 award {len(_aw)}｜②_t2 觸發 raise：{'是' if _t2_raise else '否'}"
                     f"｜同塊源**實際被納入候選池**：{_same_blk_used or '∅'}")
            if err:
                L.append(f"      🔴 raise：{err[:150]}")
            for a in _aw:
                L.append(f"      award {a['blk']}{a['side']} winner={a['winner']}"
                         f" need_p={a['need_p']} g_at={a['g_at']} stage3={a['stage3']}")
                for x in a["allocs"]:
                    L.append(f"        · 源 {x['src']} a′={x['a_prime']} {x['stage']}")
            L.append(f"      registry: {_reg.get('sources') or '∅'} → {_reg.get('targets') or '∅'}")
            # 逐 ①候選 逐來源（**含被擋掉者**·BLOCKED-2 之對治）
            _by_cand = {}
            for r in rec:
                _by_cand.setdefault(r["cand"], []).append(r)
            for _c in sorted(_by_cand):
                _rows = _by_cand[_c]
                _ok = [r for r in _rows if r["ok"]]
                L.append(f"      ①候選 {_c}：合格來源 {len(_ok)}／評估 {len(_rows)}")
                for r in sorted(_rows, key=lambda x: (not x["ok"], x["src"])):
                    L.append(f"          {'✅' if r['ok'] else '⛔'} {r['src']:>12}"
                             f" blk={r['src_blk']:>4} {'同塊' if r['same_blk'] else '他塊'}"
                             f" G_A₀={r['G_A0']:>8.2f} gtrue={r['gtrue']:>8.2f}"
                             f"{'' if r['ok'] else '  ← ' + str(r['why'])}")
            if _base is None:
                _base = _sig
                L.append("      （基準）")
            else:
                L.append(f"      vs A：{'逐格全等' if _sig == _base else '🚩 **有差異**'}")
                if _nm.startswith("A′") and _sig != _base:
                    bad.append(f"[{tag}] A′ 載具自檢失敗（應與 A 逐格全等）")

    L.append("")
    L.append("-" * 118)
    L.append("📌 措辭：forced 解鎖 ＝ **抵費地位置由街角移回中間**（總量不變）；禁「釋回／減少抵費地」語。")
    if bad:
        L.append(f"RESULT: FAIL（{len(bad)} 違例）")
        for x in bad[:20]:
            L.append("  " + x)
    else:
        L.append("RESULT: PASS（A′ 載具自檢通過·差異逐格列於上表）")
    L.append("=" * 118)
    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
