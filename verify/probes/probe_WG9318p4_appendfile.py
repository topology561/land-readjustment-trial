# -*- coding: utf-8 -*-
r"""W-G.9-318 補令四：通用之**嚴格末端追加**器（`append-only` 之判**三值化**·`恆常附款 x`）。

用法：`probe_WG9318p4_appendfile.py <倉內路徑> <payload 檔> [--apply]`
🔒 期初須 ＝ 開工態 `bc97c9d…` 之 blob；不符即停機。
🔒 出艙四造（`恆常附款 j③`）：前綴逐位／payload 逐位／bytes 算式／期末 `sha256`。
"""
import hashlib
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "bc97c9d72d1680e820872aba787ecc453fa3a509"


def main():
    rel, payfile = sys.argv[1], sys.argv[2]
    apply = "--apply" in sys.argv
    tgt = REPO + "\\" + rel.replace("/", "\\")

    p = subprocess.run(["git", "show", "%s:%s" % (REV, rel)],
                       cwd=REPO, capture_output=True)
    exists = p.returncode == 0
    base = p.stdout if exists else b""
    before = open(tgt, "rb").read()

    print("受詞 ＝ `%s`" % rel)
    print("── 期初（**三值**·`恆常附款 x`）──")
    print("  開工態 `%s` 之 blob：%s（%d B）"
          % (REV[:7], "存在" if exists else "⛔ 存在（新檔）", len(base)))
    print("  工作區 bytes ＝ %d" % len(before))
    print("  工作區 ＝ 開工態 blob：%s" % (before == base))
    if before != base:
        raise SystemExit("🛑 期初與開工態不符 ⇒ 停機")

    payload = open(payfile, "rb").read().replace(b"\r\n", b"\n")
    print("\n── payload ──")
    print("  bytes ＝ %d（含末換行）／列 ＝ %d／CR ＝ %d"
          % (len(payload), payload.count(b"\n"), payload.count(b"\r")))
    print("  sha256 ＝ %s" % hashlib.sha256(payload).hexdigest())

    after = before + payload
    print("\n── 期末之期值（算式）──")
    print("  期末 bytes ＝ 期初 %d ＋ payload %d ＝ **%d**"
          % (len(before), len(payload), len(after)))
    if not apply:
        print("\n（乾跑·未落檔）")
        return
    with open(tgt, "wb") as fh:
        fh.write(after)
    now = open(tgt, "rb").read()
    print("\n── 落檔後之機驗（四造）──")
    print("  ① append-only 嚴格前綴逐位 ：%s" % (now[:len(before)] == before))
    print("  ② payload 逐位相符        ：%s" % (now[len(before):] == payload))
    print("  ③ 期末 bytes ＝ 期初 ＋ payload：%s（%d）" % (len(now) == len(after), len(now)))
    print("  ④ 期末 sha256 ＝ %s" % hashlib.sha256(now).hexdigest())
    print("  CR 全檔 ＝ %d" % now.count(b"\r"))


if __name__ == "__main__":
    main()
