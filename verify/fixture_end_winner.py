# -*- coding: utf-8 -*-
"""§4 末端塊 gate **判別力**合成夾具（F-2·KL 裁 2026-07-25）。**左＋右雙側·0m/3.5m 雙 tag**。

## 存在理由（reviewer：`_cond1` 鑑別力 ≈ 0）

`wf_f4._reshape_block` 之末端 gate ＝ `_cond1 and (_unfront_area > 1e-3)`
（`grep -n "_end_gate = _cond1" verify/wf_f4.py`）。

* `_cond1 = not fo["{side}_has_side"]` ＝**直接讀旗標**、**by construction 近恆真**——
  對其斷言等於斷言「我剛才填進去的值等於我剛才填進去的值」，**咬不到任何實作**。
* 真正承載幾何語意者是 **`_unfront_area`**（該側「未臨正街半平面」∩block 之面積）。
  故本夾具之核心斷言為：**cond1 為真而 cond2 為假時，gate 必須不觸發**——
  此命題**唯有** `_unfront_area` 被真的計算並比較時才成立，`_cond1` 單獨無從產生。

另驗 **末端 winner 前後集合**：gate 開時 `wf_f4` 以「G ≥ area(R_end)」**往後找**
（`grep -n "往後找" verify/wf_f4.py`），gate 關時取首個 `_qual` 宗 ⇒ **標的宗換人**。

## 期望值出處（`fixture-provenance`·**全部獨立手算**·禁跑一次回填）

`cad_alloc=+y ⇒ s≡x`；`F=4 / W=40 / H=10 / MW=3.5`（同 `fixture_end_fallback` 之合成幾何）。

| 量 | 手算 | 依據 |
|---|---|---|
| `frag` 面積 | `F×H` ＝ **40.0** | 未臨正街段 4m×10m |
| 末端帶面積 | `MW×H` ＝ **35.0** | 過 end_pt·∥cad_alloc·⊥垂距 MW |
| `area(R_end)` | **75.0** | `frag ∪ 末端帶`（兩者不相交） |
| cond2 之 `_unfront_area`（A/B 案） | `F×H` ＝ **40.0** | `block∩{s<0}`（左）／`block∩{s>s(p2)}`（右） |
| cond2 之 `_unfront_area`（C 案） | **0.0** | block 起於 x=0 ⇒ 半平面空（frag 落 block 外） |

**分歧點之手算**：候選 G ＝ `[60, 90, 90]`。`60 < 75 ≤ 90` ⇒
gate 開 → 首宗**被跳過**、標的換第 2 宗；gate 關 → 標的即首宗。**二者結果必不同**。

> 📌 **結構恆等式（手算·非實測回填）**：本合成幾何下「gate 門檻」與「整形後寬閘」**同值**——
> 標的吞楔形後 `S_new` 滿足 `strip(0,S_new) + frag = G`，而 `strip(0,mw) = 末端帶`，
> 故 `S_new ≥ mw ⟺ G ≥ frag + 末端帶 ＝ area(R_end)`。
> ⇒ gate 關而 `G < area(R_end)` 時，下游 `整形後寬 <mw` 必 raise。
> **gate 之作用即把該下游 raise 前移為「往後找」**。本夾具據此對**結果種類**斷言（見 `_OUTCOME`）。

## 重跑
    python verify/fixture_end_winner.py
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(os.path.join(REPO, "verify"))

from shapely.geometry import Polygon                      # noqa: E402
from app_harvest import harvest                           # noqa: E402
import wf_f4                                              # noqa: E402

ns, _st = harvest()
for _n in ("_end_region_R", "_end_band", "_strip_s_range", "_block_strip"):
    assert _n in ns, f"harvest 未取得 {_n}"

F, W, H, MW = 4.0, 40.0, 10.0, 3.5
BLK = "TEST"
AREA_REND = (F + MW) * H            # 75.0（手算）
G_SPLIT = [60.0, 90.0, 90.0]        # 60 < 75 ≤ 90 ⇒ gate 開必跳首宗
G_NOSPLIT = [90.0, 90.0, 90.0]      # 首宗即 ≥ 75 ⇒ gate 開/關同標的

SNAP = {"blocks": {BLK: {"街廓分配深度_m": H, "正面": {"路寬_m": 12.0}}}}
CAD = {"front_lines": {BLK: {"p1": [0.0, 0.0], "p2": [float(W), 0.0]}},
       "alloc_dir_by_block": {BLK: [0.0, 1.0]}}
MINA = {BLK: 30.0}


def _build(side, *, overhang, gvals):
    """回傳 (block, frag, forced_base, rowsE, frag_row)。
    `overhang=True` ⇒ block 含未臨正街段（cond2 真）；False ⇒ block 起於正街端、frag 落 block 外（cond2 假）。"""
    if side == "left":
        block = (Polygon([(-F, 0), (W, 0), (W, H), (-F, H)]) if overhang
                 else Polygon([(0, 0), (W, 0), (W, H), (0, H)]))
        frag = Polygon([(-F, 0), (0, 0), (0, H), (-F, H)])       # s<0（p1 外）
        frag_s = 0.2
        xs, cums = [], []
        _x = 0.0
        for g in gvals:                                          # 首宗貼 frag（楔形須與標的相鄰）
            xs.append(_x)
            cums.append(_x)
            _x += g / H
    else:
        block = (Polygon([(0, 0), (W + F, 0), (W + F, H), (0, H)]) if overhang
                 else Polygon([(0, 0), (W, 0), (W, H), (0, H)]))
        frag = Polygon([(W, 0), (W + F, 0), (W + F, H), (W, H)])  # s>s(p2)（p2 外）
        frag_s = 0.99
        xs, cums = [], []
        _hi = W                                                  # 首宗貼 frag 之內側
        _corner = (W + F) if overhang else W
        for g in gvals:
            _w = g / H
            xs.append(_hi - _w)
            cums.append(_corner - _hi)
            _hi -= _w
    rowsE = []
    for i, (g, x) in enumerate(zip(gvals, xs)):
        wdt = g / H                                              # 乾淨：G=寬×H（寬 ≥ MW）
        poly_i = Polygon([(x, 0), (x + wdt, 0), (x + wdt, H), (x, H)])
        rowsE.append({"所屬街廓": BLK, "推進側別": side, "暫編地號": f"{BLK}-{i+1}",
                      "S(m)": wdt, "G(㎡)": g, "宗地寬度(m)": wdt, "累積S(m)": cums[i],
                      "幾何面積(㎡)": g, "畸零地旗標": "",
                      "cut_coords": list(poly_i.exterior.coords)})
    frag_row = {"街廓": BLK, "暫編": f"{BLK}-抵費地-2", "poly": frag, "面積": round(frag.area, 2),
                "s": frag_s, "三分類": "碎片", "cut_coords": list(frag.exterior.coords)}
    return block, frag, rowsE, frag_row


def _outcome(side, *, has_side, overhang, gvals, tag):
    """跑 `_reshape_block`，把結果正規化為可比 token（**不比字面訊息全文**·只比種類）。
    回 ("ok", target_id) ／ ("raise", kind)。kind∈{不相鄰, 整形寬, 其他:<類名>}。"""
    block, frag, rowsE, frag_row = _build(side, overhang=overhang, gvals=gvals)
    cb_by = {BLK: {"vertices": list(block.exterior.coords)[:-1], "category": "住宅區"}}
    forced = {f"{side}_has_side": has_side,
              ("right" if side == "left" else "left") + "_has_side": True,
              "left_forced_offset": False, "right_forced_offset": False,
              "left_corner_min_area": 0.0, "right_corner_min_area": 0.0}
    try:
        _rows, _polys, tgt = wf_f4._reshape_block(ns, SNAP, cb_by, CAD, {BLK: forced},
                                                  rowsE, BLK, frag_row, tag, MINA)
    except Exception as e:
        _m = str(e)
        kind = ("不相鄰" if "不相鄰" in _m else
                ("整形寬" if "整形後寬" in _m else f"其他:{type(e).__name__}"))
        return ("raise", kind)
    return ("ok", tgt)


def _unfront_of(side, *, overhang):
    """獨立重算 cond2 之 `_unfront_area`（與 `wf_f4` 同式·供對手算值）。"""
    import numpy as np
    block, *_ = _build(side, overhang=overhang, gvals=G_SPLIT)
    d_hat = np.array([1.0, 0.0])
    p1 = np.array([0.0, 0.0])
    alloc = ns["alloc_normal_axis"]([0.0, 1.0])
    dom = ns["_strip_s_range"](block, d_hat, p1, alloc)
    s0, s1 = (float(dom[0]), float(dom[1])) if dom else (0.0, 0.0)
    if side == "left":
        if s0 >= -1e-6:
            return 0.0
        return float(ns["_block_strip"](block, d_hat, p1 + s0 * d_hat, -s0,
                                        allocation_dir=alloc)[1] or 0.0)
    s_p2 = W
    if s1 <= s_p2 + 1e-6:
        return 0.0
    return float(ns["_block_strip"](block, d_hat, p1 + s_p2 * d_hat, s1 - s_p2,
                                    allocation_dir=alloc)[1] or 0.0)


def run(*, patch_rend=False):
    """回傳 (ok, lines)。`patch_rend=True` ＝**咬合反例**：把 `_end_region_R` 之面積壓成 0，
    使 `G ≥ area(R_end)` 恆真、gate 失去判別力 ⇒ 本夾具之核心斷言**必須轉紅**。"""
    ok, out = True, []
    _orig = ns["_end_region_R"]
    if patch_rend:
        def _fake(*a, **k):
            _b, _p, _ = _orig(*a, **k)
            return _b, _p, 0.0
        ns["_end_region_R"] = _fake
    try:
        for tag in ("0m", "3.5m"):                     # tag-agnostic：兩 tag 同一套判準
            for side in ("left", "right"):
                # 驗0：cond2 之 `_unfront_area` 對獨立手算
                u_on, u_off = _unfront_of(side, overhang=True), _unfront_of(side, overhang=False)
                d0 = max(abs(u_on - F * H), abs(u_off - 0.0))
                out.append(f"[{tag}·{side}] 驗0 _unfront_area：有伸出 {u_on:.4f}(手算 {F*H:.4f})"
                           f"／無伸出 {u_off:.4f}(手算 0.0000)  {'✅' if d0 < 1e-6 else '🔴'}")
                ok &= d0 < 1e-6

                # A＝cond1真+cond2真（gate 開）／B＝cond1假（gate 關）／C＝cond1真+cond2假（gate 關）
                A = _outcome(side, has_side=False, overhang=True, gvals=G_SPLIT, tag=tag)
                B = _outcome(side, has_side=True, overhang=True, gvals=G_SPLIT, tag=tag)
                C = _outcome(side, has_side=False, overhang=False, gvals=G_SPLIT, tag=tag)
                B2 = _outcome(side, has_side=True, overhang=False, gvals=G_SPLIT, tag=tag)

                # 斷言1（**核心·`_cond1` 無從產生**）：cond1 真而 cond2 假 ⇒ 同 gate 關
                ok1 = (C == B2)
                out.append(f"[{tag}·{side}] 驗1 cond1真+cond2假 ⇒ 同 gate 關："
                           f"C={C} vs B2={B2}  {'✅' if ok1 else '🔴'}")
                ok &= ok1
                # 斷言2：cond2 真 ⇒ 末端 winner 前後集合**改變**（gate 咬得到）
                ok2 = (A != B)
                out.append(f"[{tag}·{side}] 驗2 cond2真 ⇒ 標的換人：A={A} vs B={B}"
                           f"  {'✅' if ok2 else '🔴'}")
                ok &= ok2
                # 斷言3：首宗即 G ≥ area(R_end) ⇒ gate 開/關同標的（不需要時不亂動）
                A3 = _outcome(side, has_side=False, overhang=True, gvals=G_NOSPLIT, tag=tag)
                B3 = _outcome(side, has_side=True, overhang=True, gvals=G_NOSPLIT, tag=tag)
                ok3 = (A3 == B3 == ("ok", f"{BLK}-1"))
                out.append(f"[{tag}·{side}] 驗3 首宗達 area(R_end) ⇒ gate 開關同標的："
                           f"A3={A3} B3={B3}  {'✅' if ok3 else '🔴'}")
                ok &= ok3
    finally:
        ns["_end_region_R"] = _orig
    return ok, out


def main():
    print("=" * 84)
    print(f"§4 末端 gate 判別力夾具（F-2）｜area(R_end) 手算 ＝ {AREA_REND}")
    print("=" * 84)
    ok, lines = run()
    for _l in lines:
        print(_l)
    print("-" * 84)
    # ── 咬合實證（`no-silent-fallback`／交接文 §5.2「凡新立閘，必造反例證其會紅」）──
    ko, klines = run(patch_rend=True)
    print("【咬合反例】把 `_end_region_R` 面積壓成 0（模擬 gate 失去判別力）⇒ 本夾具應轉紅：")
    for _l in klines:
        if "🔴" in _l:
            print("   " + _l)
    print(f"   反例結果：{'🔴 FAIL（正確——閘咬得到）' if not ko else '✅ PASS（**錯誤**：閘咬不到，本夾具無效）'}")
    bite = (not ko)
    print("=" * 84)
    _all = ok and bite
    print(f"RESULT: {'PASS' if _all else 'FAIL'}"
          + ("　⇒ gate 之判別力來自 `_unfront_area`（非 `_cond1`）且末端 winner 集合確實改變。"
             if _all else "　⇒ 停機上呈"))
    print("=" * 84)
    return 0 if _all else 1


if __name__ == "__main__":
    sys.exit(main())
