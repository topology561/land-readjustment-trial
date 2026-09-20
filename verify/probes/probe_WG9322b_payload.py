# -*- coding: utf-8 -*-
r"""`W-G.9-322 補令一` 工項五：`W-G.9-322R0` 之 payload 抽取（**檔案管線**·`常規七 一`）。

受詞 ＝ 補令之 ```markdown fence 內（`§一` 之 payload）·**⛔ 改一字**。
🔒 界由 fence **自動定位**，⛔ 硬編列號。
"""
import hashlib
import os

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
SRC_ROOT = r"C:\Users\admin\Desktop\land-readjustment-trial"
ORDER = "docs/orders/W-G.9-322_補令一_CC側新窗交接文.md"
OUT = REPO + r"\verify\out\WG9322b_R0_payload.md"


def main():
    # ── 工項零：本補令原封入倉（`追加四` 款一）──
    s = os.path.join(SRC_ROOT, ORDER.replace("/", os.sep))
    d = os.path.join(REPO, ORDER.replace("/", os.sep))
    b = open(s, "rb").read()
    h = hashlib.sha256(b).hexdigest()
    print("══ 工項零　本補令原封入倉")
    print("  bytes **%d**／列 `%d`／`CR` `%d`" % (len(b), b.count(b"\n"), b.count(b"\r")))
    print("  `sha256` `%s`" % h)
    print("  落檔前已存在：%s" % os.path.exists(d))
    with open(d, "wb") as f:
        f.write(b)
    b2 = open(d, "rb").read()
    print("  逐位相符：**%s**" % (b == b2))

    # ── `SELF_SHA256` 之自驗（`P-5` 原口徑）──
    lines = b.split(b"\n")
    idx = max(i for i, l in enumerate(lines) if b"SELF_SHA256" in l)
    subj = b"\n".join(lines[:idx])
    if subj:
        subj += b"\n"
    calc = hashlib.sha256(subj).hexdigest()
    decl = lines[idx].decode("utf-8").split(":")[-1].strip().strip("`")
    print("\n══ `SELF_SHA256` 之自驗（`P-5` 原口徑）")
    print("  受詞 `%d` B／實算 `%s`" % (len(subj), calc))
    print("  單載 `%s`" % decl)
    print("  ⇒ **逐位相符：%s**" % (calc == decl))

    # ── 工項五 payload（fence 自動定位）──
    src = b.decode("utf-8").split("\n")
    fs = [i for i, l in enumerate(src) if l.strip() == "```markdown"]
    fe = [i for i, l in enumerate(src) if l.strip() == "```" and i > fs[0]]
    a, z = fs[0] + 1, fe[0]
    pay = src[a:z]
    print("\n══ 工項五　payload（fence 自動定位·⛔ 硬編列號）")
    print("  ```markdown @ `:%d`／``` @ `:%d` ⇒ payload ＝ `:%d`–`:%d`（**`%d`** 列）"
          % (fs[0] + 1, fe[0] + 1, a + 1, z, len(pay)))
    print("  首列 ＝ %s" % pay[0][:60])
    print("  末列 ＝ %s" % pay[-1][:60])
    body = ("\n".join(pay) + "\n").encode("utf-8")
    with open(OUT, "wb") as f:
        f.write(body)
    print("  落檔 ＝ verify/out/WG9322b_R0_payload.md")
    print("  bytes **%d**／`sha256` `%s`／`CR` `%d`"
          % (len(body), hashlib.sha256(body).hexdigest(), body.count(b"\r")))
    # `§六` 之空節題須在（工項六之錨）
    has6 = any(l.startswith("## `§六`") for l in pay)
    print("  `§六` 空節題在 payload 內：**%s**（工項六之受詞）" % has6)


if __name__ == "__main__":
    main()
