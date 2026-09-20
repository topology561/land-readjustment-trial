# -*- coding: utf-8 -*-
r"""W-G.9-318 補令四 `§四`：`自誤 442` 之鑄（自誤簿檔末**嚴格追加**）。

🛑 payload 由**檔案管線**自本補令 `:135`–`:141` 抽出並剝 `> ` 前綴（`常規七 一`·⛔ 憑記憶重寫）。
🔒 `恆常附款 v①`：標題形自該簿**最近一則**（`自誤 441`）逐字複刻——`### 🩸 \`自誤 N\`　**…**`。
🔒 `恆常附款 x`（本批新立）：`append-only` 之判**三值化**出艙。
🔒 `恆常附款 l`：期值同格載其框與母體；bytes 明定末換行之歸屬。
"""
import hashlib
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "bc97c9d72d1680e820872aba787ecc453fa3a509"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
ORDER4 = "docs/orders/W-G.9-318_補令四_復驗受領與恆常附款簿及自誤442.md"
SRC_A, SRC_B = 135, 141          # 本補令之 payload 列（含）


def blob(path, rev=REV):
    p = subprocess.run(["git", "show", "%s:%s" % (rev, path)],
                       cwd=REPO, capture_output=True)
    if p.returncode != 0:
        raise SystemExit("🔴 讀不到 %s" % path)
    return p.stdout


def main():
    apply = "--apply" in sys.argv
    lp = REPO + "\\" + LEDGER.replace("/", "\\")
    op = REPO + "\\" + ORDER4.replace("/", "\\")

    before = open(lp, "rb").read()
    base = blob(LEDGER)
    print("── 期初（三值·`恆常附款 x`）──")
    print("  簿之工作區 bytes ＝ %d" % len(before))
    print("  簿之倉側 blob  bytes ＝ %d（態 `%s`）" % (len(base), REV[:7]))
    print("  工作區 ＝ blob ：%s" % (before == base))
    if before != base:
        raise SystemExit("🛑 工作區與開工態不符 ⇒ 停機")

    # ── 標題形之複刻自證（`恆常附款 v①`）──
    prev = [l for l in base.decode("utf-8").splitlines()
            if l.startswith("### 🩸 `自誤 ")]
    print("\n── 標題形之複刻（`v①`）──")
    print("  該簿最近一則之標題形 ＝ %s…" % prev[-1][:34])

    # ── payload 之抽取（檔案管線）──
    src = open(op, encoding="utf-8").read().splitlines()
    pay = []
    for ln in src[SRC_A - 1:SRC_B]:
        pay.append(ln[2:] if ln.startswith("> ") else ("" if ln.strip() == ">" else ln))
    payload = ("\n" + "\n".join(pay) + "\n").encode("utf-8")
    print("\n── payload（自 `%s:%d`–`:%d` 抽·剝 `> ` 前綴）──" % (ORDER4, SRC_A, SRC_B))
    print("  列數 ＝ %d（⛔ 含前導分隔空列）" % len(pay))
    print("  bytes ＝ %d（**含**前導分隔 `\\n` `1` B 與末換行 `1` B·`恆常附款 l②`）" % len(payload))
    print("  sha256 ＝ %s" % hashlib.sha256(payload).hexdigest())
    print("  CR ＝ %d" % payload.count(b"\r"))
    print("  首列 ＝ %s" % pay[0][:60])
    if not pay[0].startswith("### 🩸 `自誤 442`"):
        raise SystemExit("🛑 標題形不符 ⇒ 停機")

    after = before + payload
    print("\n── 期末之期值（算式·`恆常附款 w①`）──")
    print("  期末 bytes ＝ 期初 %d ＋ payload %d ＝ **%d**"
          % (len(before), len(payload), len(after)))

    if not apply:
        print("\n（乾跑·未落檔。加 `--apply` 方落檔）")
        return
    with open(lp, "wb") as fh:
        fh.write(after)
    now = open(lp, "rb").read()
    print("\n── 落檔後之機驗（`恆常附款 j③` 四造）──")
    print("  ① append-only 嚴格前綴逐位 ：%s" % (now[:len(before)] == before))
    print("  ② payload 逐位相符        ：%s" % (now[len(before):] == payload))
    print("  ③ 期末 bytes ＝ 期初 ＋ payload：%s（%d）"
          % (len(now) == len(after), len(now)))
    print("  ④ 期末 sha256 ＝ %s" % hashlib.sha256(now).hexdigest())
    print("  CR 全檔 ＝ %d" % now.count(b"\r"))


if __name__ == "__main__":
    main()
