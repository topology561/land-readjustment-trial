# -*- coding: utf-8 -*-
r"""`W-G.9-319` 工項三・四：三 payload 之抽取（**檔案管線**·`常規七 一`·⛔ 憑記憶重寫）。

① `自誤 445`（單 `:166`–`:171`·剝 `> `）⇒ 自誤簿檔末
② `恆常附款 w②` 射程增補節（節題逐字見單 `§四-2`）⇒ 恆常附款簿檔末
③ `preserve` 性質變更節（單 `:196`–`:198`·剝 `> `）⇒ CC 側換手文檔末

🔒 `恆常附款 v①`：`自誤 445` 之標題形與簿內**最近一則**（`自誤 444`）當場比對其前綴。
🔒 `恆常附款 v②`：payload 以該簿之**二框**自驗，須皆命中（⛔ 落入缺號集）。
"""
import hashlib
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "c286a79cc6a699c57c7763306c4beae9ef7b60a3"
ORDER = "docs/orders/W-G.9-319_施工單_二寬度之量差與GB170三格現查及自誤445.md"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
OUT = REPO + r"\verify\out"

# 自擬框（單 `§四-1` 逐字）與正典框（`VR-091 四` 定義框）
RE_SELF = re.compile(r"^#{1,6} [^\w`]{0,6}`?自誤 `?(\d+)`?`?\s*[｜（\u3000:：]")
RE_CANON = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?")


def wt(p):
    return open(REPO + "\\" + p.replace("/", "\\"), encoding="utf-8").read().splitlines()


def blob(p):
    return subprocess.run(["git", "-c", "core.quotepath=false", "show", "%s:%s" % (REV, p)],
                          cwd=REPO, capture_output=True).stdout.decode("utf-8")


def strip_q(s):
    return s[2:] if s.startswith("> ") else ("" if s.strip() == ">" else s)


def emit(name, lines):
    body = ("\n" + "\n".join(lines) + "\n").encode("utf-8")
    path = OUT + "\\" + name
    with open(path, "wb") as f:
        f.write(body)
    print("   落檔 ＝ verify/out/%s｜bytes **%d**（含前導分隔 `\\n` 與末換行·`恆常附款 l②`）"
          "｜`sha256` `%s`｜`CR` %d"
          % (name, len(body), hashlib.sha256(body).hexdigest(), body.count(b"\r")))
    return body


def main():
    src = wt(ORDER)
    print("# `W-G.9-319` 三 payload 之抽取（檔案管線）")
    print("態 ＝ `%s`／單 ＝ `%s`（`%d` 列）\n" % (REV, ORDER, len(src)))

    # ── ① 自誤 445 ──
    print("── ① `自誤 445`（單 `:166`–`:171`）──")
    pay = [strip_q(x) for x in src[165:171]]
    led = blob(LEDGER)
    prev = [l for l in led.splitlines() if l.startswith("### 🩸 `自誤 ")]
    print("   `v①` 範本（簿內最近一則）＝ %s…" % prev[-1][:44])
    print("   本 payload 首列          ＝ %s…" % pay[0][:44])
    ok = pay[0].startswith("### 🩸 `自誤 445`　**")
    print("   ⇒ 前綴同族（`### 🩸 \\`自誤 N\\`　**`）：**%s**" % ok)
    if not ok:
        raise SystemExit("🛑 標題形不符 ⇒ 停機")
    print("   `v②` 二框自驗（⛔ 落入缺號集）：")
    a, b = RE_SELF.match(pay[0]), RE_CANON.match(pay[0])
    print("      自擬框 `RE_ZW_DEF` ⇒ **%s**（捕獲 `%s`）"
          % (bool(a), a.group(1) if a else "—"))
    print("      正典框（`VR-091 四`）⇒ **%s**（捕獲 `%s`）"
          % (bool(b), b.group(1) if b else "—"))
    print("      判別力［必不命中］：一非標題列（本 payload 之 `**形**：` 列）⇒ 自擬框 **%s**／正典框 **%s**"
          % (bool(RE_SELF.match(pay[2])), bool(RE_CANON.match(pay[2]))))
    emit("WG9319_ziwu445_payload.md", pay)

    # ── ② 恆常附款 w② 射程之增補 ──
    print("\n── ② `恆常附款 w②` 射程之增補（恆常附款簿檔末）──")
    # 其條文逐字 ＝ 單 `:171` 之攔法段（剝 `> `）
    clause = strip_q(src[170])
    # 入倉後之 `檔:列`：本單已於工項零入倉 ⇒ 當場現查其列號
    ln = None
    for i, l in enumerate(src, 1):
        if l.startswith("> **攔法（併入 `恆常附款 w②`"):
            ln = i
            break
    print("   其逐字出處（**入倉後當場現查·⛔ 憑單載**）＝ `%s:%d`" % (ORDER, ln))
    sec = [
        "## 🔧 恆常附款 w② 射程之增補（W-G.9-319·⛔ 上文一字不刪·純末端追加）",
        "",
        "🛑 **本節⛔ 鑄任何號**——其為 `恆常附款 w②` 之**修訂**（⛔ 新立款·單 `§零-2` 裁 `3`）。",
        "🔒 **態** ＝ `%s`（本批開工態·`恆常附款 w②`）。" % REV,
        "🛑 **⛔ 追改 `§一` 表一字**（`append-only`）——本節即其增補之載體。",
        "",
        "### ① 增補之逐字（⛔ 改一字）",
        "",
        "> " + clause,
        "",
        "### ② 所繫之自誤號",
        "",
        "`自誤 445`（`docs/reports/W-G.9波_claude.ai側自誤登記.md` 檔末）。",
        "",
        "### ③ 其逐字出處（檔:列）",
        "",
        "`%s:%d`（**本單入倉後當場現查之列號**·⛔ 憑單載）。" % (ORDER, ln),
        "🔒 **除本補令自身之產物外 ＝ `0`**（`恆常附款 e`）——該逐字於倉內**僅見於本單與本節**。",
        "",
        "### ④ 款數之算式（`恆常附款 f`·⛔ 直接寫一個數）",
        "",
        "期初 ＝ **`28`**（列舉 ＝ `a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab`）",
        "＋ 本批**新立 `0`** ⇒ 期末 ＝ **`28`**；本批**修訂 `1`**（`w②` 之射程）。",
        "🔒 **`w` 之索引⛔ 變**（其 `出處` 節題一字不動）；本節係其**射程之增補**，",
        "⛔ 另立索引項（`ab②`：可由索引取得者⛔ 以文字搜框取之——`w` 之條文仍經其既有索引取）。",
    ]
    emit("WG9319_book_payload.md", sec)

    # ── ③ preserve 性質變更 ──
    print("\n── ③ `preserve` 性質變更（單 `:196`–`:198`）──")
    three = [strip_q(x) for x in src[195:198]]
    sec3 = [
        "## 🔧 preserve 之性質變更與 §12 所載其值之過期（W-G.9-319·⛔ 上文一字不刪·純末端追加）",
        "",
        "🛑 **本節⛔ 鑄任何號**；**⛔ 追改本文上文一字**（`常規四（九）五`）。",
        "🔒 **態** ＝ `%s`。" % REV,
        "",
    ] + ["> " + x if x.strip() else ">" for x in three]
    emit("WG9319_handover_payload.md", sec3)


if __name__ == "__main__":
    main()
