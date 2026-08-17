#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`W-G.9-42` 純追加稽核器（受詞可為 **檔** 或 **段**·⛔ 二者不合併算）。

🔒 **為何需要一支工具**（⛔ 非為了好看）：
  `S-5`（嚴格前綴不成立 ⇒ 停）於本批同時作用於**兩種受詞層級**——
  末端追加者受詞為**檔**，就地加註者受詞為**段**（插入點在檔中 ⇒ 檔級必然 False）。
  自誤 **13** 之案由正是「未綁受詞層級」；`W-G.9-41` §七 已以**分解驗證**處置。
  ⇒ 本器把該分解**機械化**，並強制每項附**判別力自檢**。

🔒 **量測框**：字元 ＝ python `len()`；比對前兩側一律 `CRLF → LF`
  （`CLAUDE.md`「位元組數／校驗碼須聲明量測框」·本機 working tree 為 CRLF、blob 為 LF）。

🔒 **判別力自檢（⛔ 不得省）**：對每一項，另以「**於舊文行中插入一字**」之竄改本重跑，
  **須得 False**。若竄改本亦 True，該項之 PASS ⛔ 不得採信（＝閘恆綠·考古 65 族）。

⚠️ **本器不判「內容對不對」**，只判「**舊文有沒有被動過**」。
  受詞為段者，另檢**段前與段後之補集逐字未變**——否則「段內純追加」可掩護段外之刪改。

用法：
    python verify/tools/wg942_append_audit.py            # 對 HEAD 比
    python verify/tools/wg942_append_audit.py <base-ref> # 對指定 commit 比
"""
import io
import subprocess
import sys

# (路徑, 受詞, 段起字樣, 段訖字樣)　受詞 "檔" 時後二者為 None
# 🔒 段界字樣一律取**可 grep 之唯一字樣**，⛔ 不以行號為錨（`CLAUDE.md` 行號衛生第 4 款）。
TARGETS = [
    (".gitattributes", "檔", None, None),
    ("docs/specs/figures/README.md", "段",
     "⚠️ 上節第 31–32 行之「CC 無法自對話擷取／請 KL 置於 `Downloads/`」",
     "🔴 **權威射程（承 `PROVENANCE §四`）**"),
    ("docs/specs/figures/PROVENANCE_宗地分配線邏輯.md", "段",
     "🛑 **`.jpg` 二檔待補件**", "## §二 元資料"),
    ("docs/reports/W-G.9波_claude.ai側自誤登記.md", "檔", None, None),
    ("docs/reports/W-G.4_泛用阻塞項登記表.md", "檔", None, None),
    ("docs/驗證裁定登記表.md", "檔", None, None),
    ("CLAUDE.md", "段", "**K-9 五則（KL 裁 2026-08-01·canonical 見正典**", "- 前置地基檢查："),
    # 🔒 `K-6` 本批受**三處就地加註** ⇒ 檔級嚴格前綴**必然 False**（插入點在檔中）。
    #   依自誤 **13**（受詞未綁結構層）與 `W-G.9-41` §七之**分解驗證**家法，
    #   受詞降為**段**，並另檢**補集逐字未變**（否則「段內純追加」可掩護段外之刪改）。
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "段",
     "| **K-9-5** | 街角第 1 宗**寬度要實量**",
     "### K-9 §一-1、合併後之分配成果判準"),
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "段",
     "⇒ 本則與 `K-9-2`／`K-9-3` **互不取代、互不衝突**。",
     "**四、不合格之處置**"),
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "段",
     "⚠️ 依 **`K-9-3`**，宗地層**一律不量深度** ⇒ 本款**僅供名詞釐清**",
     "**八、參考線之身分（⛔ 禁互代）**"),
    # ── `W-G.9-43` 追加之受詞（`K-9-6-h ②` 就地加註）────────────────────────
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "段",
     "   **一條都沒有 ⇒ ⛔ 不算臨後側境界線 ⇒ 停機報錯**",
     "③ 最小寬度之計算域"),
    (".claude/skills/failure-archaeology/SKILL.md", "檔", None, None),
    # ── `W-G.9-44` 追加之受詞 ────────────────────────────────────────────
    ("docs/reports/W-G.9-43_K9-11入倉與平行判測.md", "檔", None, None),
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "段",
     "🔒 **逐字段已保留原字**；本讀法⛔ **不得寫回逐字段**",
     "#### K-9-11 之定式"),
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "段",
     "> ⇒ 若 KL 認二者**非**同構，本款須重訂；⛔ 不得以「逐字已載」稱之。",
     "**四、遞補者須重測**"),
    # ── `W-G.9-47` 追加之受詞（`K-9-10 四` 就地加註）────────────────────
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "段",
     "⛔ 非垂距、⛔ 非 MBR 短邊、⛔ 非內接矩形寬。",
     "**五、最小寬度**"),
    ("docs/reports/W-G.9-44_呈KL兩題.md", "檔", None, None),
]

# 受詞為「段」而**同一檔有多段**者：補集之檢查須把**全部段**一起挖掉再比
#   ——逐段各自檢補集會互相誤報（甲段之補集含乙段之新增）。
MULTI = {}
for _p, _k, _h, _t in TARGETS:
    if _k == "段":
        MULTI.setdefault(_p, []).append((_h, _t))


def blob(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8").replace("\r\n", "\n")


def work(path):
    return io.open(path, encoding="utf-8", newline="").read().replace("\r\n", "\n")


def cut(s, head, tail):
    """取 [head, tail) 之段。⛔ 任一字樣缺席或多命中即 raise（⛔ 不靜默取第一個）。"""
    if s.count(head) != 1:
        raise RuntimeError(f"段起字樣命中 {s.count(head)} 次（須恰 1）：{head!r}")
    i = s.index(head)
    if s.count(tail) < 1:
        raise RuntimeError(f"段訖字樣 0 命中：{tail!r}")
    j = s.index(tail, i)
    return s[i:j], s[:i], s[j:]


def complement(s, segs):
    """把 `segs` 所指之全部段自 `s` 挖除，回其餘部分（＝補集）。
    🔒 一次挖全部段，⛔ 非逐段各自挖——後者於同檔多段時會互相誤報。"""
    spans = []
    for head, tail in segs:
        i = s.index(head)
        spans.append((i, s.index(tail, i)))
    spans.sort()
    out, pos = [], 0
    for a, b in spans:
        out.append(s[pos:a])
        pos = b
    out.append(s[pos:])
    return "".join(out)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    bad = 0
    print(f"【`W-G.9-42` 純追加稽核】base ＝ {base}")
    print("=" * 78)
    for path, kind, head, tail in TARGETS:
        old_all = blob(base, path)
        if old_all is None:
            print(f"  ⛔ {path}：{base} 無此檔（新檔）⇒ 不適用嚴格前綴")
            continue
        new_all = work(path)
        if kind == "檔":
            old, new = old_all, new_all
            extra = ""
        else:
            old, _, _ = cut(old_all, head, tail)
            new, _, _ = cut(new_all, head, tail)
            # 補集：把**該檔全部受詞段**一併挖掉後比對（⛔ 非逐段各自比）
            #
            # 🩸 **判準之更正（`W-G.9-43`·⛔ 非放寬）**：首版用**相等**，於「同批既有
            #   **段內加註**又有**檔末追加**」時會誤報——`K-9-11` 追加於 `K-6` 檔末，
            #   落在全部四段之外 ⇒ 補集必然改變，而該改變**正是合法之純追加**。
            #   ⇒ 正確判準為 **新補集以舊補集為嚴格前綴**（容許檔末追加、仍擋任何刪改）。
            #   🔒 **⛔ 不是把閘關掉**：段外之**刪除或行中竄改**仍會使 `startswith` 為 False。
            oc, nc = complement(old_all, MULTI[path]), complement(new_all, MULTI[path])
            same_comp = nc.startswith(oc)
            # 判別力自檢：於舊補集行中插入一字 ⇒ 須 False
            oc_tam = oc[: len(oc) // 2] + "中" + oc[len(oc) // 2:]
            comp_disc = nc.startswith(oc_tam)
            extra = (f"　補集（扣除該檔全部 {len(MULTI[path])} 段·判準＝嚴格前綴）："
                     f"{'✅' if same_comp else '🔴異'}"
                     f"／判別力自檢＝{comp_disc}（須 False）")
            if (not same_comp) or comp_disc:
                bad += 1
        ok = new.startswith(old)
        # 判別力自檢：於舊文正中插入一字 ⇒ 須 False
        tam = old[: len(old) // 2] + "中" + old[len(old) // 2:]
        disc = new.startswith(tam)
        if not ok or disc:
            bad += 1
        print(f"  {'✅' if ok else '🔴'} [{kind}] {path}")
        print(f"       {len(old)} → {len(new)}　嚴格前綴＝{ok}"
              f"　判別力自檢（行中插入）＝{disc}（須 False）{extra}")
    print("=" * 78)
    print(f"  結論：{'✅ 全部成立' if bad == 0 else f'🔴 {bad} 項不成立 ⇒ S-5 觸發'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
