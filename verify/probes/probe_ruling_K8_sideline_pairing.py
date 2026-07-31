r"""W-G.5 K-8 前置 B — **SIDE_LINE ↔ 街廓／側別 配對之驗證**（比照段一：先量、不改碼）。

## ⚠️ 施工單前提之更正（**本檔第一個發現**）

K-8 段三 施工單 §前置B 稱 `app.py:1281-1283` 現行為
「**貪婪式 1:1 配對 ＋ 街角地校正**」、與失敗考古 #38 之 BASELINE 失效手法同族。

**實測：該敘述來自一段陳舊註解，機制早已換掉。**
`app.py:1281-1283` 是 **Phase 11 Hotfix** 時期之註解；其後 **C-6**（KL 裁 2026-07-26）
已把 SIDE_LINE 之街廓歸屬改為**結構判準**——
`_best_block()` ＝ `_line_block_overlap()`（共線＋投影重疊長）取最大者、
同分按塊名之**決定性排序**、勝差 ≤ `_BIND_MARGIN_M` 即入 `_ambig`（禁靜默選）。
側別則由**既鎖之 `FRONT_LINE p1=左／p2=右`** 端點距離導出，逾 `_TOL_SL` 亦入 `_ambig`。
⇒ 與 BASELINE 之 C-1~C-5 **同族**，不是貪婪法。

（`grep -n "def _best_block" app.py`／`grep -n "C-6：SIDE_LINE 同判準綁定" app.py`）

⇒ 施工單所列之「**登記泛化項：貪婪 1:1 須比照 C-1~C-5 改為逐街廓獨立解**」
**已由 C-6 完成**，無待辦。惟該陳舊註解**正是本次誤讀之來源**，本批一併改寫（見 app.py）。

## 🔴 量測必須用**倉內原語**

`_line_block_overlap(line_pts, block_poly, ang_tol_deg=2.0, perp_tol_m=1.0)`。
**自行重寫一個「共線重疊」並自訂容差會得到錯誤結論**——CC 初次以 `10×q`（µm 級）
自寫，得「`#6` 對所有街廓皆 0.0000」之假象，險些誤報停機條件 #1。
CAD 之 SIDE 線畫到**未截角尖角**，與 BLOCK 邊有公尺級的端部落差，
`perp_tol_m=1.0` 正是為此而設。

## 對照靶（claude.ai 獨立自 DXF 量出·CC 以倉內機制重現）

| 街廓 | SIDE_LINE 實體 | 重疊率 |
|---|---|---|
| R1 | `#5`／`#6` | 0.90／0.89 |
| R2 | `#0` | 0.92 |
| R3 | `#1` | 0.93 |
| R4 | `#3`／`#4` | 0.90／0.89 |
| R5 | `#2` | 0.92 |
| R6 | `#7` | 0.92 |

靶以 **2dp** 陳述 ⇒ 比對容差 `0.01`（＝所述精度之粒度，**非**由殘差回推之閘寬）。

## 斷言

1. SIDE_LINE 實體 **8 條**；可建築街廓之街角側合計 **8 個**。
2. **無任一實體被兩個以上可建築街廓認領**——判準用 **`_best_block` 自己的判準**：
   `勝差（首名 − 次名，公尺） > _BIND_MARGIN_M`，且 `diagnostics.binding_ambiguity`
   無 SIDE_LINE 條目（有歧義時 `parse_cad_precision_layers` 會 `raise CadBindingAmbiguity`，
   本探針走得到這裡本身即證明無歧義）。
   ⛔ **禁自創更嚴之判準**：CC 初版寫「重疊率 > 0 者恰一塊」，
   而 `#0/#2/#3/#4` 對鄰塊有**次毫米級**重疊（4dp 顯示為 0.0000）⇒ 假紅 4 筆。
   歸屬之正典是「重疊最大者 ＋ 勝差 > 1.0m」，不是「唯一非零」。
3. **每個街角側都取得到實體**；且 `cad['side_lines_by_side'][blk][side]['mid']`
   與該實體之中點**逐格相符**（1e-6）。
4. 重疊率與對照靶差 ≤ `0.01`。

**2 或 3 不成立 ⇒ 停機上呈**（施工單 §停機條件 1）。

## 【4】截角落差（供 K-8 §三 本體用）

重疊率一律 0.89–0.93、非 1.00。缺口 `(1−ratio) × 實體全長` 與該側**截角股長**同量級
⇒ 佐證 **SIDE_LINE 實體 ＝ 截角前側界；街廓多邊形邊界 ＝ 截角後側界**
（K-8 §三 §2「兩套側界勿混」之實證基礎）。

## 重跑
    python verify/probes/probe_ruling_K8_sideline_pairing.py    # rc=0 綠／1 紅

⚠️ **零注入·唯讀**。輸出 `verify/out/probe_ruling_K8_sideline_pairing.log`。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon                                # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

LOG = os.path.join(VERIFY, "out", "probe_ruling_K8_sideline_pairing.log")

# claude.ai 獨立量出之對照靶（實體編號＝DXF 讀取序）
PAIR_EXPECT = {"R1": {"left": 6, "right": 5}, "R2": {"left": 0}, "R3": {"right": 1},
               "R4": {"left": 4, "right": 3}, "R5": {"left": 2}, "R6": {"right": 7}}
RATIO_EXPECT = {0: 0.92, 1: 0.93, 2: 0.92, 3: 0.90, 4: 0.89, 5: 0.90, 6: 0.89, 7: 0.92}
RATIO_TOL = 0.01          # ＝靶所述之 2dp 粒度（非殘差回推）
N_ENTS_EXPECT = 8
N_CORNER_SIDES_EXPECT = 8


def _ents():
    """DXF 之 SIDE_LINE 實體（讀取序編號·聚合線不拆段——與 app 之 `_side_line_buffer` 同構）。"""
    import ezdxf
    doc = ezdxf.readfile(rv.V6DXF)
    out = []
    for e in doc.modelspace():
        if "SIDELINE" not in str(e.dxf.layer).upper().replace("_", ""):
            continue
        if e.dxftype() == "LINE":
            out.append(([(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)],
                        str(e.dxf.handle)))
        elif e.dxftype() in ("LWPOLYLINE", "POLYLINE"):
            out.append(([tuple(p[:2]) for p in e.get_points()], str(e.dxf.handle)))
    return out


def _plen(pts):
    return sum(((pts[i + 1][0] - pts[i][0]) ** 2 + (pts[i + 1][1] - pts[i][1]) ** 2) ** 0.5
               for i in range(len(pts) - 1))


def _pmid(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    L, bad = [], []
    snap = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fs = harvest()
    cb_by, cad = rv.build_pipeline(ns, fs, snap)
    ovl = ns["_line_block_overlap"]                 # 🔴 倉內原語·禁自寫
    fcb = ns["F3_CATEGORY_BURDEN"]
    slbs = cad.get("side_lines_by_side") or {}
    blds = [b for b in sorted(cb_by)
            if fcb.get(cb_by[b].get("category", ""), "") == "可建築土地"]
    polys = {b: Polygon([(v[0], v[1]) for v in cb_by[b]["vertices"]]) for b in blds}
    ents = _ents()

    L.append("=" * 112)
    L.append("【K-8 前置 B】SIDE_LINE↔街廓／側別 配對之**驗證**（既有 C-6·非新機制）")
    L.append("=" * 112)
    L.append(f"  可建築街廓 {blds}｜SIDE_LINE 實體 {len(ents)} 條（期 {N_ENTS_EXPECT}）")
    if len(ents) != N_ENTS_EXPECT:
        bad.append(f"實體數 {len(ents)} ≠ {N_ENTS_EXPECT}")
    for i, (pts, h) in enumerate(ents):
        m = _pmid(pts)
        L.append(f"    #{i} handle={h} len={_plen(pts):8.3f} mid=({m[0]:11.3f},{m[1]:11.3f})")

    # ── 【1】重疊率矩陣（倉內原語）────────────────────────────────────────────────
    L.append("")
    L.append("【1】重疊率 ＝ `_line_block_overlap`(公尺) ÷ 實體全長（ang 2.0°／perp 1.0m）")
    L.append("-" * 112)
    ratio = {}
    L.append("  塊   " + "".join(f"{'#' + str(i):>9}" for i in range(len(ents))))
    for b in blds:
        row = []
        for i, (pts, _h) in enumerate(ents):
            _L = _plen(pts)
            r = (float(ovl(pts, polys[b])) / _L) if _L > 0 else 0.0
            ratio[(b, i)] = r
            row.append(r)
        L.append(f"  {b:5}" + "".join(f"{x:9.4f}" for x in row))

    # ── 【2】歸屬唯一性：用 `_best_block` 自己的判準（勝差 > _BIND_MARGIN_M）─────────
    #   ⛔ 禁自創「重疊率 > 0 者恰一塊」——鄰塊有次毫米級重疊，該判準會給 4 筆假紅。
    L.append("")
    L.append("【2】歸屬唯一性（停機條件 1 之一）：勝差 ＞ `_BIND_MARGIN_M`（＝ C-6 之判準）")
    L.append("-" * 112)
    _MARGIN = 1.0        # app 內 `_BIND_MARGIN_M`（`grep -n "_BIND_MARGIN_M = " app.py`）
    _amb = ((cad.get("diagnostics") or {}).get("binding_ambiguity") or [])
    _amb_sl = [a for a in _amb if "SIDE_LINE" in str(a.get("layer", ""))]
    L.append(f"  `diagnostics.binding_ambiguity` 之 SIDE_LINE 條目：{len(_amb_sl)}（期 0）"
             f"  {'✅' if not _amb_sl else '🔴'}")
    if _amb_sl:
        bad.append(f"SIDE_LINE 綁定歧義 {len(_amb_sl)} 筆：{_amb_sl[:2]}")
    L.append(f"  {'實體':6}{'首名':>8}{'重疊m':>10}{'次名':>8}{'重疊m':>10}{'勝差m':>10}  判")
    for i in range(len(ents)):
        _pts = ents[i][0]
        _rk = sorted(((float(ovl(_pts, polys[b])), b) for b in blds), reverse=True)
        _top, _tb = _rk[0]
        _sec, _sb = (_rk[1] if len(_rk) > 1 else (0.0, "—"))
        _mg = _top - _sec
        ok_i = (_mg > _MARGIN)
        L.append(f"  #{i:<5}{_tb:>8}{_top:10.4f}{_sb:>8}{_sec:10.6f}{_mg:10.4f}"
                 f"  {'✅' if ok_i else '🔴'}")
        if not ok_i:
            bad.append(f"#{i} 勝差 {_mg:.4f}m ≤ {_MARGIN}（{_tb} vs {_sb}）⇒ 歸屬不決定")

    # ── 【3】街角側全覆蓋 ＋ app 輸出逐格對拍 ─────────────────────────────────────
    L.append("")
    L.append("【3】街角側全覆蓋 ＋ `cad['side_lines_by_side']` 對拍（停機條件 1 之二）")
    L.append("-" * 112)
    n_sides = 0
    for b in sorted(PAIR_EXPECT):
        for side, idx in sorted(PAIR_EXPECT[b].items()):
            n_sides += 1
            got = (slbs.get(b) or {}).get(side)
            if not got:
                bad.append(f"{b} {side} 取不到 SIDE_LINE 實體")
                L.append(f"  {b} {side:5}  🔴 缺件")
                continue
            em = _pmid(ents[idx][0])
            d = float(np.hypot(got["mid"][0] - em[0], got["mid"][1] - em[1]))
            _ok = d <= 1e-6
            L.append(f"  {b} {side:5} → 期 #{idx}（handle={ents[idx][1]}）"
                     f"｜mid 差 {d:.2e}m  {'✅' if _ok else '🔴'}")
            if not _ok:
                bad.append(f"{b} {side} 之 mid 與 #{idx} 差 {d:.3e}m")
    L.append(f"  ⇒ 街角側合計 {n_sides}（期 {N_CORNER_SIDES_EXPECT}）"
             f"  {'✅' if n_sides == N_CORNER_SIDES_EXPECT else '🔴'}")
    if n_sides != N_CORNER_SIDES_EXPECT:
        bad.append(f"街角側 {n_sides} ≠ {N_CORNER_SIDES_EXPECT}")

    # ── 【4】重疊率對靶 ＋ 截角落差 ──────────────────────────────────────────────
    L.append("")
    L.append("【4】重疊率對靶（容差 0.01＝靶之 2dp 粒度）＋ 截角落差")
    L.append("-" * 112)
    L.append(f"  {'實體':6}{'認領':6}{'長度':>10}{'重疊率':>10}{'靶':>8}{'Δ':>9}"
             f"{'缺口(m)':>10}  判")
    for i, (pts, _h) in enumerate(ents):
        owner = [b for b in blds if ratio[(b, i)] > 0]
        r = ratio[(owner[0], i)] if owner else 0.0
        tgt = RATIO_EXPECT[i]
        dv = r - tgt
        gap = (1.0 - r) * _plen(pts)
        _ok = abs(dv) <= RATIO_TOL
        L.append(f"  #{i:<5}{(owner[0] if owner else '—'):6}{_plen(pts):10.3f}"
                 f"{r:10.4f}{tgt:8.2f}{dv:+9.4f}{gap:10.3f}  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"#{i} 重疊率 {r:.4f} 與靶 {tgt} 差 {dv:+.4f} > {RATIO_TOL}")
    L.append("")
    L.append("  ⇒ 缺口皆為公尺級（非零）＝ SIDE_LINE 畫到**未截角尖角**、BLOCK 邊已截角。")
    L.append("     **SIDE_LINE 實體 ＝ 截角前側界；街廓多邊形邊界 ＝ 截角後側界**"
             "（K-8 §三 §2 兩套側界之實證基礎）。")

    L.append("")
    L.append("-" * 112)
    if bad:
        L.append(f"RESULT: FAIL（{len(bad)} 違例）")
        for x in bad[:20]:
            L.append("  " + x)
    else:
        L.append("RESULT: PASS（8 實體／8 街角側／無共用／app 輸出逐格相符／重疊率對靶）")
    L.append("=" * 112)
    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
