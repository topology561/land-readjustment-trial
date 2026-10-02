# -*- coding: utf-8 -*-
"""W-G.9-357 量測器（發單側窗五十三擬·檔 F16·⛔ 由受單側改一字）：段三後處理之 `K-9-48` 七項 `3`〜`6` 與
`K-9-51`（剩餘土地之去處：同一地主已配得土地之街廓，距離該筆土地最近者先；同距離者配得面積大者先）。

子命令（一律 python verify/probes/probe_WG9357_k948.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k6b_stage3_run`／`adj_intake`；`verify/selection_pipeline.py`
           取 `k6b_stage3_pool_temp`）。玩具：B3（X2(1)／X1(1)）、公園 PK（P1(1)）、B5（Y1(1)／K5(1)／Y2(1)）、道路 RD、
           B7（Z1(1)／Q7(1)）、BW（W1(1)）；歸戶 g1 ＝ X1／X2／Y1／Y2／Z1／W1（P1 依例）。段三：B3 右端之候選 X1(1)
           以同街廓之 X2(1) 於 ① 成；後處理之受詞 ＝ P1(1)（公設地上·平分入 X1／Y1）或 W1(1)（他街廓建地·整筆）。
           回呼：街廓內受併之累加 `>` 該街廓之容量 ⇒ 配餘地不合格（「不影響原位次」不過）。
           K1〜K15 ＝ 各支（整批通過／最大面積／第 5 項之距離序／同距離之 G 序／整筆之第 5 項／轉調配／0.01 ㎡／
           a′ 之折算／停機／舊鍵之重寫／公設地調配之 temp／調配之輸入）；K16〜K18 ＝ `K-9-50` 題一 4 之承前（玩具二：
           BX／BY 隔道路 RX 相對，只 BX 成，Y1 不能依原位次配地·其與其半併入 X1 不過 ⇒ 七項 3〜5）；K19〜K22 ＝ 補令一
           （K19 題一 4 之轉調配即終局·後處理⛔ 再處置；K20／K20′ 有剩下之判準一〔round(r, 4) ＞ 0〕；K21 距離之四捨五入
           〔0.125 ⇒ 0.13〕；K22 候選為空 ⇒ ⛔ 查 G）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  run      <repo> [<退縮> …]
           harness ＋ 畫面實跑本案（預設退縮 `3.5`、`0.0`）：R1 `alloc_state` 之 `G`（harness 之 `_k6b_callbacks` 與
           畫面之 `k6b_screen_callbacks`·同一宗地）——二者之保留集相同、`G` 之鍵 ＝ 保留集之聯集、逐宗差 ≤ `0.01`；
           R2 段三（harness `run_corner_pk_k6b`）之紀錄逐列 ＝ 開工態之實測（本器所載·數值容差 `0.01`），且其出之
           宗地⛔ 帶 `段三部分併出`／`段三餘量`（本案⛔ 觸發七項 `3`〜`6`）。
           🔧 `W-G.9-363`（⛔ 上列一字不刪）：run 於行程內設 WV_K953=off（手冊先行亦以段三之鍵標其片）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import contextlib, copy, importlib.util, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

TOL = 0.01


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _load(repo, rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(repo, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


# ── 玩具（⛔ 本案資料）──
H, PK, RDC = "住宅區", "鄰里公園", "道路"


def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


def _world(a=None, p_owner="g1", w1=False):
    """B3（x∈[0,20]）：X2(1)[0,10]／X1(1)[10,20]；公園 PK（x∈[20,30]）：P1(1)；B5（x∈[30,50]）：Y1(1)[30,40]／
    K5(1)[40,45]／Y2(1)[45,50]；道路 RD（y∈[-10,0]）：R0(1)；B7（y∈[-40,-10]）：Z1(1)[30,40]／Q7(1)[40,50]；
    （w1）BW（y∈[30,40]·x∈[0,20]）：W1(1)。歸戶 g1 ＝ X1／X2／Y1／Y2／Z1／W1（P1 依 p_owner）。"""
    a = dict(dict(X1=100, X2=60, P1=200, Y1=100, K5=80, Y2=50, R0=500, Z1=100, Q7=90, W1=50), **(a or {}))
    t = [_tp("X2(1)", "B3", H, _R(0, 10, 0, 30), a["X2"]), _tp("X1(1)", "B3", H, _R(10, 20, 0, 30), a["X1"]),
         _tp("P1(1)", "PK", PK, _R(20, 30, 0, 30), a["P1"]),
         _tp("Y1(1)", "B5", H, _R(30, 40, 0, 30), a["Y1"]), _tp("K5(1)", "B5", H, _R(40, 45, 0, 30), a["K5"]),
         _tp("Y2(1)", "B5", H, _R(45, 50, 0, 30), a["Y2"]),
         _tp("R0(1)", "RD", RDC, _R(0, 50, -10, 0), a["R0"]),
         _tp("Z1(1)", "B7", H, _R(30, 40, -40, -10), a["Z1"]), _tp("Q7(1)", "B7", H, _R(40, 50, -40, -10), a["Q7"])]
    if w1:
        t.append(_tp("W1(1)", "BW", H, _R(0, 20, 30, 40), a["W1"]))
    own = {"X1": "g1", "X2": "g1", "Y1": "g1", "Y2": "g1", "Z1": "g1", "W1": "g1", "P1": p_owner,
           "K5": "gK", "R0": "gR", "Q7": "gQ"}
    blocks = {"B3": {"category": H}, "PK": {"category": PK}, "B5": {"category": H}, "RD": {"category": RDC},
              "B7": {"category": H}, "BW": {"category": H}}
    return t, own, blocks, {"RD": [(-10.0, -5.0), (60.0, -5.0)]}


def _g(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _cbs(cap, price=None, drop=(), no_g=False):
    """玩具之回呼：`alloc_state` 以 build 之全部（`drop` 除外）為保留；街廓內受併之累加（`面積_m2` 之和）
    `>` `cap[街廓]` ⇒ 該街廓之配餘地不合格一處；`G` ＝ 分攤登記面積 ＋ 面積（`no_g` ⇒ ⛔ 回 `G`）。
    `a_prime` ＝ a(src) × p(src 之街廓) ÷ p(dst 之街廓)（`price` 缺者 ＝ 1）。`trial_winner` ＝ G ≥ 門檻即當選。"""
    price = price or {}

    def a_prime(src, dst):
        return _g(src) * price.get(src["所屬街廓"], 1.0) / price.get(dst["所屬街廓"], 1.0)

    def alloc_state(temp, build):
        kept, bad, G, acc = {}, {}, {}, {}
        for b in build:
            acc[b["所屬街廓"]] = acc.get(b["所屬街廓"], 0.0) + float(b.get("面積_m2", 0) or 0)
            if b["暫編地號"] in drop:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            G[b["暫編地號"]] = _g(b)
        for blk, v in acc.items():
            if v > cap.get(blk, 1e9) + 1e-9:
                bad[blk] = 1
        out = {"kept": kept, "bad_pools": bad, "err": None}
        if not no_g:
            out["G"] = G
        return out

    def trial_winner(temp, build, blk, end, cand):
        by = {b["暫編地號"]: b for b in build}
        g = _g(by[cand]) if cand in by else 0.0
        return (cand if g >= 150.0 else None), round(g, 2), 150.0
    return a_prime, trial_winner, alloc_state


ORDER = [{"最終序位": 1, "街廓": "B3", "端": "右", "暫編地號": "X1(1)"}]
KEYS3 = ("段三併出", "段三部分併出", "段三餘量")


def _go(ns, cap, price=None, drop=(), no_g=False, a=None, p_owner="g1", w1=False, pre=None):
    temp, own, blocks, cl = _world(a, p_owner, w1)
    for pid, kv in (pre or {}).items():
        next(t for t in temp if t["暫編地號"] == pid).update(kv)
    build = [t for t in temp if t["街廓分類"] == H]
    ap, tw, st = _cbs(cap, price, drop, no_g)
    t2, b2, log = ns["k6b_stage3_run"](ORDER, set(), own, temp, build, blocks, cl, ap, tw, st,
                                       log_print=lambda *x: None)
    by = {t["暫編地號"]: t for t in t2}
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
             tuple(sorted((k, round(v, 2)) for k, v in (x.get("併入量") or {}).items())))
            for x in log if x.get("序") == "後處理"]
    acc = {k: round(float(v.get("面積_m2", 0) or 0), 2) for k, v in sorted(by.items())
           if float(v.get("面積_m2", 0) or 0)}
    keys = {k: {kk: (v[kk] if not isinstance(v[kk], dict) else dict(sorted((a2, round(b2_, 2)) for a2, b2_ in v[kk].items())))
                for kk in KEYS3 if kk in v} for k, v in sorted(by.items()) if any(kk in v for kk in KEYS3)}
    for k, v in keys.items():
        if "段三餘量" in v:
            v["段三餘量"] = round(float(v["段三餘量"]), 2)
    return post, acc, keys, sorted(b["暫編地號"] for b in b2), (t2, b2, own, blocks)


def _world4(a=None):
    """題一（`K-9-50`）之玩具：BX（X1(1)[0,10]／PX(1)）與 BY（Y1(1)[0,10]／QY(1)）隔道路 RX（X3(1)[0,10]／R0(1)·中心線
    y ＝ -5 ⇒ X3 切為上下各半）相對；B7：Z1(1)（x∈[60,70]·距 BY 50.99）。歸戶 g1 ＝ X1／X3／Y1／Z1。"""
    a = dict(dict(X1=100, X3=80, Y1=90, Z1=100, PX=500, QY=500, R0=300), **(a or {}))
    t = [_tp("X1(1)", "BX", H, _R(0, 10, 0, 30), a["X1"]), _tp("PX(1)", "BX", H, _R(10, 40, 0, 30), a["PX"]),
         _tp("X3(1)", "RX", RDC, _R(0, 10, -10, 0), a["X3"]), _tp("R0(1)", "RX", RDC, _R(10, 40, -10, 0), a["R0"]),
         _tp("Y1(1)", "BY", H, _R(0, 10, -40, -10), a["Y1"]), _tp("QY(1)", "BY", H, _R(10, 40, -40, -10), a["QY"]),
         _tp("Z1(1)", "B7", H, _R(60, 70, 0, 30), a["Z1"])]
    own = {"X1": "g1", "X3": "g1", "Y1": "g1", "Z1": "g1", "PX": "gP", "R0": "gR", "QY": "gQ"}
    blocks = {"BX": {"category": H}, "RX": {"category": RDC}, "BY": {"category": H}, "B7": {"category": H}}
    return t, own, blocks, {"RX": [(-10.0, -5.0), (60.0, -5.0)]}


def _go4(ns, cap, thr=None, drop=("Y1(1)",)):
    """二末端塊之競合（題一）：BX 左端 X1(1) 以其半（40）達門檻 130；BY 左端 Y1(1) 連其半（130）未達 200 ⇒ 只 BX 成；
    Y1 恆⛔ 保留（不能依原位次配地）⇒ 題一 4：Y1 連同其半併入 X1。"""
    thr = thr or {("BX", "左"): 130.0, ("BY", "左"): 200.0}
    temp, own, blocks, cl = _world4()
    build = [t for t in temp if t["街廓分類"] == H]
    ap, _tw, st = _cbs(cap, None, drop)

    def tw(temp_, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        g = _g(by[cand]) if cand in by else 0.0
        return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]
    order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
             {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
    ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
    t2, b2, log = ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap, tw, st,
                                       log_print=lambda *x: None, contests=ct)
    by = {t["暫編地號"]: t for t in t2}
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
             tuple(sorted((k, round(v, 2)) for k, v in (x.get("併入量") or {}).items())))
            for x in log if x.get("序") == "後處理"]
    acc = {k: round(float(v.get("面積_m2", 0) or 0), 2) for k, v in sorted(by.items())
           if float(v.get("面積_m2", 0) or 0)}
    keys = {k: {kk: (v[kk] if not isinstance(v[kk], dict) else dict(sorted((a2, round(b2_, 2)) for a2, b2_ in v[kk].items())))
                for kk in KEYS3 if kk in v} for k, v in sorted(by.items()) if any(kk in v for kk in KEYS3)}
    for k, v in keys.items():
        if "段三餘量" in v:
            v["段三餘量"] = round(float(v["段三餘量"]), 2)
    return post, acc, keys, sorted(b["暫編地號"] for b in b2)


def _world5():
    """補令一 K21 之玩具：`_world4` ＋ B8（Z8(1)·y∈[-60,-40.125]·距 Y1 0.125）＋ B9（Z9(1)·x∈[-20,-0.13]·距 Y1 0.13）；
    歸戶 g1 ＋ Z8／Z9；Z8 之 G ＝ 10、Z9 ＝ 500。"""
    t, own, blocks, cl = _world4()
    t = t + [_tp("Z8(1)", "B8", H, _R(0, 10, -60, -40.125), 10), _tp("Z9(1)", "B9", H, _R(-20, -0.13, -40, -10), 500)]
    own = dict(own, Z8="g1", Z9="g1")
    blocks = dict(blocks, B8={"category": H}, B9={"category": H})
    return t, own, blocks, cl


def _go5(ns, cap):
    """題一之玩具（`_go4` 之形）於 `_world5`；回 ① 後處理之列（`_go4` 之形）② 第 5 項之非轉調配列之（候選, 受併宗, 距離, G）。"""
    thr = {("BX", "左"): 130.0, ("BY", "左"): 200.0}
    temp, own, blocks, cl = _world5()
    build = [t for t in temp if t["街廓分類"] == H]
    ap, _tw, st = _cbs(cap, None, ("Y1(1)",))

    def tw(temp_, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        g = _g(by[cand]) if cand in by else 0.0
        return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]
    order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
             {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
    ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
    _t2, _b2, log = ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap, tw, st,
                                         log_print=lambda *x: None, contests=ct)
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
             tuple(sorted((k, round(v, 2)) for k, v in (x.get("併入量") or {}).items())))
            for x in log if x.get("序") == "後處理"]
    d5 = [(x["候選"], x["受併宗"], x.get("距離"), round(float(x.get("G") or 0), 2))
          for x in log if x.get("層級") == "後處理·第5項" and x.get("結果") != "轉調配"]
    return post, d5


def _halt(ns, phrase, **kw):
    try:
        _go(ns, **kw)
    except RuntimeError as e:
        return ("停機", phrase in str(e))
    return ("無停機",)


C_ALL = {"B3": 1000.0, "B5": 1000.0, "B7": 1000.0}
_X2 = {"X2(1)": {"段三併出": ["X1(1)"]}}
_BL = ["K5(1)", "Q7(1)", "X1(1)", "Y1(1)", "Y2(1)", "Z1(1)"]


def _cap(**kw):
    return dict(C_ALL, **kw)


def _pool(sp, t2):
    pool = sp.k6b_stage3_pool_temp(t2)
    by0 = {t["暫編地號"]: t for t in t2}
    return ([(t["暫編地號"], t is by0[t["暫編地號"]], round(float(t["分攤登記面積_m2"]), 2)) for t in pool],
            pool is not t2)


def _intake(ns, world):
    t2, b2, own, blocks = world
    burden = {b: ns["F3_CATEGORY_BURDEN"][v["category"]] for b, v in blocks.items()}
    g_rows = [{"暫編地號": b["暫編地號"], "推進側別": "left"} for b in b2]
    r = ns["adj_intake"](t2, b2, g_rows, {}, own, burden)
    rows = {x["暫編地號"]: (x["類"], round(float(x["原有面積"]), 2), round(float(x.get("段三併出面積") or 0), 2))
            for x in r["slices"] if x["暫編地號"] in ("P1(1)", "R0(1)", "X2(1)")}
    units = [(u["歸戶"], u["軌"], round(float(u["原有面積合計"]), 2), sorted(x["暫編地號"] for x in u["共同負擔用地"]))
             for u in r["units"]]
    step4 = [(s["歸戶"], sorted(x["暫編地號"] for x in s["共同負擔用地"])) for s in r["step4"]]
    tot = {k: round(v[1], 2) for k, v in sorted(r["totals"].items()) if v[1]}
    cons = abs(sum(v[1] for v in r["totals"].values()) - float(r["all_area"])) <= 1e-6
    return rows, units, step4, tot, cons


def _cases(ns, sp):
    out = []
    # K1 整批通過 ⇒ 逐位同本批前（對照·新舊碼皆綠）
    _run(out, "K1 整批通過 ⇒ 一列、二受併宗各 100、⛔ 新鍵",
         lambda: _go(ns, C_ALL)[:4],
         ([("P1(1)", "後處理(c)", "成", ("X1(1)", "Y1(1)"), (("X1(1)", 100.0), ("Y1(1)", 100.0)))],
          {"X1(1)": 160.0, "Y1(1)": 100.0}, {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2}, _BL))
    # K2 七項 3：X1 之分只容 60（最大面積）；Y1 之分 100 通過；餘 40 依第 5 項 ⇒ 距離最近之 B5（Y1·G 200 ＞ Y2·G 50）
    _run(out, "K2 最大面積 60 ＋ 第 5 項併入 Y1（距 0·G 大者）⇒ 全數併出",
         lambda: _go(ns, _cap(B3=120.0))[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 40.0),))],
          {"X1(1)": 120.0, "Y1(1)": 140.0}, {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2}, _BL))
    # K3 第 5 項之序：B5（距 0）之 Y1 只容 20、Y2 不容 ⇒ 次 B7（距 10）之 Z1 收 20
    _run(out, "K3 第 5 項依距離：B5 之 Y1 部分 20、Y2 未成 ⇒ B7 之 Z1 收 20",
         lambda: _go(ns, _cap(B3=120.0, B5=120.0))[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "部分成", "Y1(1)", (("Y1(1)", 20.0),)),
           ("P1(1)", "後處理·第5項", "未成", "Y2(1)", ()),
           ("P1(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),))],
          {"X1(1)": 120.0, "Y1(1)": 120.0, "Z1(1)": 20.0},
          {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)", "Z1(1)"]}, **_X2}, _BL))
    # K4 皆不能全收 ⇒ 餘 15 轉調配；三鍵
    _run(out, "K4 餘 15 轉調配：段三併出＋段三部分併出＋段三餘量",
         lambda: _go(ns, _cap(B3=120.0, B5=120.0, B7=5.0))[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "部分成", "Y1(1)", (("Y1(1)", 20.0),)),
           ("P1(1)", "後處理·第5項", "未成", "Y2(1)", ()),
           ("P1(1)", "後處理·第5項", "部分成", "Z1(1)", (("Z1(1)", 5.0),)),
           ("P1(1)", "後處理·第5項", "轉調配", "—", ())],
          {"X1(1)": 120.0, "Y1(1)": 120.0, "Z1(1)": 5.0},
          {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)", "Z1(1)"],
                     "段三部分併出": {"X1(1)": 60.0, "Y1(1)": 120.0, "Z1(1)": 5.0}, "段三餘量": 15.0}, **_X2}, _BL))
    # K5 同距離（B5）⇒ 配得面積（G）大者先：Y2（300）先於 Y1（200）
    _run(out, "K5 同距離者 G 大者先 ⇒ Y2 收 40",
         lambda: _go(ns, _cap(B3=120.0), a={"Y2": 300})[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y2(1)", (("Y2(1)", 40.0),))],
          {"X1(1)": 120.0, "Y1(1)": 100.0, "Y2(1)": 40.0},
          {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)", "Y2(1)"]}, **_X2}, _BL))
    # K6 七項 4：不可拆分之建地 W1 整筆併入 X1 不過 ⇒ 未成 ⇒ 第 5 項：B5（距 10）之 Y1（G 100 ＞ Y2 50）整筆通過
    _run(out, "K6 整筆不過 ⇒ 未成；第 5 項整筆併入 Y1；W1 出 build",
         lambda: _go(ns, _cap(B3=90.0), p_owner="gP", w1=True, drop=("W1(1)",))[:4],
         ([("W1(1)", "後處理(a)", "未成", "X1(1)", (("X1(1)", 50.0),)),
           ("W1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 50.0),))],
          {"X1(1)": 60.0, "Y1(1)": 50.0}, {"W1(1)": {"段三併出": ["Y1(1)"]}, **_X2}, _BL))
    # K7 整筆皆不過 ⇒ 轉調配；W1 留於 build、⛔ 新鍵
    _run(out, "K7 整筆皆不過 ⇒ 轉調配；W1 留 build",
         lambda: _go(ns, _cap(B3=90.0, B5=0.0, B7=0.0), p_owner="gP", w1=True, drop=("W1(1)",))[:4],
         ([("W1(1)", "後處理(a)", "未成", "X1(1)", (("X1(1)", 50.0),)),
           ("W1(1)", "後處理·第5項", "未成", "Y1(1)", ()),
           ("W1(1)", "後處理·第5項", "未成", "Y2(1)", ()),
           ("W1(1)", "後處理·第5項", "未成", "Z1(1)", ()),
           ("W1(1)", "後處理·第5項", "轉調配", "—", ())],
          {"X1(1)": 60.0}, dict(_X2), sorted(_BL + ["W1(1)"])))
    # K8 可拆分者一分未併 ⇒ 未成二列；第 5 項（B3／B5 已不過 ⇒ 唯 B7）未成 ⇒ 轉調配；唯 段三餘量 ＝ 200
    _run(out, "K8 一分未併 ⇒ 段三餘量 200、⛔ 段三併出",
         lambda: _go(ns, _cap(B3=60.0, B5=0.0, B7=0.0))[:4],
         ([("P1(1)", "後處理(c)", "未成", "X1(1)", ()), ("P1(1)", "後處理(c)", "未成", "Y1(1)", ()),
           ("P1(1)", "後處理·第5項", "未成", "Z1(1)", ()), ("P1(1)", "後處理·第5項", "轉調配", "—", ())],
          {"X1(1)": 60.0}, {"P1(1)": {"段三餘量": 200.0}, **_X2}, _BL))
    # K9 最大面積以 0.01 ㎡ 為單位（容量 120.005 ⇒ 60.00·⛔ 60.01）
    _run(out, "K9 0.01 ㎡ 之格：容 60.005 ⇒ 收 60.00",
         lambda: _go(ns, _cap(B3=120.005))[:2],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 40.0),))],
          {"X1(1)": 120.0, "Y1(1)": 140.0}))
    # K10 a′ 之折算（PK 之地價為住宅區之 2 倍）：受併宗之增 ＝ 2 × 源之面積；段三部分併出以源之面積計
    _run(out, "K10 a′ 折算：X1 收 120（源 60）、Y1 收 200＋80",
         lambda: _go(ns, _cap(B3=180.0), price={"PK": 2.0})[:3],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 120.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 200.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 80.0),))],
          {"X1(1)": 180.0, "Y1(1)": 280.0}, {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2}))
    _run(out, "K10′ a′ 折算之餘：B5／B7 亦滿 ⇒ 段三部分併出 {X1: 60, Y1: 100}（源）、段三餘量 40",
         lambda: _go(ns, _cap(B3=180.0, B5=200.0, B7=0.0), price={"PK": 2.0})[2],
         {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"], "段三部分併出": {"X1(1)": 60.0, "Y1(1)": 100.0},
                    "段三餘量": 40.0}, **_X2})
    # K11 第 5 項須 alloc_state 回 G；缺 ⇒ 停機（⛔ 以他量代之）
    _run(out, "K11 alloc_state 未回 G ⇒ 停機",
         lambda: _halt(ns, "未回 G", cap=_cap(B3=120.0), no_g=True), ("停機", True))
    # K12 入段三時已帶舊鍵者，本趟全數併出 ⇒ 舊鍵去之
    _run(out, "K12 舊之 段三餘量 於全數併出後去之",
         lambda: _go(ns, _cap(B3=120.0), pre={"P1(1)": {"段三餘量": 200.0, "段三部分併出": {"Q": 1.0}}})[2],
         {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2})
    # K13 公設地調配之 temp：全數併出者去之；部分併出者以其餘量之比縮之（新物件）；未觸者同一物件
    _run(out, "K13 k6b_stage3_pool_temp：P1 以 15 入（新物件）、X2 去、餘同一物件",
         lambda: _pool(sp, _go(ns, _cap(B3=120.0, B5=120.0, B7=5.0))[4][0]),
         ([("X1(1)", True, 100.0), ("P1(1)", False, 15.0), ("Y1(1)", True, 100.0), ("K5(1)", True, 80.0),
           ("Y2(1)", True, 50.0), ("R0(1)", True, 500.0), ("Z1(1)", True, 100.0), ("Q7(1)", True, 90.0)], True))
    # K14 調配之輸入：部分併出之餘與一分未併者 ⇒ 入合併單位（K-9-45）——縱其歸戶有原位次配地
    _run(out, "K14 adj_intake：P1 之餘 15 入合併單位（公設軌）；守恆",
         lambda: _intake(ns, _go(ns, _cap(B3=120.0, B5=120.0, B7=5.0))[4]),
         ({"P1(1)": ("共同負擔用地·入合併單位", 15.0, 185.0), "R0(1)": ("共同負擔用地·入合併單位", 500.0, 0.0),
           "X2(1)": ("原位次配地", 60.0, 0.0)},
          [("g1", "公設軌", 15.0, ["P1(1)"]), ("gR", "公設軌", 500.0, ["R0(1)"])], [],
          {"原位次配地": 765.0, "共同負擔用地·入合併單位": 515.0}, True))
    _run(out, "K14′ adj_intake：一分未併之 P1（200）入合併單位",
         lambda: _intake(ns, _go(ns, _cap(B3=60.0, B5=0.0, B7=0.0))[4])[:2],
         ({"P1(1)": ("共同負擔用地·入合併單位", 200.0, 0.0), "R0(1)": ("共同負擔用地·入合併單位", 500.0, 0.0),
           "X2(1)": ("原位次配地", 60.0, 0.0)},
          [("g1", "公設軌", 200.0, ["P1(1)"]), ("gR", "公設軌", 500.0, ["R0(1)"])]))
    # K15 對照：整批通過之出，其公設地調配之 temp 與調配之輸入同本批前（P1 去之·入原位次配地）
    _run(out, "K15 對照：整批通過 ⇒ P1 ⛔ 入公設地調配之 temp；adj_intake 歸原位次配地",
         lambda: (sorted(t["暫編地號"] for t in sp.k6b_stage3_pool_temp(_go(ns, C_ALL)[4][0])),
                  _intake(ns, _go(ns, C_ALL)[4])[0]["P1(1)"]),
         (["K5(1)", "Q7(1)", "R0(1)", "X1(1)", "Y1(1)", "Y2(1)", "Z1(1)"], ("原位次配地", 200.0, 0.0)))
    # K16 對照：題一 4 之合併通過（逐位同本批前）
    _run(out, "K16 題一 4 對照：Y1 連同其半併入 X1 通過 ⇒ 一列",
         lambda: _go4(ns, {"BX": 1000.0, "BY": 1000.0, "B7": 1000.0}),
         ([("Y1(1)", "題一 4", "成", "X1(1)", (("X1(1)", 130.0),))], {"X1(1)": 170.0},
          {"X3(1)": {"段三併出": ["X1(1)"]}, "Y1(1)": {"段三併出": ["X1(1)"]}}, ["PX(1)", "QY(1)", "X1(1)", "Z1(1)"]))
    # K17 題一 4 之合併不過 ⇒ 七項 4：Y1 整筆不併入 X1 ⇒ 第 5 項 ⇒ Z1；Y1 之半（40）：七項 3 ⇒ X1 只容 20 ⇒ 餘 20 ⇒ Z1
    _run(out, "K17 題一 4 不過 ⇒ Y1 整筆經第 5 項入 Z1；其半 X1 收 20、餘 20 入 Z1（⛔ 停機）",
         lambda: _go4(ns, {"BX": 60.0, "BY": 1000.0, "B7": 1000.0}),
         ([("Y1(1)", "題一 4", "未成", "X1(1)", ()), ("Y1(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 90.0),)),
           ("X3(1)", "題一 4", "部分成", "X1(1)", (("X1(1)", 20.0),)),
           ("X3(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),))],
          {"X1(1)": 60.0, "Z1(1)": 110.0},
          {"X3(1)": {"段三併出": ["X1(1)", "Z1(1)"]}, "Y1(1)": {"段三併出": ["Z1(1)"]}}, ["PX(1)", "QY(1)", "X1(1)", "Z1(1)"]))
    # K18 同上而 B7 只容 100 ⇒ X3 之餘 10 轉調配；段三部分併出含已取得一端之半（40 ＋ 20）
    _run(out, "K18 題一 4 之餘 10 轉調配：X3 段三部分併出 {X1: 60, Z1: 10}、段三餘量 10",
         lambda: _go4(ns, {"BX": 60.0, "BY": 1000.0, "B7": 100.0})[2],
         {"X3(1)": {"段三併出": ["X1(1)", "Z1(1)"], "段三部分併出": {"X1(1)": 60.0, "Z1(1)": 10.0}, "段三餘量": 10.0},
          "Y1(1)": {"段三併出": ["Z1(1)"]}})
    # ── 補令一 ──
    # K19 題一 4 之合併不過、Y1 整筆經第 5 項亦不過 ⇒ 轉調配即終局：後處理⛔ 再處置 Y1（⛔ 後處理(a) 之列·轉調配恰一列）
    _run(out, "K19 題一 4 之 Y1 轉調配即終局 ⇒ Y1 恰三列、轉調配恰一列；X3 之餘 20 入 Z1",
         lambda: _go4(ns, {"BX": 60.0, "BY": 1000.0, "B7": 50.0}),
         ([("Y1(1)", "題一 4", "未成", "X1(1)", ()), ("Y1(1)", "後處理·第5項", "未成", "Z1(1)", ()),
           ("Y1(1)", "後處理·第5項", "轉調配", "—", ()),
           ("X3(1)", "題一 4", "部分成", "X1(1)", (("X1(1)", 20.0),)),
           ("X3(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),))],
          {"X1(1)": 60.0, "Z1(1)": 20.0}, {"X3(1)": {"段三併出": ["X1(1)", "Z1(1)"]}},
          ["PX(1)", "QY(1)", "X1(1)", "Y1(1)", "Z1(1)"]))
    # K20 有剩下之判準一：P1 ＝ 200.00006（各半 100.00003）；X1 之分收 100.00、差 0.00003（round 4 ＝ 0）⇒ 視為全收：
    #     ⛔ 第 5 項、⛔ 轉調配、⛔ 段三部分併出／段三餘量；其列之結果 ＝ 成
    _cap20 = _cap(B3=160.0, B5=100.00003, B7=0.0)
    _run(out, "K20 差 0.00003（四位小數為 0）⇒ 視為全收：二列皆成、⛔ 第 5 項、⛔ 餘量之鍵",
         lambda: _go(ns, _cap20, a={"P1": 200.00006})[:4],
         ([("P1(1)", "後處理(c)", "成", "X1(1)", (("X1(1)", 100.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),))],
          {"X1(1)": 160.0, "Y1(1)": 100.0}, {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2}, _BL))
    _run(out, "K20′ 同上之調配之輸入：P1 歸原位次配地、⛔ 入合併單位（對照）",
         lambda: _intake(ns, _go(ns, _cap20, a={"P1": 200.00006})[4])[:2],
         ({"P1(1)": ("原位次配地", 200.0, 0.0), "R0(1)": ("共同負擔用地·入合併單位", 500.0, 0.0),
           "X2(1)": ("原位次配地", 60.0, 0.0)},
          [("gR", "公設軌", 500.0, ["R0(1)"])]))
    # K21 距離之四捨五入至 0.01 m：Z8 距 0.125 ⇒ 0.13 ＝ Z9 之 0.13 ⇒ 同距離 ⇒ G 大者（Z9·500）先
    _run(out, "K21 距離 0.125 四捨五入 ⇒ 0.13 ＝ Z9 ⇒ G 大者 Z9 先；紀錄之距離 ＝ 0.13",
         lambda: _go5(ns, {"BX": 60.0, "BY": 1000.0, "B7": 1000.0, "B8": 1000.0, "B9": 1000.0}),
         ([("Y1(1)", "題一 4", "未成", "X1(1)", ()), ("Y1(1)", "後處理·第5項", "成", "Z9(1)", (("Z9(1)", 90.0),)),
           ("X3(1)", "題一 4", "部分成", "X1(1)", (("X1(1)", 20.0),)),
           ("X3(1)", "後處理·第5項", "成", "Z9(1)", (("Z9(1)", 20.0),))],
          [("Y1(1)", "Z9(1)", 0.13, 500.0), ("X3(1)", "Z9(1)", 0.13, 590.0)]))
    # K22 候選為空（W1 整筆不過；g1 之他宗皆⛔ 保留）⇒ ⛔ 查 G（⛔ 停機·轉調配）；對照 ＝ K11（候選非空 ⇒ 停機）
    _run(out, "K22 候選為空 ⇒ alloc_state 未回 G 亦⛔ 停機：W1 未成 ⇒ 轉調配",
         lambda: _go(ns, _cap(B3=90.0), p_owner="gP", w1=True, no_g=True,
                     drop=("W1(1)", "Y1(1)", "Y2(1)", "Z1(1)"))[0],
         [("W1(1)", "後處理(a)", "未成", "X1(1)", (("X1(1)", 50.0),)), ("W1(1)", "後處理·第5項", "轉調配", "—", ())])
    return out


def _perturb(v):
    if isinstance(v, bool):
        return not v
    if isinstance(v, (int, float)):
        return v + 1
    if isinstance(v, str):
        return v + "′"
    if isinstance(v, tuple):
        return (v + ("′",)) if not v else (_perturb(v[0]),) + v[1:]
    if isinstance(v, list):
        return v + ["′"]
    if isinstance(v, dict):
        return dict(v, **{"′": 0})
    return ("′", v)


def selftest(repo):
    ns, _ = _harvest(repo)
    import selection_pipeline as sp
    need = [n for n in ("k6b_stage3_run", "adj_intake", "F3_CATEGORY_BURDEN") if n not in ns]
    if need or not hasattr(sp, "k6b_stage3_pool_temp"):
        print(f"  🔴 受詞缺：{need}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    cases = _cases(ns, sp)
    print("── 段三後處理之七項 3〜6 與第 5 項之序（K-9-51）──")
    red = _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    hits = 0
    for i in range(len(cases)):
        pert = [(n, g, (_perturb(e) if j == i else e)) for j, (n, g, e) in enumerate(cases)]
        r = _report(pert, verbose=False)
        base = set(red)
        code = cases[i][0].split()[0]
        if (set(r) - base) == {code} or (code in base and set(r) == base):
            hits += 1
    ok0 = hits == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {hits}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本案（harness ＋ 畫面）──
R2_EXPECT = {
    3.5: [
        (1, 'R5', '左', '628-18(2)', '②', '未成', '—', ()),
        (2, 'R3', '右', '628-45(2)', '①', '成', '628-45(2)', (('628-45(2)', 783.29),)),
        (3, 'R2', '左', '628-41(1)', '②', '成', '628-41(1)', (('628-41(1)', 241.7),)),
        (4, 'R3', '右', '628-42(2)', '—', '略·已定案', '—', ()),
        (5, 'R5', '左', '628-45(1)', '①', '成', '628-45(1)', (('628-45(1)', 541.69),)),
        (6, 'R2', '左', '628-42(1)', '—', '略·已定案', '—', ()),
        (7, 'R3', '右', '628-28(1)', '—', '略·已定案', '—', ()),
        (8, 'R2', '左', '628-27(1)', '—', '略·已定案', '—', ()),
        (9, 'R5', '左', '628-53(2)', '—', '略·已定案', '—', ()),
        (10, 'R2', '左', '628-40(1)', '—', '略·已定案', '—', ()),
        (11, 'R5', '左', '628-7(2)', '—', '略·已定案', '—', ()),
        (12, 'R3', '右', '628-27(2)', '—', '略·已定案', '—', ()),
        (13, 'R3', '右', '628-29(1)', '—', '略·已定案', '—', ()),
        ('後處理', 'R2', '—', '628-30(2)', '後處理(a)', '成', '628-45(2)', (('628-45(2)', 150.3),)),
        ('後處理', 'RD2', '—', '628-45(5)', '後處理(b)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 105.0325), ('628-45(2)', 101.1875))),
        ('後處理', 'RD2', '—', '628-30(4)', '後處理(b)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 48.7553), ('628-45(2)', 51.6647))),
        # 🔧 `W-G.9-361`（`K-9-54`·KL 裁 `2026-09-30`）：地籍相連之判之座標容差 ⇒ 地主甲之合併群含 `R6` 之 `628-20(1)`
        #   ⇒ `628-20(3)` 新增、`628-45(3)`／`628-45(4)` 三街廓平分（原二列：R3／R5 各 136.545／112.3）
        ('後處理', 'RD3', '—', '628-20(3)', '後處理(b)', '成', '628-20(1)', (('628-20(1)', 42.15),)),
        ('後處理', 'G1', '—', '628-45(3)', '後處理(c)', '成', ('628-20(1)', '628-45(1)', '628-45(2)'), (('628-20(1)', 91.03), ('628-45(1)', 91.03), ('628-45(2)', 91.03))),
        ('後處理', 'RD4', '—', '628-45(4)', '後處理(c)', '成', ('628-20(1)', '628-45(1)', '628-45(2)'), (('628-20(1)', 74.8667), ('628-45(1)', 74.8667), ('628-45(2)', 74.8667))),
    ],
    0.0: [],
}


def _norm_log(log):
    out = []
    for r in log or []:
        rv = r.get("受併宗")
        rv = rv if isinstance(rv, str) else tuple(rv)
        q = tuple(sorted((k, round(float(v), 4)) for k, v in (r.get("併入量") or {}).items()))
        s = r.get("序")
        out.append((s if isinstance(s, str) else int(s), r.get("街廓"), r.get("端"), r.get("候選"), r.get("層級"),
                    r.get("結果"), rv, q))
    return out


def _same_log(a, b):
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x[:7] != y[:7] or [k for k, _ in x[7]] != [k for k, _ in y[7]]:
            return False
        if any(abs(u - v) > TOL for (_, u), (_, v) in zip(x[7], y[7])):
            return False
    return True


def run(repo, sbs):
    # 🔧 `W-G.9-363`（發單側窗六十四）：R2 之期係段三之出（手冊先行〔`K-9-53` ①〕前之態·其亦以段三之鍵標之）
    #   ⇒ 行程內設 WV_K953=off
    os.environ["WV_K953"] = "off"
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    if "k6b_screen_callbacks" not in ns or not hasattr(sp, "_k6b_callbacks"):
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    f4 = _load(repo, "verify/probes/probe_WG9345_screen.py", "f4_for_f16")
    red = []
    for sb in sbs:
        ss = fst.session_state
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                snap = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fst, snap)
                rv.build_ownership(ns, fst, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
                params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
            cb = list(cb_by.values())
            saved, k917 = copy.deepcopy(dict(ss)), copy.deepcopy(ns["K917_DROPPED"])
            with contextlib.redirect_stdout(io.StringIO()):
                H = sp._k6b_callbacks(ns, fst, cb, cad, params, sb, snap)["alloc_state"](tp, bp)
            ss.clear(); ss.update(copy.deepcopy(saved))
            ns["K917_DROPPED"].clear(); ns["K917_DROPPED"].update(copy.deepcopy(k917))
            pk, g = f4._screen_inputs(ns, fst, snap, cb, cad, params, tp, bp, sb)
            qs = f4.QuietSt(ss)
            with contextlib.redirect_stdout(io.StringIO()):
                S = ns["k6b_screen_callbacks"](qs, pk_kwargs=pk, g_kwargs=g)["alloc_state"](tp, bp)
            ss.clear(); ss.update(copy.deepcopy(saved))
            ns["K917_DROPPED"].clear(); ns["K917_DROPPED"].update(copy.deepcopy(k917))
            with contextlib.redirect_stdout(io.StringIO()):
                _d, _s, _o, _w, _f, t3, b3 = sp.run_corner_pk_k6b(ns, fst, cb, cad, params, tp, bp, sb, snapshot=snap)
            log = copy.deepcopy(ss.get("f3_k6b_stage3_log") or [])
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️ {sb}：執行中止 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
            print("⇒ rc 3（無從判定）")
            return 3
        kept_h = {b: sorted(v) for b, v in sorted((H.get("kept") or {}).items())}
        kept_s = {b: sorted(v) for b, v in sorted((S.get("kept") or {}).items())}
        allk = sorted(p for v in kept_h.values() for p in v)
        gh, gs = H.get("G"), S.get("G")
        e1 = H.get("err") is None and S.get("err") is None and kept_h == kept_s and len(allk) > 0
        e2 = isinstance(gh, dict) and isinstance(gs, dict) and sorted(gh) == allk and sorted(gs) == allk
        dmax = max((abs(float(gh[p]) - float(gs[p])) for p in allk), default=0.0) if e2 else None
        e3 = e2 and dmax <= TOL and all(float(gh[p]) > 0 for p in allk)
        ok1 = e1 and e2 and e3
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：保留集 harness ＝ 畫面 {e1}（{len(allk)} 宗）；G 之鍵 ＝ 保留集 {e2}；"
              f"逐宗差 max {dmax}（≤ {TOL}）{e3}")
        if not ok1:
            red.append(f"R1@{sb}")
        got = _norm_log(log)
        e4 = _same_log(got, R2_EXPECT.get(sb, []))
        nk = sorted(t["暫編地號"] for t in t3 if "段三部分併出" in t or "段三餘量" in t)
        nr = sorted({r[5] for r in got} & {"部分成", "轉調配"})
        ok2 = e4 and not nk and not nr
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：段三紀錄 {len(got)} 列 ＝ 開工態 {e4}；新鍵之片 {nk}；新結果 {nr}")
        if not ok2:
            red.append(f"R2@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], argv[2]
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
