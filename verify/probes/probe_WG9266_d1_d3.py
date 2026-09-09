# -*- coding: utf-8 -*-
"""W-G.9-266 工項七：`d-3`（`K-9-12` 充分側）＋ `d-1`（`K-9-9 一` ∥ALLOCLINE）。唯讀探針。

🔒 唯讀：讀 harness 落檔 ＋ 生產解析器之輸出（`build_param_table`／`cad`）。
   ⛔ 動 `app.py` 與 `verify/` 生產路徑一字。

【`W × D` 之來源（單 §八 明令·⛔ 硬編 `3.5`／`14`·⛔ 一律套 `10.0`）】
  `W`／`D` ＝ `get_min_lot_size(category, front_road_width_m)` 之 `min_width`／`min_depth`；
  `category` ＝ `cad`／`cb` 之 `b['category']`（**逐街廓**）；
  `front_road_width_m` ＝ `build_param_table` 之 `正面路寬(m)` 欄（**逐街廓實測**·生產碼所算）。

【`d-1` 之自我驗證閘】＝ 碼面對「哪一條界 ∥ 哪一條線」之**明文斷言**（逐字出艙其內容錨）；
  **必紅組** ＝ 街角第 `0` 宗（`第1筆街角 == 是`）——其遠側界依 `K-9-9 五`／`K-9-5-4 ②` 須 **∥SIDELINE**
  而**非** ∥ALLOCLINE ⇒ 該組於 ∥ALLOCLINE 之檢下**必紅**；
  **必綠組** ＝ 第 `1` 宗以後。二者若同色 ⇒ 閘失能、⛔ 得下結論。
"""
import ast
import csv
import io
import math
import os
import sys

from shapely.geometry import Polygon

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out")
SCEN = [("0m", "got_G值_退縮0m_partial.csv", 0.0), ("3.5m", "got_G值_退縮3.5m_partial.csv", 3.5)]
QK = 1e-6


def poly(c):
    p = Polygon(c)
    return p if p.is_valid else p.buffer(0)


def load(fn):
    with io.open(os.path.join(OUT, fn), "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def parse(s):
    if not s or not s.strip():
        return None
    try:
        v = ast.literal_eval(s)
    except Exception:
        return None
    return [(float(a), float(b)) for a, b in v] if v and len(v) >= 3 else None


def rect_fits_no_rotation(coords, W, D, dh):
    """不旋轉之矩形容納（`K-9-12 三`：`W` 沿 FRONTLINE、`D` 沿其法向）。
    判準 ＝ 於 (s,t) 框下，該多邊形能否容納一 `W × D` 之軸對齊矩形（掃描 s 之離散步長）。
    🔒 本式係**必要條件之加強**：以 s 方向掃描 ＋ 每一 s 窗內取 t 之最小上界／最大下界。"""
    ux, uy = dh
    nx, ny = -uy, ux
    pts = [((x * ux + y * uy), (x * nx + y * ny)) for (x, y) in coords]
    p = Polygon(pts)
    if not p.is_valid:
        p = p.buffer(0)
    s0 = min(q[0] for q in pts); s1 = max(q[0] for q in pts)
    if s1 - s0 < W:
        return False, "s 幅 %.4f < W %.4f" % (s1 - s0, W)
    N = 200
    for i in range(N + 1):
        a = s0 + (s1 - s0 - W) * i / N
        band = Polygon([(a, -1e9), (a + W, -1e9), (a + W, 1e9), (a, 1e9)])
        inter = p.intersection(band)
        if inter.is_empty:
            continue
        # 於該帶內，矩形須整條落在多邊形內 ⇒ 取帶內之「t 之共同區間」
        lo, hi = -1e18, 1e18
        ok = True
        for j in range(21):
            sx = a + W * j / 20.0
            line = Polygon([(sx - 1e-9, -1e9), (sx + 1e-9, -1e9), (sx + 1e-9, 1e9), (sx - 1e-9, 1e9)])
            seg = p.intersection(line)
            if seg.is_empty:
                ok = False
                break
            ymin, ymax = seg.bounds[1], seg.bounds[3]
            # 需為單一連通段方可用 bounds
            if hasattr(seg, "geoms") and len(getattr(seg, "geoms", [])) > 1:
                best = max(seg.geoms, key=lambda g: g.bounds[3] - g.bounds[1])
                ymin, ymax = best.bounds[1], best.bounds[3]
            lo = max(lo, ymin); hi = min(hi, ymax)
            if hi - lo < D:
                ok = False
                break
        if ok and hi - lo >= D:
            return True, "s ＝ %.4f 起之窗內 t 幅 %.4f ≥ D %.4f" % (a, hi - lo, D)
    return False, "全 %d 個 s 窗皆不可容納" % (N + 1)


def main():
    sys.path.insert(0, os.path.join(REPO, "verify"))
    import run_verification as rv
    from app_harvest import harvest
    ns, fake = harvest()
    snap = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake, snap)
    gmls = ns["get_min_lot_size"]

    print("=" * 116)
    print("【W-G.9-266 工項七】`d-3`（`K-9-12` 充分側）＋ `d-1`（`K-9-9 一` ∥ALLOCLINE）")
    print("=" * 116)

    # ── W×D 之逐街廓來源（⛔ 硬編·⛔ 一律套 10.0）
    print()
    print("── `W × D` 之逐街廓來源（生產函式 ＋ 生產碼所算之逐街廓路寬·⛔ 硬編）──")
    WD = {}
    for tag, fn, sb in SCEN:
        params = rv.build_param_table(ns, fake, cb_by, cad, snap, sb)
        rows = params if isinstance(params, list) else params.get("rows", params)
        for r in rows:
            lbl = str(r.get("街廓", "")).strip()
            if not lbl:
                continue
            fw = float(r.get("正面路寬(m)", 0) or 0)
            cat = cb_by[lbl]["category"] if lbl in cb_by else str(r.get("分類", ""))
            g = gmls(cat, fw)
            WD[(tag, lbl)] = (float(g["min_width"]), float(g["min_depth"]), cat, fw,
                              float(r.get("法定最小寬(m)", 0) or 0), float(r.get("法定最小深(m)", 0) or 0))
    for k in sorted(WD):
        W, D, cat, fw, lw, ld = WD[k]
        agree = (abs(W - lw) < 1e-9 and abs(D - ld) < 1e-9)
        print("   %-5s %-4s 分類 %-4s｜正面路寬 %5.2f m ⇒ get_min_lot_size ⇒ W %.2f × D %.2f ＝ %.2f ㎡"
              % (k[0], k[1], cat, fw, W, D, W * D))
        print("        [自我驗證閘] vs `build_param_table` 之 `法定最小寬/深` 欄（%.2f／%.2f）⇒ %s"
              % (lw, ld, "✅ 相符" if agree else "🔴 不符"))
    print("   [判別力] `get_min_lot_size('住宅區', 5.0)` ⇒ %s ⇒ 該查表⛔ 為常數" % gmls("住宅區", 5.0))
    print("   🛑 逐街廓路寬**實測**（⛔ 一律套 `10.0`）——上表之 `正面路寬(m)` 逐街廓相異值 ＝ %s"
          % sorted({WD[k][3] for k in WD}))

    # ── d-3
    print()
    print("=" * 116)
    print("`d-3`　`K-9-12` 之**充分側**：`G ≥ W×D` 之宗能否實際容納矩形")
    print("=" * 116)
    FL = cad.get("front_lines") or {}
    tot = fit_nr = nofit_nr = 0
    harness_ok = harness_bad = harness_na = 0
    rot0 = 0
    mism = []
    for tag, fn, sb in SCEN:
        rows = load(fn)
        for r in rows:
            side = (r.get("推進側別") or "").strip()
            if side == "抵費地":
                continue
            lbl = (r.get("所屬街廓") or "").strip()
            cc = parse(r.get("cut_coords"))
            if cc is None or lbl not in FL:
                continue
            W, D, _c, _f, _lw, _ld = WD[(tag, lbl)]
            G = float(r.get("G(㎡)") or 0)
            if G < W * D:
                continue
            tot += 1
            p1, p2 = FL[lbl]["p1"], FL[lbl]["p2"]
            L = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
            dh = ((p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L)
            ok, why = rect_fits_no_rotation(cc, W, D, dh)
            if ok:
                fit_nr += 1
            else:
                nofit_nr += 1
            hv = (r.get("驗_A幾何") or "").strip()
            ang = (r.get("驗_A_命中角") or "").strip()
            if hv == "合格":
                harness_ok += 1
                if ang == "0.0":
                    rot0 += 1
            elif hv == "不合格":
                harness_bad += 1
            else:
                harness_na += 1
            if (hv == "合格") != ok and ang == "0.0":
                mism.append((tag, lbl, (r.get("暫編地號") or "").strip(), hv, ang, ok, why))
    print("   受詞（`G ≥ W×D` 之分配宗·二情境合計）＝ **%d 宗**" % tot)
    print("   本探針之**不旋轉**判：可容納 %d 宗／不可容納 %d 宗" % (fit_nr, nofit_nr))
    print("   落檔 `驗_A幾何`（harness 之**可旋轉**判·`K-9-12-c` KL 自陳更正）：合格 %d／不合格 %d／不適用 %d"
          % (harness_ok, harness_bad, harness_na))
    print("   其中 `驗_A_命中角 == 0.0`（＝ **不旋轉**即可容納）＝ **%d 宗**" % rot0)
    print("   🔒 二判之受詞相異：本探針測 `K-9-12 三`（**⛔ 旋轉**）；落檔測 `K-9-12-c`（**可旋轉**）")
    print("   [對拍·命中角 0.0 之子集] 本探針與落檔相異 ＝ %d 宗" % len(mism))
    for m in mism[:5]:
        print("        %s" % (m,))
    # 否證對照（單 §八 明令）
    print()
    print("   ── 否證對照（人造四至·單 §八 明令）──")
    dh0 = (1.0, 0.0)
    for name, w, h, must in (("必紅 人造 3.0 × 13.0 之四至", 3.0, 13.0, False),
                             ("必綠 人造 10 × 20 之四至", 10.0, 20.0, True)):
        rect = [(0.0, 0.0), (w, 0.0), (w, h), (0.0, h)]
        W0, D0 = 3.50, 14.00
        ok, why = rect_fits_no_rotation(rect, W0, D0, dh0)
        print("      %-28s ⇒ 容納 `%.2f × %.2f`？ %s（%s）%s"
              % (name, W0, D0, ok, why, "✅" if ok == must else "🔴 **未如預期 ⇒ 器紅**"))
        if ok != must:
            print("🔴 否證對照未如預期 ⇒ 量測器紅、輸出⛔ 出艙")
            return 4

    # ── d-1
    print()
    print("=" * 116)
    print("`d-1`　`K-9-9 一`：各宗遠側界是否 ∥ALLOCLINE")
    print("=" * 116)
    print("   🔒 **自我驗證閘之三處碼面明文斷言（內容錨·逐字·⛔ 行號為錨）**")
    ANCH = [
        "而 `K-9-5-4 ②` 令街角第 1 宗遠側界 ∥SIDELINE、「第 2 宗遠側界不動」使其遠側界留 ∥ALLOC",
        "#     街角第 1 宗之 `allocation_dir` 已換為 `_first_corner_alloc_dir(side_mid)` ⇒ 其遠側界 **∥SIDELINE**、非 ∥ALLOC。",
        "    ⛔ 不涵蓋第 2 宗以後（其境界線間皆 ∥ALLOCLINE·`K-9-17 四`）。",
    ]
    src = io.open(os.path.join(REPO, "app.py"), encoding="utf-8").read().split("\n")
    allok = True
    for a in ANCH:
        # 🔒 以**去縮排後之逐字**比對（`grep` 之輸出不帶原縮排 ⇒ 逐字比對須同框）
        n = sum(1 for l in src if l.rstrip("\r").strip() == a.strip())
        allok &= (n == 1)
        print("      命中 %d（須 1）｜逐字 ＝ %s" % (n, a.strip()[:96]))
    wide = sum(1 for l in src if "∥ALLOC" in l)
    print("      [唯一性之判別力自檢] 寬字樣 `∥ALLOC` @ app.py ＝ %d 列 ⇒ 該檢⛔ 恆為 1" % wide)
    if not allok:
        print("🔴 自我驗證閘之錨不唯一 ⇒ ⛔ 得下結論")
        return 5

    ALLOC = cad.get("alloc_dir_by_block") or {}
    print("   ALLOCLINE 之方向來源 ＝ **生產解析器**之 `cad['alloc_dir_by_block']`（⛔ 自寫第二份解析）")
    print("   其鍵 ＝ %s" % (sorted(ALLOC) if ALLOC else "🔴 **查無**"))
    if not ALLOC:
        print("   🛑 **`d-1` ⛔ 得下結論**：`cad` ⛔ 提供 ALLOCLINE 之方向向量")
        print("      **阻斷點** ＝ 其鍵名於 `cad` 之相異鍵 %s 內查無" % sorted(cad.keys()))
        return 0
    for k in sorted(ALLOC):
        print("        %-4s %s" % (k, ALLOC[k]))

    def ang_of(v):
        return math.degrees(math.atan2(v[1], v[0])) % 180.0

    print()
    print("   逐宗判（母體 ＝ 二情境全部分配宗·必紅組 ＝ 第 `0` 宗且 `第1筆街角 == 是`）")
    res = {"corner": [0, 0], "rest": [0, 0]}
    for tag, fn, sb in SCEN:
        rows = load(fn)
        grp = {}
        for r in rows:
            side = (r.get("推進側別") or "").strip()
            if side == "抵費地":
                continue
            lbl = (r.get("所屬街廓") or "").strip()
            cc = parse(r.get("cut_coords"))
            if cc is None:
                continue
            grp.setdefault((lbl, side), []).append((r, cc))
        for key, its in grp.items():
            its.sort(key=lambda t: float(t[0].get("累積S(m)") or 0))
            al = ALLOC.get(key[0])
            if not al:
                continue
            if isinstance(al, dict):
                av = (al["p2"][0] - al["p1"][0], al["p2"][1] - al["p1"][1])
            else:
                av = (float(al[0]), float(al[1]))     # 單位方向向量
            a_ang = ang_of(av)
            for i in range(len(its) - 1):
                sh = []
                for x in its[i][1]:
                    for y in its[i + 1][1]:
                        if abs(x[0] - y[0]) < QK and abs(x[1] - y[1]) < QK:
                            if not any(abs(x[0] - s[0]) < QK and abs(x[1] - s[1]) < QK for s in sh):
                                sh.append(x)
                if len(sh) != 2:
                    continue
                e_ang = ang_of((sh[1][0] - sh[0][0], sh[1][1] - sh[0][1]))
                d = min(abs(e_ang - a_ang), 180 - abs(e_ang - a_ang))
                par = d < 0.5
                is_corner = (its[i][0].get("第1筆街角") or "").strip() == "是"
                k = "corner" if is_corner else "rest"
                res[k][0 if par else 1] += 1
                if is_corner:
                    print("        〔必紅組〕%-5s %-4s %-6s %-14s 遠側界 ∠%.4f° vs ALLOC ∠%.4f°｜Δ %.4f° ⇒ %s"
                          % (tag, key[0], key[1], (its[i][0].get("暫編地號") or "").strip(),
                             e_ang, a_ang, d, "🔴 ∥ALLOCLINE" if par else "✅ ⛔ ∥（合於 `K-9-9 五`）"))
    print("      第 `0` 宗（街角地·**必紅組**）：∥ALLOCLINE %d 宗／⛔ ∥ %d 宗" % tuple(res["corner"]))
    print("      第 `1` 宗以後（**必綠組**）：  ∥ALLOCLINE %d 宗／⛔ ∥ %d 宗" % tuple(res["rest"]))
    same = (res["corner"][0] > 0) == (res["rest"][0] > 0) and (res["corner"][1] > 0) == (res["rest"][1] > 0)
    print("      ⇒ 二組同色？ %s ⇒ %s" % (same, "🔴 **閘失能·⛔ 得下結論**" if same else "✅ 閘有判別力"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
