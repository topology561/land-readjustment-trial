# -*- coding: utf-8 -*-
"""`W-G.9-174 補正①` `N-0-d`：以**入倉後**之證據複現 `W-G.9-174 §零-3`（⛔ 只讀·⛔ 零生產碼）。

受詞 ＝ `verify/out/KL_UI_3.5m_{a3c97aa,2e08a41}_*`（KL 於 `2026-08-30` 三趟 UI 實跑之產物·
來源 ＝ **原始 stdout 存檔**／匯出 CSV）。
🔒 配對一律以 `sha256`（`自誤 211` 之戒 `27`）·⛔ 不以檔名。
"""
import csv
import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
L = []


def say(s=""):
    print(s)
    L.append(s)


def rd(name):
    with open(os.path.join(OUTDIR, name), "rb") as f:
        return f.read()


PAIRS = [
    ("W-D.1.3-d驗收_抵費地情形.csv", 0),
    ("W-B驗收_街角規定範圍面積.csv", 0),
    ("第1宗街角地指配結果.csv", 0),
    ("W-D.1.2診斷_逐候選評點明細.csv", 8),
]
LOGS = [("KL_UI_3.5m_a3c97aa_stdout.log",
         "d45b0b95044f6f9d0266ad8db5d64483bbd61325964c9fb02e0fff6d0dc96f0a", 166385),
        ("KL_UI_3.5m_2e08a41_stdout.log",
         "fe2ba81d698f106683cd3b4cd999015443e01bb9083f502d478aeb9b111f2e76", 166944)]


def main():
    say("=" * 100)
    say("【W-G.9-174 補正① N-0-d】以入倉後之證據複現 §零-3（⛔ 只讀）")
    say("=" * 100)

    say()
    say("── 一、入倉後之 `sha256`／位元組（與 `174 §零-3`／`補正① §一-2` 之表對拍）──")
    say("   %-52s %-64s %10s" % ("入倉檔名", "sha256", "位元組"))
    for nm, h, nb in LOGS:
        b = rd(nm)
        ok = (hashlib.sha256(b).hexdigest() == h) and (len(b) == nb)
        say("   %-52s %-64s %10d %s" % (nm, hashlib.sha256(b).hexdigest(), len(b),
                                        "✅" if ok else "🔴"))
    for base, _ in PAIRS:
        for tag in ("a3c97aa", "2e08a41"):
            nm = "KL_UI_3.5m_%s_%s" % (tag, base)
            b = rd(nm)
            say("   %-52s %-64s %10d" % (nm, hashlib.sha256(b).hexdigest(), len(b)))

    say()
    say("── 二、逐列 `diff`（二態·以入倉後之檔）──")
    diffs = {}
    for base, exp in PAIRS:
        a = rd("KL_UI_3.5m_a3c97aa_%s" % base).decode("utf-8-sig").replace("\r\n", "\n")
        b = rd("KL_UI_3.5m_2e08a41_%s" % base).decode("utf-8-sig").replace("\r\n", "\n")
        la = [x for x in a.split("\n") if x != ""]
        lb = [x for x in b.split("\n") if x != ""]
        import difflib
        d = [x for x in difflib.unified_diff(la, lb, lineterm="", n=0)
             if x[:1] in "+-" and x[:3] not in ("+++", "---")]
        diffs[base] = d
        say("   %-40s 相異列 = **%d**（期望 %d）%s"
            % (base, len(d), exp, "✅" if len(d) == exp else "🔴"))
        say("      位元組全等 = %s"
            % (rd("KL_UI_3.5m_a3c97aa_%s" % base) == rd("KL_UI_3.5m_2e08a41_%s" % base)))

    say()
    say("── 三、`W-D.1.2 診斷` 之逐格差（唯一相異欄須 ＝ `原位次(投影序)`）──")
    base = "W-D.1.2診斷_逐候選評點明細.csv"

    def rows(tag):
        t = rd("KL_UI_3.5m_%s_%s" % (tag, base)).decode("utf-8-sig")
        return list(csv.DictReader(io.StringIO(t)))

    ra, rb = rows("a3c97aa"), rows("2e08a41")
    say("   列數 %d／%d ／ 欄數 %d／%d" % (len(ra), len(rb), len(ra[0]), len(rb[0])))
    key = lambda r: (r["街廓"], r["端"], r["候選地號"])
    ma = {key(r): r for r in ra}
    mb = {key(r): r for r in rb}
    say("   鍵集相同 = %s（|A|=%d |B|=%d）" % (set(ma) == set(mb), len(ma), len(mb)))
    cells, cols = [], set()
    for k in sorted(ma):
        for c in ma[k]:
            if ma[k][c] != mb[k][c]:
                cells.append((k, c, ma[k][c], mb[k][c]))
                cols.add(c)
    say("   逐格相異 = **%d** 格 ／ 相異欄集合 = %r" % (len(cells), sorted(cols)))
    for k, c, va, vb in cells:
        say("      %-28s %-16s %s → %s" % ("／".join(k), c, va, vb))

    say()
    say("── 四、與 `verify/out/WG9167_predicted_diff.json` 之對拍 ──")
    with io.open(os.path.join(OUTDIR, "WG9167_predicted_diff.json"),
                 encoding="utf-8") as f:
        pred = json.load(f)
    txt = json.dumps(pred, ensure_ascii=False)
    say("   預測檔頂層鍵 = %r" % (list(pred)[:8],))
    got = {(k[0], k[2]): (va, vb) for k, c, va, vb in cells}
    say("   本批實得四鍵四值 = %r" % {"／".join(k): "%s→%s" % v for k, v in
                                     {(k[0], k[2]): (va, vb)
                                      for k, c, va, vb in cells}.items()})
    for (blk, lot), (va, vb) in sorted(got.items()):
        pat = re.compile(re.escape(lot))
        say("      `%s`／`%s`：%s→%s ／ 預測檔命中該地號 %d 次"
            % (blk, lot, va, vb, len(pat.findall(txt))))

    say()
    say("── 五、二 stdout log 之 `[T2-DIAG]` 逐字（`§零-2` 之來源）──")
    for nm, _, _ in LOGS:
        t = rd(nm).decode("utf-8").replace("\r\n", "\n")
        ls = [x for x in t.split("\n") if x.startswith("[T2-DIAG]")]
        uniq = sorted(set(ls))
        say("   %s：`[T2-DIAG]` %d 列（相異 %d 列）" % (nm, len(ls), len(uniq)))
        for x in uniq:
            say("      %s" % x)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    rc = main()
    with open(os.path.join(OUTDIR, "probe_WG9174_klui.log"), "w",
              encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    sys.exit(rc)
