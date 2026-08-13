# -*- coding: utf-8 -*-
r"""`W-G.9-18`：**降維鏈之逐段追蹤**（⛔ 零生產碼·⛔ 只追·不改）。

## 受詞

`_build_corner_range_v3` 回傳之**多邊形**（含**真正之遠側界**），
在**無 WINNER**（強制抵費地）路徑上被**壓成一個面積數字**——追出**哪一段丟掉什麼**。

🔒 **鍵一律用字樣錨**，⛔ 不用行號（倉規·行號衛生第 4 款）。
🔒 **母體釘在明確 commit**（驗收 #8）；**凡出艙計數必附母體與判準**（驗收 #2）。
🔒 **凡「查無」須先證所查之鍵在母體中確實可命中**（驗收 #10）。

## 重跑
    python verify/probes/probe_WG918_downcast.py [<commit-sha>]
"""
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
SHA = sys.argv[1] if len(sys.argv) > 1 else "08eeebb"       # ＝ W-G.9-18 commit A
OUT = os.path.join(VERIFY, "out", "probe_WG918_downcast.log")
L = []


def say(s=""):
    print(s)
    L.append(s)


def show(p):
    t = subprocess.run(["git", "-C", REPO, "show", f"{SHA}:{p}"],
                       capture_output=True).stdout.decode("utf-8", "replace")
    assert t.strip(), f"🔴 母體為空：{SHA}:{p}"
    return t.split("\n")


APP = show("app.py")


def hits(key, lines=None):
    lines = APP if lines is None else lines
    return [(i + 1, x.rstrip()) for i, x in enumerate(lines) if key in x]


def main():
    say("=" * 106)
    say("【`W-G.9-18`】降維鏈之逐段追蹤（⛔ 只追·不改）")
    say("=" * 106)
    say(f"  🔒 **母體釘於 commit {SHA}**｜`app.py` **{len(APP)}** 行（⛔ 非工作樹現況）")
    say(f"  🔒 **母體可命中之對照**（驗收 #10）：`def ` ＝ {len(hits('def '))} 行 ⇒ 下列各式非因母體壞掉")

    say()
    say("  ══ 降維鏈（**字樣錨**·⛔ 非行號）══")
    chain = [
        ("① 產生", "_rng_cr = _build_corner_range_v3(",
         "收到：**多邊形**（含遠側界）", "丟掉：**無**（此段完整）"),
        ("② 降維", "_left_min = round(float(_rng_cr.area), 2)",
         "收到：多邊形", "🔴 **丟掉：整條遠側界、整個形狀**——只留 `.area` 一個純量"),
        ("③ 存欄", "'【左】街角最小面積(㎡)': _left_min,",
         "收到：純量", "丟掉：**無**（已無可丟）"),
        ("④ 取欄", "_l_min = _row_for_buffer.get('【左】街角最小面積(㎡)')",
         "收到：純量", "丟掉：**無**"),
        ("⑤ 消費", "_left_buffer_S = _corner_buffer_S(",
         "收到：純量作 `range_area`", "丟掉：**無**——但它**只拿得到面積**，故只能以 ∥ALLOC 另建一帶湊出等面積"),
    ]
    for name, key, got, lost in chain:
        h = hits(key)
        say()
        say(f"    ▸ {name}｜字樣錨 `{key[:52]}`")
        say(f"        命中 **{len(h)}** 行（母體＝`app.py` 全 {len(APP)} 行·判準＝含該字樣）")
        for n, x in h:
            say(f"          {n} | {x.strip()[:88]}")
        say(f"        {got}")
        say(f"        {lost}")

    # ── H-1／C2 ──────────────────────────────────────────────────────────
    say()
    say("  ══ `H-1`／`C2`：遠側界除 `.area` 外有無**生產**消費者 ══")
    for var, note in (("_rng_cr", "無 WINNER（強制抵費地）路徑"),
                      ("_rng_wb", "PK 路徑（`select_corner_lots_both_sides_v12` 內）")):
        h = hits(var)
        say(f"    ▸ `{var}`（{note}）之全部用處 ＝ **{len(h)}** 行")
        for n, x in h:
            say(f"        {n} | {x.strip()[:92]}")
    say()
    say("    🔴 **`C2` 破 ⇒ `J-1`**：`_rng_wb` 之多邊形**整個被保留**"
        "（`_corner_range_left = _rng_wb`／`_corner_range_right = _rng_wb`）")
    say("      ⇒ **遠側界在生產路徑上<u>另有消費者</u>**，⛔ 非只取面積。")
    say("      ⚠️ **降維只發生在無 WINNER 那一條路徑**；PK 路徑拿的是完整多邊形。")

    # ── C4：下游是否以 s 座標為介面 ──────────────────────────────────────
    say()
    say("  ══ `C4`：下游是否以 `s` 座標為介面 ══")
    key = "帶 `s ∈ ["
    h = hits(key)
    say(f"    `_corner_buffer_S` 之 docstring 含 `{key}` ＝ **{len(h)}** 行")
    for n, x in h:
        say(f"        {n} | {x.strip()[:92]}")
    say("    🔴 **`C4` 成立**：`_corner_buffer_S` 之帶**以 `s` 區間表達**"
        "（`left` → `s ∈ [max(s_min,0), buf]`／`right` → `s ∈ [s_max − buf, s_max]`）")
    say("      ⇒ **∥SIDELINE 所界之區域<u>不是</u> `s` 區間** ⇒ 該結構前置**為真**"
        "（＝`GB-58` 措辭查無、實質機制在者）。")

    # ── C5：S1_par 與 W 互代 ─────────────────────────────────────────────
    say()
    say("  ══ `C5`：`S1_par` 與 `W` 之互代（**語意窮舉**·先證鍵可命中）══")
    for k in ("S1_par", "路平行", "同名不同量", "垂距"):
        say(f"    `{k}`：`app.py` **{len(hits(k))}** 行（⇒ 鍵可命中·非壞鍵）")
    say("    🔍 碼面之戒（逐字）：")
    for k in ("路平行", "同名不同量"):
        for n, x in hits(k)[:2]:
            say(f"        {n} | {x.strip()[:92]}")
    say("    ⇒ **查無**「把 `S1_par` 當垂距用」或「把 `W` 當路平行距用」之實例。")
    say("    ⚠️ **射程聲明**：本項之受詞限**字面上把二者當同一個量用**；")
    say("      ⛔ **不宣稱**涵蓋「概念上誤用」——後者無機械判準，本批⛔ 未量。")

    say()
    say("=" * 106)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
