# -*- coding: utf-8 -*-
r"""**`W-G.9-190R` `§九（甲）`**：施工單 **pre-flight 機檢器**（⛔ 零生產碼）

## 受詞（施工單 `§九` 逐字）

> 事由：`§八` 六則自誤全出自發單側。CC 之交叉檢查擋下四則，`228` **⛔ 不在其射程內**，
> `229` 由接手窗自查而得。本節之目的是把「靠發單側自律」改成「受單側收單時機檢」。

輸入 ＝ 一張施工單之 `.md` 路徑；輸出 ＝ 逐項判與 `rc`。

## 🛑 性質⛔ 不得混同（單 `§九（甲）` 逐字）

- **`P-3`／`P-5` 係機械可判** ⇒ 列為開工閘之**停機款**（本器以 `rc≠0` 表之）。
- **`P-1`／`P-2`／`P-4`／`P-6` 係文字啟發式、<u>必有偽陽</u>** ⇒ **⛔ 不得列為停機款**；
  其處置為「**逐項具名，採納或具名豁免**」，⛔ 不得靜默略過。**恆綠 ⇒ 檢查器紅。**

## 🔑 判別力造（單所令·`--selftest`·⛔ 不可省）

以 `docs/orders/` 內既有之 `W-G.9-190`（**已知含 `P-3` 與 `P-4` 之缺**）為靶：`P-3` 須**紅**、
`P-4` 須**提示**；另以 `W-G.9-191` 交接文之 `§六-3`（「實質差須由 `20` 降為 `19`」**未具名實測出處**）
為 `P-6` 之靶，須**提示**。**三者任一不觸 ⇒ 檢查器紅、⛔ 不得入倉。**

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不寫死本機絕對路徑。⛔ 不改任何既有閘。
⛔ **不自動退單**——其輸出係供受單側於開工閘逐項處置之材料。
"""
import ast
import hashlib
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 推得·⛔ 不寫死絕對路徑
ORDERS = os.path.join(REPO, "docs", "orders")

CHANNEL = ("run_step_g", "run_all", "[T2-DIAG]", "逐街廓")
NEG = ("查無", "不存在", "無任何")
STOPW = ("停機", "🛑")


def main_range():
    """`app.py` 之 `def main` 之 AST 區間（🛑 實查·⛔ 不得硬編·單 `P-3` 逐字）。"""
    t = ast.parse(open(os.path.join(REPO, "app.py"), encoding="utf-8").read())
    for n in ast.walk(t):
        if isinstance(n, ast.FunctionDef) and n.name == "main":
            return n.lineno, n.end_lineno
    raise RuntimeError("🔴 `app.py` 內找不到 `def main` ⇒ ⛔ 不得以推定代之")


def sections(text):
    """依 markdown 標題切節；回 [(標題, 起列, 迄列, 全文)]。"""
    lines = text.splitlines()
    idx = [i for i, l in enumerate(lines) if re.match(r"^#{1,6} ", l)]
    if not idx or idx[0] != 0:
        idx = [0] + idx
    out = []
    for k, i in enumerate(idx):
        j = idx[k + 1] if k + 1 < len(idx) else len(lines)
        out.append((lines[i][:70], i + 1, j, "\n".join(lines[i:j])))
    return out


def units(para_start, para_text):
    r"""把一「段」再切為**條目**（bullet／編號項）——🩸 **粒度之修正（CC 自捕）**。

    案由：`--selftest` 之靶③ 未觸。bullet list 於空行分段下係**單一段**，
    致「本條之停機款」被「**他條**之『實跑』」豁免（`W-G.9-191:121` 之三 bullet 同段）。
    ⇒ 凡逐條各自成立之判（`P-6`），一律以**條目**為單位，⛔ 非以段。
    """
    lines = para_text.splitlines()
    marks = [i for i, l in enumerate(lines)
             if re.match(r"^\s*(?:[-*+]|\d+\.)\s", l)]
    if not marks:
        return [(para_start, para_text)]
    out = []
    if marks[0] > 0:
        out.append((para_start, "\n".join(lines[:marks[0]])))
    for k, i in enumerate(marks):
        j = marks[k + 1] if k + 1 < len(marks) else len(lines)
        out.append((para_start + i, "\n".join(lines[i:j])))
    return out


def paras(text):
    """空行分段；回 [(起列, 全文)]。"""
    out, buf, st = [], [], 1
    for i, l in enumerate(text.splitlines(), 1):
        if l.strip():
            if not buf:
                st = i
            buf.append(l)
        elif buf:
            out.append((st, "\n".join(buf)))
            buf = []
    if buf:
        out.append((st, "\n".join(buf)))
    return out


def check(path):                                                 # noqa: C901
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8")
    R = {"red": [], "warn": [], "info": []}
    nm = os.path.basename(path)
    print("=" * 116)
    print("【order pre-flight】%s（%d B／%d 列）" % (nm, len(raw), len(txt.splitlines())))
    print("=" * 116)

    # ── P-5（🔴 機械）SELF_SHA256 ────────────────────────────────────
    ls = raw.splitlines(keepends=True)
    idx = [i for i, l in enumerate(ls) if b"SELF_SHA256" in l]
    if not idx:
        R["warn"].append(("P-5", 0, "⛔ 無 `SELF_SHA256` 列 ⇒ ⛔ 不可對拍（🟡 非紅：非所有文件皆須有）"))
    else:
        i = idx[-1]
        got = hashlib.sha256(b"".join(ls[:i])).hexdigest()
        dec = ls[i].decode("utf-8", "replace").split(":")[-1].strip().strip("`")
        ok = (got == dec)
        (R["info"] if ok else R["red"]).append(
            ("P-5", i + 1, "SELF_SHA256 %s（取檔內**最末**一個·受詞 %d B）｜實算 %s…／單載 %s…"
             % ("✅ 相符" if ok else "🔴 **不符**", sum(len(x) for x in ls[:i]),
                got[:16], dec[:16])))

    # ── P-3（🔴 機械）主閘之受詞是否落於 `app.py` 之 `def main` ────────
    lo, hi = main_range()
    R["info"].append(("P-3", 0, "`app.py` 之 `def main` 區間（AST 實查）＝ `%d`-`%d`" % (lo, hi)))
    for title, s0, s1, body in sections(txt):
        refs = [(m.group(0), int(m.group(1)))
                for m in re.finditer(r"app\.py:(\d{2,6})", body)]
        inmain = [(t_, n) for t_, n in refs if lo <= n <= hi]
        has_gate = ("主閘" in body)
        chans = [c for c in CHANNEL if c in body]
        # 🩸 **射程之修正（CC 自捕·`--selftest` 反靶偽陽·二輪）**：凡該節係**引述**一個
        #   既往／已知有缺之設計者——**登記**（`自誤`／`案由`）、**廢止**（`廢止`／`原款`）、
        #   或**指定為判別力造之靶**（`靶`）——其所引之 `app.py:N` 係**被描述之錯**、
        #   ⛔ 非本單所立之閘 ⇒ **排除**。
        #   🔒 ⛔ 若不排除，本器將於「**修正該錯之單**」與「**本器自身之規格節**」上自紅。
        #   🛑 **本排除⛔ 不得過寬之保證** ＝ `--selftest` 之**靶①**（`W-G.9-190 §一 N-1`
        #      ⛔ 不含上開任一語）須**仍紅**；若因排除而失效，自檢即轉紅。
        REGIS = ("自誤", "廢止", "原款", "案由", "靶")
        is_regis = any(w in body for w in REGIS)
        if is_regis and inmain and has_gate:
            R["info"].append(("P-3", s0, "ℹ️ 節「%s」含 `main()` 內之 `app.py:N`，"
                              "惟該節係**登記／廢止**既往設計（命中 %s）⇒ **⛔ 非閘規格**，排除"
                              % (title.strip(), [w for w in REGIS if w in body])))
        elif inmain and has_gate and chans:
            R["red"].append(("P-3", s0,
                             "🔴 節「%s」：主閘之受詞 %s **落於 `def main` 內**（`run_all` 從不執行之），"
                             "而該節又令以 %s 量之 ⇒ **該閘判別力為零**"
                             % (title.strip(), [t_ for t_, _ in inmain], chans)))
        elif inmain and has_gate:
            R["warn"].append(("P-3", s0, "🟡 節「%s」：受詞 %s 在 `main` 內但該節未具名量測通道 ⇒ 人工判"
                              % (title.strip(), [t_ for t_, _ in inmain])))

    # ── P-1（🟡）全稱否定須具名母體與所查範圍 ───────────────────────
    for st, p in paras(txt):
        if any(w in p for w in NEG):
            has_pop = bool(re.search(r"母體|全倉|`ls-files|全檔|共 ?`?\d+`? ?(檔|列|B)", p))
            if not has_pop:
                R["warn"].append(("P-1", st, "🟡 全稱否定而同段⛔ 未具名母體／所查範圍：%s"
                                  % p.splitlines()[0][:90]))

    # ── P-2（🟡）計數須同段載其框；框無 `^` 錨須二數並報 ──────────────
    for st, p in paras(txt):
        if re.search(r"(命中|得數|得|計|共)\s*`?\d+`?\s*(處|列|次|筆|個|檔)", p):
            has_frame = ("框" in p) or ("grep" in p) or ("^" in p)
            if not has_frame:
                R["warn"].append(("P-2", st, "🟡 出艙計數而同段⛔ 未載其框：%s"
                                  % p.splitlines()[0][:90]))
            elif ("^" not in p) and ("二數並報" not in p) and ("CLAUDE.md:725" not in p):
                R["warn"].append(("P-2", st, "🟡 框⛔ 無 `^` 錨而同段未依 `CLAUDE.md:725` 二數並報：%s"
                                  % p.splitlines()[0][:90]))

    # ── P-4（🟡）方向性轉引須具名座標系 ─────────────────────────────
    for st, p in paras(txt):
        if ("→" in p) and re.search(r"逐字|轉引|引", p):
            if not re.search(r"座標系|方向|注入方向|來源.*[:：]|自.*抽出", p):
                R["warn"].append(("P-4", st, "🟡 方向性轉引而同段⛔ 未具名座標系：%s"
                                  % p.splitlines()[0][:90]))
        elif "→" in p and re.search(r"應為|須為|收斂", p):
            if "座標系" not in p and "注入方向" not in p:
                R["warn"].append(("P-4", st, "🟡 含方向箭頭之期望而⛔ 未具名座標系：%s"
                                  % p.splitlines()[0][:90]))

    # ── P-6（🟡）停機款所繫之數是否經實測 ───────────────────────────
    NUMCHG = re.compile(r"(由 ?`?\d+`? ?降為 ?`?\d+`?|`?\d+`? ?→ ?`?\d+`?|須為 ?`?\d+`?|須由 ?`?\d+`?)")
    for st0, p0 in paras(txt):
        for st, p in units(st0, p0):          # 🩸 以**條目**為單位（見 `units` docstring）
            if any(w in p for w in STOPW) and NUMCHG.search(p):
                if not re.search(r"實測|實跑|log|【倉】|verify/out|發單側.*實跑", p):
                    R["warn"].append(("P-6", st,
                                      "🟡 停機款所繫之數⛔ 未具名實測出處：%s"
                                      % p.splitlines()[0][:90]))

    for k, tag in (("red", "🔴 機械·停機款"), ("warn", "🟡 提示·須逐項處置"), ("info", "ℹ️ 記錄")):
        print("\n── %s：%d 項 ──" % (tag, len(R[k])))
        for c, ln, msg in R[k]:
            print("  [%s] :%-4s %s" % (c, ln or "-", msg))
    print()
    return R


def selftest():
    """🔑 判別力造（單 `§九（甲）` 所令·⛔ 不可省）。"""
    print("#" * 116)
    print("【判別力造】三靶（⛔ 任一不觸 ⇒ 檢查器紅、⛔ 不得入倉）")
    print("#" * 116)
    t190 = os.path.join(ORDERS, "W-G.9-190_施工單_族二三切換.md")
    t191 = os.path.join(ORDERS, "W-G.9-191_發單側交接文.md")
    t190r = os.path.join(ORDERS, "W-G.9-190R_族二三切換.md")
    bad = []
    for p in (t190, t191, t190r):
        if not os.path.exists(p):
            bad.append("🛑 靶不存在：%s" % p)
    if bad:
        for b in bad:
            print(b)
        return 1
    a = check(t190)
    p3 = [x for x in a["red"] if x[0] == "P-3"]
    p4 = [x for x in a["warn"] if x[0] == "P-4"]
    b = check(t191)
    p6 = [x for x in b["warn"] if x[0] == "P-6"]
    c = check(t190r)
    c3 = [x for x in c["red"] if x[0] == "P-3"]
    print("=" * 116)
    print("【判別力造之判】")
    ok = True
    for nm, cond, why in (
            ("靶① `W-G.9-190` 之 `P-3` 須**紅**", bool(p3), "主閘架於 `run_step_g` 而受詞在 `main()` 內"),
            ("靶② `W-G.9-190` 之 `P-4` 須**提示**", bool(p4), "三量方向未具名座標系"),
            ("靶③ `W-G.9-191 §六-3` 之 `P-6` 須**提示**", bool(p6), "「由 `20` 降為 `19`」未具名實測出處"),
            ("反靶 `W-G.9-190R` 之 `P-3` 須**不紅**", not c3, "其主閘已改源碼層 ⇒ 證本器⛔ 非恆紅")):
        ok &= cond
        print("  %s %s —— %s" % ("✅" if cond else "🔴", nm, why))
    print("=" * 116)
    print("判別力造：%s" % ("✅ 全數成立 ⇒ 本器非恆綠亦非恆紅" if ok else "🔴 未全數成立 ⇒ **檢查器紅**"))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    if len(sys.argv) < 2:
        print("用法：python verify/probes/probe_order_preflight.py <施工單.md> ｜ --selftest")
        sys.exit(2)
    r = check(sys.argv[1])
    print("🛑 `rc` ＝ 紅項數（`P-3`／`P-5` 之機械款）；🟡 提示⛔ 不計入 `rc`（單 `§九（甲）` 逐字）")
    sys.exit(1 if r["red"] else 0)
