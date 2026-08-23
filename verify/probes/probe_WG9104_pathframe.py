# -*- coding: utf-8 -*-
r"""`W-G.9-101 補正③`：**路徑解析之框**——`quotepath` 救不了空白（量測·⛔ 零管線）。

## 受詞

`VR-059 三` 只綁 `-c core.quotepath=false`，該款**正確但不充分**：
`quotepath` 只解除**非 ASCII** 之 C-style 轉義引號，⛔ **不處理含空白之路徑**
—— 後者於任何框下皆逐字輸出、⛔ 不加引號 ⇒ 以空白 tokenize 者**仍被切碎**（`VR-060`）。

## 🔒 本探針自身須遵 `VR-060 二` 三要件並**自證其遵守**（`P-5`）

1. **逐列切分**（`splitlines()`），⛔ 不以空白 tokenize；
2. `--name-status` 等含欄位者以 `\t` 切且 `maxsplit=1`；
3. 明綁 `-c core.quotepath=false`（載體級直檢 ＝ `ARGV_LOG`·`VR-062 一`）。

## 🔒 `P-8`：三值 ＋ **正交來源**之自我適用（`VR-061 一`／`VR-062 二`）

`P-6` 之判別力對照以**三值**出艙；其「是否退化」之判定**取自 `-z`（NUL 分隔）**
——該來源⛔ 不受 `core.quotepath` 支配，且其**正交性於本檔自證**（⛔ 不假定）。

## 🔒 母體之態

一切量取自 `blob@BASE_FULL`（⛔ 非工作區）⇒ 本檔之值⛔ 不因本批之附加而漂移。

## 預測值之出處（`fixture-provenance`）

`P-1`〜`P-8` 之期望值**逐項引自施工單** `W-G.9-101 補正③` `§二`（⛔ 非由本檔現跑一次回填）。

## 重跑

    python verify/probes/probe_WG9104_pathframe.py

`rc` **恆 `0`**；停機以**逐字具名**表示。
"""
import ast
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "e669ddb"
BASE_FULL = "e669ddbf42949661685ed279fe9944f1e52ea12b"
WIDTH = 112
SELFSRC = os.path.abspath(__file__)

# ── 施工單 `§二` 之預測值（⛔ 非本檔現跑回填）──────────────────────────────
EXP_P1 = 1352
EXP_P2 = 1419
EXP_GAP = 67
EXP_P3 = 45
EXP_P3_PREFIX = "verify/baselines/"
EXP_P4 = 0

LAND_QUOTED = "ΣΔ ＝ +1.0300／池增量 84.0800 ㎡／R1 ΣΔ ＝ +0.000000"

L, STOPS, SKIPPED = [], [], []

# 🔒 `ARGV_LOG` ＝ **實際執行之 argv**（載體級直檢·`VR-062 一`·⛔ 非「打算執行什麼」）。
ARGV_LOG = []


def P(s=""):
    print(s)
    L.append(s)


def hdr(s):
    P("")
    P("=" * WIDTH)
    P(s)
    P("=" * WIDTH)


def stop(tag, text):
    STOPS.append((tag, text))
    P("  🛑 **停機 %s**：%s" % (tag, text))


def skipped(tag, text):
    SKIPPED.append((tag, text))
    P("  ⚠️ **略過 %s**：%s（⛔ 不計為證據·亦⛔ 不計為反證）" % (tag, text))


def M(ok):
    return "✅" if ok else "🛑"


def git(args):
    """🔒 要件③：**一律**明綁 `-c core.quotepath=false`；argv 逐次入 `ARGV_LOG`。"""
    argv = ["git", "-C", REPO, "-c", "core.quotepath=false"] + args
    ARGV_LOG.append(argv)
    return subprocess.run(argv, stdout=subprocess.PIPE, check=True).stdout.decode("utf-8")


def git_raw_z(args, quotepath="false"):
    """🔒 `-z`（NUL 分隔）之**正交來源**：其輸出⛔ 不受 `core.quotepath` 支配（本檔自證）。"""
    argv = ["git", "-C", REPO, "-c", "core.quotepath=%s" % quotepath] + args
    ARGV_LOG.append(argv)
    return subprocess.run(argv, stdout=subprocess.PIPE, check=True).stdout


def paths_by_line(raw):
    """🔒 要件①：**逐列切分**（`splitlines()`）——救**空白**。"""
    return [x for x in raw.splitlines() if x.strip()]


def _wrong_tokenize(raw):
    """🩸 **刻意之錯誤對照組**（⛔ 非本檔之路徑解析路徑）：以空白 tokenize。
    🔒 本檔全部 `.split()`（無參數）之出現**皆**限於本函式；`P-5` 對此自證。"""
    return raw.split()


# 🔒 `P-5` 要件① 之**人造二造對照**（家法 `9`／`VR-062 四`：判別力須以**相異之二輸入**證之）。
CTL_POS = 'def f(s):\n    return s.split()\n'
CTL_NEG = 'def f(s):\n    return s.split("\\t", 1)\n'


def bare_split_calls(src):
    """🔒 以 `ast` 判「**無參數之 `.split()` 呼叫節點**」（⛔ 非字面掃描）。

    回傳 `(裸呼叫之列號, _wrong_tokenize 起列, 迄列)`；無該函式者回 `(…, 0, -1)`。
    """
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "split" and not node.args and not node.keywords):
            hits.append(node.lineno)
    lo, hi = 0, -1
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "_wrong_tokenize":
            lo, hi = node.lineno, node.end_lineno
    return sorted(hits), lo, hi


def name_status_pairs(raw):
    """🔒 要件②：`--name-status` 以 `\\t` 切且 `maxsplit=1`（⛔ 不以空白切）。"""
    out = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t", 1)
        if len(parts) == 2:
            out.append((parts[0], parts[1]))
    return out


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG9104_pathframe_%s.log" % BASE_REF)

    hdr("【W-G.9-101 補正③】路徑解析之框（⛔ 零生產碼·⛔ **零管線**·態 ＝ blob@%s）" % BASE_REF)
    P("  基座（一切量之態）＝ **%s**（⛔ 本檔不印任何隨 `HEAD` 而變之值）" % BASE_FULL)
    P("  `app.py` blob@基座 ＝ %s" % git(["rev-parse", "%s:app.py" % BASE_FULL]).strip())
    P("  🔒 預測值出處 ＝ 施工單 `W-G.9-101 補正③` `§二`（⛔ 非本檔現跑回填）。")

    raw = git(["ls-tree", "-r", "--name-only", BASE_FULL])
    by_line = paths_by_line(raw)
    by_tok = _wrong_tokenize(raw)
    ws = [p for p in by_line if " " in p]
    quoted = [p for p in ws if p.startswith('"')]

    # ── §一　`P-1`／`P-2`／`P-6` ───────────────────────────────────────────
    hdr("【§一】二解析器之對照（`P-1`／`P-2`／`P-6`·同一輸出·只換解析器）")
    ok1 = (len(by_line) == EXP_P1)
    ok2 = (len(by_tok) == EXP_P2)
    gap = len(by_tok) - len(by_line)
    P("  %s `P-1` **逐列切分**（`splitlines()`·要件①）⇒ 路徑 **%d** 條（單 %d）"
      % (M(ok1), len(by_line), EXP_P1))
    P("  %s `P-2` **空白 tokenize**（`.split()`·🩸 刻意之錯誤對照）⇒ **%d** token（單 %d）"
      % (M(ok2), len(by_tok), EXP_P2))
    P("  %s `P-6` **擾動量 ＝ %d**（單 %d）⇒ %s"
      % (M(gap == EXP_GAP), gap, EXP_GAP,
         "該對照⛔ 未退化（家法 `9`）" if gap > 0 else "**已退化**"))

    # ── §二　`P-3`／`P-4`／`P-7` ───────────────────────────────────────────
    hdr("【§二】含空白之路徑（`P-3`）・旗標之無效性（`P-4`）・否證通道（`P-7`）")
    ok3 = (len(ws) == EXP_P3)
    ok4 = (len(quoted) == EXP_P4)
    allpfx = all(p.startswith(EXP_P3_PREFIX) for p in ws)
    P("  %s `P-3` 含空白之路徑 ＝ **%d** 條（單 %d）；全在 `%s` 下 ＝ **%s**"
      % (M(ok3), len(ws), EXP_P3, EXP_P3_PREFIX, allpfx))
    P("     前三條逐字：")
    for p in ws[:3]:
        P("        %r" % p)
    P("     （⛔ 全列於下·`POPULATION=%d`）" % len(ws))
    for p in ws:
        P("        %s" % p)
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # 含空白之路徑（全列）" % (len(ws), len(ws)))
    P("  %s `P-4` 該 %d 條於 `quotepath=false` 下**加引號者 ＝ %d**（單 %d）"
      % (M(ok4), len(ws), len(quoted), EXP_P4))
    P("     ⇒ 🔴 **旗標⛔ 救不了空白**——`quotepath` 之作用域僅及非 ASCII 之 C-style 轉義。")
    empty = (len(ws) == 0)
    P("  %s `P-7` 否證通道：布林「含空白之路徑集為空」＝ **%s**（單 `False`）" % (M(not empty), empty))
    if empty:
        stop("⑦", "`P-7` 為 `True` ⇒ 本單受詞不成立 ⇒ 上呈發單側")
    if not (ok1 and ok2 and ok3 and ok4):
        stop("⑥", "`P-1`〜`P-4` 有與預測不符者 ⇒ ⛔ 不得改樣式去湊（家法 `6`）")

    # ── §三　`P-8`：三值 ＋ 正交來源之自我適用 ─────────────────────────────
    hdr("【§三】🔒 `P-8`：`P-6` 之**三值** ＋ 退化判定之**正交來源**（`VR-061 一`／`VR-062 二`）")
    zt = git_raw_z(["ls-tree", "-r", "-z", "--name-only", BASE_FULL], quotepath="true")
    zf = git_raw_z(["ls-tree", "-r", "-z", "--name-only", BASE_FULL], quotepath="false")
    z_imm = (zt == zf)
    znames = [x.decode("utf-8") for x in zf.split(b"\x00") if x]
    z_ws = [x for x in znames if " " in x]
    P("  🔒 **正交性自證**（⛔ 不假定）：二框之 `-z` 輸出逐位相同 ＝ **%s**（須 `True`）%s"
      % (z_imm, M(z_imm)))
    P("     ⇒ `-z` 之輸出⛔ 不受 `core.quotepath` 支配 ⇒ 得作**退化判定之正交來源**。")
    P("  🔒 **退化判定（取自 `-z`·⛔ 非取自被測之解析器輸出）**："
      "`-z` 解出 **%d** 條路徑／其中含空白 **%d** 條" % (len(znames), len(z_ws)))
    if not z_imm:
        p6 = False
        why = "🔴 正交來源之免疫性不成立 ⇒ 退化判定不可信"
    elif len(z_ws) == 0:
        p6 = None
        why = "母體無含空白之路徑 ⇒ **擾動無從顯現**"
    else:
        p6 = (gap > 0)
        why = "母體含空白之路徑 **%d** 條 ⇒ 擾動應顯現" % len(z_ws)
    P("  🔒 **`P-6` 之三值**：**%s**（`True` ＝ 擾動已顯現／`False` ＝ 該顯現而未顯現 ⇒ 紅／"
      "`略過` ＝ 母體無從使擾動顯現）" % ("略過" if p6 is None else p6))
    P("     依據 ＝ %s" % why)
    P("  🔒 **判別力自檢**（⛔ 不得寫成 `f(X) != f(X)`·`VR-062 四`）："
      "以**同一解析器**跑**相異之二輸入** ——")
    ascii_raw = git(["ls-tree", "-r", "--name-only", BASE_FULL, "--",
                     "verify/wf_f0.py", "verify/wf_f1.py"])
    a_line, a_tok = len(paths_by_line(ascii_raw)), len(_wrong_tokenize(ascii_raw))
    disc = (a_tok - a_line)
    P("     以**無空白之子樹**（`verify/wf_f0.py`／`wf_f1.py`）代入同一對照 ⇒ "
      "`splitlines()` %d ／ `.split()` %d ⇒ 擾動量 ＝ **%d**（須 `0`）%s"
      % (a_line, a_tok, disc, M(disc == 0)))
    P("     ⇒ 該對照之 `True` **確因母體含空白而來**（⛔ 非恆真）。")
    if p6 is None:
        skipped("⑧", "`P-6` 之對照退化（母體無含空白之路徑）")
    elif p6 is False:
        stop("⑧", "`P-6` 之擾動量 ＝ 0 而母體本應使其顯現")

    # ── §四　`P-5`：自證遵 `VR-060 二` ────────────────────────────────────
    hdr("【§四】🔒 `P-5`：**自證**遵 `VR-060 二` 三要件（碼面直檢 ＋ 載體級直檢）")
    with open(SELFSRC, "rb") as fh:
        me = fh.read().decode("utf-8")
    me_lines = me.splitlines()
    n_call = len(ARGV_LOG)
    n_bound = sum(1 for a in ARGV_LOG if "core.quotepath=false" in a)
    n_true = sum(1 for a in ARGV_LOG if "core.quotepath=true" in a)
    P("  **要件③（載體級·`VR-062 一`）**：`git` 呼叫 ＝ **%d** 次；"
      "其 argv 含 `core.quotepath=false` ＝ **%d** 次；含 `=true` ＝ **%d** 次"
      % (n_call, n_bound, n_true))
    P("     🔒 該 `%d` 次 `=true` **全數**係 `-z` 正交性自證之**對照組**（⛔ 非路徑解析路徑）。" % n_true)
    ok5c = (n_bound + n_true == n_call) and (n_true == 1)
    P("     %s ⇒ **無任何 `git` 呼叫未綁 `core.quotepath`** ＝ %s"
      % (M(ok5c), n_bound + n_true == n_call))
    bare, fn_lo, fn_hi = bare_split_calls(me)
    inside = [i for i in bare if fn_lo <= i <= fn_hi]
    outside = [i for i in bare if not (fn_lo <= i <= fn_hi)]
    P("  **要件①**：`.split()`（**無參數**·🔒 以 `ast` 判**呼叫節點**·⛔ 非字面掃描）"
      "⇒ 出現 **%d** 處（列 %s）；其中在 `_wrong_tokenize`（`:%d`–`:%d`·刻意之錯誤對照）內 ＝ **%d**；"
      "**在外 ＝ %d**" % (len(bare), bare, fn_lo, fn_hi, len(inside), len(outside)))
    ok5a = (len(outside) == 0)
    P("     %s ⇒ **⛔ 無 `.split()` 用於路徑解析**（實際解析一律 `splitlines()`）" % M(ok5a))
    P("     🔒 **判別力對照**（同一函式·人造二造）：含裸 `.split()` 之源 ⇒ 偵得 %d 處（應 ≥1）；"
      "只含 `.split(\"\\t\", 1)` 之源 ⇒ 偵得 %d 處（應 0）"
      % (len(bare_split_calls(CTL_POS)[0]), len(bare_split_calls(CTL_NEG)[0])))
    P("     🩸 **CC 自捕**：本檢首版以 `\".split()\" in line` 之**字面**掃描，"
      "咬中 docstring／`print` 內之 `` `.split()` `` 共 `7` 處 ⇒ **假紅**；"
      "⇒ 改 `ast` 後在外 ＝ `0`。**紅的是量測器、⛔ 不是被檢物**。")
    ns_ok = (me.count('line.split("\\t", 1)') >= 1)
    P("  **要件②**：`--name-status` 之切分 ＝ `line.split(\"\\t\", 1)`（`\\t` 且 `maxsplit=1`）"
      "⇒ 碼面命中 ＝ **%s** %s" % (ns_ok, M(ns_ok)))
    P("     判別力對照（人造）：`'M\\tpath with space'.split(\"\\t\", 1)` ⇒ %r（路徑完整）；"
      "`.split()` ⇒ %r（**被切碎**）"
      % (name_status_pairs("M\tpath with space")[0], _wrong_tokenize("M\tpath with space")))
    if not (ok5a and ok5c and ns_ok):
        stop("⑧", "`P-5` 有不成立之要件 ⇒ 本探針自身違反其所立之裁")

    # ── §五　土地三數 ─────────────────────────────────────────────────────
    hdr("【§五】🔒 土地三數 ＝ **未重算之轉述**")
    P("  %s" % LAND_QUOTED)
    P("  🔒 本檔**零管線** ⇒ 上三數⛔ **未重算**；池增量係**依守恆式導出·⛔ 非幾何實量**（`VR-054 三`）。")

    return finish(log_path)


def finish(log_path):
    hdr("【§六】收工：停機逐字")
    if SKIPPED:
        P("  ⚠️ **本批之略過（對照退化）**：")
        for t_, x in SKIPPED:
            P("     略過 %s：%s" % (t_, x))
    if STOPS:
        P("  🛑 **本批之停機（逐字具名·`rc` 恆 `0`）**：")
        for t_, x in STOPS:
            P("     停機 %s：%s" % (t_, x))
    else:
        P("  ✅ 本檔未觸任一停機條件。")
    os.makedirs(OUTDIR, exist_ok=True)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("")
    print("log -> %s" % os.path.relpath(log_path, REPO).replace(os.sep, "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
