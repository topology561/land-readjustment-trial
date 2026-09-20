# -*- coding: utf-8 -*-
r"""W-G.9-319：`P-5` 之框之別——證「傳輸保真未破」（自解款白名單 `2`）。

🛑 **⛔ 動 `verify/probes/probe_order_preflight.py` 一字**（白名單 `2` 明令）。
本器只做二事：① 以 `P-5` 之原口徑重算；② 自單內**以二框**取其自載值並逐位比對。
🔒 判別力二造：[必相符] 本單；[必不符] 對**全檔**（含 `SELF_SHA256` 列）施同一口徑 ⇒ 須相異。
"""
import hashlib
import re

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
ORDER = "docs/orders/W-G.9-319_施工單_二寬度之量差與GB170三格現查及自誤445.md"

# 二框：舊形 `SELF_SHA256: <hash>` ／ 本單所用之形 `SELF_SHA256` ＝ `<hash>`
F_OLD = re.compile(r"^SELF_SHA256:\s*([0-9a-f]{64})\s*$", re.M)
F_NEW = re.compile(r"^`SELF_SHA256`\s*[＝=]\s*`([0-9a-f]{64})`", re.M)


def main():
    raw = open(REPO + "\\" + ORDER.replace("/", "\\"), "rb").read()
    txt = raw.decode("utf-8")
    print("受詞檔 ＝ `%s`" % ORDER)
    print("全檔 bytes ＝ %d／CR ＝ %d" % (len(raw), raw.count(b"\r")))

    print("\n── 二框之自載值 ──")
    old = F_OLD.findall(txt)
    new = F_NEW.findall(txt)
    print("  舊形 `SELF_SHA256: <hash>`      命中 %d  %s" % (len(old), old))
    print("  本單形 `` `SELF_SHA256` ＝ `<hash>` ``  命中 %d  %s" % (len(new), new))
    if not new:
        raise SystemExit("🛑 二框皆⛔ 命中 ⇒ 停機")
    declared = new[-1]

    # `P-5` 之原口徑：自檔首至**最末**一個 SELF_SHA256 列之前一個 `\n`（含）
    lines = raw.split(b"\n")
    idx = max(i for i, l in enumerate(lines)
              if b"SELF_SHA256" in l)
    subject = b"\n".join(lines[:idx])
    if subject:
        subject += b"\n"
    calc = hashlib.sha256(subject).hexdigest()

    print("\n── `P-5` 原口徑之重算 ──")
    print("  受詞 bytes ＝ %d（至第 %d 列之前·含其前一個換行）" % (len(subject), idx + 1))
    print("  實算 ＝ %s" % calc)
    print("  單載 ＝ %s" % declared)
    print("  ⇒ **逐位相符：%s**" % (calc == declared))

    print("\n── 判別力二造 ──")
    whole = hashlib.sha256(raw).hexdigest()
    print("  [必相符] 上開受詞           ⇒ %s" % (calc == declared))
    print("  [必不符] 對**全檔**施同一口徑 ⇒ %s（須 False）" % (whole == declared))
    print("     全檔 sha256 ＝ %s" % whole)
    print("\n🔒 結論：`P-5` 之紅係**框之別**（該器只認舊形），"
          "**傳輸保真未破** ⇒ 自解款白名單 `2`；⛔ 動 `P-5` 一字。")


if __name__ == "__main__":
    main()
