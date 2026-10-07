# -*- coding: utf-8 -*-
"""W-G.9-367 量測器（發單側窗六十八擬·檔 F24·⛔ 由受單側改一字）：規格步 4 乙（`K-9-53` ②·第一趟·`K-9-56`）——
合併單位之地主另有已配得之宗者，沿其候選街廓名單，至第一個有其已配得之宗之街廓，將合併單位之土地（`a′` 折算）併入其
已配得之宗（`app.py` 之 `adj4_pass1_run`）；並量手冊先行之 `GB-201` 之防護（`k953_manual_run`）。

子命令（一律 python verify/probes/probe_WG9367_adj4.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取受詞；`verify/selection_pipeline.py` 取 `run_adj4`）。玩具之回呼：
           `alloc_state` 以 build 之全部（`drop` 除外）為保留；街廓內之 `面積_m2` 之和 `>` 該街廓之容量 ⇒ 該街廓之配餘地
           不合格一處；`err_cap` 逾者 ⇒ 配地中止；`lose` ＝ `{宗: (門檻, 失者)}`（該宗之 `面積_m2` `>` 門檻 ⇒ 失者不保留）；
           `G` ＝ 分攤登記面積 ＋ 面積（`gmap` 覆寫）；`a_prime` ＝ a(src) × p(src 之街廓) ÷ p(dst 之街廓）；
           `tie` ＝ `{片: 失者}`（該片離 build ⇒ 失者不保留）；`bar` ＝ `{片: 受阻者}`（該片在 build ⇒ 受阻者不保留）
           （二者皆 `W-G.9-370` 增）。
           K1〜K27 ＝ 各支（K23〜K27 ＝ `W-G.9-370` 之增·以 CC 之碼之突變之判別力為據；K9 之期 ＝ `W-G.9-370` 之訊息）（期值出自規格單 `§三`·⛔ 呼叫受測碼求期）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           接線（AST·字樣·工作樹對基準）：W1 模組層之新名與簽名；W2 harness 之入口（`run_adj4`）與 `run_corner_pk_k6b`
           之序；W3 畫面之入口（`f3_screen_adj4`）與 `f3_screen_k6b_stage3` 之序；W4 新碼⛔ 案件字面；W5 既有函式對基準
           一字未動（本單所改之三函式除外）·頂層節點之相異 ⊆ 本單之許；W6 本單所改之三函式對基準唯增列（⛔ 改既有一列）；
           W7 既有量測器之錨（其字串常數〔長 ≥ 4〕於基準之 app.py／selection_pipeline.py 恰一見者）於工作樹仍恰一見；
           基準中恰一之函式名（含巢狀）於工作樹仍恰一。（以 CC 之碼之字樣為錨之接線與突變之判別力 ＝ 復驗時補寫·另單。）
           🔧 `W-G.9-370`：W6 許 `k953_manual_run` 之 `S219` 之停機訊息之基準二列（`W6_REPL`·逐字）易之（`K-9-57` ⑧·
           程式自我檢查），唯此二列；其新文由 F25 之 `X5` 量之。W7 之錨之母體⛔ 含 F25（`W7_SKIP`）：其突變之錨為函式之段內
           之錨（其恰一之判於其函式之段內·F25 之 `mutate` 自量之），⛔ 為全檔之錨。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：同一行程先設 `WV_ADJ4=off`、再去之，各跑一次：R1 第一趟之紀錄逐列 ＝
           本器所載；R2 街角第 1 宗 ＝ off 之實跑；R3 配地之變（G 之差 ＞ 容差 `0.01` 之宗、各街廓之抵費地之差）＝ 本器所載，
           且 Σ抵費地之減 ＝ ΣG 之增（容差 `0.1`）；R4 調配之輸入之類（切片數·原有面積）與合併單位數 ＝ 本器所載；
           R5 受詞之片之段三之三鍵 ＝ 本器所載。
  offsnap  <repo> <out.json> [<退縮> …]
           於行程內設 `WV_ADJ4=off`，harness 實跑本案，以 sha256 摘要其街角、宗地（暫編地號·段三之三鍵·面積二欄）、build、
           段三紀錄、末端塊紀錄、手冊先行之紀錄、配地列、入池閘紀錄、不配地紀錄、調配之輸入，寫 out。
  offcmp   <a.json> <b.json>
           二 offsnap 之摘要逐項同（第一趟之紀錄唯出艙·⛔ 入判）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, difflib, io, os, re, subprocess, sys, warnings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

TOL = 0.01
FN = "adj4_pass1_run"
SELF_NAME = "probe_WG9367_adj4.py"
REMAIN = "留於合併單位（規格步 5）"


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__, str(ex)[:160])
    out.append((name, got, exp))


# ── 玩具（⛔ 本案資料）──
H, RDC, PKC = "住宅區", "道路", "鄰里公園"
TB, TP = "建地軌", "公設軌"


def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a, lot=None):
    return {"暫編地號": pid, "原地號": lot or pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


def _a(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, lose=None, calls=None, tie=None, bar=None):
    """玩具之回呼（`calls` ＝ list ⇒ 每次試算附一筆）。"""
    cap, price, gmap, err_cap, lose = cap or {}, price or {}, gmap or {}, err_cap or {}, lose or {}
    tie, bar = tie or {}, bar or {}

    def a_prime(src, dst):
        return _a(src) * price.get(src["所屬街廓"], 1.0) / price.get(dst["所屬街廓"], 1.0)

    def alloc_state(temp, build):
        if calls is not None:
            calls.append(1)
        acc = {}
        for b in build:
            acc[b["所屬街廓"]] = acc.get(b["所屬街廓"], 0.0) + float(b.get("面積_m2", 0) or 0)
        for blk, v in acc.items():
            if v > err_cap.get(blk, 1e18) + 1e-9:
                return {"kept": {}, "bad_pools": {}, "err": f"玩具之配地中止（{blk}）", "G": {}, "members": {},
                        "units": {}}
        gone = set(drop)
        by = {b["暫編地號"]: b for b in build}
        for h, (thr, lost) in lose.items():
            if h in by and float(by[h].get("面積_m2", 0) or 0) > thr + 1e-9:
                gone.add(lost)
        for p, lost in tie.items():                 # 🆕 `W-G.9-370`：該片離 build ⇒ 失者不保留
            if p not in by:
                gone.add(lost)
        for p, lost in bar.items():                 # 🆕 `W-G.9-370`：該片在 build ⇒ 受阻者不保留
            if p in by:
                gone.add(lost)
        kept, bad, G, mem = {}, {}, {}, {}
        for b in build:
            p = b["暫編地號"]
            if p in gone:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(p)
            G[p] = gmap.get(p, _a(b))
            mem[p] = [p]
        for blk, v in acc.items():
            if v > cap.get(blk, 1e18) + 1e-9:
                bad[blk] = 1
        return {"kept": kept, "bad_pools": bad, "err": None, "G": G, "members": mem, "units": {}}
    return a_prime, alloc_state


def _w():
    """世界：BA x∈[0,20]、BB x∈[20,40]、BD x∈[40,60]（y∈[0,30]·住宅區）；道路 RD（y∈[-10,0]）；公園 PK（y∈[30,50]·
    x∈[0,20]）。歸戶 g1：X1(1)（BA·分不到之建地）、X1(2)／W1(1)（BB·已配得）、Z1(1)（BD·已配得）、R1(1)（道路片）、
    P1(1)（公設片）。"""
    t = [_tp("Q1(1)", "BA", H, _R(0, 10, 0, 30), 300), _tp("X1(1)", "BA", H, _R(10, 20, 0, 30), 60),
         _tp("X1(2)", "BB", H, _R(20, 30, 0, 30), 300), _tp("W1(1)", "BB", H, _R(30, 40, 0, 30), 200),
         _tp("Z1(1)", "BD", H, _R(40, 50, 0, 30), 400), _tp("Q2(1)", "BD", H, _R(50, 60, 0, 30), 300),
         _tp("R9(1)", "RD", RDC, _R(0, 20, -10, 0), 200), _tp("R1(1)", "RD", RDC, _R(20, 30, -10, 0), 100),
         _tp("R8(1)", "RD", RDC, _R(30, 60, -10, 0), 300),
         _tp("P1(1)", "PK", PKC, _R(0, 10, 30, 50), 200), _tp("P9(1)", "PK", PKC, _R(10, 20, 30, 50), 200)]
    own = {"Q1": "gQ", "X1": "g1", "W1": "g1", "Z1": "g1", "Q2": "gQ2", "R9": "gR", "R1": "g1", "R8": "gR8",
           "P1": "g1", "P9": "gP", "V1": "g1"}
    return t, own


SJ = {"歸戶": "g1", "軌": TB, "錨點": "P1(1)", "名單": ["BA", "BB", "BD"], "片": ["X1(1)", "R1(1)", "P1(1)"],
      "原有面積合計": 360.0}
_NS = {}


def _go(*, sj=None, cap=None, price=None, drop=("X1(1)",), gmap=None, err_cap=None, lose=None, own_upd=None,
        pre=None, lot_upd=None, temp_geom=None, geom_extra=None, geom_rm=(), calls=None, raw=False, tie=None, bar=None):
    t, own = _w()
    own = dict(own, **(own_upd or {}))
    by = {x["暫編地號"]: x for x in t}
    geom = {x["暫編地號"]: [list(c) for c in x["polygon_coords"]] for x in t}
    for pid, poly in (geom_extra or {}).items():
        geom[pid] = [list(c) for c in poly]
    for pid in geom_rm:
        geom.pop(pid, None)
    for pid, lot in (lot_upd or {}).items():
        by[pid]["原地號"] = lot
    for pid, poly in (temp_geom or {}).items():
        by[pid]["polygon_coords"] = [list(c) for c in poly]
    for pid, kv in (pre or {}).items():
        by[pid].update(copy.deepcopy(kv))
    build = [x for x in t if x["街廓分類"] == H]
    ap, st = _cbs(cap, price, drop, gmap, err_cap, lose, calls, tie, bar)
    subj = [dict(SJ, **(sj or {}))] if sj is not False else []
    res = _NS["fn"](t, build, own, subj, geom, ap, st, log_print=lambda *x: None)
    return (res, t, build) if raw else res


def _rows(res):
    out = []
    for r in res[2]:
        q = tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items()))
        if r.get("序") == "剩下":
            out.append(("剩下", r.get("歸戶"), r.get("片"), r.get("結果"),
                        tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("餘量") or {}).items()))))
        else:
            out.append((r.get("序"), r.get("歸戶"), r.get("街廓"), r.get("片"), r.get("類"), r.get("受併宗"), q,
                        r.get("結果")))
    return out


def _keys(res):
    out = {}
    for x in res[0]:
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


def _acc(res):
    return {x["暫編地號"]: round(float(x.get("面積_m2", 0) or 0), 2) for x in res[0]
            if float(x.get("面積_m2", 0) or 0)}


def _bids(res):
    return [b["暫編地號"] for b in res[1]]


def _halt(fn, phrases):
    try:
        fn()
    except RuntimeError as e:
        return ("停機", all(p in str(e) for p in phrases))
    return ("無停機",)


class _FakeSt:
    """畫面之假 st：`session_state` ＝ dict；方法之呼叫依序記其名。"""

    def __init__(self):
        self.session_state = {}
        self.calls = []

    def error(self, *a, **k):
        self.calls.append("error")

    def stop(self):
        self.calls.append("stop")

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError(name)

        def _f(*a, **k):
            self.calls.append(name)
            return contextlib.nullcontext()
        return _f


ENVS = ("WV_ADJ4", "WV_K953", "WV_K929_6")


def _setenv(vals):
    for k, v in zip(ENVS, vals):
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v


# 手冊先行之世界（同 F23 之世界一·⛔ 讀 F23）——GB-201 之例
def _wk():
    t = [_tp("X1(1)", "BA", H, _R(10, 20, 0, 30), 60), _tp("X1(2)", "BB", H, _R(20, 30, 0, 30), 300),
         _tp("Y1(1)", "BB", H, _R(30, 40, 0, 30), 200), _tp("Z1(1)", "BD", H, _R(40, 50, 0, 30), 400),
         _tp("Q1(1)", "BA", H, _R(0, 10, 0, 30), 300), _tp("Q2(1)", "BD", H, _R(50, 60, 0, 30), 300),
         _tp("R1(1)", "RD", RDC, _R(20, 30, -10, 0), 100), _tp("R9(1)", "RD", RDC, _R(0, 20, -10, 0), 200),
         _tp("R8(1)", "RD", RDC, _R(30, 60, -10, 0), 300),
         _tp("C1(1)", "BC", H, _R(20, 30, -40, -10), 300), _tp("C9(1)", "BC", H, _R(0, 20, -40, -10), 300),
         _tp("C8(1)", "BC", H, _R(30, 60, -40, -10), 300),
         _tp("P1(1)", "PK", PKC, _R(20, 30, 30, 50), 200), _tp("P9(1)", "PK", PKC, _R(30, 40, 30, 50), 200)]
    own = {"X1": "g1", "Y1": "gY", "Z1": "gZ", "Q1": "gQ", "Q2": "gQ2", "R1": "g1", "R9": "gR", "R8": "gR8",
           "C1": "g1", "C9": "gC", "C8": "gC8", "P1": "g1", "P9": "gP"}
    blocks = {"BA": {"category": H}, "BB": {"category": H}, "BD": {"category": H}, "RD": {"category": RDC},
              "BC": {"category": H}, "PK": {"category": PKC}}
    return t, own, blocks, {"RD": [(-10.0, -5.0), (70.0, -5.0)]}


def _k15(ns):
    """GB-201：手冊先行中，X1(1) 之整筆併入 X1(2)（其檢核之街廓唯 BA／BB）使他街廓之某宗不保留；其後以該宗為計畫之
    受併宗之併入 ⇒ 停機（⛔ 以已失保留之宗為受併宗而靜默併入）。甲 ＝ 可拆分之片（道路片 R1(1) 之計畫含 C1(1)）；
    乙 ＝ 整筆之建地片（BE 之 X1(3) 之計畫 ＝ BD 之 Q2(1)〔同歸戶〕）。"""
    def go(lost, extra, own_upd, blk_upd, drop):
        t, own, blocks, cl = _wk()
        t += extra
        own = dict(own, **own_upd)
        blocks = dict(blocks, **blk_upd)
        build = [x for x in t if x["街廓分類"] == H]
        ap, st0 = _cbs(None, None, drop)

        def st(temp, b):
            r = st0(temp, b)
            x2 = next((x for x in temp if x["暫編地號"] == "X1(2)"), None)
            if x2 is not None and float(x2.get("面積_m2", 0) or 0) > 0:
                r["kept"] = {k: set(v) - {lost} for k, v in r["kept"].items()}
            return r
        return ns["k953_manual_run"](t, build, own, blocks, cl, ap, st, log_print=lambda *x: None)
    a = _halt(lambda: go("C1(1)", [], {}, {}, ("X1(1)",)), ["GB-201", "C1(1)", "R1(1)"])
    b = _halt(lambda: go("Q2(1)", [_tp("X1(3)", "BE", H, _R(60, 70, 0, 30), 50)], {"Q2": "g1"}, {"BE": {"category": H}},
                         ("X1(1)", "X1(3)")), ["GB-201", "Q2(1)", "X1(3)"])
    return a, b


def _k11(ns):
    def u(g, track, area, blks, inb, com):
        return {"歸戶": g, "軌": track, "原有面積合計": area, "同歸戶原位次配地之街廓": blks,
                "建築街廓內不能分配": [{"暫編地號": x} for x in inb], "共同負擔用地": [{"暫編地號": x} for x in com]}
    units = [u("gA", TP, 500.0, ["B1"], [], ["a(1)", "a(2)"]), u("gB", TB, 100.0, ["B2"], ["b(1)"], ["b(2)", "b(1)"]),
             u("gC", TB, 300.0, [], ["c(1)"], []), u("gD", TB, 100.0, ["B3"], ["d(1)"], [])]
    lists = [{"歸戶": g, "錨點": f"{g[1].lower()}(1)", "名單": [{"街廓": "B2"}, {"街廓": "B1"}]} for g in ("gA", "gB", "gC", "gD")]
    it = {"units": units}
    su = [x["歸戶"] for x in ns["adj4_subject_units"](it)]
    sj = ns["adj4_subjects"](it, lists)
    view = [(s["歸戶"], s["軌"], s["錨點"], tuple(s["名單"]), tuple(s["片"]), s["原有面積合計"]) for s in sj]
    miss = _halt(lambda: ns["adj4_subjects"](it, [x for x in lists if x["歸戶"] != "gD"]), ["gD", "無候選街廓名單"])
    dup = _halt(lambda: ns["adj4_subjects"](it, lists + [lists[0]]), ["gA", "名單重複"])
    return su, view, miss, dup


def _k18(ns):
    """adj4_plan：無受詞 ⇒ []（⛔ 求名單）；公設軌之受詞而無正面道路 ⇒ 以佔位代之、名單依距離；建地軌 ⇒ 停機。"""
    sq = lambda x0, y0: [[x0, y0], [x0 + 10, y0], [x0 + 10, y0 + 10], [x0, y0 + 10]]  # noqa: E731
    cb = [{"label": "B1", "category": H, "id": "i1"}, {"label": "B2", "category": H, "id": "i2"},
          {"label": "RD", "category": RDC, "id": "i3"}]
    g_rows = [{"所屬街廓": "B1", "推進側別": "抵費地", "暫編地號": "p1", "cut_coords": sq(0, 0)},
              {"所屬街廓": "B2", "推進側別": "抵費地", "暫編地號": "p2", "cut_coords": sq(100, 0)}]
    temp = [{"暫編地號": "r(1)", "polygon_coords": sq(80, 0)}]

    def it(track, home):
        return {"units": [{"歸戶": "g1", "軌": track, "原街廓": home, "原有面積合計": 100.0, "同歸戶原位次配地之街廓": ["B1"],
                           "建築街廓內不能分配": [], "共同負擔用地": [{"暫編地號": "r(1)", "原有面積": 100.0}]}]}
    empty = ns["adj4_plan"]({"units": [dict(it(TP, None)["units"][0], 同歸戶原位次配地之街廓=[])]},
                            None, None, None, None, None, None, None, None)
    args = (temp, g_rows, cb, {}, {}, {}, {"B1": 8.0, "B2": 8.0}, {"B1": 20.0, "B2": 20.0})
    pub = ns["adj4_plan"](it(TP, None), *args)
    pubv = [(s["歸戶"], s["軌"], s["錨點"], tuple(s["名單"]), tuple(s["片"])) for s in pub]
    bld = _halt(lambda: ns["adj4_plan"](it(TB, "B1"), *args), ["正面道路無識別符"])
    return empty, pubv, bld


def _k16(ns, sp):
    """三旗標之任一 off ⇒ harness 與畫面皆回輸入之同一物件、紀錄 []、⛔ 呼叫 st。"""
    keep = tuple(os.environ.get(k) for k in ENVS)
    t, _own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    out = []
    try:
        for vals in (("off", None, None), (None, "off", None), (None, None, "off")):
            _setenv(vals)
            fst = _FakeSt()
            fst.session_state["f3_adj4_log"] = ["舊"]
            r = sp.run_adj4(ns, fst, None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None,
                            forced=None, slices=None)
            st = _FakeSt()
            st.session_state["f3_adj4_log"] = ["舊"]
            rr = ns["f3_screen_adj4"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={}, slices=None)
            out.append((r[0] is t, r[1] is b, fst.session_state.get("f3_adj4_log"),
                        rr["temp"] is t, rr["build"] is b, rr["log"], st.session_state.get("f3_adj4_log"), st.calls))
    finally:
        _setenv(keep)
    return tuple(out)


def _k17(ns, sp):
    """三旗標之任一其值非法 ⇒ harness 上拋；畫面走停機之路（`f3_k6b_stage3_error`·`st.error`·`st.stop`）。"""
    keep = tuple(os.environ.get(k) for k in ENVS)
    t, _own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    out = []
    try:
        for vals in (("maybe", None, None), (None, "maybe", None), (None, None, "maybe")):
            _setenv(vals)
            try:
                sp.run_adj4(ns, _FakeSt(), None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None,
                            forced=None, slices=None)
                h1 = "無停機"
            except RuntimeError:
                h1 = "停機"
            st = _FakeSt()
            st.session_state["f3_k6b_stage3_error"] = "前之標記"
            try:
                ns["f3_screen_adj4"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={}, slices=None)
                h2 = "無停機"
            except RuntimeError:
                h2 = "停機"
            except Exception as e:  # noqa: BLE001
                h2 = type(e).__name__
            out.append((h1, h2, st.calls, str(st.session_state.get("f3_k6b_stage3_error", "")).startswith("（第一趟）"),
                        "f3_adj4_log" in st.session_state))
    finally:
        _setenv(keep)
    return tuple(out)


def _k21(ns):
    """adj4_possible（先篩·純函式）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True。"""
    t, own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    f = ns["adj4_possible"]
    tg = copy.deepcopy(t)
    for x in tg:
        if x["暫編地號"] == "R9(1)":
            x["_is_ghost_sliver"] = True
    bg = [x for x in tg if x["街廓分類"] == H]
    return (f(t, b, own), f(t, b, {}), f(t, b, None), f(t, b, {"Q1": "gQ"}), f(t, b, {"Q1": "gQ", "R9": "gQ"}),
            f(tg, bg, {"Q1": "gQ", "R9": "gQ"}), f(t, b, {"R9": "gR", "P9": "gR"}))


def _k22(ns, sp):
    """三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st。"""
    keep = tuple(os.environ.get(k) for k in ENVS)
    t, _own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    try:
        _setenv((None, None, None))
        fst = _FakeSt()
        fst.session_state.update({"f3_adj4_log": ["舊"], "t8_ownership_map": {}})
        r = sp.run_adj4(ns, fst, None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None,
                        forced=None, slices=None)
        st = _FakeSt()
        st.session_state.update({"f3_adj4_log": ["舊"], "t8_ownership_map": {}})
        rr = ns["f3_screen_adj4"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={}, slices=None)
        return (r[0] is t, r[1] is b, fst.session_state.get("f3_adj4_log"), rr["temp"] is t, rr["build"] is b,
                rr["log"], st.session_state.get("f3_adj4_log"), st.calls)
    finally:
        _setenv(keep)


def _k1(ns):
    keep = os.environ.get("WV_ADJ4")
    out = []
    try:
        for v in (None, "", " On ", "off", "OFF", "maybe"):
            if v is None:
                os.environ.pop("WV_ADJ4", None)
            else:
                os.environ["WV_ADJ4"] = v
            try:
                out.append(ns["adj4_enabled"]())
            except RuntimeError:
                out.append("停機")
    finally:
        if keep is None:
            os.environ.pop("WV_ADJ4", None)
        else:
            os.environ["WV_ADJ4"] = keep
    return tuple(out)


def _k2():
    calls = []
    res, t, b = _go(sj=False, calls=calls, raw=True)
    t2, b2 = copy.deepcopy(t), [x for x in t if x["街廓分類"] == H]
    bad = _halt(lambda: _NS["fn"](t2[:-1], b2 + [t2[-1]], {}, [], {}, None, None), ["非 temp_parcels 之片"])
    return (res[0] is t, res[1] is b, res[2], len(calls), bad)


def _k3():
    res, t, b = _go(raw=True)
    t2, b2 = res[0], res[1]
    ids = {id(x) for x in t2}
    untouched = all(float(x.get("面積_m2", 0) or 0) == 0 and "段三併出" not in x for x in t)
    return (_rows(res), _keys(res), _acc(res), _bids(res), all(id(x) in ids for x in b2), untouched, len(b))


B_ALL = ["Q1(1)", "X1(1)", "X1(2)", "W1(1)", "Z1(1)", "Q2(1)"]
B_NOX = ["Q1(1)", "X1(2)", "W1(1)", "Z1(1)", "Q2(1)"]


def _first_recv(**kw):
    return _rows(_go(sj={"名單": ["BB"], **kw.pop("sj", {})}, **kw))[0][5]


def _cases(ns, sp):
    out = []
    _NS["fn"] = ns[FN]
    _run(out, "K1 旗標：未設／空／' On ' ⇒ True；off／OFF ⇒ False；他值 ⇒ 停機", lambda: _k1(ns),
         (True, True, True, False, False, "停機"))
    _run(out, "K2 無受詞 ⇒ 回輸入之同一物件、紀錄 []、⛔ 試算；build 片不在 temp ⇒ 停機（受詞為空亦然）", _k2,
         (True, True, [], 0, ("停機", True)))
    _run(out, "K3 整體成：名單首 BA 無其已配得之宗 ⇒ 略過；BB 之受併宗 X1(2)（同原地號）；三片皆併、建地片自 build 去、"
              "輸入⛔ 改、build ⊆ temp（同物件）", _k3,
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (("X1(2)", 360.0),), "成")],
          {"P1(1)": {"段三併出": ("X1(2)",)}, "R1(1)": {"段三併出": ("X1(2)",)}, "X1(1)": {"段三併出": ("X1(2)",)}},
          {"X1(2)": 360.0}, B_NOX, True, True, 6))
    r4 = lambda: _go(cap={"BB": 150.0})  # noqa: E731
    _run(out, "K4 整體不過（BB 之容量 150）⇒ 逐片：建地整筆成、道路片取最大面積（0.01 之格）、公設片未成；剩下續往名單之"
              "下一街廓 BD（整體成·受併宗 Z1(1)）", lambda: (_rows(r4()), _keys(r4()), _acc(r4()), _bids(r4())),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 90.0),), "部分成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (), "未成"),
           ("整體", "g1", "BD", "2 片", "—", "Z1(1)", (("Z1(1)", 210.0),), "成")],
          {"P1(1)": {"段三併出": ("Z1(1)",)}, "R1(1)": {"段三併出": ("X1(2)", "Z1(1)")},
           "X1(1)": {"段三併出": ("X1(2)",)}},
          {"X1(2)": 150.0, "Z1(1)": 210.0}, B_NOX))
    _run(out, "K4b 整體不過之列記其由（配餘地不合格）", lambda: r4()[2][0].get("不過之由"), "BB 配餘地不合格")
    r5 = lambda: _go(cap={"BB": 150.0}, sj={"名單": ["BA", "BB"]})  # noqa: E731
    _run(out, "K5 名單盡而有剩下 ⇒ 剩下之列（留於合併單位）；部分併出者之三鍵（段三部分併出·段三餘量）",
         lambda: (_rows(r5())[-1], _keys(r5())),
         (("剩下", "g1", "P1(1)、R1(1)", REMAIN, (("P1(1)", 200.0), ("R1(1)", 10.0))),
          {"R1(1)": {"段三併出": ("X1(2)",), "段三部分併出": (("X1(2)", 90.0),), "段三餘量": 10.0},
           "X1(1)": {"段三併出": ("X1(2)",)}}))
    r6 = lambda: _go(cap={"BB": 0.0, "BD": 0.0})  # noqa: E731
    _run(out, "K6 全不容 ⇒ 每街廓整體＋三逐片皆未成、剩下 ＝ 全部；⛔ 改宗地（建地片仍在 build·無鍵·無增）",
         lambda: (len(_rows(r6())), [r[-1] for r in _rows(r6())[:-1]], _rows(r6())[-1], _keys(r6()), _acc(r6()),
                  _bids(r6())),
         (9, ["未成"] * 8, ("剩下", "g1", "P1(1)、R1(1)、X1(1)", REMAIN,
                            (("P1(1)", 200.0), ("R1(1)", 100.0), ("X1(1)", 60.0))), {}, {}, B_ALL))
    sq = {"A0(1)": _R(25, 35, 40, 50)}
    _run(out, "K7 受併宗之序（同街廓有二宗）：① 同原地號居先（距離較遠亦然）② 距離近 ③ 同距離 ⇒ G 大 ④ 同 G ⇒ 暫編地號小",
         lambda: (_first_recv(sj={"錨點": "Q2(1)"}),
                  _first_recv(sj={"錨點": "Q2(1)"}, lot_upd={"X1(2)": "V1"}),
                  _first_recv(sj={"錨點": "A0(1)"}, lot_upd={"X1(2)": "V1"}, geom_extra=sq),
                  _first_recv(sj={"錨點": "A0(1)"}, lot_upd={"X1(2)": "V1"}, geom_extra=sq,
                              gmap={"X1(2)": 250.0, "W1(1)": 250.0})),
         ("X1(2)", "W1(1)", "X1(2)", "W1(1)"))
    sr = {"軌": TP, "錨點": "R1(1)", "名單": ["BB"], "片": ["R1(1)"], "原有面積合計": 100.0}
    pre = {"R1(1)": {"段三併出": ["Q9(1)"], "段三部分併出": {"Q9(1)": 40.0}, "段三餘量": 60.0}}
    _run(out, "K8 前已有段三之三鍵之片：其剩下 ＝ 段三餘量；全併 ⇒ 段三併出合之、去部分二鍵；部分 ⇒ 段三部分併出合之、"
              "段三餘量 ＝ 新剩下",
         lambda: (_rows(_go(sj=sr, pre=pre)), _keys(_go(sj=sr, pre=pre)), _rows(_go(sj=sr, pre=pre, cap={"BB": 50.0})),
                  _keys(_go(sj=sr, pre=pre, cap={"BB": 50.0}))),
         ([("整體", "g1", "BB", "1 片", "—", "X1(2)", (("X1(2)", 60.0),), "成")],
          {"R1(1)": {"段三併出": ("Q9(1)", "X1(2)")}},
          [("整體", "g1", "BB", "1 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 50.0),), "部分成"),
           ("剩下", "g1", "R1(1)", REMAIN, (("R1(1)", 10.0),))],
          {"R1(1)": {"段三併出": ("Q9(1)", "X1(2)"), "段三部分併出": (("Q9(1)", 40.0), ("X1(2)", 50.0)),
                     "段三餘量": 10.0}}))
    _run(out, "K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（程式自我檢查·K-9-57 ⑧·`W-G.9-370` 之訊息）",
         lambda: _halt(lambda: _go(drop=()), ["X1(1)", "程式自我檢查", "沿名單至街廓 BA", "依既定機制不會發生",
                                              "觸之即程式有錯"]), ("停機", True))
    _run(out, "K10 現態之配地中止 ⇒ 停機", lambda: _halt(lambda: _go(err_cap={"BB": -1.0}), ["現態之配地中止"]),
         ("停機", True))
    _run(out, "K11 受詞：同歸戶原位次配地之街廓非空者；序 ＝ (建地軌先, 原有面積大, 歸戶)；片 ＝ 建築街廓內不能分配 ＋ "
              "共同負擔用地（相異）；無名單 ⇒ 停機；名單重複 ⇒ 停機", lambda: _k11(ns),
         (["gA", "gB", "gD"],
          [("gB", TB, "b(1)", ("B2", "B1"), ("b(1)", "b(2)"), 100.0), ("gD", TB, "d(1)", ("B2", "B1"), ("d(1)",), 100.0),
           ("gA", TP, "a(1)", ("B2", "B1"), ("a(1)", "a(2)"), 500.0)],
          ("停機", True), ("停機", True)))
    far = {"W1(1)": _R(1000, 1010, 0, 30)}
    _run(out, "K12 GB-199：受併宗之序之距離取 slice_geom 之原形（temp 之形縱異亦然）；片之原形缺 ⇒ 停機",
         lambda: (_first_recv(sj={"錨點": "Q2(1)"}, lot_upd={"X1(2)": "V1"}, temp_geom=far),
                  _halt(lambda: _go(geom_rm=("R1(1)",)), ["R1(1)", "原形缺"])),
         ("W1(1)", ("停機", True)))
    pr = {"BB": 2.0}
    r13 = lambda: _go(price=pr, cap={"BB": 100.0}, sj={"名單": ["BA", "BB"]})  # noqa: E731
    _run(out, "K13 a′ 折算（K-9-45 二）：併入量 ＝ 來源面積 × p(來源) ÷ p(受併宗)；最大面積之格取來源面積；三鍵之部分併出記"
              "來源面積",
         lambda: (_rows(_go(price=pr, sj={"名單": ["BB"]})), _acc(_go(price=pr, sj={"名單": ["BB"]})), _rows(r13()),
                  _keys(r13())),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (("X1(2)", 180.0),), "成")], {"X1(2)": 180.0},
          [("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 30.0),), "成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 50.0),), "成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 20.0),), "部分成"),
           ("剩下", "g1", "P1(1)", REMAIN, (("P1(1)", 160.0),))],
          {"P1(1)": {"段三併出": ("X1(2)",), "段三部分併出": (("X1(2)", 40.0),), "段三餘量": 160.0},
           "R1(1)": {"段三併出": ("X1(2)",)}, "X1(1)": {"段三併出": ("X1(2)",)}}))
    r14 = lambda: _go(lose={"X1(2)": (50.0, "W1(1)")}, sj={"名單": ["BA", "BB"]})  # noqa: E731
    _run(out, "K14 「不影響原位次」：併入使同街廓原保留之宗不保留 ⇒ 不過（整體與逐片皆然）",
         lambda: (_rows(r14()), r14()[2][0].get("不過之由")),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 50.0),), "部分成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (), "未成"),
           ("剩下", "g1", "P1(1)、R1(1)、X1(1)", REMAIN, (("P1(1)", 200.0), ("R1(1)", 50.0), ("X1(1)", 60.0)))],
          "BB 原保留之宗 ['W1(1)'] 不保留"))
    _run(out, "K15 GB-201（手冊先行）：計畫之受併宗於當下之試算未保留 ⇒ 停機（可拆分之片／整筆之建地片）", lambda: _k15(ns),
         (("停機", True), ("停機", True)))
    no_call = ((True, True, [], True, True, [], [], []),) * 3
    _run(out, "K16 三旗標（WV_ADJ4／WV_K953／WV_K929_6）之任一 off ⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 呼叫 st",
         lambda: _k16(ns, sp), no_call)
    _run(out, "K17 三旗標之任一其值非法 ⇒ harness 停機；畫面 ⇒ f3_k6b_stage3_error ＝ （第一趟）…、st.error、st.stop、"
              "⛔ 寫紀錄", lambda: _k17(ns, sp), (("停機", "停機", ["error", "stop"], True, False),) * 3)
    _run(out, "K18 adj4_plan：無受詞 ⇒ []；唯公設軌 ⇒ 正面道路之缺以佔位代之、名單依距離；建地軌 ⇒ 停機（正面道路無識別符）",
         lambda: _k18(ns), ([], [("g1", TP, "r(1)", ("B2", "B1"), ("r(1)",))], ("停機", True)))
    _run(out, "K19 adj4_depth_of：取 f3_alloc_depth_by_label（缺 ⇒ {}）；回新 dict",
         lambda: (ns["adj4_depth_of"]({"f3_alloc_depth_by_label": {"B1": 20.0}}), ns["adj4_depth_of"]({}),
                  ns["adj4_depth_of"](None)), ({"B1": 20.0}, {}, {}))
    bu = [{"暫編地號": "u(1)", "入池閘併入": ["u(1)", "u(2)"]}, {"暫編地號": "v(1)"}]
    _run(out, "K20 adj4_trial_state：摘要 ＋ err ＋ 成員與單元（成員 ≥ 2 者為單元·深拷貝）",
         lambda: (lambda r: (sorted(r), r["kept"], r["err"], r["members"], sorted(r["units"]),
                             r["units"]["u(1)"] is not bu[0]))(
             ns["adj4_trial_state"]({"kept": {"B1": {"u(1)"}}, "bad_pools": {}, "G": {"u(1)": 1.0}}, None, bu)),
         (["G", "bad_pools", "err", "kept", "members", "units"], {"B1": {"u(1)"}}, None,
          {"u(1)": ["u(1)", "u(2)"], "v(1)": ["v(1)"]}, ["u(1)"], True))
    _run(out, "K21 adj4_possible（先篩）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True",
         lambda: _k21(ns), (True, False, False, False, True, False, False))
    _run(out, "K22 三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st",
         lambda: _k22(ns, sp), (True, True, [], True, True, [], [], []))
    # ── 🆕 `W-G.9-370`（`W-G.9-367 §四-2`·以 CC 之碼之突變之判別力為據·期值出自規格單 `§三`·⛔ 呼叫受測碼求期）──
    r23 = lambda: _go(lose={"X1(2)": (150.0, "Q1(1)")}, sj={"名單": ["BB", "BD"]})  # noqa: E731
    _run(out, "K23 R-8 之止：整體不過（他街廓之原保留之宗失·非單調之玩具）而逐片皆成 ⇒ 諸片皆無剩下 ⇒ 止於本街廓"
              "（⛔ 往名單之次街廓 BD）",
         lambda: (_rows(r23()), _acc(r23())),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 100.0),), "成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 200.0),), "成")],
          {"X1(2)": 360.0}))
    r24 = lambda: _go(tie={"X1(1)": "Q1(1)"}, sj={"名單": ["BB"]})  # noqa: E731
    _run(out, "K24 R-9／R-10 之 T 含建地片之所屬街廓：建地片去 build 使其所屬街廓 BA 之原保留之宗失 ⇒ 整體與該片之逐片"
              "皆不過",
         lambda: (_rows(r24()), r24()[2][0].get("不過之由"), r24()[2][1].get("不過之由")),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 100.0),), "成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 200.0),), "成"),
           ("剩下", "g1", "X1(1)", REMAIN, (("X1(1)", 60.0),))],
          "BA 原保留之宗 ['Q1(1)'] 不保留", "BA 原保留之宗 ['Q1(1)'] 不保留"))
    s25 = {"名單": ["BB"], "片": ["X1(1)", "R1(1)", "R9(1)"]}
    r25 = lambda: _go(own_upd={"R9": "g1"}, cap={"BB": 250.0}, sj=s25)  # noqa: E731
    _run(out, "K25 R-10 之序：同類之片依剩下大者先（R9(1) 200 先於 R1(1) 100）",
         lambda: _rows(r25()),
         [("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
          ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
          ("逐片", "g1", "BB", "R9(1)", "道路", "X1(2)", (("X1(2)", 190.0),), "部分成"),
          ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (), "未成"),
          ("剩下", "g1", "R1(1)、R9(1)", REMAIN, (("R1(1)", 100.0), ("R9(1)", 10.0)))])
    r26 = lambda: _go(err_cap={"BB": 200.0}, sj={"名單": ["BB"]})  # noqa: E731
    _run(out, "K26 R-12：併入後之配地中止 ⇒ 不過（記其由）；整體不過 ⇒ 逐片（公設片取最大面積）",
         lambda: (_rows(r26()), r26()[2][0].get("不過之由")),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 100.0),), "成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 40.0),), "部分成"),
           ("剩下", "g1", "P1(1)", REMAIN, (("P1(1)", 160.0),))],
          "併入後配地中止：玩具之配地中止（BB）"))
    s27 = {"名單": ["BB"], "片": ["Q1(1)", "X1(1)", "R1(1)"]}
    _run(out, "K27 R-10′（K-9-57 ⑧·程式自我檢查）：逐片之建地片之整筆之試之前，以當下之試算查之——前一建地片併出後該片已"
              "為已配得之宗（依既定機制不會發生·玩具以非單調之回呼造之）⇒ 停機（⛔ 靜默併出）",
         lambda: _halt(lambda: _go(drop=("Q1(1)",), bar={"Q1(1)": "X1(1)"}, own_upd={"Q1": "g1"}, cap={"BB": 360.0},
                                   sj=s27), ["X1(1)", "程式自我檢查", "逐片之整筆之試之前", "依既定機制不會發生",
                                             "觸之即程式有錯"]),
         ("停機", True))
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


def _need(ns, sp):
    names = (FN, "adj4_enabled", "adj4_possible", "adj4_subject_units", "adj4_subjects", "adj4_plan", "adj4_depth_of",
             "adj4_trial_state",
             "f3_screen_adj4",
             "k953_manual_run", "k953_enabled", "k929_6_enabled")
    return [n for n in names if n not in ns] + ([] if hasattr(sp, "run_adj4") else ["run_adj4"])


def selftest(repo):
    ns, _ = _harvest(repo)
    import selection_pipeline as sp
    need = _need(ns, sp)
    if need:
        print(f"  🔴 受詞缺：{need}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    cases = _cases(ns, sp)
    print("── 規格步 4 乙（K-9-53 ②·第一趟）之各支 ──")
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
SIG = ["temp_parcels", "build_parcels", "own_map", "subjects", "slice_geom", "a_prime", "alloc_state"]
NEW_APP = {"adj4_enabled": [], "adj4_possible": ["temp_parcels", "build_parcels", "own_map"],
           "adj4_subject_units": ["intake"], "adj4_subjects": ["intake", "cand_lists"],
           "adj4_depth_of": ["session"], "adj4_trial_state": ["summary", "err", "build_used"],
           "adj4_plan": ["intake", "temp_parcels", "g_rows", "classified_blocks", "eff_min_build_by",
                         "front_derive_by", "front_name_by", "width_by", "depth_by"],
           FN: SIG, "f3_screen_adj4": ["st"]}
NEW_CONST = ("ADJ4_ENV", "ADJ4_IDENT_UNUSED")
CHG_APP = ("k953_manual_run", "f3_screen_k6b_stage3")
RA_SIG = ["ns", "fake_st", "cb", "cad", "param_rows", "temp_parcels", "build_parcels", "setback"]
RA_KW = ["snapshot", "callbacks", "winners", "forced", "slices"]
CHG_SP = ("run_corner_pk_k6b",)
# 🆕 `W-G.9-370`：W7 之錨之母體⛔ 含 F25（突變器·其錨為函式之段內之錨·由其 `mutate` 自量之）
W7_SKIP = ("probe_WG9370_adj4mut.py",)
# 🆕 `W-G.9-370`（K-9-57 ⑧）：W6 之許——`k953_manual_run` 之 `S219` 之停機訊息之基準二列（逐字）得易之（唯此二列）
W6_REPL = {"k953_manual_run": (
    '            raise RuntimeError(f"{_hdr953} 建地片 {_x}（{_blk953[_x]}）於當下之試算已為已配得之宗 {_own953}"',
    '                               "或其成員——K-9-53 ① 之「分不到」不立、K-9-51 之「剩餘土地」不立 ⇒ 停機")')}


def _git_show(repo, rev, rel):
    return subprocess.run(["git", "-C", repo, "show", f"{rev}:{rel}"], capture_output=True,
                          check=True).stdout.decode("utf-8")


def _defs(src):
    tree = ast.parse(src)
    return {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}, tree


def _calls(node):
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            nm = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else None)
            if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant):
                nm = str(f.slice.value)
            out.append((nm, n.lineno, n.col_offset, n))
    return sorted(out, key=lambda x: (x[1], x[2]))


def _top_dump(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            k = n.name
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            k = n.targets[0].id
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            k = n.target.id
        else:
            k = f"<{type(n).__name__}>"
        out.setdefault(k, []).append(ast.dump(n))
    return out


def _fn_names(src):
    out = {}
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[n.name] = out.get(n.name, 0) + 1
    return out


def _kw(call, name):
    for k in call.keywords:
        if k.arg == name:
            return k.value
    return None


def _insert_only(old, new, repl=()):
    """old → new 之差唯增列（⛔ 改、⛔ 刪既有一列·`repl` 所列之基準之列除外〔`W-G.9-370`〕）且增段 ≥ 1。
    回 (ok, 增段數, 說明)。"""
    a, b = old.splitlines(), new.splitlines()
    ops = difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()
    bad = [(t, i1 + 1, i2) for t, i1, i2, _j1, _j2 in ops
           if t not in ("equal", "insert") and not (repl and set(a[i1:i2]) <= set(repl))]
    ins = [j2 - j1 for t, _i1, _i2, j1, j2 in ops if t == "insert"]
    return (not bad and len(ins) > 0), len(ins), f"非增之段（基準之列）{bad[:3]}"


def _wiring_checks(repo, base, app=None, spp=None):
    chk = []
    if app is None:
        app = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    if spp is None:
        spp = open(os.path.join(repo, "verify", "selection_pipeline.py"), encoding="utf-8").read()
    ad, atree = _defs(app)
    sd, stree = _defs(spp)
    # W1 新名與簽名
    consts = {}
    for n in atree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) \
                and isinstance(n.value, ast.Constant):
            consts.setdefault(n.targets[0].id, []).append(n.value.value)
    fsig = {nm: ([a.arg for a in ad[nm].args.args] if nm in ad else None) for nm in NEW_APP}
    okk = (ad.get(FN) is not None and [a.arg for a in ad[FN].args.kwonlyargs] == ["log_print"]
           and ad.get("f3_screen_adj4") is not None
           and [a.arg for a in ad["f3_screen_adj4"].args.kwonlyargs] == ["pk_kwargs", "g_kwargs", "slices"])
    okc = (consts.get("ADJ4_ENV") == ["WV_ADJ4"] and len(consts.get("ADJ4_IDENT_UNUSED") or []) == 1
           and isinstance(consts["ADJ4_IDENT_UNUSED"][0], str) and consts["ADJ4_IDENT_UNUSED"][0].strip() != "")
    ra = sd.get("run_adj4")
    oks = (ra is not None and [a.arg for a in ra.args.args] == RA_SIG and [a.arg for a in ra.args.kwonlyargs] == RA_KW)
    chk.append(("W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）",
                fsig == NEW_APP and okk and okc and oks, f"簽名 {fsig == NEW_APP}／kw {okk}／常數 {okc}／harness {oks}"))
    # W2 harness 之入口與序
    cra = _calls(ra) if ra is not None else []
    need_ra = ("adj4_enabled", "k953_enabled", "k929_6_enabled", "adj4_possible", "adj_intake", "adj4_plan",
               "k953_alloc_summary", "adj4_trial_state", "adj4_depth_of", "run_step_g")
    okr = (ra is not None and sum(1 for c in cra if c[0] == FN) == 1 and sum(1 for c in cra if c[0] == "adj4_plan") == 1
           and all(any(c[0] == nm for c in cra) for nm in need_ra)
           and not any(c[0] in ("run_corner_pk", "run_corner_pk_k6b", "run_k953") for c in cra))
    pk = sd.get("run_corner_pk_k6b")
    cs = _calls(pk) if pk is not None else []
    i_k = [c for c in cs if c[0] == "run_k953"]
    i_a = [c for c in cs if c[0] == "run_adj4"]
    i_pk_after = [c for c in cs if c[0] == "run_corner_pk" and i_a and c[1] > i_a[0][1]]
    sl = _kw(i_a[0][3], "slices") if i_a else None
    okw = (len(i_k) == 1 and len(i_a) == 1 and i_a[0][1] > i_k[0][1] and not i_pk_after
           and {k.arg for k in i_a[0][3].keywords} >= {"winners", "forced", "callbacks", "snapshot", "slices"}
           and isinstance(sl, ast.Name) and sl.id == "temp_parcels")
    asg_ok = False
    ret_ok = False
    if pk is not None and i_a:
        for n in ast.walk(pk):
            if isinstance(n, ast.Assign) and n.value is i_a[0][3]:
                tg = n.targets[0]
                asg_ok = isinstance(tg, ast.Tuple) and [getattr(e, "id", None) for e in tg.elts] == ["temp3", "build3"]
        last = pk.body[-1]
        ret_ok = (isinstance(last, ast.Return) and isinstance(last.value, ast.Tuple)
                  and [getattr(e, "id", None) for e in last.value.elts[-2:]] == ["temp3", "build3"])
    chk.append(("W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫"
                "街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ "
                "回傳之末二值、其後⛔ 再呼叫 run_corner_pk", okr and okw and asg_ok and ret_ok,
                f"入口 {okr}／序 {okw}／承接 {asg_ok}／回傳 {ret_ok}"))
    # W3 畫面之入口與序
    fs = ad.get("f3_screen_adj4")
    cfs = _calls(fs) if fs is not None else []
    need_fs = ("adj4_enabled", "k953_enabled", "k929_6_enabled", "adj4_possible", "adj_intake", "adj4_plan",
               "f3_screen_stepg_run",
               "k6b_screen_callbacks", "k953_alloc_summary", "adj4_trial_state", "adj4_depth_of")
    ok3 = (fs is not None and sum(1 for c in cfs if c[0] == FN) == 1 and sum(1 for c in cfs if c[0] == "adj4_plan") == 1
           and all(any(c[0] == nm for c in cfs) for nm in need_fs)
           and not any(c[0] in ("f3_screen_corner_pk_run", "f3_screen_k6b_stage3", "f3_screen_k953") for c in cfs))
    s3 = ad.get("f3_screen_k6b_stage3")
    c5 = _calls(s3) if s3 is not None else []
    i5k = [c for c in c5 if c[0] == "f3_screen_k953"]
    i5a = [c for c in c5 if c[0] == "f3_screen_adj4"]
    sl5 = _kw(i5a[0][3], "slices") if i5a else None
    t0 = False
    for n in (s3.body if s3 is not None else []):
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple) \
                and [getattr(e, "id", None) for e in n.targets[0].elts] == ["temp0", "build0"]:
            t0 = ast.unparse(n.value) == "(pk_kwargs['temp_parcels'], pk_kwargs['build_parcels'])"
    ok4 = (len(i5k) == 1 and len(i5a) == 1 and i5a[0][1] > i5k[0][1] and isinstance(sl5, ast.Name)
           and sl5.id == "temp0" and t0)
    chk.append(("W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、"
                "⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0"
                "（＝ pk_kwargs['temp_parcels']）", ok3 and ok4, f"入口 {ok3}／序 {ok4}"))
    # W4 新碼⛔ 案件字面
    lits = []
    for nm, node in [(k, ad.get(k)) for k in NEW_APP] + [("run_adj4", ra)]:
        for x in (ast.walk(node) if node is not None else []):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
                lits.append((nm, x.value))
    chk.append(("W4 新碼⛔ 案件字面", not lits, str(lits)))
    try:
        bapp = _git_show(repo, base, "app.py")
        bsp = _git_show(repo, base, "verify/selection_pipeline.py")
    except Exception as e:  # noqa: BLE001
        chk.append(("W5 頂層之相異 ⊆ 本單之許", False, f"基準讀不到：{type(e).__name__}"))
        return chk
    # W5 頂層之相異 ⊆ 本單之許
    allow_app = set(NEW_APP) | set(NEW_CONST) | set(CHG_APP)
    allow_sp = {"run_adj4"} | set(CHG_SP)
    for nm_, cur_, old_, allow_ in (("app.py", atree, ast.parse(bapp), allow_app),
                                    ("verify/selection_pipeline.py", stree, ast.parse(bsp), allow_sp)):
        a_, b_ = _top_dump(cur_), _top_dump(old_)
        diff = sorted(k for k in set(a_) | set(b_) if a_.get(k) != b_.get(k))
        chk.append((f"W5 {nm_} 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）", set(diff) <= allow_,
                    f"相異 {diff}；逾 {sorted(set(diff) - allow_)}"))
    # W6 本單所改之三函式：唯增列、增列皆屬本單
    bd, _ = _defs(bapp)
    bsd, _ = _defs(bsp)
    w6 = []
    for nm, cur, old, src_c, src_o in [(n, ad.get(n), bd.get(n), app, bapp) for n in CHG_APP] + \
                                      [(n, sd.get(n), bsd.get(n), spp, bsp) for n in CHG_SP]:
        if cur is None or old is None:
            w6.append((nm, False, 0, "缺"))
            continue
        ok_, k_, note_ = _insert_only(ast.get_source_segment(src_o, old), ast.get_source_segment(src_c, cur),
                                      W6_REPL.get(nm, ()))
        w6.append((nm, ok_, k_, note_))
    chk.append(("W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列"
                "（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）", all(x[1] for x in w6), "；".join(f"{a} {b}·增段 {c}" + ("" if b else f"（{d}）")
                                                       for a, b, c, d in w6)))
    # W7 既有量測器之錨仍恰一見；基準中恰一之函式名仍恰一
    lits8 = set()
    pdir = os.path.join(repo, "verify", "probes")
    for p8 in sorted(os.listdir(pdir)):
        if not p8.endswith(".py") or p8 == SELF_NAME or p8 in W7_SKIP:
            continue
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                t8 = ast.parse(open(os.path.join(pdir, p8), encoding="utf-8").read())
        except Exception:  # noqa: BLE001
            continue
        for x in ast.walk(t8):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and len(x.value) >= 4:
                lits8.add(x.value)
    for nm_, cur_s, old_s in (("app.py", app, bapp), ("verify/selection_pipeline.py", spp, bsp)):
        anc = [x for x in lits8 if old_s.count(x) == 1]
        moved = sorted((x[:60], cur_s.count(x)) for x in anc if cur_s.count(x) != 1)
        fb, fc = _fn_names(old_s), _fn_names(cur_s)
        dup = sorted((k, fc.get(k, 0)) for k, v in fb.items() if v == 1 and fc.get(k, 0) != 1)
        chk.append((f"W7 {nm_}：既有量測器之錨（{len(anc)}）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·"
                    f"{sum(1 for v in fb.values() if v == 1)}）仍恰一", not moved and not dup,
                    f"錨之異 {moved[:6]}；函式名之異 {dup[:8]}"))
    return chk


def wiring(repo, base):
    chk = _wiring_checks(repo, base)
    red = []
    for name, ok, note in chk:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本案（harness）──
# 第一趟之紀錄之 (序, 歸戶, 街廓, 片, 類, 受併宗, ((受併宗, 併入量 2 位)…), 結果)／剩下 ⇒ (剩下, 歸戶, 片, 結果, 餘量)
R1_EXPECT = {
    3.5: [("整體", "G001", "R3", "1 片", "—", "628-34(2)", (("628-34(2)", 13.15),), "成")],
    0.0: [("整體", "G001", "R3", "1 片", "—", "628-34(2)", (("628-34(2)", 13.15),), "成")],
}
# 配地之變（off → on）：{暫編地號: (G_off 2 位, G_on 2 位)}（|ΔG| ＞ 容差者）；{街廓: (抵費地_off, 抵費地_on)}
R3_EXPECT = {
    3.5: ({"628-34(2)": (250.24, 257.91)}, {"R3": (1659.06, 1651.41)}),
    0.0: ({"628-34(2)": (250.24, 257.91)}, {"R3": (1659.05, 1651.41)}),
}
# 調配之輸入之類（切片數, 原有面積合計 ㎡）與合併單位數；off → on 之去者（歸戶）
_R4_TOT = {"共同負擔用地·入合併單位": (31, 7103.74), "原位次配地": (74, 26324.86),
           "建築街廓內不能分配": (13, 1432.13), "無地號之殘料": (8, 0.0)}
R4_EXPECT = {3.5: (_R4_TOT, 17, ["G001"]), 0.0: (_R4_TOT, 17, ["G001"])}
# 受詞之片之段三之三鍵
R5_EXPECT = {3.5: {"628-3(1)": {"段三併出": ("628-34(2)",)}}, 0.0: {"628-3(1)": {"段三併出": ("628-34(2)",)}}}


def _pipeline(ns, fst, rv, sp, sb):
    from stepg_pipeline import run_step_g
    with contextlib.redirect_stdout(io.StringIO()):
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fst, snap)
        rv.build_ownership(ns, fst, rv.ANON_XLSX)
        v6 = open(rv.V6DXF, "rb").read()
        tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
        params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
        res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
        log = copy.deepcopy(fst.session_state.get("f3_adj4_log"))
        ns["K917_DROPPED"].clear()
        sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                        eff_min_build_by_blk={})
    drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
    own = dict(fst.session_state.get("t8_ownership_map") or {})
    bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
    it = ns["adj_intake"](res[5], sg["k929_6"]["build"], sg["g_rows"], drops, own, bur)
    return log, sg["g_rows"], it, res[5]


def _norm(log):
    out = []
    for r in log or []:
        q = tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items()))
        if r.get("序") == "剩下":
            out.append(("剩下", r.get("歸戶"), r.get("片"), r.get("結果"),
                        tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("餘量") or {}).items()))))
        else:
            out.append((r.get("序"), r.get("歸戶"), r.get("街廓"), r.get("片"), r.get("類"), r.get("受併宗"), q,
                        r.get("結果")))
    return out


def _gpool(rows):
    g = {str(r["暫編地號"]): (r["所屬街廓"], r["推進側別"], float(r["G(㎡)"])) for r in rows
         if r.get("推進側別") in ("left", "right")}
    p = {}
    for r in rows:
        if r.get("推進側別") == "抵費地":
            p[r["所屬街廓"]] = p.get(r["所屬街廓"], 0.0) + float(r.get("幾何面積(㎡)") or 0)
    return g, p


def _keys_of(temp, ids):
    out = {}
    for t in temp:
        if str(t["暫編地號"]) not in ids:
            continue
        d = {}
        for k in ("段三併出", "段三部分併出", "段三餘量"):
            if k in t:
                v = t[k]
                d[k] = (tuple(v) if isinstance(v, list) else
                        tuple(sorted((a, round(float(b), 2)) for a, b in v.items())) if isinstance(v, dict)
                        else round(float(v), 2))
        out[str(t["暫編地號"])] = d
    return out


def run(repo, sbs, show=False):
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    if FN not in ns or not hasattr(sp, "run_adj4"):
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    for sb in sbs:
        env = os.environ.get("WV_ADJ4")
        try:
            os.environ["WV_ADJ4"] = "off"
            log0, rows0, it0, _t0 = _pipeline(ns, fst, rv, sp, sb)
            if env is None:
                os.environ.pop("WV_ADJ4", None)
            else:
                os.environ["WV_ADJ4"] = env
            log, rows, it, temp = _pipeline(ns, fst, rv, sp, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️ {sb}：執行中止 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
            print("⇒ rc 3（無從判定）")
            return 3
        finally:
            if env is None:
                os.environ.pop("WV_ADJ4", None)
            else:
                os.environ["WV_ADJ4"] = env
        got1 = _norm(log)
        ok1 = log0 == [] and got1 == R1_EXPECT.get(sb)
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：第一趟之紀錄 {len(got1)} 列 ＝ 本器所載（off 之紀錄 ＝ []：{log0 == []}）")
        if not ok1:
            red.append(f"R1@{sb}")
            print(f"      得 {got1!r}")
        c0 = sorted((r["所屬街廓"], r["推進側別"], str(r["暫編地號"])) for r in rows0 if r.get("驗_宗序") == "街角第1宗")
        c1 = sorted((r["所屬街廓"], r["推進側別"], str(r["暫編地號"])) for r in rows if r.get("驗_宗序") == "街角第1宗")
        ok2 = c0 == c1 and len(c0) > 0
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：街角第 1 宗 ＝ off 之實跑 {ok2}（{len(c1)} 宗）")
        if not ok2:
            red.append(f"R2@{sb}")
        g0, p0 = _gpool(rows0)
        g1, p1 = _gpool(rows)
        dg_ = {k: (round(g0[k][2], 2) if k in g0 else None, round(g1[k][2], 2) if k in g1 else None)
               for k in sorted(set(g0) | set(g1))
               if k not in g0 or k not in g1 or g0[k][:2] != g1[k][:2] or abs(g0[k][2] - g1[k][2]) > TOL}
        dp_ = {k: (round(p0.get(k, 0.0), 2), round(p1.get(k, 0.0), 2)) for k in sorted(set(p0) | set(p1))
               if abs(p0.get(k, 0.0) - p1.get(k, 0.0)) > TOL}
        sdg = sum(v[2] for v in g1.values()) - sum(v[2] for v in g0.values())
        sdp = sum(p1.values()) - sum(p0.values())
        sabs = sum(abs(g1[k][2] - g0[k][2]) for k in set(g0) & set(g1))
        ok3 = (dg_, dp_) == R3_EXPECT.get(sb) and abs(sdg + sdp) <= 0.1
        print(("  ✅" if ok3 else "  🔴") + f" R3@{sb}：配地之變 {len(dg_)} 宗·抵費地之變 {len(dp_)} 街廓 ＝ 本器所載；"
              f"ΣΔG {sdg:+.4f}（Σ|ΔG| {sabs:.4f}）／ΣΔ抵費地 {sdp:+.4f}（和 {sdg + sdp:+.4f}·≤ 0.1）")
        if not ok3 or show:
            print(f"      得 {(dg_, dp_)!r}")
            if not ok3:
                red.append(f"R3@{sb}")
        tot = {k: (v[0], round(v[1], 2)) for k, v in sorted(it["totals"].items())}
        e4 = (tot, len(it["units"]), sorted({u["歸戶"] for u in it0["units"]} - {u["歸戶"] for u in it["units"]}))
        ok4 = e4 == R4_EXPECT.get(sb)
        print(("  ✅" if ok4 else "  🔴") + f" R4@{sb}：調配之輸入之類·合併單位數 {e4[1]}·去者 {e4[2]} ＝ 本器所載")
        if not ok4 or show:
            print(f"      得 {e4!r}")
            if not ok4:
                red.append(f"R4@{sb}")
        k5 = _keys_of(temp, _subj_pieces(log, temp))
        ok5 = k5 == R5_EXPECT.get(sb)
        print(("  ✅" if ok5 else "  🔴") + f" R5@{sb}：受詞之片之段三之三鍵 ＝ 本器所載（{len(k5)} 片）")
        if not ok5 or show:
            print(f"      得 {k5!r}")
            if not ok5:
                red.append(f"R5@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _subj_pieces(log, temp):
    """紀錄所及之片：逐片之列之片 ＋ 剩下之列之片 ＋ 整體之列之受併宗所承之片（temp 之段三併出含之者）。"""
    ids = set()
    rcv = set()
    for r in log or []:
        if r.get("序") == "逐片":
            ids.add(str(r["片"]))
        elif r.get("序") == "剩下":
            ids |= set(str(r["片"]).split("、"))
        elif r.get("序") == "整體":
            rcv.add(str(r["受併宗"]))
    for t in temp:
        if set(t.get("段三併出") or []) & rcv:
            ids.add(str(t["暫編地號"]))
    return ids


# ── offsnap／offcmp：旗標 off ⇒ 逐位同開工態 ──
def _canon(x):
    import hashlib
    import json
    b = json.dumps(x, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
    return hashlib.sha256(b).hexdigest(), len(b)


def offsnap(repo, out, sbs):
    import json
    os.environ["WV_ADJ4"] = "off"           # 行程內自設（開工態無此旗標 ⇒ 無作用）
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    from stepg_pipeline import run_step_g
    snap_out = {}
    for sb in sbs:
        ns["K917_DROPPED"].clear()
        with contextlib.redirect_stdout(io.StringIO()):
            snap = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fst, snap)
            rv.build_ownership(ns, fst, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
            params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
            res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
            ss = fst.session_state
            s3log = copy.deepcopy(ss.get("f3_k6b_stage3_log"))
            eblog = copy.deepcopy(ss.get("f3_end_block_merge_log"))
            k953 = copy.deepcopy(ss.get("f3_k953_log"))
            a4 = ss.get("f3_adj4_log", "<缺>")
            ns["K917_DROPPED"].clear()
            sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                            eff_min_build_by_blk={})
        drops = {f"{k}": list(v) for k, v in ns["K917_DROPPED"].items()}
        own = dict(fst.session_state.get("t8_ownership_map") or {})
        bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
        it = ns["adj_intake"](res[5], sg["k929_6"]["build"], sg["g_rows"], ns["K917_DROPPED"], own, bur)
        part = {
            "街角": [res[3], res[4]],
            "宗地": [[t.get("暫編地號"), t.get("段三併出"), t.get("段三部分併出"), t.get("段三餘量"),
                     t.get("面積_m2"), t.get("分攤登記面積_m2")] for t in res[5]],
            "build": [b.get("暫編地號") for b in res[6]],
            "段三紀錄": s3log, "末端塊紀錄": eblog, "手冊先行之紀錄": k953,
            "配地": sg["g_rows"], "入池閘": sg["k929_6"].get("log"), "不配地": drops,
            "調配之輸入": {"totals": it["totals"], "units": it["units"], "step4": it["step4"]},
        }
        snap_out[str(sb)] = {k: _canon(v) for k, v in part.items()}
        snap_out[str(sb)]["第一趟之紀錄"] = (a4 if a4 == "<缺>" else len(a4))
        print(f"  {sb}：" + "；".join(f"{k} {v[0][:12]}" for k, v in snap_out[str(sb)].items() if isinstance(v, tuple))
              + f"；第一趟之紀錄 {snap_out[str(sb)]['第一趟之紀錄']}")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(snap_out, fh, ensure_ascii=False, indent=1, sort_keys=True)
    print(f"⇒ 寫 {out}；rc 0")
    return 0


def offcmp(a, b):
    import json
    A, B = json.load(open(a, encoding="utf-8")), json.load(open(b, encoding="utf-8"))
    red = []
    for sb in sorted(set(A) | set(B)):
        for k in sorted(set(A.get(sb, {})) | set(B.get(sb, {}))):
            if k == "第一趟之紀錄":
                continue
            ok = A.get(sb, {}).get(k) == B.get(sb, {}).get(k)
            print(("  ✅ " if ok else "  🔴 ") + f"{sb}·{k}")
            if not ok:
                red.append(f"{sb}·{k}")
        print(f"  ℹ️ {sb}·第一趟之紀錄：{A.get(sb, {}).get('第一趟之紀錄')} → {B.get(sb, {}).get('第一趟之紀錄')}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "offcmp" and len(argv) == 4:
        return offcmp(os.path.abspath(argv[2]), os.path.abspath(argv[3]))
    repo = os.path.abspath(argv[2])
    if cmd == "selftest" and len(argv) == 3:
        return selftest(repo)
    if cmd == "wiring" and len(argv) == 4:
        return wiring(repo, argv[3])
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    if cmd == "offsnap" and len(argv) >= 4:
        return offsnap(repo, os.path.abspath(argv[3]), [float(x) for x in argv[4:]] or [3.5, 0.0])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
