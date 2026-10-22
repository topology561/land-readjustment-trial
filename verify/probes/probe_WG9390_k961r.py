# -*- coding: utf-8 -*-
"""W-G.9-390 量測器（發單端擬·檔 F34·⛔ 由受單側改一字）：段三（街角合併重試·與末端塊合併再試同一函式）之取得街角（或
末端塊）之宗之鎖定（KL `2026-10-20 22:30`／`22:55`「取得即鎖定」·取代 `K-9-61` ④ 之還原）。

〔補令三·⛔ 上列之 K1〜K27 之還原之例〕所量之性質：經合併再試取得街角（或末端塊）之宗即為原位次已配定之宗而鎖定——步驟 1〜8
  畢而成者 ≥ 1 ⇒ 以一次之試算（`alloc_state`）查一切成者之宗之保留：試算中止 ⇒ 停機（無從判定）；有未保留者 ⇒ 停機（程式錯誤·
  ⛔ 還原、⛔ 重試、⛔ 下一名續試）；皆保留 ⇒ 步驟 10 沿用其試算；成者為零 ⇒ ⛔ 查。鎖定之宗仍得受同一地主之併入（原地變寬·
  KL 22:55 問2「可以」）；鎖定之受詞唯成者之宗（他宗之未保留⛔ 停機）。

子命令（一律 python3 verify/probes/probe_WG9390_k961r.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k6b_stage3_run`）。玩具：街廓 BA（y∈[0,30]）臨正面道路 RD
           （y∈[-10,0]·中心線 y ＝ -5），RD 之另一側為 BB（y∈[-40,-10]）；各宗寬依各例。回呼：`trial_winner` ＝ G ≥ 門檻即
           當選；`alloc_state` 以 build 之全部為保留、唯各例之「⛔ 保留之式」所指者除外（G ＝ 分攤登記面積 ＋ 面積），並計其
           呼叫之數；`a_prime` ＝ a(src)。期值皆手算（各例之註）。
           L1 合併再試（①）所得之宗⛔ 保留 ⇒ 停機（⛔ 還原·該群無待後處理之土地者亦查）；L2 經道路片（②）所得者⛔ 保留 ⇒ 停機；
           L3 二端皆⛔ 保留 ⇒ 停機（訊息具二者）；L4 先成者保留而後成之右端者⛔ 保留 ⇒ 停機（訊息具後者）；L5 競合（`K-9-50`
           題二）之所取之一端⛔ 保留 ⇒ 停機；L6 競合（題一·切半二端各配一宗）而皆⛔ 保留 ⇒ 停機；L7 皆保留 ⇒ 步驟之列、後處理
           （道路片併入鎖定之宗·原地變寬）、G 同改前、試算 3（步驟 10 沿用其查之試算）；L8 有成者而該群無待後處理之土地 ⇒ 仍查
           （試算 1）；L9 查之試算中止 ⇒ 停機（無從判定）；L10 無成者 ⇒ ⛔ 查（試算 0）；L11 L7 之換名、左右鏡射、旋轉 37° 並移至
           TWD97 之尺度 ⇒ 同 L7；L12 成者皆保留而非成者之宗⛔ 保留 ⇒ ⛔ 停機（同 L7 之列）；L13 皆保留之紀錄⛔ 含回原狀之列
           （結果、檢核皆⛔ 以「回原狀」起首）；L14 題一（切半）只一端成、他端依題一 4 照配（後處理之成之列）⇒ 該列⛔ 為
           成者、⛔ 停機。L4 另綁訊息⛔ 具保留之成者。P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           X1 `k6b_stage3_run` 內之字串常數（f-string 之字面部分亦計·其 docstring 除外）：舊停機之字樣（「受併宗於現態未保留」·
           以拼接立之）去之；含「回原狀」者 `0`、含「還原後仍出現」者 `0`；含「取得即鎖定之宗之查」者 ≥ `1`；X2 app.py 之頂層
           節點對基準之相異 ＝ `{k6b_stage3_run}`、頂層之名之集⛔ 變；X3 `k6b_stage3_run` 內⛔ 案件字面；X4 `verify/` 之 `*.py`
           （頂層）對基準逐位同。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 街角選位至配地（`run_corner_pk_k6b` ＋ `run_step_g`）⛔ 停機、段三與
           末端塊合併再試之諸紀錄中以「回原狀」起首之結果或檢核皆 `0`；R0 諸退縮之段三之成者之和 ≥ `1`（其查已行）⇒ 本案之配地
           ⛔ 變（其逐位由 `k6s3 cmp`／`F8`／`parity` 量之）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

H, RDC = "住宅區", "道路"
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
LOCK = "取得即鎖定之宗之查"
KEPT = "於試算⛔ 保留"
BLOCKS = {"BA": {"category": H}, "BB": {"category": H}, "RD": {"category": RDC}}
CL = {"RD": [(-40.0, -5.0), (90.0, -5.0)]}
# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
W392 = W392 + ("_corner_first_lot_G",)   # 🔧 `W-G.9-392` 補令一：評選之式之起算點（K-9-41 ①·F36 W8 量之）


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _g(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _O(*rows):
    return [{"最終序位": i, "街廓": b, "端": e, "暫編地號": c} for i, (b, e, c) in enumerate(rows, 1)]


def _xf(T):
    """T ＝ (旋轉之度, 鏡射〔x → 50 − x〕, (平移 x, 平移 y))"""
    deg, mir, (tx, ty) = T
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))

    def f(pt):
        x, y = pt
        if mir:
            x = 50.0 - x
        return (x * c - y * s + tx, x * s + y * c + ty)
    return f


def _world(parcels, own, T=(0.0, False, (0.0, 0.0)), names=None, extra=None):
    """parcels：[(暫編地號, 街廓, 類, 多邊形, 分攤登記面積)]；names：{舊名: 新名}（暫編地號之原地號部、街廓、地主）；
    extra：BLOCKS 以外之街廓（補令一之 K22）。"""
    nm = names or {}
    f = _xf(T)

    def rn(pid):
        base, _, rest = pid.partition("(")
        return nm.get(base, base) + "(" + rest

    temp = []
    for pid, blk, cat, poly, a, *z in parcels:    # 🔧 補令二：第六欄（缺 ⇒ 0）＝ 面積_m2 之初值
        p2 = rn(pid)
        temp.append({"暫編地號": p2, "原地號": p2.split("(")[0], "polygon_coords": [list(f(pt)) for pt in poly],
                     "所屬街廓": nm.get(blk, blk), "街廓分類": cat, "分攤登記面積_m2": float(a),
                     "面積_m2": float(z[0]) if z else 0.0})
    own2 = {nm.get(k, k): nm.get(v, v) for k, v in own.items()}
    blocks = {nm.get(k, k): v for k, v in dict(BLOCKS, **(extra or {})).items()}
    cl = {nm.get(k, k): [f(p) for p in v] for k, v in CL.items()}
    return temp, own2, blocks, cl


def _go(ns, parcels, own, order, thr, dropf, *, T=(0.0, False, (0.0, 0.0)), names=None, err_if=None, contests=None,
        extra=None):
    """回 dict：rows（步驟之列 (序, 候選, 結果, 層級, 整筆併入, 檢核)）、post（後處理之列 (候選, 層級, 結果, 受併宗)）、G、build、
    temp、calls（alloc_state 之呼叫數）、log；停機 ⇒ ('停機', 訊息)。dropf(pid, G, Gmap) ⇒ 真者⛔ 保留（pid 為原名）。"""
    nm = names or {}
    inv = {}
    for k, v in nm.items():
        inv[v] = k
    temp, own2, blocks, cl = _world(parcels, own, T, names, extra)
    build = [t for t in temp if t["街廓分類"] == H]
    calls = [0]

    def back(pid):
        base, _, rest = pid.partition("(")
        return inv.get(base, base) + "(" + rest

    def a_prime(src, dst):
        return _g(src)

    def alloc_state(temp_, build_):
        calls[0] += 1
        gm = {back(b["暫編地號"]): _g(b) for b in build_}
        if err_if is not None and err_if(gm):
            return {"kept": {}, "bad_pools": {}, "err": "合成之配地中止", "G": {}}
        kept, G = {}, {}
        for b in build_:
            if dropf(back(b["暫編地號"]), _g(b), gm):
                continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            G[b["暫編地號"]] = _g(b)
        return {"kept": kept, "bad_pools": {}, "err": None, "G": G}

    def trial_winner(temp_, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        gg = _g(by[cand]) if cand in by else 0.0
        return (cand if gg >= thr else None), round(gg, 2), thr

    od = [dict(r, 街廓=nm.get(r["街廓"], r["街廓"]), 暫編地號=(lambda p: (nm.get(p.partition("(")[0], p.partition("(")[0])
                                                                     + "(" + p.partition("(")[2]))(r["暫編地號"]))
          for r in order]
    ct = None
    if contests:
        ct = [{"形": c["形"], "列": [(nm.get(b, b), e, (nm.get(p.partition("(")[0], p.partition("(")[0]) + "("
                                                        + p.partition("(")[2]), a) for b, e, p, a in c["列"]]}
              for c in contests]
    try:
        t2, b2, log = ns["k6b_stage3_run"](od, set(), own2, temp, build, blocks, cl, a_prime, trial_winner,
                                           alloc_state, log_print=lambda *x: None, blk5=lambda: {}, contests=ct)
    except RuntimeError as e:
        return ("停機", str(e))

    def bl(x):
        return [back(p) for p in x] if isinstance(x, (list, tuple)) else x
    rows = [(r["序"], back(r["候選"]), r["結果"], r.get("層級"), sorted(bl(r.get("整筆併入") or [])), r.get("檢核"))
            for r in log if r.get("序") != "後處理"]
    post = [(back(r["候選"]), r["層級"], r["結果"],
             back(r["受併宗"]) if isinstance(r["受併宗"], str) and r["受併宗"] != "—" else
             (tuple(back(x) for x in r["受併宗"]) if isinstance(r["受併宗"], (list, tuple)) else r["受併宗"]))
            for r in log if r.get("序") == "後處理"]
    return {"rows": rows, "post": post, "G": {back(t["暫編地號"]): round(_g(t), 2) for t in t2},
            "build": sorted(back(b["暫編地號"]) for b in b2), "temp": {back(t["暫編地號"]): t for t in t2},
            "calls": calls[0], "log": log}


def _st(res, *keys):
    if not isinstance(res, dict):
        return res
    return tuple(res[k] for k in keys)


# ── 玩具之宗（暫編地號, 街廓, 類, 多邊形, 分攤登記面積）──
def _w1():
    # BA（x∈[0,50]）：g1 之 A1(1)[0,10]（100）、A2(1)[10,20]（60）；g2 之 B1(1)[20,30]（100）、B2(1)[30,40]（55）；g3 之 C1(1)
    p = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A2(1)", "BA", H, _R(10, 20, 0, 30), 60),
         ("B1(1)", "BA", H, _R(20, 30, 0, 30), 100), ("B2(1)", "BA", H, _R(30, 40, 0, 30), 55),
         ("C1(1)", "BA", H, _R(40, 50, 0, 30), 300)]
    own = {"A1": "g1", "A2": "g1", "B1": "g2", "B2": "g2", "C1": "g3"}
    return p, own, _O(("BA", "左", "A1(1)"), ("BA", "左", "B1(1)"))


def _w4():
    # BA：g1 之 A1(1)[0,10]（100）／A2(1)[10,20]（60）（左端）；g9 之 M(1)[20,30]；g4 之 E2(1)[30,40]（60）／E1(1)[40,50]（100）（右端）
    p = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A2(1)", "BA", H, _R(10, 20, 0, 30), 60),
         ("M(1)", "BA", H, _R(20, 30, 0, 30), 500), ("E2(1)", "BA", H, _R(30, 40, 0, 30), 60),
         ("E1(1)", "BA", H, _R(40, 50, 0, 30), 100)]
    own = {"A1": "g1", "A2": "g1", "M": "g9", "E1": "g4", "E2": "g4"}
    return p, own, _O(("BA", "左", "A1(1)"), ("BA", "右", "E1(1)"))


def _drop4(pid, g, gm):
    # 二端皆合併（A1、E1 之 G 皆 ＞ 150）⇒ 二者皆⛔ 保留（街廓之容不足之合成）；否則皆保留
    return pid in ("A1(1)", "E1(1)") and gm.get("A1(1)", 0) > 150 and gm.get("E1(1)", 0) > 150


def _halt2(res, *must, nots=()):
    if isinstance(res, tuple) and res and res[0] == "停機":
        return ("停機", all(m in res[1] for m in must) and not any(n in res[1] for n in nots))
    return ("無停機",) + ((res["rows"], res["calls"]) if isinstance(res, dict) else (res,))


def _cases(ns):
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:200])
        out.append((name, got, exp))

    p1, own1, od1 = _w1()
    # L1：門檻 150；A1 之 ① ＝ 100 ＋ 60 ＝ 160 ⇒ 成；A1 於 G ＞ 150 時⛔ 保留 ⇒ 停機（g1 無待後處理之土地·⛔ 還原、⛔ B1 續試）
    run("L1 合併再試（①）所得之宗⛔ 保留 ⇒ 停機（⛔ 還原）",
        lambda: _halt2(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: pid == "A1(1)" and g > 150), LOCK, KEPT, "A1(1)"),
        ("停機", True))
    # L2：A1(1)[0,10]（100）無同街廓之相鄰同一地主之宗；g1 之道路片 A9(1)（RD·x∈[0,10]·60）⇒ ② ＝ 160 ⇒ 成；A1 恆⛔ 保留 ⇒ 停機
    p3 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A9(1)", "RD", RDC, _R(0, 10, -10, 0), 60),
          ("B1(1)", "BA", H, _R(10, 20, 0, 30), 100), ("B2(1)", "BA", H, _R(20, 30, 0, 30), 55),
          ("C1(1)", "BA", H, _R(30, 50, 0, 30), 300)]
    own3 = {"A1": "g1", "A9": "g1", "B1": "g2", "B2": "g2", "C1": "g3"}
    run("L2 經道路片（②）所得者⛔ 保留 ⇒ 停機",
        lambda: _halt2(_go(ns, p3, own3, od1, 150.0, lambda pid, g, gm: pid == "A1(1)"), LOCK, KEPT, "A1(1)"), ("停機", True))
    p4, own4, od4 = _w4()
    # L3：二端皆成（A1 160、E1 160）⇒ 二者皆⛔ 保留 ⇒ 停機（訊息具 A1、E1）
    run("L3 二端皆⛔ 保留 ⇒ 停機（訊息具二者）",
        lambda: _halt2(_go(ns, p4, own4, od4, 150.0, _drop4), LOCK, KEPT, "A1(1)", "E1(1)"), ("停機", True))
    # L4：L3 之地；唯 E1（後成·右端）於 G ＞ 150 時⛔ 保留 ⇒ 停機（訊息具 E1、⛔ 具保留之 A1）
    run("L4 先成者保留而後成之右端者⛔ 保留 ⇒ 停機（訊息具後者、⛔ 具保留者）",
        lambda: _halt2(_go(ns, p4, own4, od4, 150.0, lambda pid, g, gm: pid == "E1(1)" and g > 150), LOCK, KEPT, "E1(1)",
                       nots=("A1(1)",)), ("停機", True))
    # L5：BA：g1 之 L1(1)[0,10]（100）／L2(1)[10,20]（60）、g9 之 M(1)[20,30]、g1 之 R2(1)[30,40]（70）／R1(1)[40,50]（100）；g1 之
    #   道路片 D9(1)（RD·x∈[0,50]·50）連之 ⇒ 同一合併群；競合（題二）交面積 L 30 ＞ R 20；① 二端皆成（160／170）⇒ L1；L1 於
    #   G ＞ 150 時⛔ 保留 ⇒ 停機
    p7 = [("L1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("L2(1)", "BA", H, _R(10, 20, 0, 30), 60),
          ("M(1)", "BA", H, _R(20, 30, 0, 30), 500), ("R2(1)", "BA", H, _R(30, 40, 0, 30), 70),
          ("R1(1)", "BA", H, _R(40, 50, 0, 30), 100), ("D9(1)", "RD", RDC, _R(0, 50, -10, 0), 50)]
    own7 = {"L1": "g1", "L2": "g1", "R1": "g1", "R2": "g1", "D9": "g1", "M": "g9"}
    ct7 = [{"形": "二", "列": [("BA", "左", "L1(1)", 30.0), ("BA", "右", "R1(1)", 20.0)]}]
    run("L5 競合（題二）之所取之一端⛔ 保留 ⇒ 停機",
        lambda: _halt2(_go(ns, p7, own7, _O(("BA", "左", "L1(1)"), ("BA", "右", "R1(1)")), 150.0,
                           lambda pid, g, gm: pid == "L1(1)" and g > 150, contests=ct7), LOCK, KEPT, "L1(1)"), ("停機", True))
    # L6：BA 之 g1 之 A1(1)[0,10]（100）、BB 之 g1 之 F1(1)[0,10]（110）、g1 之道路片 D(1)（RD·x∈[0,10]·80·依中心線分為北半、
    #   南半各 40）；他人 M(1)、N(1)；門檻 138；競合（題一）；切半：A 140／F 150 ⇒ 二端各配一宗（同一次所施）；二者之 G 皆 ＞ 130
    #   ⇒ 皆⛔ 保留 ⇒ 停機（訊息具 A1、F1·⛔ 依序還原其一）
    p21 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("M(1)", "BA", H, _R(10, 50, 0, 30), 500),
           ("D(1)", "RD", RDC, _R(0, 10, -10, 0), 80),
           ("F1(1)", "BB", H, _R(0, 10, -40, -10), 110), ("N(1)", "BB", H, _R(10, 50, -40, -10), 500)]
    own21 = {"A1": "g1", "D": "g1", "F1": "g1", "M": "g9", "N": "g8"}
    ct21 = [{"形": "一", "列": [("BA", "左", "A1(1)", 30.0), ("BB", "左", "F1(1)", 20.0)]}]
    odAF = _O(("BA", "左", "A1(1)"), ("BB", "左", "F1(1)"))

    def _drop21(pid, g, gm):
        return pid in ("A1(1)", "F1(1)") and gm.get("A1(1)", 0) > 130 and gm.get("F1(1)", 0) > 130
    run("L6 競合（題一·切半二端各配一宗）而皆⛔ 保留 ⇒ 停機",
        lambda: _halt2(_go(ns, p21, own21, odAF, 138.0, _drop21, contests=ct21), LOCK, KEPT, "A1(1)", "F1(1)"),
        ("停機", True))
    # L7：g1 之 A1(1)[0,10]（100）／A2(1)[10,20]（60）、道路片 A9(1)（RD·x∈[0,10]·40）；皆保留 ⇒ A1 成（①）、A9 ⇒ A1（200·
    #   鎖定之宗受同一地主之併入·原地變寬）；試算：查 1 ＋ 後處理之整批之檢核 2 ＝ 3（步驟 10 沿用查之試算）
    p8 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A2(1)", "BA", H, _R(10, 20, 0, 30), 60),
          ("A9(1)", "RD", RDC, _R(0, 10, -10, 0), 40), ("M(1)", "BA", H, _R(20, 50, 0, 30), 500)]
    own8 = {"A1": "g1", "A2": "g1", "A9": "g1", "M": "g9"}
    exp7 = ([(1, "A1(1)", "成", "①", ["A2(1)"], "免")], [("A9(1)", "後處理(b)", "成", "A1(1)")],
            {"A1(1)": 200.0, "A2(1)": 60.0, "A9(1)": 40.0, "M(1)": 500.0}, 3)
    run("L7 皆保留 ⇒ 同改前、鎖定之宗受併入、試算 3（步驟 10 沿用其查之試算）",
        lambda: _st(_go(ns, p8, own8, _O(("BA", "左", "A1(1)")), 150.0, lambda pid, g, gm: False),
                    "rows", "post", "G", "calls"), exp7)
    # L8：L1 之形而皆保留 ⇒ A1 成、B1 略；g1 無待後處理之土地 ⇒ 仍查（試算 1）
    run("L8 有成者而該群無待後處理之土地 ⇒ 仍查（試算 1）",
        lambda: _st(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: False), "rows", "calls"),
        ([(1, "A1(1)", "成", "①", ["A2(1)"], "免"), (2, "B1(1)", "略·已定案", "—", [], "—")], 1))
    # L9：查之試算中止（任一宗 G ＞ 150 ⇒ 配地中止）⇒ 停機（⛔ 以之為保留、⛔ 以之為未保留·訊息帶試算之中止之由）
    run("L9 查之試算中止 ⇒ 停機（無從判定）",
        lambda: _halt2(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: False,
                           err_if=lambda gm: any(v > 150 for v in gm.values())), LOCK, "試算中止", "合成之配地中止"),
        ("停機", True))
    # L10：門檻 500 ⇒ A1 之 ①（160）、B1 之 ①（155）皆未成 ⇒ 成者 0 ⇒ ⛔ 查（試算 0）
    run("L10 無成者 ⇒ ⛔ 查（試算 0）",
        lambda: _st(_go(ns, p1, own1, od1, 500.0, lambda pid, g, gm: False), "calls"), (0,))
    # L11：L7 之換名（BA→QZ、A→P、M→N、g1→h7、g9→h9）、左右鏡射（x → 50 − x·A 在右端）、旋轉 37° 並移至 (303000, 2650000)
    nm11 = {"BA": "QZ", "A1": "P1", "A2": "P2", "A9": "P9", "M": "N", "g1": "h7", "g9": "h9"}
    run("L11 L7 之換名、左右鏡射、旋轉並移至 TWD97 之尺度 ⇒ 同 L7",
        lambda: _st(_go(ns, p8, own8, _O(("BA", "右", "A1(1)")), 150.0, lambda pid, g, gm: False,
                        T=(37.0, True, (303000.0, 2650000.0)), names=nm11), "rows", "post", "G", "calls"), exp7)
    # L12：L7 之地而 M（非成者·他地主）⛔ 保留 ⇒ 鎖定之受詞唯成者之宗 ⇒ ⛔ 停機（列同 L7）
    run("L12 成者皆保留而非成者之宗⛔ 保留 ⇒ ⛔ 停機",
        lambda: _st(_go(ns, p8, own8, _O(("BA", "左", "A1(1)")), 150.0, lambda pid, g, gm: pid == "M(1)"),
                    "rows", "post"), exp7[:2])

    # L13：L7 之紀錄之一切列之結果、檢核⛔ 以「回原狀」起首
    def k13():
        r = _go(ns, p8, own8, _O(("BA", "左", "A1(1)")), 150.0, lambda pid, g, gm: False)
        if not isinstance(r, dict):
            return r
        return sum(1 for y in r["log"] for k in ("結果", "檢核") if str(y.get(k, "")).startswith("回原狀"))
    run("L13 紀錄⛔ 含回原狀之列", k13, 0)
    # L14：L6 之地、門檻 145 ⇒ 切半：A 140 未成、F 150 成 ⇒ 只一端成 ⇒ F1；題一 4：A1 連同其北半依原位次（140·保留）照配
    #   （後處理之「成」之列·⛔ 為成者 ⇒ ⛔ 鎖定之受詞）；皆保留 ⇒ ⛔ 停機
    def k14():
        r = _go(ns, p21, own21, odAF, 145.0, lambda pid, g, gm: False, contests=ct21)
        if not isinstance(r, dict):
            return r
        return sorted((x[1], x[2], x[5]) for x in r["rows"]), r["post"], r["G"]["A1(1)"], r["G"]["F1(1)"]
    run("L14 題一 4 之照配（後處理之成）⛔ 為鎖定之受詞 ⇒ ⛔ 停機", k14,
        ([("A1(1)", "未成", "—"), ("F1(1)", "成", "通過")], [("A1(1)", "題一 4", "成", "A1(1)")], 140.0, 150.0))
    return out


def selftest(repo):
    try:
        ns, _ = _harvest(repo)
    except Exception as e:  # noqa: BLE001
        print(f"  🔴 受詞之取得中止：{type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    if "k6b_stage3_run" not in ns:
        print("  🔴 受詞缺 ['k6b_stage3_run']")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    C = _cases(ns)
    for name, got, exp in C:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {got!r}"[:700])
            print(f"       期 {exp!r}"[:700])
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

def _git(repo, *a):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else ""


def _fn(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return ast.get_source_segment(src, n), n
    return "", None


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


def wiring(repo, base):
    print(f"── 接線（工作樹之 app.py 對基準 {base}）──")
    red = []
    try:
        app = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠️ 工作樹之 app.py 讀不到：{type(e).__name__}")
        print("⇒ rc 3（無從判定）")
        return 3
    old = _git(repo, "show", f"{base}:app.py")
    if not old:
        print("  ⚠️ 基準之 app.py 取不到")
        print("⇒ rc 3（無從判定）")
        return 3
    k6, fn = _fn(app, "k6b_stage3_run")
    # 舊停機之字樣以執行時之拼接立之（各段長 ≤ 3·⛔ 成為長 ≥ 4 之字串常數·避 F23 W8／F24 W7 之「恰一見」之錨）
    gone = "".join(("受併宗", "於現態", "未保留"))
    # 受詞 ＝ 函式內之字串常數（f-string 之字面部分亦計·函式之 docstring 除外）
    doc = ast.get_docstring(fn, clean=False) if fn else None
    consts = [n.value for n in ast.walk(fn) if isinstance(n, ast.Constant) and isinstance(n.value, str)
              and n.value != doc] if fn else []
    cnt = {"回原狀": sum(1 for c in consts if "回原狀" in c),
           "還原後仍出現": sum(1 for c in consts if "還原後仍出現" in c)}
    nlock = sum(1 for c in consts if LOCK in c)
    left = sum(1 for c in consts if gone in c)
    ok1 = bool(fn) and left == 0 and all(v == 0 for v in cnt.values()) and nlock >= 1
    print(("  ✅" if ok1 else "  🔴") + f" X1 舊停機之字樣去之（殘 {left}）、還原之字樣去之（{cnt}）、鎖定之查之字樣 {nlock}（期 ≥ 1）")
    if not ok1:
        red.append("X1")
    ta, tb = _top(app), _top(old)
    diff = sorted(k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k))
    ok2 = diff == ["k6b_stage3_run"] and set(ta) == set(tb)
    # 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點亦許（F35 量之）
    ok2 = ok2 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW391) and set(tb) <= set(ta)
                  and set(diff) <= {"k6b_stage3_run"} | set(W391))
    # 🔧 `W-G.9-392`：同（F36 量之）
    ok2 = ok2 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW391) | set(NEW392) and set(tb) <= set(ta)
                  and set(diff) <= {"k6b_stage3_run"} | set(W391) | set(W392))
    print(("  ✅" if ok2 else "  🔴") + f" X2 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
    if not ok2:
        red.append("X2")
    lits = sorted({n.value for n in ast.walk(fn) if isinstance(n, ast.Constant) and isinstance(n.value, str)
                   and CASE_LIT_RE.match(n.value)}) if fn else ["(無函式)"]
    print(("  ✅" if not lits else "  🔴") + f" X3 ⛔ 案件字面（{lits}）")
    if lits:
        red.append("X3")
    ch = [l for l in _git(repo, "diff", "--name-only", base, "--", "verify/").splitlines()
          if l.count("/") == 1 and l.endswith(".py") and l not in F391]   # 🔧 `W-G.9-391`：harness 二檔（F35 量之）
    print(("  ✅" if not ch else "  🔴") + f" X4 verify/ 頂層之 *.py 對基準逐位同（異 {ch}）")
    if ch:
        red.append("X4")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ───────────────────────── run ─────────────────────────

def run(repo, sbs):
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    if "k6b_stage3_run" not in ns:
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    orig = ns["k6b_stage3_run"]
    logs = []

    def wrap(*a, **k):
        t2, b2, lg = orig(*a, **k)
        logs.append(list(lg))
        return t2, b2, lg
    red, wins = [], []
    ns["k6b_stage3_run"] = wrap
    try:
        for sb in sbs:
            del logs[:]
            try:
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
                nrest = sum(1 for lg in logs for r in lg if str(r.get("結果", "")).startswith("回原狀"))
                nchk = sum(1 for lg in logs for r in lg if str(r.get("檢核", "")).startswith("回原狀"))
                nwin = sum(1 for r in (logs[0] if logs else []) if r.get("結果") == "成" and r.get("序") != "後處理")
                ok1 = nrest == 0 and nchk == 0 and bool(sg.get("g_rows"))
                wins.append(nwin)
                det = (f"段三等之呼叫 {len(logs)}·回原狀之列 {nrest}·其檢核 {nchk}·段三之成者 {nwin}·"
                       f"G 值列 {len(sg.get('g_rows') or [])}")
            except Exception as e:  # noqa: BLE001
                ok1, det = False, f"停機 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}"
            print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：本案⛔ 停機、⛔ 回原狀（{det}）")
            if not ok1:
                red.append(f"R1@{sb}")
    finally:
        ns["k6b_stage3_run"] = orig
    ok0 = sum(wins) >= 1
    print(("  ✅" if ok0 else "  🔴") + f" R0 諸退縮之段三之成者之和 {sum(wins)}（{wins}·期 ≥ 1·其查已行）")
    if not ok0:
        red.append("R0")
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
