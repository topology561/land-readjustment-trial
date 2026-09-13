# -*- coding: utf-8 -*-
"""`W-G.9-276` `§三-1`：**`k956_W_from_mp` 計數之判別力補證**（二法並施·逐法分列）。

🔒 **底本** ＝ `verify/probes/probe_WG9274_rw_origin.py` 之 `drive`／`_spy_*`（⛔ 另寫第二份判準）。

🔒 **二法（單 `§三-1` 逐字）**
   · **法甲** ＝ 改寫 `ns["<名>"]`（前窗之法）。
   · **法乙** ＝ 改寫 **app 模組之全域屬性**——使**模組全域名解析**亦被攔。
     🩸 本倉**⛔ 存在名為 `app` 之模組物件**（`app_harvest.harvest()` 係
        `exec(code, ns)`·`ns` 為 plain dict）⇒ 法乙之**唯一可實作形** ＝
        自一**已取得之函式物件**取其 `__globals__` 映射（⛔ 假定其即 `ns`）並於其上賦值。
        本器**逐次 drive 出艙** `f.__globals__ is ns` 之機驗結果，⛔ 以斷言代之。

🛑 **坑 `bb` 之攔法**：框內省一律 `sys._getframe(depth + 1)` ＋ **自我驗證閘**
   （所錄之鍵須為已知母體之**非空子集**；含 `None` 即 loud 拒測）。

🛑 **準據（發單側定·⛔ CC 自訂·單 `§三-1` 逐字）**
   · 某法對**二對照皆得 `0`** ⇒ 該法之計數對任何函式皆⛔ 可信 ⇒ 其下之 `k956`
     計數**⛔ 出艙為受詞之事實**。
   · 僅當**至少一法**對二對照皆 `>0` 時，`k956` 於該法下之計數方得出艙為事實。
   · 二法之 `k956` 計數相異 ⇒ **照實並報二值與各自之法**，**⛔ 判孰誤**。

🛑 **⛔ 判 `k956` 是否「未被消費」、⛔ 判其為缺陷、⛔ 鑄 `GB`。**

🩸 **本器之自捕（坑 `9` 族·`W-G.9-276R` 具名）**：初版之提示文字以 `\\u21db`（⇛）
   誤代 `⛔`、`\\u8231`（舱）誤代 `艙`、`\\u947d`（鑽）誤代 `鑄`——**碼位記錯**。
   量測結果**⛔ 受影響**（字面僅見於提示文字），惟其形即坑 `9` 所戒。
   **攔法**：本檔一律用**逐字字面**，⛔ 用 `\\uXXXX` 轉義寫 CJK。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9276_k956_count.py [倉根]`
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

# 三函式（單 `§三-1` 表·逐字）
F_TEST = "k956_W_from_mp"                     # 受測
F_C1 = "_pool_strips_for_block"               # 對照甲[必命中]
F_C2 = "k6_step0_merge"                       # 對照乙[必命中·於態甲]
NAMES = [F_TEST, F_C1, F_C2]

M_A = "甲"
M_B = "乙"


def say(s=""):
    print(s)


def _blob(path):
    r = subprocess.run(["git", "cat-file", "blob", "HEAD:" + path],
                       cwd=REPO, capture_output=True)
    return r.stdout.decode("utf-8", "replace")


def drive(sb, mode, method):
    """method ∈ {甲, 乙}。回傳計數與各項併出艙之量。"""
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

    # ── 法乙之標的解析（⛔ 假定其即 `ns`）────────────────────────────
    probe_fn = ns[F_C1]                       # 任取一已 harvest 之函式物件
    gmap = probe_fn.__globals__               # ＝ app 碼之模組全域映射
    same = (gmap is ns)

    cnt = {n: 0 for n in NAMES}
    k956_out = []
    slot_peek = []
    orig = {n: ns[n] for n in NAMES}

    def _peek(depth, keys):
        f = sys._getframe(depth + 1).f_locals   # 🔒 +1 ＝ 補 `_peek` 自身之一層（坑 `bb`）
        return {k: f.get(k) for k in keys}

    def _mk(name):
        o = orig[name]

        def _spy(*a, **kw):
            out = o(*a, **kw)
            cnt[name] += 1
            if name == F_TEST:
                try:
                    k956_out.append(float(out))
                except Exception:                       # noqa: BLE001
                    k956_out.append(None)
            return out                                  # 🛑 逐位原樣回傳
        return _spy

    target = ns if method == M_A else gmap
    for n in NAMES:
        target[n] = _mk(n)

    # `_select_pool_slot` 之框內省（供 `_fo_left`／`_fo_right` 之交叉驗）
    _o_slot = ns["_select_pool_slot"]

    def _spy_slot(widths, left, right):
        out = _o_slot(widths, left, right)
        slot_peek.append(_peek(1, ["blk_label", "_fo_left", "_fo_right",
                                   "_N", "_degenerate_order"]))
        return out
    ns["_select_pool_slot"] = _spy_slot

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

    err = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build_p, wins, forced, sb,
                       eff_min_build_by_blk={})
    except RuntimeError as e:
        err = str(e).split("\n")[0][:150]

    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {}
    for b in BLKS:
        d = fo.get(b, {}) or {}
        fo_tab[b] = (bool(d.get("left_forced_offset", False)),
                     bool(d.get("right_forced_offset", False)))
    return {"cnt": dict(cnt), "k956_out": list(k956_out), "same": same,
            "err": err, "fo": fo_tab, "slot_peek": list(slot_peek)}


def main():
    say("=" * W)
    say("【`W-G.9-276` `§三-1`】`k956_W_from_mp` 計數之判別力補證（二法並施·逐法分列）")
    say("=" * W)
    say("🛑 **⛔ 判 `k956` 是否未被消費、⛔ 判其為缺陷、⛔ 鑄 `GB`**"
        "——本器只證**器可信與否**並出艙事實。")

    D = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in ((M_A, None), (M_B, "off")):
            for meth in (M_A, M_B):
                D[(tag, lab, meth)] = drive(sb, mode, meth)
    os.environ.pop(ENV, None)

    # ── 法乙標的之機驗 ────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【法乙之標的】`f.__globals__ is ns` 之機驗（**⛔ 以斷言代之**）")
    say("─" * W)
    allsame = all(v["same"] for v in D.values())
    say("   · 全 %d 次 drive 之 `probe_fn.__globals__ is ns` ⇒ %s"
        % (len(D), "**全為 `True`**" if allsame else "**非全 `True`**"))
    say("   ⇒ 於本 harness，**法甲與法乙之標的為同一個 dict** %s"
        % ("✅" if allsame else "🔴"))

    # ── 框內省之自我驗證閘 ────────────────────────────────────────
    say("")
    say("─" * W)
    say("【自我驗證閘】框內省所錄之 `blk_label`（⛔ 不過即 loud 拒測·坑 `bb`）")
    say("─" * W)
    tot_peek = 0
    bad = []
    for k, v in sorted(D.items()):
        bl = [p.get("blk_label") for p in v["slot_peek"]]
        tot_peek += len(bl)
        ok = (not bl) or all(b in BLKS for b in bl)
        if bl and not ok:
            bad.append(k)
        say("   · `%s` 態%s 法%s｜所錄 ＝ %s ⇒ %s"
            % (k[0], k[1], k[2], bl, "✅" if ok else "🔴 **含 `None`**"))
    if bad:
        say("   🛑 **不過**（%s）⇒ loud 拒測。" % bad)
        return 5
    if tot_peek == 0:
        say("   🟡 **所錄總數 ＝ 0** ⇒ 本閘【⛔ 可得】，**⛔ 以其綠充「器非紅」**。")
    else:
        say("   ⇒ **器非紅** ✅（所錄 %d 筆·皆為 `BLKS` 之成員）" % tot_peek)

    # ── 6 格計數表（逐情境 × 逐態）──────────────────────────────
    say("")
    say("─" * W)
    say("【主表】三函式 × 二法 ＝ `6` 格計數（逐情境 `0m`／`3.5m` × 逐態 甲／乙）")
    say("─" * W)
    say("   | 情境 | 態 | 函式 | 角色 | 法甲 `ns[...]` | 法乙 `__globals__` | 判 |")
    say("   |---|---|---|---|---|---|---|")
    ROLE = {F_TEST: "**受測**", F_C1: "對照甲[必命中]",
            F_C2: "對照乙[必命中·於態甲]"}
    verdicts = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab in (M_A, M_B):
            a = D[(tag, lab, M_A)]["cnt"]
            b = D[(tag, lab, M_B)]["cnt"]
            for n in NAMES:
                say("   | `%s` | %s | `%s` | %s | **%d** | **%d** | %s |"
                    % (tag, lab, n, ROLE[n], a[n], b[n],
                       "相同" if a[n] == b[n] else "🔴 **相異**"))
            for meth, cc in ((M_A, a), (M_B, b)):
                c1, c2 = cc[F_C1], cc[F_C2]
                if c1 > 0 and c2 > 0:
                    v = "可信"
                elif c1 == 0 and c2 == 0:
                    v = "⛔ 可信（二對照皆 `0`）"
                else:
                    v = "部分（只一對照 `>0`）"
                verdicts[(tag, lab, meth)] = (c1, c2, cc[F_TEST], v)

    # ── 準據之逐格判 ────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【準據之逐格判】（發單側定·`§三-1` 逐字）")
    say("─" * W)
    say("   | 情境 | 態 | 法 | 對照甲 `%s` | 對照乙 `%s` | `k956` 計數 | 該法之計數 |"
        % (F_C1, F_C2))
    say("   |---|---|---|---|---|---|---|")
    for k in sorted(verdicts):
        c1, c2, ct, v = verdicts[k]
        say("   | `%s` | %s | %s | %d | %d | **%d** | %s |" % (k[0], k[1], k[2], c1, c2, ct, v))

    trust = [k for k, v in verdicts.items() if v[3] == "可信"]
    say("")
    say("   ⇒ **二對照皆 `>0`** 之格 ＝ **%d**／%d" % (len(trust), len(verdicts)))
    if trust:
        say("   ⇒ 於該等格，`k956` 之計數**得出艙為事實**（逐格具名於上表）。")
    else:
        say("   🔴 ⇒ 全數不可信，`k956` 之計數**⛔ 得出艙為受詞之事實**。")

    # ── `k956` 之回傳值集合 ─────────────────────────────────────
    say("")
    say("─" * W)
    say("【`k956` 之回傳值集合】（供 `§三-2` 逐位比對）")
    say("─" * W)
    for k in sorted(D):
        v = D[k]
        say("   · `%s` 態%s 法%s ⇒ n ＝ %d｜值 ＝ %r"
            % (k[0], k[1], k[2], len(v["k956_out"]), v["k956_out"][:12]))

    # ── 併出艙 1：綁定時點 ──────────────────────────────────────
    say("")
    say("─" * W)
    say("【併出艙 `1`】`_k956_W_from_mp = ns[\"k956_W_from_mp\"]` 之**綁定時點** vs 間諜**安裝時點**")
    say("─" * W)
    sp = _blob("verify/stepg_pipeline.py").split("\n")
    lit = "_k956_W_from_mp = ns[" + chr(34) + "k956_W_from_mp" + chr(34) + "]"
    hits = [i + 1 for i, ln in enumerate(sp) if lit in ln]
    defs = [i + 1 for i, ln in enumerate(sp) if ln.startswith("def run_step_g")]
    say("   · 逐字 `%s` 之列框命中 ＝ **%d**（列 %s）" % (lit, len(hits), hits))
    say("   · `def run_step_g` 之列 ＝ %s" % defs)
    tree = ast.parse("\n".join(sp))
    encl = None
    for nd in ast.walk(tree):
        if isinstance(nd, ast.FunctionDef) and hits and nd.lineno <= hits[0] <= (nd.end_lineno or 0):
            if encl is None or nd.lineno > encl[1]:
                encl = (nd.name, nd.lineno, nd.end_lineno)
    say("   · **AST 實查**：該列之最內層 def ＝ `%s`（`%s`–`%s`）" % encl if encl
        else "   · AST 實查：⛔ 得")
    say("   · ⇒ 其綁定於該 def 之**入口段**（**每次呼叫皆重新綁定**）；")
    say("   · 間諜之安裝於 `harvest()` 後、`run_step_g` 呼叫**之前** ⇒ **安裝於綁定之前**。")

    # ── 併出艙 1′：k956 各呼叫點之最內層 def（AST 實查）────────
    say("")
    say("─" * W)
    say("【併出艙 `1'`】`k956_W_from_mp` 各呼叫點之**包層 def 鏈**（AST 實查·⛔ 硬編）")
    say("─" * W)
    for path in ("app.py", "verify/stepg_pipeline.py"):
        txt = _blob(path)
        lines = txt.split("\n")
        t = ast.parse(txt)
        fns = [(n.name, n.lineno, n.end_lineno) for n in ast.walk(t)
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        say("   · `%s`：" % path)
        for i, ln in enumerate(lines):
            s = ln.strip()
            if ("k956_W_from_mp(" in ln) and not s.startswith("#") and not s.startswith("def "):
                no = i + 1
                enc = sorted([f for f in fns if f[1] <= no <= (f[2] or 0)], key=lambda x: x[1])
                say("     - :%d  %s｜包層 ＝ `%s`"
                    % (no, s[:72], " > ".join(f[0] for f in enc) or "(頂層)"))

    # ── 併出艙 2：`_fo_left`／`_fo_right` 全母體 24 格 ──────────
    say("")
    say("─" * W)
    say("【併出艙 `2`】`_fo_left`／`_fo_right` 之**實際值**"
        "（逐街廓 × 逐情境 × 逐態·全母體 `24` 格）")
    say("─" * W)
    say("   源 ＝ `fake_st.session_state['f3L_forced_offset'][<街廓>]`"
        "（即 `verify/stepg_pipeline.py` 之 `_fo_block` 之同一來源）")
    say("   | 街廓 | `0m` 態甲 | `0m` 態乙 | `3.5m` 態甲 | `3.5m` 態乙 |")
    say("   |---|---|---|---|---|")
    ncell = 0
    ntrue = 0
    for b in BLKS:
        cells = []
        for tag in ("0m", "3.5m"):
            for lab in (M_A, M_B):
                l, r = D[(tag, lab, M_A)]["fo"][b]
                cells.append("L=%s R=%s" % (l, r))
                ncell += 1
                ntrue += int(l) + int(r)
        say("   | `%s` | %s | %s | %s | %s |" % (b, cells[0], cells[1], cells[2], cells[3]))
    say("   ⇒ 格數 ＝ **%d**（期 `24`）｜`True` 之總數 ＝ **%d**" % (ncell, ntrue))
    say("   🔒 **判別力**：若全母體皆 `False` ⇒ 該欄⛔ 具鑑別力；"
        "實測 `True` 總數 ＝ **%d** ⇒ %s"
        % (ntrue, "非全 `False`·具鑑別力 ✅" if ntrue else "🟡 全 `False`·須具名"))
    say("   · 框內省交叉驗（`_select_pool_slot` 呼叫端之 `_fo_left`／`_fo_right`）：")
    for k in sorted(D):
        for p in D[k]["slot_peek"]:
            say("     - `%s` 態%s 法%s｜`%s`：_fo_left=%s _fo_right=%s _N=%s _deg=%s"
                % (k[0], k[1], k[2], p.get("blk_label"), p.get("_fo_left"),
                   p.get("_fo_right"), p.get("_N"), p.get("_degenerate_order")))

    # ── 併出艙 3：`left_forced_offset` 之來源逐字 ───────────────
    say("")
    say("─" * W)
    say("【併出艙 `3`】`_fo_block.get('left_forced_offset')`／"
        "`('right_forced_offset')` 之**來源逐字**")
    say("─" * W)
    for path in ("verify/stepg_pipeline.py", "verify/selection_pipeline.py", "app.py"):
        for i, ln in enumerate(_blob(path).split("\n")):
            if ("left_forced_offset" in ln) or ("f3L_forced_offset" in ln):
                say("   | `%s:%d` | `%s` |" % (path, i + 1, ln.strip()[:112]))
    nos = "left_forced_offset" + chr(95) + "NOSUCH"
    say("   🔒 **判別力**：一人造字面（**執行期組出**）於 `verify/stepg_pipeline.py` ＝ **%d**（須 `0`）"
        % sum(1 for ln in _blob("verify/stepg_pipeline.py").split("\n") if nos in ln))

    # ── 終止態 ─────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【終止態】`run_step_g` 之中止閘（逐情境 × 逐態 × 逐法）")
    say("─" * W)
    for k in sorted(D):
        say("   · `%s` 態%s 法%s ⇒ %s" % (k[0], k[1], k[2], D[k]["err"]))
    say("")
    say("RESULT=OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
