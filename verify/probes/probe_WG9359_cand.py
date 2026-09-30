# -*- coding: utf-8 -*-
"""W-G.9-359 量測器（發單側窗五十六擬·檔 F18·⛔ 由受單側改一字）：調配之候選街廓名單（規格步 `3`·五級八鍵·
`K-9-52`：正面道路只限「道路」類之街廓；「次一級路寬」以本區實有之路寬逐級往窄、較寬者排最後；深度相差 `0.1 m`
以內視為同深〔只用於候選街廓之先後〕）。

子命令（一律 python verify/probes/probe_WG9359_cand.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `adj_q2`／`adj_block_ctx`／`adj_pool_anchor`／
           `adj_candidate_lists`／`adj_candidate_rows` 與 `ADJ_DEPTH_TIE_TOL_M`、`F3_CATEGORY_FRONT_ROAD`）。
           C1〜C18 ＝ 八鍵各鍵之決勝（使用分區／最小建築面積〔往小、往大、第二趟排除〕／正面道路／正面路寬／
           次一級路寬〔問二附圖之例〕／深度〔0.10 同深·0.11 較淺〕／距離／街廓名）、公設軌、錨點、原街廓居首、
           停機、抵費地之迄點、類別表、顯示列、四捨五入、深度差之 2 位；C19〜C22 ＝ 補令一（退化之池列⛔ 計、
           錨點退化 ⇒ 停機、自交之錨點以 buffer(0) 之質心、最小建築面積非數／非有限／負 ⇒ 停機）；P0 ＝ 判式自驗。
           🔒 以程式字樣為錨之突變（判別力）⛔ 載於本器——規格單流程由發單側讀受單側之碼後補寫（`W-G.9-359 §四-2`）。
  wiring   <repo>
           AST ＋ 畫面區塊之合成執行：W1 具名常數 ＝ `0.1`、二函式之預設引用之、新函式內⛔ 字面 `0.1`／`0.5`；
           W2 類別表之鍵 ＝ `F3_BLOCK_CATEGORIES`、唯「道路」為真；W3 正面道路推導之候選 ＝ 非可建築 ∩ 類別表為真者；
           W4 新函式⛔ 案件字面、⛔ 讀 session、⛔ 含既有閘所禁之消費字樣；W5 `main()` 之候選街廓區塊（自
           `_adj359_bf` 之賦值起連續 `2` 句）以假 st ＋ 合成資料實際執行（名稱以 `id` 取、路寬取 `f3_sb_rows`、
           深度取 `f3_alloc_depth_by_label`、最小建築面積取 `K91_SS_MBA_EFFECTIVE`·四變體各有其誘餌）；
           W6 `verify/run_verification.py` 之 `FRONT_ROAD_NAMES`／`load_front_road_names`。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R0 區外道路名稱檔；R1 正面道路推導（候選皆「道路」類·推導 ＝
           `W-G.9-350 §一` 項 `5` 之表）；R2 名單⛔ 停機且與外部錨（本器另寫之排序·⛔ 呼叫名單之函式）逐單位逐序相同；
           R3 畫面區塊以假 st 於本案資料實跑，其二表 ＝ harness 之顯示列；R4 `K-9-52` ③ 之可見效果（原街廓 R6
           之建地軌單位：`0.1` ⇒ R6、R2、R3、R5、R1、R4；以 `0.5` 重算 ⇒ R6、R5、R2、R3、R1、R4）；
           R5 公設軌之名單 ＝ 全部可建築街廓、距離不減。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, math, os, re, sys
from decimal import Decimal, ROUND_HALF_UP

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FUNCS = ["adj_q2", "adj_block_ctx", "adj_pool_anchor", "adj_candidate_lists", "adj_candidate_rows"]
CONSTS = ["ADJ_DEPTH_TIE_TOL_M", "ADJ_POOL_SIDE", "ADJ_TRACK_BUILD", "ADJ_TRACK_PUBLIC",
          "F3_BLOCK_CATEGORIES", "F3_CATEGORY_FRONT_ROAD"]
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
FORBID_TOKS = ["adj_intake", "SS_ADJ_BUILD_FINAL", "SS_ADJ_DROPPED", "f3_k929_6", "r3_front_road",
               "SS_FRONT_ROAD", "front_road_derive", "session_state"]
D = Decimal


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _extract_ns(src, funcs=FUNCS, consts=CONSTS, prefixes=()):
    """自 `app.py` 以 AST 抽出所列之常數與函式，於隔離之命名空間執行。"""
    tree = ast.parse(src)
    parts = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and (node.targets[0].id in consts or node.targets[0].id.startswith(tuple(prefixes) or ("\0",))):
            parts.append(ast.get_source_segment(src, node))
    ns = {}
    exec(compile("\n\n".join(parts), "<cand_extract>", "exec"), ns)
    return ns


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
H, CM = "住宅區", "商業區"


def _sq(cx, cy, h=1.0):
    return [[cx - h, cy - h], [cx + h, cy - h], [cx + h, cy + h], [cx - h, cy + h]]


def _ctx(ns, spec):
    """spec ＝ {label: (使用分區, 最小建築面積, 正面道路, 正面路寬, 深度)}。"""
    L = sorted(spec)
    return ns["adj_block_ctx"](L, {k: spec[k][0] for k in L}, {k: spec[k][1] for k in L},
                               {k: spec[k][2] for k in L}, {k: spec[k][3] for k in L}, {k: spec[k][4] for k in L})


def _unit(ns, g, build, home, slices):
    rows = [{"暫編地號": p, "原有面積": float(a)} for p, a in slices]
    return {"歸戶": g, "軌": ns["ADJ_TRACK_BUILD"] if build else ns["ADJ_TRACK_PUBLIC"], "原街廓": home,
            "建築街廓內不能分配": rows, "共同負擔用地": []}


def _lists(ns, spec, pools, units, coords=None, **kw):
    coords = coords if coords is not None else {"u": _sq(0.0, 0.0)}
    return ns["adj_candidate_lists"]({"units": units}, _ctx(ns, spec), pools, coords, **kw)


def _seq(res, i=0):
    return [it["街廓"] for it in res[i]["名單"]]


def _one(ns, spec, pools, home="S", **kw):
    return _lists(ns, spec, pools, [_unit(ns, "g1", True, home, [("u", 100.0)])], **kw)


def _cases(ns):
    out = []
    X = lambda d: (d, 0.0)  # noqa: E731
    # C1 使用分區
    s1 = {"S": (H, 0, "X", 8, 40), "A": (CM, 0, "X", 8, 40), "B": (H, 0, "Y", 6, 50)}
    _run(out, "C1 使用分區相同者先（縱其他鍵較差、距離較遠）",
         lambda: _seq(_one(ns, s1, {"A": X(10), "B": X(100), "S": X(1)})), ["S", "B", "A"])
    # C2 最小建築面積
    s2 = {"S": (H, 150, "X", 8, 40), "a": (H, 100, "X", 8, 40), "b": (H, 0, "X", 8, 40),
          "c": (H, 200, "X", 8, 40), "d": (H, 150, "X", 8, 40)}
    p2 = {"a": X(40), "b": X(30), "c": X(10), "d": X(50), "S": X(1)}
    _run(out, "C2 最小建築面積：同級 → 往小（次一級先）→ 往大；往大者第二趟排除",
         lambda: [(it["街廓"], it["最小建築面積"], it["第二趟排除"]) for it in _one(ns, s2, p2)[0]["名單"][1:]],
         [("d", "同級", False), ("a", "往小 1 級", False), ("b", "往小 2 級", False), ("c", "往大 1 級", True)])
    # C3 正面道路
    s3 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "Y", 8, 40), "B": (H, 0, "X", 8, 40)}
    _run(out, "C3 正面道路相同者先", lambda: _seq(_one(ns, s3, {"A": X(5), "B": X(50)})), ["S", "B", "A"])
    # C4 正面路寬
    s4 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "Y", 10, 40), "B": (H, 0, "Z", 8, 40)}
    _run(out, "C4 正面路寬相同者先", lambda: _seq(_one(ns, s4, {"A": X(5), "B": X(50)})), ["S", "B", "A"])
    # C5 次一級路寬（問二附圖之例）
    s5 = {"S": (H, 0, "A", 12, 40), "T1": (H, 0, "B", 12, 40), "T2": (H, 0, "C", 10, 40),
          "T3": (H, 0, "D", 8, 40), "T4": (H, 0, "E", 6, 40), "T5": (H, 0, "F", 15, 40), "T6": (H, 0, "G", 20, 40)}
    p5 = {"T1": X(60), "T2": X(50), "T3": X(40), "T4": X(30), "T5": X(20), "T6": X(10)}
    _run(out, "C5 次一級路寬：本區實有路寬逐級往窄，較寬者排最後（問二附圖）",
         lambda: [(it["街廓"], it["路寬級距"]) for it in _one(ns, s5, p5)[0]["名單"][1:]],
         [("T1", "同級"), ("T2", "往窄 1 級"), ("T3", "往窄 2 級"), ("T4", "往窄 3 級"),
          ("T5", "往寬 1 級"), ("T6", "往寬 2 級")])
    # C6 深度（容差 0.1）
    s6 = {"S": (H, 0, "X", 8, 40.00), "a": (H, 0, "X", 8, 40.10), "b": (H, 0, "X", 8, 39.89),
          "c": (H, 0, "X", 8, 39.50), "d": (H, 0, "X", 8, 40.11), "e": (H, 0, "X", 8, 42.00),
          "f": (H, 0, "X", 8, 39.90)}
    p6 = {"a": X(60), "f": X(50), "b": X(40), "c": X(30), "d": X(20), "e": X(10)}
    _run(out, "C6 深度：相差 0.10 以內同深（再依距離）→ 較淺（差小者先）→ 較深（差小者先）",
         lambda: [(it["街廓"], it["深度"]) for it in _one(ns, s6, p6)[0]["名單"][1:]],
         [("f", "同深"), ("a", "同深"), ("b", "較淺"), ("c", "較淺"), ("d", "較深"), ("e", "較深")])
    _run(out, "C7 深度：以 tol ＝ 0.5 重算 ⇒ 0.50 以內皆同深（依距離）",
         lambda: _seq(_one(ns, s6, p6, tol=0.5)), ["S", "d", "c", "b", "f", "a", "e"])
    # C8 距離；無抵費地者排於同鍵之末
    s8 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40), "B": (H, 0, "X", 8, 40), "C": (H, 0, "X", 8, 40)}
    _run(out, "C8 距離近者先；無抵費地之街廓（距離 —）排於同鍵者之後",
         lambda: [(it["街廓"], it["距離"]) for it in _one(ns, s8, {"A": X(30), "B": X(20)})[0]["名單"][1:]],
         [("B", D("20.00")), ("A", D("30.00")), ("C", None)])
    # C9 街廓名
    s9 = {"S": (H, 0, "X", 8, 40), "B": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40)}
    _run(out, "C9 八鍵前七皆同 ⇒ 街廓名之字典序",
         lambda: _seq(_one(ns, s9, {"A": (10.0, 0.0), "B": (-10.0, 0.0)})), ["S", "A", "B"])
    # C10 公設軌
    s10 = {"A": (H, 0, "X", 8, 40), "B": (CM, 500, "Y", 20, 10), "C": (H, 0, "X", 8, 40), "Dd": (H, 0, "X", 8, 40)}
    _run(out, "C10 公設軌：全部可建築街廓依距離（其他鍵⛔ 用）",
         lambda: (lambda r: (r[0]["原街廓"], _seq(r)))(
             _lists(ns, s10, {"A": X(30), "B": X(10), "C": X(20)}, [_unit(ns, "g2", False, None, [("u", 5.0)])])),
         (None, ["B", "C", "A", "Dd"]))
    # C11 錨點
    s11 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40)}
    _run(out, "C11 錨點 ＝ 原有面積最大之一筆（並列取暫編地號小者）；距離自其質心起算",
         lambda: (lambda r: (r[0]["錨點"], r[0]["名單"][1]["距離"]))(
             _lists(ns, s11, {"A": X(10), "S": X(3)},
                    [_unit(ns, "g3", True, "S", [("p2", 50.0), ("p3", 80.0), ("p1", 80.0)])],
                    coords={"p1": _sq(0.0, 0.0), "p2": _sq(500.0, 0.0), "p3": _sq(1000.0, 0.0)})),
         ("p1", D("10.00")))
    # C12 原街廓居首
    s12 = {"S": (CM, 900, "Z", 30, 5), "A": (H, 0, "X", 8, 40), "B": (H, 0, "X", 8, 40)}
    _run(out, "C12 建地軌：原街廓居首（⛔ 排序·僅一次）",
         lambda: (lambda r: [(it["街廓"], it["原街廓"], it["鍵"] is None) for it in r[0]["名單"]])(
             _one(ns, s12, {"A": X(1), "B": X(2), "S": X(99)})),
         [("S", True, True), ("A", False, False), ("B", False, False)])
    # C13 停機
    def _stop(fn):
        try:
            fn()
            return "未停"
        except RuntimeError as ex:
            return ("停", "B" in str(ex) and "C" in str(ex)) if "正面道路" in str(ex) else ("停",)
    L3 = ["A", "B", "C"]
    _run(out, "C13a 正面道路無名者一次列出全部 ⇒ 停機",
         lambda: _stop(lambda: ns["adj_block_ctx"](L3, {k: H for k in L3}, {}, {"A": "X", "B": None, "C": ""},
                                                   {k: 8 for k in L3}, {k: 40 for k in L3})), ("停", True))
    _run(out, "C13b 正面路寬為 0 ⇒ 停機",
         lambda: _stop(lambda: ns["adj_block_ctx"](["A"], {"A": H}, {}, {"A": "X"}, {"A": 0}, {"A": 40})), ("停",))
    _run(out, "C13c 深度缺 ⇒ 停機",
         lambda: _stop(lambda: ns["adj_block_ctx"](["A"], {"A": H}, {}, {"A": "X"}, {"A": 8}, {})), ("停",))
    _run(out, "C13d 原街廓非可建築街廓 ⇒ 停機",
         lambda: _stop(lambda: _one(ns, {"A": (H, 0, "X", 8, 40)}, {}, home="Q")), ("停",))
    _run(out, "C13e 錨點無幾何 ⇒ 停機",
         lambda: _stop(lambda: _one(ns, {"S": (H, 0, "X", 8, 40)}, {}, coords={})), ("停",))
    # C14 抵費地之迄點
    rows = [{"推進側別": "抵費地", "所屬街廓": "A", "暫編地號": "A-抵費地-1", "cut_coords": _sq(0, 0, 5)},
            {"推進側別": "抵費地", "所屬街廓": "A", "暫編地號": "A-抵費地-2", "cut_coords": _sq(100, 0, 2)},
            {"推進側別": "left", "所屬街廓": "A", "暫編地號": "a1", "cut_coords": _sq(500, 0, 50)},
            {"推進側別": "抵費地", "所屬街廓": "B", "暫編地號": "B-抵費地-2", "cut_coords": _sq(0, 0, 3)},
            {"推進側別": "抵費地", "所屬街廓": "B", "暫編地號": "B-抵費地-1", "cut_coords": _sq(10, 0, 3)},
            {"推進側別": "抵費地", "所屬街廓": "C", "暫編地號": "C-抵費地", "cut_coords": [[0, 0], [1, 1]]}]
    _run(out, "C14 迄點 ＝ 各街廓之抵費地列中面積最大者之質心（並列取暫編地號小者；非抵費地、無幾何者⛔ 計）",
         lambda: {k: (round(v[0], 6), round(v[1], 6)) for k, v in ns["adj_pool_anchor"](rows).items()},
         {"A": (0.0, 0.0), "B": (10.0, 0.0)})
    # C15 類別表
    _run(out, "C15 類別表之鍵 ＝ F3_BLOCK_CATEGORIES；得為正面道路者唯「道路」",
         lambda: (sorted(ns["F3_CATEGORY_FRONT_ROAD"]) == sorted(ns["F3_BLOCK_CATEGORIES"]),
                  sorted(k for k, v in ns["F3_CATEGORY_FRONT_ROAD"].items() if v is True),
                  all(isinstance(v, bool) for v in ns["F3_CATEGORY_FRONT_ROAD"].values())),
         (True, ["道路"], True))
    # C16 顯示列
    def _rows():
        rv = ns["adj_candidate_rows"](_one(ns, s2, p2))
        allstr = all(isinstance(v, str) for r in rv["units"] + rv["detail"] for v in r.values())
        return (allstr, rv["units"][0]["候選街廓（依序）"], len(rv["detail"]), "0.10 m" in rv["lines"][0])
    _run(out, "C16 顯示列：各欄皆字串；序列標原街廓與第二趟排除；逐候選一列；總句載容差",
         _rows, (True, "S（原街廓） → d → a → b → c（第二趟排除）", 5, True))
    # C17 四捨五入
    _run(out, "C17 adj_q2 ＝ 四捨五入至 0.01（ROUND_HALF_UP）",
         lambda: (str(ns["adj_q2"](0.125)), str(ns["adj_q2"](2.675)), str(ns["adj_q2"](1.005)), str(ns["adj_q2"](-0.125))),
         ("0.13", "2.68", "1.01", "-0.13"))
    # C18 深度差以二位小數計
    s18 = {"S": (H, 0, "X", 8, 44.47), "A": (H, 0, "X", 8, 44.34), "B": (H, 0, "X", 8, 44.57)}
    _run(out, "C18 深度差以二位小數計：−0.13 ⇒ 較淺；＋0.10 ⇒ 同深",
         lambda: [(it["街廓"], it["深度差"], it["深度"]) for it in _one(ns, s18, {"A": X(9), "B": X(1)})[0]["名單"][1:]],
         [("B", D("0.10"), "同深"), ("A", D("-0.13"), "較淺")])
    # ── 補令一（`W-G.9-359`）──
    from shapely.geometry import Polygon as _Pg
    s19 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40), "B": (H, 0, "X", 8, 40)}
    r19 = [{"推進側別": "抵費地", "所屬街廓": "A", "暫編地號": "A-p1", "cut_coords": [[0, 0], [1, 0], [2, 0]]},
           {"推進側別": "抵費地", "所屬街廓": "B", "暫編地號": "B-p1", "cut_coords": [[0, 5], [1, 5], [2, 5]]},
           {"推進側別": "抵費地", "所屬街廓": "B", "暫編地號": "B-p2", "cut_coords": _sq(10, 0, 2)}]

    def _c19():
        pa = ns["adj_pool_anchor"](r19)
        return ({k: (round(v[0], 6), round(v[1], 6)) for k, v in pa.items()},
                [(it["街廓"], it["距離"]) for it in _one(ns, s19, pa)[0]["名單"][1:]])
    _run(out, "C19 退化（buffer(0) 後為空）之池列⛔ 計；某街廓之池列皆退化 ⇒ 視同無抵費地（距離 —·排於同鍵者之後）",
         _c19, ({"B": (10.0, 0.0)}, [("B", D("10.00")), ("A", None)]))
    _run(out, "C20 錨點之多邊形退化（buffer(0) 後為空）⇒ 停機",
         lambda: _stop(lambda: _one(ns, {"S": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40)}, {"A": X(10)},
                                    coords={"u": [[0, 0], [1, 0], [2, 0]]})), ("停",))
    bow = [[0, 0], [6, 3], [6, 0], [0, 3]]

    def _c21():
        pb = _Pg(bow).buffer(0)
        pr = _Pg(bow)
        e_b = ns["adj_q2"](math.hypot(10.0 - pb.centroid.x, 0.0 - pb.centroid.y))
        e_r = ns["adj_q2"](math.hypot(10.0 - pr.centroid.x, 0.0 - pr.centroid.y))
        got = _one(ns, {"S": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40)}, {"A": X(10)},
                   coords={"u": bow})[0]["名單"][1]["距離"]
        return (_Pg(bow).is_valid, got == e_b, e_b != e_r)
    _run(out, "C21 錨點之多邊形無效（自交）⇒ 以 buffer(0) 之質心起算（同抵費地之迄點）", _c21, (False, True, True))
    _run(out, "C22 最小建築面積非數、非有限或負 ⇒ 停機",
         lambda: tuple(_stop(lambda v=v: ns["adj_block_ctx"](["A"], {"A": H}, {"A": v}, {"A": "X"}, {"A": 8}, {"A": 40}))
                       for v in ("x", float("nan"), -1.0)), (("停",), ("停",), ("停",)))
    return out


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in FUNCS + CONSTS if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（harvest 之 app.py·⛔ 本案資料）──")
    cases = _cases(ns)
    red = _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    n_ok = 0
    for i, (name, got, exp) in enumerate(cases):
        pert = [(n, g, ("擾動", e) if j == i else e) for j, (n, g, e) in enumerate(cases)]
        rr = _report(pert, verbose=False)
        n_ok += int(rr == sorted(set(red) | {name.split()[0]}, key=[c[0].split()[0] for c in cases].index))
    ok0 = n_ok == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {n_ok}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.calls = []

    def __getattr__(self, name):
        def rec(*a, **k):
            self.calls.append((name, a, k))
            return _NullCM()
        return rec


class _NullCM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _find_main_block(mn):
    for n in ast.walk(mn):
        for fld in ("body", "orelse", "finalbody"):
            body = getattr(n, fld, None)
            if not isinstance(body, list):
                continue
            for i, s in enumerate(body):
                if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name) \
                        and s.targets[0].id == "_adj359_bf" and i + 1 < len(body) and isinstance(body[i + 1], ast.If):
                    return body[i:i + 2]
    return None


def _screen_ns(app_src):
    return _extract_ns(app_src, funcs=FUNCS + ["adj_intake", "r3_front_road_identifier", "r3_normalize_road_name"],
                       consts=CONSTS + ["SS_FRONT_ROAD_NAME", "SS_FRONT_ROAD_DERIVE", "K91_SS_MBA_EFFECTIVE"],
                       prefixes=("ADJ_", "SS_ADJ_", "R3_STATUS_"))


def _exec_block(app_src, blk, ss, g_extra):
    import pandas as pd
    rns = _screen_ns(app_src)
    fst = _FakeSt(ss)
    g = dict(rns, st=fst, _pd=pd, k6b_stage3_selected=lambda ss_, b_, s_: None)
    g.update(g_extra)
    exec(compile(ast.Module(body=blk, type_ignores=[]), "<main_cand_block>", "exec"), g)
    return fst


def _toy_screen(rns_keys, variant):
    """合成畫面（⛔ 本案資料）：可建築街廓 B1（區外·名稱以 id 'b1' 存）／B2、B3（皆臨道路 C1）；歸戶 GA 之 y 不配地
    ⇒ 建地軌、原街廓 B1。距離：B3 近於 B2。深度：`f3_alloc_depth_by_label` ＝ B1 40／B2 30／B3 45（⇒ B2 較淺、B3 較深），
    另置誘餌 `f3_block_depth_by_label` ＝ B1 10／B2 50／B3 35（取之則 B3 先於 B2）。
    variant：'a' 基本｜'b' `f3_sb_rows` 之 B2 路寬 6｜'c' `K91_SS_MBA_EFFECTIVE` ＝ B1 100／B2 200／B3 100｜
             'd' 名稱改以 label 存（⛔ 以 id）。"""
    def _t(pid, lot, blk, a, c):
        return {"暫編地號": pid, "原地號": lot, "所屬街廓": blk, "分攤登記面積_m2": a, "面積_m2": 0.0,
                "重劃前地價區段": "z", "polygon_coords": _sq(*c)}
    temp = [_t("x", "L1", "B1", 100.0, (0, 0)), _t("y", "L2", "B1", 50.0, (5, 0)),
            _t("q", "L4", "B2", 60.0, (100, 0)), _t("r", "L5", "B3", 60.0, (-100, 0))]
    build = [dict(t) for t in temp]
    gv = [{"暫編地號": "x", "推進側別": "left", "所屬街廓": "B1"}, {"暫編地號": "q", "推進側別": "left", "所屬街廓": "B2"},
          {"暫編地號": "r", "推進側別": "left", "所屬街廓": "B3"},
          {"暫編地號": "B1-抵費地", "推進側別": "抵費地", "所屬街廓": "B1", "cut_coords": _sq(10, 0, 2)},
          {"暫編地號": "B2-抵費地", "推進側別": "抵費地", "所屬街廓": "B2", "cut_coords": _sq(80, 0, 2)},
          {"暫編地號": "B3-抵費地", "推進側別": "抵費地", "所屬街廓": "B3", "cut_coords": _sq(-20, 0, 2)}]
    der = {"B1": {"status": rns_keys["R3_STATUS_OUTSIDE"], "derived": [], "candidates": []},
           "B2": {"status": rns_keys["R3_STATUS_DERIVED"], "derived": ["C1"], "candidates": [{"block": "C1", "ratio": 0.9}]},
           "B3": {"status": rns_keys["R3_STATUS_DERIVED"], "derived": ["C1"], "candidates": [{"block": "C1", "ratio": 0.9}]}}
    ss = {rns_keys["SS_ADJ_BUILD_FINAL"]: build,
          rns_keys["SS_ADJ_DROPPED"]: {("B1", "left"): [{"暫編地號": "y", "G(㎡)": 20.0}]},
          "f3_G_values": gv, "f3L_setback_default": 3.5,
          "t8_ownership_map": {"L1": "GA", "L2": "GA", "L4": "GB", "L5": "GC"},
          rns_keys["SS_FRONT_ROAD_DERIVE"]: der,
          rns_keys["SS_FRONT_ROAD_NAME"]: ({"B1": "外路"} if variant == "d" else {"b1": "外路"}),
          "f3_sb_rows": [{"街廓": "B1", "正面路寬(m)": 8.0}, {"街廓": "B2", "正面路寬(m)": 6.0 if variant == "b" else 8.0},
                         {"街廓": "B3", "正面路寬(m)": 8.0}],
          "f3_alloc_depth_by_label": {"B1": 40.0, "B2": 30.0, "B3": 45.0},
          "f3_block_depth_by_label": {"B1": 10.0, "B2": 50.0, "B3": 35.0},
          rns_keys["K91_SS_MBA_EFFECTIVE"]: ({"B1": 100.0, "B2": 200.0, "B3": 100.0} if variant == "c" else {})}
    extra = {"build_parcels": build, "temp_parcels": temp,
             "classified_blocks": [{"label": "B1", "id": "b1", "category": H}, {"label": "B2", "id": "b2", "category": H},
                                   {"label": "B3", "id": "b3", "category": H},
                                   {"label": "C1", "id": "c1", "category": "道路"}],
             "F3_CATEGORY_BURDEN": {H: "可建築土地", "道路": "共同負擔"}}
    return ss, extra


SCREEN_EXP = {
    "a": "B1（原街廓） → B2 → B3",
    "b": "B1（原街廓） → B3 → B2",
    "c": "B1（原街廓） → B3 → B2（第二趟排除）",
}


def _synth_screen(app_src, mn):
    """`main()` 之候選街廓區塊（自 `_adj359_bf` 之賦值起連續 `2` 句）以假 st ＋ 合成資料實際執行（四變體）。"""
    if mn is None:
        return False, "無 main()"
    blk = _find_main_block(mn)
    if blk is None:
        return False, "抽不到候選街廓區塊"
    bad = []
    for v in ("a", "b", "c", "d"):
        try:
            rns = _screen_ns(app_src)
            ss, extra = _toy_screen(rns, v)
            fst = _exec_block(app_src, blk, ss, extra)
        except Exception as e:  # noqa: BLE001
            bad.append(f"{v}：執行拋 {type(e).__name__}: {e}")
            continue
        dfs = [c[1][0] for c in fst.calls if c[0] == "dataframe"]
        errs = [str(c[1][0]) for c in fst.calls if c[0] == "error"]
        caps = [c[1][0] for c in fst.calls if c[0] == "caption"]
        if v == "d":
            if dfs or len(errs) != 1 or "B1" not in errs[0]:
                bad.append(f"d：期 st.error 一則且列 B1、⛔ 出表（得 error {errs}、表 {len(dfs)}）")
            continue
        ok = not errs and len(dfs) == 2 and len(caps) == 1 and caps[0].startswith("合併單位 1") \
            and list(dfs[0]["歸戶"]) == ["GA"] and list(dfs[0]["候選街廓（依序）"]) == [SCREEN_EXP[v]] \
            and len(dfs[1]) == 3
        if v == "a":
            ok = ok and list(dfs[1]["深度差(m)"]) == ["—", "-10.00", "5.00"] and list(dfs[1]["深度"]) == ["—", "較淺", "較深"]
        if not ok:
            bad.append(f"{v}：得 error {errs[:1]}、表 {len(dfs)}、序 {list(dfs[0]['候選街廓（依序）']) if dfs else None}")
    return (not bad), f"不符 {bad}"


def _wiring_checks(app_src, rv_src):
    res = []
    tree = ast.parse(app_src)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    c = consts.get("ADJ_DEPTH_TIE_TOL_M")
    ok1 = c is not None and isinstance(c.value, ast.Constant) and c.value.value == 0.1
    dflt = all(f in top and any(isinstance(d, ast.Name) and d.id == "ADJ_DEPTH_TIE_TOL_M" for d in top[f].args.defaults)
               for f in ("adj_candidate_lists", "adj_candidate_rows"))
    lit = [n.lineno for f in FUNCS if f in top for n in ast.walk(top[f])
           if isinstance(n, ast.Constant) and n.value in (0.1, 0.5) and not isinstance(n.value, bool)]
    res.append(("W1 具名常數 ADJ_DEPTH_TIE_TOL_M ＝ 0.1、二函式之預設引用之、新函式內⛔ 字面 0.1／0.5",
                ok1 and dflt and not lit, f"字面之列 {lit}"))
    fr = consts.get("F3_CATEGORY_FRONT_ROAD")
    bc = consts.get("F3_BLOCK_CATEGORIES")
    ok2 = False
    note2 = ""
    if fr is not None and bc is not None:
        try:
            frv, bcv = ast.literal_eval(fr.value), ast.literal_eval(bc.value)
            ok2 = sorted(frv) == sorted(bcv) and [k for k, v in frv.items() if v is True] == ["道路"] \
                and all(isinstance(v, bool) for v in frv.values())
        except Exception as ex:  # noqa: BLE001
            note2 = f"literal_eval 失敗 {type(ex).__name__}"
    res.append(("W2 類別表 F3_CATEGORY_FRONT_ROAD 之鍵 ＝ F3_BLOCK_CATEGORIES、唯「道路」為真", ok2, note2))
    pc = top.get("parse_cad_precision_layers")
    ok3 = False
    if pc is not None:
        for n in ast.walk(pc):
            if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) \
                    and isinstance(n.targets[0].slice, ast.Constant) \
                    and n.targets[0].slice.value == "front_road_derive" \
                    and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", None) == "r3_front_road_derive":
                a = n.value.args
                if len(a) >= 2 and isinstance(a[1], ast.DictComp):
                    ifs = [cond for g in a[1].generators for cond in g.ifs]
                    notin = any(isinstance(x, ast.Compare) and isinstance(x.ops[0], ast.NotIn)
                                and getattr(x.comparators[0], "id", None) == "_buildable_blocks" for x in ifs)
                    cat = any(isinstance(x, ast.Call) and isinstance(x.func, ast.Attribute) and x.func.attr == "get"
                              and getattr(x.func.value, "id", None) == "F3_CATEGORY_FRONT_ROAD" for x in ifs)
                    ok3 = notin and cat
    res.append(("W3 正面道路推導之候選 ＝ 非可建築（_buildable_blocks 之補集）∩ 類別表為真者", ok3, ""))
    lits, toks, bad_fn = [], [], [f for f in FUNCS if f not in top]
    for f in FUNCS:
        if f not in top:
            continue
        seg = ast.get_source_segment(app_src, top[f]) or ""
        lits += sorted({n.value for n in ast.walk(top[f]) if isinstance(n, ast.Constant)
                        and isinstance(n.value, str) and CASE_LIT_RE.match(n.value)})
        toks += [(f, t) for t in FORBID_TOKS if t in seg]
    res.append(("W4 新函式俱在、⛔ 案件字面、⛔ 讀 session、⛔ 含既有閘所禁之消費字樣", not (lits or toks or bad_fn),
                f"缺 {bad_fn}；案件字面 {lits}；字樣 {toks}"))
    ok5, note5 = _synth_screen(app_src, top.get("main"))
    res.append(("W5 main() 之候選街廓區塊以假 st 實際執行（四變體：深度取 f3_alloc_depth_by_label、路寬取 f3_sb_rows、"
                "最小建築面積取 K91_SS_MBA_EFFECTIVE、名稱以 id 取）",
                ok5, note5))
    rtree = ast.parse(rv_src)
    rtop = {n.name for n in rtree.body if isinstance(n, ast.FunctionDef)}
    rconst = {n.targets[0].id: ast.get_source_segment(rv_src, n) for n in rtree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    ok6 = "load_front_road_names" in rtop and "case_front_road_names_UC9898.json" in (rconst.get("FRONT_ROAD_NAMES") or "")
    res.append(("W6 verify/run_verification.py 之 FRONT_ROAD_NAMES ＝ …/case_front_road_names_UC9898.json、"
                "load_front_road_names 在", ok6, ""))
    return res


def wiring(repo):
    app_src = _read(repo, "app.py")
    rv_src = _read(repo, "verify/run_verification.py")
    red = []
    print("── 接線（AST·app.py ＋ verify/run_verification.py）──")
    for name, ok, note in _wiring_checks(app_src, rv_src):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run ──
def _q2(x):
    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _independent(units, labels, cat, mba, ident, width, depth, g_rows, coords, pool_side, track_build, tol):
    """外部錨：本器另寫之排序（⛔ 呼叫名單之函式）。回 {歸戶: (錨點, [(街廓, 距離, 第二趟排除)])}。"""
    from shapely.geometry import Polygon
    best = {}
    for r in g_rows:
        cs = r.get("cut_coords") or []
        if r.get("推進側別") != pool_side or len(cs) < 3:
            continue
        p = Polygon(cs)
        p = p if p.is_valid else p.buffer(0)
        if p.is_empty:
            continue    # 補令一 裁一：退化之池列⛔ 計
        k = (-p.area, str(r["暫編地號"]))
        b = str(r["所屬街廓"])
        if b not in best or k < best[b][0]:
            best[b] = (k, (p.centroid.x, p.centroid.y))
    pa = {b: v[1] for b, v in best.items()}
    m = {l: _q2(mba.get(l, 0) or 0) for l in labels}
    w = {l: _q2(width[l]) for l in labels}
    dp = {l: _q2(depth[l]) for l in labels}
    lad2 = sorted(set(m.values()))
    lad5 = sorted(set(w.values()), reverse=True)
    T = Decimal(repr(float(tol)))
    out = {}
    for u in units:
        sl = list(u["建築街廓內不能分配"]) + list(u["共同負擔用地"])
        a = min(sl, key=lambda r: (-float(r["原有面積"]), str(r["暫編地號"])))
        p = Polygon(coords[str(a["暫編地號"])])
        p = p if p.is_valid else p.buffer(0)
        if p.is_empty:
            raise RuntimeError(f"外部錨：錨點 {a['暫編地號']!r} 之多邊形為空（補令一 裁二 ⇒ 停機）")
        ax, ay = p.centroid.x, p.centroid.y
        dist = {l: (_q2(math.hypot(pa[l][0] - ax, pa[l][1] - ay)) if l in pa else None) for l in labels}
        dk = {l: ((0, dist[l]) if dist[l] is not None else (1, Decimal(0))) for l in labels}
        if u["軌"] == track_build:
            s = u["原街廓"]
            keys = {}
            for t in labels:
                if t == s:
                    continue
                d2 = lad2.index(m[t]) - lad2.index(m[s])
                d5 = lad5.index(w[t]) - lad5.index(w[s])
                dd = dp[t] - dp[s]
                r6 = (0, Decimal(0)) if abs(dd) <= T else ((0, -dd) if dd < 0 else (1, dd))
                keys[t] = (int(cat[t] != cat[s]), (0, -d2) if d2 <= 0 else (1, d2), int(ident[t] != ident[s]),
                           int(w[t] != w[s]), (0, d5) if d5 >= 0 else (1, -d5), r6, dk[t], t)
            seq = [s] + sorted(keys, key=keys.get)
            out[u["歸戶"]] = (str(a["暫編地號"]), [(t, dist[t], t != s and keys[t][1][0] == 1) for t in seq])
        else:
            seq = sorted(labels, key=lambda t: (dk[t], t))
            out[u["歸戶"]] = (str(a["暫編地號"]), [(t, dist[t], False) for t in seq])
    return out


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        miss = [n for n in FUNCS + CONSTS if n not in ns]
        if miss:
            print(f"  🔴 受詞缺：{miss}")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g
        if not hasattr(rv, "load_front_road_names"):
            print("  🔴 受詞缺：run_verification.load_front_road_names")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        app_src = _read(repo, "app.py")
        mn = next((n for n in ast.parse(app_src).body if isinstance(n, ast.FunctionDef) and n.name == "main"), None)
        blk = _find_main_block(mn) if mn is not None else None
        OK = ns["R3_STATUS_DERIVED"]
        for sb in sbs:
            with contextlib.redirect_stdout(io.StringIO()):
                snapshot = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
                    ns["K917_DROPPED"].clear()
                    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                                    eff_min_build_by_blk={})
            except RuntimeError as e:
                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
                return 3
            k9 = sg.get("k929_6")
            if k9 is None:
                print(f"🔴 退縮 {sb}：run_step_g 無 k929_6 ⇒ 無從判定")
                return 3
            print(f"══ 退縮 {sb} ══")
            drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
            cbl = list(cb_by.values())
            bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cbl}
            bb = sorted((b for b in cbl if bur[b["label"]] == ns["ADJ_BURDEN_BUILD"]), key=lambda b: b["label"])
            labels = [b["label"] for b in bb]
            der = cad.get("front_road_derive") or {}
            # R0 區外道路名稱檔
            names = rv.load_front_road_names()
            need = sorted(l for l in labels if (der.get(l) or {}).get("status") != OK)
            ok0 = sorted(names) == need and len(set(names.values())) == 1
            print(("  ✅" if ok0 else "  🔴") + f" R0 區外道路名稱檔：列 {sorted(names)} ＝ 推導無值者 {need}；"
                  f"同一條（相異名稱 {len(set(names.values()))}）")
            if not ok0:
                red.append(f"R0@{sb}")
            # R1 正面道路推導
            cands = [(l, c["block"], c["category"]) for l in labels for c in (der.get(l) or {}).get("candidates", [])]
            badc = [x for x in cands if ns["F3_CATEGORY_FRONT_ROAD"].get(x[2]) is not True]
            st_now = {l: ((der.get(l) or {}).get("status"), tuple((der.get(l) or {}).get("derived") or [])) for l in labels}
            OUT = ns["R3_STATUS_OUTSIDE"]
            st_350 = {"R1": (OUT, ()), "R2": (OK, ("RD1",)), "R3": (OK, ("RD2",)), "R4": (OUT, ()),
                      "R5": (OK, ("RD2",)), "R6": (OK, ("RD3",))}
            ok1 = not badc and st_now == st_350
            print(("  ✅" if ok1 else "  🔴") + f" R1 正面道路之候選皆「道路」類（{len(cands)} 對·非道路 {badc}）；"
                  f"推導 ＝ W-G.9-350 §一 項 5 之表：{st_now == st_350}")
            if not ok1:
                red.append(f"R1@{sb}")
            # R2 名單 vs 外部錨
            ident = ns["r3_front_road_identifier"](labels, der, names)
            idm = {l: ident[l]["id"] for l in labels}
            prow = {r["街廓"]: r for r in params}
            width = {l: prow[l]["正面路寬(m)"] for l in labels}
            depth = dict(fake_st.session_state.get("f3_alloc_depth_by_label") or {})
            cat = {b["label"]: b.get("category", "") for b in bb}
            coords = {str(t["暫編地號"]): (t.get("polygon_coords") or []) for t in tp3}
            try:
                it = ns["adj_intake"](tp3, k9["build"], sg["g_rows"], drops, own, bur)
                ctx = ns["adj_block_ctx"](labels, cat, {}, idm, width, depth)
                lst = ns["adj_candidate_lists"](it, ctx, ns["adj_pool_anchor"](sg["g_rows"]), coords)
            except RuntimeError as e:
                print(f"  🔴 R2 名單停機：{str(e)[:300]}")
                red.append(f"R2@{sb}")
                continue
            ind = _independent(it["units"], labels, cat, {}, idm, width, depth, sg["g_rows"], coords,
                               ns["ADJ_POOL_SIDE"], ns["ADJ_TRACK_BUILD"], ns["ADJ_DEPTH_TIE_TOL_M"])
            got = {u["歸戶"]: (u["錨點"], [(i["街廓"], i["距離"], i["第二趟排除"]) for i in u["名單"]]) for u in lst}
            dif = sorted(g for g in set(ind) | set(got) if ind.get(g) != got.get(g))
            for u in lst:
                print(f"     {u['歸戶']}｜{u['軌']}｜原街廓 {u['原街廓']}｜錨點 {u['錨點']}｜"
                      + " → ".join(f"{i['街廓']}({'—' if i['距離'] is None else i['距離']})" for i in u["名單"]))
            print(("  ✅" if not dif else "  🔴") + f" R2 名單（{len(got)} 單位）與外部錨逐單位逐序相同：相異 {dif}")
            if dif:
                red.append(f"R2@{sb}")
            # R3 畫面區塊於本案資料
            if blk is None:
                print("  🔴 R3 抽不到畫面之候選街廓區塊")
                red.append(f"R3@{sb}")
            else:
                rns = _screen_ns(app_src)
                ss = {rns["SS_ADJ_BUILD_FINAL"]: k9["build"], rns["SS_ADJ_DROPPED"]: drops, "f3_G_values": sg["g_rows"],
                      "f3L_setback_default": sb, "t8_ownership_map": own, rns["SS_FRONT_ROAD_DERIVE"]: der,
                      rns["SS_FRONT_ROAD_NAME"]: {b["id"]: names[b["label"]] for b in bb if b["label"] in names},
                      "f3_sb_rows": params, "f3_alloc_depth_by_label": depth, rns["K91_SS_MBA_EFFECTIVE"]: {}}
                try:
                    fst = _exec_block(app_src, blk, ss, {"build_parcels": bp3, "temp_parcels": tp3, "classified_blocks": cbl,
                                                         "F3_CATEGORY_BURDEN": ns["F3_CATEGORY_BURDEN"]})
                    dfs = [c[1][0] for c in fst.calls if c[0] == "dataframe"]
                    errs = [str(c[1][0])[:200] for c in fst.calls if c[0] == "error"]
                    view = ns["adj_candidate_rows"](lst)
                    ok3 = not errs and len(dfs) == 2 and dfs[0].to_dict("records") == view["units"] \
                        and dfs[1].to_dict("records") == view["detail"]
                    note = f"error {errs}；表 {len(dfs)}"
                except Exception as e:  # noqa: BLE001
                    ok3, note = False, f"執行拋 {type(e).__name__}: {e}"
                print(("  ✅" if ok3 else "  🔴") + f" R3 畫面區塊於本案資料之二表 ＝ harness 之顯示列（{note}）")
                if not ok3:
                    red.append(f"R3@{sb}")
            # R4 K-9-52 ③ 之可見效果
            six = [u for u in lst if u["軌"] == ns["ADJ_TRACK_BUILD"] and u["原街廓"] == "R6"]
            l05 = ns["adj_candidate_lists"]({"units": [u0 for u0 in it["units"] if u0.get("原街廓") == "R6"]}, ctx,
                                            ns["adj_pool_anchor"](sg["g_rows"]), coords, tol=0.5)
            s01 = sorted({tuple(i["街廓"] for i in u["名單"]) for u in six})
            s05 = sorted({tuple(i["街廓"] for i in u["名單"]) for u in l05})
            ok4 = bool(six) and s01 == [("R6", "R2", "R3", "R5", "R1", "R4")] and s05 == [("R6", "R5", "R2", "R3", "R1", "R4")]
            print(("  ✅" if ok4 else "  🔴") + f" R4 原街廓 R6 之建地軌 {len(six)} 單位：0.1 ⇒ {s01}；0.5 ⇒ {s05}")
            if not ok4:
                red.append(f"R4@{sb}")
            # R5 公設軌
            pub = [u for u in lst if u["軌"] != ns["ADJ_TRACK_BUILD"]]
            ok5 = all(sorted(i["街廓"] for i in u["名單"]) == labels
                      and all(u["名單"][k]["距離"] <= u["名單"][k + 1]["距離"] for k in range(len(u["名單"]) - 1))
                      for u in pub)
            print(("  ✅" if ok5 else "  🔴") + f" R5 公設軌 {len(pub)} 單位：名單 ＝ 全部可建築街廓、距離不減")
            if not ok5:
                red.append(f"R5@{sb}")
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
        return wiring(repo)
    sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
    return run(repo, sbs)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
