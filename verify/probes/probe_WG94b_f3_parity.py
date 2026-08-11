# -*- coding: utf-8 -*-
"""`W-G.9-4b` `F3` 對拍探針：**受限 ns 路徑**之引擎輸出，鍵 ＝ (情境 × 街廓 × 側別)。

## 為何是這個觀測量（⛔ 非「隨手挑一個能比的」）

`F3` 原式為「修復後 app 路徑之七級調配**可完成**，其輸出與 `6ab9e86` 相同」。
但**既有另案**（`v3·StepG0m`／`v3·StepG3.5m`「結構閘/看守觸發」·見
`verify/out/WG94_runall.log`）使 `run_step_g` 於**兩情境皆** raise
⇒ 「可完成」在本倉態下**不可能成立**，且該 raise **先於本批存在**。

⇒ 本探針改取**可達之最深觀測量**：`run_step_g`（餵 `_wf_ns()` 之受限 ns）
之**全部 stdout ＋ 終止例外**，逐 (情境 × 街廓 × 側別) 分桶取 md5。
該輸出含真實生產數（`理論@k*`／`實跑`／`Δ`／逐界面 `W_far`/`W_near`／
`[T2-DIAG]` 之池帶面積與覆蓋殘差／`[配餘]` 之入抵費地量）
⇒ **若二版逐桶 md5 全等，則生產行為於可達範圍內未變**。

⛔ **不用宗序號為鍵**（施工單 §6 閘 2）；`暫編地號` 僅作桶內資料。
⛔ **不以 `harvest()` 全 globals 之結果充證**（施工單 §6 閘 3）——ns 一律取 `_wf_ns()`。

## 用法
    python verify/probes/probe_WG94b_f3_parity.py <標籤>
        <標籤> ＝ 輸出檔名之後綴（如 `HEAD` / `6ab9e86`）
輸出：`verify/out/probe_WG94b_f3_parity_<標籤>.log`（摘要＋逐桶 md5）
      `verify/out/probe_WG94b_f3_parity_<標籤>.raw`（正規化全文·供逐位元 diff）
"""
import hashlib
import io
import os
import re
import sys
import traceback
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

TAGS = (("0m", 0.0), ("3.5m", 3.5))
SIDE_TOKENS = (("left", ("left", "左")), ("right", ("right", "右")))


def normalize(text):
    """去除與**版本無關**之環境噪音：絕對路徑、行號。⛔ 不觸任何數值。"""
    t = text.replace("\r\n", "\n").replace("\\", "/")
    t = re.sub(r"[A-Za-z]:/[^\s\"']*/(?=(verify|app\.py|data)/)", "", t)
    t = re.sub(r"(stepg_pipeline\.py|app\.py|wf_f\d\.py):\d+", r"\1:<行號>", t)
    return t


def bucket(lines, tag, labels):
    """逐行分桶：鍵 ＝ (情境, 街廓, 側別)。⛔ 一行可落多桶（同時提及塊與側）。
    未提及街廓者入 `(tag, '—', '—')`；提及街廓未提側別者入 `(tag, blk, '—')`。"""
    out = {}
    for ln in lines:
        blks = [b for b in labels if b in ln] or ["—"]
        sides = [s for s, toks in SIDE_TOKENS if any(t in ln for t in toks)] or ["—"]
        for b in blks:
            for s in sides:
                out.setdefault((tag, b, s), []).append(ln)
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    label = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g

    snapshot = rv.load_snapshot()
    ns_full, fake_st = harvest()
    ns_app = ns_full["_wf_ns"]()                     # ⇦ **受限 ns**（施工單 §6 閘 3）
    L = [f"# `W-G.9-4b` `F3` 對拍｜標籤 ＝ {label}",
         f"  `_wf_ns()` 受限 ns 名目數 ＝ {len(ns_app)}",
         f"  `k956_W_from_mp` ∈ 受限 ns ⇒ {'k956_W_from_mp' in ns_app}", ""]
    raw_all, buckets = [], {}

    for tag, setback in TAGS:
        cb_by, cad = rv.build_pipeline(ns_full, fake_st, snapshot)
        params = rv.build_param_table(ns_full, fake_st, cb_by, cad, snapshot, setback)
        build_ownership(ns_full, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(
            ns_full, fake_st, v6, list(cb_by.values()), snapshot)
        _d, _s, _o, winners, forced = run_corner_pk(
            ns_full, fake_st, list(cb_by.values()), cad, params, temp, build,
            setback, snapshot=snapshot)

        cap = io.StringIO()
        outcome = "未拋（完整跑完）"
        with redirect_stdout(cap):
            try:
                run_step_g(ns_app, fake_st, list(cb_by.values()), cad, snapshot,
                           params, build, winners, forced, setback)
            except BaseException as e:               # ⛔ 不吞：型別＋訊息全入輸出
                tb = traceback.extract_tb(sys.exc_info()[2])[-1]
                outcome = (f"{type(e).__name__} @ "
                           f"{os.path.basename(tb.filename)}:{tb.lineno}｜{e}")
        body = normalize(cap.getvalue() + f"\n[終止] {normalize(outcome)}\n")
        lines = [x for x in body.split("\n") if x.strip()]
        labels = sorted(cb_by.keys())
        buckets.update(bucket(lines, tag, labels))
        raw_all.append(f"===== 情境 {tag} =====\n" + body)
        L.append(f"## 情境 {tag}｜街廓 {len(labels)} 塊｜輸出 {len(lines)} 行")
        L.append(f"   終止 ＝ {normalize(outcome)}")
        L.append("")

    L.append("## 逐桶 md5（鍵 ＝ 情境 × 街廓 × 側別）")
    L.append(f"{'情境':<6}{'街廓':<6}{'側別':<7}{'行數':>5}  md5(前12)")
    L.append("-" * 56)
    for k in sorted(buckets):
        blob = "\n".join(buckets[k]).encode("utf-8")
        L.append(f"{k[0]:<6}{k[1]:<6}{k[2]:<7}{len(buckets[k]):>5}  "
                 f"{hashlib.md5(blob).hexdigest()[:12]}")
    L.append("-" * 56)
    L.append(f"桶數 ＝ {len(buckets)}")
    whole = "\n".join(raw_all)
    L.append(f"**全文 md5 ＝ {hashlib.md5(whole.encode('utf-8')).hexdigest()}**")

    os.makedirs(os.path.join(VERIFY, "out"), exist_ok=True)
    base = os.path.join(VERIFY, "out", f"probe_WG94b_f3_parity_{label}")
    with open(base + ".log", "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    with open(base + ".raw", "w", encoding="utf-8") as f:
        f.write(whole)
    print("\n".join(L))
    print(f"\n[log] {os.path.relpath(base + '.log', REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
