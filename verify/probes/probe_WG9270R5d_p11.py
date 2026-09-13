# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令六 `§四-3`：**`p11` —— 待落地清單與依賴序之現態出艙**。

🛑 **⛔ 提落地之順序主張、⛔ 動任何碼、⛔ 判任何項之優先**——**出艙即止**（`§四-3` 款 `4`）。
🛑 **⛔ 以「已讀過」代「已執行」**——四子項逐項以**逐字**證其在否（款 `3`）。
🔒 **⛔ 以行號為錨**（`自誤 372`／`374`：錨只能是逐字）——行號僅作導引，逐字為錨。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9270R5d_p11.py`
`rc`：`0` 量測成立／`5` 量測器紅（對照組未如期）。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
os.chdir(REPO)

W = 108
K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
CLA = "CLAUDE.md"
GBT = "docs/reports/W-G.4_泛用阻塞項登記表.md"


def hr(t=""):
    print("\n── %s %s" % (t, "─" * max(0, W - len(t) - 4)))


def lines(p):
    return io.open(p, encoding="utf-8").read().split("\n")


def cnt(p, s):
    return sum(1 for L in lines(p) if s in L)


def show(p, s, limit=None, label=""):
    """逐字錨之命中（行號僅作導引·⛔ 為錨）"""
    hits = [(i, L) for i, L in enumerate(lines(p), 1) if s in L]
    print("   %-36s 命中 %3d  （%s）" % (label or repr(s)[:36], len(hits), p.split("/")[-1]))
    for i, L in (hits[:limit] if limit else hits):
        print("     · 導引 :%d  %s" % (i, L.strip()[:150]))
    return hits


def main():
    rc = 0
    print("=" * W)
    print("【`W-G.9-270` 補令六 `§四-3`】**`p11` —— 待落地清單與依賴序之現態出艙**")
    print("=" * W)
    print("🛑 ⛔ 提落地之順序主張、⛔ 動任何碼、⛔ 判任何項之優先——出艙即止。")

    # ── 款 1：`3′` 一項之逐字 ───────────────────────────────────────
    hr("款 `1`　`W-G.4_泛用阻塞項登記表` 檔尾之 `3′` 一項（逐字）")
    h3 = show(GBT, "`3′`", label="逐字錨 `3′`")
    if not h3:
        h3 = show(GBT, "3′", label="寬字樣 3′")
    print("   判別力（寬字樣 `依賴序`·須非 0）＝ %d" % cnt(GBT, "依賴序"))

    # ── 款 2：CLAUDE.md 之 ⬜ 清單（二框並報）─────────────────────
    hr("款 `2`　`CLAUDE.md` 之 `⬜` 清單（**二框並報**·逐項 `檔:逐字錨`·⛔ 行號為錨）")
    narrow = [(i, L) for i, L in enumerate(lines(CLA), 1) if "⬜ **未落地**" in L]
    wide = [(i, L) for i, L in enumerate(lines(CLA), 1) if "⬜" in L]
    print("   窄框 `⬜ **未落地**` ＝ %d 列 ／ 寬框 `⬜` ＝ %d 列" % (len(narrow), len(wide)))
    print("   🛑 二數相異 ⇒ **⛔ 以其一代另一**（`VR-091 一`：計數須同格載其框）")
    print("\n   **寬框 `⬜` 之逐列**（行號僅作導引）")
    for i, L in wide:
        print("     · :%d  %s" % (i, L.strip()[:170]))
    # 對照組（必命中／必為零）
    c_ok = cnt(CLA, "待落地")
    neg = "⬜" + "NOSUCH" + str(7 * 13)
    c_ng = cnt(CLA, neg)
    print("\n   對照組：必命中 `待落地` ＝ %d（須 >0）／必為零（執行期組出）＝ %d（須 0）" % (c_ok, c_ng))
    if c_ok == 0 or c_ng != 0:
        print("   🔴 **量測器紅** ⇒ ⛔ 出艙本節任何計數")
        rc = 5

    # ── 款 3：K-9-29 碼側落地之四子項 ─────────────────────────────
    hr("款 `3`　`K-9-29` 碼側落地之**四子項**之現態（逐項以<u>逐字</u>證其在否）")

    print("\n   **子項 `1`　`app.py` 之 `k6_step0_merge` 呼叫（KL 已令廢）**")
    a1 = show("app.py", "temp_parcels, _diag_k6 = k6_step0_merge(",
              label="逐字錨（呼叫點）")
    print("     判別力（寬字樣 `k6_step0_merge` @ app.py·須 >1）＝ %d" % cnt("app.py", "k6_step0_merge"))
    print("     ⇒ 🔴 **仍在**（命中 %d）" % len(a1) if a1 else "     ⇒ 🟢 已撤")

    print("\n   **子項 `2`　`wf_f0` 之 `Σa` vs `a + a′`**")
    for s, lab in (("a′", "`a′` 字樣"), ("Σa", "`Σa` 字樣"),
                   ("a + a", "`a + a` 字樣"), ("_mina_by_block", "`_mina_by_block`")):
        print("     %-18s @ verify/wf_f0.py 命中 %d" % (lab, cnt("verify/wf_f0.py", s)))
    print("     🛑 **⛔ 由字樣命中逕判其已否落地**——僅出艙字樣之在否（`§四-3` 款 `3`）。")

    print("\n   **子項 `3`　步驟 D 是否逐筆**")
    for s in ("步驟 D", "步驟D", "逐筆"):
        for f in ("app.py", "verify/wf_f0.py", "verify/stepg_pipeline.py"):
            print("     `%s` @ %-28s 命中 %d" % (s, f, cnt(f, s)))

    print("\n   **子項 `4`　入池閘是否存在**")
    for s in ("入池閘", "入池"):
        for f in ("app.py", "verify/wf_f0.py", "verify/wf_f4.py", "verify/stepg_pipeline.py"):
            print("     `%s` @ %-28s 命中 %d" % (s, f, cnt(f, s)))
    print("     對照組（必命中·證器非紅）：`調配池` @ app.py ＝ %d" % cnt("app.py", "調配池"))
    if cnt("app.py", "調配池") == 0:
        print("     🔴 **量測器紅**")
        rc = 5

    # ── K-9-29 之裁與其款之逐字（供對位）─────────────────────────
    hr("附　`K-9-29` 之相關款之逐字（供對位·⛔ 改寫）")
    show(K6, "🔒 **二（廢前置合併）**", label="款 `二`（廢止）")
    show(K6, "步驟 0 之 `9` 組／`13` 宗解併", label="款 `八`（土地後果）")
    show(CLA, "🔴 **該項經 `K-9-29 二`", label="`CLAUDE.md` 之作廢標記")
    show(CLA, "`K-9-29` **本身之碼側落地**", label="`CLAUDE.md` 之碼側落地併記")
    show(K6, "### 步驟 0：同街廓相鄰合併（前置·無條件）", label="`K-6 §二` 步驟 0 之節題")

    print("\n🛑 **本器⛔ 提任何落地順序主張、⛔ 判任何項之優先**——出艙即止。")
    return rc


if __name__ == "__main__":
    sys.exit(main())
