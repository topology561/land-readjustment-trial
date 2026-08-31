# -*- coding: utf-8 -*-
r"""**`W-G.9-190R` commit `4`**：族③ 切換之主閘 `G-4`／`G-5` ＋ 三量之復量

## 受詞（施工單 `§六-5`）

- **`G-4`（源碼層·🛑 直接對 `app.py` 檔案 `grep -F`·⛔ 不經 `S-6` 之 log 通道）**：
  `'b': _left_buffer_S * _cos_dn` ／ `'b': _right_buffer_S * _cos_dn` 二框須由 `1` 降為 `0`；
  且新式之錨字樣（`k956_W_from_mp` 於 `main()` 內之呼叫）命中 `≥ 1`。
- **`G-5`（判別力造·⛔ 不可省）**：於複本上還原舊式後重跑 `G-4`，二框須各得 `1`。恆得 `0` ⇒ 閘紅。
- **族③ 之預測**：`R2` 三量**⛔ 不再變動**（`CLAUDE.md:760` 載其於 `R2` 實測零後果，
  且逐字警示 ⛔ 不可外推至他街廓／他案）。

🛑 **單 `§六-5` 逐字之戒**：**⛔ 不得以 `S-6` 之清單為族③ 之閘**——族③ 之二字樣於
`S-6` 之 log 中命中**恆為 `0`**（`GB-115` 之顯示截斷所致·⛔ 非「受詞不存在」），
以其立閘者將**恆綠**。⇒ 本檔之 `G-4`／`G-5` **一律直接對 `app.py` 檔案**為之。

## ⛔ 本檔不做

⛔ 不改生產碼一字（`G-5` 之還原係於**記憶體內字串副本**上為之·⛔ 不落檔）。
⛔ 不改 `verify/stepg_pipeline.py`。⛔ 不寫死本機絕對路徑。⛔ 不跑 `run_all`。
"""
import contextlib
import io
import os
import platform
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

APP = os.path.join(REPO, "app.py")
OUTDIR = os.path.join(VERIFY, "out")
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
SB = 3.5
REF_SHIM = (33.0810700422, 2, 3)
TOL = 1e-4
L = []


def say(s=""):
    L.append(s)
    print(s, file=sys.stderr)


OLDL = "'b': _left_buffer_S * _cos_dn"
OLDR = "'b': _right_buffer_S * _cos_dn"
NEWL = "'b': _b_L0"
NEWR = "'b': _b_R0"
DELEG = "k956_W_from_mp(_bp0"


def g4(src, tag):
    a, b, c = src.count(OLDL), src.count(OLDR), src.count(DELEG)
    say("  【%s】" % tag)
    say("    %-38s 命中 %d（須 0）%s" % (OLDL, a, "✅" if a == 0 else "🔴"))
    say("    %-38s 命中 %d（須 0）%s" % (OLDR, b, "✅" if b == 0 else "🔴"))
    say("    %-38s 命中 %d（須 ≥1）%s" % ("k956_W_from_mp(...) 之委派呼叫", c,
                                        "✅" if c >= 1 else "🔴"))
    return (a == 0 and b == 0 and c >= 1), (a, b, c)


def main():                                                      # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                        # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    name = os.environ.get("WV_OUT_NAME") or "probe_WG9190R_fam3.log"
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)

    src = open(APP, encoding="utf-8").read()
    say("=" * 122)
    say("【W-G.9-190R commit 4】族③ 切換之主閘 G-4／G-5 ＋ 三量之復量 — ⛔ 本檔零生產碼")
    say("=" * 122)
    say("  環境：python %s" % platform.python_version())
    say("  🛑 `G-4`／`G-5` **一律直接對 `app.py` 檔案 `grep -F`**——單 `§六-5` 逐字：")
    say("     ⛔ 不得以 `S-6` 之清單為族③ 之閘（其於 log 命中恆 `0` 係 `GB-115` 之顯示截斷，")
    say("     ⛔ 非「受詞不存在」；以其立閘者將**恆綠**）。")
    say("")

    say("── `G-4`（源碼層）──")
    ok4, n4 = g4(src, "現況（族③ 切換後）")
    say("  🔒 `G-4` 之判：%s" % ("✅ **過**" if ok4 else "🛑 **不符 ⇒ 停機**"))
    say("")

    say("── `G-5`（判別力造·⛔ 不可省）──")
    if src.count(NEWL) != 1 or src.count(NEWR) != 1:
        say("  🛑 還原之錨命中非各 1（%d／%d）⇒ ⛔ 不得據以判 `G-5`"
            % (src.count(NEWL), src.count(NEWR)))
        ok5 = False
    else:
        rev = src.replace(NEWL, OLDL, 1).replace(NEWR, OLDR, 1)
        say("  🔒 還原係於**記憶體內之字串副本**上為之 ⇒ ⛔ 未落檔、⛔ 未動工作樹")
        _o, n5 = g4(rev, "還原舊式後（二框須各得 1）")
        ok5 = (n5[0] == 1 and n5[1] == 1)
    say("  🔒 `G-5` 之判：%s"
        % ("✅ **過**（還原後二框各得 `1` ⇒ `G-4` ⛔ 非恆綠）" if ok5
           else "🛑 **恆得 `0` ⇒ 閘紅·⛔ 不得入倉**"))
    say("")

    # ── 族③ 之預測：R2 三量⛔ 不再變動 ─────────────────────────────
    say("── 族③ 之預測（`§六-5`）：`R2` 三量**⛔ 不再變動** ──")
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    o_pool = ns["_pool_strips_for_block"]
    _sr = ns["_strip_s_range"]
    _eps = ns["_S_EPS"]
    CAP = {}

    def spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
            _label='', _depth=None, _verbose=True):
        if _label == "R2" and "R2" not in CAP:
            bz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
            s0, s1 = _sr(block_poly, d_hat, corner_pt, allocation_dir)
            iv = sorted(x for x in (_sr(p, d_hat, corner_pt, allocation_dir) for p in bz)
                        if x is not None)
            mg = []
            for a, b in iv:
                if mg and a <= mg[-1][1]:
                    mg[-1] = (mg[-1][0], max(mg[-1][1], b))
                else:
                    mg.append((a, b))
            raw, cur = [], s0
            for a, b in mg:
                if a > cur:
                    raw.append((cur, min(a, s1)))
                cur = max(cur, b)
            if cur < s1:
                raw.append((cur, s1))
            CAP["R2"] = {"merged": len(mg),
                         "degen": len([1 for a, b in raw if (b - a) <= _eps]),
                         "keep": [(a, b) for a, b in raw if (b - a) > _eps]}
        return o_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                      _label=_label, _depth=_depth, _verbose=_verbose)

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB, snapshot=snapshot)
    ns["_pool_strips_for_block"] = spy
    T2 = {}
    try:
        for blk in BLKS:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == blk],
                               wins, forced, SB)
                except Exception:                                # noqa: BLE001
                    pass
            T2[blk] = [x for x in buf.getvalue().splitlines() if "[T2-DIAG]" in x]
    finally:
        ns["_pool_strips_for_block"] = o_pool

    c = CAP.get("R2")
    if not c or len(c["keep"]) < 2:
        say("  🛑 `R2` 之池帶擷取失敗 ⇒ 逐字具名，⛔ 不以推定代之")
        okp = False
        got = None
    else:
        w2 = c["keep"][1][1] - c["keep"][1][0]
        got = (w2, c["degen"], c["merged"])
        say("  族② 後（commit 3 現跑）：%.10f ／ %d ／ %d" % REF_SHIM)
        say("  **族③ 後（本批現跑）**  ：%.10f ／ %d ／ %d" % got)
        okp = (abs(got[0] - REF_SHIM[0]) <= TOL and got[1] == REF_SHIM[1]
               and got[2] == REF_SHIM[2])
        say("  🔒 |Δ| 池帶2 寬 %.3e（容差 %.0e）／退化帶 %+d／`merged` %+d"
            % (abs(got[0] - REF_SHIM[0]), TOL, got[1] - REF_SHIM[1], got[2] - REF_SHIM[2]))
        say("  🔒 預測之判：%s"
            % ("✅ **⛔ 未再變動**（與族② 後逐項相同）" if okp
               else "🛑 **竟再變動 ⇒ 停機上呈**（同 `N-1` 之性質·係模型不完整、⛔ 非失敗）"))
    say("")
    say("  🛑 **本量之通道限（明載·⛔ 不得省）**：族③ 之受詞 `_select_pool_slot` 之 `'b'` 槽")
    say("     位於 `app.py` 之 `main()` 內，而 harness 走 `verify/stepg_pipeline.py` 之複本")
    say("     ⇒ **本量對族③ 之切換<u>結構上不敏感</u>**——其「未變動」係**必然**、")
    say("     ⛔ **非**「切換無後果」之證據。族③ 之實質證明在 `G-4`／`G-5`（源碼層）。")
    say("     🔒 殘餘風險歸 `GB-123`，本批**⛔ 不解除、明載之**。")
    say("")
    say("── 停機款 `8`：`[T2-DIAG]` 之逐街廓（本趟）──")
    for blk in BLKS:
        say("  %-3s ｜ %d 列%s" % (blk, len(T2[blk]),
                                  ("｜%s" % T2[blk][0][:110]) if T2[blk] else "｜🔴 ⛔ 無（期望事實）"))
    say("")
    say("=" * 122)
    allok = ok4 and ok5 and okp
    say("🛑 總判：`G-4` %s ／ `G-5` %s ／ 三量未變 %s ⇒ %s"
        % ("✅" if ok4 else "🛑", "✅" if ok5 else "🛑", "✅" if okp else "🛑",
           "✅ 全過" if allok else "🛑 **有不過項 ⇒ 停機**"))
    say("=" * 122)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path, file=sys.stderr)
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
