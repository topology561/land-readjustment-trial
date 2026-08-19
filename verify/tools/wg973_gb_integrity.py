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


def audit(reg_path, use_forms=("A", "B", "C")):
    """回 dict：識別字集／逐式涵蓋／缺號集／懸空清單。"""
    lines = io.open(reg_path, encoding="utf-8").read().split("\n")
    syms = sorted({s for l in lines for s in _SYM.findall(l)},
                  key=lambda x: int(x.split("-")[1]))
    # 缺號集合：**自登記表現讀**（⛔ 不硬編）
    missing = sorted({s for l in lines if _MISSING in l for s in _SYM.findall(l)},
                     key=lambda x: int(x.split("-")[1]))
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
    return {"reg": reg_path, "syms": syms, "cover": cover, "missing": missing,
            "defined": defined, "dangling": dangling, "used": tuple(use_forms)}


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
    L.append("")
    L.append(f"  **懸空 ＝ 母體 {len(r['syms'])} − 有定義列 {len(r['defined'])} "
             f"− 缺號 {len(r['missing'])} ＝ {len(r['dangling'])}**")
    if r["dangling"]:
        L.append("  🔴 **懸空之逐項列名（⛔ 只報計數者視同未查完·節 97）**：")
        for s in r["dangling"]:
            L.append(f"      🔴 {s}")
    else:
        L.append("  ✅ **懸空 ＝ 0**")
    L.append("=" * 100)
    return L


def main(argv):
    reg, forms = REG, ("A", "B", "C")
    if "--reg" in argv:
        reg = argv[argv.index("--reg") + 1]
    if "--forms" in argv:
        forms = tuple(argv[argv.index("--forms") + 1])
    r = audit(reg, forms)
    for l in report(r):
        print(l)
    return 1 if r["dangling"] else 0


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    sys.exit(main(sys.argv))
