# -*- coding: utf-8 -*-
"""W-G.9-392 量測器（發單端擬·檔 F36·⛔ 由受單側改一字）：每宗之應分配面積之試算至穩定（`K-9-80` ③·KL `2026-10-22 05:22`
「甲」）與取得之宗（街角第 1 宗、末端塊之當選者）之自我檢查。

所量之性質：G 之二分求解收斂至 `K980_G_TOL`（㎡）後取至小數 2 位 ⇒ 其值⛔ 依二分之上界（`S_max`）而異（評選與實配之二次
所算同值）；取得之宗於實配之末趟（`_commit`）以評選之式重算之值與實配之值取至 2 位不同 ⇒ 停機（`GB-206`·經
`k6_program_stop` 登記·試算之內亦上拋·⛔ 靜默取其一）。

子命令（一律 python3 verify/probes/probe_WG9392_k980g.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式）。玩具街廓 GA：矩形 x∈[0,60]、y∈[0,D]，正面 y ＝ 0、宗地分配線 ∥ y 軸，
           無側街（`Rw` ＝ 0）⇒ 宗地之面積 ＝ `S·D`，法定式 `G ＝ (a(1−A·B) − S·l₂)(1−C)` 之不動點有解析解：
           `S* ＝ a(1−A·B)(1−C) ／ (D ＋ l₂(1−C))`、`G* ＝ D·S*`（期值之源·⛔ 由受測之碼產）。A ＝ 1.2、B ＝ 0.3、C ＝ 0.25。
           G1 D ＝ 15、l₂ ＝ 6、a ＝ 150 ＋ 1.37k（k ＝ 0〜299）：`_solve_G_one` 之 G 於二上界（街廓全長 60；`1.07·S* ＋ 0.31`）、
              二座標系（原座標；旋轉 37°、鏡射、移至 TWD97 之尺度）之四解皆 ＝ `round(G*, 2)`（G* 距 0.005 之倍數 ＜ 1e-4 者略之·其數記之·量 ≥ 270）；
           G2 同 G1 而 D ＝ 25、l₂ ＝ 2；
           G3 邊界：G* ＝ 某值之半分之上 ＋2e-5、之下 −2e-5（由 G* 反求 a）⇒ 四解皆 ＝ `round(G*, 2)`（進、捨各一）；
           G4 常數：`K980_G_TOL` ≤ 1e-6、`K980_G_MAX_ITER` ≥ 100。
           H1 `k980_acq_check` 二值同（307.78、307.78）⇒ 回 None、登記⛔ 增；H2 二值異（307.79、307.78）⇒ RuntimeError，訊息含
              「GB-206」「K-9-80 ③」與宗之暫編地號、二值，且 `K6_PROGRAM_STOPS` 增恰一（其全文 ＝ 訊息）；H3 未捨入異而取至 2 位同
              （307.7849、307.7751）⇒ None；H4 取至 2 位恰差 0.01（300.02、300.01·浮點之差 ≤ 0.01）⇒ 停；H5 末端塊、右側之形 ⇒
              停且訊息含「末端塊」「right」。
           E1 `end_block_trial_G` 之左端：以替身之 `solve_one` 錄其引數 ⇒ (a, A, l₂, 0, 0, 街廓, d̂, p1, max(0.1,S), False, '無', 深度)
              與 `_allocation_dir`、`_side_mid=None`、`_W_prev=0`、`_w0_start=0`、`_near_dir=None`、`_is_chain_head=True`、`_s_back`；
           E2 右端 ⇒ 方向 −d̂、起點 p1 ＋ S·d̂；E3 S ＝ 0.05 ⇒ 上界 0.1；E4 側別非 left／right ⇒ 停機；E5 回 (G, S_raw)。
           P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           W1 `_solve_G_one` 之 `solve_G_binary(` 之呼叫恰一，以 `tol=K980_G_TOL`、`max_iter=K980_G_MAX_ITER` 傳之；`app.py` 全檔之
              `solve_G_binary(` 之呼叫恰一；
           W2 `k980_acq_check(` 之呼叫：`f3_screen_stepg_run`（`app.py`）與 `_run_step_g_impl`（`verify/stepg_pipeline.py`）內各恰四
              （街角第 1 宗、末端塊 × 左、右），各在一 `if`／`elif` 之下而其判式含 `_commit`；街角之二之評選之值 ＝
              `_corner_first_lot_G(…)`、末端塊之二 ＝ `end_block_trial_G(…)[0]`；側別之字面 left／right 各二；
           W3 `end_block_host` 內 `end_block_trial_G(` 之呼叫恰一、`solve_one(` 之直呼為零；
           W4 `verify/stepg_pipeline.py` 經 `ns[…]` 取之新名皆在 `app.py` 之 `_WF_NS_NAMES`；
           W5 `app.py` 之頂層之名之增恰 `{K980_G_TOL, K980_G_MAX_ITER, end_block_trial_G, k980_acq_check}`、無減；
           W6 `k980_acq_check` 之內呼叫 `k6_program_stop` 且含字面「GB-206」；
           W7 新增或改之頂層節點內⛔ 新增案件字面。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`·段三之入口 `run_corner_pk_k6b` ＋ `run_step_g`）：
           R1 取得之宗之自我檢查之呼叫 ≥ 1（街角第 1 宗、末端塊各 ≥ 1）且皆過、⛔ 停機；評選（`_corner_first_lot_G` 之所錄）與
              終態之街角第 1 宗以（暫編地號、側、a）配對者皆同值（配對 ≥ 1）；末端塊之評選之紀錄之當選者之試算 G 與終態同（其 a 未變者·其數記之·本案之當選者皆已受同一地主之併入 ⇒ `0`·其一致由自我檢查之「末端塊」之呼叫量之）；
           R2 本案之錨（KL `2026-10-22 05:22` 所核之請示表〔`ops/queue` 之 `待KL/2026-10-22_街角地評選與實配之面積差.md`〕
              之「甲」之欄）：`628-18(1)` 307.78（二退縮）、`628-18(2)` 268.34（3.5 m）／259.13（0 m）、抵費地 R1 851.69、R3 1651.40、
              R4 697.39、R5 1221.45（3.5 m）／1221.46（0 m）、R6 980.58（二退縮）。
  diff     <pre.json> <post.json>
           `probe_WG9344_k6s3.py run` 之二落檔之逐欄之全比（⛔ 容差）：逐宗（街廓、暫編地號、推進之側）之 `a 面積(㎡)`、`G(㎡)`、
           `驗_總判`、`驗_宗序`、`歸戶`，抵費地之 `面積`、`容納內接矩形`，`wins`、`forced`、`dropped`、`err`；逐項出艙一列、末列
           `全比相異 <n> 項`（rc 0·其項之期由單定之）。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, copy, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
NEW_TOP = {"K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check"}
GB = "GB-206"


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


_A, _B, _C, _L = 1.2, 0.3, 0.25, 60.0


def _gstar(a, D, lf):
    s = a * (1 - _A * _B) * (1 - _C) / (D + lf * (1 - _C))
    return D * s, s


def _solve(ns, a, smax, frame, D, lf):
    from shapely.geometry import Polygon
    f, v = frame
    poly = Polygon([f(p) for p in [(0, 0), (_L, 0), (_L, D), (0, D)]])
    ad = ns["alloc_normal_axis"](v((0, 1)))
    r, _ = ns["_solve_G_one"](a_m2=a, A=_A, l_front=lf, l_side=0.0, F=0.0, blk_poly=poly, d_hat=v((1, 0)),
                              baseline_pt=f((0, 0)), S_max=smax, is_corner=False, side="左側", avg_depth=D, B=_B, C=_C,
                              tab6_burden=_B + _C, allocation_dir=ad, side_mid=None, W_prev=0.0, near_dir=None,
                              w0_start=0.0, is_chain_head=True, s_back=0.0)
    return float(r["G"])


def _sweep(ns, D, lf, avals):
    fr0 = _xf(0, False, 0.0, 0.0)
    fr1 = _xf(37, True, 307123.4, 2654321.7)
    bad, skip, n = [], 0, 0
    for a in avals:
        g, s = _gstar(a, D, lf)
        if abs(((g * 100.0) % 1.0) - 0.5) < 1e-2:      # G* 距 0.005 之倍數 ＜ 1e-4 ⇒ 略（期值之捨入不穩）
            skip += 1
            continue
        exp = round(g, 2)
        got = [_solve(ns, a, sm, fr, D, lf) for sm in (_L, 1.07 * s + 0.31) for fr in (fr0, fr1)]
        n += 1
        if any(x != exp for x in got):
            bad.append((round(a, 4), exp, got))
    return n, skip, bad


def selftest(repo):
    ns, _ = _harvest(repo)
    need = ["_solve_G_one", "k980_acq_check", "end_block_trial_G", "K980_G_TOL", "K980_G_MAX_ITER",
            "k6_program_stop", "K6_PROGRAM_STOPS", "alloc_normal_axis"]
    miss = [n for n in need if n not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    C = []
    av = [150.0 + 1.37 * k for k in range(300)]
    n1, sk1, b1 = _sweep(ns, 15.0, 6.0, av)
    C.append(("G1 D 15·l₂ 6：二上界 × 二座標系之 G ＝ round(G*, 2)", (n1 >= 270, b1[:3]), (True, [])))
    n2, sk2, b2 = _sweep(ns, 25.0, 2.0, av)
    C.append(("G2 D 25·l₂ 2：同 G1", (n2 >= 270, b2[:3]), (True, [])))
    g3 = []
    for base_, sgn in ((431.235, 1.0), (431.245, -1.0)):           # 半分之上（進）、之下（捨）
        gt = base_ + sgn * 2e-5
        a = gt / 15.0 * (15.0 + 6.0 * (1 - _C)) / ((1 - _A * _B) * (1 - _C))
        g, s = _gstar(a, 15.0, 6.0)
        fr1 = _xf(37, True, 307123.4, 2654321.7)
        got = [_solve(ns, a, sm, fr, 15.0, 6.0) for sm in (_L, 1.07 * s + 0.31) for fr in (_xf(0, False, 0, 0), fr1)]
        g3.append((round(g, 2), got))
    C.append(("G3 邊界：G* 於半分之上 2e-5 ⇒ 進、之下 2e-5 ⇒ 捨（四解皆同）",
              [(e, all(x == e for x in got)) for e, got in g3], [(431.24, True), (431.24, True)]))
    C.append(("G4 常數：K980_G_TOL ≤ 1e-6、K980_G_MAX_ITER ≥ 100",
              (float(ns["K980_G_TOL"]) <= 1e-6, int(ns["K980_G_MAX_ITER"]) >= 100), (True, True)))
    chk = ns["k980_acq_check"]
    stops = ns["K6_PROGRAM_STOPS"]

    def call(*a):
        n0 = len(stops)
        try:
            r = chk(*a)
            return ("過", r, len(stops) - n0, "")
        except RuntimeError as e:
            m = str(e)
            reg = (len(stops) - n0, (stops[-1] == m) if len(stops) > n0 else False)
            return ("停", None, reg, m)
    h1 = call("街角第1宗", "GA", "right", "X-1(1)", 307.78, 307.78)
    C.append(("H1 二值同 ⇒ 過（回 None·登記⛔ 增）", h1[:3], ("過", None, 0)))
    h2 = call("街角第1宗", "GA", "right", "X-1(1)", 307.79, 307.78)
    C.append(("H2 二值異 ⇒ 停（GB-206·K-9-80 ③·宗·二值·登記增恰一而全文同）",
              (h2[0], h2[2], all(t in h2[3] for t in (GB, "K-9-80 ③", "X-1(1)", "307.79", "307.78"))),
              ("停", (1, True), True)))
    h3 = call("街角第1宗", "GA", "left", "X-2(1)", 307.7849, 307.7751)
    C.append(("H3 取至 2 位同 ⇒ 過", h3[:3], ("過", None, 0)))
    h4 = call("街角第1宗", "GA", "left", "X-3(1)", 300.02, 300.01)
    C.append(("H4 取至 2 位恰差 0.01 ⇒ 停", (h4[0], h4[2]), ("停", (1, True))))
    h5 = call("末端塊", "GA", "right", "X-4(1)", 500.00, 500.01)
    C.append(("H5 末端塊·右 ⇒ 停（訊息含末端塊、right）", (h5[0], "末端塊" in h5[3], "right" in h5[3]), ("停", True, True)))
    import numpy as np
    rec = []

    def stub(*a, **k):
        rec.append((a, k))
        return ({"G": 123.456, "S_raw": 7.89, "S": 7.89}, "替身")
    tg = ns["end_block_trial_G"]
    d = np.array((0.6, 0.8)); p1 = np.array((307000.0, 2654000.0)); ad = np.array((-0.8, 0.6))
    rec.clear()
    r1 = tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 42.0, 18.0, ad, "left", 3.25)
    a1, k1 = rec[0]
    C.append(("E1 左端之引數", (a1[:5], a1[5], tuple(np.round(a1[6], 9)), tuple(np.round(a1[7], 6)), a1[8:],
                             (tuple(np.round(k1.get("_allocation_dir"), 9)), k1.get("_side_mid"), k1.get("_W_prev"),
                              k1.get("_w0_start"), k1.get("_near_dir"), k1.get("_is_chain_head"), k1.get("_s_back"))),
              ((321.5, 1.25, 0.7, 0.0, 0.0), "POLY", (0.6, 0.8), (307000.0, 2654000.0), (42.0, False, "無", 18.0),
               ((-0.8, 0.6), None, 0.0, 0.0, None, True, 3.25))))
    rec.clear()
    tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 42.0, 18.0, ad, "right", 0.0)
    a2, k2 = rec[0]
    C.append(("E2 右端：方向 −d̂、起點 p1 ＋ S·d̂", (tuple(np.round(a2[6], 9)), tuple(np.round(a2[7], 6)), k2.get("_s_back")),
              ((-0.6, -0.8), (307025.2, 2654033.6), 0.0)))
    rec.clear()
    tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 0.05, 18.0, ad, "left", 0.0)
    C.append(("E3 S ＝ 0.05 ⇒ 上界 0.1", rec[0][0][8], 0.1))
    try:
        tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 42.0, 18.0, ad, "中段", 0.0)
        e4 = "過"
    except RuntimeError:
        e4 = "停"
    C.append(("E4 側別非 left／right ⇒ 停機", e4, "停"))
    C.append(("E5 回 (G, S_raw)", tuple(r1), (123.456, 7.89)))
    red = []
    for name, got, exp in C:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {got!r}"[:700])
            print(f"       期 {exp!r}"[:700])
            red.append(name.split()[0])
    print(f"  ℹ️ G1 量 {n1}·略 {sk1}；G2 量 {n2}·略 {sk2}")
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


def _guarded(fn):
    """{呼叫節點: 其所在之 if 之判式之名之集}（最近之一層 if／elif）。"""
    out = {}

    def walk(node, test_names):
        for ch in ast.iter_child_nodes(node):
            if isinstance(ch, ast.If):
                names = {x.id for x in ast.walk(ch.test) if isinstance(x, ast.Name)}
                for b in ch.body:
                    walk_one(b, names)
                for b in ch.orelse:
                    walk_one(b, names if not (len(ch.orelse) == 1 and isinstance(b, ast.If)) else test_names)
            else:
                walk_one(ch, test_names)

    def walk_one(node, names):
        if isinstance(node, ast.Call) and _callee(node) == "k980_acq_check":
            out[node] = names
        if isinstance(node, ast.If):
            walk(ast.Module(body=[node], type_ignores=[]), names)
            return
        walk(node, names)
    walk(fn, set())
    return out


def wiring(repo, base):
    paths = ("app.py", "verify/stepg_pipeline.py")
    srcs = {p: open(os.path.join(repo, p), encoding="utf-8").read() for p in paths}
    old = _git(repo, "show", f"{base}:app.py")
    if not old:
        print(f"  🔴 基準 {base} 之 app.py 取不到")
        print("⇒ 紅 ['基準缺']；rc 1")
        return 1
    trees = {p: ast.parse(s) for p, s in srcs.items()}
    ta = trees["app.py"]
    red = []
    # W1
    sg1 = _fn_node(ta, "_solve_G_one")
    cs = _calls(sg1, "solve_G_binary") if sg1 else []
    kw = {k.arg: k.value for k in cs[0].keywords} if len(cs) == 1 else {}
    ok1 = (len(cs) == 1 and isinstance(kw.get("tol"), ast.Name) and kw["tol"].id == "K980_G_TOL"
           and isinstance(kw.get("max_iter"), ast.Name) and kw["max_iter"].id == "K980_G_MAX_ITER"
           and len(_calls(ta, "solve_G_binary")) == 1)
    print(("  ✅" if ok1 else "  🔴") + f" W1 _solve_G_one 之 solve_G_binary 以 K980_G_TOL／K980_G_MAX_ITER（呼叫 {len(cs)}·全檔 {len(_calls(ta, 'solve_G_binary'))}）")
    if not ok1:
        red.append("W1")
    # W2
    w2 = []
    for p, fname in (("app.py", "f3_screen_stepg_run"), ("verify/stepg_pipeline.py", "_run_step_g_impl")):
        fn = _fn_node(trees[p], fname)
        g = _guarded(fn) if fn else {}
        combos = []
        for c, names in g.items():
            side = c.args[2].value if len(c.args) >= 3 and isinstance(c.args[2], ast.Constant) else None
            ev = c.args[4] if len(c.args) >= 5 else None
            kind = None
            if isinstance(ev, ast.Call) and _callee(ev) == "_corner_first_lot_G":
                kind = "街角"
            elif (isinstance(ev, ast.Subscript) and isinstance(ev.value, ast.Call) and _callee(ev.value) == "end_block_trial_G"
                  and isinstance(ev.slice, ast.Constant) and ev.slice.value == 0):
                kind = "末端"
            combos.append((str(kind), str(side), "_commit" in names))
        ok_ = (len(g) == 4 and sorted(combos) == sorted([("街角", "left", True), ("街角", "right", True),
                                                          ("末端", "left", True), ("末端", "right", True)]))
        w2.append((p, len(g), ok_))
    ok2 = all(x[2] for x in w2)
    print(("  ✅" if ok2 else "  🔴") + f" W2 取得之宗之自我檢查之四處（{[(a, b) for a, b, _ in w2]}）")
    if not ok2:
        red.append("W2")
    # W3
    eh = _fn_node(ta, "end_block_host")
    n_tg = len(_calls(eh, "end_block_trial_G")) if eh else -1
    n_so = len(_calls(eh, "solve_one")) if eh else -1
    ok3 = n_tg == 1 and n_so == 0
    print(("  ✅" if ok3 else "  🔴") + f" W3 end_block_host 之評選經 end_block_trial_G（{n_tg}）·solve_one 之直呼 {n_so}")
    if not ok3:
        red.append("W3")
    # W4
    wf = next((n.value for n in ta.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
               and t.id == "_WF_NS_NAMES" for t in n.targets)), None)
    wfn = {e.value for e in getattr(wf, "elts", []) if isinstance(e, ast.Constant)}
    used = {n.slice.value for n in ast.walk(trees["verify/stepg_pipeline.py"]) if isinstance(n, ast.Subscript)
            and isinstance(n.value, ast.Name) and n.value.id == "ns" and isinstance(n.slice, ast.Constant)
            and n.slice.value in NEW_TOP}
    ok4 = bool(used) and used <= wfn
    print(("  ✅" if ok4 else "  🔴") + f" W4 引擎經 ns 取之新名 {sorted(used)} ⊆ _WF_NS_NAMES（漏 {sorted(used - wfn)}）")
    if not ok4:
        red.append("W4")
    # W5
    tb, tn = _top(old), _top(srcs["app.py"])
    add, rem = set(tn) - set(tb), set(tb) - set(tn)
    ok5 = add == NEW_TOP and not rem
    print(("  ✅" if ok5 else "  🔴") + f" W5 頂層之名之增 {sorted(add)}·減 {sorted(rem)}")
    if not ok5:
        red.append("W5")
    # W6
    kc = _fn_node(ta, "k980_acq_check")
    ok6 = bool(kc) and len(_calls(kc, "k6_program_stop")) >= 1 and any(
        isinstance(c, ast.Constant) and isinstance(c.value, str) and GB in c.value for c in ast.walk(kc))
    print(("  ✅" if ok6 else "  🔴") + " W6 k980_acq_check 經 k6_program_stop 立 GB-206 之停機")
    if not ok6:
        red.append("W6")
    # W7
    chg = sorted(k for k in tn if tn.get(k) != tb.get(k))
    lits = []
    tbo = ast.parse(old)
    for n in ta.body:
        nm = getattr(n, "name", None) or (n.targets[0].id if isinstance(n, ast.Assign)
                                          and isinstance(n.targets[0], ast.Name) else None)
        if nm in chg:
            ob = _fn_node(tbo, nm)
            newc = {c.value for c in ast.walk(n) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                    and CASE_LIT_RE.match(c.value)}
            oldc = {c.value for c in ast.walk(ob) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                    and CASE_LIT_RE.match(c.value)} if ob is not None else set()
            lits += sorted((nm, x) for x in newc - oldc)
    ok7 = not lits
    print(("  ✅" if ok7 else "  🔴") + f" W7 新增或改之頂層節點（{len(chg)}）內新增之案件字面 {lits}")
    if not ok7:
        red.append("W7")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

# 本案之錨：KL `2026-10-22 05:22` 所核之請示表之「甲」之欄（⛔ 由受測之碼產）
ANCHOR = {
    3.5: ({"628-18(1)": 307.78, "628-18(2)": 268.34},
          {"R1-抵費地-1": 851.69, "R3-抵費地": 1651.40, "R4-抵費地": 697.39, "R5-抵費地": 1221.45, "R6-抵費地": 980.58}),
    0.0: ({"628-18(1)": 307.78, "628-18(2)": 259.13},
          {"R1-抵費地-1": 851.69, "R3-抵費地": 1651.40, "R4-抵費地": 697.39, "R5-抵費地": 1221.46, "R6-抵費地": 980.58}),
}


def _one(repo, sb):
    probes = os.path.join(repo, "verify", "probes")
    if probes not in sys.path:
        sys.path.insert(0, probes)
    os.environ["WV_K6B_STAGE3"] = "on"
    import probe_WG9344_k6s3 as K
    ns, fst, snap, cb_by, cad, tp, bp, params = K._boot(repo, sb)
    if "k980_acq_check" not in ns:
        return None
    import selection_pipeline as sp
    calls, ev = [], []
    o_chk = ns["k980_acq_check"]

    def w_chk(kind, blk, side, pid, ge, ga):
        calls.append((kind, blk, side, pid, round(float(ge), 2), round(float(ga), 2)))
        return o_chk(kind, blk, side, pid, ge, ga)
    ns["k980_acq_check"] = w_chk
    o_cf = ns["_corner_first_lot_G"]
    phase = {"p": "pk"}

    def w_cf(**kw):
        g = o_cf(**kw)
        if phase["p"] == "pk":
            lab = str(kw.get("_label", ""))
            ev.append((lab.split("·")[1] if lab.count("·") >= 2 else None, {"左": "left", "右": "right"}.get(kw.get("side")),
                       round(float(kw.get("a_m2")), 2), round(float(g), 2)))
        return g
    ns["_corner_first_lot_G"] = w_cf
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _o, wins, forced, _tp2, bp2 = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb,
                                                                   snapshot=snap)
    phase["p"] = "sg"
    res = K._materialize(ns, fst, snap, cb_by, cad, params, tp, bp2, wins, forced, sb)
    ebv = copy.deepcopy(fst.session_state.get(ns["SS_END_BLOCK_EVAL"]) or {})
    a0 = {t["暫編地號"]: round(float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0), 2) for t in tp}
    ns["k980_acq_check"] = o_chk
    ns["_corner_first_lot_G"] = o_cf
    return res, calls, ev, ebv, a0


def run(repo, sbs):
    red = []
    for sb in sbs:
        try:
            got = _one(repo, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  🔴 R1@{sb} 例外 {type(e).__name__}：{str(e)[:200]}")
            red.append(f"R1@{sb}")
            continue
        if got is None:
            print("  🔴 受詞缺（k980_acq_check）")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        res, calls, ev, ebv, a0 = got
        rows = res["rows"]
        # R1
        kinds = {c[0] for c in calls}
        bad_c = sorted({c for c in calls if c[4] != c[5]})
        firsts = [r for r in rows if r.get("驗_宗序") == "街角第1宗"]
        pairs, bad_p = 0, []
        for r in firsts:
            key = (r["暫編地號"], r["推進側別"], round(float(r["a 面積(㎡)"]), 2))
            m = [e for e in ev if (e[0], e[1], e[2]) == key]
            if m:
                pairs += 1
                if any(e[3] != round(float(r["G(㎡)"]), 2) for e in m):
                    bad_p.append((key, sorted({e[3] for e in m}), r["G(㎡)"]))
        eb_pairs, bad_e = 0, []
        byk = {r["暫編地號"]: r for r in rows}
        for blk, e in ebv.items():
            for sd, v in e.items():
                w = v.get("當選") if isinstance(v, dict) else None
                if not w or w not in byk:
                    continue
                if round(float(byk[w]["a 面積(㎡)"]), 2) != a0.get(w):
                    continue
                gw = [c.get("試算G(㎡)") for c in v.get("候選", []) if c.get("暫編地號") == w]
                eb_pairs += 1
                if not gw or round(float(gw[0]), 2) != round(float(byk[w]["G(㎡)"]), 2):
                    bad_e.append((blk, sd, w, gw, byk[w]["G(㎡)"]))
        ok1 = (res["err"] is None and {"街角第1宗", "末端塊"} <= kinds and not bad_c and pairs >= 1 and not bad_p
               and not bad_e)
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb} 自我檢查 {len(calls)} 次（{sorted(kinds)}·異 {bad_c[:3]}）；"
              f"評選對終態之街角第 1 宗 配對 {pairs}·異 {bad_p[:3]}；末端塊 配對 {eb_pairs}·異 {bad_e[:3]}；err {res['err']}")
        if not ok1:
            red.append(f"R1@{sb}")
        # R2
        lots, pools = ANCHOR[sb]
        gl = {r["暫編地號"]: r["G(㎡)"] for r in rows}
        gp = {p["池"]: p["面積"] for p in res["pools"]}
        bad2 = [(k, gl.get(k), v) for k, v in lots.items() if gl.get(k) != v] + \
               [(k, gp.get(k), v) for k, v in pools.items() if gp.get(k) != v]
        ok2 = not bad2
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb} 本案之錨（KL 05:22 所核之甲）不合 {bad2}")
        if not ok2:
            red.append(f"R2@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def diff(pre, post):
    import json
    a = json.load(open(pre, encoding="utf-8"))
    b = json.load(open(post, encoding="utf-8"))
    out = []

    def key(r):
        return (str(r.get("所屬街廓")), str(r.get("暫編地號")), str(r.get("推進側別")))
    ra = {key(r): r for r in a.get("rows") or []}
    rb = {key(r): r for r in b.get("rows") or []}
    for k in sorted(set(ra) | set(rb)):
        x, y = ra.get(k) or {}, rb.get(k) or {}
        for f in ("a 面積(㎡)", "G(㎡)", "驗_總判", "驗_宗序", "歸戶"):
            if x.get(f) != y.get(f) or (k in ra) != (k in rb):
                out.append(f"宗 {k[0]}·{k[1]}·{k[2]} {f} {x.get(f)!r} → {y.get(f)!r}")
    pa = {p["池"]: p for p in a.get("pools") or []}
    pb = {p["池"]: p for p in b.get("pools") or []}
    for k in sorted(set(pa) | set(pb)):
        for f in ("面積", "容納內接矩形"):
            if (pa.get(k) or {}).get(f) != (pb.get(k) or {}).get(f):
                out.append(f"抵費地 {k} {f} {(pa.get(k) or {}).get(f)!r} → {(pb.get(k) or {}).get(f)!r}")
    for f in ("wins", "forced", "dropped", "err"):
        if a.get(f) != b.get(f):
            out.append(f"{f} 異")
    for l in out:
        print("  " + l)
    print(f"全比相異 {len(out)} 項")
    return 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], os.path.abspath(argv[2])
    if cmd == "diff":
        if len(argv) != 4:
            print("用法：diff <pre.json> <post.json>")
            return 2
        return diff(argv[2], argv[3])
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
