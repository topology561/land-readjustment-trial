#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""`W-G.9-237` 工項二：**`PreToolUse` heredoc 硬閘**——`GB-143` 補款二之**對應機制**。

── 本器之地位 ────────────────────────────────────────────────────────────────
`GB-143` 補款二 款 `二` 逐字令「**凡經 heredoc 者一律⛔ 執行**」，而其機制原為**自檢**
（＝執行者之人工判斷）⇒ `W-G.9-235R2` 工項二判其為「**已知無閘之禁令**」、發生次數 `3`。
本器即該禁令之**真攔截點**：由 harness 之 `PreToolUse` hook 於 `Bash` 工具**執行前**呼叫，
非零退出即阻斷該次呼叫 ⇒ **⛔ 繫於執行者是否記得**。

── 四條件（`W-G.9-237` 工項二 `b`·缺一即為落地不全）────────────────────────
`①` **判準具名且可出艙**：比對之字樣集 ＝ 下方 `PATTERNS`（**本檔為 `.py`·可 `grep`**），
    **⛔ 僅存於 config**。
`②` **誤攔之處置明定**：見下 `MISFIRE_POLICY`（⛔ 設任何自助式 bypass 旗標）。
`③` **攔截須 loud**：非零退出 ＋ `stderr` 逐字理由（含所命中之樣式代稱與其偏移）；
    **⛔ 靜默丟棄、⛔ 靜默改寫命令**。
`④` **本器失效須可偵測**：`--selftest` 走**與 hook 完全同一之 `verdict()`**
    （`GB-148` 之教訓：`--selftest` ⛔ 繞過受測路徑）；且**器之生效與否**須由
    **活體攔截實測**（工項二 `c`）判定——`--selftest` 綠**⛔ 蘊含** hook 已接線。

── 契約 ──────────────────────────────────────────────────────────────────────
`stdin` ＝ hook 事件之 JSON（含 `tool_name` 與 `tool_input`）。
`Bash` 之受詞 ＝ `tool_input.command`。非 `Bash` 一律放行（`exit 0`）。
阻斷時**二法並用**（以相容於不同之 hook 契約）：
  · `stdout` 輸出 `permissionDecision = "deny"` 之 JSON；
  · **`exit 2`**（`PreToolUse` 之阻斷碼）。
"""
import json
import re
import sys

# ── ① 判準（具名·可 grep·⛔ 僅存於 config）────────────────────────────────
#    受詞 ＝ `戒`（`W-G.9-234R` 附 `3`）：「`Bash` 之 `command` 內⛔ 出現 `<<` 之任何形」。
#    ⇒ 本器**刻意採寬形**（含 `<<`／`<<-`／`<<'X'`／`<<"X"`／`<<<`）：
#      過攔可由 `②` 之處置救回，漏攔則重演 `GB-143` 之五度。
PATTERNS = [
    ("H1 heredoc/herestring 引入符", re.compile(r"<<")),
]

# ── ② 誤攔之處置（⛔ 自助式 bypass）──────────────────────────────────────
MISFIRE_POLICY = """\
[誤攔之處置｜⛔ 本器設任何 bypass 旗標]
 一 首選：改以 `Write` 工具落檔，再以**路徑**呼叫（此即 GB-143 處置一之逐字所令者）。
 二 若該命令之合法用途確不可改走一（如 shell 之位元左移 `<<`）：
    ⛔ 停用本器、⛔ 改本器之 PATTERNS；改寫該命令以避開該字樣
    （例：以變數或 `python -c` 之等價式替代）。
 三 若二亦不可行：**停並上呈發單側／KL**，並於該批報告新設「誤攔登記」節，
    逐則載：命令之**代稱**（⛔ 逐字·GB-147）／被攔之樣式代稱／所欲之合法用途／改寫之嘗試。
 四 本器之任何改動（含 PATTERNS）須於該批報告逐行具名理由，並重跑 `--selftest`。"""

_DENY_HEAD = "🔴 [wg9237_heredoc_guard] 已阻斷：Bash 命令含 heredoc 引入符"


def verdict(tool_name, command):
    """回 (是否阻斷, 理由字串)。🔒 hook 路徑與 `--selftest` **共用本函式**（`GB-148`）。"""
    if tool_name != "Bash":
        return False, ""
    if not isinstance(command, str) or not command:
        return False, ""
    for name, rx in PATTERNS:
        m = rx.search(command)
        if m:
            return True, (
                f"{_DENY_HEAD}\n"
                f"  命中樣式 ＝ {name}（偏移 {m.start()}）\n"
                f"  依據 ＝ GB-143 補款二 款二 逐字「凡經 heredoc 者一律⛔ 執行」；\n"
                f"        戒（W-G.9-234R 附 3）「Bash 之 command 內⛔ 出現該引入符之任何形」。\n"
                f"{MISFIRE_POLICY}")
    return False, ""


def _selftest():
    """④ 之自檢：兩造對照組**皆須如期**，否則本器⛔ 得宣稱為閘。
    🔒 二例皆走 `verdict()`（＝ hook 之同一路徑）。"""
    pos_cmd = "echo 'A" + "<" + "<B'"        # 器須綠：含引入符 ⇒ 須阻斷（執行亦無害）
    neg_cmd = "echo 'A-B'"                    # 器須紅：不含 ⇒ 須放行
    b1, r1 = verdict("Bash", pos_cmd)
    b2, _ = verdict("Bash", neg_cmd)
    b3, _ = verdict("Read", pos_cmd)          # 非 Bash ⇒ 須放行（射程之界）
    ok = (b1 is True) and (b2 is False) and (b3 is False)
    print("[selftest] 對照組 甲（含引入符·期望 阻斷）      =", b1, "OK" if b1 else "FAIL")
    print("[selftest] 對照組 乙（不含·期望 放行）          =", (not b2),
          "OK" if not b2 else "FAIL")
    print("[selftest] 對照組 丙（非 Bash·期望 放行）       =", (not b3),
          "OK" if not b3 else "FAIL")
    print("[selftest] 阻斷理由之首行 =", r1.split("\n")[0] if r1 else "(無)")
    print("[selftest] 判 =", "PASS" if ok else "FAIL")
    print("[selftest] 🛑 本自檢綠 ⛔ 蘊含 hook 已接線——接線與否須由**活體攔截實測**判定。")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv[1:]:
        return _selftest()
    # 🩸 **第二個真缺陷之修**（`W-G.9-238` 活體攔截實測當場咬中）：
    #    首版用 `sys.stdin.read()` ⇒ 走**平台預設編碼**（本機 `cp950`）
    #    ⇒ 凡命令含 CJK 者，其 UTF-8 位元組以 `cp950` 解碼後破壞 JSON 結構
    #    ⇒ 落入「解析失敗 ⇒ 阻斷」⇒ **誤攔一切含中文之 `Bash` 命令**（`②` 之誤攔情形）。
    #    🔒 hook 事件之 wire 編碼恆為 **UTF-8** ⇒ 一律自 `sys.stdin.buffer` 取**位元組**後顯式解碼。
    raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
    # ③ loud：**空 stdin 亦係「無從判定」**——⛔ 落入 `{}` 而靜默放行。
    #    依 `W-G.9-14` 修法 `②`：「無從判定」與「判定為可」**⛔ 共用同一出艙碼**。
    #    🩸 本分支係 `W-G.9-237` 工項二 `c` 之 `⟨NEG3⟩` 案當場捕獲之真缺陷（首版靜默放行）。
    if not raw.strip():
        sys.stderr.write("🔴 [wg9237_heredoc_guard] hook 事件為空 ⇒ 無從判定 ⇒ 阻斷"
                         "（⛔ 靜默放行·W-G.9-14 修法 ②）\n")
        return 2
    try:
        ev = json.loads(raw)
    except Exception:
        # ③ loud：解析不能亦⛔ 靜默放行——「無從判定」與「判定為可」⛔ 共用出艙碼。
        sys.stderr.write("🔴 [wg9237_heredoc_guard] hook 事件 JSON 解析失敗 ⇒ 阻斷（⛔ 靜默放行）\n")
        return 2
    tool = ev.get("tool_name") or ev.get("toolName") or ""
    cmd = (ev.get("tool_input") or ev.get("toolInput") or {}).get("command", "")
    blocked, reason = verdict(tool, cmd)
    if not blocked:
        return 0
    # 🩸 **第三個真缺陷之修**（`W-G.9-238` 活體攔截實測·隔離實驗所得）：
    #    首版**二法並用**（`stdout` 之 `hookSpecificOutput` deny JSON ＋ `exit 2`）。
    #    活體實測：僅 `stderr` ＋ `exit 2` 者**確被攔**（CJK 解析失敗案）；
    #    而二法並用者**未被攔** ⇒ 🔒 **`stdout` 之 JSON 覆蓋 `exit 2` 而其驗證未過 ⇒ 回落放行**。
    #    ⇒ **⛔ 二法並用**；一律**只走 `stderr` ＋ `exit 2`**（`PreToolUse` 之阻斷碼）。
    sys.stderr.write(reason + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
