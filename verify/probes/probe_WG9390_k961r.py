# -*- coding: utf-8 -*-
"""W-G.9-390 量測器（發單端擬·檔 F34·⛔ 由受單側改一字）：段三（街角合併重試·與末端塊合併再試同一函式）之取得街角之宗
其後未被保留者之回原狀（`K-9-61` ④·KL 裁 `2026-10-06 01:29`「E組所列的題目：均是」）。

所量之性質：經合併再試取得街角（或末端塊）之宗，其後於配地結果（試算）中未被保留者——該次合併再試視為不成、回原狀（已
  併入之土地回其原狀），由該端之下一名續試；其後之列依新態重排；同一端回原狀後仍出現者 ⇒ 停機（程式錯誤）。未保留之宗二以上
  ⇒ 由最後成者起逐一回原狀（`K-6` 典「`K-9-65` 之落地之讀法」之丑之「由最近之一次起」）。查之時點 ＝ 步驟 1〜8 之一試畢
  （⛔ 限於有後處理之群）；步驟 10 沿用其試算。

子命令（一律 python3 verify/probes/probe_WG9390_k961r.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k6b_stage3_run`）。玩具：街廓 BA（y∈[0,30]）臨正面道路 RD
           （y∈[-10,0]·中心線 y ＝ -5），RD 之另一側為 BB（y∈[-40,-10]）；各宗寬依各例。回呼：`trial_winner` ＝ G ≥ 門檻即
           當選；`alloc_state` 以 build 之全部為保留、唯各例之「⛔ 保留之式」所指者除外（G ＝ 分攤登記面積 ＋ 面積），並計其
           呼叫之數；`a_prime` ＝ a(src)。期值皆手算（各例之註）。
           K1 合併再試所得之宗（①）⛔ 保留 ⇒ 回原狀、該端之下一名續試（該群已無待後處理之土地者亦查）；K2 該端之下一名亦然
           ⇒ 停機（還原後仍出現）；K3 經道路片（②）所得者 ⇒ 道路片回原狀（⛔ 段三併出）；K4 二端皆⛔ 保留而其由相關 ⇒ 唯最後
           成者回原狀；K5 二端各自⛔ 保留 ⇒ 由最後成者起逐一回原狀（三試）；K6 回原狀後其後之列重排（前試「略·已併出」之候選
           續試）；K7 競合（`K-9-50` 題二）之一端回原狀 ⇒ 該端不成、他端取之，其後處理照舊；K8 皆保留 ⇒ 結果同改前、試算之數 ＝
           3（步驟 10 沿用其查之試算）；K9 有成者而該群無待後處理之土地 ⇒ 仍查（試算 1）；K10 查之試算中止 ⇒ 停機（無從判定）；
           K11 K4 之換名、左右鏡射；K12 K1 之旋轉 37° 並移至 TWD97 之尺度；K13 回原狀之列之內容（層級、整筆併入、試算G、門檻；
           ⛔ 受併宗、⛔ 併入量）；K14 回原狀之候選⛔ 再試（② 亦⛔）；K15 回原狀之土地與未併者同（該群有他端之成者 ⇒ 照配、
           道路片依中心線分予二側）；K16 同一端之次一名之合併與回原狀者同一組合（同一批土地）⇒ ⛔ 再施（不成）、再次一名續試；
           K17 競合（`K-9-50` 題一·隔道路相對）之一端回原狀 ⇒ 他端取之、回原狀之端之土地照配、道路片依中心線分予二側。
           〔補令一·KL `2026-10-20 08:47`「採乙」〕題一之二端同時之成（① 皆成、二端之道路互不相涉之整片皆成、切半皆成）而
           二者皆⛔ 保留 ⇒ 保留 `K-9-50` 題一 3 之序之先者（交面積大 → 並列〔小數二位〕⇒ 暫編地號小）、先還原其後者：K18 ① 皆成
           （交面積之大者後處理）；K19 交面積相等 ⇒ 暫編地號小者保留；K20 交面積之差 ＜ 0.005（小數二位相等）⇒ 並列；K21 切半
           皆成（題一 4：被還原之一端連同其半併入保留之一端）；K22 二端之道路互不相涉之整片皆成；K23 同時之成而唯保留之序之
           先者⛔ 保留 ⇒ 還原該者；K24 K21 之換名、鏡射、旋轉並移至 TWD97 之尺度；K25 同時之成之後另有後成者亦⛔ 保留 ⇒ 先還原
           該後成者（最近之一次起·同時之成⛔ 先）；K26 前試之同時之成之記於重試時去之（重試中同二端為先後二次之成 ⇒ 照最後成者）。
           P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           X1 `k6b_stage3_run` 內之字串常數（f-string 之字面部分亦計·其 docstring 除外）：舊停機之字樣（「受併宗於現態未保留」·
           以拼接立之）去之；有常數 ＝「回原狀（受併宗未保留·K-9-61 ④）」、有常數 ＝「回原狀（K-9-61 ④）」、有常數含「還原後仍出現」、
           有常數含「成者之宗之保留之查」；X2 app.py 之頂層節點對基準之相異 ＝
           `{k6b_stage3_run}`、頂層之名之集⛔ 變；X3 `k6b_stage3_run` 內⛔ 案件字面；X4 `verify/` 之 `*.py`（頂層）對基準
           逐位同。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 街角選位至配地（`run_corner_pk_k6b` ＋ `run_step_g`）⛔ 停機；段三與
           末端塊合併再試之諸紀錄中「回原狀（受併宗未保留」之列與「回原狀（K-9-61 ④）」之檢核皆 `0`；R0 諸退縮之段三之成者之
           和 ≥ `1`（其查已行·退縮 `0 m` 段三⛔ 辦者其成者 `0`）⇒ 本案之配地⛔ 變（其逐位由 `k6s3 cmp`／`F8`／`parity` 量之）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, math, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

H, RDC = "住宅區", "道路"
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
REST = "回原狀（受併宗未保留·K-9-61 ④）"
REST_CHK = "回原狀（K-9-61 ④）"
BLOCKS = {"BA": {"category": H}, "BB": {"category": H}, "RD": {"category": RDC}}
CL = {"RD": [(-40.0, -5.0), (90.0, -5.0)]}


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
    for pid, blk, cat, poly, a in parcels:
        p2 = rn(pid)
        temp.append({"暫編地號": p2, "原地號": p2.split("(")[0], "polygon_coords": [list(f(pt)) for pt in poly],
                     "所屬街廓": nm.get(blk, blk), "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0})
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


def _halt(res, phrase):
    if isinstance(res, tuple) and res and res[0] == "停機":
        return ("停機", phrase in res[1])
    return ("無停機",)


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


def _cases(ns):
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:200])
        out.append((name, got, exp))

    p1, own1, od1 = _w1()
    # K1：門檻 150；A1 之 ① ＝ 100 ＋ 60 ＝ 160 ⇒ 成；A1 於 G ＞ 150 時⛔ 保留 ⇒ 回原狀；B1 之 ① ＝ 100 ＋ 55 ＝ 155 ⇒ 成
    #   （g1、g2 皆無待後處理之土地·改前⛔ 查 ⇒ A1 成、B1 略·已定案）
    run("K1 合併再試所得之宗⛔ 保留 ⇒ 回原狀、該端之下一名續試",
        lambda: _st(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: pid == "A1(1)" and g > 150), "rows", "build", "G"),
        ([(1, "A1(1)", REST, "①", ["A2(1)"], "—"), (2, "B1(1)", "成", "①", ["B2(1)"], "免")],
         ["A1(1)", "A2(1)", "B1(1)", "C1(1)"],
         {"A1(1)": 100.0, "A2(1)": 60.0, "B1(1)": 155.0, "B2(1)": 55.0, "C1(1)": 300.0}))
    # K2：⛔ 保留之式 ＝ 150 ＜ G ＜ 200 ⇒ B1（155）亦⛔ 保留 ⇒ 同一端第二次 ⇒ 停機
    run("K2 該端之下一名亦⛔ 保留 ⇒ 停機（還原後仍出現）",
        lambda: _halt(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: 150 < g < 200), "還原後仍出現"), ("停機", True))
    # K3：A1(1)[0,10]（100）無同街廓之相鄰同一地主之宗；g1 之道路片 A9(1)（RD·x∈[0,10]·60）⇒ ② ＝ 160 ⇒ 成（A1 恆⛔ 保留 ⇒
    #   檢核之前後皆無 A1 ⇒ 過）；查 ⇒ 回原狀；B1(1)[10,20]（100）＋ B2(1)[20,30]（55）⇒ 155 成；A9 ⛔ 帶段三併出
    p3 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A9(1)", "RD", RDC, _R(0, 10, -10, 0), 60),
          ("B1(1)", "BA", H, _R(10, 20, 0, 30), 100), ("B2(1)", "BA", H, _R(20, 30, 0, 30), 55),
          ("C1(1)", "BA", H, _R(30, 50, 0, 30), 300)]
    own3 = {"A1": "g1", "A9": "g1", "B1": "g2", "B2": "g2", "C1": "g3"}

    def k3():
        r = _go(ns, p3, own3, od1, 150.0, lambda pid, g, gm: pid == "A1(1)")
        if not isinstance(r, dict):
            return r
        a9 = r["temp"]["A9(1)"]
        return r["rows"], "段三併出" in a9, round(float(a9.get("面積_m2", 0) or 0), 4), r["G"]["A1(1)"]
    run("K3 經道路片所得者（②）⇒ 道路片回原狀（⛔ 段三併出）", k3,
        ([(1, "A1(1)", REST, "②", ["A9(1)"], "—"), (2, "B1(1)", "成", "①", ["B2(1)"], "免")], False, 0.0, 100.0))
    p4, own4, od4 = _w4()
    # K4：二端皆成（A1 160、E1 160）⇒ 二者皆⛔ 保留 ⇒ 最後成者 E1 回原狀 ⇒ 重試：A1 成、E1 回原狀 ⇒ A1 保留（E1 未合併）
    run("K4 二端皆⛔ 保留而其由相關 ⇒ 唯最後成者回原狀",
        lambda: _st(_go(ns, p4, own4, od4, 150.0, _drop4), "rows", "calls"),
        ([(1, "A1(1)", "成", "①", ["A2(1)"], "免"), (2, "E1(1)", REST, "①", ["E2(1)"], "—")], 2))
    # K5：左端 A1(1)[0,5]／A2(1)[5,10]、B1(1)[10,15]（100）／B2(1)[15,20]（55）；右端 E2／E1；A1、E1 各於其 G ＞ 150 時⛔ 保留
    #   ⇒ 第一試：A1 成、B1 略、E1 成；查：A1、E1 ⇒ E1 回原狀；第二試：查 A1 ⇒ 回原狀；第三試：B1 成（155）⇒ 試算 3
    p5 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A2(1)", "BA", H, _R(5, 10, 0, 30), 60),
          ("B1(1)", "BA", H, _R(10, 15, 0, 30), 100), ("B2(1)", "BA", H, _R(15, 20, 0, 30), 55),
          ("M(1)", "BA", H, _R(20, 30, 0, 30), 500), ("E2(1)", "BA", H, _R(30, 40, 0, 30), 60),
          ("E1(1)", "BA", H, _R(40, 50, 0, 30), 100)]
    own5 = {"A1": "g1", "A2": "g1", "B1": "g2", "B2": "g2", "M": "g9", "E1": "g4", "E2": "g4"}
    od5 = _O(("BA", "左", "A1(1)"), ("BA", "左", "B1(1)"), ("BA", "右", "E1(1)"))
    run("K5 二端各自⛔ 保留 ⇒ 由最後成者起逐一回原狀",
        lambda: _st(_go(ns, p5, own5, od5, 150.0, lambda pid, g, gm: pid in ("A1(1)", "E1(1)") and g > 150),
                    "rows", "calls"),
        ([(1, "A1(1)", REST, "①", ["A2(1)"], "—"), (2, "B1(1)", "成", "①", ["B2(1)"], "免"),
          (3, "E1(1)", REST, "①", ["E2(1)"], "—")], 3))
    # K6：BA（x∈[0,30]）：g1 之 A1(1)[0,10]（100）、A2(1)[10,20]（60）、A3(1)[20,30]（80）相連；左端 A1 之 ① 併 A2、A3 ⇒ 240 成，
    #   右端 A3 ⇒ 略·已併出；A1 於 G ＞ 150 時⛔ 保留 ⇒ 回原狀；重試：A3 之 ① 併 A1、A2 ⇒ 240 成
    p6 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A2(1)", "BA", H, _R(10, 20, 0, 30), 60),
          ("A3(1)", "BA", H, _R(20, 30, 0, 30), 80)]
    own6 = {"A1": "g1", "A2": "g1", "A3": "g1"}
    run("K6 回原狀後其後之列重排（前試略·已併出之候選續試）",
        lambda: _st(_go(ns, p6, own6, _O(("BA", "左", "A1(1)"), ("BA", "右", "A3(1)")), 150.0,
                        lambda pid, g, gm: pid == "A1(1)" and g > 150), "rows", "build", "G"),
        ([(1, "A1(1)", REST, "①", ["A2(1)", "A3(1)"], "—"), (2, "A3(1)", "成", "①", ["A1(1)", "A2(1)"], "免")],
         ["A3(1)"], {"A1(1)": 100.0, "A2(1)": 60.0, "A3(1)": 240.0}))
    # K7：BA：g1 之 L1(1)[0,10]（100）／L2(1)[10,20]（60）、g9 之 M(1)[20,30]、g1 之 R2(1)[30,40]（70）／R1(1)[40,50]（100）；g1 之
    #   道路片 D9(1)（RD·x∈[0,50]·50）連之 ⇒ 同一合併群；競合（題二）交面積 L 30 ＞ R 20；① 二端皆成（160／170）⇒ L1；L1 於
    #   G ＞ 150 時⛔ 保留 ⇒ 回原狀；重試：L1 不成（檢核 回原狀）、R1 成；後處理：L1、L2 照配；D9 之北半鄰 BA ⇒ R1（G 170 ＞
    #   L1 100 ＞ L2 60·皆相鄰）、南半⛔ 鄰 B ⇒ D9 整片（50）⇒ R1 ＝ 170 ＋ 50 ＝ 220
    p7 = [("L1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("L2(1)", "BA", H, _R(10, 20, 0, 30), 60),
          ("M(1)", "BA", H, _R(20, 30, 0, 30), 500), ("R2(1)", "BA", H, _R(30, 40, 0, 30), 70),
          ("R1(1)", "BA", H, _R(40, 50, 0, 30), 100), ("D9(1)", "RD", RDC, _R(0, 50, -10, 0), 50)]
    own7 = {"L1": "g1", "L2": "g1", "R1": "g1", "R2": "g1", "D9": "g1", "M": "g9"}
    ct7 = [{"形": "二", "列": [("BA", "左", "L1(1)", 30.0), ("BA", "右", "R1(1)", 20.0)]}]

    def k7():
        r = _go(ns, p7, own7, _O(("BA", "左", "L1(1)"), ("BA", "右", "R1(1)")), 150.0,
                lambda pid, g, gm: pid == "L1(1)" and g > 150, contests=ct7)
        if not isinstance(r, dict):
            return r
        return sorted((x[1], x[2], x[5]) for x in r["rows"]), r["post"], r["G"]["R1(1)"], r["build"]
    run("K7 競合（題二）之一端回原狀 ⇒ 該端不成、他端取之", k7,
        ([("L1(1)", "未成", REST_CHK), ("R1(1)", "成", "免")], [("D9(1)", "後處理(b)", "成", "R1(1)")], 220.0,
         ["L1(1)", "L2(1)", "M(1)", "R1(1)"]))
    # K8：g1 之 A1(1)[0,10]（100）／A2(1)[10,20]（60）、道路片 A9(1)（RD·x∈[0,10]·40）；皆保留 ⇒ A1 成（①）、A9 ⇒ A1（200）；
    #   試算：查 1 ＋ 後處理之整批之檢核 2 ＝ 3（步驟 10 沿用查之試算·改前：步驟 10 之試算 1 ＋ 2 ＝ 3）
    p8 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A2(1)", "BA", H, _R(10, 20, 0, 30), 60),
          ("A9(1)", "RD", RDC, _R(0, 10, -10, 0), 40), ("M(1)", "BA", H, _R(20, 50, 0, 30), 500)]
    own8 = {"A1": "g1", "A2": "g1", "A9": "g1", "M": "g9"}
    run("K8 皆保留 ⇒ 結果同改前、試算 3（步驟 10 沿用其查之試算）",
        lambda: _st(_go(ns, p8, own8, _O(("BA", "左", "A1(1)")), 150.0, lambda pid, g, gm: False),
                    "rows", "post", "G", "calls"),
        ([(1, "A1(1)", "成", "①", ["A2(1)"], "免")], [("A9(1)", "後處理(b)", "成", "A1(1)")],
         {"A1(1)": 200.0, "A2(1)": 60.0, "A9(1)": 40.0, "M(1)": 500.0}, 3))
    # K9：K1 之形而皆保留 ⇒ A1 成、B1 略；g1 無待後處理之土地 ⇒ 仍查（試算 1·改前 0）
    run("K9 有成者而該群無待後處理之土地 ⇒ 仍查（試算 1）",
        lambda: _st(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: False), "rows", "calls"),
        ([(1, "A1(1)", "成", "①", ["A2(1)"], "免"), (2, "B1(1)", "略·已定案", "—", [], "—")], 1))
    # K10：查之試算中止（任一宗 G ＞ 150 ⇒ 配地中止）⇒ 停機（⛔ 以之為保留、⛔ 以之為未保留）
    run("K10 查之試算中止 ⇒ 停機（無從判定）",
        lambda: _halt(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: False,
                          err_if=lambda gm: any(v > 150 for v in gm.values())), "成者之宗之保留之查"), ("停機", True))
    # K11：K4 之換名（BA→QZ、A→P、E→W、M→N、g1→h7、g4→h2）、左右鏡射（x → 50 − x·A 在右、E 在左·端之名隨之）⇒ 同 K4
    nm11 = {"BA": "QZ", "A1": "P1", "A2": "P2", "E1": "W1", "E2": "W2", "M": "N", "g1": "h7", "g4": "h2", "g9": "h9"}
    run("K11 K4 之換名、左右鏡射 ⇒ 同 K4",
        lambda: _st(_go(ns, p4, own4, _O(("BA", "右", "A1(1)"), ("BA", "左", "E1(1)")), 150.0, _drop4,
                        T=(0.0, True, (0.0, 0.0)), names=nm11), "rows", "calls"),
        ([(1, "A1(1)", "成", "①", ["A2(1)"], "免"), (2, "E1(1)", REST, "①", ["E2(1)"], "—")], 2))
    # K12：K1 之旋轉 37° 並移至 (303000, 2650000)（TWD97 之尺度）⇒ 同 K1
    run("K12 K1 之旋轉並移至 TWD97 之尺度 ⇒ 同 K1",
        lambda: _st(_go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: pid == "A1(1)" and g > 150,
                        T=(37.0, False, (303000.0, 2650000.0))), "rows", "build"),
        ([(1, "A1(1)", REST, "①", ["A2(1)"], "—"), (2, "B1(1)", "成", "①", ["B2(1)"], "免")],
         ["A1(1)", "A2(1)", "B1(1)", "C1(1)"]))

    # K13：K1 之回原狀之列：層級 ①、整筆併入 [A2(1)]、試算G 160.0、門檻 150.0；受併宗 —、併入量 {}、檢核 —
    def k13():
        r = _go(ns, p1, own1, od1, 150.0, lambda pid, g, gm: pid == "A1(1)" and g > 150)
        if not isinstance(r, dict):
            return r
        x = [y for y in r["log"] if y.get("結果") == REST][0]
        return (x["層級"], list(x["整筆併入"]), x["試算G"], x["門檻"], x["受併宗"], x["併入量"], x["檢核"])
    run("K13 回原狀之列之內容", k13, ("①", ["A2(1)"], 160.0, 150.0, "—", {}, "—"))
    # K14：K1 ＋ g1 之道路片 A9(1)（RD·x∈[0,10]·40）；A1 於 150 ＜ G ＜ 180 時⛔ 保留 ⇒ ① 成（160）而回原狀；其 ②（200·保留）
    #   ⛔ 再試 ⇒ B1 成
    p14 = p1 + [("A9(1)", "RD", RDC, _R(0, 10, -10, 0), 40)]
    own14 = dict(own1, A9="g1")
    run("K14 回原狀之候選⛔ 再試（② 亦⛔）",
        lambda: _st(_go(ns, p14, own14, od1, 150.0, lambda pid, g, gm: pid == "A1(1)" and 150 < g < 180), "rows"),
        ([(1, "A1(1)", REST, "①", ["A2(1)"], "—"), (2, "B1(1)", "成", "①", ["B2(1)"], "免")],))
    # K15：g1 之 A1(1)[0,10]（100）／A2(1)[10,20]（60）（BA 左端）、道路片 D(1)（RD·x∈[0,10]·40）、BB 之 F1(1)[0,10]（100）／
    #   F2(1)[10,20]（70）（BB 左端）；A1 於 G ＞ 150 時⛔ 保留 ⇒ 回原狀；F1 成（170）；後處理：A1、A2 照配（保留），D 之北半 ⇒
    #   A1（唯 A1 與之相鄰）、南半 ⇒ F1 ⇒ A1 ＝ 100 ＋ 20 ＝ 120、F1 ＝ 170 ＋ 20 ＝ 190
    p15 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("A2(1)", "BA", H, _R(10, 20, 0, 30), 60),
           ("M(1)", "BA", H, _R(20, 50, 0, 30), 500), ("D(1)", "RD", RDC, _R(0, 10, -10, 0), 40),
           ("F1(1)", "BB", H, _R(0, 10, -40, -10), 100), ("F2(1)", "BB", H, _R(10, 20, -40, -10), 70),
           ("N(1)", "BB", H, _R(20, 50, -40, -10), 500)]
    own15 = {"A1": "g1", "A2": "g1", "D": "g1", "F1": "g1", "F2": "g1", "M": "g9", "N": "g8"}
    run("K15 回原狀之土地與未併者同（照配、道路片依中心線分予二側）",
        lambda: _st(_go(ns, p15, own15, _O(("BA", "左", "A1(1)"), ("BB", "左", "F1(1)")), 150.0,
                        lambda pid, g, gm: pid == "A1(1)" and g > 150), "rows", "post", "G"),
        ([(1, "A1(1)", REST, "①", ["A2(1)"], "—"), (2, "F1(1)", "成", "①", ["F2(1)"], "免")],
         [("D(1)", "後處理(b)", "成", ("A1(1)", "F1(1)"))],
         {"A1(1)": 120.0, "A2(1)": 60.0, "D(1)": 40.0, "F1(1)": 190.0, "F2(1)": 70.0, "M(1)": 500.0, "N(1)": 500.0}))
    # K16：K1 之形，段二序 A1 → A2 → B1（A1、A2 同屬 g1·皆左端之候選）；g1 之宗於 G ＞ 150 時⛔ 保留 ⇒ A1 回原狀；A2 之 ①
    #   併 A1 ⇒ 組合 {A1, A2} 與回原狀者同 ⇒ ⛔ 再施（未成·檢核 回原狀）；B1 ⇒ 155 成（⛔ 停機）
    run("K16 次一名之合併與回原狀者同一組合 ⇒ ⛔ 再施、再次一名續試",
        lambda: _st(_go(ns, p1, own1, _O(("BA", "左", "A1(1)"), ("BA", "左", "A2(1)"), ("BA", "左", "B1(1)")), 150.0,
                        lambda pid, g, gm: pid in ("A1(1)", "A2(1)") and g > 150), "rows", "build"),
        ([(1, "A1(1)", REST, "①", ["A2(1)"], "—"), (2, "A2(1)", "未成", "①", ["A1(1)"], REST_CHK),
          (3, "B1(1)", "成", "①", ["B2(1)"], "免")], ["A1(1)", "A2(1)", "B1(1)", "C1(1)"]))
    # K17：K15 之地而 BA 左端與 BB 左端為競合（`K-9-50` 題一·交面積 A 30 ＞ F 20）；① 二端皆成（160／170）⇒ 二端皆取之；
    #   A1 ⛔ 保留 ⇒ 回原狀；重試：A1 之 ① 不成（回原狀）⇒ 只一端成 ⇒ F1；A1 之整片（A2、D·②）亦不成（回原狀）；後處理：
    #   A1、A2 照配；D 之北半 ⇒ 題一之未得之一端之候選 A1、南半 ⇒ F1 ⇒ A1 ＝ 120、F1 ＝ 190
    ct17 = [{"形": "一", "列": [("BA", "左", "A1(1)", 30.0), ("BB", "左", "F1(1)", 20.0)]}]

    def k17():
        r = _go(ns, p15, own15, _O(("BA", "左", "A1(1)"), ("BB", "左", "F1(1)")), 150.0,
                lambda pid, g, gm: pid == "A1(1)" and g > 150, contests=ct17)
        if not isinstance(r, dict):
            return r
        return sorted((x[1], x[2], x[5]) for x in r["rows"]), r["post"], r["G"]["A1(1)"], r["G"]["F1(1)"]
    run("K17 競合（題一）之一端回原狀 ⇒ 他端取之、道路片依中心線分予二側", k17,
        ([("A1(1)", "未成", REST_CHK), ("F1(1)", "成", "免")], [("D(1)", "後處理(b)", "成", ("A1(1)", "F1(1)"))],
         120.0, 190.0))

    # ── 補令一（R-2′·KL `2026-10-20 08:47` 採乙）：題一之二端同時之成而二者皆⛔ 保留 ──
    # K18：K15 之地；競合（題一）交面積 A 20 ＜ F 30；① 二端皆成（160／170·同一次所施）；A1、F1 於二者之 G 皆 ＞ 150 時皆⛔ 保留
    #   ⇒ 保留 F 端（交面積大）、先還原 A 端（現碼：先還原後處理之 F 端）；重試：A1 之 ① 不成（回原狀）⇒ 只一端成 ⇒ F1（170·
    #   A1 ＝ 100 ⇒ 皆保留）；A1 之整片（A2、D·②）亦不成；後處理：A1、A2 照配；D 之北半 ⇒ A1、南半 ⇒ F1 ⇒ A1 120、F1 190
    #   （現碼之果：A1 180、F1 120）
    def _drop18(pid, g, gm):
        return pid in ("A1(1)", "F1(1)") and gm.get("A1(1)", 0) > 150 and gm.get("F1(1)", 0) > 150

    def _k18(ct, od, dropf=_drop18, **kw):
        r = _go(ns, p15, own15, od, 150.0, dropf, contests=ct, **kw)
        if not isinstance(r, dict):
            return r
        return sorted((x[1], x[2], x[5]) for x in r["rows"]), r["post"], r["G"]["A1(1)"], r["G"]["F1(1)"]
    odAF = _O(("BA", "左", "A1(1)"), ("BB", "左", "F1(1)"))
    odFA = _O(("BB", "左", "F1(1)"), ("BA", "左", "A1(1)"))
    keepF = ([("A1(1)", "未成", REST_CHK), ("F1(1)", "成", "免")], [("D(1)", "後處理(b)", "成", ("A1(1)", "F1(1)"))],
             120.0, 190.0)
    keepA = ([("A1(1)", "成", "免"), ("F1(1)", "未成", REST_CHK)], [("D(1)", "後處理(b)", "成", ("A1(1)", "F1(1)"))],
             180.0, 120.0)
    run("K18 題一 ① 二端同時之成而皆⛔ 保留 ⇒ 保留交面積大之一端、先還原他端",
        lambda: _k18([{"形": "一", "列": [("BA", "左", "A1(1)", 20.0), ("BB", "左", "F1(1)", 30.0)]}], odAF), keepF)
    # K19：K18 之地而交面積相等（25／25）、段二序 F1 先 ⇒ 並列 ⇒ 暫編地號小者（A1）保留、先還原 F 端（現碼：先還原後處理之 A 端）
    run("K19 交面積相等 ⇒ 暫編地號小者保留、先還原他端",
        lambda: _k18([{"形": "一", "列": [("BB", "左", "F1(1)", 25.0), ("BA", "左", "A1(1)", 25.0)]}], odFA), keepA)
    # K20：交面積 F 30.004、A 30.0（小數二位相等 ⇒ 並列·同 `K-9-50` 題一 3 之判）、段二序 F1 先 ⇒ A1 保留、先還原 F 端
    #   （以原值比 ⇒ F 端保留）
    run("K20 交面積之差在小數二位之內 ⇒ 並列（暫編地號小者保留）",
        lambda: _k18([{"形": "一", "列": [("BB", "左", "F1(1)", 30.004), ("BA", "左", "A1(1)", 30.0)]}], odFA), keepA)
    # K21（請示之圖五之形）：BA 之 g1 之 A1(1)[0,10]（100）、BB 之 g1 之 F1(1)[0,10]（100）、g1 之道路片 D(1)（RD·x∈[0,10]·80·
    #   依中心線分為北半、南半各 40）；他人 M(1)、N(1)；門檻 138；交面積 A 30 ＞ F 20、段二序 F1 先；切半：二端各 140 ⇒ 皆成
    #   （二端各配一宗）；二者之 G 皆 ＞ 130 ⇒ 皆⛔ 保留 ⇒ 保留 A 端、先還原 F 端（現碼：先還原後處理之 A 端）；重試：F1 之切半
    #   不成（回原狀）、A1 成（140）⇒ 題一 4：F1 連同其半依原位次（F1 140·A1 140 ⇒ 皆⛔ 保留）不能 ⇒ 併入 A1 ⇒ A1 ＝ 140 ＋ 40
    #   ＋ 100 ＝ 280（F1 去之）
    p21 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("M(1)", "BA", H, _R(10, 50, 0, 30), 500),
           ("D(1)", "RD", RDC, _R(0, 10, -10, 0), 80),
           ("F1(1)", "BB", H, _R(0, 10, -40, -10), 100), ("N(1)", "BB", H, _R(10, 50, -40, -10), 500)]
    own21 = {"A1": "g1", "D": "g1", "F1": "g1", "M": "g9", "N": "g8"}
    ct21 = [{"形": "一", "列": [("BB", "左", "F1(1)", 20.0), ("BA", "左", "A1(1)", 30.0)]}]

    def _drop21(pid, g, gm):
        return pid in ("A1(1)", "F1(1)") and gm.get("A1(1)", 0) > 130 and gm.get("F1(1)", 0) > 130

    def k21(**kw):
        r = _go(ns, p21, own21, odFA, 138.0, _drop21, contests=ct21, **kw)
        if not isinstance(r, dict):
            return r
        return sorted((x[1], x[2], x[5]) for x in r["rows"]), r["post"], r["G"]["A1(1)"], r["build"]
    exp21 = ([("A1(1)", "成", "通過"), ("F1(1)", "未成", REST_CHK)], [("F1(1)", "題一 4", "成", "A1(1)")], 280.0,
             ["A1(1)", "M(1)", "N(1)"])
    run("K21 切半二端各配一宗而皆⛔ 保留 ⇒ 保留交面積大之一端、被還原之一端連同其半併入之", k21, exp21)
    # K22：BA 之 g1 之 A1(1)[0,10]（100）與其道路片 DA(1)（RD·x∈[0,10]·40）；BB 之 g1 之 F1(1)[20,30]（100）與其道路片 DF(1)（RD·
    #   x∈[20,30]·40）（二道路片⛔ 相鄰 ⇒ 互不相涉）；BA 之 g1 之 X(1)[20,30]（30·臨 DF·⛔ 鄰 A1）與 BA 北側之街廓 BC 之 g1 之
    #   Q(1)（x∈[0,30]·y∈[30,60]·200·臨 A1、X）連之 ⇒ 同一合併群；他人 M(1)、M2(1)、N(1)、N2(1)；門檻 138；交面積 A 20 ＜ F 30、
    #   段二序 A1 先；整片（無共同之道路）：二端各 140 ⇒ 皆成（同一次所施）；二者之 G 皆 ＞ 130 ⇒ 皆⛔ 保留 ⇒ 保留 F 端、
    #   先還原 A 端（現碼：先還原後處理之 F 端）；重試：A1 之整片不成（回原狀）、F1 成
    p22 = [("A1(1)", "BA", H, _R(0, 10, 0, 30), 100), ("M(1)", "BA", H, _R(10, 20, 0, 30), 500),
           ("X(1)", "BA", H, _R(20, 30, 0, 30), 30), ("M2(1)", "BA", H, _R(30, 50, 0, 30), 500),
           ("Q(1)", "BC", H, _R(0, 30, 30, 60), 200),
           ("DA(1)", "RD", RDC, _R(0, 10, -10, 0), 40), ("DF(1)", "RD", RDC, _R(20, 30, -10, 0), 40),
           ("N(1)", "BB", H, _R(0, 20, -40, -10), 500), ("F1(1)", "BB", H, _R(20, 30, -40, -10), 100),
           ("N2(1)", "BB", H, _R(30, 50, -40, -10), 500)]
    own22 = {"A1": "g1", "X": "g1", "Q": "g1", "DA": "g1", "DF": "g1", "F1": "g1", "M": "g9", "M2": "g9", "N": "g8",
             "N2": "g8"}

    def k22():
        r = _go(ns, p22, own22, odAF, 138.0, _drop21, extra={"BC": {"category": H}},
                contests=[{"形": "一", "列": [("BA", "左", "A1(1)", 20.0), ("BB", "左", "F1(1)", 30.0)]}])
        if not isinstance(r, dict):
            return r
        return sorted((x[1], x[2], x[5]) for x in r["rows"])
    run("K22 二端之道路互不相涉之整片同時之成而皆⛔ 保留 ⇒ 保留交面積大之一端", k22,
        [("A1(1)", "未成", REST_CHK), ("F1(1)", "成", "通過")])
    # K23：K18 之地與競合（交面積 A 20 ＜ F 30）；唯 F1 於其 G ＞ 150 時⛔ 保留（A1 保留）⇒ 同時之成而唯保留之序之先者（F）⛔ 保留
    #   ⇒ 還原 F 端（⛔ 因同時之成而改還原 A 端）；重試：F1 不成（回原狀）、A1 成（160）；後處理：F1、F2 照配；D 之北半 ⇒ A1、
    #   南半 ⇒ F1 ⇒ A1 180、F1 120
    run("K23 同時之成而唯保留之序之先者⛔ 保留 ⇒ 還原該者",
        lambda: _k18([{"形": "一", "列": [("BA", "左", "A1(1)", 20.0), ("BB", "左", "F1(1)", 30.0)]}], odAF,
                     dropf=lambda pid, g, gm: pid == "F1(1)" and g > 150), keepA)
    # K24：K21 之換名（BA→QZ、BB→QY、RD→QD、A1→P1、F1→W1、D→E9、M→Q5、N→Q6、g1→h7、g8→h8、g9→h9·暫編地號之序 P ＜ W 同 A ＜ F）、
    #   左右鏡射、旋轉 41° 並移至 (304000, 2651000)（TWD97 之尺度）⇒ 同 K21
    nm24 = {"BA": "QZ", "BB": "QY", "RD": "QD", "A1": "P1", "F1": "W1", "D": "E9", "M": "Q5", "N": "Q6",
            "g1": "h7", "g8": "h8", "g9": "h9"}
    run("K24 K21 之換名、鏡射、旋轉並移至 TWD97 之尺度 ⇒ 同 K21",
        lambda: k21(T=(41.0, True, (304000.0, 2651000.0)), names=nm24), exp21)
    # K25（補令一之唯讀審查之例 C2）：K18 之地 ＋ BA 右端 g4 之 E2(1)[30,40]（60）／E1(1)[40,50]（100）（M 縮為 [20,30]）；段二序 A1、F1、
    #   E1；交面積 A 20 ＜ F 30；E1 於其 G ＞ 150 時⛔ 保留；A1、F1 於 A1、F1、E1 之 G 皆 ＞ 150 時皆⛔ 保留 ⇒ 第一試：A1 160／F1 170
    #   （同一次）、E1 160 ⇒ 三者皆⛔ ⇒ 最後成者 E1（非同時之成）⇒ 還原 E1；第二試：A1、F1 成、E1 回原狀（100）⇒ 皆保留 ⇒ 止；
    #   後處理：D 之北半 ⇒ A1、南半 ⇒ F1 ⇒ A1 180、F1 190（若先處理同時之成 ⇒ 還原 A 端 ⇒ 終 A1 120）
    p25 = [r for r in p15 if r[0] != "M(1)"] + [("M(1)", "BA", H, _R(20, 30, 0, 30), 500),
                                                ("E2(1)", "BA", H, _R(30, 40, 0, 30), 60),
                                                ("E1(1)", "BA", H, _R(40, 50, 0, 30), 100)]
    own25 = dict(own15, E1="g4", E2="g4")

    def k25():
        r = _go(ns, p25, own25, _O(("BA", "左", "A1(1)"), ("BB", "左", "F1(1)"), ("BA", "右", "E1(1)")), 150.0,
                lambda pid, g, gm: (pid == "E1(1)" and g > 150) or
                (pid in ("A1(1)", "F1(1)") and all(gm.get(k, 0) > 150 for k in ("A1(1)", "F1(1)", "E1(1)"))),
                contests=[{"形": "一", "列": [("BA", "左", "A1(1)", 20.0), ("BB", "左", "F1(1)", 30.0)]}])
        if not isinstance(r, dict):
            return r
        return sorted((x[1], x[2], x[5]) for x in r["rows"]), r["G"]["A1(1)"], r["G"]["F1(1)"], r["G"]["E1(1)"]
    run("K25 同時之成之後另有後成者亦⛔ 保留 ⇒ 先還原該後成者", k25,
        ([("A1(1)", "成", "免"), ("E1(1)", REST, "—"), ("F1(1)", "成", "免")], 180.0, 190.0, 100.0))
    # K26（補令一之唯讀審查之例 C3）：BC（BA 之北）之 g1 之 K(1)[0,10]（100）、g5 之 J(1)[10,20]（100）／J2(1)[20,30]（60）、他人 Z；
    #   BA 之 g1 之 A1(1)（x∈[0,10]·y∈[0,20]·100）與其北之 g1 之片 P(1)（道路類·屬 BA·x∈[0,10]·y∈[20,30]·60·連 A1 與 K）、他人 M、
    #   g7 之 L2(1)／L(1)（右端）；g1 之道路片 D(1)（60）、BB 之 g1 之 F1(1)／F2(1)（70）；段二序 BC 左 J、BC 左 K、BA 左 A1、BB 左 F1、
    #   BA 右 L；競合（題一）A 30 ＞ F 20；門檻 150。J 於其 G ＞ 150 時⛔ 保留；A1、F1 於 K、L、A1、F1 之 G 皆 ＞ 150 時皆⛔ 保留 ⇒
    #   第一試：J 160、A1（＋P）160／F1（＋F2）170 同一次、L 160 ⇒ 唯 J ⛔ ⇒ 還原 J；第二試：K（＋P）160 先取 P ⇒ A1 之 ① 無地 ⇒
    #   F1 先成（①）、A1 後成（②·＋D）＝ 先後二次；A1、F1 皆⛔ ⇒ 最後成者 A1 ⇒ 還原 A1（前試之同時之成之記若⛔ 去 ⇒ 改還原 F1）；
    #   第三試：F1 成、A1 不成（回原狀）⇒ 皆保留；後處理：D 之北半 ⇒ A1、南半 ⇒ F1 ⇒ A1 130、F1 200
    p26 = [("K(1)", "BC", H, _R(0, 10, 30, 60), 100), ("J(1)", "BC", H, _R(10, 20, 30, 60), 100),
           ("J2(1)", "BC", H, _R(20, 30, 30, 60), 60), ("Z(1)", "BC", H, _R(30, 50, 30, 60), 500),
           ("A1(1)", "BA", H, _R(0, 10, 0, 20), 100), ("P(1)", "BA", RDC, _R(0, 10, 20, 30), 60),
           ("M(1)", "BA", H, _R(10, 30, 0, 30), 500), ("L2(1)", "BA", H, _R(30, 40, 0, 30), 60),
           ("L(1)", "BA", H, _R(40, 50, 0, 30), 100), ("D(1)", "RD", RDC, _R(0, 10, -10, 0), 60),
           ("F1(1)", "BB", H, _R(0, 10, -40, -10), 100), ("F2(1)", "BB", H, _R(10, 20, -40, -10), 70),
           ("N(1)", "BB", H, _R(20, 50, -40, -10), 500)]
    own26 = {"K": "g1", "A1": "g1", "P": "g1", "D": "g1", "F1": "g1", "F2": "g1", "J": "g5", "J2": "g5", "Z": "g6",
             "M": "g9", "L": "g7", "L2": "g7", "N": "g8"}

    def _drop26(pid, g, gm):
        if pid == "J(1)":
            return g > 150
        return pid in ("A1(1)", "F1(1)") and all(gm.get(k, 0) > 150 for k in ("K(1)", "L(1)", "A1(1)", "F1(1)"))

    def k26():
        r = _go(ns, p26, own26, _O(("BC", "左", "J(1)"), ("BC", "左", "K(1)"), ("BA", "左", "A1(1)"), ("BB", "左", "F1(1)"),
                                   ("BA", "右", "L(1)")), 150.0, _drop26, extra={"BC": {"category": H}},
                contests=[{"形": "一", "列": [("BA", "左", "A1(1)", 30.0), ("BB", "左", "F1(1)", 20.0)]}])
        if not isinstance(r, dict):
            return r
        return (sorted((x[1], x[2], x[5]) for x in r["rows"] if x[1] in ("A1(1)", "F1(1)")), r["G"]["A1(1)"],
                r["G"]["F1(1)"])
    run("K26 前試之同時之成之記於重試時去之", k26,
        ([("A1(1)", "未成", REST_CHK), ("F1(1)", "成", "免")], 130.0, 200.0))
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
    cnt = {"結果「" + REST + "」": sum(1 for c in consts if c == REST),
           "檢核「" + REST_CHK + "」": sum(1 for c in consts if c == REST_CHK),
           "還原後仍出現": sum(1 for c in consts if "還原後仍出現" in c),
           "成者之宗之保留之查": sum(1 for c in consts if "成者之宗之保留之查" in c)}
    left = sum(1 for c in consts if gone in c)
    ok1 = bool(fn) and left == 0 and all(v >= 1 for v in cnt.values())
    print(("  ✅" if ok1 else "  🔴") + f" X1 舊停機之字樣去之（殘 {left}）、四字樣皆見（{cnt}）")
    if not ok1:
        red.append("X1")
    ta, tb = _top(app), _top(old)
    diff = sorted(k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k))
    ok2 = diff == ["k6b_stage3_run"] and set(ta) == set(tb)
    print(("  ✅" if ok2 else "  🔴") + f" X2 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
    if not ok2:
        red.append("X2")
    lits = sorted({n.value for n in ast.walk(fn) if isinstance(n, ast.Constant) and isinstance(n.value, str)
                   and CASE_LIT_RE.match(n.value)}) if fn else ["(無函式)"]
    print(("  ✅" if not lits else "  🔴") + f" X3 ⛔ 案件字面（{lits}）")
    if lits:
        red.append("X3")
    ch = [l for l in _git(repo, "diff", "--name-only", base, "--", "verify/").splitlines()
          if l.count("/") == 1 and l.endswith(".py")]
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
                nrest = sum(1 for lg in logs for r in lg if str(r.get("結果", "")).startswith("回原狀（受併宗未保留"))
                nchk = sum(1 for lg in logs for r in lg if r.get("檢核") == REST_CHK)
                nwin = sum(1 for r in (logs[0] if logs else []) if r.get("結果") == "成" and r.get("序") != "後處理")
                ok1 = nrest == 0 and nchk == 0 and bool(sg.get("g_rows"))
                wins.append(nwin)
                det = (f"段三等之呼叫 {len(logs)}·回原狀之列 {nrest}·其檢核 {nchk}·段三之成者 {nwin}·"
                       f"G 值列 {len(sg.get('g_rows') or [])}")
            except Exception as e:  # noqa: BLE001
                ok1, det = False, f"停機 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}"
            print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：本案⛔ 觸回原狀（{det}）")
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
