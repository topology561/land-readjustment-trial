#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-269` 補令九 `§二-3`：**交接註「坑」索引**之全倉出艙（**數字系 ⋀ 字母系二系分列**）。

🩸 **本器之存在理由**（補令九 `§二-2` 逐字）
   「發單側交予新窗之開場文令其**逐坑覆述徵候與攔法**——索引不解析，該令即**不可執行**；
     而新窗若**猜**其內容或**略過**之，即等於把一條攔法當成已執行（`自誤 347` 之族）。」

🔒 **框之具名**（補令九 `§二-3` 款 `1`：🛑 框須具名·⛔ 裸框）
   **定義處**（其一即足·**聯集**）：
     `D-H` **標題形** ＝ `^#{1,6}` … `坑` … 標籤（標籤得帶反引號）
     `D-T` **坑表之資料列** ＝ 一 markdown 表，其**表頭列**同時含 `徵候` ⋀ `攔法`
            ⇒ 其分隔列以下之各資料列，**首格**（去反引號／星號／空白）即該坑之標籤。
            🔒 **本形係發單側之框所<u>漏</u>者**——`前置階 §丁` 之坑表其首欄為 `#`、
               標籤格⛔ 冠「坑」字（`| \x60a\x60 | …`）⇒ `| **坑 X**` 之框必失配。
   **引用處** ＝ 文中 `坑` ＋ 選擇性空白 ＋ 標籤（帶或不帶反引號·**二形並取**·`GB-158`），
                 且**⛔ 落於任一定義處之列**。

🔒 **判別力（補令九 `§二-3` 款 `1` 所令·二造）**
   `(甲)` 一**已知有定義**之坑（`n`）⇒ 其定義處須 `≥ 1`；
   `(乙)` 一**人造之坑**（**執行期組出**·其字面⛔ 出艙·`GB-147`）⇒ 其命中須 `0`。
   🛑 二造任一不如預期 ⇒ **量測器紅** ⇒ ⛔ 出艙任何索引（`坑 u`／`常規五`）。

🔒 **`形／徵候／攔法` 是否齊備**（款 `1` 所令之第三欄）
   `D-H`：自該標題至**次一同級或更高級標題**之間，三字樣**逐一**檢其在否。
   `D-T`：表頭之欄名集合含 `徵候` ⋀ `攔法` ⇒ 檢該列對應格**非空**；`形` 以**首格之後**之描述欄充之。

用法：`python verify/probes/probe_WG9269_pit_index.py <rev> [<rev2> …]`
`rc`：`0` 全綠／`2` **量測器紅**（二造不如預期 ⇒ loud 拒測）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」（`坑 9`）。
"""
import re
import subprocess
import sys

BT = chr(96)                                   # 反引號·⛔ 令其經 bash 一層（`坑 7`）
W = 112

NUM_LABELS = [str(i) for i in range(1, 27)]    # 數字系 1〜26
# 字母系：`a`〜`z` ＋ 二字母形 `aa`〜`ak`
#   🔒 `y`／`z`／`aa`／`ab`／`ac` 係 `W-G.9-269` 補令十二段 `§二` 所立（本波末五坑）。
#   🛑 **二字母形⛔ 與單字母形相混**——`D-T` 之比對為**整格相等**（`lab in labels`），
#      引用之框為 `坑 ` ＋ 反引號 ＋ 標籤 ＋ 反引號 ⇒ `坑 \x60a\x60` ⛔ 命中 `坑 \x60aa\x60`。
#   🔒 `ad`〜`ak` 係 `W-G.9-269` 補令十六段（`c3` 併線之收工交接）所立（本波末八坑）。
#   🔒 `al`〜`ao` 係 `W-G.9-269` 補令十七段（`c4` 之收工交接）所立（本波末四坑）。
ALPHA_LABELS = ([chr(c) for c in range(ord("a"), ord("z") + 1)]
                + ["aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak",
                   "al", "am", "an", "ao"])


def tracked_md(rev):
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", "-z", rev],
                         capture_output=True, check=True).stdout
    return [f for f in out.decode("utf-8").split("\0") if f.endswith(".md")]


def blob_text(rev, path):
    r = subprocess.run(["git", "show", "%s:%s" % (rev, path)],
                       capture_output=True)
    if r.returncode != 0:
        return None
    try:
        return r.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return None


def _strip_cell(s):
    return s.strip().strip("*").strip().strip(BT).strip().strip("*").strip()


def scan_file(text, labels):
    """回 (defs, refs, deflines)。defs/refs ＝ {label: [(列號, 形式, 三項齊備, 摘)]}"""
    lines = text.split("\n")
    defs, refs = {}, {}
    deflines = set()

    # ── D-H 標題形 ───────────────────────────────────────────────────
    hrx = re.compile(r"^(#{1,6})[^\n]*?坑[\s\u3000]*" + BT + r"?([0-9a-z][0-9a-z\-]*)"
                     + BT + r"?")
    heads = []
    for i, ln in enumerate(lines):
        m = hrx.match(ln)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
    for k, (i, lvl, lab) in enumerate(heads):
        if lab not in labels:
            continue
        end = len(lines)
        for j, ln in enumerate(lines[i + 1:], start=i + 1):
            hm = re.match(r"^(#{1,6})\s", ln)
            if hm and len(hm.group(1)) <= lvl:
                end = j
                break
        body = "\n".join(lines[i:end])
        trio = ("形" in body, "徵候" in body, "攔法" in body)
        # 🔴 **標題含該坑 ⇏ 該標題即其定義**——`補令八:43` 之
        #    `### 二-3　立準（承 CC 之坑 \x60m\x60）` 係**引用**、⛔ 定義。
        #    ⇒ `D-H` 僅於**三項齊備**時計為定義；否則歸引用（⛔ 入 `deflines`）。
        if all(trio):
            defs.setdefault(lab, []).append((i + 1, "D-H", trio, lines[i].strip()[:70]))
            deflines.add(i)

    # ── D-T 坑表之資料列 ─────────────────────────────────────────────
    for i, ln in enumerate(lines):
        if not re.match(r"^\s*\|[\s:\-\|]+\|\s*$", ln):      # 分隔列
            continue
        if i == 0:
            continue
        hdr = lines[i - 1]
        if not hdr.strip().startswith("|"):
            continue
        cols = [c.strip() for c in hdr.strip().strip("|").split("|")]
        joined = "".join(cols)
        if not ("徵候" in joined and "攔法" in joined):
            continue
        try:
            ci_x = next(k for k, c in enumerate(cols) if "徵候" in c)
            ci_l = next(k for k, c in enumerate(cols) if "攔法" in c)
        except StopIteration:                                 # pragma: no cover
            continue
        for j in range(i + 1, len(lines)):
            row = lines[j]
            if not row.strip().startswith("|"):
                break
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if not cells:
                break
            lab = _strip_cell(cells[0])
            lab = re.sub(r"^坑[\s\u3000]*", "", lab).strip(BT).strip()
            if lab in labels:
                ok_x = len(cells) > ci_x and _strip_cell(cells[ci_x]) != ""
                ok_l = len(cells) > ci_l and _strip_cell(cells[ci_l]) != ""
                shape = len(cells) > 1 and _strip_cell(cells[1]) != ""
                if not (ok_x and ok_l):
                    continue
                defs.setdefault(lab, []).append(
                    (j + 1, "D-T", (shape, ok_x, ok_l), row.strip()[:70]))
                deflines.add(j)

    # ── 引用處（⛔ 落於定義列）────────────────────────────────────────
    for lab in labels:
        pats = ["坑 " + BT + lab + BT, "坑 " + lab]
        for i, ln in enumerate(lines):
            if i in deflines:
                continue
            hit = False
            if pats[0] in ln:
                hit = True
            else:
                for m in re.finditer(r"坑[\s\u3000]*" + re.escape(lab), ln):
                    tail = ln[m.end():m.end() + 1]
                    if not re.match(r"[0-9a-zA-Z\-]", tail):
                        hit = True
                        break
            if hit:
                refs.setdefault(lab, []).append((i + 1, ln.strip()[:70]))
    return defs, refs


def run(rev, labels, title):
    files = tracked_md(rev)
    D, R = {}, {}
    for f in files:
        t = blob_text(rev, f)
        if t is None:
            continue
        d, r = scan_file(t, labels)
        for k, v in d.items():
            D.setdefault(k, []).extend((f,) + x for x in v)
        for k, v in r.items():
            R.setdefault(k, []).extend((f,) + x for x in v)
    print("")
    print("── %s ── 母體 ＝ %s 之追蹤 `.md` **%d** 檔" % (title, rev[:7], len(files)))
    print("   | 坑 | 定義處 | 形／徵候／攔法 | 引用處 | 判 |")
    print("   |---|---|---|---|---|")
    for lab in labels:
        ds, rs = D.get(lab, []), R.get(lab, [])
        if ds:
            f, ln, form, trio, _s = ds[0]
            t3 = "".join("✅" if b else "🔴" for b in trio)
            dtxt = "`%s:%d`（%s）%s" % (f.split("/")[-1], ln, form,
                                       "＋%d" % (len(ds) - 1) if len(ds) > 1 else "")
            judge = "✅ 可解析" if all(trio) else "🟡 定義在·三項缺"
        else:
            t3 = "—"
            dtxt = "🔴 **`0`**"
            judge = "🔴 **⛔ 可解析**" if rs else "⚪ 未用"
        print("   | `%s` | %s | %s | `%d` | %s |" % (lab, dtxt, t3, len(rs), judge))
    # 🔒 定義處為 `0` 而有引用者 ⇒ 逐筆出艙其引用（補令九 `§二-3` 款 `1`：引用處逐筆）
    orphan = [l for l in labels if not D.get(l) and R.get(l)]
    if orphan:
        print("")
        print("   🔴 **定義處 ＝ `0` 而有引用者**（逐筆·款 `1` 所令）")
        for lab in orphan:
            print("     坑 `%s`（引用 %d 筆）" % (lab, len(R[lab])))
            for f, ln, s in R[lab]:
                print("       `%s:%d`　%s" % (f, ln, s))
    return D, R


def issuer_frame(rev, labels, title):
    """🔒 **二框對照**（補令二 `§三`：二方之數相異 ⇒ **先對齊母體再判孰誤**·⛔ 逕判他方有誤）。

    受詞 ＝ 補令九 `§二-1` 所**逐字**具名之框：「列首為 `#### 坑 X` 或 `| **坑 X**`」。
    併列 ＝ 前窗（`W-G.9-269R_本體階_新窗開工與c2前置.md` `§三-2`）所用之框：字串 `坑 ` ＋ 標籤。
    """
    files = tracked_md(rev)
    A = {l: 0 for l in labels}        # 補令九 §二-1 之框
    B = {l: 0 for l in labels}        # 前窗之框（字串 `坑 X`·二形並取）
    for f in files:
        t = blob_text(rev, f)
        if t is None:
            continue
        for ln in t.split("\n"):
            for lab in labels:
                if re.match(r"^#### 坑 " + BT + r"?" + re.escape(lab) + BT + r"?", ln) \
                        or re.match(r"^\|\s*\*\*坑 " + BT + r"?" + re.escape(lab)
                                    + BT + r"?\*\*", ln):
                    A[lab] += 1
                if ("坑 " + BT + lab + BT) in ln:
                    B[lab] += 1
    print("")
    print("── 二框對照：%s（母體同上·**列框**）" % title + "─" * 30)
    print("   | 框 | 定義處合計 | 得 `0` 之標籤 |")
    print("   |---|---|---|")
    zc = [l for l in labels if A[l] == 0]
    print("   | 補令九 `§二-1` 之框（`#### 坑 X` ∪ `\\| **坑 X**`） | `%d` | %s |"
          % (sum(A.values()), ("**全部 %d 個**" % len(zc)) if len(zc) == len(labels)
             else "`%s`" % ", ".join(zc) if zc else "（無）"))
    zb = [l for l in labels if B[l] == 0]
    print("   | 前窗之框（字串 `坑 ` ＋ 標籤） | `%d` | %s |"
          % (sum(B.values()), "`%s`" % ", ".join(zb) if zb else "（無）"))


def main():
    revs = sys.argv[1:] or ["HEAD"]
    print("=" * W)
    print("【`W-G.9-269` 補令九 `§二-3`】交接註「坑」索引（全倉·二系分列）")
    print("=" * W)
    print("🔒 框（逐字）：定義處 ＝ `D-H` 標題形 ∪ `D-T` 坑表資料列"
          "（表頭含 `徵候` ⋀ `攔法`）；引用處 ＝ 文中「坑 ＋ 標籤」二形並取·⛔ 落於定義列")

    rc = 0
    for rev in revs:
        files = tracked_md(rev)
        # ── 判別力二造（**先跑先判**·`坑 u`）───────────────────────
        fake = "z" + "".join(chr(c) for c in (57, 57))       # 執行期組出·字面⛔ 出艙
        Dc, Rc = {}, {}
        for f in files:
            t = blob_text(rev, f)
            if t is None:
                continue
            d, r = scan_file(t, ["n", fake])
            for k, v in d.items():
                Dc.setdefault(k, []).extend(v)
            for k, v in r.items():
                Rc.setdefault(k, []).extend(v)
        c_ok = len(Dc.get("n", [])) >= 1
        c_zero = (len(Dc.get(fake, [])) == 0 and len(Rc.get(fake, [])) == 0)
        print("")
        print("── 判別力二造（`rev` ＝ %s）" % rev[:7] + "─" * 60)
        print("   造甲[必有定義] 坑 `n`            ⇒ 定義處 %d ／ 期 ≥ 1 ⇒ %s"
              % (len(Dc.get("n", [])), "✅" if c_ok else "🔴"))
        print("   造乙[必為零] 人造之坑（**執行期組出**·字面⛔ 出艙）⇒ 定義 %d ／引用 %d"
              " ／ 期 0／0 ⇒ %s"
              % (len(Dc.get(fake, [])), len(Rc.get(fake, [])), "✅" if c_zero else "🔴"))
        if not (c_ok and c_zero):
            print("   🔴 **二造未全如預期 ⇒ 量測器紅 ⇒ loud 拒測**（⛔ 出艙索引）")
            rc = 2
            continue
        print("   ⇒ **器非紅** ✅")
        run(rev, NUM_LABELS, "數字系 `1`〜`26`")
        run(rev, ALPHA_LABELS, "字母系 `a`〜`z` ＋ `aa`〜`ak`")
        issuer_frame(rev, NUM_LABELS, "數字系 `1`〜`26`")
        issuer_frame(rev, ALPHA_LABELS, "字母系 `a`〜`z` ＋ `aa`〜`ak`")
    return rc


if __name__ == "__main__":
    sys.exit(main())
