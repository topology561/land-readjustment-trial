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
   （剩下之部分所含之重劃前土地；已併出者⛔ 計·同「他處依地價折算併入的土地不計」）；
⑥ 趟中之帳（補令二）：同一趟之內（段三、手冊先行、第一趟之各一呼），建地一經部分併出，其後之試算所見之該片即帶其帳
   （`段三部分併出` 含本趟已併出之量）——其「面積_m2 ＋ 段三部分併出之和」恆等於其前受併入之量（玩具中為 `0`）。

子命令（一律 python verify/probes/probe_WG9373p1_partrem.py <子命令> <repo>）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取受詞）。玩具取自倉內既有之量測器（皆以 `importlib` 載入·⛔ 改其檔）：
           E 用 `F12`（`probe_WG9353_endmerge.py`）之 `_toy`／`_toy_cb`（街廓 BX·候選 C1(1)／C2(1)·`a_prime` ＝ a(src)）；
           S 用 `F16`（`probe_WG9357_k948.py`）之 `_world4`／`_cbs`／`_g`（題一之二末端塊）；
           I 用 `F27`（`probe_WG9373_k966.py`）之 `_w_world`（Y(1)·分攤 50·已部分併出 20）；
           M 用 `F23`（`probe_WG9363_k953.py`）之 `_go`／`_w1`（世界一·X1(1)·跨分配線併入 X1(2)）；
           Q 仿 `F27` 之 `_c`（入池閘·二宗同歸戶相鄰·G ＝ a × 0.6·a ＜ 150 ⇒ 不配地）。
           L 用 `F16` 之 `_world4`（段三）、`F27` 之 `_cbs`／`_tp`／`_R`（手冊先行·`F27` `T1` 之形；第一趟·`F27` `V1` 之形），
           其 `alloc_state` 包一層以記每次試算所見之受詞之片。
           E1〜E7 ＝ ①；S1〜S6 ＝ ②；I1〜I3 ＝ ③；M1〜M2 ＝ ④；Q1〜Q2 ＝ ⑤；L1〜L3 ＝ ⑥；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
           期值出自 KL 之裁（甲案）、`K-9-49`、`K-9-66` 通知 `3` 與補令一 `§二`（發單側手算·⛔ 呼叫受測碼求期）；
           等面積之對照（⛔ 帶前帳而面積同其剩下·其配地之結果須同）：E1／E2、E3／E4、E6／E7、S3／S5、S4／S6、M1／M2、Q1／Q2；
           S2 ＝ ⛔ 帶前帳之同片（非等面積）、I2 ＝ ⛔ 其後受併入之同片（非等面積）。
           🔧 `W-G.9-377`（`W-G.9-373` 補令二 `§三` 之⛔ 量之二項·⛔ 上列一字不刪）：增 L4〜L6（三處各一）——受詞之片帶前帳
           （向本趟亦併入之受併宗）且同一趟之內部分併出二次（L4／L5）或於其後之輪仍見（L6）：⑦ 趟中之帳之**累加**（其後之試算所見之
           「面積_m2 ＋ 段三部分併出之和」恆 ＝ 0·⛔ 以「最末一次」或「輸入之帳 ＋ 最末一次」代之）；⑧ `R-19″` 之重劃前面積之表之
           **取態**（受測碼呼叫 `k967_pre_area` 時所傳之表，其受詞之片之值 ＝ 分攤登記面積 − 當下之帳之和·⛔ 取輸入之態）——以
           包一層之 `k967_pre_area`（`ns` 即受測碼之 globals）記每次所傳之表之受詞之值。期值手算（各例之註）。
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


# ── L：趟中之帳（補令二）──
def _rec(st, ids, seen):
    def wrapped(temp, build):
        for b in build:
            if b["暫編地號"] in ids and float(b.get("面積_m2", 0) or 0) < -1e-9:
                seen.append(round(float(b.get("面積_m2", 0) or 0)
                                  + sum(float(v) for v in (b.get("段三部分併出") or {}).values()), 4) + 0.0)
        return st(temp, build)
    return wrapped


def _l1(ns, f16):
    temp, own, blocks, cl = f16._world4()
    build = [t for t in temp if t["街廓分類"] == f16.H]
    ap, _tw, st = f16._cbs({"BX": 60.0, "BY": 1000.0, "B7": 50.0}, None, ("Y1(1)",))
    seen = []
    thr = {("BX", "左"): 130.0, ("BY", "左"): 200.0}

    def tw(temp_, build_, blk, end, cand):
        b_ = {b["暫編地號"]: b for b in build_}
        g = f16._g(b_[cand]) if cand in b_ else 0.0
        return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]
    order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
             {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
    ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
    ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap, tw, _rec(st, {"Y1(1)"}, seen),
                         log_print=lambda *x: None, contests=ct)
    return sorted(set(seen)), len(seen) > 0


def _l2(ns, f27):
    tp, R = f27._tp, f27._R
    t = [tp("X(1)", "BA", f27.H, R(0, 10, 0, 30), 60), tp("Y(1)", "BA", f27.H, R(10, 20, 0, 30), 50),
         tp("Z(1)", "BA", f27.H, R(20, 30, 0, 30), 40),
         tp("A1(1)", "BB", f27.H, R(0, 10, 30, 60), 300), tp("B1(1)", "BB", f27.H, R(10, 20, 30, 60), 300),
         tp("C1(1)", "BB", f27.H, R(20, 30, 30, 60), 300), tp("A2(1)", "BD", f27.H, R(40, 50, 0, 30), 300)]
    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "Z": "丙", "C1": "丙"}
    blocks = {b: {"category": f27.H} for b in ("BA", "BB", "BD")}
    ap, st = f27._cbs({"BB": 130.0}, drop=("X(1)", "Y(1)", "Z(1)"))
    seen = []
    ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, _rec(st, {"X(1)", "Y(1)", "Z(1)"}, seen),
                          log_print=lambda *x: None)
    return sorted(set(seen)), len(seen) > 0


def _l3(ns, f27):
    tp, R = f27._tp, f27._R
    t = [tp("X1(1)", "BA", f27.H, R(0, 10, 0, 30), 60.0), tp("Y1(1)", "BA", f27.H, R(10, 20, 0, 30), 40.0),
         tp("X1(2)", "BB", f27.H, R(0, 10, 30, 60), 300), tp("Y2(1)", "BB", f27.H, R(10, 20, 30, 60), 300),
         tp("Y3(1)", "BC", f27.H, R(20, 30, 0, 30), 300)]
    own = {"X1": "g1", "Y1": "g2", "Y2": "g2", "Y3": "g2"}
    geom = {x["暫編地號"]: [list(c) for c in x["polygon_coords"]] for x in t}
    ap, st = f27._cbs({"BB": 50.0}, drop=("X1(1)", "Y1(1)"))
    subj = [{"歸戶": "g1", "軌": "建地軌", "錨點": "X1(1)", "名單": ["BB"], "片": ["X1(1)"], "原有面積合計": 60.0},
            {"歸戶": "g2", "軌": "建地軌", "錨點": "Y1(1)", "名單": ["BB"], "片": ["Y1(1)"], "原有面積合計": 40.0}]
    seen = []
    ns["adj4_pass1_run"](t, list(t), own, subj, geom, ap, _rec(st, {"X1(1)", "Y1(1)"}, seen), log_print=lambda *x: None)
    return sorted(set(seen)), len(seen) > 0


# 🆕 `W-G.9-377`：趟中之帳之累加（⑦）與 `R-19″` 之表之取態（⑧）
def _pre_spy(ns, ids, rec):
    """回 (原函式, 包一層者)：每次呼叫記其所傳之表中 `ids` 之值（依暫編地號排序之 tuple）。"""
    orig = ns["k967_pre_area"]

    def wrapped(pid, members, area_of):
        rec.append(tuple((x, round(float(area_of[x]), 4) + 0.0) for x in sorted(ids) if x in area_of))
        return orig(pid, members, area_of)
    return orig, wrapped


def _with_spy(ns, ids, fn):
    seen, rec = [], []
    orig, w = _pre_spy(ns, ids, rec)
    ns["k967_pre_area"] = w
    try:
        fn(seen)
    finally:
        ns["k967_pre_area"] = orig
    return sorted(set(seen)), sorted(set(rec)), len(seen) > 0


def _l4(ns, f27):
    """手冊先行（F27 T1 之形）：X(1)（甲·分攤 60）帶前帳（A1(1) 5·面積_m2 −5）。第 1 輪 BB（容 130）三片按比例 130 ÷ 145
    （X 55／Y 50／Z 40）⇒ X 再併入 A1(1) 49.3103；剩下 5.6897 於 K-9-51 之輪至 BD 之 A2(1)（容 5）⇒ 部分 5。
    ⑦ 第 2 輪之試算所見之 X(1)：面積_m2 −59.3103 −v ＋ 帳 {A1(1) 54.3103, A2(1) v} ＝ 0；⑧ 計畫之表（輸入之態）X 55／Y 50／Z 40；
    K-9-51 之表（第 1 輪之後）X 60 − 5 − 49.3103 ＝ 5.6897、Y 50 × 15 ÷ 145 ＝ 5.1724、Z 40 × 15 ÷ 145 ＝ 4.1379。"""
    tp, R, H = f27._tp, f27._R, f27.H
    x = tp("X(1)", "BA", H, R(0, 10, 0, 30), 60)
    x.update({"面積_m2": -5.0, "段三併出": ["A1(1)"], "段三部分併出": {"A1(1)": 5.0}})
    t = [x, tp("Y(1)", "BA", H, R(10, 20, 0, 30), 50), tp("Z(1)", "BA", H, R(20, 30, 0, 30), 40),
         tp("A1(1)", "BB", H, R(0, 10, 30, 60), 300), tp("B1(1)", "BB", H, R(10, 20, 30, 60), 300),
         tp("C1(1)", "BB", H, R(20, 30, 30, 60), 300), tp("A2(1)", "BD", H, R(40, 50, 0, 30), 300)]
    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "Z": "丙", "C1": "丙"}
    blocks = {b: {"category": H} for b in ("BA", "BB", "BD")}
    ap, st = f27._cbs({"BB": 130.0, "BD": 5.0}, drop=("X(1)", "Y(1)", "Z(1)"))
    ids = {"X(1)", "Y(1)", "Z(1)"}
    return _with_spy(ns, ids, lambda seen: ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, _rec(st, ids, seen),
                                                                log_print=lambda *a: None))


def _l5(ns, f27):
    """第一趟（F27 V1 之形）：X1(1)（g1·分攤 60）帶前帳（X1(2) 5·面積_m2 −5）；名單 BB → BC。第 1 輪至 BB 之 X1(2)（容 30）
    ⇒ 部分 30；第 2 輪至 BC 之 X1(3)（容 10）⇒ 部分 10；剩下 15 留於合併單位。⑦ 第 2 輪之試算所見之 X1(1)：
    面積_m2 −35 −v ＋ 帳 {X1(2) 35, X1(3) v} ＝ 0；⑧ 各輪之表：第 1 輪 60 − 5 ＝ 55、第 2 輪 60 − 5 − 30 ＝ 25。"""
    tp, R, H = f27._tp, f27._R, f27.H
    x = tp("X1(1)", "BA", H, R(0, 10, 0, 30), 60.0)
    x.update({"面積_m2": -5.0, "段三併出": ["X1(2)"], "段三部分併出": {"X1(2)": 5.0}})
    t = [x, tp("X1(2)", "BB", H, R(0, 10, 30, 60), 300), tp("X1(3)", "BC", H, R(20, 30, 0, 30), 300)]
    own = {"X1": "g1"}
    geom = {q["暫編地號"]: [list(c) for c in q["polygon_coords"]] for q in t}
    ap, st = f27._cbs({"BB": 30.0, "BC": 10.0}, drop=("X1(1)",))
    subj = [{"歸戶": "g1", "軌": "建地軌", "錨點": "X1(1)", "名單": ["BB", "BC"], "片": ["X1(1)"], "原有面積合計": 60.0}]
    return _with_spy(ns, {"X1(1)"}, lambda seen: ns["adj4_pass1_run"](t, list(t), own, subj, geom, ap,
                                                                      _rec(st, {"X1(1)"}, seen),
                                                                      log_print=lambda *a: None))


def _l6(ns, f16):
    """段三（F28 L1 之形）：Y1(1)（分攤 90）帶前帳（X1(1) 5·面積_m2 −5）；題一 4 再部分併入 X1(1) 20，剩下於第 5 項之輪至
    Z1(1)（部分 50）。⑦ 其後之試算所見之 Y1(1)：面積_m2 ＋ 帳之和 ＝ 0（帳 {X1(1) 25, Z1(1) …}）；⑧ 第 5 項之表（題一 4 之後）
    Y1(1) ＝ 90 − 5 − 20 ＝ 65。"""
    temp, own, blocks, cl = f16._world4()
    for q in temp:
        if q["暫編地號"] == "Y1(1)":
            q.update({"面積_m2": -5.0, "段三併出": ["X1(1)"], "段三部分併出": {"X1(1)": 5.0}})
    build = [q for q in temp if q["街廓分類"] == f16.H]
    ap, _tw, st = f16._cbs({"BX": 60.0, "BY": 1000.0, "B7": 50.0}, None, ("Y1(1)",))
    thr = {("BX", "左"): 130.0, ("BY", "左"): 200.0}

    def tw(temp_, build_, blk, end, cand):
        b_ = {b["暫編地號"]: b for b in build_}
        g = f16._g(b_[cand]) if cand in b_ else 0.0
        return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]
    order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
             {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
    ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
    return _with_spy(ns, {"Y1(1)"}, lambda seen: ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap,
                                                                      tw, _rec(st, {"Y1(1)"}, seen),
                                                                      log_print=lambda *a: None, contests=ct))


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
    _run(out, "L1 趟中之帳·段三（F28 S2 之形）：Y1(1) 題一 4 部分併出 X1(1) 20 之後，其後之試算所見之 Y1(1) 皆帶其帳"
              "（面積_m2 ＋ 段三部分併出之和 ＝ 0）",
         lambda: _l1(ns, f16), ([0.0], True))
    _run(out, "L2 趟中之帳·手冊先行（F27 T1 之形）：X／Y／Z 第 1 輪按比例部分併出之後，其後之試算所見者皆帶其帳",
         lambda: _l2(ns, f27), ([0.0], True))
    _run(out, "L3 趟中之帳·第一趟（F27 V1 之形）：X1(1)／Y1(1) 於 BB 按比例部分併出之試施，其試算所見者皆帶其帳",
         lambda: _l3(ns, f27), ([0.0], True))
    # 🆕 `W-G.9-377`
    _run(out, "L4 趟中之帳之累加與 K-9-51 之表之取態·手冊先行：X(1) 帶前帳、同一趟部分併出二次 ⇒ 所見恆 0；"
              "表 ＝ 計畫時 55／50／40、K-9-51 時 5.6897／5.1724／4.1379",
         lambda: _l4(ns, f27),
         ([0.0], [(("X(1)", 5.6897), ("Y(1)", 5.1724), ("Z(1)", 4.1379)),
                  (("X(1)", 55.0), ("Y(1)", 50.0), ("Z(1)", 40.0))], True))
    _run(out, "L5 趟中之帳之累加與各輪之表之取態·第一趟：X1(1) 帶前帳、二輪各部分併出 ⇒ 所見恆 0；表 ＝ 第 1 輪 55、第 2 輪 25",
         lambda: _l5(ns, f27), ([0.0], [(("X1(1)", 25.0),), (("X1(1)", 55.0),)], True))
    _run(out, "L6 趟中之帳之累加與第 5 項之表之取態·段三：Y1(1) 帶前帳、題一 4 再併入同一受併宗 ⇒ 所見恆 0；表 ＝ 65",
         lambda: _l6(ns, f16), ([0.0], [(("Y1(1)", 65.0),)], True))
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
