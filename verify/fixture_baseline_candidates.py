# -*- coding: utf-8 -*-
"""W-G.5 C-5 夾具 — BASELINE 候選之**三分支**（KL 裁 2026-07-26·補件）。

## 存在理由

C-1/C-2 把 BASELINE 改成結構性 1:N 配對，但**決勝仍是「垂距最小」靜默取**
（舊 `if _best is None or _t_mid < _best[0]`），**未接入** C-11 之
`_ambig`／`CadBindingAmbiguity` 機制。而實測 **R1 之候選勝差僅 0.05m**
（FRONT 80.26m／SIDE 29.56m 相比之下是碾壓）——
🔴 **唯一薄的那個綁定，正是唯一沒有閘的**（KL 指認）。

## 三分支（C-5·canonical）

| # | 條件 | 處置 |
|---|---|---|
| ① | ≥2 候選且**量測值等價**：`max(perp)−min(perp) ≤ eps`，`eps = max(_EPS_LEGAL, min(k·q·(L/ℓ), _EPS_LEGAL_CEIL))` | 取確定性規則（最小 DXF handle）＋記 `_match.equivalent_n`；**不進 `_ambig`** |
| ② | ≥2 候選、非①、勝差 ≤ `_BL_PERP_TOL_M` | **進 `_ambig`** → `CadBindingAmbiguity` → UI 確認頁（**設計好的安全閥·非故障**·成本＝一次點選） |
| ③ | ≥2 候選、非①、勝差 > 門檻 | 採垂距最小者（真正的屁股線） |

## 本夾具之檢查

- **分支① golden ＝ UC9898 之 R1**（BL#1／BL#3 共線·已實證方位差 0.0005°、互垂距 0.0000）
  ⇒ `equivalent_n == 2` 且 **不觸發** `CadBindingAmbiguity`。
- **分支②／③** 以**合成幾何**構造（不倚賴本案 CAD·`fixture-provenance`：期望值由**手算**給出）。
- **反例自證**：把分支②之兩條 BASELINE 改成共線 ⇒ 應由 ② 轉 ①（不再 raise）
  ⇒ 證明本夾具測到的是「共線與否」、非恆真。

## 重跑
    python verify/fixture_baseline_candidates.py        # rc=0 綠／rc=1 紅
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402


class _E:
    """最小 DXF 實體替身（`parse_cad_precision_layers` 只用 layer/handle/dxftype/start/end）。"""

    class _D:
        pass

    def __init__(self, layer, p1, p2, handle):
        self.dxf = _E._D()
        self.dxf.layer = layer
        self.dxf.handle = handle
        self.dxf.start = type("P", (), {"x": p1[0], "y": p1[1], "z": 0.0})()
        self.dxf.end = type("P", (), {"x": p2[0], "y": p2[1], "z": 0.0})()

    def dxftype(self):
        return "LINE"


class _Msp:
    def __init__(self, e):
        self._e = list(e)

    def query(self, *_a, **_k):
        return list(self._e)


class _Doc:
    def __init__(self, e):
        self._e = list(e)

    def modelspace(self):
        return _Msp(self._e)


def _synth_block(lbl, w=60.0, d=40.0, x0=0.0, y0=0.0):
    """合成矩形街廓：FRONT 在 y=y0（下緣）、屁股在 y=y0+d。"""
    return {
        "label": lbl, "category": "住宅區",
        "vertices": [(x0, y0), (x0 + w, y0), (x0 + w, y0 + d), (x0, y0 + d), (x0, y0)],
        "area_m2": w * d,
        "centroid": (x0 + w / 2.0, y0 + d / 2.0),
    }


def _synth_dxf_bytes(decimals):
    """合成**最小 ASCII DXF 文字**，其坐標群碼之值恰有 `decimals` 位小數
    ⇒ 供 `_detect_dxf_quantum` 測出 `q = 10**-decimals`。
    （本夾具不解析此文字·僅用於 q 偵測·故毋須完整 DXF 結構。）"""
    _v = "1." + "0" * decimals
    return ("\n".join([" 10", _v, " 20", _v, " 11", _v, " 21", _v])).encode("ascii")


def _run(ns, blocks, lines, dxf_bytes=None):
    """回 (result, exc)。exc 為 CadBindingAmbiguity 或 None。"""
    ents = [_E(ly, a, b, h) for (ly, a, b, h) in lines]
    try:
        return ns["parse_cad_precision_layers"](
            _Doc(ents), blocks, dxf_bytes=dxf_bytes), None
    except ns["CadBindingAmbiguity"] as e:
        return None, e


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ns, fake_st = harvest()
    out = []
    ok = True

    W, D = 60.0, 40.0
    blk = [_synth_block("R9")]
    FRONT = ("FRONT_LINE", (0.0, 0.0), (W, 0.0), "F1")

    # ── 分支①：兩條 BASELINE **共線**（皆在 y=D 上·分成兩段）──────────────────
    r1, e1 = _run(ns, blk, [FRONT,
                            ("BASELINE", (0.0, D), (25.0, D), "B1"),
                            ("BASELINE", (30.0, D), (W, D), "B2")])
    if e1 is not None:
        ok = False
        out.append(f"  分支① 共線兩段：🔴 不應 raise，卻得 CadBindingAmbiguity（{len(e1.items)} 項）")
    else:
        _m1 = ((r1.get("baselines") or {}).get("R9") or {}).get("_match") or {}
        _eq = _m1.get("equivalent_n")
        _hd = _m1.get("handle")
        _hit = (_eq == 2 and _hd == "B1")       # 手算：兩段共線 ⇒ n=2；確定性取最小 handle "B1"
        ok &= _hit
        out.append(f"  分支① 共線兩段：equivalent_n={_eq}(期 2)　handle={_hd}(期 B1)"
                   f"　垂距={_m1.get('perp_mid_m')}(期 {D:.1f})　{'✅' if _hit else '🔴'}")

    # ── 分支②：兩條**不共線**、垂距接近（勝差 0.3m ≤ 容差 1.0）⇒ 應 raise ────────
    #   手算：BASELINE-a 在 y=D；BASELINE-b 在 y=D+0.3（平行但非同線·互垂距 0.3 ≤1.0
    #   ⇒ 🔴 注意：0.3 ≤ perp_tol ⇒ 仍判**共線**）。故取 y=D+1.5（互垂距 1.5 >1.0 ⇒ 不共線）
    #   而勝差 1.5 > 1.0 ⇒ 落分支③。欲構分支②須「不共線且勝差 ≤1.0」——
    #   以**夾角**製造：b 與 FRONT 夾 5°（≤10° 仍過 (a)），過點使中點垂距僅差 0.4m。
    _ang = 5.0
    _t = math.tan(math.radians(_ang))
    _bx0, _by0 = 0.0, D + 0.4 - (W / 2.0) * _t
    r2, e2 = _run(ns, blk, [FRONT,
                            ("BASELINE", (0.0, D), (W, D), "B1"),
                            ("BASELINE", (_bx0, _by0), (_bx0 + W, _by0 + W * _t), "B2")])
    _hit2 = (e2 is not None and any(it.get("layer") == "BASELINE" for it in e2.items))
    ok &= _hit2
    out.append(f"  分支② 不共線·勝差 0.40m ≤ 容差 1.0m："
               f"{'✅ 已 raise CadBindingAmbiguity' if _hit2 else '🔴 未 raise（靜默選了）'}")
    if _hit2:
        _it = [i for i in e2.items if i.get("layer") == "BASELINE"][0]
        out.append(f"      候選：{[(c.get('baseline_handle'), c.get('perp_m')) for c in _it['candidates']]}")

    # ── 分支③：兩條不共線、勝差 > 容差 ⇒ 取垂距最小者、不 raise ──────────────────
    r3, e3 = _run(ns, blk, [FRONT,
                            ("BASELINE", (0.0, D), (W, D), "B1"),
                            ("BASELINE", (0.0, D + 8.0), (W, D + 8.0), "B2")])
    if e3 is not None:
        ok = False
        out.append(f"  分支③ 勝差 8.0m > 容差：🔴 不應 raise")
    else:
        _m3 = ((r3.get("baselines") or {}).get("R9") or {}).get("_match") or {}
        _hit3 = (abs(float(_m3.get("perp_mid_m", -1)) - D) < 1e-6
                 and _m3.get("equivalent_n") == 1)
        ok &= _hit3
        out.append(f"  分支③ 勝差 8.0m > 容差：垂距={_m3.get('perp_mid_m')}(期 {D:.1f})"
                   f"　equivalent_n={_m3.get('equivalent_n')}(期 1)　{'✅' if _hit3 else '🔴'}")

    # ── 🆕 C-5 收尾（KL 令）：兩線**近平行但互垂距 0.5m**（非共線）⇒ 須**轉② raise**，
    #    **不得被①吸收**。手算：B1 在 y=D、B2 在 y=D+0.5 ⇒ 垂距 40.0 vs 40.5、
    #    max−min = 0.5m。舊碼以 `perp_tol_m=1.0` 判「同一條線」⇒ 0.5 ≤ 1.0 ⇒ **被①吸收**
    #    ⇒ 靜默取最小 handle ⇒ 深度平移 0.5m 而無訊號（KL 指認之洞·對照最淺街廓
    #    R4 vs R1 僅差 0.0415m ⇒ 該洞為決勝差距之 12 倍）。
    #    新閘 `_BL_EQUIV_EPS_M=1e-4` ⇒ 0.5 ≫ 1e-4 ⇒ 落 ②。
    r5, e5 = _run(ns, blk, [FRONT,
                            ("BASELINE", (0.0, D), (W, D), "B1"),
                            ("BASELINE", (0.0, D + 0.5), (W, D + 0.5), "B2")])
    _hit5 = (e5 is not None and any(it.get("layer") == "BASELINE" for it in e5.items))
    ok &= _hit5
    out.append(f"  🆕 近平行·互垂距 0.5m（非共線）：期 **轉② raise**、不得被①吸收 ⇒ "
               f"{'✅ 已 raise' if _hit5 else '🔴 被①吸收（靜默選了·深度會平移 0.5m 而無訊號）'}")
    if _hit5:
        _it5 = [i for i in e5.items if i.get("layer") == "BASELINE"][0]
        out.append(f"      候選：{[(c.get('baseline_handle'), c.get('perp_m')) for c in _it5['candidates']]}"
                   f"（手算 B1=40.0／B2=40.5·max−min=0.5）")

    # ── 🆕 C-5 結案：**同一幾何、只換匯出精度 q** ⇒ 須由 ② 轉 ①（q 項吸收）─────────
    #   手算：B1 = (0,D)→(25,D)；B2 = (30,D+6e-4)→(60,D+6e-4)。FRONT 中點 M=(30,0)、n=(0,1)。
    #     perp(B1)=40.0、perp(B2)=40.0006 ⇒ **spread = 6e-4**。
    #     `L/ℓ` 取**各候選之最大**（最保守·碼即如此）：
    #       B2：最近點 (30,40.0006) ⇒ L=40.0006、ℓ=30 ⇒ 1.33335
    #       B1：最近點 (25,40)      ⇒ L=√(5²+40²)=√1625=40.31129、ℓ=25 ⇒ **1.612452 ← max**
    #     · q=1e-5（5dp）：k·q·(L/ℓ) = 4×1e-5×1.612452 = 6.450e-5 < _EPS_LEGAL(1e-4)
    #       ⇒ eps = 1e-4；spread 6e-4 > 1e-4 ⇒ **落 ②**。
    #     · q=1e-3（3dp·CAD 常見匯出）：4×1e-3×1.612452 = 6.450e-3 → **上限截為 5e-3**
    #       ⇒ eps = 5e-3；spread 6e-4 ≤ 5e-3 ⇒ **落 ①**。
    #   ⇒ 證「換匯出精度不會使同一幾何誤落②」，且門檻確由 q 驅動、非寫死。
    _DZ = 6e-4
    _lines_q = [FRONT,
                ("BASELINE", (0.0, D), (25.0, D), "B1"),
                ("BASELINE", (30.0, D + _DZ), (W, D + _DZ), "B2")]
    r6a, e6a = _run(ns, blk, _lines_q, dxf_bytes=_synth_dxf_bytes(5))
    _hit6a = (e6a is not None)
    r6b, e6b = _run(ns, blk, _lines_q, dxf_bytes=_synth_dxf_bytes(3))
    _m6b = (((r6b or {}).get("baselines") or {}).get("R9") or {}).get("_match") or {}
    _hit6b = (e6b is None and _m6b.get("equivalent_n") == 2
              and abs(float(_m6b.get("q_detected") or 0) - 1e-3) < 1e-12)
    ok &= (_hit6a and _hit6b)
    out.append(f"  🆕 同幾何(spread 6e-4)·q=1e-5(5dp)：期 **落②** ⇒ "
               f"{'✅ 已 raise' if _hit6a else '🔴 未 raise'}")
    out.append(f"  🆕 同幾何(spread 6e-4)·q=1e-3(3dp)：期 **落①**（q 項吸收）⇒ "
               f"{'✅' if _hit6b else '🔴'}"
               f"　eq_n={_m6b.get('equivalent_n')}　q={_m6b.get('q_detected')}"
               f"　L/l={_m6b.get('L_over_l')}(手算 1.612452)　eps={_m6b.get('eps_used')}(手算 5e-3)")

    # ── 反例自證：把分支②之 B2 改成與 B1 共線 ⇒ 應由 ② 轉 ①（不再 raise）──────────
    r4, e4 = _run(ns, blk, [FRONT,
                            ("BASELINE", (0.0, D), (25.0, D), "B1"),
                            ("BASELINE", (30.0, D), (W, D), "B2")])
    _bite = (e4 is None)
    ok &= _bite
    out.append(f"  反例自證（②之兩線改共線 ⇒ 應轉①·不再 raise）：{'✅' if _bite else '🔴'}")

    # ── golden：UC9898 之 R1（BL#1／BL#3 共線·實證方位差 0.0005°、互垂距 0.0000）──
    try:
        snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        _mR1 = ((cad.get("baselines") or {}).get("R1") or {}).get("_match") or {}
        _gn = _mR1.get("equivalent_n")
        _sp = float(_mR1.get("perp_spread_m") or 0.0)
        _epsg = float(_mR1.get("eps_used") or 0.0)
        _hitg = (_gn == 2 and _sp <= _epsg)   # 單邊斷言：只比不變式 spread ≤ eps_used
        ok &= _hitg
        out.append(f"  golden UC9898·R1：equivalent_n={_gn}(期 2)　"
                   f"perp_spread={_sp:.3e} ≤ eps_used={_epsg:.3e}　"
                   f"垂距={_mR1.get('perp_mid_m')}　{'✅' if _hitg else '🔴'}")
        # golden R4：**單邊斷言**（KL 令·C-5 結案 (3)）——只斷言真正的**不變式**：
        #   `spread ≤ eps_used` ∧ `equivalent_n == 2`。
        #   ⛔ **禁**加下界 `1e-6 < spread`：那會把「CAD 存在雜訊」釘成**必要條件**
        #      ⇒ 日後圖資畫得更精準／換乾淨匯出鏈使離散下降時，**夾具會因輸入變好而轉紅**。
        #   「門檻不得取 1e-6」之教訓寫在註解與正典即可，**不得寫成對圖資品質之執行期斷言**。
        _mR4 = ((cad.get("baselines") or {}).get("R4") or {}).get("_match") or {}
        _sp4 = float(_mR4.get("perp_spread_m") or 0.0)
        _eps4 = float(_mR4.get("eps_used") or 0.0)
        _hit4 = (_mR4.get("equivalent_n") == 2 and _sp4 <= _eps4)
        ok &= _hit4
        out.append(f"  golden UC9898·R4：equivalent_n={_mR4.get('equivalent_n')}(期 2)　"
                   f"perp_spread={_sp4:.3e} ≤ eps_used={_eps4:.3e}　{'✅' if _hit4 else '🔴'}")
        out.append(f"      （資訊性錨·**不參與判紅**：本次觀測 spread={_sp4:.3e}、"
                   f"q={_mR4.get('q_detected')}、L/ℓ={_mR4.get('L_over_l')}；"
                   f"史載 5.795e-06 曾證「門檻不得取 1e-6」）")
        _n6 = len(cad.get("baselines") or {})
        ok &= (_n6 == 6)
        out.append(f"  golden UC9898：配到 BASELINE 之街廓數={_n6}(期 6)　{'✅' if _n6 == 6 else '🔴'}")
    except Exception as _e:
        ok = False
        out.append(f"  golden UC9898：🔴 例外 {_e}")

    print("=" * 100)
    print("【C-5 夾具】BASELINE 候選三分支（共線等價／歧義 raise／勝差足夠）")
    print("=" * 100)
    for ln in out:
        print(ln)
    print("-" * 100)
    print(f"RESULT: {'PASS' if ok else 'FAIL'}")
    print("=" * 100)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
