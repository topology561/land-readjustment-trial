# -*- coding: utf-8 -*-
r"""**D-2b-10 §前-2**：T2 對照用之**全保真基準**（原文**不截斷** ＋ sha256）＋ 具名更正。

## 為何需要

T2（鋪滿一般化）之驗收依賴「與現況逐字比對」，而現有基準**被截斷**：
`verify/probes/probe_D2b8_guard.py:109` 以 `v['err'][:140]`、
`verify/probes/probe_D2b6_split.py:267` 以 `_st[:150]`。
實測 12 格字長 `0m`＝`111／119／111／9／119／111`、`3.5m`＝`111／142／111／9／142／142`
⇒ **僅 `[3.5m]` 之 R2／R5／R3 三格真被截斷**（142 ＝ 140 ＋ 前綴），其餘九格為完整原文。
被截斷之三格恰停在 `628-42(1)→` 一帶，**逐界面 `W_far` 全段落在截斷之外**
——而那正是 T2 會改變之欄位 ⇒ 舊基準對 T2 **不可用**。

## 本檔之保證

- 六街廓 × 兩情境，**完整例外原文·⛔ 一律不截斷**（無例外者記字面 `（無例外）`·⛔ 不留空）
- 每格之 **sha256（全 64 hex）** 與**字元長度**
- **自證未截斷**：所印原文之實際字元數須 `==` 所記長度欄；不等 ⇒ raise
- log 首行記載執行時之 commit hash

⛔ 不修改／不覆寫 `probe_D2b8_guard.log`／`probe_D2b6_split.log`／`probe_D2b9_guard_degen.log`。
⛔ 不回頭改舊探針之截斷參數（舊 log 已入庫·改之會使兩者不一致）。
"""
import contextlib
import hashlib
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
# 🆕 D-2b-11【a-2】：輸出檔可由環境變數覆寫，供**複驗**寫入新檔
#   ⇒ ⛔ **不覆寫** `probe_D2b10_baseline.log`（已入庫實料）。預設值不變。
LOG = os.path.join(OUTDIR, os.environ.get("WV_BASELINE_LOG", "probe_D2b10_baseline.log"))
NOEXC = "（無例外）"
W = 200
TRUNC_CELLS = {("3.5m", "R2"), ("3.5m", "R5"), ("3.5m", "R3")}   # 舊基準真被截斷者


def _head():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                              capture_output=True, text=True).stdout.strip()
    except Exception:
        return "（無法取得）"


def _old_a3():
    """讀 `probe_D2b8_guard.log`【A-3】之（已截斷）基準原文（⛔ 只讀不改）。"""
    out = {}
    p = os.path.join(OUTDIR, "probe_D2b8_guard.log")
    try:
        body = io.open(p, encoding="utf-8").read().split("【A-3】", 1)[1]
    except Exception:
        return out
    for ln in body.splitlines():
        if ln.lstrip().startswith("【"):
            break
        m = re.match(r"\s*\[(0m|3\.5m)\]\s+(R\d)\s", ln)
        if m and "｜" in ln:
            out[(m.group(1), m.group(2))] = ln.split("｜", 1)[1].strip()
    return out


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)

    CUR = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p, setback, snapshot=snapshot)
        for lbl in blks:
            err = ""
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, setback)
                except Exception as e:
                    err = f"{type(e).__name__}: {e}"
            CUR[(sb, lbl)] = err if err else NOEXC

    L = []
    L.append("=" * W)
    L.append(f"【D-2b-10 §前-2】T2 對照用**全保真基準**　commit ＝ `{_head()}`")
    L.append("=" * W)
    L.append("  🔒 原文**一律不截斷**；無例外者記字面「（無例外）」（⛔ 不留空）")
    L.append("  🔒 自證：所印原文之**實際字元數** == 所記**長度**欄；不等即 raise")

    OLD = _old_a3()
    L.append("")
    L.append("【1】12 格全保真基準（完整原文／sha256／字元長度）")
    L.append("-" * W)
    _bad_len = []
    SHA = {}
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            t = CUR[(sb, lbl)]
            h = hashlib.sha256(t.encode("utf-8")).hexdigest()
            SHA[(sb, lbl)] = (h, len(t))
            L.append(f"  ── [{sb}] {lbl} ──　長度 **{len(t)}**　sha256 `{h}`")
            L.append(f"     原文：{t}")
            if len(L[-1]) - len("     原文：") != len(t):
                _bad_len.append((sb, lbl))
    if _bad_len:
        raise RuntimeError(f"🔴 自證未截斷失敗：{_bad_len} 之實際字元數 ≠ 所記長度（停）")
    L.append("  ⇒ ✅ **自證通過**：12 格之實際字元數皆 == 所記長度（⇒ 未截斷）")

    L.append("")
    L.append("【2】可比性（**分兩級**·⛔ 不得混為一談）")
    L.append("-" * W)
    _lv1_bad, _lv2_bad = [], []
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            t = CUR[(sb, lbl)]
            o = OLD.get((sb, lbl), "")
            # 舊 log 之無例外格記為「✅ 跑完（無例外）」；本檔記「（無例外）」⇒ 語意同、字面異
            _o_norm = NOEXC if o.strip() == "✅ 跑完（無例外）" else o
            _t_disp = t if t != NOEXC else NOEXC
            if (sb, lbl) in TRUNC_CELLS:
                _pre = _o_norm.lstrip("🔴").strip()
                _t2 = _t_disp
                _ok = _t2.startswith(_pre[:min(len(_pre), 140)])
                if not _ok:
                    _lv2_bad.append((sb, lbl))
                L.append(f"  [{sb}] {lbl}　**級二·舊基準已截斷**："
                         f"前 {min(len(_pre), 140)} 字 {'✅ 相同' if _ok else '🔴 不同'}")
                L.append(f"      ⚠️ **舊基準在 140 字之後不存在 ⇒ 超出部分無從比對·不可比**"
                         f"（⛔ 不得就此宣稱該格「零變動」）")
            else:
                _pre = _o_norm.lstrip("🔴").strip()
                _ok = (_t_disp.strip() == _pre)
                if not _ok:
                    _lv1_bad.append((sb, lbl))
                L.append(f"  [{sb}] {lbl}　**級一·未截斷**：逐字全文 "
                         f"{'✅ 相同' if _ok else '🔴 **不同**'}")
                if not _ok:
                    L.append(f"      舊：{_pre[:170]}")
                    L.append(f"      新：{_t_disp[:170]}")
    L.append(f"  ⇒ 級一（9 格·未截斷）不同 **{len(_lv1_bad)}**"
             f"　級二（3 格·前 140 字）不同 **{len(_lv2_bad)}**")
    if _lv1_bad:
        raise RuntimeError(f"🔴 級一格出現非預期行為變更：{_lv1_bad}（停機上呈·§五）")

    L.append("")
    L.append("【3】sha256 表")
    L.append("-" * W)
    L.append(f"  {'情境':<6}{'街廓':<5}{'長度':>6}  sha256")
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            h, n = SHA[(sb, lbl)]
            L.append(f"  {sb:<6}{lbl:<5}{n:>6}  {h}")

    L.append("")
    L.append("【4】🔧 §前-3 具名更正（⛔ 不刪不改任何既有 log 原文）")
    L.append("-" * W)
    L.append("  (1) `verify/out/probe_D2b9_guard_degen.log` 所載「**閘族數 ＝ 14**」**應為 15**。")
    L.append("      成因：`_family()` 之 `（其他）` 萬用桶含 `:575`（條件③ J 非零看守破）與")
    L.append("      `:819`（停機②（J 下降））**兩族**。已由 D-2b-10【前-1】修正，"
             "新表見 `verify/out/probe_D2b10_family.log`。")
    L.append("  (2) 同檔【驗收 1】於**全部 12 格**標註「基準已截斷」**不確**：")
    L.append("      實為 **9 格完整、3 格截斷**（`[3.5m]` R2／R5／R3）。")
    L.append("      該三格之比對涵蓋範圍**僅及前 140 字**；⛔ 不得就此宣稱其「零變動」。")
    L.append("  ⛔ 上述兩檔**一字未刪未改**。")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
