# -*- coding: utf-8 -*-
"""`W-G.9-270` `p3` 之前置：以**間諜法**取 `run_verification.diff_rows` 之**全量違規列**。

🩸 **何以必須**：`run_verification.py:1497-1505` 逐字只印 `viol[:12]`，其餘以
   「另 N 列未顯示·本閘違規總計 N 列」帶過 ⇒ **逐格歸因⛔ 得自 log 取**
   （`CLAUDE.md` 之「引用違規列數須註明顯示數抑或總計數」即此族）。

🔒 **本器⛔ 改生產碼一字**——只在**本行程記憶體內**包裹 `rv.diff_rows`，
   其包裹**逕行委派原函式**並錄其 `(label, baseline_path, viol)`；
   🛑 **⛔ 改其回傳值** ⇒ 對 `run_verification` 之行為**逐位無影響**。

🛑 **`GB-162` 三禁令維持**：⛔ 設 `WV_BAKE`（本器**顯式斷言其未設**）／
   ⛔ 覆寫 `verify/baselines`（本器⛔ 任何寫入該目錄之路徑）／⛔ 併線 `p3a`。

🛑 **母體之可證（坑 `aj`）**：呼叫端須於本器之**前**跑 `rm -f verify/out/got_*`。
   本器於起跑前後各出艙 `got_*` 之檔數與 `mtime`。

用法：`python verify/probes/probe_WG9270_p3_spy.py`
產物：`verify/out/WG9270R_p3_viol.tsv`（`label <TAB> baseline_path <TAB> 違規列`）
`rc`：承 `rv.main()` 之 `rc`（⛔ 頂替）。
"""
import io
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, os.path.join(REPO, "verify", "fixtures"))

import run_verification as rv                                       # noqa: E402

OUTTSV = os.path.join(REPO, "verify", "out", "WG9270R_p3_viol.tsv")
REC = []

# 🛑 `GB-162`：顯式斷言 `WV_BAKE` **未設**（⛔ 靜默假定）
_bk = os.environ.get("WV_BAKE")
print("🔒 `WV_BAKE` 之現查 ＝ %r ⇒ %s" % (_bk, "✅ 未設" if not _bk else "🔴 已設 ⇒ 停"))
if _bk:
    sys.exit(9)

_gd = os.path.join(REPO, "verify", "out")
_pre = sorted(f for f in os.listdir(_gd) if f.startswith("got_"))
print("🔒 起跑前 `verify/out/got_*` ＝ **%d** 支（坑 `aj`：母體須可證）" % len(_pre))
_T0 = time.time()
print("🔒 起跑時刻 ＝ %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_T0)))

_orig_diff = rv.diff_rows


def _spy_diff(got_rows, baseline_path, key_cols, label, skip_cols=None):
    ok, viol = _orig_diff(got_rows, baseline_path, key_cols, label, skip_cols=skip_cols)
    REC.append({
        "label": str(label),
        "baseline": os.path.relpath(baseline_path, REPO).replace("\\", "/"),
        "key_cols": list(key_cols),
        "n": len(viol),
        "viol": list(viol),
    })
    return ok, viol            # 🛑 **逐位原樣回傳**（⛔ 改一字 ⇒ 行為無影響）


rv.diff_rows = _spy_diff

rc = rv.main()

# ── 產物落檔（`Write` 之外唯一之落檔·其內容為**機械產物**·⛔ 手寫）──────
with io.open(OUTTSV, "w", encoding="utf-8", newline="\n") as f:
    f.write("# W-G.9-270 p3：`diff_rows` 之全量違規列（間諜法·⛔ 改生產碼一字）\n")
    f.write("# 欄：label \\t baseline \\t key_cols \\t 違規列\n")
    for r in REC:
        for v in r["viol"]:
            f.write("%s\t%s\t%s\t%s\n"
                    % (r["label"], r["baseline"], "|".join(r["key_cols"]),
                       str(v).replace("\t", " ").replace("\n", " ")))

_post = sorted(f for f in os.listdir(_gd) if f.startswith("got_"))
_late = [f for f in _post
         if os.path.getmtime(os.path.join(_gd, f)) >= _T0 - 1.0]
print()
print("=" * 110)
print("🔒 收跑時刻 ＝ %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
print("🔒 收跑後 `got_*` ＝ **%d** 支；其 `mtime` **晚於起跑**者 ＝ **%d** 支 ⇒ %s"
      % (len(_post), len(_late), "✅ 母體可證" if len(_late) == len(_post)
         else "🔴 有檔非本次所寫 ⇒ 坑 `aj`"))
print("🔒 `diff_rows` 之呼叫 ＝ **%d** 次｜違規列總計 ＝ **%d** 列"
      % (len(REC), sum(r["n"] for r in REC)))
print("🔒 產物 ＝ `%s`（%d B）"
      % (os.path.relpath(OUTTSV, REPO).replace("\\", "/"),
         os.path.getsize(OUTTSV)))
print("🛑 `verify/baselines` **未被寫入**——本器⛔ 任何寫入該目錄之路徑；"
      "其樹之復驗由呼叫端以 `git status` ⋀ 逐檔 `sha256` 為之。")
print("=" * 110)
sys.exit(rc if isinstance(rc, int) else 0)
