# -*- coding: utf-8 -*-
"""
B6 — 真 vs 匿名 歸戶同構縮小版（街角候選宗地限定；遷移前最後把關）。

KL 裁示規程（2026-07-05）：
  - 真地籍檔全程留本機、**只讀**、不進 repo（本腳本不寫任何真資料衍生檔）。
  - 產出僅 verify/out/b6_report.md：候選筆數、同構 True/False、群組數對比等
    **結論性數字，零 PII**（絕不列人名/統編；指紋本身不落地）。
  - 預期 True（全案 21,476 群已證同構）；此為流程把關、非探索。

方法：
  1. harness 標準管線（匿名檔）→ build_parcels ∩ ownership → 街角候選宗地之原地號集。
  2. 對 真/匿名 兩檔各跑一次 build_ownership（同一份 tab1 複刻碼）。
  3. 比對（限縮在候選宗地集）：
     a. Gxxx 逐筆相同？（定理鏈預期全同）
     b. 歸戶劃分同構？（把候選宗地依 gid 分組 → 兩邊 partition 是否為同一組集合）
  4. dtype 嫌犯 1.5 註記：真檔統編若為數字型，指紋字串會帶 '.0' 形式差 →
     指紋文字不同「不影響」劃分同構（檔內一致）；本腳本只比 partition/Gxxx，不比指紋原文。

用法：python verify/b6_isomorphism.py [真檔路徑]
"""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from app_harvest import harvest                      # noqa: E402
from selection_pipeline import (                     # noqa: E402
    build_ownership, build_build_parcels, OWNERSHIP_TARGETS)
import run_verification as rv                        # noqa: E402

ANON_XLSX = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
REAL_XLSX_DEFAULT = os.path.join(REPO, "data", "地籍資料來源_花蓮單一7_文中2-3.xlsx")
REPORT = os.path.join(HERE, "out", "b6_report.md")


def _partition(own_map, parcels):
    """候選宗地依 gid 分組 → frozenset of frozensets（地號）。無 gid 者單獨列出。"""
    by_gid = {}
    missing = []
    for p in parcels:
        gid = own_map.get(p, "")
        if not gid:
            missing.append(p)
            continue
        by_gid.setdefault(gid, set()).add(p)
    return frozenset(frozenset(v) for v in by_gid.values()), by_gid, missing


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    real_path = sys.argv[1] if len(sys.argv) > 1 else REAL_XLSX_DEFAULT
    if not os.path.exists(real_path):
        print(f"🔴 真檔不存在：{real_path}"); return 1

    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)

    # ── 匿名側（harness 標準路徑；同時定義候選宗地集） ──
    own_anon = build_ownership(ns, fake_st, ANON_XLSX)
    anon_map = dict(fake_st.session_state["t8_ownership_map"])
    with open(rv.V6DXF, "rb") as f:
        v6_raw = f.read()
    temp_parcels, build_parcels, _sw = build_build_parcels(
        ns, fake_st, v6_raw, list(cb_by.values()), snapshot)
    cand_parents = sorted({tp["原地號"] for tp in build_parcels
                           if anon_map.get(tp["原地號"], "")})

    # ── 真側（同一份複刻碼、只讀） ──
    own_real = build_ownership(ns, fake_st, real_path)
    real_map = dict(fake_st.session_state["t8_ownership_map"])
    # 還原匿名 map 回 session（避免後續誤用真側狀態）
    fake_st.session_state["t8_ownership_map"] = anon_map

    # ── 比對（限縮候選宗地集；零 PII） ──
    part_anon, by_anon, miss_anon = _partition(anon_map, cand_parents)
    part_real, by_real, miss_real = _partition(real_map, cand_parents)
    iso = (part_anon == part_real)
    gxxx_same = [p for p in cand_parents if anon_map.get(p) == real_map.get(p)]
    gxxx_diff = [p for p in cand_parents if anon_map.get(p) != real_map.get(p)]
    targets_real_ok = all(real_map.get(ln) == exp for ln, exp in OWNERSHIP_TARGETS.items())

    lines = [
        "# B6 — 真 vs 匿名 歸戶同構縮小版（街角候選宗地限定）",
        "",
        f"- 執行：2026-07-05（W-V 選位半綠後、Phase A 前最後把關）",
        f"- 真檔：`{os.path.basename(real_path)}`（本機只讀、不進 repo）｜"
        f"匿名檔：`{os.path.basename(ANON_XLSX)}`",
        "",
        "## 兩側 ownership 概要",
        "",
        "| 側 | 重劃區地籍 | U_LAND | 對應失敗 | 歸戶群組數 |",
        "|---|---|---|---|---|",
        f"| 匿名 | {own_anon['n_rezoning']} | {own_anon['n_uland']} | "
        f"{own_anon['n_fail']} | {own_anon['n_groups']} |",
        f"| 真 | {own_real['n_rezoning']} | {own_real['n_uland']} | "
        f"{own_real['n_fail']} | {own_real['n_groups']} |",
        "",
        "## 同構判定（限縮：街角候選宗地）",
        "",
        f"- 街角候選宗地（原地號，去重）：**{len(cand_parents)} 筆**",
        f"- 兩側皆有歸戶之候選：匿名缺 {len(miss_anon)}、真缺 {len(miss_real)}",
        f"- **Gxxx 逐筆相同：{len(gxxx_same)}/{len(cand_parents)}**"
        + ("" if not gxxx_diff else f"（相異地號：{', '.join(gxxx_diff)}）"),
        f"- **歸戶劃分同構（partition 相等）：{iso}**",
        f"- 候選集內群組數：匿名 {len(by_anon)}、真 {len(by_real)}",
        f"- 靶組（G005/G007/G009/G019/G023/G029）於**真檔**重現：{targets_real_ok}",
        "",
        "## 結論",
        "",
        ("✅ **同構成立**：真/匿名兩側對街角候選宗地之歸戶劃分完全一致、Gxxx 逐筆相同 → "
         "匿名化因素自嫌犯清單**排除**（README 嫌犯序 3 永久封閉）；Phase A 遷移把關通過。"
         if (iso and not gxxx_diff) else
         "🔴 **同構不成立** → 停：依 Gxxx 全等定理鏈反查三環（列序/指紋複刻/迭代起點），交 KL 仲裁。"),
        "",
        "> 註（dtype 嫌犯 1.5）：真檔法人統編若為數字型，指紋**原文**可帶 `.0` 形式差；"
        "檔內一致故不影響劃分同構。本報告只比 partition 與 Gxxx，不落地任何指紋原文（零 PII）。",
        "",
    ]
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))
    print(f"\n報告 → {REPORT}")
    return 0 if (iso and not gxxx_diff) else 1


if __name__ == "__main__":
    sys.exit(main())
