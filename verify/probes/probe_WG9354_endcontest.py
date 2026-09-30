# -*- coding: utf-8 -*-
"""W-G.9-354 量測器（發單側窗五十擬·檔 F13·⛔ 由受單側改一字）：數末端塊合併再試之競合（`K-9-50`）
＋ 段三後處理之承前（`K-9-48` 其二·讀法 `1` ⑤：無本段受併宗之街廓，其依原位次配得之宗照配並承受分往該街廓之土地；
道路片全在中心線之一側者不切）。

子命令（一律 python verify/probes/probe_WG9354_endcontest.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `end_block_merge_run`〔其內 `k6b_stage3_run` 為真〕）。
           玩具一（題一）：街廓 BX（上）與 BY（下）隔道路 RX 相對，地主甲（g1）之 X1(1)／X2(1)（BX）、X3(1)（RX）、
           Y1(1)／Y2(1)（BY）；道路中心線 y ＝ -4（X3 切為 0.4／0.6）。TA〜TM ＝ 題一之各支（① 二端成／① 一端成而
           他端整片成·不成（其候選配得／不配得）／切半二端成／切半一端成而他端之候選連其半配得／不配得／整片一端成／
           整片二端成而交面積大者／並列而暫編地號小者／皆不成而他人續試／夥伴之端先由他人定案〔逐列〕／夥伴之端於
           擱置中由他人定案〔釋出〕／公設片平分）。玩具二（題二）：一街廓 BZ 左右端，甲 Z1(1)／Z4(1)／Z2(1) 相連、
           道路片 Z3(1)。TN〜TR ＝ 題二之各支（① 只一端／① 二端而交面積大者／並列而 p1 側／② 只一端／皆不成）。
           H1〜H3 ＝ 停機（三個以上之末端塊／一筆土地同時跨占二末端塊／一端屬二競合）。P1〜P3 ＝ 後處理承前（他街廓
           依原位次配得之宗照配／須承受而配得者二筆 ⇒ 停機／唯一 ⇒ 承受公設平分之分）。S1 ＝ 道路片全在中心線之
           一側 ⇒ 不切、全歸該側。另施十四突變，每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST／字樣：W1 `end_block_merge_run` 交競合（`contests=(_ct or None)`）、三以上／一端二競合之停機；
           W2 `k6b_stage3_run` 之 `contests=None`、逐列之環經 `_k950_rows`、無競合 ⇒ 逐列依序（`yield from rows`）；
           W3 段三之二呼叫端（harness `run_corner_pk_k6b`、畫面 `f3_screen_k6b_stage3`）⛔ 給競合；W4 道路切分之
           單一真相源（`_road_halves` 之二呼叫）；W5 後處理之承受（`_stay`／`_recv_of`）；W6 ⛔ 案件字面。
           另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 無標的 ⇒ 紀錄⛔ 載競合。另於退縮 `3.5` 實跑三合成案（注入於
           harness 之 `ns`·⛔ 改檔）——`R3` 左端與 `R5` 右端（隔 `RD2` 相對）以所給之寬構末端帶（⛔ 未臨正街）：
           甲 ＝ 寬 `8`／`16`（地主 `G009` 之 `628(4)`／`628(3)` 競合·皆不成 ⇒ `R5` 右端由 `628-23(2)` 續試而成；
           🔧 `W-G.9-361`：`G017` 之 `R6` 三片上鎖〔`K-9-54` 後其合併群跨 `R5`／`R6`〕）；
           乙 ＝ 寬 `8`／`5.5`，`628-23(2)` 假設跨占街角規定範圍、`G009` 他街廓之片上鎖（整片只 `R5` 成）；
           丙 ＝ 寬 `8`／`5.0`，同乙（切半只 `R5` 成，`628(4)` 連其半併入 `628(3)`）。外部錨 ＝ 本器另寫之末端帶、
           交面積、切半之比與 G 公式（⛔ 呼叫 `end_block_*`／`_end_band`／`_end_region_R`／`solve_G_binary`）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

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


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__, str(ex)[:160])
    out.append((name, got, exp))


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)
    return red


# ── 玩具 ──
def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a, lot=None):
    return {"暫編地號": pid, "原地號": lot or pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


H = "住宅區"


def _world1(a=None, extra=(), own_extra=None, x3_cat="道路", split_by=False, x5=False):
    """題一之玩具。道路 RX 之中心線 y ＝ -4 ⇒ X3(1)（y∈[-10,0]）切為上 0.4（鄰 BX）／下 0.6（鄰 BY）。"""
    a = dict(dict(X1=100, X2=60, X3=80, Y1=90, Y2=50, K1=70, K2=40, P=900, Q=900, R0=350, M1=30, M2=40, X5=20),
             **(a or {}))
    x3_blk = "RX" if x3_cat == "道路" else "PX"
    t = [_tp("X1(1)", "BX", H, _R(0, 5, 0, 30), a["X1"]), _tp("X2(1)", "BX", H, _R(5, 10, 0, 30), a["X2"]),
         _tp("K1(1)", "BX", H, _R(10, 15, 0, 30), a["K1"]), _tp("K2(1)", "BX", H, _R(15, 20, 0, 30), a["K2"]),
         _tp("P(1)", "BX", H, _R(20, 40, 0, 30), a["P"]),
         _tp("X3(1)", x3_blk, x3_cat, _R(0, 5, -10, 0), a["X3"]),
         _tp("Y1(1)", "BY", H, _R(0, 5, -40, -10), a["Y1"]), _tp("Y2(1)", "BY", H, _R(5, 10, -40, -10), a["Y2"])]
    if x5:
        t += [_tp("X5(1)", "RX", "道路", _R(5, 10, -3, 0), a["X5"]), _tp("R0(1)", "RX", "道路", _R(10, 40, -10, 0), a["R0"]),
              _tp("R9(1)", "RX", "道路", _R(5, 10, -10, -3), 5.0)]
    else:
        t += [_tp("R0(1)", "RX", "道路", _R(5, 40, -10, 0), a["R0"])]
    if split_by:
        t += [_tp("M1(1)", "BY", H, _R(10, 15, -40, -10), a["M1"]), _tp("M2(1)", "BY", H, _R(15, 20, -40, -10), a["M2"]),
              _tp("Q(1)", "BY", H, _R(20, 40, -40, -10), a["Q"])]
    else:
        t += [_tp("Q(1)", "BY", H, _R(10, 40, -40, -10), a["Q"])]
    t += [dict(e) for e in extra]
    own = {"X1": "g1", "X2": "g1", "X3": "g1", "X5": "g1", "Y1": "g1", "Y2": "g1", "K1": "gK", "K2": "gK",
           "P": "gP", "Q": "gQ", "R0": "gR", "R9": "gR", "M1": "gM", "M2": "gM"}
    own.update(own_extra or {})
    blocks = {"BX": {"category": H}, "BY": {"category": H}, "RX": {"category": "道路"}}
    if x3_cat != "道路":
        blocks["PX"] = {"category": x3_cat}
    for e in extra:
        blocks.setdefault(e["所屬街廓"], {"category": e["街廓分類"]})
    cl = {"RX": [(-10.0, -4.0), (50.0, -4.0)]}
    return t, own, blocks, cl


def _world2(a=None):
    """題二之玩具：一街廓 BZ（x∈[0,40]）；甲 Z1(1)[0,5]／Z4(1)[5,30]／Z2(1)[30,35]；他人 W1(1)[35,40]（右端最外）；
    道路 RZ：甲 Z3(1)[0,20]、他人 W3(1)[20,40]；他人 W2(1) 於 BW。"""
    a = dict(dict(Z1=100, Z4=200, Z2=80, W1=60, W2=90, Z3=70, W3=300), **(a or {}))
    t = [_tp("Z1(1)", "BZ", H, _R(0, 5, 0, 30), a["Z1"]), _tp("Z4(1)", "BZ", H, _R(5, 30, 0, 30), a["Z4"]),
         _tp("Z2(1)", "BZ", H, _R(30, 35, 0, 30), a["Z2"]), _tp("W1(1)", "BZ", H, _R(35, 40, 0, 30), a["W1"]),
         _tp("Z3(1)", "RZ", "道路", _R(0, 20, -10, 0), a["Z3"]), _tp("W3(1)", "RZ", "道路", _R(20, 40, -10, 0), a["W3"]),
         _tp("W2(1)", "BW", H, _R(35, 40, -40, -10), a["W2"])]
    own = {"Z1": "g1", "Z4": "g1", "Z2": "g1", "Z3": "g1", "W1": "gW", "W3": "gW", "W2": "gW"}
    blocks = {"BZ": {"category": H}, "RZ": {"category": "道路"}, "BW": {"category": H}}
    return t, own, blocks, {"RZ": [(-10.0, -5.0), (50.0, -5.0)]}


def _cbs(targets, drop=(), bad_if_grow=()):
    """玩具之回呼：`alloc_eval` 以 G ＝ 分攤登記面積 ＋ 面積（a′ 之累加）逐端依所給之候選序評選（門檻 ＝ R_end）；
    `alloc_state` 以 `drop` 為恆不配得之宗、`bad_if_grow` 之宗一旦受併即使其街廓之配餘地不合格。"""
    def g(t):
        return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)

    def a_prime(src, dst):
        return g(src)

    def alloc_eval(temp, build):
        by = {b["暫編地號"]: b for b in build}
        out = {}
        for (blk, sd), cfg in targets.items():
            rows, win = [], None
            for c in cfg["cands"]:
                if c not in by:
                    continue
                ok = g(by[c]) >= cfg["thr"]
                rows.append({"暫編地號": c, "原地號": by[c]["原地號"], "跨占R_end(㎡)": cfg.get("cross", {}).get(c, 10.0),
                             "試算G(㎡)": round(g(by[c]), 2), "臨正街寬(m)": 5.0, "結果": "當選" if ok else "未達"})
                if ok:
                    win = c
                    break
            out.setdefault(blk, {})[sd] = {"觸發": True, "R_end(㎡)": cfg["thr"], "候選": rows, "當選": win}
        return out

    def alloc_state(temp, build):
        kept, bad = {}, {}
        for b in build:
            if b["暫編地號"] in drop:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            if b["暫編地號"] in bad_if_grow and float(b.get("面積_m2", 0) or 0) > 0:
                bad[b["所屬街廓"]] = bad.get(b["所屬街廓"], 0) + 1
        return {"kept": kept, "bad_pools": bad, "err": None}
    return a_prime, alloc_eval, alloc_state


def _go(ns, world, targets, **kw):
    temp, own, blocks, cl = world
    temp = copy.deepcopy(temp)
    build = [t for t in temp if t["街廓分類"] == H]
    ap, ev, st = _cbs(targets, **kw)
    t2, b2, log, rec = ns["end_block_merge_run"](temp, build, own, set(), set(), blocks, cl, ap, ev, st,
                                                 setback=3.5, log_print=lambda *x: None)
    by = {t["暫編地號"]: t for t in t2}
    main = [(x["候選"], x["層級"], x["結果"], x["檢核"]) for x in log if x.get("序") != "後處理"]
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]))
            for x in log if x.get("序") == "後處理"]
    ar = {k: round(float(v.get("面積_m2", 0) or 0), 4) for k, v in by.items() if float(v.get("面積_m2", 0) or 0)}
    bl = sorted(b["暫編地號"] for b in b2)
    return main, post, rec.get("皆未達"), ar, bl


def _halt(ns, world, targets, phrase, **kw):
    try:
        _go(ns, world, targets, **kw)
    except RuntimeError as e:
        return ("停機", phrase in str(e))
    return ("無停機",)


A1, B1 = ("BX", "left"), ("BY", "left")


def _T(thrA, thrB, cA=None, cB=None, ca=("X1(1)", "X2(1)", "K1(1)"), cb=("Y1(1)", "Y2(1)")):
    return {A1: dict(thr=thrA, cands=list(ca), cross=cA or {}), B1: dict(thr=thrB, cands=list(cb), cross=cB or {})}


L2, R2 = ("BZ", "left"), ("BZ", "right")


def _T2(thrL, thrR, cL=None, cR=None):
    return {L2: dict(thr=thrL, cands=["Z1(1)"], cross=cL or {}),
            R2: dict(thr=thrR, cands=["W1(1)", "Z2(1)"], cross=cR or {})}


_D = ("X2(1)", "—", "略·已定案", "—")
_K = ("K1(1)", "—", "略·已定案", "—")
_YD = ("Y2(1)", "—", "略·已定案", "—")
_YS = ("Y2(1)", "—", "略·競合歸他端", "—")


def _cases(ns):
    out = []
    w = _world1()
    # X1 100／X2 60／X3 80（上 32·下 48）／Y1 90／Y2 50；甲於 BX 之相連 ＝ 160，於 BY ＝ 140
    _run(out, "TA 題一 ① 二端皆以本街廓內之土地成 ⇒ 道路於後處理依中心線切分各歸",
         lambda: _go(ns, w, _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {}, {"X1(1)": 92.0, "Y1(1)": 98.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TB 題一 ① 只 A 成 ⇒ 只一端需要 ⇒ B 整片成",
         lambda: _go(ns, w, _T(160, 220)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "②", "成", "通過"), _D, _K, _YD], [], {},
          {"X1(1)": 60.0, "Y1(1)": 130.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TC 題一 ① 只 A 成、B 整片未成（Y1 配得）⇒ 道路之下半併 Y1、Y2 照配",
         lambda: _go(ns, w, _T(160, 300)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "②", "未成", "—"), _D, _K, _YS],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {"BY": ["left"]}, {"X1(1)": 92.0, "Y1(1)": 48.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TD 題一 ① 只 A 成、B 整片未成（Y1 不配得）⇒ Y1 併入 X1、道路之下半併 Y2",
         lambda: _go(ns, w, _T(160, 300), drop={"Y1(1)"}),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "②", "未成", "—"), _D, _K, _YS],
          [("Y1(1)", "後處理(a)", "成", "X1(1)"), ("X3(1)", "後處理(b)", "成", ("X1(1)", "Y2(1)"))], {"BY": ["left"]},
          {"X1(1)": 182.0, "Y2(1)": 48.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y2(1)"]))
    _run(out, "TE 題一 切半二端皆成（上 0.4／下 0.6）",
         lambda: _go(ns, w, _T(190, 185)),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "成", "通過"), _D, _K, _YD], [], {},
          {"X1(1)": 92.0, "Y1(1)": 98.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TF 題一 切半只 A 成、Y1 連其半配得 ⇒ 其半併 Y1",
         lambda: _go(ns, w, _T(190, 189)),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "未成", "—"), _D, _K, _YS],
          [("Y1(1)", "題一 4", "成", "Y1(1)")], {"BY": ["left"]}, {"X1(1)": 92.0, "Y1(1)": 48.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TG 題一 切半只 A 成、Y1 連其半不能配得 ⇒ 連同其半併入 X1",
         lambda: _go(ns, w, _T(190, 189), bad_if_grow={"Y1(1)"}),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "未成", "—"), _D, _K, _YS],
          [("Y1(1)", "題一 4", "成", "X1(1)")], {"BY": ["left"]}, {"X1(1)": 230.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y2(1)"]))
    _run(out, "TH 題一 整片只 A 成",
         lambda: _go(ns, w, _T(230, 225)),
         ([("X1(1)", "②", "成", "通過"), ("Y1(1)", "②", "未成", "—"), _D, _K, _YS], [], {"BY": ["left"]},
          {"X1(1)": 140.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TI 題一 整片二端皆成 ⇒ 交面積大者（B 30 ＞ A 15）；A 續試他人",
         lambda: _go(ns, w, _T(230, 210, cA={"X1(1)": 10, "X2(1)": 5}, cB={"Y1(1)": 20})),
         ([("Y1(1)", "②", "成", "通過"), ("X1(1)", "②", "未成", "通過"), ("X2(1)", "—", "略·競合歸他端", "—"),
           ("K1(1)", "①", "未成", "—"), _YD], [], {"BX": ["left"]}, {"Y1(1)": 130.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "X2(1)", "Y1(1)"]))
    _run(out, "TJ 題一 整片二端皆成·交面積並列 ⇒ 跨占者暫編地號小者",
         lambda: _go(ns, w, _T(230, 210, cA={"X1(1)": 10}, cB={"Y1(1)": 10})),
         ([("X1(1)", "②", "成", "通過"), ("Y1(1)", "②", "未成", "通過"), _D, _K, _YS], [], {"BY": ["left"]},
          {"X1(1)": 140.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TK 題一 皆不成 ⇒ 二端皆⛔ 併；A 由他人（K1 併 K2）續試而成",
         lambda: _go(ns, _world1({"K2": 200}), _T(250, 300, ca=("X1(1)", "K1(1)"))),
         ([("X1(1)", "②", "未成", "—"), ("Y1(1)", "②", "未成", "—"), ("K1(1)", "①", "成", "免"), _YS], [],
          {"BY": ["left"]}, {"K1(1)": 200.0}, ["K1(1)", "P(1)", "Q(1)", "X1(1)", "X2(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TL 題一 夥伴之端先由他人定案 ⇒ 競合消滅·逐列（B 整片成）",
         lambda: _go(ns, w, _T(105, 215, ca=("K1(1)", "X1(1)"))),
         ([("K1(1)", "①", "成", "免"), ("X1(1)", "—", "略·已定案", "—"), ("Y1(1)", "②", "成", "通過"), _YD], [], {},
          {"K1(1)": 40.0, "Y1(1)": 130.0}, ["K1(1)", "P(1)", "Q(1)", "X1(1)", "X2(1)", "Y1(1)"]))
    _run(out, "TM 題一 A 擱置中 B 由他人（M1 併 M2）定案 ⇒ 釋出·A 逐列成（Y2 不配得 ⇒ 併 Y1）",
         lambda: _go(ns, _world1({"M2": 100}, split_by=True), _T(150, 120, ca=("X1(1)",), cb=("M1(1)", "Y1(1)")),
                     drop={"Y2(1)"}),
         ([("M1(1)", "①", "成", "免"), ("X1(1)", "①", "成", "免"), ("Y1(1)", "—", "略·已定案", "—")],
          [("Y2(1)", "後處理(a)", "成", "Y1(1)"), ("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {},
          {"M1(1)": 100.0, "X1(1)": 92.0, "Y1(1)": 98.0}, ["K1(1)", "K2(1)", "M1(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TN 題一 公設片平分（0.5／0.5）二端皆成",
         lambda: _go(ns, _world1(x3_cat="鄰里公園"), _T(200, 180)),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "成", "通過"), _D, _K, _YD], [], {},
          {"X1(1)": 100.0, "Y1(1)": 90.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    w2 = _world2()
    # 甲相連 ＝ Z1 100 ＋ Z4 200 ＋ Z2 80 ＝ 380；＋ Z3 70 ＝ 450；W1 ＋ W3 ＝ 360
    _W1 = ("W1(1)", "②", "未成", "—")
    _run(out, "TO 題二 ① 只左拿得下",
         lambda: _go(ns, w2, _T2(380, 400)),
         ([_W1, ("Z1(1)", "①", "成", "免"), ("Z2(1)", "①", "未成", "—")], [("Z3(1)", "後處理(b)", "成", "Z1(1)")],
          {"BZ": ["right"]}, {"Z1(1)": 350.0}, ["W1(1)", "W2(1)", "Z1(1)"]))
    _run(out, "TP 題二 ① 二端皆拿得下 ⇒ 交面積大者（右 20 ＞ 左 10）",
         lambda: _go(ns, w2, _T2(380, 380, cL={"Z1(1)": 10}, cR={"Z2(1)": 20})),
         ([_W1, ("Z2(1)", "①", "成", "免"), ("Z1(1)", "①", "未成", "免")], [("Z3(1)", "後處理(b)", "成", "Z2(1)")],
          {"BZ": ["left"]}, {"Z2(1)": 370.0}, ["W1(1)", "W2(1)", "Z2(1)"]))
    _run(out, "TQ 題二 ① 二端皆拿得下·交面積並列 ⇒ 前緣線 p1 側（左）",
         lambda: _go(ns, w2, _T2(380, 380, cL={"Z1(1)": 10}, cR={"Z2(1)": 10})),
         ([_W1, ("Z1(1)", "①", "成", "免"), ("Z2(1)", "①", "未成", "免")], [("Z3(1)", "後處理(b)", "成", "Z1(1)")],
          {"BZ": ["right"]}, {"Z1(1)": 350.0}, ["W1(1)", "W2(1)", "Z1(1)"]))
    _run(out, "TR 題二 ② 只右拿得下",
         lambda: _go(ns, w2, _T2(460, 440)),
         ([_W1, ("Z2(1)", "②", "成", "通過"), ("Z1(1)", "②", "未成", "—")], [], {"BZ": ["left"]},
          {"Z2(1)": 370.0}, ["W1(1)", "W2(1)", "Z2(1)"]))
    _run(out, "TS 題二 二端皆拿不下 ⇒ 皆⛔ 併",
         lambda: _go(ns, w2, _T2(500, 500)),
         ([_W1, ("Z1(1)", "—", "未成", "—"), ("Z2(1)", "—", "未成", "—")], [], {"BZ": ["left", "right"]}, {},
          ["W1(1)", "W2(1)", "Z1(1)", "Z2(1)", "Z4(1)"]))
    # ── 停機 ──
    _run(out, "H1 同一合併群之候選分屬三個末端塊 ⇒ 停機",
         lambda: _halt(ns, w, {A1: dict(thr=500, cands=["X1(1)"]), B1: dict(thr=500, cands=["Y1(1)"]),
                               ("BY", "right"): dict(thr=500, cands=["Y2(1)"])}, "[末端塊合併再試] 同一合併群"),
         ("停機", True))
    _run(out, "H2 一筆土地同時跨占二末端塊 ⇒ 停機",
         lambda: _halt(ns, w, {A1: dict(thr=500, cands=["X1(1)"]), ("BX", "right"): dict(thr=500, cands=["X1(1)"])},
                       "一筆土地同時跨占二末端塊"), ("停機", True))
    wk = _world1(extra=[_tp("KR(1)", "RX", "道路", _R(40, 45, -10, 0), 20), _tp("K3(1)", "BY", H, _R(40, 45, -40, -10), 20),
                        _tp("K4(1)", "BX", H, _R(40, 45, 0, 30), 20)],
                 own_extra={"KR": "gK", "K3": "gK", "K4": "gK"})
    _run(out, "H3 一末端塊屬二競合 ⇒ 停機",
         lambda: _halt(ns, wk, {A1: dict(thr=500, cands=["X1(1)", "K4(1)"]), B1: dict(thr=500, cands=["Y1(1)"]),
                                ("BY", "right"): dict(thr=500, cands=["K3(1)"])}, "屬二以上之競合（K-9-50 射程 ③·逐案呈核）"),
         ("停機", True))
    # ── 後處理之承前 ──
    wp1 = _world1(extra=[_tp("W5(1)", "BW", H, _R(5, 10, -60, -40), 30)], own_extra={"W5": "g1"})
    _run(out, "P1 他街廓依原位次配得之宗照配（⛔ 動·⛔ 停機）",
         lambda: _go(ns, wp1, _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {}, {"X1(1)": 92.0, "Y1(1)": 98.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "W5(1)", "X1(1)", "Y1(1)"]))
    wp2 = _world1(extra=[_tp("G5(1)", "PK", "鄰里公園", _R(-10, 0, 0, 30), 90), _tp("W5(1)", "BW", H, _R(5, 10, -60, -40), 30),
                         _tp("W6(1)", "BW", H, _R(10, 15, -60, -40), 30)],
                  own_extra={"G5": "g1", "W5": "g1", "W6": "g1"})
    _run(out, "P2 公設片平分須由 BW 承受而其配得之宗二筆 ⇒ 停機（承受之宗未定）",
         lambda: _halt(ns, wp2, _T(160, 140), "承受之宗未定"), ("停機", True))
    wp3 = _world1(extra=[_tp("G5(1)", "PK", "鄰里公園", _R(-10, 0, 0, 30), 90), _tp("W5(1)", "BW", H, _R(5, 10, -60, -40), 30)],
                  own_extra={"G5": "g1", "W5": "g1"})
    _run(out, "P3 公設片三街廓平分，BW 由其唯一配得之宗承受",
         lambda: _go(ns, wp3, _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)")), ("G5(1)", "後處理(c)", "成", ("W5(1)", "X1(1)", "Y1(1)"))],
          {}, {"W5(1)": 30.0, "X1(1)": 122.0, "Y1(1)": 128.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "W5(1)", "X1(1)", "Y1(1)"]))
    _run(out, "S1 道路片全在中心線之一側（X5）⇒ 不切、全歸該側",
         lambda: _go(ns, _world1(x5=True), _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)")), ("X5(1)", "後處理(b)", "成", "X1(1)")], {},
          {"X1(1)": 112.0, "Y1(1)": 98.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    return out


SELF_MUTS = [
    ("M1 ⛔ 交競合（逐列）", "end_block_merge_run", "contests=(_ct or None))", "contests=None)"),
    ("M2 交面積之比較反向", "k6b_stage3_run",
     "return (A, B) if float(A['area']) > float(B['area']) else (B, A)",
     "return (B, A) if float(A['area']) > float(B['area']) else (A, B)"),
    ("M3 並列取暫編地號大者", "k6b_stage3_run", "return (A, B) if A['c'] < B['c'] else (B, A)",
     "return (B, A) if A['c'] < B['c'] else (A, B)"),
    ("M4 並列取 p2 側", "k6b_stage3_run", "return (A, B) if A['end'] == '左' else (B, A)",
     "return (B, A) if A['end'] == '左' else (A, B)"),
    ("M5 ⛔ 切半", "k6b_stage3_run", "_rh[e['k']] = _ct_try(e, _its, '②半')",
     "_rh[e['k']] = dict(_ct_try(e, _its, '②半'), ok=False)"),
    ("M6 未得之一端恆併入已取得之一端", "k6b_stage3_run", "if (Lo['c'] in _kb1 and not (_kb0 - _kb1)",
     "if (False and Lo['c'] in _kb1 and not (_kb0 - _kb1)"),
    ("M7 ⛔ 查三以上", "end_block_merge_run", "            if len(_hit) >= 3:", "            if False:"),
    ("M8 ⛔ 查一端二競合", "end_block_merge_run", "                if (_blk, _sd) in _tgc:", "                if False:"),
    ("M9 未得之一端⛔ 略同群之候選", "k6b_stage3_run",
     "            _skip.setdefault((e['blk'], e['end']), set()).update(_mem)", "            pass"),
    ("M10 無受併宗街廓之配得者⛔ 照配", "k6b_stage3_run", "        R = R - _stay\n", "        R = R\n"),
    ("M11 未得之一端之土地⛔ 歸已取得之一端", "k6b_stage3_run",
     "                    _cls['a'].append((x, _cl0['勝']['blk']))\n                    continue",
     "                    pass"),
    ("M12 道路片須恰切二", "k6b_stage3_run", "        if len(_parts) not in (1, 2):", "        if len(_parts) != 2:"),
    ("M13 ⛔ 擱置（逐列）", "k6b_stage3_run",
     "                elif _ci not in _susp:\n                    _susp[_ci] = [_r]\n                    continue",
     "                elif False:\n                    pass"),
    ("M14 夥伴之端定案⛔ 釋出", "k6b_stage3_run", "            if (not _was) and _tg in won:",
     "            if False:"),
]


def selftest(repo):
    try:
        ns, _ = _harvest(repo)
    except Exception as ex:  # noqa: BLE001
        print(f"  🔴 harvest 失敗：{type(ex).__name__}")
        print("⇒ 紅 ['harvest']；rc 1")
        return 1
    src = _read(repo, "app.py")
    if "contests=None" not in (_fn_src(src, "k6b_stage3_run") or "")[:400]:
        print("  🔴 受詞缺：k6b_stage3_run 之 contests")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（harvest 之 end_block_merge_run〔其內 k6b_stage3_run 為真〕）──")
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
            turned = [n.split()[0] for n in _report(_cases(ns), verbose=False) if n not in base_red]
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
def _wiring_checks(app, sel):
    res = []
    mr = _fn_src(app, "end_block_merge_run") or ""
    ok1 = (mr.count("contests=(_ct or None))") == 1 and "if len(_hit) >= 3:" in mr and "if (_blk, _sd) in _tgc:" in mr
           and "'形': ('二' if _hit[0][0] == _hit[1][0] else '一')" in mr and "k6b_stage3_run(_rows, _L, own_map" in mr)
    res.append(("W1 `end_block_merge_run` 交競合、三以上與一端二競合停機、題一／題二依街廓之同異", ok1, ""))
    k6 = _fn_src(app, "k6b_stage3_run") or ""
    ok2 = False
    if k6:
        fn = ast.parse(k6).body[0]
        kws = [a.arg for a in fn.args.kwonlyargs]
        dflt = {a.arg: d for a, d in zip(fn.args.kwonlyargs, fn.args.kw_defaults)}
        inner = {n.name: ast.get_source_segment(k6, n) for n in ast.walk(fn) if isinstance(n, ast.FunctionDef)}
        g = inner.get("_k950_rows") or ""
        ok2 = ("contests" in kws and isinstance(dflt.get("contests"), ast.Constant) and dflt["contests"].value is None
               and k6.count("for _r in _k950_rows(sorted(order, key=lambda r: r['最終序位'])):") == 1
               and "if not contests:\n            yield from rows\n            return" in g)
    res.append(("W2 `k6b_stage3_run`：`contests=None`、逐列之環經 `_k950_rows`、無競合 ⇒ 逐列依序", ok2, ""))
    k6c = _fn_src(sel, "run_corner_pk_k6b") or ""
    scr = _fn_src(app, "f3_screen_k6b_stage3") or ""
    ci = k6c.find('ns["k6b_stage3_run"](')
    si = scr.find("k6b_stage3_run(")
    ok3 = (ci >= 0 and si >= 0 and "contests" not in k6c[ci:ci + 400].split("finally:")[0]
           and "contests" not in scr[si:si + 400].split("finally:")[0])
    res.append(("W3 段三之二呼叫端（harness／畫面）⛔ 給競合", ok3, ""))
    ok4 = (k6.count("_road_halves(x, '") == 2 and k6.count("def _road_halves(") == 1
           and "_split(_geo[x], _line)" in k6 and k6.count("_split(") == 1)
    res.append(("W4 道路片之中心線切分 ＝ 單一真相源（後處理 (b) 與題一之切半）", ok4, ""))
    ok5 = ("R = R - _stay" in k6 and k6.count("_recv_of(") >= 5 and "def _recv_of(b):" in k6)
    res.append(("W5 後處理：無本段受併宗之街廓之配得者照配、承受之宗經 `_recv_of`", ok5, ""))
    lits = []
    for name, src in (("end_block_merge_run", mr), ("k6b_stage3_run", k6)):
        if src:
            for n in ast.walk(ast.parse(src)):
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value):
                    lits.append((name, n.value))
    res.append(("W6 二函式內⛔ 案件字面", not lits and bool(mr) and bool(k6), f"案件字面 {lits}"))
    return res


WIRE_MUTS = [
    ("N1 ⛔ 交競合", "app.py", "                                           contests=(_ct or None))",
     "                                           contests=None)", "W1"),
    ("N2 逐列之環⛔ 經 `_k950_rows`", "app.py",
     "    for _r in _k950_rows(sorted(order, key=lambda r: r['最終序位'])):",
     "    for _r in sorted(order, key=lambda r: r['最終序位']):", "W2"),
    ("N3 後處理 (b) 另切", "app.py", "            _parts = _road_halves(x, '後處理 (b)')",
     "            _parts = list(_split(_geo[x], _geo[x].exterior))", "W4"),
    ("N4 ⛔ 照配", "app.py", "        R = R - _stay\n", "        R = R\n", "W5"),
]


def wiring(repo):
    app = _read(repo, "app.py")
    sel = _read(repo, "verify/selection_pipeline.py")
    print("── 接線（AST／字樣·app.py ＋ verify/selection_pipeline.py）──")
    red = []
    base = _wiring_checks(app, sel)
    for name, ok, note in base:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    for mname, f, x, y, exp in WIRE_MUTS:
        src = {"app.py": app, "verify/selection_pipeline.py": sel}[f]
        n = src.count(x)
        if n != 1:
            print(f"  🔴 {mname}：突變錨不存在（{n}）")
            red.append(mname.split()[0])
            continue
        m = src.replace(x, y, 1)
        a2, l2 = (m if f == "app.py" else app), (m if f == "verify/selection_pipeline.py" else sel)
        turned = [nm.split()[0] for (nm, ok, _), (_, ok0, _) in zip(_wiring_checks(a2, l2), base) if ok0 and not ok]
        ok = exp in turned
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本器另寫之幾何與 G 公式（外部錨·同 F11／F12 之法）──
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


def _frame(P, blk):
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
    return bp, p1, p2, L, d, u, big


def _band(P, blk, side, wid):
    """外部錨：末端帶 ＝ 過該端之 FRONT 端點、∥ 分配線、向街廓內垂距 `wid` 之帶 ∩ 街廓（本器另寫）。"""
    import numpy as np
    from shapely.geometry import Polygon
    bp, p1, p2, L, d, u, big = _frame(P, blk)
    e = p1 if side == "left" else p2
    ca = u
    nrm = np.array([-ca[1], ca[0]])
    if float(np.dot(np.asarray(bp.centroid.coords[0]) - e, nrm)) < 0:
        nrm = -nrm
    return Polygon([e - big * ca, e + big * ca, e + big * ca + wid * nrm, e - big * ca + wid * nrm]).intersection(bp)


def _anchor_G(P, blk, a, fin, side, pre_zone):
    """外部錨：該端第 1 位之 G（無未臨正街·G 之 S ＝ 沿 FRONT 之寬）——本器另寫之二分法。"""
    bp, p1, p2, L, d, u, big = _frame(P, blk)
    l2 = float(fin["sb_rows_by_label"][blk]["正街尺度"])
    post = float(fin["post_price_by_block"][blk])
    pre = float(fin["pre_price_by_zone"].get(pre_zone, 0.0) or 0.0)
    A = post / pre if pre > 0 else 1.0
    B, C = fin["B"], fin["C"]
    smin = min(_s_of(v, p1, d, u) for v in bp.exterior.coords)
    smax = max(_s_of(v, p1, d, u) for v in bp.exterior.coords)
    lo, hi = 0.0, L
    for _ in range(100):
        m = (lo + hi) / 2
        hp = _halfplane(p1, d, u, smin - 1.0, m, big) if side == "left" else _halfplane(p1, d, u, L - m, smax + 1.0, big)
        if bp.intersection(hp).area - (a * (1 - A * B) - m * l2) * (1 - C) < 0:
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


SCEN = {
    # 🔧 `W-G.9-361`（`K-9-54`）：地籍相連之判之座標容差 ⇒ `G017` 之合併群跨 `R5`／`R6`；其 `R6` 之片 `628-22(1)` 所鄰之
    #   已配得之街廓非恰一（`R5`／`R6`·`K-9-51` 射程 ③ ⇒ 段三後處理停機）⇒ 甲之注入加鎖 `G017` 之 `R6` 三片，以存本例之受詞
    #   （二末端塊之競合·`R5` 右端由 `628-23(2)` 續試而成）
    "甲": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 16.0}, lock=["628-21(1)", "628-22(1)", "628-23(1)"], excl=[]),
    "乙": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 5.5},
              lock=["628(1)", "628(2)", "628(5)", "628-1(1)", "628-1(2)", "628-1(3)"], excl=["628-23(2)"]),
    "丙": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 5.0},
              lock=["628(1)", "628(2)", "628(5)", "628-1(1)", "628-1(2)", "628-1(3)"], excl=["628-23(2)"]),
}


def _pipeline(ns, fake_st, rv, sb, scen=None):
    import numpy as np
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    from selection_pipeline import run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    saved = {k: ns[k] for k in ("end_block_host", "end_block_merge_run", "end_block_side_geom")}
    cfg = SCEN.get(scen) or dict(wid={}, lock=[], excl=[])
    hits = {"host": 0, "merge": 0, "geo": 0}

    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
        # 注入：所給之端 ⇒ 末端塊（⛔ 未臨正街），R_end ＝ 以所給之寬構之末端帶（經宿主之 `_end_band`）
        w = cfg["wid"].get((_label, side))
        if w is None:
            return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
                                                min_width, side, _label=_label)
        hits["geo"] += 1
        p1 = np.asarray(corner_pt, float)[:2]
        dd = np.asarray(d_hat, float)[:2]
        sp2 = float(np.dot(np.asarray(front_p2, float)[:2] - p1, dd))
        e = p1 if side == "left" else p1 + sp2 * dd
        band = ns["_end_band"](block_poly, cad_alloc, e, w, _label=_label)
        rr = ns["_strip_s_range"](band, d_hat, corner_pt, allocation_dir)
        buf = float(rr[1]) if side == "left" else float(sp2 - float(rr[0]))
        return {"gate": True, "unfront": 0.0, "s_back": 0.0, "r_end": band, "r_end_area": float(band.area),
                "band_area": float(band.area), "buf": buf}

    def host(ordered, **kw):
        if cfg["excl"]:
            crp = dict(kw["corner_range_polys"])
            fake = [Polygon(e["tp"]["polygon_coords"]).buffer(0) for e in ordered
                    if e["tp"].get("暫編地號") in cfg["excl"]]
            if fake:
                hits["host"] += 1
                for sd in ("left", "right"):
                    crp[sd] = unary_union(fake + ([crp[sd]] if crp.get(sd) is not None else []))
            kw["corner_range_polys"] = crp
        return saved["end_block_host"](ordered, **kw)

    def merge(temp, build, own, locked, corner, *a, **k):
        if cfg["lock"]:
            hits["merge"] += 1
        return saved["end_block_merge_run"](temp, build, own, set(locked) | set(cfg["lock"]), corner, *a, **k)
    ns["end_block_host"], ns["end_block_merge_run"], ns["end_block_side_geom"] = host, merge, geo
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            snapshot = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
            rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        out = dict(cb_by=cb_by, cad=cad, snapshot=snapshot, params=params, hits=hits, err=None, temp0=temp_p)
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
        return out
    finally:
        for k, v in saved.items():
            ns[k] = v


def _blk_check(P, blk):
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    rows = [r for r in P["rows"] if r.get("所屬街廓") == blk]
    bp = Polygon(P["cb_by"][blk]["vertices"]).buffer(0)
    polys = [(r["暫編地號"], Polygon(r["cut_coords"]).buffer(0), r) for r in rows
             if r.get("cut_coords") and not isinstance(r.get("cut_coords"), str)]
    un = unary_union([p for _, p, _ in polys])
    ovl = sum(polys[i][1].intersection(polys[j][1]).area for i in range(len(polys)) for j in range(i + 1, len(polys)))
    return polys, un.symmetric_difference(bp).area, ovl


def _head(polys, side):
    cand = [r for _, _, r in polys if r.get("推進側別") == side and "抵費地" not in str(r.get("暫編地號"))]
    return sorted(cand, key=lambda r: float(r.get("累積S(m)", 0) or 0))[0] if cand else None


def run(repo, sbs):
    from shapely.geometry import Polygon, LineString
    from shapely.ops import split, unary_union
    import numpy as np
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        src = _read(repo, "app.py")
        if "contests=None" not in (_fn_src(src, "k6b_stage3_run") or "")[:400]:
            print("  🔴 受詞缺：k6b_stage3_run 之 contests")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from stepg_pipeline import _compute_v3_finance
        for sb in sbs:
            P = _pipeline(ns, fake_st, rv, sb)
            if P["err"]:
                print(f"🔴 執行中止（退縮 {sb}·{P['err'][0]}）：{P['err'][1]} ⇒ 無從判定")
                return 3
            ok = P["rec"] == {"退縮": sb, "標的": [], "皆未達": {}} and P["log"] == []
            print(("  ✅" if ok else "  🔴") + f" R1 退縮 {sb}：合併再試紀錄 {P['rec']}（⛔ 載競合）；逐列 {len(P['log'])}")
            if not ok:
                red.append(f"R1@{sb}")
        sb = 3.5
        fin = None
        for scen in ("甲", "乙", "丙"):
            P = _pipeline(ns, fake_st, rv, sb, scen)
            if fin is None:
                fin = _compute_v3_finance(ns, P["snapshot"], list(P["cb_by"].values()), P["cad"])
            cfg = SCEN[scen]
            print(f"══ 合成案{scen}（退縮 {sb}·注入 末端帶寬 {list(cfg['wid'].values())}、上鎖 {len(cfg['lock'])}、"
                  f"假設跨占街角 {cfg['excl']}·咬到 {P['hits']}）══")
            bit = P["hits"]["geo"] > 0 and (P["hits"]["merge"] > 0 if cfg["lock"] else True) and \
                (P["hits"]["host"] > 0 if cfg["excl"] else True)
            if not bit:
                print("  🔴 注入未咬到 ⇒ 無從判定")
                red.append(f"注入@{scen}")
                continue
            if P["err"]:
                print(f"  🔴 執行中止：{P['err']}")
                red.append(f"中止@{scen}")
                continue
            rec, log = P["rec"], P["log"]
            by0 = {t["暫編地號"]: t for t in P["temp0"]}
            by = {t["暫編地號"]: t for t in P["temp"]}
            own = fake_st.session_state.get("t8_ownership_map", {}) or {}
            main = [(r["候選"], r["層級"], r["結果"], r["檢核"]) for r in log if r.get("序") != "後處理"]
            post = [(r["候選"], r["層級"], r["結果"], r["受併宗"]) for r in log if r.get("序") == "後處理"]
            # 外部錨：地主 G009 原有土地與二端末端帶之交（競合之交面積）
            bA, bB = _band(P, "R3", "left", cfg["wid"][("R3", "left")]), _band(P, "R5", "right", cfg["wid"][("R5", "right")])
            gid = own.get("628")
            g9 = [Polygon(t["polygon_coords"]).buffer(0) for t in P["temp0"] if own.get(t.get("原地號")) == gid
                  and len(t.get("polygon_coords") or []) >= 3]
            xa = round(sum(p.intersection(bA).area for p in g9 if p.intersection(bA).area > 1.0), 2)
            xb = round(sum(p.intersection(bB).area for p in g9 if p.intersection(bB).area > 1.0), 2)
            ct = (rec or {}).get("競合") or []
            okc = (len(ct) == 1 and ct[0]["形"] == "一" and [e[:3] for e in ct[0]["列"]] == [["R3", "左", "628(4)"],
                                                                                               ["R5", "右", "628(3)"]]
                   and abs(ct[0]["列"][0][3] - xa) <= 0.02 and abs(ct[0]["列"][1][3] - xb) <= 0.02)
            print(("  ✅" if okc else "  🔴") + f" C{scen} 競合 ＝ {ct}；外部錨之交面積 R3 左 {xa}／R5 右 {xb}")
            if not okc:
                red.append(f"C@{scen}")
            polys3, d3, o3 = _blk_check(P, "R3")
            polys5, d5, o5 = _blk_check(P, "R5")
            pools3 = [(k, p) for k, p, r in polys3 if "抵費地" in k]
            fp = [(k, p) for k, p in pools3 if abs(p.area - bA.area) <= 0.05 and p.symmetric_difference(bA).area <= 0.05]
            lx = sum(p.intersection(bA).area for k, p, r in polys3 if "抵費地" not in k)
            okr3 = (rec["皆未達"].get("R3") == ["left"] and len(fp) == 1 and lx <= 1e-4 and d3 <= 0.05 and o3 <= 0.05)
            print(("  ✅" if okr3 else "  🔴") + f" F{scen} R3 左強制抵費地 {fp and fp[0][0]}（{fp and round(fp[0][1].area, 2)}·"
                  f"外部錨末端帶 {bA.area:.2f}）；宗地 ∩ 帶 {lx:.6f}；聯集 △ 街廓 {d3:.4f}、兩兩疊 {o3:.4f}")
            if not okr3:
                red.append(f"F@{scen}")
            h5 = _head(polys5, "right")
            if scen == "甲":
                exp_main = [("628(4)", "②", "未成", "—"), ("628(3)", "②", "未成", "—"), ("628-34(2)", "—", "未成", "—"),
                            ("628-23(2)", "①", "成", "免"), ("628-22(2)", "—", "略·已定案", "—")]
                exp_post = [("628-23(3)", "後處理(b)", "成", "628-23(2)"), ("628-22(3)", "後處理(b)", "成", "628-23(2)")]
                # 外部錨：628-23(3)／628-22(3) 全在 RD2 中心線之一側（切分得 1 片）
                clp = P["cad"]["centerlines"]["RD2"]
                (x1, y1), (x2, y2) = clp[0], clp[-1]
                dv = np.array([x2 - x1, y2 - y1]) / float(np.hypot(x2 - x1, y2 - y1))
                ln = LineString([tuple(np.array([x1, y1]) - 500 * dv), tuple(np.array([x2, y2]) + 500 * dv)])
                one = all(len(list(split(Polygon(by0[x]["polygon_coords"]).buffer(0), ln).geoms)) == 1
                          for x in ("628-23(3)", "628-22(3)"))
                recv = "628-23(2)"
                add = sum(_aprime(P["snapshot"], by0[x], by0[recv]) for x in ("628-21(2)", "628-22(2)", "628-23(3)", "628-22(3)"))
                ga = _anchor_G(P, "R5", round(float(by0[recv]["分攤登記面積_m2"]) + add, 2), fin, "right",
                               by0[recv].get("重劃前地價區段", ""))
                ok = (main == exp_main and post == exp_post and one and rec["皆未達"] == {"R3": ["left"]}
                      and h5 is not None and h5["暫編地號"] == recv and abs(float(h5["G(㎡)"]) - ga) <= 0.02
                      and d5 <= 0.05 and o5 <= 0.05)
                print(("  ✅" if ok else "  🔴") + f" X甲：逐列 {main}；後處理 {post}；二片皆全在中心線之一側 {one}；"
                      f"R5 右鏈首宗 {h5 and h5['暫編地號']} G {h5 and h5['G(㎡)']} ＝ 外部錨 {ga}；R5 聯集 △ 街廓 {d5:.4f}、"
                      f"兩兩疊 {o5:.4f}")
                if not ok:
                    red.append("X甲")
            else:
                recv, los = "628(3)", "628(4)"
                if scen == "乙":
                    exp_main = [("628(3)", "②", "成", "通過"), ("628(4)", "②", "未成", "—"), ("628-34(2)", "—", "未成", "—")]
                    exp_post = [("628(4)", "後處理(a)", "成", "628(3)")]
                    okh = True
                    hnote = ""
                else:
                    exp_main = [("628(3)", "②半", "成", "通過"), ("628(4)", "②半", "未成", "—"), ("628-34(2)", "—", "未成", "—")]
                    exp_post = [("628(4)", "題一 4", "成", "628(3)")]
                    # 外部錨：628(6) 依 RD2 中心線切二，鄰 R5 者之比 × a′(628(6)→628(3)) ＝ 切半所併之量
                    clp = P["cad"]["centerlines"]["RD2"]
                    (x1, y1), (x2, y2) = clp[0], clp[-1]
                    dv = np.array([x2 - x1, y2 - y1]) / float(np.hypot(x2 - x1, y2 - y1))
                    ln = LineString([tuple(np.array([x1, y1]) - 500 * dv), tuple(np.array([x2, y2]) + 500 * dv)])
                    g6 = Polygon(by0["628(6)"]["polygon_coords"]).buffer(0)
                    parts = list(split(g6, ln).geoms)
                    b5 = Polygon(P["cb_by"]["R5"]["vertices"]).buffer(0)
                    f5 = sum(q.area for q in parts if q.distance(b5) < 1e-6) / g6.area
                    q5 = _aprime(P["snapshot"], by0["628(6)"], by0[recv]) * f5
                    q3 = _aprime(P["snapshot"], by0["628(6)"], by0[recv]) * (1.0 - f5)
                    wr = next(r for r in log if r.get("候選") == recv and r.get("序") != "後處理")
                    lr = next(r for r in log if r.get("候選") == los and r.get("序") == "後處理")
                    okh = (len(parts) == 2 and abs(float(wr["切分併入"].get("628(6)", -1)) - q5) <= 0.02
                           and abs(float(lr["切分併入"].get("628(6)", -1)) - q3) <= 0.02 and lr["整筆併入"] == [los])
                    hnote = f"；切半之量 {wr['切分併入']}／{lr['切分併入']} ＝ 外部錨 {q5:.4f}／{q3:.4f}（R5 側之比 {f5:.4f}）"
                add = _aprime(P["snapshot"], by0["628(6)"], by0[recv]) + _aprime(P["snapshot"], by0[los], by0[recv])
                ga = _anchor_G(P, "R5", round(float(by0[recv]["分攤登記面積_m2"]) + add, 2), fin, "right",
                               by0[recv].get("重劃前地價區段", ""))
                ok = (main == exp_main and post == exp_post and okh and rec["皆未達"] == {"R3": ["left"]}
                      and h5 is not None and h5["暫編地號"] == recv and abs(float(h5["G(㎡)"]) - ga) <= 0.02
                      and d5 <= 0.05 and o5 <= 0.05 and los not in {b["暫編地號"] for b in P["build"]})
                print(("  ✅" if ok else "  🔴") + f" X{scen}：逐列 {main}；後處理 {post}{hnote}；R5 右鏈首宗 "
                      f"{h5 and h5['暫編地號']} G {h5 and h5['G(㎡)']} ＝ 外部錨 {ga}；R5 聯集 △ 街廓 {d5:.4f}、兩兩疊 {o5:.4f}")
                if not ok:
                    red.append(f"X{scen}")
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
