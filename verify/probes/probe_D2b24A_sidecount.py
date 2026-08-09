r"""**D-2b-24 commit A**：逐側宗數實測（類 C 分類用）—— ⛔ **零生產碼變更**

## 為何存在

`D-2b-23C` §三-3 之類 C（`3.5m R1` 左側殘 `5.3881`）當時**推論**「該側只有 1 宗」，
CC 已明標**未證**。KL 裁 2026-08-09：**先實測逐側宗數再分類，⛔ 不得先歸入類 B。**

## 量法（⛔ 每個選擇皆寫明）

`run_step_g` 之 `g_rows` 帶 `推進側別` 欄，**惟失敗之街廓不產 rows** ⇒ 不可用。
⇒ 改於 `_solve_G_one` 掛 spy，逐次記 `(街廓, 推進向, baseline_pt)`。

🔴 **⛔ 不得以 `_solve_G_one` 之 `side` 實參當推進側**（CC 首版之錯·已修）：
現查 `grep -n "side = entry.get('side'" verify/stepg_pipeline.py app.py` ⇒
`side` ＝ **該宗自身之街角側屬性**（`'無'`／`'左側'`／`'右側'`），多數宗為 `'無'`
⇒ 以其為鍵，248 次呼叫只有約 22 次落在 `左側`／`右側`，其餘**靜默漏失**。
✅ **真判別 ＝ `d_hat`**：左迴圈傳 `d_hat`、右迴圈傳 `d_hat_rev`（`= −d̂`）
⇒ 依 `d_hat` 與該街廓 FRONT `p1→p2` 之**內積正負**分左右（正＝左、負＝右）。

**⚠️ 一個街廓會跑<u>多趟</u>推進**（`_advance_block_with_split` 之基準趟 `k_naive`
＋正式趟 `k*`；退化時單趟）⇒ 直接數呼叫次數**會多算**。
**切出最後一趟之判準**：同一 (街廓, side) 內，`t = baseline_pt · d̂`（投影純量）
於**同一趟內單調遞增**（推進即累加 `cum_S`），趟與趟之交界處 `t` **回落**
⇒ **最後一趟 ＝ 由尾端往前之極大遞增後綴**。
🔒 左右兩側皆成立：右側傳入之 `d_hat` 已為 `d_hat_rev`，其 `baseline_pt` 沿之遞增。

⛔ **不以「應該是 N 宗」推定**；⛔ 不以 `is_corner` 次數反推（其為 2 趟 × 側數）。

## 涵蓋（KL §4「逐側」）

**正面列舉全部 (情境, 街廓, 側)**——6 街廓 × 2 側 × 2 情境 ＝ **24** 列，
⛔ 非只列有 `SIDE_LINE` 者、⛔ 非只列有街角者。同時標注該側有無 `SIDE_LINE`。
"""
import contextlib
import io
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                       # noqa: E402
import run_verification as rv                                         # noqa: E402
from selection_pipeline import run_corner_pk                          # noqa: E402
from stepg_pipeline import run_step_g                                 # noqa: E402
from probe_D2b17_dual import replicate_pieces                         # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 200


def _resolve_out(default_name):
    """⛔ 禁覆寫已入庫 log（同 `probe_D2b22_attrib` 之守衛·fail-fast）。"""
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError(f"🔴 拒絕覆寫既有 log：{path}　⇒ 請設 WV_OUT_NAME=<新檔名>")
    return path


def last_pass(seq):
    """由尾端往前之**極大遞增後綴** ＝ 最後一趟（seq ＝ 依呼叫序之 t 值）。"""
    if not seq:
        return []
    i = len(seq) - 1
    while i > 0 and seq[i - 1] < seq[i]:
        i -= 1
    return seq[i:]


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                             # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    out = _resolve_out("probe_D2b24A_sidecount.log")
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-24 commit A】逐側宗數實測（類 C 分類）— ⛔ 零生產碼變更")
    P("=" * W)
    P("  量法：spy `_solve_G_one` 記 (街廓, side, t=baseline_pt·d̂)；")
    P("        最後一趟 ＝ 由尾端往前之極大遞增後綴（⛔ 非呼叫次數÷趟數之推定）")

    ns, fake_st = harvest()
    SEQ = {}                       # (情境, 街廓, side) -> [t, …] 依呼叫序
    BIZ = {}                       # (情境, 街廓) -> [(s_lo, s_hi), …] 依**生產順序**
    _orig = ns["_solve_G_one"]
    _orig_pool = ns["_pool_strips_for_block"]

    def _spy_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                  _label='', _depth=None, _verbose=True):
        # 🔑 **第二量測器（獨立於 t-啟發式）**：`biz_polys` 之順序即生產順序
        #    `stepg:915` 逐字 `for _entry, _res in (left_results + right_results)`
        #    ⇒ **左組（s 遞增）在前、右組（s 遞減）在後** ⇒ 分界 ＝ s 停止遞增之處。
        key = (_spy_pool.tag, _label)
        if key not in BIZ:
            try:
                iv = []
                for g in (biz_polys or []):
                    r = ns["_strip_s_range"](g, d_hat, corner_pt, allocation_dir)
                    iv.append((float(r[0]), float(r[1])) if r else None)
                BIZ[key] = iv
            except Exception as e:                                    # noqa: BLE001
                BIZ[key] = [("err", str(e))]
        return _orig_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                          _label=_label, _depth=_depth, _verbose=_verbose)
    _spy_pool.tag = ""

    def _spy(**kw):
        bp, dh = kw.get("baseline_pt"), kw.get("d_hat")
        if bp is not None and dh is not None:
            dh = np.asarray(dh, float)[:2]
            t = float(np.dot(np.asarray(bp, float)[:2], dh))
            ref = _spy.ref.get(_spy.blk)
            if ref is None:
                sd = "（無 FRONT）"
            else:
                sd = "左側" if float(np.dot(dh, ref)) >= 0 else "右側"
            SEQ.setdefault((_spy.tag, _spy.blk, sd), []).append(t)
        return _orig(**kw)
    _spy.ref = {}
    _spy.tag = _spy.blk = ""

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

    # 各街廓之正典推進向 d̂ ＝ FRONT p1→p2（`p1` 為左·CLAUDE.md CAD 圖層規範）
    _fls = (fake_st.session_state.get('f3_cad_front_lines', {}) or {})
    for _b in blks:
        _fl = _fls.get(_b) or {}
        if _fl.get("p1") is not None and _fl.get("p2") is not None:
            _v = np.asarray(_fl["p2"], float)[:2] - np.asarray(_fl["p1"], float)[:2]
            _n = float(np.linalg.norm(_v))
            if _n > 1e-9:
                _spy.ref[_b] = _v / _n
    if not _spy.ref:
        raise RuntimeError("🔴 FRONT 參考向量母體為空 ⇒ ⛔ 不得據此下結論")

    # 🔒 **效度檢查之獨立真相源**：該街廓之宗數（自 `build_parcels` 現數·⛔ 與本探針之啟發式無關）
    LOTS = {}
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l:
            LOTS[_l] = LOTS.get(_l, 0) + 1

    _slbs = (fake_st.session_state.get('f3_cad_side_lines_by_side', {}) or {})
    has_side = {(b, w): bool((_slbs.get(b) or {}).get(w))
                for b in blks for w in ("left", "right")}

    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in blks:
            _spy.tag, _spy.blk = sb, lbl
            _spy_pool.tag = sb
            ns["_solve_G_one"] = _spy
            ns["_pool_strips_for_block"] = _spy_pool
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                                 # noqa: BLE001
                        pass
            finally:
                ns["_solve_G_one"] = _orig
                ns["_pool_strips_for_block"] = _orig_pool
            print(f"    [{sb}] {lbl} 擷取完畢", file=sys.stderr)

    if not SEQ:
        raise RuntimeError("🔴 母體為空 ⇒ ⛔ 不得據此下任何結論")

    P("")
    P(f"  母體 ＝ {len(SEQ)} 個 (情境,街廓,側) 有呼叫紀錄"
      f"／`_solve_G_one` 總呼叫 {sum(len(v) for v in SEQ.values())} 次（⛔ 非空）")
    P("")
    _covered = set()
    P(f"  {'情境':<6}{'街廓':<5}{'側':<8}{'有SIDE':<8}{'總呼叫':>7}{'最後一趟宗數':>13}"
      f"{'趟數(推得)':>12}   最後一趟之 t 序列（前 4）")
    P("-" * W)
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            for side, key in (("左側", "left"), ("右側", "right")):
                seq = SEQ.get((sb, lbl, side), [])
                _covered.add((sb, lbl, side))
                lp = last_pass(seq)
                npass = (f"{len(seq)/len(lp):.2g}" if lp else "—")
                pv = "  ".join(f"{x:.3f}" for x in lp[:4]) if lp else "（該側無宗）"
                P(f"  {sb:<6}{lbl:<5}{side:<8}"
                  f"{('✅' if has_side.get((lbl, key)) else '—'):<8}"
                  f"{len(seq):>7}{len(lp):>13}{npass:>12}   {pv}")
    P("")
    P("  🔑 **第二量測器：依 `biz_polys` 之生產順序切左右**（⛔ 與 t-啟發式獨立）")
    P(f"     {'情境':<6}{'街廓':<5}{'biz 數':>7}{'左組':>6}{'右組':>6}   s_lo 序列（生產序）")
    P("     " + "-" * 120)
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            iv = BIZ.get((sb, lbl))
            if not iv:
                P(f"     {sb:<6}{lbl:<5}{'（未擷取）':>7}")
                continue
            los = [x[0] for x in iv if isinstance(x, tuple) and not isinstance(x[0], str)]
            # 🔴 **off-by-one 修正（CC 首版之錯）**：右組之**首宗即全域最大 s**
            #    ⇒ 「停止遞增之處」`k` 已把右組首宗算進左組 ⇒ **左組 = k − 1**。
            #    ⚠️ **不可判之情形**：全序列無嚴格下降（左組末宗 s < 右組首宗 s 且右組僅 1 宗）
            #    ⇒ 標 `不可判`，⛔ 不得猜。
            k = 1
            while k < len(los) and los[k] > los[k - 1]:
                k += 1
            if k >= len(los):
                lft, rgt, note = "不可判", "不可判", "🔴 無嚴格下降 ⇒ 左右分界不可判"
            else:
                lft, rgt, note = k - 1, len(los) - (k - 1), ""
            P(f"     {sb:<6}{lbl:<5}{len(los):>7}{str(lft):>6}{str(rgt):>6}   "
              + "  ".join(f"{x:.2f}" for x in los) + ("   " + note if note else ""))
    P("")
    _miss = {k: len(v) for k, v in SEQ.items() if k not in _covered}
    _tot_shown = sum(len(SEQ.get(k, [])) for k in _covered)
    P("")
    P(f"  🔒 **母體守恆自證**（⛔ 防「只印子集當母體」·CC 首版即栽於此）：")
    P(f"     已印出之呼叫 ＝ {_tot_shown}／總呼叫 {sum(len(v) for v in SEQ.values())}"
      f"　未印出之鍵 ＝ {_miss if _miss else '（無·✅ 全數涵蓋）'}")
    if _miss:
        raise RuntimeError(f"🔴 有呼叫未被表涵蓋：{_miss} ⇒ ⛔ 本表不得採信")
    P("")
    P("  🔑 判讀：『最後一趟宗數』＝ 該 (情境,街廓,側) 於**正式趟**實配之宗數。")
    P("     ⛔ 『總呼叫』含基準趟與（右側之）數值微修後援，**不得**直接當宗數。")
    P("")
    P("  🔒 **效度檢查（可失敗·⛔ 非眼力核對）**：`左+右` 是否 == 該街廓宗數")
    P("     （宗數之真相源 ＝ `build_parcels` 現數，⛔ 與本探針之遞增後綴啟發式無關）")
    P(f"     {'情境':<6}{'街廓':<5}{'左':>5}{'右':>5}{'左+右':>7}{'宗數':>7}   判")
    P("     " + "-" * 60)
    _bad = []
    for sb in ("0m", "3.5m"):
        for lbl in blks:
            l = len(last_pass(SEQ.get((sb, lbl, "左側"), [])))
            r = len(last_pass(SEQ.get((sb, lbl, "右側"), [])))
            n = LOTS.get(lbl, -1)
            ok = (l + r == n)
            if not ok:
                _bad.append((sb, lbl, l, r, n))
            P(f"     {sb:<6}{lbl:<5}{l:>5}{r:>5}{l + r:>7}{n:>7}   "
              f"{'✅' if ok else '🔴 **不符 ⇒ 該格之逐側數不可採信**'}")
    P("")
    if _bad:
        P(f"  🔴 **效度檢查未全過**：{len(_bad)} 格不符 ⇒ ⛔ **該等格之『最後一趟宗數』不得引用**")
        P("     成因（推定·未證）：該塊之最後一趟內 `t` 非單調（右側微修後援／階段2 落位）")
        P("     ⇒ 遞增後綴之切法於該塊失效。⛔ 其餘通過之格不受影響（各自獨立驗過）。")
        for sb, lbl, l, r, n in _bad:
            P(f"       · [{sb}] {lbl}：左 {l} ＋ 右 {r} ＝ {l + r} ≠ 宗數 {n}")
    else:
        P("  ✅ **效度檢查全過** ⇒ 逐側數可採信")

    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"\n📄 {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
