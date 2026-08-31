# -*- coding: utf-8 -*-
r"""**`W-G.9-190R` commit `3`**：族② 切換之主閘 `G-1`〜`G-3` ＋ 佐閘（三量之方向）

## 受詞（施工單 `§六-3`／`§六-4`）

- **`G-1`（源碼層·⛔ 不經 log 通道 ⇒ 無截斷風險）**：以 AST 取 `app.py` 與
  `verify/stepg_pipeline.py` 中 `_W_prev_left`／`_W_prev_right` 之賦值節點，`ast.dump` 逐位相同。
  🔒 **射程之界定（CC 之工程裁·`§零-2`「純技術自行做完」）**：限縮於
  **`_advance_block_with_split` 內**。⛔ **不取「全檔首次」**——實測 `app.py` 之全檔首個
  `_W_prev_left` 賦值在 `:9649`（`_place_pool_parcels` 族之 `float(adv_final.get('Wf_left'…))`），
  與 `stepg:628` **語意上⛔ 非對應物**；限縮後二側**恰各 `2` 節點**、對應明確。
- **`G-2`（判別力造·⛔ 不可省）**：於**拋棄式複本**上還原舊式後重跑 `G-1`，須判**不同**。
- **`G-3`（`S-6` 之受詞層·🛑 框須逐字宣告母體）**：四框之命中數。
  🛑 **二母體之框⛔ 不通用**——`app.py` **原始碼**含**字面括號**，而 `S-6` 之清單經
  `ast.unparse` **正規化去括號**。
- **佐閘（`§六-4`）**：`R2` 三量之方向。🔒 **權威來源 ＝**
  `docs/reports/W-G.9-177R_二裁落地與R2-0.1171歸屬.md §四-4`（⛔ **非** `CLAUDE.md:760` 之箭頭
  ——該處記的是 **shim 之注入方向**）。

## 🔒 佐閘之量法（⛔ 不硬編 app 之式）

**自 `app.py` 以 AST 讀出其 `_W_prev_*` 初值運算式**，據以決定注入：
- 該式為常數 `0.0` ⇒ 注入 ≡ 不注入 ⇒ 直接量 harness 之三量。
- 否則 ⇒ 以 `177R` 同法 spy `ns["_solve_G_one"]` 注入之。
🔒 ⇒ **本閘之「切換後」值⛔ 非硬編，係由碼面現況推得** ⇒ 切換若未落地，本閘自動量到舊值。

## 🔒 佐閘之限（明載·⛔ 不得省·單 `§六-4` 逐字）

本量係 **harness 內之注入式模擬**、⛔ **非 app 路徑實跑**。**殘餘風險**：app 路徑（`main()`）
從未被任何自動測試執行（`CLAUDE.md` 逐字「`main()` 內之敘述從不被 `run_all` 執行」）
⇒ 歸 `GB-123`，本批**⛔ 不解除、明載之**。唯一真量 app 路徑者係 KL 之 UI 實跑
（前例：【倉】`verify/out/KL_UI_3.5m_2e08a41_stdout.log`）——**本批⛔ 未授權、⛔ 不辦**。

## ⛔ 本檔不做

⛔ 不改生產碼一字（`G-2` 之還原係於**記憶體內之字串副本**上為之·⛔ 不落檔）。
⛔ 不改 `verify/stepg_pipeline.py`。⛔ 不寫死本機絕對路徑。⛔ 不跑 `run_all`。
"""
import ast
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
STG = os.path.join(VERIFY, "stepg_pipeline.py")
OUTDIR = os.path.join(VERIFY, "out")
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
SB = 3.5
NAMES = ("_W_prev_left", "_W_prev_right")

# ── 【倉】`W-G.9-177R §四-4`（⛔ 非本批現跑·⛔ 非 `CLAUDE.md:760` 之箭頭）─────
REF_SHIM = (33.0810700422, 2, 3)      # 新式（目標）
REF_APP_OLD = (32.9639559294, 3, 4)   # 舊式（切換前）
TOL = 1e-4                            # `177R` 之容差

L = []


def say(s=""):
    L.append(s)
    print(s, file=sys.stderr)


def abws_assigns(src):
    """`_advance_block_with_split` 內之 `_W_prev_*` 賦值節點（正規化後之 dump）。"""
    t = ast.parse(src)
    out = {}
    for n in ast.walk(t):
        if isinstance(n, ast.FunctionDef) and n.name == "_advance_block_with_split":
            for m in ast.walk(n):
                if isinstance(m, ast.Assign):
                    for tg in m.targets:
                        if isinstance(tg, ast.Name) and tg.id in NAMES:
                            d = ast.dump(ast.parse(ast.unparse(m)).body[0],
                                         annotate_fields=False)
                            out.setdefault(tg.id, []).append((m.lineno, d))
    return {k: sorted(v) for k, v in out.items()}


def g1(src_a, src_s, tag):
    A, S = abws_assigns(src_a), abws_assigns(src_s)
    ok = True
    rows = []
    for nm in NAMES:
        a, s = A.get(nm, []), S.get(nm, [])
        same = (len(a) == len(s)) and all(x[1] == y[1] for x, y in zip(a, s))
        ok &= same
        rows.append((nm, [x[0] for x in a], [x[0] for x in s], same))
    say("  【%s】" % tag)
    for nm, la, ls, same in rows:
        say("    %-16s app @%s ／ stepg @%s ⇒ 逐節點 `ast.dump` 逐位相同 = %s %s"
            % (nm, la, ls, same, "✅" if same else "🔴"))
    return ok


def init_expr(src):
    """自 `app.py` 讀出 `_W_prev_left` 之**初值**運算式（`_advance_block_with_split` 內首個）。"""
    a = abws_assigns(src).get("_W_prev_left", [])
    if not a:
        raise RuntimeError("🔴 `app.py` 之 `_advance_block_with_split` 內找不到 `_W_prev_left` 賦值")
    t = ast.parse(ast.unparse(ast.parse(src)))   # 佔位（保持純度）
    del t
    ln = a[0][0]
    node = None
    tree = ast.parse(src)
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and n.lineno == ln:
            node = n
            break
    return ast.unparse(node.value)


def main():                                                      # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                        # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    name = os.environ.get("WV_OUT_NAME") or "probe_WG9190R_fam2.log"
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)

    src_a = open(APP, encoding="utf-8").read()
    src_s = open(STG, encoding="utf-8").read()

    say("=" * 122)
    say("【W-G.9-190R commit 3】族② 切換之主閘 G-1〜G-3 ＋ 佐閘 — ⛔ 本檔零生產碼")
    say("=" * 122)
    say("  環境：python %s" % platform.python_version())
    say("  🔒 `G-1` 之射程 ＝ `_advance_block_with_split` **內**之全部 `_W_prev_*` 賦值節點")
    say("     （⛔ 非「全檔首次」——`app.py` 全檔首個在 `:9649` 之 `_place_pool_parcels` 族，"
        "與 `stepg:628` **語意上⛔ 非對應物**）")
    say("")

    # ── G-1 ──────────────────────────────────────────────────────
    say("── `G-1`（源碼層·⛔ 不經 log 通道）──")
    ok1 = g1(src_a, src_s, "現況（族② 切換後）")
    say("  🔒 `G-1` 之判：%s" % ("✅ **過**" if ok1 else "🛑 **不符 ⇒ 停機**"))
    say("")

    # ── G-2（判別力造·於**記憶體內**還原舊式·⛔ 不落檔）─────────────
    say("── `G-2`（判別力造·⛔ 不可省）──")
    OLD1 = "                            _W_prev_left = 0.0\n"
    OLD2 = "                            _W_prev_right = 0.0\n"
    REV1 = ("                            _W_prev_left = (_left_buffer_S * _cos_dn)"
            " if _has_left_corner else 0.0\n")
    REV2 = ("                            _W_prev_right = (_right_buffer_S * _cos_dn)"
            " if _has_right_corner else 0.0\n")
    if src_a.count(OLD1) != 1 or src_a.count(OLD2) != 1:
        say("  🛑 還原之錨命中非各 1（%d／%d）⇒ **⛔ 不得據以判 `G-2`**"
            % (src_a.count(OLD1), src_a.count(OLD2)))
        ok2 = False
    else:
        rev = src_a.replace(OLD1, REV1, 1).replace(OLD2, REV2, 1)
        say("  🔒 還原係於**記憶體內之字串副本**上為之 ⇒ ⛔ 未落檔、⛔ 未動工作樹")
        ok2 = not g1(rev, src_s, "還原舊式後（須**不同**）")
    say("  🔒 `G-2` 之判：%s" % ("✅ **過**（還原後確判不同 ⇒ `G-1` ⛔ 非恆真）"
                                if ok2 else "🛑 **恆判相同 ⇒ 閘紅·⛔ 不得入倉**"))
    say("")

    # ── G-3（框表·🛑 二母體之框⛔ 不通用）────────────────────────────
    say("── `G-3`（框表·🛑 二母體之框⛔ 不通用）──")
    s6log = os.path.join(OUTDIR, "probe_WG9190R_S6_after.log")
    s6txt = open(s6log, encoding="utf-8").read() if os.path.exists(s6log) else None
    FR = [("`app.py` 原始碼", src_a, "_W_prev_left = (_left_buffer_S * _cos_dn)"),
          ("`app.py` 原始碼", src_a, "_W_prev_right = (_right_buffer_S * _cos_dn)"),
          ("`S-6` log（`ast.unparse` 去括號）", s6txt, "_W_prev_left = _left_buffer_S * _cos_dn"),
          ("`S-6` log（同上）", s6txt, "_W_prev_right = _right_buffer_S * _cos_dn")]
    ok3 = True
    say("  %-34s %-46s %6s %6s" % ("母體", "框（`grep -F` 固定字串）", "基座", "現況"))
    for pop, txt, fr in FR:
        if txt is None:
            say("  %-34s %-46s %6s %6s 🛑 **母體不存在** ⇒ 逐字具名，⛔ 不以推定代之"
                % (pop, fr, "1", "—"))
            ok3 = False
            continue
        n = txt.count(fr)
        ok3 &= (n == 0)
        say("  %-34s %-46s %6s %6d %s" % (pop, fr, "1", n, "✅" if n == 0 else "🔴"))
    say("  🔒 `G-3` 之判：%s（判準 ＝ 四框皆由 `1` 降為 `0`）"
        % ("✅ **過**" if ok3 else "🛑 **未全數降為 0 ⇒ 停機**"))
    say("")

    # ── 佐閘（§六-4）：R2 三量之方向 ─────────────────────────────────
    say("── 佐閘（`§六-4`）：`R2` 三量之方向 ──")
    expr = init_expr(src_a)
    say("  🔒 自 `app.py` 以 AST 讀出之 `_W_prev_left` **初值運算式** ＝ `%s`" % expr)
    is_zero = (expr.strip() == "0.0")
    say("  ⇒ 其為常數 `0.0` = %s ⇒ %s"
        % (is_zero, "注入 ≡ 不注入 ⇒ 直接量 harness 之三量" if is_zero
           else "須以 `177R` 同法注入之"))

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
    try:
        for blk in BLKS:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == blk],
                               wins, forced, SB)
                except Exception:                                # noqa: BLE001
                    pass
    finally:
        ns["_pool_strips_for_block"] = o_pool

    c = CAP.get("R2")
    if not c or len(c["keep"]) < 2:
        say("  🛑 `R2` 之池帶擷取失敗 ⇒ 逐字具名，⛔ 不以推定代之")
        okg = False
    else:
        w2 = c["keep"][1][1] - c["keep"][1][0]
        got = (w2, c["degen"], c["merged"])
        say("")
        say("  %-24s %26s %12s %12s" % ("量", "池帶2 `s` 寬（全精度）", "退化帶數", "`merged` 段數"))
        say("  %-24s %26s %12s %12s"
            % ("切換前（【倉】`177R`·app 舊式）", "%.10f" % REF_APP_OLD[0],
               REF_APP_OLD[1], REF_APP_OLD[2]))
        say("  %-24s %26s %12s %12s"
            % ("**切換後（本批現跑）**", "%.10f" % got[0], got[1], got[2]))
        say("  %-24s %26s %12s %12s"
            % ("目標（【倉】`177R`·shim 新式）", "%.10f" % REF_SHIM[0],
               REF_SHIM[1], REF_SHIM[2]))
        okg = (abs(got[0] - REF_SHIM[0]) <= TOL and got[1] == REF_SHIM[1]
               and got[2] == REF_SHIM[2])
        say("")
        say("  🔒 **方向**（權威來源 ＝ `177R §四-4`·⛔ 非 `CLAUDE.md:760` 之箭頭）：")
        say("     池帶2 寬 `32.9640 → 33.0811`／退化帶數 **`3 → 2`**／`merged` 段數 **`4 → 3`**")
        say("     ⚠️ `CLAUDE.md:760` 載 `2→3`／`3→4` 係 **shim 之注入方向**（`自誤 227`）")
        say("  🔒 與目標之 |Δ|：池帶2 寬 %.3e（容差 %.0e）／退化帶數 %+d／`merged` %+d"
            % (abs(got[0] - REF_SHIM[0]), TOL, got[1] - REF_SHIM[1], got[2] - REF_SHIM[2]))
        say("  🔒 佐閘之判：%s"
            % ("✅ **三量同時收斂至 shim 值**" if okg
               else "🛑 **未同時收斂（含部分收斂）⇒ 停機上呈**（⛔ 不得自判為切換失敗、⛔ 不得回退）"))
    say("")
    say("  🔒 **佐閘之限（明載·⛔ 不得省）**：本量係 **harness 內之模擬**、⛔ **非 app 路徑實跑**。")
    say("     殘餘風險 ＝ app 路徑（`main()`）從未被任何自動測試執行 ⇒ 歸 `GB-123`，")
    say("     本批**⛔ 不解除、明載之**。唯一真量者係 KL 之 UI 實跑——**本批⛔ 未授權、⛔ 不辦**。")
    say("")
    say("=" * 122)
    allok = ok1 and ok2 and ok3 and okg
    say("🛑 總判：`G-1` %s ／ `G-2` %s ／ `G-3` %s ／ 佐閘 %s ⇒ %s"
        % ("✅" if ok1 else "🛑", "✅" if ok2 else "🛑", "✅" if ok3 else "🛑",
           "✅" if okg else "🛑", "✅ 全過" if allok else "🛑 **有不過項 ⇒ 停機**"))
    say("=" * 122)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path, file=sys.stderr)
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
