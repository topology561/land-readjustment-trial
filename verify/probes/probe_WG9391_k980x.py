# -*- coding: utf-8 -*-
"""W-G.9-391 量測器（發單端擬·檔 F35·⛔ 由受單側改一字）：街角規定範圍與末端塊範圍依最小建築面積之擴大（`K-9-34`·
`K-9-80` ④⑤）與短街廓之二範圍相接或重疊之警示停止（`K-9-80` ⑥）。

所量之性質：街廓有最小建築面積之輸入（有效值 ＞ 0）而範圍之面積 ＜ 之 ⇒ 街角規定範圍之遠側界線續沿 SIDE_LINE 之法向平移
（∥SIDE_LINE）、末端塊範圍之內側界線續沿 ALLOC 平行內移（末端塊無退縮），至 `0 ≤ 面積 − 最小建築面積 ≤ 0.01 ㎡`；未輸入
（`None`、`0`）或面積已 ≥ 之 ⇒ 範圍⛔ 變（逐位同）；跨占之名單與門檻皆以擴大後之範圍定之（單一真相源）；一街廓之二範圍
（街角與街角、街角與末端塊、末端塊與末端塊）擴大後相接（距 ≤ 0.01 m）或重疊、或擴至街廓之他端仍未達 ⇒ 停機（警示停止）。

子命令（一律 python3 verify/probes/probe_WG9391_k980x.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式）。玩具街廓 BA：x∈[0,60]、y∈[0,30]，正面 y ＝ 0（p1 ＝ (0,0)·
           p2 ＝ (60,0)），屁股線 y ＝ 30，左側街 x ＝ 0（截角三角形 (0,0)(3,0)(0,3)），宗地分配線 ∥ y 軸；退縮 0、畸零地寬 3.5、
           分配深度 30。期值皆手算（各例之註）：
           C1 未輸入（`None`）⇒ 面積 100.5（＝ 3.5×30 − 4.5）；C2 輸入 0 ⇒ 與 C1 逐位同；C3 輸入 100（＜ 100.5）⇒ 同 C1；
           C4 輸入恰 100.5 ⇒ 同 C1（門檻上）；C5 輸入 150 ⇒ 面積 ∈ [150, 150.01]、遠側界線 x ＝ 5.15（±0.001）∥ SIDE_LINE、
           含 C1 之範圍；C6 輸入 2000（＞ 街廓 1795.5）⇒ 停機（訊息含「K-9-80 ⑥」）；C7 輸入 −1 ⇒ 停機；C8 C5 之旋轉 37°、
           鏡射並移至 TWD97 之尺度 ⇒ 面積同 C5（±1e-6）；C9 側街斜交（SIDE_LINE (0,0)→(6,30)·宗地分配線 ∥ y 軸·截角
           (0,0)(3,0)(0.6,3)）輸入 200 ⇒ 面積 ∈ [200, 200.01]、遠側界線 ∥ SIDE_LINE（其於 y＝0 與 y＝30 之 x 差 ＝ 6）。末端塊之玩具 BE：多邊形 (10,0)(70,0)(70,30)(0,30)，正面 p1 ＝ (10,0)、
           p2 ＝ (70,0)，左端之未臨正街 ＝ 三角形 150 ㎡：E1 未輸入 ⇒ R_end 255（＝ 150 ＋ 3.5×30）、內側界 x ＝ 13.5；E2 輸入 255
           （門檻上）⇒ 同 E1；E3 輸入 300 ⇒ R_end ∈ [300, 300.01]、內側界 x ＝ 15（±0.001·∥ ALLOC）；E4 輸入 2000 ⇒ 停機
           （「K-9-80 ⑥」）；E5 E3 之旋轉、鏡射、TWD97 ⇒ 同 E3；E6 `_end_region_R` 之未輸入與 0 ⇒ R_end 逐位同（255）、
           `end_block_band_width` 之 0 ⇒ 停機（⛔ 入本函式）。
           相接之判 T1 二矩形之距 0.02 ⇒ ⛔ 停；T2 距恰 0.01 ⇒ 停（≤）；T3 距 0.005 ⇒ 停；T4 重疊 ⇒ 停（訊息含二範圍之名）；
           T5 唯一範圍或含 `None` ⇒ ⛔ 停；T6 三範圍而唯其中二者相接 ⇒ 停。K1 `k980_mba` 之有效值之序（`K-9-1` ⑨ 裁丙：街廓覆寫
           → 分區底 → 0；session 無鍵或 `None` ⇒ 0）。P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           W1 `_build_corner_range_v3(` 之生產呼叫（`app.py`、`verify/stepg_pipeline.py`、`verify/run_verification.py`·AST）
           皆以關鍵字傳 `min_build_area`；W2 `end_block_side_geom(`、`end_block_host(`、`_place_pool_parcels(` 之呼叫（同上
           三檔·含 `ns["…"](` 之形）皆傳 `min_build_area`；W3 末端帶之單一真相源：`_place_pool_parcels` 呼叫 `_end_region_R`
           恰一、⛔ 呼叫 `_end_band`，`_end_region_R` 呼叫 `end_block_band_width` 恰一（全檔亦恰一）；W4 上開生產呼叫之 `min_build_area=` 之值皆為 `k980_mba(…)`
           （`select_corner_lots_both_sides_v12` 之 `_mba_pk` 之賦值恰一為之·其餘唯 `None`）、`k91_effective_min_build_area` 於
           `k980_mba` 外之呼叫之數對基準⛔ 增；W5 `k980_range_touch_check(` 之呼叫：`select_corner_lots_both_sides_v12` 內、
           `f3_screen_stepg_run` 內、`verify/stepg_pipeline.py` 之 `_run_step_g_impl` 內各恰一（`app.py` 全檔恰二）；W6 `app.py`
           之頂層之名之增恰 `{K980_AREA_TOL, K980_AREA_EPS, K980_TOUCH_TOL, end_block_band_width, k980_range_touch_check,
           k980_mba}`、無減；W7 新增或改之頂層節點內⛔ 案件字面；
           W8 `min_build_area` 之逐層照傳（`end_block_host`→`end_block_apply`→`end_block_side_geom`→`_end_region_R`、
           `_place_pool_parcels`→`_end_region_R` 之呼叫皆恰一而傳 `min_build_area=min_build_area`）；W9 `verify/stepg_pipeline.py`
           經 `ns["…"]` 取之新名皆在 `app.py` 之 `_WF_NS_NAMES`（app 之七級調配之路·漏列即 KeyError）。另 W4 之 `k980_mba`
           之分區之引數⛔ 為字面、W5 之範圍之名齊全（v12 二·二宿主四）。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 未輸入（harness 之現狀）⇒ 參數表之街角最小面積、街角選位之範圍面積、
           Step-G 之 ctx 之範圍面積三者同、末端塊之紀錄之 `R_end` ＝ 改前之式（未臨正街 ＋ 末端帶）；R2 以 session 之 `K91_SS_MBA_BY_LABEL`（畫面之同一鍵）輸入「各街廓之最小建築面積 ＝ 其未輸入時之最大範圍之面積
           ＋ 10 ㎡」⇒ 上開三源之街角最小面積皆 ＝ 輸入值（±0.01）、末端塊之 `R_end` ＝ 輸入值（±0.01）、⛔ 停機。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
K6 = "K-9-80 ⑥"
NEW392 = {"K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check"}   # 🔧 `W-G.9-392`
NEW398 = {"RW_TABLE_25"}   # 🔧 `W-G.9-398`（側面道路負擔百分率之附表 25·F41 量之）
# 🔧 `W-G.9-398` 補令一（寬度先取至公釐·跳處之甲·KL `2026-10-27 23:29`·`2026-10-28 10:48`·⛔ 上列一字不刪）：其二新函式與所改之頂層節點（F41 量之）。
NEW398B = {"rw_width_mm", "rw_pct_2dp"}
# 🔧 `W-G.9-399`（末端塊評選指數·KL `2026-10-26 22:09`／`22:42`／`22:57`·⛔ 上列一字不刪）：其新之頂層名與所改之頂層節點（F42 量之）。
NEW399 = {"END_BLOCK_LINE_TOL", "END_BLOCK_IDX_W_LINE", "END_BLOCK_IDX_W_AREA", "end_block_end_line", "end_block_end_segs",
          "end_block_end_geom", "k960_idx_rank", "k960_idx_key", "k960_idx_first"}
NEW_TOP = {"K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check",
           "k980_mba"}


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


# ───────────────────────── selftest ─────────────────────────

def _xf(ang_deg, mirror, tx, ty):
    c, s = math.cos(math.radians(ang_deg)), math.sin(math.radians(ang_deg))

    def f(p):
        x, y = float(p[0]), float(p[1])
        if mirror:
            x = -x
        return (c * x - s * y + tx, s * x + c * y + ty)

    def v(d):
        x, y = float(d[0]), float(d[1])
        if mirror:
            x = -x
        return (c * x - s * y, s * x + c * y)
    return f, v


def _corner(ns, mba, xf=None, mirror=False):
    from shapely.geometry import Polygon
    f, v = xf if xf else ((lambda p: (float(p[0]), float(p[1]))), (lambda d: (float(d[0]), float(d[1]))))
    blk = [f(p) for p in [(3, 0), (60, 0), (60, 30), (0, 30), (0, 3)]]
    front = [f((0, 0)), f((60, 0))]
    if mirror:                                  # 鏡射 ⇒ 左右互換：p1 須仍為「左」（FRONT 之方向約定）
        front = [front[1], front[0]]
    cen = Polygon(blk).centroid.coords[0]
    return ns["_build_corner_range_v3"](
        blk, cen, front, [f((0, 30)), f((60, 30))], [f((0, 0)), f((0, 30))], v((0, 1)), 30.0, 0.0, 3.5,
        Polygon([f((0, 0)), f((3, 0)), f((0, 3))]), dxf_quantum=0.0001, _label="BA",
        _side=("right" if mirror else "left"), min_build_area=mba)


def _end(ns, mba, xf=None, mirror=False):
    import numpy as np
    from shapely.geometry import Polygon
    f, v = xf if xf else ((lambda p: (float(p[0]), float(p[1]))), (lambda d: (float(d[0]), float(d[1]))))
    poly = Polygon([f(p) for p in [(10, 0), (70, 0), (70, 30), (0, 30)]])
    A = np.asarray
    p1, p2 = A(f((10, 0))), A(f((70, 0)))
    d = A(v((1, 0)))
    ca = A(v((0, 1)))
    ad = A((-ca[1], ca[0]))
    if mirror:                                  # 鏡射之後左端在 p2 側 ⇒ 以右端量之（p1／p2 互換、d̂ 反向）
        g = ns["end_block_side_geom"](poly, -d, p2, p1, ca, -ad, 3.5, "right", _label="BE", min_build_area=mba)
    else:
        g = ns["end_block_side_geom"](poly, d, p1, p2, ca, ad, 3.5, "left", _label="BE", min_build_area=mba)
    return g


def _inner_x(geom, xf_inv=None):
    xs = [p[0] for p in geom.exterior.coords]
    return xs


def selftest(repo):
    ns, _ = _harvest(repo)
    need = ["_build_corner_range_v3", "end_block_side_geom", "end_block_band_width", "k980_range_touch_check",
            "_end_band", "K980_AREA_TOL", "K980_TOUCH_TOL", "k980_mba"]
    miss = [n for n in need if n not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    from shapely.geometry import Polygon, box
    C = []

    def run(fn):
        try:
            return ("ok", fn())
        except RuntimeError as e:
            return ("停", str(e))
        except Exception as e:  # noqa: BLE001
            return ("例外", f"{type(e).__name__}: {e}")

    def area(r):
        return round(float(r[1].area), 6) if r[0] == "ok" else r

    def stopped(r, key=K6):
        return r[0] == "停" and key in r[1]

    c1 = run(lambda: _corner(ns, None))
    base_wkb = c1[1].wkb if c1[0] == "ok" else None
    C.append(("C1 未輸入 ⇒ 100.5", area(c1), 100.5))
    for nm, m in (("C2 輸入 0 ⇒ 逐位同 C1", 0), ("C3 輸入 100 ⇒ 逐位同 C1", 100.0), ("C4 輸入恰 100.5 ⇒ 逐位同 C1", 100.5)):
        r = run(lambda m=m: _corner(ns, m))
        C.append((nm, (r[0] == "ok" and r[1].wkb == base_wkb), True))
    c5 = run(lambda: _corner(ns, 150.0))
    if c5[0] == "ok":
        a5 = float(c5[1].area)
        xs = sorted({round(p[0], 3) for p in c5[1].exterior.coords})
        xm = max(p[0] for p in c5[1].exterior.coords)
        par = {(round(p[0], 9), round(p[1], 6)) for p in c5[1].exterior.coords if abs(p[0] - xm) < 1e-3}
        g5 = (150.0 <= a5 <= 150.01, abs(xm - 5.15) <= 0.001,
              len(par) >= 2 and max(q[0] for q in par) - min(q[0] for q in par) < 1e-9,
              bool(c1[0] == "ok" and c5[1].buffer(1e-9).contains(c1[1])))
    else:
        g5 = c5
    C.append(("C5 輸入 150 ⇒ 面積∈[150,150.01]·遠側 x＝5.15·∥SIDE_LINE·含 C1", g5, (True, True, True, True)))
    C.append(("C6 輸入 2000 ⇒ 停機（K-9-80 ⑥）", stopped(run(lambda: _corner(ns, 2000.0))), True))
    C.append(("C7 輸入 −1 ⇒ 停機", run(lambda: _corner(ns, -1.0))[0], "停"))
    xf = _xf(37.0, True, 301234.5, 2650987.25)
    c8 = run(lambda: _corner(ns, 150.0, xf=xf, mirror=True))
    C.append(("C8 C5 之旋轉 37°·鏡射·TWD97 ⇒ 面積同 C5", (c8[0] == "ok" and c5[0] == "ok"
                                                    and abs(float(c8[1].area) - float(c5[1].area)) <= 1e-6), True))
    def _obl(mba):
        blk = [(3, 0), (60, 0), (60, 30), (6, 30), (0.6, 3)]
        return ns["_build_corner_range_v3"](
            blk, Polygon(blk).centroid.coords[0], [(0, 0), (60, 0)], [(6, 30), (60, 30)], [(0, 0), (6, 30)], (0, 1),
            30.0, 0.0, 3.5, Polygon([(0, 0), (3, 0), (0.6, 3)]), dxf_quantum=0.0001, _label="BO", _side="left",
            min_build_area=mba)
    c9 = run(lambda: _obl(200.0))
    if c9[0] == "ok":
        _pts = list(c9[1].exterior.coords)
        _xa = max(p[0] for p in _pts if abs(p[1]) < 1e-6)
        _xb = max(p[0] for p in _pts if abs(p[1] - 30.0) < 1e-6)
        g9 = (200.0 <= float(c9[1].area) <= 200.01, abs((_xb - _xa) - 6.0) <= 1e-6)
    else:
        g9 = c9
    C.append(("C9 側街斜交（∦ 宗地分配線）輸入 200 ⇒ 面積∈[200,200.01]·遠側界線 ∥ SIDE_LINE（Δx＝6）", g9, (True, True)))
    e1 = run(lambda: _end(ns, None))
    if e1[0] == "ok":
        g1 = (round(float(e1[1]["r_end_area"]), 6), round(float(e1[1]["buf"]), 6))
    else:
        g1 = e1
    C.append(("E1 未輸入 ⇒ R_end 255·內側界 13.5（buf 3.5）", g1, (255.0, 3.5)))
    e2 = run(lambda: _end(ns, 255.0))
    C.append(("E2 輸入恰 255 ⇒ 逐位同 E1", (e2[0] == "ok" and e1[0] == "ok" and e2[1]["r_end"].wkb == e1[1]["r_end"].wkb), True))
    e3 = run(lambda: _end(ns, 300.0))
    if e3[0] == "ok":
        a3 = float(e3[1]["r_end_area"])
        g3 = (300.0 <= a3 <= 300.01, abs(float(e3[1]["buf"]) - 5.0) <= 0.001)
    else:
        g3 = e3
    C.append(("E3 輸入 300 ⇒ R_end∈[300,300.01]·內側界 x＝15", g3, (True, True)))
    C.append(("E4 輸入 2000 ⇒ 停機（K-9-80 ⑥）", stopped(run(lambda: _end(ns, 2000.0))), True))
    e5 = run(lambda: _end(ns, 300.0, xf=xf, mirror=True))
    C.append(("E5 E3 之旋轉·鏡射·TWD97 ⇒ R_end 同 E3", (e5[0] == "ok" and e3[0] == "ok"
                                                and abs(float(e5[1]["r_end_area"]) - float(e3[1]["r_end_area"])) <= 1e-6), True))
    bp = Polygon([(10, 0), (70, 0), (70, 30), (0, 30)])
    frag = Polygon([(10, 0), (10, 30), (0, 30)])
    import numpy as np
    e6 = [run(lambda m=m: ns["_end_region_R"](bp, np.asarray((0.0, 1.0)), np.asarray((10.0, 0.0)), 3.5, frag,
                                             _label="BE", min_build_area=m)) for m in (None, 0)]
    e6b = run(lambda: ns["end_block_band_width"](bp, np.asarray((0.0, 1.0)), np.asarray((10.0, 0.0)), 3.5, frag, 0,
                                                 _label="BE"))
    C.append(("E6 _end_region_R 之未輸入與 0 ⇒ R_end 逐位同（255）；end_block_band_width 之 0 ⇒ 停機",
              (all(x[0] == "ok" for x in e6) and e6[0][1][1].wkb == e6[1][1][1].wkb and round(e6[0][1][2], 6),
               e6b[0]), (255.0, "停")))
    chk = ns["k980_range_touch_check"]
    a = box(0, 0, 10, 30)
    C.append(("T1 距 0.02 ⇒ ⛔ 停", run(lambda: chk("BA", {"甲": a, "乙": box(10.02, 0, 20, 30)}))[0], "ok"))
    # 距恰為 K980_TOUCH_TOL 之浮點值（0.01 − 0 ＝ 0.01·⛔ 以 10.01 − 10 之捨入）
    C.append(("T2 距恰 0.01 ⇒ 停", stopped(run(lambda: chk("BA", {"甲": box(-10, 0, 0, 30), "乙": box(0.01, 0, 10, 30)}))),
              True))
    C.append(("T3 距 0.005 ⇒ 停", stopped(run(lambda: chk("BA", {"甲": a, "乙": box(10.005, 0, 20, 30)}))), True))
    t4 = run(lambda: chk("BA", {"左側街角規定範圍": a, "右端末端塊範圍": box(9, 0, 20, 30)}))
    C.append(("T4 重疊 ⇒ 停（訊息具二範圍之名）", (stopped(t4) and "左側街角規定範圍" in t4[1] and "右端末端塊範圍" in t4[1]), True))
    C.append(("T5 唯一範圍或含 None ⇒ ⛔ 停", [run(lambda: chk("BA", {"甲": a}))[0],
                                          run(lambda: chk("BA", {"甲": a, "乙": None}))[0]], ["ok", "ok"]))
    C.append(("T6 三範圍而唯其中二者相接 ⇒ 停", stopped(run(lambda: chk("BA", {"甲": a, "乙": box(30, 0, 40, 30),
                                                                    "丙": box(40.0, 0, 50, 30)}))), True))
    mb = ns["k980_mba"]
    L_, C_ = ns["K91_SS_MBA_BY_LABEL"], ns["K91_SS_MBA_BY_CATEGORY"]
    C.append(("K1 有效值之序（K-9-1 ⑨）：街廓覆寫 → 分區底 → 0；session 無鍵或 None ⇒ 0",
              [mb({L_: {"BA": 180.0}, C_: {"住宅區": 120.0}}, "BA", "住宅區"),
               mb({L_: {"BB": 180.0}, C_: {"住宅區": 120.0}}, "BA", "住宅區"),
               mb({L_: {"BA": 0}, C_: {"商業區": 120.0}}, "BA", "住宅區"), mb({}, "BA", "住宅區"), mb(None, "BA", "住宅區")],
              [180.0, 120.0, 0.0, 0.0, 0.0]))
    red = []
    for name, got, exp in C:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {got!r}"[:700])
            print(f"       期 {exp!r}"[:700])
            red.append(name.split()[0])
    base = {j for j, (_, g2, e2) in enumerate(C) if g2 != e2}
    p0 = 0
    for i in range(len(C)):
        bad = {j for j, (_, g2, e2) in enumerate(C) if g2 != (("擾動", e2) if j == i else e2)}
        if bad == base | {i}:
            p0 += 1
    ok0 = p0 == len(C)
    print(("  ✅ " if ok0 else "  🔴 ") + f"P0 判式自驗 {p0}／{len(C)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── wiring ─────────────────────────

def _git(repo, *a):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else ""


def _callee(n):
    f = n.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant) and isinstance(f.slice.value, str):
        return f.slice.value
    return None


def _calls(tree, name):
    return [n for n in ast.walk(tree) if isinstance(n, ast.Call) and _callee(n) == name]


def _kw(n, k):
    return any(kw.arg == k for kw in n.keywords)


def _fn_node(tree, name):
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return n
    return None


def _top(src):
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            out[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = ast.dump(n)
    return out


def wiring(repo, base):
    print(f"── 接線（工作樹對基準 {base}）──")
    red = []
    srcs = {}
    for p in ("app.py", "verify/stepg_pipeline.py", "verify/run_verification.py", "verify/selection_pipeline.py"):
        try:
            srcs[p] = open(os.path.join(repo, p), encoding="utf-8").read()
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️ {p} 讀不到：{type(e).__name__}")
            print("⇒ rc 3（無從判定）")
            return 3
    old = _git(repo, "show", f"{base}:app.py")
    if not old:
        print("  ⚠️ 基準之 app.py 取不到")
        print("⇒ rc 3（無從判定）")
        return 3
    trees = {p: ast.parse(s) for p, s in srcs.items()}
    three = ("app.py", "verify/stepg_pipeline.py", "verify/run_verification.py")
    w1 = [(p, n.lineno, _kw(n, "min_build_area")) for p in three for n in _calls(trees[p], "_build_corner_range_v3")]
    ok1 = len(w1) >= 4 and all(x[2] for x in w1)
    print(("  ✅" if ok1 else "  🔴") + f" W1 _build_corner_range_v3 之呼叫 {len(w1)}（期 ≥ 4）皆傳 min_build_area："
          f"{[x[:2] for x in w1 if not x[2]] or '皆傳'}")
    if not ok1:
        red.append("W1")
    w2 = {nm: [(p, n.lineno, _kw(n, "min_build_area")) for p in three for n in _calls(trees[p], nm)]
          for nm in ("end_block_side_geom", "end_block_host", "_place_pool_parcels")}
    ok2 = (len(w2["end_block_side_geom"]) >= 1 and len(w2["end_block_host"]) >= 2 and len(w2["_place_pool_parcels"]) >= 2
           and all(x[2] for v in w2.values() for x in v))
    print(("  ✅" if ok2 else "  🔴") + f" W2 諸呼叫之數 {[(k, len(v)) for k, v in w2.items()]}（期 ≥ 1、≥ 2、≥ 2）皆傳 "
          f"min_build_area：{[(k, x[:2]) for k, v in w2.items() for x in v if not x[2]] or '皆傳'}")
    if not ok2:
        red.append("W2")
    ta = trees["app.py"]
    ppp, erR = _fn_node(ta, "_place_pool_parcels"), _fn_node(ta, "_end_region_R")
    w3 = {"_place_pool_parcels→_end_region_R": len(_calls(ppp, "_end_region_R")) if ppp else -1,
          "_place_pool_parcels→_end_band": len(_calls(ppp, "_end_band")) if ppp else -1,
          "_end_region_R→end_block_band_width": len(_calls(erR, "end_block_band_width")) if erR else -1,
          "end_block_band_width 之呼叫（全檔）": len(_calls(ta, "end_block_band_width"))}
    ok3 = (w3["_place_pool_parcels→_end_region_R"] == 1 and w3["_place_pool_parcels→_end_band"] == 0
           and w3["_end_region_R→end_block_band_width"] == 1 and w3["end_block_band_width 之呼叫（全檔）"] == 1)
    print(("  ✅" if ok3 else "  🔴") + f" W3 末端帶之單一真相源 {w3}（期 1、0、1、1）")
    if not ok3:
        red.append("W3")
    # W4 最小建築面積之源：生產呼叫之 `min_build_area=` 之值皆為 `k980_mba(…)`（或 v12 之 `_mba_pk`·其賦值為之）
    vals, bad4 = [], []
    for p in three:
        for nm in ("_build_corner_range_v3", "end_block_host", "_place_pool_parcels"):
            for n in _calls(trees[p], nm):
                v = next((k.value for k in n.keywords if k.arg == "min_build_area"), None)
                ok_ = (isinstance(v, ast.Call) and _callee(v) == "k980_mba") or (isinstance(v, ast.Name) and v.id == "_mba_pk")
                vals.append((p, nm, n.lineno))
                if not ok_:
                    bad4.append((p, nm, n.lineno))
    v12 = _fn_node(ta, "select_corner_lots_both_sides_v12")
    asg = [n for n in ast.walk(v12) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_mba_pk"
                                                                        for t in n.targets)] if v12 else []
    asg_ok = sum(1 for n in asg if isinstance(n.value, ast.Call) and _callee(n.value) == "k980_mba") == 1 and \
        all((isinstance(n.value, ast.Call) and _callee(n.value) == "k980_mba") or
            (isinstance(n.value, ast.Constant) and n.value.value is None) for n in asg)
    k91 = [(p, n.lineno) for p in three for n in _calls(trees[p], "k91_effective_min_build_area")
           if _fn_node(trees[p], "k980_mba") is None or not (_fn_node(trees[p], "k980_mba").lineno <= n.lineno
                                                              <= _fn_node(trees[p], "k980_mba").end_lineno)]
    k91b = [(p, n.lineno) for p in three for n in _calls(ast.parse(_git(repo, "show", f"{base}:{p}") or "pass"),
                                                          "k91_effective_min_build_area")]
    lit_cat = [(p, n.lineno) for p in three for n in _calls(trees[p], "k980_mba")
               if len(n.args) >= 3 and isinstance(n.args[2], ast.Constant)]
    ok4 = len(vals) >= 8 and not bad4 and asg_ok and len(k91) == len(k91b) and not lit_cat
    print(("  ✅" if ok4 else "  🔴") + f" W4 min_build_area 之值皆為 k980_mba（呼叫 {len(vals)}·期 ≥ 8·不合 {bad4}）、v12 之 _mba_pk "
          f"之賦值 {asg_ok}、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（{len(k91)}／基準 {len(k91b)}）、"
          f"k980_mba 之分區之引數為字面者 {lit_cat}（期無）")
    if not ok4:
        red.append("W4")
    w5 = []
    for fname in ("select_corner_lots_both_sides_v12", "f3_screen_stepg_run"):
        fn = _fn_node(ta, fname)
        w5.append((fname, len(_calls(fn, "k980_range_touch_check")) if fn else -1))
    tot5 = len(_calls(ta, "k980_range_touch_check"))
    sgh = _fn_node(trees["verify/stepg_pipeline.py"], "_run_step_g_impl")
    w5.append(("stepg:_run_step_g_impl", len(_calls(sgh, "k980_range_touch_check")) if sgh else -1))
    K4 = {"左側街角規定範圍", "右側街角規定範圍", "左端末端塊範圍", "右端末端塊範圍"}
    keys5 = []
    for fn, need in ((_fn_node(ta, "select_corner_lots_both_sides_v12"), K4 - {"左端末端塊範圍", "右端末端塊範圍"}),
                     (_fn_node(ta, "f3_screen_stepg_run"), K4), (sgh, K4)):
        for n in (_calls(fn, "k980_range_touch_check") if fn else []):
            d = n.args[1] if len(n.args) >= 2 else None
            got = {k.value for k in d.keys if isinstance(k, ast.Constant)} if isinstance(d, ast.Dict) else set()
            keys5.append(got == need)
    ok5 = all(c == 1 for _, c in w5) and tot5 == 2 and len(keys5) == 3 and all(keys5)
    print(("  ✅" if ok5 else "  🔴") + f" W5 k980_range_touch_check 之呼叫 {w5}·app.py 全檔 {tot5}（期各 1·app.py 全 2）、"
          f"其範圍之名齊全 {keys5}（期三真）")
    if not ok5:
        red.append("W5")
    tn, tb = _top(srcs["app.py"]), _top(old)
    add, rem = set(tn) - set(tb), set(tb) - set(tn)
    ok6 = add == NEW_TOP and not rem
    ok6 = ok6 or (add == NEW_TOP | NEW392 and not rem)   # 🔧 `W-G.9-392`：其後之單之四新名亦許（F36 量之）
    ok6 = ok6 or (add == NEW_TOP | NEW392 | NEW398 and not rem)   # 🔧 `W-G.9-398`：其後之單之新常數亦許（F41 量之）
    ok6 = ok6 or (add == NEW_TOP | NEW392 | NEW398 | NEW398B and not rem)   # 🔧 `W-G.9-398` 補令一：同（F41 量之）
    ok6 = ok6 or (add == NEW_TOP | NEW392 | NEW398 | NEW398B | NEW399 and not rem)   # 🔧 `W-G.9-399`：同（F42 量之）
    print(("  ✅" if ok6 else "  🔴") + f" W6 頂層之名之增 {sorted(add)}（期 {sorted(NEW_TOP)}）、減 {sorted(rem)}")
    if not ok6:
        red.append("W6")
    chg = sorted(k for k in tn if tn.get(k) != tb.get(k))
    lits = []
    for n in ta.body:
        nm = getattr(n, "name", None) or (n.targets[0].id if isinstance(n, ast.Assign)
                                          and isinstance(n.targets[0], ast.Name) else None)
        if nm in chg:
            seg = ast.get_source_segment(srcs["app.py"], n) or ""
            segb = ""
            ob = _fn_node(ast.parse(old), nm)
            if ob is not None:
                segb = ast.get_source_segment(old, ob) or ""
            newc = {c.value for c in ast.walk(n) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                    and CASE_LIT_RE.match(c.value)}
            oldc = {c.value for c in ast.walk(ob) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                    and CASE_LIT_RE.match(c.value)} if ob is not None else set()
            lits += sorted((nm, x) for x in newc - oldc)
    ok7 = not lits
    print(("  ✅" if ok7 else "  🔴") + f" W7 新增或改之頂層節點（{len(chg)}）內新增之案件字面 {lits}")
    if not ok7:
        red.append("W7")
    # W8 逐層照傳（`min_build_area=min_build_area`·⛔ 改傳 None 或他值）
    w8 = []
    for outer, inner in (("end_block_host", "end_block_apply"), ("end_block_apply", "end_block_side_geom"),
                         ("end_block_side_geom", "_end_region_R"), ("_place_pool_parcels", "_end_region_R")):
        fo = _fn_node(ta, outer)
        cs = _calls(fo, inner) if fo else []
        ok_ = len(cs) == 1 and any(k.arg == "min_build_area" and isinstance(k.value, ast.Name)
                                   and k.value.id == "min_build_area" for k in cs[0].keywords)
        w8.append((outer, inner, ok_))
    ok8 = all(x[2] for x in w8)
    print(("  ✅" if ok8 else "  🔴") + f" W8 逐層照傳 min_build_area {[(a, b) for a, b, o in w8 if not o] or '皆照傳'}")
    if not ok8:
        red.append("W8")
    # W9 引擎經 ns 取之新名皆在 `_WF_NS_NAMES`（app 之七級調配之路·漏列即 KeyError）
    wf = next((n.value for n in ta.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
               and t.id == "_WF_NS_NAMES" for t in n.targets)), None)
    wfn = {e.value for e in getattr(wf, "elts", []) if isinstance(e, ast.Constant)}
    used = {n.slice.value for n in ast.walk(trees["verify/stepg_pipeline.py"]) if isinstance(n, ast.Subscript)
            and isinstance(n.value, ast.Name) and n.value.id == "ns" and isinstance(n.slice, ast.Constant)
            and n.slice.value in NEW_TOP}
    ok9 = bool(used) and used <= wfn
    print(("  ✅" if ok9 else "  🔴") + f" W9 引擎經 ns 取之新名 {sorted(used)} ⊆ _WF_NS_NAMES（漏 {sorted(used - wfn)}）")
    if not ok9:
        red.append("W9")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

def _one(ns, fst, sb, mba_by):
    import run_verification as rv
    import selection_pipeline as sp
    from stepg_pipeline import run_step_g
    import stepg_pipeline
    out = {"err": None}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            snap = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fst, snap)
            # 最小建築面積之輸入 ＝ session 之 `K91_SS_MBA_BY_LABEL`（畫面之同一鍵）；`None` ⇒ 去之（未輸入）
            fst.session_state.pop(ns["K91_SS_MBA_BY_CATEGORY"], None)
            if mba_by is None:
                fst.session_state.pop(ns["K91_SS_MBA_BY_LABEL"], None)
            else:
                fst.session_state[ns["K91_SS_MBA_BY_LABEL"]] = dict(mba_by)
            rv.build_ownership(ns, fst, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
            params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
            out["param"] = {(r["街廓"], s): r.get(f"【{c}】街角最小面積(㎡)") for r in params
                            for s, c in (("left", "左"), ("right", "右")) if r.get(f"【{c}】街角最小面積(㎡)") is not None}
            try:
                # 🔧 `W-G.9-393`：段三之入口（`run_corner_pk_k6b`·含末端塊之合併再試）——無側街之端一律為末端塊之後，
                #   輸入之最小建築面積可使無三角地之端之各筆單獨皆未達，其處置（合併再試 ⇒ 強制抵費地）唯此入口有之。
                os.environ["WV_K6B_STAGE3"] = "on"
                res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
                ra = fst.session_state.get("f3_corner_range_areas", {}) or {}
                out["pk"] = {(b, s): v.get(s) for b, v in ra.items() for s in ("left", "right") if v.get(s) is not None}
                ns["K917_DROPPED"].clear()
                sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                                eff_min_build_by_blk={})
                out["ctx"] = {k: round(float(v.area), 2) for k, v in (sg.get("corner_range_polys") or {}).items()
                              if v is not None}
                ev = fst.session_state.get(ns["SS_END_BLOCK_EVAL"]) or {}
                out["rend"] = {(b, s): v.get("R_end(㎡)") for b, e in ev.items() for s, v in e.items() if v.get("觸發")}
            except RuntimeError as e:
                out["err"] = str(e).splitlines()[0][:300]
    finally:
        fst.session_state.pop(ns["K91_SS_MBA_BY_LABEL"], None)
    return out


def run(repo, sbs):
    ns, fst = _harvest(repo)
    if "end_block_band_width" not in ns:
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    for sb in sbs:
        try:
            r0 = _one(ns, fst, sb, None)
            ok1 = (r0["err"] is None and r0["param"] and all(abs(float(r0["param"][k]) - float(r0["pk"].get(k, -1))) <= 0.01
                                                             for k in r0["param"])
                   and all(abs(float(r0["param"][k]) - float(r0["ctx"].get(k, -1))) <= 0.01 for k in r0["param"]))
            det1 = f"街角 {len(r0.get('param') or {})}·末端塊 {r0.get('rend')}·err {r0['err']}"
        except Exception as e:  # noqa: BLE001
            ok1, det1, r0 = False, f"例外 {type(e).__name__}：{str(e)[:200]}", None
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb} 未輸入：三源之街角範圍面積同（{det1}）")
        if not ok1:
            red.append(f"R1@{sb}")
            continue
        mx = {}
        for (b, s), v in list(r0["param"].items()) + list((r0.get("rend") or {}).items()):
            mx[b] = max(mx.get(b, 0.0), float(v))
        mba = {b: round(v + 10.0, 2) for b, v in mx.items()}
        try:
            r2 = _one(ns, fst, sb, mba)
            if r2["err"] is not None:
                ok2 = False    # 輸入值 ＝ 最大範圍 ＋ 10 ㎡ ⇒ 本案⛔ 短街廓·任何停機皆不合
                det2 = f"停機 {r2['err'][:160]}"
            else:
                bad = [(k, v, mba[k[0]]) for src in ("param", "pk", "ctx", "rend") for k, v in (r2.get(src) or {}).items()
                       if not (mba[k[0]] - 1e-9 <= float(v) + 0.005 and float(v) <= mba[k[0]] + 0.01 + 0.005)]
                ok2 = (not bad and set(r2["param"]) == set(r0["param"]) and set(r2["pk"]) == set(r0["param"])
                       and set(r2["ctx"]) == set(r0["param"]) and set(r2.get("rend") or {}) == set(r0.get("rend") or {}))
                det2 = f"輸入 {mba}·不合 {bad[:4]}"
        except Exception as e:  # noqa: BLE001
            ok2, det2 = False, f"例外 {type(e).__name__}：{str(e)[:200]}"
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb} 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（{det2}）")
        if not ok2:
            red.append(f"R2@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], os.path.abspath(argv[2])
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "wiring":
        if len(argv) != 4:
            print("用法：wiring <repo> <基準 commit>")
            return 2
        return wiring(repo, argv[3])
    if cmd == "run":
        sys.path.insert(0, os.path.join(repo, "verify"))
        os.chdir(repo)
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
