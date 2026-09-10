# -*- coding: utf-8 -*-
"""`W-G.9-268′` `c2`：`P-9` 之**機械歸類**（類 `(ii)` vs 類 `(iii)` 之判別）。

🔑 **判別式（⛔ 以街廓名為啟發式）**
   `P-9` 之類 `(iii)` 逐字 ＝ 「**原可達且原綠**而今紅」。
   ⇒ 其**充要之機械判準** ＝ 「該名目於**期初 log** 是否曾以 **`✅ PASS`** 出現」。
     · 期初 **PASS** ⋀ 期末 **FAIL** ⇒ **類 `(iii)` 真迴歸** ⇒ 🛑 **停機**
     · 期初 **⛔ 出現**（既非 PASS 亦非 FAIL ⇒ **該世代未執行**）⋀ 期末 FAIL
       ⇒ **類 `(ii)`** 新可達之世代所新曝
     · 期初 FAIL ⋀ 期末 FAIL ⇒ ⛔ 屬本差集（`classify` 已另計為 I／II／III）

🩸 **名目含動態內容**（如 `k* 六塊經驗錨0m {'R1': 2, …}`）⇒ 期初／期末**字面不同**。
   故除**全等**外另取**前綴鍵**（截至首個 `{`／`（`／`(`），二者**並報**，
   ⛔ 只用其一；前綴命中而全等不中者**逐項具名**。

用法：`python .../probe_WG9268p_c2_p9class.py <期初log> <期末log>`
"""
import io
import re
import sys

PRE = sys.argv[1]
POST = sys.argv[2]

_PASS = re.compile(r"^\s*✅ PASS\s\s(.*?)\s*$")
_FAIL = re.compile(r"^\s*🔴 FAIL\s\s(.*?)\s*$")


def judged(path):
    p, f = [], []
    for ln in io.open(path, encoding="utf-8", errors="replace").read() \
            .replace("\r\n", "\n").split("\n"):
        m = _PASS.match(ln)
        if m:
            p.append(m.group(1))
            continue
        m = _FAIL.match(ln)
        if m:
            f.append(m.group(1))
    return p, f


def pref(s):
    for ch in ("{", "（", "("):
        i = s.find(ch)
        if i > 0:
            return s[:i].strip()
    return s.strip()


pre_p, pre_f = judged(PRE)
post_p, post_f = judged(POST)

print("=" * 118)
print("【`c2`】`P-9` 之機械歸類（類 `(ii)` vs 類 `(iii)`）")
print("=" * 118)
print("三軸 (1) 期初 ＝ %s ／期末 ＝ %s" % (PRE, POST))
print("三軸 (2) 母體 ＝ 二 log 之 `✅ PASS` ＋ `🔴 FAIL` 判定行")
print("三軸 (3) 粒度框 ＝ **名目**（全等 ＋ 前綴鍵·二者並報）")
print()
print("🔒 期初：PASS **%d** ／FAIL **%d** ／合計 **%d**"
      % (len(pre_p), len(pre_f), len(pre_p) + len(pre_f)))
print("🔒 期末：PASS **%d** ／FAIL **%d** ／合計 **%d**"
      % (len(post_p), len(post_f), len(post_p) + len(post_f)))
print()

pre_pset, pre_fset = set(pre_p), set(pre_f)
pre_ppref = {pref(x) for x in pre_p}
pre_fpref = {pref(x) for x in pre_f}

new_fail = [x for x in post_f if x not in pre_fset]
print("🔒 期末 FAIL 而期初⛔ FAIL 者 ＝ **%d** 項（本節之受詞）" % len(new_fail))
print()

c_ii, c_iii, amb = [], [], []
for nm in new_fail:
    k = pref(nm)
    exact_pass = nm in pre_pset
    pref_pass = k in pre_ppref
    pref_fail = k in pre_fpref
    if exact_pass:
        c_iii.append((nm, "期初**全等** PASS"))
    elif pref_pass:
        c_iii.append((nm, "期初**前綴** PASS（名目含動態內容·前綴鍵 `%s`）" % k))
    elif pref_fail:
        amb.append((nm, "期初**前綴** FAIL（前綴鍵 `%s`）⇒ 同一檢而名目變 ⇒ ⛔ 本差集之受詞" % k))
    else:
        c_ii.append((nm, "期初**⛔ 出現**（既非 PASS 亦非 FAIL）⇒ 該世代**未執行**"))

print("── 類 `(iii)`　**真迴歸**（原可達且原綠而今紅）＝ **%d** 項" % len(c_iii))
for nm, why in c_iii:
    print("   🛑 %s" % nm)
    print("      〔%s〕" % why)
print()
print("── 類 `(ii)`　**新可達之世代所新曝**之紅 ＝ **%d** 項" % len(c_ii))
for nm, why in c_ii:
    print("   🟡 %s" % nm)
print()
print("── ⚠️ **前綴命中 FAIL**（同一檢·名目字面變動）＝ **%d** 項" % len(amb))
for nm, why in amb:
    print("   ⚠️ %s" % nm)
    print("      〔%s〕" % why)
print()

# 🔑 判別力（證本器非恆綠亦非恆紅）
probe_iii = [x for x in pre_p if x][:1]
print("🔑 **判別力（兩造·⛔ 恆綠）**")
if probe_iii:
    t = probe_iii[0]
    print("   [必紅] 取一**期初 PASS** 之名目 `%s` 假設其今紅 ⇒ 本式判 ＝ **類 (iii)** %s"
          % (t[:48], "✅" if (t in pre_pset) else "🔴"))
else:
    print("   🛑 期初⛔ 任何 PASS ⇒ 判別力對照**不可造** ⇒ loud")
fake = "⟨必不存在之名目·執行期組出⟩"
print("   [必綠] 一必不存在之名目 ⇒ 本式判 ＝ **類 (ii)** %s"
      % ("✅" if (fake not in pre_pset and fake not in pre_fset) else "🔴"))
print()

print("=" * 118)
if c_iii:
    print("🛑 **停機款觸發**（施工單 `§八`）：類 `(iii)` 真迴歸 **非空**（%d 項）" % len(c_iii))
    sys.exit(1)
print("✅ 類 `(iii)` 真迴歸 ＝ **空** ⇒ `P-9` 之停機款**未觸發**")
if amb:
    print("⚠️ 惟有 **%d** 項前綴命中 FAIL，須於報告內逐項具名（⛔ 靜默）" % len(amb))
print("=" * 118)
sys.exit(0)
