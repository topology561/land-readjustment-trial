# -*- coding: utf-8 -*-
r"""`W-G.9-319 補令一` 工項一・二・三：三 payload 之抽取（**檔案管線**·`常規七 一`）。

① `自誤 446`／`447`／`448`（單 `:59`–`:66`／`:70`–`:76`／`:80`–`:89`·剝 `> `）⇒ 自誤簿檔末
② `恆常附款 w②`／`v②`／`u` 射程增補節 ⇒ 恆常附款簿檔末
③ `停一` 成因之坐實節 ⇒ `W-G.9-319R` 檔末

🔒 `v①`：三則之標題形與簿內**最近一則**（`自誤 445`）當場比對其前綴。
🔒 `v②`：三則 payload 以**二框**自驗，須皆命中（⛔ 落入缺號集）。
"""
import hashlib
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "51a641d334847d285f323257909748acdf7052e1"
ORDER = "docs/orders/W-G.9-319_補令一_停一成因與自誤446至448及v②射程.md"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
OUT = REPO + r"\verify\out"

RE_SELF = re.compile(r"^#{1,6} [^\w`]{0,6}`?自誤 `?(\d+)`?`?\s*[｜（\u3000:：]")
RE_CANON = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?")
SPANS = [(446, 59, 66), (447, 70, 76), (448, 80, 89)]


def wt(p):
    return open(REPO + "\\" + p.replace("/", "\\"), encoding="utf-8").read().splitlines()


def blob(p):
    return subprocess.run(["git", "-c", "core.quotepath=false", "show", "%s:%s" % (REV, p)],
                          cwd=REPO, capture_output=True).stdout.decode("utf-8")


def sq(s):
    return s[2:] if s.startswith("> ") else ("" if s.strip() == ">" else s)


def emit(name, lines):
    body = ("\n" + "\n".join(lines) + "\n").encode("utf-8")
    with open(OUT + "\\" + name, "wb") as f:
        f.write(body)
    print("   落檔 ＝ verify/out/%s｜bytes **%d**｜`sha256` `%s`｜`CR` %d"
          % (name, len(body), hashlib.sha256(body).hexdigest(), body.count(b"\r")))
    return body


def main():
    src = wt(ORDER)
    print("# `W-G.9-319 補令一` 三 payload 之抽取（檔案管線）")
    print("態 ＝ `%s`／單 `%d` 列\n" % (REV, len(src)))

    # ── ① 自誤 446／447／448 ──
    print("── ① `自誤 446`／`447`／`448` ──")
    prev = [l for l in blob(LEDGER).splitlines() if l.startswith("### 🩸 `自誤 ")]
    print("   `v①` 範本（簿內最近一則）＝ %s…" % prev[-1][:40])
    allp = []
    for n, a, b in SPANS:
        pay = [sq(x) for x in src[a - 1:b]]
        ok = pay[0].startswith("### 🩸 `自誤 %d`　**" % n)
        m1, m2 = RE_SELF.match(pay[0]), RE_CANON.match(pay[0])
        print("   `自誤 %d`：首列前綴同族 **%s**｜自擬框 **%s**（%s）｜正典框 **%s**（%s）｜列 `%d`"
              % (n, ok, bool(m1), m1.group(1) if m1 else "—",
                 bool(m2), m2.group(1) if m2 else "—", len(pay)))
        if not (ok and m1 and m2):
            raise SystemExit("🛑 `自誤 %d` 之形或二框自驗不過 ⇒ 停機" % n)
        allp.extend(pay + [""])
    allp = allp[:-1]
    print("   判別力［必不命中］：一非標題列 ⇒ 自擬框 **%s**／正典框 **%s**"
          % (bool(RE_SELF.match(allp[2])), bool(RE_CANON.match(allp[2]))))
    emit("WG9319b_ziwu446_448_payload.md", allp)

    # ── ② 恆常附款 射程增補 ──
    print("\n── ② `恆常附款 w②`／`v②`／`u⑥⑦` 射程增補 ──")
    # 其逐字取自單之表列與 `§二-3` 之攔法二款
    u6 = sq(src[87])
    u7 = sq(src[88])
    sec = [
        "## 🔧 恆常附款 w② 與 v② 與 u 之射程增補（W-G.9-319 補令一·⛔ 上文一字不刪·純末端追加）",
        "",
        "🛑 **本節⛔ 鑄任何號**——其為 `w②`／`v②`／`u` 三款之**修訂**（⛔ 新立款）。",
        "🔒 **態** ＝ `%s`（本批開工態）。🛑 **⛔ 追改 `§一` 表一字**。" % REV,
        "",
        "| 款 | 增補之逐字 | 所繫 |",
        "|---|---|---|",
    # 🩸 自捕：首版取 `src[95:98]` ⇒ 含分隔列而**漏 `u` 之列**；表列之三行為 `:97`–`:99`
    ] + [l for l in src[96:99]] + [
        "",
        "### `u⑥`／`u⑦` 之逐字（自單 `§二-3` 抽·⛔ 改一字）",
        "",
        "> " + u6,
        "> " + u7,
        "",
        "### 款數之算式（`恆常附款 f`·⛔ 直接寫一個數）",
        "",
        "期初 ＝ **`28`** 款（列舉 ＝ `a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab`）",
        "＋ 本批**新立 `0`** ⇒ 期末 ＝ **`28`**；本批**修訂 `3` 款**（`w`／`v`／`u`）。",
        "🔒 三款之索引⛔ 變（其 `出處` 節題一字不動）；本節係其**射程之增補**，⛔ 另立索引項。",
    ]
    emit("WG9319b_book_payload.md", sec)

    # ── ③ W-G.9-319R 之末端追加 ──
    print("\n── ③ `W-G.9-319R` 之末端追加（`§四` 所令·承載裁 `1`〜`5` 逐字）──")
    rules = [l for l in src[11:44]]      # `§零-1` 裁 `1`〜`5` 之區間
    sec3 = [
        "## 🔧 停一 成因之坐實與 [必相符] 造之撤回重設（W-G.9-319 補令一·⛔ 上文一字不刪·純末端追加）",
        "",
        "🛑 **本節⛔ 鑄任何號**；**⛔ 追改本報告上文一字**（`常規四（九）五`）",
        "——`§三-4` 所載之「停一 成立」係**其立節當時之現態**，其**沿革**於此保留。",
        "🔒 **態** ＝ `%s`（本補令之開工態）。" % REV,
        "",
        "### 一　發單側之五裁（逐字轉錄·⛔ 改寫）",
        "",
    ] + ["> " + l if l.strip() else ">" for l in rules] + [
        "",
        "### 二　重設之造與 CC 實得之逐位對拍",
        "",
        "| 量 | 值 | 判 |",
        "|---|---|---|",
        "| 重設之造（同簿末端追加 `:8254` 逐字）`理論@k*` | **`87.72`** | — |",
        "| CC 實得 `R(13.98)` | `87.724000` ⇒ `2dp` **`87.72`** | 🟢 **逐位相符** ⇒ **其器非紅、其量為正** |",
        "",
        "### 三　🩸 具名之相異（**只登記·⛔ 判其成因·⛔ 據以改任何判**）",
        "",
        "| 量 | 值 |",
        "|---|---|",
        "| CC 實得 `R(14.17)` | `88.395000` ⇒ `2dp` **`88.39`** |",
        "| 閘之 `實跑(階段1)` | **`88.40`** |",
        "| 差（`2dp` 顯示層） | **`0.01`** ⇒ **⛔ 逐位相符** |",
        "",
        "🛑 其可能之由（**⛔ 判**·單 `§零-1` 裁 `2` 逐字）＝ 實跑側所餵之 `W` 為**未捨入**"
        "而本器之 `W(m)` 欄為 `2dp`——即 `GB` 簿 `W₀ 二消費者之粒度不對稱` 一節所登記之同族現象。",
        "",
        "### 四　階段 `b` 三造之受詞（**釘死於此**·其執行**另單 `W-G.9-320`·新窗**）",
        "",
        "| 造 | `widths` 所餵 | 分離之因 |",
        "|---|---|---|",
        "| `α` | `_宗地寬度`（現況·`2dp`） | 基座 |",
        "| `β` | `round(W, 2)` | **只換軸**·粒度同 `α` |",
        "| `γ` | `W`（未捨入） | 換軸 ＋ 換粒度 |",
        "",
        "🔒 **其分離之由**（單 `裁 3` 逐字）：原設計同時更動**軸**與**粒度** ⇒ 其產物**⛔ 可歸因**。",
        "🛑 **三造之執行⛔ 於本補令辦。**",
    ]
    emit("WG9319b_report_payload.md", sec3)


if __name__ == "__main__":
    main()
