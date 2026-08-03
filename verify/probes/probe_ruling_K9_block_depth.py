# -*- coding: utf-8 -*-
"""K-9-2 街廓層剖面深度警示 — **碼面自算實測**（K-6-A2 段一）。

## 本探針之用途

`k92_block_depth_check` 之接線於**本案為零警示**（六街廓餘裕 15.37m 以上），
而「零警示之接線」與「根本沒接線」**外觀相同**。本探針即為此提供**碼面自算輸出**：
逐街廓印出剖面兩端垂距、剖面最小深度、附表門檻、餘裕、判定。

⛔ **禁抄交辦文之數字**——本檔一律由 `app` 之碼現算。
🔴 **唯一算法源＝`app.n19p_depth_info_by_label` ＋ `app.k92_block_depth_check`**
   （`grep -n "def k92_block_depth_check" app.py`）。
   禁在 `verify/` 側另寫一套深度算法或另訂一套判準——那是用自己的尺去驗別人的機制。

## 判準（正典 K-9-2·逐字）

> 前緣線上每一點沿 **BASELINE 法向**至 BASELINE 之垂距，
> **任一點 ≤ 畸零地最小深度即警示**（**等於也警示**）。

解析：兩線皆直線 ⇒ 垂距沿弦**線性** ⇒ min 必落於前緣線兩端之一。**禁取樣、禁掃描。**

## 兩個「最小深度」（K-9-6-a·嚴禁互代）

| # | 名 | 本檔欄位 | 本案值 |
|---|---|---|---|
| 1 | **量測值**：該街廓剖面之最小深度 | `D_k92_min` | 33〜47m |
| 2 | **門檻值**：畸零地**附表**之最小深度 | `min_depth_table` | 14.00 |

此處係附表門檻之**正確**用途（K-9-6：附表值＝可建築門檻）；
與 **GB-13** 所述「附表值被誤用為**量測帶深**」係兩回事、勿混。

## 資料源

- 深度：`app.n19p_depth_info_by_label`（自 `data/V6.dxf` 現算·K-8 §三 commit A 之同源鏈）
- 正面路寬：快照 `verify/case_params_UC9898.json` 之 `blocks[*].正面.路寬_m`
  ——即 `run_verification.build_param_table` 之 `正面路寬(m)` 同源
  （app-live 側對應 `sb['rows']` 之 `正面路寬(m)`；本案二者同值 12/8/8/12/8/8）。

## 對照靶（正典 K-8 §二 兩端垂距表·**供對拍、非本檔之值來源**）

R1 33.164/33.128・R2 44.954/43.981・R3 43.772/44.898・
R4 33.126/33.084・R5 43.510/47.904・R6 47.657/43.361

## 重跑

    python verify/probes/probe_ruling_K9_block_depth.py

rc 恆 0（**只量不判**；本檔不作為閘）。輸出 `verify/out/probe_ruling_K9_block_depth.log`。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_ruling_K9_block_depth.log")


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 118)
    L.append("【K-9-2 街廓層剖面深度警示】碼面自算實測（K-6-A2 段一）")
    L.append("判準：前緣線上任一點沿 BASELINE 法向至 BASELINE 之垂距 ≤ 畸零地最小深度 ⇒ 警示"
             "（**等於也警示**）")
    L.append("算法源：app.n19p_depth_info_by_label ＋ app.k92_block_depth_check（禁 verify 側另寫）")
    L.append("=" * 118)

    ns, _fs = harvest()
    for _sym in ("n19p_depth_info_by_label", "k92_block_depth_check"):
        if not callable(ns.get(_sym)):
            raise RuntimeError(f"🔴 harvest 未取得 {_sym}（K-6-A2 段一之接線未落地？）")

    # 深度：與 `run_verification.n19p_depth_by_block` 同一條鏈（現算·非快照）
    cb, cad = rv._build_cb_cad(ns)
    fcb = ns.get("F3_CATEGORY_BURDEN", {})
    build_blocks = [b for b in cb
                    if fcb.get(b.get("category", ""), "") == "可建築土地"]
    depth_info = ns["n19p_depth_info_by_label"](
        build_blocks,
        cad.get("alloc_dir_by_block", {}) or {},
        cad.get("front_lines", {}) or {},
        cad.get("baselines", {}) or {})

    # 正面路寬：快照（＝ build_param_table 之同源）。缺格不兜底 ⇒ 交由被測函式 loud raise。
    snap = rv.load_snapshot_raw()
    fw_by = {lbl: float(((snap.get("blocks") or {}).get(lbl) or {})
                        .get("正面", {}).get("路寬_m", 0.0) or 0.0)
             for lbl in [b["label"] for b in build_blocks]}

    rows = ns["k92_block_depth_check"](build_blocks, depth_info, fw_by)

    L.append("")
    L.append("【A】逐街廓剖面深度 vs 畸零地附表門檻")
    L.append("-" * 118)
    L.append(f"{'街廓':<6}{'分區':<8}{'正面路寬':>9}{'d(p1左)':>12}{'d(p2右)':>12}"
             f"{'剖面最小':>12}{'附表門檻':>10}{'餘裕':>11}   判定")
    L.append("-" * 118)
    for r in sorted(rows, key=lambda x: x["label"]):
        L.append(f"{r['label']:<6}{r['category']:<8}{r['front_road_width_m']:>9.2f}"
                 f"{r['d_front_p1']:>12.3f}{r['d_front_p2']:>12.3f}"
                 f"{r['D_k92_min']:>12.3f}{r['min_depth_table']:>10.2f}"
                 f"{r['margin']:>+11.3f}   {'🔴 警示' if r['warn'] else '✅ 無警示'}")
    L.append("-" * 118)

    _bad = [r for r in rows if r["warn"]]
    _tight = min(rows, key=lambda r: r["margin"]) if rows else None
    L.append("")
    L.append("【B】彙總")
    L.append(f"  街廓數（可建築）        ＝ {len(rows)}")
    L.append(f"  警示數                  ＝ {len(_bad)}"
             f"{'（' + '／'.join(r['label'] for r in _bad) + '）' if _bad else ''}")
    if _tight is not None:
        L.append(f"  餘裕最緊者              ＝ {_tight['label']}　"
                 f"{_tight['D_k92_min']:.3f}m − {_tight['min_depth_table']:.2f}m "
                 f"= {_tight['margin']:+.3f}m")
    L.append("")
    L.append("【C】註記")
    L.append("  · 剖面最小 ＝ min(前緣線兩端垂距)；線性 ⇒ 兩端取 min 即全段 min（解析·禁取樣）。")
    L.append("  · 本表為**量測值 vs 門檻值**之對照；K-9-3：街廓層過 ⇒ 宗地層一律不量深度。")
    L.append("  · K-9 §二-1 之封閉性另需扣「該街廓最大截角股長」（見正典 ②-1），本表不含該扣減；")
    L.append("    該扣減屬 K-9-8 虛擬量測塊之範圍（GB-18／GB-19·尚未實作）。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
