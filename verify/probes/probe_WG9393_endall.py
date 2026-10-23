# -*- coding: utf-8 -*-
"""W-G.9-393 量測器（發單端擬·檔 F37·⛔ 由受單側改一字）：無側街之端一律為末端塊（KL `2026-10-23 07:39`（二）「是」·
`K-9-31`·既裁 `2026-07-17`、`08-03`、`09-17`、`10-06` 之合讀）——⛔ 以「未臨正街之三角地」為要件。

所量之性質：街廓之一端無 SIDE_LINE ⇒ 該端為末端塊（評選、落位、範圍之相接之查、調配池之末端保留皆及之），不論該端之
未臨正街（左 ＝ block∩{s<0}、右 ＝ block∩{s>s(p2)}）之有無；未臨正街 ≤ `END_BLOCK_UNFRONT_EPS`（無三角地）者其 `R_end`
＝ 末端帶（自該端之 FRONT 端點 ∥ 宗地分配線、⊥垂距 畸零地寬〔有最小建築面積之輸入者擴大之·`K-9-80` ④〕之帶 ∩ 街廓）、
`s_back` ＝ `0`；有三角地者照舊（`R_end` ＝ 未臨正街 ∪ 末端帶）。

子命令（一律 python3 verify/probes/probe_WG9393_endall.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式·期值皆手算）。玩具街廓：FRONT 沿 x 軸 p1 ＝ (0,0) → p2 ＝ (40,0)、
           宗地分配線 ∥ y 軸、深 30、畸零地寬 3.5。
           T1 左端無三角地（矩形 x∈[0,40]）⇒ gate 真、未臨正街 0、s_back 0、末端帶 105 ＝ R_end 105（R_end 與末端帶之對稱差 0）、buf 3.5；
           T2 右端無三角地（同一矩形）⇒ 同 T1（buf 3.5）；
           T3a／T3b 門檻之下：左端外斜之三角地 0.0005、0.000999 ㎡（≤ ε）⇒ 無三角地之讀（s_back 0·R_end ＝ 末端帶 105）；
           T4a／T4b 門檻之上：0.001001、0.002 ㎡（＞ ε）⇒ 有三角地（s_back ＞ 0·R_end − 末端帶 ＝ 未臨正街）；
           T5 有三角地（左端外斜 3 m·未臨正街 45）⇒ (45, 3, R_end 150, 末端帶 105)（舊之形·⛔ 變）；
           T6 端之界線內斜（x 自 0 斜至 2·街廓之後緣較短）⇒ gate 真、s_back 0、R_end ＝ 末端帶 ＝ 75（梯形·手算 3.5·30 − 2·30／2）；
           T7 有最小建築面積 150（T1 之矩形·左端）⇒ R_end ＝ 末端帶、面積 ∈ [150, 150 ＋ K980_AREA_TOL]、其帶寬 5（手算 150／30）；
           T8 換名、鏡射、旋轉 37°、移至 TWD97 之尺度：T1／T6／T7 之量（面積、s_back）皆同（容差 1e-6）；
           T9 `end_block_apply`：左無側街、右有 ⇒ 左之紀錄「觸發」真、R_end 105、當選 ＝ 跨占 R_end 而首個 G ≥ 105 之宗（替身之試算）、
              右 ⇒ 無紀錄；二端皆無側街 ⇒ 二端皆有紀錄與當選；
           T10 `_place_pool_parcels` 之末端保留（無三角地·`verify/fixture_end_reserve.py` 之幾何而 F ＝ 0）：左無側街 ⇒ 池窗之起點
              0 → 3.5；右無側街 ⇒ 池窗之寬 40 → 36.5（有側街者皆不動）；
           T11 短街廓（長 6）二端皆無側街 ⇒ 二末端帶相疊 ⇒ `k980_range_touch_check` 停機（`K-9-80` ⑥）；長 40 ⇒ 過。
           T12 二端皆無側街而一筆同時跨占二端之 R_end（長 20·寬 18 之宗）⇒ 停機（`GB-207`·`K-9-60` ① 未落地·`K6_PROGRAM_STOPS`
               增恰一而全文同）；T12b 一宗之街廓 ⇒ 同；T12c 無同時跨占者 ⇒ 過。
           （判別力之證 ＝ 單之突變之表〔發單端施於其原型〕與主線 `cf1b415` 之紅·本器⛔ 含突變〔其錨將繫於受單側之碼之字面〕。）
  wiring   <repo> <基準 commit>
           W1 `end_block_side_geom` 內⛔ 有 `'gate': False` 之回傳；
           W2 `_place_pool_parcels` 內⛔ 有「判式含 `_unfront` 而其體含 `continue`」之 `if`，且引 `END_BLOCK_UNFRONT_EPS`
              （⛔ 寫死 `1e-3`）；
           W3 `_end_region_R`、`end_block_band_width` 內⛔ 有「frag_poly 空」之停機；
           W4 `end_block_apply` 內⛔ 有 `'gate'` 之字面（未觸發之支去之）；
           W5 `app.py` 之頂層之名⛔ 增減；頂層節點之相異 ＝ `{end_block_side_geom, _end_region_R, end_block_band_width,
              _place_pool_parcels, end_block_apply}`；
           W6 新增或改之頂層節點內⛔ 新增案件字面；
           W7 `verify/` 頂層之 `*.py`（含 `verify/wf_f4.py`、`verify/stepg_pipeline.py`、`verify/selection_pipeline.py`）對基準相異 0；
           W8 `END_BLOCK_UNFRONT_EPS` ＝ 1e-3（⛔ 變）；
           W9 `end_block_apply` 內 `raise k6_program_stop(…)` 而其訊息含「GB-207」者恰一（試算之內亦上拋·`W-G.9-389`）。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`·段三之入口 `run_corner_pk_k6b` ＋ `run_step_g`）之末端塊之評選之紀錄
           （`SS_END_BLOCK_EVAL`）：
           R1 紀錄之「觸發」皆真（⛔ 有未觸發之端）、觸發之端之數 ＝ 4；
           R2 R_end（㎡）：`R2` 右 154.49、`R3` 左 153.77、`R5` 右 167.54（`K-6` 典 `W-G.9-392` 之節之六·發單端之實量）、
              `R6` 左 252.28（`K-6` 典 `W-G.9-352` 之節之「本案之量」）；
           R3 當選者：`R2` 右 `628-34(1)`、`R3` 左 `628-34(2)`、`R5` 右 `628-23(2)`（同 R2 之源）、`R6` 左 `628-4(1)`（同）；
           R4 終態之配地之列：各觸發之端之鏈首之宗（該側之列之首）＝ 其當選者；`err` 為 None。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, copy, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
FRAG_EMPTY = "frag_poly" + " 空"          # 舊之停機之訊息之子字串（以二常數之和書之·⛔ 為 F23／F24 之字樣之錨）
CHG_TOP = {"end_block_side_geom", "_end_region_R", "end_block_band_width", "_place_pool_parcels", "end_block_apply"}
MW, DEP, LEN = 3.5, 30.0, 40.0


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


ID = _xf(0, False, 0.0, 0.0)
FR = _xf(37, True, 307123.4, 2654321.7)


def _blk(pts, frame=ID):
    from shapely.geometry import Polygon
    f, v = frame
    return Polygon([f(p) for p in pts])


def _geom(ns, pts, side, frame=ID, mba=None, mw=MW):
    f, v = frame
    cad = v((0.0, 1.0))
    r = ns["end_block_side_geom"](_blk(pts, frame), v((1.0, 0.0)), f((0.0, 0.0)), f((LEN, 0.0)), cad,
                                  ns["alloc_normal_axis"](cad), mw, side, _label="T", min_build_area=mba)
    return r


def _q(r):
    """(gate, 未臨正街, s_back, R_end, 末端帶, R_end 與末端帶之差之面積, buf)，皆取至 6 位。"""
    if not r.get("gate"):
        return (False, round(float(r.get("unfront", 0.0)), 6))
    return (True, round(float(r["unfront"]), 6), round(float(r["s_back"]), 6), round(float(r["r_end_area"]), 6),
            round(float(r["band_area"]), 6), round(float(r["r_end_area"]) - float(r["band_area"]), 6),
            round(float(r["buf"]), 6))


RECT = [(0, 0), (LEN, 0), (LEN, DEP), (0, DEP)]


def _sliver(area):
    """左端外斜之三角地之面積 ＝ area（底 δ 於 y ＝ DEP·高 DEP ⇒ δ ＝ 2·area／DEP）。"""
    d = 2.0 * area / DEP
    return [(0, 0), (LEN, 0), (LEN, DEP), (-d, DEP)], d


def _tp(pid, coords):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(c) for c in coords]}


def _e(tp):
    return {"tp": tp, "pre_position": 0, "is_corner_winner": False, "side": "中段"}


def _apply(ns, has_left, has_right, Gv):
    import numpy as np
    seq = [_e(_tp("A(1)", [(0, 0), (2, 0), (2, DEP), (0, DEP)])), _e(_tp("B(1)", [(2, 0), (8, 0), (8, DEP), (2, DEP)])),
           _e(_tp("C(1)", [(8, 0), (30, 0), (30, DEP), (8, DEP)])), _e(_tp("D(1)", [(30, 0), (38, 0), (38, DEP), (30, DEP)])),
           _e(_tp("E(1)", [(38, 0), (LEN, 0), (LEN, DEP), (38, DEP)]))]
    blk = _blk(RECT)
    cad = (0.0, 1.0)
    cache = {}
    out, info = ns["end_block_apply"](
        seq, blk_label="BX", block_poly=blk, d_hat=np.array((1.0, 0.0)), corner_pt=np.array((0.0, 0.0)),
        front_p2=np.array((LEN, 0.0)), cad_alloc=cad, allocation_dir=ns["alloc_normal_axis"](cad), min_width=MW,
        has_side_pk={"left": has_left, "right": has_right}, has_side_cad={"left": has_left, "right": has_right},
        corner_range_polys={}, trial=lambda tp, s, w: (Gv[tp["暫編地號"]], 5.0), cache=cache)
    rec = cache.get("BX") or {}
    return ([x["tp"]["暫編地號"] for x in out],
            {sd: (bool(v.get("觸發")), v.get("R_end(㎡)"), v.get("當選")) for sd, v in sorted(rec.items())},
            {sd: (None if info[sd] is None else (info[sd]["winner"], round(info[sd]["s_back"], 6))) for sd in ("left", "right")})


def _both(ns, lots, length=20.0):
    """二端皆無側街之短街廓（長 `length`）：回 (過／停, 訊息之合或序, 登記之增)。"""
    import numpy as np
    blk = _blk([(0, 0), (length, 0), (length, DEP), (0, DEP)])
    seq = [_e(_tp(p, [(a, 0), (b, 0), (b, DEP), (a, DEP)])) for p, a, b in lots]
    cad = (0.0, 1.0)
    stops = ns["K6_PROGRAM_STOPS"]
    n0 = len(stops)
    try:
        out, _ = ns["end_block_apply"](
            seq, blk_label="BX", block_poly=blk, d_hat=np.array((1.0, 0.0)), corner_pt=np.array((0.0, 0.0)),
            front_p2=np.array((length, 0.0)), cad_alloc=cad, allocation_dir=ns["alloc_normal_axis"](cad), min_width=MW,
            has_side_pk={"left": False, "right": False}, has_side_cad={"left": False, "right": False},
            corner_range_polys={}, trial=lambda tp, s, w: (999.0, 5.0), cache={})
        return ("過", [x["tp"]["暫編地號"] for x in out], len(stops) - n0)
    except RuntimeError as e:
        m = str(e)
        return ("停", all(t in m for t in ("GB-207", "K-9-60 ①", lots[0][0])),
                (len(stops) - n0, bool(stops) and stops[-1] == m))


def _pool(ns, side, has_side):
    """`verify/fixture_end_reserve.py` 之幾何而 F ＝ 0（無三角地）：回 (池窗之起點 s, 池窗之寬)。"""
    import numpy as np
    H = 10.0
    blk = _blk([(0, 0), (LEN, 0), (LEN, H), (0, H)])
    rec = []

    def solve_one(_a, _A, _lf, _ls, _F, _bp_poly, _dh, _baseline_pt, _S_max,
                  _is_corner, _side, _depth, _allocation_dir=None, _side_mid=None, _W_prev=0.0):
        rec.append((np.asarray(_baseline_pt, dtype=float), float(_S_max)))
        return ({"G": 10.0, "area_geom": 10.0, "S": 1.0, "S_raw": 1.0, "W": 0.0, "W_far": 0.0, "Rw_pct": 0.0,
                 "cut_coords": [], "converged": True, "iterations": 1, "trace": []}, "stub")
    tp = {"暫編地號": "SYN-1", "配地階段": "池內", "面積_m2": 20.0, "重劃前地價區段": "z", "所屬街廓": "TEST"}
    adv = {"rows": [], "left_results": [], "right_results": [], "left_cum_S": 0.0, "right_cum_S": 0.0,
           "Wf_left": 0.0, "Wf_right": 0.0}
    cad = [0.0, 1.0]
    with contextlib.redirect_stdout(io.StringIO()):
        ns["_place_pool_parcels"](
            stage2_parcels=[tp], adv_final=adv, blk_poly=blk, blk_area=float(blk.area), blk_label="TEST",
            blk_vertices=list(blk.exterior.coords), blk_centroid=(blk.centroid.x, blk.centroid.y),
            d_hat=np.array([1.0, 0.0]), corner_pt=np.array([0.0, 0.0]), s_max_blk=LEN,
            allocation_dir=ns["alloc_normal_axis"](cad), alloc_dir_cad=cad, front_len=LEN, l_front=1.0, avg_depth=H,
            side_mid_left=None, side_mid_right=None, l_side_left=0.0, F_left=0.0, l_side_right=0.0, F_right=0.0,
            post_price=100.0, pre_price_by_zone={"z": 100.0}, solve_one=solve_one, build_g_row=lambda *a, **k: {},
            mark_zaling=lambda r: r, has_side_left=(has_side if side == "left" else True),
            has_side_right=(has_side if side == "right" else True), min_width=MW, s_front_p2=LEN, _verbose=False)
    if not rec:
        return ("未呼叫",)
    return (round(float(np.dot(rec[0][0], np.array([1.0, 0.0]))), 6), round(rec[0][1], 6))


def _touch(ns, length):
    import numpy as np
    blk = _blk([(0, 0), (length, 0), (length, DEP), (0, DEP)])
    cad = (0.0, 1.0)
    rg = {}
    for sd in ("left", "right"):
        r = ns["end_block_side_geom"](blk, np.array((1.0, 0.0)), np.array((0.0, 0.0)), np.array((length, 0.0)), cad,
                                      ns["alloc_normal_axis"](cad), MW, sd, _label="T")
        rg[("左端末端塊範圍" if sd == "left" else "右端末端塊範圍")] = r.get("r_end")
    try:
        ns["k980_range_touch_check"]("BX", rg)
        return "過"
    except RuntimeError:
        return "停"


NEED = ["end_block_side_geom", "_end_region_R", "end_block_band_width", "end_block_apply", "_place_pool_parcels",
            "k980_range_touch_check", "alloc_normal_axis", "END_BLOCK_UNFRONT_EPS", "K980_AREA_TOL",
            "K6_PROGRAM_STOPS"]

def _cases(ns):
    C = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:120])
        C.append((name, got, exp))

    band = MW * DEP
    run("T1 左端無三角地 ⇒ 末端塊（R_end ＝ 末端帶 105·s_back 0·buf 3.5）", lambda: _q(_geom(ns, RECT, "left")),
        (True, 0.0, 0.0, band, band, 0.0, MW))
    run("T2 右端無三角地 ⇒ 同 T1", lambda: _q(_geom(ns, RECT, "right")), (True, 0.0, 0.0, band, band, 0.0, MW))
    for tg, ar in (("T3a", 0.0005), ("T3b", 0.000999)):
        run(f"{tg} 門檻之下：三角地 {ar} ㎡ ⇒ 無三角地之讀（s_back 0·R_end ＝ 末端帶）",
            lambda ar=ar: (lambda r: (r[0], r[2], r[3], r[5]))(_q(_geom(ns, _sliver(ar)[0], "left"))),
            (True, 0.0, band, 0.0))
    for tg, ar in (("T4a", 0.001001), ("T4b", 0.002)):
        pts, d = _sliver(ar)
        run(f"{tg} 門檻之上：三角地 {ar} ㎡ ⇒ 有三角地（s_back ＝ δ·R_end − 末端帶 ＝ 未臨正街）",
            lambda pts=pts: (lambda r: (r[0], r[1], r[2], r[5]))(_q(_geom(ns, pts, "left"))),
            (True, round(ar, 6), round(d, 6), round(ar, 6)))
    run("T5 有三角地（外斜 3 m）⇒ 舊之形（未臨正街 45·s_back 3·R_end 150·末端帶 105）",
        lambda: _q(_geom(ns, [(0, 0), (LEN, 0), (LEN, DEP), (-3, DEP)], "left")),
        (True, 45.0, 3.0, 150.0, band, 45.0, MW))
    trap = MW * DEP - 2.0 * DEP / 2.0
    run("T6 端之界線內斜（後緣較短）⇒ 末端塊（R_end ＝ 末端帶 ＝ 75）",
        lambda: (lambda r: (r[0], r[1], r[2], r[3], r[5]))(_q(_geom(ns, [(0, 0), (LEN, 0), (LEN, DEP), (2, DEP)], "left"))),
        (True, 0.0, 0.0, trap, 0.0))
    tol = float(ns["K980_AREA_TOL"])

    def t7(frame=ID):
        r = _geom(ns, RECT, "left", frame=frame, mba=150.0)
        a = float(r["r_end_area"])
        return (bool(r["gate"]), 150.0 <= a <= 150.0 + tol, round(a - float(r["band_area"]), 6),
                round(float(r["s_back"]), 6), abs(float(r["buf"]) - 150.0 / DEP) <= 1e-4)
    run("T7 最小建築面積 150 ⇒ R_end ＝ 末端帶 ∈ [150, 150＋容差]·帶寬 5", t7, (True, True, 0.0, 0.0, True))

    def t8():
        a = [_q(_geom(ns, RECT, sd, frame=FR)) for sd in ("left", "right")]
        b = _q(_geom(ns, [(0, 0), (LEN, 0), (LEN, DEP), (2, DEP)], "left", frame=FR))
        c = t7(FR)
        return (all(abs(x[3] - band) <= 1e-6 and abs(x[2]) <= 1e-6 and x[0] for x in a),
                abs(b[3] - trap) <= 1e-6 and abs(b[2]) <= 1e-6, c)
    run("T8 鏡射、旋轉 37°、TWD97 之尺度 ⇒ T1／T2／T6／T7 之量同", t8, (True, True, (True, True, 0.0, 0.0, True)))
    Gv = {"A(1)": 50.0, "B(1)": 200.0, "C(1)": 900.0, "D(1)": 400.0, "E(1)": 50.0}
    run("T9 end_block_apply：左無側街 ⇒ 左觸發·R_end 105·當選 B(1)（A 未達）·落位首；右有側街 ⇒ 無紀錄",
        lambda: _apply(ns, False, True, Gv),
        (["B(1)", "A(1)", "C(1)", "D(1)", "E(1)"], {"left": (True, band, "B(1)")}, {"left": ("B(1)", 0.0), "right": None}))
    run("T9b 二端皆無側街 ⇒ 二端皆觸發（右：E(1) 未達、D(1) 當選而移至末）",
        lambda: _apply(ns, False, False, Gv),
        (["B(1)", "A(1)", "C(1)", "E(1)", "D(1)"], {"left": (True, band, "B(1)"), "right": (True, band, "D(1)")},
         {"left": ("B(1)", 0.0), "right": ("D(1)", 0.0)}))
    run("T12 二端皆無側街而一筆同時跨占二端之 R_end（長 20·A 寬 18）⇒ 停機（GB-207·K-9-60 ①·登記增恰一）",
        lambda: _both(ns, [("A(1)", 0, 18), ("B(1)", 18, 20)]), ("停", True, (1, True)))
    run("T12b 一宗之街廓（長 20）二端皆無側街 ⇒ 同 T12",
        lambda: _both(ns, [("A(1)", 0, 20)]), ("停", True, (1, True)))
    run("T12c 長 20 而無一筆同時跨占（A 寬 10、B 寬 10）⇒ 過（二端各當選）",
        lambda: _both(ns, [("A(1)", 0, 10), ("B(1)", 10, 20)]), ("過", ["A(1)", "B(1)"], 0))
    run("T10 末端保留（無三角地）：左無側街 ⇒ 池窗起點 0 → 3.5；有側街 ⇒ 0",
        lambda: (_pool(ns, "left", True)[0], _pool(ns, "left", False)[0]), (0.0, MW))
    run("T10b 末端保留（無三角地）：右無側街 ⇒ 池窗寬 40 → 36.5；有側街 ⇒ 40",
        lambda: (_pool(ns, "right", True)[1], _pool(ns, "right", False)[1]), (LEN, LEN - MW))
    run("T11 短街廓（長 6）二端之末端帶相疊 ⇒ 停機（K-9-80 ⑥）；長 40 ⇒ 過",
        lambda: (_touch(ns, 6.0), _touch(ns, LEN)), ("停", "過"))
    return C


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in NEED if n not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    C = _cases(ns)
    red = []
    for name, got, exp in C:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {got!r}"[:700])
            print(f"       期 {exp!r}"[:700])
            red.append(name.split()[0])
    red = sorted(set(red), key=red.index)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── wiring ─────────────────────────

def _git(repo, *a):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
    return r.stdout if r.returncode == 0 else None


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


def _strs(node):
    return [c.value for c in ast.walk(node) if isinstance(c, ast.Constant) and isinstance(c.value, str)]


def wiring(repo, base):
    src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    old_b = _git(repo, "show", f"{base}:app.py")
    if not old_b:
        print(f"  🔴 基準 {base} 之 app.py 取不到")
        print("⇒ 紅 ['基準缺']；rc 1")
        return 1
    old = old_b.decode("utf-8")
    ta = ast.parse(src)
    red = []

    def rep(tag, ok, msg):
        print(("  ✅" if ok else "  🔴") + f" {tag} {msg}")
        if not ok:
            red.append(tag)
    # W1
    sg = _fn_node(ta, "end_block_side_geom")
    bad1 = 0 if sg else -1
    if sg:
        for d in ast.walk(sg):
            if isinstance(d, ast.Dict):
                for k, v in zip(d.keys, d.values):
                    if isinstance(k, ast.Constant) and k.value == "gate" and isinstance(v, ast.Constant) and v.value is False:
                        bad1 += 1
    rep("W1", bad1 == 0, f"end_block_side_geom 之 'gate': False 之回傳 {bad1}")
    # W2
    pp = _fn_node(ta, "_place_pool_parcels")
    bad2, eps2, lit2 = -1, False, 0
    if pp:
        bad2 = 0
        for n in ast.walk(pp):
            if isinstance(n, ast.If) and any(isinstance(x, ast.Name) and x.id == "_unfront" for x in ast.walk(n.test)):
                if any(isinstance(x, ast.Continue) for b in n.body for x in ast.walk(b)):
                    bad2 += 1
                if any(isinstance(x, ast.Name) and x.id == "END_BLOCK_UNFRONT_EPS" for x in ast.walk(n.test)):
                    eps2 = True
                lit2 += sum(1 for x in ast.walk(n.test) if isinstance(x, ast.Constant) and x.value == 1e-3)
    rep("W2", bad2 == 0 and eps2 and lit2 == 0,
        f"_place_pool_parcels 之「_unfront 之判 ⇒ continue」{bad2}·引 END_BLOCK_UNFRONT_EPS {eps2}·寫死 1e-3 {lit2}")
    # W3
    bad3 = []
    for fn in ("_end_region_R", "end_block_band_width"):
        nd = _fn_node(ta, fn)
        if nd is None or any(FRAG_EMPTY in s for s in _strs(nd)):
            bad3.append(fn)
    rep("W3", not bad3, f"_end_region_R／end_block_band_width 之「frag_poly 空」之停機 {bad3}")
    # W4
    ea = _fn_node(ta, "end_block_apply")
    n4 = sum(1 for s in _strs(ea) if s == "gate") if ea else -1
    rep("W4", n4 == 0, f"end_block_apply 之 'gate' 之字面 {n4}")
    # W5
    tb, tn = _top(old), _top(src)
    add, rem = set(tn) - set(tb), set(tb) - set(tn)
    chg = {k for k in tn if k in tb and tn[k] != tb[k]}
    rep("W5", not add and not rem and chg == CHG_TOP, f"頂層之名之增 {sorted(add)}·減 {sorted(rem)}·相異之節點 {sorted(chg)}")
    # W6
    tbo = ast.parse(old)
    lits = []
    for nm in sorted(chg):
        nn, ob = _fn_node(ta, nm), _fn_node(tbo, nm)
        if nn is None:
            continue
        newc = {s for s in _strs(nn) if CASE_LIT_RE.match(s)}
        oldc = {s for s in _strs(ob) if CASE_LIT_RE.match(s)} if ob is not None else set()
        lits += sorted((nm, x) for x in newc - oldc)
    rep("W6", not lits, f"新增或改之頂層節點內新增之案件字面 {lits}")
    # W7
    vb = _git(repo, "ls-tree", "--name-only", base, "verify/")
    names = sorted(x for x in (vb or b"").decode("utf-8").split("\n") if x.endswith(".py"))
    diff7 = []
    for p in names:
        ob = _git(repo, "show", f"{base}:{p}")
        try:
            nb = open(os.path.join(repo, p), "rb").read()
        except OSError:
            nb = None
        if ob != nb:
            diff7.append(p)
    rep("W7", bool(names) and not diff7, f"verify/ 頂層之 *.py（{len(names)}）對基準相異 {diff7}")
    # W8
    eps = next((n.value.value for n in ta.body if isinstance(n, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == "END_BLOCK_UNFRONT_EPS" for t in n.targets)
        and isinstance(n.value, ast.Constant)), None)
    rep("W8", eps == 1e-3, f"END_BLOCK_UNFRONT_EPS ＝ {eps!r}")
    # W9
    n9 = -1
    if ea:
        n9 = sum(1 for n in ast.walk(ea) if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call)
                 and getattr(n.exc.func, "id", None) == "k6_program_stop"
                 and any("GB-207" in x for x in _strs(n.exc)))
    rep("W9", n9 == 1, f"end_block_apply 之 `raise k6_program_stop(…GB-207…)` {n9}（期 1）")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

# 本案之錨（⛔ 由受測之碼產）：`K-6` 典 `W-G.9-392` 之節之六（`R2` 右、`R3` 左、`R5` 右·發單端之實量·KL `2026-10-23 07:39`（二）
# 所確認之請示之表同值）與 `W-G.9-352` 之節之「本案之量」（`R6` 左）。二退縮同值。
ANCHOR = {("R2", "right"): (154.49, "628-34(1)"), ("R3", "left"): (153.77, "628-34(2)"),
          ("R5", "right"): (167.54, "628-23(2)"), ("R6", "left"): (252.28, "628-4(1)")}


def _one(repo, sb):
    probes = os.path.join(repo, "verify", "probes")
    if probes not in sys.path:
        sys.path.insert(0, probes)
    os.environ["WV_K6B_STAGE3"] = "on"
    import probe_WG9344_k6s3 as K
    ns, fst, snap, cb_by, cad, tp, bp, params = K._boot(repo, sb)
    import selection_pipeline as sp
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _o, wins, forced, _tp2, bp2 = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb,
                                                                   snapshot=snap)
    res = K._materialize(ns, fst, snap, cb_by, cad, params, tp, bp2, wins, forced, sb)
    ebv = copy.deepcopy(fst.session_state.get(ns["SS_END_BLOCK_EVAL"]) or {})
    return res, ebv


def run(repo, sbs):
    red = []
    for sb in sbs:
        try:
            res, ebv = _one(repo, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  🔴 R1@{sb} 例外 {type(e).__name__}：{str(e)[:200]}")
            red.append(f"R1@{sb}")
            continue
        recs = {(b, sd): v for b, e in ebv.items() for sd, v in (e or {}).items() if isinstance(v, dict)}
        untrig = sorted(k for k, v in recs.items() if not v.get("觸發"))
        trig = sorted(k for k, v in recs.items() if v.get("觸發"))
        ok1 = not untrig and len(trig) == 4
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb} 末端塊之紀錄：觸發 {trig}·未觸發 {untrig}")
        if not ok1:
            red.append(f"R1@{sb}")
        bad2 = [(k, (recs.get(k) or {}).get("R_end(㎡)"), a) for k, (a, _) in ANCHOR.items()
                if (recs.get(k) or {}).get("R_end(㎡)") != a]
        ok2 = not bad2
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb} R_end 之錨不合 {bad2}")
        if not ok2:
            red.append(f"R2@{sb}")
        bad3 = [(k, (recs.get(k) or {}).get("當選"), w) for k, (_, w) in ANCHOR.items()
                if (recs.get(k) or {}).get("當選") != w]
        ok3 = not bad3
        print(("  ✅" if ok3 else "  🔴") + f" R3@{sb} 當選者之錨不合 {bad3}")
        if not ok3:
            red.append(f"R3@{sb}")
        rows = res.get("rows") or []
        bad4 = []
        for (blk, sd), (_, w) in ANCHOR.items():
            grp = [r for r in rows if r.get("所屬街廓") == blk and r.get("推進側別") == sd]
            head = grp[0]["暫編地號"] if grp else None
            if head != w:
                bad4.append((blk, sd, head, w))
        ok4 = not bad4 and res.get("err") is None
        print(("  ✅" if ok4 else "  🔴") + f" R4@{sb} 觸發之端之鏈首 ＝ 當選者（不合 {bad4}·err {res.get('err')}）")
        if not ok4:
            red.append(f"R4@{sb}")
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
