# -*- coding: utf-8 -*-
"""`W-G.9-268′` `c2`：`run_all` 名目差集（併線前必答 `3` ＋ 性質閘 `P-9`）。

🔒 **比較端 ＝ `S-5` 所記之期初態**（施工單 `§六 3` 逐字：⛔ 凍存名單之舊態）
   ＝ `verify/out/WG9268pR_runall_pre.log`（倉內·`c1` 併線前之 `off` 態實跑）。
🔒 **受測端** ＝ `c2` 態（旗標預設 `on`）之 `run_all` 落檔。

🔒 **框⛔ 自擬**：三分類一律用倉內既有器 `verify/wv_reconcile.py` 之
   `parse_log()` ＋ `classify()`（`W-G.9-7` 所立·KL 2026-08-11 裁）。

🔒 **`P-9` 之三類**（施工單 `§三` 逐字）
   `(i)`   本批所修者**轉綠**（期初 FAIL、期末⛔ FAIL）
   `(ii)`  **新可達之世代所新曝**之紅（⛔ 本批所致之迴歸）
   `(iii)` **真迴歸**（原可達且原綠而今紅）⇒ 🛑 **停機上呈**
   🛑 **紅之總數增減本身⛔ 為判準**（逐項歸類方為判準）。

🩸 `(ii)` 與 `(iii)` 之別繫於「該名目之受詞於期初是否**可達**」。
   本器**⛔ 自行臆斷**：以期初 `off` 態之**可達街廓集**為據機械分派，
   並將**無法機械歸類者**逐項具名為 `⛔ 可自動歸類` ⇒ **loud·候人工裁**。

用法：`python verify/probes/probe_WG9268p_c2_nameset.py <期初log> <期末log> [倉根]`
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))

import wv_reconcile as wv                                           # noqa: E402

PRE = sys.argv[1]
POST = sys.argv[2]

# 🔒 期初 `off` 態之可達街廓（本批 `probe_WG9268p_c2_gates.py` 實測·三軸見報告）
REACH_PRE = {"0m": {"R1", "R2"}, "3.5m": {"R1", "R2", "R4", "R5", "R6"}}
NEW_BLK = {"0m": {"R3", "R4", "R5", "R6"}, "3.5m": {"R3"}}


def main():                                                         # noqa: C901
    pre_t = io.open(PRE, encoding="utf-8", errors="replace").read()
    post_t = io.open(POST, encoding="utf-8", errors="replace").read()
    pre = wv.parse_log(pre_t)
    post = wv.parse_log(post_t)

    print("=" * 118)
    print("【`c2`】`run_all` 名目差集（併線前必答 `3` ＋ `P-9`）")
    print("=" * 118)
    print("三軸 (1) 期初 ＝ %s（%d B）" % (PRE, len(pre_t.encode("utf-8"))))
    print("         期末 ＝ %s（%d B）" % (POST, len(post_t.encode("utf-8"))))
    print("三軸 (2) 母體 ＝ 二 log 各自之 `🔴 FAIL` 名目集（`wv_reconcile.parse_log`）")
    print("三軸 (3) 粒度框 ＝ **名目**（⛔ 列數·⛔ 計數）")
    print()
    print("🔒 FAIL 名目數：期初 **%d** ／期末 **%d**" % (len(pre), len(post)))
    print("🛑 **紅之總數增減本身⛔ 為判準**（施工單 `P-9` 逐字）——判準為<u>逐項歸類</u>")
    print()

    res = wv.classify(pre, post)
    # 🩸 `wv.report()` 回 `(rc, 行清單)` 之 **tuple**（⛔ 字串）——⛔ 逕 `print` 之。
    _rc_rep, _lines = wv.report(res, title="`c2` 名目差集（期初 ⇒ 期末）")
    for _ln in _lines:
        print(_ln)
    print()

    only_pre = res["名目_僅凍存有"]      # 期初 FAIL、期末⛔ FAIL ⇒ 轉綠
    only_post = res["名目_僅現況有"]     # 期末新增之 FAIL

    print("=" * 118)
    print("【`P-9`】逐項歸類（⛔ 以總數增減為判準）")
    print("=" * 118)
    print()
    print("── 類 `(i)`　本批所修者**轉綠**（期初 FAIL ⇒ 期末⛔ FAIL）＝ **%d** 項"
          % len(only_pre))
    for nm in only_pre:
        print("   🟢 %s" % nm)
    print()

    cls_ii, cls_iii, unknown = [], [], []
    for nm in only_post:
        hit_new = sorted({b for tag, s in NEW_BLK.items() for b in s if b in nm})
        hit_old = sorted({b for tag, s in REACH_PRE.items() for b in s if b in nm})
        if hit_new and not hit_old:
            cls_ii.append((nm, hit_new))
        elif hit_old and not hit_new:
            cls_iii.append((nm, hit_old))
        else:
            unknown.append((nm, hit_new, hit_old))

    print("── 類 `(ii)`　**新可達之世代所新曝**之紅（⛔ 本批所致之迴歸）＝ **%d** 項"
          % len(cls_ii))
    for nm, b in cls_ii:
        print("   🟡 %s　〔新可達街廓 %s〕" % (nm, b))
    print()
    print("── 類 `(iii)`　**真迴歸**（原可達且原綠而今紅）＝ **%d** 項" % len(cls_iii))
    for nm, b in cls_iii:
        print("   🛑 %s　〔期初已可達 %s〕" % (nm, b))
    print()
    print("── ⛔ **可自動歸類**（loud·候人工裁·⛔ 靜默歸入任一類）＝ **%d** 項" % len(unknown))
    for nm, hn, ho in unknown:
        print("   ⚠️ %s　〔新可達命中 %s／期初可達命中 %s〕" % (nm, hn or "無", ho or "無"))
    print()

    print("=" * 118)
    if cls_iii:
        print("🛑 **停機款觸發**（施工單 `§八`）：類 `(iii)` 真迴歸 **非空**（%d 項）"
              % len(cls_iii))
        return 1
    if unknown:
        print("🟡 類 `(iii)` **機械歸類為空**，惟有 **%d** 項⛔ 可自動歸類 ⇒ **須人工逐項裁**"
              % len(unknown))
        print("   🛑 ⛔ 以本器之「類 `(iii)` 為空」逕報通過。")
        return 2
    print("✅ 類 `(iii)` 真迴歸 ＝ **空** ⇒ `P-9` 之停機款**未觸發**")
    print("=" * 118)
    return 0


if __name__ == "__main__":
    sys.exit(main())
