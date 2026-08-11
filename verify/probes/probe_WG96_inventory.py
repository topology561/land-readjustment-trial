# -*- coding: utf-8 -*-
"""`W-G.9-6` `Q3`：22 名目逐項盤點（① 站點／② 失聲者／③ 候選接手者）。

## 三欄之分工（⛔ 誠實界定）

| 欄 | 本檔產出 | 報告補完 |
|---|---|---|
| ① **原守命題** | `results.append` 站點行號 ＋ 其**名目字面** | 由 CC 讀該字面與碼註後**逐字轉述**（⛔ 不憑推想） |
| ② **失聲者** | 由**覆蓋資料**求：該項所屬 `try` body 內**執行次數為 0** 之行，及落於其中之 `results.append` 站點（＝**連登記都沒發生**之閘） | — |
| ③ **現由誰守** | **候選**接手者：`run_verification.py` 內**曾執行**之站點 ＋ `run_all.py` 之 golden／末端夾具段（subprocess·**不在覆蓋射程內但確有執行**），以命題關鍵詞相交求之 | 由 CC 逐一判定並附三項射程 |

⚠️ ③ 之「候選」**⛔ 不等於**「接手者」；候選為空**⛔ 不等於**「無人接手」。
   報告中每一句「無人接手」須**另附**三項射程之否定性宣稱。

## 🔴 射程（⛔ 正面寫·非附註）

- **母體**＝`verify/run_verification.py`；`app.py`／`wf_f*.py`／`stepg_pipeline.py` 之
  內部斷言**不在母體內**。
- **② 之判定來自覆蓋資料**（`verify/out/WG96_coverage.txt`），⛔ **非**由 `try` 結構之閱讀推得。
- 🔴 **行覆蓋只能證「未執行」，⛔ 不能證「執行了就有在守」**——一道執行了但**恆真**之閘
  同樣不守任何事。**本批⛔ 不量恆真性**。
- **`run_all` 之 subprocess 段不在覆蓋射程內**（故 ③ 之候選中，夾具段係以**靜態清單**列出、
  並註明其 rc 來自長跑 log，⛔ 非來自覆蓋）。

## 重跑
    python verify/probes/probe_WG96_inventory.py
"""
import ast
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
RV = os.path.join(VERIFY, "run_verification.py")
RA = os.path.join(VERIFY, "run_all.py")
COV = os.path.join(VERIFY, "out", "WG96_coverage.txt")
LIST_INUSE = os.path.join(VERIFY, "out", "K6A2_期望FAIL名單_D2b1切換後.txt")
COV_LOG = os.path.join(VERIFY, "out", "WG96_runall_cov.log")
OUT = os.path.join(VERIFY, "out", "probe_WG96_inventory.log")
FAIL_RE = re.compile(r"^\s*🔴 FAIL\s\s(.*?)\s*$")

# 命題關鍵詞（⛔ 不預設任何符號名·取**領域語意**詞）——供 ③ 之候選相交
KEYS = ("守恆", "位次序", "投影序", "毗鄰", "G值", "滑池槽", "J表", "池流向", "池差",
        "旗標", "合併決策", "跨街廓", "跨區段", "碎片", "遞補", "整形", "錨",
        "結構永久閘", "結構不變量", "覆蓋", "MinA", "抵費地", "調配", "曝出", "接線")
L = []
RC = [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def load_cov():
    if not os.path.exists(COV):
        return None
    ex = set()
    for ln in open(COV, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        ex.add(int(ln.split("\t")[0]))
    return ex


def name_literal(node):
    a0 = node.args[0]
    tgt = a0.elts[0] if isinstance(a0, (ast.Tuple, ast.List)) and a0.elts else a0
    if isinstance(tgt, ast.Constant) and isinstance(tgt.value, str):
        return tgt.value
    if isinstance(tgt, ast.JoinedStr):
        return "".join(v.value if isinstance(v, ast.Constant) and isinstance(v.value, str)
                       else "{…}" for v in tgt.values)
    return None


def keys_of(s):
    return {k for k in KEYS if k in (s or "")}


def fixture_names():
    """`run_all.py` 末端夾具清單之檔名（⛔ 靜態讀·其 rc 見長跑 log）。"""
    return sorted(set(re.findall(r'\("(fixture_[A-Za-z0-9_]+\.py)"', open(RA, encoding="utf-8").read())))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    src = open(RV, encoding="utf-8").read()
    tree = ast.parse(src)
    parent = {}
    for n in ast.walk(tree):
        for c in ast.iter_child_nodes(n):
            parent[c] = n
    executed = load_cov()

    say("=" * 104)
    say("# `W-G.9-6` `Q3` 盤點：22 名目逐項三欄（機械部分）")
    say(f"  母體 ＝ {os.path.relpath(RV, REPO)}")
    say("  🔴 **射程上界**：行覆蓋只能證「**未執行**」，⛔ **不能**證「執行了就有在守」（恆真性未量）")
    say("  🔴 **射程**：`run_all` 之 subprocess 夾具段**不在**覆蓋射程內")
    say("=" * 104)
    if executed is None:
        red(f"覆蓋表不存在 ⇒ ② 欄無從判定，⛔ 不得以空當通過")
        return _dump()

    stmt_lines = {x.lineno for x in ast.walk(tree) if isinstance(x, ast.stmt)}
    say(f"  覆蓋：可執行敘述行 {len(stmt_lines)}｜其中**未執行** {len(stmt_lines - executed)}"
        f"（{100*len(stmt_lines-executed)/len(stmt_lines):.1f}%）")

    sites = []
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append" and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "results"):
            sites.append((n.lineno, name_literal(n), n))
    sites.sort()
    live = [(l, s) for l, s, _ in sites if l in executed]
    dead = [(l, s) for l, s, _ in sites if l not in executed]
    say(f"  `results.append` 站點 ＝ {len(sites)}｜✅ 曾執行 {len(live)}"
        f"｜🔴 **從未執行 {len(dead)}**（該閘連登記結果都沒發生）")
    if not sites:
        red("站點母體 ＝ 0 ⇒ ⛔ 不得以空當通過")
        return _dump()

    want = [m.group(1) for m in (FAIL_RE.match(x)
            for x in open(LIST_INUSE, encoding="utf-8").read().splitlines()) if m]
    fx = fixture_names()
    say(f"  期望 FAIL 名單 ＝ {len(want)} 名目｜`run_all` 末端夾具 ＝ {len(fx)} 支（subprocess·射程外但確有執行）")

    def match_site(nm):
        hit = [(l, s) for l, s, _ in sites if s == nm]
        if hit:
            return hit
        return [(l, s) for l, s, _ in sites
                if s and s.split("{…}")[0] and nm.startswith(s.split("{…}")[0])]

    def enclosing_try(node):
        cur = parent.get(node)
        while cur is not None:
            if isinstance(cur, ast.Try):
                return cur
            cur = parent.get(cur)
        return None

    say()
    say("─" * 104)
    say("【逐項】22 名目（⛔ 含 ②③ 為空者亦正面列出）")
    say("─" * 104)
    n_with_dead, total_dead_sites = 0, set()
    for nm in want:
        hits = match_site(nm)
        say()
        say(f"▸ **{nm}**")
        if not hits:
            red(f"① 站點**未能靜態解析** ⇒ ⛔ 由 CC 於報告以人工現查補（不得留空）")
            continue
        ln0, lit = hits[0]
        node = [n for l2, _s, n in sites if l2 == ln0][0]
        say(f"   ① 站點 `run_verification.py:{ln0}`　名目字面 ＝ {lit!r}"
            f"　（本輪{'✅ 有執行' if ln0 in executed else '🔴 未執行'}）")
        tr = enclosing_try(node)
        if tr is None:
            say(f"   ② **無** ——該站點不在任何 `try` 內 ⇒ 無「因例外而中止」之後續判定式")
            say(f"   ③ **自身仍活**：本站點本輪有執行、且產出 FAIL 明細 ⇒ 其命題仍被判定（只是紅）")
            continue
        body = sorted({x.lineno for st in tr.body for x in ast.walk(st) if hasattr(x, "lineno")})
        dead_lines = [x for x in body if x not in executed]
        inner = [(l, s) for l, s in dead if body and body[0] <= l <= body[-1]]
        total_dead_sites |= {l for l, _ in inner}
        if dead_lines:
            n_with_dead += 1
        say(f"   ② `try`(:{tr.lineno}) body {len(body)} 行 → **未執行 {len(dead_lines)} 行**"
            + (f"（{dead_lines[0]}–{dead_lines[-1]}）" if dead_lines else "")
            + f"；其中**從未執行之 `results.append` 站點 ＝ {len(inner)} 處**")
        for l, s in inner:
            say(f"        🔴 :{l:<6} {s}")
        if not inner:
            say(f"        （無）——⛔ 空係量出來的，非未查")
        # ③ 候選：與該項失聲之閘共享命題關鍵詞、且**本輪曾執行**之站點
        ks = set()
        for _l, s in inner:
            ks |= keys_of(s)
        # 🔒 排除**該項自身**之站點（含其 `except` 分支之 fallback append）——
        #   否則「W-G G.2 曝出契約」會撈到自己的 except 站點而看似有人接手（首版即如此）。
        self_head = (lit or "").split("{…}")[0]
        cand = sorted({s for l, s in live if s and keys_of(s) & ks
                       and s != lit and not (self_head and s.startswith(self_head))})
        say(f"   ③ 候選接手者（曾執行之站點 ∩ 命題關鍵詞 {sorted(ks) if ks else '（無關鍵詞）'}）"
            f" ＝ {cand if cand else '**（空）**'}")
        if not cand and inner:
            say(f"        ⚠️ 候選為空 ⇒ 報告須以**三項射程之否定性宣稱**補證，"
                f"⛔ 不得逕記為「無人接手」")

    say()
    say("─" * 104)
    say(f"【小結】22 名目中，其 `try` body 有未執行行者 ＝ {n_with_dead} 項；")
    say(f"        落於其中、**從未執行之 `results.append` 站點** ＝ {len(total_dead_sites)} 處")
    say(f"        全檔從未執行之站點 ＝ {len(dead)} 處（含不屬上列 22 項 `try` 者）")
    say("  🔴 **射程重述**：以上只證「**未執行**」。⛔ 已執行之 27 處是否**恆真**，本批未量。")
    return _dump()


def _dump():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
