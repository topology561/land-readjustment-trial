# -*- coding: utf-8 -*-
"""W-G.9-318 補令四：開工閘之量測器（唯讀·⛔ 動任何既有檔）。

受詞
  · 閘 `7`  生產碼 `34` 檔之 blob 錨（正面列舉·⛔ 空 pathspec）
  · 閘 `8`  四簿之**二框並報**（母體逐簿單檔）
  · 閘 `10` 取號現查：`自誤 442`（意指占用·**二形並取**·`GB-158`）／`恆常附款 x`（字母框·二形並取）

🛑 本器**唯讀**：一切量測取自 `git show <態>:<path>` 之倉側 blob，⛔ 讀工作區。
🔒 對照組（`常規五`／`常規四（七）補款二 二`）：每一計數皆附【必非零】與【必為零】二造；
   人造哨兵**執行期組出並當場自證其為真零**，字面⛔ 落入本檔、亦⛔ 落入 log。

🩸 本器之四項自捕（首版皆紅·已修·`W-G.9-318R4p` §自捕）
  ① `GB` 框過窄（`^#{2,4}` ⇒ 相異 `96`）⇒ 增列**裸錨定框**並二框並報。
  ② 對 `自誤 N` 套用宣告框 `⑤`／`⑨`（其受詞 ＝ **單號 ＝ 檔名之號**）⇒ 對照甲得 `0` ⇒ 量測器紅。
     改用**意指占用**之錨定框（母體 ＝ 全倉追蹤 `.md`）＋ 自誤簿單檔之正典定義框。
  ③ 哨兵取既存之人造受詞 ⇒ 對照乙非零 ⇒ 改為執行期搜出之真零號。
  ④ 字母框僅取帶反引號之一形 ⇒ 與裁 `3` 之 `b`／`e` 不符 ⇒ 改**二形並取**。
"""
import hashlib
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"

PROD34 = ["app.py"] + ["verify/" + n for n in [
    "app_harvest.py", "b6_isomorphism.py", "fixture_baseline_candidates.py",
    "fixture_block_depth_n19p.py", "fixture_cad_binding_order.py",
    "fixture_corner_range_k8.py", "fixture_e2e_termination.py",
    "fixture_end_fallback.py", "fixture_end_reserve.py", "fixture_end_winner.py",
    "fixture_g3_static_guards.py", "fixture_klui_t2diag.py",
    "fixture_midlayer_6items.py", "fixture_n14_feed_chain.py",
    "fixture_n14_min_width.py", "fixture_wf_ns_wiring.py",
    "fixture_yi_construction.py", "run_all.py", "run_verification.py",
    "selection_pipeline.py", "stepg_pipeline.py", "test_corner_first_lot_G.py",
    "wd3_fragment_geom.py", "wd4_tier_list.py", "wf_f0.py", "wf_f1.py",
    "wf_f2.py", "wf_f3.py", "wf_f4.py", "wg_g1_smoke.py", "wg_g2_smoke.py",
    "wg_g3.py", "wv_reconcile.py"]]

LEDGER_ZIWU = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
LEDGER_GB = "docs/reports/W-G.4_泛用阻塞項登記表.md"
LEDGER_VR = "docs/驗證裁定登記表.md"
LEDGER_K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"

OWN = {"docs/orders/W-G.9-318_補令四_復驗受領與恆常附款簿及自誤442.md",
       "docs/reports/W-G.9波_恆常附款登記表.md"}


def run(args):
    return subprocess.run(args, cwd=REPO, capture_output=True)


def git_text(rev, path):
    p = run(["git", "show", "%s:%s" % (rev, path)])
    if p.returncode != 0:
        raise RuntimeError("git show 失敗 %s:%s" % (rev, path))
    return p.stdout.decode("utf-8")


def ls_md(rev):
    """母體 ＝ 倉側**全倉追蹤 `.md`**（⛔ `grep -r .`·常規補款二）。"""
    p = run(["git", "-c", "core.quotepath=false", "ls-tree", "-r",
             "--name-only", rev])
    return [x for x in p.stdout.decode("utf-8").splitlines() if x.endswith(".md")]


# ══════════════════════════ 閘 7 ══════════════════════════
def gate7(rev):
    print("\n══ 閘 `7`　生產碼 `34` 檔之 blob 錨 ══")
    print("母體 ＝ 正面列舉 **`%d`** 檔（⛔ 空 pathspec）" % len(PROD34))
    assert len(PROD34) == 34
    rows, miss = [], []
    for path in PROD34:
        p = run(["git", "rev-parse", "%s:%s" % (rev, path)])
        if p.returncode != 0:
            miss.append(path)
            continue
        blob = p.stdout.decode().strip()
        sz = int(run(["git", "cat-file", "-s", blob]).stdout.decode().strip())
        rows.append((path, blob, sz))
    print("存在 ＝ `%d`／缺 ＝ `%d`  %s" % (len(rows), len(miss), miss or ""))
    for path, blob, sz in rows:
        if path in ("app.py", "verify/stepg_pipeline.py", "verify/run_all.py",
                    "verify/run_verification.py"):
            print("  %-32s %s…  %8d B" % (path, blob[:16], sz))
    agg = hashlib.sha256("\n".join("%s %s" % (b, p) for p, b, _ in rows).encode()).hexdigest()
    print("🔒 `34` 檔 blob 清單之聚合 `sha256` ＝ `%s`" % agg)
    return {p: b for p, b, _ in rows}, agg


# ══════════════════════════ 閘 8 ══════════════════════════
ZIWU_DEF = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
ZIWU_RANGE = re.compile(
    r"^#+[^\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?[\s\u3000`]*[〜～\-–~]+[\s\u3000`]*`?([0-9]{1,4})`?",
    re.M)
GB_HEAD = re.compile(r"^#{2,4}[^\n]*?GB-([0-9]{1,4})", re.M)
GB_BARE = re.compile(r"(?<![0-9\-])GB-([0-9]{1,4})(?![0-9])")
VR_FRAME = re.compile(r"^#+ `?VR-([0-9]{1,4})`?", re.M)
K9_FRAME = re.compile(r"^#{2,4}[^\n]*?K-9-([0-9]{1,3})", re.M)


def spans(s):
    lo, hi = min(s), max(s)
    return lo, hi, sorted(set(range(lo, hi + 1)) - s)


def show(label, frame_desc, s, cap=14):
    lo, hi, miss = spans(s)
    print("  %-6s／%-26s 相異 `%d`／MIN `%d`／MAX `%d`／缺號 %s"
          % (label, frame_desc, len(s), lo, hi,
             miss if len(miss) <= cap else "(%d 個)" % len(miss)))
    return len(s), hi, miss


def gate8(rev):
    print("\n══ 閘 `8`　四簿（**二框並報**·母體逐簿單檔）══")
    out = {}
    t = git_text(rev, LEDGER_ZIWU)
    only_def = set(int(x) for x in ZIWU_DEF.findall(t))
    wide, nrng = set(only_def), 0
    for a, b in ZIWU_RANGE.findall(t):
        a, b = int(a), int(b)
        if b > a and b - a < 40:
            wide.update(range(a, b + 1))
            nrng += 1
    out["自誤_定義框"] = show("自誤", "定義框〔⛔ 併範圍框〕", only_def)
    out["自誤_正典"] = show("自誤", "正典框〔定義框＋範圍框〕", wide)
    print("        （範圍標題命中 `%d` 條）" % nrng)

    t = git_text(rev, LEDGER_GB)
    out["GB_標題"] = show("GB", "標題錨定框 `^#{2,4}…GB-N`", set(int(x) for x in GB_HEAD.findall(t)))
    out["GB_裸"] = show("GB", "裸錨定框 `(?<![0-9-])GB-N(?!\\d)`", set(int(x) for x in GB_BARE.findall(t)))

    t = git_text(rev, LEDGER_VR)
    out["VR"] = show("VR", "標題錨定框 `^#+ `?VR-N`?`", set(int(x) for x in VR_FRAME.findall(t)) - {999})

    t = git_text(rev, LEDGER_K6)
    out["K-9"] = show("K-9", "標題錨定框 `^#{2,4}…K-9-N`", set(int(x) for x in K9_FRAME.findall(t)))
    return out


# ══════════════════════════ 閘 10 ══════════════════════════
def two_forms(token_plain, token_ticked, files, texts):
    """意指占用之**二形並取**（`常規四（七）補款一`錨定框 ＋ `補款二`／`GB-158`）。"""
    res = {}
    for nm, tok in (("B 形〔`自誤 N`〕", token_plain), ("C 形〔`` `自誤 N` ``〕", token_ticked)):
        pat = re.compile(r"(?<![0-9\-])" + re.escape(tok) + r"(?![0-9])")
        lines = set()
        for p in files:
            for i, ln in enumerate(texts[p].splitlines(), 1):
                if pat.search(ln):
                    lines.add((p, i))
        res[nm] = lines
    return res


def occupancy(label, plain, ticked, files, texts, role):
    r = two_forms(plain, ticked, files, texts)
    print("\n  受詞 `%s`　（%s）" % (label, role))
    tot = set()
    for nm, lines in r.items():
        ext = sorted({p for p, _ in lines} - OWN)
        print("    %s：列 `%d`／檔 `%d`／**除本補令自身之產物外 檔 `%d`**"
              % (nm, len(lines), len({p for p, _ in lines}), len(ext)))
        tot |= lines
    ext_lines = [(p, i) for p, i in sorted(tot) if p not in OWN]
    print("    ⇒ 二形聯集：列 `%d`／**除本補令自身之產物外 列 `%d`**"
          % (len(tot), len(ext_lines)))
    for p, i in ext_lines[:8]:
        print("      · %s:%d" % (p, i))
    return len(ext_lines)


def pick_sentinel(files, texts):
    """執行期組出之真零哨兵：當場自證其全倉命中 ＝ `0`（字面⛔ 出艙）。"""
    for n in range(8100, 8200):
        tok = "自誤 " + str(n)
        pat = re.compile(r"(?<![0-9\-])" + re.escape(tok) + r"(?![0-9])")
        if not any(pat.search(texts[p]) for p in files):
            return tok, "`` `" + tok + "` ``".replace("`` `", "`").replace("` ``", "`")
    raise SystemExit("⛔ 找不到真零哨兵 ⇒ 量測器紅")


def letters(rev, files, texts):
    """恆常附款之字母框·**二形並取**（裁 `3`）。"""
    f_def = [re.compile(r"立為恆常附款[^\n]{0,20}?`([a-z])`"),
             re.compile(r"恆常附款 `([a-z])` [：＝]")]
    f_ref = [re.compile(r"恆常附款 `([a-z])`"),
             re.compile(r"恆常附款 ([a-z])(?![a-z])")]
    defs, refs, meta = {}, {}, {}
    for p in files:
        for i, ln in enumerate(texts[p].splitlines(), 1):
            for fr in f_def:
                for mt in fr.finditer(ln):
                    defs.setdefault(mt.group(1), set()).add((p, i))
            for fr in f_ref:
                for mt in fr.finditer(ln):
                    refs.setdefault(mt.group(1), set()).add((p, i))
                    if "框 ＝" in ln or "框＝" in ln or "之 `` 恆常附款" in ln:
                        meta.setdefault(mt.group(1), set()).add((p, i))
    return defs, refs, meta


def gate10(rev):
    print("\n══ 閘 `10`　取號現查（母體 ＝ **全倉追蹤 `.md`**·`常規四（七）二`）══")
    files = ls_md(rev)
    texts, unread = {}, 0
    for p in files:
        try:
            texts[p] = git_text(rev, p)
        except Exception:
            texts[p] = ""
            unread += 1
    print("母體 ＝ 全倉追蹤 `.md` **`%d`** 檔（讀不到 `%d`）" % (len(files), unread))

    occupancy("自誤 442", "自誤 442", "`自誤 442`", files, texts, "受詢【須 0】")
    occupancy("自誤 441", "自誤 441", "`自誤 441`", files, texts, "對照甲【必非零】")
    sp, st = pick_sentinel(files, texts)
    occupancy("〔哨兵·字面⛔ 出艙〕", sp, st, files, texts, "對照乙【必為零·執行期組出】")

    print("\n  ── 恆常附款之字母框（裁 `3` 之二形並取）──")
    defs, refs, meta = letters(rev, files, texts)
    for ch in "abcdefghijklmnopqrstuvwxy":
        nd, nr, nm = len(defs.get(ch, ())), len(refs.get(ch, ())), len(meta.get(ch, ()))
        tag = ""
        if ch in ("x", "y"):
            real = nr - nm
            tag = "　◀ 受詢：真占用 ＝ `%d`（扣**框之後設變數**引用 `%d`）" % (real, nm)
        print("    `%s`　定義 `%d`／引用 `%d`%s" % (ch, nd, nr, tag))
    print("    對照乙【必為零】字母 `z`：定義 `%d`／引用 `%d`"
          % (len(defs.get("z", ())), len(refs.get("z", ()))))
    print("    對照甲【必非零】字母 `u`：定義 `%d`／引用 `%d`"
          % (len(defs.get("u", ())), len(refs.get("u", ()))))
    for p, i in sorted(refs.get("x", ())):
        print("      · `x` 之命中 %s:%d　〔%s〕"
              % (p, i, "框之後設變數" if (p, i) in meta.get("x", ()) else "🔴 待判"))
    return defs, refs, meta


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    full = run(["git", "rev-parse", rev]).stdout.decode().strip()
    print("# `W-G.9-318` 補令四　開工閘之量測（唯讀）")
    print("態 ＝ `%s`" % full)
    gate7(rev)
    gate8(rev)
    gate10(rev)
    print("\n🔒 本器唯讀：⛔ 改任何既有檔一字。")


if __name__ == "__main__":
    main()
