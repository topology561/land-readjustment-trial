# -*- coding: utf-8 -*-
"""W-G.9-318 補令四：`§二` 恆常附款簿之組建（逐字由檔案管線抽取·`常規七 一`）。

🛑 本器**⛔ 改寫任何條文**：每一款之逐字皆以 `(檔, 起, 迄)` 自倉側 blob 抽出。
🔒 `所繫之自誤號`**機械導出**——定義處在自誤簿者取其**最近之前一則** `### 🩸 自誤 N` 標題；
   定義處在單者取其行內之 `（自誤 NNN）` 標記。⛔ 由 CC 指派。
"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "bc97c9d72d1680e820872aba787ecc453fa3a509"

O308B = "docs/orders/W-G.9-308_補令一_K-9-38與K-9-39之鑄及自誤420至421與款4之靜態結案.md"
O310 = "docs/orders/W-G.9-310_施工單_K-9-40之鑄與三則末端註記及自誤422.md"
O311 = "docs/orders/W-G.9-311_施工單_修批前置之現態診斷與自誤423_424.md"
O312 = "docs/orders/W-G.9-312_施工單_步驟0二態對拍與自誤425.md"
O313 = "docs/orders/W-G.9-313_施工單_自誤426與312二態對拍之登記.md"
O314 = "docs/orders/W-G.9-314_施工單_自誤427與428之鑄及恆常附款jk之立.md"
O315 = "docs/orders/W-G.9-315_施工單_K-9-5-12反事實之態乙驅動與自誤429.md"
O316 = "docs/orders/W-G.9-316_施工單_W0消費者定位與項5補測及自誤430_431.md"
O317 = "docs/orders/W-G.9-317_施工單_K-9-41之鑄與落地前最後定位及自誤432.md"
O318B = "docs/orders/W-G.9-318_補令一_forced側之避讓與自誤434至438.md"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
ORDER4 = "docs/orders/W-G.9-318_補令四_復驗受領與恆常附款簿及自誤442.md"

# 款 → (檔, 起列, 迄列)　※ 迄列含
MAP = [
    ("a", O308B, 82, 82), ("b", O308B, 83, 83), ("c", O308B, 84, 84),
    ("d", O310, 83, 86),
    ("e", O311, 89, 89), ("f", O311, 90, 90),
    ("g", O312, 90, 90),
    ("h", O313, 82, 82), ("i", O313, 83, 83),
    ("j", O314, 96, 99), ("k", O314, 101, 104),
    ("l", O315, 98, 102),
    ("m", O316, 99, 99), ("n", O316, 100, 100),
    ("o", O317, 99, 99),
    ("p", LEDGER, 10659, 10662),
    ("q", O318B, 109, 109), ("r", O318B, 114, 114), ("s", O318B, 118, 118),
    ("t", O318B, 122, 122), ("u", O318B, 129, 129),
    ("v", LEDGER, 10701, 10704),
    ("w", LEDGER, 10727, 10730),
]

ZIWU_HEAD = re.compile(r"^###\s*🩸?\s*`?自誤\s*`?([0-9]{1,4})`?")


def blob(path, rev=REV):
    p = subprocess.run(["git", "show", "%s:%s" % (rev, path)],
                       cwd=REPO, capture_output=True)
    if p.returncode != 0:
        raise SystemExit("🔴 讀不到 %s@%s" % (path, rev[:7]))
    return p.stdout.decode("utf-8").splitlines()


def main():
    cache = {}
    for _, f, _, _ in MAP:
        if f not in cache:
            cache[f] = blob(f)
    cache[ORDER4] = open(REPO + "\\" + ORDER4.replace("/", "\\"),
                         encoding="utf-8").read().splitlines()

    # ── 所繫自誤號之機械導出 ──
    tie = {}
    for ch, f, a, b in MAP:
        lines = cache[f]
        if f == LEDGER:
            n = None
            for j in range(a - 1, -1, -1):
                m = ZIWU_HEAD.match(lines[j])
                if m:
                    n = m.group(1)
                    break
            tie[ch] = ("自誤 %s" % n) if n else "⛔ 導出"
        else:
            body = "\n".join(lines[a - 1:b])
            m = re.search(r"`自誤 ([0-9]{1,4})`", body)
            if m:
                tie[ch] = "自誤 %s" % m.group(1)
            else:
                m2 = re.search(r"（(§零-2 裁 `?\d+`?|`?W-G\.9-\d+R`? 自捕 `?\d+`?)", body)
                tie[ch] = m2.group(1) if m2 else "⛔ 繫自誤號"

    print("── 所繫自誤號之機械導出 ──")
    for ch, _, _, _ in MAP:
        print("  款 `%s` → %s" % (ch, tie[ch]))

    # ── 逐字塊之落檔（供簿之附錄轉錄）──
    out = []
    for ch, f, a, b in MAP:
        out.append("§ 款 `%s`　出處 ＝ `%s:%d`%s" %
                   (ch, f, a, ("–`:%d`" % b) if b > a else ""))
        for k in range(a - 1, b):
            out.append(cache[f][k])
        out.append("")
    with open(REPO + r"\verify\out\WG9318p4_clauses_verbatim.txt", "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out))
    print("\n逐字塊已落檔 ＝ verify/out/WG9318p4_clauses_verbatim.txt（%d 列）" % len(out))

    # ── 自誤 442 之 payload（自本補令 :135–141 抽·剝除 `> ` 前綴）──
    src = cache[ORDER4][134:141]
    payload = []
    for ln in src:
        payload.append(ln[2:] if ln.startswith("> ") else ("" if ln.strip() == ">" else ln))
    with open(REPO + r"\verify\out\WG9318p4_ziwu442_payload.txt", "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(payload))
    print("自誤 442 payload 已落檔（%d 列·剝 `> ` 前綴）" % len(payload))
    print("  首列 ＝ %s" % payload[0][:70])

    # ── 款 x 之逐字（本補令 :144·剝 `> `）──
    xl = cache[ORDER4][143]
    xl = xl[2:] if xl.startswith("> ") else xl
    with open(REPO + r"\verify\out\WG9318p4_clause_x.txt", "w",
              encoding="utf-8", newline="\n") as fh:
        fh.write(xl)
    print("款 `x` 逐字已落檔：%s" % xl[:70])


if __name__ == "__main__":
    main()
