# -*- coding: utf-8 -*-
r"""W-G.9-318 補令五 `§二`：`自誤 443` 之 payload 抽取（檔案管線·`常規七 一`）。

受詞 ＝ 本補令 `:71`–`:79`，剝 `> ` 前綴；前置一分隔空列。
🔒 `恆常附款 v①`：標題形須與自誤簿**最近一則**（`自誤 442`）逐字同族——本器當場比對其前綴。
"""
import hashlib
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "549121b27beb6a34b3a6c823af43c78e37b0c7ee"
ORDER5 = "docs/orders/W-G.9-318_補令五_裁3之撤回與自誤443及恆常附款z_aa.md"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
OUT = REPO + r"\verify\out\WG9318p5_ziwu443_payload.md"
A, B = 71, 79


def main():
    src = open(REPO + "\\" + ORDER5.replace("/", "\\"), encoding="utf-8").read().splitlines()
    pay = []
    for ln in src[A - 1:B]:
        pay.append(ln[2:] if ln.startswith("> ") else ("" if ln.strip() == ">" else ln))

    led = subprocess.run(["git", "-c", "core.quotepath=false", "show",
                          "%s:%s" % (REV, LEDGER)], cwd=REPO,
                         capture_output=True).stdout.decode("utf-8")
    prev = [l for l in led.splitlines() if l.startswith("### 🩸 `自誤 ")]
    print("── `恆常附款 v①` 標題形之複刻自證 ──")
    print("  簿內最近一則 ＝ %s…" % prev[-1][:30])
    print("  本 payload 首列 ＝ %s…" % pay[0][:30])
    ok = pay[0].startswith("### 🩸 `自誤 443`　**")
    print("  前綴同族（`### 🩸 \\`自誤 N\\`　**`）：%s" % ok)
    if not ok:
        raise SystemExit("🛑 標題形不符 ⇒ 停機")
    if "443" in led:
        pass
    body = "\n".join(pay) + "\n"
    blob = ("\n" + body).encode("utf-8")
    with open(OUT, "wb") as fh:
        fh.write(blob)
    print("\n── payload ──")
    print("  列數 ＝ %d（含前導分隔空列 1）" % (len(pay) + 1))
    print("  bytes ＝ %d（**含**前導分隔 `\\n` 與末換行·`恆常附款 l②`）" % len(blob))
    print("  sha256 ＝ %s" % hashlib.sha256(blob).hexdigest())
    print("  CR ＝ %d" % blob.count(b"\r"))
    print("  落檔 ＝ %s" % OUT)


if __name__ == "__main__":
    main()
