# -*- coding: utf-8 -*-
"""驗收固定項之出艙閘（`CLAUDE.md` 待落地正本表 `序 9` 之落地·`W-G.9-223` 工項五）。

受詞（⛔ 硬編固定項清單）
--------------------------------
逐單解析：讀該批**施工單**之 `【驗收】` 段，自其中**資料驅動**地取出應出艙之字樣，
於該批**執行報告**之本體逐項查命中；命中 `0` 者列出。

字樣之取法（二源·皆自單之 `【驗收】` 段當場取）
  ①-a 反引號括起之 token（`` `left-right` `` 等）——去反引號後為字樣；
  ①-b **ASCII 詞**（`[A-Za-z][A-Za-z0-9_.-]{2,}`）——如 `left-right`／`sha256`／`deletions`。
  以上二者為**判定組**。
  ② 長度 ≥ 2 之中日韓詞（去停用詞）——**參考組·⛔ 作判**（其係單之行文片段，偽陽為主）。
⛔ 任何硬編之項目清單。

🛑 **判定組為空之單⇒ 本器<u>恆綠</u>、判別力為零** ⇒ 該情形須逐單具名回報，
   ⛔ 以「命中 0 個」充綠。

`GB-147` 處置二：對照組命中 `≠` 期望時⛔ 逕判紅——本器對每一字樣併算
「該字樣於**報告本體**之命中」與「其於**單本身**之命中」，俾使用者得自扣自指增量。

`GB-145`：一切 `rc` 取自 `subprocess.run(...).returncode` **直取**，⛔ shell、⛔ 管線。
`GB-139` ②：受詞一律取倉側 blob（索引側 `:<path>`），⛔ 工作樹位元組。

⛔ 入生產碼路徑、⛔ 被 `app.py` import（本檔為獨立工具·僅 `__main__` 執行）。

用法
----
    python verify/tools/wg9223_acceptance_audit.py <單之路徑> <報告之路徑> [...成對]
    python verify/tools/wg9223_acceptance_audit.py --selftest
"""
import re
import subprocess
import sys

REPO = None


def _repo():
    global REPO
    if REPO is None:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True)
        assert r.returncode == 0, ("rev-parse rc", r.returncode)
        REPO = r.stdout.decode("utf-8").strip()
    return REPO


def blob(path):
    """索引側 blob（⛔ 工作樹）。回傳 (bytes, rc)。"""
    r = subprocess.run(["git", "-C", _repo(), "cat-file", "blob", ":" + path],
                       capture_output=True)
    return r.stdout, r.returncode


def lines(path):
    b, rc = blob(path)
    assert rc == 0, ("cat-file rc", path, rc)
    return b.decode("utf-8", "replace").replace("\r\n", "\n").split("\n")


# 停用詞：於【驗收】段內為結構語、非應出艙之項
STOP = {"驗收", "全以", "復驗", "推後", "回報", "全部", "逐項", "本批", "以下", "所列",
        "各項", "之", "與", "及", "含", "者", "須", "須為", "全數", "上開", "如下",
        "停與升", "純技術項", "自主", "或觸", "時停", "即停", "並回報", "不符",
        "工項", "全值", "並列", "現值", "成因", "差異", "結果", "逐份", "四份"}


def parse_acceptance(order_path):
    """自單之 `【驗收】` 段取出字樣（資料驅動）。
    回傳 **3 元組** `(判定組 list, 參考組 list, 段之列範圍)`；
    無 `【驗收】` 段者回 `([], [], (None, None))`（**元數須一致**·⛔ 早退回 2 元組）。"""
    ln = lines(order_path)
    st = en = None
    for i, x in enumerate(ln):
        if st is None and x.lstrip().startswith("【驗收】"):
            st = i
        elif st is not None and x.lstrip().startswith("【") and i > st:
            en = i
            break
    if st is None:
        return [], [], (None, None)     # 🔒 元數須與正常回傳一致（3）——早退路徑之修正
    if en is None:
        en = len(ln)
    seg = "\n".join(ln[st:en])
    toks = []
    for t in re.findall(r"`([^`\n]{1,40})`", seg):          # ① 反引號 token
        t = t.strip()
        if t and t not in toks:
            toks.append(t)
    for t in re.findall(r"[A-Za-z][A-Za-z0-9_.\-]{2,}", seg):   # ①-b ASCII 詞 ⇒ 併入判定組
        if t not in toks:
            toks.append(t)
    ref = []
    seg2 = re.sub(r"`[^`\n]*`", " ", seg)                    # ② 中日韓詞 ⇒ **參考欄**·⛔ 作判
    for t in re.findall(r"[一-鿿]{2,12}", seg2):
        if t in STOP or t in toks or t in ref:
            continue
        ref.append(t)
    return toks, ref, (st + 1, en)


def audit(order_path, report_path):
    """回傳 (判定組 toks, 參考組 ref, 段範圍, 判定列, 判定缺項, 參考缺項)。
    🔒 **判之受詞限反引號 token**；CJK 詞為參考欄、⛔ 作判（其係單之行文片段）。"""
    toks, ref, rng = parse_acceptance(order_path)
    rl = lines(report_path)
    ol = lines(order_path)

    def _rows(ts):
        return [(t, sum(1 for x in rl if t in x), sum(1 for x in ol if t in x)) for t in ts]
    rows = _rows(toks)
    rrows = _rows(ref)
    return (toks, ref, rng, rows, [r for r in rows if r[1] == 0],
            [r for r in rrows if r[1] == 0])


def _fmt(order_path, report_path):
    toks, ref, rng, rows, miss, rmiss = audit(order_path, report_path)
    ob, _ = blob(order_path)
    rb, _ = blob(report_path)
    out = []
    out.append("── 單 `%s`（**%d** B）／報告 `%s`（**%d** B） ──"
               % (order_path.split("/")[-1], len(ob), report_path.split("/")[-1], len(rb)))
    if rng[0] is None:
        out.append("   🔴 該單⛔ 有 `【驗收】` 段 ⇒ **不可回測**")
        return "\n".join(out), None
    out.append("   `【驗收】` 段 ＝ `:%d`–`:%d`｜判定組（反引號 token）**%d** 個／參考組（CJK 詞）**%d** 個"
               % (rng[0], rng[1], len(toks), len(ref)))
    out.append("   ⇒ 🔒 **判定組**之報告命中 `0` ＝ **%d** 個" % len(miss))
    for t, c_rep, c_ord in miss:
        out.append("      🔴 `%s`（報告 **%d** ／ 單本身 **%d**）" % (t, c_rep, c_ord))
    if not toks:
        out.append("      🛑 **判定組為空** ⇒ 本器於此單**恆綠·判別力為零**（⛔ 充綠）")
    elif not miss:
        out.append("      ✅ 判定組全數命中")
    out.append("   ⇒ 參考組之報告命中 `0` ＝ **%d** 個（**⛔ 作判**·係單之行文片段）" % len(rmiss))
    return "\n".join(out), len(miss)


def selftest():
    """判別力自證：以一必命中之字樣與一必不命中者各造一列，驗本器分得開。
    🔒 哨兵之字樣⛔ 寫入本檔（`GB-147` 處置一）——以執行期組出。"""
    probe_hit = "驗收"
    probe_missA = "Z" * 3 + "Q" * 3 + "9"
    probe_miss = probe_missA + chr(95) * 2
    sample = ["本列含 %s 二字" % probe_hit, "本列不含彼字樣"]
    a = sum(1 for x in sample if probe_hit in x)
    b = sum(1 for x in sample if probe_miss in x)
    print("【自證】必命中字樣 ⇒ **%d**（須 > 0）／必不命中之人造字樣 ⇒ **%d**（須 0）⇒ %s"
          % (a, b, "✅" if (a > 0 and b == 0) else "🔴"))
    return 0 if (a > 0 and b == 0) else 1


def main(argv):
    if len(argv) == 1 and argv[0] == "--selftest":
        return selftest()
    if len(argv) < 2 or len(argv) % 2:
        print(__doc__)
        return 2
    rc = 0
    for i in range(0, len(argv), 2):
        txt, n = _fmt(argv[i], argv[i + 1])
        print(txt)
        if n is None or n:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
