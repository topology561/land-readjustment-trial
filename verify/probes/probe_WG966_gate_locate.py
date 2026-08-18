#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-66】**受詞定位**：街角第 1 宗之資格閘 ＋ 寬度閘之不存在 ⛔ 零生產碼

**受詞**：`K-9-5-3`（硬門檻·不設容差）與 `K-9-5-2-a`-3（面積過、寬不足 ⇒ loud raise）
**二則所預設之量測——「街角範圍之寬度」——生產碼今天有沒有做？**

🔴 **本檔之出艙句式受嚴格限制**（施工單 §二 A-2 明令）：
  ⛔ **不得**由「字樣全 0」推論「二則正典已被遵守」；
  ✅ **正確陳述** ＝ 「**二則所預設之量測，生產碼未做 ⇒ 二則今日皆無施力點**」。

🔒 **空集⛔ 不得作為證據**——A-2 之表附**二個必為非 0 之對照**，
  另附 **A-4-2 變異注入**（於 `scratchpad` 之 `app.py` 複本插入含 `fits_at` 之註解）
  ⇒ 證該 grep 管線**確實會回非 0**。🔑 **一個從未回過非 0 的 grep，跟一段註解證據力相同。**
🔒 **變異一律於複本為之**（⛔ 不動倉內 `app.py`），跑完**刪除複本**並出艙該事實。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import ast
import io
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
ROOT = os.path.dirname(VERIFY)
for _p in (VERIFY, os.path.join(VERIFY, "fixtures"), HERE):
    sys.path.insert(0, _p)

import run_verification as rv                                       # noqa: E402
from app_harvest import harvest                                     # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 160
SB = 0.0
APP = os.path.join(ROOT, "app.py")
EIGHT = [("R1", "left"), ("R1", "right"), ("R2", "left"), ("R3", "right"),
         ("R4", "left"), ("R4", "right"), ("R5", "left"), ("R6", "right")]
SIDE_ZH = {"左": "left", "右": "right"}

# A-2 之六字樣（⛔ 逐項出艙·⛔ 不得只報「都沒有」）
PATS = ["fits_at", "rect_fits", "w_max", "寬度 >=", "width >=", "矩形容納"]
# 判別力對照（須 ≥1·⇒ 證該管線會回非 0）
CTRL = ["min_area_to_apply", "parcel_min_width_n14"]
ANCHOR = "cand_G < cand.get('min_area_to_apply'"


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _count(pat, path):
    """該字樣於該檔之**命中行數**（⛔ 顯式 UTF-8 解碼·本機 `text=True` 會走 cp950）。"""
    r = subprocess.run(["grep", "-c", "--", pat, path], capture_output=True, timeout=30)
    out = (r.stdout or b"").decode("utf-8", "replace").strip()
    return int(out) if out.isdigit() else 0


def _lines(pat, path):
    r = subprocess.run(["grep", "-n", "--", pat, path], capture_output=True, timeout=30)
    return [x for x in (r.stdout or b"").decode("utf-8", "replace").splitlines() if x.strip()]


def _enclosing_func(path, lineno):
    """回包住該行之**最內層** `def` 之名（⛔ 以 AST 判·非字串猜）。"""
    tree = ast.parse(io.open(path, encoding="utf-8").read())
    best = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            end = getattr(node, "end_lineno", None)
            if end is not None and node.lineno <= lineno <= end:
                if best is None or node.lineno > best.lineno:
                    best = node
    return (best.name, best.lineno) if best else (None, None)


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-66】**受詞定位**：街角第 1 宗之資格閘 ＋ **寬度閘之不存在**")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；A-4-2 之變異一律於 `scratchpad` 之複本為之、跑完即刪。")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【A-1】街角第 1 宗之**資格閘**（⛔ 逐字出艙）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-1】生產碼之**街角第 1 宗資格閘**（⛔ 逐字·⛔ 附命中數與所屬函式）")
    P("=" * WID)
    hits = _lines(ANCHOR, APP)
    P(f"  🔒 錨（施工單所給·**CC 已自行複查**）：`{ANCHOR}`")
    P(f"  🔒 於 `app.py` 之**命中數 ＝ {len(hits)}**")
    for h in hits:
        ln = int(h.split(":", 1)[0])
        body = h.split(":", 1)[1]
        fn, fl = _enclosing_func(APP, ln)
        P(f"     · 行 {ln}（成立於 commit **{sha}**）")
        P(f"       **逐字** ＝ `{body.strip()}`")
        P(f"       所屬函式（AST 判定·⛔ 非字串猜）＝ **`{fn}`**（其 `def` 於行 {fl}）")
    P("")
    P("  🔒 **`min_area_to_apply` 之全部出現處**（⛔ 正面列舉·⇒ 門檻從哪來）")
    P(f"  {'行':>7}   {'逐字':<110}{'所屬函式':<28}")
    P("-" * WID)
    for h in _lines("min_area_to_apply", APP):
        ln = int(h.split(":", 1)[0])
        body = h.split(":", 1)[1].strip()
        fn, _fl = _enclosing_func(APP, ln)
        P(f"  {ln:>7}   {body[:110]:<110}{str(fn):<28}")
    P("-" * WID)
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【A-2】寬度閘之**不存在**（⛔ 正面列舉·⛔ 空集不得作為證據）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-2】**街角範圍之寬度判定**是否存在於 `app.py`（⛔ 逐項出艙命中數）")
    P("=" * WID)
    P(f"  {'#':>3}  {'字樣':<26}{'命中數':>8}   {'性質':<40}")
    P("-" * WID)
    n_pat = {}
    for i, p in enumerate(PATS, 1):
        c = _count(p, APP)
        n_pat[p] = c
        note = ""
        if c and p == "矩形容納":
            note = "⚠️ 須辨明「註解 vs 判定碼」（見下）"
        P(f"  {i:>3}  {p:<26}{c:>8}   {note:<40}")
    P("-" * WID)
    P(f"  {'—':>3}  {'（判別力對照）':<26}")
    ctrl_ok = True
    for p in CTRL:
        c = _count(p, APP)
        ctrl_ok &= (c >= 1)
        note = ("⚠️ **宗地層**之寬·⛔ 非街角範圍之寬" if p == "parcel_min_width_n14" else "")
        P(f"  {'—':>3}  {p:<26}{c:>8}   {note:<40}")
    P("-" * WID)
    allzero = all(v == 0 for v in n_pat.values())
    P(f"  ⇒ 六字樣 **{'全部為 0' if allzero else '🔴 有非 0 者'}**；"
      f"二對照 **{'皆 ≥1' if ctrl_ok else '🔴 有 0 者'}**")
    P("")
    P("  🔴 **本表之<u>正確讀法</u>（施工單 §二 A-2 明令·⛔ 不得改寫）**：")
    P("     ⛔ **不得**由「全 0」推論「二則正典已被遵守」。")
    P("     ✅ 正確陳述 ＝ **「二則所預設之量測（街角範圍之寬度實量），")
    P("        生產碼未做 ⇒ 二則今日皆<u>無施力點</u>。」**")
    P("     🔒 `parcel_min_width_n14`（29 命中）係 **N-14 之<u>宗地</u>寬度**，")
    P("        **⛔ 非** `K-9-5-2 ③`／`K-9-5-3` 所指之「**街角規定範圍**之寬度」")
    P("        ——**同名不同量**，⛔ 不得互代。")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【A-4-2】變異注入（⇒ 證該 grep 管線非恆 0）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-4-2】🔴 **變異注入**：於 `scratchpad` 之 `app.py` **複本**插入含 `fits_at` 之註解")
    P("=" * WID)
    tmp = os.environ.get("TEMP") or os.environ.get("TMP") or VERIFY
    cp = os.path.join(tmp, "_wg966_app_copy.py")
    before = _count("fits_at", APP)
    shutil.copyfile(APP, cp)
    with io.open(cp, "a", encoding="utf-8") as f:
        f.write("\n# W-G.9-66 變異注入（⛔ 複本·跑完即刪）：fits_at\n")
    after = _count("fits_at", cp)
    existed = os.path.exists(cp)
    os.remove(cp)
    removed = not os.path.exists(cp)
    P(f"  · 複本路徑（⛔ 倉外）：`{cp}`")
    P(f"  · 倉內 `app.py` 之 `fits_at` 命中 ＝ **{before}**")
    P(f"  · 複本（已注入）之 `fits_at` 命中 ＝ **{after}**")
    P(f"  ⇒ **{before} ⇒ {after}** "
      f"{'✅ 該管線確會回非 0（⇒ ⛔ 非恆 0）' if (before == 0 and after >= 1) else '🔴 未證'}")
    P(f"  🔒 複本已建立 ＝ {existed}；**已刪除 ＝ {removed}**（⛔ 不留殘檔）")
    P(f"  🔒 倉內 `app.py` 之命中**未變** ＝ {_count('fits_at', APP) == before}（⛔ 未動倉內）")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【A-3】「面積過」之逐格坐實（`K-9-5-2-a`-3 之另一半要件）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-3】🔴 **「面積過」之逐格坐實**：八格之 `真G` vs `門檻`（＝ `min_area_to_apply`）")
    P("=" * WID)
    P("  🔒 **本項之量取自 `run_corner_pk` 之<u>診斷列</u>**——該閘於街角 PK 期間評值，")
    P("     ⇒ **⛔ 不需 `run_step_g`** ⇒ 既有停機（`GB-55`／`GB-67`）**不阻斷本項**。")
    P("  🔒 **⛔ 不以 winner 計數充當已測**（`W-G.9-63` 僅載 winner 8／8 ＝ **間接**推論）。")
    P("")
    ns, fake = harvest()
    snap = rv.load_snapshot()
    cb, cad = rv.build_pipeline(ns, fake, snap)
    rv.build_ownership(ns, fake, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    tp, bp, _ = rv.build_build_parcels(ns, fake, v6, list(cb.values()), snap)
    params = rv.build_param_table(ns, fake, cb, cad, snap, SB)
    d0, _s2, _o2, win, forced = run_corner_pk(
        ns, fake, list(cb.values()), cad, params, tp, bp, SB, snapshot=snap)
    P(f"  🔒 `run_corner_pk` 診斷列數 ＝ **{len(d0 or [])}**（⇒ 母體非空·⛔ 空真假綠之防）")
    P("")
    sel = {}
    for r in (d0 or []):
        lbl = str(r.get("街廓", "")).strip()
        w = SIDE_ZH.get(str(r.get("端", "")).strip(), "")
        if str(r.get("選中", "")) == "✅":
            sel[(lbl, w)] = r
    P(f"  {'街廓':<5}{'側':<7}{'候選地號（winner）':>20}{'真G(㎡)':>14}"
      f"{'門檻(㎡)':>14}{'G − 門檻':>14}{'碼面達標欄':>12}{'判（面積過?）':>14}")
    P("-" * WID)
    n_pass = n_got = 0
    miss = []
    for lbl, which in EIGHT:
        r = sel.get((lbl, which))
        if r is None:
            miss.append(f"{lbl}/{which}")
            P(f"  {lbl:<5}{which:<7}{'（無選中列）':>20}{'—':>14}{'—':>14}"
              f"{'—':>14}{'—':>12}{'🛑 未取得':>14}")
            continue
        g = r.get("真G(㎡)")
        th = r.get("門檻(㎡)")
        if g in ("", None) or th in ("", None):
            miss.append(f"{lbl}/{which}")
            P(f"  {lbl:<5}{which:<7}{str(r.get('候選地號', '')):>20}"
              f"{str(g or '—'):>14}{str(th or '—'):>14}{'—':>14}"
              f"{str(r.get('達標', '—')):>12}{'🛑 值缺':>14}")
            continue
        n_got += 1
        gf, tf = float(g), float(th)
        ok = gf >= tf
        n_pass += 1 if ok else 0
        P(f"  {lbl:<5}{which:<7}{str(r.get('候選地號', '')):>20}{gf:>14.2f}"
          f"{tf:>14.2f}{gf - tf:>14.2f}{str(r.get('達標', '—')):>12}"
          f"{('✅ 過' if ok else '🔴 不過'):>15}")
    P("-" * WID)
    P(f"  ⇒ **取得 {n_got}／8 格**；其中**面積過 {n_pass} 格**"
      + (f"　🛑 **未取得者逐格具名：{'／'.join(miss)}**" if miss else "　（⛔ 無未取得之格）"))
    P("")
    P("  🔒 **三焦點格之逐格判**（`K-9-5-2-a`-3 之逐字要件 ＝「**面積過**、寬不足」）")
    for lbl, which in [("R1", "right"), ("R5", "left"), ("R6", "right")]:
        r = sel.get((lbl, which))
        if r is None:
            P(f"     · `{lbl}/{which}` ⇒ 🛑 未取得 ⇒ ⛔ 該格之「面積過」**未經坐實**")
            continue
        g, th = r.get("真G(㎡)"), r.get("門檻(㎡)")
        if g in ("", None) or th in ("", None):
            P(f"     · `{lbl}/{which}` ⇒ 🛑 值缺 ⇒ ⛔ 該格之「面積過」**未經坐實**")
            continue
        P(f"     · `{lbl}/{which}`（winner `{r.get('候選地號', '')}`）：真G `{float(g):.2f}` "
          f"vs 門檻 `{float(th):.2f}` ⇒ **{'面積過 ✅' if float(g) >= float(th) else '面積不過 🔴'}**"
          f"；甲式寬度短少 > 0（`W-G.9-65` §C-1）⇒ "
          f"**{'⇒ 確為「面積過、寬不足」' if float(g) >= float(th) else '⇒ ⛔ 非該款之情形'}**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【E】逐項判定
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【E】逐項判定")
    P("=" * WID)
    items = [
        ("A-1", f"資格閘之錨命中 ＝ {len(hits)}（須 1）·已出艙逐字與所屬函式", len(hits) == 1),
        ("A-2", f"六字樣{'全 0' if allzero else '有非 0'}；二對照{'皆 ≥1' if ctrl_ok else '有 0'}",
         allzero and ctrl_ok),
        ("A-4-1", "反例存在檢：對照確為非 0 ⇒ grep 管線會回非 0", ctrl_ok),
        ("A-4-2", f"變異注入：{before} ⇒ {after}；複本已刪 ＝ {removed}",
         before == 0 and after >= 1 and removed),
        ("A-3", f"面積閘：取得 {n_got}／8·面積過 {n_pass} 格", n_got == 8 and n_pass == 8),
    ]
    for k, t, ok in items:
        P(f"  {k:<8}{'✅' if ok else '🔴'}　{t}")
    P("-" * WID)
    P(f"  ⇒ **{'✅ 全部成立' if all(o for _a, _b, o in items) else '🔴 有未成立項'}**")
    P("")
    P("  🔴 **`Z-1` 之入倉條件**（施工單 §三）：")
    P(f"     ① A-2 字樣 1〜5 全 0 ⇒ **{'✅ 成立' if all(n_pat[p] == 0 for p in PATS[:5]) else '🔴 不成立'}**")
    P(f"     ② A-3「面積過」成立 ⇒ **{'✅ 成立' if (n_got == 8 and n_pass == 8) else '🔴 不成立'}**")
    P(f"     ⇒ **{'✅ 可入倉 `Z-1`' if (all(n_pat[p] == 0 for p in PATS[:5]) and n_got == 8 and n_pass == 8) else '🛑 ⛔ 停止入倉 `Z-1`，改為只報告'}**")
    P("=" * WID)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG966_gate_locate_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
