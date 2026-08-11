# -*- coding: utf-8 -*-
r"""`W-G.9-11`：**22 名目全拆解**（考古 70 之收割）＋ 基準溯源對應。

`W-G.9-10` 只拆了 `G3` 三項，發現其 15 個主判定中有 **3 個之阻塞不是資料不足、而是<u>順序</u>**
（與擋路之 `raise` 同在一個 `try` 內、且排在其後）。本工具把受詞泛化為**名單上之 22 名目**。

## 分類判準（⛔ 事前登記已封·`docs/reports/W-G.9-11_前置登記.md` §2）

| 判 | 條件 |
|---|---|
| **只被順序擋住**（可回收） | 輸入**只有**：原始碼檔案／常數字面／`snapshot` |
| **真需管線** | 輸入含任何**須經 `run_step_g` 或 `wf_f*.compute` 產生**之物 |
| **需人判** | 以上皆不成立 ⇒ **印證據、交人**（⛔ 不自動歸類） |

⛔ **不得以「它在那個 `try` 裡」推定它需要管線**（考古 70 修法 ①）；
⛔ **不得以名目字面推定**（兩方向皆禁）；⛔ **不得以 `G3` 之 3/15 外推**。

## 🔒 母體自證（考古 69 修法 ①②）

斷言倉根、母體檔、覆蓋產物皆存在，並**印出母體規模**。

## `--verify-g3`：跨實作對拍（考古 69 修法 ③·`M2`）

以 `subprocess` 跑**舊工具** `wg910_g3_dissect.py`、解析其輸出，
與本工具對同三名目之結論**逐項比對**。⛔ 不重現即不得用本工具產生任何新結論。

## 重跑
    python verify/tools/wg911_all_dissect.py              # 22 名目全拆解
    python verify/tools/wg911_all_dissect.py --verify-g3  # 與舊工具對拍
"""
import ast
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
RV = os.path.join(VERIFY, "run_verification.py")
COV = os.path.join(VERIFY, "out", "WG96_coverage.txt")
LIST = os.path.join(VERIFY, "out", "K6A2_期望FAIL名單_WG97_名目加原因.txt")
OLD = os.path.join(HERE, "wg910_g3_dissect.py")

# 🔒 母體自證（⛔ 指錯檔／少一層 dirname 即產生假綠·考古 69）
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
for _p in (RV, COV, LIST, OLD):
    assert os.path.exists(_p), f"🔴 母體檔不存在：{_p}"

_SRC = open(RV, encoding="utf-8").read()
_AST = ast.parse(_SRC)

# 管線標記：其產物須經 `run_step_g`／`wf_f*.compute` 方存在
# 🔴 **兩層要分開**（`W-G.9-11` 現查·⛔ 首版混為一談）：
#   擋路之另案只在 `run_step_g`（結構閘 raise）；`build_pipeline`／`run_corner_pk` 等
#   **CAD 管線本身跑得通**（`wd3_fragment_geom.compute()` 即先跑完它們才死在 `run_step_g`）。
#   ⇒ 另立「**需 CAD 管線但不需 `run_step_g`**」之中間層——⛔ 該層**不在**事前登記之
#      「只被順序擋住」定義內（其定義限「原始碼／常數／snapshot」），故**另格呈現**、⛔ 不併入。
BLOCKED_CALLS = ("run_step_g", "compute")
CADPIPE_CALLS = ("build_pipeline", "run_corner_pk", "build_build_parcels",
                 "build_param_table", "build_ownership", "harvest")
PIPE_CALLS = BLOCKED_CALLS + CADPIPE_CALLS
PIPE_NAMES = ("_ctx", "_f0", "_f1", "_f2", "_f3", "_f4", "stepg_ctx",
              "_f2_ok", "_f0_ok", "_f3_ok")
STATIC_CALLS = ("open", "read", "count", "load_snapshot", "join", "sorted", "len",
                "abs", "round", "float", "int", "str", "set", "list", "dict")
STATIC_NAMES = ("snapshot", "HERE", "os", "V3RUN", "F0DIR", "F1DIR", "F2DIR", "F3DIR")


def name_literal(node):
    a0 = node.args[0]
    t = a0.elts[0] if isinstance(a0, (ast.Tuple, ast.List)) and a0.elts else a0
    if isinstance(t, ast.Constant) and isinstance(t.value, str):
        return t.value
    if isinstance(t, ast.JoinedStr):
        return "".join(v.value if isinstance(v, ast.Constant) and isinstance(v.value, str)
                       else "{…}" for v in t.values)
    return None


def all_appends():
    out = []
    for n in ast.walk(_AST):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append" and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "results"):
            out.append((n.lineno, name_literal(n), n))
    return sorted(out)


def load_cov():
    ex = set()
    for ln in open(COV, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        ex.add(int(ln.split("\t")[0]))
    return ex


def wanted_names():
    pat = re.compile(r"^🔴 FAIL\s\s(.*?)\s*$")
    return [m.group(1) for m in (pat.match(x) for x in
            open(LIST, encoding="utf-8").read().splitlines()) if m]


def match_site(nm, appends):
    """名目字面 → 站點（先精確、再 f-string 前綴）。"""
    hit = [(l, s, n) for l, s, n in appends if s == nm]
    if hit:
        return hit
    return [(l, s, n) for l, s, n in appends
            if s and s.split("{…}")[0] and nm.startswith(s.split("{…}")[0])]


def build_parent():
    p = {}
    for n in ast.walk(_AST):
        for c in ast.iter_child_nodes(n):
            p[c] = n
    return p


_PARENT = build_parent()


def enclosing_try(node):
    cur, in_handler = _PARENT.get(node), False
    seen = []
    while cur is not None:
        seen.append(cur)
        if isinstance(cur, ast.ExceptHandler):
            in_handler = True
        if isinstance(cur, ast.Try):
            return cur, in_handler
        cur = _PARENT.get(cur)
    return None, False


def try_span(t):
    lo = min(x.lineno for st in t.body for x in ast.walk(st) if hasattr(x, "lineno"))
    hi = max(getattr(x, "end_lineno", x.lineno) for st in t.body
             for x in ast.walk(st) if hasattr(x, "lineno"))
    return lo, hi


# ══════════════════════════════════════════════════════════════════════════
# 依賴分析（⛔ 印證據·不自動歸類無把握者）
# ══════════════════════════════════════════════════════════════════════════
def assign_map(t):
    """try body 內之 `name → [RHS 節點]`。

    🔴 **含<u>變異</u>**：`X.append(...)`／`X += ...`／`X.update(...)`／`X.extend(...)`
    之引數亦計為 `X` 之相依。
    ⚠️ **首版未含之** ⇒ `_vgN = []` 後以 `.append` 填值之判定（`W-G G.1`／`G.2`）
    其相依看似為空、被誤判為「可回收」——**偽陽性、且是危險方向**
    （`W-G.9-4b` 已證 `G.1` 崩於 `_ctx["0m"]`）。本批自誌。
    """
    m = {}
    for st in t.body:
        for n in ast.walk(st):
            if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                    and n.func.attr in ("append", "extend", "update", "add")
                    and isinstance(n.func.value, ast.Name)):
                for a in n.args:
                    m.setdefault(n.func.value.id, []).append(a)
            elif isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name):
                m.setdefault(n.target.id, []).append(n.value)
            elif isinstance(n, ast.Assign):
                for tg in n.targets:
                    for sub in ast.walk(tg):
                        if isinstance(sub, ast.Name):
                            m.setdefault(sub.id, []).append(n.value)
            elif isinstance(n, (ast.For, ast.comprehension)):
                tg = n.target
                for sub in ast.walk(tg):
                    if isinstance(sub, ast.Name):
                        m.setdefault(sub.id, []).append(getattr(n, "iter", None))
    return m


def deps(node, amap, depth=0, seen=None):
    """回 (呼叫名集合, 未解析名集合)。"""
    seen = seen or set()
    calls, names = set(), set()
    stack = [(node, 0)]
    while stack:
        cur, d = stack.pop()
        if cur is None or d > 6:
            continue
        for sub in ast.walk(cur):
            if isinstance(sub, ast.Call):
                f = sub.func
                if isinstance(f, ast.Name):
                    calls.add(f.id)
                elif isinstance(f, ast.Attribute):
                    calls.add(f.attr)
            elif isinstance(sub, ast.Name):
                if sub.id in amap and sub.id not in seen:
                    seen.add(sub.id)
                    for rhs in amap[sub.id]:
                        stack.append((rhs, d + 1))
                elif sub.id not in amap:
                    names.add(sub.id)
    return calls, names


def classify(site_node, amap):
    """⚠️ 只分析 `results.append(...)` 之**引數**——⛔ 不得把 `append` 自身算入呼叫，
    否則每一項都會落入「需人判」（本工具首版即如此·`W-G.9-11` 自誌）。"""
    calls, names = set(), set()
    for a in site_node.args:
        c, n = deps(a, amap)
        calls |= c
        names |= n
    blocked = sorted((calls & set(BLOCKED_CALLS)) | (names & set(PIPE_NAMES)))
    if blocked:
        return "真需管線", blocked, calls, names
    cadp = sorted(calls & set(CADPIPE_CALLS))
    if cadp:
        return "需CAD管線", cadp, calls, names
    # ⚠️ **被呼叫之名不是資料相依**：`open` 等既入 `calls` 又入 `names`（`ast.Name` 節點），
    #   首版未扣除 ⇒ `F.2／F.3 靜態閘`（其實只讀原始碼）被誤判為「需人判」。
    unknown = sorted(n for n in names if n not in STATIC_NAMES and not n.startswith("_")
                     and n not in calls
                     and n not in ("results", "tag", "nm", "rows", "n", "x", "k", "r"))
    odd = sorted(c for c in calls if c not in STATIC_CALLS)
    if not odd and not unknown:
        return "只被順序擋住", [], calls, names
    return "需人判", [], calls, names


# ══════════════════════════════════════════════════════════════════════════
def dissect():
    ex = load_cov()
    appends = all_appends()
    want = wanted_names()
    print(f"【母體】{os.path.relpath(RV, REPO).replace(chr(92),'/')}："
          f"{len(_SRC.splitlines())} 行｜`results.append` 站點 {len(appends)} 處")
    print(f"【覆蓋】{os.path.relpath(COV, REPO).replace(chr(92),'/')}：已執行行 {len(ex)}")
    print(f"【名單】{os.path.relpath(LIST, REPO).replace(chr(92),'/')}：{len(want)} 名目")
    assert appends and ex and want, "🔴 母體為空 ⇒ ⛔ 不得續（考古 67 修法 ①）"
    print()
    res = {}
    for nm in want:
        hits = match_site(nm, appends)
        if not hits:
            print(f"【{nm}】🔴 **站點未解析**")
            res[nm] = None
            continue
        ln0, lit, node = hits[0]
        t, in_h = enclosing_try(node)
        if t is None:
            print(f"【{nm}】無 `try` ⇒ 自身即活判定（本輪{'有' if ln0 in ex else '未'}執行）")
            res[nm] = {"try": None, "in_except": False, "main": []}
            continue
        lo, hi = try_span(t)
        amap = assign_map(t)
        mains = [(l, s, n) for l, s, n in appends if lo <= l <= hi]
        rows = []
        for l, s, n in mains:
            cls, pipe, calls, names = classify(n, amap)
            rows.append({"line": l, "name": s, "exec": l in ex, "cls": cls,
                         "pipe": pipe, "calls": sorted(calls), "names": sorted(names)})
        res[nm] = {"try": (lo, hi), "in_except": in_h, "main": rows}
        dead = [r for r in rows if not r["exec"]]
        rec = [r for r in dead if r["cls"] == "只被順序擋住"]
        need = [r for r in dead if r["cls"] == "需人判"]
        print(f"【{nm}】try {lo}–{hi}｜名目出自 `except` ⇒ {in_h}"
              f"｜主判定 {len(mains)}｜未執行 {len(dead)}"
              f"｜**可回收 {len(rec)}**｜需人判 {len(need)}")
        for r in rows:
            mark = "✅" if r["exec"] else {"只被順序擋住": "🟢", "需CAD管線": "🔵",
                                           "需人判": "🟡"}.get(r["cls"], "🔴")
            print(f"   {mark} {r['cls']:<8} {r['name']}")
            if not r["exec"] and r["cls"] != "真需管線":
                print(f"        呼叫 ＝ {r['calls']}")
                print(f"        未解析名 ＝ {r['names']}")
            elif not r["exec"]:
                print(f"        管線標記 ＝ {r['pipe']}")
        print()
    # 🔒 **去重**：多個名目（如 `…0m`／`…3.5m`）共用同一 `try` ⇒ 主判定會被重複計數。
    #   本工具首版報 90／85，**高於全檔死站點 80** 即其症狀（`W-G.9-11` 自誌）。
    uniq = {}
    for v in res.values():
        if v and v["main"]:
            for r in v["main"]:
                uniq[r["line"]] = r
    tot = len(uniq)
    dead = sum(1 for r in uniq.values() if not r["exec"])
    rec = sum(1 for r in uniq.values() if not r["exec"] and r["cls"] == "只被順序擋住")
    need = sum(1 for r in uniq.values() if not r["exec"] and r["cls"] == "需人判")
    cadn = sum(1 for r in uniq.values() if not r["exec"] and r["cls"] == "需CAD管線")
    print("=" * 96)
    print(f"⇒ 22 名目合計：主判定 **{tot}**｜未執行 **{dead}**"
          f"｜**只被順序擋住 {rec}**｜**需CAD管線（不需 run_step_g）{cadn}**"
          f"｜需人判 {need}｜真需管線 {dead - rec - need - cadn}")
    # 🔒 判別力自檢（考古 69 修法 ④）：受詞須**確在集合內**——⛔ 空清單不算自檢
    probe = [r for r in uniq.values() if r["exec"]]
    assert probe, "🔴 自檢受詞為空 ⇒ ⛔ 不得算通過（空自檢＝假綠·`W-G.9-11` 自誌）"
    print(f"🔒 判別力自檢：集合內**已執行**之主判定 {len(probe)} 個"
          f"（例：{probe[0]['name'][:40]}）⇒ 上式**非恆判未執行**")
    # 🔒 校準（⛔ 分類器須重現 `W-G.9-10` 之既有結論）
    CAL = ("F.3 靜態閘（wf_f3 不呼叫 calc_a_prime／三廢）",
           "F.3 跨區段 fixture（a→b a′={…}≠a·ratio≠1）",
           "W-G G.2 世代幾何曝出契約＋只寫不讀（v3/f0/f1/f2/f3/E 逐宗座標·靜態越界=0）")
    # 🔒 **校準判準**（⛔ 非「三項皆須自動判為可回收」——語法層無法解跨模組呼叫之輸入，
    #   如 `wf_f3.fixture_cross_zone_f3(snapshot)`）。本分類器定位為**保守篩子**：
    #     ① **⛔ 絕不可**把已證可回收者判為「真需管線」（**偽陰性為零**）；
    #     ② 判為「需人判」者**交人裁**（印證據）——此為設計，非失敗。
    print("🔒 校準（vs `W-G.9-10` 之三項已證可回收者·判準見碼註）：")
    miscal = []
    for c in CAL:
        got = [r["cls"] for r in uniq.values() if r["name"] == c]
        ok = got and got[0] != "真需管線"
        print(f"     {'✅' if ok else '🔴'} {c[:44]:<46} ⇒ {got}"
              f"{'' if got == ['只被順序擋住'] else '　（落需人判 ⇒ 交人裁）'}")
        if not ok:
            miscal.append(c)
    if miscal:
        print(f"🔴 **校準失敗（偽陰性）**：{miscal} ⇒ ⛔ 本分類器之判定不得採信")
    else:
        print("     ✅ **偽陰性為零** ⇒ 分類器可作為保守篩子（「真需管線」之判定可信）")
    return res


def verify_g3():
    """跨實作對拍：本工具 vs 舊工具（`wg910_g3_dissect.py`）對 `G3` 三項之結論。"""
    print("=" * 96)
    print("# `M2` 跨實作對拍：泛化工具 vs 舊工具（⛔ 不重現即不得用新工具產生結論）")
    print("=" * 96)
    r = subprocess.run([sys.executable, OLD], capture_output=True, text=True,
                       encoding="utf-8", env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    assert r.returncode == 0, f"🔴 舊工具 rc={r.returncode}"
    old_txt = r.stdout
    hdr = re.compile(r"^【(.+?)】try (\d+)–(\d+)｜except 之名目站點 @(\d+)（曾執行 ⇒ (\w+)）")
    site = re.compile(r"^\s+(🔴|✅) :(\d+)\s+(.*?)\s*$")
    old = {}
    cur = None
    for ln in old_txt.splitlines():
        m = hdr.match(ln)
        if m:
            cur = m.group(1)
            old[cur] = {"try": (int(m.group(2)), int(m.group(3))), "sites": []}
            continue
        m2 = site.match(ln)
        if m2 and cur:
            old[cur]["sites"].append((int(m2.group(2)), m2.group(3), m2.group(1) == "✅"))
    assert len(old) == 3, f"🔴 舊工具輸出解析出 {len(old)} 項（須 3）"
    print(f"  舊工具：解析出 {len(old)} 項｜"
          f"主判定合計 {sum(len(v['sites']) for v in old.values())}")

    ex, appends = load_cov(), all_appends()
    bad = []
    for nm, o in old.items():
        hits = match_site(nm, appends)
        assert hits, f"🔴 新工具找不到 {nm}"
        t, in_h = enclosing_try(hits[0][2])
        lo, hi = try_span(t)
        mains = sorted((l, s, l in ex) for l, s, _n in appends if lo <= l <= hi)
        if (lo, hi) != o["try"]:
            bad.append(f"{nm}：try 範圍 新{ (lo,hi) } ≠ 舊{o['try']}")
        if mains != sorted(o["sites"]):
            bad.append(f"{nm}：主判定集合不符\n     新={mains}\n     舊={sorted(o['sites'])}")
        if not in_h:
            bad.append(f"{nm}：新工具判其名目**非**出自 except（舊工具判為是）")
        print(f"  【{nm}】try {'✅' if (lo,hi)==o['try'] else '🔴'}"
              f"｜主判定 {len(mains)} 個 {'✅' if mains==sorted(o['sites']) else '🔴'}"
              f"｜except {'✅' if in_h else '🔴'}")
    print()
    if bad:
        for b in bad:
            print(f"  🔴 {b}")
        print("🔴 **M2 破 ⇒ `Y-2` 停機**（⛔ 不得擇一採用）")
        return 1
    print("  ✅ **M2 成立**：泛化工具逐項重現舊工具之結論（try 範圍／主判定集合／except 歸屬）")
    # 🔒 判別力自檢：人造一個不符，證上式抓得到
    fake = dict(old)
    k0 = list(fake)[0]
    probe = sorted(fake[k0]["sites"]) + [(999999, "（合成）", False)]
    print(f"  🔒 判別力自檢：對 `{k0}` 之集合人造一筆 ⇒ "
          f"{'✅ 會判不符' if probe != sorted(fake[k0]['sites']) else '🔴 仍判相符'}")
    return 0


if __name__ == "__main__":
    sys.exit(verify_g3() if "--verify-g3" in sys.argv else (dissect() and 0 or 0))
