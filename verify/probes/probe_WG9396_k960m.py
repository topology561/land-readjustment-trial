# -*- coding: utf-8 -*-
"""W-G.9-396 量測器（發單端擬·檔 F43·⛔ 由受單側改一字）：三個以上之末端塊（`K-9-60` ②·KL `2026-10-05 22:59`·
`2026-10-25 03:58`「二是」·`10:18`「一甲」·`2026-10-26 22:09`「第一題：乙」）與其互相等待之已排定之先後（KL `2026-10-30 23:02`
「丁」·`2026-10-31 07:52`「一乙、二是」）。

所量之性質：
  ① 同一合併群之未達候選分屬三個以上之末端塊 ⇒ ⛔ 停機；其競合之形 ＝「多」，列 ＝ 各端之首個候選。
  ② 題一之步驟推延至多端：各端先以本街廓內之土地；仍需要者，道路片依中心線、餘依所臨分給各端；**拿得下之端定案、拿不下之端
     不得**；唯「分給各端後全部拿不下」（以共用道路、公設地之端群計·一乙）時改以整片各試，能達標者二以上 ⇒ 應分配面積 →
     重劃前面積 → 暫編地號之先者一端得。不得之端之分 ⇒ 題一 4（照配 → 連同其分併入 → K-9-48 七項）。
  ③ 他人先定案之端自競合去之；餘二端 ⇒ 依二端之形（隔道路相對 ⇒ 題一）。
  ④ 二是：互相等待之人皆只跨兩端者，結果與現行（主線 `9fd3427`）逐例同（含先處理者之紀錄）。
  ⑤ 換名、旋轉、鏡射、TWD97 之尺度 ⇒ 除名稱外同。

示意之數（KL 10-30 23:02）：應分配面積 G ＝ 0.6 ×（重劃前面積 ＋ 併入之 a′）＜ 重劃前面積；a′ ＝ 來源之重劃前面積（地價均一）。

子命令（一律 python3 verify/probes/probe_WG9396_k960m.py <子命令> …）：
  selftest <repo>
           世界 W3：三街廓縱列 BA（y∈[0,30]）、BB（[-40,-10]）、BC（[-80,-50]），其間道路 RA（[-10,0]·中心線 y＝-5）、RB
           （[-50,-40]·中心線 y＝-45）；丁：D1 BA、Da RA、D2 BB、Db RB、D3 BC（皆 x∈[0,5]）；他人之片居 x∈[5,40]。三端皆左端·
           各端之候選唯丁之片（H5 另有庚）。期值皆手算：
           H1 部分拿得下（a 皆 100·門檻 BA 100／BB 110／BC 100）：分給各端 ⇒ Da、Db 依中心線各半；G：BA 0.6×150＝90、
              BB 0.6×200＝120、BC 90 ⇒ BB 定案（D2 ＋ 50 ＋ 50）；BA、BC 不得，其半依題一 4 照配（D1 ＋ 50、D3 ＋ 50）；
              皆未達 BA、BC（⛔ 改整片·⛔ 停機）。
           H2 全部拿不下 ⇒ 整片各試（D1 150、餘 100·門檻皆 140）：分給 ⇒ 120／120／90 皆不達；整片 BA 0.6×250＝150 ✓、
              BB 0.6×300＝180 ✓、BC 0.6×200＝120 ✗ ⇒ 二端能達標 ⇒ G 大者 BB（D2 ＋ 200）得；BA、BC 不得（⛔ 依原位次之先 BA）。
           H3 端群各判（世界 W4：BA、RA、BB、BC〔與 BB 直接相鄰·D2 與 D3 共邊〕、RC、BD；丁：D1 BA、Da RA、D2 BB、D3 BC、
              Dc RC、D4 BD；a 皆 100 唯 D4 110；門檻 BA 85／BB 95／BC 95／BD 100）：群一 {BA, BB}（共 Da）：分給 ⇒ BA 90 ✓、
              BB 90 ✗ ⇒ BA 定案（D1 ＋ 50）、BB 不得而照配其半（D2 ＋ 50）；群二 {BC, BD}（共 Dc）：分給 ⇒ 90 ✗、96 ✗ ⇒ 整片
              BC 120 ✓、BD 126 ✓ ⇒ BD（D4 ＋ 100）得（⛔「全部拿不下」以全部之端計 ⇒ 群二無得者〔KL 10-26 第一題未擇之甲〕）。
           H4 H3 之換名（街廓、地號）、旋轉 37°、鏡射、TWD97 之尺度 ⇒ 除名稱外同 H3。
           H5 他人先定案之端去之（W3 ＋ 庚 X、X2 於 BA·BA 之候選序 X、D1；a 皆 100；門檻 BA 100／BB 110／BC 100）：X 以 X2 併入
              120 先得 BA ⇒ 丁之競合餘 BB、BC ⇒ 題一：Db 共用而依中心線各半、Da 唯 BB 需要而整片 ⇒ BB 0.6×250＝150 ✓、
              BC 90 ✗ ⇒ BB 定案（D2 ＋ 150）、BC 照配其半（D3 ＋ 50）；皆未達唯 BC。
           H8 一乙（世界 B1〜B4 直接相鄰·F 跨四端、Z 跨三端、D 跨二端·門檻不可達·指數與序鍵如 `T8` 之註）：第一次
              互相等待（F、D、Z·兩兩成圈）⇒ 序鍵之先者 F 先處理、唯 D（持 F 之未至之列）延後；第二次 F、Z ⇒ F 與 Z 之先後
              未記 ⇒ 依現行重比 ⇒ Z 於共同之端（a、e）皆第 1 名而先（⛔ 一甲之「F 先於當次每一人」⇒ F 先）。先處理之列
              之候選之首二 ＝ [F1(1), Z4(1)]。
           H6 主線（二端）之停機之形「同一合併群之候選分屬 3 個末端塊」⛔ 再現（H1 之世界）。
           E2 二端之隨機世界（倉外之生成式·種子固定·每位地主皆只跨兩端·皆有互相等待）31 例：結果（宗地之面積與併出、
              保留、紀錄之列、先處理者之紀錄）之摘要 ＝ 主線 `9fd3427` 之實跑之摘要（期值之出處·二是 ⇒ 須同現行）。
  wiring   <repo> <基準 commit>
           W1 `end_block_merge_run` 之停機之訊息⛔ 含「三個以上之末端塊」；其碼含 `'多'`；W2 `k6b_stage3_run` 有巢狀
           `_ct_multi`（恰一）且 `_contest` 呼之；`_k950_rows` 之停機⛔ 含「列數 ≠ 2」；W3 `_k950_rows` 內有 `_pre396` 之記
           （`.add`）唯在「當次之人有形多」之判之後（其判之 `if` 之字面恰一）；W4 頂層之名對基準⛔ 增減；W5 所改之二節點內⛔ 新增
           案件字面。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設 `3.5`、`0.0`）：R1 合併再試之標的 []、競合 無（本案⛔ 觸三個以上之末端塊）。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, copy, hashlib, io, json, math, os, random, re, subprocess, sys

H = "住宅區"
BUR = 0.6
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
GONE_HIT3 = "".join(("三個以", "上之末", "端塊"))
GONE_ROWS = "".join(("列數", " ≠ ", "2"))
PICK2 = [[0, 4, "ca759c4d782bd240"], [0, 129, "7ac8aef4b46590e0"], [0, 199, "8a1f19f6681e24db"], [0, 261, "2906b2d393a4164f"], [0, 442, "8ff5a33728962d17"], [0, 610, "0e0a442e62ec4702"], [0, 651, "43f5b22220bc112a"], [0, 880, "0d82c2ceee9b5176"], [0, 967, "0594d93758f7886c"], [0, 968, "667243243083ed28"], [0, 1005, "1607204214a2573e"], [0, 1016, "d01168b871b08761"], [0, 1062, "54f0e0933630633d"], [0, 1066, "ff1df1cc3f0cd4cb"], [0, 1090, "fffa1cbc021560c5"], [0, 1091, "7d44bf7f0d37bd37"], [0, 1122, "20d75092702085ff"], [0, 1132, "15e4eb97b8917b03"], [0, 1230, "f97bb15844e6a48e"], [0, 1240, "0ab9466289213bef"], [0, 1252, "379c716b0e184dff"], [0, 1254, "ab6f660f0ef5eb78"], [0, 1362, "0dda75b7fe9d8e69"], [0, 1380, "9b11ad28f94f71fd"], [1, 56, "b2e5e321f2d52ff1"], [1, 105, "bb76e0703785f05d"], [1, 204, "f4213a35a9e7cae1"], [1, 206, "6e2006947ceb4c8e"], [1, 216, "e505aa594f2394df"], [1, 261, "932b4fcda302891c"], [2, 20, "94ee6fbba25862f9"]]
CFG2 = [{"nr": 3, "nc": 2, "nlink": 6}, {"nr": 4, "nc": 3, "nlink": 10}, {"nr": 3, "nc": 3, "nlink": 12}]


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns


def _tp(pid, blk, cat, poly, a, area=0.0):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": float(area)}


def _cbs(targets):
    def g(x):
        return BUR * (float(x.get("分攤登記面積_m2", 0) or 0) + float(x.get("面積_m2", 0) or 0))

    def a_prime(src, dst):
        return float(src.get("分攤登記面積_m2", 0) or 0) + float(src.get("面積_m2", 0) or 0)

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
                             "評選指數": cfg.get("idx", {}).get(c, 0.5), "試算G(㎡)": round(g(by[c]), 2),
                             "臨正街寬(m)": 5.0, "結果": "當選" if ok else "未達"})
                if ok:
                    win = c
                    break
            out.setdefault(blk, {})[sd] = {"觸發": True, "R_end(㎡)": cfg["thr"], "候選": rows, "當選": win}
        return out

    def alloc_state(temp, build):
        kept = {}
        for b in build:
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
        return {"kept": kept, "bad_pools": {}, "err": None, "G": {b["暫編地號"]: g(b) for b in build},
                "members": {}, "pool_out": {}}
    return a_prime, alloc_eval, alloc_state


def _go(ns, world, targets):
    temp, own, blocks, cl = world
    temp = copy.deepcopy(temp)
    build = [t for t in temp if t["街廓分類"] == H]
    ap, ev, st = _cbs(targets)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            t2, b2, log, rec = ns["end_block_merge_run"](temp, build, own, set(), set(), blocks, cl, ap, ev, st,
                                                         setback=3.5, log_print=lambda *x: None)
    except Exception as e:  # noqa: BLE001
        return {"err": type(e).__name__ + ": " + str(e).split("\n")[0][:300]}
    return {"err": None, "t2": t2, "b2": b2, "log": log, "rec": rec}


def _xf(ang, mirror, tx, ty):
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))

    def f(p):
        x, y = p
        if mirror:
            x = -x
        return (round(tx + c * x - s * y, 6), round(ty + s * x + c * y, 6))
    return f


ID = _xf(0, False, 0.0, 0.0)
FR = _xf(37, True, 307123.4, 2654321.7)


def _w(spec, nm=None, frame=ID, cly=None):
    """spec ＝ [(暫編地號, 街廓, 類, (x0, x1, y0, y1), a)]；nm ＝ 換名表；回 (temp, own, blocks, cl)。"""
    nm = nm or {}
    n = lambda s: nm.get(s, s)
    t, own, blocks, cl = [], {}, {}, {}
    for pid, blk, cat, (x0, x1, y0, y1), a, o in spec:
        t.append(_tp(n(pid), n(blk), cat, [frame(p) for p in [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]], a))
        own[n(pid).split("(")[0]] = o
        blocks[n(blk)] = {"category": cat}
        if cat == "道路":
            ym = (cly or {}).get(blk, (y0 + y1) / 2)
            cl[n(blk)] = [frame((-20.0, ym)), frame((50.0, ym))]
    return t, own, blocks, cl


R = "道路"


def _w3(a, extra=()):
    s = [("D1(1)", "BA", H, (0, 5, 0, 30), a["D1"], "g丁"), ("P(1)", "BA", H, (5, 40, 0, 30), 900, "gP"),
         ("Da(1)", "RA", R, (0, 5, -10, 0), a["Da"], "g丁"), ("Ra(1)", "RA", R, (5, 40, -10, 0), 300, "gRa"),
         ("D2(1)", "BB", H, (0, 5, -40, -10), a["D2"], "g丁"), ("Q(1)", "BB", H, (5, 40, -40, -10), 900, "gQ"),
         ("Db(1)", "RB", R, (0, 5, -50, -40), a["Db"], "g丁"), ("Rb(1)", "RB", R, (5, 40, -50, -40), 300, "gRb"),
         ("D3(1)", "BC", H, (0, 5, -80, -50), a["D3"], "g丁"), ("T(1)", "BC", H, (5, 40, -80, -50), 900, "gT")]
    return [x for x in s if not (extra and x[0] == "P(1)")] + list(extra)


def _w4():
    return [("D1(1)", "BA", H, (0, 5, 0, 30), 100, "g丁"), ("P(1)", "BA", H, (5, 40, 0, 30), 900, "gP"),
            ("Da(1)", "RA", R, (0, 5, -10, 0), 100, "g丁"), ("Ra(1)", "RA", R, (5, 40, -10, 0), 300, "gRa"),
            ("D2(1)", "BB", H, (0, 5, -40, -10), 100, "g丁"), ("Q(1)", "BB", H, (5, 40, -40, -10), 900, "gQ"),
            ("D3(1)", "BC", H, (0, 5, -70, -40), 100, "g丁"), ("T(1)", "BC", H, (5, 40, -70, -40), 900, "gT"),
            ("Dc(1)", "RC", R, (0, 5, -80, -70), 100, "g丁"), ("Rc(1)", "RC", R, (5, 40, -80, -70), 300, "gRc"),
            ("D4(1)", "BD", H, (0, 5, -110, -80), 110, "g丁"), ("V(1)", "BD", H, (5, 40, -110, -80), 900, "gV")]


def _w8():
    """H8 之世界：四街廓直接相鄰（B1 y∈[0,30]、B2 [-30,0]、B3 [-60,-30]、B4 [-90,-60]·各 6 條·寬 10）；
    F：B1 s0（F1）、B1 s5（F2）、B2 s0（F3）、B2 s5（F6）、B3 s0（F5）、B3 s5（F7）、B4 全（F8）——相連；
    D：B1 s4（D1）、B2 s4（D2）；Z：B1 s1（Z1）、B2 s1〜s3（Z2、Z3、Z4）、B3 s1（Z5）；他人 O1〜O5。"""
    S = lambda b, k: (k * 10, k * 10 + 10) + {"B1": (0, 30), "B2": (-30, 0), "B3": (-60, -30), "B4": (-90, -60)}[b]
    sp = [("F1(1)", "B1", 0, 200, "gF"), ("Z1(1)", "B1", 1, 100, "gZ"), ("O1(1)", "B1", 2, 100, "g1"),
          ("O2(1)", "B1", 3, 100, "g2"), ("D1(1)", "B1", 4, 100, "gD"), ("F2(1)", "B1", 5, 200, "gF"),
          ("F3(1)", "B2", 0, 200, "gF"), ("Z2(1)", "B2", 1, 100, "gZ"), ("Z3(1)", "B2", 2, 100, "gZ"),
          ("Z4(1)", "B2", 3, 100, "gZ"), ("D2(1)", "B2", 4, 100, "gD"), ("F6(1)", "B2", 5, 100, "gF"),
          ("F5(1)", "B3", 0, 200, "gF"), ("Z5(1)", "B3", 1, 100, "gZ"), ("O3(1)", "B3", 2, 100, "g3"),
          ("O4(1)", "B3", 3, 100, "g4"), ("O5(1)", "B3", 4, 100, "g5"), ("F7(1)", "B3", 5, 100, "gF")]
    out = [(p, b, H, S(b, k), a, o) for p, b, k, a, o in sp]
    return out + [("F8(1)", "B4", H, (0, 60, -90, -60), 300, "gF")]


# 端 a ＝ B1 左〔F1, Z1〕、b ＝ B1 右〔D1, F2〕、c ＝ B2 左〔F3〕、d ＝ B2 右〔Z4, D2〕、e ＝ B3 左〔Z5, F5〕（候選之序如列·門檻不可達）；
# 指數：a Z1 0.6／F1 0.3、b F2 0.6／D1 0.3、d D2 0.6／Z4 0.3、e Z5 0.6／F5 0.3 ⇒ F 勝 D（b）、D 勝 Z（d）、Z 勝 F（a、e 皆第 1）成圈；
# 序鍵：ΣG F 0.6×800＝480 ＞ Z 180 ＞ D 120 ⇒ 第一次（F、D、Z）F 先處理，唯 D 持 F 之未至之列（b）⇒ 唯 D 延後；其後 F5 入 Z 之 e 之候列 ⇒
# 第二次 F、Z ⇒ 一乙：F 與 Z 之先後未記 ⇒ 重比 ⇒ Z 先（其最先至之列 Z4）；一甲：F 已記先於 Z ⇒ F 先。
T8 = {("B1", "left"): dict(thr=1e6, cands=["F1(1)", "Z1(1)"], idx={"F1(1)": 0.3, "Z1(1)": 0.6}),
      ("B1", "right"): dict(thr=1e6, cands=["D1(1)", "F2(1)"], idx={"D1(1)": 0.3, "F2(1)": 0.6}),
      ("B2", "left"): dict(thr=1e6, cands=["F3(1)"], idx={"F3(1)": 0.5}),
      ("B2", "right"): dict(thr=1e6, cands=["Z4(1)", "D2(1)"], idx={"Z4(1)": 0.3, "D2(1)": 0.6}),
      ("B3", "left"): dict(thr=1e6, cands=["Z5(1)", "F5(1)"], idx={"Z5(1)": 0.6, "F5(1)": 0.3})}


def _tg(thr, cands, nm=None):
    nm = nm or {}
    n = lambda s: nm.get(s, s)
    return {(n(b), "left"): dict(thr=thr[b], cands=[n(c) for c in cands[b]]) for b in thr}


def _sum(r, nm=None):
    """結果之摘：(err, 得者 [(街廓, 端, 候選)], 丁之片之面積 {片: 面積}, 皆未達) ——以原名（nm 之逆）表之。"""
    inv = {v: k for k, v in (nm or {}).items()}
    o = lambda s: inv.get(s, s)
    if r["err"]:
        return (r["err"][:60],)
    won = sorted((o(x["街廓"]), x["端"], o(x["候選"])) for x in r["log"] if x.get("結果") == "成" and x.get("序") != "後處理")
    ar = {o(t["暫編地號"]): round(float(t.get("面積_m2", 0) or 0), 4) for t in r["t2"]
          if t["街廓分類"] == H and o(t["暫編地號"])[0] in "DX"}
    na = dict(sorted((o(b), v) for b, v in (r["rec"].get("皆未達") or {}).items()))
    return (None, won, ar, na)


ALL100 = dict(D1=100, Da=100, D2=100, Db=100, D3=100)


def _cases(ns):
    C = []
    C3 = {"BA": ["D1(1)"], "BB": ["D2(1)"], "BC": ["D3(1)"]}
    r = _go(ns, _w(_w3(ALL100)), _tg({"BA": 100, "BB": 110, "BC": 100}, C3))
    C.append(("H1 部分拿得下 ⇒ BB 定案、BA／BC 不得而照配其半", _sum(r),
              (None, [("BB", "左", "D2(1)")], {"D1(1)": 50.0, "D2(1)": 100.0, "D3(1)": 50.0},
               {"BA": ["left"], "BC": ["left"]})))
    C.append(("H1′ 其競合之形 ＝ 多、列 ＝ 三端之首個候選",
              None if r["err"] else [(c["形"], [tuple(e[:3]) for e in c["列"]]) for c in r["rec"].get("競合") or []],
              [("多", [("BA", "左", "D1(1)"), ("BB", "左", "D2(1)"), ("BC", "左", "D3(1)")])]))
    r = _go(ns, _w(_w3(dict(ALL100, D1=150))), _tg({"BA": 140, "BB": 140, "BC": 140}, C3))
    C.append(("H2 全部拿不下 ⇒ 整片各試·二端能達標 ⇒ G 大者 BB 得", _sum(r),
              (None, [("BB", "左", "D2(1)")], {"D1(1)": 0.0, "D2(1)": 200.0, "D3(1)": 0.0},
               {"BA": ["left"], "BC": ["left"]})))
    C4 = {"BA": ["D1(1)"], "BB": ["D2(1)"], "BC": ["D3(1)"], "BD": ["D4(1)"]}
    T4 = {"BA": 85, "BB": 95, "BC": 95, "BD": 100}
    E3 = (None, [("BA", "左", "D1(1)"), ("BD", "左", "D4(1)")],
          {"D1(1)": 50.0, "D2(1)": 50.0, "D3(1)": 0.0, "D4(1)": 100.0}, {"BB": ["left"], "BC": ["left"]})
    r = _go(ns, _w(_w4()), _tg(T4, C4))
    C.append(("H3 端群各判：群一 BA 得、群二全部拿不下 ⇒ 整片 BD 得", _sum(r), E3))
    nm = {"BA": "甲街", "BB": "乙街", "BC": "丙街", "BD": "丁街", "RA": "路一", "RC": "路二",
          "D1(1)": "丁-7(3)", "D2(1)": "丁-2(1)", "D3(1)": "丁-9(2)", "D4(1)": "丁-1(4)", "Da(1)": "丁-5(1)",
          "Dc(1)": "丁-8(1)", "D1": "丁-7", "D2": "丁-2", "D3": "丁-9", "D4": "丁-1", "Da": "丁-5", "Dc": "丁-8"}
    r = _go(ns, _w(_w4(), nm, FR), _tg(T4, C4, nm))
    C.append(("H4 H3 之換名、旋轉、鏡射、TWD97 ⇒ 同 H3", _sum(r, nm), E3))
    ext = [("X(1)", "BA", H, (5, 10, 0, 30), 100, "g庚"), ("X2(1)", "BA", H, (10, 15, 0, 30), 100, "g庚"),
           ("P(1)", "BA", H, (15, 40, 0, 30), 900, "gP")]
    r = _go(ns, _w(_w3(ALL100, ext)), _tg({"BA": 100, "BB": 110, "BC": 100},
                                          {"BA": ["X(1)", "D1(1)"], "BB": ["D2(1)"], "BC": ["D3(1)"]}))
    C.append(("H5 他人先定案之端去之 ⇒ 餘二端依題一", _sum(r),
              (None, [("BA", "左", "X(1)"), ("BB", "左", "D2(1)")],
               {"D1(1)": 0.0, "D2(1)": 150.0, "D3(1)": 50.0, "X(1)": 100.0, "X2(1)": 0.0}, {"BC": ["left"]})))
    e7 = [("Dz(1)", "RA", R, (-10, 0, -10, 0), 20, "g丁"), ("P0(1)", "BA", H, (-10, 0, 0, 30), 300, "gP0"),
          ("P(1)", "BA", H, (5, 40, 0, 30), 900, "gP")]
    r = _go(ns, _w(_w3(ALL100, e7), cly={"RA": -4.0}), _tg({"BA": 100, "BB": 110, "BC": 100}, C3))
    C.append(("H7 中心線偏（RA 之 Da 上 0.4／下 0.6）、Dz 唯臨 BA 而整片歸之 ⇒ BB 定案、BA 照配 Da 0.4 ＋ Dz", _sum(r),
              (None, [("BB", "左", "D2(1)")], {"D1(1)": 60.0, "D2(1)": 110.0, "D3(1)": 50.0},
               {"BA": ["left"], "BC": ["left"]})))
    r = _go(ns, _w(_w8()), T8)
    C.append(("H8 一乙：第一次 F 依序鍵先、唯延後 D；第二次 F、Z ⇒ 重比 ⇒ Z 先（⛔ 一甲之 F 先）",
              None if r["err"] else [x["候選"] for x in r["log"] if x.get("結果") == "互相等待 ⇒ 先處理"][:2],
              ["F1(1)", "Z4(1)"]))
    r = _go(ns, _w(_w3(ALL100)), _tg({"BA": 100, "BB": 110, "BC": 100}, C3))
    C.append(("H6 ⛔ 停機（三個以上之末端塊）", bool(r["err"]) and "末端塊" in r["err"], False))
    return C


# ── E2：二端之隨機世界（與倉外之生成式同·種子固定）──
def _rw(seed, nr=3, nc=2, road=False, nS=5, nlink=None):
    rnd = random.Random(seed)
    BW, BH, RG, SW = nS * 10.0, 30.0, (10.0 if road else 0.0), 10.0
    t, own, blocks, cl, sid, oc = [], {}, {}, {}, {}, [0]

    def newo():
        oc[0] += 1
        return f"o{oc[0]}"
    for i in range(nr):
        for j in range(nc):
            b = f"B{i}{j}"
            blocks[b] = {"category": H}
            y1 = -i * (BH + RG)
            y0 = y1 - BH
            for k in range(nS):
                x0 = j * BW + k * SW
                lot = f"L{i}{j}{k}"
                sid[(i, j, k)] = lot
                own[lot] = newo()
                t.append(_tp(lot + "(1)", b, H, [(x0, y0), (x0 + SW, y0), (x0 + SW, y1), (x0, y1)], rnd.randint(40, 160)))
        if road and i < nr - 1:
            rb = f"R{i}"
            blocks[rb] = {"category": "道路"}
            y1 = -i * (BH + RG) - BH
            y0 = y1 - RG
            cl[rb] = [(-10.0, (y0 + y1) / 2), (nc * BW + 10.0, (y0 + y1) / 2)]
            for j in range(nc):
                for k in range(nS):
                    x0 = j * BW + k * SW
                    lot = f"Q{i}{j}{k}"
                    sid[("r", i, j, k)] = lot
                    own[lot] = newo()
                    t.append(_tp(lot + "(1)", rb, "道路", [(x0, y0), (x0 + SW, y0), (x0 + SW, y1), (x0, y1)],
                                 rnd.randint(10, 60)))
    links = []
    for i in range(nr):
        for j in range(nc):
            for k in range(nS):
                if i < nr - 1:
                    links.append(("v", i, j, k))
                if k == nS - 1 and j < nc - 1:
                    links.append(("h", i, j, k))
                if k < nS - 1:
                    links.append(("s", i, j, k))
    nl = nlink if nlink is not None else rnd.randint(2, max(3, nr * nc))
    for kind, i, j, k in rnd.sample(links, min(nl, len(links))):
        a = sid[(i, j, k)]
        if kind == "v":
            bs = [sid[(i + 1, j, k)]] + ([sid[("r", i, j, k)]] if road else [])
        elif kind == "h":
            bs = [sid[(i, j + 1, 0)]]
        else:
            bs = [sid[(i, j, k + 1)]]
        o = own[a]
        for b in bs:
            ob = own[b]
            for key in list(own):
                if own[key] == ob:
                    own[key] = o
    by = {x["暫編地號"]: x for x in t}
    targets = {}
    for i in range(nr):
        for j in range(nc):
            b = f"B{i}{j}"
            for sd, ks in (("left", list(range(0, 3))), ("right", list(range(nS - 1, nS - 4, -1)))):
                cs = [sid[(i, j, k)] + "(1)" for k in ks[:rnd.choice([2, 3])]]
                if rnd.random() < 0.5:
                    rnd.shuffle(cs)
                g = max(BUR * by[c]["分攤登記面積_m2"] for c in cs)
                targets[(b, sd)] = dict(thr=round(g + rnd.choice([1, 5, 15, 40, 80]), 2), cands=cs,
                                        idx={c: round(rnd.random(), 3) for c in cs},
                                        cross={c: float(rnd.randint(5, 60)) for c in cs})
    return (t, own, blocks, cl), targets


def _dg(ns, w, tg):
    r = _go(ns, w, tg)
    if r["err"]:
        d = {"err": r["err"]}
    else:
        t2, b2, log, rec = r["t2"], r["b2"], r["log"], r["rec"]
        a0 = {x["暫編地號"]: float(x["分攤登記面積_m2"]) for x in w[0]}
        used = {x["暫編地號"] for x in t2 if x.get("段三併出")}
        tot = sum(float(x.get("面積_m2", 0) or 0) for x in t2)
        d = {"err": None,
             "land": sorted((x["暫編地號"], round(float(x.get("面積_m2", 0) or 0), 4), tuple(sorted(x.get("段三併出") or ())))
                            for x in t2),
             "build": sorted(b["暫編地號"] for b in b2),
             "log": [(x.get("序"), x.get("街廓"), x.get("端"), x.get("候選"), x.get("層級"), x.get("結果"), x.get("受併宗"))
                     for x in log],
             "first": [x.get("競合") for x in log if x.get("結果") == "互相等待 ⇒ 先處理"],
             "nct": len(rec.get("競合") or []), "multi": sum(1 for c in (rec.get("競合") or []) if len(c["列"]) >= 3)}
        d = json.loads(json.dumps(d, ensure_ascii=False))
    return hashlib.sha256(json.dumps(d, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]


NEED = ["end_block_merge_run", "k6b_stage3_run", "k960_idx_first", "k967_rank"]


def selftest(repo):
    ns = _harvest(repo)
    miss = [n for n in NEED if n not in ns]
    if miss:
        print(f"  🔴 受詞缺 {miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    print("── 甲 K-9-60 ②（三個以上之末端塊）──")
    for name, got, exp in _cases(ns):
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + name)
        if not ok:
            print(f"       得 {got!r}"[:900])
            print(f"       期 {exp!r}"[:900])
            red.append(name.split()[0])
    print("── 乙 二是：二端之隨機世界 ＝ 主線 9fd3427 ──")
    bad = []
    for ci, s, dg in PICK2:
        w, tg = _rw(s, **CFG2[ci])
        if _dg(ns, w, tg) != dg:
            bad.append((ci, s))
    ok = not bad
    print(("  ✅ " if ok else "  🔴 ") + f"E2 {len(PICK2)} 例之摘要 ＝ 主線（不符 {bad[:6]}{'…' if len(bad) > 6 else ''}）")
    if not ok:
        red.append("E2")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _git(repo, *a):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def _top(src):
    out = {}
    for n in ast.parse(src).body:
        nm = getattr(n, "name", None)
        if nm is None and isinstance(n, ast.Assign):
            nm = ",".join(x.id for x in n.targets if isinstance(x, ast.Name)) or None
        if nm:
            out.setdefault(nm, []).append(ast.dump(n))
    return out


def _fn(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return n
    return None


def _strs(node):
    return [x.value for x in ast.walk(node) if isinstance(x, ast.Constant) and isinstance(x.value, str)]


def _raise_strs(node):
    return [s for r in ast.walk(node) if isinstance(r, ast.Raise) for s in _strs(r)]


def _inner(node, name):
    return [x for x in ast.walk(node) if isinstance(x, ast.FunctionDef) and x.name == name]


def wiring(repo, base):
    src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    bsrc = _git(repo, "show", f"{base}:app.py")
    red = []

    def rep(tag, ok, msg):
        print(("  ✅ " if ok else "  🔴 ") + f"{tag} {msg}")
        if not ok:
            red.append(tag)
    if bsrc is None:
        print(f"  🔴 基準 {base} 之 app.py 取不到")
        print("⇒ 紅 ['基準']；rc 1")
        return 1
    bsrc = bsrc.decode("utf-8")
    n2, n3 = _fn(src, "end_block_merge_run"), _fn(src, "k6b_stage3_run")
    if not (n2 and n3):
        rep("W0", False, "受詞缺")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    rep("W1", not any(GONE_HIT3 in s for s in _raise_strs(n2)) and "多" in _strs(n2),
        "end_block_merge_run：⛔ 有「三個以上之末端塊」之停機；有形「多」之字面")
    cm, ct, k950 = _inner(n3, "_ct_multi"), _inner(n3, "_contest"), _inner(n3, "_k950_rows")
    calls = [x for x in ast.walk(ct[0]) if isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
             and x.func.id == "_ct_multi"] if len(ct) == 1 else []
    rep("W2", len(cm) == 1 and len(calls) == 1 and len(k950) == 1
        and not any(GONE_ROWS in s for s in _raise_strs(k950[0])),
        f"_ct_multi 恰一（{len(cm)}）且 _contest 呼之（{len(calls)}）；_k950_rows 之停機⛔ 含「列數 ≠ 2」")
    k_src = ast.get_source_segment(src, k950[0]) if len(k950) == 1 else ""
    gate = "if not any(len(contests[_y396]['列']) >= 3 for _y396 in _scc396):"
    ia, ib = k_src.find(gate), k_src.find("_pre396.add(")
    rep("W3", k_src.count(gate) == 1 and k_src.count("_pre396.add(") == 1 and 0 <= ia < ib
        and "_pre396.update(" not in k_src,
        "_k950_rows：已排定之先後之記（_pre396.add 恰一·⛔ update）唯在「當次之人有形多」之判（恰一）之後")
    a, b = _top(src), _top(bsrc)
    rep("W4", set(a) == set(b), f"頂層之名之增減 {sorted(set(a) ^ set(b))}（期 []）")
    lits = []
    for nm in ("end_block_merge_run", "k6b_stage3_run"):
        cur = [s for s in _strs(_fn(src, nm)) if CASE_LIT_RE.match(s)]
        bn = _fn(bsrc, nm)
        old = [s for s in _strs(bn) if CASE_LIT_RE.match(s)] if bn else []
        lits += [(nm, s) for s in cur if cur.count(s) > old.count(s)]
    rep("W5", not lits, f"所改之二節點內新增案件字面 {sorted(set(lits))}（期 []）")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def run(repo, setbacks):
    probes = os.path.join(repo, "verify", "probes")
    if probes not in sys.path:
        sys.path.insert(0, probes)
    import probe_WG9395_k960 as F39
    red = []
    for sb in setbacks:
        try:
            res, ev, mr = F39._one(repo, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  🔴 R0@{sb} 例外 {type(e).__name__}：{str(e)[:200]}")
            red.append(f"R0@{sb}")
            continue
        ok = isinstance(mr, dict) and mr.get("標的") == [] and not mr.get("競合") and res.get("err") is None
        print(("  ✅ " if ok else "  🔴 ") + f"R1@{sb} 合併再試之標的 {(mr or {}).get('標的')!r}（期 []）、競合 "
              f"{(mr or {}).get('競合')!r}（期 無）、err {res.get('err')!r}")
        if not ok:
            red.append(f"R1@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "selftest":
        return selftest(argv[2])
    if len(argv) >= 4 and argv[1] == "wiring":
        return wiring(argv[2], argv[3])
    if len(argv) >= 3 and argv[1] == "run":
        repo = os.path.abspath(argv[2])
        sys.path.insert(0, os.path.join(repo, "verify"))
        os.chdir(repo)
        return run(repo, [float(x) for x in argv[3:]] or [3.5, 0.0])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
