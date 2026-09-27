# -*- coding: utf-8 -*-
"""W-G.9-352 量測器（發單側窗四十八擬·檔 F11·⛔ 由受單側改一字）：末端塊之評選與落位（`K-9-36 ①②`·`K-9-49`）。

子命令（一律 python verify/probes/probe_WG9352_endblock.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·以 AST 自 `app.py` 抽出 `END_BLOCK_*`／`SS_END_BLOCK_EVAL` 與 `end_block_*`、
           `solve_G_binary`、`_select_pool_slot` 及其幾何基元）：觸發（左、右鏡像、未臨正街 ≤ ε 不觸發）、R_end 之面積、
           評選（往後找、等號當選、跨占 ≤ 門檻者非候選、跨占街角規定範圍者歸街角側、皆未達停機）、落位（左首、右末、
           入池閘合併單元、街角第 1 宗停機）、首趟評選之沿用、二源不一致停機、選槽之 pin、顯示、定案趟之檢、
           `s_back`（宗地 ＝ 未臨正街 ∪ 正街段；G 公式之 S 只計正街段；`s_back=0` 逐位同）。
           另施七突變，每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST／字樣查接線（app.py 與 verify/stepg_pipeline.py 二宿主）：W1 模組層之常數與函式、⛔ 案件字面；
           W2 二宿主於 `_ov2_idx` 之前恰一次呼叫 `end_block_host`（`solve_one=_solve_one`）；W3 左鏈一處、右鏈二處之
           `_solve_one` 帶 `_s_back`（取 `_eb_info`）；W4 定案趟呼叫 `end_block_assert_head`；W5 選槽之 `pin` 與
           `_kmin_c`／`_kmax_c`；W6 非試算趟先清 `SS_END_BLOCK_EVAL`；W7 入池閘之畫面入口於復原之後帶出評選、
           `K6B_SCREEN_TRIAL_KEYS` 含其鍵且末項仍為 `f3_k929_6_log`；W8 `_WF_NS_NAMES` 含三名；W9 `solve_G_binary`／
           `_solve_G_one` 之 `s_back` 與 fallback 停機；W10 `main()` 之顯示。另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：以本器**另寫之幾何與 G 公式**（⛔ 呼叫 `end_block_*`／
           `_end_region_R`／`solve_G_binary`）為外部錨：R1 各無側街之端之觸發與 R_end；R2 候選（跨占者依原投影序）、
           各筆單獨試算之 G 與當選者；R3 配地列：觸發之端之鏈首宗 ＝ 當選者、其宗地 ⊇ R_end、其 G ＝ 試算 G；
           R4 無抵費地與未臨正街相交；R5 本街廓之宗地與抵費地之聯集 ＝ 街廓、兩兩⛔ 疊。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

EB_FUNCS = ["end_block_side_geom", "end_block_pick", "end_block_pin", "end_block_apply",
            "end_block_host", "end_block_eval_rows", "end_block_assert_head"]
DEP_FUNCS = ["_strip_axis", "_strip_s_range", "_block_strip", "_end_band", "_end_region_R",
             "alloc_normal_axis", "solve_G_binary", "_select_pool_slot", "rw_from_width"]
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _extract_ns(src):
    tree = ast.parse(src)
    parts = []
    names = set(EB_FUNCS) | set(DEP_FUNCS)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and (node.targets[0].id.startswith("END_BLOCK_") or node.targets[0].id == "SS_END_BLOCK_EVAL"
                     or node.targets[0].id in ("RW_SATURATION_WIDTH_M", "_STRIP_PARALLEL_TOL")):
            parts.append(ast.get_source_segment(src, node))
    got = {n.name for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in EB_FUNCS}
    if got != set(EB_FUNCS):
        raise KeyError("受詞缺")
    ns = {}
    exec(compile("\n\n".join(parts), "<eb_extract>", "exec"), ns)
    return ns


# ── 合成幾何：FRONT 沿 x 軸 p1=(0,0)→p2=(40,0)；ALLOC ∥ y 軸；深 30；左端外斜 3 m（未臨正街 45 ㎡）──
def _geo(ns, mirror=False):
    from shapely.geometry import Polygon
    import numpy as np
    if not mirror:
        blk = Polygon([(0, 0), (40, 0), (40, 30), (-3, 30)])
    else:
        blk = Polygon([(0, 0), (40, 0), (43, 30), (0, 30)])
    cad = (0.0, 1.0)
    return dict(blk=blk, d=np.array([1.0, 0.0]), p1=np.array([0.0, 0.0]), p2=np.array([40.0, 0.0]),
                cad=cad, ad=ns["alloc_normal_axis"](cad))


def _tp(pid, coords, lot=None, **kw):
    d = {"暫編地號": pid, "原地號": lot or pid.split("(")[0], "polygon_coords": [list(c) for c in coords]}
    d.update(kw)
    return d


def _e(tp, **kw):
    d = {"tp": tp, "pre_position": 0, "is_corner_winner": False, "side": "中段"}
    d.update(kw)
    return d


def _cases(ns):
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__)
        out.append((name, got, exp))

    G = _geo(ns)
    GM = _geo(ns, mirror=True)
    geo = ns["end_block_side_geom"]

    def gl(g, side):
        r = geo(g["blk"], g["d"], g["p1"], g["p2"], g["cad"], g["ad"], 3.5, side, _label="T")
        return (r["gate"], round(r["unfront"], 4), round(r.get("s_back", 0.0), 4),
                round(r.get("r_end_area", 0.0), 4), round(r.get("band_area", 0.0), 4))

    run("S1 左端觸發（未臨正街 45·s_back 3·末端帶 105·R_end 150）", lambda: gl(G, "left"),
        (True, 45.0, 3.0, 150.0, 105.0))
    run("S2 右端觸發（鏡像）", lambda: gl(GM, "right"), (True, 45.0, 3.0, 150.0, 105.0))
    run("S3 未臨正街 0 ⇒ 不觸發（左端鉛直）", lambda: gl(GM, "left")[0], False)

    gg = geo(G["blk"], G["d"], G["p1"], G["p2"], G["cad"], G["ad"], 3.5, "left", _label="T")
    # 原位次序列（自左端起）：a 跨占 R_end（6 ㎡）、b 跨占（G 恰 150）、c 跨占、d 不跨占
    a = _tp("A(1)", [(-3, 30), (-1, 10), (5, 10), (5, 30)])
    b = _tp("B(1)", [(-1, 10), (0, 0), (5, 0), (5, 10)])
    c = _tp("C(1)", [(3.4, 0), (10, 0), (10, 30), (3.4, 30)])
    dd = _tp("D(1)", [(20, 0), (30, 0), (30, 30), (20, 30)])
    tiny = _tp("T(1)", [(3.0, 0), (3.49, 0), (3.49, 1.0), (3.0, 1.0)])
    Gv = {"A(1)": 100.0, "B(1)": 150.0, "C(1)": 500.0, "D(1)": 900.0, "T(1)": 999.0}
    calls = []

    def trial(tp):
        calls.append(tp["暫編地號"])
        return Gv[tp["暫編地號"]], 5.0

    pick = ns["end_block_pick"]
    seq = [_e(a), _e(b), _e(c), _e(dd)]
    run("S4 往後找·等號當選（A 未達、B ＝ 150 當選）",
        lambda: (pick("left", gg, seq, {}, trial, _label="T")["winner"],
                 [r["結果"] for r in pick("left", gg, seq, {}, trial, _label="T")["rows"]]),
        ("B(1)", ["未達", "當選"]))
    run("S5 跨占 ≤ 門檻者非候選（T 跨占 0.49 ㎡）",
        lambda: pick("left", gg, [_e(tiny), _e(c)], {}, trial, _label="T")["winner"], "C(1)")
    from shapely.geometry import Polygon as _P
    run("S6 跨占街角規定範圍者歸街角側（⛔ 候選）",
        lambda: [(r["暫編地號"], r["結果"]) for r in pick("left", gg, [_e(b), _e(c)], {"right": _P([(-1, 0), (1, 0), (1, 12), (-1, 12)])},
                                                         trial, _label="T")["rows"]],
        [("B(1)", "跨占街角規定範圍·歸街角側"), ("C(1)", "當選")])
    run("S7 皆未達 ⇒ 停機", lambda: pick("left", gg, [_e(a)], {}, trial, _label="T"), ("例外", "RuntimeError"))

    pin = ns["end_block_pin"]
    run("S8 落位（左）：當選者移至首·餘者原序",
        lambda: [(x["tp"]["暫編地號"], bool(x.get("is_end_block"))) for x in pin(seq, "left", "C(1)", _label="T")],
        [("C(1)", True), ("A(1)", False), ("B(1)", False), ("D(1)", False)])
    run("S9 落位（右）：當選者移至末",
        lambda: [x["tp"]["暫編地號"] for x in pin(seq, "right", "B(1)", _label="T")],
        ["A(1)", "C(1)", "D(1)", "B(1)"])
    u = _tp("U(1)", [(0, 0), (1, 0), (1, 1)], 入池閘併入=["U(1)", "B(1)"])
    run("S10 落位：當選者為入池閘合併單元之成員 ⇒ 移該單元",
        lambda: [x["tp"]["暫編地號"] for x in pin([_e(a), _e(u)], "left", "B(1)", _label="T")], ["U(1)", "A(1)"])
    run("S10b 落位：當選者為街角第 1 宗 ⇒ 停機",
        lambda: pin([_e(a, is_corner_winner=True)], "left", "A(1)", _label="T"), ("例外", "RuntimeError"))

    apply = ns["end_block_apply"]

    def ap(cache, trial_fn, has_pk=None, has_cad=None, g=G, order=None):
        return apply(order or seq, blk_label="BX", block_poly=g["blk"], d_hat=g["d"], corner_pt=g["p1"],
                     front_p2=g["p2"], cad_alloc=g["cad"], allocation_dir=g["ad"], min_width=3.5,
                     has_side_pk=has_pk or {"left": False, "right": True},
                     has_side_cad=has_cad or {"left": False, "right": True},
                     corner_range_polys={}, trial=trial_fn, cache=cache)

    def s11():
        cache = {}
        calls.clear()
        o1, i1 = ap(cache, lambda tp, s, w: trial(tp))
        n1 = len(calls)
        calls.clear()
        o2, i2 = ap(cache, lambda tp, s, w: (0.0, 0.0), order=[_e(dd), _e(c), _e(b), _e(a)])
        return (o1[0]["tp"]["暫編地號"], n1, o2[0]["tp"]["暫編地號"], len(calls), round(i1["left"]["s_back"], 4),
                cache["BX"]["left"]["當選"], i1["right"])
    run("S11 首趟評選、次趟沿用（⛔ 重評）", s11, ("B(1)", 2, "B(1)", 0, 3.0, "B(1)", None))
    run("S11b 二源不一致 ⇒ 停機",
        lambda: ap({}, lambda tp, s, w: trial(tp), has_pk={"left": False, "right": True},
                   has_cad={"left": True, "right": True}), ("例外", "RuntimeError"))
    run("S12 首趟未觸發而本趟觸發 ⇒ 停機",
        lambda: ap({"BX": {"left": {"觸發": False}}}, lambda tp, s, w: trial(tp)), ("例外", "RuntimeError"))

    sps = ns["_select_pool_slot"]
    run("S13 選槽之 pin（左 pin ⇒ k≥1；右 pin ⇒ k≤n−1）",
        lambda: (min(t["k"] for t in sps([1, 1, 1], {"has": False, "pin": True}, {"has": False})["table"]),
                 max(t["k"] for t in sps([1, 1, 1], {"has": False}, {"has": False, "pin": True})["table"]),
                 min(t["k"] for t in sps([1, 1, 1], {"has": False}, {"has": False})["table"])),
        (1, 2, 0))
    run("S14 顯示（值皆字串·未觸發之端具名）",
        lambda: (ns["end_block_eval_rows"]({"BX": {"left": {"觸發": True, "未臨正街(㎡)": 45.0, "末端帶(㎡)": 105.0,
                                                           "R_end(㎡)": 150.0, "當選": "B(1)",
                                                           "候選": [{"暫編地號": "A(1)", "試算G(㎡)": None}]},
                                                  "right": {"觸發": False, "未臨正街(㎡)": 0.0}}})),
        {"lines": ["BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；當選 B(1)",
                   "BX 右端（無側街）：未臨正街 0.0 ㎡ ⇒ 未觸發"],
         "rows": [{"街廓": "BX", "端": "左", "暫編地號": "A(1)", "試算G(㎡)": "—"}]})
    ah = ns["end_block_assert_head"]
    run("S15 定案趟之檢：首宗非當選者 ⇒ 停機；是 ⇒ 過",
        lambda: ((lambda: (ah("BX", {"left": {"winner": "B(1)"}, "right": None}, [(_e(a), {})], []), "過")[1])(),),
        ("例外", "RuntimeError"))
    run("S15b 定案趟之檢：首宗為當選者 ⇒ 過",
        lambda: (ah("BX", {"left": {"winner": "B(1)"}, "right": None}, [(_e(b, is_end_block=True), {})], []), "過")[1],
        "過")

    sgb = ns["solve_G_binary"]
    a_, A_, B_, C_, l2 = 700.0, 1.2, 0.2, 0.1, 2.0

    def s16():
        r = sgb(a=a_, A=A_, B=B_, C=C_, l_front=l2, l_side=0.0, F=0.0, block_poly=G["blk"], d_hat=G["d"],
                baseline_pt=G["p1"], S_max_limit=40.0, allocation_dir=G["ad"], s_back=3.0)
        cut = _P(r["cut_coords"])
        S = float(r["S_raw"])
        Gf = (a_ * (1 - A_ * B_) - S * l2) * (1 - C_)
        wedge = _P([(0, 0), (0, 30), (-3, 30)])
        return (abs(r["G"] - round(Gf, 2)) <= 0.01, abs(cut.area - Gf) <= 0.02,
                round(wedge.difference(cut).area, 6), round(cut.bounds[0], 4), abs(cut.bounds[2] - S) <= 1e-6)
    run("S16 s_back：宗地 ＝ 未臨正街 ∪ [0,S]；G 之 S 只計正街段", s16, (True, True, 0.0, -3.0, True))

    def s17():
        kw = dict(a=a_, A=A_, B=B_, C=C_, l_front=l2, l_side=0.0, F=0.0, block_poly=G["blk"], d_hat=G["d"],
                  baseline_pt=G["p1"], S_max_limit=40.0, allocation_dir=G["ad"])
        r0 = sgb(**kw)
        r1 = sgb(**kw, s_back=0.0)
        return (r0["cut_coords"] == r1["cut_coords"], r0["G"] == r1["G"], r0["S_raw"] == r1["S_raw"])
    run("S17 s_back＝0 ⇒ 逐位同", s17, (True, True, True))
    run("S18 s_back 與 side_mid 並存 ⇒ 停機",
        lambda: sgb(a=a_, A=A_, B=B_, C=C_, l_front=l2, l_side=0.0, F=0.0, block_poly=G["blk"], d_hat=G["d"],
                    baseline_pt=G["p1"], S_max_limit=40.0, allocation_dir=G["ad"], side_mid=(0, 15), s_back=3.0),
        ("例外", "RuntimeError"))
    return out


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)
    return red


def selftest(repo):
    src = _read(repo, "app.py")
    try:
        ns = _extract_ns(src)
    except Exception:  # noqa: BLE001
        print(f"  🔴 受詞缺：{EB_FUNCS}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（AST 抽出之 end_block_*／solve_G_binary／_select_pool_slot）──")
    red = _report(_cases(ns))
    print("── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──")
    base_red = set(red)
    m0 = _report(_cases(_extract_ns(src)), verbose=False)
    print(("  ✅ " if m0 == red else "  🔴 ") + f"M0 未突變之抽出版：紅 {m0}（期 {red}）")
    if m0 != red:
        red.append("M0")
    muts = [
        ("M1 當選改為嚴格大於", "_ok = float(_g) >= _thr", "_ok = float(_g) > _thr"),
        ("M2 首筆跨占者即當選（⛔ 往後找）", "        rows.append(_row)\n        if _ok:",
         "        rows.append(_row)\n        if True:"),
        ("M3 跨占街角規定範圍者⛔ 排除",
         "if any(float(_pg.intersection(_c).area) > END_BLOCK_CROSS_MIN_AREA for _c in _crs):", "if False:"),
        ("M4 落位⛔ 移至首", "        _out.insert(0, _e)", "        _out.insert(_idx[0], _e)"),
        ("M5 未臨正街計入臨街", "                             - S_guess * l_front) * (1.0 - C))",
         "                             - (S_guess + _s_back) * l_front) * (1.0 - C))"),
        ("M6 首趟評選⛔ 沿用", "        if _cached is not None:\n            _c = _cached.get(_sd) or {}",
         "        if False:\n            _c = _cached.get(_sd) or {}"),
        ("M7 選槽⛔ 理 pin", "    k_min = 1 if (has_L or bool(_L.get('pin'))) else 0", "    k_min = 1 if has_L else 0"),
    ]
    for mname, x, y in muts:
        if src.count(x) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{src.count(x)}）")
            red.append(mname.split()[0])
            continue
        try:
            turned = [n for n in _report(_cases(_extract_ns(src.replace(x, y, 1))), verbose=False) if n not in base_red]
        except Exception as ex:  # noqa: BLE001
            turned = [f"抽出拋 {type(ex).__name__}"]
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
def _fn_src(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return ast.get_source_segment(src, n)
    return None


def _wiring_checks(app, sg):
    res = []
    tree = ast.parse(app)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    lits = []
    for f in EB_FUNCS:
        if f in top:
            for n in ast.walk(top[f]):
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value):
                    lits.append((f, n.value))
    ok1 = all(f in top for f in EB_FUNCS) and {"END_BLOCK_UNFRONT_EPS", "END_BLOCK_CROSS_MIN_AREA",
                                                 "SS_END_BLOCK_EVAL"} <= consts and not lits
    res.append((f"W1 模組層之常數與七函式、函式內⛔ 案件字面（案件字面 {lits}）", ok1, ""))
    scr = _fn_src(app, "f3_screen_stepg_run") or ""
    hsg = _fn_src(sg, "_run_step_g_impl") or ""
    outer = _fn_src(sg, "run_step_g") or ""

    def host_ok(h, call):
        i = h.find(call)
        j = h.find("['_ov2_idx'] = ")
        return h.count(call) == 1 and 0 <= i < j and "solve_one=_solve_one" in h[i:i + 1200]
    res.append(("W2 二宿主於 `_ov2_idx` 前恰一次呼叫 end_block_host（solve_one=_solve_one）",
                host_ok(scr, "end_block_host(") and host_ok(hsg, 'ns["end_block_host"]('), ""))
    pl = "_s_back=(float(_eb_info['left']['s_back'])"
    pr = "_s_back=(float(_eb_info['right']['s_back'])"
    res.append(("W3 左鏈一處、右鏈二處之 `_solve_one` 帶 `_s_back`（二宿主）",
                scr.count(pl) == 1 and scr.count(pr) == 2 and hsg.count(pl) == 1 and hsg.count(pr) == 2, ""))
    res.append(("W4 定案趟呼叫 end_block_assert_head（二宿主）",
                re.search(r"if _commit:\s*\n\s*end_block_assert_head\(blk_label, _eb_info, left_results, right_results\)", scr)
                is not None and
                re.search(r'if _commit:\s*\n\s*ns\["end_block_assert_head"\]\(blk_label, _eb_info, left_results, right_results\)', hsg)
                is not None, ""))
    pin = ("'pin': _eb_info['left'] is not None", "'pin': _eb_info['right'] is not None",
           "_kmin_c = 1 if (_has_left_corner or _eb_info['left'] is not None) else 0",
           "_kmax_c = (_N - 1) if (_has_right_corner or _eb_info['right'] is not None) else _N")
    res.append(("W5 選槽之 pin 與 _kmin_c／_kmax_c（二宿主）", all(scr.count(p) == 1 and hsg.count(p) == 1 for p in pin), ""))
    res.append(("W6 非試算趟先清 SS_END_BLOCK_EVAL（二宿主）",
                re.search(r"if not _k929_6_inner:\s*\n\s*st\.session_state\.pop\(SS_END_BLOCK_EVAL, None\)", scr) is not None
                and re.search(r'if not _k929_6_inner:\s*\n\s*fake_st\.session_state\.pop\(ns\["SS_END_BLOCK_EVAL"\], None\)', outer)
                is not None, ""))
    gate = _fn_src(app, "_k929_6_screen_gate") or ""
    keys = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "K6B_SCREEN_TRIAL_KEYS" for t in n.targets):
            keys = ast.literal_eval(n.value)
    ig = gate.find("_ss[SS_END_BLOCK_EVAL] = _ev352")
    res.append(("W7 入池閘之畫面入口於復原之後帶出評選；鍵 ∈ K6B_SCREEN_TRIAL_KEYS 且末項 ＝ f3_k929_6_log",
                ig > gate.find("finally:") > 0 and "_ev352 = _cp_k9296s.deepcopy(_ss.get(SS_END_BLOCK_EVAL))" in gate
                and bool(keys) and "f3_end_block_eval" in keys and keys[-1] == "f3_k929_6_log", ""))
    wf = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets):
            wf = ast.literal_eval(n.value)
    res.append(("W8 _WF_NS_NAMES 含 end_block_host／end_block_assert_head／SS_END_BLOCK_EVAL",
                bool(wf) and {"end_block_host", "end_block_assert_head", "SS_END_BLOCK_EVAL"} <= set(wf), ""))
    sgb = _fn_src(app, "solve_G_binary") or ""
    sgo = _fn_src(app, "_solve_G_one") or ""
    res.append(("W9 solve_G_binary／_solve_G_one 之 s_back 與 fallback 停機",
                "s_back: float = 0.0" in sgb and "_S + _s_back, allocation_dir=allocation_dir)" in sgb
                and "s_back=s_back," in sgo and "if float(s_back or 0.0) > 0.0:" in sgo, ""))
    mn = _fn_src(app, "main") or ""
    res.append(("W10 main() 之顯示（end_block_eval_rows 讀 SS_END_BLOCK_EVAL）",
                "_eb352 = st.session_state.get(SS_END_BLOCK_EVAL)" in mn and "end_block_eval_rows(_eb352)" in mn, ""))
    return res


def wiring(repo):
    app = _read(repo, "app.py")
    sg = _read(repo, "verify/stepg_pipeline.py")

    def rep(r):
        red = []
        for n, ok, note in r:
            print(("  ✅ " if ok else "  🔴 ") + n + (f"（{note}）" if note else ""))
            if not ok:
                red.append(n.split()[0])
        return red
    print("── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py）──")
    red = rep(_wiring_checks(app, sg))
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    base = {n.split()[0] for n, ok, _ in _wiring_checks(app, sg) if not ok}
    muts = [
        ("N1 harness 左鏈去 _s_back", "sg", "_s_back=(float(_eb_info['left']['s_back'])", "_s_bak=(float(_eb_info['left']['s_back'])"),
        ("N2 入池閘之畫面入口⛔ 帶出評選", "app", "        _ss[SS_END_BLOCK_EVAL] = _ev352", "        pass"),
        ("N3 畫面選槽去 pin", "app", "'l1': _lside_left, 'b': _bL_c, 'pin': _eb_info['left'] is not None},",
         "'l1': _lside_left, 'b': _bL_c},"),
        ("N4 harness 非試算趟⛔ 清評選", "sg", '        fake_st.session_state.pop(ns["SS_END_BLOCK_EVAL"], None)', "        pass"),
    ]
    for mname, which, x, y in muts:
        s_app, s_sg = app, sg
        tgt = s_app if which == "app" else s_sg
        if tgt.count(x) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{tgt.count(x)}）")
            red.append(mname.split()[0])
            continue
        if which == "app":
            s_app = app.replace(x, y, 1)
        else:
            s_sg = sg.replace(x, y, 1)
        turned = sorted({n.split()[0] for n, ok, _ in _wiring_checks(s_app, s_sg) if not ok} - base)
        print(("  ✅ " if turned else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not turned:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本器另寫之幾何與 G 公式（外部錨）──
def _s_of(x, p1, d, u):
    """點 x 之 s 座標（沿 d，切線 ∥ u）：x = p1 + s·d + t·u。"""
    import numpy as np
    v = np.asarray(x, float) - p1
    den = d[0] * u[1] - d[1] * u[0]
    return (v[0] * u[1] - v[1] * u[0]) / den


def _halfplane(p1, d, u, s_lo, s_hi, big):
    """{s_lo ≤ s ≤ s_hi} 之平行四邊形（切線 ∥ u）。"""
    from shapely.geometry import Polygon
    import numpy as np
    a = p1 + s_lo * d
    b = p1 + s_hi * d
    return Polygon([a - big * u, b - big * u, b + big * u, a + big * u])


def run(repo, sbs):
    import numpy as np
    from shapely.geometry import Polygon, LineString
    from shapely.ops import unary_union
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        from app_harvest import harvest
        with contextlib.redirect_stdout(io.StringIO()):
            ns, fake_st = harvest(os.path.join(repo, "app.py"))
        if "end_block_host" not in ns:
            print("  🔴 受詞缺：end_block_host")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g, _compute_v3_finance
        for sb in sbs:
            with contextlib.redirect_stdout(io.StringIO()):
                snapshot = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
                    ns["K917_DROPPED"].clear()
                    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                                    eff_min_build_by_blk={})
            except RuntimeError as e:
                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
                return 3
            ss = fake_st.session_state
            ev = ss.get(ns["SS_END_BLOCK_EVAL"]) or {}
            fin = _compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)
            B, C = fin["B"], fin["C"]
            print(f"══ 退縮 {sb} ══")
            rows = sg["g_rows"]
            mwmap = ss.get("f3_min_width_by_label", {}) or {}
            slbs = cad.get("side_lines_by_side", {}) or {}
            for blk, fo in sorted(forced.items()):
                bm = cb_by[blk]
                bp = Polygon(bm["vertices"])
                bp = bp if bp.is_valid else bp.buffer(0)
                fl = cad["front_lines"][blk]
                p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
                L = float(np.linalg.norm(p2 - p1))
                d = (p2 - p1) / L
                u = np.array(cad["alloc_dir_by_block"][blk], float)
                u = u / np.linalg.norm(u)
                big = 4 * float(np.hypot(*(np.array(bp.bounds[2:]) - np.array(bp.bounds[:2]))))
                svals = [_s_of(v, p1, d, u) for v in bp.exterior.coords]
                smin, smax = min(svals), max(svals)
                mw = float(mwmap.get(blk, 0.0) or 0.0)
                for side in ("left", "right"):
                    has = bool(fo.get(f"{side}_has_side")) or ((slbs.get(blk) or {}).get(side) or {}).get("mid") is not None
                    if has:
                        continue
                    rec = (ev.get(blk) or {}).get(side)
                    if side == "left":
                        unf = bp.intersection(_halfplane(p1, d, u, smin - 1.0, 0.0, big)) if smin < -1e-6 else Polygon()
                        endp = p1
                    else:
                        unf = bp.intersection(_halfplane(p1, d, u, L, smax + 1.0, big)) if smax > L + 1e-6 else Polygon()
                        endp = p2
                    trig = unf.area > 1e-3
                    ok1 = rec is not None and bool(rec.get("觸發")) == trig
                    if not trig:
                        print(("  ✅" if ok1 else "  🔴") + f" R1 {blk} {side}：未臨正街 {unf.area:.4f} ㎡ ⇒ 不觸發（評選紀錄 {rec}）")
                        if not ok1:
                            red.append(f"R1@{sb}:{blk}{side}")
                        continue
                    nrm = np.array([-u[1], u[0]])
                    if np.dot(np.asarray(bp.centroid.coords[0]) - endp, nrm) < 0:
                        nrm = -nrm
                    band = bp.intersection(Polygon([endp - big * u, endp + big * u, endp + big * u + mw * nrm,
                                                    endp - big * u + mw * nrm]))
                    rend = unary_union([unf, band])
                    ok1 = ok1 and abs(rec["R_end(㎡)"] - round(rend.area, 2)) <= 0.011 \
                        and abs(rec["未臨正街(㎡)"] - round(unf.area, 2)) <= 0.011
                    print(("  ✅" if ok1 else "  🔴") + f" R1 {blk} {side}：未臨正街 {unf.area:.2f}＋末端帶 {band.area:.2f}"
                          f"＝R_end {rend.area:.2f}（紀錄 {rec['未臨正街(㎡)']}／{rec['末端帶(㎡)']}／{rec['R_end(㎡)']}）")
                    if not ok1:
                        red.append(f"R1@{sb}:{blk}{side}")
                    # R2：候選與試算（外部錨：本器之帶與 G 公式）
                    l2 = float(fin["sb_rows_by_label"][blk]["正街尺度"])
                    post = float(fin["post_price_by_block"][blk])
                    crps = [Polygon(c) for c in ((ss.get("f3_corner_range_polys", {}) or {}).get(blk) or {}).values()
                            if c and len(c) >= 3]
                    # 原位次：本器以代表點投影於 FRONT 線（p1→p2）排序（外部錨·⛔ 呼叫 _projection_order）
                    lots = [t for t in bp3 if t.get("所屬街廓") == blk and len(t.get("polygon_coords") or []) >= 3
                            and str(t.get("原地號", "")) != "_GHOST"]
                    fln = LineString([p1, p2])
                    lots.sort(key=lambda t: fln.project(Polygon(t["polygon_coords"]).representative_point()))
                    if side == "right":
                        lots = lots[::-1]
                    exp_rows = []
                    winner = None
                    for t in lots:
                        pg = Polygon(t["polygon_coords"])
                        pg = pg if pg.is_valid else pg.buffer(0)
                        ov = pg.intersection(rend).area
                        if ov <= 1.0:
                            continue
                        if any(pg.intersection(c).area > 1.0 for c in crps):
                            exp_rows.append((t["暫編地號"], "跨占街角規定範圍·歸街角側"))
                            continue
                        a = round(float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0), 2)
                        pre = float(fin["pre_price_by_zone"].get(t.get("重劃前地價區段", ""), 0.0) or 0.0)
                        A = post / pre if pre > 0 else 1.0
                        w = (-smin) if side == "left" else (smax - L)

                        def area_at(S):
                            if side == "left":
                                return bp.intersection(_halfplane(p1, d, u, -w, S, big)).area
                            return bp.intersection(_halfplane(p1, d, u, L - S, L + w, big)).area
                        lo, hi = 0.0, L
                        for _ in range(100):
                            m = (lo + hi) / 2
                            if area_at(m) - (a * (1 - A * B) - m * l2) * (1 - C) < 0:
                                lo = m
                            else:
                                hi = m
                        S = (lo + hi) / 2
                        g = (a * (1 - A * B) - S * l2) * (1 - C)
                        res_ = "當選" if round(g, 2) >= rec["R_end(㎡)"] - 1e-9 else "未達"
                        exp_rows.append((t["暫編地號"], res_, round(g, 2)))
                        if res_ == "當選":
                            winner = t["暫編地號"]
                            break
                    got_rows = [(r["暫編地號"], r["結果"]) + ((r["試算G(㎡)"],) if r["試算G(㎡)"] is not None else ())
                                for r in rec["候選"]]
                    ok2 = winner == rec["當選"] and len(got_rows) == len(exp_rows) and all(
                        gr[:2] == er[:2] and (len(er) < 3 or abs(gr[2] - er[2]) <= 0.02)
                        for gr, er in zip(got_rows, exp_rows))
                    print(("  ✅" if ok2 else "  🔴") + f" R2 {blk} {side}：候選與試算 {got_rows} ＝ 外部錨 {exp_rows}")
                    if not ok2:
                        red.append(f"R2@{sb}:{blk}{side}")
                    # R3：配地列
                    chain = sorted([r for r in rows if r["所屬街廓"] == blk and r["推進側別"] == side],
                                   key=lambda r: float(r.get("累積S(m)", 0) or 0))
                    head = chain[0] if chain else None
                    hp = Polygon(head["cut_coords"]) if head and head.get("cut_coords") else Polygon()
                    trial_g = next((x[2] for x in exp_rows if x[0] == winner and len(x) > 2), None)
                    ok3 = (head is not None and head["暫編地號"] == winner and rend.difference(hp).area <= 1e-6
                           and trial_g is not None and abs(float(head["G(㎡)"]) - trial_g) <= 0.02)
                    print(("  ✅" if ok3 else "  🔴") + f" R3 {blk} {side}：鏈首宗 {head and head['暫編地號']}"
                          f"（G {head and head['G(㎡)']}·試算 {trial_g}）⊇ R_end（差 {rend.difference(hp).area:.6f}）")
                    if not ok3:
                        red.append(f"R3@{sb}:{blk}{side}")
                    pools = [Polygon(r["cut_coords"]) for r in rows if r["所屬街廓"] == blk
                             and r["推進側別"] not in ("left", "right") and r.get("cut_coords")]
                    pw = sum(p.intersection(unf).area for p in pools)
                    ok4 = pw <= 1e-6
                    print(("  ✅" if ok4 else "  🔴") + f" R4 {blk} {side}：抵費地 ∩ 未臨正街 ＝ {pw:.6f} ㎡")
                    if not ok4:
                        red.append(f"R4@{sb}:{blk}{side}")
                    allp = [Polygon(r["cut_coords"]) for r in rows if r["所屬街廓"] == blk and r.get("cut_coords")]
                    un = unary_union(allp)
                    ovl = sum(allp[i].intersection(allp[j]).area for i in range(len(allp)) for j in range(i + 1, len(allp)))
                    ok5 = un.symmetric_difference(bp).area <= 0.05 and ovl <= 0.05
                    print(("  ✅" if ok5 else "  🔴") + f" R5 {blk}：宗地與抵費地之聯集 △ 街廓 {un.symmetric_difference(bp).area:.4f} ㎡、"
                          f"兩兩疊 {ovl:.4f} ㎡")
                    if not ok5:
                        red.append(f"R5@{sb}:{blk}")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], argv[2]
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "wiring":
        return wiring(repo)
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
