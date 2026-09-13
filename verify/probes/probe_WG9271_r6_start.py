# -*- coding: utf-8 -*-
"""`W-G.9-271` `§二-3`：**`R6` 起點端 `85.71 ㎡` 之成因**（零生產碼·**出艙即止**）。

🔒 **器之底本** ＝ `probe_WG9271_s_frame.py` 之 `drive_spy`（其本身承
   `probe_WG9270R4_p6_interleave.py`）——`block_poly`／`d_hat`／`corner_pt`／`allocation_dir`
   **逐位取自間諜所錄之同一次呼叫實參**（⛔ 器內重導切線座標）。

🔒 **逐情境（`0m`／`3.5m`）出艙**（單 `§二-3` 逐字）
   `1` `s` 域 ＝ `ns["_strip_s_range"](block_poly, d_hat, corner_pt, allocation_dir)` 之 `(s_min, s_max)`；
   `2` 鏈頭第一宗（`s` 起最小之配地宗）之**暫編地號**與其 `s` 起；
   `3` `2` − `1` 之差（**未捨入值**·落檔 2dp 僅為顯示）；
   `4` 該片（`R6-池#2`）之 `s` 區間與面積。

🔒 **判別力二造**（施於量測式本身）
   甲[必非零] `s_max - s_min` ⇒ `>0`；
   乙[必為零] 同一 `block_poly` **自比**之 `s_min` 差 ⇒ `0`。
   ⇒ 二造不如預期 ⇒ `rc = 5` loud 拒測。

🛑 **⛔ 判其為缺陷、⛔ 提任何處置主張**——候發單側與 KL。
🛑 **⛔ 判已登記之錨移二值（`+3.39 m`＠`0m·R2·left`／`+3.32 m`＠`3.5m·R5·left`）與本量為同一量**
   ——**照實並列**，先對齊母體／受詞再判（單 `§二-3` 明令）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9271_r6_start.py [倉根]`
`rc`：`0`／`3` 母體為 `0`／`5` **量測器紅**。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

import probe_WG9271_s_frame as SF                                   # noqa: E402

W = 118
SBS = (0.0, 3.5)
BLK = "R6"
# 🔒 已登記之錨移二值（**照實並列**·⛔ 判其為同一量）
ANCHOR_SHIFT = [("0m", "R2", "left", 3.39), ("3.5m", "R5", "left", 3.32)]


def say(s=""):
    print(s)


def main():
    say("=" * W)
    say("【`W-G.9-271` `§二-3`】**`R6` 起點端之成因**（**出艙即止**）")
    say("=" * W)
    say("🛑 **⛔ 判其為缺陷、⛔ 提任何處置主張**——候發單側與 KL。")

    rc = 0
    for sb in SBS:
        tag = "%gm" % sb
        say("")
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        ns, rec, rows = SF.drive_spy(sb)
        ssr = ns["_strip_s_range"]
        if BLK not in rec:
            say("🛑 `%s` ⛔ 在間諜所錄之母體 ⇒ 其量 **⛔ 可得**" % BLK)
            rc = 3
            continue
        calls = rec[BLK]
        say("🔒 間諜所錄之 `%s` 呼叫次數 ＝ **%d**（⇒ 取末一次；其餘逐次之片數 ＝ %s）"
            % (BLK, len(calls), [len(c["pieces"]) for c in calls]))
        d = calls[-1]

        # ── 判別力二造（**先於**出艙任何結論）────────────────────────────
        bp = d.get("block_poly")
        if bp is None:
            say("🛑 間諜未錄 `block_poly` ⇒ **loud 拒測**（⛔ 以他物代之）")
            return 5
        r_all = ssr(bp, d["d_hat"], d["corner_pt"], d["alloc"])
        if r_all is None:
            say("🛑 `block_poly` 之 `s` 域**不可得**（`_strip_s_range` 回 `None`）⇒ **loud 拒測**")
            return 5
        s_min, s_max = float(r_all[0]), float(r_all[1])
        r_self = ssr(bp, d["d_hat"], d["corner_pt"], d["alloc"])
        say("   判別力[必非零] `s_max - s_min` ＝ **%.9f** ⇒ %s"
            % (s_max - s_min, "✅" if s_max - s_min > 0 else "🔴"))
        say("   判別力[必為零] 同一 `block_poly` **自比**之 `s_min` 差 ＝ **%.12f** ⇒ %s"
            % (float(r_self[0]) - s_min, "✅" if float(r_self[0]) - s_min == 0.0 else "🔴"))
        if not (s_max - s_min > 0 and float(r_self[0]) - s_min == 0.0):
            say("   🛑 **二造不如預期 ⇒ 器紅** ⇒ loud 拒測")
            return 5

        # ── 1　`s` 域 ──────────────────────────────────────────────────
        say("")
        say("   `1`　`s` 域（`block_poly` 之 `(s_min, s_max)`·**未捨入**）")
        say("        `s_min` ＝ **%.9f**｜`s_max` ＝ **%.9f**｜長 ＝ %.9f"
            % (s_min, s_max, s_max - s_min))

        # ── 2　鏈頭第一宗 ─────────────────────────────────────────────
        cut = SF.cut_polys(rows, BLK)
        C, bad = SF.sranges(ssr, cut, d)
        if not C:
            say("   🛑 `%s` 之配地宗母體 ＝ `0` ⇒ **⛔ 可得**（`s` 不可得 %d）" % (BLK, bad))
            rc = 3
            continue
        C.sort(key=lambda t: t[1])
        head = C[0]
        say("")
        say("   `2`　鏈頭第一宗（`s` 起最小之配地宗）·母體 ＝ **%d** 宗（`s` 不可得 %d）"
            % (len(C), bad))
        say("        暫編地號 ＝ `%s`｜`s` 起 ＝ **%.9f**｜`s` 迄 ＝ %.9f｜面積 ＝ %.4f ㎡"
            % (head[0], head[1], head[2], head[3]))
        say("        （次三宗：%s）"
            % "；".join("`%s` s起 %.6f" % (x[0], x[1]) for x in C[1:4]))

        # ── 3　差 ─────────────────────────────────────────────────────
        gap = head[1] - s_min
        say("")
        say("   `3`　`2` − `1` 之差（**未捨入值**·落檔 `2dp` 僅為顯示）")
        say("        `s起(鏈頭) - s_min` ＝ **%.9f** m（2dp 顯示 ＝ %.2f）" % (gap, gap))

        # ── 4　該片之 `s` 區間與面積 ───────────────────────────────────
        pieces = [("%s-池#%d" % (BLK, i + 1), g) for i, g in enumerate(d["pieces"])]
        P, badp = SF.sranges(ssr, pieces, d)
        say("")
        say("   `4`　`%s` 之池片逐片（`s` 不可得 %d）" % (BLK, badp))
        say("        | 池片 | `s` 起 | `s` 迄 | `s` 長 | 面積(㎡) |")
        say("        |---|---|---|---|---|")
        for nm, p0, p1, pa in P:
            say("        | `%s` | %.9f | %.9f | %.9f | **%.4f** |" % (nm, p0, p1, p1 - p0, pa))

        # ── 照實並列（⛔ 判其為同一量）────────────────────────────────
        say("")
        say("   🔒 **照實並列已登記之錨移二值**（🛑 **⛔ 判其為同一量**——先對齊母體／受詞再判）")
        say("        | 出處之情境 | 街廓 | 側 | 錨移值 (m) | 本量之受詞 |")
        say("        |---|---|---|---|---|")
        for t, b, sd, v in ANCHOR_SHIFT:
            say("        | `%s` | `%s` | `%s` | `+%.2f` | 本量 ＝ `%s` 之「鏈頭 `s` 起 − `s_min`」＝ %.6f |"
                % (t, b, sd, v, BLK, gap))
        say("        🛑 二者之**街廓相異**（`%s` vs `R2`／`R5`）、**側之受詞相異**（本量⛔ 分側）"
            % BLK)
        say("           ⇒ **⛔ 得逕判為同一量**；照實具名，其裁候發單側。")
    return rc


if __name__ == "__main__":
    sys.exit(main())
