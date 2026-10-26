# -*- coding: utf-8 -*-
"""W-G.9-398 量測器（發單端擬·檔 F41·⛔ 由受單側改一字）：街角地側面道路負擔百分率（`Rw`）改照手冊附表 25
（KL `2026-10-26 09:53`「是」·`K-9-41` ⑥ 之細化）。

所量之性質：`rw_from_width(W)`（`Rw` 之唯一之產生處·`rw_increment` 與一切消費者皆經之）之值 ＝ 手冊附表 25「街角地側面道路負擔
百分率累積表」——`W` ＝ 1.0〜17.9 m 每 0.1 m 一格（二位小數）、格間（公分以下）線性內插、`W ≥ 18 m` ＝ 100；`W ≤ 0` ＝ 0（首宗起點
一律為 0·`K-9-5-12`·累積差額制之全側合計 ＝ `R(W_最末) − R(0)`·`K-9-41` ⑤）；`0 ＜ W ＜ 1` ＝ 自 (0, 0) 至 (1.0, 17.36) 之線性內插
（附表 25 與附件二之簡表皆自 1 m 起·手冊無 0〜1 m 之值·塊 `K46` 之二丙：凡寬 ＜ 1 m 之宗皆不合最小寬〔畸零地附表之最小寬 ≥ 3 m〕
而不配地 ⇒ 其值⛔ 生土地之果）。

期值之源（⛔ 由受測之碼產·`fixture-provenance`）：`HB` ＝ 手冊附表 25 之逐格（`ops/queue` 之 `參考/市地重劃作業手冊.txt`
第 4053、4062〜4078 列〔附表 25·手冊頁 119·列號依 `grep -n`〕之逐字·與出圖線 `W-P.003` 之 `RW_TABLE` 逐格同）；整數公尺之值與手冊第 3029〜3035 列
之簡表（附件二·一位小數）四捨五入一致（17 格皆同）。

子命令（一律 python3 verify/probes/probe_WG9398_rw25.py <子命令> …）：
  selftest <repo>
           `harvest(app.py)` 取 `rw_from_width`、`rw_increment`、`_solve_G_one`、`alloc_normal_axis`（⛔ 讀本案資料）。
           T1 格點：W ＝ (10k ＋ j)／10（k ＝ 1〜17、j ＝ 0〜9）之 170 格與 W ＝ 18 ⇒ |R − HB| ≤ 1e-9（不合之格數 ＝ 0）；
           T2 格間：每一格間（170）之 1／4、1／2、3／4 處 ⇒ |R − 二端之線性內插| ≤ 1e-9；
           T3 KL 所見之請示表（監看窗 `2026-10-25 17:0x`）：5.30 ⇒ 45.85、5.35 ⇒ 46.15、7.00 ⇒ 55.69；
           T4 起點與 0〜1 m：R(0) ＝ 0、R(−1) ＝ 0、R(None) ＝ 0、R(0.25) ＝ 4.34、R(0.5) ＝ 8.68、R(0.999999) 與 R(1) 之差 ≤ 1e-4；
           T5 飽和：R(18) ＝ R(18.0001) ＝ R(25) ＝ R(1e6) ＝ 100、R(17.95) ＝ 99.875、R(17.9999) 與 100 之差 ≤ 1e-3；
           T6 格點之浮點之鄰：W ＝ 5.3 ± 1e-12、0.1 × 53（＝ 5.300000000000001）、2.7 ＋ 2.6 ⇒ |R − 45.85| ≤ 1e-9；
           T7 連續與不減：W ＝ 0〜18.5 每 0.0007 m（整數步）⇒ 相鄰二值不減、其差 ≤ 0.02（無跳躍）；
           T8 累積差額：`rw_increment` 之鏈 W ＝ 0 → 4.2 → 9.7 → 13.05 → 18.3 ⇒ 0.3905、0.3063、0.14545、0.15775（|差| ≤ 1e-12）、
              其和 ＝ 1；W 倒退（9.7 → 4.2）⇒ 0；
           T9 玩具街廓（左右二側 × 二座標系〔原座標；旋轉 37°、鏡射、移至 TWD97 之尺度〕× 二 a）之街角第 1 宗與第 2 宗：
              `_solve_G_one` 之 G 取至 2 位 ＝ 發單端以 HB 自解之不動點（矩形 D ＝ 20、正面長 60、SIDE_LINE ⟂ 正面 ⇒ W ＝ S〔第 1 宗〕、
              W ＝ S₁ ＋ S₂〔第 2 宗〕；`D·S ＝ (a(1−A·B) − ΔR·F·l₁／100 − S·l₂)(1−C)`·二分至 1e-12）；其 16 解皆同而與「舊表」
              〔附件二之簡表之整數公尺一位小數·線性內插〕之自解至少一解異、且 HB 之自解皆距半分（0.005 之奇數倍）≥ 0.001（判別與捨入之前提·⛔ 恆綠）。
           P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           X1 `app.py` 之頂層之名之增恰 `{RW_TABLE_25}`、無減；頂層節點之相異 ＝ `{RW_TABLE_25, rw_from_width}`；
           X2 `RW_TABLE_25` ＝ 17 列 × 10 之數之字面（tuple 或 list·AST 之字面）而逐格 ＝ HB；
           X3 `rw_from_width` 讀 `RW_TABLE_25` 與 `RW_SATURATION_WIDTH_M`，其內⛔ 有附表 25 或簡表之值之數之常數（1 ＜ x ＜ 100 而取至
              2 位 ∈ 二表之值者 ＝ 0 個）、⛔ 有數之串（X5 之式）；
           X4 `rw_increment`、`RW_SATURATION_WIDTH_M` 之節點對基準⛔ 變；
           X5 生產碼（`app.py` 與 `verify/` 頂層之 `*.py`）中，`RW_TABLE_25` 以外⛔ 有附表 25 或簡表之數之字面之串（連續 ≥ 5 個之數之
              常數而其中 ≥ 3 個 ∈ HB 或簡表之值者 ＝ 0 處）；
           X6 新增或改之頂層節點內⛔ 新增案件字面；
           X7 `verify/` 頂層之 `*.py`（生產碼）對基準相異 ＝ 0。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")

# 手冊附表 25（街角地側面道路負擔百分率累積表·頁 119）之逐格：列 ＝ 整數公尺 1〜17，欄 ＝ 小數第一位 0〜9；18 m ＝ 100.00
HB = {
    1: (17.36, 18.08, 18.80, 19.52, 20.23, 20.94, 21.64, 22.35, 23.05, 23.75),
    2: (24.44, 25.14, 25.83, 26.52, 27.20, 27.88, 28.56, 29.24, 29.91, 30.58),
    3: (31.25, 31.92, 32.58, 33.24, 33.89, 34.55, 35.20, 35.85, 36.49, 37.14),
    4: (37.78, 38.42, 39.05, 39.68, 40.31, 40.94, 41.56, 42.18, 42.80, 43.42),
    5: (44.03, 44.64, 45.24, 45.85, 46.45, 47.05, 47.64, 48.24, 48.83, 49.42),
    6: (50.00, 50.58, 51.16, 51.74, 52.31, 52.88, 53.45, 54.02, 54.58, 55.14),
    7: (55.69, 56.25, 56.80, 57.35, 57.89, 58.44, 58.98, 59.52, 60.05, 60.58),
    8: (61.11, 61.64, 62.16, 62.68, 63.20, 63.72, 64.23, 64.74, 65.24, 65.75),
    9: (66.25, 66.75, 67.24, 67.74, 68.23, 68.72, 69.20, 69.68, 70.16, 70.64),
    10: (71.11, 71.58, 72.05, 72.52, 72.98, 73.44, 73.89, 74.35, 74.80, 75.25),
    11: (75.69, 76.14, 76.58, 77.02, 77.45, 77.88, 78.31, 78.74, 79.16, 79.58),
    12: (80.00, 80.42, 80.83, 81.24, 81.64, 82.05, 82.45, 82.85, 83.24, 83.64),
    13: (84.03, 84.42, 84.80, 85.18, 85.56, 85.94, 86.31, 86.68, 87.05, 87.42),
    14: (87.78, 88.14, 88.49, 88.85, 89.20, 89.55, 89.89, 90.24, 90.58, 90.92),
    15: (91.25, 91.59, 91.91, 92.24, 92.56, 92.88, 93.20, 93.52, 93.83, 94.14),
    16: (94.44, 94.75, 95.05, 95.35, 95.64, 95.94, 96.23, 96.52, 96.80, 97.08),
    17: (97.36, 97.64, 97.91, 98.18, 98.45, 98.72, 98.98, 99.24, 99.49, 99.75),
}
# 附件二之簡表（手冊第 3029〜3035 列·整數公尺·一位小數）：判別之前提之「舊表」與 X5 之受詞
SIMPLE = (0.0, 17.4, 24.4, 31.3, 37.8, 44.0, 50.0, 55.7, 61.1, 66.3, 71.1, 75.7, 80.0, 84.0, 87.8, 91.3, 94.4, 97.4, 100.0)


def _grid(i):
    """格點 i（W ＝ i／10·i ＝ 10〜180）之 HB 值。"""
    return 100.0 if i >= 180 else HB[i // 10][i % 10]


def hb_R(W):
    """發單端之獨立之模型（期值之源）：附表 25 之格點與格間之線性內插；0〜1 m 自 (0, 0) 內插；≥ 18 ⇒ 100。"""
    W = float(W)
    if W <= 0:
        return 0.0
    if W >= 18.0:
        return 100.0
    if W < 1.0:
        return HB[1][0] * W
    i = int(math.floor(W * 10.0 + 1e-9))
    f = W * 10.0 - i
    if abs(f) <= 1e-9:
        return _grid(i)
    return _grid(i) + (_grid(i + 1) - _grid(i)) * f


def old_R(W):
    W = float(W)
    if W <= 0:
        return 0.0
    if W >= 18.0:
        return 100.0
    i = int(W)
    return SIMPLE[i] + (SIMPLE[i + 1] - SIMPLE[i]) * (W - i)


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


# ───────────────────────── selftest ─────────────────────────

def _xf(ang_deg, mirror, tx, ty):
    import numpy as np
    c, s = math.cos(math.radians(ang_deg)), math.sin(math.radians(ang_deg))

    def f(p):
        x, y = float(p[0]), float(p[1])
        if mirror:
            x = -x
        return np.array((c * x - s * y + tx, s * x + c * y + ty))

    def v(d):
        x, y = float(d[0]), float(d[1])
        if mirror:
            x = -x
        return np.array((c * x - s * y, s * x + c * y))
    return f, v


_L, _D, _A, _B, _C, _LF, _LS, _F = 60.0, 20.0, 1.2, 0.3, 0.25, 6.0, 4.0, 20.0


def _fix(a, s0, R):
    """玩具之不動點：D·S ＝ (a(1−A·B) − (R(s0＋S) − R(s0))·F·l₁／100 − S·l₂)(1−C)·二分至 1e-12（⛔ 由受測之碼產）。"""
    lo, hi = 0.0, _L - s0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        rhs = (a * (1 - _A * _B) - (R(s0 + m) - R(s0)) * _F * _LS / 100.0 - m * _LF) * (1 - _C)
        if _D * m > rhs:
            hi = m
        else:
            lo = m
    s = 0.5 * (lo + hi)
    return _D * s, s


def _toy(ns):
    """T9：街角第 1 宗與第 2 宗（左右二側 × 二座標系 × 二 a）之 `_solve_G_one` 對 HB 之自解。"""
    import numpy as np
    from shapely.geometry import Polygon
    import streamlit as _st9
    got, exp_new, exp_old, mg = [], [], [], 1.0
    for fr in (_xf(0, False, 0.0, 0.0), _xf(37, True, 307123.4, 2654321.7)):
        f, v = fr
        poly = Polygon([f(p) for p in [(0, 0), (_L, 0), (_L, _D), (0, _D)]])
        dh = np.array(v((1, 0)), dtype=float)
        ad = ns["alloc_normal_axis"](v((0, 1)))
        for side in ("左", "右"):
            x = 0.0 if side == "左" else _L
            sd = {"p1": f((x, 0.0)), "p2": f((x, _D)), "mid": f((x, _D / 2.0))}
            _st9.session_state["f3_cad_side_lines_by_side"] = {"GT": {"left" if side == "左" else "right": sd}}
            mid = np.array(sd["mid"], dtype=float)
            d_use = dh if side == "左" else -dh
            for a1, a2 in ((159.1, 141.7), (231.9, 118.0)):
                base = np.array(f((x, 0.0)), dtype=float)
                r1, _ = ns["_solve_G_one"](a_m2=a1, A=_A, l_front=_LF, l_side=_LS, F=_F, blk_poly=poly, d_hat=d_use,
                                           baseline_pt=base, S_max=_L, is_corner=True, side=side + "側", avg_depth=_D,
                                           B=_B, C=_C, tab6_burden=_B + _C, allocation_dir=ad, side_mid=mid,
                                           W_prev=0.0, near_dir=None, w0_start=0.0, is_chain_head=True, s_back=0.0)
                s1 = float(r1["S_raw"]) if r1.get("S_raw") is not None else float(r1["S"])
                b2 = base + s1 * d_use
                r2, _ = ns["_solve_G_one"](a_m2=a2, A=_A, l_front=_LF, l_side=_LS, F=_F, blk_poly=poly, d_hat=d_use,
                                           baseline_pt=b2, S_max=_L - s1, is_corner=False, side=side + "側",
                                           avg_depth=_D, B=_B, C=_C, tab6_burden=_B + _C, allocation_dir=ad,
                                           side_mid=mid, W_prev=s1, near_dir=r1.get("_alloc_dir_used"),
                                           w0_start=None, is_chain_head=False, s_back=0.0)
                g1n, s1n = _fix(a1, 0.0, hb_R)
                g2n, _ = _fix(a2, s1n, hb_R)
                mg = min([mg] + [abs((g * 100.0) % 1.0 - 0.5) / 100.0 for g in (g1n, g2n)])
                g1o, s1o = _fix(a1, 0.0, old_R)
                g2o, _ = _fix(a2, s1o, old_R)
                got += [round(float(r1["G"]), 2), round(float(r2["G"]), 2)]
                exp_new += [round(g1n, 2), round(g2n, 2)]
                exp_old += [round(g1o, 2), round(g2o, 2)]
    _st9.session_state.pop("f3_cad_side_lines_by_side", None)
    return got, exp_new, exp_old, mg


def selftest(repo):
    ns, _ = _harvest(repo)
    need = ["rw_from_width", "rw_increment", "_solve_G_one", "alloc_normal_axis"]
    miss = [n for n in need if n not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    R, RI = ns["rw_from_width"], ns["rw_increment"]
    C = []
    t1 = [(i, R(i / 10.0)) for i in range(10, 181) if abs(R(i / 10.0) - _grid(i)) > 1e-9]
    C.append(("T1 格點 171（1.0〜18.0 m 每 0.1 m）＝ 附表 25", (len(t1), t1[:3]), (0, [])))
    t2 = []
    for i in range(10, 180):
        for q in (0.25, 0.5, 0.75):
            w = (i + q) / 10.0
            e = _grid(i) + (_grid(i + 1) - _grid(i)) * q
            if abs(R(w) - e) > 1e-9:
                t2.append((round(w, 4), R(w), e))
    C.append(("T2 格間 170 × 3 處 ＝ 二端之線性內插（公分以下用內插法）", (len(t2), t2[:3]), (0, [])))
    C.append(("T3 請示表：5.30 ⇒ 45.85、5.35 ⇒ 46.15、7.00 ⇒ 55.69",
              tuple(abs(R(w) - e) <= 1e-9 for w, e in ((5.30, 45.85), (5.35, 46.15), (7.00, 55.69))), (True,) * 3))
    C.append(("T4 起點 0 與 0〜1 m（自 (0, 0) 至 (1.0, 17.36) 線性）",
              (R(0.0), R(-1.0), R(None), abs(R(0.25) - 4.34) <= 1e-9, abs(R(0.5) - 8.68) <= 1e-9,
               abs(R(0.999999) - R(1.0)) <= 1e-4), (0.0, 0.0, 0.0, True, True, True)))
    C.append(("T5 飽和：≥ 18 m ＝ 100；17.95 ⇒ 99.875",
              (R(18.0), R(18.0001), R(25.0), R(1e6), abs(R(17.95) - 99.875) <= 1e-9, abs(R(17.9999) - 100.0) <= 1e-3),
              (100.0, 100.0, 100.0, 100.0, True, True)))
    C.append(("T6 格點之浮點之鄰（5.3 ± 1e-12、0.1×53、2.7＋2.6）⇒ 45.85",
              tuple(abs(R(w) - 45.85) <= 1e-9 for w in (5.3 + 1e-12, 5.3 - 1e-12, 0.1 * 53, 2.7 + 2.6)), (True,) * 4))
    vals = [R(k * 0.0007) for k in range(0, int(18.5 / 0.0007) + 1)]
    dec = sum(1 for a, b in zip(vals, vals[1:]) if b < a - 1e-12)
    jmp = max(b - a for a, b in zip(vals, vals[1:]))
    C.append(("T7 0〜18.5 m 每 0.0007 m：不減、相鄰之差 ≤ 0.02", (dec, jmp <= 0.02), (0, True)))
    ch = (0.0, 4.2, 9.7, 13.05, 18.3)
    inc = [RI(a, b) for a, b in zip(ch, ch[1:])]
    exp8 = (0.3905, 0.3063, 0.14545, 0.15775)
    C.append(("T8 累積差額之鏈 0→4.2→9.7→13.05→18.3 與倒退",
              (tuple(abs(x - e) <= 1e-12 for x, e in zip(inc, exp8)), abs(sum(inc) - 1.0) <= 1e-12, RI(9.7, 4.2)),
              ((True,) * 4, True, 0.0)))
    got, en, eo, mg = _toy(ns)
    C.append(("T9 玩具街廓之街角第 1、2 宗（左右 × 二座標系 × 二 a）＝ HB 之自解；舊表之自解至少一異；自解距半分 ≥ 0.001",
              (len(got), [(k, g, e) for k, (g, e) in enumerate(zip(got, en)) if g != e], en != eo, mg >= 0.001),
              (16, [], True, True)))
    red = []
    for name, g, e in C:
        ok = g == e
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {g!r}"[:700])
            print(f"       期 {e!r}"[:700])
            red.append(name.split()[0])
    print(f"  ℹ️ T9 之解（HB）{en}")
    print(f"  ℹ️ T9 之解（舊表）{eo}")
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


def _top(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            out[n.name] = n
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = n
    return out


def _nums(node):
    return [c.value for c in ast.walk(node) if isinstance(c, ast.Constant) and type(c.value) in (int, float)]


_TBLV = {round(x, 2) for r in HB.values() for x in r} | {round(x, 1) for x in SIMPLE[1:-1]}


def _runs(tree):
    """連續 ≥ 5 個之數之常數（list／tuple 之元素）而其中 ≥ 3 個屬附表 25 或簡表之值者之處。"""
    out = []
    for n in ast.walk(tree):
        if isinstance(n, (ast.List, ast.Tuple)):
            xs = [e.value for e in n.elts if isinstance(e, ast.Constant) and type(e.value) in (int, float)]
            if len(xs) >= 5 and sum(1 for x in xs if round(float(x), 2) in _TBLV and float(x) > 1.0) >= 3:
                out.append((getattr(n, "lineno", 0), len(xs)))
    return out


def wiring(repo, base):
    old = _git(repo, "show", f"{base}:app.py")
    if not old:
        print(f"  🔴 基準 {base} 之 app.py 取不到")
        print("⇒ 紅 ['基準缺']；rc 1")
        return 1
    src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    to, tn = ast.parse(old), ast.parse(src)
    mo, mn = _top(to), _top(tn)
    do = {k: ast.dump(v) for k, v in mo.items()}
    dn = {k: ast.dump(v) for k, v in mn.items()}
    red = []
    add, rem = set(dn) - set(do), set(do) - set(dn)
    chg = {k for k in dn if dn.get(k) != do.get(k)}
    ok1 = add == {"RW_TABLE_25"} and not rem and chg == {"RW_TABLE_25", "rw_from_width"}
    print(("  ✅" if ok1 else "  🔴") + f" X1 頂層之名之增 {sorted(add)}·減 {sorted(rem)}·相異之節點 {sorted(chg)}")
    if not ok1:
        red.append("X1")
    tbl = mn.get("RW_TABLE_25")
    ok2, why2 = False, "缺"
    if isinstance(tbl, ast.Assign):
        try:
            val = ast.literal_eval(tbl.value)
            rows = [tuple(float(x) for x in r) for r in val]
            ok2 = (isinstance(tbl.value, (ast.Tuple, ast.List)) and len(rows) == 17
                   and all(len(r) == 10 for r in rows)
                   and all(abs(rows[k - 1][j] - HB[k][j]) <= 1e-12 for k in range(1, 18) for j in range(10)))
            why2 = f"列 {len(rows)}"
        except Exception as e:  # noqa: BLE001
            why2 = f"非字面（{type(e).__name__}）"
    print(("  ✅" if ok2 else "  🔴") + f" X2 RW_TABLE_25 ＝ 17 × 10 之字面而逐格 ＝ 附表 25（{why2}）")
    if not ok2:
        red.append("X2")
    fn = mn.get("rw_from_width")
    names = {x.id for x in ast.walk(fn) if isinstance(x, ast.Name)} if fn is not None else set()
    big = ([x for x in _nums(fn) if 1.0 < float(x) < 100.0 and round(float(x), 2) in _TBLV] + _runs(fn)
           if fn is not None else ["缺"])
    ok3 = {"RW_TABLE_25", "RW_SATURATION_WIDTH_M"} <= names and not big
    print(("  ✅" if ok3 else "  🔴") + f" X3 rw_from_width 讀 RW_TABLE_25／RW_SATURATION_WIDTH_M·其內表之值之數之常數 {big[:5]}")
    if not ok3:
        red.append("X3")
    ok4 = all(dn.get(k) == do.get(k) and k in dn for k in ("rw_increment", "RW_SATURATION_WIDTH_M"))
    print(("  ✅" if ok4 else "  🔴") + " X4 rw_increment、RW_SATURATION_WIDTH_M 之節點⛔ 變")
    if not ok4:
        red.append("X4")
    hits = []
    prod = ["app.py"] + sorted("verify/" + f for f in os.listdir(os.path.join(repo, "verify"))
                               if f.endswith(".py"))
    for p in prod:
        t = tn if p == "app.py" else ast.parse(open(os.path.join(repo, p), encoding="utf-8").read())
        tl = {getattr(tbl, "lineno", -1)} if p == "app.py" else set()
        for ln, k in _runs(t):
            if p == "app.py" and tbl is not None and tbl.lineno <= ln <= tbl.end_lineno:
                continue
            hits.append((p, ln, k))
    ok5 = not hits
    print(("  ✅" if ok5 else "  🔴") + f" X5 RW_TABLE_25 以外之表之數之串（生產碼 {len(prod)} 檔）{hits[:5]}")
    if not ok5:
        red.append("X5")
    lits = []
    for k in sorted(chg):
        newc = {c.value for c in ast.walk(mn[k]) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                and CASE_LIT_RE.match(c.value)}
        oldc = ({c.value for c in ast.walk(mo[k]) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                 and CASE_LIT_RE.match(c.value)} if k in mo else set())
        lits += sorted((k, x) for x in newc - oldc)
    ok6 = not lits
    print(("  ✅" if ok6 else "  🔴") + f" X6 新增或改之頂層節點內新增之案件字面 {lits}")
    if not ok6:
        red.append("X6")
    dv = [x for x in _git(repo, "diff", "--name-only", base, "--", "verify/").split("\n")
          if x and re.match(r"^verify/[^/]+\.py$", x)]
    ok7 = not dv
    print(("  ✅" if ok7 else "  🔴") + f" X7 verify/ 頂層之 *.py 對基準之相異 {dv}")
    if not ok7:
        red.append("X7")
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
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
