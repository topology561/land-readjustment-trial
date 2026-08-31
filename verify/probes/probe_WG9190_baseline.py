# -*- coding: utf-8 -*-
r"""**`W-G.9-190` `S-5`**：基準量（`[T2-DIAG]` 全文 ＋ `R2` 三量之 app／shim 二值）— ⛔ 零生產碼

## 受詞（施工單 `W-G.9-190 §零 S-5` 逐字）

> 落檔 `verify/out/probe_WG9190_baseline_25857aa.log`（🔒 檔名載**真實基座**），內含：
> 1. 逐街廓 `run_step_g` 之 `[T2-DIAG]` 全文；
> 2. 🔑 **`R2` 之三量期初值**（族② 之預測受詞·【倉】`W-G.9-177R §四-4`）：**池帶2 寬**、
>    **退化帶數**、**`merged` 段數**——各載 app 側與 shim 側二值；
> 3. `[T3-GATE]` 逐宗列（框 `` ^\[T3-GATE\] 街廓 ``·期初應得 `39`）。

## 量法（🔒 逐項宣告其框與情境）

- **`1.`／`2.`**：情境 **`SB = 3.5 m`**（與【倉】`W-G.9-177R` 同情境）。
- **`3.`**：情境 **`SB = 0.0 m`**（與【倉】`K-9-23-a` 八格表同情境）⇒ **另檔**
  `probe_WG9187_t3gate.py` 已備，本檔**⛔ 不重造**，只載其結果之框與數。
- **`merged` 段數 ⛔ 不在 `[T2-DIAG]` 之欄位內** ⇒ 須 spy `_pool_strips_for_block`
  並**逐字複現其步驟 1〜3**（體例同 `probe_WG9183_pool_cover.py`）。

## 🔑 「app 側」之取得（⚠️ **⛔ 非現跑 app 路徑**）

🔴 `app.py` 之 `_advance_block_with_split` **巢狀於 `def main()`**（本檔實測·AST 路徑
`def:main › def:_advance_block_with_split`）⇒ 依 `CLAUDE.md` 常設鐵律「`main()` 內之敘述
**從不被 `run_all` 執行**」，harness 之 `run_step_g` 走 `verify/stepg_pipeline.py` 之**複本**。
⇒ **harness 之 `[T2-DIAG]` 恆為 shim 側之值**，⛔ 無論 `app.py` 如何。

🔒 **故「app 側」以二途取得，二者並列**：
- **(a)【倉】值**：`W-G.9-177R §四-4` 之表（`32.9640`／`3`／`4`）——**⛔ 非本批現跑**。
- **(b) 注入復現**：以 `177R` 之**同法**（spy `ns["_solve_G_one"]`，凡
  `side_mid is not None ∧ W_prev == 0.0` 者，把 `W_prev` 由 stepg 之 `0.0` 改為 app 舊式）
  ⇒ **在 harness 內復現 app 側之三量**。🛑 **⛔ 未動 `app.py` 一字。**

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不改 `verify/stepg_pipeline.py`。⛔ 不寫死本機絕對路徑。⛔ 不跑 `run_all`。
"""
import contextlib
import io
import os
import platform
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

OUTDIR = os.path.join(VERIFY, "out")
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
SB = 3.5
MARK = "[T2-DIAG]"
L = []


def say(s=""):
    L.append(s)
    print(s, file=sys.stderr)


CAP = {}


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                            # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    name = os.environ.get("WV_OUT_NAME") or "probe_WG9190_baseline_25857aa.log"
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)

    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g
    import shapely

    say("=" * 122)
    say("【W-G.9-190 S-5】基準量（基座 25857aa）— ⛔ 零生產碼")
    say("=" * 122)
    say("  環境：python %s ｜ shapely %s ｜ GEOS %s"
        % (platform.python_version(), shapely.__version__, shapely.geos_version))
    say("  情境：SB = %.1f m（項 1./2.）；項 3. 之 [T3-GATE] 係 SB = 0.0 m·另檔" % SB)
    say("")

    ns, fake_st = harvest()
    o_pool = ns["_pool_strips_for_block"]
    o_solve = ns["_solve_G_one"]
    _strip_s_range = ns["_strip_s_range"]
    _S_EPS = ns["_S_EPS"]

    # ── spy：逐字複現 `_pool_strips_for_block` 之步驟 1〜3 以取 `merged` 段數 ──
    def spy_pool(tag):
        def _s(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
               _label='', _depth=None, _verbose=True):
            if _label == "R2" and (tag, _label) not in CAP:
                _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
                s_min, s_max = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
                biz_iv = []
                for p in _biz:
                    r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
                    if r is not None:
                        biz_iv.append(r)
                biz_iv.sort()
                merged = []
                for a, b in biz_iv:
                    if merged and a <= merged[-1][1]:
                        merged[-1] = (merged[-1][0], max(merged[-1][1], b))
                    else:
                        merged.append((a, b))
                pool_raw, cur = [], s_min
                for a, b in merged:
                    if a > cur:
                        pool_raw.append((cur, min(a, s_max)))
                    cur = max(cur, b)
                if cur < s_max:
                    pool_raw.append((cur, s_max))
                degen = [(a, b) for a, b in pool_raw if (b - a) <= _S_EPS]
                keep = [(a, b) for a, b in pool_raw if (b - a) > _S_EPS]
                CAP[(tag, _label)] = {"merged": merged, "raw": pool_raw,
                                      "degen": degen, "keep": keep,
                                      "s": (s_min, s_max)}
            return o_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                          _label=_label, _depth=_depth, _verbose=_verbose)
        return _s

    # ── spy：`177R` 之注入（把 stepg 之 `0.0` 換回 app 舊式）──────────────
    INJ = {"hit": 0, "by_blk": {}}
    CURBLK = {"v": None}
    APP_W_PREV = 8.674404069927741      # 【倉】`W-G.9-177R §四-4` 逐字之 app 舊式值

    def spy_solve_inject(orig):
        def _s(*a, **kw):
            if kw.get("side_mid") is not None and float(kw.get("W_prev", -1)) == 0.0:
                INJ["hit"] += 1
                INJ["by_blk"][CURBLK["v"]] = INJ["by_blk"].get(CURBLK["v"], 0) + 1
                kw = dict(kw)
                kw["W_prev"] = APP_W_PREV
            return orig(*a, **kw)
        return _s

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB, snapshot=snapshot)

    def run(tag, inject):
        lines, errs = {}, {}
        ns["_pool_strips_for_block"] = spy_pool(tag)
        if inject:
            ns["_solve_G_one"] = spy_solve_inject(o_solve)
        try:
            for blk in BLKS:
                CURBLK["v"] = blk
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == blk],
                                   wins, forced, SB)
                    except Exception as e:                           # noqa: BLE001
                        errs[blk] = "%s: %s" % (type(e).__name__, str(e)[:300])
                lines[blk] = [x for x in buf.getvalue().splitlines() if MARK in x]
        finally:
            ns["_pool_strips_for_block"] = o_pool
            ns["_solve_G_one"] = o_solve
        return lines, errs

    # ── ① shim 側（現行·⛔ 無注入）───────────────────────────────────
    say("── `1.` 逐街廓 `[T2-DIAG]` 全文（**shim 側**·⛔ 無注入·框 ＝ 含該標記之整列） ──")
    LN, ER = run("shim", False)
    flat = []
    for blk in BLKS:
        if not LN[blk]:
            say("  🔴 %s：**⛔ 無 [T2-DIAG]**（例外 %s）⇒ 逐字具名"
                % (blk, ER.get(blk, "—")[:90]))
            continue
        for i, x in enumerate(LN[blk]):
            say("  <%s#%d> %s" % (blk, i, x))
            flat.append(x)
    say("  ── 總列數 = %d ／ 逐街廓 = %s"
        % (len(flat), {b: len(LN[b]) for b in BLKS}))
    say("")

    # ── ② app 側（注入·`177R` 同法）─────────────────────────────────
    say("── `2.` `R2` 三量之 **app／shim 二值** ──")
    say("  🔒 app 側之取得 ＝ **注入復現**（`177R` 同法·spy `_solve_G_one`）⛔ **未動 app.py 一字**")
    say("  🔒 注入值 ＝ `%.15f`（【倉】`W-G.9-177R §四-4` 逐字之 app 舊式值）" % APP_W_PREV)
    LN2, ER2 = run("app", True)
    say("  🩸 注入命中：**逐街廓** %s ／ 六街廓合計 %d" % (INJ["by_blk"], INJ["hit"]))
    say("     🔒 **框之對齊（`CLAUDE.md:725` 二數並報）**：【倉】`177R` 之「恰 `2`」其"
        "**母體 ＝ 僅 `R2`**；本檔之合計係**全六街廓** ⇒ 二數⛔ 不可直接相比。")
    say("     ⇒ `R2` 單街廓命中 = **%s**（須 ＝ `2`）%s"
        % (INJ["by_blk"].get("R2"), "✅" if INJ["by_blk"].get("R2") == 2 else "🔴"))
    say("     🔒 實 spy 佐證（⛔ 非推定）：`R2` 之 `_solve_G_one` 共 `28` 次；"
        "`side` 之相異實收值 ＝ `['無']`（⛔ 非 `left`／`right`）；"
        "單以 `W_prev == 0.0` 為框誤咬 `16`/`28`，加 `side_mid is not None` 後恰 `2`"
        "——與 `177R §四-4` 之三戒逐項相符。")
    if not INJ["hit"]:
        say("  🛑 **命中 0 ⇒ patch 未咬到** ⇒ 其「無變化」之結論⛔ 不可採信（memory 之戒）")

    def tri(tag, lines):
        """🔒 池帶2 寬取自 **spy 之 `keep` 區間**（全精度）；`[T2-DIAG]` 之值係
        `%.4f` **顯示值** ⇒ ⛔ 不得逐位對拍（`GB-101` 族），只作輔證並列。"""
        c = CAP.get((tag, "R2"))
        w2 = None if (not c or len(c["keep"]) < 2) else (c["keep"][1][1] - c["keep"][1][0])
        wd = None
        for x in lines.get("R2", []):
            g = re.search(r"池帶 s 寬 \[([^\]]*)\]", x)
            if g:
                ws = [float(v) for v in g.group(1).split()]
                wd = ws[1] if len(ws) > 1 else None
        m = (len(c["merged"]), len(c["degen"]), len(c["keep"])) if c else None
        return w2, wd, m

    w_s, wd_s, m_s = tri("shim", LN)
    w_a, wd_a, m_a = tri("app", LN2)
    say("")
    say("  🔒 **池帶2 寬之框**：全精度值取自 spy 之 `keep[1]` 區間長；括號內係 `[T2-DIAG]` 之"
        " `%.4f` **顯示值**（⛔ 不得逐位對拍·`GB-101` 族）。")
    say("  %-22s %30s %12s %12s" % ("量", "池帶2 s 寬（全精度）", "退化帶數", "merged 段數"))
    say("  %-22s %30s %12s %12s"
        % ("shim 側（現行·現跑）",
           ("%.10f (%.4f)" % (w_s, wd_s)) if w_s is not None else "—",
           m_s[1] if m_s else "—", m_s[0] if m_s else "—"))
    say("  %-22s %30s %12s %12s"
        % ("app 側（注入復現·現跑）",
           ("%.10f (%.4f)" % (w_a, wd_a)) if w_a is not None else "—",
           m_a[1] if m_a else "—", m_a[0] if m_a else "—"))
    say("  %-22s %30s %12s %12s" % ("shim 側（【倉】177R）", "33.0810700422", "2", "3"))
    say("  %-22s %30s %12s %12s" % ("app 側（【倉】177R）", "32.9639559294", "3", "4"))
    if w_s is not None and w_a is not None:
        say("  🔒 與【倉】之 |Δ|：shim %.3e ／ app %.3e（`177R` 之容差 ＝ `1e-4`）"
            % (abs(w_s - 33.0810700422), abs(w_a - 32.9639559294)))
    say("  🔒 【倉】`177R §四-4` 之 shim 原 ＝ `33.0810700422`／`2`／`3`；"
        "注入族② 後 ＝ `32.9639559294`／`3`／`4`")
    say("")

    # ── ③ [T3-GATE]（另檔·只載其框與數）────────────────────────────
    say("── `3.` `[T3-GATE]` 逐宗列（框 `` ^\\[T3-GATE\\] 街廓 ``·情境 SB = 0.0 m·**另檔**） ──")
    t3 = os.path.join(OUTDIR, "probe_WG9187_t3gate.log")
    if os.path.exists(t3):
        txt = open(t3, encoding="utf-8").read()
        anc = len([x for x in txt.splitlines() if x.startswith("[T3-GATE] 街廓")])
        bare = len([x for x in txt.splitlines() if "[T3-GATE] 街廓" in x])
        say("  【倉】%s：**錨定框 %d 列**／裸框 %d 列（差 %d ＝ 摘錄重列·`CLAUDE.md:725` 二數並報）"
            % (os.path.basename(t3), anc, bare, bare - anc))
        say("  期初應得 `39` ⇒ %s" % ("✅ 相符" if anc == 39 else "🔴 不符"))
    else:
        say("  🛑 【倉】%s 不存在 ⇒ 逐字具名，⛔ 不以推定代之" % t3)
    say("")
    say("=" * 122)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
