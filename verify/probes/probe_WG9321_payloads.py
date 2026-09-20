# -*- coding: utf-8 -*-
r"""`W-G.9-321` 工項一：`自誤 449` 之 payload 抽取（**檔案管線**·`常規七 一`）。

受詞 ＝ 單之 ```markdown fence 內（`:193`–`:204`）·**⛔ 增刪一字·⛔ 改標點**（單 `§二` 明文）。
🔒 `恆常附款 v`：標題形與自誤簿**最近一則**（`自誤 448`）當場比對其前綴。
🔒 `v②`：以二框自驗，須皆命中。
"""
import hashlib
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "d9df12bad5441ec3e1df7819c17e6de9b8e8f10c"
ORDER = "docs/orders/W-G.9-321_輕量單.md"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
OUT = REPO + r"\verify\out\WG9321_ziwu449_payload.md"

RE_SELF = re.compile(r"^#{1,6} [^\w`]{0,6}`?自誤 `?(\d+)`?`?\s*[｜（\u3000:：]")
RE_CANON = re.compile(r"^#+[^0-9０-９（(\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?")


def main():
    src = open(REPO + "\\" + ORDER.replace("/", "\\"), encoding="utf-8").read().split("\n")
    # 以 fence 為界自動定位（⛔ 硬編列號之唯一依賴）
    fs = [i for i, l in enumerate(src) if l.strip() == "```markdown"]
    fe = [i for i, l in enumerate(src) if l.strip() == "```" and i > fs[0]]
    a, b = fs[0] + 1, fe[0]
    pay = src[a:b]
    print("# `W-G.9-321` `自誤 449` payload 之抽取")
    print("fence 定位：```markdown @ `:%d`／``` @ `:%d` ⇒ payload ＝ `:%d`–`:%d`（`%d` 列）"
          % (fs[0] + 1, fe[0] + 1, a + 1, b, len(pay)))

    led = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (REV, LEDGER)],
                         capture_output=True).stdout.decode("utf-8")
    prev = [l for l in led.split("\n") if l.startswith("### 🩸 `自誤 ")]
    print("\n🔒 `v` 範本（簿內最近一則）＝ %s…" % prev[-1][:42])
    print("   本 payload 首列       ＝ %s…" % pay[0][:42])
    ok = pay[0].startswith("### 🩸 `自誤 449`　**")
    print("   ⇒ 前綴同族：**%s**" % ok)
    if not ok:
        raise SystemExit("🛑 標題形不符 ⇒ 停機")
    m1, m2 = RE_SELF.match(pay[0]), RE_CANON.match(pay[0])
    print("🔒 `v②` 二框自驗：自擬框 **%s**（%s）／正典框 **%s**（%s）"
          % (bool(m1), m1.group(1) if m1 else "—", bool(m2), m2.group(1) if m2 else "—"))
    print("   判別力［必不命中］：一非標題列（`**形**：` 列）⇒ 自擬框 **%s**／正典框 **%s**"
          % (bool(RE_SELF.match(pay[2])), bool(RE_CANON.match(pay[2]))))
    if not (m1 and m2):
        raise SystemExit("🛑 二框自驗不過 ⇒ 停機")

    body = ("\n" + "\n".join(pay) + "\n").encode("utf-8")
    with open(OUT, "wb") as f:
        f.write(body)
    print("\n落檔 ＝ verify/out/WG9321_ziwu449_payload.md")
    print("  bytes **%d**（含前導分隔 `\\n` 與末換行·`恆常附款 l②`）｜`sha256` `%s`｜`CR` %d"
          % (len(body), hashlib.sha256(body).hexdigest(), body.count(b"\r")))
    print("  末列 ＝ %s" % pay[-1][:70])


if __name__ == "__main__":
    main()
