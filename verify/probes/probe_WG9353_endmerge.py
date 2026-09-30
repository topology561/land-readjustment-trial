# -*- coding: utf-8 -*-
"""W-G.9-353 量測器（發單側窗四十九擬·檔 F12·⛔ 由受單側改一字）：末端塊之合併再試與強制抵費地
（`K-9-49 ②`·`K-9-36 ③`·補丁十 §一 之無勝者 fallback）。

子命令（一律 python verify/probes/probe_WG9353_endmerge.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取函式）：S1 評選之強制抵費地准否；S2〜S4 一街廓之落位
           （強制 ⇒ ⛔ 落位·紀錄·沿用·不准即停機）；S5 強制帶之 s 長；S6 強制帶之多邊形；S7 定案趟之檢；
           S8 顯示；S9 宿主之准否（試算恆准·定案唯同退縮之合併再試紀錄所載者准）；S10 合併再試（① 同街廓成·
           ② 道路成且驗「不影響原位次」·該驗不過 ⇒ 未成·皆未達 ⇒ 記之·除外三類·試算中止 ⇒ 逕回並記）。
           另施七突變，每一突變須使至少一例轉紅（判別力）。
           🔧 `W-G.9-354`：原 S10h（數末端塊之競合 ⇒ 停機）與其突變 M7 撤除——競合自該批起依 `K-9-50` 處之，
           其對照移量測器 F13（`verify/probes/probe_WG9354_endcontest.py`）。
  wiring   <repo>
           AST／字樣查接線：W1 模組層之常數與函式、⛔ 案件字面；W2 二宿主之強制帶 s 長與池之強制帶；
           W3 宿主之准否；W4 harness 段三與末端塊合併再試之試算皆為 `'trial'`、`run_corner_pk_k6b` 於段三（或其
           不辦）之後恰一次呼叫 `run_end_block_merge`；W5 `run_end_block_merge` 之隔離與紀錄；W6 `_WF_NS_NAMES`；
           W7 `end_block_merge_run` 之單一真相源（`k6b_stage3_run`）與競合之檢。另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 無標的（`R6` 左端各筆單獨已有當選者·合併再試紀錄
           ＝ 無標的·無皆未達）。另於退縮 `3.5` 實跑四合成案（注入於 harness 之 `ns`·⛔ 改檔）：
           甲 ＝ 假設 `628-4(1)` 跨占街角規定範圍；乙 ＝ 甲 ＋ `628-1(3)` 上鎖；丙 ＝ 乙 ＋ `628-21(1)`、`628-22(1)` 上鎖；
           丁 ＝ `R6` 左端之末端帶以 `13 m` 構之。外部錨 ＝ 本器另寫之幾何與 G 公式（⛔ 呼叫 `end_block_*`／
           `_end_region_R`／`solve_G_binary`）。
           🔧 `W-G.9-354`：甲之停機點由「他街廓已配地而本段無受併宗」移至後處理 (a)（他街廓依原位次配得者照配·
           `K-9-48` 其二·讀法 `1` ⑤；餘片不鄰任一配得之街廓·`K-9-48` 七項 3／5／6 之承前缺口）。
           🔧 `W-G.9-361`（`K-9-54`·地籍相連之判之座標容差）：甲之停機之因改為餘片鄰二配得之街廓（`['R4', 'R6']`·
           目標街廓非恰一）；乙之注入加鎖 `628-22(3)`、`628-23(3)`（`G017` 之 `RD2` 道路片·其受併宗於 `R5` 非恰一），
           故乙 ≠ 丙之前段（丙之鎖同本批前）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

NEW_FUNCS = ["end_block_forced_buf", "end_block_forced_bands", "end_block_merge_run"]
NEW_CONSTS = ["SS_END_BLOCK_MODE", "SS_END_BLOCK_MERGE"]
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _fn_src(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return ast.get_source_segment(src, n)
    return None


# ── 合成幾何（同 F11）：FRONT 沿 x 軸 p1=(0,0)→p2=(40,0)；ALLOC ∥ y 軸；深 30；左端外斜 3 m（未臨正街 45 ㎡）──
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


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__)
    out.append((name, got, exp))


# ── S10 之玩具：一街廓 BX（住宅區）＋ 道路 RX；候選 C1(1)／C2(1)（依原投影序）──
def _toy(a_c1b=40.0, mark=None):
    bx = dict(所屬街廓="BX", 街廓分類="住宅區", 面積_m2=0.0)
    temp = [
        _tp("C1(1)", [(0, 0), (5, 0), (5, 30), (0, 30)], "C1", 分攤登記面積_m2=100.0, **bx),
        _tp("C1(2)", [(5, 0), (10, 0), (10, 30), (5, 30)], "C1B", 分攤登記面積_m2=a_c1b, **bx),
        _tp("C2(1)", [(10, 0), (15, 0), (15, 30), (10, 30)], "C2", 分攤登記面積_m2=90.0, **bx),
        _tp("R2(1)", [(10, -10), (15, -10), (15, 0), (10, 0)], "R2", 分攤登記面積_m2=70.0,
            所屬街廓="RX", 街廓分類="道路", 面積_m2=0.0),
        _tp("D(1)", [(15, 0), (40, 0), (40, 30), (15, 30)], "D", 分攤登記面積_m2=500.0, **bx),
    ]
    if mark:
        for t in temp:
            if t["暫編地號"] == mark:
                t["段三併出"] = ["X(1)"]
    build = [t for t in temp if t["所屬街廓"] == "BX" and not t.get("段三併出")]
    own = {"C1": "g1", "C1B": "g1", "C2": "g2", "R2": "g2", "D": "g3"}
    blocks = {"BX": {"category": "住宅區"}, "RX": {"category": "道路"}}
    return temp, build, own, blocks


def _toy_cb(thr, noaff_bad=False, both_ends=None, fail_probe=False):
    calls = {"eval": 0, "state": 0}

    def a_prime(src, dst):
        return float(src.get("分攤登記面積_m2", 0) or 0) + float(src.get("面積_m2", 0) or 0)

    def alloc_eval(temp, build):
        calls["eval"] += 1
        if fail_probe:
            raise RuntimeError("🔴 注入之配地中止")
        ids = {b["暫編地號"] for b in build}
        by = {b["暫編地號"]: b for b in build}
        out = {}
        for sd, cands in (both_ends or {"left": ["C1(1)", "C2(1)"]}).items():
            rows, win = [], None
            for c in cands:
                if c not in ids:
                    continue
                g = float(by[c].get("分攤登記面積_m2", 0) or 0) + float(by[c].get("面積_m2", 0) or 0)
                ok = g >= thr
                rows.append({"暫編地號": c, "試算G(㎡)": round(g, 2), "結果": "當選" if ok else "未達"})
                if ok:
                    win = c
                    break
            out[sd] = {"觸發": True, "R_end(㎡)": thr, "候選": rows, "當選": win}
        return {"BX": out}

    def alloc_state(temp, build):
        calls["state"] += 1
        by = {b["暫編地號"]: b for b in build}
        bad = 1 if (noaff_bad and float((by.get("C2(1)") or {}).get("面積_m2", 0) or 0) > 0) else 0
        return {"kept": {"BX": set(by)}, "bad_pools": {"BX": bad}, "err": None}
    return a_prime, alloc_eval, alloc_state, calls


def _cases(ns):
    from shapely.geometry import Polygon
    out = []
    G = _geo(ns)
    GM = _geo(ns, mirror=True)
    geo = ns["end_block_side_geom"]
    gg = geo(G["blk"], G["d"], G["p1"], G["p2"], G["cad"], G["ad"], 3.5, "left", _label="T")
    a = _tp("A(1)", [(-3, 30), (-1, 10), (5, 10), (5, 30)])
    b = _tp("B(1)", [(-1, 10), (0, 0), (5, 0), (5, 10)])
    seq = [_e(a), _e(b)]

    def trial(tp):
        return {"A(1)": 100.0, "B(1)": 120.0}[tp["暫編地號"]], 5.0
    pick = ns["end_block_pick"]
    _run(out, "S1 皆未達而准 ⇒ 無當選·列全留",
         lambda: (lambda r: (r["winner"], [x["結果"] for x in r["rows"]]))(
             pick("left", gg, seq, {}, trial, _label="T", allow_forced=True)),
         (None, ["未達", "未達"]))
    _run(out, "S1b 皆未達而不准 ⇒ 停機", lambda: pick("left", gg, seq, {}, trial, _label="T"),
         ("例外", "RuntimeError"))

    apply = ns["end_block_apply"]

    def ap(cache, allow, g=G, order=None, has=None):
        return apply(order or seq, blk_label="BX", block_poly=g["blk"], d_hat=g["d"], corner_pt=g["p1"],
                     front_p2=g["p2"], cad_alloc=g["cad"], allocation_dir=g["ad"], min_width=3.5,
                     has_side_pk=has or {"left": False, "right": True},
                     has_side_cad=has or {"left": False, "right": True},
                     corner_range_polys={}, trial=lambda tp, s, w: trial(tp), cache=cache,
                     allow_forced=allow)

    def s2():
        cache = {}
        o, i = ap(cache, lambda sd: True)
        L = i["left"]
        return ([x["tp"]["暫編地號"] for x in o], L["winner"], L["forced"], round(L["buf"], 4),
                round(L["r_end"].area, 4), cache["BX"]["left"]["當選"], cache["BX"]["left"].get("強制抵費地"),
                any(x.get("is_end_block") for x in o), i["right"])
    _run(out, "S2 強制 ⇒ ⛔ 落位·紀錄當選 None·強制抵費地·buf 3.5·R_end 150", s2,
         (["A(1)", "B(1)"], None, True, 3.5, 150.0, None, True, False, None))
    _run(out, "S3 首趟強制而本趟不准 ⇒ 停機",
         lambda: ap({"BX": {"left": {"觸發": True, "當選": None, "強制抵費地": True}}}, lambda sd: False),
         ("例外", "RuntimeError"))

    def s4():
        n = []
        o, i = apply(seq, blk_label="BX", block_poly=G["blk"], d_hat=G["d"], corner_pt=G["p1"], front_p2=G["p2"],
                     cad_alloc=G["cad"], allocation_dir=G["ad"], min_width=3.5,
                     has_side_pk={"left": False, "right": True}, has_side_cad={"left": False, "right": True},
                     corner_range_polys={}, trial=lambda tp, s, w: (n.append(1), trial(tp))[1],
                     cache={"BX": {"left": {"觸發": True, "當選": None, "強制抵費地": True}}},
                     allow_forced=lambda sd: True)
        return (i["left"]["forced"], len(n), [x["tp"]["暫編地號"] for x in o])
    _run(out, "S4 首趟強制而本趟准 ⇒ 沿用（⛔ 重評）", s4, (True, 0, ["A(1)", "B(1)"]))

    fb = ns["end_block_forced_buf"]

    def s5():
        _, iL = ap({}, lambda sd: True)
        cm = _tp("M(1)", [(35, 0), (40, 0), (43, 30), (35, 30)])
        _, iR = apply([_e(cm)], blk_label="BM", block_poly=GM["blk"], d_hat=GM["d"], corner_pt=GM["p1"],
                      front_p2=GM["p2"], cad_alloc=GM["cad"], allocation_dir=GM["ad"], min_width=3.5,
                      has_side_pk={"left": True, "right": False}, has_side_cad={"left": True, "right": False},
                      corner_range_polys={}, trial=lambda tp, s, w: (1.0, 0.0), cache={},
                      allow_forced=lambda sd: True)
        _, iW = ap({}, lambda sd: True, order=[_e(a), _e(b)])
        iW["left"]["forced"] = False
        return (round(fb(iL, "left"), 4), round(fb(iL, "right"), 4), round(fb(iR, "right"), 4),
                round(fb(iW, "left"), 4), round(fb(None, "left"), 4))
    _run(out, "S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）", s5, (3.5, 0.0, 3.5, 0.0, 0.0))

    bands = ns["end_block_forced_bands"]

    def s6():
        _, i = ap({}, lambda sd: True)
        bs = bands(i)
        i2 = dict(i)
        i2["left"] = dict(i["left"], forced=False)
        return (len(bs), round(bs[0].area, 4), len(bands(i2)), len(bands({"left": None, "right": None})))
    _run(out, "S6 強制帶 ＝ R_end（非強制⛔ 入）", s6, (1, 150.0, 0, 0))

    ah = ns["end_block_assert_head"]
    _run(out, "S7 定案趟：強制側有末端塊之宗 ⇒ 停機",
         lambda: ah("BX", {"left": {"winner": None, "forced": True}, "right": None},
                    [(_e(a, is_end_block=True), {})], []), ("例外", "RuntimeError"))
    _run(out, "S7b 定案趟：強制側無末端塊之宗 ⇒ 過",
         lambda: (ah("BX", {"left": {"winner": None, "forced": True}, "right": None}, [(_e(a), {})], []), "過")[1],
         "過")
    _run(out, "S8 顯示：強制抵費地之列",
         lambda: ns["end_block_eval_rows"]({"BX": {"left": {"觸發": True, "未臨正街(㎡)": 45.0, "末端帶(㎡)": 105.0,
                                                          "R_end(㎡)": 150.0, "當選": None, "強制抵費地": True,
                                                          "候選": []}}})["lines"],
         ["BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；各筆單獨與合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）"])

    host = ns["end_block_host"]

    def hs(sess_extra):
        sess = {"f3_min_width_by_label": {"BX": 3.5},
                "f3L_forced_offset": {"BX": {"left_has_side": False, "right_has_side": True}},
                "f3_cad_side_lines_by_side": {"BX": {"right": {"mid": (40.0, 15.0)}}}}
        sess.update(sess_extra)

        def solve_one(*args, **kw):
            return {"G": 100.0, "S_raw": 5.0}, "stub"
        o, i = host(list(seq), blk_label="BX", blk_poly=G["blk"], d_hat=G["d"], corner_pt=G["p1"], front_p2=G["p2"],
                    alloc_dir_cad=G["cad"], allocation_dir=G["ad"], session=sess, corner_range_polys={},
                    solve_one=solve_one, l_front=1.0, avg_depth=30.0, S_block_max=40.0, post_price=1.0,
                    pre_price_by_zone={})
        return (i["left"]["forced"], i["left"]["winner"])
    MODE, MERGE = ns["SS_END_BLOCK_MODE"], ns["SS_END_BLOCK_MERGE"]
    _run(out, "S9a 宿主：試算 ⇒ 准", lambda: hs({MODE: "trial"}), (True, None))
    _run(out, "S9b 宿主：定案而無紀錄 ⇒ 停機", lambda: hs({}), ("例外", "RuntimeError"))
    _run(out, "S9c 宿主：定案而紀錄（同退縮）載該端 ⇒ 准",
         lambda: hs({"f3L_setback_default": 3.5, MERGE: {"退縮": 3.5, "皆未達": {"BX": ["left"]}}}), (True, None))
    _run(out, "S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機",
         lambda: hs({"f3L_setback_default": 0.0, MERGE: {"退縮": 3.5, "皆未達": {"BX": ["left"]}}}),
         ("例外", "RuntimeError"))
    _run(out, "S9e 宿主：定案而紀錄只載他街廓 ⇒ 停機",
         lambda: hs({"f3L_setback_default": 3.5, MERGE: {"退縮": 3.5, "皆未達": {"BY": ["left"]}}}),
         ("例外", "RuntimeError"))

    mr = ns["end_block_merge_run"]

    def m(thr, a_c1b=40.0, noaff_bad=False, locked=(), corner=(), mark=None, both=None, fail=False):
        temp, build, own, blocks = _toy(a_c1b, mark)
        ap_, ev_, st_, calls = _toy_cb(thr, noaff_bad, both, fail)
        t2, b2, log, rec = mr(temp, build, own, set(locked), set(corner), blocks, {}, ap_, ev_, st_, setback=3.5,
                              log_print=lambda *x: None)
        main = [(r["候選"], r["層級"], r["結果"], r["檢核"]) for r in log if r.get("序") != "後處理"]
        return dict(same=(t2 is temp and b2 is build), rows=main, rec=rec, calls=dict(calls),
                    build=sorted(x["暫編地號"] for x in b2))
    _run(out, "S10a 無標的（C1(1) 單獨即達）⇒ 逕回（同一物件）",
         lambda: (lambda r: (r["same"], r["rec"]["標的"], r["rows"], r["calls"]["state"]))(m(95.0)),
         (True, [], [], 0))
    _run(out, "S10b ① 同街廓成（⛔ 驗不影響原位次）",
         lambda: (lambda r: (r["rows"], r["rec"]["皆未達"], r["calls"]["state"], r["build"]))(m(150.0, a_c1b=60.0)),
         ([("C1(1)", "①", "成", "免"), ("C2(1)", "—", "略·已定案", "—")], {}, 0, ["C1(1)", "C2(1)", "D(1)"]))
    _run(out, "S10c ② 道路成且驗不影響原位次",
         lambda: (lambda r: (r["rows"], r["rec"]["皆未達"], r["calls"]["state"]))(m(150.0)),
         ([("C1(1)", "①", "未成", "—"), ("C2(1)", "②", "成", "通過")], {}, 2))
    _run(out, "S10d ② 之驗不過 ⇒ 未成 ⇒ 皆未達",
         lambda: (lambda r: (r["rows"], r["rec"]["皆未達"]))(m(150.0, noaff_bad=True)),
         ([("C1(1)", "①", "未成", "—"), ("C2(1)", "②", "未成", "不過")], {"BX": ["left"]}))
    _run(out, "S10e 除外：上鎖者⛔ 併入", lambda: m(150.0, a_c1b=60.0, locked={"C1(2)"})["rows"][0],
         ("C1(1)", "—", "未成", "—"))
    _run(out, "S10f 除外：街角第 1 宗⛔ 併入", lambda: m(150.0, a_c1b=60.0, corner={"C1(2)"})["rows"][0],
         ("C1(1)", "—", "未成", "—"))
    _run(out, "S10g 除外：段三已併出者⛔ 併入", lambda: m(150.0, a_c1b=60.0, mark="C1(2)")["rows"][0],
         ("C1(1)", "—", "未成", "—"))
    _run(out, "S10i 試算中止 ⇒ 逕回並記其由",
         lambda: (lambda r: (r["same"], r["rec"]["標的"], "試算中止" in r["rec"]))(m(150.0, fail=True)),
         (True, None, True))
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


SELF_MUTS = [
    ("M1 皆未達⛔ 理准否（恆停機）", "end_block_pick", "    if allow_forced:\n        return {'winner': None, 'rows': rows}",
     "    if False:\n        return {'winner': None, 'rows': rows}"),
    ("M2 宿主恆准", "end_block_host", "        return _mode == 'trial' or side in _mfail", "        return True"),
    ("M3 宿主⛔ 對退縮", "end_block_host",
     "if (_msb is not None and _ssb is not None and abs(float(_msb) - float(_ssb)) < 1e-9) else [])",
     "if True else [])"),
    ("M4 強制帶之 s 長恆 0", "end_block_forced_buf", "    return float(_i['buf'])", "    return 0.0"),
    ("M5 強制⛔ 入池", "end_block_forced_bands", "            _out.append(_i['r_end'])", "            pass"),
    ("M6 段三已併出者⛔ 除外", "end_block_merge_run",
     "          | {t['暫編地號'] for t in temp_parcels if t.get('段三併出')})", "          | set())"),
    ("M8 試算中止⛔ 攔", "end_block_merge_run", "    except RuntimeError as _e:\n        _rec['標的'] = None",
     "    except KeyError as _e:\n        _rec['標的'] = None"),
]


def selftest(repo):
    try:
        ns, _ = _harvest(repo)
    except Exception as ex:  # noqa: BLE001
        print(f"  🔴 harvest 失敗：{type(ex).__name__}")
        print("⇒ 紅 ['harvest']；rc 1")
        return 1
    miss = [n for n in NEW_FUNCS + NEW_CONSTS if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    src = _read(repo, "app.py")
    print("── 合成對照（harvest 之 end_block_*／end_block_merge_run〔其內 k6b_stage3_run 為真〕）──")
    red = _report(_cases(ns))
    base_red = set(red)
    print("── 判別力（突變之函式以其原始碼改一處後重綁於 ns·每一突變須使至少一例轉紅·畢即復原）──")
    for mname, fname, x, y in SELF_MUTS:
        fsrc = _fn_src(src, fname)
        if fsrc is None or fsrc.count(x) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{0 if fsrc is None else fsrc.count(x)}）")
            red.append(mname.split()[0])
            continue
        orig = ns[fname]
        try:
            exec(compile(fsrc.replace(x, y, 1), "<mut>", "exec"), ns)
            turned = [n for n in _report(_cases(ns), verbose=False) if n not in base_red]
        except Exception as ex:  # noqa: BLE001
            turned = [f"重綁拋 {type(ex).__name__}"]
        finally:
            ns[fname] = orig
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    m0 = _report(_cases(ns), verbose=False)
    print(("  ✅ " if m0 == [n for n in red if n in base_red] else "  🔴 ") + f"M0 復原後：紅 {m0}")
    if m0 != [n for n in red if n in base_red]:
        red.append("M0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
def _wiring_checks(app, sg, sel):
    res = []
    tree = ast.parse(app)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    lits = []
    for f in NEW_FUNCS:
        if f in top:
            for n in ast.walk(top[f]):
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value):
                    lits.append((f, n.value))
    res.append(("W1 模組層之二常數與三函式、函式內⛔ 案件字面",
                all(c in consts for c in NEW_CONSTS) and all(f in top for f in NEW_FUNCS) and not lits,
                f"案件字面 {lits}"))
    scr = _fn_src(app, "f3_screen_stepg_run") or ""
    hsg = _fn_src(sg, "_run_step_g_impl") or ""

    def w2(src, fb, fbs):
        s_l = f"left_cum_S += {fb}(_eb_info, 'left')"
        s_r = f"right_cum_S += {fb}(_eb_info, 'right')"
        s_p = f"_fb_p2.extend({fbs}(_eb_info))"
        if not (src.count(s_l) == 1 and src.count(s_r) == 1 and src.count(s_p) == 1):
            return False
        i0, i1 = src.find("right_cum_S = float(_right_buffer_S)"), src.find(s_l)
        i2 = src.find("for entry in left_group:", i1)
        j1 = src.find(s_p)
        j2 = src.find("offset_geoms = _pool_strips_for_block(", j1)
        return 0 <= i0 < i1 < i2 and 0 <= j1 < j2 and "forced_bands=_fb_p2" in src[j2:j2 + 400]
    res.append(("W2 二宿主：強制帶之 s 長入鏈之起點（左鏈之前）、強制帶入池（`_pool_strips_for_block` 之前）",
                w2(scr, "end_block_forced_buf", "end_block_forced_bands")
                and w2(hsg, 'ns["end_block_forced_buf"]', 'ns["end_block_forced_bands"]'), ""))
    host = _fn_src(app, "end_block_host") or ""
    res.append(("W3 宿主之准否：讀 `SS_END_BLOCK_MODE`／`SS_END_BLOCK_MERGE`／退縮，傳 `allow_forced=_allow`",
                all(s in host for s in ("session.get(SS_END_BLOCK_MODE)", "session.get(SS_END_BLOCK_MERGE)",
                                        "session.get('f3L_setback_default')", "allow_forced=_allow"))
                and "allow_forced=_allow" in (_fn_src(app, "end_block_host") or ""), ""))
    cbk = _fn_src(sel, "_k6b_callbacks") or ""
    k6b = _fn_src(sel, "run_corner_pk_k6b") or ""

    def before_stepg(fsrc, fname):
        f = _fn_src(fsrc, fname) or ""
        i = f.find("""ss[ns["SS_END_BLOCK_MODE"]] = 'trial'""")
        j = f.find("run_step_g(ns, fake_st")
        return 0 <= i < j
    ok4 = False
    if cbk:
        inner = {n.name: ast.get_source_segment(cbk, n) for n in ast.walk(ast.parse(cbk))
                 if isinstance(n, ast.FunctionDef)}
        ok4 = all(before_stepg(inner.get(k, ""), k) for k in ("alloc_state", "alloc_eval"))
    kt = ast.parse(k6b) if k6b else None
    calls = []
    if kt is not None:
        fn = kt.body[0]
        for st_ in fn.body:
            for n in ast.walk(st_):
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "run_end_block_merge":
                    calls.append(type(st_).__name__)
    ok4 = ok4 and calls == ["Assign"] and "_cbk['alloc_state']" in k6b
    res.append(("W4 harness：`alloc_state`／`alloc_eval` 於配地前設 `'trial'`；`run_corner_pk_k6b` 於段三之 if／else 之後"
                "（頂層）恰一次呼叫 `run_end_block_merge`，段三亦用同一組回呼", ok4, f"頂層呼叫 {calls}"))
    rem = _fn_src(sel, "run_end_block_merge") or ""
    ok5 = all(s in rem for s in ('ns["end_block_merge_run"](', "finally:", "ss.update(_ss_saved)",
                                 'ns["K917_DROPPED"].update(_k917_saved)', 'ss[ns["SS_END_BLOCK_MERGE"]] = rec',
                                 "setback=setback")) and rem.find("finally:") < rem.find('ss[ns["SS_END_BLOCK_MERGE"]] = rec')
    res.append(("W5 `run_end_block_merge`：隔離（finally 復原 session 與 `K917_DROPPED`）後寫紀錄、帶退縮", ok5, ""))
    wf = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets):
            wf = ast.literal_eval(n.value)
    res.append(("W6 `_WF_NS_NAMES` 含 `end_block_forced_buf`／`end_block_forced_bands`",
                bool(wf) and "end_block_forced_buf" in wf and "end_block_forced_bands" in wf, ""))
    mr = _fn_src(app, "end_block_merge_run") or ""
    ok7 = ("k6b_stage3_run(_rows, _L, own_map" in mr and "k6_merge_groups(_pk, own_map)" in mr
           and "set(locked or ()) | set(corner_lots or ())" in mr)
    res.append(("W7 `end_block_merge_run`：交 `k6b_stage3_run`（單一真相源）、除外三類、競合以合併群查", ok7, ""))
    return res


WIRE_MUTS = [
    ("N1 harness 左鏈⛔ 讓出強制帶", "verify/stepg_pipeline.py",
     "            left_cum_S += ns[\"end_block_forced_buf\"](_eb_info, 'left')\n", "", "W2"),
    ("N2 harness 配地試算⛔ 設 trial", "verify/selection_pipeline.py",
     "            ss[ns[\"SS_END_BLOCK_MODE\"]] = 'trial'   # 🆕 `W-G.9-353`：試算\n", "", "W4"),
    ("N3 宿主⛔ 傳准否", "app.py", "trial=_trial, cache=_cache, allow_forced=_allow)", "trial=_trial, cache=_cache)", "W3"),
    ("N4 畫面⛔ 入池強制帶", "app.py",
     "                _fb_p2.extend(end_block_forced_bands(_eb_info))   # 🆕 `W-G.9-353`：強制抵費地（末）之 `R_end`\n",
     "", "W2"),
]


def wiring(repo):
    app = _read(repo, "app.py")
    sg = _read(repo, "verify/stepg_pipeline.py")
    sel = _read(repo, "verify/selection_pipeline.py")
    print("── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py ＋ verify/selection_pipeline.py）──")
    red = []
    base = _wiring_checks(app, sg, sel)
    for name, ok, note in base:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    for mname, f, x, y, exp in WIRE_MUTS:
        src = {"app.py": app, "verify/stepg_pipeline.py": sg, "verify/selection_pipeline.py": sel}[f]
        n = src.count(x)
        if n != 1:
            print(f"  🔴 {mname}：突變錨不存在（{n}）")
            red.append(mname.split()[0])
            continue
        m = src.replace(x, y, 1)
        a2, s2, l2 = (m if f == "app.py" else app), (m if f == "verify/stepg_pipeline.py" else sg), \
            (m if f == "verify/selection_pipeline.py" else sel)
        turned = [nm.split()[0] for (nm, ok, _), (_, ok0, _) in zip(_wiring_checks(a2, s2, l2), base) if ok0 and not ok]
        ok = exp in turned
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本器另寫之幾何與 G 公式（外部錨·同 F11 之法）──
def _s_of(x, p1, d, u):
    import numpy as np
    v = np.asarray(x, float) - p1
    den = d[0] * u[1] - d[1] * u[0]
    return (v[0] * u[1] - v[1] * u[0]) / den


def _halfplane(p1, d, u, s_lo, s_hi, big):
    from shapely.geometry import Polygon
    a = p1 + s_lo * d
    b = p1 + s_hi * d
    return Polygon([a - big * u, b - big * u, b + big * u, a + big * u])


SCEN = {
    "甲": dict(excl=["628-4(1)"], lock=[], mw=None),
    # 🔧 `W-G.9-361`（`K-9-54`）：地籍相連之判之座標容差 ⇒ `G017` 之合併群含 `R5` 之三宗與 `RD2` 之二道路片；其道路片之
    #   受併宗於 `R5` 非恰一（段三後處理之「承受之宗未定」）⇒ 乙之注入加鎖此二道路片，以存本例之受詞（① 同街廓合併之當選）
    "乙": dict(excl=["628-4(1)"], lock=["628-1(3)", "628-22(3)", "628-23(3)"], mw=None),
    "丙": dict(excl=["628-4(1)"], lock=["628-1(3)", "628-21(1)", "628-22(1)"], mw=None),
    "丁": dict(excl=[], lock=[], mw=13.0),
}


def _pipeline(ns, fake_st, rv, sb, scen=None):
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    from selection_pipeline import run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    saved = {k: ns[k] for k in ("end_block_host", "end_block_merge_run", "end_block_side_geom")}
    cfg = SCEN.get(scen) or dict(excl=[], lock=[], mw=None)
    hits = {"host": 0, "merge": 0, "geo": 0}

    def host(ordered, **kw):
        if kw.get("blk_label") == "R6" and cfg["excl"]:
            crp = dict(kw["corner_range_polys"])
            fake = [Polygon(e["tp"]["polygon_coords"]).buffer(0) for e in ordered
                    if e["tp"].get("暫編地號") in cfg["excl"]]
            if fake:
                hits["host"] += 1
                crp["left"] = unary_union(fake + ([crp["left"]] if crp.get("left") is not None else []))
            kw["corner_range_polys"] = crp
        return saved["end_block_host"](ordered, **kw)

    def merge(temp, build, own, locked, corner, *a, **k):
        if cfg["lock"]:
            hits["merge"] += 1
        return saved["end_block_merge_run"](temp, build, own, set(locked) | set(cfg["lock"]), corner, *a, **k)

    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
        if cfg["mw"] is not None and _label == "R6":
            hits["geo"] += 1
            min_width = cfg["mw"]
        return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
                                            min_width, side, _label=_label)
    ns["end_block_host"], ns["end_block_merge_run"], ns["end_block_side_geom"] = host, merge, geo
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            snapshot = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
            rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        out = dict(cb_by=cb_by, cad=cad, snapshot=snapshot, params=params, hits=hits, err=None)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                    ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
        except RuntimeError as e:
            out["err"] = ("段三／合併再試", str(e).splitlines()[0][:400])
            return out
        ss = fake_st.session_state
        out["rec"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_MERGE"]))
        out["log"] = copy.deepcopy(ss.get("f3_end_block_merge_log") or [])
        out["temp"], out["build"] = tp3, bp3
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ns["K917_DROPPED"].clear()
                sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                                eff_min_build_by_blk={})
        except RuntimeError as e:
            out["err"] = ("配地", str(e).splitlines()[0][:400])
            return out
        out["ev"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_EVAL"]) or {})
        out["rows"] = sg["g_rows"]
        out["mw"] = dict(ss.get("f3_min_width_by_label", {}) or {})
        return out
    finally:
        for k, v in saved.items():
            ns[k] = v


def _anchor_G(ns, P, blk, tp, add_a, rend, fin, snapshot, side="left"):
    """外部錨：末端位之 G（宗地 ＝ 未臨正街 ∪ 正街段之帶；G 之 S 只計正街段）——本器另寫之二分法。"""
    import numpy as np
    from shapely.geometry import Polygon
    bp = Polygon(P["cb_by"][blk]["vertices"]).buffer(0)
    fl = P["cad"]["front_lines"][blk]
    p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
    L = float(np.linalg.norm(p2 - p1))
    d = (p2 - p1) / L
    u = np.array(P["cad"]["alloc_dir_by_block"][blk], float)
    u = u / np.linalg.norm(u)
    big = 4 * float(np.hypot(*(np.array(bp.bounds[2:]) - np.array(bp.bounds[:2]))))
    smin = min(_s_of(v, p1, d, u) for v in bp.exterior.coords)
    l2 = float(fin["sb_rows_by_label"][blk]["正街尺度"])
    post = float(fin["post_price_by_block"][blk])
    a = round(float(tp.get("分攤登記面積_m2", 0) or 0) + float(tp.get("面積_m2", 0) or 0) + add_a, 2)
    pre = float(fin["pre_price_by_zone"].get(tp.get("重劃前地價區段", ""), 0.0) or 0.0)
    A = post / pre if pre > 0 else 1.0
    B, C = fin["B"], fin["C"]
    w = -smin
    lo, hi = 0.0, L
    for _ in range(100):
        m = (lo + hi) / 2
        if bp.intersection(_halfplane(p1, d, u, -w, m, big)).area - (a * (1 - A * B) - m * l2) * (1 - C) < 0:
            lo = m
        else:
            hi = m
    S = (lo + hi) / 2
    return round((a * (1 - A * B) - S * l2) * (1 - C), 2)


def _aprime(snapshot, src, dst):
    fv3 = snapshot["財務接線_v3"]
    z, p = fv3["原地號_區段"], fv3["重劃前區段_面積單價"]
    ps = float(p[z[src["原地號"]]]["單價_元每m2"])
    pd_ = float(p[z[dst["原地號"]]]["單價_元每m2"])
    return (float(src.get("分攤登記面積_m2", 0) or 0) + float(src.get("面積_m2", 0) or 0)) * ps / pd_


def run(repo, sbs):
    import numpy as np
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        if any(n not in ns for n in NEW_FUNCS + NEW_CONSTS):
            print("  🔴 受詞缺：end_block_merge_run 等")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from stepg_pipeline import _compute_v3_finance
        for sb in sbs:
            P = _pipeline(ns, fake_st, rv, sb)
            if P["err"]:
                print(f"🔴 執行中止（退縮 {sb}·{P['err'][0]}）：{P['err'][1]} ⇒ 無從判定")
                return 3
            rec, ev = P["rec"], P["ev"]
            ok = (rec == {"退縮": sb, "標的": [], "皆未達": {}} and P["log"] == []
                  and ((ev.get("R6") or {}).get("left") or {}).get("當選") == "628-4(1)")
            print(("  ✅" if ok else "  🔴") + f" R1 退縮 {sb}：合併再試紀錄 {rec}；逐列 {len(P['log'])}；"
                  f"R6 左當選 {((ev.get('R6') or {}).get('left') or {}).get('當選')}")
            if not ok:
                red.append(f"R1@{sb}")
        sb = 3.5
        fin = None
        for scen in ("甲", "乙", "丙", "丁"):
            P = _pipeline(ns, fake_st, rv, sb, scen)
            if fin is None:
                fin = _compute_v3_finance(ns, P["snapshot"], list(P["cb_by"].values()), P["cad"])
            print(f"══ 合成案{scen}（退縮 {sb}·注入 {SCEN[scen]}·咬到 {P['hits']}）══")
            bit = (P["hits"]["host"] > 0 if SCEN[scen]["excl"] else True) and \
                  (P["hits"]["merge"] > 0 if SCEN[scen]["lock"] else True) and \
                  (P["hits"]["geo"] > 0 if SCEN[scen]["mw"] else True)
            if not bit:
                print("  🔴 注入未咬到 ⇒ 無從判定")
                red.append(f"注入@{scen}")
                continue
            if scen == "甲":
                e = P["err"]
                # 🔧 `W-G.9-361`（`K-9-54`）：`628(3)`（`R5`）與 `R4` 之 `628(1)`、`R6` 之 `628(2)` 隔分配線相鄰 ⇒ 所鄰之 B 內
                #   街廓由 `[]` 改為 `['R4', 'R6']`（目標街廓非恰一·`K-9-51` 射程 ③）；仍停機
                ok = (e is not None and e[0] == "段三／合併再試" and "後處理 (a)" in e[1]
                      and "所鄰之 B 內街廓 ＝ ['R4', 'R6']" in e[1] and "停機款 9" in e[1])
                print(("  ✅" if ok else "  🔴") + " X1 甲：地主 G009 以道路併入成，其合併群之他街廓依原位次配得者照配"
                      f"（`W-G.9-354`·`K-9-48` 其二·讀法 `1` ⑤）；餘片鄰二配得之街廓 ⇒ 後處理 (a) 停機（{e}）")
                if not ok:
                    red.append("X1@甲")
                continue
            if P["err"]:
                print(f"  🔴 執行中止：{P['err']}")
                red.append(f"中止@{scen}")
                continue
            rec, log, ev = P["rec"], P["log"], P["ev"]
            rows = [r for r in P["rows"] if r.get("所屬街廓") == "R6"]
            main = [(r["候選"], r["層級"], r["結果"], r["檢核"]) for r in log if r.get("序") != "後處理"]
            e6 = (ev.get("R6") or {}).get("left") or {}
            by = {t["暫編地號"]: t for t in P["temp"]}
            bp = Polygon(P["cb_by"]["R6"]["vertices"]).buffer(0)
            polys = [(r["暫編地號"], Polygon(r["cut_coords"]).buffer(0), r) for r in rows
                     if r.get("cut_coords") and not isinstance(r.get("cut_coords"), str)]
            un = unary_union([p for _, p, _ in polys])
            ovl = sum(polys[i][1].intersection(polys[j][1]).area for i in range(len(polys))
                      for j in range(i + 1, len(polys)))
            okg = un.symmetric_difference(bp).area <= 0.05 and ovl <= 0.05
            if scen == "乙":
                exp = [("628(2)", "①", "未成", "—"), ("628-1(2)", "①", "未成", "—"), ("628-23(1)", "①", "成", "免")]
                add = sum(_aprime(P["snapshot"], by[x], by["628-23(1)"]) for x in ("628-21(1)", "628-22(1)"))
                tp0 = dict(by["628-23(1)"], 面積_m2=0.0)
                ga = _anchor_G(ns, P, "R6", tp0, add, None, fin, P["snapshot"])
                head = sorted([r for _, _, r in polys if r["推進側別"] == "left"],
                              key=lambda r: float(r.get("累積S(m)", 0) or 0))[0]
                ok = (main == exp and rec["皆未達"] == {} and e6.get("當選") == "628-23(1)"
                      and head["暫編地號"] == "628-23(1)" and abs(float(head["G(㎡)"]) - ga) <= 0.02 and okg)
                print(("  ✅" if ok else "  🔴") + f" X2 乙：逐列 {main}；當選 {e6.get('當選')}；鏈首宗 {head['暫編地號']}"
                      f" G {head['G(㎡)']} ＝ 外部錨 {ga}；聯集 △ 街廓 {un.symmetric_difference(bp).area:.4f}、兩兩疊 {ovl:.4f}")
                if not ok:
                    red.append("X2@乙")
            elif scen == "丙":
                exp = [("628(2)", "①", "未成", "—"), ("628-1(2)", "①", "未成", "—"), ("628-23(1)", "—", "未成", "—")]
                fl = P["cad"]["front_lines"]["R6"]
                p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
                d = (p2 - p1) / float(np.linalg.norm(p2 - p1))
                u = np.array(P["cad"]["alloc_dir_by_block"]["R6"], float)
                u = u / np.linalg.norm(u)
                big = 4 * float(np.hypot(*(np.array(bp.bounds[2:]) - np.array(bp.bounds[:2]))))
                smin = min(_s_of(v, p1, d, u) for v in bp.exterior.coords)
                unf = bp.intersection(_halfplane(p1, d, u, smin - 1.0, 0.0, big))
                mw = float(P["mw"].get("R6", 0.0))
                band = bp.intersection(_halfplane(p1, d, u, 0.0, mw / abs(float(np.dot(d, np.array([-u[1], u[0]])))), big))
                rend = unary_union([unf, band])
                pools = [(k, p) for k, p, r in polys if "抵費地" in k]
                fp = [(k, p) for k, p in pools if abs(p.area - rend.area) <= 0.05 and p.symmetric_difference(rend).area <= 0.05]
                lots = [p for k, p, r in polys if "抵費地" not in k]
                lx = sum(p.intersection(rend).area for p in lots)
                ok = (main == exp and rec["皆未達"] == {"R6": ["left"]} and e6.get("當選") is None
                      and e6.get("強制抵費地") is True and len(fp) == 1 and lx <= 1e-4 and okg
                      and abs(float(e6.get("R_end(㎡)")) - round(rend.area, 2)) <= 0.011)
                print(("  ✅" if ok else "  🔴") + f" X3 丙：逐列 {main}；皆未達 {rec['皆未達']}；強制抵費地 {fp and fp[0][0]}"
                      f"（{fp and round(fp[0][1].area, 2)}·外部錨 R_end {rend.area:.2f}·紀錄 {e6.get('R_end(㎡)')}）；"
                      f"宗地 ∩ R_end {lx:.6f}；聯集 △ 街廓 {un.symmetric_difference(bp).area:.4f}、兩兩疊 {ovl:.4f}")
                if not ok:
                    red.append("X3@丙")
            else:
                exp_head = [("628(2)", "②", "未成", "—"), ("628-1(2)", "②", "未成", "—"),
                            ("628-23(1)", "①", "未成", "—"), ("628-4(1)", "②", "成", "通過")]
                add = _aprime(P["snapshot"], by["628-4(2)"], by["628-4(1)"])
                tp0 = dict(by["628-4(1)"], 面積_m2=0.0)
                ga = _anchor_G(ns, P, "R6", tp0, add, None, fin, P["snapshot"])
                head = sorted([r for _, _, r in polys if r["推進側別"] == "left"],
                              key=lambda r: float(r.get("累積S(m)", 0) or 0))[0]
                ok = (main[:4] == exp_head and all(x[2] == "略·已定案" for x in main[4:]) and rec["皆未達"] == {}
                      and e6.get("當選") == "628-4(1)" and head["暫編地號"] == "628-4(1)"
                      and abs(float(head["G(㎡)"]) - ga) <= 0.02 and okg)
                print(("  ✅" if ok else "  🔴") + f" X4 丁：逐列 {main}；當選 {e6.get('當選')}（R_end {e6.get('R_end(㎡)')}）；"
                      f"鏈首宗 {head['暫編地號']} G {head['G(㎡)']} ＝ 外部錨 {ga}；聯集 △ 街廓 "
                      f"{un.symmetric_difference(bp).area:.4f}、兩兩疊 {ovl:.4f}")
                if not ok:
                    red.append("X4@丁")
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
