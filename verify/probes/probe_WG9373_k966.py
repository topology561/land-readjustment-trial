# -*- coding: utf-8 -*-
"""W-G.9-373 量測器（發單側窗七十五擬·檔 F27·⛔ 由受單側改一字）：`K-9-66`（同一街廓要併入他處之土地之順序及比例）、
`K-9-68`（多位地主之土地陸續到達同一街廓：同一輪到達者始按比例、先到者⛔ 重分）、`K-9-67`（應分配面積相同而須擇一宗者：
重劃前面積大者先、再同取暫編地號小者）之落地——三處（手冊先行 `k953_manual_run`、段三後處理 `k6b_stage3_run`、第一趟
`adj4_pass1_run`）、入池閘之代表宗（`k929_6_fixpoint`）、建地之部分併出之下游（`adj_intake`、`k6b_stage3_pool_temp`）。

子命令（一律 python verify/probes/probe_WG9373_k966.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取受詞；`verify/selection_pipeline.py` 取 `k6b_stage3_pool_temp`）。
           玩具之回呼：`alloc_state` 以 build 之全部（`drop` 除外）為保留；街廓內受併之累加（正之 `面積_m2` 之和·建地之
           部分併出之負值⛔ 計）`>` 該街廓之容量 ⇒ 該街廓之配餘地不合格一處；`G` ＝ 分攤登記面積 ＋ 面積（`gmap` 覆寫）；
           `a_prime` ＝ a(src)（地價皆同）。
           A1〜A9 ＝ `k966_block_merge`（單一受併之街廓·純函式·KL 例一／例二·格·逐類·停機·態之承接）；
           B1〜B3 ＝ `k967_rank`／`k967_pre_area`；C1〜C4 ＝ 入池閘之代表宗之並列（`K-9-67`·`0.01 ㎡`）；
           T1〜T3 ＝ 手冊先行（三位地主同到一街廓 ⇒ 按比例；`K-9-68` 先到者⛔ 重分；第 2 輪二位地主同到他街廓 ⇒ 亦按比例）；U0〜U2 ＝ 段三後處理（二位地主同到
           一街廓 ⇒ 按比例；第 2 輪同到他街廓 ⇒ 亦按比例）；V1〜V2 ＝ 第一趟（二受詞同到 ⇒ 按比例；`K-9-68`）；
           W1〜W3 ＝ 建地之部分併出之下游（調配之輸入之類與面積、公設地調配之 temp）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
           期值出自 `K-9-66`／`K-9-67`／`K-9-68` 與規格單 `§三`（發單側手算·⛔ 呼叫受測碼求期）。
  wiring   <repo>
           Y1 模組層之新名與簽名（`K966_CLASSES`、`K966_GRID`、`k966_block_merge`、`k967_rank`、`k967_pre_area`）；
           Y2 `k966_block_merge` 之呼叫恰在三處（`k953_manual_run`、`k6b_stage3_run`、`adj4_pass1_run`）各恰一見、他處⛔ 見；
           Y3 `k967_rank` 之呼叫見於 `k929_6_fixpoint`、`k953_manual_run`（≥ 3）、`k6b_stage3_run`、`adj4_pass1_run`；
           Y4 新碼⛔ 案件字面；Y5 已去之巢狀 def（`_max357`、`_k951`、`_split357`、`_fill953`、`_remain953`、`_vmax_a4`）
           於 app.py ⛔ 見；Y6 三處及入池閘⛔ 以「並列 ⇒ 停機」之舊字樣（「應分配面積並列」）擇宗。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 三處之紀錄皆一次全部試併即過（段三後處理⛔ `K-9-66`／第 5 項之列；
           手冊先行之整批成、⛔ `K-9-66`／`K-9-51` 之列；第一趟之整體皆成）；R2 入池閘之代表宗：本案唯 `R3`（地主
           `G014`）之 `628-28(1)`／`628-29(1)` 應分配面積並列（`0.01 ㎡`），其重劃前面積亦同（`114.00`）⇒ 取暫編地號小者
           `628-28(1)`（＝ 現行）；`R6` 之代表宗 ＝ `628-21(1)`（G 最大·非並列）；R3 段三之試算（harness 與畫面·同一宗地）
           之 `members` 相同，且含入池閘之單元之成員。
  🔧 `W-G.9-377`（⛔ 上列一字不刪）：
  selftest 增 T5（手冊先行之第 1 輪之來源量 ＝ 計畫之量 ÷ κ·玩具之地價 BB 為 BA 之半）；P0 隨之 28 項。
  wiring   增 Y7（三處之 `k966_block_merge` 皆以 `state` 為前態、以其回傳之態承接·`F17` 之 W2 之代）。
  mutate   <repo>
           以受測碼之字樣為錨之突變 N01〜N57（`MUT377`·`F17` 之 W2／W3／W12 與 `F25` 之 M01〜M19／M28／M29／M31 之代·
           `k966_block_merge`、`k967_rank`／`k967_pre_area`、三處之試施·輪·候選·趟中之帳·表之取態·段三步驟 10、調配之輸入）：
           每一突變於 `app.py` 之所指函式之區間錨恰一見，施之於倉外之暫存之 `app.py`，以子程序跑本器、F28、F23、F24、F16
           之 selftest 之項，其「所指之項」皆須紅；另跑基準一（⛔ 突變·五器之項皆綠）。受測碼之該段改寫者其錨隨之更新（另單）。
           ⛔ 列者（明書之）：手冊先行之 K-9-51 之候選之序「距離 → 本街廓者先」之對調——距離取片至街廓之形（該街廓之片之
           聯集）之距離，本街廓者恆為 0 ⇒ 對調為等價之突變（行為⛔ 異）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, importlib.util, io, os, re, sys, warnings
import json, shutil, subprocess, tempfile                            # 🆕 `W-G.9-377`（mutate）
from concurrent.futures import ThreadPoolExecutor                    # 🆕 `W-G.9-377`（mutate）

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

TOL = 0.01
H, RDC, PK = "住宅區", "道路", "鄰里公園"


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


def _halt(fn, phrases):
    try:
        fn()
    except RuntimeError as e:
        return ("停機", all(p in str(e) for p in phrases))
    return ("無停機",)


# ── A：`k966_block_merge`（單一受併之街廓·純函式）──
def _cl(cls, s, tag):
    return {"cls": cls, "s": float(s), "tag": tag}


def _cap_try(cap, calls=None):
    """玩具：態 ＝ 已併入之量（float）；施 [(claim, v)] ⇒ 新態 ＝ 態 ＋ Σv；Σ ≤ cap ⇒ 過。"""
    def try_apply(st, pairs):
        tot = sum(float(v) for _c, v in pairs)
        if calls is not None:
            calls.append(round(tot, 6))
        new = st + tot
        return (new, "") if new <= cap + 1e-9 else (None, f"逾容量 {cap}")
    return try_apply


def _bm(ns, claims, cap, calls=None, st0=0.0):
    st, got, steps = ns["k966_block_merge"](st0, claims, _cap_try(cap, calls))
    return (round(st, 2), [round(g, 2) for g in got],
            [(x["步"], x["結果"], None if x["比例"] is None else round(x["比例"], 6)) for x in steps])


KL1 = [("建地", 60, "甲"), ("建地", 50, "乙"), ("建地", 40, "丙"), ("道路", 30, "甲"), ("道路", 20, "乙"), ("道路", 10, "丙")]


def _a9(ns):
    """態之承接：回傳之態 ＝ 末次通過之 try_apply 所回之物件（同一物件）；全不過 ⇒ 輸入之態（同一物件）。"""
    seen = []

    def try_apply(st, pairs):
        tot = sum(float(v) for _c, v in pairs)
        new = {"v": st["v"] + tot}
        if new["v"] <= 25.0 + 1e-9:
            seen.append(new)
            return new, ""
        return None, "逾"
    st0 = {"v": 0.0}
    st1, _g, _s = ns["k966_block_merge"](st0, [_cl("道路", 30, "a"), _cl("道路", 20, "b")], try_apply)
    st2, _g2, _s2 = ns["k966_block_merge"](st0, [_cl("道路", 30, "a")], lambda st, p: (None, "恆不過"))
    return (st1 is seen[-1], round(st1["v"], 2), st2 is st0)


# ── B：`k967_rank`／`k967_pre_area` ──
def _b1(ns):
    rk = ns["k967_rank"]
    c = [("B", 100.0, 80.0), ("A", 100.004, 90.0), ("C", 100.006, 10.0)]
    return [p for p, _g, _a in sorted(c, key=lambda e: rk(e[1], e[2], e[0]))]


def _b2(ns):
    rk = ns["k967_rank"]
    c = [("B(1)", 50.0, 70.0), ("A(1)", 50.0, 70.0), ("A(2)", 50.0, 69.996)]
    return [p for p, _g, _a in sorted(c, key=lambda e: rk(e[1], e[2], e[0]))]


def _b3(ns):
    pa = ns["k967_pre_area"]
    return (pa("u", ["a", "b"], {"a": 10.0, "b": 20.5}), pa("a", None, {"a": 10.0}),
            _halt(lambda: pa("u", ["a", "z"], {"a": 10.0}), ["z"]))


# ── C：入池閘之代表宗（`K-9-67`）──
def _rect(x0, x1, y0=0.0, y1=30.0):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]


def _c(ns, y1_pre, y1_add, y2_pre=100.0):
    """B：Y1（地號 L1）｜Y2（地號 L2）同歸戶相鄰；G ＝ (分攤 ＋ 面積) × 0.6；a ＜ 150 ⇒ 不配地；合併後 ⇒ 配地。回標的。"""
    fl = {"B": {"p1": (0.0, 0.0), "p2": (100.0, 0.0)}}

    def P(pid, x0, x1, pre, add, lot):
        return {"暫編地號": pid, "原地號": lot, "所屬街廓": "B", "分攤登記面積_m2": pre, "面積_m2": add,
                "重劃前地價區段": "z1", "polygon_coords": _rect(x0, x1)}

    def trial(b):
        rows, dl = [], []
        for t in b:
            a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
            if a < 150:
                dl.append({"暫編地號": t["暫編地號"], "G(㎡)": a * 0.6})
            else:
                rows.append({"暫編地號": t["暫編地號"], "推進側別": "left", "G(㎡)": a * 0.6, "驗_宗序": "其後"})
        return rows, ({("B", "left"): dl} if dl else {}), None
    b = [P("Y1", 0, 2, y1_pre, y1_add, "L1"), P("Y2", 2, 4, y2_pre, 0.0, "L2")]
    _bf, _o, log = ns["k929_6_fixpoint"](b, trial, {"L1": "G1", "L2": "G1"}, {"z1": 1000.0}, fl)
    return [e["標的"] for e in log]


# ── 共用之玩具 ──
def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


def _a(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _cbs(cap=None, drop=(), gmap=None):
    cap, gmap = cap or {}, gmap or {}

    def a_prime(src, dst):
        return _a(src)

    def alloc_state(temp, build):
        kept, bad, G, acc, mem = {}, {}, {}, {}, {}
        for b in build:
            acc[b["所屬街廓"]] = acc.get(b["所屬街廓"], 0.0) + max(0.0, float(b.get("面積_m2", 0) or 0))
        for b in build:
            p = b["暫編地號"]
            if p in drop:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(p)
            G[p] = gmap.get(p, _a(b))
            mem[p] = [p]
        for blk, v in acc.items():
            if v > cap.get(blk, 1e18) + 1e-9:
                bad[blk] = 1
        return {"kept": kept, "bad_pools": bad, "err": None, "G": G, "members": mem, "units": {}}
    return a_prime, alloc_state


def _keys(t2):
    out = {}
    for x in t2:
        d = {}
        for k in ("段三併出", "段三部分併出", "段三餘量"):
            if k in x:
                v = x[k]
                d[k] = (tuple(v) if isinstance(v, list) else
                        tuple(sorted((a, round(float(b), 2)) for a, b in v.items())) if isinstance(v, dict)
                        else round(float(v), 2))
        if d:
            out[x["暫編地號"]] = d
    return out


def _acc(t2):
    return {x["暫編地號"]: round(float(x.get("面積_m2", 0) or 0), 2) for x in t2 if float(x.get("面積_m2", 0) or 0)}


def _q(r):
    return tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items()))


# ── T：手冊先行 ──
def _t1(ns, with_a2=True):
    """BA（分不到之建地 X 甲 60／Y 乙 50／Z 丙 40）跨分配線各鄰其地主於 BB 之已配得之宗 A1／B1／C1；BB 之容量 130；
    （with_a2）甲另有 BD 之 A2（距 X 30）。"""
    t = [_tp("X(1)", "BA", H, _R(0, 10, 0, 30), 60), _tp("Y(1)", "BA", H, _R(10, 20, 0, 30), 50),
         _tp("Z(1)", "BA", H, _R(20, 30, 0, 30), 40),
         _tp("A1(1)", "BB", H, _R(0, 10, 30, 60), 300), _tp("B1(1)", "BB", H, _R(10, 20, 30, 60), 300),
         _tp("C1(1)", "BB", H, _R(20, 30, 30, 60), 300)]
    if with_a2:
        t.append(_tp("A2(1)", "BD", H, _R(40, 50, 0, 30), 300))
    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "Z": "丙", "C1": "丙"}
    blocks = {b: {"category": H} for b in ("BA", "BB", "BD")}
    ap, st = _cbs({"BB": 130.0}, drop=("X(1)", "Y(1)", "Z(1)"))
    return ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, st, log_print=lambda *x: None)


def _t2(ns):
    """呈文（`K-9-68`）之例：BB 剩下能容 100；甲之建地 X 80 依手冊併入 BB 之 A1；乙之建地 Y 60 依手冊先試 BC 之 C1（不容）
    ⇒ 第 2 輪依距離轉 BB 之 B1，唯分 BB 當時剩下之 20（甲之 80 ⛔ 重分）。"""
    t = [_tp("X(1)", "BA", H, _R(0, 10, 0, 30), 80), _tp("Y(1)", "BA", H, _R(10, 20, 0, 30), 60),
         _tp("A1(1)", "BB", H, _R(0, 10, 30, 60), 300), _tp("O1(1)", "BB", H, _R(10, 20, 30, 60), 300),
         _tp("B1(1)", "BB", H, _R(20, 30, 30, 60), 300), _tp("C1(1)", "BC", H, _R(20, 30, 0, 30), 300)]
    own = {"X": "甲", "A1": "甲", "Y": "乙", "B1": "乙", "C1": "乙", "O1": "丁"}
    blocks = {b: {"category": H} for b in ("BA", "BB", "BC")}
    ap, st = _cbs({"BB": 100.0, "BC": 0.0}, drop=("X(1)", "Y(1)"))
    return ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, st, log_print=lambda *x: None)


def _t3(ns):
    """第 2 輪（`K-9-51`）二位地主之剩下同到一街廓 ⇒ 亦依 `K-9-66` 按比例：BA 之 X 甲 60／Y 乙 40 依手冊併入 BB（容 50）之
    A1／B1 ⇒ 第 1 輪按比例 30／20；剩下 30／20 依距離同轉 BD（容 25）之 A2／B2 ⇒ 第 2 輪按比例 15／10；餘入合併單位。"""
    t = [_tp("X(1)", "BA", H, _R(0, 10, 0, 30), 60), _tp("Y(1)", "BA", H, _R(10, 20, 0, 30), 40),
         _tp("A1(1)", "BB", H, _R(0, 10, 30, 60), 300), _tp("B1(1)", "BB", H, _R(10, 20, 30, 60), 300),
         _tp("A2(1)", "BD", H, _R(40, 50, 0, 30), 300), _tp("B2(1)", "BD", H, _R(50, 60, 0, 30), 300)]
    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "B2": "乙"}
    blocks = {b: {"category": H} for b in ("BA", "BB", "BD")}
    ap, st = _cbs({"BB": 50.0, "BD": 25.0}, drop=("X(1)", "Y(1)"))
    return ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, st, log_print=lambda *x: None)


def _t5(ns):
    """🆕 `W-G.9-377`：`T1` 之形而 BB 之地價為 BA 之半（併入 BB 者 a′ ＝ 2a·κ ＝ 2）：第 1 輪之要求之來源量 ＝ 計畫之量 ÷ κ
    （X 60／Y 50／Z 40）；BB 之容量 130 ⇒ 2 × Σv ≤ 130 ⇒ 比例 130 ÷ 300 ＝ 0.433333：X 26（A1 得 52）、Y 21.67（B1 得 43.33）、
    Z 17.33（C1 得 34.67）；甲之剩下 34 依距離全入 BD 之 A2（κ ＝ 1）；乙丙之剩下入合併單位。"""
    t = [_tp("X(1)", "BA", H, _R(0, 10, 0, 30), 60), _tp("Y(1)", "BA", H, _R(10, 20, 0, 30), 50),
         _tp("Z(1)", "BA", H, _R(20, 30, 0, 30), 40),
         _tp("A1(1)", "BB", H, _R(0, 10, 30, 60), 300), _tp("B1(1)", "BB", H, _R(10, 20, 30, 60), 300),
         _tp("C1(1)", "BB", H, _R(20, 30, 30, 60), 300), _tp("A2(1)", "BD", H, _R(40, 50, 0, 30), 300)]
    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "Z": "丙", "C1": "丙"}
    blocks = {b: {"category": H} for b in ("BA", "BB", "BD")}
    _ap, st = _cbs({"BB": 130.0}, drop=("X(1)", "Y(1)", "Z(1)"))

    def ap(src, dst):
        return _a(src) * (2.0 if dst.get("所屬街廓") == "BB" else 1.0)
    return ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, st, log_print=lambda *x: None)


def _rows953(res):
    return [(r.get("序"), r.get("片"), r.get("受併宗") if isinstance(r.get("受併宗"), str) else tuple(r.get("受併宗")),
             _q(r), r.get("結果")) for r in res[2] if r.get("序") in ("K-9-66", "手冊", "K-9-51")]


# ── U：段三後處理 ──
def _u(ns, cap, b5=False):
    """B3（x∈[0,40]）：A2／A1（地主 gA）｜C1／C2（地主 gC）；左端 A2 以 A1、右端 C2 以 C1 於 ① 成；公園 PK 之 PA（gA·60·
    鄰 A1／A2）、PC（gC·40·鄰 C1／C2）⇒ 後處理 (c) 各併入其受併宗（同在 B3）；（b5）gA／gC 另有遠處 B5 之 A9／C9。"""
    t = [_tp("A2(1)", "B3", H, _R(0, 10, 0, 30), 100), _tp("A1(1)", "B3", H, _R(10, 20, 0, 30), 100),
         _tp("C1(1)", "B3", H, _R(20, 30, 0, 30), 100), _tp("C2(1)", "B3", H, _R(30, 40, 0, 30), 100),
         _tp("PA(1)", "PK", PK, _R(0, 20, 30, 50), 60), _tp("PC(1)", "PK", PK, _R(20, 40, 30, 50), 40)]
    if b5:
        t += [_tp("A9(1)", "B5", H, _R(100, 110, 0, 30), 100), _tp("C9(1)", "B5", H, _R(110, 120, 0, 30), 100)]
    own = {"A1": "gA", "A2": "gA", "PA": "gA", "A9": "gA", "C1": "gC", "C2": "gC", "PC": "gC", "C9": "gC"}
    blocks = {"B3": {"category": H}, "PK": {"category": PK}, "B5": {"category": H}}
    build = [x for x in t if x["街廓分類"] == H]
    ap, st = _cbs(cap)

    def tw(temp, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        g = _a(by[cand]) if cand in by else 0.0
        return (cand if g >= 150.0 else None), round(g, 2), 150.0
    order = [{"最終序位": 1, "街廓": "B3", "端": "左", "暫編地號": "A2(1)"},
             {"最終序位": 2, "街廓": "B3", "端": "右", "暫編地號": "C2(1)"}]
    t2, b2, log = ns["k6b_stage3_run"](order, set(), own, t, build, blocks, {}, ap, tw, st, log_print=lambda *x: None)
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]), _q(x))
            for x in log if x.get("序") == "後處理"]
    return post, _keys(t2), _acc(t2)


# ── V：第一趟 ──
def _v(ns, cap, lists, ax=60.0, ay=40.0):
    """BA：X1(1)（g1·建地）／Y1(1)（g2·建地）；BB：X1(2)（g1）／Y2(1)（g2）；BC：Y3(1)（g2）。受詞 g1（名單 lists[0]）、
    g2（名單 lists[1]）·依序。"""
    t = [_tp("X1(1)", "BA", H, _R(0, 10, 0, 30), ax), _tp("Y1(1)", "BA", H, _R(10, 20, 0, 30), ay),
         _tp("X1(2)", "BB", H, _R(0, 10, 30, 60), 300), _tp("Y2(1)", "BB", H, _R(10, 20, 30, 60), 300),
         _tp("Y3(1)", "BC", H, _R(20, 30, 0, 30), 300)]
    own = {"X1": "g1", "Y1": "g2", "Y2": "g2", "Y3": "g2"}
    geom = {x["暫編地號"]: [list(c) for c in x["polygon_coords"]] for x in t}
    ap, st = _cbs(cap, drop=("X1(1)", "Y1(1)"))
    subj = [{"歸戶": "g1", "軌": "建地軌", "錨點": "X1(1)", "名單": list(lists[0]), "片": ["X1(1)"], "原有面積合計": ax},
            {"歸戶": "g2", "軌": "建地軌", "錨點": "Y1(1)", "名單": list(lists[1]), "片": ["Y1(1)"], "原有面積合計": ay}]
    t2, b2, log = ns["adj4_pass1_run"](t, list(t), own, subj, geom, ap, st, log_print=lambda *x: None)
    rows = []
    for r in log:
        if r.get("序") == "剩下":
            rows.append(("剩下", r.get("歸戶"), r.get("片"),
                         tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("餘量") or {}).items()))))
        else:
            rv = r.get("受併宗")
            rows.append((r.get("序"), r.get("歸戶"), r.get("街廓"), r.get("片"),
                         rv if isinstance(rv, str) else tuple(rv), _q(r), r.get("結果")))
    return rows, _keys(t2), _acc(t2), [b["暫編地號"] for b in b2]


# ── W：建地之部分併出之下游 ──
def _w_world(alloc_y):
    """BA：Y(1)（乙·分攤 50·已部分併出 20 於 BB 之 B1·面積_m2 −20·留 build）、O(1)（丁）；BB：B1(1)（乙·+20）。"""
    y = _tp("Y(1)", "BA", H, _R(10, 20, 0, 30), 50)
    y.update({"面積_m2": -20.0, "段三併出": ["B1(1)"], "段三部分併出": {"B1(1)": 20.0}})
    o = _tp("O(1)", "BA", H, _R(0, 10, 0, 30), 300)
    b1 = _tp("B1(1)", "BB", H, _R(10, 20, 30, 60), 300)
    b1["面積_m2"] = 20.0
    temp = [y, o, b1]
    own = {"Y": "乙", "B1": "乙", "O": "丁"}
    g_rows = [{"暫編地號": "O(1)", "推進側別": "left"}, {"暫編地號": "B1(1)", "推進側別": "left"}]
    dropped = {}
    if alloc_y:
        g_rows.append({"暫編地號": "Y(1)", "推進側別": "left"})
    else:
        dropped = {("BA", "left"): [{"暫編地號": "Y(1)", "G(㎡)": 25.0, "不配地由": "玩具"}]}
    return temp, [y, o, b1], g_rows, dropped, own


def _w(ns, alloc_y):
    temp, build, g_rows, dropped, own = _w_world(alloc_y)
    burden = {"BA": ns["F3_CATEGORY_BURDEN"][H], "BB": ns["F3_CATEGORY_BURDEN"][H]}
    r = ns["adj_intake"](temp, build, g_rows, dropped, own, burden)
    y = next(x for x in r["slices"] if x["暫編地號"] == "Y(1)")
    yrow = (y["類"], round(float(y["原有面積"]), 2), round(float(y.get("段三併出面積") or 0), 2), y.get("應分配面積"),
            sorted(y.get("配地街廓") or []))
    units = [(u["歸戶"], u["軌"], u["原街廓"], round(float(u["原有面積合計"]), 2)) for u in r["units"]]
    tot = {k: round(v[1], 2) for k, v in sorted(r["totals"].items()) if v[1]}
    cons = abs(sum(v[1] for v in r["totals"].values()) - float(r["all_area"])) <= 1e-6
    return yrow, units, tot, cons


def _w3(sp):
    temp, _b, _g, _d, _o = _w_world(False)
    gone = _tp("G(1)", "BA", H, _R(20, 30, 0, 30), 70)
    gone["段三併出"] = ["B1(1)"]          # 全數併出之建地（已去 build）
    temp = temp + [gone]
    pool = sp.k6b_stage3_pool_temp(temp)
    by0 = {t["暫編地號"]: t for t in temp}
    return [(t["暫編地號"], t is by0[t["暫編地號"]]) for t in pool], pool is not temp


def _cases(ns, sp):
    out = []
    # ── A ──
    _run(out, "A1 KL 例一（街廓 B 能再容 130）：建地全部一次不過 ⇒ 按比例 52／43.33／34.67（130 × 60／150 等）；道路未試",
         lambda: _bm(ns, [_cl(c, s, g) for c, s, g in KL1], 130.0),
         (130.0, [52.0, 43.33, 34.67, 0.0, 0.0, 0.0],
          [("整體", "未成", None), ("建地", "部分成", 0.866667), ("道路", "未試", None)]))
    _run(out, "A2 KL 例二（能再容 170）：建地 150 全入；剩 20 按 30：20：10 分給道路 10／6.67／3.33",
         lambda: _bm(ns, [_cl(c, s, g) for c, s, g in KL1], 170.0),
         (170.0, [60.0, 50.0, 40.0, 10.0, 6.67, 3.33],
          [("整體", "未成", None), ("建地", "成", 1.0), ("道路", "部分成", 0.333333)]))
    _run(out, "A3 一次全部即過 ⇒ 全入、唯整體一步",
         lambda: _bm(ns, [_cl(c, s, g) for c, s, g in KL1], 300.0),
         (210.0, [60.0, 50.0, 40.0, 30.0, 20.0, 10.0], [("整體", "成", 1.0)]))
    calls4 = []
    _run(out, "A4 唯一類（道路 30／20·容 25）⇒ 整體即該類之全部（⛔ 重試全部）⇒ 按比例 15／10；全量之試恰一次",
         lambda: (_bm(ns, [_cl("道路", 30, "a"), _cl("道路", 20, "b")], 25.0, calls4), calls4.count(50.0)),
         ((25.0, [15.0, 10.0], [("整體", "未成", None), ("道路", "部分成", 0.5)]), 1))
    _run(out, "A5 格 ＝ 該類之合計每 0.01 ㎡：容 60.005 ⇒ 60.00；容 59.999 ⇒ 59.99",
         lambda: (_bm(ns, [_cl("公設地", 100, "a")], 60.005)[1], _bm(ns, [_cl("公設地", 100, "a")], 59.999)[1]),
         ([60.0], [59.99]))
    _run(out, "A6 建地、道路皆全入；公設地 200 唯容 10 ⇒ 0.05",
         lambda: _bm(ns, [_cl("公設地", 200, "c"), _cl("道路", 50, "b"), _cl("建地", 100, "a")], 160.0),
         (160.0, [10.0, 50.0, 100.0],
          [("整體", "未成", None), ("建地", "成", 1.0), ("道路", "成", 1.0), ("公設地", "部分成", 0.05)]))
    _run(out, "A7 建地之比例步亦全不容 ⇒ 未成（比例 0）、其後之類未試、⛔ 併入",
         lambda: _bm(ns, [_cl("建地", 10, "a"), _cl("建地", 20, "b"), _cl("道路", 5, "c")], 0.0),
         (0.0, [0.0, 0.0, 0.0], [("整體", "未成", None), ("建地", "未成", 0.0), ("道路", "未試", None)]))
    _run(out, "A8 類非三類之一 ⇒ 停機；來源量 ≤ 0 ⇒ 停機",
         lambda: (_halt(lambda: _bm(ns, [_cl("農地", 10, "a")], 5.0), ["K-9-66"]),
                  _halt(lambda: _bm(ns, [_cl("建地", 0, "a")], 5.0), ["K-9-66"])),
         (("停機", True), ("停機", True)))
    _run(out, "A9 回傳之態 ＝ 末次通過之試所回之物件；全不過 ⇒ 輸入之態（同一物件）",
         lambda: _a9(ns), (True, 25.0, True))
    # ── B ──
    _run(out, "B1 k967_rank：應分配面積以 0.01 ㎡ 比（100.004 ＝ 100.00·100.006 ＝ 100.01）；同 ⇒ 重劃前面積大者先",
         lambda: _b1(ns), ["C", "A", "B"])
    _run(out, "B2 k967_rank：再同（重劃前面積 69.996 ＝ 70.00）⇒ 暫編地號小者先",
         lambda: _b2(ns), ["A(1)", "A(2)", "B(1)"])
    _run(out, "B3 k967_pre_area：成員之分攤登記面積之和；成員缺 ⇒ 自身；取不到 ⇒ 停機",
         lambda: _b3(ns), (30.5, 10.0, ("停機", True)))
    # ── C ──
    _run(out, "C1 入池閘之代表宗：G 並列（60.00）⇒ 重劃前面積大者 Y2（100 ＞ 80）",
         lambda: _c(ns, 80.0, 20.0), ["Y2"])
    _run(out, "C2 G 差 0.004（0.01 ㎡ 為同）⇒ 並列 ⇒ 重劃前面積大者 Y2",
         lambda: _c(ns, 80.0, 20.0067), ["Y2"])
    _run(out, "C3 G 差 0.006（60.01 ＞ 60.00）⇒ G 大者 Y1",
         lambda: _c(ns, 80.0, 20.01), ["Y1"])
    _run(out, "C4 G 與重劃前面積皆同 ⇒ 暫編地號小者 Y1",
         lambda: _c(ns, 100.0, 0.0), ["Y1"])
    # ── T ──
    _run(out, "T1 手冊先行·三位地主之建地同到 BB（容 130）⇒ K-9-66 之列、按比例 52／43.33／34.67；甲之剩下 8 依距離併入 "
              "A2；乙丙之剩下入合併單位；部分併出者留 build（面積_m2 減其量·段三部分併出·⛔ 段三餘量）",
         lambda: (lambda r: (_rows953(r), _keys(r[0]), _acc(r[0]), [b["暫編地號"] for b in r[1]]))(_t1(ns)),
         ([("K-9-66", "3 片", "—", (), "整體未成；建地部分成（0.866667）"),
           ("手冊", "X(1)", "A1(1)", (("A1(1)", 52.0),), "部分成"),
           ("手冊", "Y(1)", "B1(1)", (("B1(1)", 43.33),), "部分成"),
           ("手冊", "Z(1)", "C1(1)", (("C1(1)", 34.67),), "部分成"),
           ("K-9-51", "X(1)", "A2(1)", (("A2(1)", 8.0),), "成"),
           ("K-9-51", "Y(1)", "—", (), "入合併單位"),
           ("K-9-51", "Z(1)", "—", (), "入合併單位")],
          {"X(1)": {"段三併出": ("A1(1)", "A2(1)")},
           "Y(1)": {"段三併出": ("B1(1)",), "段三部分併出": (("B1(1)", 43.33),)},
           "Z(1)": {"段三併出": ("C1(1)",), "段三部分併出": (("C1(1)", 34.67),)}},
          {"A1(1)": 52.0, "A2(1)": 8.0, "B1(1)": 43.33, "C1(1)": 34.67, "Y(1)": -43.33, "Z(1)": -34.67},
          ["Y(1)", "Z(1)", "A1(1)", "B1(1)", "C1(1)", "A2(1)"]))
    _run(out, "T2 手冊先行·K-9-68：甲之 80 第 1 輪全入 BB；乙之 60 第 1 輪試 BC 不過、第 2 輪轉 BB 唯得剩下之 20（⛔ 重分）",
         lambda: (lambda r: (_rows953(r), _acc(r[0])))(_t2(ns)),
         ([("手冊", "X(1)", "A1(1)", (("A1(1)", 80.0),), "成"),
           ("手冊", "Y(1)", "C1(1)", (), "未成"),
           ("K-9-51", "Y(1)", "B1(1)", (("B1(1)", 20.0),), "部分成"),
           ("K-9-51", "Y(1)", "—", (), "入合併單位")],
          {"A1(1)": 80.0, "B1(1)": 20.0, "Y(1)": -20.0}))
    _run(out, "T3 手冊先行·第 2 輪（K-9-51）二位地主之剩下同到 BD（容 25）⇒ 亦依 K-9-66 按比例 15／10；餘入合併單位",
         lambda: (lambda r: (_rows953(r), _keys(r[0]), _acc(r[0])))(_t3(ns)),
         ([("K-9-66", "2 片", "—", (), "整體未成；建地部分成（0.500000）"),
           ("手冊", "X(1)", "A1(1)", (("A1(1)", 30.0),), "部分成"),
           ("手冊", "Y(1)", "B1(1)", (("B1(1)", 20.0),), "部分成"),
           ("K-9-66", "2 片", "—", (), "整體未成；建地部分成（0.500000）"),
           ("K-9-51", "X(1)", "A2(1)", (("A2(1)", 15.0),), "部分成"),
           ("K-9-51", "Y(1)", "B2(1)", (("B2(1)", 10.0),), "部分成"),
           ("K-9-51", "X(1)", "—", (), "入合併單位"),
           ("K-9-51", "Y(1)", "—", (), "入合併單位")],
          {"X(1)": {"段三併出": ("A1(1)", "A2(1)"), "段三部分併出": (("A1(1)", 30.0), ("A2(1)", 15.0))},
           "Y(1)": {"段三併出": ("B1(1)", "B2(1)"), "段三部分併出": (("B1(1)", 20.0), ("B2(1)", 10.0))}},
          {"A1(1)": 30.0, "A2(1)": 15.0, "B1(1)": 20.0, "B2(1)": 10.0, "X(1)": -45.0, "Y(1)": -30.0}))
    # 🆕 `W-G.9-377`
    _run(out, "T5 手冊先行·第 1 輪之來源量 ＝ 計畫之量 ÷ κ（BB 之 κ ＝ 2）⇒ 比例 0.433333：A1 52／B1 43.33／C1 34.67；"
              "甲之剩下 34 全入 A2；帳以來源量計（Y 21.67／Z 17.33）",
         lambda: (lambda r: (_rows953(r), _keys(r[0]), _acc(r[0])))(_t5(ns)),
         ([("K-9-66", "3 片", "—", (), "整體未成；建地部分成（0.433333）"),
           ("手冊", "X(1)", "A1(1)", (("A1(1)", 52.0),), "部分成"),
           ("手冊", "Y(1)", "B1(1)", (("B1(1)", 43.33),), "部分成"),
           ("手冊", "Z(1)", "C1(1)", (("C1(1)", 34.67),), "部分成"),
           ("K-9-51", "X(1)", "A2(1)", (("A2(1)", 34.0),), "成"),
           ("K-9-51", "Y(1)", "—", (), "入合併單位"),
           ("K-9-51", "Z(1)", "—", (), "入合併單位")],
          {"X(1)": {"段三併出": ("A1(1)", "A2(1)")},
           "Y(1)": {"段三併出": ("B1(1)",), "段三部分併出": (("B1(1)", 21.67),)},
           "Z(1)": {"段三併出": ("C1(1)",), "段三部分併出": (("C1(1)", 17.33),)}},
          {"A1(1)": 52.0, "A2(1)": 34.0, "B1(1)": 43.33, "C1(1)": 34.67, "Y(1)": -21.67, "Z(1)": -17.33}))
    # ── U ──
    _run(out, "U0 段三後處理·對照：整批即過 ⇒ 二列皆成（⛔ K-9-66 之列）",
         lambda: _u(ns, {"B3": 1000.0})[0],
         [("PA(1)", "後處理(c)", "成", "A2(1)", (("A2(1)", 60.0),)),
          ("PC(1)", "後處理(c)", "成", "C2(1)", (("C2(1)", 40.0),))])
    _run(out, "U1 段三後處理·二位地主之公設地同到 B3（剩下能容 50）⇒ K-9-66 之列、按比例 30／20；剩下轉調配",
         lambda: _u(ns, {"B3": 250.0}),
         ([("2 片", "K-9-66", "整體未成；公設地部分成（0.500000）", "—", ()),
           ("PA(1)", "後處理(c)", "部分成", "A2(1)", (("A2(1)", 30.0),)),
           ("PC(1)", "後處理(c)", "部分成", "C2(1)", (("C2(1)", 20.0),)),
           ("PA(1)", "後處理·第5項", "轉調配", "—", ()), ("PC(1)", "後處理·第5項", "轉調配", "—", ())],
          {"A1(1)": {"段三併出": ("A2(1)",)}, "C1(1)": {"段三併出": ("C2(1)",)},
           "PA(1)": {"段三併出": ("A2(1)",), "段三部分併出": (("A2(1)", 30.0),), "段三餘量": 30.0},
           "PC(1)": {"段三併出": ("C2(1)",), "段三部分併出": (("C2(1)", 20.0),), "段三餘量": 20.0}},
          {"A2(1)": 130.0, "C2(1)": 120.0}))
    _run(out, "U2 段三後處理·第 2 輪二位地主之剩下同到 B5（容 25）⇒ 亦依 K-9-66 按比例 15／10",
         lambda: _u(ns, {"B3": 250.0, "B5": 25.0}, b5=True)[0],
         [("2 片", "K-9-66", "整體未成；公設地部分成（0.500000）", "—", ()),
          ("PA(1)", "後處理(c)", "部分成", "A2(1)", (("A2(1)", 30.0),)),
          ("PC(1)", "後處理(c)", "部分成", "C2(1)", (("C2(1)", 20.0),)),
          ("2 片", "K-9-66", "整體未成；公設地部分成（0.500000）", "—", ()),
          ("PA(1)", "後處理·第5項", "部分成", "A9(1)", (("A9(1)", 15.0),)),
          ("PC(1)", "後處理·第5項", "部分成", "C9(1)", (("C9(1)", 10.0),)),
          ("PA(1)", "後處理·第5項", "轉調配", "—", ()), ("PC(1)", "後處理·第5項", "轉調配", "—", ())])
    # ── V ──
    _run(out, "V1 第一趟·二受詞之建地同到 BB（容 50）⇒ K-9-66 之列、按比例 30／20；剩下留於合併單位；部分併出者留 build",
         lambda: _v(ns, {"BB": 50.0}, (["BB"], ["BB"])),
         ([("K-9-66", "—", "BB", "2 片", ("X1(2)", "Y2(1)"), (), "整體未成；建地部分成（0.500000）"),
           ("整體", "g1", "BB", "1 片", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "X1(2)", (("X1(2)", 30.0),), "部分成"),
           ("整體", "g2", "BB", "1 片", "Y2(1)", (), "未成"),
           ("逐片", "g2", "BB", "Y1(1)", "Y2(1)", (("Y2(1)", 20.0),), "部分成"),
           ("剩下", "g1", "X1(1)", (("X1(1)", 30.0),)), ("剩下", "g2", "Y1(1)", (("Y1(1)", 20.0),))],
          {"X1(1)": {"段三併出": ("X1(2)",), "段三部分併出": (("X1(2)", 30.0),)},
           "Y1(1)": {"段三併出": ("Y2(1)",), "段三部分併出": (("Y2(1)", 20.0),)}},
          {"X1(1)": -30.0, "X1(2)": 30.0, "Y1(1)": -20.0, "Y2(1)": 20.0},
          ["X1(1)", "Y1(1)", "X1(2)", "Y2(1)", "Y3(1)"]))
    _run(out, "V2 第一趟·K-9-68：g1 之 80 第 1 輪全入 BB；g2 之 60 第 1 輪於 BC 不過、第 2 輪至 BB 唯得剩下之 20（⛔ 重分）",
         lambda: _v(ns, {"BB": 100.0, "BC": 0.0}, (["BB"], ["BC", "BB"]), 80.0, 60.0)[:3],
         ([("整體", "g1", "BB", "1 片", "X1(2)", (("X1(2)", 80.0),), "成"),
           ("整體", "g2", "BC", "1 片", "Y3(1)", (), "未成"),
           ("逐片", "g2", "BC", "Y1(1)", "Y3(1)", (), "未成"),
           ("整體", "g2", "BB", "1 片", "Y2(1)", (), "未成"),
           ("逐片", "g2", "BB", "Y1(1)", "Y2(1)", (("Y2(1)", 20.0),), "部分成"),
           ("剩下", "g2", "Y1(1)", (("Y1(1)", 40.0),))],
          {"X1(1)": {"段三併出": ("X1(2)",)}, "Y1(1)": {"段三併出": ("Y2(1)",), "段三部分併出": (("Y2(1)", 20.0),)}},
          {"X1(2)": 80.0, "Y1(1)": -20.0, "Y2(1)": 20.0}))
    # ── W ──
    _run(out, "W1 調配之輸入·部分併出之建地（其單元不配地）⇒ 建築街廓內不能分配：原有面積 ＝ 50 × 30／50 ＝ 30、"
              "已併出 20 計入原位次配地、應分配面積 ＝ 該趟之 G（原位·剩下之面積）；守恆",
         lambda: _w(ns, False),
         (("建築街廓內不能分配", 30.0, 20.0, 25.0, []), [("乙", "建地軌", "BA", 30.0)],
          {"原位次配地": 620.0, "建築街廓內不能分配": 30.0}, True))
    _run(out, "W2 調配之輸入·部分併出之建地（其單元配地）⇒ 原位次配地（配地街廓含受併宗之街廓）；守恆",
         lambda: _w(ns, True),
         (("原位次配地", 30.0, 20.0, None, ["BA", "BB"]), [], {"原位次配地": 650.0}, True))
    _run(out, "W3 公設地調配之 temp：部分併出之建地（⛔ 段三餘量）原物件入之；全數併出之建地去之；餘同一物件",
         lambda: _w3(sp), ([("Y(1)", True), ("O(1)", True), ("B1(1)", True)], True))
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


NEED = ("K966_CLASSES", "K966_GRID", "k966_block_merge", "k967_rank", "k967_pre_area", "k929_6_fixpoint",
        "k953_manual_run", "k6b_stage3_run", "adj4_pass1_run", "adj_intake", "F3_CATEGORY_BURDEN")


def selftest(repo):
    ns, _ = _harvest(repo)
    import selection_pipeline as sp
    need = [n for n in NEED if n not in ns] + ([] if hasattr(sp, "k6b_stage3_pool_temp") else ["k6b_stage3_pool_temp"])
    if need:
        print(f"  🔴 受詞缺：{need}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    cases = _cases(ns, sp)
    print("── K-9-66／K-9-67／K-9-68 之各支 ──")
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


# ── wiring ──
CASE_LIT_RE = re.compile(r"^(R\d+|RD\d+|G\d+|G0\d\d|\d{3}(-\d+)?(\(\d+\))?|left|right|左|右|住宅區|商業區)$")
SIGS = {"k966_block_merge": (["state", "claims", "try_apply"], ["grid"]), "k967_rank": (["g", "pre_area", "pid"], []),
        "k967_pre_area": (["pid", "members", "area_of"], [])}
PLACES = ("k953_manual_run", "k6b_stage3_run", "adj4_pass1_run")
# 🔧 `W-G.9-375`（`K-9-65`·`K-9-64`）：排配地時之第 2 步（依手冊併入他街廓·`K-9-66`）亦以之 ⇒ Y2 之處增入池閘
PLACES += ("k929_6_fixpoint",)
GONE = ("_max357", "_k951", "_split357", "_fill953", "_remain953", "_vmax_a4")


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


def _calls(node, name):
    return [n for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == name]


def _wiring_checks(app):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        tree = ast.parse(app)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            try:
                consts[n.targets[0].id] = ast.literal_eval(n.value)
            except Exception:  # noqa: BLE001
                consts[n.targets[0].id] = None
    chk = []
    sig_bad = []
    for nm, (pos, kwo) in SIGS.items():
        f = top.get(nm)
        if f is None:
            sig_bad.append((nm, "缺"))
            continue
        if [a.arg for a in f.args.args] != pos or [a.arg for a in f.args.kwonlyargs] != kwo:
            sig_bad.append((nm, [a.arg for a in f.args.args], [a.arg for a in f.args.kwonlyargs]))
    c_ok = consts.get("K966_CLASSES") == ("建地", "道路", "公設地") and consts.get("K966_GRID") == 0.01
    chk.append(("Y1 模組層之新名與簽名", not sig_bad and c_ok,
                f"簽名之異 {sig_bad}；K966_CLASSES {consts.get('K966_CLASSES')!r}；K966_GRID {consts.get('K966_GRID')!r}"))
    per = {nm: len(_calls(top[nm], "k966_block_merge")) if nm in top else None for nm in PLACES}
    tot = len(_calls(tree, "k966_block_merge"))
    chk.append(("Y2 k966_block_merge 之呼叫恰在四處各一（三處 ＋ 入池閘·W-G.9-375）",
                all(v == 1 for v in per.values()) and tot == len(PLACES), f"四處 {per}；全檔 {tot}"))
    rk = {nm: len(_calls(top[nm], "k967_rank")) if nm in top else None
          for nm in ("k929_6_fixpoint", "k953_manual_run", "k6b_stage3_run", "adj4_pass1_run")}
    rk_ok = (rk["k929_6_fixpoint"] or 0) >= 1 and (rk["k953_manual_run"] or 0) >= 3 and \
        (rk["k6b_stage3_run"] or 0) >= 1 and (rk["adj4_pass1_run"] or 0) >= 1
    chk.append(("Y3 k967_rank 之呼叫（入池閘 ≥ 1·手冊先行 ≥ 3·段三 ≥ 1·第一趟 ≥ 1）", rk_ok, f"{rk}"))
    lits = []
    for nm in ("k966_block_merge", "k967_rank", "k967_pre_area"):
        for x in ast.walk(top.get(nm) or ast.Module(body=[], type_ignores=[])):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
                lits.append((nm, x.value))
    chk.append(("Y4 新碼⛔ 案件字面", not lits, f"{lits}"))
    gone = sorted({n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name in GONE})
    chk.append(("Y5 已去之巢狀 def ⛔ 見", not gone, f"{gone}"))
    old = []
    for nm in ("k953_manual_run", "k929_6_fixpoint"):
        for x in ast.walk(top.get(nm) or ast.Module(body=[], type_ignores=[])):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and "應分配面積並列" in x.value:
                old.append(nm)
    chk.append(("Y6 擇宗⛔ 以「並列 ⇒ 停機」", not old, f"{old}"))
    # 🆕 `W-G.9-377`（`F17` 之 W2 之代·所施者 ＝ 末次通過之試所回之態）：三處之 k966_block_merge 之呼叫皆為
    #   `state, … = k966_block_merge(state, …)`（以其前態為輸入、以其回傳之態承接）
    thr = {}
    for nm in PLACES[:3]:
        f = top.get(nm)
        asg = [a for a in ast.walk(f) if isinstance(a, ast.Assign) and isinstance(a.value, ast.Call)
               and isinstance(a.value.func, ast.Name) and a.value.func.id == "k966_block_merge"] if f else []
        thr[nm] = [len(a.targets) == 1 and isinstance(a.targets[0], ast.Tuple) and len(a.targets[0].elts) == 3
                   and isinstance(a.targets[0].elts[0], ast.Name) and a.targets[0].elts[0].id == "state"
                   and bool(a.value.args) and isinstance(a.value.args[0], ast.Name) and a.value.args[0].id == "state"
                   for a in asg]
    chk.append(("Y7 三處之 k966_block_merge 皆以 state 為前態、以其回傳之態承接（state, … ＝ …(state, …)）",
                all(v == [True] for v in thr.values()), f"{thr}"))
    return chk


def wiring(repo):
    chk = _wiring_checks(_read(repo, "app.py"))
    red = []
    for name, ok, note in chk:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── 🆕 `W-G.9-377` mutate：以受測碼之字樣為錨之突變（`F17` 之 W2／W3／W12 與 `F25` 之 M01〜M19／M28／M29／M31 之代）──
#   各為 (號, 條, 述, 函式, 錨, 換, 所指之項)；錨須於該函式之區間恰一見；所指之項 ＝ 「器:項」（F27 本器、F28、F23、F24、F16
#   之 selftest 之項），施突變後其皆須紅。受測碼之該段改寫者，其錨隨之更新（另單）。
_BM, _RK, _PA = "k966_block_merge", "k967_rank", "k967_pre_area"
_S3, _MN, _A4, _AI = "k6b_stage3_run", "k953_manual_run", "adj4_pass1_run", "adj_intake"
MUT377 = [
    ("N01", "K-9-66 ①", "整體成而⛔ 回", _BM,
     "    if _new966 is not None:\n        return _new966, list(_s966)",
     "    if False:\n        return _new966, list(_s966)",
     {"F27:A3"}),
    ("N02", "K-9-66 ②", "唯一類者亦以該類之全量再試", _BM, "        if len(_have966) > 1:\n", "        if len(_have966) >= 1:\n",
     {"F27:A4"}),
    ("N03", "K-9-66 ②", "類之序反之", _BM, "    for _j966, _k966 in enumerate(_have966):",
     "    for _j966, _k966 in enumerate(_have966[::-1]):", {"F27:A2", "F27:A6"}),
    ("N04", "K-9-66 通知 2", "格改 0.1", _BM, "def k966_block_merge(state, claims, try_apply, *, grid=K966_GRID):",
     "def k966_block_merge(state, claims, try_apply, *, grid=K966_GRID * 10):", {"F27:A5"}),
    ("N05", "K-9-66 ②", "按比例之後仍試次類", _BM,
     "'由': f'{_k966}未全入（K-9-66）'})\n        break\n", "'由': f'{_k966}未全入（K-9-66）'})\n", {"F27:A1", "F27:A7"}),
    ("N06", "K-9-66", "回傳輸入之態（⛔ 末次通過之態）", _BM, "    return _cur966, _got966, _steps966",
     "    return state, _got966, _steps966", {"F27:A9"}),
    ("N07", "K-9-66 ②", "二分法之支反之", _BM, "            if _new966 is None:\n                _hi966",
     "            if _new966 is not None:\n                _hi966", {"F27:A1"}),
    ("N08", "K-9-66", "要求之類之停機去之", _BM, "        if _c966.get('cls') not in K966_CLASSES:", "        if False:",
     {"F27:A8"}),
    ("N09", "K-9-66 ②", "二分法⛔ 記通過之態", _BM, "                _lo966, _win966 = _md966, _new966",
     "                _lo966 = _md966", {"F27:A9"}),
    ("N10", "K-9-66 ②", "試之量與所記之量不一", _BM, "_s966[_i966] * (_md966 * grid) / _sum966)",
     "_s966[_i966] * (_md966 * grid) / _sum966 * 1.0001)", {"F27:A1"}),
    ("N11", "K-9-66 ②", "類之全量成而⛔ 承接其態", _BM, "                _cur966 = _new966\n                for _i966 in _ix966:",
     "                for _i966 in _ix966:", {"F27:A2", "F27:A6"}),
    ("N12", "K-9-67", "去重劃前面積之鍵", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
     "return (-adj_q2(g), str(pid))", {"F27:C1"}),
    ("N13", "K-9-67", "應分配面積⛔ 以 0.01 ㎡ 量化", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
     "return (-float(g), -adj_q2(pre_area), str(pid))", {"F27:C2"}),
    ("N14", "K-9-67", "重劃前面積之序反之", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
     "return (-adj_q2(g), adj_q2(pre_area), str(pid))", {"F27:B1", "F27:C1"}),
    ("N15", "K-9-67", "重劃前面積先於應分配面積", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
     "return (-adj_q2(pre_area), -adj_q2(g), str(pid))", {"F27:B1"}),
    ("N16", "K-9-67", "成員缺⛔ 取自身", _PA, "    for _m967 in (members or [pid]):", "    for _m967 in (members or []):",
     {"F27:B3"}),
    ("N17", "K-9-68", "段三：一輪之要求⛔ 依受併之街廓分組", _S3,
     "            _b = _blk_of[e['r']]\n            if _b not in _bg:",
     "            _b = _blk_of[e['r']]\n            _bg.pop(_b, None)\n            if _b not in _bg:", {"F27:U1"}),
    ("N18", "K-9-51", "段三：第 5 項之候選⛔ 扣已試而未全收之街廓", _S3,
     "if _p == x or _p in merged_out or _b in F.get(x, set()) or _p not in state[\"by\"]:",
     "if _p == x or _p in merged_out or _p not in state[\"by\"]:", {"F27:U2"}),
    ("N19", "K-9-51", "段三：第 5 項之候選之序以 k967_rank 先於距離", _S3,
     "_cands.append(((_d, k967_rank(_G[_p], k967_pre_area(_p, _cm.get(_p), _pa), _p)), _p, _d,",
     "_cands.append(((k967_rank(_G[_p], k967_pre_area(_p, _cm.get(_p), _pa), _p), _d), _p, _d,", {"F16:K3"}),
    ("N20", "K-9-66", "段三：K-9-66 之列⛔ 記", _S3,
     "for e in _cs}) >= 2 and not (", "for e in _cs}) >= 9 and not (", {"F27:U1"}),
    ("N21", "K-9-68", "段三：第 5 項之輪之剩下⛔ 減其所併", _S3,
     "                if F is None:\n                    rem[x] -= g",
     "                if F is None:\n                    pass",
     {"F16:K2"}),
    ("N22", "R-17″", "段三：趟中之帳同一受併宗⛔ 累加（覆寫）", _S3,
     "                    _lg373[e['r']] = float(_lg373.get(e['r'], 0.0)) + float(v)",
     "                    _lg373[e['r']] = float(v)", {"F28:L6"}),
    ("N23", "R-17″", "段三：趟中之帳取輸入之帳 ＋ 最末一次", _S3,
     "                    _lg373 = dict(_dx.get('段三部分併出') or {})",
     "                    _lg373 = dict(_by0[x].get('段三部分併出') or {})", {"F28:L1", "F28:L6"}),
    ("N24", "R-17″", "段三：趟中之帳⛔ 寫", _S3,
     "                    _dx.update({'段三部分併出': _lg373, '段三併出': sorted(set(_dx.get('段三併出') or ()) | {e['r']})})",
     "                    pass", {"F28:L1"}),
    ("N25", "R-19″", "段三：第 5 項之重劃前面積之表取輸入之態", _S3,
     "               for p, t in state[\"by\"].items()}", "               for p, t in _by0.items()}", {"F28:L6"}),
    ("N26", "K-9-66", "段三：試施之受併宗之量⛔ 乘 κ", _S3,
     "            _apply(_tt, e['r'], [(x, e['k'] * float(v), False)])",
     "            _apply(_tt, e['r'], [(x, float(v), False)])", {"F16:K10"}),
    ("N27", "K-9-68", "段三：第 1 輪⛔ 記已試而未全收之街廓", _S3,
     "                elif _has357(e['s'] - g):\n                    F.setdefault(x, set()).add(_b)",
     "                elif _has357(e['s'] - g):\n                    pass", {"F27:U2"}),
    ("N28", "R-7 ③", "段三：題一 4 之半之片⛔ 入第 5 項之輪", _S3,
     "        _rnd373(_rq, _rem, _F)\n        _p5_373([c] + _hv, _rem, _F)",
     "        _rnd373(_rq, _rem, _F)\n        _p5_373([c], _rem, _F)",
     {"F16:K17"}),
    ("N29", "K-9-66", "段三：⛔ 以 k966_block_merge 之回傳之態承接", _S3,
     "            state, _gs, _steps = k966_block_merge(state, _cs, _try373)",
     "            _s0, _gs, _steps = k966_block_merge(state, _cs, _try373)", {"F27:U1"}),
    ("N30", "R-7 ②", "段三步驟 10：第 1 輪之來源量⛔ 除 κ", _S3,
     "            _rq10.append({'cls': _cls373[_kind(x)], 's': float(_q) / _kq,",
     "            _rq10.append({'cls': _cls373[_kind(x)], 's': float(_q),", {"F16:K10"}),
    ("N31", "R-7 ②", "段三步驟 10：非建地之片之剩下⛔ 記", _S3,
     "                _left[x] = max(0.0, _rem10.get(x, 0.0))", "                pass", {"F27:U1"}),
    ("N32", "R-7 ②", "段三步驟 10：剩下⛔ 入第 5 項之輪", _S3, "        _p5_373(_xs10, _rem10, _F10)", "        pass",
     {"F27:U2"}),
    ("N33", "K-9-66 R-5 (a)", "段三：建地之部分併出⛔ 留 build", _S3,
     "                if _has357(float(_dx.get('分攤登記面積_m2', 0) or 0) + float(_dx.get('面積_m2', 0) or 0) - float(v)):",
     "                if False:", {"F16:K7", "F16:K19"}),
    ("N34", "K-9-68", "手冊先行：一輪之要求⛔ 依受併之街廓分組", _MN,
     "            if _e953['bk'] not in _bg953:\n",
     "            _bg953.pop(_e953['bk'], None)\n            if _e953['bk'] not in _bg953:\n",
     {"F27:T1"}),
    ("N35", "K-9-51", "手冊先行：候選⛔ 扣已試而未全收之街廓", _MN,
     "                    if str(_bk) in _F953.get(_x, set()):\n                        continue\n",
     "                    if False:\n                        continue\n", {"F27:T2"}),
    ("N36", "K-9-66", "手冊先行：K-9-66 之列⛔ 記", _MN,
     "for _e953 in _cs953}) >= 2 and not (", "for _e953 in _cs953}) >= 9 and not (", {"F27:T1"}),
    ("N37", "K-9-68", "手冊先行：K-9-51 之輪之剩下⛔ 減其所併", _MN,
     "                if not _first:\n                    _rem953[_x] -= _gv",
     "                if not _first:\n                    pass",
     {"F27:T1"}),
    ("N38", "R-17″", "手冊先行：趟中之帳同一受併宗⛔ 累加（覆寫）", _MN,
     "                    _lg953[_e953['r']] = float(_lg953.get(_e953['r'], 0.0)) + float(_v)",
     "                    _lg953[_e953['r']] = float(_v)", {"F28:L4"}),
    ("N39", "R-17″", "手冊先行：趟中之帳取輸入之帳 ＋ 最末一次", _MN,
     "                    _lg953 = dict(_dx.get('段三部分併出') or {})",
     "                    _lg953 = dict(_tin953[_x].get('段三部分併出') or {})", {"F28:L4"}),
    ("N40", "R-17″", "手冊先行：趟中之帳⛔ 寫", _MN,
     "                    _dx.update({'段三部分併出': _lg953, '段三併出': sorted(set(_dx.get('段三併出') or ()) | {_e953['r']})})",
     "                    pass", {"F28:L2"}),
    ("N41", "R-19″", "手冊先行：K-9-51 之重劃前面積之表取輸入之態", _MN,
     "                       for _pk953, _tq in state[\"by\"].items()}",
     "                       for _pk953, _tq in _tin953.items()}",
     {"F28:L4"}),
    ("N42", "K-9-66 R-5", "手冊先行：第 1 輪之來源量⛔ 除 κ", _MN,
     "                _rq953.append({'cls': _kind953[_sort953(_tin953[_x])], 's': float(_qv) / _kv,",
     "                _rq953.append({'cls': _kind953[_sort953(_tin953[_x])], 's': float(_qv),", {"F27:T5"}),
    ("N43", "R-18″", "手冊先行：趟末之前帳取當下之態", _MN,
     "            _pp953 = dict((str(_k), float(_v)) for _k, _v in (_tin953[_x].get('段三部分併出') or {}).items())",
     "            _pp953 = dict((str(_k), float(_v)) for _k, _v in (_d.get('段三部分併出') or {}).items())", {"F27:T1"}),
    ("N44", "K-9-66", "手冊先行：⛔ 以 k966_block_merge 之回傳之態承接", _MN,
     "            state, _gs953, _stp953 = k966_block_merge(state, _cs953, _try953k)",
     "            _s0, _gs953, _stp953 = k966_block_merge(state, _cs953, _try953k)", {"F27:T1"}),
    ("N45", "K-9-68", "第一趟：一輪之要求⛔ 依受併之街廓分組", _A4,
     "            if _e['bk'] not in _bg_a4:\n",
     "            _bg_a4.pop(_e['bk'], None)\n            if _e['bk'] not in _bg_a4:\n",
     {"F27:V1"}),
    ("N46", "R-17″", "第一趟：趟中之帳同一受併宗⛔ 累加（覆寫）", _A4,
     "                    _lg_a4[_e['r']] = float(_lg_a4.get(_e['r'], 0.0)) + float(_v)",
     "                    _lg_a4[_e['r']] = float(_v)", {"F28:L5"}),
    ("N47", "R-17″", "第一趟：趟中之帳取輸入之帳 ＋ 最末一次", _A4,
     "                    _lg_a4 = dict(_dx.get('段三部分併出') or {})",
     "                    _lg_a4 = dict(_tin_a4[_x].get('段三部分併出') or {})", {"F28:L5"}),
    ("N48", "R-17″", "第一趟：趟中之帳⛔ 寫", _A4,
     "                    _dx.update({'段三部分併出': _lg_a4, '段三併出': sorted(set(_dx.get('段三併出') or ()) | {_e['r']})})",
     "                    pass", {"F28:L3"}),
    ("N49", "R-19″", "第一趟：各輪之重劃前面積之表取輸入之態", _A4,
     "- sum(float(_v) for _v in (_t.get('段三部分併出') or {}).values()) for _p, _t in state[\"by\"].items()}",
     "- sum(float(_v) for _v in (_t.get('段三部分併出') or {}).values()) for _p, _t in _tin_a4.items()}", {"F28:L5"}),
    ("N50", "K-9-66", "第一趟：K-9-66 之列⛔ 記", _A4,
     "for _e in _cs_a4}) >= 2 and not _all_ok:", "for _e in _cs_a4}) >= 9 and not _all_ok:", {"F27:V1"}),
    ("N51", "K-9-68", "第一趟：剩下⛔ 減其所併（記為 0）", _A4, "                    _L[_x] = _e['s'] - _g",
     "                    _L[_x] = 0.0", {"F27:V1"}),
    ("N52", "K-9-68", "第一趟：受詞每輪沿名單⛔ 止於首一有其宗之街廓", _A4,
     "                break\n        _bo_a4, _bg_a4 = [], {}", "\n        _bo_a4, _bg_a4 = [], {}", {"F27:V2"}),
    ("N53", "K-9-66", "第一趟：同類之片之序（剩下大者先）反之", _A4,
     "key=lambda _y: (_rank_a4[_cls[_y]], -_L[_y], _y)):", "key=lambda _y: (_rank_a4[_cls[_y]], _L[_y], _y)):",
     {"F24:K25"}),
    ("N54", "K-9-67", "第一趟：受併宗之序去 k967_rank", _A4,
     "            k967_rank(_S['G'][_h], k967_pre_area(_h, _ms, _pre_a4), _h))", "            _h)", {"F24:K7"}),
    ("N55", "R-18″", "第一趟：趟末之前帳取當下之態", _A4,
     "            _pp_a4 = dict((str(_k), float(_v)) for _k, _v in (_tin_a4[_x].get('段三部分併出') or {}).items())",
     "            _pp_a4 = dict((str(_k), float(_v)) for _k, _v in (_d.get('段三部分併出') or {}).items())", {"F27:V1"}),
    ("N56", "K-9-66", "第一趟：⛔ 以 k966_block_merge 之回傳之態承接", _A4,
     "            state, _gs_a4, _st_a4 = k966_block_merge(state, _cs_a4, _try_a4k)",
     "            _s0, _gs_a4, _st_a4 = k966_block_merge(state, _cs_a4, _try_a4k)", {"F27:V1"}),
    ("N57", "K-9-66 通知 3", "調配之輸入：建地之部分併出之原有面積⛔ 依剩下之比", _AI,
     "            _row.update(所屬單元=_up, 原有面積=_a(t) * _rho_b, 段三併出面積=_a(t) * (1.0 - _rho_b))",
     "            _row.update(所屬單元=_up, 原有面積=_a(t), 段三併出面積=0.0)", {"F27:W1", "F27:W2"}),
]


def _fn_spans(src):
    ls = src.splitlines(keepends=True)
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef):
            out[n.name] = (sum(len(x) for x in ls[:n.lineno - 1 - len(n.decorator_list)]),
                           sum(len(x) for x in ls[:n.end_lineno]))
    return out


def _child(repo, app):
    """（內部）以 `app` 取受詞，跑 F27／F28／F23／F24／F16 之 selftest 之項，印 {器: 紅項} 之 JSON（末列）。"""
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    import selection_pipeline as sp
    with contextlib.redirect_stdout(io.StringIO()):
        ns, _ = harvest(app)
    me = sys.modules[__name__]
    P = "verify/probes/"
    f12 = _load(repo, P + "probe_WG9353_endmerge.py", "f12_377")
    f16 = _load(repo, P + "probe_WG9357_k948.py", "f16_377")
    f23 = _load(repo, P + "probe_WG9363_k953.py", "f23_377")
    f24 = _load(repo, P + "probe_WG9367_adj4.py", "f24_377")
    f28 = _load(repo, P + "probe_WG9373p1_partrem.py", "f28_377")
    out = {}
    for k, fn in (("F27", lambda: _cases(ns, sp)), ("F28", lambda: f28._cases(ns, f12, f16, me, f23)),
                  ("F23", lambda: f23._cases(ns, sp)), ("F24", lambda: f24._cases(ns, sp)),
                  ("F16", lambda: f16._cases(ns, sp))):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                cs = fn()
            out[k] = _report(cs, verbose=False)
        except Exception as ex:  # noqa: BLE001
            out[k] = ["執行中止", type(ex).__name__]
    print(json.dumps(out, ensure_ascii=False))
    return 0


def mutate(repo):
    src = _read(repo, "app.py")
    spans = _fn_spans(src)
    tmp = tempfile.mkdtemp(prefix="wg9377mut_")
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")

    def one(m):
        mid, cl, desc, fn, old, new, want = m
        if mid == "N00":
            n, text = 1, src
        else:
            a, b = spans.get(fn, (0, 0))
            n = src[a:b].count(old)
            if n != 1:
                return m, n, None
            text = src[:a] + src[a:b].replace(old, new, 1) + src[b:]
        p = os.path.join(tmp, f"app_{mid}.py")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        try:
            r = subprocess.run([sys.executable, os.path.abspath(__file__), "_child", repo, p], capture_output=True,
                               text=True, encoding="utf-8", env=env, timeout=600)
        except subprocess.TimeoutExpired:
            return m, n, ("逾時",)
        try:
            red = json.loads((r.stdout.strip().splitlines() or ["null"])[-1])
        except Exception:  # noqa: BLE001
            red = None
        if r.returncode != 0 or not isinstance(red, dict):
            return m, n, ("例外", (r.stderr.strip().splitlines() or ["?"])[-1][:200])
        return m, n, red

    todo = [("N00", "—", "基準（⛔ 突變）", None, None, None, set())] + MUT377
    bad = []
    try:
        with ThreadPoolExecutor(2) as ex:
            res = list(ex.map(one, todo))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)          # 暫存之 app_*.py（每份約 1.8 MB）⛔ 遺留
    for m, n, red in res:
        mid, cl, desc, fn, old, new, want = m
        got = {f"{k}:{i}" for k, v in red.items() for i in v} if isinstance(red, dict) else None
        if mid == "N00":
            ok = got == set()
        else:
            ok = n == 1 and got is not None and bool(want) and want <= got
        if not ok:
            bad.append(mid)
        shown = sorted(got) if got is not None else red
        print(f"  {'✅' if ok else '🔴'} {mid} {cl}·{desc}：錨 {n} 見；所指 {sorted(want)}；紅 {shown}")
    print(f"⇒ 突變 {len(MUT377)}（另基準一）；紅 {bad}；rc {1 if bad else 0}")
    return 1 if bad else 0


# ── run：本案 ──
R2_EXPECT = {3.5: [("R3", ["628-28(1)", "628-29(1)"], "628-28(1)", 69.2, 114.0), ("R6", ["628-21(1)", "628-22(1)",
                                                                                         "628-23(1)"], "628-21(1)", None, None)],
             0.0: [("R3", ["628-28(1)", "628-29(1)"], "628-28(1)", 65.75, 114.0), ("R6", ["628-21(1)", "628-22(1)",
                                                                                          "628-23(1)"], "628-21(1)", None, None)]}


def run(repo, sbs):
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    from stepg_pipeline import run_step_g
    for k in list(os.environ):
        if k.startswith("WV_"):
            print(f"  🔴 殼有 {k}（本器須於無 WV_ 之殼跑）")
            print("⇒ 紅 ['殼']；rc 1")
            return 1
    f4 = _load(repo, "verify/probes/probe_WG9345_screen.py", "f4_for_f27")
    orig = ns["k929_6_fixpoint"]
    cap = []

    def wrap(build, trial, own, pre, fl, **kw):
        outs = []

        def tr(b):
            o = trial(b)
            outs.append(o)
            return o
        bf, last, log = orig(build, tr, own, pre, fl, **kw)
        pre_a = {str(t.get("暫編地號")): float(t.get("分攤登記面積_m2") or 0) for t in build}
        for e in log:
            rows, dropped = outs[e["輪"] - 1][0], outs[e["輪"] - 1][1]
            g = {}
            for r in rows or []:
                g[str(r.get("暫編地號"))] = float(r.get("G(㎡)") or 0)
            for _k, lst in (dropped or {}).items():
                for d in lst:
                    g[str(d.get("暫編地號"))] = float(d.get("G(㎡)") or 0)
            cap.append((e["街廓"], sorted(e["成員"]), e["標的"], {p: g.get(p) for p in e["成員"]},
                        {p: pre_a.get(p) for p in e["成員"]}))
        return bf, last, log
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
                Hs = sp._k6b_callbacks(ns, fst, cb, cad, params, sb, snap)["alloc_state"](tp, bp)
            ss.clear(); ss.update(copy.deepcopy(saved))
            ns["K917_DROPPED"].clear(); ns["K917_DROPPED"].update(copy.deepcopy(k917))
            pk, g = f4._screen_inputs(ns, fst, snap, cb, cad, params, tp, bp, sb)
            qs = f4.QuietSt(ss)
            with contextlib.redirect_stdout(io.StringIO()):
                Ss = ns["k6b_screen_callbacks"](qs, pk_kwargs=pk, g_kwargs=g)["alloc_state"](tp, bp)
            ss.clear(); ss.update(copy.deepcopy(saved))
            ns["K917_DROPPED"].clear(); ns["K917_DROPPED"].update(copy.deepcopy(k917))
            with contextlib.redirect_stdout(io.StringIO()):
                res = sp.run_corner_pk_k6b(ns, fst, cb, cad, params, tp, bp, sb, snapshot=snap)
            s3 = copy.deepcopy(ss.get("f3_k6b_stage3_log") or [])
            k953 = copy.deepcopy(ss.get("f3_k953_log") or [])
            a4 = copy.deepcopy(ss.get("f3_adj4_log") or [])
            cap.clear()
            ns["k929_6_fixpoint"] = wrap
            ns["K917_DROPPED"].clear()
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    run_step_g(ns, fst, cb, cad, snap, params, res[6], res[3], res[4], sb, eff_min_build_by_blk={})
            finally:
                ns["k929_6_fixpoint"] = orig
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️ {sb}：執行中止 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
            print("⇒ rc 3（無從判定）")
            return 3
        # R1
        s3p = [r for r in s3 if r.get("序") == "後處理"]
        s3_bad = [r.get("候選") for r in s3p if r.get("層級") in ("K-9-66", "後處理·第5項") or r.get("結果") != "成"]
        k_batch = [r.get("結果") for r in k953 if r.get("序") == "整批"]
        k_bad = [r.get("序") for r in k953 if r.get("序") in ("K-9-66", "K-9-51")]
        a_bad = [(r.get("序"), r.get("結果")) for r in a4 if not (r.get("序") == "整體" and r.get("結果") == "成")]
        ok1 = not s3_bad and k_batch in ([], ["成"]) and not k_bad and not a_bad
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：段三後處理 {len(s3p)} 列皆成、⛔ K-9-66／第 5 項 {not s3_bad}；"
              f"手冊先行之整批 {k_batch}、⛔ K-9-66／K-9-51 {not k_bad}；第一趟 {len(a4)} 列皆整體成 {not a_bad}")
        if not ok1:
            red.append(f"R1@{sb}")
        # R2
        got2 = []
        for blk, mem, tgt, gm, pm in cap:
            q = {p: round(float(v), 2) for p, v in gm.items() if v is not None}
            tie = len(set(q.values())) == 1 and len(q) >= 2
            got2.append((blk, mem, tgt, (next(iter(q.values())) if tie else None),
                         (round(float(next(iter(pm.values()))), 2) if tie and len({round(float(v), 2) for v in pm.values()}) == 1
                          else None)))
        ok2 = sorted(got2) == sorted(R2_EXPECT.get(sb, []))
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：入池閘之代表宗（街廓, 成員, 標的, 並列之 G, 並列之重劃前面積）{sorted(got2)}")
        if not ok2:
            red.append(f"R2@{sb}")
        # R3
        mh, ms = Hs.get("members"), Ss.get("members")
        unit = (mh or {}).get("628-28(1)")
        ok3 = isinstance(mh, dict) and mh == ms and len(mh) > 0 and unit == ["628-28(1)", "628-29(1)"]
        print(("  ✅" if ok3 else "  🔴") + f" R3@{sb}：段三之試算之 members harness ＝ 畫面 {isinstance(mh, dict) and mh == ms}"
              f"（{len(mh or {})} 宗）；R3 之單元 {unit}")
        if not ok3:
            red.append(f"R3@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], os.path.abspath(argv[2])
    if cmd == "mutate":                                       # 🆕 `W-G.9-377`
        return mutate(repo)
    if cmd == "_child" and len(argv) == 4:                    # 🆕 `W-G.9-377`（mutate 之子程序·內部）
        return _child(repo, os.path.abspath(argv[3]))
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
