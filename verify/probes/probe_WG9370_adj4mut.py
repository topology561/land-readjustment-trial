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
  🔧 `W-G.9-373`（`K-9-66`／`K-9-67`／`K-9-68`·⛔ 上列一字不刪）：第一趟改依 `K-9-66`（同一輪到達同一街廓者一起·逐類全併、
           不過之類按比例）與 `K-9-68`（輪）、受併宗之序之末改依 `K-9-67` ⇒ 其逐片之碼與序之鍵已去：`mutate` 唯留錨仍在之
           M20／M21／M23〜M27／M30（檢核·輸出之鍵·`GB-201` 之判），餘退（新碼之突變由次單以 CC 之碼之字樣為錨補寫）。
           `wiring`：X2 唯量頂層之相異 ⊆ {二函式} ∪ 本單之許（二函式之逐列之限退·本單重寫）；X3 改量 `_bpre_a4` 之新施點
           （其呼叫恰一、與 `k966_block_merge` 之呼叫同在一 `for` 之內且先之）；X4 之差除本單所改之二函式（`_k6b_callbacks`、
           `k6b_stage3_pool_temp`）之段；X5 之 `R-10′` 之模板改為新施點之文（「於第一趟併入街廓 {_bk} 之前」）。
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
    ("M30", "R-16", "GB-201 之判恆過", K953,
     "if not any(str(_r) in {str(_h) for _h in _hs} for _hs in (_Sg953.get(" + "\"kept\"" + ") or {}).values()):",
     "if False:", {"K15"}),
]
# 🔧 `W-G.9-373`：M01〜M19、M28、M29、M31 退（其錨隨 `K-9-66`／`K-9-67`／`K-9-68` 之重寫而去）


# 🆕 `W-G.9-370`（K-9-57 ⑧）：三停機訊息之模板（逐字）。`TOK`（「已為已配得」）拆字書之，以免他器以全檔之錨（長 ≥ 4 之
# 字串常數）收之。
TOK = "已為" + "已配得"
MSGS = [
    ("S238", A4, None,
     "{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g_str}）於第一趟沿名單至街廓 {_bk} 時，當下之試算已為已配得之宗或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
    # 🔧 `W-G.9-373`：`R-10′` 之施點改為「該輪併入街廓 _bk 之前」
    ("R-10′", A4, "_bpre_a4",
     "{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g}）於第一趟併入街廓 {_bk} 之前，當下之試算已為已配得之宗或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
    ("S219", K953, "_wpre953",
     "{_hdr953} 程式自我檢查：建地片 {_x}（{_blk953[_x]}）於整筆之主併入之前，當下之試算已為已配得之宗 {_own953} 或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
]


# 🔧 `W-G.9-373`：本單之許（頂層）與所改之 harness 二函式
ALLOW373_APP = ("K966_CLASSES", "K966_GRID", "k966_block_merge", "k967_rank", "k967_pre_area", "k6b_stage3_run",
                "k929_6_fixpoint", "adj_intake", "k6b_screen_callbacks")
ALLOW373_SP = ("_k6b_callbacks", "k6b_stage3_pool_temp")


def _strip_fns(src, names):
    """🔧 `W-G.9-373`：除去模組層函式 `names` 之原文（含其裝飾之列·無之 ⇒ 不變）。"""
    t = ast.parse(src)
    ls = src.splitlines(keepends=True)
    cut = sorted(((n.lineno - 1 - len(n.decorator_list), n.end_lineno, n.name) for n in t.body
                  if isinstance(n, ast.FunctionDef) and n.name in names), reverse=True)
    for a, b, nm in cut:
        ls[a:b] = [f"# <{nm}>\n"]
    return "".join(ls)


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
    ok2, notes = set(dif) <= {A4, K953} | set(ALLOW373_APP), []
    for fn in ():                   # 🔧 `W-G.9-373`：二函式之逐列之限退（本單重寫）
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
    res.append(("X2", f"app.py 之頂層節點對基準相異者 ⊆ {{{A4}, {K953}}} ∪ 本單之許（相異 {dif}；逾 "
                      f"{sorted(set(dif) - {A4, K953} - set(ALLOW373_APP))}）", ok2))
    # 🔧 `W-G.9-373`：`_bpre_a4` 之新施點——定義恰一（於 adj4_pass1_run 內）、呼叫恰一，且與 `k966_block_merge` 之呼叫
    #   （恰一）同在一 `for` 之內、先之
    tops0 = {n.name: n for n in ast.parse(a1).body if isinstance(n, ast.FunctionDef)}
    fa4 = tops0.get(A4)
    nd = calls_n = 0
    pos = False
    if fa4 is not None:
        par = {c: p for p in ast.walk(fa4) for c in ast.iter_child_nodes(p)}
        nd = sum(1 for n in ast.walk(fa4) if isinstance(n, ast.FunctionDef) and n.name == "_bpre_a4")
        bc = [n for n in ast.walk(fa4) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "_bpre_a4"]
        kc = [n for n in ast.walk(fa4) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
              and n.func.id == "k966_block_merge"]
        calls_n = len(bc)
        if len(bc) == 1 and len(kc) == 1:
            cur = kc[0]
            loop = None
            while cur in par:
                cur = par[cur]
                if isinstance(cur, ast.For):
                    loop = cur
                    break
            pos = (loop is not None and any(n is bc[0] for n in ast.walk(loop))
                   and (bc[0].lineno, bc[0].col_offset) < (kc[0].lineno, kc[0].col_offset))
    res.append(("X3", f"_bpre_a4：定義 {nd} 見、呼叫 {calls_n} 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 {pos}",
                nd == 1 and calls_n == 1 and pos))
    s0 = _strip_fns(_git_show(repo, base, "verify/selection_pipeline.py"), ALLOW373_SP).splitlines()
    s1 = _strip_fns(open(os.path.join(repo, "verify", "selection_pipeline.py"), encoding="utf-8").read(),
                    ALLOW373_SP).splitlines()
    d = [x for x in difflib.unified_diff(s0, s1, n=0, lineterm="") if x[:1] in "+-" and x[:3] not in ("+++", "---")]
    want = ['-            temp_parcels, build_parcels, ss["t8_ownership_map"]):',
            '-    _own_a4 = ss["t8_ownership_map"]',
            '+            temp_parcels, build_parcels, ss.get("t8_ownership_map", {}) or {}):',
            '+    _own_a4 = ss.get("t8_ownership_map", {}) or {}']
    res.append(("X4", f"verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化"
                      f"（差之列 {len(d)}）",
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
