# -*- coding: utf-8 -*-
"""`W-G.9-277` `§三-1`／`§三-2`：**`W` 鏈之逐宗實參** ＋ `W_prev = 0.1775` 之受詞
   ＋ **本案之 `理論@k*` 出自哪一解算器**。

🔒 **底本** ＝ `verify/probes/probe_WG9276_k956_count.py` 之 `drive`（⛔ 另寫第二份判準）。
🔒 **辦法**：包裹 `ns["rw_increment"]`，錄其每次呼叫之**實參 `(W_prev, W_cur)`、回傳**，
   並以**框內省**錄其呼叫端之**解算器名**（`solve_G_binary`／`iterate_G_S`）與
   **街廓／側別／宗**（`blk_label`／`side`／`暫編地號`）及 `is_corner`／`is_chain_head`／
   `_W_near`／`_rw_start`／`W_prev`（參數）／`S_guess`。

🛑 **坑 `bb` 之攔法**：框內省一律 `sys._getframe(depth + 1)`（補輔助函式自身之一層）
   ＋ **自我驗證閘**（所錄之 `blk_label` 須為 `BLKS` 之**非空子集**；含 `None` 即 loud 拒測）。

🛑 **判別力（單 `§三-1`·<u>逐態各備</u>·承 `§二` 之通則）**
   · **必命中**對照 ＝ `rw_increment` 本身——其於**每一態**皆須 `>0`；
   · **必為零**對照 ＝ 一**人造實參**（執行期組出·字面⛔ 出艙）須⛔ 出現於所錄集合。
   · 某態之必命中對照得 `0` ⇒ **該態之計數⛔ 出艙為事實**，逐態具名。

🛑 **⛔ 判實跑側違反 `K-9-5-12`、⛔ 判孰為正確之 `W_0`、⛔ 判二解算器孰誤、⛔ 提修法主張。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9277_wchain.py [倉根]`
`rc`：`0`／`5` **量測器紅**（框內省自我驗證閘不過）。
"""
import ast
import contextlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
M_A = "甲"
M_B = "乙"
SOLVERS = ("solve_G_binary", "iterate_G_S")

# 單 `§三-1` 項 `2` 所指之受詢值（逐字自單抄錄）
TARGET = "0.1775004071"


def say(s=""):
    print(s)


def _blob(path):
    return subprocess.run(["git", "cat-file", "blob", "HEAD:" + path],
                          cwd=REPO, capture_output=True).stdout.decode("utf-8", "replace")


def drive(sb, mode):
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    rec = []
    _o_rwi = ns["rw_increment"]

    def _climb(names, upto=14):
        """自**呼叫 `_climb` 者**之上一層起往外走，逐名取其**最內層**之值。

        🔒 `depth + 1` ＝ 補 `_climb` 自身之一層（坑 `bb`）。
        """
        out = {k: None for k in names}
        chain = []
        for d in range(1, upto + 1):
            try:
                f = sys._getframe(d + 1)            # 🔒 +1 ＝ 補本函式自身之一層
            except ValueError:
                break
            chain.append(f.f_code.co_name)
            for k in names:
                if out[k] is None and k in f.f_locals:
                    out[k] = f.f_locals[k]
        out["_chain"] = chain
        return out

    def _spy_rwi(W_prev, W_cur):
        out = _o_rwi(W_prev, W_cur)
        p = _climb(["blk_label", "side", "tp", "is_corner", "is_chain_head",
                    "_W_near", "_rw_start", "W", "S_guess",
                    "_lg_idx_left", "_lg_idx_right", "W_cur", "S"])
        tp = p.get("tp") or {}
        rec.append({
            "W_prev": float(W_prev), "W_cur": float(W_cur),
            "out": float(out), "pct": float(out) * 100.0,
            "solver": (p["_chain"][0] if p.get("_chain") else None),
            "blk": p.get("blk_label"), "side": p.get("side"),
            "lot": (tp.get("暫編地號") if isinstance(tp, dict) else None),
            "is_corner": p.get("is_corner"), "is_chain_head": p.get("is_chain_head"),
            "_W_near": p.get("_W_near"), "_rw_start": p.get("_rw_start"),
            "idxL": p.get("_lg_idx_left"), "idxR": p.get("_lg_idx_right"),
        })
        return out                                  # 🛑 逐位原樣回傳

    ns["rw_increment"] = _spy_rwi

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    n0 = len(rec)
    err = None
    g_rows = []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb, eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    return {"rec": rec, "from_stepg": n0, "err": err, "fo": fo_tab, "g_rows": g_rows}


def _final_per_lot(rec, frm):
    """每 (街廓, 側, 宗) 取其**最末**一次呼叫（＝二分收斂後之定案）。"""
    seen = {}
    order = []
    for r in rec[frm:]:
        k = (r["blk"], r["side"], r["lot"])
        if k not in seen:
            order.append(k)
        seen[k] = r
    return [(k, seen[k]) for k in order]


def main():
    say("=" * W)
    say("【`W-G.9-277` `§三-1`／`§三-2`】`W` 鏈之逐宗實參 ＋ `W_prev` 之受詞 ＋ 解算器之歸屬")
    say("=" * W)
    say("🛑 **⛔ 判實跑側違反 `K-9-5-12`、⛔ 判孰為正確之 `W_0`、⛔ 判二解算器孰誤、⛔ 提修法主張。**")

    D = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in ((M_A, None), (M_B, "off")):
            D[(tag, lab)] = drive(sb, mode)
    os.environ.pop(ENV, None)

    # ── 判別力（逐態各備）────────────────────────────────────────
    say("")
    say("─" * W)
    say("【判別力·<u>逐態各備</u>】（單 `§三-1`·承 `§二` 之通則：對照之必命中性須逐態成立）")
    say("─" * W)
    say("   | 情境 | 態 | 必命中對照 `rw_increment` 之呼叫數 | 判 | 必為零對照（人造實參）之命中 | 判 |")
    say("   |---|---|---|---|---|---|")
    FAKE = -987654.321                      # 人造實參·執行期組出·字面⛔ 出艙
    untrust = []
    for k in sorted(D):
        n = len(D[k]["rec"])
        nf = sum(1 for r in D[k]["rec"]
                 if r["W_prev"] == FAKE or r["W_cur"] == FAKE)
        ok = n > 0
        if not ok:
            untrust.append(k)
        say("   | `%s` | %s | **%d** | %s | **%d** | %s |"
            % (k[0], k[1], n, "✅ `>0`" if ok else "🔴 `0`",
               nf, "✅ `0`" if nf == 0 else "🔴"))
    if untrust:
        say("   🛑 **下列態之必命中對照得 `0`** ⇒ 其計數**⛔ 出艙為事實**：%s" % untrust)
    else:
        say("   ⇒ **四態之必命中對照皆 `>0`、必為零對照皆 `0`** ⇒ **器非紅（逐態）** ✅")

    # ── 框內省之自我驗證閘 ────────────────────────────────────────
    say("")
    say("─" * W)
    say("【自我驗證閘】框內省所錄之 `blk_label`（⛔ 不過即 loud 拒測·坑 `bb`）")
    say("─" * W)
    bad = []
    for k in sorted(D):
        bl = sorted({r["blk"] for r in D[k]["rec"][D[k]["from_stepg"]:]})
        ok = bool(bl) and all(b in BLKS for b in bl)
        if not ok:
            bad.append(k)
        say("   · `%s` 態%s｜`run_step_g` 段所錄之 `blk_label` ＝ %s ⇒ %s"
            % (k[0], k[1], bl, "✅" if ok else "🔴 **含 `None` 或空**"))
    say("   · 併錄：`run_corner_pk` 段（`run_step_g` 之前）之呼叫數 ＝ %s"
        % {("%s/%s" % k): D[k]["from_stepg"] for k in sorted(D)})
    if bad:
        say("   🛑 **不過**（%s）⇒ loud 拒測，⛔ 據以下任何結論。" % bad)
        return 5
    say("   ⇒ **器非紅** ✅")

    # ── 解算器之歸屬（`§三-2` 項 2）────────────────────────────
    say("")
    say("─" * W)
    say("【`§三-2` 項 `2`】`rw_increment` 之**呼叫端解算器**（框內省·⛔ 推定）")
    say("─" * W)
    say("   | 情境 | 態 | `solve_G_binary` | `iterate_G_S` | 其他 |")
    say("   |---|---|---|---|---|")
    for k in sorted(D):
        c = {}
        for r in D[k]["rec"]:
            c[r["solver"]] = c.get(r["solver"], 0) + 1
        other = {s: n for s, n in c.items() if s not in SOLVERS}
        say("   | `%s` | %s | **%d** | **%d** | %s |"
            % (k[0], k[1], c.get("solve_G_binary", 0), c.get("iterate_G_S", 0),
               other or "（無）"))

    # ── `R4 right` 之鏈（`§三-1` 項 1）────────────────────────
    say("")
    say("─" * W)
    say("【`§三-1` 項 `1`】`R4` `right` 之該側宗序列與**逐宗 `W_i`／`Rw_i`**（**未捨入**）")
    say("─" * W)
    for k in sorted(D):
        allr4 = [(kk, r) for kk, r in _final_per_lot(D[k]["rec"], D[k]["from_stepg"])
                 if kk[0] == "R4"]
        fin = [x for x in allr4 if str(x[0][1]).find("右") >= 0]
        if fin:
            say("   · `%s` 態%s ⇒ `R4` **`right`** 之定案筆數 ＝ %d（`R4` 全側 ＝ %d）"
                % (k[0], k[1], len(fin), len(allr4)))
        else:
            # 🛑 ⛔ 靜默退路：明載其退為全 `R4`，並具名其所含之側
            say("   · `%s` 態%s ⇒ 🟡 **`R4` `right` 之定案筆數 ＝ 0**"
                "（**⛔ 靜默退路**：下列為該態 `R4` **全側** %d 筆，其側別逐列具名）"
                % (k[0], k[1], len(allr4)))
            fin = allr4
        if not fin:
            say("     🟡 該態之 `R4` **全側**亦為 `0` 筆 ⇒ 【**⛔ 可得**】（管線未達該街廓）")
            continue
        say("     | # | 宗 | side | solver | `is_corner` | `is_chain_head` | `_W_near` | "
            "`_rw_start`(＝實參 `W_prev`) | `W`(＝實參 `W_cur`) | `Rw_i`(%) |")
        say("     |---|---|---|---|---|---|---|---|---|---|")
        for i, (kk, r) in enumerate(fin, 1):
            say("     | %d | `%s` | %s | `%s` | %s | %s | %s | **%.10f** | **%.10f** | %.6f |"
                % (i, kk[2], kk[1], r["solver"], r["is_corner"], r["is_chain_head"],
                   ("%.10f" % r["_W_near"]) if isinstance(r["_W_near"], float) else r["_W_near"],
                   r["W_prev"], r["W_cur"], r["pct"]))

    # ── `0.1775004071` 之序位（`§三-1` 項 2／3）────────────────
    say("")
    say("─" * W)
    say("【`§三-1` 項 `2`／`3`】`W_prev = %s` 之**序位**（⛔ 推定·以所錄具名）" % TARGET)
    say("─" * W)
    hit = []
    for k in sorted(D):
        for kk, r in _final_per_lot(D[k]["rec"], D[k]["from_stepg"]):
            if ("%.10f" % r["W_prev"]) == TARGET:
                hit.append((k, kk, r))
    say("   · 於**定案筆**中之命中 ＝ **%d** 筆" % len(hit))
    for k, kk, r in hit:
        chainhead = bool(r["is_corner"]) or bool(r["is_chain_head"])
        idx = r["idxR"] if str(kk[1]).find("右") >= 0 else r["idxL"]
        say("     - `%s` 態%s｜街廓 `%s`｜side `%s`｜宗 `%s`" % (k[0], k[1], kk[0], kk[1], kk[2]))
        say("       `is_corner` ＝ %s／`is_chain_head` ＝ %s ⇒ **%s**"
            % (r["is_corner"], r["is_chain_head"],
               "其為**鏈頭之 `W_0`**（`_rw_start ← _W_near`）" if chainhead
               else "其為**前一宗之 `W_i`**（`_rw_start ← 外層 `W_prev``）"))
        say("       `_W_near` ＝ %r／`_rw_start` ＝ %.10f｜本側 `_lg_idx` ＝ %r"
            % (r["_W_near"], r["W_prev"], idx))
        b = kk[0]
        say("       🔒 該側之 `_fo_%s` ＝ **%s**（`§三-1` 項 `3` 所令之同格具名）"
            % ("right" if str(kk[1]).find("右") >= 0 else "left",
               D[k]["fo"][b][1] if str(kk[1]).find("右") >= 0 else D[k]["fo"][b][0]))
    if not hit:
        say("   🟡 **定案筆中⛔ 命中** ⇒ 改查**全部呼叫**：")
        for k in sorted(D):
            n = sum(1 for r in D[k]["rec"] if ("%.10f" % r["W_prev"]) == TARGET)
            say("     - `%s` 態%s ⇒ %d 筆" % (k[0], k[1], n))

    # ── `W_0` 值表（`§三-1` 項 5）──────────────────────────────
    say("")
    say("─" * W)
    say("【`§三-1` 項 `5`】**鏈頭之 `W_0`**（＝ `_rw_start` @ `is_corner ∨ is_chain_head`）"
        "·全六街廓 × 二側 × 二情境 × 二態")
    say("─" * W)
    say("   | 街廓 | 側 | `0m` 態甲 | `0m` 態乙 | `3.5m` 態甲 | `3.5m` 態乙 |")
    say("   |---|---|---|---|---|---|")
    W0 = {}
    for k in sorted(D):
        for kk, r in _final_per_lot(D[k]["rec"], D[k]["from_stepg"]):
            if bool(r["is_corner"]) or bool(r["is_chain_head"]):
                sd = "right" if str(kk[1]).find("右") >= 0 else "left"
                W0.setdefault((kk[0], sd), {})[k] = (r["W_prev"], kk[2])
    # 🔒 零之判準須**具名常數**（⛔ 字面）；三分類⛔ 二分——`==0`／`≈0`／`非 0` 之別
    #    須顯示，否則 `-2.057e-06` 之類會被一個過嚴之門檻誤歸「非 `0`」（本批自捕）。
    TOL0 = 1e-6
    ncell = nexact = nnear = 0
    for b in BLKS:
        for sd in ("left", "right"):
            cells = []
            for tag in ("0m", "3.5m"):
                for lab in (M_A, M_B):
                    v = W0.get((b, sd), {}).get((tag, lab))
                    if v is None:
                        cells.append("—")
                    else:
                        ncell += 1
                        nexact += (v[0] == 0.0)
                        nnear += (v[0] != 0.0 and abs(v[0]) <= TOL0)
                        cells.append("`%.10f`（`%s`）" % (v[0], v[1]))
            say("   | `%s` | %s | %s | %s | %s | %s |"
                % (b, sd, cells[0], cells[1], cells[2], cells[3]))
    nfar = ncell - nexact - nnear
    say("   ⇒ 有值之格 ＝ **%d**｜**嚴格 `== 0`** ＝ **%d**｜**`≈ 0`**（`0 < |W_0| ≤ %g`）＝ **%d**"
        "｜**`|W_0| > %g`** ＝ **%d**" % (ncell, nexact, TOL0, nnear, TOL0, nfar))
    say("   🔒 **零之判準 ＝ 具名常數 `TOL0 = %g`**（⛔ 字面·⛔ 二分）。" % TOL0)
    say("   🔒 **判別力**：若全格落於同一類，該欄⛔ 具鑑別力；實測 `≈0`／`>TOL0` ＝ "
        "**%d**／**%d** ⇒ %s" % (nnear + nexact, nfar,
                                 "**二類並存·具鑑別力** ✅" if ((nnear + nexact) and nfar)
                                 else "🟡 **單一類·須具名**"))

    # ── `_fo` 表（供項 3 同格具名）────────────────────────────
    say("")
    say("   · `_fo_left`／`_fo_right`（同格具名·源 ＝ `f3L_forced_offset`）：")
    for b in BLKS:
        say("     - `%s`：%s" % (b, "　".join(
            "`%s`態%s L=%s R=%s" % (t, l, D[(t, l)]["fo"][b][0], D[(t, l)]["fo"][b][1])
            for t in ("0m", "3.5m") for l in (M_A, M_B))))

    # ── `§三-2` 項 1：二解算器之呼叫式逐字（自碼面現查）────────
    say("")
    say("─" * W)
    say("【`§三-2` 項 `1`】二解算器內 `rw_increment(...)` 之**呼叫式逐字**（自碼面現查·⛔ 採轉述）")
    say("─" * W)
    src = _blob("app.py")
    lines = src.split("\n")
    t = ast.parse(src)
    fns = {n.name: (n.lineno, n.end_lineno) for n in ast.walk(t)
           if isinstance(n, ast.FunctionDef) and n.name in SOLVERS}
    # 🔒 以 **AST 之語法真值**取（⛔ 文字層啟發式·`自誤 377`）——文字層會咬中 docstring
    #    與註解內之同形字樣（本批自捕：`app.py:6428` 係 docstring 之一列）。
    nodes = {n.name: n for n in ast.walk(t)
             if isinstance(n, ast.FunctionDef) and n.name in SOLVERS}
    for name in SOLVERS:
        lo, hi = fns[name]
        say("   · `%s`（`app.py:%d`–`:%d`）·**AST `Call` 節點**：" % (name, lo, hi))
        cnt = 0
        for c in ast.walk(nodes[name]):
            if isinstance(c, ast.Call) and getattr(c.func, "id", None) == "rw_increment":
                cnt += 1
                args = ", ".join(ast.unparse(a) for a in c.args)
                say("     - `app.py:%d`　`rw_increment(%s)`　｜該列逐字 ＝ `%s`"
                    % (c.lineno, args, lines[c.lineno - 1].strip()))
        say("     ⇒ 該解算器內之 `rw_increment` **呼叫節點數 ＝ %d**" % cnt)
        # 文字層之對照（證二法之別·⛔ 以文字層為判準）
        txt_n = sum(1 for i in range(lo - 1, hi)
                    if "rw_increment(" in lines[i] and not lines[i].strip().startswith("#"))
        say("     ℹ️ **文字層**（`'rw_increment(' in line` 且非 `#` 起首）之列數 ＝ **%d**%s"
            % (txt_n, "　🟡 **與 AST 相異**（其咬中 docstring／註解）" if txt_n != cnt else ""))
    nos = "rw_increment" + chr(95) + "NOSUCH"
    say("   🔒 **判別力**：一人造字面（**執行期組出**）於 `app.py` ＝ **%d**（須 `0`）；"
        "對照組 `rw_increment(` ＝ **%d** 列（須 `>0`）"
        % (sum(1 for ln in lines if nos in ln),
           sum(1 for ln in lines if "rw_increment(" in ln)))

    # ── 終止態 ───────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【終止態】`run_step_g` 之中止（逐情境 × 逐態）")
    say("─" * W)
    for k in sorted(D):
        say("   · `%s` 態%s ⇒ %s" % (k[0], k[1], D[k]["err"]))
    say("")
    say("RESULT=OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
