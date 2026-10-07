# -*- coding: utf-8 -*-
"""W-G.9-370 量測器（發單側窗六十九擬·窗七十一改·檔 F25·⛔ 由受單側改一字）：規格步 4 乙之第一趟（`adj4_pass1_run`）與
手冊先行之 `GB-201` 之防護（`k953_manual_run`）——以 CC 之碼之字樣為錨之突變之判別力（`W-G.9-367 §四-2`），及 `W-G.9-370`
之改動之接線（`R-10′`、`R-22`、`K-9-57` ⑧ 之三停機訊息）。

子命令（一律 python verify/probes/probe_WG9370_adj4mut.py <子命令> …）：
  mutate <repo>
           逐突變：於其函式（`adj4_pass1_run`／`k953_manual_run`）之源碼段內，其錨恰一見 ⇒ 換之、寫出倉外之暫存檔，另一行程
           以之 harvest、跑 F24（`verify/probes/probe_WG9367_adj4.py`）之 `_cases` ⇒ 紅之集；判 ＝ 錨恰一見 且 其所指之項 ⊆ 紅之集。
           基準 M00（⛔ 突變）之紅之集須為空。
           ⛔ 列之突變：`R-12` 之「`R` 之除」（`(前保留 − R) − 後保留` → `前保留 − 後保留`）——`R-8` 之查（街廓之首）與 `R-10′` 之查
           （逐片之建地之整筆之試之前）使每一 `R ≠ ∅` 之檢核之 `R` 與其前態之已配得之宗之成員⛔ 交 ⇒ 等價之突變。
  wiring <repo> <基準 commit>
           X1 生產碼 `34` 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}；X2 app.py 之頂層節點對基準相異者 ⊆
           {adj4_pass1_run, k953_manual_run}；`adj4_pass1_run` 對基準唯增列，唯基準中訊息含 `TOK` 之 raise 之列得易；
           `k953_manual_run` 對基準之差唯在基準中訊息含 `TOK` 之 raise 之列之內（⛔ 他處增列）；X3 `def _bpre_a4(_x, _g):` 於
           `adj4_pass1_run` 恰一見、其呼叫 `_bpre_a4(_x, _g_str)` 恰一見，其前一非空列 ＝ `if _cls[_x] == '建地':`、其後一非空列 ＝
           `_c1 = _dup_a4(state)`；X4 verify/selection_pipeline.py 對基準之差恰為 `run_adj4` 之二列（`ss["t8_ownership_map"]` →
           `ss.get("t8_ownership_map", {}) or {}`）；X5 三停機訊息（`K-9-57` ⑧·程式自我檢查）：`MSGS` 之三模板各於其處（`S238` ＝
           `adj4_pass1_run` 之本體、`R-10′` ＝ 其巢狀之 `_bpre_a4`、`S219` ＝ `k953_manual_run` 之巢狀之 `_wpre953`）之 raise 之訊息
           恰一見，且二函式中訊息含 `TOK` 之 raise 皆屬之（舊訊息⛔ 存）。模板 ＝ 訊息之 f-string 之常數段逐字、其代入段
           以 `{` ＋ 式之 `ast.unparse` ＋ `}` 代之。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, difflib, io, json, os, re, subprocess, sys, tempfile, textwrap
from concurrent.futures import ThreadPoolExecutor

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

A4, K953 = "adj4_pass1_run", "k953_manual_run"
# (號, 條, 述, 函式, 錨, 換, 所指之項)
MUTS = [
    ("M01", "R-8", "受併宗之鍵：同原地號居先去之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)", {"K7"}),
    ("M02", "R-8", "受併宗之鍵：距離之序反之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0 if _same else 1, -float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)", {"K7"}),
    ("M03", "R-8", "受併宗之鍵：同距離之 G 序反之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), float(_S['G'][_h]), _h)", {"K7"}),
    ("M04", "R-8", "受併宗之鍵：末鍵（暫編地號）反之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), "
     "[-ord(_c) for _c in _h])", {"K7"}),
    ("M05", "R-8", "受併宗之候選⛔ 限同歸戶", A4,
     "if str(_h) in state[\"by\"] and _gw_a4(state[\"by\"][str(_h)]) == _g_str)",
     "if str(_h) in state[\"by\"])", {"K3"}),
    ("M06", "R-8", "受併宗之成員之形改取當下之 temp 之形（GB-199）", A4,
     "_cen = _uu_a4([_orig_a4(_m, '受併宗之成員') for _m in _ms]).centroid",
     "_cen = _uu_a4([_Pg_a4(state['by'][_m]['polygon_coords']).buffer(0) for _m in _ms if _m in state['by']])"
     ".centroid", {"K12"}),
    ("M07", "R-8", "街廓之首之「建地片已為已配得」之查去之", A4,
     "if _cls[_x] == '建地' and _pos_a4(_L[_x]) and _x in _inS:", "if False:", {"K9"}),
    ("M08", "R-9", "整體成而⛔ 止", A4,
     "                    _L[_x] = 0.0\n                break\n", "                    _L[_x] = 0.0\n", {"K3"}),
    ("M09", "R-8", "街廓之首之止（諸片皆無剩下）去之", A4,
     "            if not any(_pos_a4(_L[_x]) for _x in _pcs):\n                break\n",
     "            if False:\n                break\n", {"K23"}),
    ("M10", "R-9", "live 改為全部之片", A4,
     "_live = [_x for _x in _pcs if _pos_a4(_L[_x])]", "_live = list(_pcs)", {"K4"}),
    ("M11", "R-9", "整體之併入量改以原面積（⛔ 剩下）", A4,
     "_q_all = sum(_kv_a4[_x] * _L[_x] for _x in _live)",
     "_q_all = sum(_kv_a4[_x] * _amt_a4(_tin_a4[_x]) for _x in _live)", {"K4"}),
    ("M12", "R-9", "整體之建地片⛔ 自 build 去", A4,
     "_c_all[\"build\"] = [_b for _b in _c_all[\"build\"] if str(_b['暫編地號']) not in set(_blds)]", "pass",
     {"K3", "K24"}),
    ("M13", "R-9", "整體之檢核之 T 唯本街廓", A4,
     "_ok, _why = _chk_a4(state, _c_all, {_bk} | {str(_tin_a4[_x].get('所屬街廓', '') or '') for _x in _blds},",
     "_ok, _why = _chk_a4(state, _c_all, {_bk},", {"K24"}),
    ("M14", "R-10", "逐片之類之序反之", A4,
     "_rank_a4 = {'建地': 0, '道路': 1, '公設地': 2}", "_rank_a4 = {'建地': 2, '道路': 1, '公設地': 0}", {"K4"}),
    ("M15", "R-10", "逐片之同類之序（剩下大者先）反之", A4,
     "key=lambda _y: (_rank_a4[_cls[_y]], -_L[_y], _y)", "key=lambda _y: (_rank_a4[_cls[_y]], _L[_y], _y)", {"K25"}),
    ("M16", "R-10", "最大面積之格改 0.1", A4,
     "_got = _probe_a4(_n_md / 100.0)", "_got = _probe_a4(_n_md // 10 * 10 / 100.0)", {"K4"}),
    ("M17", "R-10", "最大面積⛔ 先試全量", A4, "_whole_st = _probe_a4(_s)\n", "_whole_st = None\n", {"K13"}),
    ("M18", "R-10", "逐片之建地之檢核之 T 唯本街廓", A4,
     "_ok1, _why1 = _chk_a4(state, _c1, {_bk, str(_tin_a4[_x].get('所屬街廓', '') or '')}, {_x})",
     "_ok1, _why1 = _chk_a4(state, _c1, {_bk}, {_x})", {"K24"}),
    ("M19", "R-10", "逐片之建地片⛔ 自 build 去", A4,
     "_c1[\"build\"] = [_b for _b in _c1[\"build\"] if str(_b['暫編地號']) != _x]", "pass", {"K24"}),
    ("M20", "R-12", "原保留之宗之判去之", A4,
     "            if _lost:\n                _why.append(", "            if False:\n                _why.append(", {"K14"}),
    ("M21", "R-12", "配餘地不合格之判去之", A4,
     "if int(_sa[\"bad_pools\"].get(_t, 0)) > int(_sb[\"bad_pools\"].get(_t, 0)):", "if False:", {"K4b"}),
    ("M23", "R-12", "併入後之配地中止改為過", A4,
     "            return False, '併入後配地中止：' + str(_sa.get('err'))[:120]\n", "            return True, ''\n",
     {"K26"}),
    ("M24", "R-13", "段三併出⛔ 合既有", A4,
     "_d['段三併出'] = sorted(set(str(_y) for _y in (_d.get('段三併出') or [])) | _marks_a4[_x])",
     "_d['段三併出'] = sorted(_marks_a4[_x])", {"K8"}),
    ("M25", "R-13", "段三部分併出⛔ 合既有", A4,
     "_acc_a4 = {str(_k): float(_v) for _k, _v in (_d.get('段三部分併出') or {}).items()}", "_acc_a4 = {}", {"K8"}),
    ("M26", "R-13", "全併⛔ 去部分二鍵", A4,
     "            _d.pop('段三部分併出', None)\n            _d.pop('段三餘量', None)\n", "            pass\n", {"K8"}),
    ("M27", "R-13", "段三餘量之值誤", A4,
     "_d['段三餘量'] = round(_rm_a4, 4)", "_d['段三餘量'] = round(_rm_a4 + 0.01, 4)", {"K8"}),
    ("M28", "R-16", "施點甲（可拆分之片之最大面積之試之前）去之", K953,
     "        _gb201_953(_x, _r)              # 🆕 `W-G.9-367`（R-16）：可拆分之片",
     "        pass                            # 🆕 `W-G.9-367`（R-16）：可拆分之片", {"K15"}),
    ("M29", "R-16", "施點乙（整筆之主併入之前）去之", K953,
     "            _gb201_953(_x, _r)          # 🆕 `W-G.9-367`（R-16）：整筆之主併入之前",
     "            pass                        # 🆕 `W-G.9-367`（R-16）：整筆之主併入之前", {"K15"}),
    ("M30", "R-16", "GB-201 之判恆過", K953,
     "if not any(str(_r) in {str(_h) for _h in _hs} for _hs in (_Sg953.get(" + "\"kept\"" + ") or {}).values()):",
     "if False:", {"K15"}),
    ("M31", "R-10′", "逐片之建地之整筆之試之前之查（K-9-57 ⑧·程式自我檢查）去之", A4,
     "                    _bpre_a4(_x, _g_str)\n", "                    pass\n", {"K27"}),
]


# 🆕 `W-G.9-370`（K-9-57 ⑧）：三停機訊息之模板（逐字）。`TOK`（「已為已配得」）拆字書之，以免他器以全檔之錨（長 ≥ 4 之
# 字串常數）收之。
TOK = "已為" + "已配得"
MSGS = [
    ("S238", A4, None,
     "{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g_str}）於第一趟沿名單至街廓 {_bk} 時，當下之試算已為已配得之宗或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
    ("R-10′", A4, "_bpre_a4",
     "{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g}）於逐片之整筆之試之前，當下之試算已為已配得之宗或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
    ("S219", K953, "_wpre953",
     "{_hdr953} 程式自我檢查：建地片 {_x}（{_blk953[_x]}）於整筆之主併入之前，當下之試算已為已配得之宗 {_own953} 或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
]


def _span(src, fn):
    a = src.index("\ndef " + fn + "(") + 1
    m = re.search(r"\n(def |class |[A-Za-z_])", src[a:])
    return a, (a + m.start() + 1 if m else len(src))


def _child(repo, app):
    sys.path.insert(0, os.path.join(repo, "verify", "probes"))
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, _ = harvest(app)
    import probe_WG9367_adj4 as F
    import selection_pipeline as sp
    need = F._need(ns, sp)
    if need:
        print(json.dumps(["受詞缺"] + need, ensure_ascii=False))
        return 0
    with contextlib.redirect_stdout(io.StringIO()):
        cases = F._cases(ns, sp)
    print(json.dumps(F._report(cases, verbose=False), ensure_ascii=False))
    return 0


def mutate(repo):
    src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    tmp = tempfile.mkdtemp(prefix="wg9368mut_")
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")

    def one(m):
        mid, cl, desc, fn, old, new, want = m
        if mid == "M00":
            n, text = 1, src
        else:
            a, b = _span(src, fn)
            n = src[a:b].count(old)
            if n != 1:
                return m, n, None
            text = src[:a] + src[a:b].replace(old, new, 1) + src[b:]
        p = os.path.join(tmp, f"app_{mid}.py")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        r = subprocess.run([sys.executable, os.path.abspath(__file__), "_child", repo, p], capture_output=True,
                           text=True, encoding="utf-8", env=env)
        try:
            red = json.loads((r.stdout.strip().splitlines() or ["null"])[-1])
        except Exception:  # noqa: BLE001
            red = None
        if r.returncode != 0 or not isinstance(red, list):
            return m, n, ("例外", (r.stderr.strip().splitlines() or ["?"])[-1][:200])
        return m, n, red

    todo = [("M00", "—", "基準（⛔ 突變）", None, None, None, set())] + MUTS
    bad = []
    with ThreadPoolExecutor(2) as ex:
        for m, n, red in ex.map(one, todo):
            mid, cl, desc, fn, old, new, want = m
            if mid == "M00":
                ok = red == []
            else:
                ok = n == 1 and isinstance(red, list) and bool(want) and want <= set(red)
            if not ok:
                bad.append(mid)
            print(f"  {'✅' if ok else '🔴'} {mid} {cl}·{desc}：錨 {n} 見；紅 {red}；所指 {sorted(want)}")
    print(f"⇒ 突變 {len(MUTS)}（另基準一）；紅 {bad}；rc {1 if bad else 0}")
    return 1 if bad else 0


def _git_show(repo, rev, rel):
    return subprocess.run(["git", "-C", repo, "show", f"{rev}:{rel}"], capture_output=True, check=True
                          ).stdout.decode("utf-8")


def _top(src):
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = ast.dump(n)
    return out


def _tpl(e):
    """raise 之訊息之模板：f-string 之常數段逐字、代入段以 `{式}` 代之；字串常數照錄；他形 ⇒ None。"""
    if isinstance(e, ast.Constant) and isinstance(e.value, str):
        return e.value
    if isinstance(e, ast.JoinedStr):
        out = []
        for v in e.values:
            if isinstance(v, ast.Constant):
                out.append(str(v.value))
            elif isinstance(v, ast.FormattedValue):
                cv = {-1: "", 114: "!r", 115: "!s", 97: "!a"}[v.conversion]
                out.append("{" + ast.unparse(v.value) + cv + "}")
            else:
                return None
        return "".join(out)
    return None


def _raise_tpls(node):
    """node 之內（含巢狀）一切 `raise X(<訊息>, …)` 之訊息之模板。"""
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call) and n.exc.args:
            t = _tpl(n.exc.args[0])
            if t is not None:
                out.append(t)
    return out


def _tok_raise_lines(src):
    """函式之源碼段（自 `def` 列起）中，訊息含 `TOK` 之 raise 之列之索引（0 起·該段內）之集。"""
    t = ast.parse(textwrap.dedent(src))
    lines = set()
    for n in ast.walk(t):
        if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call) and n.exc.args:
            m = _tpl(n.exc.args[0])
            if m is not None and TOK in m:
                lines |= set(range(n.lineno - 1, n.end_lineno))
    return lines


def _fn_src(src, fn):
    a, b = _span(src, fn)
    return src[a:b]


def wiring(repo, base):
    res = []
    r = subprocess.run(["git", "-C", repo, "diff", "--name-only", base, "--", "app.py", ":(glob)verify/*.py"],
                       capture_output=True, text=True, encoding="utf-8")
    chg = sorted(x for x in r.stdout.split() if x)
    res.append(("X1", f"生產碼 34 檔對基準相異者 ⊆ {{app.py, verify/selection_pipeline.py}}（相異 {chg}）",
                r.returncode == 0 and set(chg) <= {"app.py", "verify/selection_pipeline.py"}))
    a0, a1 = _git_show(repo, base, "app.py"), open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    t0, t1 = _top(a0), _top(a1)
    dif = sorted(k for k in set(t0) | set(t1) if t0.get(k) != t1.get(k))
    ok2, notes = set(dif) <= {A4, K953}, []
    for fn in (A4, K953):
        src0 = _fn_src(a0, fn)
        f0, f1 = src0.splitlines(), _fn_src(a1, fn).splitlines()
        rl = _tok_raise_lines(src0)
        ops = [o for o in difflib.SequenceMatcher(a=f0, b=f1, autojunk=False).get_opcodes() if o[0] != "equal"]
        if fn == A4:
            bad = [o for o in ops if o[0] != "insert" and not set(range(o[1], o[2])) <= rl]
        else:
            bad = [o for o in ops if not (rl and min(rl) <= o[1] and o[2] <= max(rl) + 1)]
        ok2 = ok2 and not bad
        notes.append(f"{fn}：差之段 {len(ops)}、逾許者 {[(o[0], o[1] + 1, o[2]) for o in bad][:3]}、許易之列 {len(rl)}")
    res.append(("X2", f"app.py 之頂層節點對基準相異者 ⊆ {{{A4}, {K953}}}（相異 {dif}）；" + "；".join(notes), ok2))
    body = _fn_src(a1, A4)
    lines = [x for x in body.splitlines() if x.strip()]
    nd = sum(1 for x in lines if x.strip() == "def _bpre_a4(_x, _g):")
    calls = [i for i, x in enumerate(lines) if x.strip() == "_bpre_a4(_x, _g_str)"]
    pos = (len(calls) == 1 and lines[calls[0] - 1].strip() == "if _cls[_x] == '建地':"
           and lines[calls[0] + 1].strip() == "_c1 = _dup_a4(state)")
    res.append(("X3", f"_bpre_a4：定義 {nd} 見、呼叫 {len(calls)} 見、其位 ＝ 建地之支之首 {pos}",
                nd == 1 and len(calls) == 1 and pos))
    s0 = _git_show(repo, base, "verify/selection_pipeline.py").splitlines()
    s1 = open(os.path.join(repo, "verify", "selection_pipeline.py"), encoding="utf-8").read().splitlines()
    d = [x for x in difflib.unified_diff(s0, s1, n=0, lineterm="") if x[:1] in "+-" and x[:3] not in ("+++", "---")]
    want = ['-            temp_parcels, build_parcels, ss["t8_ownership_map"]):',
            '-    _own_a4 = ss["t8_ownership_map"]',
            '+            temp_parcels, build_parcels, ss.get("t8_ownership_map", {}) or {}):',
            '+    _own_a4 = ss.get("t8_ownership_map", {}) or {}']
    res.append(("X4", f"verify/selection_pipeline.py 對基準之差 ＝ run_adj4 之二列之 .get 化（差之列 {len(d)}）",
                sorted(d) == sorted(want)))
    tree = ast.parse(a1)
    tops = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    x5, ok5 = [], True
    for tag, fn, inner, tpl in MSGS:
        node = tops.get(fn)
        if node is not None and inner is not None:
            node = next((n for n in ast.walk(node) if isinstance(n, ast.FunctionDef) and n.name == inner), None)
        got = [t for t in (_raise_tpls(node) if node is not None else []) if t == tpl]
        x5.append(f"{tag} {len(got)} 見")
        ok5 = ok5 and len(got) == 1
    stray = []
    for fn in (A4, K953):
        for t in (_raise_tpls(tops[fn]) if fn in tops else []):
            if TOK in t and t not in {m[3] for m in MSGS}:
                stray.append((fn, t[:60]))
    res.append(("X5", f"三停機訊息（K-9-57 ⑧）之模板：{'、'.join(x5)}；含 TOK 而⛔ 屬模板之 raise {stray[:3]}",
                ok5 and not stray))
    red = [c for c, _, ok in res if not ok]
    for c, msg, ok in res:
        print(f"  {'✅' if ok else '🔴'} {c} {msg}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) >= 4 and argv[1] == "_child":
        return _child(os.path.abspath(argv[2]), os.path.abspath(argv[3]))
    if len(argv) == 3 and argv[1] == "mutate":
        return mutate(os.path.abspath(argv[2]))
    if len(argv) == 4 and argv[1] == "wiring":
        return wiring(os.path.abspath(argv[2]), argv[3])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
