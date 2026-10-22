# -*- coding: utf-8 -*-
"""W-G.9-389 量測器（發單端擬·檔 F33·⛔ 由受單側改一字）：試算內之程式之停機之上拋。

所量之性質：程式之停機（訊息帶 `GB-` 之號或【未裁】者）於試算（街角定案、併入之前後之配地）之內觸之者，⛔ 判為
  「不過」「未成」「試算中止」而續辦——其訊息之全文上拋（配地停機·loud）；他之試算中止（配地上不可）照舊為「不過」。
  機制：`app.py` 之 `k6_program_stop`（登記於 `K6_PROGRAM_STOPS` 並回 `RuntimeError`）、`k6_trial_mark`、
  `k6_trial_raise_since`；吞試算之中止之處，於試算之前取其長度、其後見有新登記者即上拋。

子命令（一律 python3 verify/probes/probe_WG9389_trialstop.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取三函式、`k929_6_fixpoint`、`end_block_merge_run`；入池閘之玩具
           借 F29〔`probe_WG9375_k965.py`〕之 `ToyLate`／`mk`／`BLK`，另以前緣線之軸定推進序〔`ToyAxis`·供旋轉、鏡射〕）：
           K1〜K16（期值皆手算·見各例之註）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           AST 查接線：X1 `app.py` 之 `raise` 其字串常數帶 `GB-\\d+`／【未裁】者皆為 `raise k6_program_stop(…)`，
           `raise k6_program_stop(…)` 之訊息皆帶號，`k6_program_stop` ⛔ 他用；X2 `app.py` 與 `verify/selection_pipeline.py` 之每一 `try`——其本體呼叫試算
           （`f3_screen_stepg_run`／`run_step_g`／`trial`／`alloc_eval`）而有吞 `RuntimeError`／`_K6BTrialStop`／`Exception`
           之處置（其本體無 `raise`）者——其前之同一區塊（或其所屬之 with 之區塊）以 `<名> = k6_trial_mark()` 取 mark，
           且其每一吞之處置之本體之某句、或其後之首句，即 `k6_trial_raise_since(<該名>, …)` 之句（⛔ 於 if／lambda 之內）；X3 新頂層之名 ＝ 五；`app.py` 之頂層節點對基準之相異 ⊆ 本單之許，其差唯
           `raise RuntimeError(`→`raise k6_program_stop(` 之換與含 `k6_trial_` 之增列；X4 `verify/` 頂層之 `*.py` 對基準
           唯 `selection_pipeline.py` 異、其差唯含 `k6_trial_` 之增列；X5 三函式內⛔ 案件字面。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 街角選位至配地（`run_corner_pk_k6b` ＋ `run_step_g`）⛔ 停機、
           且 `K6_PROGRAM_STOPS` 終為空（本案之一切試算⛔ 觸程式之停機 ⇒ 上拋之機制⛔ 觸 ⇒ 配地⛔ 變）；
           R2（唯首一退縮）注入：手冊先行之內，入池閘自其第 2 次之呼叫起立程式之停機（`GB-999`）⇒ 須上拋至
           `run_corner_pk_k6b`（訊息含 `GB-999` 與「試算內之程式之停機·手冊先行」）·⛔ 判為不過而續辦。
🔧 `W-G.9-390`（`K-9-61` ④·⛔ 上列一字不刪）：X3 之許增 `k6b_stage3_run`（其差⛔ 限於二形·其行為與接線由 F34 量之）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, difflib, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

FNS = ["k6_program_stop", "k6_trial_mark", "k6_trial_raise_since"]
NEW_TOP = {"K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since"}
# 本單之許（app.py 之頂層節點·其差唯 X3 之二形）
ALLOW = {"evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
         "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953",
         "f3_screen_adj4"}
# 🔧 `W-G.9-390`：其後之單所改之頂層節點（⛔ 限於二形·F34 量之）
ALLOW390 = {"k6b_stage3_run"}
# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
TAG_RE = re.compile(r"(?<![0-9A-Za-z\-])GB-\d+(?![0-9])|【未裁】")
TRIAL_CALLS = {"f3_screen_stepg_run", "run_step_g", "trial", "alloc_eval"}
CATCH = {"RuntimeError", "_K6BTrialStop", "Exception"}
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _f29(repo):
    sys.path.insert(0, os.path.join(repo, "verify", "probes"))
    import probe_WG9375_k965 as F29
    return F29


# ───────────────────────── selftest ─────────────────────────

def _toy_axis(F29):
    class ToyAxis(F29.ToyLate):
        """F29 之 ToyLate，而推進序依各街廓之前緣線之軸（p1→p2）之投影（⛔ 依 x）；`stop` ＝ (成員之集, 種類)：
        build 含某單元之成員 ⊇ 所指者 ⇒ 試算立停機（種類 'prog' ＝ 程式之停機〔k6_program_stop〕；'plain' ＝ 配地中止）。"""

        def __init__(self, blocks, fl, ns, stop=None, tag="GB-999 玩具"):
            super().__init__(blocks)
            self.fl, self.ns, self.stop, self.tag, self.hits = fl, ns, stop, tag, 0

        def trial(self, build):
            from shapely.geometry import Polygon
            if self.stop is not None:
                need, kind = self.stop
                if any(frozenset(t.get("入池閘併入") or [t["暫編地號"]]) >= frozenset(need) for t in build):
                    self.hits += 1
                    if kind == "prog":
                        raise self.ns["k6_program_stop"](f"🔴 [{self.tag}] 試算內之程式之停機（合成）")
                    raise RuntimeError("🔴 [玩具] 配地中止（合成·⛔ 帶號）")
            rows, dropped = [], {}
            for blk, P in self.blocks.items():
                (x1, y1), (x2, y2) = self.fl[blk]["p1"], self.fl[blk]["p2"]
                L = math.hypot(x2 - x1, y2 - y1)
                ux, uy = (x2 - x1) / L, (y2 - y1) / L
                ps = [t for t in build if t["所屬街廓"] == blk]
                pr = {}
                for t in ps:
                    q = Polygon(t["polygon_coords"]).centroid
                    pr[t["暫編地號"]] = (q.x - x1) * ux + (q.y - y1) * uy
                left = sorted([t for t in ps if pr[t["暫編地號"]] < P["split_x"]], key=lambda t: pr[t["暫編地號"]])
                right = sorted([t for t in ps if pr[t["暫編地號"]] >= P["split_x"]], key=lambda t: -pr[t["暫編地號"]])
                sumg = 0.0
                for side, grp in (("left", left), ("right", right)):
                    p = 0
                    for t in grp:
                        k = t["暫編地號"]
                        a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
                        corner = k in P["corner"]
                        g = a * F29.RHO - (P["burden"] if (p == 0 and not corner) else 0.0)
                        if not corner and g < P["m"]:
                            dropped.setdefault((blk, side), []).append({"暫編地號": k, "G(㎡)": round(g, 4)})
                            continue
                        rows.append({"暫編地號": k, "所屬街廓": blk, "推進側別": side, "G(㎡)": round(g, 4),
                                     "驗_宗序": "街角第1宗" if corner else "其後", "驗_總判": "保留"})
                        sumg += g
                        p += 1
                w = max(0.01, (P["cap"] - sumg) / P["depth"])
                rows.append({"暫編地號": f"{blk}-抵費地", "所屬街廓": blk, "推進側別": "抵費地", "G(㎡)": 0,
                             "cut_coords": F29.rect(0, w, 0, P["depth"])})
            return rows, dropped, None
    return ToyAxis


def _xf(pt, T):
    # T ＝ (θ 度, 鏡射與否, 平移 (dx, dy))：先鏡射（x → −x）、次旋轉、再平移
    th, mir, (dx, dy) = T
    x, y = pt
    if mir:
        x = -x
    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
    return (x * c - y * s + dx, x * s + y * c + dy)


def _world(F29, T=(0.0, False, (0.0, 0.0)), names=None):
    """示範街廓（F29 K6 之形）：街廓 A·前緣線 p1(0,0)→p2(30,0)·三宗由 p1 往 p2 依序：
    C（歸戶甲·分攤 300·街角第 1 宗）、X（歸戶甲·60）、Z（歸戶丙·400）。玩具：G ＝ a × 0.6；各側首宗減側街負擔 9（街角
    第 1 宗免、恆配地）；最小分配 100。手算：C 180；X 於 C 之後 36 ＜ 100 ⇒ 不配地；Z 240。入池閘：X 與同街廓同歸戶之
    街角第 1 宗 C 相連 ⇒ ⛔ 合併、依手冊併入 C（`K-9-58` ①·併入之後試算以檢核之）⇒ 單元 C{C, X}：a ＝ 360 ⇒ 216。
    `names` ＝ 換名之表（暫編地號、原地號、街廓、歸戶）。"""
    n = dict(X="X", C="C", Z="Z", A="A", o1="o1", oc="oc", o9="o9", 甲="GA", 丙="GZ")
    n.update(names or {})
    b = [F29.mk(n["C"], n["oc"], n["A"], 300, 0, 10), F29.mk(n["X"], n["o1"], n["A"], 60, 10, 20),
         F29.mk(n["Z"], n["o9"], n["A"], 400, 20, 30)]
    for t in b:
        cs = [_xf(c, T) for c in t["polygon_coords"]]
        if T[1]:
            cs = cs[::-1]
        t["polygon_coords"] = cs
    p1, p2 = _xf((0.0, 0.0), T), _xf((30.0, 0.0), T)
    own = {n["oc"]: n["甲"], n["o1"]: n["甲"], n["o9"]: n["丙"]}
    return b, own, {n["A"]: F29.BLK(split_x=1000.0, corner={n["C"]})}, {n["A"]: {"p1": p1, "p2": p2}}, n


def _run_world(ns, F29, Toy, T=(0.0, False, (0.0, 0.0)), names=None, stop_kind=None):
    b, own, blocks, fl, n = _world(F29, T, names)
    toy = Toy(blocks, fl, ns, stop=((n["X"], n["C"]), stop_kind) if stop_kind else None)
    kw = dict(temp_parcels=b, cat_of={k: "住宅區" for k in blocks}, front_rows={k: {"正面路寬(m)": 8} for k in blocks})
    try:
        bf, out, log = ns["k929_6_fixpoint"](b, toy.trial, own, {"z1": 1.0}, fl, **kw)
    except RuntimeError as e:
        return {"停機": str(e), "hits": toy.hits}, n
    s = F29._summ(bf, out, log)
    return {"alloc": s["alloc"], "units": s["units"], "drops": s["drops"], "hits": toy.hits}, n


def _canon(res, n):
    # 名之還原（換名之例與原例比）
    inv = {v: k for k, v in n.items()}
    if "停機" in res:
        return {"停機含號": bool(TAG_RE.search(res["停機"])), "hits≥1": res["hits"] >= 1}
    return {"alloc": {inv.get(k, k): v for k, v in res["alloc"].items()},
            "units": {inv.get(k, k): sorted(inv.get(m, m) for m in v) for k, v in res["units"].items()},
            "drops": sorted(inv.get(k, k) for k in res["drops"]), "hits": res["hits"]}


def cases(ns, F29):
    C = []
    STOPS = ns["K6_PROGRAM_STOPS"]
    ps, mark, since = ns["k6_program_stop"], ns["k6_trial_mark"], ns["k6_trial_raise_since"]

    # K1 登記之全文：長訊（號在第 1500 字之後）⇒ 回 RuntimeError（⛔ 拋）·登記 ＋1·全文逐字（`自誤`／387 之註：截去號之誤）
    m0 = len(STOPS)
    long = "🔴 " + "長" * 1500 + "（GB-205）⇒ 停機"
    e = ps(long)
    C.append(("K1 程式之停機：回 RuntimeError·登記全文（⛔ 截）",
              (type(e).__name__, str(e) == long, len(STOPS) - m0, (STOPS[-1] if STOPS else None) == long), ("RuntimeError", True, 1, True)))
    # K2 ⛔ 帶號之訊息 ⇒ 停機（⛔ 登記）
    m0 = len(STOPS)
    try:
        ps("🔴 一般之配地中止")
        got = ("未停機", len(STOPS) - m0)
    except RuntimeError as e2:
        got = ("W-G.9-389" in str(e2), len(STOPS) - m0)
    C.append(("K2 ⛔ 帶號 ⇒ 停機、⛔ 登記", got, (True, 0)))
    # K3 邊界：號之前接英字（`XGB-12`、`MGB-1`）、連字號（`W-GB-1`）、數字（`1GB-2`）⇒ ⛔ 號；無數字（`GB-`）⇒ ⛔ 號；
    #     數字後接英字（`GB-12a`）⇒ 號；【未裁】單獨 ⇒ 號
    res = []
    for s_ in ("XGB-12 停機", "GB- 停機", "(GB-13)", "【未裁】", "GB-2050", "·GB-201：", "MGB-1", "W-GB-1", "1GB-2",
               "GB-12a"):
        m0 = len(STOPS)
        try:
            ps(s_)
            res.append((s_, len(STOPS) - m0))
        except RuntimeError:
            res.append((s_, "停"))
    C.append(("K3 號之邊界（前接英數或連字號者⛔ 號；無數字者⛔ 號）", res,
              [("XGB-12 停機", "停"), ("GB- 停機", "停"), ("(GB-13)", 1), ("【未裁】", 1), ("GB-2050", 1),
               ("·GB-201：", 1), ("MGB-1", "停"), ("W-GB-1", "停"), ("1GB-2", "停"), ("GB-12a", 1)]))
    # K4 零／一／二：mark 之後無新登記 ⇒ ⛔ 拋；一 ⇒ 拋其全文；二 ⇒ 拋其首者
    k0 = mark()
    try:
        since(k0, "例")
        z = "⛔ 拋"
    except RuntimeError as e3:
        z = str(e3)
    ps("🔴 甲 GB-1")
    try:
        since(k0, "例")
        o = "⛔ 拋"
    except RuntimeError as e4:
        o = str(e4)
    ps("🔴 乙 GB-2")
    try:
        since(k0, "例")
        t2 = "⛔ 拋"
    except RuntimeError as e5:
        t2 = str(e5)
    C.append(("K4 新登記 零／一／二 ⇒ ⛔ 拋／拋其全文／拋其首者",
              (z, o.endswith("🔴 甲 GB-1") and "例" in o, t2.endswith("🔴 甲 GB-1")), ("⛔ 拋", True, True)))
    # K5 巢狀：外 mark → 登記 A → 內 mark → 登記 B ⇒ 內見 B、外見 A
    k_out = mark()
    ps("🔴 A GB-3")
    k_in = mark()
    ps("🔴 B GB-4")
    got5 = []
    for k_ in (k_in, k_out):
        try:
            since(k_, "巢")
            got5.append("⛔ 拋")
        except RuntimeError as e6:
            got5.append(str(e6).split("] ", 1)[1])
    C.append(("K5 巢狀之試算以長度分之", got5, ["🔴 B GB-4", "🔴 A GB-3"]))

    Toy = _toy_axis(F29)
    T0 = (0.0, False, (0.0, 0.0))
    # K6 入池閘：依手冊併入後之試算（檢核）立程式之停機 ⇒ 上拋（含號）·⛔ 判為不過（手算：C{C,X} 之試算觸之）
    r6, _n6 = _run_world(ns, F29, Toy, T0, stop_kind="prog")
    C.append(("K6 入池閘之併入後之試算立程式之停機 ⇒ 上拋",
              ("停機" in r6 and "GB-999 玩具" in r6["停機"] and "試算內之程式之停機·入池閘" in r6["停機"], r6["hits"]),
              (True, 1)))
    # K7 對照：同形而為配地中止（⛔ 帶號）⇒ 照舊：整筆之併入判為不過 ⇒ 依 `K-9-66` 按比例（`0.01 ㎡` 之格·玩具唯整筆之
    #     單元觸之）⇒ 併入 59.99 ⇒ C (300 ＋ 59.99) × 0.6 ＝ 215.994 → 215.99；X 剩 0.01 不配地；⛔ 單元；Z 240
    r7, n7 = _run_world(ns, F29, Toy, T0, stop_kind="plain")
    EXP7 = {"alloc": {"C": 215.99, "Z": 240.0}, "units": {}, "drops": ["X"], "hits": 1}
    C.append(("K7 對照：配地中止（⛔ 帶號）⇒ 照舊為不過", _canon(r7, n7), EXP7))
    # K8 無停機之形（基底）：X 依手冊併入 C ⇒ C{C,X} 216、Z 240（同 F29 K6）
    r8, n8 = _run_world(ns, F29, Toy, T0)
    EXP8 = {"alloc": {"C": 216.0, "Z": 240.0}, "units": {"C": ["C", "X"]}, "drops": [], "hits": 0}
    C.append(("K8 基底（無停機）：X 依手冊併入街角第 1 宗 C", _canon(r8, n8), EXP8))
    # K9〜K12 換名、鏡射、旋轉（實座標之尺度 TWD97·任意角）：K6〜K8 之果除名稱外皆同
    NM = dict(X="甲-01", C="甲-00", Z="丙-07", A="B-東", o1="1001-1", oc="1001", o9="1009-3", 甲="H甲", 丙="H丙")
    for nm, T, names in (("K9 換名", T0, NM), ("K10 鏡射", (0.0, True, (0.0, 0.0)), None),
                         ("K11 旋轉 37°·TWD97", (37.0, False, (302511.37, 2652874.91)), None),
                         ("K12 鏡射 ＋ 旋轉 213°·TWD97·換名", (213.0, True, (302511.37, 2652874.91)), NM)):
        gs = []
        for sk in ("prog", "plain", None):
            r_, n_ = _run_world(ns, F29, Toy, T, names, stop_kind=sk)
            gs.append(_canon(r_, n_))
        C.append((f"{nm}：K6／K7／K8 之果除名稱外同", gs,
                  [{"停機含號": True, "hits≥1": True}, EXP7, EXP8]))
    # K13 末端塊合併再試：試算立程式之停機 ⇒ 上拋（⛔ 記為試算中止）
    def _ae_prog(t, b):
        raise ps("🔴 [GB-998 玩具] 末端塊之試算內之程式之停機")

    def _ae_plain(t, b):
        raise RuntimeError("🔴 [玩具] 末端塊之試算之配地中止")
    EBM = ns["end_block_merge_run"]
    try:
        EBM([], [], {}, set(), set(), {}, {}, None, _ae_prog, None, setback=3.5)
        g13 = "⛔ 拋"
    except RuntimeError as e7:
        g13 = ("GB-998 玩具" in str(e7), "試算內之程式之停機·末端塊合併再試" in str(e7))
    C.append(("K13 末端塊合併再試之試算立程式之停機 ⇒ 上拋", g13, (True, True)))
    # K14 對照：配地中止 ⇒ 照舊（標的 None·記其由）
    try:
        _t, _b, _l, rec = EBM([], [], {}, set(), set(), {}, {}, None, _ae_plain, None, setback=3.5)
        g14 = (rec.get("標的"), "末端塊之試算之配地中止" in str(rec.get("試算中止")), _l)
    except RuntimeError as e8:
        g14 = ("拋", str(e8)[:80])
    C.append(("K14 對照：末端塊之試算之配地中止 ⇒ 照舊記試算中止", g14, (None, True, [])))
    # K15 先前之登記（試算之前已在）⇒ ⛔ 致其後之試算上拋（以長度分之）：K1〜K5 所留之登記在，K7 仍照舊
    C.append(("K15 試算之前之登記⛔ 波及（K7 於 K1〜K5 之登記之後）", len(STOPS) > 0 and _canon(r7, n7) == EXP7, True))
    # K16 程式之停機上拋時，訊息之全文（含號之後之字）⛔ 截：長訊之號在第 1500 字之後
    m0 = mark()
    ps(long)
    try:
        since(m0, "長")
        g16 = "⛔ 拋"
    except RuntimeError as e9:
        g16 = str(e9).endswith(long)
    C.append(("K16 上拋之訊息為全文（號在 1500 字之後）", g16, True))
    return C


def selftest(repo):
    try:
        ns, _ = _harvest(repo)
        F29 = _f29(repo)
    except Exception as e:  # noqa: BLE001
        print(f"  🔴 受詞之取得中止：{type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    miss = [f for f in FNS + ["K6_PROGRAM_STOPS", "k929_6_fixpoint", "end_block_merge_run"] if f not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    ns["get_min_lot_size"] = lambda cat, w: {"min_width": 3.0, "min_depth": 10.0}
    ns["_rect_fits_free_pose"] = lambda P, W, D, *a, **k: (P.bounds[2] - P.bounds[0]) >= W - 1e-9
    red = []
    try:
        C = cases(ns, F29)
    except Exception as e:  # noqa: BLE001
        print(f"  🔴 例之執行中止：{type(e).__name__}：{str(e).splitlines()[0][:300] if str(e) else ''}")
        print("⇒ 紅 ['執行中止']；rc 1")
        return 1
    for name, got, exp in C:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {got!r}"[:600])
            print(f"       期 {exp!r}"[:600])
            red.append(name.split()[0])
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

def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _git_show(repo, base, rel):
    return subprocess.run(["git", "-C", repo, "show", f"{base}:{rel}"], capture_output=True,
                          check=True).stdout.decode("utf-8")


def _consts(node):
    return "".join(c.value for c in ast.walk(node) if isinstance(c, ast.Constant) and isinstance(c.value, str))


def _callname(c):
    f = c.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant) and isinstance(f.slice.value, str):
        return f.slice.value     # ns["名"](…)
    return None


def _x1(tree):
    bad, n_ok, other = [], 0, []
    raises = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call):
            raises.add(id(n.exc))
            if TAG_RE.search(_consts(n.exc)):
                if _callname(n.exc) == "k6_program_stop":
                    n_ok += 1
                else:
                    bad.append(n.lineno)
            elif _callname(n.exc) == "k6_program_stop":
                bad.append(n.lineno)          # ⛔ 帶號之訊息而經 k6_program_stop
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and _callname(n) == "k6_program_stop" and id(n) not in raises:
            other.append(n.lineno)
    return n_ok, bad, other


def _blocks_of(tree):
    # 每一語句之串列與其所屬之語句（函式之本體、if／for／while／with／try 之各支·處置之本體）→ [(串列, 所屬)]
    out = []
    for n in ast.walk(tree):
        for fld in ("body", "orelse", "finalbody"):
            v = getattr(n, fld, None)
            if isinstance(v, list) and v and all(isinstance(s, ast.stmt) for s in v):
                out.append((v, n))
        if isinstance(n, ast.Try):
            for h in n.handlers:
                out.append((h.body, h))
    return out


def _catches(h):
    t = h.type
    if t is None:
        return True
    names = [t] if not isinstance(t, ast.Tuple) else list(t.elts)
    return any((isinstance(x, ast.Name) and x.id in CATCH) for x in names)


def _calls_in(nodes, names):
    return any(isinstance(c, ast.Call) and _callname(c) in names for s in nodes for c in ast.walk(s))


def _x2(tree):
    """吞試算之中止之處：其前（同一串列、或其所屬之 with 之串列）有 `_m = k6_trial_mark()`；其每一吞之處置之內呼叫
    `k6_trial_raise_since`，或 try（連同其所屬之 with·該 with 之本體以之為末句者）之後之首句呼叫之。"""
    blocks = _blocks_of(tree)
    where = {}
    for lst, own in blocks:
        for i, st in enumerate(lst):
            where[id(st)] = (lst, i, own)
    sites, bad = [], []
    for lst, own in blocks:
        for i, s in enumerate(lst):
            if not isinstance(s, ast.Try) or not _calls_in(s.body, TRIAL_CALLS):
                continue
            sw = [h for h in s.handlers if _catches(h) and not any(isinstance(x, ast.Raise) for x in ast.walk(h))]
            if not sw:
                continue
            sites.append(s.lineno)
            chain = [(lst, i)]
            cur_l, cur_i, cur_own = lst, i, own
            while isinstance(cur_own, ast.With) and id(cur_own) in where:
                pl, pi, po = where[id(cur_own)]
                chain.append((pl, pi))
                if cur_i != len(cur_l) - 1:
                    break
                cur_l, cur_i, cur_own = pl, pi, po
            marks = {t.id for l_, j_ in chain for p in l_[:j_]
                     if isinstance(p, ast.Assign) and isinstance(p.value, ast.Call)
                     and _callname(p.value) == "k6_trial_mark" for t in p.targets if isinstance(t, ast.Name)}
            pre = bool(marks)

            def _is_rs(st):
                # 句之本身 ＝ `k6_trial_raise_since(<mark 之名>, …)`（Expr·⛔ 於 if／lambda 之內·首引數 ＝ 其前所取之 mark）
                return (isinstance(st, ast.Expr) and isinstance(st.value, ast.Call)
                        and _callname(st.value) == "k6_trial_raise_since" and st.value.args
                        and isinstance(st.value.args[0], ast.Name) and st.value.args[0].id in marks)
            inh = all(any(_is_rs(x) for x in h.body) for h in sw)
            after = False
            l_, j_ = lst, i
            k = 0
            while True:
                if j_ + 1 < len(l_):
                    after = _is_rs(l_[j_ + 1])
                    break
                k += 1
                if k >= len(chain):
                    break
                l_, j_ = chain[k]
            if not (pre and (after or inh)):
                bad.append(s.lineno)
    return sites, bad


def _top(src):
    t = ast.parse(src)
    out = {}
    for n in t.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out[n.name] = ast.get_source_segment(src, n)
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            out[n.targets[0].id] = ast.get_source_segment(src, n)
    return out


def _diff_ok(a, b):
    # 差唯：- `raise RuntimeError(` 之列 ↔ + 同列而換為 `raise k6_program_stop(`；+ 含 `k6_trial_` 之列
    dl = [l for l in difflib.ndiff(a.split("\n"), b.split("\n")) if l[:2] in ("- ", "+ ")]
    minus = [l[2:] for l in dl if l.startswith("- ")]
    plus = [l[2:] for l in dl if l.startswith("+ ")]
    conv = [l.replace("raise RuntimeError(", "raise k6_program_stop(", 1) for l in minus]
    if any("raise RuntimeError(" not in l for l in minus):
        return False, f"刪列非 raise RuntimeError：{[l for l in minus if 'raise RuntimeError(' not in l][:2]}"
    rest = list(plus)
    for c in conv:
        if c in rest:
            rest.remove(c)
        else:
            return False, f"換列之對無：{c[:80]}"
    extra = [l for l in rest if "k6_trial_" not in l]
    return (not extra), (f"增列非 k6_trial_：{extra[:2]}" if extra else f"換 {len(conv)}／增 {len(rest)}")


def wiring(repo, base):
    res = []
    try:
        src = _read(repo, "app.py")
        tree = ast.parse(src)
        bsrc = _git_show(repo, base, "app.py")
        btree = ast.parse(bsrc)
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠️ 受詞之讀取中止：{type(e).__name__}：{e}")
        print("⇒ rc 3（無從判定）")
        return 3
    # X1
    n_ok, bad, other = _x1(tree)
    bn_ok, bbad, _bo = _x1(btree)
    # 🔧 `W-G.9-392`：其後之單之 `k980_acq_check`（`GB-206`）之帶號之 raise 恰一亦許（其行為由 F36 量之）
    _kc392 = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "k980_acq_check"), None)
    _n392 = 0 if _kc392 is None else sum(1 for n in ast.walk(_kc392) if isinstance(n, ast.Raise)
                                         and isinstance(n.exc, ast.Call) and getattr(n.exc.func, "id", None) == "k6_program_stop")
    res.append(("X1 帶號之 raise 皆 k6_program_stop·⛔ 他用", (not bad) and (not other)
                and (n_ok == bn_ok + len(bbad) or (_n392 == 1 and n_ok == bn_ok + len(bbad) + 1))
                and n_ok > 0, f"帶號 {n_ok}（基準之帶號 {bn_ok + len(bbad)}·k980_acq_check {_n392}）／非者 {bad}／他用 {other}"))
    # X2
    try:
        ssrc = _read(repo, "verify/selection_pipeline.py")
        sbsrc = _git_show(repo, base, "verify/selection_pipeline.py")
        s1, b1 = _x2(tree)
        s2, b2 = _x2(ast.parse(ssrc))
        bs1, _ = _x2(btree)
        bs2, _ = _x2(ast.parse(sbsrc))
        ok2 = (not b1) and (not b2) and len(s1) == len(bs1) and len(s2) == len(bs2) and len(s1) + len(s2) > 0
        res.append(("X2 吞試算之中止之處皆取 mark 並上拋", ok2,
                    f"app.py 之處 {len(s1)}（基準 {len(bs1)}）未合 {b1}；selection_pipeline 之處 {len(s2)}"
                    f"（基準 {len(bs2)}）未合 {b2}"))
    except Exception as e:  # noqa: BLE001
        res.append(("X2 吞試算之中止之處皆取 mark 並上拋", False, f"中止 {type(e).__name__}：{e}"))
    # X3
    bt, ct = _top(bsrc), _top(src)
    add = set(ct) - set(bt)
    gone = set(bt) - set(ct)
    dif = sorted(k for k in set(bt) & set(ct) if bt[k] != ct[k])
    why = []
    for k in dif:
        if k in ALLOW:
            ok_, w_ = _diff_ok(bt[k], ct[k])
            if not ok_:
                why.append(f"{k}：{w_}")
    ok3 = add == NEW_TOP and not gone and set(dif) <= ALLOW | ALLOW390 and not why
    # 🔧 `W-G.9-391`：其新名與所改之頂層節點亦許（⛔ 及 ALLOW 之二形之查·F35 量之）
    ok3 = ok3 or (add == NEW_TOP | set(NEW391) and not gone and set(dif) <= ALLOW | ALLOW390 | set(W391) and not why)
    # 🔧 `W-G.9-392`：同（F36 量之）
    ok3 = ok3 or (add == NEW_TOP | set(NEW391) | set(NEW392) and not gone
                  and set(dif) <= ALLOW | ALLOW390 | set(W391) | set(W392) and not why)
    res.append(("X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形", ok3,
                f"增 {sorted(add)}／去 {sorted(gone)}／相異 {dif}／不合 {why}"))
    # X4
    try:
        ls = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", base, "verify/"], capture_output=True,
                            check=True).stdout.decode("utf-8").split()
        tops = sorted(p for p in ls if p.endswith(".py"))
        diffs = [p for p in tops if _git_show(repo, base, p) != _read(repo, p)]
        ok4a, w4 = _diff_ok(sbsrc, ssrc)
        ok4 = diffs == ["verify/selection_pipeline.py"] and ok4a and "換 0" in w4
        # 🔧 `W-G.9-391`：harness 二檔之增列亦許（selection_pipeline 之查照舊·F35 量之）
        ok4 = ok4 or (sorted(set(diffs) - set(F391)) == ["verify/selection_pipeline.py"] and ok4a and "換 0" in w4)
        res.append(("X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列", ok4, f"異 {diffs}／{w4}"))
    except Exception as e:  # noqa: BLE001
        res.append(("X4 verify/ 頂層唯 selection_pipeline.py 異", False, f"中止 {type(e).__name__}：{e}"))
    # X5
    lits = []
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name in FNS:
            for c in ast.walk(n):
                if isinstance(c, ast.Constant) and isinstance(c.value, str) and CASE_LIT_RE.match(c.value):
                    lits.append((n.name, c.value))
    res.append(("X5 三函式內⛔ 案件字面", not lits, f"{lits}"))
    red = []
    for name, ok, det in res:
        print(("  ✅ " if ok else "  🔴 ") + f"{name}（{det}）")
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

def _pipeline(ns, fst, rv, sp, sb):
    with contextlib.redirect_stdout(io.StringIO()):
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fst, snap)
        rv.build_ownership(ns, fst, rv.ANON_XLSX)
        v6 = open(rv.V6DXF, "rb").read()
        tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
        params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
        res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
        from stepg_pipeline import run_step_g
        ns["K917_DROPPED"].clear()
        sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                        eff_min_build_by_blk={})
    return res, sg


def run(repo, sbs):
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    if any(f not in ns for f in FNS + ["K6_PROGRAM_STOPS"]):
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    for sb in sbs:
        n0 = len(ns["K6_PROGRAM_STOPS"])
        try:
            _res, sg = _pipeline(ns, fst, rv, sp, sb)
            ok1 = len(ns["K6_PROGRAM_STOPS"]) == n0 and bool(sg.get("g_rows"))
            det = f"登記 {len(ns['K6_PROGRAM_STOPS']) - n0}·G 值列 {len(sg.get('g_rows') or [])}"
        except Exception as e:  # noqa: BLE001
            ok1, det = False, f"停機 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}"
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：本案⛔ 觸程式之停機（{det}）")
        if not ok1:
            red.append(f"R1@{sb}")
    # R2 注入（首一退縮）
    sb = sbs[0]
    k953, k929 = ns["k953_manual_run"], ns["k929_6_fixpoint"]
    st_ = {"in": False, "n": 0}

    def k953_w(*a, **k):
        st_["in"], st_["n"] = True, 0
        try:
            return k953(*a, **k)
        finally:
            st_["in"] = False

    def k929_w(*a, **k):
        if st_["in"]:
            st_["n"] += 1
            if st_["n"] >= 2:
                raise ns["k6_program_stop"]("🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成）")
        return k929(*a, **k)
    ns["k953_manual_run"], ns["k929_6_fixpoint"] = k953_w, k929_w
    try:
        _pipeline(ns, fst, rv, sp, sb)
        ok2, det = False, f"⛔ 上拋（手冊先行之入池閘之呼叫 {st_['n']}）"
    except RuntimeError as e:
        m = str(e)
        ok2 = "GB-999 注入" in m and "試算內之程式之停機·手冊先行" in m and st_["n"] >= 2
        det = f"上拋：{m.splitlines()[0][:160]}"
    except Exception as e:  # noqa: BLE001
        ok2, det = False, f"他之中止 {type(e).__name__}：{str(e).splitlines()[0][:160] if str(e) else ''}"
    finally:
        ns["k953_manual_run"], ns["k929_6_fixpoint"] = k953, k929
    print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：手冊先行之試算內之程式之停機 ⇒ 上拋（{det}）")
    if not ok2:
        red.append(f"R2@{sb}")
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
