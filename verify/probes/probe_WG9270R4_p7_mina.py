# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令三 `§四`：**`p7` `115.85` vs `115.88` 之歸屬判**（零生產碼·唯讀）。

🛑 **⛔ 逕改任一實作以使三者一致**——其為生產碼且屬 `GB-7` 之受詞（補令三 `§四` 明令）。
🛑 本器**全唯讀**：⛔ 寫任何生產碼、⛔ 寫 `verify/baselines`、⛔ 設 `WV_BAKE`。

🔒 **須答（補令三 `§四`）**
  `1` 該 `0.03` 是否即 **`GB-7`**（「per-block `MinA` 之 `round` 位置與正典不符——**三份實作**」）之同一件事？
      **以碼面逐處對拍**三份實作之 `round` 位置與 `CLAUDE.md:408` 所載之 `round(D_avg,2)=33.10`。
  `2` **是** ⇒ 併入 `GB-7` 之末端追加（⛔ 另立新號）。
  `3` **否** ⇒ **停機上呈**（`rc = 7`），由發單側判其是否另鑄。

🔒 **二形之定義（逐字·⛔ 器內另創）**
  **正典形**（`K-8 §二-1`·`wf_f0._mina_by_block` docstring 逐字「per-block MinA_i ＝
  `round(D_avg_i, 2) × min_width_i`（**正典寫法**）」）＝ `round(D, 2) * w`
  **碼面形**（三份實作皆然）＝ `round(D * w, 2)`

🔒 **三份實作之具名（`GB-8` 逐字）**
  ① `verify/wf_f0._mina_by_block`（`3` 參數 → `dict`·**引擎土地後果路徑**）
  ② `verify/wd4_tier_list._mina_by_block`（`4` 參數 → `(dict, min)`·**清單／回歸路徑**）
  ③ `app.py` 之 `_min_alloc_area_by_blk`（**生產 UI 路徑**·寫入 `f3_min_alloc_area_by_label`）

🔒 **深度之真相源**：`snapshot["blocks"][lbl]["街廓分配深度_m"]`（②③ 之 `SB` 即此；
  ③ 於 UI 側另有覆寫格 `f3L_depth_ov_*`·`GB-7b` 之受詞）。
  🔒 `app.py:5966` 逐字 `'D_avg': round(D_avg, 2)` ⇒ **自動量測之深度於來源即 `2dp`**。

🔒 **判別力**：本器對**三形**（正典形／碼面形／`CLAUDE.md` 所載之 `33.10`）逐塊並算，
  其**必有至少一塊三者相異**方證本比對非恆同（否則⛔ 出艙任何歸屬判）。

用法：`python verify/probes/probe_WG9270R4_p7_mina.py [倉根]`
`rc`：`0` 歸屬 ＝ `GB-7`／`7` **⛔ 屬 `GB-7` ⇒ 停機上呈**／`5` 量測器紅。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
import wd4_tier_list as WD4                                         # noqa: E402
import wf_f0 as F0                                                  # noqa: E402

BT = chr(96)
W = 116
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
# 🔒 `CLAUDE.md:408` 逐字所載（**⛔ 憑記憶**·本器另以 grep 復現之）
CLAUDE_LINE_ANCHOR = "現值＝**115.85 @ R4**"


def say(s=""):
    print(s)


def src_line(path, pat):
    p = os.path.join(REPO, path)
    with open(p, encoding="utf-8") as f:
        for i, ln in enumerate(f, 1):
            if re.search(pat, ln):
                return i, ln.rstrip("\n")
    return None, None


def main():
    say("=" * W)
    say("【`W-G.9-270` 補令三 `§四`】**`p7` `115.85` vs `115.88` 之歸屬判**")
    say("=" * W)
    say("🛑 **⛔ 逕改任一實作**（其為生產碼且屬 `GB-7` 之受詞）；本器**全唯讀**。")
    say("")

    # ── 一　碼面逐處對拍：三份實作之 `round` 位置 ────────────────────────
    say("─" * W)
    say("【一】碼面逐處對拍：**三份實作之 `round` 位置**（`GB-8` 所具名之三處）")
    say("─" * W)
    # 🩸 **框之自捕**：初版對 ① 用 `mina\[...\]`，而該支之變數名為 **`m`**
    #    （`verify/wf_f0.py:192` 逐字 `m[lbl] = round(d * mw, 2)`）⇒ **loud 拒測**（⛔ 靜默）。
    #    ⇒ 改以「賦值端為 `<名>[<鍵>]` ⋀ 右端為 `round(...)`」之通式，⛔ 猜其變數名。
    impl = [
        ("① `verify/wf_f0._mina_by_block`", "verify/wf_f0.py",
         r"^\s*m\[lbl\]\s*=\s*round"),
        ("② `verify/wd4_tier_list._mina_by_block`", "verify/wd4_tier_list.py",
         r"mina\[lbl\]\s*=\s*round"),
        ("③ `app.py` 之 `_min_alloc_area_by_blk`", "app.py",
         r"_min_alloc_area_by_blk\[[^\]]+\]\s*=\s*\(?round"),
    ]
    forms = []
    for nm, path, pat in impl:
        i, ln = src_line(path, pat)
        if i is None:
            say("   %s ⇒ 🛑 **⛔ 命中其算式** ⇒ loud 拒測" % nm)
            sys.exit(5)
        body = ln.strip()
        先乘後捨 = bool(re.search(r"round\(\s*[^,]*\*[^,]*,\s*2\s*\)", body))
        forms.append(先乘後捨)
        say("   %s" % nm)
        say("      `%s:%d`　%s" % (path, i, body[:104]))
        say("      ⇒ 形 ＝ **%s**" % ("`round(D × w, 2)`（**先乘後捨**·碼面形）" if 先乘後捨
                                      else "🔴 **非**先乘後捨 ⇒ 須另判"))
    say("   ⇒ 三份實作之形**是否一致** ＝ **%s**（皆先乘後捨 ＝ %s）"
        % ("✅ 一致" if len(set(forms)) == 1 else "🔴 分歧", all(forms)))
    i2, ln2 = src_line("verify/wf_f0.py", r"per-block MinA_i ＝")
    say("   🔒 **正典形之逐字**（`verify/wf_f0.py:%d` docstring）：%s" % (i2, (ln2 or "").strip()))
    say("")

    # ── 二　活體深度與二形之逐塊並算 ───────────────────────────────────
    say("─" * W)
    say("【二】**活體深度**與二形之逐塊並算（深度之真相源 ＝ `snapshot.blocks[*].街廓分配深度_m`）")
    say("─" * W)
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    SB = snapshot["blocks"]
    gm = ns["get_min_lot_size"]
    _fcb = ns["F3_CATEGORY_BURDEN"]
    bb = [b for b in cb_by.values()
          if _fcb.get(b.get("category", ""), "") == "可建築土地"]

    say("   %-6s %-22s %-10s %-16s %-16s %-14s %s"
        % ("街廓", "深度 D（**未捨入之原值**）", "min_width", "正典形 round(D,2)×w",
           "碼面形 round(D×w,2)", "Δ（碼−典）", "D 是否已 2dp"))
    rows = []
    for b in sorted(bb, key=lambda x: x["label"]):
        lbl = b["label"]
        D = float(SB[lbl]["街廓分配深度_m"])
        w = float(gm(b["category"], float(SB[lbl]["正面"]["路寬_m"]))["min_width"])
        canon = round(D, 2) * w
        code = round(D * w, 2)
        is2dp = (abs(D - round(D, 2)) < 1e-12)
        rows.append((lbl, D, w, canon, code))
        say("   %-6s %-22r %-10s %-16.6f %-16.6f %-14.6f %s"
            % (lbl, D, w, canon, code, code - canon, "✅" if is2dp else "🔴 **非 2dp**"))

    canon_min = min(r[3] for r in rows)
    code_min = min(r[4] for r in rows)
    canon_blk = [r[0] for r in rows if r[3] == canon_min]
    code_blk = [r[0] for r in rows if r[4] == code_min]
    say("")
    say("   🔑 **`MinA_區`（＝ `min` 之值）**：正典形 ＝ **%.6f**（落於 %s）／碼面形 ＝ **%.6f**（落於 %s）"
        % (canon_min, canon_blk, code_min, code_blk))

    # 生產側之實測（逕呼二實作·⛔ 器內重導）
    _m2, mq2 = WD4._mina_by_block(ns, snapshot, cb_by, bb)
    m1 = F0._mina_by_block(ns, snapshot, cb_by)
    mq1 = min(m1.values())
    say("   🔒 **逕呼生產側**：② `wd4_tier_list._mina_by_block` ⇒ `MinA_區` ＝ **%s**；"
        "① `wf_f0._mina_by_block` ⇒ `min` ＝ **%s**" % (mq2, mq1))
    say("      ①②之逐塊值是否相同 ＝ %s"
        % ("✅ 是" if all(abs(m1[k] - _m2[k]) < 1e-12 for k in _m2) else "🔴 否"))

    # ── 三　判別力（證本比對非恆同）────────────────────────────────────
    say("")
    diff_blk = [r[0] for r in rows if abs(r[4] - r[3]) > 1e-9]
    say("   🔒 **判別力**：二形相異之街廓 ＝ **%s**（%d／%d）⇒ %s"
        % (diff_blk, len(diff_blk), len(rows),
           "✅ 本比對⛔ 恆同" if diff_blk else "🔴 **恆同** ⇒ ⛔ 出艙歸屬判"))
    if not diff_blk:
        say("   🛑 量測器紅 ⇒ ⛔ 出艙")
        sys.exit(5)

    # ── 四　與 `CLAUDE.md:408` 及 `GB-7` 所載之對拍 ────────────────────
    say("")
    say("─" * W)
    say("【三】與 `CLAUDE.md` 及 `GB-7` 所載之對拍（**⛔ 憑記憶**·當場 grep 復現）")
    say("─" * W)
    ic, lc = src_line("CLAUDE.md", re.escape(CLAUDE_LINE_ANCHOR))
    say("   `CLAUDE.md:%s`　%s" % (ic, (lc or "🛑 ⛔ 命中").strip()))
    ig, lg = src_line("docs/reports/W-G.4_泛用阻塞項登記表.md", r"\*\*GB-7\*\* 🆕")
    m = re.search(r"R4[^｜|]*?33\.10×3\.5=115\.85", lg or "")
    say("   `GB-7` @ `W-G.4_泛用阻塞項登記表.md:%s`　其逐字含 `R4 33.10×3.5=115.85` ⇒ %s"
        % (ig, "✅ 命中" if m else "🛑 ⛔ 命中"))
    say("   🔒 `GB-7` 所載之四塊真分歧（逐字）：`R1 116.025/116.02`、`R2 155.645/155.64`、"
        "`R5 159.985/159.99`、`R6 159.285/159.28`；**`R3`/`R4` 等值**")
    say("")
    r4 = [r for r in rows if r[0] == "R4"][0]
    say("   🔑 **`R4` 之當場實測**：`D` ＝ **%r**／`w` ＝ `%s`／正典形 ＝ **%.6f**／碼面形 ＝ **%.6f**"
        % (r4[1], r4[2], r4[3], r4[4]))
    say("      ⇒ 二形於 `R4` %s（Δ ＝ %.9f）"
        % ("**相同**" if abs(r4[4] - r4[3]) < 1e-9 else "🔴 **相異**", r4[4] - r4[3]))
    say("      ⇒ `CLAUDE.md` 所載之 `round(D_avg,2) = 33.10` 與實測 `round(D,2) = %.2f` ⇒ %s"
        % (round(r4[1], 2), "✅ 相符" if abs(round(r4[1], 2) - 33.10) < 1e-9 else "🔴 **相異**"))

    # ── 五　歸屬判（**逐項分解**·⛔ 以「二形相異」逕判）────────────────
    say("")
    say("─" * W)
    say("【四】**歸屬判**（補令三 `§四` 款 `1`）——🔑 **逐項分解**，⛔ 以「二形相異」逕判")
    say("─" * W)
    say("   🩸 **本節之判準曾為錯（出艙前自捕）**：初版之規則為「`R4` 之二形相異 ⇒ 屬 `GB-7`」。")
    say("      🔴 該規則**混同二事**——「`GB-7` **有貢獻**」⛔ 等於「`GB-7` **解釋該 `0.03`**」。")
    say("      ⇒ 改為**分解**：把受詢之差拆成**深度之變**與 **`round` 位置**二項，並附**自洽驗算**。")
    say("")
    D_live = r4[1]
    w4 = r4[2]
    D_claude = 33.10                       # `CLAUDE.md:408` 逐字（上已 grep 復現）
    v_claude = round(D_claude, 2) * w4     # 正典形 @ `CLAUDE.md` 之深度
    v_canon_live = round(D_live, 2) * w4   # 正典形 @ 活體深度
    v_code_live = round(D_live * w4, 2)    # 碼面形 @ 活體深度（＝ 生產側實測）
    d_total = v_code_live - v_claude
    d_depth = v_canon_live - v_claude
    d_round = v_code_live - v_canon_live
    say("   %-46s %s" % ("`CLAUDE.md` 所載（正典形 @ `D = 33.10`）", "**%.6f**" % v_claude))
    say("   %-46s %s" % ("正典形 @ **活體深度** `D = %.2f`" % D_live, "**%.6f**" % v_canon_live))
    say("   %-46s %s" % ("碼面形 @ 活體深度（＝ 生產側實測）", "**%.6f**" % v_code_live))
    say("")
    say("   🔑 **分解**")
    say("      `Δ_total`（受詢之差）　＝ 碼面形@活體 − `CLAUDE.md` ＝ **%+.6f**" % d_total)
    say("      `Δ_depth`（**深度之變**）＝ 正典形@活體 − 正典形@`33.10` ＝ **%+.6f**"
        "　（`%.2f → %.2f` × `%.1f`）" % (d_depth, D_claude, round(D_live, 2), w4))
    say("      `Δ_round`（**`GB-7` 之受詞**）＝ 碼面形@活體 − 正典形@活體 ＝ **%+.6f**" % d_round)
    ok = abs((d_depth + d_round) - d_total) < 1e-9
    say("      **自洽驗算**：`Δ_depth + Δ_round` ＝ %+.6f ／ `Δ_total` ＝ %+.6f ⇒ %s"
        % (d_depth + d_round, d_total, "✅ 相等" if ok else "🔴 **不相等** ⇒ 分解未窮盡"))
    if not ok:
        say("   🛑 分解未窮盡 ⇒ ⛔ 出艙歸屬判 ⇒ **停機上呈**")
        sys.exit(7)
    share = abs(d_round) / abs(d_total) if d_total else float("inf")
    say("")
    say("   🔑 **`GB-7` 所佔之比** ＝ `|Δ_round| / |Δ_total|` ＝ **%.1f%%**（%.6f ／ %.6f）"
        % (share * 100.0, abs(d_round), abs(d_total)))
    say("   🔑 **主項** ＝ %s（佔 %.1f%%）"
        % ("**深度之變**" if abs(d_depth) > abs(d_round) else "`round` 位置",
           max(abs(d_depth), abs(d_round)) / abs(d_total) * 100.0))
    say("")
    if abs(d_depth) < 1e-9:
        say("   🟢 **判 ＝ 屬 `GB-7`**——`Δ_depth = 0` ⇒ 受詢之差**全數**由 `round` 位置產生。")
        say("   ⇒ 依款 `2`：併入 `GB-7` 之末端追加（⛔ 另立新號）。")
        sys.exit(0)
    say("   🔴 **判 ＝ ⛔ 屬 `GB-7`（⛔ 同一件事）**")
    say("      `GB-7` 之受詞為「**`round` 位置**」，其於本案僅佔 **%+.6f**（`%.1f%%`）；" % (d_round, share * 100.0))
    say("      **主項 `%+.6f` 係「深度之值本身已變」**（`CLAUDE.md` 載 `%.2f`／活體 `%.2f`）"
        % (d_depth, D_claude, round(D_live, 2)))
    say("      ——**深度之變⛔ 在 `GB-7` 之受詞內**（`GB-7` 逐字：「**per-block `MinA` 之 `round` 位置**與正典不符」）。")
    say("   🔒 **併記（照實）**：`GB-7` 逐字載 `R4` 為「`33.10×3.5=115.85` 恰 `2dp`**故兩形同值**」，")
    say("      而活體 `D = %.2f` ⇒ `R4` **已由「兩形同值」轉為「兩形相異 `%+.6f`」**" % (round(D_live, 2), d_round))
    say("      ⇒ **`GB-7` 本文之「本案零後果」之前提（min 恰落在 `R4` 且該塊兩形同值）已<u>不再成立</u>**；")
    say("      其自身逐字亦載「⚠️ **本案零後果係『min 恰落在 R4』之巧合**、非結構保證」。")
    say("   🛑 **依補令三 `§四` 款 `3`：否 ⇒ 停機上呈**，由發單側判其是否另鑄。")
    sys.exit(7)


if __name__ == "__main__":
    main()
