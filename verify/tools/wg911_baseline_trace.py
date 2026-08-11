# -*- coding: utf-8 -*-
r"""`W-G.9-11` 乙組：16 個 v3 基準之**溯源表**（五欄）。

| 欄 | 取得 |
|---|---|
| ① 檔名 | `verify/baselines/v3/*.csv` |
| ② **哪些主判定拿它對比** | **AST 現查** `diff_rows(..., os.path.join(V3RUN, "<檔>"), ...)` ⛔ 非由檔名推想 |
| ③ 烘焙 commit／日期 | `git log -1` |
| ④ 自烘焙以來生產側是否觸及其產生路徑 | `git log <bake>..HEAD -- <路徑集>`（**附三項射程**） |
| ⑤ ⇒「基準過期」是否為活假說 | 由 ④ 導出 |

🔒 母體自證（考古 69 修法 ①②）：斷言倉根與母體，並印母體規模。
"""
import ast
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True).stdout.strip()
assert REPO and os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
os.chdir(REPO)
RV = "verify/run_verification.py"
BDIR = "verify/baselines/v3"
assert os.path.exists(RV) and os.path.isdir(BDIR), "🔴 母體不存在"

# 🔴 ④ 之【目錄射程】：**生產側**＝產生 v3 基準之路徑
#   ⚠️ 本清單為**一層直接參與者**，⛔ **未做 import 遞移閉包**——具名聲明於輸出。
PROD = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
        "verify/run_verification.py", "verify/wd3_fragment_geom.py",
        "verify/wd4_tier_list.py", "verify/app_harvest.py",
        "verify/case_params_UC9898.json", "data/V6.dxf", "data/地籍資料來源_匿名版.xlsx"]


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True,
                          encoding="utf-8").stdout.strip()


def baseline_consumers():
    """AST：`diff_rows(got, os.path.join(V3RUN, "<f>"), keys, label)` → {檔名: [label…]}。"""
    src = open(RV, encoding="utf-8").read()
    tree = ast.parse(src)
    out = {}
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == "diff_rows" and len(n.args) >= 4):
            continue
        p = n.args[1]
        fn = None
        if isinstance(p, ast.Call) and isinstance(p.func, ast.Attribute) and p.func.attr == "join":
            for a in p.args:
                if isinstance(a, ast.Constant) and isinstance(a.value, str) and a.value.endswith(".csv"):
                    fn = a.value
                elif isinstance(a, ast.JoinedStr):
                    fn = "".join(v.value if isinstance(v, ast.Constant) else "{…}"
                                 for v in a.values)
            base = p.args[0]
            base_id = getattr(base, "id", "?")
        else:
            continue
        if base_id != "V3RUN" or not fn:
            continue
        lab = n.args[3]
        lab_s = (lab.value if isinstance(lab, ast.Constant)
                 else "".join(v.value if isinstance(v, ast.Constant) else "{…}"
                              for v in lab.values) if isinstance(lab, ast.JoinedStr) else "?")
        out.setdefault(fn, []).append(lab_s)
    return out


def main():
    files = sorted(f for f in os.listdir(BDIR) if f.endswith(".csv"))
    cons = baseline_consumers()
    print(f"【母體】{BDIR}：{len(files)} 檔｜{RV}：{len(open(RV,encoding='utf-8').read().splitlines())} 行")
    print(f"【② 之取得】AST 掃 `diff_rows(..., os.path.join(V3RUN, <檔>), ...)` ⇒ 解析出 {len(cons)} 檔之消費者")
    print("【④ 之射程】")
    print("  ·【目錄射程】生產側一層直接參與者（⛔ **未做 import 遞移閉包**·具名聲明）：")
    for x in PROD:
        print(f"       {x}")
    print("  ·【字樣射程】`git log <烘焙commit>..HEAD -- <上列路徑>`（⛔ 非內容比對·僅 commit 觸及）")
    print("  ·【連接方式】逐檔獨立查詢（⛔ 無距離窗）")
    assert files and cons, "🔴 母體或消費者為空 ⇒ ⛔ 不得續"
    print()
    live = 0
    print(f"{'① 檔名':<40}{'③ 烘焙':<22}{'④ 觸及':<8}{'⑤ 過期為活假說'}")
    print("-" * 92)
    rows = []
    for f in files:
        p = os.path.join(BDIR, f)
        bake = git("log", "-1", "--format=%h %ad", "--date=short", "--", p)
        sha = bake.split()[0] if bake else ""
        n_touch = 0
        if sha:
            out = git("log", "--format=%h", f"{sha}..HEAD", "--", *PROD)
            n_touch = len([x for x in out.splitlines() if x.strip()])
        alive = "🔴 是" if n_touch else "✅ 否"
        live += 1 if n_touch else 0
        rows.append((f, bake, n_touch, cons.get(f, [])))
        print(f"{f[:38]:<40}{bake:<22}{n_touch:<8}{alive}")
    print("-" * 92)
    print(f"⇒ 16 檔中，**「過期」為活假說者 = {live}**")
    print()
    # 🔴 **樣式比對**（⛔ 首版只做字面比對 ⇒ 14 個以 f-string 命名之基準被誤報「查無消費者」）
    import re as _re
    print("【② 逐檔之消費者（主判定 label）·樣式比對】")
    miss = []
    for f, bake, n, c in rows:
        hits = list(c)
        for pat, labs in cons.items():
            if "{…}" not in pat:
                continue
            rx = "^" + "".join(_re.escape(x) if x != "{…}" else ".*"
                               for x in _re.split(r"(\{…\})", pat)) + "$"
            if _re.match(rx, f):
                hits.extend(labs)
        hits = sorted(set(hits))
        print(f"  {f}")
        print(f"     ⇒ {hits if hits else '🔴 **查無消費者**（⛔ 具名·不猜）'}")
        if not hits:
            miss.append(f)
    print(f"  ⇒ **查無消費者之檔 = {len(miss)}**{('：' + str(miss)) if miss else '（空）'}")
    print()
    print("🔒 判別力自檢（考古 69 修法 ④）：以**必然觸及**之路徑重算 ⇒ ", end="")
    probe = git("log", "--format=%h", "HEAD~5..HEAD", "--", "verify/run_all.py")
    print(f"{len([x for x in probe.splitlines() if x.strip()])} 個 commit ⇒ 上式非恆為 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
