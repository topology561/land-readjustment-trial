# -*- coding: utf-8 -*-
"""W-G.9-388 量測器（發單端擬·檔 F32·⛔ 由受單側改一字）：段三後處理之承受之宗與分不到之建地之去處（`K-9-61` ①②③⑥·
KL 裁 `2026-10-06 01:29`；`2026-10-18 08:03`〔問二 ＝ 手冊道路用地分配原則第 2 點〕、`08:14`〔問一、問三依 10/06 既裁〕）。

子命令（一律 python3 verify/probes/probe_WG9388_k961s3.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k6b_stage3_run`）。玩具：街廓 BA（y∈[0,30]）臨正面道路 RD
           （y∈[-10,0]·中心線 y ＝ -5）與側面道路 RS（x∈[40,50]·中心線 x ＝ 45）；RD 之另一側為 BB（y∈[-40,-10]）；BA 之後
           為 BX（y∈[30,40]）；BA 之左為 BC（x∈[-30,0]）。地主 g1 之土地依各例置之；他人之土地 M(1)。回呼：`alloc_state`
           以 build 之全部（`drop` 除外）為保留，`G` ＝ 分攤登記面積 ＋ 面積（`no_g` ⇒ ⛔ 回 `G`）；`trial_winner` ＝ G ≥ 門檻
           即當選；`a_prime` ＝ a(src)。期值皆依 `K-9-61` 之文與 `k967_rank` 之定義（`0.01 ㎡`）手算（各例之註）。
           K1 同一街廓左右兩端皆取得街角（二受併宗）而道路片與二者皆相鄰 ⇒ 應分配面積大者；K2 道路片唯與其一相鄰 ⇒
           該宗（縱其應分配面積小）；K3 二者之應分配面積以 0.01 ㎡ 相同 ⇒ 重劃前面積大者；K4 再同 ⇒ 暫編地號小者；
           K5 無本段之受併宗之街廓，該群依原位次配得之宗二筆 ⇒ 同 ①（相鄰者先）；K6 有受併宗之街廓內另有不相連之原位次
           配得之宗 ⇒ 照配（⛔ 動、⛔ 併入受併宗），且與道路片相鄰者由之承受；K7 分不到之建地所鄰之配得街廓二 ⇒ 承受之宗之
           應分配面積大之一側；K8 二側之承受之宗之應分配面積相同 ⇒ 重劃前面積大之一側；K9 所鄰二而其一為本街廓 ⇒ 本街廓；
           K10 所鄰為零而該地主之道路片與之相鄰並臨道路另一側之配得街廓 ⇒ 併入該側之宗（手冊道路用地分配原則第 2 點）；
           K11 所鄰為零而無此道路片 ⇒ 第 5 項之輪（距離）；K12 所鄰為零而本街廓另有配得之宗（⛔ 相鄰）⇒ 第 5 項（本街廓之
           候選先）；K13 二受併宗之一於現態未保留 ⇒ 仍停機（`K-9-61` ④ 另單）；K14 公設片平分，每街廓之一份由該街廓之
           擇定之一宗整份承受；K15 承受之宗唯一者⛔ 須 G（未回 G 亦⛔ 停機）；K16 須擇而未回 G ⇒ 停機；
           K17 相鄰以宗連同其於本段整筆併入之片判之；K18 經道路片而臨者隨該道路片之受者（4、5 地號往 6 地號）；K19 道路片之
           端所臨之街廓⛔ 為另一側；K20 本街廓有同一地主之他群之配得之宗 ⇒ 第 5 項；K21 第 5 項之來源量為整筆；K22／K23 重劃前
           面積扣段三部分併出／入池閘之帳；K24 經道路片以該建地與之共邊為準；K25 已為街角之合併所併出之道路片
           ⛔ 經之（`K-9-73` ⑥）；K26 同一街廓經二道路片而其受者異 ⇒ `k967_rank`；K27 經道路片而臨二側 ⇒ 以其經道路片之受者比；
           K28 穿越之道路片⛔ 經之。
           P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           X1 `k6b_stage3_run` 內四停機之字樣皆去（「有二受併宗」「承受之宗未定」「§三-2 未定」「（期恰 1）」）、「於現態未保留」
           之停機仍在；X2 `_recv_of` 之形 ＝ `def _recv_of(b, y):`，其呼叫皆二引數；X3 app.py 之頂層節點對基準之相異 ＝
           `{k6b_stage3_run}`、頂層之名之集⛔ 變；X4 `k6b_stage3_run` 內⛔ 案件字面；X5 `verify/` 之 `*.py`（頂層）對基準
           逐位同。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

H, PK, RDC = "住宅區", "鄰里公園", "道路"
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, _fake = harvest(os.path.join(repo, "app.py"))
    return ns


def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


BLOCKS = {"BA": {"category": H}, "BB": {"category": H}, "BX": {"category": H}, "BC": {"category": H},
          "BE": {"category": H}, "BF": {"category": H}, "RD": {"category": RDC}, "RS": {"category": RDC},
          "RD2": {"category": RDC}, "RX": {"category": RDC}, "PK": {"category": PK}}
CL = {"RD": [(-40.0, -5.0), (60.0, -5.0)], "RS": [(45.0, -20.0), (45.0, 50.0)], "RD2": [(-40.0, -45.0), (60.0, -45.0)]}


def _g(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _cbs(thr, drop=(), no_g=False, pool_out=None):
    def a_prime(src, dst):
        return _g(src)

    def alloc_state(temp, build):
        kept, G = {}, {}
        for b in build:
            if b["暫編地號"] in drop:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            G[b["暫編地號"]] = _g(b)
        out = {"kept": kept, "bad_pools": {}, "err": None}
        if not no_g:
            out["G"] = G
        if pool_out is not None:
            out["pool_out"] = dict(pool_out)
        return out

    def trial_winner(temp, build, blk, end, cand):
        by = {b["暫編地號"]: b for b in build}
        g = _g(by[cand]) if cand in by else 0.0
        return (cand if g >= thr else None), round(g, 2), thr
    return a_prime, trial_winner, alloc_state


def _b5(blocks):
    from decimal import Decimal
    return {b: {"使用分區": H, "最小建築面積": Decimal("0"), "正面道路": "RD", "正面路寬": Decimal("8"),
                "深度": Decimal("30")} for b, v in blocks.items() if v.get("category") == H}


def _go(ns, parcels, own, order, thr=150.0, drop=(), no_g=False, pre=None, pool_out=None):
    """回 (後處理之列, 各宗之受併之累加, 末之 build)；後處理之列 ＝ (候選, 層級, 結果, 受併宗)。`pre` ＝ {暫編地號: 其輸入另帶之鍵}。"""
    temp = [_tp(*p) for p in parcels]
    for t in temp:
        t.update((pre or {}).get(t["暫編地號"], {}))
    build = [t for t in temp if t["街廓分類"] == H]
    ap, tw, st = _cbs(thr, drop, no_g, pool_out)
    t2, b2, log = ns["k6b_stage3_run"](order, set(), own, temp, build, BLOCKS, CL, ap, tw, st,
                                       log_print=lambda *x: None, blk5=lambda: _b5(BLOCKS))
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]))
            for x in log if x.get("序") == "後處理"]
    acc = {t["暫編地號"]: round(float(t.get("面積_m2", 0) or 0), 2) for t in t2 if float(t.get("面積_m2", 0) or 0)}
    return post, acc, sorted(b["暫編地號"] for b in b2)


def _halt(fn, phrase):
    try:
        fn()
    except RuntimeError as e:
        return ("停機", phrase in str(e))
    return ("無停機",)


def _O(*rows):
    return [{"最終序位": i, "街廓": b, "端": e, "暫編地號": c} for i, (b, e, c) in enumerate(rows, 1)]


# ── 玩具之宗（暫編地號, 街廓, 類, 多邊形, 分攤登記面積）──
def _two_ends(a1=100, a1b=60, a2=100, a2b=40, rs=True):
    """BA：g1 之 A1(1)[0,5]／A1b(1)[5,10]（左端）、他人 M(1)[10,30]、g1 之 A2b(1)[30,35]／A2(1)[35,40]（右端）；
    g1 之道路片 D1(1)（RD·x∈[0,40]·與 BA 之五宗皆相鄰）；（rs）g1 之道路片 D2(1)（RS·x∈[40,45]·唯與 A2 相鄰）。"""
    p = [("A1(1)", "BA", H, _R(0, 5, 0, 30), a1), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), a1b),
         ("M(1)", "BA", H, _R(10, 30, 0, 30), 500), ("A2b(1)", "BA", H, _R(30, 35, 0, 30), a2b),
         ("A2(1)", "BA", H, _R(35, 40, 0, 30), a2), ("D1(1)", "RD", RDC, _R(0, 40, -10, 0), 50)]
    if rs:
        p.append(("D2(1)", "RS", RDC, _R(40, 45, 0, 30), 20))
    own = {"A1": "g1", "A1b": "g1", "A2": "g1", "A2b": "g1", "D1": "g1", "D2": "g1", "M": "gM"}
    return p, own, _O(("BA", "左", "A1(1)"), ("BA", "右", "A2(1)"))


def _cases(ns):
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__, str(ex)[:200])
        out.append((name, got, exp))

    # K1：門檻 130；G(A1) ＝ 100 ＋ 60 ＝ 160、G(A2) ＝ 100 ＋ 40 ＝ 140（皆於 ① 成）；D1 與二者皆相鄰 ⇒ A1；D2 唯鄰 A2 ⇒ A2
    p, own, od = _two_ends()
    run("K1 二受併宗皆與道路片相鄰 ⇒ 應分配面積大者（D1 ⇒ A1）",
        lambda: [r for r in _go(ns, p, own, od, thr=130.0)[0] if r[0] == "D1(1)"],
        [("D1(1)", "後處理(b)", "成", "A1(1)")])
    run("K2 道路片唯與其一相鄰 ⇒ 該宗（D2 ⇒ A2·縱 G 140 ＜ 160）",
        lambda: [r for r in _go(ns, p, own, od, thr=130.0)[0] if r[0] == "D2(1)"],
        [("D2(1)", "後處理(b)", "成", "A2(1)")])
    # K3：G(A1) ＝ 100 ＋ 60.004 ＝ 160.004、G(A2) ＝ 120 ＋ 40 ＝ 160（0.01 ㎡ 同·逐位比則 A1 大）；重劃前面積 A1 100 ＜
    #   A2 120 ⇒ A2
    p3, own3, od3 = _two_ends(a1=100, a1b=60.004, a2=120, a2b=40, rs=False)
    run("K3 應分配面積以 0.01 ㎡ 相同 ⇒ 重劃前面積大者（D1 ⇒ A2）",
        lambda: [r for r in _go(ns, p3, own3, od3)[0] if r[0] == "D1(1)"],
        [("D1(1)", "後處理(b)", "成", "A2(1)")])
    # K4：G 皆 160、重劃前面積皆 100 ⇒ 暫編地號小者 A1(1)
    p4, own4, od4 = _two_ends(a1=100, a1b=60, a2=100, a2b=60, rs=False)
    run("K4 再同 ⇒ 暫編地號小者（D1 ⇒ A1）",
        lambda: [r for r in _go(ns, p4, own4, od4)[0] if r[0] == "D1(1)"],
        [("D1(1)", "後處理(b)", "成", "A1(1)")])
    # K5：BA 左端 A1 取得街角（A1b 併入）；BB（RD 之另一側）之 g1 之 S1(1)[0,10]（120）、S2(1)[30,40]（200）依原位次配得
    #   （⛔ 本段之受併宗）；D1 之下半鄰 BB 之二宗、D3(1)（RD·x∈[40,45]·y∈[-10,0]）唯鄰 S2 之上緣之一段？——D3 之下緣
    #   y ＝ -10、x∈[40,45] 與 BB 之 S3(1)[40,45]（g1·60）相鄰 ⇒ 承受 D3 之下半者：BB 之候選 S1／S2／S3 中唯 S3 相鄰 ⇒ S3；
    #   D1 之下半：S1、S2 皆相鄰（S3 ⛔）⇒ G 大者 S2
    p5 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
          ("M(1)", "BA", H, _R(10, 40, 0, 30), 500), ("D1(1)", "RD", RDC, _R(0, 40, -10, 0), 50),
          ("D3(1)", "RD", RDC, _R(40, 45, -10, 0), 10),
          ("S1(1)", "BB", H, _R(0, 10, -40, -10), 120), ("N(1)", "BB", H, _R(10, 30, -40, -10), 500),
          ("S2(1)", "BB", H, _R(30, 40, -40, -10), 200), ("S3(1)", "BB", H, _R(40, 45, -40, -10), 60)]
    own5 = {"A1": "g1", "A1b": "g1", "D1": "g1", "D3": "g1", "S1": "g1", "S2": "g1", "S3": "g1", "M": "gM", "N": "gN"}
    od5 = _O(("BA", "左", "A1(1)"))
    run("K5 無本段受併宗之街廓之原位次配得之宗二以上 ⇒ 相鄰者先 → G（D1 ⇒ A1／S2；D3 ⇒ S3）",
        lambda: sorted(r for r in _go(ns, p5, own5, od5)[0] if r[0] in ("D1(1)", "D3(1)")),
        [("D1(1)", "後處理(b)", "成", ("A1(1)", "S2(1)")), ("D3(1)", "後處理(b)", "成", "S3(1)")])
    # K6：BA 左端 A1 取得街角；g1 之 K(1)[30,40]（80）依原位次配得而與 A1 不相連；D1（x∈[0,40]）皆鄰 ⇒ G 大者 A1（160）；
    #   D2（RS）唯鄰 K ⇒ K；K 照配（⛔ 於後處理之列、仍在 build）
    p6 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
          ("M(1)", "BA", H, _R(10, 30, 0, 30), 500), ("K(1)", "BA", H, _R(30, 40, 0, 30), 80),
          ("D1(1)", "RD", RDC, _R(0, 40, -10, 0), 50), ("D2(1)", "RS", RDC, _R(40, 45, 0, 30), 20)]
    own6 = {"A1": "g1", "A1b": "g1", "K": "g1", "D1": "g1", "D2": "g1", "M": "gM"}

    def k6():
        post, acc, bl = _go(ns, p6, own6, _O(("BA", "左", "A1(1)")))
        return (sorted(post), acc.get("K(1)"), "K(1)" in bl, any(r[0] == "K(1)" for r in post))
    run("K6 有受併宗之街廓內另有原位次配得之宗 ⇒ 照配、與 D2 相鄰而承受之（D1 ⇒ A1·D2 ⇒ K）",
        k6, ([("D1(1)", "後處理(b)", "成", "A1(1)"), ("D2(1)", "後處理(b)", "成", "K(1)")], 20.0, True, False))
    # K7：BX（BA 之後·y∈[30,40]）之 g1 之 X(1)[0,20]（30·恆⛔ 保留）與 BA 之 A1(1)（G 160·其後緣）、BC（BX 之末端之
    #   鄰·x∈[-20,0]·y∈[30,40]·與 BA 唯一點相接 ⇒ 街角宗之側邊⛔ 貼他街廓）之 C1(1)（x∈[-10,0]·G 170）皆相鄰；C1 依原位次
    #   配得（BC 無本段之受併宗）⇒ 二側之承受之宗 A1 160／C1 170 ⇒ BC
    def w7(c1=170, c1b=None):
        p = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
             ("M(1)", "BA", H, _R(10, 40, 0, 30), 500), ("X(1)", "BX", H, _R(0, 20, 30, 40), 30),
             ("C1(1)", "BC", H, _R(-10, 0, 30, 40), c1), ("MC(1)", "BC", H, _R(-20, -10, 30, 40), 500)]
        own = {"A1": "g1", "A1b": "g1", "X": "g1", "C1": "g1", "M": "gM", "MC": "gM"}
        return p, own
    p7, own7 = w7()
    run("K7 所鄰之配得街廓二 ⇒ 承受之宗之 G 大之一側（X ⇒ C1·170 ＞ 160）",
        lambda: _go(ns, p7, own7, _O(("BA", "左", "A1(1)")), drop=("X(1)",))[0],
        [("X(1)", "後處理(a)", "成", "C1(1)")])
    # K8：A1 ＝ 100 ＋ 60.004 ＝ 160.004、C1 ＝ 160（0.01 ㎡ 同·逐位比則 A1 大）⇒ 重劃前面積：A1 100、C1 160 ⇒ C1
    p8, own8 = w7(c1=160)
    p8 = [tuple(r) if r[0] != "A1b(1)" else (r[0], r[1], r[2], r[3], 60.004) for r in p8]
    run("K8 二側之 G 以 0.01 ㎡ 相同 ⇒ 重劃前面積大之一側（X ⇒ C1）",
        lambda: _go(ns, p8, own8, _O(("BA", "左", "A1(1)")), drop=("X(1)",))[0],
        [("X(1)", "後處理(a)", "成", "C1(1)")])
    # K9：同 K7 ＋ BX 之 g1 之 X9(1)[20,40]（40·依原位次配得·與 X 相鄰）⇒ 所鄰 BA／BC／BX，本街廓 BX ∈ 之 ⇒ X9
    p9 = p7 + [("X9(1)", "BX", H, _R(20, 40, 30, 40), 40)]
    own9 = dict(own7, X9="g1")
    run("K9 所鄰二以上而其一為本街廓 ⇒ 本街廓之宗（X ⇒ X9）",
        lambda: _go(ns, p9, own9, _O(("BA", "左", "A1(1)")), drop=("X(1)",))[0],
        [("X(1)", "後處理(a)", "成", "X9(1)")])
    # K10：BB 之 g1 之 Y(1)[0,10]（30·恆⛔ 保留）隔 RD 與 BA 之 A1 相對；g1 之道路片 D1(1)（x∈[0,10]）與 Y、A1、A1b 相鄰
    #   ⇒ Y 所鄰之配得街廓為零，經 D1 而臨 BA ⇒ Y 併入 A1（4、5 地號往 6 地號）；D1 之下半鄰 BB（∉ B）⇒ D1 整片 ⇒ A1
    p10 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
           ("M(1)", "BA", H, _R(10, 40, 0, 30), 500), ("D1(1)", "RD", RDC, _R(0, 10, -10, 0), 50),
           ("MR(1)", "RD", RDC, _R(10, 40, -10, 0), 300),
           ("Y(1)", "BB", H, _R(0, 10, -40, -10), 30), ("N(1)", "BB", H, _R(10, 40, -40, -10), 500)]
    own10 = {"A1": "g1", "A1b": "g1", "D1": "g1", "Y": "g1", "M": "gM", "MR": "gM", "N": "gN"}
    run("K10 所鄰為零而經同一地主之道路片臨道路另一側之配得街廓 ⇒ 併入該側之宗（Y、D1 ⇒ A1）",
        lambda: sorted(_go(ns, p10, own10, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0]),
        sorted([("Y(1)", "後處理(a)", "成", "A1(1)"), ("D1(1)", "後處理(b)", "成", "A1(1)")]))
    # K11：BB 之 Y(1) 與 g1 之公園片 P(1)（PK·x∈[-20,0]·y∈[-40,30]·鄰 A1 與 Y）相連，⛔ 道路片 ⇒ 所鄰為零 ⇒ 第 5 項之輪：
    #   候選唯 A1（g1 之已配得之宗）⇒ 成；P 平分入 B ＝ [BA] ⇒ A1
    p11 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
           ("M(1)", "BA", H, _R(10, 40, 0, 30), 500), ("MR(1)", "RD", RDC, _R(0, 40, -10, 0), 300),
           ("P(1)", "PK", PK, _R(-20, 0, -40, 30), 40),
           ("Y(1)", "BB", H, _R(0, 10, -40, -10), 30), ("N(1)", "BB", H, _R(10, 40, -40, -10), 500)]
    own11 = {"A1": "g1", "A1b": "g1", "P": "g1", "Y": "g1", "M": "gM", "MR": "gM", "N": "gN"}
    run("K11 所鄰為零而無同一地主之道路片相鄰 ⇒ 第 5 項之輪（Y ⇒ A1）",
        lambda: sorted(_go(ns, p11, own11, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0]),
        sorted([("Y(1)", "後處理(a)", "依第5項", "—"), ("Y(1)", "後處理·第5項", "成", "A1(1)"),
                ("P(1)", "後處理(c)", "成", "A1(1)")]))
    # K12：K10 ＋ BB 之 g1 之 Z(1)[30,40]（G 300·依原位次配得·與 Y ⛔ 相鄰；N 改 [10,30]）＋ g1 之公園片 P2(1)（PK·
    #   y∈[-50,-40]·x∈[0,40]·鄰 Y 與 Z ⇒ Z 入同一合併群）⇒ 本街廓 BB ∈ B ⇒ 第 5 項，其建地之片之本街廓之候選恆先
    #   （`K-9-71`）⇒ Z（縱經 D1 而臨 BA）
    p12 = [r for r in p10 if r[0] != "N(1)"] + [("N(1)", "BB", H, _R(10, 30, -40, -10), 500),
                                                 ("Z(1)", "BB", H, _R(30, 40, -40, -10), 300),
                                                 ("P2(1)", "PK", PK, _R(0, 40, -50, -40), 20)]
    own12 = dict(own10, Z="g1", P2="g1")

    def k12():
        post = _go(ns, p12, own12, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0]
        return [r for r in post if r[0] == "Y(1)"]
    run("K12 所鄰為零而本街廓另有已配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Z）",
        k12, [("Y(1)", "後處理(a)", "依第5項", "—"), ("Y(1)", "後處理·第5項", "成", "Z(1)")])
    # K13：K1 之形而 A2 於現態恆⛔ 保留 ⇒ 仍停機（`K-9-61` ④ 另單）
    run("K13 二受併宗之一於現態未保留 ⇒ 停機（④ 另單）",
        lambda: _halt(lambda: _go(ns, p, own, od, thr=130.0, drop=("A2(1)",)), "於現態未保留"), ("停機", True))
    # K14：K5 之形 ＋ g1 之公園片 P(1)（PK·x∈[45,65]·y∈[-40,-10]·唯鄰 S3）⇒ B ＝ [BA, BB]，各一份（÷ 2）：
    #   BA ⇒ A1（唯一）；BB ⇒ S3（唯 S3 與 P 相鄰；S2 之 G 較大、S1 之暫編地號較小，皆⛔ 相鄰）
    p14 = p5 + [("P(1)", "PK", PK, _R(45, 65, -40, -10), 40)]
    own14 = dict(own5, P="g1")

    def k14():
        post, acc, _bl = _go(ns, p14, own14, od5)
        return [r for r in post if r[0] == "P(1)"]
    run("K14 公設片平分，每街廓之一份由擇定之一宗整份承受（P ⇒ A1／S3）",
        k14, [("P(1)", "後處理(c)", "成", ("A1(1)", "S3(1)"))])
    # K15：K10 之形（承受之宗唯一）而 alloc_state ⛔ 回 G ⇒ ⛔ 停機（同本批前）
    run("K15 承受之宗唯一者⛔ 須 G",
        lambda: sorted(_go(ns, p10, own10, _O(("BA", "左", "A1(1)")), drop=("Y(1)",), no_g=True)[0]),
        sorted([("Y(1)", "後處理(a)", "成", "A1(1)"), ("D1(1)", "後處理(b)", "成", "A1(1)")]))
    # K16：K1 之形而⛔ 回 G ⇒ 停機（須擇而無從定之）
    run("K16 須擇而 alloc_state 未回 G ⇒ 停機",
        lambda: _halt(lambda: _go(ns, p, own, od, thr=130.0, no_g=True), "未回 G"), ("停機", True))
    # K17：門檻 130；A1 ＝ 100 ＋ 40 ＝ 140、A2 ＝ 100 ＋ 60 ＝ 160；g1 之公園片 P5(1)（PK·x∈[5,10]·y∈[30,35]）唯與 A1 已
    #   整筆併入之 A1b 相鄰（與 A1 唯一點相接）⇒ 宗連同其所併者相鄰 ⇒ A1（縱 G 小）
    p17, own17, od17 = _two_ends(a1=100, a1b=40, a2=100, a2b=60, rs=False)
    p17 = p17 + [("P5(1)", "PK", PK, _R(5, 10, 30, 35), 10)]
    own17 = dict(own17, P5="g1")
    run("K17 相鄰以宗連同其於本段整筆併入之片判之（P5 ⇒ A1）",
        lambda: [r for r in _go(ns, p17, own17, od17, thr=130.0)[0] if r[0] == "P5(1)"],
        [("P5(1)", "後處理(c)", "成", "A1(1)")])
    # K18：BA 之 g1 之 K(1)[0,10]（80·原位次配得）、他人 M(1)[10,30]、右端 A1b(1)[30,35]／A1(1)[35,40]（取得街角·G 160）；
    #   RD 之 g1 之 D1(1)[0,10]（唯鄰 K 與 BB 之 Y）、D9(1)[10,40]（鄰 A1、A1b·與 Y 唯一點相接）；BB 之 Y(1)[0,10]（30·恆⛔
    #   保留）⇒ Y 經 D1 之遠半臨 BA，隨 D1 之受者（D1 唯鄰 K ⇒ K）——Y、D1 ⇒ K（4、5 地號往 6 地號）；D9 ⇒ A1
    p18 = [("K(1)", "BA", H, _R(0, 10, 0, 30), 80), ("M(1)", "BA", H, _R(10, 30, 0, 30), 500),
           ("A1b(1)", "BA", H, _R(30, 35, 0, 30), 60), ("A1(1)", "BA", H, _R(35, 40, 0, 30), 100),
           ("D1(1)", "RD", RDC, _R(0, 10, -10, 0), 40), ("D9(1)", "RD", RDC, _R(10, 40, -10, 0), 50),
           ("Y(1)", "BB", H, _R(0, 10, -40, -10), 30), ("N(1)", "BB", H, _R(10, 40, -40, -10), 500)]
    own18 = {"K": "g1", "A1": "g1", "A1b": "g1", "D1": "g1", "D9": "g1", "Y": "g1", "M": "gM", "N": "gN"}
    run("K18 經道路片而臨者隨該道路片之受者（Y、D1 ⇒ K；D9 ⇒ A1）",
        lambda: sorted(_go(ns, p18, own18, _O(("BA", "右", "A1(1)")), drop=("Y(1)",))[0]),
        sorted([("Y(1)", "後處理(a)", "成", "K(1)"), ("D1(1)", "後處理(b)", "成", "K(1)"),
                ("D9(1)", "後處理(b)", "成", "A1(1)")]))
    # K19：BA 左端 A1(1)[0,5]／A1b(1)[5,10]（G 160）、他人 M(1)[10,40]；RD 之 g1 之 D9(1)[0,30]、D1(1)[30,40]；RD 之東端外之
    #   BE（x∈[40,50]·y∈[-10,-5]）之 g1 之 E1(1)（G 300·原位次配得·唯與 D1 之近半〔Y 之一側〕相鄰）；BB 之 Y(1)[30,40]（30·
    #   恆⛔ 保留·唯鄰 D1）⇒ 遠半之所臨唯 BA（BE 唯臨近半 ⇒ ⛔ 計）⇒ Y ⇒ A1（縱 E1 之 G 較大·整片之相鄰則 BA／BE 二側）
    p19 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
           ("M(1)", "BA", H, _R(10, 40, 0, 30), 500), ("D9(1)", "RD", RDC, _R(0, 30, -10, 0), 50),
           ("D1(1)", "RD", RDC, _R(30, 40, -10, 0), 40), ("E1(1)", "BE", H, _R(40, 50, -10, -5), 300),
           ("N(1)", "BB", H, _R(0, 30, -40, -10), 500), ("Y(1)", "BB", H, _R(30, 40, -40, -10), 30)]
    own19 = {"A1": "g1", "A1b": "g1", "D9": "g1", "D1": "g1", "E1": "g1", "Y": "g1", "M": "gM", "N": "gN"}

    def k19():
        return [r for r in _go(ns, p19, own19, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0] if r[0] == "Y(1)"]
    run("K19 道路片之端所臨之街廓⛔ 為道路之另一側（Y ⇒ A1·⛔ E1）", k19, [("Y(1)", "後處理(a)", "成", "A1(1)")])
    # K20：K10 ＋ BB 之 g1 之 Q(1)[30,40]（200·依原位次配得·與該群⛔ 相連 ⇒ 另一合併群；N 改 [10,30]）⇒ 本街廓有同一地主
    #   之已配得之宗 ⇒ 第 5 項（本街廓之候選先）⇒ Q（縱經 D1 而臨 BA）
    p20 = [r for r in p10 if r[0] != "N(1)"] + [("N(1)", "BB", H, _R(10, 30, -40, -10), 500),
                                                 ("Q(1)", "BB", H, _R(30, 40, -40, -10), 200)]
    own20 = dict(own10, Q="g1")

    def k20():
        return [r for r in _go(ns, p20, own20, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0] if r[0] == "Y(1)"]
    run("K20 本街廓有同一地主之他群之配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Q）",
        k20, [("Y(1)", "後處理(a)", "依第5項", "—"), ("Y(1)", "後處理·第5項", "成", "Q(1)")])
    # K21：K11 之形 ⇒ 第 5 項之來源量 ＝ 整筆（a′ ＝ 30）：A1 之受併之累加 ＝ A1b 60 ＋ P 40 ＋ Y 30 ＝ 130；Y 出 build
    def k21():
        _p, acc, bl = _go(ns, p11, own11, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))
        return acc.get("A1(1)"), "Y(1)" in bl
    run("K21 所鄰為零而依第 5 項者其來源量為整筆、整筆併出（A1 130·Y 出 build）", k21, (130.0, False))
    # K22：K3 之形而 A2 之輸入帶 段三部分併出 {Z: 30} ⇒ A2 之重劃前面積 ＝ 120 − 30 ＝ 90 ＜ A1 100 ⇒ A1
    run("K22 重劃前面積扣段三部分併出（D1 ⇒ A1）",
        lambda: [r for r in _go(ns, p3, own3, od3, pre={"A2(1)": {"段三部分併出": {"Z(1)": 30.0}}})[0] if r[0] == "D1(1)"],
        [("D1(1)", "後處理(b)", "成", "A1(1)")])
    # K23：K3 之形而試算之 pool_out ＝ {A2: 30}（入池閘之帳）⇒ A2 之重劃前面積 90 ＜ 100 ⇒ A1
    run("K23 重劃前面積扣同一試算之入池閘之帳（D1 ⇒ A1）",
        lambda: [r for r in _go(ns, p3, own3, od3, pool_out={"A2(1)": 30.0})[0] if r[0] == "D1(1)"],
        [("D1(1)", "後處理(b)", "成", "A1(1)")])
    # K24：K10 之形而 BB 之 g1 之 Y2(1)[0,10]（20·恆⛔ 保留·鄰 D1）、Y(1)[10,20]（30·恆⛔ 保留·唯鄰 Y2·與 D1 唯一點相接）、
    #   他人 N(1)[20,40] ⇒ Y 與道路片⛔ 共邊 ⇒ ⛔ 經道路片 ⇒ 第 5 項；Y2 經 D1 ⇒ A1
    p24 = [r for r in p10 if r[0] not in ("Y(1)", "N(1)")] + [("Y2(1)", "BB", H, _R(0, 10, -40, -10), 20),
                                                              ("Y(1)", "BB", H, _R(10, 20, -40, -10), 30),
                                                              ("N(1)", "BB", H, _R(20, 40, -40, -10), 500)]
    own24 = dict(own10, Y2="g1")

    def k24():
        return sorted(r for r in _go(ns, p24, own24, _O(("BA", "左", "A1(1)")), drop=("Y(1)", "Y2(1)"))[0]
                      if r[0] in ("Y(1)", "Y2(1)"))
    run("K24 經道路片之判以該建地與道路片共邊為準（Y ⇒ 第 5 項；Y2 ⇒ A1）",
        k24, sorted([("Y(1)", "後處理(a)", "依第5項", "—"), ("Y(1)", "後處理·第5項", "成", "A1(1)"),
                     ("Y2(1)", "後處理(a)", "成", "A1(1)")]))
    # K25：K19 之形而 BE 之 E1(1)（x∈[40,50]·y∈[-10,0]）於段三取得 BE 之左端，② 併 D1、D9（街角地分配機制已用掉之同地主
    #   之道路土地·`K-9-73` ⑥ ⇒ ⛔ 為經之之道路片）⇒ Y 所鄰為零而無可經之道路片 ⇒ 第 5 項：候選 A1（BA·距 10）、E1（BE·
    #   距 0·點接）·五級皆同 ⇒ 距離近者 E1
    p25 = [r if r[0] != "E1(1)" else ("E1(1)", "BE", H, _R(40, 50, -10, 0), 300) for r in p19]

    def k25():
        return [r for r in _go(ns, p25, own19, _O(("BA", "左", "A1(1)"), ("BE", "左", "E1(1)")), thr=150.0,
                               drop=("Y(1)",))[0] if r[0] == "Y(1)"]
    run("K25 已為街角之合併所併出之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ E1）", k25,
        [("Y(1)", "後處理(a)", "依第5項", "—"), ("Y(1)", "後處理·第5項", "成", "E1(1)")])
    # K26：BA 左端 A1(1)[0,5]／A1b(1)[5,10]（G 160）、他人 M(1)[10,30]、g1 之 K(1)[30,40]（G 200·原位次配得）；RD 之 g1 之
    #   D1(1)[0,10]（鄰 A1、A1b）、他人 MR(1)[10,30]、g1 之 D2(1)[30,40]（鄰 K）；BB 之 g1 之 Y(1)[0,40]（30·恆⛔ 保留·鄰 D1、
    #   D2）⇒ 經 D1 之受者 A1、經 D2 之受者 K（同一街廓 BA）⇒ 二以上 ⇒ `k967_rank` ⇒ K（200 ＞ 160）
    p26 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
           ("M(1)", "BA", H, _R(10, 30, 0, 30), 500), ("K(1)", "BA", H, _R(30, 40, 0, 30), 200),
           ("D1(1)", "RD", RDC, _R(0, 10, -10, 0), 40), ("MR(1)", "RD", RDC, _R(10, 30, -10, 0), 300),
           ("D2(1)", "RD", RDC, _R(30, 40, -10, 0), 40), ("Y(1)", "BB", H, _R(0, 40, -40, -10), 30)]
    own26 = {"A1": "g1", "A1b": "g1", "K": "g1", "D1": "g1", "D2": "g1", "Y": "g1", "M": "gM", "MR": "gM"}
    run("K26 同一街廓經二道路片而其受者異 ⇒ `k967_rank`（Y ⇒ K）",
        lambda: [r for r in _go(ns, p26, own26, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0] if r[0] == "Y(1)"],
        [("Y(1)", "後處理(a)", "成", "K(1)")])
    # K27：BB 之 Y(1)[0,10]（30·恆⛔ 保留）介於 RD（上）與 RD2（y∈[-50,-40]·下）之間；RD 之 g1 之 D1(1)[0,10]（鄰 A1、A1b）、
    #   g1 之 D9(1)[10,40]（鄰 K·連 D1）；BA 之 A1(1)／A1b(1)（G 160）、他人 M(1)[10,30]、g1 之 K(1)[30,40]（G 300·⛔ 鄰 D1）；
    #   RD2 之 g1 之 D5(1)[0,10]；BF（y∈[-80,-50]）之 g1 之 F1(1)[0,10]（G 200）⇒ 二側：BA 經 D1 之受者 A1（160）、BF 經 D5
    #   之受者 F1（200）⇒ BF ⇒ Y ⇒ F1（若以 BA 之 G 最大之 K〔300〕比則誤取 BA）
    p27 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
           ("M(1)", "BA", H, _R(10, 30, 0, 30), 500), ("K(1)", "BA", H, _R(30, 40, 0, 30), 300),
           ("D1(1)", "RD", RDC, _R(0, 10, -10, 0), 40), ("D9(1)", "RD", RDC, _R(10, 40, -10, 0), 50),
           ("Y(1)", "BB", H, _R(0, 10, -40, -10), 30), ("N(1)", "BB", H, _R(10, 40, -40, -10), 500),
           ("D5(1)", "RD2", RDC, _R(0, 10, -50, -40), 20), ("MR2(1)", "RD2", RDC, _R(10, 40, -50, -40), 300),
           ("F1(1)", "BF", H, _R(0, 10, -80, -50), 200), ("MF(1)", "BF", H, _R(10, 40, -80, -50), 500)]
    own27 = {"A1": "g1", "A1b": "g1", "K": "g1", "D1": "g1", "D9": "g1", "Y": "g1", "D5": "g1", "F1": "g1",
             "M": "gM", "N": "gN", "MR2": "gM", "MF": "gM"}
    run("K27 經道路片而臨二側 ⇒ 各側以其經道路片之受者比（Y ⇒ F1）",
        lambda: [r for r in _go(ns, p27, own27, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0] if r[0] == "Y(1)"],
        [("Y(1)", "後處理(a)", "成", "F1(1)")])
    # K28：BB 之 Y(1)[0,10]（30·恆⛔ 保留）唯鄰 g1 之穿越之道路片 C(1)（RX·x∈[0,10]·y∈[-10,0]·鄰 BA、BB 與公園 PK 之他人之
    #   P9(1) ⇒ 臨三街廓而含公設 ⇒ 穿越·RX ⛔ 中心線）⇒ ⛔ 為經之之道路片（⛔ 切之）⇒ 第 5 項 ⇒ A1；C 依 (c) ⇒ A1
    p28 = [("A1(1)", "BA", H, _R(0, 5, 0, 30), 100), ("A1b(1)", "BA", H, _R(5, 10, 0, 30), 60),
           ("M(1)", "BA", H, _R(10, 40, 0, 30), 500), ("C(1)", "RX", RDC, _R(0, 10, -10, 0), 40),
           ("P9(1)", "PK", PK, _R(-10, 0, -10, 0), 50),
           ("Y(1)", "BB", H, _R(0, 10, -40, -10), 30), ("N(1)", "BB", H, _R(10, 40, -40, -10), 500)]
    own28 = {"A1": "g1", "A1b": "g1", "C": "g1", "Y": "g1", "M": "gM", "N": "gN", "P9": "gP"}
    run("K28 穿越之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ A1；C ⇒ (c)）",
        lambda: sorted(_go(ns, p28, own28, _O(("BA", "左", "A1(1)")), drop=("Y(1)",))[0]),
        sorted([("Y(1)", "後處理(a)", "依第5項", "—"), ("Y(1)", "後處理·第5項", "成", "A1(1)"),
                ("C(1)", "後處理(c)", "成", "A1(1)")]))
    return out


def _report(cases):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


def selftest(repo):
    print("── selftest（合成·K-9-61 ①②③⑥）──")
    try:
        ns = _harvest(repo)
    except Exception as ex:  # noqa: BLE001
        print(f"  ⚠️ harvest 中止：{type(ex).__name__}: {ex}")
        return 3
    cases = _cases(ns)
    red = _report(cases)
    # P0：判式自驗——逐項擾動其期，紅之集須恰為「原紅 ∪ 該項」
    bad = 0
    for i in range(len(cases)):
        r = {n.split()[0] for j, (n, g, e) in enumerate(cases) if g != (("擾動",) if j == i else e)}
        if r != set(red) | {cases[i][0].split()[0]}:
            bad += 1
    print(("  ✅" if bad == 0 else "  🔴") + f" P0 逐項擾動恰該項紅 {len(cases) - bad}／{len(cases)}")
    if bad:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _git(repo, *a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, encoding="utf-8").stdout


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
    app = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    old = _git(repo, "show", f"{base}:app.py")
    if not old:
        print("  ⚠️ 基準之 app.py 取不到")
        return 3
    k6, fn = _fn(app, "k6b_stage3_run")
    # 四字樣以執行時之拼接立之（各段長 ≤ 3·⛔ 成為長 ≥ 4 之字串常數·避 F23 W8／F24 W7 之「恰一見」之錨）
    gone = ["".join(w) for w in (("有二受", "併宗"), ("承受之", "宗未定"), ("§三", "-2 ", "未定"), ("（期恰", " 1）"))]
    left = [s for s in gone if s in k6]
    ok1 = bool(k6) and not left and "於現態未保留" in k6
    print(("  ✅" if ok1 else "  🔴") + f" X1 四停機之字樣皆去（殘 {left}）、「於現態未保留」之停機仍在")
    if not ok1:
        red.append("X1")
    defs = [n for n in ast.walk(fn) if isinstance(n, ast.FunctionDef) and n.name == "_recv_of"] if fn else []
    calls = [n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
             and n.func.id == "_recv_of"] if fn else []
    ok2 = (len(defs) == 1 and [a.arg for a in defs[0].args.args] == ["b", "y"] and calls
           and all(len(c.args) == 2 and not c.keywords for c in calls))
    print(("  ✅" if ok2 else "  🔴") + f" X2 `_recv_of(b, y)` 之形與其 {len(calls)} 呼叫皆二引數")
    if not ok2:
        red.append("X2")
    ta, tb = _top(app), _top(old)
    diff = sorted(k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k))
    ok3 = diff == ["k6b_stage3_run"] and set(ta) == set(tb)
    print(("  ✅" if ok3 else "  🔴") + f" X3 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
    if not ok3:
        red.append("X3")
    lits = sorted({n.value for n in ast.walk(fn) if isinstance(n, ast.Constant) and isinstance(n.value, str)
                   and CASE_LIT_RE.match(n.value)}) if fn else ["(無函式)"]
    print(("  ✅" if not lits else "  🔴") + f" X4 ⛔ 案件字面（{lits}）")
    if lits:
        red.append("X4")
    ch = [l for l in _git(repo, "diff", "--name-only", base, "--", "verify/").splitlines()
          if l.count("/") == 1 and l.endswith(".py")]
    print(("  ✅" if not ch else "  🔴") + f" X5 verify/ 頂層之 *.py 對基準逐位同（異 {ch}）")
    if ch:
        red.append("X5")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "selftest":
        return selftest(argv[2])
    if len(argv) >= 4 and argv[1] == "wiring":
        return wiring(argv[2], argv[3])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
