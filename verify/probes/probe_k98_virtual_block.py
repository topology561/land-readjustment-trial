r"""K-9-8 虛擬還原塊 — **只量不判**（K-6-A2 段四(a)）。

## 定位

段四三段式：**(a) 只量不判（本檔）→ (b) 攤給 KL（🛑 停機）→ (c) 上閘/切換**。
本檔**不接生產**：`k98_virtual_measure_block` 之生產呼叫點為 **0**
（`grep -rn "k98_virtual_measure_block" --include="*.py" .` 僅命中定義與本檔）。

## 量什麼

對**街角第 1 宗**（`corner_side_pts` ＝ **SIDE_LINE**·K-9-8 (3) 第一款）比較三代：

| 代 | 量測多邊形 | 深度起算線 |
|---|---|---|
| 二代（**現行生產**） | `cut_coords`（**截角後**實際宗地） | FRONT_LINE |
| 三代（**K-9-8**） | **虛擬還原塊**（伸出街廓外·含被截角切掉之部分） | **`PQ`**（過 `P_block` 平行 FRONT） |

⇒ 對照 **GB-18** 已載之量級（截角後 `0m`）：
`R1 右 0.7855 → 4.1725`／`R5 左 0.6706 → 3.8531`／`R6 右 1.3999 → 4.8108`。

## `L_in` 與 `corner_side` 之取法（⚠️ 不臆造）

- `L_in` ＝ 該宗多邊形中**平行 `alloc_dir`** 之二邊裡、**較靠街廓內側**者
  （以「沿 `d̂` 之座標距街角較遠」定之）——由**輸出幾何**反推，非重跑受測者之算式。
- `corner_side_pts` ＝ **SIDE_LINE 實體**（K-9-8 (3)：街角第 1 宗止於 SIDE_LINE）。
  ⛔ **本檔只做街角第 1 宗**——第 2 宗以後須止於「前一宗之 ALLOC_LINE」、末端塊止於
  BLOCK 邊界（K-9-8 (3) 明令 **不得一律延伸至 SIDE_LINE**），該二類留待後續批次。

**rc 恆 0**（只量不判）。輸出 `verify/out/probe_k98_virtual_block.log`。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import math                                                          # noqa: E402
from app_harvest import harvest                                      # noqa: E402
import run_verification as rv                                        # noqa: E402
from selection_pipeline import run_corner_pk                         # noqa: E402
from stepg_pipeline import run_step_g                                # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_k98_virtual_block.log")


def _alloc_edges(coords, au):
    """自宗地多邊形取**平行 alloc_dir** 之邊（回 [(p,q,長度)]）。"""
    out = []
    cs = list(coords)
    if cs[0] != cs[-1]:
        cs = cs + [cs[0]]
    for p, q in zip(cs[:-1], cs[1:]):
        vx, vy = float(q[0]) - float(p[0]), float(q[1]) - float(p[1])
        n = math.hypot(vx, vy)
        if n < 1e-9:
            continue
        if abs(abs((vx / n) * au[0] + (vy / n) * au[1]) - 1.0) < 1e-6:
            out.append(((float(p[0]), float(p[1])), (float(q[0]), float(q[1])), n))
    return out


REF_LOG = os.path.join(VERIFY, "out", "probe_ruling_K9_corner_width_V6_1.log")
# 🔴 `P` 之對照錨須用 **V6**（＝生產圖）那支，非 `_V6_1`：
#    內縮量與落點**因圖而異**（GB-19 已載：V6_1 為 12 格全退化，V6 為 10 退化／2 截角邊）。
REF_LOG_P = os.path.join(VERIFY, "out", "probe_ruling_K9_corner_width.log")


def _load_ref_p():
    """讀 `probe_ruling_K9_corner_width.log`【K-9-8-A/B】之 `內縮量(m)`／`P 落點` 欄（**V6**）。

    🔒 同為倉內既有錨，⛔ 不由本檔重算。錨側之量為**有號** `-t_P`，
    本檔之 `inset_from_front` 為**絕對值** ⇒ 只比**量值**、不比號。
    """
    if not os.path.exists(REF_LOG_P):
        return None, f"缺對照檔 {os.path.relpath(REF_LOG_P, REPO)}"
    with open(REF_LOG_P, encoding="utf-8") as f:
        lines = f.read().splitlines()
    try:
        i0 = next(i for i, s in enumerate(lines) if "【K-9-8-A/B】" in s)
    except StopIteration:
        return None, "對照檔內無【K-9-8-A/B】段"
    ref = {}
    for s in lines[i0 + 1:]:
        if "【" in s:
            break
        t = s.split()
        if len(t) < 6 or t[0] not in ("0m", "3.5m") or "/" not in t[1]:
            continue
        try:
            _in = float(t[3])
        except ValueError:
            continue
        ref[(t[0], t[1])] = {"inset": _in, "spot": "截角邊" if "截角邊" in s else "FRONT 重疊段"}
    return ref, f"{len(ref)} 列 ← {os.path.relpath(REF_LOG_P, REPO)}:{i0 + 1}"


def _load_ref():
    """讀**倉內既有錨**：`probe_ruling_K9_corner_width_V6_1.log` 之【K-9-8-D】表。

    🔒 `fixture-provenance`：一代／二代／三代之對照值**一律取自此既有量測**，
    ⛔ **不由本檔現跑新碼回填**（那是套套邏輯）。本檔自算者**只有三代**，
    且拿它與此表之三代欄對拍——**二者異源**（該表由 `probe_ruling_K9_corner_width.py`
    之獨立實作 `_k98_virtual_block` 產出；本檔走 `app.py` 之 `k98_virtual_measure_block`）
    ⇒ 對得上即為**獨立復現**，非自我採信。

    ⚠️ 該表量於 **V6_1.dxf**，本檔跑 **V6.dxf**（生產）⇒ 容有 mm 級差異，
    故本檔**只列 Δ、不設閘**（只量不判·rc 恆 0）。
    """
    if not os.path.exists(REF_LOG):
        return None, f"缺對照檔 {os.path.relpath(REF_LOG, REPO)}"
    ref, cur = {}, None
    with open(REF_LOG, encoding="utf-8") as f:
        lines = f.read().splitlines()
    try:
        i0 = next(i for i, s in enumerate(lines) if "【K-9-8-D】" in s)
    except StopIteration:
        return None, "對照檔內無【K-9-8-D】段"
    # 🔴 只掃**本段**：遇下一個「【…】」節標即止。
    #    前版以 `lines[i0:i0+40]` 為窗 ⇒ 掃過頭吃到**鄰段**同前綴之列（`0m R1/left …`），
    #    且後到者**覆蓋**先到者 ⇒ 12 列中 9 列被鄰段之座標字串污染。
    for s in lines[i0 + 1:]:
        if "【" in s:
            break
        t = s.split()
        if len(t) < 8 or t[0] not in ("0m", "3.5m") or "/" not in t[1]:
            continue
        try:                                   # 五個讀數須皆為數 ⇒ 才是本段之列
            [float(x) for x in t[3:8]]
        except ValueError:
            continue
        cur = (t[0], t[1])
        ref[cur] = {"pid": t[2], "d2": t[3], "d3": t[4],
                    "w1": t[5], "w2": t[6], "w3": t[7]}
    return (ref, f"{len(ref)} 列 ← {os.path.relpath(REF_LOG, REPO)}:{i0 + 1}")


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 120)
    L.append("【K-9-8 虛擬還原塊】只量不判·未接生產（K-6-A2 段四(a)）")
    L.append("範圍：**街角第 1 宗**（K-9-8 (3) 第一款·止於 SIDE_LINE）")
    L.append("⛔ 第 2 宗以後／末端塊之止點另有規定，本檔不做（禁一律延伸至 SIDE_LINE）")
    L.append("=" * 120)

    ns, fake_st = harvest()
    for _s in ("k98_virtual_measure_block", "parcel_min_width_n14"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}

    rows = []
    for setback in (0.0, 3.5):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s2, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params,
            temp_parcels, build_parcels, setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build_parcels, winners, forced, setback)
        by_pid = {str(r.get("暫編地號")): r for r in sg["g_rows"]}
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            fl = fl_by.get(lbl) or {}
            if not (fl.get("p1") and fl.get("p2")):
                continue
            bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
            au = al_by.get(lbl)
            if not au:
                continue
            nrm = math.hypot(float(au[0]), float(au[1]))
            auh = (float(au[0]) / nrm, float(au[1]) / nrm)
            for side in ("left", "right"):
                if side not in (sd_by.get(lbl) or {}):
                    continue
                w = (winners or {}).get(lbl) or {}
                pid = w.get("p1_end" if side == "left" else "p2_end")
                rec = {"sb": setback, "lbl": lbl, "side": side, "pid": pid}
                if not pid:
                    rec["note"] = "無 winner（強制留設抵費地）"
                    rows.append(rec); continue
                row = by_pid.get(str(pid))
                cc = (row or {}).get("cut_coords") or []
                if len(cc) < 3:
                    rec["note"] = f"cut_coords 不足（{len(cc)} 點）"
                    rows.append(rec); continue
                sd = sd_by[lbl][side]
                # 二代：現行生產之量法（cut_coords ＋ FRONT 起算）
                F1, F2 = fl["p1"], fl["p2"]
                dxy = (float(F2[0]) - float(F1[0]), float(F2[1]) - float(F1[1]))
                dl = math.hypot(*dxy)
                # 🔒 一代／二代**不由本檔重算**——取倉內既有錨（見 `_load_ref` docstring）。
                #    前版曾以 `get_min_lot_size(...)['min_depth']`（附表 14.00）為帶深現算，
                #    那是**一代**（GB-13 所記之誤用）而非二代；重算第三套只會再生一個歧異源。
                # 三代：K-9-8 虛擬還原塊（**本檔唯一自算者**）
                # 🔴 街角第 1 宗由 FRONT／SIDE_LINE／ALLOC／BASELINE 圍成
                #    ⇒ **平行 ALLOC 之邊本就恰 1 條**（靠街角側是 SIDE_LINE，不平行 ALLOC）。
                #    前版要求 `>=2` ⇒ 16 格中 6 格誤判為「L_in 不可定」。改為 `>=1`。
                _edges = _alloc_edges(cc, auh)
                if len(_edges) < 1:
                    rec["note"] = "無平行 ALLOC 之邊 ⇒ L_in 不可定"
                    rows.append(rec); continue
                # 街角：前緣線 ∩ SIDE_LINE 之 d̂ 座標；L_in ＝ 距街角較遠者
                dh = (dxy[0] / dl, dxy[1] / dl)
                def _s_of(p):
                    return (p[0] - float(F1[0])) * dh[0] + (p[1] - float(F1[1])) * dh[1]
                _sx = _s_of((float(sd["p1"][0]), float(sd["p1"][1])))
                _edges.sort(key=lambda e: abs((_s_of(e[0]) + _s_of(e[1])) / 2.0 - _sx))
                _lin = _edges[-1]
                try:
                    k98 = ns["k98_virtual_measure_block"](
                        b.get("vertices"), [F1, F2], bp,
                        [_lin[0], _lin[1]], [sd["p1"], sd["p2"]],
                        _label=lbl, _pid=str(pid), _lot_kind="corner_first")
                    rec["w3"] = k98["min_width"]
                    rec["inset"] = k98["inset_from_front"]
                    rec["depth3"] = k98["depth_from_PQ"]
                    # 🔒 落點**取自建構器之量得值**，⛔ 禁手寫、⛔ 禁由他處結論引入。
                    rec["spot"] = ("FRONT 重疊段" if k98["on_front"] else "非 FRONT 重疊段")
                except RuntimeError as e:
                    rec["w3"] = None
                    rec["w3err"] = str(e).splitlines()[0][:70]
                rows.append(rec)

    ref, refnote = _load_ref()
    L.append("")
    L.append("【A】街角第 1 宗最小寬度：三代（K-9-8 虛擬塊）之**獨立復現**")
    L.append(f"  對照錨：{refnote}")
    L.append("  一代/二代/三代(錨) ← 倉內既有量測（**非本檔重算**）；三代(本次) ← app.py "
             "`k98_virtual_measure_block`")
    L.append("  ⚠️ 錨量於 V6_1.dxf、本次跑 V6.dxf（生產）⇒ 容 mm 級差異；**只列 Δ、不設閘**。")
    L.append("-" * 120)
    L.append(f"  {'情境':<6}{'街廓/側':<12}{'街角第1宗':<12}"
             f"{'一代(錨)':>10}{'二代(錨)':>10}{'三代(錨)':>10}"
             f"{'三代(本次)':>11}{'Δ vs錨':>10}{'P內縮(m)':>11}{'三代深':>10}")
    L.append("-" * 120)
    dmax = 0.0
    for r in rows:
        tag = f"{r['sb']:g}m"
        key = f"{r['lbl']}/{r['side']}"
        if r.get("note"):
            L.append(f"  {tag:<6}{key:<12}{'—':<12}  {r['note']}")
            continue
        R = (ref or {}).get((tag, key)) or {}
        w3 = r.get("w3")
        f3 = f"{w3:.4f}" if w3 is not None else "raise"
        dd = "—"
        if w3 is not None and R.get("w3"):
            try:
                _d = w3 - float(R["w3"]); dd = f"{_d:+.4f}"; dmax = max(dmax, abs(_d))
            except ValueError:
                pass
        L.append(f"  {tag:<6}{key:<12}{str(r['pid']):<12}"
                 f"{R.get('w1', '—'):>10}{R.get('w2', '—'):>10}{R.get('w3', '—'):>10}"
                 f"{f3:>11}{dd:>10}"
                 f"{(r.get('inset') if r.get('inset') is not None else float('nan')):>11.6f}"
                 f"{(r.get('depth3') if r.get('depth3') is not None else float('nan')):>10.4f}")
        if r.get("w3err"):
            L.append(f"        三代 raise：{r['w3err']}")
    L.append("-" * 120)
    L.append(f"  |Δ| 最大 ＝ {dmax:.4f} m（僅為讀數·非判準）")
    refp, refpnote = _load_ref_p()
    L.append("")
    L.append("【B】`P_block` 之內縮量與落點：對**生產圖 V6** 之既有錨")
    L.append(f"  對照錨：{refpnote}")
    L.append("  ⚠️ 錨側為**有號** `-t_P`、本檔為**絕對值** ⇒ 只比量值不比號。")
    L.append("-" * 120)
    L.append(f"  {'情境':<6}{'街廓/側':<12}{'內縮:錨':>12}{'內縮:本次':>12}{'Δ':>12}"
             f"   {'落點:錨':<16}{'落點:本次':<16}{'一致':<6}")
    L.append("-" * 120)
    imax, nbad = 0.0, 0
    for r in rows:
        tag = f"{r['sb']:g}m"
        key = f"{r['lbl']}/{r['side']}"
        if r.get("note") or r.get("inset") is None:
            continue
        R = (refp or {}).get((tag, key)) or {}
        a = abs(R["inset"]) if R.get("inset") is not None else None
        m = float(r["inset"])
        dd = f"{m - a:+.6f}" if a is not None else "—"
        if a is not None:
            imax = max(imax, abs(m - a))
        sp_ref = R.get("spot", "—")
        sp_now = r.get("spot", "—")
        # 錨之「截角邊」＝非 FRONT 重疊段 ⇒ 語意對映後比一致性
        ok = "—"
        if sp_ref != "—" and sp_now != "—":
            same = ((sp_ref == "FRONT 重疊段") == (sp_now == "FRONT 重疊段"))
            ok = "✓" if same else "✗"
            if not same:
                nbad += 1
        L.append(f"  {tag:<6}{key:<12}"
                 f"{(f'{a:.6f}' if a is not None else '—'):>12}{m:>12.6f}{dd:>12}"
                 f"   {sp_ref:<16}{sp_now:<16}{ok:<6}")
    L.append("-" * 120)
    L.append(f"  |Δ內縮| 最大 ＝ {imax:.6f} m；落點不一致 {nbad} 格")
    L.append("  · 落點欄**由建構器之 `on_front` 量得**（判準 `|inset| <= _EPS_TOUCH_FRONT`），")
    L.append("    ⛔ 非手寫、⛔ 非引用他處結論。`on_chamfer` 仍回 None（須截角三角形，本函式不臆造）。")
    L.append("")
    L.append("【C】註記")
    L.append("  · 本檔**只量不判**：不設門檻、不判合格/不合格、rc 恆 0。")
    L.append("  · 三代之量測多邊形**未與街廓取交集**（K-9-8 紅線一）；")
    L.append("    其面積**未進入任何面積帳**（紅線二·守恆不受擾）。")
    L.append("  · 寬度由 `k98_virtual_measure_block` **轉呼 `parcel_min_width_n14`** 量之——")
    L.append("    K-9-8 只換**被量的多邊形**與**深度起算線**，**不換量法**（⛔ 禁 fork 第二套寬度）。")
    L.append("  · 第 2 宗以後／末端塊之止點另有規定（K-9-8 (3)），**本檔不做**。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
