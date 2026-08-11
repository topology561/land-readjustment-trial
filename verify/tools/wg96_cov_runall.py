# -*- coding: utf-8 -*-
"""`W-G.9-6` `Q1`：以**行覆蓋**跑一次完整 `run_all`，母體 ＝ `verify/run_verification.py`。

## 工具與其足夠性（⛔ 施工單 §2-1 要求寫明）

`coverage.py` 於本機**不可得**（`ModuleNotFoundError`）；⛔ 本批不安裝套件。
改採 **stdlib `sys.monitoring`**（Python 3.13.11）之 `LINE` 事件。

**為何足以支撐本命題**：`G1` 之命題為「**某行執行次數為 0**」——`LINE` 事件由
直譯器於**每一行執行時**直接觸發，其產生之「已執行行號 → 次數」即為該命題之
**直接觀測量**。`coverage.py` 7.x 於 Python ≥3.12 亦以同一機制取行覆蓋
⇒ 二者對**本命題**等價（⛔ 不主張在分支覆蓋等其他命題上等價）。

## 🔴 射程（⛔ 正面寫·非附註）

1. **subprocess 段不在射程內**：`run_all` 之末端夾具等以 `subprocess` 起，
   子進程**不受本監控追蹤**。射程僅及**同進程執行之 `run_verification.py`**
   （`run_all.py:261` `import run_verification as v` ／ `:268` `rc2 = v.main()`）。
2. **行覆蓋只能證「未執行」，⛔ 不能證「執行了就有在守」**——執行了但**恆真**之閘
   同樣不守任何事。**本批⛔ 不量恆真性**。
3. **母體限 `run_verification.py`**；`app.py`／`wf_f*.py`／`stepg_pipeline.py`
   之內部斷言**不在母體內**。

## 計數上限（⛔ 具名·非靜默截斷）

每行計數達 `CAP`（預設 1000）即對該位置 `DISABLE`，其後不再計數 ⇒ 該行記為 `>=CAP`。
**理由**：本命題只需區辨 `0` 與 `>0`；不設上限則熱迴圈之逐行回呼會使長跑不可控。
⇒ 輸出中 `>=CAP` 之列**已正面標示**，⛔ 不得讀成精確次數。

## 重跑
    python verify/tools/wg96_cov_runall.py > verify/out/WG96_runall_cov.log 2>&1
輸出：`verify/out/WG96_coverage.txt`（行號 → 次數 ／ 未執行行清單）
"""
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

TARGET = os.path.abspath(os.path.join(VERIFY, "run_verification.py"))
RUN_ALL = os.path.abspath(os.path.join(VERIFY, "run_all.py"))
OUT = os.path.join(VERIFY, "out", "WG96_coverage.txt")
CAP = 1000

mon = sys.monitoring
TOOL = mon.PROFILER_ID
counts = {}


def _line(code, lineno):
    if code.co_filename != TARGET:
        return mon.DISABLE                      # 非母體：永久停用該位置（零殘餘成本）
    c = counts.get(lineno, 0) + 1
    counts[lineno] = c
    if c >= CAP:
        return mon.DISABLE                      # 達上限：停用，該行記為 >=CAP
    return None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"[WG96-cov] 工具＝sys.monitoring（Python {sys.version.split()[0]}）"
          f"｜母體＝{os.path.relpath(TARGET, REPO)}｜CAP={CAP}")
    print(f"[WG96-cov] ⚠️ 射程：subprocess 子進程**不在**射程內；"
          f"行覆蓋⛔**不能**證「執行了就有在守」（恆真性未涵蓋）")
    mon.use_tool_id(TOOL, "wg96")
    mon.register_callback(TOOL, mon.events.LINE, _line)
    mon.set_events(TOOL, mon.events.LINE)
    rc = 0
    try:
        runpy.run_path(RUN_ALL, run_name="__main__")
    except SystemExit as e:
        rc = int(e.code or 0)
    finally:
        mon.set_events(TOOL, 0)
        mon.register_callback(TOOL, mon.events.LINE, None)
        mon.free_tool_id(TOOL)

    src = open(TARGET, encoding="utf-8").read().splitlines()
    n = len(src)
    executed = sorted(counts)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(f"# W-G.9-6 Q1 行覆蓋｜母體={os.path.relpath(TARGET, REPO)}"
                f"｜總行數={n}｜CAP={CAP}\n")
        f.write(f"# 工具=sys.monitoring LINE（Python {sys.version.split()[0]}）"
                f"｜run_all rc={rc}\n")
        f.write("# ⚠️ 射程：subprocess 子進程不在射程內；行覆蓋不量恆真性\n")
        f.write(f"# 已執行行數={len(executed)}\n")
        f.write("#\n# lineno\tcount\n")
        for ln in executed:
            c = counts[ln]
            f.write(f"{ln}\t{'>=%d' % CAP if c >= CAP else c}\n")
    print(f"[WG96-cov] run_all rc={rc}｜已執行行數={len(executed)} / 檔總行數={n}")
    print(f"[WG96-cov] 覆蓋表 → {os.path.relpath(OUT, REPO)}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
