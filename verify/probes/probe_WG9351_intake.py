# -*- coding: utf-8 -*-
"""W-G.9-351 量測器（發單側窗四十七擬·檔 F10·⛔ 由受單側改一字）：調配階段之輸入（步 1 之尾〜步 2）。

子命令（一律 python verify/probes/probe_WG9351_intake.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·以 AST 自 `app.py` 抽出 `ADJ_*` 常數與 `adj_intake`／`adj_intake_rows`）：
           逐切片之類、合併單位之軌與原街廓（應分配面積較大者·⛔ 原有面積）、入池閘之合併單元、段三所併出者、
           殘料、待同歸戶併入與八種停機；另施四突變（原街廓改以原有面積比、兼有配地者⛔ 成單位、段三所併出者當共同負擔、
           並列⛔ 停機），每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST 查接線：W1 模組層之常數與二函式、二函式內⛔ 案件字面；W2 入池閘之畫面入口於復原之後寫末趟之不配地紀錄、
           配地本體同生命週期去／寫末態 build；W3 二鍵 ∈ `K6B_SCREEN_TRIAL_KEYS` 且其末項仍為 `f3_k929_6_log`；
           W4 消費端 ＝ 生產碼 `34` 檔中除 `app.py` 外命中 `0`、`app.py` 中只在許可之函式內（🔧 `W-G.9-363`：許可之函式
           另含 `f3_screen_k953`〔手冊先行之畫面試算讀入池閘之末態 build〕；🔧 `W-G.9-367`：另含 app.py 之 `f3_screen_adj4`／`adj4_plan`
           與 harness 之 `run_adj4`〔規格步 4 乙以 `adj_intake` 定其受詞〕）；W5 畫面路徑之合成案
           （`自誤 517`：抽出 `main()` 之盤點區塊，以假 st 與合成資料實際執行）。另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0` 二者）：以 `adj_intake` 盤點，並以本器**另寫之分類**（⛔ 呼叫
           `adj_intake`）逐切片對拍（外部錨）：R1 盤點⛔ 停機；R2 逐切片之類相同；R3 合併單位（歸戶·軌·原街廓·成員）
           相同；R4 逐類之切片數與原有面積之和 ＝ 全部切片；R5 入池閘之入池宗（不配地之 build 單元之成員）之數與
           原有面積 ＝ 類「建築街廓內不能分配」者。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ADJ_FUNCS = ["adj_intake", "adj_intake_rows"]
ADJ_KEYS = ["f3_k929_6_build", "f3_k929_6_dropped"]
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _extract_ns(src):
    """自 `app.py` 以 AST 抽出 `ADJ_*`／`SS_ADJ_*` 常數與 `adj_*` 函式，於隔離之命名空間執行。"""
    tree = ast.parse(src)
    parts = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")):
            parts.append(ast.get_source_segment(src, node))
    if not parts:
        raise KeyError("受詞缺")
    ns = {}
    exec(compile("\n\n".join(parts), "<adj_extract>", "exec"), ns)
    return ns


def _t(pid, lot, blk, a, **kw):
    d = {"暫編地號": pid, "原地號": lot, "所屬街廓": blk, "分攤登記面積_m2": a, "面積_m2": 0.0,
         "重劃前地價區段": "z"}
    d.update(kw)
    return d


BUR = {"B1": "可建築土地", "B2": "可建築土地", "C1": "共同負擔", "C2": "共同負擔", "N1": "非共同負擔"}


def _cases(ns):
    """回 [(名, 得, 期)]；任一例拋例外 ⇒ 以 ('例外', 型別名) 記之（⛔ 吞）。"""
    I, RW = ns["adj_intake"], ns["adj_intake_rows"]
    AL, PO, CU, C4, GH = (ns["ADJ_DISP_ALLOC"], ns["ADJ_DISP_POOL"], ns["ADJ_DISP_COMMON_UNIT"],
                          ns["ADJ_DISP_COMMON_STEP4"], ns["ADJ_DISP_GHOST"])
    TB, TP = ns["ADJ_TRACK_BUILD"], ns["ADJ_TRACK_PUBLIC"]
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as e:  # noqa: BLE001
            got = ("例外", type(e).__name__)
        out.append((name, got, exp))

    def rows(*pids):
        return [{"暫編地號": p, "推進側別": "left"} for p in pids] + [{"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]

    own = {"L1": "GA", "L2": "GA", "L3": "GB", "L4": "GC", "L5": "GD", "L6": "GD", "L7": "GE"}
    # 基本案：GA 有 x（配地）、y（不配地·B1）、r（道路）；GB 只有公設地；GC 有配地 z 與道路 s
    temp = [_t("x", "L1", "B1", 100.0), _t("y", "L2", "B1", 50.0), _t("r", "L2", "C1", 30.0),
            _t("p", "L3", "C2", 80.0), _t("z", "L4", "B2", 120.0), _t("s", "L4", "C1", 20.0)]
    build = [dict(t) for t in temp if BUR[t["所屬街廓"]] == "可建築土地"]
    drops = {("B1", "left"): [{"暫編地號": "y", "G(㎡)": 20.0, "不配地由": "內接矩形"}]}
    base = lambda: I(temp, build, rows("x", "z"), drops, own, BUR)  # noqa: E731
    cls = lambda d: {r["暫編地號"]: r["類"] for r in d["slices"]}  # noqa: E731
    run("S1 逐切片之類", lambda: cls(base()), {"x": AL, "y": PO, "r": CU, "p": CU, "z": AL, "s": C4})
    run("S2 合併單位（歸戶·軌·原街廓·成員）",
        lambda: [(u["歸戶"], u["軌"], u["原街廓"], sorted(r["暫編地號"] for r in u["建築街廓內不能分配"] + u["共同負擔用地"]))
                 for u in base()["units"]],
        [("GA", TB, "B1", ["r", "y"]), ("GB", TP, None, ["p"])])
    run("S3 待同歸戶併入（兼有配地者之共同負擔用地）",
        lambda: [(u["歸戶"], [r["暫編地號"] for r in u["共同負擔用地"]], u["同歸戶原位次配地之街廓"]) for u in base()["step4"]],
        [("GC", ["s"], ["B2"])])
    run("S4 盤點之和 ＝ 全部",
        lambda: (round(sum(v[1] for v in base()["totals"].values()), 6), round(base()["all_area"], 6)), (400.0, 400.0))
    # 原街廓：二街廓各有不能分配者 ⇒ 取應分配面積（G）較大者，⛔ 原有面積
    temp2 = [_t("u", "L5", "B1", 100.0), _t("v", "L6", "B2", 40.0)]
    b2 = [dict(t) for t in temp2]
    d2 = {("B1", "left"): [{"暫編地號": "u", "G(㎡)": 10.0}], ("B2", "right"): [{"暫編地號": "v", "G(㎡)": 25.0}]}
    run("S5 原街廓 ＝ 應分配面積較大者（⛔ 原有面積）",
        lambda: I(temp2, b2, [], d2, own, BUR)["units"][0]["原街廓"], "B2")
    d2t = {("B1", "left"): [{"暫編地號": "u", "G(㎡)": 25.0}], ("B2", "right"): [{"暫編地號": "v", "G(㎡)": 25.0}]}
    run("S6 應分配面積並列 ⇒ loud", lambda: I(temp2, b2, [], d2t, own, BUR), ("例外", "RuntimeError"))
    # 入池閘之合併單元：入池（不配地）與留置（配地）
    temp3 = [_t("m1", "L5", "B1", 60.0), _t("m2", "L6", "B1", 30.0), _t("k1", "L7", "B2", 70.0)]
    b3 = [dict(temp3[0], 入池閘併入=["m1", "m2"]), dict(temp3[2])]
    d3 = {("B1", "left"): [{"暫編地號": "m1", "G(㎡)": 40.0}]}
    run("S7 入池之合併單元 ⇒ 成員皆不能分配、其 G 只計一次",
        lambda: (cls(I(temp3, b3, rows("k1"), d3, own, BUR)),
                 I(temp3, b3, rows("k1"), d3, own, BUR)["units"][0]["原街廓之據"]),
        ({"m1": PO, "m2": PO, "k1": AL}, {"B1": 40.0}))
    run("S8 留置之合併單元 ⇒ 成員皆配地", lambda: cls(I(temp3, b3, rows("m1", "k1"), {}, own, BUR)),
        {"m1": AL, "m2": AL, "k1": AL})
    # 段三所併出者
    temp4 = [_t("c", "L1", "B1", 200.0), _t("q", "L1", "C1", 15.0, 段三併出=["c"])]
    run("S9 段三所併出者 ⇒ 配地（配地街廓 ＝ 受併宗之街廓）",
        lambda: [(r["暫編地號"], r["類"], r["配地街廓"]) for r in I(temp4, [dict(temp4[0])], rows("c"), {}, own, BUR)["slices"]],
        [("c", AL, ["B1"]), ("q", AL, ["B1"])])
    run("S10 段三之受併宗未配地 ⇒ loud",
        lambda: I(temp4, [dict(temp4[0])], [], {("B1", "left"): [{"暫編地號": "c", "G(㎡)": 1.0}]}, own, BUR),
        ("例外", "RuntimeError"))
    gh = {"暫編地號": "_GH_(B1)", "原地號": "_GH", "所屬街廓": "B1", "分攤登記面積_m2": 0.0, "_is_ghost_sliver": True}
    run("S11 殘料（可重名·a＝0）⇒ 另類、⛔ 入單位",
        lambda: (I(temp + [gh, dict(gh)], build + [dict(gh)], rows("x", "z"), drops, own, BUR)["totals"][GH],
                 len(I(temp + [gh, dict(gh)], build + [dict(gh)], rows("x", "z"), drops, own, BUR)["units"])),
        ([2, 0.0], 2))
    run("S12 殘料之原有面積 > 0 ⇒ loud", lambda: I(temp + [dict(gh, 分攤登記面積_m2=1.0)], build, rows("x", "z"), drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S13 build 之宗既非配地亦非不配地 ⇒ loud", lambda: I(temp, build, rows("x"), drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S14 G 值列之未知推進側別 ⇒ loud",
        lambda: I(temp, build, rows("x", "z") + [{"暫編地號": "w", "推進側別": "中間"}], drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S15 非共同負擔之街廓上之切片 ⇒ loud（【未裁】）",
        lambda: I(temp + [_t("n", "L3", "N1", 5.0)], build, rows("x", "z"), drops, own, BUR), ("例外", "RuntimeError"))
    run("S16 無歸戶之切片 ⇒ loud", lambda: I(temp + [_t("w2", "LX", "C1", 5.0)], build, rows("x", "z"), drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S17 不配地紀錄之街廓與切片不同 ⇒ loud",
        lambda: I(temp, build, rows("x", "z"), {("B2", "left"): [{"暫編地號": "y", "G(㎡)": 20.0}]}, own, BUR),
        ("例外", "RuntimeError"))
    run("S18 兼有配地與不能分配者 ⇒ 建地軌（其共同負擔用地入單位）",
        lambda: [(u["歸戶"], u["軌"], u["同歸戶原位次配地之街廓"]) for u in base()["units"]][:1], [("GA", TB, ["B1"])])
    run("R1 顯示列各欄皆字串",
        lambda: all(isinstance(v, str) for k in ("units", "step4", "totals") for r in RW(base())[k] for v in r.values()),
        True)
    run("R2 顯示之總句", lambda: RW(base())["lines"], [f"合併單位 2（{TB} 1·{TP} 1）；待同歸戶併入之歸戶 1"])
    return out


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)
    return red


def selftest(repo):
    src = _read(repo, "app.py")
    try:
        ns = _extract_ns(src)
        ns["adj_intake"]
    except Exception:  # noqa: BLE001
        print(f"  🔴 受詞缺：{ADJ_FUNCS}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（AST 抽出之 adj_*）──")
    red = _report(_cases(ns))
    print("── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──")
    base_red = set(red)
    m0 = _report(_cases(_extract_ns(src)), verbose=False)
    print(("  ✅ " if m0 == red else "  🔴 ") + f"M0 未突變之抽出版：紅 {m0}（期 {red}）")
    if m0 != red:
        red.append("M0")
    muts = [
        ("M1 原街廓改以原有面積比", "float(_r['應分配面積'])", "float(_r['原有面積'])"),
        ("M2 兼有配地者⛔ 成單位", "if _pool or (_cm and not _al):", "if (_pool and not _al) or (_cm and not _al):"),
        ("M3 段三所併出者當共同負擔", "if '段三併出' in t:", "if False:"),
        ("M4 並列⛔ 停機", "if len(_cands) != 1:", "if len(_cands) < 1:"),
    ]
    for mname, a, b in muts:
        if src.count(a) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{src.count(a)}）")
            red.append(mname.split()[0])
            continue
        try:
            turned = [n for n in _report(_cases(_extract_ns(src.replace(a, b, 1))), verbose=False) if n not in base_red]
        except Exception as e:  # noqa: BLE001
            turned = [f"抽出拋 {type(e).__name__}"]
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


PROD_OTHERS_RE = re.compile(r"^verify/[^/]+\.py$")


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
                        and s.targets[0].id == "_adj351_bf" and i + 1 < len(body) and isinstance(body[i + 1], ast.If):
                    return body[i:i + 2]
    return None


def _synth_screen(app_src, mn):
    """`自誤 517`：`main()` 內之敘述⛔ 為 run_all 所執行 ⇒ 抽出盤點區塊（自 `_adj351_bf` 之賦值起連續 `2` 句），
    以假 st ＋ 合成資料實際執行，驗其輸出。"""
    if mn is None:
        return False, "無 main()"
    blk = _find_main_block(mn)
    if blk is None:
        return False, "抽不到盤點區塊"
    try:
        import pandas as pd
        rns = _extract_ns(app_src)
        temp = [_t("x", "L1", "B1", 100.0), _t("y", "L2", "B1", 50.0), _t("r", "L2", "C1", 30.0),
                _t("p", "L3", "C2", 80.0)]
        build = [dict(temp[0]), dict(temp[1])]
        ss = {rns["SS_ADJ_BUILD_FINAL"]: build,
              rns["SS_ADJ_DROPPED"]: {("B1", "left"): [{"暫編地號": "y", "G(㎡)": 20.0}]},
              "f3_G_values": [{"暫編地號": "x", "推進側別": "left"}], "f3L_setback_default": 3.5,
              "t8_ownership_map": {"L1": "GA", "L2": "GA", "L3": "GB"}}
        fst = _FakeSt(ss)
        cats = {"B1": "住宅區", "C1": "道路", "C2": "鄰里公園"}
        g = dict(rns, st=fst, _pd=pd, build_parcels=build, temp_parcels=temp,
                 classified_blocks=[{"label": k, "category": v} for k, v in cats.items()],
                 F3_CATEGORY_BURDEN={"住宅區": "可建築土地", "道路": "共同負擔", "鄰里公園": "共同負擔"},
                 k6b_stage3_selected=lambda ss_, b_, s_: None)
        exec(compile(ast.Module(body=blk, type_ignores=[]), "<main_adj_block>", "exec"), g)
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    dfs = [c[1][0] for c in fst.calls if c[0] == "dataframe"]
    errs = [c for c in fst.calls if c[0] == "error"]
    caps = [c[1][0] for c in fst.calls if c[0] == "caption"]
    checks = {
        "無 st.error": not errs,
        "三表": len(dfs) == 3,
        "單位 2 列（GA 建地軌·GB 公設軌）": len(dfs) == 3 and list(dfs[0]["歸戶"]) == ["GA", "GB"],
        "待同歸戶併入 0 列": len(dfs) == 3 and len(dfs[1]) == 0,
        "盤點合計 260.00": len(dfs) == 3 and dfs[2].iloc[-1]["原有面積(㎡)"] == "260.00",
        "總句 1": len(caps) == 1 and caps[0].startswith("合併單位 2"),
    }
    bad = [k for k, v in checks.items() if not v]
    return (not bad), f"不符 {bad}"


def _wiring_checks(app_src, others):
    """回 [(名, 真偽, 註)]。`others` ＝ {路徑: 原始碼}（生產碼 34 檔中 app.py 以外者）。"""
    res = []
    tree = ast.parse(app_src)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    ok1 = all(f in top for f in ADJ_FUNCS) and all(k in consts for k in ("SS_ADJ_BUILD_FINAL", "SS_ADJ_DROPPED"))
    ok1k = ok1 and ast.literal_eval(consts["SS_ADJ_BUILD_FINAL"].value) == ADJ_KEYS[0] \
        and ast.literal_eval(consts["SS_ADJ_DROPPED"].value) == ADJ_KEYS[1]
    lits = sorted({n.value for f in ADJ_FUNCS if f in top for n in ast.walk(top[f])
                   if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value)})
    res.append(("W1 模組層之 ADJ 常數與二函式、二鍵之值、二函式內⛔ 案件字面", ok1k and not lits, f"案件字面 {lits}"))
    gate = top.get("_k929_6_screen_gate")
    ok2a = False
    if gate is not None:
        tries = [i for i, st_ in enumerate(gate.body) if isinstance(st_, ast.Try)]
        for st_ in gate.body[(tries[-1] + 1) if tries else len(gate.body):]:
            seg = ast.get_source_segment(app_src, st_) or ""
            if isinstance(st_, ast.Assign) and "_ss[SS_ADJ_DROPPED]" in seg and "dict(_last[1])" in seg:
                ok2a = True
    f = top.get("f3_screen_stepg_run")
    ok2b = ok2c = False
    if f is not None:
        seg_f = ast.get_source_segment(app_src, f) or ""
        i_gate = seg_f.find("_k929_6_screen_gate(st, dict(")
        i_pop = seg_f.find("st.session_state.pop(SS_ADJ_BUILD_FINAL, None)")
        ok2b = 0 <= i_gate < i_pop and "st.session_state.pop(SS_ADJ_DROPPED" not in seg_f
        for n in ast.walk(f):
            if isinstance(n, ast.If) and isinstance(n.test, ast.Compare) \
                    and getattr(n.test.left, "id", None) == "_k929_6_log":
                seg = ast.get_source_segment(app_src, n) or ""
                ok2c = "st.session_state[SS_ADJ_BUILD_FINAL] = build_parcels" in seg
    res.append(("W2a 入池閘之畫面入口於復原之後寫 SS_ADJ_DROPPED ＝ 末趟之不配地紀錄（_last[1]）", ok2a, ""))
    res.append(("W2b 配地本體於入池閘之後去 SS_ADJ_BUILD_FINAL（⛔ 去 SS_ADJ_DROPPED）", ok2b, ""))
    res.append(("W2c 配地本體於 _k929_6_log 非 None 時寫 SS_ADJ_BUILD_FINAL ＝ build_parcels", ok2c, ""))
    keys = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "K6B_SCREEN_TRIAL_KEYS"
                                             for t in n.targets):
            keys = ast.literal_eval(n.value)
    res.append(("W3 二鍵 ∈ K6B_SCREEN_TRIAL_KEYS 且末項 ＝ f3_k929_6_log",
                bool(keys) and all(k in keys for k in ADJ_KEYS) and keys[-1] == "f3_k929_6_log", ""))
    toks = ADJ_FUNCS + ["SS_ADJ_BUILD_FINAL", "SS_ADJ_DROPPED"] + ADJ_KEYS
    tok_re = re.compile("|".join(re.escape(t) for t in toks))
    # 🔧 `W-G.9-367`（發單側窗六十八）：harness 之 `run_adj4`（規格步 4 乙之 harness 入口）許可——除其原文而後計他檔之命中
    others = {p: (_drop_fn367(s, "run_adj4") if p == "verify/selection_pipeline.py" else s) for p, s in others.items()}
    other_hits = {p: len(tok_re.findall(s)) for p, s in sorted(others.items()) if tok_re.search(s)}
    allowed = set(ADJ_FUNCS) | {"main", "f3_screen_stepg_run", "_k929_6_screen_gate"}
    allowed |= {"f3_screen_k953"}   # 🔧 `W-G.9-363`（發單側窗六十四）：手冊先行之畫面試算讀入池閘之末態 build（其單元）
    allowed |= {"f3_screen_adj4", "adj4_plan"}   # 🔧 `W-G.9-367`（發單側窗六十八）：規格步 4 乙之畫面試算以 `adj_intake` 定其受詞（其受詞之純函式讀之）
    bad = []
    for fname, node in top.items():
        if fname in allowed:
            continue
        seg = ast.get_source_segment(app_src, node) or ""
        if tok_re.search(seg):
            bad.append(fname)
    res.append((f"W4 消費端：生產碼他檔（{len(others)} 檔）命中 0；app.py 只在許可之函式內",
                not other_hits and not bad, f"他檔 {other_hits}；app.py 非許可函式 {bad}"))
    ok5, note5 = _synth_screen(app_src, top.get("main"))
    res.append(("W5 畫面路徑之合成案：main() 之盤點區塊以假 st 實際執行", ok5, note5))
    return res


def _drop_fn367(src, name):
    """🔧 `W-G.9-367`（發單側窗六十八）：除去模組層函式 `name` 之原文（無之 ⇒ 原文不變）。"""
    t = ast.parse(src)
    ls = src.splitlines(keepends=True)
    for n in t.body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return "".join(ls[:n.lineno - 1] + ls[n.end_lineno:])
    return src


def _prod_others(repo):
    out = {}
    vd = os.path.join(repo, "verify")
    for fn in sorted(os.listdir(vd)):
        p = "verify/" + fn
        if fn.endswith(".py") and PROD_OTHERS_RE.match(p):
            out[p] = _read(repo, p)
    return out


def wiring(repo):
    app_src = _read(repo, "app.py")
    others = _prod_others(repo)
    red = []
    print(f"── 接線（AST·app.py ＋ 生產碼他檔 {len(others)} 檔）──")
    base_red = set()
    for name, ok, note in _wiring_checks(app_src, others):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
            base_red.add(name.split()[0])
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    muts = [
        ("N1 配地本體⛔ 寫 build", app_src.replace(
            "st.session_state[SS_ADJ_BUILD_FINAL] = build_parcels", "pass", 1), others),
        ("N2 入池閘之畫面入口寫空之紀錄", app_src.replace(
            "_ss[SS_ADJ_DROPPED] = _cp_k9296s.deepcopy(dict(_last[1]))",
            "_ss[SS_ADJ_DROPPED] = _cp_k9296s.deepcopy(dict())", 1), others),
        ("N3 注入 harness 消費者", app_src,
         dict(others, **{"verify/stepg_pipeline.py": others.get("verify/stepg_pipeline.py", "")
                         + "\n_adjx = ns['adj_intake']\n"})),
        ("N4 單位表只出首列", app_src.replace(
            "st.dataframe(_pd.DataFrame(_adj351_view['units']),",
            "st.dataframe(_pd.DataFrame(_adj351_view['units'][:1]),", 1), others),
    ]
    for mname, msrc, moth in muts:
        if mname != "N3 注入 harness 消費者" and msrc == app_src:
            print(f"  🔴 {mname}：突變錨不存在")
            red.append(mname.split()[0])
            continue
        turned = [n.split()[0] for n, ok, _ in _wiring_checks(msrc, moth)
                  if not ok and n.split()[0] not in base_red]
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _independent(tp3, bfin, rows, drops, own, bur):
    """外部錨：本器另寫之分類（⛔ 呼叫 adj_intake）。回 ({暫編: 類名}, {歸戶: (軌, 原街廓, 成員)})。"""
    alloc = {str(r["暫編地號"]) for r in rows if r.get("推進側別") in ("left", "right")}
    dg = {str(e["暫編地號"]): (str(b), float(e.get("G(㎡)") or 0)) for (b, s), v in drops.items() for e in v}
    mem = {}
    for u in bfin:
        if u.get("_is_ghost_sliver"):
            continue
        for m in u.get("入池閘併入") or [u["暫編地號"]]:
            mem[str(m)] = str(u["暫編地號"])
    kind, owner, s3 = {}, {}, set()
    for t in tp3:
        if t.get("_is_ghost_sliver"):
            continue
        k = str(t["暫編地號"])
        owner[k] = own[str(t["原地號"])]
        # 🔧 `W-G.9-363`（發單側窗六十四·⛔ 下列一字不刪）：帶 段三餘量 而其值 ＞ 0 之片（段三或手冊先行之剩下）⇒
        #   恆入合併單位（`W-G.9-357`）——其歸戶無入池之宗而有配地者，另成公設軌之單位（`adj_intake` 之 `_s3`）
        if float(t.get("段三餘量", 0) or 0) > 0:
            kind[k] = "公"
            s3.add(k)
        elif "段三併出" in t:
            kind[k] = "配"
        elif bur[t["所屬街廓"]] == "可建築土地":
            kind[k] = "配" if mem[k] in alloc else "池"
        else:
            kind[k] = "公"
    per = {}
    for k, g in owner.items():
        per.setdefault(g, []).append(k)
    units = {}
    for g, ks in per.items():
        has_p = any(kind[k] == "池" for k in ks)
        has_a = any(kind[k] == "配" for k in ks)
        cm = [k for k in ks if kind[k] == "公"]
        if has_p:
            bl = {}
            for u in {mem[k] for k in ks if kind[k] == "池"}:
                bl[dg[u][0]] = bl.get(dg[u][0], 0.0) + dg[u][1]
            units[g] = ("建", max(bl, key=bl.get), sorted([k for k in ks if kind[k] == "池"] + cm))
            for k in cm:
                kind[k] = "公入"
        elif cm and not has_a:
            units[g] = ("公", None, sorted(cm))
            for k in cm:
                kind[k] = "公入"
        else:
            for k in cm:
                kind[k] = "公4"
            # 🔧 `W-G.9-363`：段三之剩下（`s3`）⇒ 另成公設軌之單位
            if any(k in s3 for k in cm):
                units[g] = ("公", None, sorted(k for k in cm if k in s3))
                for k in cm:
                    if k in s3:
                        kind[k] = "公入"
    return kind, units


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        from app_harvest import harvest
        with contextlib.redirect_stdout(io.StringIO()):
            ns, fake_st = harvest(os.path.join(repo, "app.py"))
        if "adj_intake" not in ns:
            print("  🔴 受詞缺：adj_intake")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g
        MAP = {ns["ADJ_DISP_ALLOC"]: "配", ns["ADJ_DISP_POOL"]: "池", ns["ADJ_DISP_COMMON_UNIT"]: "公入",
               ns["ADJ_DISP_COMMON_STEP4"]: "公4"}
        TR = {ns["ADJ_TRACK_BUILD"]: "建", ns["ADJ_TRACK_PUBLIC"]: "公"}
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
                print(f"🔴 退縮 {sb}：run_step_g 無 k929_6（入池閘未啟用？）⇒ 無從判定")
                return 3
            drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
            bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
            print(f"══ 退縮 {sb} ══")
            try:
                it = ns["adj_intake"](tp3, k9["build"], sg["g_rows"], drops, own, bur)
            except RuntimeError as e:
                print(f"  🔴 R1 盤點停機：{str(e)[:300]}")
                red.append(f"R1@{sb}")
                continue
            print("  ✅ R1 盤點⛔ 停機")
            view = ns["adj_intake_rows"](it)
            for ln in view["lines"]:
                print("  " + ln)
            for r in view["totals"]:
                print(f"     {r['類']}：{r['切片數']} 片·{r['原有面積(㎡)']} ㎡")
            for r in view["units"]:
                print(f"     單位 {r['歸戶']}｜{r['軌']}｜原街廓 {r['原街廓']}｜據 {r['原街廓之據（應分配面積㎡）']}｜"
                      f"建 {r['建築街廓內不能分配之土地']}｜公 {r['公設地／道路上之土地']}｜合 {r['原有面積合計(㎡)']}｜"
                      f"配 {r['同歸戶原位次配地之街廓']}")
            for r in view["step4"]:
                print(f"     待併 {r['歸戶']}｜{r['公設地／道路上之土地']}｜合 {r['原有面積合計(㎡)']}｜"
                      f"配 {r['同歸戶原位次配地之街廓']}")
            kind, units = _independent(tp3, k9["build"], sg["g_rows"], drops, own, bur)
            got_k = {r["暫編地號"]: MAP[r["類"]] for r in it["slices"]}
            dif = sorted(k for k in set(kind) | set(got_k) if kind.get(k) != got_k.get(k))
            print(("  ✅" if not dif else "  🔴") + f" R2 逐切片之類（{len(got_k)} 片）與外部錨相同：相異 {dif[:10]}")
            if dif:
                red.append(f"R2@{sb}")
            got_u = {u["歸戶"]: (TR[u["軌"]], u["原街廓"],
                                 sorted(r["暫編地號"] for r in u["建築街廓內不能分配"] + u["共同負擔用地"]))
                     for u in it["units"]}
            difu = sorted(g for g in set(units) | set(got_u) if units.get(g) != got_u.get(g))
            print(("  ✅" if not difu else "  🔴") + f" R3 合併單位（{len(got_u)}）與外部錨相同：相異 {difu}")
            if difu:
                red.append(f"R3@{sb}")
            s_all = sum(float(t.get("分攤登記面積_m2", 0) or 0) for t in tp3)
            s_cls = sum(v[1] for v in it["totals"].values())
            n_cls = sum(v[0] for v in it["totals"].values())
            ok4 = abs(s_all - s_cls) <= 1e-6 and n_cls == len(tp3)
            print(("  ✅" if ok4 else "  🔴") + f" R4 逐類之和 ＝ 全部：{n_cls}／{len(tp3)} 片；{s_cls:.4f}／{s_all:.4f} ㎡")
            if not ok4:
                red.append(f"R4@{sb}")
            bfid = {str(u["暫編地號"]): u for u in k9["build"] if not u.get("_is_ghost_sliver")}
            dmem = [m for (b, s), v in drops.items() for e in v for m in (bfid[str(e["暫編地號"])].get("入池閘併入")
                                                                           or [str(e["暫編地號"])])]
            by3 = {str(t["暫編地號"]): t for t in tp3 if not t.get("_is_ghost_sliver")}
            n5, a5 = len(dmem), sum(float(by3[m].get("分攤登記面積_m2", 0) or 0) for m in dmem)
            c5 = it["totals"].get(ns["ADJ_DISP_POOL"], [0, 0.0])
            ok5 = n5 == c5[0] and abs(a5 - c5[1]) <= 1e-6
            print(("  ✅" if ok5 else "  🔴") + f" R5 入池宗（不配地單元之成員）{n5} 宗·{a5:.2f} ㎡ ＝ "
                  f"類「{ns['ADJ_DISP_POOL']}」{c5[0]} 片·{c5[1]:.2f} ㎡")
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
