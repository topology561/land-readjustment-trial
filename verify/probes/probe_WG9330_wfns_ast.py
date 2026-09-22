# -*- coding: utf-8 -*-
"""發單側（窗二十五·唯讀·⛔ 零生產碼）：`GB-167` 之現態——`_WF_NS_NAMES`（AST 取值）對引擎經 `ns[...]` 取用之名。

用法：python probe_WG9330_wfns_ast.py <repo 絕對路徑>
🔒 成員數一律以 AST `literal_eval` 取值（`GB-167` 登記之攔法·⛔ 文字層括號配對）。
🔒 取用框 ＝ 引擎六檔之 `ns["名"]`／`ns['名']`（regex）；判別力：`_pool_strips_for_block` 須命中（必非零）。
rc：0 ＝ 無缺；3 ＝ 有缺（逐名列出）；6 ＝ 器紅（取不到 `_WF_NS_NAMES` 或判別力不成立）。
"""
import ast, os, re, sys
REPO = sys.argv[1]
ENGINE = ["verify/stepg_pipeline.py", "verify/wf_f0.py", "verify/wf_f1.py",
          "verify/wf_f2.py", "verify/wf_f3.py", "verify/wf_f4.py"]
src = open(os.path.join(REPO, "app.py"), encoding="utf-8").read()
names = None
for n in ast.walk(ast.parse(src)):
    if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets):
        if names is not None:
            print("🔴 器紅：`_WF_NS_NAMES` 賦值不只一處"); sys.exit(6)
        names = ast.literal_eval(n.value)
if not names:
    print("🔴 器紅：取不到 `_WF_NS_NAMES`"); sys.exit(6)
pat = re.compile(r'ns\[\s*["\']([A-Za-z_0-9]+)["\']\s*\]')
used = {}
for f in ENGINE:
    for m in pat.finditer(open(os.path.join(REPO, f), encoding="utf-8").read()):
        used.setdefault(m.group(1), set()).add(f)
if "_pool_strips_for_block" not in used:
    print("🔴 器紅：判別力不成立（`_pool_strips_for_block` 未命中）"); sys.exit(6)
missing = sorted(k for k in used if k not in names)
print("_WF_NS_NAMES 成員數（AST）＝", len(names), "／相異 ＝", len(set(names)))
print("引擎經 ns 取用之相異名 ＝", len(used))
for k in missing:
    print("缺：", k, "←", sorted(used[k]))
sys.exit(3 if missing else 0)
