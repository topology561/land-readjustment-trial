#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-159**：`_projection_order` **十二呼叫點之母體實測**（`GB-105` 落地之前置）。

## 受詞

施工單 `W-G.9-159` `§二` 將十二點歸為**五類**，並於 `L-3` 令每點斷言
「**實參 ≡ `filter(BASE)`**」（`④` 改為 `_mem ⊆ BASE`）。
本檔**只讀**量測該五類之歸屬是否成立，**⛔ 不寫任何斷言、⛔ 不改任何生產碼**。

## 法

包住 `ns["_projection_order"]`（`ns is _projection_order.__globals__` ⇒ 亦攔得到
`app.py` 內部直呼·`W-G.9-147R` 已證），再驅動 `run_verification.main()`。
`BASE(blk)` 取自**類 ① 之實參**（`selection_pipeline.py:339` ＝ `by_blk.get(_lbl, [])`）
——⛔ 非另行重建，故⛔ 無「重建錯了」之風險。

🩸 **量測器紅之自捕（⛔ 非受詞紅·常規五）**：首版以 `contextlib.redirect_stdout(StringIO)`
收 `rv.main()` 之輸出，而該函式呼叫 `sys.stdout.reconfigure(...)`（`StringIO` 無該法）
⇒ `AttributeError` ⇒ `REC` 為 `0` 筆。改由 shell 之 `>` 收其輸出後方得 `72` 筆。

## 重跑

    PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9159_projorder_pop.py

`rc` 恆為 `0`。⚠️ 本檔會驅動 `run_verification`（**會寫 `verify/out/**`**·`GB-94`）
⇒ **須於拋棄式 clone 內跑**。
"""
import collections
import inspect
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # verify/probes
VERIFY = os.path.dirname(HERE)                              # verify
REPO = os.path.dirname(VERIFY)                              # 倉根（⛔ 不寫死絕對路徑）
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "2d72de3"                     # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD）
sys.path.insert(0, VERIFY)

REC = []
L = []


def say(s=""):
    print(s, flush=True)
    L.append(s)


def install(ns):
    orig = ns["_projection_order"]
    if getattr(orig, "_wg159_wrapped", False):
        return
    say("  🔒 量測器自檢①　`ns is _projection_order.__globals__` ＝ **%s**（須 True）"
        % (ns is orig.__globals__))

    def wrapped(parcels, p1, p2, *a, **k):
        try:
            fr = inspect.stack()[1]
            site = "%s:%d" % (os.path.basename(fr.filename), fr.lineno)
        except Exception:                                   # noqa: BLE001
            site = "<unknown>"
        try:
            lst = list(parcels)
            REC.append({
                "site": site, "n": len(lst),
                "ids": [tp.get("暫編地號") for tp in lst],
                "blks": sorted({tp.get("所屬街廓") for tp in lst}),
                "nkeys": len(lst[0].keys()) if lst else 0,
                "n_ghost": sum(1 for tp in lst if tp.get("_is_ghost_sliver")),
                "n_stage": sum(1 for tp in lst if "配地階段" in tp),
            })
        except Exception as e:                              # noqa: BLE001
            REC.append({"site": site, "err": repr(e)[:120]})
        return orig(parcels, p1, p2, *a, **k)

    wrapped._wg159_wrapped = True
    ns["_projection_order"] = wrapped


def main():                                                 # noqa: C901
    sys.stdout.reconfigure(encoding="utf-8")
    W = 104
    say("=" * W)
    say("【W-G.9-159】`_projection_order` 十二呼叫點之**母體實測**（`GB-105` 落地前置）")
    say("=" * W)
    say("  HEAD        = %s" % subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True,
        check=True).stdout.decode().strip())
    say("  app.py blob = %s" % subprocess.run(
        ["git", "rev-parse", "HEAD:app.py"], cwd=REPO, capture_output=True,
        check=True).stdout.decode().strip())
    say("  基座(log 綁) = %s" % BASE_REF)
    say("")

    import run_verification as rv
    _orig_h = rv.harvest

    def _patched():
        ns, st = _orig_h()
        install(ns)
        return ns, st

    rv.harvest = _patched
    say("── 以下為 `run_verification.main()` 之輸出（⛔ 未 redirect·見檔頭 🩸）──")
    rc = 1
    try:
        rc = rv.main()
    except SystemExit as e:                                 # noqa: BLE001
        rc = int(getattr(e, "code", 1) or 0)
    except Exception as e:                                  # noqa: BLE001
        say("🔴 run_verification 例外：%r" % (e,))
    say("── `run_verification` rc ＝ %s ──" % rc)
    say("")

    say("=" * W)
    say("§A　觀測到之呼叫點與次數（🔒 母體 ＝ 本次 `run_verification` 之全部呼叫）")
    say("=" * W)
    c = collections.Counter(r["site"] for r in REC)
    for s, n in sorted(c.items()):
        say("  %-42s 呼叫 %d 次" % (s, n))
    say("  合計 %d 次／相異呼叫點 %d 個" % (len(REC), len(c)))
    say("")
    say("  🔴 **十二點中僅 %d 點被觀測**——`run_verification` 於 trunk A 之" % len(c))
    say("     `②-宗 圍堵閘破[R2]` 即中止 ⇒ `wf_f0`〜`wf_f4` **從未執行**；")
    say("     `app.py:18913` 在 `main()` 內（`CLAUDE.md` 逐字：**從不被 `run_all` 執行**）。")
    say("     ⇒ 其餘各點之歸類只能**靜態**認定（見 `§D`），⛔ 非「不存在」。")
    say("")

    BASE = {}
    for r in REC:
        if r.get("site", "").endswith("selection_pipeline.py:339") and len(r.get("blks", [])) == 1:
            BASE.setdefault(r["blks"][0], set()).update(r["ids"])
    say("=" * W)
    say("§B　`BASE(blk)`（🔒 取自**類 ① 之實參**＝ `by_blk.get(_lbl, [])`·⛔ 非另行重建）")
    say("=" * W)
    for k in sorted(BASE):
        say("  %-4s |BASE| = %-3d  %s" % (k, len(BASE[k]), sorted(BASE[k])))
    say("")

    say("=" * W)
    say("§C　逐類之關係實測")
    say("=" * W)
    S1 = {}
    for r in REC:
        if r.get("site", "").endswith("stepg_pipeline.py:499") and len(r.get("blks", [])) == 1:
            S1.setdefault(r["blks"][0], set()).update(r["ids"])
    P5 = {}
    for r in REC:
        if r.get("site", "").endswith(":7731") and len(r.get("blks", [])) == 1:
            P5.setdefault(r["blks"][0], set()).update(r["ids"])

    say("── 類 ② `stage1` vs `BASE`（單稱 `stage1(BASE)`）──")
    ok2 = 0
    for blk in sorted(BASE):
        a, b = BASE[blk], S1.get(blk, set())
        good = b <= a
        ok2 += good
        say("  %-4s |BASE|=%-3d |stage1|=%-3d  `stage1 ⊆ BASE` ＝ %-5s  只在 BASE ＝ %s"
            % (blk, len(a), len(b), good, sorted(a - b)))
    say("  ⇒ **%d/%d** 成立。⚠️ `R3`〜`R6` 之 `stage1` 為空（該情境未走到）⇒ ⊆ **空真**。"
        % (ok2, len(BASE)))
    say("")

    say("── 類 ⑤ `app.py:7731` vs 類 ② `stepg:499`（單 `§二` 稱 `passthrough(stage1)`）──")
    for blk in sorted(P5):
        say("  %-4s |7731|=%-3d |stepg|=%-3d  **逐位相同** ＝ %s"
            % (blk, len(P5[blk]), len(S1.get(blk, set())), P5[blk] == S1.get(blk, set())))
    say("")

    say("── 🔴 類 ④ `_mem`（`app.py:11396`） vs `BASE(該街廓)`（單 `L-3` 令斷言 `⊆`）──")
    seen, bad = set(), 0
    for r in REC:
        if not r.get("site", "").endswith(":11396"):
            continue
        blk = r["blks"][0] if len(r["blks"]) == 1 else str(tuple(r["blks"]))
        key = (blk, tuple(r["ids"]))
        if key in seen:
            continue
        seen.add(key)
        extra = [i for i in r["ids"] if i not in BASE.get(blk, set())]
        bad += bool(extra)
        say("  %-4s n=%d  ids=%-46s ⊆BASE ＝ %-5s  只在 `_mem` ＝ %s"
            % (blk, r["n"], str(r["ids"])[:46], not extra, extra))
    say("  ⇒ 🔴 **違反 `⊆` 之相異呼叫 ＝ %d／%d（全數）**" % (bad, len(seen)))
    say("")

    say("=" * W)
    say("§D　十二點之**靜態**分類（實參符號·逐行自檔案抽取）")
    say("=" * W)
    SITES = [("app.py", 7731), ("app.py", 11396), ("app.py", 18913),
             ("verify/selection_pipeline.py", 339), ("verify/stepg_pipeline.py", 499),
             ("verify/wf_f0.py", 256), ("verify/wf_f1.py", 376), ("verify/wf_f2.py", 95),
             ("verify/wf_f3.py", 78), ("verify/wf_f4.py", 1043),
             ("verify/wf_f4.py", 1433), ("verify/wf_f4.py", 1503)]
    for f, n in SITES:
        ln = open(os.path.join(REPO, f), encoding="utf-8").read().split("\n")[n - 1]
        say("  %-30s:%-5d %s" % (f, n, ln.strip()[:88]))
    say("")
    say("  🔒 `pseudo` 三處之構造（`wf_f1:374-375`／`wf_f4:1431-1432`／`:1501-1502`）皆為")
    say("     `[{\"暫編地號\": k, \"polygon_coords\": list(v.exterior.coords)} for k, v in <polys>.items()]`")
    say("     ⇒ **合成 dict·僅二鍵·其 `polygon_coords` 係<u>重整後</u>之幾何**")
    say("     ⇒ 🔴 **⛔ 非 `BASE` 之任何濾式**（`BASE` 之元素有 14〜16 鍵·且幾何為重整<u>前</u>）。")
    say("")

    os.makedirs(OUTDIR, exist_ok=True)
    lg = os.path.join(OUTDIR, "probe_WG9159_projorder_pop_%s.log" % BASE_REF)
    with open(lg, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(L) + "\n")
    js = os.path.join(OUTDIR, "probe_WG9159_projorder_pop_%s.json" % BASE_REF)
    json.dump(REC, open(js, "w", encoding="utf-8"), ensure_ascii=False)
    print("\n  log → %s" % os.path.relpath(lg, REPO))
    print("  raw → %s" % os.path.relpath(js, REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
