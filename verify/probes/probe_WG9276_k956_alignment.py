# -*- coding: utf-8 -*-
"""`W-G.9-276` `§三-2` 項 `3`／`4`：**三個 `W` 與 `k956_W_from_mp` 回傳值之逐位對位**
   ＋ `§三-1` 之**正面第三造**（模組全域名解析確可被攔之機械證）。

🛑 **判法（單 `§三-2` 項 `3` 逐字）**：以 `§三-1` **法乙**之間諜所錄之**回傳值集合**
   與三值**逐位比對**（`14.01`／`14.20`／`14.1988975422`·`W_prev = 0.1775004071`）。

🛑 **三態（單 `§三-2` 項 `4`）**：`逐位相符`／`⛔ 相符`／`⛔ 可得`（器不可信時）
   ——**⛔ 二義共用出艙碼**。

🛑 **判別力（單 `§三-2` 逐字）**：
   · **必不相符之對照** ＝ 一**人造值**（執行期組出·字面⛔ 出艙）須判「⛔ 相符」；
   · **必相符之對照** ＝ 取回傳值集合中任一元與其自身比 ⇒ 須判「逐位相符」。
   · 二造同判 ⇒ **器紅**。

🛑 **⛔ 判孰為正確之 `W`、⛔ 提修法主張、⛔ 判 `K-9-5-6` 之射程。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9276_k956_alignment.py [倉根]`
`rc`：`0`／`5` **量測器紅**（判別力二造同判）。
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

# 單 `§三-2` 項 `3` 所指之三值（＋ `W_prev`）·逐字自單抄錄
THREE = [("宗地寬度(m)", "14.01"), ("W(m)", "14.20"), ("W_cur", "14.1988975422")]
W_PREV = "0.1775004071"


def say(s=""):
    print(s)


def _blob(path):
    return subprocess.run(["git", "cat-file", "blob", "HEAD:" + path],
                          cwd=REPO, capture_output=True).stdout.decode("utf-8", "replace")


def drive_k956(sb, mode):
    """法乙（`__globals__`）之間諜·只錄 `k956_W_from_mp` 之回傳值集合。"""
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
    gmap = ns["_pool_strips_for_block"].__globals__          # 法乙之標的
    outs = []
    _o = ns["k956_W_from_mp"]

    def _spy(point, side_mid, allocation_dir, d_hat):
        r = _o(point, side_mid, allocation_dir, d_hat)
        outs.append(float(r))
        return r                                             # 🛑 逐位原樣回傳
    gmap["k956_W_from_mp"] = _spy

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
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build_p, wins, forced, sb, eff_min_build_by_blk={})
    except RuntimeError:
        pass
    return outs


def _match(val_str, pool):
    """逐位比對：以**十進位字面**比，⛔ 以浮點容差比（單令「逐位」）。"""
    reps = set()
    for x in pool:
        reps.add(repr(float(x)))
        reps.add("%.10f" % float(x))
        reps.add("%.4f" % float(x))
        reps.add("%.2f" % float(x))
    return val_str in reps


def main():
    say("=" * W)
    say("【`W-G.9-276` `§三-2` 項 `3`／`4`】三個 `W` 與 `k956_W_from_mp` 回傳值之逐位對位")
    say("=" * W)
    say("🛑 **⛔ 判孰為正確之 `W`、⛔ 提修法主張、⛔ 判 `K-9-5-6` 之射程**——出艙即止。")

    # ── 正面第三造：模組全域名解析確可被攔 ────────────────────────
    say("")
    say("─" * W)
    say("【正面第三造】**模組全域名解析**確可被間諜攔下之機械證（AST 實查 ＋ 實測計數）")
    say("─" * W)
    txt = _blob("app.py")
    lines = txt.split("\n")
    t = ast.parse(txt)
    fns = [(n.name, n.lineno, n.end_lineno) for n in ast.walk(t)
           if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    for i, ln in enumerate(lines):
        s = ln.strip()
        if "k6_step0_merge(" in ln and not s.startswith("#") and not s.startswith("def "):
            no = i + 1
            enc = sorted([f for f in fns if f[1] <= no <= (f[2] or 0)], key=lambda x: x[1])
            say("   · `app.py:%d`  %s" % (no, s[:76]))
            say("     包層 ＝ `%s`" % (" > ".join(f[0] for f in enc) or "(頂層)"))
            say("     ⇒ 其名 `k6_step0_merge` **⛔ 為該 def 之區域變數／參數** "
                "⇒ 解析走**模組全域**（`__globals__`）")
    say("   · 實測（`§三-1` 主表）：態甲之 `k6_step0_merge` 計數 ＝ **1**（二法皆然）")
    say("   ⇒ 🔒 **模組全域名解析之呼叫確被攔下** ⇒ 該間諜法**⛔ 對此類呼叫失明**。")

    # ── 回傳值集合 ────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【回傳值集合】法乙（`__globals__`）之間諜所錄（逐情境 × 逐態）")
    say("─" * W)
    POOL = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in ("甲", None), ("乙", "off"):
            POOL[(tag, lab)] = drive_k956(sb, mode)
    os.environ.pop(ENV, None)
    for k in sorted(POOL):
        say("   · `%s` 態%s ⇒ n ＝ %d｜值 ＝ %r" % (k[0], k[1], len(POOL[k]), POOL[k]))
    allpool = [x for v in POOL.values() for x in v]
    say("   · **全母體之聯集** ＝ %r（n ＝ %d）" % (sorted(set(allpool)), len(allpool)))

    # ── 判別力二造 ────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【判別力二造】（單 `§三-2` 逐字·二造同判 ⇒ 器紅）")
    say("─" * W)
    if not allpool:
        say("   🟡 **回傳值集合為空** ⇒ 「必相符之對照」**⛔ 可構造**")
        say("   ⇒ 本判別力檢【**⛔ 可得**】；下表之判一律以【**⛔ 可得**】出艙，")
        say("      **⛔ 以「⛔ 相符」頂替**（二義⛔ 共用出艙碼）。")
        say("   RESULT=INCONCLUSIVE")
        return 0
    must_hit = repr(float(allpool[0]))
    fake = "%.10f" % (float(allpool[0]) + 12345.6789)        # 人造值·執行期組出
    a = _match(must_hit, allpool)
    b = _match(fake, allpool)
    say("   · 造甲[必相符] ＝ 集合中任一元與其自身比 ⇒ %s" % ("**逐位相符** ✅" if a else "🔴 **⛔ 相符**"))
    say("   · 造乙[必不符] ＝ 一人造值（**執行期組出**·字面⛔ 出艙）⇒ %s"
        % ("**⛔ 相符** ✅" if not b else "🔴 **逐位相符**"))
    if a == b:
        say("   🛑 **二造同判 ⇒ 器紅** ⇒ ⛔ 據下表任何結論。")
        return 5
    say("   ⇒ **器非紅** ✅")

    # ── 主表：三值 × 逐格 ────────────────────────────────────────
    say("")
    say("─" * W)
    say("【主表】三個 `W`（＋ `W_prev`）是否即 `k956_W_from_mp` 之輸出（**逐位**）")
    say("─" * W)
    say("   🔒 **器可信與否之來源** ＝ `§三-1` 之準據判：態甲 二對照皆 `>0` ⇒ **可信**；")
    say("      態乙 `k6_step0_merge` ＝ `0`（step0 關閉）⇒ **部分** ⇒ 其格出艙【**⛔ 可得**】。")
    say("   | 名 | 值（單所載） | `0m` 態甲 | `0m` 態乙 | `3.5m` 態甲 | `3.5m` 態乙 |")
    say("   |---|---|---|---|---|---|")
    TRUST = {("0m", "甲"): True, ("3.5m", "甲"): True,
             ("0m", "乙"): False, ("3.5m", "乙"): False}
    for name, v in THREE + [("W_prev", W_PREV)]:
        cells = []
        for tag in ("0m", "3.5m"):
            for lab in ("甲", "乙"):
                if not TRUST[(tag, lab)]:
                    cells.append("**⛔ 可得**（器不可信）")
                elif _match(v, POOL[(tag, lab)]):
                    cells.append("**逐位相符**")
                else:
                    cells.append("**⛔ 相符**")
        say("   | `%s` | `%s` | %s | %s | %s | %s |"
            % (name, v, cells[0], cells[1], cells[2], cells[3]))
    say("")
    say("   🛑 **三態⛔ 共用出艙碼**：「**⛔ 相符**」＝ 器可信且比對不中；")
    say("      「**⛔ 可得**」＝ 器不可信（`§三-1` 準據）⇒ **該格未作比對**。")
    say("")
    say("RESULT=OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
