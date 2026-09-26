# -*- coding: utf-8 -*-
"""W-G.9-350 量測器（發單側窗四十六擬·檔 F9·⛔ 由受單側改一字）：正面道路識別符（五級八鍵之 `r3`）。

子命令（一律 python verify/probes/probe_WG9350_frontroad.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·只 harvest `app.py`）：`r3_front_road_derive` 之九例（成功·區外·恰半·
           過半·歧義·折線·自身排除·頂點不足·線長為 0）、`r3_front_road_identifier`／`r3_front_road_rows`／
           `r3_front_road_caption` 之八例；另以 AST 自 `app.py` 抽出同名函式施三突變（`>` → `>=`、折線改取二端點、
           推導有值仍採使用者所填），每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST 查接線：W1 具名常數；W2 `parse_cad_precision_layers` 之初值鍵、折線頂點之留存、推導之呼叫與候選集
           （非可建築土地之補集）；W3 `main()` 之 session 寫入與二顯示函式之呼叫；W4 消費端 ＝ 生產碼 `34` 檔中
           除 `app.py` 外命中 `0`、`app.py` 中只在許可之函式內；W5 畫面路徑之合成案（`自誤 517`：抽出 `main()`
           之一覽區塊與卡片說明句，以假 st 與合成資料實際執行）。另施四突變（刪推導之賦值、改 session 鍵、
           於 `verify/stepg_pipeline.py` 注入一消費者、一覽只出首列），每一突變須轉紅。
  run      <repo>
           harness 之 CAD 入口（`run_verification._build_cb_cad`）實跑本案；出艙逐街廓之推導與一覽，並驗：
             R1 可建築街廓皆有推導；R2 狀態與比值一致（入推導集 ⇔ 比值 > 具名常數）；
             R3 線長之自我驗證閘（＝ `front_lines` 之 `length`·`LineString.length`）；
             R4 外部錨：以 shapely 之 `line ∩ polygon.buffer(1.0)` 另算比值，逐一分類（> 具名常數與否）與 R2 相同。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, json, math, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

R3_FUNCS = ["r3_front_road_derive", "r3_normalize_road_name", "r3_front_road_identifier",
            "r3_front_road_caption", "r3_front_road_rows"]
R3_CONSTS = ["R3_FRONT_ROAD_MAJORITY", "SS_FRONT_ROAD_DERIVE", "R3_STATUS_DERIVED",
             "R3_STATUS_OUTSIDE", "R3_STATUS_AMBIGUOUS", "R3_STATUS_NO_FRONT"]


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _extract_ns(src):
    """自 `app.py` 原始碼以 AST 抽出 `_line_block_overlap`、R3 常數與 R3 函式，於隔離之命名空間執行。"""
    tree = ast.parse(src)
    want_f = set(R3_FUNCS) | {"_line_block_overlap"}
    parts = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in want_f:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id in R3_CONSTS:
            parts.append(ast.get_source_segment(src, node))
    ns = {}
    exec(compile("\n\n".join(parts), "<r3_extract>", "exec"), ns)
    return ns


def _band(x0, x1, y0=-10.0, y1=0.0):
    from shapely.geometry import Polygon
    return Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def _cases(ns):
    """回 [(名, 得, 期)]；任一例拋例外 ⇒ 以 ('例外', 型別名) 記之（⛔ 吞）。"""
    from shapely.geometry import Polygon
    D = ns["r3_front_road_derive"]
    I = ns["r3_front_road_identifier"]
    RW = ns["r3_front_road_rows"]
    C = ns["r3_front_road_caption"]
    OK, OUT, AMB, NOF = (ns["R3_STATUS_DERIVED"], ns["R3_STATUS_OUTSIDE"],
                         ns["R3_STATUS_AMBIGUOUS"], ns["R3_STATUS_NO_FRONT"])
    LINE = {"B": [(0.0, 0.0), (100.0, 0.0)]}
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as e:  # noqa: BLE001
            got = ("例外", type(e).__name__)
        out.append((name, got, exp))

    def st(d):
        return (d["B"]["status"], d["B"]["derived"])

    run("S1 全長臨一道路 ⇒ 成功", lambda: st(D(LINE, {"A": ("道路", _band(0, 100))})), (OK, ["A"]))
    run("S2 無候選 ⇒ 區外", lambda: st(D(LINE, {})), (OUT, []))
    run("S3 沿線 30% ⇒ 區外", lambda: st(D(LINE, {"A": ("道路", _band(0, 30))})), (OUT, []))
    run("S4 沿線恰 50% ⇒ 區外（嚴格大於）", lambda: st(D(LINE, {"A": ("道路", _band(0, 50))})), (OUT, []))
    run("S5 沿線 50.5% ⇒ 成功", lambda: st(D(LINE, {"A": ("道路", _band(0, 50.5))})), (OK, ["A"]))
    run("S6 二候選各過半 ⇒ 歧義（重疊長降冪）",
        lambda: st(D(LINE, {"A": ("道路", _band(0, 60)), "B2": ("道路", _band(30, 100))})), (AMB, ["B2", "A"]))
    L2 = {"B": [(0.0, 0.0), (50.0, 0.0), (50.0, 50.0)]}
    run("S7 折線：只臨首段（50／100）⇒ 區外", lambda: st(D(L2, {"A": ("道路", _band(0, 50))})), (OUT, []))
    Lsh = Polygon([(0, -10), (60, -10), (60, 50), (50, 50), (50, 0), (0, 0)])
    run("S8 折線：臨二段 ⇒ 成功", lambda: st(D(L2, {"A": ("道路", Lsh)})), (OK, ["A"]))
    run("S9 候選含自身 ⇒ 排除", lambda: st(D(LINE, {"B": ("道路", _band(0, 100))})), (OUT, []))
    run("S10 頂點不足 ⇒ loud", lambda: D({"B": [(0.0, 0.0)]}, {}), ("例外", "ValueError"))
    run("S11 線長為 0 ⇒ loud", lambda: D({"B": [(1.0, 1.0), (1.0, 1.0)]}, {}), ("例外", "ValueError"))

    dv = D({"P": [(0.0, 0.0), (100.0, 0.0)], "Q": [(0.0, 50.0), (100.0, 50.0)],
            "R": [(0.0, 100.0), (100.0, 100.0)]},
           {"RD1": ("道路", _band(0, 100))})
    labels = ["P", "Q", "R", "Z"]
    run("I1 推導有值 ⇒ 採推導、使用者所填不採",
        lambda: (I(labels, dv, {"P": "中山路"})["P"]["id"], I(labels, dv, {"P": "中山路"})["P"]["user_text_ignored"]),
        ("RD1", True))
    run("I2 區外 ⇒ 採正規化後之名稱", lambda: I(labels, dv, {"Q": "  中正　路 "})["Q"]["id"], "中正 路")
    run("I3 區外而未填 ⇒ None", lambda: I(labels, dv, {})["Q"]["id"], None)
    run("I4 無推導 ⇒ 無正面線", lambda: (I(labels, dv, {"Z": "X"})["Z"]["status"], I(labels, dv, {"Z": "X"})["Z"]["id"]),
        (NOF, None))
    run("I5 全形 ＲＤ１ ⇒ 與推導之 RD1 同組",
        lambda: RW(labels, dv, {"Q": "ＲＤ１", "R": "中正路"})["groups"], {"RD1": ["P", "Q"], "中正路": ["R"]})
    run("I6 未填者列入 missing", lambda: RW(labels, dv, {"Q": "中正路"})["missing"], ["R", "Z"])
    run("I7 一覽各欄皆字串",
        lambda: all(isinstance(v, str) for r in RW(labels, dv, {"Q": "X"})["rows"] for v in r.values()), True)
    run("I8 說明句三態",
        lambda: ("推導有值" in C(dv["P"]), "重劃區外" in C(dv["Q"]), "無正面線" in C(None)), (True, True, True))
    return out


def _mutate(src, fname, old, new):
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == fname:
            seg = ast.get_source_segment(src, node)
            if seg.count(old) != 1:
                return None
            return src.replace(seg, seg.replace(old, new), 1)
    return None


MUTS_FN = [
    ("M1 `>` → `>=`", "r3_front_road_derive",
     "if _c['ratio'] > majority]", "if _c['ratio'] >= majority]"),
    ("M2 折線改取二端點", "r3_front_road_derive",
     "for _i in range(len(_pts) - 1))",
     "for _i in range(len(_pts) - 1)) * 0 + _m_r3.hypot(_pts[-1][0] - _pts[0][0], _pts[-1][1] - _pts[0][1])"),
    ("M3 推導有值仍採使用者所填", "r3_front_road_identifier",
     "{'id': _d['derived'][0],", "{'id': (_name or _d['derived'][0]),"),
]


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in R3_FUNCS + R3_CONSTS if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    print("── 合成對照（harvest 之 app.py）──")
    for name, got, exp in _cases(ns):
        ok = (got == exp)
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)
    print("── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──")
    src = _read(repo, "app.py")
    base = _extract_ns(src)
    b_red = [n for n, g, e in _cases(base) if g != e]
    print(("  ✅ " if not b_red else "  🔴 ") + f"M0 未突變之抽出版：紅 {b_red}（期 []）")
    if b_red:
        red.append("M0")
    for mname, fname, old, new in MUTS_FN:
        msrc = _mutate(src, fname, old, new)
        if msrc is None:
            print(f"  🔴 {mname}：突變錨不存在或非唯一")
            red.append(mname)
            continue
        m_red = [n for n, g, e in _cases(_extract_ns(msrc)) if g != e]
        ok = bool(m_red)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {m_red}")
        if not ok:
            red.append(mname)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


PROD_OTHERS_RE = re.compile(r"^verify/[^/]+\.py$")


def _wiring_checks(app_src, others):
    """回 [(名, 真偽, 註)]。`others` ＝ {路徑: 原始碼}（生產碼 34 檔中 app.py 以外者）。"""
    res = []
    tree = ast.parse(app_src)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    c = consts.get("R3_FRONT_ROAD_MAJORITY")
    ok1 = c is not None and isinstance(c.value, ast.Constant) and c.value.value == 0.5
    fd = top.get("r3_front_road_derive")
    ok1b = fd is not None and any(isinstance(d, ast.Name) and d.id == "R3_FRONT_ROAD_MAJORITY"
                                  for d in fd.args.defaults)
    lit = [n.lineno for f in R3_FUNCS if f in top for n in ast.walk(top[f])
           if isinstance(n, ast.Constant) and n.value == 0.5]
    res.append(("W1 具名常數 R3_FRONT_ROAD_MAJORITY ＝ 0.5、推導之預設引用之、R3 函式內⛔ 字面 0.5",
                ok1 and ok1b and not lit, f"字面 0.5 之列 {lit}"))
    pc = top.get("parse_cad_precision_layers")
    init_ok = keep_ok = call_ok = pool_ok = False
    if pc is not None:
        for n in ast.walk(pc):
            if isinstance(n, ast.Dict) and any(isinstance(k, ast.Constant) and k.value == "front_road_derive"
                                               for k in n.keys):
                init_ok = True
            if isinstance(n, ast.For) and isinstance(n.iter, ast.Name) and n.iter.id == "_front_raw":
                for m in ast.walk(n):
                    if isinstance(m, ast.Assign) and isinstance(m.targets[0], ast.Subscript) \
                            and isinstance(m.targets[0].value, ast.Name) \
                            and m.targets[0].value.id == "_front_pts_chosen":
                        keep_ok = True
            if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) \
                    and isinstance(n.targets[0].slice, ast.Constant) \
                    and n.targets[0].slice.value == "front_road_derive" \
                    and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name) \
                    and n.value.func.id == "r3_front_road_derive":
                call_ok = True
                a = n.value.args
                if len(a) >= 2 and isinstance(a[0], ast.Name) and a[0].id == "_front_pts_chosen" \
                        and isinstance(a[1], ast.DictComp):
                    for g in a[1].generators:
                        for cond in g.ifs:
                            if isinstance(cond, ast.Compare) and isinstance(cond.ops[0], ast.NotIn) \
                                    and isinstance(cond.comparators[0], ast.Name) \
                                    and cond.comparators[0].id == "_buildable_blocks":
                                pool_ok = True
    res.append(("W2a 解析之回傳初值含 'front_road_derive'", init_ok, ""))
    res.append(("W2b FRONT_LINE 綁定迴圈內留存全部頂點（_front_pts_chosen[...] ＝ …）", keep_ok, ""))
    res.append(("W2c result['front_road_derive'] ＝ r3_front_road_derive(_front_pts_chosen, …)", call_ok, ""))
    res.append(("W2d 候選集 ＝ 非 _buildable_blocks 之補集", pool_ok, ""))
    mn = top.get("main")
    store_ok = cap_ok = rows_ok = False
    if mn is not None:
        for n in ast.walk(mn):
            if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) \
                    and isinstance(n.targets[0].slice, ast.Name) \
                    and n.targets[0].slice.id == "SS_FRONT_ROAD_DERIVE":
                for m in ast.walk(n.value):
                    if isinstance(m, ast.Call) and isinstance(m.func, ast.Attribute) and m.func.attr == "get" \
                            and m.args and isinstance(m.args[0], ast.Constant) \
                            and m.args[0].value == "front_road_derive":
                        store_ok = True
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
                if n.func.id == "r3_front_road_caption":
                    cap_ok = True
                if n.func.id == "r3_front_road_rows":
                    rows_ok = True
    res.append(("W3a main()：st.session_state[SS_FRONT_ROAD_DERIVE] ＝ _cad_layers.get('front_road_derive', …)", store_ok, ""))
    res.append(("W3b main()：呼叫 r3_front_road_caption", cap_ok, ""))
    res.append(("W3c main()：呼叫 r3_front_road_rows", rows_ok, ""))
    toks = R3_FUNCS + ["SS_FRONT_ROAD_DERIVE", "front_road_derive", "R3_FRONT_ROAD_MAJORITY"]
    tok_re = re.compile("|".join(re.escape(t) for t in toks))
    other_hits = {p: len(tok_re.findall(s)) for p, s in sorted(others.items()) if tok_re.search(s)}
    allowed = set(R3_FUNCS) | {"parse_cad_precision_layers", "main"}
    bad = []
    for fname, node in top.items():
        if fname in allowed:
            continue
        seg = ast.get_source_segment(app_src, node) or ""
        if tok_re.search(seg):
            bad.append(fname)
    res.append((f"W4 消費端：生產碼他檔（{len(others)} 檔）命中 0；app.py 只在許可之函式內",
                not other_hits and not bad, f"他檔 {other_hits}；app.py 非許可函式 {bad}"))
    ok5, note5 = _synth_screen(app_src, mn)
    res.append(("W5 畫面路徑之合成案：main() 之一覽區塊與卡片說明句以假 st 實際執行", ok5, note5))
    return res


class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.calls = []

    def __getattr__(self, name):
        def rec(*a, **k):
            self.calls.append((name, a, k))
        return rec


def _synth_screen(app_src, mn):
    """`自誤 517`：`main()` 內之敘述⛔ 為 run_all 所執行 ⇒ 抽出其一覽區塊（自 `_r3_names_persist` 之賦值起
    連續 `6` 句）與卡片說明句，以假 st ＋ 合成資料實際執行，驗其輸出。"""
    if mn is None:
        return False, "無 main()"
    blk = cap = None
    for n in ast.walk(mn):
        for fld in ("body", "orelse", "finalbody"):
            body = getattr(n, fld, None)
            if not isinstance(body, list):
                continue
            for i, s in enumerate(body):
                if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name) \
                        and s.targets[0].id == "_r3_names_persist":
                    blk = body[i:i + 6]
                if isinstance(s, ast.Expr) and isinstance(s.value, ast.Call) \
                        and isinstance(s.value.func, ast.Attribute) and s.value.func.attr == "caption" \
                        and s.value.args and isinstance(s.value.args[0], ast.Call) \
                        and isinstance(s.value.args[0].func, ast.Name) \
                        and s.value.args[0].func.id == "r3_front_road_caption":
                    cap = s
    if blk is None or cap is None or not isinstance(blk[-1], ast.If):
        return False, "抽不到一覽區塊或說明句"
    try:
        import pandas as pd
        rns = _extract_ns(app_src)
        dv = rns["r3_front_road_derive"](
            {"P": [(0.0, 0.0), (100.0, 0.0)], "Q": [(0.0, 50.0), (100.0, 50.0)],
             "R": [(0.0, 100.0), (100.0, 100.0)]},
            {"RD1": ("道路", _band(0, 100))})
        bb = [{"id": 11, "label": "P"}, {"id": 12, "label": "Q"}, {"id": 13, "label": "R"}]
        ss = {rns["SS_FRONT_ROAD_DERIVE"]: dv, "f3_front_road_name_by_bid": {12: "中正路", 11: "甲路"}}
        fst = _FakeSt(ss)
        g = dict(rns, st=fst, pd=pd, build_blocks=bb, SS_FRONT_ROAD_NAME="f3_front_road_name_by_bid")
        exec(compile(ast.Module(body=blk, type_ignores=[]), "<main_r3_block>", "exec"), g)
        for b in bb:
            exec(compile(ast.Module(body=[cap], type_ignores=[]), "<main_r3_caption>", "exec"), dict(g, b=b))
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    dfs = [c for c in fst.calls if c[0] == "dataframe"]
    infos = [c for c in fst.calls if c[0] == "info"]
    caps = [c[1][0] for c in fst.calls if c[0] == "caption"]
    df = dfs[0][1][0] if len(dfs) == 1 else None
    checks = {
        "一覽 1 表 3 列": df is not None and len(df) == 3,
        "P 採 RD1（使用者所填不採）": df is not None and list(df["採用之識別符"]) == ["RD1", "中正路", "（未填）"],
        "組句 2": sum(1 for s in caps if s.startswith("正面道路「")) == 2,
        "待填 R": len(infos) == 1 and infos[0][1][0].endswith("R"),
        "卡片說明句 3": sum(1 for s in caps if s.startswith("🧭")) == 3,
    }
    bad = [k for k, v in checks.items() if not v]
    return (not bad), f"不符 {bad}"


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
        ("N1 刪推導之賦值", app_src.replace(
            "result['front_road_derive'] = r3_front_road_derive(", "_r3_unused = r3_front_road_derive(", 1), others),
        ("N2 main() 改寫他鍵", app_src.replace(
            "st.session_state[SS_FRONT_ROAD_DERIVE] = (", "st.session_state['f3_r3_other'] = (", 1), others),
        ("N3 注入 harness 消費者", app_src,
         dict(others, **{"verify/stepg_pipeline.py": others.get("verify/stepg_pipeline.py", "")
                         + "\n_r3x = (cad or {}).get('front_road_derive')\n"})),
        ("N4 一覽只出首列", app_src.replace(
            "st.dataframe(pd.DataFrame(_r3_view['rows']), hide_index=True)",
            "st.dataframe(pd.DataFrame(_r3_view['rows'][:1]), hide_index=True)", 1), others),
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


def run(repo):
    ns, _ = _harvest(repo)
    if "r3_front_road_rows" not in ns:
        print("  🔴 受詞缺：r3_front_road_rows")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        import run_verification as rv
        with contextlib.redirect_stdout(io.StringIO()):
            cb, cad = rv._build_cb_cad(ns)
    finally:
        os.chdir(cwd)
    from shapely.geometry import LineString, Polygon
    K = ns["R3_FRONT_ROAD_MAJORITY"]
    OK = ns["R3_STATUS_DERIVED"]
    d = cad.get("front_road_derive")
    labels = sorted(b["label"] for b in cb if b.get("burden_type") == "可建築土地")
    polys = {}
    for b in cb:
        v = b.get("vertices") or []
        if len(v) >= 3:
            p = Polygon(v)
            polys[b["label"]] = p if p.is_valid else p.buffer(0)
    red, undet = [], []
    print(f"── 推導（具名常數 ＝ {K}·可建築街廓 {len(labels)}）──")
    if d is None:
        print("  🔴 cad 無 'front_road_derive'")
        print("⇒ 紅 ['R1']；rc 1")
        return 1
    miss = [l for l in labels if l not in d]
    print(("  ✅ " if not miss else "  🔴 ") + f"R1 可建築街廓皆有推導：缺 {miss}")
    if miss:
        red.append("R1")
    for l in labels:
        e = d.get(l)
        if e is None:
            continue
        cands = ", ".join(f"{c['block']}({c['category']}) {c['overlap_m']:.4f} m／{100 * c['ratio']:.2f}%"
                          for c in e["candidates"]) or "—"
        print(f"  {l}　線長 {e['line_length_m']:.4f}　狀態 {e['status']}　推導 {e['derived']}　候選 {cands}")
        want = [c["block"] for c in e["candidates"] if c["ratio"] > K]
        st_ok = (want == e["derived"]) and ((e["status"] == OK) == (len(want) == 1))
        if not st_ok:
            red.append(f"R2:{l}")
        fl = (cad.get("front_lines") or {}).get(l) or {}
        gate = abs(float(fl.get("length", -1)) - e["line_length_m"]) <= 1e-6
        if not gate:
            red.append(f"R3:{l}")
            print(f"    🔴 R3 線長 {e['line_length_m']:.6f} ≠ front_lines.length {fl.get('length')}")
            continue
        p1, p2 = fl.get("p1"), fl.get("p2")
        if abs(math.hypot(p2[0] - p1[0], p2[1] - p1[1]) - e["line_length_m"]) > 1e-6:
            undet.append(f"R4:{l}（折線·外部錨以二端點不可行）")
            continue
        ln = LineString([p1, p2])
        for c in e["candidates"]:
            ext = ln.intersection(polys[c["block"]].buffer(1.0)).length / e["line_length_m"]
            agree = (ext > K) == (c["ratio"] > K)
            print(f"    {'✅' if agree else '🔴'} R4 外部錨 {c['block']}：{100 * ext:.2f}%（原語 {100 * c['ratio']:.2f}%）")
            if not agree:
                red.append(f"R4:{l}:{c['block']}")
    print("── 一覽（區外道路清單為空）──")
    v = ns["r3_front_road_rows"](labels, d, {})
    for r in v["rows"]:
        print("  " + json.dumps(r, ensure_ascii=False))
    print("  組：" + "；".join(v["group_lines"]))
    print(f"  待填：{v['missing']}")
    if undet:
        print(f"  ⚠️ 無從判定：{undet}")
    rc = 1 if red else (3 if undet else 0)
    print(f"⇒ 紅 {red}；rc {rc}")
    return rc


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], os.path.abspath(argv[2])
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "wiring":
        return wiring(repo)
    if cmd == "run":
        return run(repo)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
