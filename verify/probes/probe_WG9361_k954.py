# -*- coding: utf-8 -*-
"""W-G.9-361 量測器（發單側窗六十擬·補令一改〔發單側窗六十一〕·補令二改〔發單側窗六十二〕·檔 F21·⛔ 由受單側改一字）：地籍相連之判之座標容差（`K-9-54`·`GB-195`）。

`K-6 §一`：合併群 ＝ 同歸戶 ∧ 幾何連通（重劃前地籍上共用線段·單點相接不算）。現碼以二片邊界之精確交集之
線長判之；二片之界線於圖上重合而其座標有微米級之差者（本案 R4／R5／R6 之分配線兩側、公園 G1 與道路 RD3 之
間），精確交集為點 ⇒ 判為不相連。`K-9-54`（KL `2026-09-30 20:34` 逐字「是」）：界線座標相差在 `0.1 mm`
以內者視為共用同一段界線（相連）。補令一（`R-2` ④″）：「座標相差」以**界址點**為之——二片之邊兩兩相對，
其互投影之重疊段之 Hausdorff 距 ≤ 容差者為共線之段（段之兩端 ＝ 某片之界址點或其投影·`K-6 §一`「兩端完全共點」
以 `0.1 mm` 讀之）；單點相接、夾角甚小之近切、重疊之淺交、界址點相差逾容差者⛔ 因容差而相連；坐標非有限者⛔ 重判。
補令二（裁四）：片之型為 `MultiPolygon` 者，其各部之環皆為片之環（同 `Polygon`·`K-9-54` 及於地籍界線而⛔ 繫於圖形之存法）；
非面狀（`Polygon`／`MultiPolygon` 以外）或空之片⛔ 重判。

子命令（一律 python verify/probes/probe_WG9361_k954.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k6_shares_segment`／`k6_merge_groups`／
           `k6_merge_selftest` 與 `K6_SHARE_MIN_LEN`、`K6_SHARE_COORD_TOL`）。
           A1〜A3 ＝ 精確之判之既有行為逐位同（共邊長 1 ⇒ (True, 1.0)；角點相接 ⇒ (False, 0.0)；
           共邊長 0.005 ⇒ (False, 0.005)）；A4〜A7 ＝ 重判（微米級之錯位而共線 ⇒ 相連、其長≈共線長；
           平行錯位 2e-4 m ⇒ 不相連；錯位在容差內而共線長未達門檻 ⇒ 不相連、其長 ＝ 精確之長；
           二片相距逾容差 ⇒ 不相連）；A8 ＝ 本案坐標量級（1e5〜1e6 m）之微米錯位；A9 ＝ 缺片 ⇒ (False, 0.0)；
           A10〜A11 ＝ 合併群（三片鏈之第二環為微米錯位 ⇒ 一群；錯位 2e-4 ⇒ 二群）；A12 ＝ 常數；
           A13 ＝ 既有之 `k6_merge_selftest()` 仍過；A14〜A19 ＝ 補令一（界址點之讀法）之否例：精確共線
           0.0099 ⇒ (False, 0.0099)；角點相接而二邊近切（斜率 0.0087）⇒ (False, 0.0)；重疊而邊界淺交 ⇒ (False, 0.0)；
           一端之界址點相差 1.5e-4 而餘段在容差內 ⇒ (False, 0.0)；中間之界址點相差 2e-4 ⇒ (False, 0.0)；坐標含 NaN
           ⇒ 二向皆不相連；A20 ＝ 重判之長二向逐位同；A21 ＝ 中間之界址點相差 5e-5（容差內）⇒ 相連、其長 ≈ 10；
           A22〜A27 ＝ 補令二（片之多邊形部分）：MultiPolygon 與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 1；
           自觸之環經 buffer(0) 成 MultiPolygon、其一部與他片微米錯位而共線 ⇒ 相連；MultiPolygon 之他部之坐標含
           NaN ⇒ 二向皆不相連；MultiPolygon 之一部平行錯位 2e-4 ⇒ (False, 0.0)；非面狀之受詞（線）與空片 ⇒ (False, 0.0)；
           以容差相連之二片之聯集（經 buffer(0) 仍為 MultiPolygon）與第三片（與其一部平行錯位 5e-5）⇒ 相連、其長 ≈ 1；
           P0 ＝ 判式自驗。
  wiring   <repo> [<基準 rev>]
           AST：W1 模組層 `K6_SHARE_COORD_TOL = 0.0001` 恰一處；W2 `k6_shares_segment` 先算精確交集
           （既有之字樣 `_it = _ba.intersection(_bb)` 存）、其後引 `K6_SHARE_COORD_TOL`；W3 除
           `k6_shares_segment` 及其所呼叫之模組層函式外，⛔ 他處引 `K6_SHARE_COORD_TOL`；W4 生產碼⛔ 案件字面；
           W5（給基準 rev 時）`app.py` 之頂層節點對基準 rev 相異者 ⊆ {`k6_shares_segment`、`K6_SHARE_COORD_TOL`、
           新增而唯為 `k6_shares_segment` 所呼叫之函式}。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R0 新判為相連之對（段三之輸入之切片·精確共線長 < 0.01 而
           相距 ≤ 1e-4 且界址點之共線長〔`_vtx_L`〕≥ 0.01）＝ `19` 對（同歸戶 `15`）、其頂點至他片界線之距之最大者
           < `2e-5 m`；R1 合併群（段三之輸入之全部重劃前切片）＝ 外部錨（本器另寫之
           判·⛔ 呼叫 `k6_shares_segment`）；R2 與精確之判相異之歸戶 ＝ `G005`／`G007`／`G012`／`G017`／`G022`，
           其群如 `GROUPS_TOL`；R3 段三之紀錄（`3.5` ⇒ `19` 列·`0.0` ⇒ `0` 列）與 `3.5` 之後處理之
           `628-20(3)`／`628-45(3)`／`628-45(4)` 三列；R4 `3.5` 之配地（三受併宗之 `G`、`R3`／`R5`／`R6` 之抵費地）。
           🔧 `W-G.9-363`（⛔ 上列一字不刪）：run 於行程內設 WV_K953=off（其期係手冊先行前之態）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FUNCS = ["k6_shares_segment", "k6_merge_groups", "k6_merge_selftest"]
CONSTS = ["K6_SHARE_MIN_LEN", "K6_SHARE_COORD_TOL"]
TOL = 1e-4
MINLEN = 0.01
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
# `K-9-54` 之後，與精確之判相異之歸戶之合併群（本案·退縮無涉·段三之輸入之切片）
GROUPS_TOL = {
    "G005": [["628-18(1)", "628-18(2)", "628-18(3)"]],
    "G007": [["628-20(1)", "628-20(2)", "628-20(3)", "628-30(1)", "628-30(2)", "628-30(3)", "628-30(4)",
              "628-45(1)", "628-45(2)", "628-45(3)", "628-45(4)", "628-45(5)"]],
    "G012": [["628-5(1)", "628-5(2)"]],
    "G017": [["628-21(1)", "628-21(2)", "628-22(1)", "628-22(2)", "628-22(3)", "628-23(1)", "628-23(2)",
              "628-23(3)"]],
    "G022": [["628-7(1)", "628-7(2)", "628-7(3)", "628-7(4)"]],
}
# 退縮 3.5 之段三後處理（`K-9-48` 讀法 5·`K-9-51`）之 G007 三列：(候選, 層級, 受併宗集, {受併宗: 併入量})
S3_ROWS_35 = [
    ("628-20(3)", "後處理(b)", ["628-20(1)"], {"628-20(1)": 42.15}),
    ("628-45(3)", "後處理(c)", ["628-20(1)", "628-45(1)", "628-45(2)"],
     {"628-20(1)": 91.03, "628-45(1)": 91.03, "628-45(2)": 91.03}),
    ("628-45(4)", "後處理(c)", ["628-20(1)", "628-45(1)", "628-45(2)"],
     {"628-20(1)": 74.8667, "628-45(1)": 74.8667, "628-45(2)": 74.8667}),
]
NEW_PAIRS = (19, 15)   # 段三之輸入之切片中，新判為相連之對之數與其中同歸戶者之數（本案）
G_35 = {"628-45(2)": 902.52, "628-45(1)": 525.28, "628-20(1)": 461.06}
POOL_35 = {"R3": 1883.03, "R5": 1742.99, "R6": 1777.33}


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__)
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
def _P(pts):
    from shapely.geometry import Polygon
    return Polygon(pts)


def _sq(x0, y0, x1, y1):
    return _P([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def _bt(res, nd=3):
    """(bool, 長) ⇒ (bool, 長之 nd 位小數)。"""
    return (bool(res[0]), round(float(res[1]), nd))


def _cases(ns):
    sh, mg = ns["k6_shares_segment"], ns["k6_merge_groups"]
    c = []
    a = _sq(0, 0, 1, 1)
    # A1〜A3：精確之判之既有行為（長度逐位）
    _run(c, "A1 精確共邊（長 1）⇒ (True, 1.0)·長度逐位", lambda: (bool(sh(a, _sq(1, 0, 2, 1))[0]),
                                                           sh(a, _sq(1, 0, 2, 1))[1] == 1.0), (True, True))
    _run(c, "A2 角點相接 ⇒ (False, 0.0)·長度逐位", lambda: (bool(sh(a, _sq(1, 1, 2, 2))[0]),
                                                      sh(a, _sq(1, 1, 2, 2))[1] == 0.0), (False, True))
    _run(c, "A3 精確共邊 0.005 ⇒ (False, 0.005)", lambda: _bt(sh(a, _sq(1, 0.995, 2, 2)), 9), (False, 0.005))
    # A4：b 之左邊自 (1+3e-6, -0.3) 至 (1-3e-6, 1.3)·與 a 之右邊（長 1）相距 ≤ 3e-6、精確交集為一點
    b4 = _P([(1 + 3e-6, -0.3), (2, -0.3), (2, 1.3), (1 - 3e-6, 1.3)])
    _run(c, "A4 微米級錯位而共線（精確交集為一點）⇒ 相連、其長 ≈ 1（三位小數）",
         lambda: (bool(sh(a, b4)[0]), round(float(sh(a, b4)[1]), 2)), (True, 1.0))
    _run(c, "A4′ 同 A4·精確交集之線長 ＝ 0（受詞確為現碼判為不相連之形）",
         lambda: round(sum(g.length for g in getattr(a.boundary.intersection(b4.boundary), "geoms",
                                                     [a.boundary.intersection(b4.boundary)])
                           if g.geom_type == "LineString"), 9), 0.0)
    # A5：平行錯位 2e-4（逾容差）⇒ 不相連、其長 ＝ 精確之長 0
    _run(c, "A5 平行錯位 2e-4 m ⇒ (False, 0.0)", lambda: _bt(sh(a, _sq(1 + 2e-4, 0, 2, 1)), 9), (False, 0.0))
    # A6：錯位 5e-5（容差內）而共線之長 0.008 ⇒ 不相連、其長 ＝ 精確之長 0
    b6 = _sq(1 + 5e-5, 0.992, 2, 2)
    _run(c, "A6 容差內而共線長 0.008 ⇒ (False, 0.0)", lambda: _bt(sh(a, b6), 9), (False, 0.0))
    # A7：二片相距 0.01（逾容差）⇒ 不相連
    _run(c, "A7 相距 0.01 m ⇒ (False, 0.0)", lambda: _bt(sh(a, _sq(1.01, 0, 2, 1)), 9), (False, 0.0))
    # A8：本案坐標量級之微米錯位（共線長 12）
    X0, Y0 = 310500.0, 2651850.0
    a8 = _P([(X0, Y0), (X0 + 10, Y0), (X0 + 10, Y0 + 12), (X0, Y0 + 12)])
    b8 = _P([(X0 + 10 + 2e-6, Y0 - 1), (X0 + 20, Y0 - 1), (X0 + 20, Y0 + 13), (X0 + 10 - 2e-6, Y0 + 13)])
    _run(c, "A8 坐標 ~3e5／2.6e6 m 之微米錯位（共線長 12）⇒ 相連、其長 ≈ 12",
         lambda: (bool(sh(a8, b8)[0]), round(float(sh(a8, b8)[1]), 1)), (True, 12.0))
    _run(c, "A9 缺片（None）⇒ (False, 0.0)", lambda: _bt(sh(None, a), 9), (False, 0.0))
    pk = lambda poly, ono: {"polygon": poly, "原地號": ono}  # noqa: E731
    A, B = _sq(0, 0, 1, 1), _sq(1, 0, 2, 1)
    C1 = _P([(2 + 3e-6, -0.2), (3, -0.2), (3, 1.2), (2 - 3e-6, 1.2)])
    C2 = _sq(2 + 2e-4, 0, 3, 1)
    own = {"A": "G1", "B": "G1", "C": "G1"}
    _run(c, "A10 三片鏈（A–B 精確、B–C 微米錯位）⇒ 一群",
         lambda: mg([pk(A, "A"), pk(B, "B"), pk(C1, "C")], own), [[0, 1, 2]])
    _run(c, "A11 三片鏈（B–C 平行錯位 2e-4）⇒ 二群",
         lambda: mg([pk(A, "A"), pk(B, "B"), pk(C2, "C")], own), [[0, 1], [2]])
    _run(c, "A12 常數 K6_SHARE_COORD_TOL ＝ 1e-4、K6_SHARE_MIN_LEN ＝ 0.01",
         lambda: (ns["K6_SHARE_COORD_TOL"], ns["K6_SHARE_MIN_LEN"]), (TOL, MINLEN))
    _run(c, "A13 既有之 k6_merge_selftest() 仍過（S-1〜S-7）",
         lambda: len(ns["k6_merge_selftest"]()) >= 16, True)
    # A14〜A21：補令一（`R-2` ④″·界址點之讀法）
    a10 = _P([(0, 0), (10, 0), (10, -5), (0, -5)])
    _run(c, "A14 精確共線 0.0099（容差不增其長）⇒ (False, 0.0099)",
         lambda: _bt(sh(a, _sq(1, 0, 2, 0.0099)), 9), (False, 0.0099))
    _run(c, "A15 角點相接而二邊近切（斜率 0.0087）⇒ (False, 0.0)",
         lambda: _bt(sh(a10, _P([(0, 0), (10, 0.087), (10, 5), (0, 5)])), 9), (False, 0.0))
    _run(c, "A16 二片重疊而邊界淺交（斜率 0.0087）⇒ (False, 0.0)",
         lambda: _bt(sh(a10, _P([(2, -0.0261), (8, 0.0261), (8, 5), (2, 5)])), 9), (False, 0.0))
    _run(c, "A17 一端之界址點相差 1.5e-4、他端 5e-5（中段在容差內）⇒ (False, 0.0)",
         lambda: _bt(sh(_P([(0, 0), (20, 0), (20, -5), (0, -5)]), _P([(0, 1.5e-4), (20, 5e-5), (20, 5), (0, 5)])), 9),
         (False, 0.0))
    _run(c, "A18 中間之界址點相差 2e-4 ⇒ (False, 0.0)",
         lambda: _bt(sh(a10, _P([(0, 0), (5, 2e-4), (10, 0), (10, 5), (0, 5)])), 9), (False, 0.0))
    def _a19():
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            b19 = _P([(1 + 3e-6, -0.3), (2, -0.3), (1.5, float("nan")), (2, 1.3), (1 - 3e-6, 1.3)])
            return (bool(sh(a, b19)[0]), bool(sh(b19, a)[0]))
    _run(c, "A19 坐標含 NaN（共線之邊在容差內）⇒ 二向皆不相連", _a19, (False, False))
    _run(c, "A20 重判之長二向逐位同（A4 之形）",
         lambda: (bool(sh(a, b4)[0]), sh(a, b4)[1] == sh(b4, a)[1]), (True, True))
    _run(c, "A21 中間之界址點相差 5e-5（容差內）⇒ 相連、其長 ≈ 10（三位小數）",
         lambda: _bt(sh(a10, _P([(0, 0), (5, 5e-5), (10, 0), (10, 5), (0, 5)])), 3), (True, 10.0))
    # A22〜A27：補令二（裁四·片之多邊形部分）
    from shapely.geometry import MultiPolygon, LineString
    m22 = MultiPolygon([a])
    _run(c, "A22 MultiPolygon 與他片微米錯位而共線（A4 之形）⇒ 二向皆相連、其長 ≈ 1",
         lambda: (bool(sh(m22, b4)[0]), round(float(sh(m22, b4)[1]), 2), bool(sh(b4, m22)[0])), (True, 1.0, True))
    f23 = _P([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (1, 2), (1, 1), (0, 1)]).buffer(0)
    b23 = _P([(2 + 3e-6, 0.7), (3, 0.7), (3, 2.3), (2 - 3e-6, 2.3)])
    _run(c, "A23 自觸之環經 buffer(0) 成 MultiPolygon（二部）、其一部與他片微米錯位而共線 ⇒ 相連、其長 ≈ 1",
         lambda: (f23.geom_type, len(f23.geoms), _bt(sh(f23, b23), 2)), ("MultiPolygon", 2, (True, 1.0)))
    def _a24():
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            m24 = MultiPolygon([a, _P([(5, 5), (6, 5), (5.5, float("nan")), (6, 6), (5, 6)])])
            return (bool(sh(m24, b4)[0]), bool(sh(b4, m24)[0]))
    _run(c, "A24 MultiPolygon 之他部之坐標含 NaN（共線之部在容差內）⇒ 二向皆不相連", _a24, (False, False))
    _run(c, "A25 MultiPolygon 之一部與他片平行錯位 2e-4 ⇒ (False, 0.0)",
         lambda: _bt(sh(MultiPolygon([a, _sq(5, 5, 6, 6)]), _sq(1 + 2e-4, 0, 2, 1)), 9), (False, 0.0))
    l26 = LineString([(1 + 1e-6, 0), (1 + 1e-6, 1)])
    _run(c, "A26 非面狀之受詞（線·沿 A1 之共邊微米錯位）二向與空片 ⇒ 皆 (False, 0.0)",
         lambda: (_bt(sh(l26, a), 9), _bt(sh(a, l26), 9), _bt(sh(_P([]), a), 9)),
         ((False, 0.0), (False, 0.0), (False, 0.0)))
    from shapely.ops import unary_union
    u27 = unary_union([a, _sq(1 + 5e-5, 0, 2, 1)]).buffer(0)
    _run(c, "A27 以容差相連之二片之聯集（buffer(0) 後仍為 MultiPolygon）與第三片平行錯位 5e-5 ⇒ 相連、其長 ≈ 1",
         lambda: (u27.geom_type, _bt(sh(u27, _sq(2 + 5e-5, 0, 3, 1)), 2)), ("MultiPolygon", (True, 1.0)))
    return c


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in FUNCS + CONSTS if n not in ns]
    if [n for n in miss if n in FUNCS]:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    if miss:
        print(f"  🔴 受詞缺（常數）：{miss}——續跑行為之例（其例以例外記）")
    print("── 合成對照（harvest 之 app.py·⛔ 本案資料）──")
    cases = _cases(ns)
    red = (["受詞缺"] if miss else []) + _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    names = [c[0].split()[0] for c in cases]
    n_ok = 0
    base_red = [r for r in red if r != "受詞缺"]
    for i, (name, got, exp) in enumerate(cases):
        pert = [(n, g, ("擾動", e) if j == i else e) for j, (n, g, e) in enumerate(cases)]
        rr = _report(pert, verbose=False)
        n_ok += int(rr == sorted(set(base_red) | {name.split()[0]}, key=names.index))
    ok0 = n_ok == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {n_ok}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
def _top(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out.setdefault(n.name, []).append(n)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out.setdefault(t.id, []).append(n)
    return out


def _calls(fn):
    return {n.func.id for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}


def _wiring_checks(src, base_src):
    tree = ast.parse(src)
    top = _top(tree)
    chk = []
    asg = top.get("K6_SHARE_COORD_TOL", [])
    val = None
    if len(asg) == 1 and isinstance(asg[0].value, ast.Constant):
        val = asg[0].value.value
    chk.append(("W1 模組層 K6_SHARE_COORD_TOL = 0.0001 恰一處", len(asg) == 1 and val == TOL,
                f"賦值 {len(asg)} 處·值 {val!r}"))
    fns = top.get("k6_shares_segment", [])
    ok2, note2 = False, "無 k6_shares_segment"
    helpers = set()
    if len(fns) == 1:
        seg = ast.get_source_segment(src, fns[0]) or ""
        i_ex = seg.find("_it = _ba.intersection(_bb)")
        i_tol = seg.find("K6_SHARE_COORD_TOL")
        ok2 = i_ex >= 0 and i_tol > i_ex
        note2 = f"精確交集之字樣於 {i_ex}·容差之引於 {i_tol}"
        helpers = {h for h in _calls(fns[0]) if h in top and isinstance(top[h][0], ast.FunctionDef)}
    chk.append(("W2 k6_shares_segment 先算精確交集、其後引 K6_SHARE_COORD_TOL", ok2, note2))
    users = sorted({n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)
                    and any(isinstance(x, ast.Name) and x.id == "K6_SHARE_COORD_TOL" for x in ast.walk(n))})
    allowed = {"k6_shares_segment"} | helpers
    chk.append(("W3 K6_SHARE_COORD_TOL 唯 k6_shares_segment 及其所呼叫之函式引之",
                bool(users) and set(users) <= allowed, f"引之者 {users}；許 {sorted(allowed)}"))
    lits = []
    for nm in ["k6_shares_segment"] + sorted(helpers):
        for fn in top.get(nm, []):
            for x in ast.walk(fn):
                if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
                    lits.append((nm, x.value))
    chk.append(("W4 k6_shares_segment 及其所呼叫之函式⛔ 案件字面", not lits, f"{lits}"))
    if base_src is not None:
        btop = _top(ast.parse(base_src))
        dump = lambda ns_: {k: [ast.dump(v) for v in vs] for k, vs in ns_.items()}  # noqa: E731
        a_, b_ = dump(top), dump(btop)
        diff = sorted(k for k in set(a_) | set(b_) if a_.get(k) != b_.get(k))
        new_helpers = {h for h in helpers if h not in btop}
        ok5 = set(diff) <= ({"k6_shares_segment", "K6_SHARE_COORD_TOL"} | new_helpers)
        chk.append(("W5 頂層節點對基準 rev 相異者 ⊆ {k6_shares_segment, K6_SHARE_COORD_TOL, 新增之其所呼叫者}",
                    ok5, f"相異 {diff}"))
    return chk


def wiring(repo, base=None):
    src = _read(repo, "app.py")
    base_src = None
    if base:
        try:
            base_src = subprocess.run(["git", "-C", repo, "show", f"{base}:app.py"], capture_output=True,
                                      check=True).stdout.decode("utf-8")
        except Exception as e:  # noqa: BLE001
            print(f"🔴 取不到基準 rev {base!r} 之 app.py：{e} ⇒ 無從判定")
            return 3
    red = []
    print("── 接線（AST·app.py）──")
    for name, ok, note in _wiring_checks(src, base_src):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run ──
def _lin(g):
    t, st = 0.0, [g]
    while st:
        x = st.pop()
        if x is None or x.is_empty:
            continue
        if x.geom_type in ("LineString", "LinearRing"):
            t += x.length
        elif hasattr(x, "geoms"):
            st.extend(x.geoms)
    return t


def _vtx_L(pa, pb, tol):
    """外部錨（⛔ 呼叫 k6_shares_segment·補令一）：界址點之讀法之共線長。二片之邊兩兩相對：以一方之邊為軸，取他方
    之邊之投影與之重疊之段（二邊各一子段），其 Hausdorff 距 ≤ tol 者計入；各邊所得之段取聯集計長；二軸 × 二片之
    四長取其小。"""
    from shapely.geometry import LineString

    def segs(p):
        out = []
        for r in _rings(p):
            cs = [tuple(c[:2]) for c in r.coords]
            out += [(cs[i], cs[i + 1]) for i in range(len(cs) - 1) if cs[i] != cs[i + 1]]
        return out

    def ulen(iv):
        tot, cur = 0.0, None
        for lo, hi in sorted(iv):
            if cur is not None and lo <= cur[1]:
                cur[1] = max(cur[1], hi)
            else:
                if cur is not None:
                    tot += cur[1] - cur[0]
                cur = [lo, hi]
        return tot + (cur[1] - cur[0] if cur is not None else 0.0)

    def axis(SX, SY):
        ix, iy = [[] for _ in SX], [[] for _ in SY]
        for i, ((x0, y0), (x1, y1)) in enumerate(SX):
            ls = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
            ux, uy = (x1 - x0) / ls, (y1 - y0) / ls
            for j, ((p0, q0), (p1, q1)) in enumerate(SY):
                u0, u1 = (p0 - x0) * ux + (q0 - y0) * uy, (p1 - x0) * ux + (q1 - y0) * uy
                if u0 == u1:
                    continue
                lo, hi = max(0.0, min(u0, u1)), min(ls, max(u0, u1))
                if hi <= lo:
                    continue
                f0, f1 = (lo - u0) / (u1 - u0), (hi - u0) / (u1 - u0)
                s_ = LineString([(x0 + lo * ux, y0 + lo * uy), (x0 + hi * ux, y0 + hi * uy)])
                t_ = LineString([(p0 + f0 * (p1 - p0), q0 + f0 * (q1 - q0)), (p0 + f1 * (p1 - p0), q0 + f1 * (q1 - q0))])
                if s_.hausdorff_distance(t_) <= tol:
                    ix[i].append((lo, hi))
                    lt = ((p1 - p0) ** 2 + (q1 - q0) ** 2) ** 0.5
                    iy[j].append((min(f0, f1) * lt, max(f0, f1) * lt))
        return sum(ulen(v) for v in ix), sum(ulen(v) for v in iy)

    SA, SB = segs(pa), segs(pb)
    a1, b1 = axis(SA, SB)
    b2, a2 = axis(SB, SA)
    return min(a1, b1, a2, b2)


def _parts(p):
    """補令二（裁四）：片之多邊形部分（`Polygon` ⇒ 其本身；`MultiPolygon` ⇒ 其各部）；他型或空 ⇒ None。"""
    if p is None or p.is_empty:
        return None
    if p.geom_type == "Polygon":
        return [p]
    if p.geom_type == "MultiPolygon":
        return list(p.geoms)
    return None


def _rings(p):
    return [r for q in _parts(p) for r in [q.exterior] + list(q.interiors)]


def _finite(p):
    import math
    return all(math.isfinite(c[0]) and math.isfinite(c[1]) for r in _rings(p) for c in r.coords)


def _conn_ext(pa, pb, tol):
    """外部錨（⛔ 呼叫 k6_shares_segment）：精確共邊之線長 ≥ 0.01，或（tol 非 None 且）二片皆為非空之 `Polygon`／
    `MultiPolygon`、坐標皆有限、相距 ≤ tol 而界址點之共線長（`_vtx_L`）≥ 0.01。"""
    if pa is None or pb is None:
        return False
    if _lin(pa.boundary.intersection(pb.boundary)) >= MINLEN:
        return True
    if tol is None or _parts(pa) is None or _parts(pb) is None:
        return False
    if not (_finite(pa) and _finite(pb)) or pa.distance(pb) > tol:
        return False
    return _vtx_L(pa, pb, tol) >= MINLEN


def _new_pairs(temp):
    """精確共線長 < 0.01 而（相距 ≤ TOL 且）界址點之共線長（`_vtx_L`）≥ 0.01 之對；並回諸對之頂點至他片界線之距之最大者
    （唯計距 ≤ TOL 之頂點）。對之元 ＝ (暫編地號, 原地號, 街廓)。"""
    from shapely.geometry import Polygon, Point
    ps = []
    for t in temp:
        cs = t.get("polygon_coords") or []
        if len(cs) >= 3:
            ps.append(((str(t["暫編地號"]), str(t.get("原地號", "")), str(t.get("所屬街廓", ""))), Polygon(cs)))
    ps.sort(key=lambda x: x[0][0])
    out, mx = [], 0.0
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            (ka, A), (kb, B) = ps[i], ps[j]
            if A.distance(B) > TOL or _lin(A.boundary.intersection(B.boundary)) >= MINLEN:
                continue
            if _vtx_L(A, B, TOL) < MINLEN:
                continue
            out.append((ka, kb))
            for X, Y in ((A, B), (B, A)):
                for v in X.exterior.coords:
                    d = Y.boundary.distance(Point(v))
                    if d <= TOL:
                        mx = max(mx, d)
    return out, mx


def _groups_ext(temp, own, tol):
    from shapely.geometry import Polygon
    by = {}
    for t in temp:
        g = str(own.get(str(t.get("原地號", "")), "") or "")
        cs = t.get("polygon_coords") or []
        if g:
            by.setdefault(g, []).append((str(t["暫編地號"]), Polygon(cs) if len(cs) >= 3 else None))
    out = {}
    for g, lst in by.items():
        adj = {p: set() for p, _ in lst}
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if _conn_ext(lst[i][1], lst[j][1], tol):
                    adj[lst[i][0]].add(lst[j][0])
                    adj[lst[j][0]].add(lst[i][0])
        seen, comps = set(), []
        for s in sorted(adj):
            if s in seen:
                continue
            comp, stk = [], [s]
            seen.add(s)
            while stk:
                u = stk.pop()
                comp.append(u)
                for v in sorted(adj[u] - seen):
                    seen.add(v)
                    stk.append(v)
            comps.append(sorted(comp))
        out[g] = sorted(comps)
    return out


def _groups_code(ns, temp, own):
    from shapely.geometry import Polygon
    pk = [{"原地號": t.get("原地號", ""),
           "polygon": Polygon(t["polygon_coords"]) if len(t.get("polygon_coords") or []) >= 3 else None}
          for t in temp]
    out = {}
    for g in ns["k6_merge_groups"](pk, own):
        gid = str(own.get(str(temp[g[0]].get("原地號", "")), ""))
        out.setdefault(gid, []).append(sorted(str(temp[i]["暫編地號"]) for i in g))
    return {k: sorted(v) for k, v in out.items()}


def run(repo, sbs):
    # 🔧 `W-G.9-363`（發單側窗六十四）：本器 run 之期（R3／R4）係手冊先行（`K-9-53` ①）前之態 ⇒ 行程內設 WV_K953=off
    os.environ["WV_K953"] = "off"
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        miss = [n for n in FUNCS + CONSTS if n not in ns]
        if [n for n in miss if n in FUNCS]:
            print(f"  🔴 受詞缺：{miss}")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        if miss:
            print(f"  🔴 受詞缺（常數）：{miss}——續跑本案之量")
            red.append("受詞缺")
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g
        done_groups = False
        for sb in sbs:
            with contextlib.redirect_stdout(io.StringIO()):
                snapshot = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
            print(f"══ 退縮 {sb} ══")
            if not done_groups:
                done_groups = True
                pairs, mx = _new_pairs(temp_p)
                n_same = sum(1 for a, b in pairs if own.get(a[1]) and own.get(a[1]) == own.get(b[1]))
                ok0 = (len(pairs), n_same) == NEW_PAIRS and mx < TOL / 5
                print(("  ✅" if ok0 else "  🔴") + f" R0 新判為相連之對 {len(pairs)}（同歸戶 {n_same}）＝ 期 {NEW_PAIRS}；"
                      f"頂點至他片界線之距之最大者 {mx:.3e} m（< {TOL / 5:.0e}）")
                for a, b in pairs:
                    print(f"     {a[0]}〔{a[2]}·{own.get(a[1], '—')}〕–{b[0]}〔{b[2]}·{own.get(b[1], '—')}〕")
                if not ok0:
                    red.append("R0")
                code = _groups_code(ns, temp_p, own)
                ext_t = _groups_ext(temp_p, own, TOL)
                ext_e = _groups_ext(temp_p, own, None)
                d1 = sorted(g for g in set(code) | set(ext_t) if code.get(g) != ext_t.get(g))
                print(("  ✅" if not d1 else "  🔴") + f" R1 合併群（{len(temp_p)} 片·{len(code)} 歸戶）＝ 外部錨：相異 {d1}")
                if d1:
                    red.append("R1")
                chg = sorted(g for g in set(ext_t) | set(ext_e) if ext_t.get(g) != ext_e.get(g))
                ok2 = chg == sorted(GROUPS_TOL) and all(code.get(g) == GROUPS_TOL[g] for g in GROUPS_TOL)
                print(("  ✅" if ok2 else "  🔴") + f" R2 與精確之判相異之歸戶 {chg}；其群 ＝ GROUPS_TOL："
                      f"{all(code.get(g) == GROUPS_TOL[g] for g in GROUPS_TOL)}")
                if not ok2:
                    red.append("R2")
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
                    log = list(fake_st.session_state.get("f3_k6b_stage3_log") or [])
                    ns["K917_DROPPED"].clear()
                    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                                    eff_min_build_by_blk={})
            except RuntimeError as e:
                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
                return 3
            n_exp = 19 if abs(sb - 3.5) < 1e-9 else (0 if abs(sb) < 1e-9 else None)
            rows = []
            ok3 = n_exp is None or len(log) == n_exp
            if abs(sb - 3.5) < 1e-9:
                for cand, lvl, recvs, qty in S3_ROWS_35:
                    r = next((x for x in log if x.get("候選") == cand and x.get("序") == "後處理"), None)
                    got = None if r is None else (r.get("層級"), sorted(r["受併宗"]) if isinstance(r.get("受併宗"), list)
                                                  else [r.get("受併宗")], r.get("結果"),
                                                  {k: round(float(v), 2) for k, v in (r.get("併入量") or {}).items()})
                    exp = (lvl, recvs, "成", {k: round(v, 2) for k, v in qty.items()})
                    rows.append((cand, got == exp, got))
                    ok3 = ok3 and got == exp
            print(("  ✅" if ok3 else "  🔴") + f" R3 段三之紀錄 {len(log)} 列（期 {n_exp}）"
                  + "".join(f"；{c} {'✅' if o else '🔴 ' + repr(g)}" for c, o, g in rows))
            if not ok3:
                red.append(f"R3@{sb}")
            if abs(sb - 3.5) < 1e-9:
                gg = {str(r.get("暫編地號")): float(r.get("G(㎡)") or 0) for r in sg["g_rows"]
                      if r.get("推進側別") in ("left", "right")}
                pools = {}
                for r in sg["g_rows"]:
                    if r.get("推進側別") == "抵費地" and r.get("cut_coords") and not isinstance(r.get("cut_coords"), str):
                        from shapely.geometry import Polygon
                        pools[r.get("所屬街廓")] = pools.get(r.get("所屬街廓"), 0.0) + Polygon(r["cut_coords"]).buffer(0).area
                okg = all(abs(gg.get(k, -1) - v) <= 0.01 for k, v in G_35.items())
                okp = all(abs(pools.get(k, -1) - v) <= 0.01 for k, v in POOL_35.items())
                print(("  ✅" if okg and okp else "  🔴") + " R4 配地：" +
                      "、".join(f"{k} G {gg.get(k, float('nan')):.2f}（期 {v:.2f}）" for k, v in G_35.items()) + "；抵費地 " +
                      "、".join(f"{k} {pools.get(k, float('nan')):.2f}（期 {v:.2f}）" for k, v in POOL_35.items()))
                if not (okg and okp):
                    red.append("R4")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3 or argv[1] not in ("selftest", "wiring", "run"):
        print(__doc__)
        return 2
    repo = os.path.abspath(argv[2])
    if argv[1] == "selftest":
        return selftest(repo)
    if argv[1] == "wiring":
        return wiring(repo, argv[3] if len(argv) > 3 else None)
    sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
    return run(repo, sbs)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
