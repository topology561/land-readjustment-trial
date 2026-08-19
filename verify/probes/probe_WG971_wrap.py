#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-71 A 組】`W-D.4` 恆紅之真因坐實　⛔ 零生產碼·⛔ 不動任何名單

**受詞**：`wv_reconcile` 之 `R1`／`R2` 於 `W-D.4` 之
`stepg_pipeline.py", line 995` 一行上**究竟跑過幾次**（⛔ 不是「應該會跑」·考古節 96 之第一問）。

🔒 **樣式一律取 `wv_reconcile` 之<u>實際</u>符號**（`_FILE_TOKEN`／`_r1`／`_r2`／`normalize`），
  ⛔ **不自寫近似樣式**（否則量的是我自己寫的那個，不是它）。

🔒 **本檔只量、不改**：⛔ 不改 `RULES`／`_FILE_TOKEN`／`DEFAULT_LIST`，⛔ 不重生任何名單。
🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import wv_reconcile as wr                                           # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 116
NEEDLE = 'stepg_pipeline.py", line 995'

FROZEN = os.path.join(OUTDIR, "K6A2_期望FAIL名單_WG97_名目加原因.txt")
SRCLOG = os.path.join(OUTDIR, "WG928_runall.log")          # 名單檔頭所載之「新來源 log」
CURLOG = os.path.join(OUTDIR, "wg970_runall_after_a9e5671.log")


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _hash_object(p):
    r = subprocess.run(["git", "hash-object", p], cwd=REPO,
                       capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip()


def read(p):
    return io.open(p, encoding="utf-8", errors="replace").read()


def _wd4_detail_line(text):
    """取 `W-D.4` **明細**中含 `NEEDLE` 之那一行（⛔ 非 log 中另一處完整 traceback）。

    判準：該行**與 `[W-D.4] compute 失敗` 同屬一段明細**——即其**前一行**即該訊息。
    ⛔ 不取「第一個含 NEEDLE 之行」（那會命中 `run_verification` 直接印之完整堆疊）。
    """
    lines = text.split("\n")
    for i, x in enumerate(lines):
        if NEEDLE in x and "凍存:" not in x and "現況:" not in x:
            if i and "[W-D.4] compute 失敗" in lines[i - 1]:
                return x
    return None


def detail_tokens(log_text):
    """log 之**被納入明細**之 `File "` token 數（＝ `render_list` 實際會寫出者）。

    🔒 ⛔ 不以「整份 log 之 token 數」作分母——log 另含**未進任何名目明細**之
      traceback 輸出（如 `run_verification` 直接印之堆疊）⇒ 那不是名單該有的。
    """
    items = wr.parse_log(log_text)
    n = 0
    for _nm, det in items:
        for d in det:
            n += len(wr._FILE_TOKEN.findall(d))
    return n, items


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-71 A 組】`W-D.4` 恆紅之真因坐實")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 ⛔ 零生產碼；樣式取 `wv_reconcile` 之實際符號；⛔ 未動任何名單。")
    P(f"  🔒 `_FILE_TOKEN` 之樣式（逐字）：{wr._FILE_TOKEN.pattern!r}")
    P(f"  🔒 `RULES` ＝ {tuple(r[0] for r in wr.RULES)}")
    P("")

    frozen_t, src_t, cur_t = read(FROZEN), read(SRCLOG), read(CURLOG)

    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-1】規則之**實際匹配數**（⛔ 本節之受詞）")
    P("=" * WID)
    P(f"  {'檔':<46}{'File \" 之 count()':>18}{'_FILE_TOKEN.findall()':>22}{'明細內之 token':>16}")
    P("-" * WID)
    rows = []
    for tag, p, t in (("凍存名單", FROZEN, frozen_t),
                      ("來源 log（名單檔頭所載）", SRCLOG, src_t),
                      ("現況 log（W-G.9-70）", CURLOG, cur_t)):
        raw = t.count('File "')
        fa = len(wr._FILE_TOKEN.findall(t))
        if p == FROZEN:
            det = sum(len(wr._FILE_TOKEN.findall(d))
                      for _n, dd in wr.parse_list(t) for d in dd)
        else:
            det, _ = detail_tokens(t)
        rows.append((tag, raw, fa, det))
        P(f"  {tag + '　' + os.path.basename(p):<46}{raw:>18}{fa:>22}{det:>16}")
    P("-" * WID)
    P(f"  🔒 來源 log 之 `git hash-object` ＝ `{_hash_object(SRCLOG)}`")
    P("     （名單檔頭所載之「新來源 log」hash：`81e6e909a8fd2ae3cbdb9311aa7da0ea20f05b84`）")
    P("")

    # ── R2 於該行上之實際改變次數 ──────────────────────────────
    P("  🔴 **`R1`／`R2` 於 `W-D.4` 之該行上之實際改變次數**")
    P(f"  {'來源':<28}{'該行 token 數':>14}{'R1 改變?':>10}{'R2 改變?':>10}{'normalize 改變?':>16}")
    P("-" * WID)
    hits = {}
    for tag, t in (("凍存名單", frozen_t), ("來源 log", src_t), ("現況 log", cur_t)):
        # 🔒 **須取 `W-D.4` <u>明細</u>之那一行**（⛔ 非 log 中另一處完整 traceback）
        #   ——首版取「第一個含 NEEDLE 之行」，於二 log 中命中的是 `run_verification`
        #   直接印之堆疊（含完整 `File "`）⇒ 量到的不是受詞。**已就地更正。**
        ln = _wd4_detail_line(t)
        if ln is None:
            P(f"  {tag:<28}{'（查無 W-D.4 明細行）':>14}")
            continue
        hits[tag] = ln
        ntok = len(wr._FILE_TOKEN.findall(ln))
        c1 = (wr._r1(ln) != ln)
        c2 = (wr._r2(ln) != ln)
        cn = (wr.normalize(ln) != ln)
        P(f"  {tag:<28}{ntok:>14}{str(c1):>10}{str(c2):>10}{str(cn):>16}")
    P("-" * WID)
    P("  ⇒ 🔒 **該行之 token 數為 0 ⇒ `R1`／`R2` 之 `sub` 匹配 0 次 ⇒ 改變 0 次**")
    P("     （⛔ 非「規則不足」——規則根本**沒有東西可吃**·考古節 96 第一問）")
    P("")

    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-2】折斷之來源（⛔ 逐字·⛔ 不猜）")
    P("=" * WID)
    for tag, t in (("凍存名單", frozen_t), ("來源 log", src_t), ("現況 log", cur_t)):
        lines = t.split("\n")
        idx = [i for i, x in enumerate(lines)
               if NEEDLE in x and "凍存:" not in x and "現況:" not in x]
        for i in idx[:1]:
            P(f"  ── {tag} ──")
            P(f"     [前一行 {i - 1}] {lines[i - 1]!r}")
            P(f"     [該行   {i}] {lines[i]!r}")
            P(f"     🔍 前一行含 `File \"`？ ⇒ **{'File \"' in lines[i - 1]}**")
            P(f"     🔍 該行含 `File \"`？　 ⇒ **{'File \"' in lines[i]}**")
            P("")
    P("  🔒 **判**：若前一行**不含** `File \"`，則該 token **⛔ 非被折到前一行**，而是**整段消失**")
    P("     ⇒ 機制為**截斷（truncation）**、⛔ **非折行（wrapping）**。")
    P("")
    P("  🔒 **截斷之產生點（正面列舉受檢檔·⛔ 非全倉排除法）**：")
    _rv = os.path.join(VERIFY, "run_verification.py")
    _rvt = read(_rv)
    P(f"     · `verify/run_verification.py` 之 `traceback.format_exc()[-` 命中 ＝ "
      f"**{_rvt.count('traceback.format_exc()[-')}**")
    for i, ln in enumerate(_rvt.split("\n"), 1):
        if "W-D.4" in ln and "format_exc" in ln:
            P(f"     · `:{i}` {ln.strip()}")
        elif '"W-D.4", False' in ln:
            P(f"     · `:{i}` {ln.strip()}")
    P(f"     · `verify/wv_reconcile.py` 之 `render_list` 每列格式 ＝ `    | {{d}}`"
      "（**逐字不折行、不截斷**）")
    P("     ⇒ 🔴 **截斷發生於 `run_verification` 產生 log 之時**，`render_list` 只是忠實轉寫。")
    P("")

    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-3】截斷點**隨路徑長度移動** ⇒ 該紅不可重現、不可比對")
    P("=" * WID)
    P("  ── (a) **實資料**（⛔ 非合成）：二側之殘存字串起頭 " + "─" * 46)
    obs = {}
    for tag, t in (("凍存名單（worktree `frosty-agnesi-fa87af`·名長 20）", frozen_t),
                   ("現況 log（worktree `w-g-9-68-cc-handoff-f0515c`·名長 26）", cur_t)):
        ln = _wd4_detail_line(t)
        core = ln.lstrip().replace("| ", "", 1).lstrip() if ln else ""
        obs[tag] = core[:18]
        P(f"     {tag}")
        P(f"       殘存起頭 18 字 ＝ {core[:18]!r}")
    P(f"     ⇒ **起頭{'相同' if len(set(obs.values())) == 1 else '不同'}**"
      "（`n\\Desktop\\land-` vs `top\\land-readjus`：切點差 **6** 字 ＝ 二 worktree 名長之差 `26−20`）")
    P("")

    P("  ── (b) **合成**：同一 traceback 只換 worktree 名，套同一 `[-300:]` " + "─" * 28)
    P("     🔒 **須用<u>真實長度</u>之尾段**——首版之合成模板尾段過短（`File \"` 距末端 < 300）")
    P("       ⇒ `[-300:]` 未切到路徑、二者皆保留 `File \"`、得出「起點相同」之**假結論**。")
    P("       **已就地更正**：尾段改用**實資料之逐字訊息**（自現況 log 取），使距末端 > 300。")
    _tail = (cur_t.split("\n")[[i for i, x in enumerate(cur_t.split("\n"))
                                if x.startswith("RuntimeError: 街廓 R2")][0]]
             if any(x.startswith("RuntimeError: 街廓 R2") for x in cur_t.split("\n"))
             else "RuntimeError: x")
    TPL = ('  File "C:\\Users\\admin\\Desktop\\land-readjustment-trial\\.claude\\worktrees\\'
           '{wt}\\verify\\stepg_pipeline.py", line 995, in run_step_g\n'
           '    raise RuntimeError(f"街廓 {{blk_label}} 抵費地計算失敗：{{_eOff}}")\n'
           + _tail + "\n")
    P(f"       （尾段長度 ＝ {len(_tail)} 字·取自現況 log 之 `RuntimeError:` 行）")
    P(f"  {'worktree 名':<30}{'名長':>5}{'該行殘存起頭 18 字':>26}{'含 File \"?':>12}{'R2 改變?':>10}")
    P("-" * WID)
    heads = {}
    for wt in ("frosty-agnesi-fa87af", "w-g-9-68-cc-handoff-f0515c"):
        s = TPL.format(wt=wt)[-300:]
        line = next((x for x in s.split("\n") if NEEDLE in x), "")
        heads[wt] = line[:18]
        P(f"  {wt:<30}{len(wt):>5}{line[:18]!r:>26}"
          f"{str('File \"' in line):>12}{str(wr._r2(line) != line):>10}")
    P("-" * WID)
    same = len(set(heads.values())) == 1
    P(f"  ⇒ **被切斷之起點{'相同' if same else '不同'}** ⇒ "
      f"{'🔴 合成未複現' if same else '✅ 二側之殘存字串不同組 ⇒ 該紅⛔ 不可重現、⛔ 不可比對'}")
    P("")

    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C】B 組自檢之**雙向判別力**（⛔ 只呼叫 `render_list`·⛔ 不寫任何名單檔）")
    P("=" * WID)
    P("  🔒 受測者 ＝ `wv_reconcile.render_list` → `assert_list_integrity`（生成路徑）")
    P("")
    # (1) 會紅：以**現有凍存名單之來源 log** 餵入
    red_ok, red_msg = False, ""
    try:
        _items = [(nm, [wr.normalize(x) for x in det]) for nm, det in wr.parse_log(src_t)]
        wr.render_list(_items, "verify/out/WG928_runall.log", "81e6e909…", _src_text=src_t)
        red_msg = "🔴 **未 raise** ⇒ 該自檢不會咬"
    except RuntimeError as e:
        red_ok, red_msg = True, str(e)
    P(f"  ── (1) **會紅**：餵入現有凍存名單之來源 log（`WG928_runall.log`）")
    P(f"     {'✅' if red_ok else '🔴'} {'raise' if red_ok else '未 raise'}")
    for _seg in [red_msg[i:i + 100] for i in range(0, min(len(red_msg), 700), 100)]:
        P("       │ " + _seg)
    P("")
    # (2) 會綠：未截斷之合成 traceback
    CLEAN = (
        "### [3/3] W-V headless 對拍（verify/run_verification.py）\n"
        "  🔴 FAIL  合成名目\n"
        "        [合成] compute 失敗：x\n"
        '        File "C:\\Users\\u\\repo\\verify\\stepg_pipeline.py", line 995, in run_step_g\n'
        "    raise RuntimeError(\"x\")\n"
        "RuntimeError: x\n"
        "============================================================\n")
    grn_ok, grn_msg = False, ""
    try:
        _ci = [(nm, [wr.normalize(x) for x in det]) for nm, det in wr.parse_log(CLEAN)]
        _out = wr.render_list(_ci, "（合成）", "n/a", _src_text=CLEAN)
        grn_ok, grn_msg = True, f"通過（產出 {len(_out.splitlines())} 行·⛔ 未寫檔）"
    except RuntimeError as e:
        grn_msg = "🔴 誤咬：" + str(e)[:150]
    P("  ── (2) **會綠**：未截斷之合成 traceback（`File \"…\"` 完整於同一行）")
    P(f"     {'✅' if grn_ok else '🔴'} {grn_msg}")
    P(f"     🔒 合成之明細行數 ＝ {sum(len(d) for _n, d in wr.parse_log(CLEAN))}"
      f"／其中含 `File \"` 者 ＝ "
      f"{sum(1 for _n, d in wr.parse_log(CLEAN) for x in d if 'File \"' in x)}")
    P("")

    P("=" * WID)
    P("【B】逐項判")
    P("=" * WID)
    fr, sr, cr_ = rows[0], rows[1], rows[2]
    def _prev_has_token(t):
        lines = t.split("\n")
        for i, x in enumerate(lines):
            if NEEDLE in x and "凍存:" not in x and "現況:" not in x and i and \
                    "[W-D.4] compute 失敗" in lines[i - 1]:
                return 'File "' in lines[i - 1]
        return None

    items = [
        ("A-1 該行匹配數", "R1／R2 於 `W-D.4` 明細之該行改變 0 次（三源皆然）",
         all(len(wr._FILE_TOKEN.findall(v)) == 0 and wr._r1(v) == v and wr._r2(v) == v
             for v in hits.values()) and len(hits) == 3),
        ("A-2 機制", "該明細行之前一行**不含** `File \"` ⇒ **截斷**、⛔ 非折行",
         all(_prev_has_token(t) is False for t in (frozen_t, src_t, cur_t))),
        ("A-3 不可比對(實資料)", "二 worktree 之殘存起頭不同（切點差 ＝ 名長差 6）",
         len(set(obs.values())) == 2),
        ("A-3 不可比對(合成)", "同一切片、只換名 ⇒ 起點不同", not same),
        ("A-1 分母", f"**明細內** token：凍存 {fr[3]}／來源 log {sr[3]}／現況 log {cr_[3]}"
                     "（⇒ `render_list` **未遺失任何 token**）", fr[3] == sr[3]),
        ("C 判別力(會紅)", "餵現有來源 log ⇒ `assert_list_integrity` raise", red_ok),
        ("C 判別力(會綠)", "餵未截斷之合成 ⇒ 通過", grn_ok),
    ]
    for k, t, ok in items:
        P(f"  {k:<18}{'✅' if ok else '🔴'}　{t}")
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
    _log = os.path.join(OUTDIR, f"probe_WG971_wrap_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
