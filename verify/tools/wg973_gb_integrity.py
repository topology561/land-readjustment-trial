#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""`W-G.9-73` **登記表完整性稽核器**——把「每個 `GB-N` 都要有定義列」變成**會紅的東西**。

🔒 **為何要一支工具**（⛔ 非為了好看）：該家法此前只存在於人的注意力裡。
  `W-G.9-72` 以**單一形式**（`###` 標題）量定義列，得「86 中 **74** 懸空」——**量測器之偽影**；
  改二式後得殘數 **2**，而**該殘數未再受同一懷疑**（考古**節 97**：量測器之修正必須**遞迴**施用
  ——離譜的數字會自己求救，**合理的不會**）。三式並取 ＋ 缺號現讀後，真懸空 ＝ **0**。

🔒 **定義列之三式（⛔ 缺一即產生偽懸空·`--forms` 可退化以自證）**：

    A ： `^##\s+`?GB-N`?`      二級標題（⚠️ `\s` 之要求使其**⛔ 不匹配** `###`）
    B ： `^###\s+`?GB-N`?`     三級標題
    C ： `^\|[^|]*GB-N`        表列（**第 1 欄**內）

🔒 **缺號集合⛔ 硬編**——自登記表**現讀**（字樣 `為缺號`）⇒ 換案／新增缺號時自動跟上。

🔒 **餘數 > 0 一律逐項列名**（⛔ 只報計數者視同未查完·節 97 修法 1）。

──────────────────────────────────────────────────────────────────────────────
🩸 **`GB-90` 之修（`W-G.9-105 乙`）**——本器首版之二病，逐字：

  **病①（取盡全列）**：首版之缺號擷取為
      `{s for l in lines if _MISSING in l for s in _SYM.findall(l)}`
  ⇒ **凡含該字樣之列，其上<u>全部</u>符號皆入缺號集**。
  ⇒ 任何在同一列同時提及該字樣與他號之**散文**，皆會把他號**靜默注入**缺號集。

  **病②（並排之二數被當成恆等式）**：`dangling` 之定義為
      `[s for s in syms if s not in defined and s not in missing]`
  ⇒ 一個同時落在 `defined` 與 `missing` 之符號會被**雙重扣除**
  ⇒ 印出之「母體 − 有定義列 − 缺號 ＝ 懸空」**⛔ 已非恆等式**，
     而 `✅` 係由 `len(dangling)` 驅動 ⇒ **閘仍綠**（＝ 假綠）。

  **修①（緊鄰式·位置式）**：缺號改取「**每個字樣之前最靠近的那一個符號**」。
      🔒 **位置式·⛔ 非距離式**——⛔ 無 `{N,M}` 之上下限，故⛔ 不受 `VR-066 四`
         之「上下限係靜默過濾器」所害。
  **修②（落差顯形）**：含字樣之列上**未被取為缺號**之其他符號，逐項**併呈**（僅供參）；
      而「該列有符號、然字樣之前無符號」者 ⇒ 🔴 **逐列列名並轉紅**
      （⇒ 修① 之靜默漏收⛔ 無處可藏）。
  **修③（分割須自證）**：顯式檢查 `有定義列 ∩ 缺號 ＝ ∅`，
      並顯式檢查 `母體 ＝ 有定義列 ＋ 缺號 ＋ 懸空` **確為恆等式**；
      任一不成立 ⇒ 🔴 **轉紅**。⇒ 🔒 **`GB-90` 之情形自此⛔ 不可能再綠**。
  **修④（判別力自檢）**：每趟以**倉內真實資料**合成一列污染（取 `defined` 中最小者，
      ⛔ 非硬編某號），證本器**確能偵得**該重疊 ⇒ 家法同 `wg942`／`wg9103`。

  🔒 **回歸**：修① 於本倉四列含字樣之列上與首版**逐列同值** ⇒ 缺號集⛔ 未變。
  🔒 **輸出**：既有各列**逐字未動**（`run_all` 只吃本器 `rc`·⛔ 無下游解析），新增者皆為**增印**。
──────────────────────────────────────────────────────────────────────────────

用法：
    python verify/tools/wg973_gb_integrity.py                 # 稽核倉內登記表（三式）
    python verify/tools/wg973_gb_integrity.py --reg <path>    # 指定登記表（判別力測試用）
    python verify/tools/wg973_gb_integrity.py --forms B       # **退化版**（只用式 B·自證三式必要）
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
REG = os.path.join(REPO, "docs", "reports", "W-G.4_泛用阻塞項登記表.md")

_SYM = re.compile(r"GB-\d+")
_MISSING = "為缺號"


def _forms(sym):
    """回三式之樣式（逐符號生成·⛔ 不用單一寬樣式一次掃·免跨符號誤配）。

    🩸 **`(?!\\d)` ⛔ 不得省（本器首版即漏·`W-G.9-73` 自誤）**：`GB-8` 之樣式若無數字邊界，
      會匹配 `## \\`GB-81\\`` 那一行（**前綴碰撞**——`CLAUDE.md` 之 `K-9-5-1` 同族）。
      實測：漏此邊界時 **式A 3→4／式B 12→14**（`GB-7`／`GB-8` 被偽涵蓋）。
      ⚠️ **其方向是「把懸空藏起來」**——偽涵蓋只會讓 `有定義列` 變多、`懸空` 變少
      ⇒ 🔒 **該類 bug ⛔ 不會使本閘轉紅，只會使它<u>假綠</u>**。
    """
    n = re.escape(sym) + r"(?!\d)"
    return {
        "A": re.compile(r"^##\s+`?" + n),        # 二級標題（`\s` 之要求 ⇒ ⛔ 不匹配 ###）
        "B": re.compile(r"^###\s+`?" + n),       # 三級標題
        "C": re.compile(r"^\|[^|]*" + n),        # 表列（第 1 欄內）
    }


def _declared_on_line(line):
    """回該列所**宣告**之缺號 ＝ 每個字樣之前**最靠近**的那一個符號（`GB-90` 修①）。

    🔒 **位置式·⛔ 非距離式**：以 `字樣之起點` 與 `符號之終點` 之**先後**判定，
      ⛔ 無任何 `{N,M}` 之上下限 ⇒ ⛔ 不引入靜默過濾器（`VR-066 四`）。
    🔒 ⛔ **不取盡該列全部符號**——此即 `GB-90` 之案由。
    """
    out = []
    for m in re.finditer(re.escape(_MISSING), line):
        prior = [s for s in _SYM.finditer(line) if s.end() <= m.start()]
        if prior:
            out.append(prior[-1].group(0))
    return out


def audit_lines(lines, use_forms=("A", "B", "C")):
    """自**逐列文字**稽核（⛔ 不綁檔案 ⇒ 判別力自檢得以真實資料合成）。"""
    syms = sorted({s for l in lines for s in _SYM.findall(l)},
                  key=lambda x: int(x.split("-")[1]))
    # 缺號集合：**自登記表現讀**（⛔ 不硬編）·**緊鄰式**（⛔ 不取盡該列·`GB-90` 修①）
    missing_set, not_taken, noprior = set(), [], []
    for i, l in enumerate(lines, 1):
        if _MISSING not in l:
            continue
        got = _declared_on_line(l)
        allsym = _SYM.findall(l)
        missing_set |= set(got)
        for s in allsym:                     # 修②：落差**併呈**（僅供參·⛔ 不作判準）
            if s not in got:
                not_taken.append((i, s))
        if allsym and not got:               # 修②：有符號而字樣之前無符號 ⇒ 🔴 判準
            noprior.append((i, l.strip()[:88]))
    missing = sorted(missing_set, key=lambda x: int(x.split("-")[1]))

    cover = {f: set() for f in ("A", "B", "C")}
    for s in syms:
        pats = _forms(s)
        for f in ("A", "B", "C"):
            if any(pats[f].match(l) for l in lines):
                cover[f].add(s)
    defined = set()
    for f in use_forms:
        defined |= cover[f]
    dangling = [s for s in syms if s not in defined and s not in missing]

    # 修③：分割須自證（⛔ 不得只把三個數並排印出）
    overlap = sorted(defined & set(missing), key=lambda x: int(x.split("-")[1]))
    identity = (len(syms) - len(defined) - len(missing) == len(dangling))
    partition = (len(syms) == len(defined) + len(missing) + len(dangling))

    return {"syms": syms, "cover": cover, "missing": missing, "defined": defined,
            "dangling": dangling, "used": tuple(use_forms), "not_taken": not_taken,
            "noprior": noprior, "overlap": overlap, "identity": identity,
            "partition": partition}


def audit(reg_path, use_forms=("A", "B", "C")):
    """回 dict：識別字集／逐式涵蓋／缺號集／懸空清單／分割自證。"""
    lines = io.open(reg_path, encoding="utf-8").read().split("\n")
    r = audit_lines(lines, use_forms)
    r["reg"] = reg_path
    r["lines"] = lines
    return r


def selftest(lines):
    """修④ **判別力自檢**：以**倉內真實資料**合成一列污染，證本器確能偵得重疊。

    🔒 受詞取 `defined` 中**最小**者（**資料驅動**·⛔ 硬編任何號 ⇒ 換案自動跟上）。
    🔒 合成之列**⛔ 不落地**——僅存於記憶體。
    """
    base = audit_lines(lines)
    if not base["defined"]:
        return None, "（`defined` 為空 ⇒ 本自檢⛔ 無受詞·須人工查）"
    victim = sorted(base["defined"], key=lambda x: int(x.split("-")[1]))[0]
    poisoned = lines + [f"> **`{victim}` {_MISSING}**（合成之污染列·判別力自檢用·⛔ 不落地）"]
    r = audit_lines(poisoned)
    detected = bool(r["overlap"]) and (victim in r["overlap"])
    return detected, victim


def report(r):
    L = []
    rel = os.path.relpath(r["reg"], REPO).replace("\\", "/")
    L.append("=" * 100)
    L.append("【`W-G.9-73`】登記表完整性稽核（`GB-N` 之定義列·三式並取）")
    L.append("=" * 100)
    L.append(f"  登記表 ＝ {rel}")
    L.append(f"  🔒 **單位 ＝ 相異識別字**（⛔ 非行數·⛔ 非 token 數）；"
             f"**母體 ＝ 該檔內全部 `GB-N`** ＝ **{len(r['syms'])}**")
    L.append(f"  🔒 本次採用之式 ＝ {'／'.join(r['used'])}"
             + ("　⚠️ **退化版**（⛔ 非正式判準）" if tuple(r["used"]) != ("A", "B", "C") else ""))
    L.append("")
    L.append("  逐式涵蓋（單位 ＝ 相異識別字）")
    for f, desc in (("A", "`^##  `?GB-N`?`   二級標題"),
                    ("B", "`^### `?GB-N`?`   三級標題"),
                    ("C", "`^\\|[^|]*GB-N`   表列（第 1 欄）")):
        _m = sorted(r["cover"][f], key=lambda x: int(x.split("-")[1]))
        L.append(f"    式 {f}　{desc:<28} ⇒ **{len(_m)}**"
                 + (f"　＝ {_m}" if len(_m) <= 16 else ""))
    _abc = r["cover"]["A"] | r["cover"]["B"] | r["cover"]["C"]
    L.append(f"    ⇒ **三式並取（去重）＝ {len(_abc)}**")
    # 🔒 **只由 A 或 B 涵蓋者**（＝ 若少了 A／B 即成偽懸空者）——⛔ 逐項列名
    _onlyab = sorted(_abc - r["cover"]["C"], key=lambda x: int(x.split("-")[1]))
    L.append(f"    🔒 **C 未涵蓋而由 A／B 補上者 ＝ {len(_onlyab)}**　{_onlyab}"
             "（⇒ 少了 A／B 即為偽懸空）")
    L.append("")
    L.append(f"  🔒 **缺號集合（自登記表現讀·字樣 `{_MISSING}`·⛔ 未硬編）** ＝ "
             f"{r['missing'] if r['missing'] else '（空）'}")
    # ── 🆕 `GB-90` 修①②：擷取式之具名 ＋ 落差顯形 ──────────────────────────────
    L.append(f"     🔒 **擷取式 ＝ 緊鄰式**（每個字樣之前最靠近之符號·**位置式**·"
             f"⛔ 無 `{{N,M}}` 上下限·⛔ 不取盡該列）——`GB-90` 修①")
    L.append(f"     併呈（**僅供參**·⛔ 不作判準）：含字樣之列上**未被取為缺號**之其他符號 ＝ "
             f"**{len(r['not_taken'])}** 個"
             + (f"　＝ {[f'{i}:{s}' for i, s in r['not_taken'][:8]]}" if r["not_taken"] else ""))
    if r["noprior"]:
        L.append(f"     🔴 **該列有符號、然字樣之前⛔ 無符號 ＝ {len(r['noprior'])} 列**"
                 "（⇒ 緊鄰式可能漏收·**逐列列名**）：")
        for i, l in r["noprior"]:
            L.append(f"         🔴 :{i}　{l}")
    else:
        L.append("     ✅ **字樣之前⛔ 無符號之列 ＝ 0**（⇒ 緊鄰式⛔ 未靜默漏收）")
    L.append("")
    L.append(f"  **懸空 ＝ 母體 {len(r['syms'])} − 有定義列 {len(r['defined'])} "
             f"− 缺號 {len(r['missing'])} ＝ {len(r['dangling'])}**")
    # ── 🆕 `GB-90` 修③：上列究竟是不是恆等式，**須自證**（⛔ 不得只把三數並排）──────
    L.append(f"     🔒 **分割自證（`GB-90` 修③·⛔ 上列⛔ 不得只當三數並排讀）**")
    L.append(f"        `有定義列 ∩ 缺號` ＝ {r['overlap'] if r['overlap'] else '（空）'}"
             f"　⇒ **不交 ＝ {not r['overlap']}**（須 `True`）")
    L.append(f"        `母體 {len(r['syms'])} ＝ 有定義列 {len(r['defined'])}"
             f" ＋ 缺號 {len(r['missing'])} ＋ 懸空 {len(r['dangling'])}"
             f" ＝ {len(r['defined']) + len(r['missing']) + len(r['dangling'])}`"
             f"　⇒ **分割 ＝ {r['partition']}**（須 `True`）")
    L.append(f"        上開減式**確為恆等式 ＝ {r['identity']}**（須 `True`）")
    if r["overlap"]:
        L.append("     🔴 **重疊之逐項列名（＝ `GB-90` 之情形·首版於此假綠）**：")
        for s in r["overlap"]:
            L.append(f"         🔴 {s}　（同時落在 `有定義列` 與 `缺號` ⇒ 被雙重扣除）")
    if r["dangling"]:
        L.append("  🔴 **懸空之逐項列名（⛔ 只報計數者視同未查完·節 97）**：")
        for s in r["dangling"]:
            L.append(f"      🔴 {s}")
    else:
        L.append("  ✅ **懸空 ＝ 0**")
    # ── 🆕 `GB-90` 修④：判別力自檢（每趟必跑·⛔ 可選）────────────────────────────
    det, victim = selftest(r["lines"])
    if det is None:
        L.append(f"  ⚠️ **判別力自檢**：{victim}")
    else:
        L.append(f"  🔒 **判別力自檢（注入合成污染列·受詞 ＝ `{victim}`·資料驅動·⛔ 未硬編）**"
                 f" ⇒ 偵得重疊 ＝ **{det}**（須 `True`）")
    L.append("=" * 100)
    return L, det


def main(argv):
    reg, forms = REG, ("A", "B", "C")
    if "--reg" in argv:
        reg = argv[argv.index("--reg") + 1]
    if "--forms" in argv:
        forms = tuple(argv[argv.index("--forms") + 1])
    r = audit(reg, forms)
    lines, det = report(r)
    for l in lines:
        print(l)
    # 🔒 **紅之四由**（`GB-90` 修③④）：懸空／重疊／緊鄰式漏收／判別力自檢失效
    bad = bool(r["dangling"]) or bool(r["overlap"]) or bool(r["noprior"]) \
        or (not r["identity"]) or (not r["partition"]) or (det is False)
    return 1 if bad else 0


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    sys.exit(main(sys.argv))
