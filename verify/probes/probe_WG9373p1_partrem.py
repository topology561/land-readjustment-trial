# -*- coding: utf-8 -*-
"""W-G.9-373 補令一 量測器（發單側窗七十六擬·檔 F28·⛔ 由受單側改一字）：部分併入他處後剩下之土地，其後與一分未併入之土地
同樣處理（KL 裁 `2026-10-08 20:18`「是，採甲案」）；已併入之部分⛔ 動、⛔ 重分；其帳（`段三併出`／`段三部分併出`／`段三餘量`）
逐趟累計——
① 末端塊之合併再試（`end_block_merge_run`）：部分併出之剩下（建地仍在 build；道路片、公設片帶正之 `段三餘量`）⛔ 列為除外
   （除外唯已全數併出者·`K-9-49 ③`），得為跨占者、同地主相鄰之土地與後處理之片；
   除外之集之「段三」之部分唯取已全數併出者；上鎖者與已分配予街角者照舊除外；
② 段三（`k6b_stage3_run`）：輸入之片帶 `段三併出` 與 `段三餘量` 者，其可併之量 ＝ `段三餘量`（依其面積之比 ρ0 ＝ `段三餘量` ÷ a 折算·折算比
   ⛔ 受 ρ0 之影響）；本趟所觸之片而其輸入帶前帳者，`段三併出` 取聯集、仍有剩下者 `段三部分併出` 逐受併宗相加、全數併出者
   去 `段三部分併出`／`段三餘量`；本趟未觸之片之帳⛔ 動；
③ 調配之輸入（`adj_intake`）：建地之部分併出之剩下 ＝ 分攤登記面積 − `段三部分併出` 之和（其後縱受他片併入亦⛔ 變）；
④ 手冊先行（`k953_manual_run`）：仍在 build 之建地片縱帶段三之鍵亦受理（其量 ＝ 剩下）；`段三併出` 取聯集；
⑤ `K-9-67` 之重劃前面積（入池閘 `k929_6_fixpoint` 之代表宗等四處）：部分併出之剩下 ＝ 分攤登記面積 − `段三部分併出` 之和
   （剩下之部分所含之重劃前土地；已併出者⛔ 計·同「他處依地價折算併入的土地不計」）。

子命令（一律 python verify/probes/probe_WG9373p1_partrem.py <子命令> <repo>）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取受詞）。玩具取自倉內既有之量測器（皆以 `importlib` 載入·⛔ 改其檔）：
           E 用 `F12`（`probe_WG9353_endmerge.py`）之 `_toy`／`_toy_cb`（街廓 BX·候選 C1(1)／C2(1)·`a_prime` ＝ a(src)）；
           S 用 `F16`（`probe_WG9357_k948.py`）之 `_world4`／`_cbs`／`_g`（題一之二末端塊）；
           I 用 `F27`（`probe_WG9373_k966.py`）之 `_w_world`（Y(1)·分攤 50·已部分併出 20）；
           M 用 `F23`（`probe_WG9363_k953.py`）之 `_go`／`_w1`（世界一·X1(1)·跨分配線併入 X1(2)）；
           Q 仿 `F27` 之 `_c`（入池閘·二宗同歸戶相鄰·G ＝ a × 0.6·a ＜ 150 ⇒ 不配地）。
           E1〜E7 ＝ ①；S1〜S6 ＝ ②；I1〜I3 ＝ ③；M1〜M2 ＝ ④；Q1〜Q2 ＝ ⑤；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
           期值出自 KL 之裁（甲案）、`K-9-49`、`K-9-66` 通知 `3` 與補令一 `§二`（發單側手算·⛔ 呼叫受測碼求期）；
           等面積之對照（⛔ 帶前帳而面積同其剩下·其配地之結果須同）：E1／E2、E3／E4、E6／E7、S3／S5、S4／S6、M1／M2、Q1／Q2；
           S2 ＝ ⛔ 帶前帳之同片（非等面積）、I2 ＝ ⛔ 其後受併入之同片（非等面積）。
rc：0 相符／1 不符／2 用法錯。
"""
import contextlib, copy, importlib.util, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

NEED = ("end_block_merge_run", "k6b_stage3_run", "adj_intake", "k953_manual_run", "F3_CATEGORY_BURDEN")
KEYS3 = ("段三併出", "段三部分併出", "段三餘量")


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


def _keys(t):
    out = {}
    for k in KEYS3:
        if k in t:
            v = t[k]
            out[k] = (tuple(sorted((a, round(float(b), 2)) for a, b in v.items())) if isinstance(v, dict)
                      else (round(float(v), 2) if k == "段三餘量" else tuple(v)))
    return out


# ── E：末端塊之合併再試（F12 之玩具·門檻 thr·`a_prime` ＝ a(src)）──
def _e(ns, f12, *, thr, a_c1b, pre=None, a_upd=None, corner=()):
    temp, build, own, blocks = f12._toy(a_c1b)
    by = {t["暫編地號"]: t for t in temp}
    for pid, a in (a_upd or {}).items():
        by[pid]["分攤登記面積_m2"] = float(a)
    for pid, kv in (pre or {}).items():
        by[pid].update(copy.deepcopy(kv))
    ap_, ev_, st_, _calls = f12._toy_cb(thr, False, None, False)
    t2, b2, log, rec = ns["end_block_merge_run"](temp, build, own, set(), set(corner), blocks, {}, ap_, ev_, st_,
                                                 setback=3.5, log_print=lambda *x: None)
    rows = [(r["候選"], r["層級"], r["結果"], r["檢核"], r.get("試算G")) for r in log if r.get("序") != "後處理"]
    o = {t["暫編地號"]: t for t in t2}
    return (rows, rec.get("皆未達"), {p: _keys(o[p]) for p in ("C1(2)", "R2(1)")},
            sorted(b["暫編地號"] for b in b2))


_C12 = {"C1(2)": {"段三併出": ["X(1)"], "段三部分併出": {"X(1)": 10.0}, "面積_m2": -10.0}}
_R2 = {"R2(1)": {"段三併出": ["Q(1)"], "段三部分併出": {"Q(1)": 40.0}, "段三餘量": 30.0}}


# ── S：段三之帳（F16 之 _world4·題一）──
def _s(ns, f16, *, pre=None):
    temp, own, blocks, cl = f16._world4()
    by = {t["暫編地號"]: t for t in temp}
    for pid, kv in (pre or {}).items():
        by[pid].update(copy.deepcopy(kv))
    build = [t for t in temp if t["街廓分類"] == f16.H]
    ap, _tw, st = f16._cbs({"BX": 60.0, "BY": 1000.0, "B7": 50.0}, None, ("Y1(1)",))
    thr = {("BX", "左"): 130.0, ("BY", "左"): 200.0}

    def tw(temp_, build_, blk, end, cand):
        b_ = {b["暫編地號"]: b for b in build_}
        g = f16._g(b_[cand]) if cand in b_ else 0.0
        return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]
    order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
             {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
    ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
    t2, b2, log = ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap, tw, st,
                                       log_print=lambda *x: None, contests=ct)
    o = {t["暫編地號"]: t for t in t2}
    head = [(r["候選"], r["層級"], r["結果"]) for r in log if r.get("序") != "後處理"]
    x3t14 = [(r["結果"], round(float(r.get("全量") or 0), 2)) for r in log
             if r.get("序") == "後處理" and r.get("候選") == "X3(1)" and r.get("層級") == "題一 4"]
    return (head, x3t14, {p: _keys(o[p]) for p in ("X3(1)", "Y1(1)")},
            {p: round(float(o[p].get("面積_m2", 0) or 0), 2) for p in ("X1(1)", "Y1(1)")},
            "Y1(1)" in [b["暫編地號"] for b in b2])


# ── I：調配之輸入之剩下（F27 之 _w_world）──
def _i(ns, f27, *, alloc_y, recv):
    temp, build, g_rows, dropped, own = f27._w_world(alloc_y)
    y = next(t for t in temp if t["暫編地號"] == "Y(1)")
    y["面積_m2"] = float(y["面積_m2"]) + float(recv)
    burden = {"BA": ns["F3_CATEGORY_BURDEN"][f27.H], "BB": ns["F3_CATEGORY_BURDEN"][f27.H]}
    r = ns["adj_intake"](temp, build, g_rows, dropped, own, burden)
    s = next(x for x in r["slices"] if x["暫編地號"] == "Y(1)")
    return s["類"], round(float(s["原有面積"]), 2), round(float(s.get("段三併出面積") or 0), 2)


# ── M：手冊先行之受理（F23 之 _go／_w1）──
def _m(ns, f23, *, pre=None, a_upd=None):
    f23._NS["fn"] = ns["k953_manual_run"]
    res = f23._go(f23._w1, own_upd={"Z1": "g1"}, rm=("R1(1)", "P1(1)"), pre=pre, a_upd=a_upd)
    t2, b2, log = res[0]
    rows = [(r.get("序"), r.get("片"), tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items())))
            for r in log]
    o = {t["暫編地號"]: t for t in t2}
    return rows, _keys(o["X1(1)"]), "X1(1)" in [b["暫編地號"] for b in b2]


# ── Q：入池閘之代表宗之重劃前面積（仿 F27 之 _c）──
def _q(ns, f27, y1):
    fl = {"B": {"p1": (0.0, 0.0), "p2": (100.0, 0.0)}}

    def P(pid, x0, x1, kv, lot):
        d = {"暫編地號": pid, "原地號": lot, "所屬街廓": "B", "重劃前地價區段": "z1", "polygon_coords": f27._rect(x0, x1)}
        d.update(copy.deepcopy(kv))
        return d

    def trial(b):
        rows, dl = [], []
        for t in b:
            a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
            if a < 150:
                dl.append({"暫編地號": t["暫編地號"], "G(㎡)": a * 0.6})
            else:
                rows.append({"暫編地號": t["暫編地號"], "推進側別": "left", "G(㎡)": a * 0.6, "驗_宗序": "其後"})
        return rows, ({("B", "left"): dl} if dl else {}), None
    b = [P("Y1", 0, 2, y1, "L1"), P("Y2", 2, 4, {"分攤登記面積_m2": 100.0, "面積_m2": 0.0}, "L2")]
    _bf, _o, log = ns["k929_6_fixpoint"](b, trial, {"L1": "G1", "L2": "G1"}, {"z1": 1000.0}, fl)
    return [e["標的"] for e in log]


def _cases(ns, f12, f16, f27, f23):
    out = []
    # E（門檻 150）：C1(1)（a 100）以 ① 同街廓併 C1(2)；C1(2) 部分併出之剩下 50（分攤 60·已併出 10）≡ 一分未併而 a 50
    _run(out, "E1 末端塊合併再試：同地主相鄰之 C1(2) 為部分併出之剩下（50）⇒ 得併入（⛔ 除外）：100 ＋ 50 ＝ 150 ⇒ ① 成；"
              "C1(2) 全數併出 ⇒ 段三併出 取聯集、去 段三部分併出",
         lambda: _e(ns, f12, thr=150.0, a_c1b=60.0, pre=_C12),
         ([("C1(1)", "①", "成", "免", 150.0), ("C2(1)", "—", "略·已定案", "—", "—")], {},
          {"C1(2)": {"段三併出": ("C1(1)", "X(1)")}, "R2(1)": {}}, ["C1(1)", "C2(1)", "D(1)"]))
    _run(out, "E2 對照：C1(2) 一分未併而 a ＝ 50 ⇒ 同 E1 之配地",
         lambda: _e(ns, f12, thr=150.0, a_c1b=50.0),
         ([("C1(1)", "①", "成", "免", 150.0), ("C2(1)", "—", "略·已定案", "—", "—")], {},
          {"C1(2)": {"段三併出": ("C1(1)",)}, "R2(1)": {}}, ["C1(1)", "C2(1)", "D(1)"]))
    # E（門檻 115）：C1(1) ＋ C1(2)（10）＝ 110 未達；C2(1)（90）以 ② 併道路片 R2(1)——R2 部分併出之剩下 30（分攤 70·已併出 40）
    _run(out, "E3 末端塊合併再試：同地主之道路片 R2(1) 為部分併出之剩下（30）⇒ 得併入、其量 ＝ 30：90 ＋ 30 ＝ 120 ⇒ ② 成；"
              "R2 全數併出 ⇒ 段三併出 取聯集、去 段三部分併出／段三餘量",
         lambda: _e(ns, f12, thr=115.0, a_c1b=10.0, pre=_R2),
         ([("C1(1)", "①", "未成", "—", 110.0), ("C2(1)", "②", "成", "通過", 120.0)], {},
          {"C1(2)": {}, "R2(1)": {"段三併出": ("C2(1)", "Q(1)")}}, ["C1(1)", "C1(2)", "C2(1)", "D(1)"]))
    _run(out, "E4 對照：R2(1) 一分未併而 a ＝ 30 ⇒ 同 E3 之配地",
         lambda: _e(ns, f12, thr=115.0, a_c1b=10.0, a_upd={"R2(1)": 30.0}),
         ([("C1(1)", "①", "未成", "—", 110.0), ("C2(1)", "②", "成", "通過", 120.0)], {},
          {"C1(2)": {}, "R2(1)": {"段三併出": ("C2(1)",)}}, ["C1(1)", "C1(2)", "C2(1)", "D(1)"]))
    _run(out, "E5 本趟未觸之片之帳⛔ 動：同 E1，另道路片 R2(1)（他地主·帶前帳·本趟未觸）⇒ 其三鍵照舊",
         lambda: _e(ns, f12, thr=150.0, a_c1b=60.0, pre=dict(_C12, **_R2)),
         ([("C1(1)", "①", "成", "免", 150.0), ("C2(1)", "—", "略·已定案", "—", "—")], {},
          {"C1(2)": {"段三併出": ("C1(1)", "X(1)")},
           "R2(1)": {"段三併出": ("Q(1)",), "段三部分併出": (("Q(1)", 40.0),), "段三餘量": 30.0}},
          ["C1(1)", "C2(1)", "D(1)"]))
    _run(out, "E6 部分併出之剩下 C1(2) 已分配予街角（corner_lots）⇒ 照舊除外：C1(1) 未成；C2(1) 以 ② 道路成；C1(2) 之帳⛔ 動",
         lambda: _e(ns, f12, thr=150.0, a_c1b=60.0, pre=_C12, corner=("C1(2)",)),
         ([("C1(1)", "—", "未成", "—", "—"), ("C2(1)", "②", "成", "通過", 160.0)], {},
          {"C1(2)": {"段三併出": ("X(1)",), "段三部分併出": (("X(1)", 10.0),)}, "R2(1)": {"段三併出": ("C2(1)",)}},
          ["C1(1)", "C1(2)", "C2(1)", "D(1)"]))
    _run(out, "E7 對照：C1(2) 一分未併而 a ＝ 50、已分配予街角 ⇒ 同 E6 之配地",
         lambda: _e(ns, f12, thr=150.0, a_c1b=50.0, corner=("C1(2)",)),
         ([("C1(1)", "—", "未成", "—", "—"), ("C2(1)", "②", "成", "通過", 160.0)], {},
          {"C1(2)": {}, "R2(1)": {"段三併出": ("C2(1)",)}},
          ["C1(1)", "C1(2)", "C2(1)", "D(1)"]))
    # S（題一）：對照 ⇒ X1(1) 以 ② 之半（X3 之半 40）成；Y1(1) 題一 4 部分併入 X1(1) 20、第 5 項部分併入 Z1(1) 50
    _run(out, "S1 段三：Y1(1) 帶前帳（Q9(1) 5·面積_m2 −5）而本趟再部分併出（X1(1) 20、Z1(1) 50）⇒ 段三併出 聯集、"
              "段三部分併出 相加、面積_m2 −75、仍在 build",
         lambda: _s(ns, f16, pre={"Y1(1)": {"段三併出": ["Q9(1)"], "段三部分併出": {"Q9(1)": 5.0}, "面積_m2": -5.0}}),
         ([("X1(1)", "②半", "成"), ("Y1(1)", "②半", "未成")], [("未成", 40.0)],
          {"X3(1)": {"段三併出": ("X1(1)",), "段三部分併出": (("X1(1)", 40.0),), "段三餘量": 40.0},
           "Y1(1)": {"段三併出": ("Q9(1)", "X1(1)", "Z1(1)"),
                     "段三部分併出": (("Q9(1)", 5.0), ("X1(1)", 20.0), ("Z1(1)", 50.0))}},
          {"X1(1)": 60.0, "Y1(1)": -75.0}, True))
    _run(out, "S2 對照：Y1(1) ⛔ 帶前帳 ⇒ 本趟之帳唯 X1(1) 20、Z1(1) 50、面積_m2 −70",
         lambda: _s(ns, f16),
         ([("X1(1)", "②半", "成"), ("Y1(1)", "②半", "未成")], [("未成", 40.0)],
          {"X3(1)": {"段三併出": ("X1(1)",), "段三部分併出": (("X1(1)", 40.0),), "段三餘量": 40.0},
           "Y1(1)": {"段三併出": ("X1(1)", "Z1(1)"), "段三部分併出": (("X1(1)", 20.0), ("Z1(1)", 50.0))}},
          {"X1(1)": 60.0, "Y1(1)": -70.0}, True))
    _run(out, "S3 段三：道路片 X3(1)（分攤 80）帶前帳（已併出 40·段三餘量 40）⇒ 其可併之量 ＝ 40：半 20 ⇒ 100 ＋ 20 ＜ 130 不成，"
              "整片 40 ⇒ 140 ⇒ ② 成；X3 全數併出 ⇒ 段三併出 聯集（Q8(1)、X1(1)）、去他二鍵",
         lambda: _s(ns, f16, pre={"X3(1)": {"段三併出": ["Q8(1)"], "段三部分併出": {"Q8(1)": 40.0}, "段三餘量": 40.0}}),
         ([("X1(1)", "②", "成"), ("Y1(1)", "②", "未成")], [],
          {"X3(1)": {"段三併出": ("Q8(1)", "X1(1)")},
           "Y1(1)": {"段三併出": ("X1(1)", "Z1(1)"), "段三部分併出": (("X1(1)", 20.0), ("Z1(1)", 50.0))}},
          {"X1(1)": 60.0, "Y1(1)": -70.0}, True))
    _run(out, "S4 段三：X3(1) 帶前帳（已併出 20·段三餘量 60）⇒ 半 30 ⇒ 100 ＋ 30 ＝ 130 ⇒ ②半 成；其另半於題一 4 之全量 30"
              "（折算比 ＝ 1·⛔ 受 ρ0 之影響）未成（BX 已滿）、第 5 項 Z1(1) 亦滿 ⇒ 段三部分併出 Q8(1) 20 ＋ X1(1) 30、段三餘量 30；"
              "Y1(1) 題一 4 併 X1(1) 30、第 5 項併 Z1(1) 50 ⇒ 面積_m2 −80",
         lambda: _s(ns, f16, pre={"X3(1)": {"段三併出": ["Q8(1)"], "段三部分併出": {"Q8(1)": 20.0}, "段三餘量": 60.0}}),
         ([("X1(1)", "②半", "成"), ("Y1(1)", "②半", "未成")], [("未成", 30.0)],
          {"X3(1)": {"段三併出": ("Q8(1)", "X1(1)"), "段三部分併出": (("Q8(1)", 20.0), ("X1(1)", 30.0)), "段三餘量": 30.0},
           "Y1(1)": {"段三併出": ("X1(1)", "Z1(1)"), "段三部分併出": (("X1(1)", 30.0), ("Z1(1)", 50.0))}},
          {"X1(1)": 60.0, "Y1(1)": -80.0}, True))
    _run(out, "S5 對照：X3(1) 一分未併而 a ＝ 40 ⇒ 同 S3 之配地",
         lambda: _s(ns, f16, pre={"X3(1)": {"分攤登記面積_m2": 40.0}}),
         ([("X1(1)", "②", "成"), ("Y1(1)", "②", "未成")], [],
          {"X3(1)": {"段三併出": ("X1(1)",)},
           "Y1(1)": {"段三併出": ("X1(1)", "Z1(1)"), "段三部分併出": (("X1(1)", 20.0), ("Z1(1)", 50.0))}},
          {"X1(1)": 60.0, "Y1(1)": -70.0}, True))
    _run(out, "S6 對照：X3(1) 一分未併而 a ＝ 60 ⇒ 同 S4 之配地",
         lambda: _s(ns, f16, pre={"X3(1)": {"分攤登記面積_m2": 60.0}}),
         ([("X1(1)", "②半", "成"), ("Y1(1)", "②半", "未成")], [("未成", 30.0)],
          {"X3(1)": {"段三併出": ("X1(1)",), "段三部分併出": (("X1(1)", 30.0),), "段三餘量": 30.0},
           "Y1(1)": {"段三併出": ("X1(1)", "Z1(1)"), "段三部分併出": (("X1(1)", 30.0), ("Z1(1)", 50.0))}},
          {"X1(1)": 60.0, "Y1(1)": -80.0}, True))
    _run(out, "I1 調配之輸入：部分併出之建地（其單元不配地·分攤 50·已併出 20）其後受併入 30 ⇒ 原有面積 30、段三併出面積 20",
         lambda: _i(ns, f27, alloc_y=False, recv=30.0), ("建築街廓內不能分配", 30.0, 20.0))
    _run(out, "I2 對照：⛔ 受併入 ⇒ 原有面積 30、段三併出面積 20",
         lambda: _i(ns, f27, alloc_y=False, recv=0.0), ("建築街廓內不能分配", 30.0, 20.0))
    _run(out, "I3 其單元配地而其後受併入 30 ⇒ 原位次配地·原有面積 30、段三併出面積 20",
         lambda: _i(ns, f27, alloc_y=True, recv=30.0), ("原位次配地", 30.0, 20.0))
    _run(out, "M1 手冊先行：X1(1) 為部分併出之剩下（分攤 60·已併出 10·仍在 build）⇒ 受理：跨分配線整筆併入 X1(2) 50；"
              "段三併出 聯集、去 段三部分併出",
         lambda: _m(ns, f23, pre={"X1(1)": {"段三併出": ["C1(1)"], "段三部分併出": {"C1(1)": 10.0}, "面積_m2": -10.0}}),
         ([("整批", "1 片", ()), ("手冊", "X1(1)", (("X1(2)", 50.0),))], {"段三併出": ("C1(1)", "X1(2)")}, False))
    _run(out, "M2 對照：X1(1) 一分未併而 a ＝ 50 ⇒ 同 M1 之併入",
         lambda: _m(ns, f23, a_upd={"X1(1)": 50.0}),
         ([("整批", "1 片", ()), ("手冊", "X1(1)", (("X1(2)", 50.0),))], {"段三併出": ("X1(2)",)}, False))
    _run(out, "Q1 入池閘之代表宗：Y1 為部分併出之剩下（分攤 130·已併出 40·其後受併入 10 ⇒ a 100）與 Y2（a 100）G 並列 60 ⇒ "
              "重劃前面積 Y1 ＝ 130 − 40 ＝ 90 ＜ 100 ⇒ Y2",
         lambda: _q(ns, f27, {"分攤登記面積_m2": 130.0, "面積_m2": -30.0, "段三併出": ["Q(1)"],
                              "段三部分併出": {"Q(1)": 40.0}}), ["Y2"])
    _run(out, "Q2 對照：Y1 一分未併而分攤 90、其後受併入 10 ⇒ 同 Q1",
         lambda: _q(ns, f27, {"分攤登記面積_m2": 90.0, "面積_m2": 10.0}), ["Y2"])
    return out


def selftest(repo):
    ns, _ = _harvest(repo)
    need = [n for n in NEED if n not in ns]
    if need:
        print(f"  🔴 受詞缺：{need}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    f12 = _load(repo, "verify/probes/probe_WG9353_endmerge.py", "f12_f28")
    f16 = _load(repo, "verify/probes/probe_WG9357_k948.py", "f16_f28")
    f27 = _load(repo, "verify/probes/probe_WG9373_k966.py", "f27_f28")
    f23 = _load(repo, "verify/probes/probe_WG9363_k953.py", "f23_f28")
    cases = _cases(ns, f12, f16, f27, f23)
    print("── 部分併入他處後剩下之土地於其後各段（甲案）──")
    red = _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    hits = 0
    base = set(red)
    for i in range(len(cases)):
        pert = [(n, g, (_perturb(e) if j == i else e)) for j, (n, g, e) in enumerate(cases)]
        r = _report(pert, verbose=False)
        code = cases[i][0].split()[0]
        if (set(r) - base) == {code} or (code in base and set(r) == base):
            hits += 1
    ok0 = hits == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {hits}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3 or argv[1] != "selftest":
        print(__doc__)
        return 2
    return selftest(os.path.abspath(argv[2]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
