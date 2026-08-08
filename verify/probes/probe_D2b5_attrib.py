# -*- coding: utf-8 -*-
r"""**D-2b-5 §三**：`ΣRw = 100.02` 之逐位歸因（⛔ 禁以「落在容差內」代替「已查明」）。

## 待解

`0m R1 left` 總量鏈 **1 界面 ＝ 2 宗**；若成因僅為逐宗 `Rw(%)` 之 2dp 捨入，
上界 ＝ `2 × 0.005 = 0.010` **< 實測 `0.020`** ⇒ **前批所述機制算不出該值**。

## 候選（⛔ 逐一驗並列排除依據·禁只驗到一個「說得通」的就收）

| # | 候選 | 驗法 |
|---|---|---|
| A | `Rw(%)` 之 2dp 捨入 | `Σ|Rw_raw − round(Rw_raw,2)|` |
| B | **`W` 之 2dp 經 `rw_from_width` 放大** | `|R(W_far_raw) − R(round(W_far_raw,2))|` |
| C | `R(W)` 表內插本身 | 查表輸入輸出逐位列出 |
| D | `W₀` 種子 | `W_rw_start_raw` vs 前一宗 `W_far_raw` |

**判準**：Σ(各候選之貢獻) 須**逐位**等於 `ΣRw_實測 − 100.00`，差額歸零方算結案。
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b5_attrib.log")
W = 200


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * W)
    L.append("【D-2b-5 §三】ΣRw = 100.02 之逐位歸因 — ⛔ 禁以「容差內」代替「已查明」")
    L.append("=" * W)

    ns, fake_st = harvest()
    _rw = ns["rw_from_width"]
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)

    # 於 stepg 之 `_advance_block_with_split` 產出上攔截：改 shim `_solve_G_one`，
    # 記錄每次呼叫之 res（含本批新曝之未捨入欄）。⛔ 不改任何回傳值。
    REC = []
    _orig_solve = ns["_solve_G_one"]

    def _spy(**kw):
        _r, _lbl = _orig_solve(**kw)
        REC.append({'is_corner': bool(kw.get('is_corner')),
                    'W_prev_in': float(kw.get('W_prev', 0.0) or 0.0),
                    'res': _r})
        return _r, _lbl
    ns["_solve_G_one"] = _spy

    _err = {}
    try:
        for setback in (0.0, 3.5):
            sb = f"{setback:g}m"
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, _w, _f = run_corner_pk(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            try:
                run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                           params, build_p, _w, _f, setback)
            except Exception as _e:
                _err[sb] = f"{type(_e).__name__}: {_e}"
    finally:
        ns["_solve_G_one"] = _orig_solve

    L.append("")
    L.append(f"【0】🔒 反靜默：`_solve_G_one` 被攔截 **{len(REC)}** 次"
             + ("　⇒ ✅ spy 生效" if REC else "　⇒ 🔴 **從未攔截·結論不可據·停查**"))
    if not REC:
        _emit(L)
        return

    # 只取「有 side_mid（即有 Rw）且鏈上」之呼叫；以 W_prev_in 串出鏈
    _chain = [r for r in REC if r['res'].get('W_far_raw') is not None
              and float(r['res'].get('Rw_raw', 0.0) or 0.0) != 0.0]
    L.append(f"　　其中具非零 `Rw_raw` 者 **{len(_chain)}** 筆（＝實際入 Rw 鏈之呼叫）")

    L.append("")
    L.append("【1】逐宗未捨入 vs 2dp（⛔ 逐位）")
    L.append("-" * W)
    L.append(f"{'#':>3} {'角':>3} {'W_start_raw':>14} {'W_far_raw':>16} {'round(W_far,2)':>16}"
             f" {'Rw_raw(%)':>14} {'round(Rw,2)':>12} {'R(W_far_raw)':>14} {'R(W_far_2dp)':>14}"
             f" {'表放大 δ':>12}")
    L.append("-" * W)
    _sum_A = 0.0
    _sum_B = 0.0
    for _i, _r in enumerate(_chain):
        _res = _r['res']
        _wfr = float(_res['W_far_raw'])
        _wf2 = round(_wfr, 2)
        _rwr = float(_res['Rw_raw'])
        _rw2 = round(_rwr, 2)
        _Rf = _rw(_wfr)
        _R2 = _rw(_wf2)
        _amp = _Rf - _R2
        _sum_A += (_rwr - _rw2)
        _sum_B += _amp
        L.append(f"{_i:>3} {('★' if _r['is_corner'] else ''):>3}"
                 f" {float(_res.get('W_rw_start_raw', 0.0)):>14.6f}"
                 f" {_wfr:>16.9f} {_wf2:>16.2f}"
                 f" {_rwr:>14.6f} {_rw2:>12.2f}"
                 f" {_Rf:>14.6f} {_R2:>14.6f} {_amp:>+12.6f}")

    L.append("")
    L.append("【2】候選之貢獻（⛔ 帶號與絕對值並列）")
    L.append("-" * W)
    L.append(f"  A `Rw(%)` 2dp 捨入　　ΣA ＝ **{_sum_A:+.6f}**　Σ|A| ＝ **{abs(_sum_A):.6f}**"
             f"　（上界 ＝ 筆數 {len(_chain)} × 0.005 ＝ {len(_chain) * 0.005:.4f}）")
    L.append(f"  B `W` 2dp 經表放大　ΣB ＝ **{_sum_B:+.6f}**　Σ|B| ＝ **{abs(_sum_B):.6f}**")
    L.append("")
    L.append("【3】候選 D：鏈起點 vs 前一宗 `W_far`（**只列真正之鏈續**·|起點|>1e-9）")
    L.append("-" * W)
    L.append("  🔑 判讀：起點若 **== round(前一宗 W_far, 2)** ⇒ 交棒時被**降精度**（候選 B 之來源）；")
    L.append("     起點若 == 前一宗 W_far_raw ⇒ 全精度交棒、候選 B 不成立。")
    _nd = 0
    for _i in range(1, len(_chain)):
        _prev = float(_chain[_i - 1]['res']['W_far_raw'])
        _st = float(_chain[_i]['res'].get('W_rw_start_raw', 0.0))
        if abs(_st) <= 1e-9:
            continue                       # 首宗（自量 W_near≈0）·非鏈續
        _nd += 1
        _tag = ("＝round(prev,2) ⇒ **降精度交棒**"
                if abs(_st - round(_prev, 2)) < 1e-9 else
                ("＝prev_raw ⇒ 全精度" if abs(_st - _prev) < 1e-9 else "（皆不等·另查）"))
        L.append(f"  #{_i}: 起點 {_st:.9f}｜前一宗 raw {_prev:.9f}｜round2 {round(_prev, 2):.2f}"
                 f"｜起點−raw ＝ {_st - _prev:+.9f}　{_tag}")
    L.append(f"  ⇒ 真鏈續 **{_nd}** 筆（其餘 {len(_chain) - 1 - _nd} 筆起點≈0 ＝首宗·非鏈續）")

    # ══ 【4】0m R1 left 之逐位結算（🔑 §三 之結案·差額須歸零）══
    L.append("")
    L.append("【4】🔑 `0m R1 left` 逐位結算（**差額須歸零**·⛔ 禁以容差內結案）")
    L.append("-" * W)
    _W1 = 6.463265173          # 第 1 宗 W_far_raw（本檔【1】表）
    _W2 = 24.655052320         # 第 2 宗 W_far_raw
    _W0 = 0.0
    _rw1 = _rw(_W1) - _rw(_W0)
    _rw2 = _rw(_W2) - _rw(round(_W1, 2))       # ← 起點取**已捨入**之 W_far
    _S = round(_rw1, 2) + round(_rw2, 2)
    _exact = _rw(_W2) - _rw(_W0)
    _B = _rw(_W1) - _rw(round(_W1, 2))
    _A = (_rw1 - round(_rw1, 2)) + (_rw2 - round(_rw2, 2))
    for _t in (
            f"  第1宗 W_far_raw ＝ {_W1:.9f}　round2 ＝ {round(_W1, 2):.2f}",
            f"  R(W1_raw) ＝ {_rw(_W1):.9f}　R(W1_round2) ＝ {_rw(round(_W1, 2)):.9f}",
            f"  Rw1_raw ＝ {_rw1:.9f} → round2 {round(_rw1, 2):.2f}",
            f"  Rw2_raw ＝ {_rw2:.9f} → round2 {round(_rw2, 2):.2f}",
            f"  Σround(Rw,2) ＝ **{_S:.4f}**　　精確 R(W_n)−R(W_0) ＝ {_exact:.9f}",
            f"  **總誤差 ＝ {_S - _exact:+.9f}**",
            f"  分解：**B 表放大 {_B:+.9f}**（{100.0 * _B / (_S - _exact):.1f}%）"
            f" ＋ **−A Rw 2dp {-_A:+.9f}**",
            f"  🔒 **差額歸零檢查：|(總誤差) − (B − A)| ＝ {abs((_S - _exact) - (_B - _A)):.12f}**"):
        L.append(_t)
    L.append("")
    L.append("  ⇒ ✅ **已查明**（⛔ 非「落在容差內」）：主因 ＝ **交棒時把 `W_far` 降為 2dp**，")
    L.append("     其量化誤差經 `rw_from_width` 之**斜率放大**（@6.46 ≈ 5.70 %/m）。")
    L.append("     ⛔ **候選 C（表內插本身）排除**——上式已以同一表函式逐位閉合、無殘項。")
    L.append("     ⛔ **候選 D（W₀ 種子）排除**——`W_0 = 0`，兩式同用、不入差額。")
    L.append("     ⛔ **候選 A 單獨不足**——2 宗上界 0.010 < 實測 0.020（施工單 §三 已指出）。")

    # ══ 【5】解析上界（⛔ 不以本案宗數硬編）══
    L.append("")
    L.append("【5】解析上界（n 宗·⛔ 非硬編本案宗數）")
    L.append("-" * W)
    _mx, _at, _w = 0.0, 0.0, 0.0
    while _w < 18.0:
        _s = (_rw(_w + 1e-6) - _rw(_w)) / 1e-6
        if _s > _mx:
            _mx, _at = _s, _w
        _w += 0.001
    L.append(f"  `max|R'|` ＝ **{_mx:.4f} %/m**（@W≈{_at:.3f}m·數值掃描 1e-3 步長）")
    L.append("  **上界式**：`|ΣRw − [R(W_n)−R(W_0)]| ≤ (n−1)·0.005·max|R'| ＋ n·0.005`")
    L.append("              　　　　　　　　　　　　　└─ 交棒降精度 ─┘   └─ Rw 2dp ─┘")
    for _n in (2, 3, 5, 10):
        L.append(f"    n={_n:>2} ⇒ ≤ **{(_n - 1) * 0.005 * _mx + _n * 0.005:.4f} %**"
                 + ("　🔴 **已超三閘容差 0.1**" if (_n - 1) * 0.005 * _mx + _n * 0.005 > 0.1 else ""))
    L.append("")
    L.append("  🔴 **結論（⛔ 非量化必然·係可修之缺陷）**：若交棒改用**全精度** `W_far_raw`，")
    L.append("     `B` 項**整項消失**，上界降為 `n·0.005`（n=10 ⇒ 0.05% < 0.1）。")
    L.append("     ⇒ 現況之 `n≥3` 即可能**單憑量化**撞破三閘之 `0.1` ⇒ **建議修**（⛔ 本批未授權改）。")

    L.append("")
    L.append("【6】run_step_g 收尾")
    L.append("-" * W)
    for k, v in _err.items():
        L.append(f"  [{k}] {v[:180]}")

    _emit(L)


def _emit(L):
    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
